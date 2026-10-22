---
url: https://docs.cloud.google.com/identity-platform/docs/error-codes/
title: Error codes \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:00.856564+00:00
---

# Error codes  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/error-codes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Reference ](https://docs.cloud.google.com/identity-platform/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Error codes

This document lists Identity Platform error codes.

## Account management error codes

Web error code | iOS error code | Android error code | Android exception | ID and description  
---|---|---|---|---  
`auth/requires-recent-login` |  `ERROR_REQUIRES_RECENT_LOGIN` |  `ERROR_REQUIRES_RECENT_LOGIN` |  `FirebaseAuthRecentLoginRequiredException` | `17014` This operation is sensitive and requires recent authentication. Log in again before retrying this request.   
  
## Authorization error codes

Web error code | iOS error code | Android error code | Android exception | ID and description  
---|---|---|---|---  
`auth/app-not-authorized` |  `ERROR_APP_NOT_AUTHORIZED` |  `ERROR_APP_NOT_AUTHORIZED` |  `FirebaseAuthException` |  `17028` This app is not authorized to use Identity Platform. On Android, verify that the correct package name and SHA-1 are configured in the Google Cloud console. On iOS, review your key configuration ensure that it accepts requests from your app's bundle ID. For web apps, check your domain and key configuration.   
  
## Multi-factor authentication error codes

**Beta**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Web error code | iOS error code | Android error code | Android exception | ID and description  
---|---|---|---|---  
`auth/missing-multi-factor-session` |  `ERROR_MISSING_MULTI_FACTOR_SESSION` |  `ERROR_MISSING_MULTI_FACTOR_SESSION` |  `FirebaseAuthInvalidCredentialsException` | `17081` The request is missing proof of first factor successful sign-in.  
`auth/missing-multi-factor-info` |  `ERROR_MISSING_MULTI_FACTOR_INFO` |  `ERROR_MISSING_MULTI_FACTOR_INFO` |  `FirebaseAuthInvalidCredentialsException` | `17082` No second factor identifier was provided.  
`auth/invalid-multi-factor-session` |  `ERROR_INVALID_MULTI_FACTOR_SESSION` |  `ERROR_INVALID_MULTI_FACTOR_SESSION` |  `FirebaseAuthInvalidCredentialsException` | `17083` The request does not contain valid proof of successful first factor sign-in.   
`auth/multi-factor-info-not-found` |  `ERROR_MULTI_FACTOR_INFO_NOT_FOUND` |  `ERROR_MULTI_FACTOR_INFO_NOT_FOUND` |  `FirebaseAuthInvalidCredentialsException` | `17084` The user does not have a second factor matching the identifier provided.   
`auth/multi-factor-auth-required` |  `ERROR_SECOND_FACTOR_REQUIRED` |  `ERROR_SECOND_FACTOR_REQUIRED` |  `FirebaseAuthMultiFactorException` | `17078` Proof of ownership of a second factor is required to complete sign-in.   
`auth/second-factor-already-in-use` |  `ERROR_SECOND_FACTOR_ALREADY_ENROLLED` |  `ERROR_SECOND_FACTOR_ALREADY_ENROLLED` |  `FirebaseAuthException` | `17087` The second factor is already enrolled on this account.  
`auth/maximum-second-factor-count-exceeded` |  `ERROR_MAXIMUM_SECOND_FACTOR_COUNT_EXCEEDED` |  `ERROR_MAXIMUM_SECOND_FACTOR_COUNT_EXCEEDED` |  `FirebaseAuthException` | `17088` The maximum allowed number of second factors on a user has been exceeded.   
`auth/unsupported-first-factor` |  `ERROR_UNSUPPORTED_FIRST_FACTOR` |  `ERROR_UNSUPPORTED_FIRST_FACTOR` |  `FirebaseAuthException` |  `17089` Enrolling a second factor or signing in with a multi-factor account requires sign-in with a supported first factor.   
`auth/email-change-needs-verification` |  `ERROR_EMAIL_CHANGE_NEEDS_VERIFICATION` |  `ERROR_EMAIL_CHANGE_NEEDS_VERIFICATION` |  `FirebaseAuthException` | `17090` Multi-factor users must always have a verified email.  
  
## Phone authentication error codes

Web error code | iOS error code | Android error code | Android exception | ID and description  
---|---|---|---|---  
`auth/missing-phone-number` |  `ERROR_MISSING_PHONE_NUMBER` |  `ERROR_MISSING_PHONE_NUMBER` |  `FirebaseAuthInvalidCredentialsException` | `17041` To send verification codes, provide a phone number for the recipient.   
`auth/invalid-phone-number` |  `ERROR_INVALID_PHONE_NUMBER` |  `ERROR_INVALID_PHONE_NUMBER` |  `FirebaseAuthInvalidCredentialsException` | `17042` The format of the phone number provided is incorrect. Enter the phone number in a format that can be parsed into E.164 format. E.164 phone numbers are written in the format: `[+][country code][subscriber number including area code]`.   
`auth/missing-verification-code` |  `ERROR_MISSING_VERIFICATION_CODE` |  `ERROR_MISSING_VERIFICATION_CODE` |  `FirebaseAuthInvalidCredentialsException` | `17043` The phone auth credential was created with an empty SMS verification code.   
`auth/invalid-verification-code` |  `ERROR_INVALID_VERIFICATION_CODE` |  `ERROR_INVALID_VERIFICATION_CODE` |  `FirebaseAuthInvalidCredentialsException` | `17044` The SMS verification code used to create the phone auth credential is invalid. Resend the verification code SMS, and be sure to use the verification code provided by the user.   
`auth/missing-verification-id` |  `ERROR_MISSING_VERIFICATION_ID` |  `ERROR_MISSING_VERIFICATION_ID` |  `FirebaseAuthInvalidCredentialsException` | `17045` The phone authentication credential was created with an empty verification ID.   
`auth/invalid-verification-id` |  `ERROR_INVALID_VERIFICATION_ID` |  `ERROR_INVALID_VERIFICATION_ID` |  `FirebaseAuthInvalidCredentialsException` |  `17046` The verification ID used to create the phone auth credential is invalid.   
`auth/code-expired` |  `ERROR_SESSION_EXPIRED` |  `ERROR_SESSION_EXPIRED` |  `FirebaseAuthInvalidCredentialsException` | `17051` The SMS code has expired. Re-send the verification code to try again.   
`auth/captcha-check-failed` | `ERROR_CAPTCHA_CHECK_FAILED` | `ERROR_CAPTCHA_CHECK_FAILED` | `FirebaseAuthRecaptchaCheckFailedException` | `17056` The reCAPTCHA response token provided is invalid, expired, already used, or the domain associated with it doesn't match the list of allowed domains.   
`auth/quota-exceeded` |  `ERROR_QUOTA_EXCEEDED` |  `ERROR_QUOTA_EXCEEDED` |  `FirebaseTooManyRequestsException` | `17052` The phone verification quota for this project has been exceeded.  
N/A |  `ERROR_APP_NOT_VERIFIED` | N/A | N/A | `17055` Identity Platform couldn't retrieve the silent push notification and therefore couldn't verify your app. Ensure that you configured your app correctly to receive push notifications.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
