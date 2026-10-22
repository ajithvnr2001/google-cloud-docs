---
url: https://docs.cloud.google.com/identity-platform/docs/recaptcha-tfp/
title: Enable reCAPTCHA SMS defense for SMS-based authentication \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:15.345460+00:00
---

# Enable reCAPTCHA SMS defense for SMS-based authentication  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/recaptcha-tfp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Enable reCAPTCHA SMS defense for SMS-based authentication

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document explains how you can use reCAPTCHA SMS defense to help protect your Identity Platform SMS-based flows, such as phone and multi-factor authentication, against SMS toll fraud (also known as SMS pumping attacks). This integration helps prevent unauthorized SMS traffic from negatively affecting your users and resources.

## Overview

If your app relies on SMS for authentication, we recommend enabling the reCAPTCHA SMS defense integration. After it's enabled, Firebase Authentication and Identity Platform automatically invoke the reCAPTCHA SMS defense feature whenever an end user requests a verification SMS message from your app or site using the following `phoneProvider` operations:

Operation | Method  
---|---  
Phone number sign up or sign in | `sendVerificationCode`  
MFA phone number enrollment | `mfaSmsEnrollment`  
MFA phone number sign in | `mfaSmsSignIn` |   
  
reCAPTCHA then provides Firebase Authentication or Identity Platform with a risk score that indicates the likelihood of SMS toll fraud for the user's phone number. This score is then compared against your configured threshold. If the risk score exceeds this threshold, the SMS message is not sent, effectively blocking fraudulent attempts.

To understand how reCAPTCHA SMS defense scores work, see [Interpret scores](https://docs.cloud.google.com/recaptcha/docs/interpret-assessment-website#interpret_scores).

For more information about the reCAPTCHA SMS defense feature, see [Detect and prevent SMS fraud](https://docs.cloud.google.com/recaptcha/docs/sms-fraud-detection).

## reCAPTCHA phone authentication enforcement modes

You can configure phone authentication enforcement for reCAPTCHA SMS defense to use either the audit or enforce mode.

#### Audit mode

When you set phone authentication enforcement to audit mode, Identity Platform uses reCAPTCHA SMS defense for app verification. If a user's request passes the toll fraud assessment, an SMS verification code is sent. If a user's request fails the toll fraud assessment and you're using the client SDK, Identity Platform triggers fallback verification methods to complete the phone authentication flow. The accepted fallback methods depend on your app's platform. 

The client SDK triggers the fallback verification methods in the following scenarios:

  * The reCAPTCHA token is missing.
  * The reCAPTCHA token is invalid or expired.
  * The reCAPTCHA token doesn't pass the score threshold.
  * reCAPTCHA is not configured correctly.



Ensure that the fallback verification methods for your app's platform are set up and ready to be triggered by the client SDK if necessary.

### Web

If the initial toll fraud assessment fails, audit mode relies on reCAPTCHA v2 for verification. Therefore, you must set up the reCAPTCHA verifier (`RecaptchaVerifier`) and pass it to the following phone authentication operations: 

  * `verifyPhoneNumber`
  * `signInWithPhoneNumber`
  * `linkWithPhoneNumber`
  * `reauthenticateWithPhoneNumber`

Without the reCAPTCHA verifier, Identity Platform can't initiate reCAPTCHA v2 and will return `auth/argument-error`. For more information on setting up the reCAPTCHA verifier, see [Set up the reCAPTCHA verifier](https://firebase.google.com/docs/auth/web/phone-auth#set-up-the-recaptcha-verifier) in the Firebase documentation. 

### Android

If the initial toll fraud assessment fails, audit mode verifies your app against the Play Integrity API. If this verification fails, reCAPTCHA v2 is triggered. reCAPTCHA v2 might be triggered in the following scenarios: 

  * If the end-user's device does not have Google Play services installed.
  * If the app is not distributed through Google Play Store (on Authentication SDK v21.2.0 and later).
  * If the obtained SafetyNet token was not valid (on Authentication SDK versions prior to v21.2.0).

For more information on setting up Android app verification, see [Enable app verification](https://firebase.google.com/docs/auth/android/phone-auth#enable-app-verification) in the Firebase documentation. 

### iOS

If the initial toll fraud assessment fails, audit mode relies on silent push notifications for verification. This verification method involves sending a token to your app on the requesting device with a silent push notification. If your app successfully receives the notification, the phone authentication flow proceeds. If your app does not receive the push notification, reCAPTCHA v2 is triggered. reCAPTCHA v2 might be triggered if silent push notifications are not configured properly. 

For more information on setting up iOS app verification, see [Enable app verification](https://firebase.google.com/docs/auth/ios/phone-auth#enable-app-verification) in the Firebase documentation. 

#### Enforce mode

When you set phone authentication enforcement to enforce mode, Identity Platform uses reCAPTCHA SMS defense for app verification. If a user's request passes the toll fraud assessment, an SMS verification code is sent. If a user's request fails the toll fraud assessment, Identity Platform blocks the request and doesn't send an SMS message containing a verification code.

There is no fallback verification required in enforce mode, you don't have to set up any additional verification methods for your app. However, we recommend [setting up reCAPTCHA verifier](https://firebase.google.com/docs/auth/web/phone-auth#set-up-the-recaptcha-verifier) for web apps to ensure that reCAPTCHA v2 is enabled if you decide to change your app's reCAPTCHA mode to `AUDIT` or `OFF`.

## Before you begin

Before you enable reCAPTCHA SMS defense for Identity Platform, complete the following tasks:

  * Configure the following for your app or site as applicable:

    * [Phone sign in for users](https://docs.cloud.google.com/identity-platform/docs/sign-in-user-phone).
    * Multi-factor authentication for your [web](https://docs.cloud.google.com/identity-platform/docs/web/mfa), [Android](https://docs.cloud.google.com/identity-platform/docs/android/mfa), or [iOS](https://docs.cloud.google.com/identity-platform/docs/ios/mfa) app.
  * Configure Firebase Authentication for your app or site as applicable:

    * **Web:** [Phone Auth Setup](https://firebase.google.com/docs/auth/web/phone-auth)
    * **iOS:** [Phone Auth Setup](https://firebase.google.com/docs/auth/ios/phone-auth)
    * **Android:** [Phone Auth Setup](https://firebase.google.com/docs/auth/android/phone-auth)



## Enable reCAPTCHA SMS defense

  1. Set up authentication:

     1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

     2. Create a service identity:
            
            gcloud beta services identity create \
                --service=identitytoolkit.googleapis.com \
                --project=PROJECT_ID
            

Replace `PROJECT_ID` with the project's ID.

     3. Grant the `roles/identitytoolkit.serviceAgent` role to the service identity that you created.
            
            gcloud projects add-iam-policy-binding PROJECT_ID \
                --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-identitytoolkit.iam.gserviceaccount.com \
                --role=roles/identitytoolkit.serviceAgent
            

Replace the following:

        * `PROJECT_ID`: the project ID
        * `PROJECT_NUMBER`: the project account number
  2. [Enable the reCAPTCHA Enterprise API](https://docs.cloud.google.com/recaptcha/docs/prepare-environment#enable-api) on your project.

  3. Enable reCAPTCHA SMS defense for your project:

     1. In the Google Cloud console, go to the reCAPTCHA page.

[Go to reCAPTCHA](https://console.cloud.google.com/security/recaptcha)

     2. Verify that the name of your project appears in the resource selector.

If you don't see the name of your project, click the resource selector, and then select your project.

     3. Click **settings Settings**.

     4. In the **SMS defense** pane, click **Configure**.

     5. Click the **Enable** toggle, and click **Save**.

When you enable reCAPTCHA SMS defense, account defender is also enabled, if not already.

It might take a few minutes for the reCAPTCHA SMS defense enablement to propagate to our systems. Once propagated, you will start receiving responses related to reCAPTCHA SMS defense as part of the assessments.

  4. To configure reCAPTCHA SMS defense settings for a Firebase Authentication or Identity Platform project, do the following:

     1. In the following URL, replace `PROJECT_ID`, `Recaptcha_MODE`, and `START_SCORE`:
            
            https://cloud.google.com/identity-platform/docs/reference/rest/v2/projects/updateConfig?apix_params={"name":"projects/PROJECT_ID/config","updateMask":"recaptchaConfig","resource":{"recaptchaConfig":{"emailPasswordEnforcementState":"OFF","phoneEnforcementState":"Recaptcha_MODE","useSmsTollFraudProtection":true,"tollFraudManagedRules":[{"action":"BLOCK","startScore":START_SCORE}]}}}
            

        * `PROJECT_ID`: the project identifier with identity-platform enabled.

        * `Recaptcha_MODE`: the mode that you want to set for reCAPTCHA phone authentication enforcement. Valid values are `OFF`, `AUDIT`, and `ENFORCE`. To enable reCAPTCHA SMS defense, this parameter must be set to `AUDIT` or `ENFORCE` and `useSmsTollFraudProtection` must be set to `true`.

When you enable reCAPTCHA SMS defense for the first time, use `AUDIT` mode to make sure the reCAPTCHA SMS defense setup is working correctly. `AUDIT` mode is strictly for verification purposes. This mode won't prevent unauthorized SMS traffic. Verify that no failures appear in the Metrics dashboard. After the verification, enable `ENFORCE` mode immediately. For more information about how the modes work, see reCAPTCHA phone authentication enforcement modes

        * `START_SCORE`: a configurable threshold that determines the highest score that an SMS request can have before it's flagged and blocked as toll fraud.

The minimum threshold is `0.0`. The maximum threshold is `0.9`. Any request with a score higher than the threshold is considered fraudulent. For example, if you set the threshold to `0.3`, reCAPTCHA will block any requests with a fraud score of `0.4` or higher.

To increase the level of your fraud protection, set the threshold to a lower value. To reduce the level of your fraud protection, set the threshold to a higher value. This setting will allow more requests with higher scores to pass through.

For initial implementation, we recommend starting with a higher threshold, such as `0.8`, and then iteratively lower it according to your specific risk tolerance.

We don't recommend a threshold of `0.0` or `1.0`. Setting the threshold to `0.0` will block all SMS messages, while `1.0` will completely disable fraud protection, which can result in SMS delivery failures to high-risk regions.

**Note:** If you want to disable fraud protection, then set `Recaptcha_MODE` to `OFF`.
     2. Enter the URL in a new browser window where you're logged into the Google Cloud Console.

  5. If you're using Identity Platform on the web or Android, register your app from the [Firebase console](https://console.firebase.google.com/): 

     * For Android, [register each Android package name that uses Identity Platform](https://firebase.google.com/docs/android/setup#register-app).

     * For web, add an authorized domain for each domain that uses reCAPTCHA:

       1. In the Google Cloud console, go to the **Identity Platform** page.

[Go to Identity Platform](https://console.cloud.google.com/customer-identity)

       2. Go to **Settings** > **Security**.

       3. Click **Add domain**.

       4. Enter the domain name and click **Add** to save the domain.

reCAPTCHA key provisioning can take several minutes to complete.

  6. Verify your configuration:

     * Fetch the reCAPTCHA configuration details:

`{replace-your-project}` with your `projectId` or `projectNumber`. Execute the `GetConfig` API in the side-panel to fetch the reCAPTCHA configuration. 

     * Verify that the reCAPTCHA SMS defense is configured correctly:

       1. If the reCAPTCHA configuration is set up correctly, then the response must have the following fields with the specified values:

          * `recaptchaKeys`: Field must not be empty and is configured for at least one of these platforms: iOS, Web, or Android.
          * `useSmsTollFraudProtection`: The value for this field must be set to `true`.
          * `phoneEnforcementState`: The value must be set to either `ENFORCE` or `AUDIT`.
          * `tollFraudManagedRules`: Within this field, `startScore` needs to be configured with your chosen threshold, which must be a value between `0` and `0.9`.

Otherwise, configure reCAPTCHA SMS defense again.

Sample Response
    
    {
        "recaptchaConfig": {
            "recaptchaKeys": [
              {
                "key": "projects/{your-project}/keys/{recaptcha-key}",
                "type": "WEB"
              },
              {
                "type": "IOS"
              },
              {
                "type": "ANDROID"
              }
            ],
            "phoneEnforcementState": "ENFORCE",
            "tollFraudManagedRules": [
              {
                "startScore": 0.8,
                "action": "BLOCK"
              }
            ],
            "useSmsTollFraudProtection": true
        }
      }
      ```
    

  7. Make sure that the SDK versions are correct.

###  Web 

Update to the [latest version of the web SDK](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade).

     * reCAPTCHA support for email and password authentication in web apps is available on JavaScript SDK versions 9.20.0 and later.
     * reCAPTCHA support for phone authentication in web apps is available on JavaScript SDK versions 11 and later.

After you've integrated the web SDK with your app, the SDK automatically fetches your reCAPTCHA configuration and enables protection for the providers that you've configured.

###  Android 

     1. Update to the latest version of the Android SDK. reCAPTCHA support for email and password authentication and phone authentication in Android apps is available on [Android SDK version 23.1.0 and later](https://firebase.google.com/support/release-notes/android#auth_v23-1-0).

In addition, reCAPTCHA support requires API level 23 (Marshmallow) or higher and Android 6 or higher.

After you've integrated the Android SDK with your app, the SDK automatically fetches your reCAPTCHA configuration and enforces the thresholds you set for the providers that you've configured.

     2. Add the following build rule to the dependencies section of your app-level `build.gradle` file:
            
            implementation 'com.google.android.recaptcha:recaptcha:18.5.1'
            

Make sure to use reCAPTCHA SDK version 18.5.1 or later.

###  iOS 

     1. Update to [iOS SDK version 11.6.0 or later](https://firebase.google.com/support/release-notes/ios#11.6.0).

After you've integrated the iOS SDK with your app, the SDK automatically fetches your reCAPTCHA configuration and enforces the thresholds you set for the providers that you've configured.

     1. To integrate reCAPTCHA iOS SDK to your app, see [Prepare your iOS environment](https://docs.cloud.google.com/recaptcha-enterprise/docs/instrument-ios-apps#prepare-environment).

     2. To verify that `-ObjC` is listed in your linker flags, navigate to **Target** > **Build Settings** > **All** > **Linking** and verify that `Other Linker Flags` shows `-ObjC`.




## Monitor reCAPTCHA metrics for reCAPTCHA SMS defense

Monitor the reCAPTCHA metrics your project emits to verify that your SMS-based authentication flows are protected. For example, these metrics can help you determine if you've set up the Identity Platform integration with the reCAPTCHA Enterprise API correctly. They can also help you refine your score threshold for your user traffic.

Verify that the reCAPTCHA SMS defense feature is working by checking the following metrics your project emits to Cloud Monitoring:

  * [`identitytoolkit.googleapis.com/recaptcha/verdict_count`](https://docs.cloud.google.com/identity-platform/docs/recaptcha-metrics#verdict-count)
  * [`identitytoolkit.googleapis.com/recaptcha/token_count`](https://docs.cloud.google.com/identity-platform/docs/recaptcha-metrics#token-count)
  * [`identitytoolkit.googleapis.com/recaptcha/sms_tf_risk_scores`](https://docs.cloud.google.com/identity-platform/docs/recaptcha-metrics#tf-risk-scores)



For more information, see [Monitor reCAPTCHA metrics](https://docs.cloud.google.com/identity-platform/docs/recaptcha-metrics).

## Enforce reCAPTCHA SMS defense

After you verify that your app is receiving acceptable user traffic, enable reCAPTCHA `ENFORCE` mode to actively block fraudulent requests to help protect users.

To enable `ENFORCE` mode for SMS-based authentication flows on a project or tenant, use the Google APIs Explorer to update the project configuration by entering the following HTTP URL in a new browser window where you're logged into the Google Cloud console:
    
    
       https://cloud.google.com/identity-platform/docs/reference/rest/v2/projects/updateConfig?apix_params={"name":"projects/PROJECT_ID/config","updateMask":"recaptchaConfig","resource":{"recaptchaConfig":{"phoneEnforcementState":"ENFORCE","useSmsTollFraudProtection":"true"}}}
    

Replace `PROJECT_ID` with the project ID.

## Use reCAPTCHA SMS defense with bot protection

It is possible to use reCAPTCHA SMS defense simultaneously with bot protection. For configurations that use both protection features, consider the following:

  * When you've set the phone authentication enforcement state to `AUDIT`, Identity Platform passes a request when it satisfies at least one of the assessments. We recommend that you monitor the reCAPTCHA metrics to verify that both reCAPTCHA SMS defense and bot protection are configured with reasonable score settings.
  * When you've set the phone authentication enforcement state to `ENFORCE`, Identity Platform only passes a request when it satisfies both assessments and the request fail closes without falling back to another verification method.



To enable both features, use the Google APIs Explorer to update the project config:
    
    
            recaptchaConfig: {
              phoneEnforcementState:  'ENFORCE_MODE',
              useSmsTollFraudProtection: true,
              useSmsBotScore: true
            }
    

Replace `ENFORCE_MODE` with the mode you want to set for reCAPTCHA phone authentication enforcement. Valid values are `OFF`, `AUDIT`, and `ENFORCE`. When you enable reCAPTCHA SMS defense for the first time, we recommend setting this parameter to `AUDIT` and ensuring your authentication flows are protected before setting this to `ENFORCE`. For more information on how the modes work, see reCAPTCHA phone authentication enforcement modes.

## Disable reCAPTCHA SMS defense while using bot protection

If you are using both reCAPTCHA SMS defense and bot protection simultaneously, and you want to disable reCAPTCHA SMS defense without disabling bot protection, use the Google APIs Explorer to update the project config:
    
    
        recaptchaConfig: {
          phoneEnforcementState:  'ENFORCE_MODE',
          useSmsTollFraudProtection: 'false',
          useSmsBotScore: 'true'
        }
    

Replace `ENFORCE_MODE` with the mode you've previously set for reCAPTCHA phone authentication enforcement. This value should be either `AUDIT` or `ENFORCE`. For more information on how the modes work, see reCAPTCHA phone authentication enforcement modes.

## Disable reCAPTCHA SMS defense

To disable reCAPTCHA SMS defense, use the Google APIs Explorer to update the project configuration by entering the following HTTP URL in a new browser window where you're logged into the Google Cloud console:
    
    
       https://cloud.google.com/identity-platform/docs/reference/rest/v2/projects/updateConfig?apix_params={"name":"projects/PROJECT_ID/config","updateMask":"recaptchaConfig","resource":{"recaptchaConfig":{"phoneEnforcementState":"OFF","useSmsTollFraudProtection":"false"}}}
    

Replace `PROJECT_ID` with the project ID.

To disable reCAPTCHA SMS defense while you're using bot protection, see Disable reCAPTCHA SMS defense while using bot protection.

## What's next

  * Learn more about the [reCAPTCHA SMS defense feature](https://docs.cloud.google.com/recaptcha/docs/sms-fraud-detection).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
