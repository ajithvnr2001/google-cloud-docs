---
url: https://docs.cloud.google.com/identity-platform/docs/admin/email-enumeration-protection/
title: Enable or disable email enumeration protection \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:49:22.552801+00:00
---

# Enable or disable email enumeration protection  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/admin/email-enumeration-protection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Enable or disable email enumeration protection

This guide explains the email enumeration protection feature and shows you how to enable and disable it. If you created your project on or after September 15, 2023, email enumeration protection is enabled by default.

**Important:** We recommend that you enable email enumeration protection on all projects.

## Overview

Email enumeration is a type of brute-force attack in which a malicious actor attempts to guess or confirm users in a system by passing an email address to the API and checking the response.

Without email enumeration protection, Identity Platform returns information that can be used in an email enumeration attack:

  * An attempt is made to sign in with an email address that doesn't exist in the system. Identity Platform returns an `EMAIL_NOT_FOUND` error.

  * An attempt is made to sign up with an email address that already exists in the system. Identity Platform returns an `EMAIL_EXISTS` error.




You can use Identity Platform's email enumeration protection feature to protect user accounts in your app from these attacks.

When email enumeration protection is enabled, your project has the following behavior:

  * The `fetchSignInForEmail` API will fail. Linking anonymous authenticated users with an email address will also not work prior to SDK version 22.3.0 for Android, 10.18.0 for iOS, and 10.6.0 for Web.

  * A list of sign-in methods for a specified email address is no longer returned when calling the [`createAuthUri`](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/accounts/createAuthUri) REST API or the [`fetchSignInMethodsForEmail`](https://firebase.google.com/docs/reference/js/auth#fetchsigninmethodsforemail) client SDK method on all platforms.

  * Users cannot change their email address without first verifying the new address. For example, you can no longer change a user's email address with the [`update`](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/accounts/update) REST API, the `setAccountInfo` REST API, or the [`updateEmail`](https://firebase.google.com/docs/reference/js/auth#updateemail) client SDK method on all platforms.

You can use [`verifyBeforeUpdateEmail`](https://firebase.google.com/docs/reference/js/auth#verifybeforeupdateemail) for Web and Android or [`sendEmailVerification(beforeUpdatingEmail:)`](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#sendemailverificationbeforeupdatingemail:) for iOS instead.

  * You can no longer use the `setAccountInfo` REST API to link an email/password provider to an existing user account. You can no longer use the [`linkWithCredential`](https://firebase.google.com/docs/reference/js/auth.md#linkwithcredential) client SDK method with an [`EmailAuthCredential`](https://firebase.google.com/docs/reference/js/auth.emailauthcredential) on any platform. Use the REST API [`signUp`](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/accounts/signUp) instead, passing the user's ID token in the `idToken` field and the `email`, `password` fields to link.

  * Removes error responses for email verification flows, including flows that were initiated by calling the [`sendOobCode`](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/accounts/sendOobCode) REST API with the `VERIFY_AND_CHANGE_EMAIL` or `PASSWORD_RESET` request types, and by calling [`verifyBeforeUpdateEmail`](https://firebase.google.com/docs/reference/js/auth#verifybeforeupdateemail) for Web and Android, [`sendEmailVerification(beforeUpdatingEmail:)`](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#sendemailverificationbeforeupdatingemail:) for iOS, or [`sendPasswordResetEmail`](https://firebase.google.com/docs/reference/js/auth#sendpasswordresetemail) on all platforms.

When you make a password reset request, a verification email is sent only if the email address exists; when you make an email address change request, a verification email is sent only if the email address doesn't already exist. In both cases, there are no specific error messages indicating when emails aren't sent.

We recommend that you don't allow users to sign up without an email verification flow.

  * Invalid sign-in cases return an `INVALID_LOGIN_CREDENTIALS` error response. Invalid sign-up cases continue to return `EMAIL_EXISTS` errors—see the recommendations in the next section.




If your app relies on any of the behaviors changed by email enumeration protection, you can disable it. However, this is not recommended in the long term; see the following section.

## Security recommendations

One of the most common methods to perform an account takeover attack is to perform credential-stuffing attacks using credentials that are leaked or easy to guess. Email enumeration can also be used to gain sensitive information about your users, or to perform phishing attacks against them. For these reasons, Google advises using the email enumeration protection feature to protect your apps against such attacks.

  * If you created your project on or after September 15, 2023, email enumeration protection is enabled by default. We recommend that you leave email enumeration protection enabled and refrain from relying on any of the behaviors listed earlier in this guide.

  * If you created your project before September 15, 2023, email enumeration protection is not automatically enabled.

If your apps don't rely on any of the behaviors described earlier in this guide, we recommend that you enable email enumeration protection immediately.

If your apps rely on any of the behaviors described earlier, we recommend that you begin migrating away from doing so, and enable email enumeration protection as soon as you can.




In addition to using email enumeration protection, consider taking measures to prevent abuse of your project's sign-up endpoints that continue to return `EMAIL_EXISTS` errors. The following are some ways to do so:

  * Enable [App Check](https://firebase.google.com/docs/app-check).
  * Integrate [reCAPTCHA](https://docs.cloud.google.com/recaptcha-enterprise/docs/overview) into your sign-up flow.
  * Disallow signing in with email addresses and passwords or email links, and use alternative methods, such as Google Sign-in, instead.



## Enable email enumeration protection

To enable email enumeration protection, follow these steps:

###  Firebase console 

  1. In the Firebase console, go to the **Authentication Settings** page.

[Go to Authentication Settings](https://console.firebase.google.com/project/_/authentication/settings)

     1. In the **User account management** pane, select **User actions**.

     2. Select **Email enumeration protection (recommended)**.

  2. Click **Save**.




###  REST 

  1. In the Google Cloud console, print an access token for your project ID using the [`gcloud auth print-access-token` command](https://docs.cloud.google.com/sdk/gcloud/reference/auth/print-access-token):
         
         gcloud auth print-access-token --project=PROJECT_ID
         

  2. Enable email enumeration protection for your project ID using the [Identity Toolkit API](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects/updateConfig):
         
         curl -X PATCH -d "{'emailPrivacyConfig':{'enableImprovedEmailPrivacy':true}}" \
             -H 'Authorization: Bearer ACCESS_TOKEN' \
             -H 'Content-Type: application/json' -H 'X-Goog-User-Project: PROJECT_ID' \
             "https://identitytoolkit.googleapis.com/admin/v2/projects/PROJECT_ID/config?updateMask=emailPrivacyConfig"
         




Replace the following:

  * ACCESS_TOKEN: the access token you generated earlier
  * PROJECT_ID: your project ID



## Disable email enumeration protection

To disable email enumeration protection, follow these steps:

###  Firebase console 

  1. In the Firebase console, go to the **Authentication Settings** page.

[Go to Authentication Settings](https://console.firebase.google.com/project/_/authentication/settings)

     1. In the **User account management** pane, select **User actions**.

     2. Clear **Email enumeration protection (recommended)**.

  2. Click **Save**.




###  REST 

  1. In the Google Cloud console, print an access token for your project ID using the [`gcloud auth print-access-token` command](https://docs.cloud.google.com/sdk/gcloud/reference/auth/print-access-token):
         
         gcloud auth print-access-token --project=PROJECT_ID
         

  2. Disable email enumeration protection using the Identity Toolkit API:
         
         curl -X PATCH -d "{'emailPrivacyConfig':{'enableImprovedEmailPrivacy':false}}" \
             -H 'Authorization: Bearer ACCESS_TOKEN' \
             -H 'Content-Type: application/json' -H 'X-Goog-User-Project: PROJECT_ID' \
             "https://identitytoolkit.googleapis.com/admin/v2/projects/PROJECT_ID/config?updateMask=emailPrivacyConfig"
         




Replace the following:

  * ACCESS_TOKEN: the access token you generated earlier
  * PROJECT_ID: your project ID



## Example of an error response

If a user attempts to sign in with an incorrect email address or password, or attempts to sign up with an email address that already exists in the system, Identity Platform returns an error similar to the following:
    
    
    {
    "code": "auth/internal-error",
    "message": "{\"error\":{\"code\":400,\"message\":\"INVALID_LOGIN_CREDENTIALS\",\"errors\":[{\"message\":\"INVALID_LOGIN_CREDENTIALS\",\"domain\":\"global\",\"reason\":\"invalid\"}]}}"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
