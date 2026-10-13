---
url: https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/accounts.mfaEnrollment/finalize/
title: Method: accounts.mfaEnrollment.finalize \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:47:12.043870+00:00
---

# Method: accounts.mfaEnrollment.finalize  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/accounts.mfaEnrollment/finalize/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Reference ](https://docs.cloud.google.com/identity-platform/docs/apis)



Send feedback 

#  Method: accounts.mfaEnrollment.finalize Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * FinalizeMfaTotpEnrollmentRequestInfo
    * JSON representation
  * FinalizeMfaTotpEnrollmentResponseInfo
  * Try it!



Finishes enrolling a second factor for the user.

### HTTP request

`POST https://identitytoolkit.googleapis.com/v2/accounts/mfaEnrollment:finalize`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "idToken": string,
      "displayName": string,
      "tenantId": string,
    
      // Union field verification_info can be only one of the following:
      "phoneVerificationInfo": {
        object ([FinalizeMfaPhoneRequestInfo](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/FinalizeMfaPhoneRequestInfo))
      },
      "totpVerificationInfo": {
        object ([FinalizeMfaTotpEnrollmentRequestInfo](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/accounts.mfaEnrollment/finalize#FinalizeMfaTotpEnrollmentRequestInfo))
      }
      // End of list of possible types for union field verification_info.
    }  
  
Fields  
---  
`idToken` |  `string` Required. ID token.  
`displayName` |  `string` Display name which is entered by users to distinguish between different second factors with same type or different type.  
`tenantId` |  `string` The ID of the Identity Platform tenant that the user enrolling MFA belongs to. If not set, the user belongs to the default Identity Platform project.  
Union field `verification_info`. MFA enrollment information to be verified. `verification_info` can be only one of the following:  
`phoneVerificationInfo` |  `object (`[FinalizeMfaPhoneRequestInfo](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/FinalizeMfaPhoneRequestInfo)`)` Verification info to authorize sending an SMS for phone verification.  
`totpVerificationInfo` |  `object (`[FinalizeMfaTotpEnrollmentRequestInfo](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/accounts.mfaEnrollment/finalize#FinalizeMfaTotpEnrollmentRequestInfo)`)` Verification information for TOTP.  
  
### Response body

mfaEnrollment.finalize response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "idToken": string,
      "refreshToken": string,
    
      // Union field auxiliary_auth_info can be only one of the following:
      "phoneAuthInfo": {
        object ([FinalizeMfaPhoneResponseInfo](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/FinalizeMfaPhoneResponseInfo))
      },
      "totpAuthInfo": {
        object ([FinalizeMfaTotpEnrollmentResponseInfo](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/accounts.mfaEnrollment/finalize#FinalizeMfaTotpEnrollmentResponseInfo))
      }
      // End of list of possible types for union field auxiliary_auth_info.
    }  
  
Fields  
---  
`idToken` |  `string` ID token updated to reflect MFA enrollment.  
`refreshToken` |  `string` Refresh token updated to reflect MFA enrollment.  
Union field `auxiliary_auth_info`. MFA verified enrollment information. `auxiliary_auth_info` can be only one of the following:  
`phoneAuthInfo` |  `object (`[FinalizeMfaPhoneResponseInfo](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/FinalizeMfaPhoneResponseInfo)`)` Auxiliary auth info specific to phone auth.  
`totpAuthInfo` |  `object (`[FinalizeMfaTotpEnrollmentResponseInfo](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/accounts.mfaEnrollment/finalize#FinalizeMfaTotpEnrollmentResponseInfo)`)` Auxiliary auth info specific to TOTP auth.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/identitytoolkit`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## FinalizeMfaTotpEnrollmentRequestInfo

Mfa request info specific to TOTP auth for FinalizeMfa.

JSON representation  
---  
      
    
    {
      "sessionInfo": string,
      "verificationCode": string
    }  
  
Fields  
---  
`sessionInfo` |  `string` An opaque string that represents the enrollment session.  
`verificationCode` |  `string` User-entered verification code.  
  
## FinalizeMfaTotpEnrollmentResponseInfo

This type has no fields.

Mfa response info specific to TOTP auth for FinalizeMfa.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
