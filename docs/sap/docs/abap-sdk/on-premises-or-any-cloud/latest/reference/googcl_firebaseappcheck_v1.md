---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_firebaseappcheck_v1/
title: Class /GOOG/CL_FIREBASEAPPCHECK_V1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:18.945319+00:00
---

# Class /GOOG/CL_FIREBASEAPPCHECK_V1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_firebaseappcheck_v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_FIREBASEAPPCHECK_V1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_firebaseappcheck_v1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_firebaseappcheck_v1)



## Class
    
    
    /GOOG/CL_FIREBASEAPPCHECK_V1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Firebase App Check API v1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `GoogleFirebaseAppcheckV1AppAttestConfig` | PUBLIC  
`TY_002` | `GoogleFirebaseAppcheckV1AppCheckToken` | PUBLIC  
`TY_003` | `GoogleFirebaseAppcheckV1BatchGetAppAttestConfigsResponse` | PUBLIC  
`TY_004` | `GoogleFirebaseAppcheckV1BatchGetDeviceCheckConfigsResponse` | PUBLIC  
`TY_005` | `GoogleFirebaseAppcheckV1BatchGetPlayIntegrityConfigsResponse` | PUBLIC  
`TY_006` | `GoogleFirebaseAppcheckV1BatchGetRecaptchaEnterpriseConfigsRe` | PUBLIC  
`TY_007` | `GoogleFirebaseAppcheckV1BatchGetRecaptchaV3ConfigsResponse` | PUBLIC  
`TY_009` | `GoogleFirebaseAppcheckV1BatchUpdateServicesRequest` | PUBLIC  
`TY_010` | `GoogleFirebaseAppcheckV1BatchUpdateServicesResponse` | PUBLIC  
`TY_011` | `GoogleFirebaseAppcheckV1DebugToken` | PUBLIC  
`TY_012` | `GoogleFirebaseAppcheckV1DeviceCheckConfig` | PUBLIC  
`TY_013` | `GoogleFirebaseAppcheckV1ExchangeAppAttestAssertionRequest` | PUBLIC  
`TY_014` | `GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationRequest` | PUBLIC  
`TY_015` | `GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationResponse` | PUBLIC  
`TY_016` | `GoogleFirebaseAppcheckV1ExchangeCustomTokenRequest` | PUBLIC  
`TY_017` | `GoogleFirebaseAppcheckV1ExchangeDebugTokenRequest` | PUBLIC  
`TY_018` | `GoogleFirebaseAppcheckV1ExchangeDeviceCheckTokenRequest` | PUBLIC  
`TY_019` | `GoogleFirebaseAppcheckV1ExchangePlayIntegrityTokenRequest` | PUBLIC  
`TY_020` | `GoogleFirebaseAppcheckV1ExchangeRecaptchaEnterpriseTokenRequ` | PUBLIC  
`TY_021` | `GoogleFirebaseAppcheckV1ExchangeRecaptchaV3TokenRequest` | PUBLIC  
`TY_024` | `GoogleFirebaseAppcheckV1GenerateAppAttestChallengeResponse` | PUBLIC  
`TY_026` | `GoogleFirebaseAppcheckV1GeneratePlayIntegrityChallengeRespon` | PUBLIC  
`TY_027` | `GoogleFirebaseAppcheckV1ListDebugTokensResponse` | PUBLIC  
`TY_028` | `GoogleFirebaseAppcheckV1ListServicesResponse` | PUBLIC  
`TY_029` | `GoogleFirebaseAppcheckV1PlayIntegrityConfig` | PUBLIC  
`TY_030` | `GoogleFirebaseAppcheckV1PublicJwk` | PUBLIC  
`TY_031` | `GoogleFirebaseAppcheckV1PublicJwkSet` | PUBLIC  
`TY_032` | `GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfig` | PUBLIC  
`TY_033` | `GoogleFirebaseAppcheckV1RecaptchaV3Config` | PUBLIC  
`TY_035` | `GoogleFirebaseAppcheckV1Service` | PUBLIC  
`TY_036` | `GoogleFirebaseAppcheckV1UpdateServiceRequest` | PUBLIC  
`TY_038` | `GoogleFirebaseAppcheckV1BatchUpdateResourcePoliciesRequest` | PUBLIC  
`TY_039` | `GoogleFirebaseAppcheckV1BatchUpdateResourcePoliciesResponse` | PUBLIC  
`TY_040` | `GoogleFirebaseAppcheckV1ListResourcePoliciesResponse` | PUBLIC  
`TY_041` | `GoogleFirebaseAppcheckV1ResourcePolicy` | PUBLIC  
`TY_042` | `GoogleFirebaseAppcheckV1UpdateResourcePolicyRequest` | PUBLIC  
`TY_T_001` | `GoogleFirebaseAppcheckV1AppAttestConfig` | PUBLIC  
`TY_T_011` | `GoogleFirebaseAppcheckV1DebugToken` | PUBLIC  
`TY_T_012` | `GoogleFirebaseAppcheckV1DeviceCheckConfig` | PUBLIC  
`TY_T_029` | `GoogleFirebaseAppcheckV1PlayIntegrityConfig` | PUBLIC  
`TY_T_030` | `GoogleFirebaseAppcheckV1PublicJwk` | PUBLIC  
`TY_T_032` | `GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfig` | PUBLIC  
`TY_T_033` | `GoogleFirebaseAppcheckV1RecaptchaV3Config` | PUBLIC  
`TY_T_035` | `GoogleFirebaseAppcheckV1Service` | PUBLIC  
`TY_T_036` | `GoogleFirebaseAppcheckV1UpdateServiceRequest` | PUBLIC  
`TY_T_041` | `GoogleFirebaseAppcheckV1ResourcePolicy` | PUBLIC  
`TY_T_042` | `GoogleFirebaseAppcheckV1UpdateResourcePolicyRequest` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250303 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://firebaseappcheck.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | firebaseappcheck:v1 | PUBLIC  
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
  
### BATCH_GET_APP_ATTEST_CONFIG

  * Description: firebaseappcheck.projects.apps.appAttestConfig.batchGet 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_NAMES` | IMPORTING | `STRING` | names  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | GoogleFirebaseAppcheckV1BatchGetAppAttestConfigsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### BATCH_GET_DEVICE_CHECK_CONF

  * Description: firebaseappcheck.projects.apps.deviceCheckConfig.batchGet 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_NAMES` | IMPORTING | `STRING` | names  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_004` | GoogleFirebaseAppcheckV1BatchGetDeviceCheckConfigsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### BATCH_GET_PLAY_INTEGRITY_CO

  * Description: firebaseappcheck.projects.apps.playIntegrityConfig.batchGet 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_NAMES` | IMPORTING | `STRING` | names  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | GoogleFirebaseAppcheckV1BatchGetPlayIntegrityConfigsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### BATCH_GET_RECAPTCHA_ENTERPR

  * Description: projects.apps.recaptchaEnterpriseConfig.batchGet 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_NAMES` | IMPORTING | `STRING` | names  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_006` | GoogleFirebaseAppcheckV1BatchGetRecaptchaEnterpriseConfigsRe  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### BATCH_GET_RECAPTCHA_V3CONFI

  * Description: firebaseappcheck.projects.apps.recaptchaV3Config.batchGet 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_NAMES` | IMPORTING | `STRING` | names  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | GoogleFirebaseAppcheckV1BatchGetRecaptchaV3ConfigsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### BATCH_UPDATE_RESOURCE_POLIC

  * Description: projects.services.resourcePolicies.batchUpdate 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IS_INPUT` | IMPORTING | `TY_038` | GoogleFirebaseAppcheckV1BatchUpdateResourcePoliciesRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_039` | GoogleFirebaseAppcheckV1BatchUpdateResourcePoliciesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### BATCH_UPDATE_SERVICES

  * Description: firebaseappcheck.projects.services.batchUpdate 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IS_INPUT` | IMPORTING | `TY_009` | GoogleFirebaseAppcheckV1BatchUpdateServicesRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | GoogleFirebaseAppcheckV1BatchUpdateServicesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_DEBUG_TOKENS

  * Description: firebaseappcheck.projects.apps.debugTokens.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_APPS_ID` | IMPORTING | `STRING` | appsId  
`IS_INPUT` | IMPORTING | `TY_011` | GoogleFirebaseAppcheckV1DebugToken  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | GoogleFirebaseAppcheckV1DebugToken  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_RESOURCE_POLICIES

  * Description: firebaseappcheck.projects.services.resourcePolicies.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IS_INPUT` | IMPORTING | `TY_041` | GoogleFirebaseAppcheckV1ResourcePolicy  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_041` | GoogleFirebaseAppcheckV1ResourcePolicy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_DEBUG_TOKENS

  * Description: firebaseappcheck.projects.apps.debugTokens.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_APPS_ID` | IMPORTING | `STRING` | appsId  
`IV_P_DEBUG_TOKENS_ID` | IMPORTING | `STRING` | debugTokensId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_RESOURCE_POLICIES

  * Description: firebaseappcheck.projects.services.resourcePolicies.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ETAG` | IMPORTING | `STRING` | etag  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_RESOURCE_POLICIES_ID` | IMPORTING | `STRING` | resourcePoliciesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### EXCHANGE_APP_ATTEST_ASSERTI

  * Description: firebaseappcheck.projects.apps.exchangeAppAttestAssertion 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_APPS_ID` | IMPORTING | `STRING` | appsId  
`IS_INPUT` | IMPORTING | `TY_013` | GoogleFirebaseAppcheckV1ExchangeAppAttestAssertionRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | GoogleFirebaseAppcheckV1AppCheckToken  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### EXCHANGE_APP_ATTEST_ASSERTI1

  * Description: firebaseappcheck.oauthClients.exchangeAppAttestAssertion 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_OAUTH_CLIENTS_ID` | IMPORTING | `STRING` | oauthClientsId  
`IS_INPUT` | IMPORTING | `TY_013` | GoogleFirebaseAppcheckV1ExchangeAppAttestAssertionRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | GoogleFirebaseAppcheckV1AppCheckToken  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### EXCHANGE_APP_ATTEST_ATTESTA

  * Description: firebaseappcheck.projects.apps.exchangeAppAttestAttestation 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_APPS_ID` | IMPORTING | `STRING` | appsId  
`IS_INPUT` | IMPORTING | `TY_014` | GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_015` | GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### EXCHANGE_APP_ATTEST_ATTESTA1

  * Description: firebaseappcheck.oauthClients.exchangeAppAttestAttestation 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_OAUTH_CLIENTS_ID` | IMPORTING | `STRING` | oauthClientsId  
`IS_INPUT` | IMPORTING | `TY_014` | GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_015` | GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### EXCHANGE_CUSTOM_TOKEN_APPS

  * Description: firebaseappcheck.projects.apps.exchangeCustomToken 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_APPS_ID` | IMPORTING | `STRING` | appsId  
`IS_INPUT` | IMPORTING | `TY_016` | GoogleFirebaseAppcheckV1ExchangeCustomTokenRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | GoogleFirebaseAppcheckV1AppCheckToken  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### EXCHANGE_DEBUG_TOKEN_APPS

  * Description: firebaseappcheck.projects.apps.exchangeDebugToken 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_APPS_ID` | IMPORTING | `STRING` | appsId  
`IS_INPUT` | IMPORTING | `TY_017` | GoogleFirebaseAppcheckV1ExchangeDebugTokenRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | GoogleFirebaseAppcheckV1AppCheckToken  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### EXCHANGE_DEBUG_TOKEN_OAUTH

  * Description: firebaseappcheck.oauthClients.exchangeDebugToken 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_OAUTH_CLIENTS_ID` | IMPORTING | `STRING` | oauthClientsId  
`IS_INPUT` | IMPORTING | `TY_017` | GoogleFirebaseAppcheckV1ExchangeDebugTokenRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | GoogleFirebaseAppcheckV1AppCheckToken  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### EXCHANGE_DEVICE_CHECK_TOKEN

  * Description: firebaseappcheck.projects.apps.exchangeDeviceCheckToken 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_APPS_ID` | IMPORTING | `STRING` | appsId  
`IS_INPUT` | IMPORTING | `TY_018` | GoogleFirebaseAppcheckV1ExchangeDeviceCheckTokenRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | GoogleFirebaseAppcheckV1AppCheckToken  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### EXCHANGE_PLAY_INTEGRITY_TOK

  * Description: firebaseappcheck.projects.apps.exchangePlayIntegrityToken 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_APPS_ID` | IMPORTING | `STRING` | appsId  
`IS_INPUT` | IMPORTING | `TY_019` | GoogleFirebaseAppcheckV1ExchangePlayIntegrityTokenRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | GoogleFirebaseAppcheckV1AppCheckToken  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### EXCHANGE_RECAPTCHA_ENTERPRI

  * Description: projects.apps.exchangeRecaptchaEnterpriseToken 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_APPS_ID` | IMPORTING | `STRING` | appsId  
`IS_INPUT` | IMPORTING | `TY_020` | GoogleFirebaseAppcheckV1ExchangeRecaptchaEnterpriseTokenRequ  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | GoogleFirebaseAppcheckV1AppCheckToken  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### EXCHANGE_RECAPTCHA_V3TOKEN

  * Description: firebaseappcheck.projects.apps.exchangeRecaptchaV3Token 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_APPS_ID` | IMPORTING | `STRING` | appsId  
`IS_INPUT` | IMPORTING | `TY_021` | GoogleFirebaseAppcheckV1ExchangeRecaptchaV3TokenRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | GoogleFirebaseAppcheckV1AppCheckToken  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GENERATE_APP_ATTEST_CHALLEN

  * Description: firebaseappcheck.projects.apps.generateAppAttestChallenge 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_APPS_ID` | IMPORTING | `STRING` | appsId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_024` | GoogleFirebaseAppcheckV1GenerateAppAttestChallengeResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GENERATE_APP_ATTEST_CHALLEN1

  * Description: firebaseappcheck.oauthClients.generateAppAttestChallenge 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_OAUTH_CLIENTS_ID` | IMPORTING | `STRING` | oauthClientsId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_024` | GoogleFirebaseAppcheckV1GenerateAppAttestChallengeResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GENERATE_PLAY_INTEGRITY_CHA

  * Description: projects.apps.generatePlayIntegrityChallenge 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_APPS_ID` | IMPORTING | `STRING` | appsId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_026` | GoogleFirebaseAppcheckV1GeneratePlayIntegrityChallengeRespon  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_APP_ATTEST_CONFIG

  * Description: firebaseappcheck.projects.apps.appAttestConfig.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_APPS_ID` | IMPORTING | `STRING` | appsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | GoogleFirebaseAppcheckV1AppAttestConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_DEBUG_TOKENS

  * Description: firebaseappcheck.projects.apps.debugTokens.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_APPS_ID` | IMPORTING | `STRING` | appsId  
`IV_P_DEBUG_TOKENS_ID` | IMPORTING | `STRING` | debugTokensId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | GoogleFirebaseAppcheckV1DebugToken  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_DEVICE_CHECK_CONFIG

  * Description: firebaseappcheck.projects.apps.deviceCheckConfig.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_APPS_ID` | IMPORTING | `STRING` | appsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | GoogleFirebaseAppcheckV1DeviceCheckConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_JWKS

  * Description: firebaseappcheck.jwks.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_031` | GoogleFirebaseAppcheckV1PublicJwkSet  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_PLAY_INTEGRITY_CONFIG

  * Description: firebaseappcheck.projects.apps.playIntegrityConfig.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_APPS_ID` | IMPORTING | `STRING` | appsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_029` | GoogleFirebaseAppcheckV1PlayIntegrityConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_RECAPTCHA_ENTERPRISE_CO

  * Description: projects.apps.recaptchaEnterpriseConfig.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_APPS_ID` | IMPORTING | `STRING` | appsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_032` | GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_RECAPTCHA_V3CONFIG

  * Description: firebaseappcheck.projects.apps.recaptchaV3Config.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_APPS_ID` | IMPORTING | `STRING` | appsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_033` | GoogleFirebaseAppcheckV1RecaptchaV3Config  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_RESOURCE_POLICIES

  * Description: firebaseappcheck.projects.services.resourcePolicies.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_RESOURCE_POLICIES_ID` | IMPORTING | `STRING` | resourcePoliciesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_041` | GoogleFirebaseAppcheckV1ResourcePolicy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_SERVICES

  * Description: firebaseappcheck.projects.services.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_035` | GoogleFirebaseAppcheckV1Service  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_DEBUG_TOKENS

  * Description: firebaseappcheck.projects.apps.debugTokens.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_APPS_ID` | IMPORTING | `STRING` | appsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_027` | GoogleFirebaseAppcheckV1ListDebugTokensResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_RESOURCE_POLICIES

  * Description: firebaseappcheck.projects.services.resourcePolicies.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_040` | GoogleFirebaseAppcheckV1ListResourcePoliciesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_SERVICES

  * Description: firebaseappcheck.projects.services.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_028` | GoogleFirebaseAppcheckV1ListServicesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_APP_ATTEST_CONFIG

  * Description: firebaseappcheck.projects.apps.appAttestConfig.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_APPS_ID` | IMPORTING | `STRING` | appsId  
`IS_INPUT` | IMPORTING | `TY_001` | GoogleFirebaseAppcheckV1AppAttestConfig  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | GoogleFirebaseAppcheckV1AppAttestConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_DEBUG_TOKENS

  * Description: firebaseappcheck.projects.apps.debugTokens.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_APPS_ID` | IMPORTING | `STRING` | appsId  
`IV_P_DEBUG_TOKENS_ID` | IMPORTING | `STRING` | debugTokensId  
`IS_INPUT` | IMPORTING | `TY_011` | GoogleFirebaseAppcheckV1DebugToken  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | GoogleFirebaseAppcheckV1DebugToken  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_DEVICE_CHECK_CONFIG

  * Description: firebaseappcheck.projects.apps.deviceCheckConfig.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_APPS_ID` | IMPORTING | `STRING` | appsId  
`IS_INPUT` | IMPORTING | `TY_012` | GoogleFirebaseAppcheckV1DeviceCheckConfig  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | GoogleFirebaseAppcheckV1DeviceCheckConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_PLAY_INTEGRITY_CONFIG

  * Description: firebaseappcheck.projects.apps.playIntegrityConfig.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_APPS_ID` | IMPORTING | `STRING` | appsId  
`IS_INPUT` | IMPORTING | `TY_029` | GoogleFirebaseAppcheckV1PlayIntegrityConfig  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_029` | GoogleFirebaseAppcheckV1PlayIntegrityConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_RECAPTCHA_ENTERPRISE

  * Description: projects.apps.recaptchaEnterpriseConfig.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_APPS_ID` | IMPORTING | `STRING` | appsId  
`IS_INPUT` | IMPORTING | `TY_032` | GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfig  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_032` | GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_RECAPTCHA_V3CONFIG

  * Description: firebaseappcheck.projects.apps.recaptchaV3Config.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_APPS_ID` | IMPORTING | `STRING` | appsId  
`IS_INPUT` | IMPORTING | `TY_033` | GoogleFirebaseAppcheckV1RecaptchaV3Config  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_033` | GoogleFirebaseAppcheckV1RecaptchaV3Config  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_RESOURCE_POLICIES

  * Description: firebaseappcheck.projects.services.resourcePolicies.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_RESOURCE_POLICIES_ID` | IMPORTING | `STRING` | resourcePoliciesId  
`IS_INPUT` | IMPORTING | `TY_041` | GoogleFirebaseAppcheckV1ResourcePolicy  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_041` | GoogleFirebaseAppcheckV1ResourcePolicy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_SERVICES

  * Description: firebaseappcheck.projects.services.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IS_INPUT` | IMPORTING | `TY_035` | GoogleFirebaseAppcheckV1Service  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_035` | GoogleFirebaseAppcheckV1Service  
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
