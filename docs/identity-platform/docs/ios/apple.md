---
url: https://docs.cloud.google.com/identity-platform/docs/ios/apple/
title: Signing in users with Apple on iOS \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:57.173531+00:00
---

# Signing in users with Apple on iOS  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/ios/apple/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Signing in users with Apple on iOS

This document shows you how to use Identity Platform to add _Sign in with Apple_ to your iOS app.

## Before you begin

  * Enable Identity Platform and have a basic iOS app. To learn about how to enable Identity Platform and sign in, see [Quickstart](https://docs.cloud.google.com/identity-platform/docs/sign-in-user-email).

  * Join the [Apple Developer Program](https://developer.apple.com/programs).




## Configuring your app with Apple

On the Apple Developer site:

  1. [Enable the Sign In with Apple capability](https://developer.apple.com/help/account/manage-identifiers/enable-app-capabilities) for your app.

  2. If you use Identity Platform to send emails to your users, [configure your project with Apple's private email relay service](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service) using the following email:
         
         noreply@project-id.firebaseapp.com
         

You can also use a custom email template, if your app has one.




## Complying with Apple's anonymized data requirements

Apple gives users the option of anonymizing their data, including their email address. Apple assigns users who select this option an obfuscated email address with the domain `privaterelay.appleid.com`.

Your app must comply with any applicable developer policies or terms from Apple regarding anonymized Apple IDs. This includes obtaining user consent before associating any personally identifying information (PII) with an anonymized Apple ID. Actions that involve PII include, but are not limited to:

  * Linking an email address to an anonymized Apple ID, or vice versa.
  * Linking a phone number to an anonymized Apple ID, or vice versa
  * Linking a non-anonymous social credential, such as Facebook or Google, to to anonymized Apple ID, or vice versa.



For more information, refer to the _Apple Developer Program License Agreement_ for your Apple developer account.

## Configuring Apple as a provider

To configure Apple as an identity provider:

  1. Go to the **Identity Providers** page in the Google Cloud console.

[Go to the Identity Providers page](https://console.cloud.google.com/customer-identity/providers)

  2. Click **Add A Provider**.

  3. Select **Apple** from the list.

  4. Under **Platform** , select **iOS**.

  5. Enter your app's **Bundle ID**.

  6. Register your app's domains by clicking **Add domain** under **Authorized Domains**. For development purposes, `localhost` is already enabled by default.

**Important:** In projects created after April 28, 2025, Identity Platform no longer includes `localhost` as an authorized domain by default. Google strongly discourages the use of `localhost` in production projects. If you choose to authorize `localhost`, you can manually add it in the **Settings** page, in **Authorized Domains** , by clicking **Add Domain**.
  7. Under **Configure your application** , click **iOS**. Copy the snippet into your app's code to initialize the Identity Platform client SDK.

  8. Click **Save**.




## Signing in users with the client SDK

  1. Sign in the user and obtain an ID token using Apple's [Authentication Services framework](https://developer.apple.com/documentation/authenticationservices).

  2. Generate a random string, known as a _nonce_ , by calling [`SecRandomCopyBytes(_:_:_:)`](https://developer.apple.com/documentation/security/1399291-secrandomcopybytes).

The nonce is used to prevent replay attacks. You include the SHA-256 hash of your nonce in your authentication request, and Apple returns it, unmodified, in the response. Identity Platform then validates the response by comparing the original hash to the value returned by Apple.

  3. Start Apple's sign-in flow, including the SHA-256 hash of the nonce you created in the previous step, and a delegate class to handle Apple's response:

###  Swift 
         
         import CryptoKit
         
         // Unhashed nonce.
         fileprivate var currentNonce: String?
         
         @available(iOS 13, *)
         func startSignInWithAppleFlow() {
           let nonce = randomNonceString()
           currentNonce = nonce
           let appleIDProvider = ASAuthorizationAppleIDProvider()
           let request = appleIDProvider.createRequest()
           request.requestedScopes = [.fullName, .email]
           request.nonce = sha256(nonce)
         
           let authorizationController = ASAuthorizationController(authorizationRequests: [request])
           authorizationController.delegate = self
           authorizationController.presentationContextProvider = self
           authorizationController.performRequests()
         }
         
         @available(iOS 13, *)
         private func sha256(_ input: String) -> String {
           let inputData = Data(input.utf8)
           let hashedData = SHA256.hash(data: inputData)
           let hashString = hashedData.compactMap {
             return String(format: "%02x", $0)
           }.joined()
         
           return hashString
         }
         

###  Objective-C 
         
         @import CommonCrypto;
         
         - (void)startSignInWithAppleFlow {
           NSString *nonce = [self randomNonce:32];
           self.currentNonce = nonce;
           ASAuthorizationAppleIDProvider *appleIDProvider = [[ASAuthorizationAppleIDProvider alloc] init];
           ASAuthorizationAppleIDRequest *request = [appleIDProvider createRequest];
           request.requestedScopes = @[ASAuthorizationScopeFullName, ASAuthorizationScopeEmail];
           request.nonce = [self stringBySha256HashingString:nonce];
         
           ASAuthorizationController *authorizationController =
               [[ASAuthorizationController alloc] initWithAuthorizationRequests:@[request]];
           authorizationController.delegate = self;
           authorizationController.presentationContextProvider = self;
           [authorizationController performRequests];
         }
         
         - (NSString *)stringBySha256HashingString:(NSString *)input {
           const char *string = [input UTF8String];
           unsigned char result[CC_SHA256_DIGEST_LENGTH];
           CC_SHA256(string, (CC_LONG)strlen(string), result);
         
           NSMutableString *hashed = [NSMutableString stringWithCapacity:CC_SHA256_DIGEST_LENGTH * 2];
           for (NSInteger i = 0; i < CC_SHA256_DIGEST_LENGTH; i++) {
             [hashed appendFormat:@"%02x", result[i]];
           }
           return hashed;
         }
         

  4. Handle Apple's response in your implementation of `ASAuthorizationControllerDelegate`. If sign-in succeeds, use the ID token from Apple's response with the unhashed nonce to authenticate with Identity Platform:

###  Swift 
         
         @available(iOS 13.0, *)
         extension MainViewController: ASAuthorizationControllerDelegate {
         
           func authorizationController(controller: ASAuthorizationController, didCompleteWithAuthorization authorization: ASAuthorization) {
             if let appleIDCredential = authorization.credential as? ASAuthorizationAppleIDCredential {
               guard let nonce = currentNonce else {
                 fatalError("Invalid state: A login callback was received, but no login request was sent.")
               }
               guard let appleIDToken = appleIDCredential.identityToken else {
                 print("Unable to fetch identity token")
                 return
               }
               guard let idTokenString = String(data: appleIDToken, encoding: .utf8) else {
                 print("Unable to serialize token string from data: \(appleIDToken.debugDescription)")
                 return
               }
               // Initialize a Firebase credential.
               let credential = OAuthProvider.credential(withProviderID: "apple.com",
                                                         IDToken: idTokenString,
                                                         rawNonce: nonce)
               // Sign in with Firebase.
               Auth.auth().signIn(with: credential) { (authResult, error) in
                 if error {
                   // Error. If error.code == .MissingOrInvalidNonce, make sure
                   // you're sending the SHA256-hashed nonce as a hex string with
                   // your request to Apple.
                   print(error.localizedDescription)
                   return
                 }
                 // User is signed in to Firebase with Apple.
                 // ...
               }
             }
           }
         
           func authorizationController(controller: ASAuthorizationController, didCompleteWithError error: Error) {
             // Handle error.
             print("Sign in with Apple errored: \(error)")
           }
         }
         

###  Objective-C 
         
         - (void)authorizationController:(ASAuthorizationController *)controller
           didCompleteWithAuthorization:(ASAuthorization *)authorization API_AVAILABLE(ios(13.0)) {
           if ([authorization.credential isKindOfClass:[ASAuthorizationAppleIDCredential class]]) {
             ASAuthorizationAppleIDCredential *appleIDCredential = authorization.credential;
             NSString *rawNonce = self.currentNonce;
             NSAssert(rawNonce != nil, @"Invalid state: A login callback was received, but no login request was sent.");
         
             if (appleIDCredential.identityToken == nil) {
               NSLog(@"Unable to fetch identity token.");
               return;
             }
             NSString *idToken = [[NSString alloc] initWithData:appleIDCredential.identityToken
                                                       encoding:NSUTF8StringEncoding];
             if (idToken == nil) {
               NSLog(@"Unable to serialize id token from data: %@", appleIDCredential.identityToken);
             }
             // Initialize a Firebase credential.
             FIROAuthCredential *credential = [FIROAuthProvider credentialWithProviderID:@"apple.com"
                                                                                 IDToken:idToken
                                                                                rawNonce:rawNonce];
             // Sign in with Firebase.
             [[FIRAuth auth] signInWithCredential:credential
                                       completion:^(FIRAuthDataResult * _Nullable authResult,
                                                    NSError * _Nullable error) {
               if (error != nil) {
                 // Error. If error.code == FIRAuthErrorCodeMissingOrInvalidNonce,
                 // make sure you're sending the SHA256-hashed nonce as a hex string
                 // with your request to Apple.
                 return;
               }
               // Sign-in succeeded!
             }];
           }
         }
         
         - (void)authorizationController:(ASAuthorizationController *)controller
                    didCompleteWithError:(NSError *)error API_AVAILABLE(ios(13.0)) {
           NSLog(@"Sign in with Apple errored: %@", error);
         }
         




Unlike many other identity providers, Apple does not provide a photo URL.

If a user chooses not to share their real email with your app, Apple provisions a unique email address for that user to share instead. This email takes the form `xyz@privaterelay.appleid.com`. If you configured the private email relay service, Apple forwards emails sent to the anonymized address to the user's real email address.

Apple only shares user information, such as display names, with apps the first time a user signs in. In most cases, Identity Platform stores this data, which lets you fetch it using `firebase.auth().currentUser.displayName` during future sessions. However, if you allowed users to sign into your app using Apple before integrating with Identity Platform, user information is not available.

### User account deletion

Apple requires that iOS apps that support account creation must also let users initiate deletion of their account from within the app.

When deleting a user account, you must revoke the user's token before deleting the user's account, as well as all data you stored for them in Firestore, Cloud Storage, and Firebase Realtime Database. For more information, see [Offering account deletion in your app](https://developer.apple.com/support/offering-account-deletion-in-your-app/) in Apple's developer support documentation.

Since Identity Platform does not store user tokens when users are created with Apple sign-in, you must ask the user to sign in before revoking their token and deleting the account. Alternatively, to avoid asking the user to sign in again if a user is signed in with Apple sign-in, you can store the authorization code to reuse during token revocation.

To revoke a user's token and delete their account, run the following:

###  Swift 
    
    
    let user = Auth.auth().currentUser
    
    // Check if the user has a token.
    if let providerData = user?.providerData {
      for provider in providerData {
        guard let provider = provider as? FIRUserInfo else {
          continue
        }
        if provider.providerID() == "apple.com" {
          isAppleProviderLinked = true
        }
      }
    }
    
    // Re-authenticate the user and revoke their token
    if isAppleProviderLinked {
      let request = appleIDRequest(withState: "revokeAppleTokenAndDeleteUser")
      let controller = ASAuthorizationController(authorizationRequests: [request])
      controller.delegate = self
      controller.presentationContextProvider = self
      controller.performRequests()
    } else {
      // Usual user deletion
    }
    
    func authorizationController(
      controller: ASAuthorizationController,
      didCompleteWithAuthorization authorization: ASAuthorization
    ) {
      if authorization.credential is ASAuthorizationAppleIDCredential {
        let appleIDCredential = authorization.credential as? ASAuthorizationAppleIDCredential
        if authorization.credential is ASAuthorizationAppleIDCredential {
          if appleIDCredential.state == "signIn" {
            // Sign in with Firebase.
            // ...
          } else if appleIDCredential.state == "revokeAppleTokenAndDeleteUser" {
            // Revoke token with Firebase.
            Auth.auth().revokeTokenWithAuthorizationCode(code) { error in
              if error != nil {
                // Token revocation failed.
              } else {
                // Token revocation succeeded then delete user again.
                let user = Auth.auth().currentUser
                user?.delete { error in
                  // ...
                }
              }
    
            }
          }
        }
      }
    }
    

###  Objective-C 
    
    
    FIRUser *user = [FIRAuth auth].currentUser;
    
    // Check if the user has a token.
    BOOL isAppleProviderLinked = false;
    for (id<FIRUserInfo> provider in user.providerData) {
      if ([[provider providerID] isEqual:@"apple.com"]) {
        isAppleProviderLinked = true;
      }
    }
    
    // Re-authenticate the user and revoke their token
    if (isAppleProviderLinked) {
      if (@available(iOS 13, *)) {
        ASAuthorizationAppleIDRequest *request =
            [self appleIDRequestWithState:@"revokeAppleTokenAndDeleteUser"];
        ASAuthorizationController *controller = [[ASAuthorizationController alloc]
            initWithAuthorizationRequests:@[ request ]];
        controller.delegate = self;
        controller.presentationContextProvider = self;
        [controller performRequests];
      }
    } else {
      // Usual user deletion
    }
    
    - (void)authorizationController:(ASAuthorizationController *)controller
        didCompleteWithAuthorization:(ASAuthorization *)authorization
        API_AVAILABLE(ios(13.0)) {
      if ([authorization.credential
              isKindOfClass:[ASAuthorizationAppleIDCredential class]]) {
        ASAuthorizationAppleIDCredential *appleIDCredential =
            authorization.credential;
    
        if ([appleIDCredential.state isEqualToString:@"signIn"]) {
          // Sign in with Firebase.
          // ...
        } else if ([appleIDCredential.state
                      isEqualToString:@"revokeAppleTokenAndDeleteUser"]) {
          // Revoke token with Firebase.
          NSString *code =
              [[NSString alloc] initWithData:appleIDCredential.authorizationCode
                                    encoding:NSUTF8StringEncoding];
          [[FIRAuth auth]
              revokeTokenWithAuthorizationCode:code
                                    completion:^(NSError *_Nullable error) {
                                      if (error != nil) {
                                        // Token revocation failed.
                                      } else {
                                        // Token revocation succeeded then delete
                                        // user again.
                                        FIRUser *user = [FIRAuth auth].currentUser;
                                        [user deleteWithCompletion:^(
                                                  NSError *_Nullable error){
                                            // ...
                                        }];
                                      }
                                    }];
        }
      }
    }
    

## What's next

  * Learn more about [Identity Platform users](https://docs.cloud.google.com/identity-platform/docs/concepts-manage-users).
  * Sign in users with [other identity providers](https://docs.cloud.google.com/identity-platform/docs/how-to#signing-in-users).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
