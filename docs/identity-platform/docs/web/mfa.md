---
url: https://docs.cloud.google.com/identity-platform/docs/web/mfa/
title: Adding multi-factor authentication to your web app \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:57.535959+00:00
---

# Adding multi-factor authentication to your web app  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/web/mfa/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Adding multi-factor authentication to your web app 

This document shows you how to add SMS multi-factor authentication to your web app.

Multi-factor authentication increases the security of your app. While attackers often compromise passwords and social accounts, intercepting a text message is more difficult.

## Before you begin

  1. Enable at least one provider that supports multi-factor authentication. Every provider supports MFA, **except** phone auth, anonymous auth, and Apple Game Center.

  2. Enable the regions where you plan to use SMS authentication. Identity Platform uses a fully blocking SMS region policy, which helps to create your projects in a more secure state by default.

  3. Ensure your app is verifying user emails. MFA requires email verification. This prevents malicious actors from registering for a service with an email they don't own, and then locking out the real owner by adding a second factor.




### Using multi-tenancy

If you are enabling multi-factor authentication for use in a [multi-tenant](https://cloud.google.com/identity-platform/docs/multi-tenancy) environment, make sure to complete the following steps (in addition to the rest of the instructions in this document):

  1. In the Google Cloud console, select the tenant you want to work with.

  2. In your code, set the `tenantId` field on the `Auth` instance to your tenant's ID. For example:

###  Web version 9
         
         import { getAuth } from "firebase/auth";
         
         const auth = getAuth(app);
         auth.tenantId = "myTenantId1";
         

###  Web version 8
         
         firebase.auth().tenantId = 'myTenantId1';
         




## Enabling multi-factor authentication

  1. Go to the **Identity Platform MFA** page in the Google Cloud console.   
[Go to the MFA page](https://console.cloud.google.com/customer-identity/mfa)  


  2. In the box titled **SMS-Based Multi-Factor Authentication** , click **Enable**.

  3. Enter the phone numbers you'll be testing your app with. While optional, registering test phone numbers is strongly recommended to avoid throttling during development.

  4. If you haven't already authorized your app's domain, add it to the allow list by clicking **Add domain** on the right.

  5. Click **Save**.




## Choosing an enrollment pattern

You can choose whether your app requires multi-factor authentication, and how and when to enroll your users. Some common patterns include:

  * Enroll the user's second factor as part of registration. Use this method if your app requires multi-factor authentication for all users.

  * Offer a skippable option to enroll a second factor during registration. Apps that want to encourage, but not require, multi-factor authentication may prefer this approach.

  * Provide the ability to add a second factor from the user's account or profile management page, instead of the sign up screen. This minimizes friction during the registration process, while still making multi-factor authentication available for security-sensitive users.

  * Require adding a second factor incrementally when the user wants to access features with increased security requirements.




## Setting up the reCAPTCHA verifier

Before you can send SMS codes, you need to configure a reCAPTCHA verifier. Identity Platform uses reCAPTCHA to prevent abuse by ensuring that phone number verification requests come from one of your app's allowed domains.

You don't need to manually set up a reCAPTCHA client; the client SDK's `RecaptchaVerifier` object automatically creates and initializes any necessary client keys and secrets.

### Using invisible reCAPTCHA

The `RecaptchaVerifier` object supports [invisible reCAPTCHA](https://www.google.com/recaptcha/intro/invisible.html), which can often verify the user without requiring any interaction. To use an invisible reCAPTCHA, create a `RecaptchaVerifier` with the `size` parameter set to `invisible`, and specify the ID of the UI element that starts multi-factor enrollment:

###  Web version 9
    
    
    import { RecaptchaVerifier, getAuth } from "firebase/auth";
    
    const recaptchaVerifier = new RecaptchaVerifier(getAuth(), "sign-in-button", {
        "size": "invisible",
        "callback": function(response) {
            // reCAPTCHA solved, you can proceed with
            // phoneAuthProvider.verifyPhoneNumber(...).
            onSolvedRecaptcha();
        }
    });
    

###  Web version 8
    
    
    var recaptchaVerifier = new firebase.auth.RecaptchaVerifier('sign-in-button', {
    'size': 'invisible',
    'callback': function(response) {
      // reCAPTCHA solved, you can proceed with phoneAuthProvider.verifyPhoneNumber(...).
      onSolvedRecaptcha();
    }
    });
    

### Using the reCAPTCHA widget

To use a visible reCAPTCHA widget, create an HTML element to contain the widget, then create a `RecaptchaVerifier` object with the ID of the UI container. You can also optionally set callbacks that are invoked when the reCAPTCHA is solved or expires:

###  Web version 9
    
    
    import { RecaptchaVerifier, getAuth } from "firebase/auth";
    
    const recaptchaVerifier = new RecaptchaVerifier(
        getAuth(),
        "recaptcha-container",
    
        // Optional reCAPTCHA parameters.
        {
          "size": "normal",
          "callback": function(response) {
            // reCAPTCHA solved, you can proceed with
            // phoneAuthProvider.verifyPhoneNumber(...).
            onSolvedRecaptcha();
          },
          "expired-callback": function() {
            // Response expired. Ask user to solve reCAPTCHA again.
            // ...
          }
        }
    );
    

###  Web version 8
    
    
    var recaptchaVerifier = new firebase.auth.RecaptchaVerifier(
      'recaptcha-container',
      // Optional reCAPTCHA parameters.
      {
        'size': 'normal',
        'callback': function(response) {
          // reCAPTCHA solved, you can proceed with phoneAuthProvider.verifyPhoneNumber(...).
          // ...
          onSolvedRecaptcha();
        },
        'expired-callback': function() {
          // Response expired. Ask user to solve reCAPTCHA again.
          // ...
        }
      });
    

### Pre-rendering the reCAPTCHA

Optionally, you can pre-render the reCAPTCHA before starting two-factor enrollment:

###  Web version 9
    
    
    recaptchaVerifier.render()
        .then(function (widgetId) {
            window.recaptchaWidgetId = widgetId;
        });
    

###  Web version 8
    
    
    recaptchaVerifier.render()
      .then(function(widgetId) {
        window.recaptchaWidgetId = widgetId;
      });
    

After `render()` resolves, you get the reCAPTCHA's widget ID, which you can use to make calls to the [reCAPTCHA API](https://developers.google.com/recaptcha/intro):
    
    
    var recaptchaResponse = grecaptcha.getResponse(window.recaptchaWidgetId);
    

RecaptchaVerifier abstracts this logic away with the [verify](https://firebase.google.com/docs/reference/js/auth.recaptchaverifier.md#recaptchaverifierverify) method, so you need not handle the `grecaptcha` variable directly.

## Enrolling a second factor

To enroll a new secondary factor for a user:

  1. Re-authenticate the user.

  2. Ask the user enter their phone number.

**Note:** Google stores and uses phone numbers to improve spam and abuse prevention across all Google services. Ensure you obtain appropriate consent from your users before sending their phone numbers to Identity Platform.
  3. Initialize the reCAPTCHA verifier as illustrated in the previous section. Skip this step if a RecaptchaVerifier instance is already configured:

###  Web version 9
         
         import { RecaptchaVerifier, getAuth } from "firebase/auth";
         
         const recaptchaVerifier = new RecaptchaVerifier(
           getAuth(),'recaptcha-container-id', undefined);
         

###  Web version 8
         
         var recaptchaVerifier = new firebase.auth.RecaptchaVerifier('recaptcha-container-id');
         

  4. Get a multi-factor session for the user:

###  Web version 9
         
         import { multiFactor } from "firebase/auth";
         
         multiFactor(user).getSession().then(function (multiFactorSession) {
             // ...
         });
         

###  Web version 8
         
         user.multiFactor.getSession().then(function(multiFactorSession) {
           // ...
         })
         

  5. Initialize a `PhoneInfoOptions` object with the user's phone number and the multi-factor session:

###  Web version 9
         
         // Specify the phone number and pass the MFA session.
         const phoneInfoOptions = {
           phoneNumber: phoneNumber,
           session: multiFactorSession
         };
         

###  Web version 8
         
         // Specify the phone number and pass the MFA session.
         var phoneInfoOptions = {
           phoneNumber: phoneNumber,
           session: multiFactorSession
         };
         

  6. Send a verification message to the user's phone:

###  Web version 9
         
         import { PhoneAuthProvider } from "firebase/auth";
         
         const phoneAuthProvider = new PhoneAuthProvider(auth);
         phoneAuthProvider.verifyPhoneNumber(phoneInfoOptions, recaptchaVerifier)
             .then(function (verificationId) {
                 // verificationId will be needed to complete enrollment.
             });
         

###  Web version 8
         
         var phoneAuthProvider = new firebase.auth.PhoneAuthProvider();
         // Send SMS verification code.
         return phoneAuthProvider.verifyPhoneNumber(phoneInfoOptions, recaptchaVerifier)
           .then(function(verificationId) {
             // verificationId will be needed for enrollment completion.
           })
         

While not required, it's a best practice to inform users beforehand that they will receive an SMS message, and that standard rates apply.

  7. If the request fails, reset the reCAPTCHA, then repeat the previous step so the user can try again. Note that `verifyPhoneNumber()` will automatically reset the reCAPTCHA when it throws an error, as reCAPTCHA tokens are one-time use only.

###  Web version 9
         
         recaptchaVerifier.clear();
         

###  Web version 8
         
         recaptchaVerifier.clear();
         

  8. Once the SMS code is sent, ask the user to verify the code:

###  Web version 9
         
         // Ask user for the verification code. Then:
         const cred = PhoneAuthProvider.credential(verificationId, verificationCode);
         

###  Web version 8
         
         // Ask user for the verification code. Then:
         var cred = firebase.auth.PhoneAuthProvider.credential(verificationId, verificationCode);
         

  9. Initialize a `MultiFactorAssertion` object with the `PhoneAuthCredential`:

###  Web version 9
         
         import { PhoneMultiFactorGenerator } from "firebase/auth";
         
         const multiFactorAssertion = PhoneMultiFactorGenerator.assertion(cred);
         

###  Web version 8
         
         var multiFactorAssertion = firebase.auth.PhoneMultiFactorGenerator.assertion(cred);
         

  10. Complete the enrollment. Optionally, you can specify a display name for the second factor. This is useful for users with multiple second factors, since the phone number is masked during the authentication flow (for example, +1******1234).

###  Web version 9
         
         // Complete enrollment. This will update the underlying tokens
         // and trigger ID token change listener.
         multiFactor(user).enroll(multiFactorAssertion, "My personal phone number");
         

###  Web version 8
         
         // Complete enrollment. This will update the underlying tokens
         // and trigger ID token change listener.
         user.multiFactor.enroll(multiFactorAssertion, 'My personal phone number');
         




The code below shows a complete example of enrolling a second factor:

###  Web version 9
    
    
    import {
        multiFactor, PhoneAuthProvider, PhoneMultiFactorGenerator,
        RecaptchaVerifier, getAuth
    } from "firebase/auth";
    
    const recaptchaVerifier = new RecaptchaVerifier(getAuth(),
        'recaptcha-container-id', undefined);
    multiFactor(user).getSession()
        .then(function (multiFactorSession) {
            // Specify the phone number and pass the MFA session.
            const phoneInfoOptions = {
                phoneNumber: phoneNumber,
                session: multiFactorSession
            };
    
            const phoneAuthProvider = new PhoneAuthProvider(auth);
    
            // Send SMS verification code.
            return phoneAuthProvider.verifyPhoneNumber(phoneInfoOptions, recaptchaVerifier);
        }).then(function (verificationId) {
            // Ask user for the verification code. Then:
            const cred = PhoneAuthProvider.credential(verificationId, verificationCode);
            const multiFactorAssertion = PhoneMultiFactorGenerator.assertion(cred);
    
            // Complete enrollment.
            return multiFactor(user).enroll(multiFactorAssertion, mfaDisplayName);
        });
    

###  Web version 8
    
    
    var recaptchaVerifier = new firebase.auth.RecaptchaVerifier('recaptcha-container-id');
    user.multiFactor.getSession().then(function(multiFactorSession) {
      // Specify the phone number and pass the MFA session.
      var phoneInfoOptions = {
        phoneNumber: phoneNumber,
        session: multiFactorSession
      };
      var phoneAuthProvider = new firebase.auth.PhoneAuthProvider();
      // Send SMS verification code.
      return phoneAuthProvider.verifyPhoneNumber(
          phoneInfoOptions, recaptchaVerifier);
    })
    .then(function(verificationId) {
      // Ask user for the verification code.
      var cred = firebase.auth.PhoneAuthProvider.credential(verificationId, verificationCode);
      var multiFactorAssertion = firebase.auth.PhoneMultiFactorGenerator.assertion(cred);
      // Complete enrollment.
      return user.multiFactor.enroll(multiFactorAssertion, mfaDisplayName);
    });
    

Congratulations! You successfully registered a second authentication factor for a user.

**Important:** You should strongly encourage your users to register more than one second factor for account recovery purposes. If a user only registers a single second factor and later loses access to it, they will be locked out of their account.

## Signing users in with a second factor

To sign in a user with two-factor SMS verification:

  1. Sign the user in with their first factor, then catch the `auth/multi-factor-auth-required` error. This error contains a resolver, hints on the enrolled second factors, and an underlying session proving the user successfully authenticated with the first factor.

For example, if the user's first factor was an email and password:

###  Web version 9
         
         import { getAuth, signInWithEmailAndPassword, getMultiFactorResolver} from "firebase/auth";
         
         const auth = getAuth();
         signInWithEmailAndPassword(auth, email, password)
             .then(function (userCredential) {
                 // User successfully signed in and is not enrolled with a second factor.
             })
             .catch(function (error) {
                 if (error.code == 'auth/multi-factor-auth-required') {
                     // The user is a multi-factor user. Second factor challenge is required.
                     resolver = getMultiFactorResolver(auth, error);
                     // ...
                 } else if (error.code == 'auth/wrong-password') {
                     // Handle other errors such as wrong password.
                 }
         });
         

###  Web version 8
         
         firebase.auth().signInWithEmailAndPassword(email, password)
           .then(function(userCredential) {
             // User successfully signed in and is not enrolled with a second factor.
           })
           .catch(function(error) {
             if (error.code == 'auth/multi-factor-auth-required') {
               // The user is a multi-factor user. Second factor challenge is required.
               resolver = error.resolver;
               // ...
             } else if (error.code == 'auth/wrong-password') {
               // Handle other errors such as wrong password.
             } ...
           });
         

If the user's first factor is a federated provider, such as OAuth, SAML, or OIDC, catch the error after calling `signInWithPopup()` or `signInWithRedirect()`.

  2. If the user has multiple secondary factors enrolled, ask them which one to use:

###  Web version 9
         
         // Ask user which second factor to use.
         // You can get the masked phone number via resolver.hints[selectedIndex].phoneNumber
         // You can get the display name via resolver.hints[selectedIndex].displayName
         
         if (resolver.hints[selectedIndex].factorId ===
             PhoneMultiFactorGenerator.FACTOR_ID) {
             // User selected a phone second factor.
             // ...
         } else if (resolver.hints[selectedIndex].factorId ===
                    TotpMultiFactorGenerator.FACTOR_ID) {
             // User selected a TOTP second factor.
             // ...
         } else {
             // Unsupported second factor.
         }
         

###  Web version 8
         
         // Ask user which second factor to use.
         // You can get the masked phone number via resolver.hints[selectedIndex].phoneNumber
         // You can get the display name via resolver.hints[selectedIndex].displayName
         if (resolver.hints[selectedIndex].factorId === firebase.auth.PhoneMultiFactorGenerator.FACTOR_ID) {
           // User selected a phone second factor.
           // ...
         } else if (resolver.hints[selectedIndex].factorId === firebase.auth.TotpMultiFactorGenerator.FACTOR_ID) {
           // User selected a TOTP second factor.
           // ...
         } else {
           // Unsupported second factor.
         }
         

  3. Initialize the reCAPTCHA verifier as illustrated in the previous section. Skip this step if a RecaptchaVerifier instance is already configured:

###  Web version 9
         
         import { RecaptchaVerifier, getAuth } from "firebase/auth";
         
         recaptchaVerifier = new RecaptchaVerifier(getAuth(),
             'recaptcha-container-id', undefined);
         

###  Web version 8
         
         var recaptchaVerifier = new firebase.auth.RecaptchaVerifier('recaptcha-container-id');
         

  4. Initialize a `PhoneInfoOptions` object with the user's phone number and the multi-factor session. These values are contained in the `resolver` object passed to the `auth/multi-factor-auth-required` error:

###  Web version 9
         
         const phoneInfoOptions = {
             multiFactorHint: resolver.hints[selectedIndex],
             session: resolver.session
         };
         

###  Web version 8
         
         var phoneInfoOptions = {
           multiFactorHint: resolver.hints[selectedIndex],
           session: resolver.session
         };
         

  5. Send a verification message to the user's phone:

###  Web version 9
         
         // Send SMS verification code.
         const phoneAuthProvider = new PhoneAuthProvider(auth);
         phoneAuthProvider.verifyPhoneNumber(phoneInfoOptions, recaptchaVerifier)
             .then(function (verificationId) {
                 // verificationId will be needed for sign-in completion.
             });
         

###  Web version 8
         
         var phoneAuthProvider = new firebase.auth.PhoneAuthProvider();
         // Send SMS verification code.
         return phoneAuthProvider.verifyPhoneNumber(phoneInfoOptions, recaptchaVerifier)
           .then(function(verificationId) {
             // verificationId will be needed for sign-in completion.
           })
         

  6. If the request fails, reset the reCAPTCHA, then repeat the previous step so the user can try again:

###  Web version 9
         
         recaptchaVerifier.clear();
         

###  Web version 8
         
         recaptchaVerifier.clear();
         

  7. Once the SMS code is sent, ask the user to verify the code:

###  Web version 9
         
         const cred = PhoneAuthProvider.credential(verificationId, verificationCode);
         

###  Web version 8
         
         // Ask user for the verification code. Then:
         var cred = firebase.auth.PhoneAuthProvider.credential(verificationId, verificationCode);
         

  8. Initialize a `MultiFactorAssertion` object with the `PhoneAuthCredential`:

###  Web version 9
         
         const multiFactorAssertion = PhoneMultiFactorGenerator.assertion(cred);
         

###  Web version 8
         
         var multiFactorAssertion = firebase.auth.PhoneMultiFactorGenerator.assertion(cred);
         

  9. Call `resolver.resolveSignIn()` to complete secondary authentication. You can then access the original sign-in result, which includes the standard provider-specific data and authentication credentials:

###  Web version 9
         
         // Complete sign-in. This will also trigger the Auth state listeners.
         resolver.resolveSignIn(multiFactorAssertion)
             .then(function (userCredential) {
                 // userCredential will also contain the user, additionalUserInfo, optional
                 // credential (null for email/password) associated with the first factor sign-in.
         
                 // For example, if the user signed in with Google as a first factor,
                 // userCredential.additionalUserInfo will contain data related to Google
                 // provider that the user signed in with.
                 // - user.credential contains the Google OAuth credential.
                 // - user.credential.accessToken contains the Google OAuth access token.
                 // - user.credential.idToken contains the Google OAuth ID token.
             });
         

###  Web version 8
         
         // Complete sign-in. This will also trigger the Auth state listeners.
         resolver.resolveSignIn(multiFactorAssertion)
           .then(function(userCredential) {
             // userCredential will also contain the user, additionalUserInfo, optional
             // credential (null for email/password) associated with the first factor sign-in.
             // For example, if the user signed in with Google as a first factor,
             // userCredential.additionalUserInfo will contain data related to Google provider that
             // the user signed in with.
             // user.credential contains the Google OAuth credential.
             // user.credential.accessToken contains the Google OAuth access token.
             // user.credential.idToken contains the Google OAuth ID token.
           });
         




The code below shows a complete example of signing in a multi-factor user:

###  Web version 9
    
    
    import {
        getAuth,
        getMultiFactorResolver,
        PhoneAuthProvider,
        PhoneMultiFactorGenerator,
        RecaptchaVerifier,
        signInWithEmailAndPassword
    } from "firebase/auth";
    
    const recaptchaVerifier = new RecaptchaVerifier(getAuth(),
        'recaptcha-container-id', undefined);
    
    const auth = getAuth();
    signInWithEmailAndPassword(auth, email, password)
        .then(function (userCredential) {
            // User is not enrolled with a second factor and is successfully
            // signed in.
            // ...
        })
        .catch(function (error) {
            if (error.code == 'auth/multi-factor-auth-required') {
                const resolver = getMultiFactorResolver(auth, error);
                // Ask user which second factor to use.
                if (resolver.hints[selectedIndex].factorId ===
                    PhoneMultiFactorGenerator.FACTOR_ID) {
                    const phoneInfoOptions = {
                        multiFactorHint: resolver.hints[selectedIndex],
                        session: resolver.session
                    };
                    const phoneAuthProvider = new PhoneAuthProvider(auth);
                    // Send SMS verification code
                    return phoneAuthProvider.verifyPhoneNumber(phoneInfoOptions, recaptchaVerifier)
                        .then(function (verificationId) {
                            // Ask user for the SMS verification code. Then:
                            const cred = PhoneAuthProvider.credential(
                                verificationId, verificationCode);
                            const multiFactorAssertion =
                                PhoneMultiFactorGenerator.assertion(cred);
                            // Complete sign-in.
                            return resolver.resolveSignIn(multiFactorAssertion)
                        })
                        .then(function (userCredential) {
                            // User successfully signed in with the second factor phone number.
                        });
                } else if (resolver.hints[selectedIndex].factorId ===
                           TotpMultiFactorGenerator.FACTOR_ID) {
                    // Handle TOTP MFA.
                    // ...
                } else {
                    // Unsupported second factor.
                }
            } else if (error.code == 'auth/wrong-password') {
                // Handle other errors such as wrong password.
            }
        });
    

###  Web version 8
    
    
    var resolver;
    firebase.auth().signInWithEmailAndPassword(email, password)
      .then(function(userCredential) {
        // User is not enrolled with a second factor and is successfully signed in.
        // ...
      })
      .catch(function(error) {
        if (error.code == 'auth/multi-factor-auth-required') {
          resolver = error.resolver;
          // Ask user which second factor to use.
          if (resolver.hints[selectedIndex].factorId ===
              firebase.auth.PhoneMultiFactorGenerator.FACTOR_ID) {
            var phoneInfoOptions = {
              multiFactorHint: resolver.hints[selectedIndex],
              session: resolver.session
            };
            var phoneAuthProvider = new firebase.auth.PhoneAuthProvider();
            // Send SMS verification code
            return phoneAuthProvider.verifyPhoneNumber(phoneInfoOptions, recaptchaVerifier)
              .then(function(verificationId) {
                // Ask user for the SMS verification code.
                var cred = firebase.auth.PhoneAuthProvider.credential(
                    verificationId, verificationCode);
                var multiFactorAssertion =
                    firebase.auth.PhoneMultiFactorGenerator.assertion(cred);
                // Complete sign-in.
                return resolver.resolveSignIn(multiFactorAssertion)
              })
              .then(function(userCredential) {
                // User successfully signed in with the second factor phone number.
              });
          } else if (resolver.hints[selectedIndex].factorId ===
            firebase.auth.TotpMultiFactorGenerator.FACTOR_ID) {
            // Handle TOTP MFA.
            // ...
          } else {
            // Unsupported second factor.
          }
        } else if (error.code == 'auth/wrong-password') {
          // Handle other errors such as wrong password.
        } ...
      });
    

Congratulations! You successfully signed in a user using multi-factor authentication.

## What's next

  * [Manage multi-factor users](https://docs.cloud.google.com/identity-platform/docs/admin/manage-mfa-users) programmatically with the Admin SDK.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
