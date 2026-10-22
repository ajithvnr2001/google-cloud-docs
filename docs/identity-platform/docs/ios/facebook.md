---
url: https://docs.cloud.google.com/identity-platform/docs/ios/facebook/
title: Signing in users with Facebook on iOS \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:45:01.486078+00:00
---

# Signing in users with Facebook on iOS  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/ios/facebook/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Signing in users with Facebook on iOS

You can let your users authenticate with Identity Platform using their Facebook accounts by integrating Facebook Login or Facebook Limited Login into your app. This page shows you how to use Identity Platform to add Sign in with Facebook to your iOS app.

## Before you begin

  1. [Add Firebase to your iOS project](https://firebase.google.com/docs/ios/setup).

  2. Include the following pods in your `Podfile`:
         
         pod 'FirebaseAuth'
         

  3. Go to the **Identity Providers** page in the Google Cloud console.

[Go to the Identity Providers page](https://console.cloud.google.com/customer-identity/providers)

  4. Click **Add A Provider**.

  5. Select **Facebook** from the list.

  6. Enter your Facebook **App ID** and **App Secret**. If you don't already have an ID and secret, you can obtain one from the [Facebook for Developers](https://developers.facebook.com/apps) page.

  7. Configure the URI listed under **Configure Facebook** as a valid OAuth redirect URI for your Facebook app. If you configured a custom domain in Identity Platform, update the redirect URI in your Facebook app configuration to use the custom domain instead of the default domain. For example, change `https://myproject.firebaseapp.com/__/auth/handler` to `https://auth.myownpersonaldomain.com/__/auth/handler`. 

  8. Register your app's domains by clicking **Add Domain** under **Authorized Domains**. For development purposes, `localhost` is already enabled by default.

**Important:** In projects created after April 28, 2025, Identity Platform no longer includes `localhost` as an authorized domain by default. Google strongly discourages the use of `localhost` in production projects. If you choose to authorize `localhost`, you can manually add it in the **Settings** page, in **Authorized Domains** , by clicking **Add Domain**.
  9. Under **Configure your application** , click **Setup Details**. Copy the snippet into your app's code to initialize the Identity Platform client SDK.

  10. Click **Save**.




## Implement Facebook Login

To use "classic" Facebook Login, complete the following steps. Alternatively, you can use Facebook Limited Login, as shown in the next section. 

  1. Integrate Facebook Login into your app by following the [ developer's documentation](https://developers.facebook.com/docs/facebook-login/ios). When you initialize the `FBSDKLoginButton` object, set a delegate to receive login and logout events. For example: 

#### Swift
         
         let loginButton = FBSDKLoginButton()
         loginButton.delegate = self

#### Objective-C
         
         FBSDKLoginButton *loginButton = [[FBSDKLoginButton alloc] init];
         loginButton.delegate = self;

In your delegate, implement `didCompleteWithResult:error:`. 

#### Swift
         
         func loginButton(_ loginButton: FBSDKLoginButton!, didCompleteWith result: FBSDKLoginManagerLoginResult!, error: Error!) {
           if let error = error {
             print(error.localizedDescription)
             return
           }
           // ...
         }

#### Objective-C
         
         - (void)loginButton:(FBSDKLoginButton *)loginButton
             didCompleteWithResult:(FBSDKLoginManagerLoginResult *)result
                             error:(NSError *)error {
           if (error == nil) {
             // ...
           } else {
             NSLog(error.localizedDescription);
           }
         }

  2. Import the Firebase module in your `UIApplicationDelegate`: 

#### Swift
         
         import FirebaseCore
         import FirebaseAuth
               

#### Objective-C
         
         @import FirebaseCore;
         @import FirebaseAuth;
               

  3. Configure a [`FirebaseApp`](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIRApp) shared instance, typically in your app's `application:didFinishLaunchingWithOptions:` method: 

#### Swift
         
         // Use Firebase library to configure APIs
         FirebaseApp.configure()

#### Objective-C
         
         // Use Firebase library to configure APIs
         [FIRApp configure];

  4. After a user successfully signs in, in your implementation of `didCompleteWithResult:error:`, get an access token for the signed-in user and exchange it for an Identity Platform credential: 

#### Swift
         
         let credential = FacebookAuthProvider
           .credential(withAccessToken: AccessToken.current!.tokenString)

#### Objective-C
         
         FIRAuthCredential *credential = [FIRFacebookAuthProvider
             credentialWithAccessToken:[FBSDKAccessToken currentAccessToken].tokenString];




## Implement Facebook Limited Login

To use Facebook Limited Login instead of "classic" Facebook Login, complete the following steps. 

  1. Integrate Facebook Limited Login into your app by following the [ developer's documentation](https://developers.facebook.com/docs/facebook-login/limited-login/ios). 
  2. For every sign-in request, generate a unique random string—a "nonce"—which you will use to make sure the ID token you get was granted specifically in response to your app's authentication request. This step is important to prevent replay attacks. You can generate a cryptographically secure nonce on iOS with `SecRandomCopyBytes(_:_:_)`, as in the following example: 

#### Swift
         
         private func randomNonceString(length: Int = 32) -> String {
           precondition(length > 0)
           var randomBytes = [UInt8](repeating: 0, count: length)
           let errorCode = SecRandomCopyBytes(kSecRandomDefault, randomBytes.count, &randomBytes)
           if errorCode != errSecSuccess {
             fatalError(
               "Unable to generate nonce. SecRandomCopyBytes failed with OSStatus \(errorCode)"
             )
           }
         
           let charset: [Character] =
             Array("0123456789ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvwxyz-._")
         
           let nonce = randomBytes.map { byte in
             // Pick a random character from the set, wrapping around if needed.
             charset[Int(byte) % charset.count]
           }
         
           return String(nonce)
         }
         
                 

#### Objective-C
         
         // Adapted from https://auth0.com/docs/api-auth/tutorials/nonce#generate-a-cryptographically-random-nonce
         - (NSString *)randomNonce:(NSInteger)length {
           NSAssert(length > 0, @"Expected nonce to have positive length");
           NSString *characterSet = @"0123456789ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvwxyz-._";
           NSMutableString *result = [NSMutableString string];
           NSInteger remainingLength = length;
         
           while (remainingLength > 0) {
             NSMutableArray *randoms = [NSMutableArray arrayWithCapacity:16];
             for (NSInteger i = 0; i < 16; i++) {
               uint8_t random = 0;
               int errorCode = SecRandomCopyBytes(kSecRandomDefault, 1, &random);
               NSAssert(errorCode == errSecSuccess, @"Unable to generate nonce: OSStatus %i", errorCode);
         
               [randoms addObject:@(random)];
             }
         
             for (NSNumber *random in randoms) {
               if (remainingLength == 0) {
                 break;
               }
         
               if (random.unsignedIntValue < characterSet.length) {
                 unichar character = [characterSet characterAtIndex:random.unsignedIntValue];
                 [result appendFormat:@"%C", character];
                 remainingLength--;
               }
             }
           }
         
           return [result copy];
         }
                 

You will send the SHA-256 hash of the nonce with your sign-in request, which Facebook will pass unchanged in the response. Identity Platform validates the response by hashing the original nonce and comparing it to the value passed by Facebook. 

#### Swift
         
         @available(iOS 13, *)
         private func sha256(_ input: String) -> String {
           let inputData = Data(input.utf8)
           let hashedData = SHA256.hash(data: inputData)
           let hashString = hashedData.compactMap {
             String(format: "%02x", $0)
           }.joined()
         
           return hashString
         }
         
                 

#### Objective-C
         
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
                 

  3. When you set up the `FBSDKLoginButton`, set a delegate to receive login and logout events, set the tracking mode to `FBSDKLoginTrackingLimited`, and attach a nonce. For example: 

#### Swift
         
         func setupLoginButton() {
             let nonce = randomNonceString()
             currentNonce = nonce
             loginButton.delegate = self
             loginButton.loginTracking = .limited
             loginButton.nonce = sha256(nonce)
         }
                 

#### Objective-C
         
         - (void)setupLoginButton {
           NSString *nonce = [self randomNonce:32];
           self.currentNonce = nonce;
           self.loginButton.delegate = self;
           self.loginButton.loginTracking = FBSDKLoginTrackingLimited
           self.loginButton.nonce = [self stringBySha256HashingString:nonce];
         }
                 

In your delegate, implement `didCompleteWithResult:error:`. 

#### Swift
         
         func loginButton(_ loginButton: FBSDKLoginButton!, didCompleteWith result: FBSDKLoginManagerLoginResult!, error: Error!) {
           if let error = error {
             print(error.localizedDescription)
             return
           }
           // ...
         }
                 

#### Objective-C
         
         - (void)loginButton:(FBSDKLoginButton *)loginButton
             didCompleteWithResult:(FBSDKLoginManagerLoginResult *)result
                             error:(NSError *)error {
           if (error == nil) {
             // ...
           } else {
             NSLog(error.localizedDescription);
           }
         }
                 

  4. Import the Firebase module in your `UIApplicationDelegate`: 

#### Swift
         
         import Firebase

#### Objective-C
         
         @import Firebase;

  5. Configure a [`FirebaseApp`](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIRApp) shared instance, typically in your app's `application:didFinishLaunchingWithOptions:` method: 

#### Swift
         
         // Use Firebase library to configure APIs
         FirebaseApp.configure()

#### Objective-C
         
         // Use Firebase library to configure APIs
         [FIRApp configure];

  6. After a user successfully signs in, in your implementation of `didCompleteWithResult:error:`, use the ID token from Facebook's response with the unhashed nonce to get an Identity Platform credential: 

#### Swift
         
         // Initialize an Identity Platform credential.
         let idTokenString = AuthenticationToken.current?.tokenString
         let nonce = currentNonce
         let credential = OAuthProvider.credential(withProviderID: "facebook.com",
                                                   IDToken: idTokenString,
                                                   rawNonce: nonce)
                 

#### Objective-C
         
         // Initialize an Identity Platform credential.
         NSString *idTokenString = FBSDKAuthenticationToken.currentAuthenticationToken.tokenString;
         NSString *rawNonce = self.currentNonce;
         FIROAuthCredential *credential = [FIROAuthProvider credentialWithProviderID:@"facebook.com"
                                                                             IDToken:idTokenString
                                                                            rawNonce:rawNonce];
                 




## Authenticate with Identity Platform

Finally, authenticate with Identity Platform using the Identity Platform credential:

#### Swift
    
    
    Auth.auth().signIn(with: credential) { authResult, error in
        if let error = error {
          let authError = error as NSError
          if isMFAEnabled, authError.code == AuthErrorCode.secondFactorRequired.rawValue {
            // The user is a multi-factor user. Second factor challenge is required.
            let resolver = authError
              .userInfo[AuthErrorUserInfoMultiFactorResolverKey] as! MultiFactorResolver
            var displayNameString = ""
            for tmpFactorInfo in resolver.hints {
              displayNameString += tmpFactorInfo.displayName ?? ""
              displayNameString += " "
            }
            self.showTextInputPrompt(
              withMessage: "Select factor to sign in\n\(displayNameString)",
              completionBlock: { userPressedOK, displayName in
                var selectedHint: PhoneMultiFactorInfo?
                for tmpFactorInfo in resolver.hints {
                  if displayName == tmpFactorInfo.displayName {
                    selectedHint = tmpFactorInfo as? PhoneMultiFactorInfo
                  }
                }
                PhoneAuthProvider.provider()
                  .verifyPhoneNumber(with: selectedHint!, uiDelegate: nil,
                                     multiFactorSession: resolver
                                       .session) { verificationID, error in
                    if error != nil {
                      print(
                        "Multi factor start sign in failed. Error: \(error.debugDescription)"
                      )
                    } else {
                      self.showTextInputPrompt(
                        withMessage: "Verification code for \(selectedHint?.displayName ?? "")",
                        completionBlock: { userPressedOK, verificationCode in
                          let credential: PhoneAuthCredential? = PhoneAuthProvider.provider()
                            .credential(withVerificationID: verificationID!,
                                        verificationCode: verificationCode!)
                          let assertion: MultiFactorAssertion? = PhoneMultiFactorGenerator
                            .assertion(with: credential!)
                          resolver.resolveSignIn(with: assertion!) { authResult, error in
                            if error != nil {
                              print(
                                "Multi factor finanlize sign in failed. Error: \(error.debugDescription)"
                              )
                            } else {
                              self.navigationController?.popViewController(animated: true)
                            }
                          }
                        }
                      )
                    }
                  }
              }
            )
          } else {
            self.showMessagePrompt(error.localizedDescription)
            return
          }
          // ...
          return
        }
        // User is signed in
        // ...
    }
        

#### Objective-C
    
    
    [[FIRAuth auth] signInWithCredential:credential
                              completion:^(FIRAuthDataResult * _Nullable authResult,
                                           NSError * _Nullable error) {
        if (isMFAEnabled && error && error.code == FIRAuthErrorCodeSecondFactorRequired) {
          FIRMultiFactorResolver *resolver = error.userInfo[FIRAuthErrorUserInfoMultiFactorResolverKey];
          NSMutableString *displayNameString = [NSMutableString string];
          for (FIRMultiFactorInfo *tmpFactorInfo in resolver.hints) {
            [displayNameString appendString:tmpFactorInfo.displayName];
            [displayNameString appendString:@" "];
          }
          [self showTextInputPromptWithMessage:[NSString stringWithFormat:@"Select factor to sign in\n%@", displayNameString]
                               completionBlock:^(BOOL userPressedOK, NSString *_Nullable displayName) {
           FIRPhoneMultiFactorInfo* selectedHint;
           for (FIRMultiFactorInfo *tmpFactorInfo in resolver.hints) {
             if ([displayName isEqualToString:tmpFactorInfo.displayName]) {
               selectedHint = (FIRPhoneMultiFactorInfo *)tmpFactorInfo;
             }
           }
           [FIRPhoneAuthProvider.provider
            verifyPhoneNumberWithMultiFactorInfo:selectedHint
            UIDelegate:nil
            multiFactorSession:resolver.session
            completion:^(NSString * _Nullable verificationID, NSError * _Nullable error) {
              if (error) {
                [self showMessagePrompt:error.localizedDescription];
              } else {
                [self showTextInputPromptWithMessage:[NSString stringWithFormat:@"Verification code for %@", selectedHint.displayName]
                                     completionBlock:^(BOOL userPressedOK, NSString *_Nullable verificationCode) {
                 FIRPhoneAuthCredential *credential =
                     [[FIRPhoneAuthProvider provider] credentialWithVerificationID:verificationID
                                                                  verificationCode:verificationCode];
                 FIRMultiFactorAssertion *assertion = [FIRPhoneMultiFactorGenerator assertionWithCredential:credential];
                 [resolver resolveSignInWithAssertion:assertion completion:^(FIRAuthDataResult * _Nullable authResult, NSError * _Nullable error) {
                   if (error) {
                     [self showMessagePrompt:error.localizedDescription];
                   } else {
                     NSLog(@"Multi factor finanlize sign in succeeded.");
                   }
                 }];
               }];
              }
            }];
         }];
        }
      else if (error) {
        // ...
        return;
      }
      // User successfully signed in. Get user data from the FIRUser object
      if (authResult == nil) { return; }
      FIRUser *user = authResult.user;
      // ...
    }];
        

## What's next

  * Learn more about [Identity Platform users](https://docs.cloud.google.com/identity-platform/docs/concepts-manage-users).
  * Sign in users with [other identity providers](https://docs.cloud.google.com/identity-platform/docs/how-to#signing-in-users).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
