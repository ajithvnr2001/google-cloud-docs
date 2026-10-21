---
url: https://docs.cloud.google.com/identity-platform/docs/work-with-mfa-users/
title: Working with multi-factor users \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:49:18.884207+00:00
---

# Working with multi-factor users  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/work-with-mfa-users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Working with multi-factor users 

This document shows you how to perform common tasks with Identity Platform users enrolled in multi-factor authentication.

## Updating a user's email

Multi-factor users must always have a verified email address. This prevents malicious actors from registering for your app with an email they don't own, and then locking out the real owner by adding a second factor.

To update a user's email, use the `verifyBeforeUpdateEmail()` method. Unlike `updateEmail()`, this method requires the user to follow a verification link before Identity Platform updates their email address. For example:

###  Web version 8 
    
    
    var user = firebase.auth().currentUser;
    user.verifyBeforeUpdateEmail(newEmail).then(function() {
      // Email sent.
      // User must click the email link before the email is updated.
    }).catch(function(error) {
      // An error happened.
    });
    

###  Web version 9 
    
    
    import { getAuth, verifyBeforeUpdateEmail } from "firebase/auth";
    
    const auth = getAuth(firebaseApp);
    verifyBeforeUpdateEmail(auth.currentUser, newEmail).then(() => {
      // Email sent.
      // User must click the email link before the email is updated.
    }).catch((error) => {
      // An error happened.
    });
    

###  iOS 
    
    
    let user = Auth.auth().currentUser
    user.verifyBeforeUpdateEmail(newEmail, completion: { (error) in
      if error != nil {
        // An error happened.
      }
      // Email sent.
      // User must click the email link before the email is updated.
    })
    

###  Android 
    
    
    FirebaseUser user = FirebaseAuth.getInstance().getCurrentUser();
    user.verifyBeforeUpdateEmail(newEmail)
       .addOnCompleteListener(
          new OnCompleteListener<Void>() {
           @Override
           public void onComplete(@NonNull Task<Void> task) {
             if (task.isSuccessful()) {
              // Email sent.
              // User must click the email link before the email is updated.
             } else {
              // An error occurred.
             }
           }
          });
    

By default, Identity Platform sends the user an email, and provides a simple, web-based handler to process the verification. There are a few ways you can customize this flow.

### Localizing the verification emails

To localize the emails sent by Identity Platform, set the language code before calling `verifyBeforeUpdateEmail()`:

###  Web version 8 
    
    
    firebase.auth().languageCode = 'fr';
    

###  Web version 9 
    
    
    import { getAuth } from "firebase/auth";
    
    const auth = getAuth();
    auth.languageCode = 'fr';
    

###  iOS 
    
    
    Auth.auth().languageCode = 'fr';
    

###  Android 
    
    
    FirebaseAuth.getInstance().setLanguageCode("fr");
    

### Passing additional state

You can use action code settings to include additional state in the verification email, or handle verification from a mobile app. For example:

###  Web version 8 
    
    
    var user = firebase.auth().currentUser;
    var actionCodeSettings = {
      url: 'https://www.example.com/completeVerification?state=*****',
      iOS: {
        bundleId: 'com.example.ios'
      },
      android: {
        packageName: 'com.example.android',
        installApp: true,
        minimumVersion: '12'
      },
      handleCodeInApp: true,
      // When multiple custom dynamic link domains are defined, specify which
      // one to use.
      dynamicLinkDomain: "example.page.link"
    };
    user.verifyBeforeUpdateEmail(newEmail, actionCodeSettings).then(function() {
      // Email sent.
      // User must click the email link before the email is updated.
    }).catch(function(error) {
      // An error happened.
    });
    

###  Web version 9 
    
    
    import { getAuth, verifyBeforeUpdateEmail } from "firebase/auth";
    
    const auth = getAuth(firebaseApp);
    const user = auth.currentUser
    const actionCodeSettings = {
      url: 'https://www.example.com/completeVerification?state=*****',
      iOS: {
        bundleId: 'com.example.ios'
      },
      android: {
        packageName: 'com.example.android',
        installApp: true,
        minimumVersion: '12'
      },
      handleCodeInApp: true,
      // When multiple custom dynamic link domains are defined, specify which
      // one to use.
      dynamicLinkDomain: "example.page.link"
    };
    
      verifyBeforeUpdateEmail(auth.currentUser, newEmail, actionCodeSettings).then(() => {
        // Email sent.
        // User must click the email link before the email is updated.
      }).catch((error) => {
        // An error happened.
      })
    

###  iOS 
    
    
    var actionCodeSettings = ActionCodeSettings.init()
    actionCodeSettings.canHandleInApp = true
    let user = Auth.auth().currentUser()
    actionCodeSettings.URL =
        String(format: "https://www.example.com/?email=%@", user.email)
    actionCodeSettings.iOSbundleID = Bundle.main.bundleIdentifier!
    actionCodeSettings.setAndroidPakageName("com.example.android",
                                             installIfNotAvailable:true,
                                             minimumVersion:"12")
    // When multiple custom dynamic link domains are defined, specify which one to use.
    actionCodeSettings.dynamicLinkDomain = "example.page.link"
    user.sendEmailVerification(withActionCodeSettings:actionCodeSettings { error in
      if error != nil {
        // Error occurred. Inspect error.code and handle error.
        return
      }
      // Email verification sent.
    })
    user.verifyBeforeUpdateEmail(newEmail, actionCodeSettings, completion: { (error) in
      if error != nil {
        // An error happened.
      }
      // Email sent.
      // User must click the email link before the email is updated.
    })
    

###  Android 
    
    
    ActionCodeSettings actionCodeSettings =
        ActionCodeSettings.newBuilder()
           .setUrl("https://www.example.com/completeVerification?state=*****")
           .setHandleCodeInApp(true)
           .setAndroidPackageName(
             "com.example.android",
             /* installIfNotAvailable= */ true,
             /* minimumVersion= */ null)
           .setIOSBundleId("com.example.ios")
           // When multiple custom dynamic link domains are defined, specify
           // which one to use.
           .setDynamicLinkDomain("example.page.link")
           .build();
    FirebaseUser multiFactorUser = FirebaseAuth.getInstance().getCurrentUser();
    multiFactorUser
       .verifyBeforeUpdateEmail(newEmail, actionCodeSettings)
       .addOnCompleteListener(
          new OnCompleteListener<Void>() {
           @Override
           public void onComplete(@NonNull Task<Void> task) {
             if (task.isSuccessful()) {
              // Email sent.
              // User must click the email link before the email is updated.
             } else {
              // An error occurred.
             }
           }
          });
    

### Customizing the verification handler

You can create your own handler to process email verification. The following example shows how to check an action code and inspect its metadata before applying it:

###  Web version 8 
    
    
    var email;
    firebase.auth().checkActionCode(actionCode)
      .then(function(info) {
        // Operation is equal to
        // firebase.auth.ActionCodeInfo.Operation.VERIFY_AND_CHANGE_EMAIL
        var operation = info['operation'];
        // This is the old email.
        var previousEmail = info['data']['previousEmail'];
        // This is the new email the user is changing to.
        email = info['data']['email'];
        // TODO: Display a message to the end user that the email address of the account is
        // going to be changed from `fromEmail` to `email`
        // …
        // On confirmation.
        return firebase.auth().applyActionCode(actionCode)
      }).then(function() {
        // Confirm to the end user the email was updated.
        showUI('You can now sign in with your new email: ' + email);
      })
      .catch(function(error) {
        // Error occurred during confirmation. The code might have expired or the
        // link has been used before.
      });
    

###  Web version 9 
    
    
    import { getAuth,  checkActionCode, applyActionCode} from "firebase/auth";
    
    const auth = getAuth(firebaseApp);
    var email;
    checkActionCode(auth, actionCode)
      .then((info) => {
        // Operation is equal to
        // ActionCodeOperation.VERIFY_AND_CHANGE_EMAIL
        const operation = info['operation'];
        // This is the old email.
        const previousEmail = info['data']['previousEmail'];
        // This is the new email the user is changing to.
        email = info['data']['email'];
        // TODO: Display a message to the end user that the email address of the account is
        // going to be changed from `fromEmail` to `email`
        // …
        // On confirmation.
        return applyActionCode(auth, actionCode)
      }).then(() => {
        // Confirm to the end user the email was updated.
        showUI('You can now sign in with your new email: ' + email);
      })
      .catch((error) => {
        // Error occurred during confirmation. The code might have expired or the
        // link has been used before.
      });
    

###  iOS 
    
    
    Auth.auth().checkActionCode(actionCode) { info, error in
      if error != nil {
        // Error occurred during confirmation. The code might have expired or the
        // link has been used before.
        return
      }
      // This is the new email the user is changing to.
      let email = info?.email
      // This is the old email.
      let oldEmail = info?.previousEmail
      // operation is equal to
      // firebase.auth.ActionCodeInfo.Operation.VERIFY_AND_CHANGE_EMAIL
      let operation = info?.operation
      // TODO: Display a message to the end user that the email address of the account is
      // going to be changed from `fromEmail` to `email`
      // …
      // On confirmation.
      return Auth.auth().applyActionCode(actionCode)
    }
    

###  Android 
    
    
    FirebaseAuth.getInstance().checkActionCode(actionCode).addOnCompleteListener(
      new OnCompleteListener<ActionCodeResult>() {
        @Override
        public void onComplete(@NonNull Task<ActionCodeResult> task) {
          if (!task.isSuccessful()) {
            // Error occurred during confirmation. The code might have expired or the
            // link has been used before.
            return;
          }
          ActionCodeResult result = task.getResult();
    
          // This maps to VERIFY_AND_CHANGE_EMAIL.
          int operation = result.getOperation();
    
          if (operation == ActionCodeResult.VERIFY_AND_CHANGE_EMAIL) {
            ActionCodeEmailInfo actionCodeInfo =
                (ActionCodeEmailInfo) result.getInfo();
    
            String fromEmail = actionCodeInfo.getFromEmail();
            String email = actionCodeInfo.getEmail();
            // TODO: Display a message to the user that the email address
            // of the account is changing from `fromEmail` to `email` once
            // they confirm.
          }
        }
      });
    

To learn more, see the Firebase documentation on [Creating custom email action handlers](https://firebase.google.com/docs/auth/custom-email-handler).

## Re-authenticating a user

Even if a user is already signed in, you might want to re-authenticate them before performing sensitive operations, such as:

  * Changing a password.
  * Adding or removing a new second factor.
  * Updating personal information (like an address).
  * Executing financial transactions.
  * Deleting a user's account.



To re-authenticate a user with an email and password:

###  Web 
    
    
    var resolver;
    var credential = firebase.auth.EmailAuthProvider.credential(
        firebase.auth().currentUser.email, password);
    firebase.auth().currentUser.reauthenticateWithCredential(credential)
      .then(function(userCredential) {
        // User successfully re-authenticated and does not require a second factor challenge.
        // ...
      })
      .catch(function(error) {
        if (error.code == 'auth/multi-factor-auth-required') {
          // Handle multi-factor authentication.
        } else {
          // Handle other errors.
        }
      });
    

###  iOS 
    
    
    let credential = EmailAuthProvider.credential(withEmail: email, password: password)
    Auth.auth().currentUser.reauthenticate(with: credential, completion: { (result, error) in
      let authError = error as NSError?
      if (authError == nil || authError!.code != AuthErrorCode.secondFactorRequired.rawValue) {
        // User is not enrolled with a second factor or is successfully signed in.
      } else {
        // Handle multi-factor authentication.
      }
    })
    

###  Android 
    
    
    FirebaseUser user = FirebaseAuth.getInstance().getCurrentUser();
    AuthCredential credential = EmailAuthProvider.getCredential(user.getEmail(), password);
    user.reauthenticate(credential)
       .addOnCompleteListener(
          new OnCompleteListener<AuthResult>() {
           @Override
           public void onComplete(@NonNull Task<AuthResult> task) {
             if (task.isSuccessful()) {
              // User successfully re-authenticated and does not
              // require a second factor challenge.
              // ...
              return;
             }
             if (task.getException() instanceof FirebaseAuthMultiFactorException) {
               // Handle multi-factor authentication.
             } else {
              // Handle other errors.
             }
           }
          });
    

To re-authenticate using an OAuth provider, such as Microsoft:

###  Web 
    
    
    var resolver;
    var user = firebase.auth().currentUser;
    // Ask the user to re-authenticate with Microsoft.
    var provider = new firebase.auth.OAuthProvider('microsoft.com');
    // Microsoft provider allows the ability to provide a login_hint.
    provider.setCustomParameters({
      login_hint: user.email
    });
    user.reauthenticateWithPopup(provider)
      .then(function(userCredential) {
        // User successfully re-authenticated and does not require a second factor challenge.
        // ...
      })
      .catch(function(error) {
        if (error.code == 'auth/multi-factor-auth-required') {
          // Handle multi-factor authentication.
        } else {
          // Unsupported second factor.
        } else {
          // Handle other errors.
        }
      });
    

###  iOS 
    
    
    var provider = OAuthProvider(providerID: "microsoft.com")
      // Replace nil with the custom class that conforms to AuthUIDelegate
      // you created in last step to use a customized web view.
      provider.getCredentialWith(nil) { credential, error in
        Auth.auth().currentUser.reauthenticate(with: credential, completion: { (result, error) in
          let authError = error as NSError?
          if (authError == nil || authError!.code != AuthErrorCode.secondFactorRequired.rawValue) {
            // User is not enrolled with a second factor or is successfully signed in.
            // ...
          } else {
            // Handle multi-factor authentication.
          }
        }
      })
    

###  Android 
    
    
    FirebaseUser user = FirebaseAuth.getInstance().getCurrentUser();
    OAuthProvider.Builder provider = OAuthProvider.newBuilder("microsoft.com");
    provider.addCustomParameter("login_hint", user.getEmail());
    user.startActivityForReauthenticateWithProvider(/* activity= */ this, provider.build())
       .addOnCompleteListener(
          new OnCompleteListener<AuthResult>() {
           @Override
           public void onComplete(@NonNull Task<AuthResult> task) {
             if (task.isSuccessful()) {
              // User successfully re-authenticated and does not
              // require a second factor challenge.
              // ...
              return;
             }
             if (task.getException() instanceof FirebaseAuthMultiFactorException) {
               // Handle multi-factor authentication.
             } else {
              // Handle other errors such as wrong password.
             }
           }
          });
    

## Revoking a recently-added second factor

When a user enrolls a second factor, Identity Platform sends a notification to their email. To protect against unauthorized activity, the email includes an option to reverse the addition of a second factor.

Identity Platform provides a default email template and handler, but you can also build your own. The following example shows how to create a custom handler:

###  Web version 8 
    
    
    var obfuscatedPhoneNumber;
    firebase.auth().checkActionCode(actionCode)
      .then(function(info) {
        // operation is equal to
        // firebase.auth.ActionCodeInfo.Operation.REVERT_SECOND_FACTOR_ADDITION
        var operation = info['operation'];
        // info.data.multiFactorInfo contains the data corresponding to the
        // enrolled second factor that the user is revoking.
        var multiFactorInfo = info['data']['multiFactorInfo'];
        obfuscatedPhoneNumber = multiFactorInfo['phoneNumber'];
        var displayName = multiFactorInfo['displayName'];
        // TODO: Display a message to the end user about the second factor that
        // was enrolled before the user can confirm the action to revert it.
        // ...
        // On confirmation.
        return firebase.auth().applyActionCode(actionCode)
      }).then(function() {
        // Confirm to the end user the phone number was removed from the account.
        showUI('The phone number ' + obfuscatedPhoneNumber +
             ' has been removed as a second factor from your account.' +
             ' You may also want to reset your password if you suspect' +
             ' your account was compromised.');
      })
      .catch(function(error) {
        // Error occurred during confirmation. The code might have expired or the
        // link has been used before.
      });
    

###  Web version 9 
    
    
    const {
      getAuth,
      checkActionCode,
      applyActionCode
    } = require("firebase/auth");
    
    const auth = getAuth(firebaseApp);
    var obfuscatedPhoneNumber;
    checkActionCode(auth, actionCode)
      .then((info) => {
        // Operation is equal to
        // ActionCodeOperation.REVERT_SECOND_FACTOR_ADDITION
        const operation = info['operation'];
        // info.data.multiFactorInfo contains the data corresponding to the
        // enrolled second factor that the user is revoking.
        var multiFactorInfo = info['data']['multiFactorInfo'];
        obfuscatedPhoneNumber = multiFactorInfo['phoneNumber'];
        const displayName = multiFactorInfo['displayName'];
        // TODO: Display a message to the end user about the second factor that
        // was enrolled before the user can confirm the action to revert it.
        // ...
        // On confirmation.
        return applyActionCode(auth, actionCode)
      }).then(() => {
        // Confirm to the end user the phone number was removed from the account.
        showUI('The phone number ' + obfuscatedPhoneNumber +
             ' has been removed as a second factor from your account.' +
             ' You may also want to reset your password if you suspect' +
             ' your account was compromised.');
      })
      .catch((error) => {
        // Error occurred during confirmation. The code might have expired or the
        // link has been used before.
      });
    

###  iOS 
    
    
    Auth.auth().checkActionCode(actionCode) { info, error in
      if error != nil {
        // Error occurred during confirmation. The code might have expired or the
        // link has been used before.
        return
      }
      // This is the new email the user is changing to.
      let email = info?.email
      // This is the old email.
      let oldEmail = info?.previousEmail
      // operation is equal to
      // firebase.auth.ActionCodeInfo.Operation.REVERT_SECOND_FACTOR_ADDITION
      let operation = info?.operation
      // info.multiFactorInfo contains the data corresponding to the enrolled second
      // factor that the user is revoking.
      let multiFactorInfo = info?.multiFactorInfo
      let obfuscatedPhoneNumber = (multiFactorInfo as! PhoneMultiFactorInfo).phone
      // TODO: Display a message to the end user that the email address of the account is
      // going to be changed from `fromEmail` to `email`
      // …
      // On confirmation.
      return Auth.auth().applyActionCode(actionCode)
    }
    

###  Android 
    
    
    FirebaseAuth.getInstance()
      .checkActionCode(actionCode)
      .continueWithTask(
          new Continuation<ActionCodeResult, Task<Void>>() {
            @Override
            public Task<Void> then(Task<ActionCodeResult> task) throws Exception {
              if (!task.isSuccessful()) {
                // Error occurred during confirmation. The code might have expired
                // or the link has been used before.
                return Tasks.forException(task.getException());
              }
              ActionCodeResult result = task.getResult();
              // The operation is equal to ActionCodeResult.REVERT_SECOND_FACTOR_ADDITION.
              int operation = result.getOperation();
              // The ActionCodeMultiFactorInfo contains the data corresponding to
              // the enrolled second factor that the user is revoking.
              ActionCodeMultiFactorInfo actionCodeInfo =
                  (ActionCodeMultiFactorInfo) result.getInfo();
              PhoneMultiFactorInfo multiFactorInfo =
                  (PhoneMultiFactorInfo) actionCodeInfo.getMultiFactorInfo();
              String obfuscatedPhoneNumber = multiFactorInfo.getPhoneNumber();
              String displayName = multiFactorInfo.getDisplayName();
              // We can now display a message to the end user about the second
              // factor that was enrolled before they confirm the action to revert
              // it.
              // ...
              // On user confirmation:
              return FirebaseAuth.getInstance().applyActionCode(actionCode);
            }
          })
      .addOnCompleteListener(
          new OnCompleteListener<Void>() {
            @Override
            public void onComplete(Task<Void> task) {
              if (task.isSuccessful()) {
                // Display a message to the user that the second factor
                // has been reverted.
              }
            }
          });
    

To learn more, see the Firebase documentation on [Creating custom email action handlers](https://firebase.google.com/docs/auth/custom-email-handler).

## Recovering a second factor

Identity Platform does not provide a built-in mechanism for recovering second factors. If a user loses access to their second factor, they will be locked out of their account. To prevent this from happening, consider the following:

  * Warning users that they will lose access to their account without their second factor.
  * Strongly encouraging users to register a backup secondary factor.
  * Using the [Admin SDK](https://docs.cloud.google.com/identity-platform/docs/admin/manage-mfa-users#updating_a_user) to build a recovery flow that disables multi-factor authentication if the user can sufficiently verify their identity (for example, by uploading a recovery key or answering personal questions).
  * Granting your support team the ability to manage user accounts (including removing second factors), and provide an option for users to contact them if they are locked out of their account.



Password reset will not allow a user to bypass multi-factor authentication. If you reset a user's password using `sendPasswordResetEmail()`, they will still be required to pass the multi-factor challenge upon signing in with their new password.

## Unenrolling a second factor

To unenroll a second factor, get it from the list of the user's enrolled factors, then call `unenroll()`. Since this is a sensitive operation, you'll need to re-authenticate the user first if they haven't signed in recently.

###  Web version 8 
    
    
    var options = user.multiFactor.enrolledFactors;
    // Ask user to select from the enrolled options.
    return user.multiFactor.unenroll(options[selectedIndex])
      .then(function() {
        // User successfully unenrolled selected factor.
      });
    

###  Web version 9 
    
    
    const multiFactorUser = multiFactor(auth.currentUser);
    const options = multiFactorUser.enrolledFactors
    // Ask user to select from the enrolled options.
    return multiFactorUser.unenroll(options[selectedIndex])
      .then(() =>
        // User successfully unenrolled selected factor.
      });
    

###  iOS 
    
    
    // Ask user to select from the enrolled options.
    user?.multiFactor.unenroll(with: (user?.multiFactor.enrolledFactors[selectedIndex])!,
      completion: { (error) in
        // ...
    })
    

###  Android 
    
    
    List<MultiFactorInfo> options = user.getMultiFactor().getEnrolledFactors();
    // Ask user to select from the enrolled options.
    user.getMultiFactor()
       .unenroll(options.get(selectedIndex))
       .addOnCompleteListener(
          new OnCompleteListener<Void>() {
           @Override
           public void onComplete(@NonNull Task<Void> task) {
             if (task.isSuccessful()) {
              // Successfully un-enrolled.
             }
           }
          });
    

In some cases, the user may be signed out after removing a second factor. Use `onAuthStateChanged()` to listen for this case, and ask the user to sign in again.

## What's next

  * Add multi-factor authentication to your [web](https://docs.cloud.google.com/identity-platform/docs/web/mfa), [iOS](https://docs.cloud.google.com/identity-platform/docs/ios/mfa), or [Android](https://docs.cloud.google.com/identity-platform/docs/android/mfa) app.

  * Manage multi-factor users [programmatically](https://docs.cloud.google.com/identity-platform/docs/admin/manage-mfa-users).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
