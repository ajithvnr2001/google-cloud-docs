---
url: https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/accounts.mfaSignIn/finalize/
title: Method: accounts.mfaSignIn.finalize \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:11.535212+00:00
---

# Method: accounts.mfaSignIn.finalize  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/accounts.mfaSignIn/finalize/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Reference ](https://docs.cloud.google.com/identity-platform/docs/apis)



Send feedback 

#  Method: accounts.mfaSignIn.finalize Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * MfaTotpSignInRequestInfo
    * JSON representation
  * Try it!



Verifies the MFA challenge and performs sign-in

### HTTP request

`POST https://identitytoolkit.googleapis.com/v2/accounts/mfaSignIn:finalize`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "mfaPendingCredential": string,
      "tenantId": string,
      "mfaEnrollmentId": string,
    
      // Union field verification_info can be only one of the following:
      "phoneVerificationInfo": {
        object ([FinalizeMfaPhoneRequestInfo](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/FinalizeMfaPhoneRequestInfo))
      },
      "totpVerificationInfo": {
        object ([MfaTotpSignInRequestInfo](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/accounts.mfaSignIn/finalize#MfaTotpSignInRequestInfo))
      }
      // End of list of possible types for union field verification_info.
    }  
  
Fields  
---  
`mfaPendingCredential` |  `string` Required. Pending credential from first factor sign-in.  
`tenantId` |  `string` The ID of the Identity Platform tenant the user is signing in to. If not set, the user will sign in to the default Identity Platform project.  
`mfaEnrollmentId` |  `string` The MFA enrollment ID from the user's list of current MFA enrollments.  
Union field `verification_info`. Proof of completion of the MFA challenge. `verification_info` can be only one of the following:  
`phoneVerificationInfo` |  `object (`[FinalizeMfaPhoneRequestInfo](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/FinalizeMfaPhoneRequestInfo)`)` Proof of completion of the SMS based MFA challenge.  
`totpVerificationInfo` |  `object (`[MfaTotpSignInRequestInfo](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/accounts.mfaSignIn/finalize#MfaTotpSignInRequestInfo)`)` Proof of completion of the TOTP based MFA challenge.  
  
### Response body

mfaSignIn.finalize response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "idToken": string,
      "refreshToken": string,
    
      // Union field auxiliary_auth_info can be only one of the following:
      "phoneAuthInfo": {
        object ([FinalizeMfaPhoneResponseInfo](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/FinalizeMfaPhoneResponseInfo))
      }
      // End of list of possible types for union field auxiliary_auth_info.
    }  
  
Fields  
---  
`idToken` |  `string` ID token for the authenticated user.  
`refreshToken` |  `string` Refresh token for the authenticated user.  
Union field `auxiliary_auth_info`. MFA verified sign-in information. `auxiliary_auth_info` can be only one of the following:  
`phoneAuthInfo` |  `object (`[FinalizeMfaPhoneResponseInfo](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/FinalizeMfaPhoneResponseInfo)`)` Extra phone auth info, including android verification proof.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/identitytoolkit`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## MfaTotpSignInRequestInfo

TOTP verification info for FinalizeMfaSignInRequest.

JSON representation  
---  
      
    
    {
      "verificationCode": string
    }  
  
Fields  
---  
`verificationCode` |  `string` User-entered verification code.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
