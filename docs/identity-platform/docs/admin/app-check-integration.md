---
url: https://docs.cloud.google.com/identity-platform/docs/admin/app-check-integration/
title: Enable App Check for a project \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:45:05.180083+00:00
---

# Enable App Check for a project  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/admin/app-check-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Enable App Check for a project 

****

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide shows you how to enable Firebase App Check for your Identity Platform project.

App Check uses [attestation services](https://firebase.google.com/docs/app-check) to check that requests made to your project originate from your app or from an authentic, untampered device.

**Note:** App Check is supported on Android, iOS, and web. Integrating with the App Check SDK might limit SDK support on web workers, service workers, and Cordova, due to limitations in reCAPTCHA support. You can work around these limitations by using a [custom App Check provider](https://firebase.google.com/docs/app-check/web/custom-provider).

App Check provides protection for the following operations used by the client SDK:

### Authentication operations

Method | Description  
---|---  
[`CreateAuthUri`](https://cloud.google.com/identity-platform/docs/reference/rest/v1/accounts/createAuthUri) | Obtains the possible sign in methods for the provided email address when signing in with an identity provider such as Google, Facebook, or Apple.  
[`SendVerificationCode`](https://cloud.google.com/identity-platform/docs/reference/rest/v1/accounts/sendVerificationCode) | Sends an SMS verification code for phone number sign-in.  
[`SignInWithCustomToken`](https://cloud.google.com/identity-platform/docs/reference/rest/v1/accounts/signInWithCustomToken) | Signs in or signs up a user by exchanging a custom Auth token.  
[`SignInWithEmailLink`](https://cloud.google.com/identity-platform/docs/reference/rest/v1/accounts/signInWithEmailLink) | Signs in or signs up a user with an out-of-band code from an email link.  
[`SignInWithIdp`](https://cloud.google.com/identity-platform/docs/reference/rest/v1/accounts/signInWithIdp) | Signs in or signs up a user using credentials from an Identity Provider (IdP).  
[`SignInWithPassword`](https://cloud.google.com/identity-platform/docs/reference/rest/v1/accounts/signInWithPassword) | Signs in with an email and password.  
[`SignInWithPhoneNumber`](https://cloud.google.com/identity-platform/docs/reference/rest/v1/accounts/signInWithPhoneNumber) | Completes a phone number authentication attempt.  
[`SignUp`](https://cloud.google.com/identity-platform/docs/reference/rest/v1/accounts/signUp) | Signs up a new email and password user or anonymous user, or upgrades an anonymous user to email and password.  
  
### Account management operations

Method | Description  
---|---  
[`DeleteAccount`](https://cloud.google.com/identity-platform/docs/reference/rest/v1/accounts/delete) | Deletes a user account.  
[`GetAccountInfo`](https://cloud.google.com/identity-platform/docs/reference/rest/v1/accounts/lookup) | Retrieves user info after signing in.  
[`GetOobCode`](https://cloud.google.com/identity-platform/docs/reference/rest/v1/accounts/sendOobCode) | Requests an out-of-band code to be sent to a user's email.  
[`ResetPassword`](https://cloud.google.com/identity-platform/docs/reference/rest/v1/accounts/resetPassword) | Completes an out-of-band password reset or checks a verification code sent to a user by email or a different out-of-band mechanism.  
[`SetAccountInfo`](https://cloud.google.com/identity-platform/docs/reference/rest/v1/accounts/update) | Updates user account information, for example, email address, password, or display name.  
  
## Enable App Check

To enable App Check for your project, do the following:

  1. In the Firebase console, go to **Build** > **App Check**.

  2. Click **Get started**.

  3. [Follow the getting starting guide](https://firebase.google.com/docs/app-check#get_started) to register and implement App Check in your project.




## What's next

  * [Enable email enumeration protection](https://docs.cloud.google.com/identity-platform/docs/admin/email-enumeration-protection) for your app
  * [Protect your app from SMS abuse](https://docs.cloud.google.com/identity-platform/docs/admin/sms-regions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
