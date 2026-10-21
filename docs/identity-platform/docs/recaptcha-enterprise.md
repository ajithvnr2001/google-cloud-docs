---
url: https://docs.cloud.google.com/identity-platform/docs/recaptcha-enterprise/
title: Integrate Identity Platform with the reCAPTCHA Enterprise API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:49:23.262202+00:00
---

# Integrate Identity Platform with the reCAPTCHA Enterprise API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/recaptcha-enterprise/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Identity Platform with the reCAPTCHA Enterprise API

This document shows you how to use the Identity Platform integration with the reCAPTCHA Enterprise API to enhance security for your users. This feature makes your app more resilient against spam, abuse, and other fraudulent activity.

The integration creates a reCAPTCHA Enterprise assessment on your behalf to validate user requests. For pricing information, see [reCAPTCHA pricing](https://cloud.google.com/recaptcha-enterprise/pricing).

## Overview

When you set up the Identity Platform integration with the reCAPTCHA Enterprise API, you enable reCAPTCHA's default protection feature—reCAPTCHA bot protection. With bot protection, Identity Platform provisions score-based reCAPTCHA keys in your project on your behalf. When a user accesses your app or site using any of the following operations, the client SDK loads reCAPTCHA when the corresponding provider is enabled.

Provider | Operation | Method  
---|---|---  
`passwordProvider` | Email and password sign-in | `signInWithPassword`  
Email and password sign-up | `signUpPassword`  
Email link sign-in | `getOobCode`  
Password reset | `getOobCode`  
`phoneProvider` | Phone number sign-up or sign-in | `sendVerificationCode`  
MFA phone number enrollment | `mfaSmsEnrollment`  
MFA phone number sign-in | `mfaSmsSignIn` |   
  
reCAPTCHA then provides Identity Platform with scores that assess the risk of the request based on your configuration and risk tolerance.

For more information, see [Overview of reCAPTCHA](https://docs.cloud.google.com/recaptcha-enterprise/docs/overview).

**Important:** In this document, you use the following billable components of Google Cloud: 

  * reCAPTCHA Enterprise
  * Identity Platform

To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

Based on the type of authentication flow you want to protect with reCAPTCHA, ensure that you've set up the following:

  * For email-password authentication flows, ensure that you have configured [email sign-in for users](https://docs.cloud.google.com/identity-platform/docs/quickstart-email-password).
  * For SMS-based authentication flows, ensure that you have onboarded to at least one of the following:

    * [Phone sign-in for users](https://docs.cloud.google.com/identity-platform/docs/sign-in-user-phone).
    * Multi-factor authentication for your [web](https://docs.cloud.google.com/identity-platform/docs/web/mfa), [Android](https://docs.cloud.google.com/identity-platform/docs/android/mfa), or [iOS](https://docs.cloud.google.com/identity-platform/docs/ios/mfa) app.



### Create a service account

The Identity Platform integration with the reCAPTCHA Enterprise API requires a Identity Platform service account for each project that will use reCAPTCHA. This allows Identity Platform to manage reCAPTCHA keys on your behalf. If you've already created a service account, grant it access to reCAPTCHA.

If you haven't already created a service account or you have additional projects that you want to protect with reCAPTCHA, do the following:

  1. Use the Google Cloud CLI to create a service account:
         
         gcloud beta services identity create \
             --service=identitytoolkit.googleapis.com \
             --project=PROJECT_ID
         

Replace `PROJECT_ID` with the project's ID.

  2. Grant the service account access to reCAPTCHA:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-identitytoolkit.iam.gserviceaccount.com \
             --role=roles/identitytoolkit.serviceAgent
         

Replace the following:

     * `PROJECT_ID`: the project ID
     * `PROJECT_NUMBER`: the project account number



## reCAPTCHA bot protection modes

reCAPTCHA bot protection has two modes that help you protect users: _audit_ and _enforce_. These modes differ in behavior based on the identity provider.

### Email-password provider

The audit and enforce modes behave as follows for email-password authentication flows.

#### Audit mode

When you set email-password enforcement to audit mode, Identity Platform creates one or more reCAPTCHA keys in your project that are used to assess traffic to Identity Platform APIs without blocking any requests. Use the metrics that are emitted during audit mode to determine if you should enable reCAPTCHA enforcement.

#### Enforce mode

When you set email-password enforcement to enforce mode, Identity Platform creates one or more reCAPTCHA keys in your project that are used to assess traffic to Identity Platform APIs. API requests that don't include a reCAPTCHA token are rejected. Only enable enforcement after you've migrated all your clients to an SDK with reCAPTCHA support.

### Phone provider

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The audit and enforce modes behave as follows for phone authentication flows.

#### Audit mode

When you set phone authentication enforcement to audit mode, Identity Platform uses reCAPTCHA bot protection for app verification. If a user's request passes the toll fraud assessment, an SMS verification code is sent. If a user's request fails the toll fraud assessment and you're using the client SDK, Identity Platform triggers fallback verification methods to complete the phone authentication flow. The accepted fallback methods depend on your app's platform. 

The client SDK triggers the fallback verification methods in the following scenarios:

  * The reCAPTCHA token is missing.
  * The reCAPTCHA token is invalid or expired.
  * The reCAPTCHA token doesn't pass the score threshold.
  * reCAPTCHA is not configured correctly.



Ensure that the fallback verification methods for your app's platform are set up and ready to be triggered by the client SDK if necessary.

### Web

If the initial bot protection assessment fails, audit mode relies on reCAPTCHA v2 for verification. Therefore, you must set up the reCAPTCHA verifier (`RecaptchaVerifier`) and pass it to the following phone authentication operations: 

  * `verifyPhoneNumber`
  * `signInWithPhoneNumber`
  * `linkWithPhoneNumber`
  * `reauthenticateWithPhoneNumber`

Without the reCAPTCHA verifier, Identity Platform can't initiate reCAPTCHA v2 and will return `auth/argument-error`. For more information on setting up the reCAPTCHA verifier, see [Set up the reCAPTCHA verifier](https://firebase.google.com/docs/auth/web/phone-auth#set-up-the-recaptcha-verifier) in the Firebase documentation. 

### Android

If the initial bot protection assessment fails, audit mode verifies your app against the Play Integrity API. If this verification fails, reCAPTCHA v2 is triggered. reCAPTCHA v2 might be triggered in the following scenarios: 

  * If the end-user's device does not have Google Play services installed.
  * If the app is not distributed through Google Play Store (on Authentication SDK v21.2.0 and later).
  * If the obtained SafetyNet token was not valid (on Authentication SDK versions prior to v21.2.0).

For more information on setting up Android app verification, see [Enable app verification](https://firebase.google.com/docs/auth/android/phone-auth#enable-app-verification) in the Firebase documentation. 

### iOS

If the initial bot protection assessment fails, audit mode relies on silent push notifications for verification. This verification method involves sending a token to your app on the requesting device with a silent push notification. If your app successfully receives the notification, the phone authentication flow proceeds. If your app does not receive the push notification, reCAPTCHA v2 is triggered. reCAPTCHA v2 might be triggered if silent push notifications are not configured properly. 

For more information on setting up iOS app verification, see [Enable app verification](https://firebase.google.com/docs/auth/ios/phone-auth#enable-app-verification) in the Firebase documentation. 

#### Enforce mode

When you set phone authentication enforcement to enforce mode, Identity Platform uses reCAPTCHA bot protection for app verification. If a user's request passes the toll fraud assessment, an SMS verification code is sent. If a user's request fails the toll fraud assessment, Identity Platform blocks the request and doesn't send an SMS message containing a verification code.

There is no fallback verification required in enforce mode, you don't have to set up any additional verification methods for your app. However, we recommend [setting up reCAPTCHA verifier](https://firebase.google.com/docs/auth/web/phone-auth#set-up-the-recaptcha-verifier) for web apps to ensure that reCAPTCHA v2 is enabled if you decide to change your app's reCAPTCHA mode to `AUDIT` or `OFF`.

## Set up the Identity Platform integration with the reCAPTCHA Enterprise API

To set up the Identity Platform integration with the reCAPTCHA Enterprise API, you perform the following tasks:

  * Use the Admin SDK to set the reCAPTCHA enforcement state and enable bot protection.
  * Configure the client SDK for your app's platform.



We recommend that you first enable reCAPTCHA enforcement in audit mode and monitor the reCAPTCHA metrics that your project emits to ensure that authentication flows are protected appropriately. You do this so that you don't interrupt your user traffic while you audit their use of reCAPTCHA. After you verify your authentication flows are protected, then set bot protection to `ENFORCE`.

### Enable reCAPTCHA bot protection

**Important:** Don't edit or delete reCAPTCHA keys named `Key for Identity Platform integration with reCAPTCHA` unless reCAPTCHA is disabled. Doing so prevents Identity Platform from applying reCAPTCHA protection. Additionally, Identity Platform SDKs cannot generate tokens from reCAPTCHA keys that you generate on your own.

### Email-password provider

To enable reCAPTCHA bot protection for email-password authentication flows, do the following:

  1. If you haven't already done so, [enable the reCAPTCHA Enterprise API](https://docs.cloud.google.com/recaptcha/docs/prepare-environment#enable-api) on your project.

  2. To enable bot protection for a _project_ , use the Admin SDK. reCAPTCHA support is available on Node.js Admin SDK versions 11.7.0 and later.

For example:
         
         // Update project config with reCAPTCHA config
         const updateConfigRequest = {
           recaptchaConfig: {
             emailPasswordEnforcementState:  'ENFORCE_MODE',
             managedRules: [{
               endScore: END_SCORE,
               action: 'BLOCK'
             }]
           }
         };
         const updateProjectConfigWithRecaptcha = () => {
           getAuth().projectConfigManager().updateProjectConfig(updateConfigRequest).then((response) => {
             console.log('Updated reCAPTCHA config for project: ', response.recaptchaConfig);
           }).catch((error) => {
             console.log('Error updating project config:', error);
           });
         }
         

Replace the following:

     * `ENFORCE_MODE`: the mode you want to set for reCAPTCHA email-password authentication enforcement. Valid values are `OFF`, `AUDIT`, and `ENFORCE`. To enable bot protection, this parameter must be set to `AUDIT` or `ENFORCE`. When you enable bot protection for the first time, we recommend setting this parameter to `AUDIT` and ensuring your authentication flows are protected before setting this to `ENFORCE`. For more information on how the modes work, see reCAPTCHA bot protection modes.
     * `END_SCORE`: the lowest bot protection assessment score a request can have before it fails. You can set this score to be between `0.0` and `1.0`. For example, if you set a threshold of `0.6`, reCAPTCHA will fail any request with a `0.5` or lower. Therefore, the higher you set the score, the stricter the rules will be.

You can also enable bot protection with the same config method for a _tenant_ using the Admin SDK. For more information on updating a tenant, see [Update a tenant](https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-managing-tenants#updating_a_tenant).

  3. If you use Identity Platform on iOS or Android, you must register your app from the [Firebase console](https://console.firebase.google.com/):

     * For iOS, [register each bundle ID that uses Identity Platform](https://firebase.google.com/docs/ios/setup#register-app)
     * For Android, [register each Android package name that uses Identity Platform](https://firebase.google.com/docs/android/setup#register-app)

If you are using Identity Platform on the web, you must add an authorized domain for each domain that uses reCAPTCHA. To add authorized domains, do the following:

     1. In the Google Cloud console, go to the Identity Platform page.

[Go to Identity Platform](https://console.cloud.google.com/customer-identity)

     2. Go to **Settings** > **Security**.

     3. Click **Add domain**.

     4. Enter the domain name and click **Add** to save the domain.

reCAPTCHA key provisioning can take several minutes to complete.

  4. If you've set enforcement to audit mode, we recommend that you monitor the reCAPTCHA metrics for bot protection to ensure that your flows are being protected.




### Phone provider

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To enable reCAPTCHA bot protection for SMS-based authentication flows, do the following:

  1. If you haven't already done so, [enable the reCAPTCHA Enterprise API](https://docs.cloud.google.com/recaptcha/docs/prepare-environment#enable-api) on your project.

  2. To enable bot protection for a _project_ , use the Admin SDK. reCAPTCHA support is available on Node.js Admin SDK versions 12.7.0 and later.

For example:
         
         // Update project config with reCAPTCHA config
         const updateProjectConfigRequest = {
           recaptchaConfig: {
             phoneEnforcementState: 'ENFORCE_MODE',
             managedRules: [{ endScore: END_SCORE, action: 'BLOCK' }],
             useSmsBotScore: 'true',
           }
         }
         let projectConfig = await getAuth().projectConfigManager().updateProject(updateProjectConfigRequest);
         

Replace the following:

     * `ENFORCE_MODE`: the mode you want to set for reCAPTCHA phone authentication enforcement. Valid values are `OFF`, `AUDIT`, and `ENFORCE`. To enable bot protection for SMS-based flows, this parameter must be set to `AUDIT` or `ENFORCE` and `useSmsBotScore` must be set to `true`.

When enabling bot protection for the first time, we recommend setting this parameter to `AUDIT` and ensuring your authentication flows are protected before setting this to `ENFORCE`. For more information on how the modes work, see reCAPTCHA bot protection modes.

     * `END_SCORE`: the lowest bot protection assessment score a request can have before it fails. You can set this score to be between `0.0` and `1.0`. For example, if you set a threshold of `0.6`, reCAPTCHA will fail any request with a `0.5` or lower. Therefore, the higher you set the score, the stricter the rules will be.

You can also enable bot protection with the same config method for a _tenant_ using the Admin SDK. For more information on updating a tenant, see [Update a tenant](https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-managing-tenants#updating_a_tenant).

**Note:** Identity Platform does not support using phone authentication and SMS multi-factor authentication with multiple tenants on mobile platforms.
  3. If you are using Identity Platform on iOS or Android, you must register your app from the [Firebase console](https://console.firebase.google.com/):

     * For iOS, [register each bundle ID that uses Identity Platform](https://firebase.google.com/docs/ios/setup#register-app)
     * For Android, [register each Android package name that uses Identity Platform](https://firebase.google.com/docs/android/setup#register-app)

If you are using Identity Platform on the web, you must add an authorized domain for each domain that uses reCAPTCHA. To add authorized domains, do the following:

     1. In the Google Cloud console, go to the Identity Platform page.

[Go to Identity Platform](https://console.cloud.google.com/customer-identity)

     2. Go to **Settings** > **Security**.

     3. Click **Add domain**.

     4. Enter the domain name and click **Add** to save the domain.

reCAPTCHA key provisioning can take several minutes to complete.

  4. If you've set enforcement to audit mode, we recommend that you monitor the reCAPTCHA metrics for bot protection to ensure that your flows are being protected.




### Configure the client SDK

Configure the client SDK according to your app's platform.

###  Web 

  1. Update to the [latest version of the web SDK](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade).

     * reCAPTCHA support for _email and password authentication_ in web apps is available on JavaScript SDK versions 9.20.0 and later.
     * reCAPTCHA support for _phone authentication_ in web apps is available on JavaScript SDK versions 11 and later.

After you've integrated the web SDK with your app, the SDK automatically fetches your reCAPTCHA configuration and enables protection for the providers you've configured.

  2. If needed, you can force fetch the reCAPTCHA signal as follows:
         
         import { initializeRecaptchaConfig } from '@firebase/auth';
         
         // Initialize Firebase Authentication
         const auth = getAuth();
         initializeRecaptchaConfig(auth)
           .then(() => {
             console.log("Recaptcha Enterprise Config Initialization successful.")
           })
           .catch((error) => {
             console.error("Recaptcha Enterprise Config Initialization failed with " + error)
           });
         




###  Android 

  1. Update to the latest version of the Android SDK. reCAPTCHA support for email and password authentication and phone authentication in Android apps is available on [Android SDK version 23.1.0 and later](https://firebase.google.com/support/release-notes/android#auth_v23-1-0).

In addition, reCAPTCHA support requires API level 23 (Marshmallow) or higher and Android 6 or higher.

After you've integrated the Android SDK with your app, the SDK automatically fetches your reCAPTCHA configuration and enables protection for the providers you've configured.

  2. Add the following build rule to the dependencies section of your app-level `build.gradle` file:
         
         implementation 'com.google.android.recaptcha:recaptcha:18.5.1'
         

Make sure to use reCAPTCHA SDK version 18.5.1 or later.

  3. If needed, you can force fetch the reCAPTCHA signal as follows:

     * Kotlin:
    
    // Initialize Firebase Authentication
    auth = Firebase.auth
    
    auth.initializeRecaptchaConfig().addOnCompleteListener(this) { task ->
        if (task.isSuccessful) {
            Log.d(TAG, "Recaptcha Enterprise Initialization successful.")
        } else {
            Log.w(TAG, "Recaptcha Enterprise Initialization failed.")
        }
    }
    

     * Java:
    
    // Initialize Firebase Authentication
    auth = FirebaseAuth.getInstance();
    auth.initializeRecaptchaConfig().addOnCompleteListener(
      this, new OnCompleteListener<void>() {
      @Override
      public void onComplete(@NonNull Task<void> task) {
        if (task.isSuccessful()) {
          Log.d(TAG, "Recaptcha Enterprise Initialization successful.");
        } else {
          Log.w(TAG, "Recaptcha Enterprise Initialization failed.");
        }
      }
    });
    




###  iOS 

  1. Update to [iOS SDK version 11.6.0 or later](https://firebase.google.com/support/release-notes/ios#11.6.0). After you've integrated the iOS SDK with your app, the SDK automatically fetches your reCAPTCHA configuration and enables protection for the providers you've configured.

  2. To integrate reCAPTCHA iOS SDK to your app, see [Prepare your environment](https://docs.cloud.google.com/recaptcha-enterprise/docs/instrument-ios-apps#prepare_your_environment).

  3. Ensure that `-ObjC` is listed in your linker flags. Navigate to **Target** > **Build Settings** > **All** > **Linking** and verify that `Other Linker Flags` shows `-ObjC`.

  4. If needed, you can force fetch the reCAPTCHA signal as follows:

     * Swift:
    
    // Initialize Firebase Authentication
    try await Auth.auth().initializeRecaptchaConfig()
    

     * Objective-C:
    
    // Initialize Firebase Authentication
    [[FIRAuth auth] initializeRecaptchaConfigWithCompletion:^(NSError * _Nullable error) {
      // Firebase Authentication initialization finished
    }];
    




### Monitor reCAPTCHA metrics for bot protection

Before you set the reCAPTCHA enforcement to enforce mode, we recommend you use audit mode and monitor the reCAPTCHA metrics your project emits to ensure that authentication flows are protected. For example, these metrics can help you determine if you've set up the Identity Platform integration with the reCAPTCHA Enterprise API correctly. They can also help you fine-tune your score threshold for your user traffic. If reCAPTCHA key provisioning fails or if required service accounts weren't created, reCAPTCHA authentication attempts still succeed normally.

Ensure that reCAPTCHA authentication is working by examining the following metrics your project emits to Cloud Monitoring:

  * [`identitytoolkit.googleapis.com/recaptcha/verdict_count`](https://docs.cloud.google.com/identity-platform/docs/recaptcha-metrics#verdict-count): Tracks the different verdicts returned by reCAPTCHA.
  * [`identitytoolkit.googleapis.com/recaptcha/token_count`](https://docs.cloud.google.com/identity-platform/docs/recaptcha-metrics#token-count): Tracks the number and status of reCAPTCHA tokens received by the Identity Platform backend.
  * [`identitytoolkit.googleapis.com/recaptcha/risk_scores`](https://docs.cloud.google.com/identity-platform/docs/recaptcha-metrics#bot-risk-scores): Tracks the bot protection score distribution.



For more information, see [Monitor reCAPTCHA metrics](https://docs.cloud.google.com/identity-platform/docs/recaptcha-metrics).

### Enforce reCAPTCHA bot protection

After you verify that your app is receiving acceptable user traffic, you can enable reCAPTCHA enforcement to protect your users. Ensure you don't disrupt existing users, including users who may be using an older version of your app.

### Email-password provider

To enable reCAPTCHA enforcement for email-password authentication flows on a project or tenant, use the Admin SDK to run the following:
    
    
    const enforceRequest = {
      recaptchaConfig: {
        emailPasswordEnforcementState:  'ENFORCE',
        }]
      }
    };
    

### Phone provider

To enable reCAPTCHA enforcement for SMS-based authentication flows on a project or tenant, use the Admin SDK to run the following:
    
    
    const enforceRequest = {
      recaptchaConfig: {
        phoneEnforcementState:  'ENFORCE',
        useSmsBotScore: 'true'
        }]
      }
    };
    

### Disable reCAPTCHA bot protection

### Email-password provider

To disable bot protection for email-password authentication flows, use the Admin SDK to run the following command:
    
    
    const disableRequest = {
      recaptchaConfig: {
        emailPasswordEnforcementState:  'OFF',
      }
    };
    

### Phone provider

To disable bot protection for SMS-based authentication flows, use the Admin SDK to run the following command:
    
    
    const disableRequest = {
      recaptchaConfig: {
        phoneEnforcementState:  'OFF',
        useSmsBotScore: 'false'
      }
    };
    

## Override reCAPTCHA verdicts with Cloud Run functions

In addition to configuring score thresholds, you can override a reCAPTCHA verdict for a given token by using blocking functions to allow or block flows based on custom factors. This is helpful in cases where a reCAPTCHA score for a given user login might be low, but the user is trusted or has been verified through other means and is therefore allowed to complete the sign-in.

The following example shows how to override a reCAPTCHA verdict by using blocking functions:

###  Node.js 
    
    
      const functions = require("firebase-functions/v1");
      exports.beforesmsv1 = functions.auth.user().beforeSms((context) => {
        if (
          context.smsType === "SIGN_IN_OR_SIGN_UP" &&
          context.additionalUserInfo.phoneNumber.includes('+91')
        ) {
          return {
            recaptchaActionOverride: "ALLOW",
          };
        }
    
        // Allow users to sign in with recaptcha score greater than 0.5
        if (event.additionalUserInfo.recaptchaScore > 0.5) {
          return {
            recaptchaActionOverride: 'ALLOW',
          };
        }
    
        // Block all others.
        return  {
          recaptchaActionOverride: 'BLOCK',
        }
      });
    
    

## What's next

  * [Enable reCAPTCHA SMS defense](https://docs.cloud.google.com/identity-platform/docs/recaptcha-tfp) for SMS-based authentication flows.
  * Learn how to [use your own reCAPTCHA key](https://docs.cloud.google.com/identity-platform/docs/recaptcha-byok).
  * Learn more about [monitoring reCAPTCHA metrics](https://docs.cloud.google.com/identity-platform/docs/recaptcha-metrics).
  * Learn more about [reCAPTCHA](https://docs.cloud.google.com/recaptcha/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
