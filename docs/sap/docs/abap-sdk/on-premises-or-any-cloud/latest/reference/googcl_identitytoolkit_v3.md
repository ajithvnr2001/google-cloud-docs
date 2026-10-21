---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_identitytoolkit_v3/
title: Class /GOOG/CL_IDENTITYTOOLKIT_V3 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:29.074517+00:00
---

# Class /GOOG/CL_IDENTITYTOOLKIT_V3  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_identitytoolkit_v3/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_IDENTITYTOOLKIT_V3 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_identitytoolkit_v3)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_identitytoolkit_v3)



## Class
    
    
    /GOOG/CL_IDENTITYTOOLKIT_V3

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Google Identity Toolkit API v3`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `CreateAuthUriResponse` | PUBLIC  
`TY_002` | `DeleteAccountResponse` | PUBLIC  
`TY_003` | `DownloadAccountResponse` | PUBLIC  
`TY_004` | `EmailLinkSigninResponse` | PUBLIC  
`TY_005` | `EmailTemplate` | PUBLIC  
`TY_006` | `GetAccountInfoResponse` | PUBLIC  
`TY_007` | `GetOobConfirmationCodeResponse` | PUBLIC  
`TY_008` | `GetRecaptchaParamResponse` | PUBLIC  
`TY_009` | `IdentitytoolkitRelyingpartyCreateAuthUriRequest` | PUBLIC  
`TY_010` | `IdentitytoolkitRelyingpartyDeleteAccountRequest` | PUBLIC  
`TY_011` | `IdentitytoolkitRelyingpartyDownloadAccountRequest` | PUBLIC  
`TY_012` | `IdentitytoolkitRelyingpartyEmailLinkSigninRequest` | PUBLIC  
`TY_013` | `IdentitytoolkitRelyingpartyGetAccountInfoRequest` | PUBLIC  
`TY_014` | `IdentitytoolkitRelyingpartyGetProjectConfigResponse` | PUBLIC  
`TY_016` | `IdentitytoolkitRelyingpartyResetPasswordRequest` | PUBLIC  
`TY_017` | `IdentitytoolkitRelyingpartySendVerificationCodeRequest` | PUBLIC  
`TY_018` | `IdentitytoolkitRelyingpartySendVerificationCodeResponse` | PUBLIC  
`TY_019` | `IdentitytoolkitRelyingpartySetAccountInfoRequest` | PUBLIC  
`TY_020` | `IdentitytoolkitRelyingpartySetProjectConfigRequest` | PUBLIC  
`TY_021` | `IdentitytoolkitRelyingpartySetProjectConfigResponse` | PUBLIC  
`TY_022` | `IdentitytoolkitRelyingpartySignOutUserRequest` | PUBLIC  
`TY_023` | `IdentitytoolkitRelyingpartySignOutUserResponse` | PUBLIC  
`TY_024` | `IdentitytoolkitRelyingpartySignupNewUserRequest` | PUBLIC  
`TY_025` | `IdentitytoolkitRelyingpartyUploadAccountRequest` | PUBLIC  
`TY_026` | `IdentitytoolkitRelyingpartyVerifyAssertionRequest` | PUBLIC  
`TY_027` | `IdentitytoolkitRelyingpartyVerifyCustomTokenRequest` | PUBLIC  
`TY_028` | `IdentitytoolkitRelyingpartyVerifyPasswordRequest` | PUBLIC  
`TY_029` | `IdentitytoolkitRelyingpartyVerifyPhoneNumberRequest` | PUBLIC  
`TY_030` | `IdentitytoolkitRelyingpartyVerifyPhoneNumberResponse` | PUBLIC  
`TY_031` | `IdpConfig` | PUBLIC  
`TY_032` | `Relyingparty` | PUBLIC  
`TY_033` | `ResetPasswordResponse` | PUBLIC  
`TY_034` | `SetAccountInfoResponse` | PUBLIC  
`TY_035` | `SignupNewUserResponse` | PUBLIC  
`TY_036` | `UploadAccountResponse` | PUBLIC  
`TY_037` | `UserInfo` | PUBLIC  
`TY_038` | `VerifyAssertionResponse` | PUBLIC  
`TY_039` | `VerifyCustomTokenResponse` | PUBLIC  
`TY_040` | `VerifyPasswordResponse` | PUBLIC  
`TY_043` | `ProviderUserInfo` | PUBLIC  
`TY_044` | `ProviderUserInfo` | PUBLIC  
`TY_045` | `Error` | PUBLIC  
`TY_T_031` | `IdpConfig` | PUBLIC  
`TY_T_037` | `UserInfo` | PUBLIC  
`TY_T_043` | `ProviderUserInfo` | PUBLIC  
`TY_T_044` | `ProviderUserInfo` | PUBLIC  
`TY_T_045` | `Error` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix | /identitytoolkit/v3/relyingparty/ | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20180723 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://www.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | identitytoolkit:v3 | PUBLIC  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
  
## Methods

For general information about a method in ABAP SDK for Google Cloud, see [API method](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#api_method). 

### CONSTRUCTOR

  * Description: Constructor 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_KEY_NAME` | IMPORTING | `/GOOG/KEYNAME` | Google Cloud Key Name  
`IV_LOG_OBJ` | IMPORTING | `BALOBJ_D` | Application log: Object name (Application code)  
`IV_LOG_SUBOBJ` | IMPORTING | `BALSUBOBJ` | Application Log: Subobject  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_AUTH_URI_RELYINGPART

  * Description: identitytoolkit.relyingparty.createAuthUri 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_009` | IdentitytoolkitRelyingpartyCreateAuthUriRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | CreateAuthUriResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_ACCOUNT_RELYINGPARTY

  * Description: identitytoolkit.relyingparty.deleteAccount 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_010` | IdentitytoolkitRelyingpartyDeleteAccountRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | DeleteAccountResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DOWNLOAD_ACCOUNT_RELYINGPAR

  * Description: identitytoolkit.relyingparty.downloadAccount 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_011` | IdentitytoolkitRelyingpartyDownloadAccountRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | DownloadAccountResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### EMAIL_LINK_SIGNIN_RELYINGPA

  * Description: identitytoolkit.relyingparty.emailLinkSignin 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_012` | IdentitytoolkitRelyingpartyEmailLinkSigninRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_004` | EmailLinkSigninResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_ACCOUNT_INFO_RELYINGPAR

  * Description: identitytoolkit.relyingparty.getAccountInfo 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_013` | IdentitytoolkitRelyingpartyGetAccountInfoRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_006` | GetAccountInfoResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_OOB_CONFIRMATION_CODE_R

  * Description: identitytoolkit.relyingparty.getOobConfirmationCode 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_032` | Relyingparty  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | GetOobConfirmationCodeResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_PROJECT_CONFIG_RELYINGP

  * Description: identitytoolkit.relyingparty.getProjectConfig 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_DELEGATEDPROJECTNUMBER` | IMPORTING | `STRING` | delegatedProjectNumber  
`IV_Q_PROJECTNUMBER` | IMPORTING | `STRING` | projectNumber  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_014` | IdentitytoolkitRelyingpartyGetProjectConfigResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_PUBLIC_KEYS_RELYINGPART

  * Description: identitytoolkit.relyingparty.getPublicKeys 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_RECAPTCHA_PARAM_RELYING

  * Description: identitytoolkit.relyingparty.getRecaptchaParam 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_008` | GetRecaptchaParamResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RESET_PASSWORD_RELYINGPARTY

  * Description: identitytoolkit.relyingparty.resetPassword 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_016` | IdentitytoolkitRelyingpartyResetPasswordRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_033` | ResetPasswordResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SEND_VERIFICATION_CODE_RELY

  * Description: identitytoolkit.relyingparty.sendVerificationCode 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_017` | IdentitytoolkitRelyingpartySendVerificationCodeRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_018` | IdentitytoolkitRelyingpartySendVerificationCodeResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SET_ACCOUNT_INFO_RELYINGPAR

  * Description: identitytoolkit.relyingparty.setAccountInfo 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_019` | IdentitytoolkitRelyingpartySetAccountInfoRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_034` | SetAccountInfoResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SET_PROJECT_CONFIG_RELYINGP

  * Description: identitytoolkit.relyingparty.setProjectConfig 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_020` | IdentitytoolkitRelyingpartySetProjectConfigRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_021` | IdentitytoolkitRelyingpartySetProjectConfigResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SIGNUP_NEW_USER_RELYINGPART

  * Description: identitytoolkit.relyingparty.signupNewUser 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_024` | IdentitytoolkitRelyingpartySignupNewUserRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_035` | SignupNewUserResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SIGN_OUT_USER_RELYINGPARTY

  * Description: identitytoolkit.relyingparty.signOutUser 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_022` | IdentitytoolkitRelyingpartySignOutUserRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_023` | IdentitytoolkitRelyingpartySignOutUserResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPLOAD_ACCOUNT_RELYINGPARTY

  * Description: identitytoolkit.relyingparty.uploadAccount 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_025` | IdentitytoolkitRelyingpartyUploadAccountRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_036` | UploadAccountResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### VERIFY_ASSERTION_RELYINGPAR

  * Description: identitytoolkit.relyingparty.verifyAssertion 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_026` | IdentitytoolkitRelyingpartyVerifyAssertionRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_038` | VerifyAssertionResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### VERIFY_CUSTOM_TOKEN_RELYING

  * Description: identitytoolkit.relyingparty.verifyCustomToken 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_027` | IdentitytoolkitRelyingpartyVerifyCustomTokenRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_039` | VerifyCustomTokenResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### VERIFY_PASSWORD_RELYINGPART

  * Description: identitytoolkit.relyingparty.verifyPassword 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_028` | IdentitytoolkitRelyingpartyVerifyPasswordRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_040` | VerifyPasswordResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### VERIFY_PHONE_NUMBER_RELYING

  * Description: identitytoolkit.relyingparty.verifyPhoneNumber 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_029` | IdentitytoolkitRelyingpartyVerifyPhoneNumberRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_030` | IdentitytoolkitRelyingpartyVerifyPhoneNumberResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CLOSE

  * Description: Close Connection 
  * Visibility: PUBLIC 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
