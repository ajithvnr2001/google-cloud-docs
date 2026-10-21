---
url: https://docs.cloud.google.com/identity-platform/docs/admin/enabling-totp-mfa/
title: Enable TOTP MFA for your app \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:49:19.268402+00:00
---

# Enable TOTP MFA for your app  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/admin/enabling-totp-mfa/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Enable TOTP MFA for your app

This document describes how to add time-based one-time password (TOTP) multi-factor authentication (MFA) to your app.

Identity Platform lets you use a TOTP as an additional factor for MFA. When you enable this feature, users attempting to sign in to your app see a request for a TOTP. To generate it, they must use an authenticator app capable of generating valid TOTP codes, such as [Google Authenticator](https://support.google.com/accounts/answer/1066447).

## Before you begin

  1. Enable at least one provider that supports MFA. Note that all providers _except_ the following support MFA:

     * Phone auth
     * Anonymous auth
     * Custom auth tokens
     * Apple Game Center
  2. Ensure your app verifies user email addresses. MFA requires email verification. This prevents malicious actors from registering for a service with an email address that they don't own, and then locking out the actual owner of the email address by adding a second factor. 

  3. Make sure you have the correct platform version. TOTP MFA is only supported on the following SDK versions:

Platform | Versions  
---|---  
Web SDK | v9.19.1+  
Android SDK | 22.1.0+  
iOS SDK | 10.12.0+  



## Enable TOTP MFA at the project level

To enable TOTP as a second factor, use the Admin SDK or call the project configuration REST endpoint.

To use the Admin SDK, do the following:

  1. If you haven't done so already, install the [Firebase Admin Node.js SDK](https://firebase.google.com/docs/admin/setup).

TOTP MFA is only supported on Firebase Admin Node.js SDK versions 11.6.0 and above.

  2. Run the following:
         
         import { getAuth } from 'firebase-admin/auth';
         
         getAuth().projectConfigManager().updateProjectConfig(
         {
               multiFactorConfig: {
                   providerConfigs: [{
                       state: "ENABLED",
                       totpProviderConfig: {
                           adjacentIntervals: NUM_ADJ_INTERVALS
                       }
                   }]
               }
         })
         

Replace the following:

     * `NUM_ADJ_INTERVALS`: The number of adjacent time-window intervals from which to accept TOTPs, from zero to ten. The default is five.

TOTPs work by ensuring that when two parties (the prover and the validator) generate OTPs within the same time window (typically 30 seconds long), they generate the same password. However, to accommodate clock drift between parties and human response time, you can configure the TOTP service to also accept TOTPs from adjacent windows.




To enable TOTP MFA using the REST API, run the following:
    
    
    curl -X PATCH "https://identitytoolkit.googleapis.com/admin/v2/projects/PROJECT_ID/config?updateMask=mfa" \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -H "X-Goog-User-Project: PROJECT_ID" \
        -d \
        '{
            "mfa": {
              "providerConfigs": [{
                "state": "ENABLED",
                "totpProviderConfig": {
                  "adjacentIntervals": NUM_ADJ_INTERVALS
                }
              }]
           }
        }'
    

Replace the following:

  * `PROJECT_ID`: The project ID.
  * `NUM_ADJ_INTERVALS`: The number of time-window intervals, from zero to ten. The default is five.

TOTPs work by ensuring that when two parties (the prover and the validator) generate OTPs within the same time window (typically 30 seconds long), they generate the same password. However, to accommodate clock drift between parties and human response time, you can configure the TOTP service to also accept TOTPs from adjacent windows.




## Enable TOTP MFA at the tenant level

To enable TOTP as a second factor for MFA at the tenant level, use the following code:
    
    
    getAuth().tenantManager().updateTenant(TENANT_ID,
    {
          multiFactorConfig: {
              state: 'ENABLED',
              providerConfigs: [{
                  totpProviderConfig: {
                      adjacentIntervals: NUM_ADJ_INTERVALS
                  }
              }]
          }
    })
    

Replace the following:

  * `TENANT_ID`: The string tenant ID.
  * `NUM_ADJ_INTERVALS`: The number of time-window intervals, from zero to ten. The default is five.



To enable TOTP MFA using the REST API at the tenant level, run the following:
    
    
    curl -X PATCH "https://identitytoolkit.googleapis.com/v2/projects/PROJECT_ID/tenants/TENANT_ID?updateMask=mfaConfig" \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -H "X-Goog-User-Project: PROJECT_ID" \
        -d \
        '{
            "mfaConfig": {
              "providerConfigs": [{
                "totpProviderConfig": {
                  "adjacentIntervals": NUM_ADJ_INTERVALS
                }
              }]
           }
        }'
    

Replace the following:

  * `PROJECT_ID`: The project ID.
  * `TENANT_ID`: The tenant ID.
  * `NUM_ADJ_INTERVALS`: The number of time-window intervals, from zero to ten. The default is five.



## Choose an enrollment pattern

You can choose whether your app requires multi-factor authentication, and how and when to enroll your users. Some common patterns include the following:

  * Enroll the user's second factor as part of registration. Use this method if your app requires multi-factor authentication for all users.

  * Offer a skippable option to enroll a second factor during registration. If you want to encourage but not require multi-factor authentication in your app, you might use this approach.

  * Provide the ability to add a second factor from the user's account or profile management page, instead of the sign-up screen. This minimizes friction during the registration process, while still making multi-factor authentication available for security-sensitive users.

  * Require adding a second factor incrementally when the user wants to access features with increased security requirements.




## Enroll users in TOTP MFA

After you enable TOTP MFA as a second factor for your app, implement client-side logic to enroll users in TOTP MFA:

###  Web 
    
    
    import {
        multiFactor,
        TotpMultiFactorGenerator,
        TotpSecret
    } from "firebase/auth";
    
    multiFactorSession = await multiFactor(activeUser()).getSession();
    totpSecret = await TotpMultiFactorGenerator.generateSecret(
        multiFactorSession
    );
    
    // Display this URL as a QR code.
    const url = totpSecret.generateQrCodeUrl( <user account id> , <app name> );
    
    // Ask the user for the verification code from the OTP app by scanning the QR
    // code.
    const multiFactorAssertion = TotpMultiFactorGenerator.assertionForEnrollment(
        totpSecret,
        verificationCode
    );
    
    // Finalize the enrollment.
    return multiFactor(user).enroll(multiFactorAssertion, mfaDisplayName);
    

###  Java
    
    
    user.getMultiFactor().getSession()
      .addOnCompleteListener(
      new OnCompleteListener<MultiFactorSession>() {
          @Override
          public void onComplete(@NonNull Task<MultiFactorSession> task) {
            if (task.isSuccessful()) {
    
              // Get a multi-factor session for the user.
              MultiFactorSession multiFactorSession = task.getResult();
    
              TotpMultiFactorGenerator.generateSecret(multiFactorSession)
                  .addOnCompleteListener(
                  new OnCompleteListener<TotpSecret>() {
                      @Override
                      public void onComplete(@NonNull Task<TotpSecret> task){
                        if (task.isSuccessful()) {
    
                          TotpSecret secret = task.getResult();
    
                          // Display this URL as a QR code for the user to scan.
                          String qrCodeUrl = secret.generateQrCodeUrl();
    
                          // Display the QR code
                          // ...
    
                          // Alternatively, you can automatically load the QR code
                          // into a TOTP authenticator app with either default or
                          // specified fallback URL and activity.
                          // Default fallback URL and activity.
                          secret.openInOtpApp(qrCodeUrl);
    
                          // Specified fallback URL and activity.
                          // secret.openInOtpApp(qrCodeUrl, fallbackUrl, activity);
    
                        }
                      }
                  });
            }
          }
        });
    
      // Ask the user for the one-time password (otp) from the TOTP authenticator app.
      MultiFactorAssertion multiFactorAssertion =
        TotpMultiFactorGenerator.getAssertionForEnrollment(
        secret, otp);
    
      // Complete the enrollment.
      user
        .getMultiFactor()
        .enroll(multiFactorAssertion, /* displayName= */ "My TOTP second factor")
        .addOnCompleteListener(
          new OnCompleteListener<Void>() {
            @Override
            public void onComplete(@NonNull Task<Void> task) {
              if (task.isSuccessful()) {
                showToast("Successfully enrolled TOTP second factor!");
                setResult(Activity.RESULT_OK);
                finish();
              }
            }
        });
    

###  Kotlin+KTX
    
    
    user.multiFactor.session.addOnCompleteListener { task ->
      if (task.isSuccessful) {
    
        // Get a multi-factor session for the user.
        val session: MultiFactorSession = task.result
        val secret: TotpSecret  = TotpMultiFactorGenerator.generateSecret(session)
    
        // Display this URL as a QR code for the user to scan.
        val qrCodeUrl = secret.generateQrCodeUrl()
        // Display the QR code
        // ...
    
        // Alternatively, you can automatically load the QR code
        // into a TOTP authenticator app with either default or
        // specified fallback URL and activity.
        // Default fallback URL and activity.
        secret.openInOtpApp(qrCodeUrl)
    
        // Specify a fallback URL and activity.
        // secret.openInOtpApp(qrCodeUrl, fallbackUrl, activity);
      }
    }
    
    // Ask the user for the one-time password (otp) from the TOTP authenticator app.
    val multiFactorAssertion =
      TotpMultiFactorGenerator.getAssertionForEnrollment(secret, otp)
    
    // Complete enrollment.
    user.multiFactor.enroll(multiFactorAssertion, /* displayName= */ "My TOTP second factor")
      .addOnCompleteListener {
      // ...
    }
    

###  Swift 
    
    
    let user = Auth.auth().currentUser
    
    // Get a multi-factor session for the user
    user?.multiFactor.getSessionWithCompletion({ (session, error) in
      TOTPMultiFactorGenerator.generateSecret(with: session!) {
        (secret, error) in
        let accountName = user?.email;
        let issuer = Auth.auth().app?.name;
    
        // Generate a QR code
        let qrCodeUrl = secret?.generateQRCodeURL(withAccountName: accountName!, issuer: issuer!)
    
        // Display the QR code
        // ...
    
        // Alternatively, you can automatically load the QR code
        // into a TOTP authenticator app with default fallback UR
        // and activity.
        secret?.openInOTPAppWithQRCodeURL(qrCodeUrl!);
    
        // Ask the user for the verification code after scanning
        let assertion = TOTPMultiFactorGenerator.assertionForEnrollment(with: secret, oneTimePassword: onetimePassword)
    
        // Complete the enrollment
        user?.multiFactor.enroll(with: assertion, displayName: accountName) { (error) in
          // ...
        }
      }
    })
    

###  Objective-C 
    
    
    FIRUser *user = FIRAuth.auth.currentUser;
    
    // Get a multi-factor session for the user
    [user.multiFactor getSessionWithCompletion:^(FIRMultiFactorSession *_Nullable session, NSError *_Nullable error) {
    
      // ...
    
      [FIRTOTPMultiFactorGenerator generateSecretWithMultiFactorSession:session completion:^(FIRTOTPSecret *_Nullable secret, NSError *_Nullable error) {
    
        NSString *accountName = user.email;
        NSString *issuer = FIRAuth.auth.app.name;
    
        // Generate a QR code
        NSString *qrCodeUrl = [secret generateQRCodeURLWithAccountName:accountName issuer:issuer];
    
        // Display the QR code
        // ...
    
        // Alternatively, you can automatically load the QR code
        // into a TOTP authenticator app with default fallback URL
        // and activity.
        [secret openInOTPAppWithQRCodeURL:qrCodeUrl];
    
        // Ask the user for the verification code after scanning
        FIRTOTPMultiFactorAssertion *assertion = [FIRTOTPMultiFactorGenerator assertionForEnrollmentWithSecret:secret oneTimePassword:oneTimePassword];
    
        // Complete the enrollment
        [user.multiFactor enrollWithAssertion:assertion
                                        displayName:displayName
                                         completion:^(NSError *_Nullable error) {
          // ...
    
        }];
      }];
    }];
    

## Sign in users with a second factor

To sign in users with TOTP MFA, use the following code:

###  Web 
    
    
    import {
        getAuth,
        getMultiFactorResolver,
        TotpMultiFactorGenerator,
        PhoneMultiFactorGenerator,
        signInWithEmailAndPassword
    } from "firebase/auth";
    
    const auth = getAuth();
    signInWithEmailAndPassword(auth, email, password)
        .then(function(userCredential) {
          // The user is not enrolled with a second factor and is successfully
          // signed in.
          // ...
        })
        .catch(function(error) {
          if (error.code === 'auth/multi-factor-auth-required') {
              const resolver = getMultiFactorResolver(auth, error);
    
              // Ask the user which second factor to use.
              if (resolver.hints[selectedIndex].factorId ===
                  TotpMultiFactorGenerator.FACTOR_ID) {
    
                  // Ask the user for the OTP code from the TOTP app.
                  const multiFactorAssertion = TotpMultiFactorGenerator.assertionForSignIn(resolver.hints[selectedIndex].uid, otp);
    
                  // Finalize the sign-in.
                  return resolver.resolveSignIn(multiFactorAssertion).then(function(userCredential) {
                    // The user successfully signed in with the TOTP second factor.
                  });
              } else if (resolver.hints[selectedIndex].factorId ===
                  PhoneMultiFactorGenerator.FACTOR_ID) {
                  // Handle the phone MFA.
              } else {
                  // The second factor is unsupported.
              }
          }
          // Handle other errors, such as a wrong password.
          else if (error.code == 'auth/wrong-password') {
            //...
          }
        });
    

###  Java
    
    
    FirebaseAuth.getInstance()
      .signInWithEmailAndPassword(email, password)
        .addOnCompleteListener(
            new OnCompleteListener<AuthResult>() {
              @Override
              public void onComplete(@NonNull Task<AuthResult> task) {
                if (task.isSuccessful()) {
    
                  // The user is not enrolled with a second factor and is
                  //  successfully signed in.
                  // ...
                  return;
                }
                if (task.getException() instanceof FirebaseAuthMultiFactorException) {
    
                  // The user is a multi-factor user. Second factor challenge is required.
                  FirebaseAuthMultiFactorException error =
                    (FirebaseAuthMultiFactorException) task.getException();
                  MultiFactorResolver multiFactorResolver = error.getResolver();
    
                  // Display the list of enrolled second factors, user picks one (selectedIndex) from the list.
                  MultiFactorInfo selectedHint = multiFactorResolver.getHints().get(selectedIndex);
    
                  if (selectedHint.getFactorId().equals(TotpMultiFactorGenerator.FACTOR_ID)) {
    
                    // Ask the user for the one-time password (otp) from the TOTP app.
                    // Initialize a MultiFactorAssertion object with the one-time password and enrollment id.
                    MultiFactorAssertion multiFactorAssertion =
                        TotpMultiFactorGenerator.getAssertionForSignIn(selectedHint.getUid(), otp);
    
                    // Complete sign-in.
                    multiFactorResolver
                        .resolveSignIn(multiFactorAssertion)
                        .addOnCompleteListener(
                            new OnCompleteListener<AuthResult>() {
                              @Override
                              public void onComplete(@NonNull Task<AuthResult> task) {
                                if (task.isSuccessful()) {
                                  // User successfully signed in with the
                                  // TOTP second factor.
                                }
                              }
                            });
                  } else if (selectedHint.getFactorId().equals(PhoneMultiFactorGenerator.FACTOR_ID)) {
                    // Handle Phone MFA.
                  } else {
                    // Unsupported second factor.
                  }
                } else {
                  // Handle other errors such as wrong password.
                }
              }
            });
    

###  Kotlin+KTX
    
    
    FirebaseAuth.getInstance
      .signInWithEmailAndPassword(email, password)
        .addOnCompleteListener{ task ->
                  if (task.isSuccessful) {
                    // User is not enrolled with a second factor and is successfully
                    // signed in.
                    // ...
                  }
                  if (task.exception is FirebaseAuthMultiFactorException) {
                      // The user is a multi-factor user. Second factor challenge is
                      // required.
                      val multiFactorResolver:MultiFactorResolver =
                      (task.exception as FirebaseAuthMultiFactorException).resolver
    
                      // Display the list of enrolled second factors, user picks one (selectedIndex) from the list.
                      val selectedHint: MultiFactorInfo = multiFactorResolver.hints[selectedIndex]
    
                      if (selectedHint.factorId == TotpMultiFactorGenerator.FACTOR_ID) {
                          val multiFactorAssertion =
                              TotpMultiFactorGenerator.getAssertionForSignIn(selectedHint.uid, otp)
    
                          multiFactorResolver.resolveSignIn(multiFactorAssertion)
                        .addOnCompleteListener { task ->
                                if (task.isSuccessful) {
                                    // User successfully signed in with the
                                    // TOTP second factor.
                                }
                                // ...
                          }
                      } else if (selectedHint.factor == PhoneMultiFactorGenerator.FACTOR_ID) {
                          // Handle Phone MFA.
                      } else {
                          // Invalid MFA option.
                      }
                  } else {
                      // Handle other errors, such as wrong password.
                  }
              }
    

###  Swift 
    
    
    Auth.auth().signIn(withEmail: email, password: password) {
      (result, error) in
      if (error != nil) {
        let authError = error! as NSError
        if authError.code == AuthErrorCode.secondFactorRequired.rawValue {
          let resolver = authError.userInfo[AuthErrorUserInfoMultiFactorResolverKey] as! MultiFactorResolver
          if resolver.hints[selectedIndex].factorID == TOTPMultiFactorID {
            let assertion = TOTPMultiFactorGenerator.assertionForSignIn(withEnrollmentID: resolver.hints[selectedIndex].uid, oneTimePassword: oneTimePassword)
            resolver.resolveSignIn(with: assertion) {
              (authResult, error) in
              if (error != nil) {
                // User successfully signed in with second factor TOTP.
              }
            }
    
          } else if (resolver.hints[selectedIndex].factorID == PhoneMultiFactorID) {
            // User selected a phone second factor.
            // ...
          } else {
            // Unsupported second factor.
            // Note that only phone and TOTP second factors are currently supported.
            // ...
          }
        }
      }
      else {
        // The user is not enrolled with a second factor and is
        //  successfully signed in.
        // ...
      }
    }
    

###  Objective-C 
    
    
    [FIRAuth.auth signInWithEmail:email
                       password:password
                     completion:^(FIRAuthDataResult * _Nullable authResult,
                                  NSError * _Nullable error) {
      if (error == nil || error.code != FIRAuthErrorCodeSecondFactorRequired) {
          // User is not enrolled with a second factor and is successfully signed in.
          // ...
      } else {
          // The user is a multi-factor user. Second factor challenge is required.
          [self signInWithMfaWithError:error];
      }
    }];
    
    - (void)signInWithMfaWithError:(NSError * _Nullable)error{
      FIRMultiFactorResolver *resolver = error.userInfo[FIRAuthErrorUserInfoMultiFactorResolverKey];
    
      // Ask user which second factor to use. Then:
      FIRMultiFactorInfo *hint = (FIRMultiFactorInfo *) resolver.hints[selectedIndex];
      if (hint.factorID == FIRTOTPMultiFactorID) {
        // User selected a totp second factor.
        // Ask user for verification code.
        FIRMultiFactorAssertion *assertion = [FIRTOTPMultiFactorGenerator  assertionForSignInWithEnrollmentID:hint.UID oneTimePassword:oneTimePassword];
        [resolver resolveSignInWithAssertion:assertion
                                      completion:^(FIRAuthDataResult *_Nullable authResult,
                                                  NSError *_Nullable error) {
          if (error != nil) {
            // User successfully signed in with the second factor TOTP.
          }
        }];
      } else if (hint.factorID == FIRPhoneMultiFactorID) {
          // User selected a phone second factor.
          // ...
      }
      else {
        // Unsupported second factor.
        // Note that only phone and totp second factors are currently supported.
      }
    }
    

The above example uses email and password as the first factor.

## Unenroll from TOTP MFA

This section describes how to handle a user unenrolling from TOTP MFA.

If a user has signed up for multiple MFA options, and if they unenroll from the most recently enabled option, they receive an `auth/user-token-expired` and are logged out. The user must sign in again and verify their existing credentials—for example, an email address and password.

To unenroll the user, handle the error, and trigger reauthentication, use the following code:

###  Web 
    
    
    import {
        EmailAuthProvider,
        TotpMultiFactorGenerator,
        getAuth,
        multiFactor,
        reauthenticateWithCredential,
    } from "firebase/auth";
    
    try {
        // Unenroll from TOTP MFA.
        await multiFactor(currentUser).unenroll(mfaEnrollmentId);
    } catch  (error) {
        if (error.code === 'auth/user-token-expired') {
            // If the user was signed out, re-authenticate them.
    
            // For example, if they signed in with a password, prompt them to
            // provide it again, then call `reauthenticateWithCredential()` as shown
            // below.
    
            const credential = EmailAuthProvider.credential(email, password);
            await reauthenticateWithCredential(
                currentUser,
                credential
            );
        }
    }
    

###  Java
    
    
    List<MultiFactorInfo> multiFactorInfoList = user.getMultiFactor().getEnrolledFactors();
    
    // Select the second factor to unenroll
    user
      .getMultiFactor()
      .unenroll(selectedMultiFactorInfo)
      .addOnCompleteListener(
          new OnCompleteListener<Void>() {
            @Override
            public void onComplete(@NonNull Task<Void> task) {
                if (task.isSuccessful()) {
                  // User successfully unenrolled the selected second factor.
                }
                else {
                  if (task.getException() instanceof FirebaseAuthInvalidUserException) {
                    // Handle reauthentication
                  }
                }
            }
          });
    

###  Kotlin+KTX
    
    
    val multiFactorInfoList = user.multiFactor.enrolledFactors
    
    // Select the option to unenroll
    user.multiFactor.unenroll(selectedMultiFactorInfo)
      .addOnCompleteListener { task ->
        if (task.isSuccessful) {
          // User successfully unenrolled the selected second factor.
        }
        else {
          if (task.exception is FirebaseAuthInvalidUserException) {
            // Handle reauthentication
          }
        }
      }
    

###  Swift 
    
    
    user?.multiFactor.unenroll(with: (user?.multiFactor.enrolledFactors[selectedIndex])!,
      completion: { (error) in
      if (error.code == AuthErrorCode.userTokenExpired.rawValue) {
        // Handle reauthentication
      }
    })
    

###  Objective-C 
    
    
    FIRMultiFactorInfo *unenrolledFactorInfo;
        for (FIRMultiFactorInfo *enrolledFactorInfo in FIRAuth.auth.currentUser.multiFactor.enrolledFactors) {
          // Pick one of the enrolled factors to delete.
        }
        [FIRAuth.auth.currentUser.multiFactor unenrollWithInfo:unenrolledFactorInfo
                                              completion:^(NSError * _Nullable error) {
          if (error.code == FIRAuthErrorCodeUserTokenExpired) {
                // Handle reauthentication
            }
        }];
    

## What's next

  * [Manage multi-factor users](https://docs.cloud.google.com/identity-platform/docs/admin/manage-mfa-users) programmatically with the Admin SDK.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
