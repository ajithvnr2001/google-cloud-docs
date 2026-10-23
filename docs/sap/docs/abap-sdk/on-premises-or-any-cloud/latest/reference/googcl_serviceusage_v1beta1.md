---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_serviceusage_v1beta1/
title: Class /GOOG/CL_SERVICEUSAGE_V1BETA1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:00:07.645734+00:00
---

# Class /GOOG/CL_SERVICEUSAGE_V1BETA1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_serviceusage_v1beta1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_SERVICEUSAGE_V1BETA1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_serviceusage_v1beta1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_serviceusage_v1beta1)



## Class
    
    
    /GOOG/CL_SERVICEUSAGE_V1BETA1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Service Usage API v1beta1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_017` | `ConsumerQuotaLimit` | PUBLIC  
`TY_018` | `ConsumerQuotaMetric` | PUBLIC  
`TY_051` | `ImportAdminOverridesRequest` | PUBLIC  
`TY_052` | `ImportConsumerOverridesRequest` | PUBLIC  
`TY_056` | `ListAdminOverridesResponse` | PUBLIC  
`TY_057` | `ListConsumerOverridesResponse` | PUBLIC  
`TY_058` | `ListConsumerQuotaMetricsResponse` | PUBLIC  
`TY_059` | `ListOperationsResponse` | PUBLIC  
`TY_077` | `Operation` | PUBLIC  
`TY_079` | `OverrideInlineSource` | PUBLIC  
`TY_082` | `ProducerQuotaPolicy` | PUBLIC  
`TY_086` | `QuotaBucket` | PUBLIC  
`TY_088` | `QuotaOverride` | PUBLIC  
`TY_089` | `RolloutInfo` | PUBLIC  
`TY_097` | `Status` | PUBLIC  
`TY_T_017` | `ConsumerQuotaLimit` | PUBLIC  
`TY_T_018` | `ConsumerQuotaMetric` | PUBLIC  
`TY_T_077` | `Operation` | PUBLIC  
`TY_T_086` | `QuotaBucket` | PUBLIC  
`TY_T_088` | `QuotaOverride` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.10 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250227 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://serviceusage.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | serviceusage:v1beta1 | PUBLIC  
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
  
### CREATE_ADMIN_OVERRIDES

  * Description: services.consumerQuotaMetrics.limits.adminOverrides.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FORCE` | IMPORTING | `STRING` | force  
`IV_Q_FORCEONLY` | IMPORTING | `STRING` | forceOnly  
`IV_P_V1BETA1ID` | IMPORTING | `STRING` | v1beta1Id  
`IV_P_V1BETA1ID1` | IMPORTING | `STRING` | v1beta1Id1  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_CONSUMER_QUOTA_METRICS_ID` | IMPORTING | `STRING` | consumerQuotaMetricsId  
`IV_P_LIMITS_ID` | IMPORTING | `STRING` | limitsId  
`IS_INPUT` | IMPORTING | `TY_088` | QuotaOverride  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_077` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_CONSUMER_OVERRIDES

  * Description: consumerQuotaMetrics.limits.consumerOverrides.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FORCE` | IMPORTING | `STRING` | force  
`IV_Q_FORCEONLY` | IMPORTING | `STRING` | forceOnly  
`IV_P_V1BETA1ID` | IMPORTING | `STRING` | v1beta1Id  
`IV_P_V1BETA1ID1` | IMPORTING | `STRING` | v1beta1Id1  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_CONSUMER_QUOTA_METRICS_ID` | IMPORTING | `STRING` | consumerQuotaMetricsId  
`IV_P_LIMITS_ID` | IMPORTING | `STRING` | limitsId  
`IS_INPUT` | IMPORTING | `TY_088` | QuotaOverride  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_077` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_ADMIN_OVERRIDES

  * Description: services.consumerQuotaMetrics.limits.adminOverrides.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FORCE` | IMPORTING | `STRING` | force  
`IV_Q_FORCEONLY` | IMPORTING | `STRING` | forceOnly  
`IV_P_V1BETA1ID` | IMPORTING | `STRING` | v1beta1Id  
`IV_P_V1BETA1ID1` | IMPORTING | `STRING` | v1beta1Id1  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_CONSUMER_QUOTA_METRICS_ID` | IMPORTING | `STRING` | consumerQuotaMetricsId  
`IV_P_LIMITS_ID` | IMPORTING | `STRING` | limitsId  
`IV_P_ADMIN_OVERRIDES_ID` | IMPORTING | `STRING` | adminOverridesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_077` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_CONSUMER_OVERRIDES

  * Description: consumerQuotaMetrics.limits.consumerOverrides.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FORCE` | IMPORTING | `STRING` | force  
`IV_Q_FORCEONLY` | IMPORTING | `STRING` | forceOnly  
`IV_P_V1BETA1ID` | IMPORTING | `STRING` | v1beta1Id  
`IV_P_V1BETA1ID1` | IMPORTING | `STRING` | v1beta1Id1  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_CONSUMER_QUOTA_METRICS_ID` | IMPORTING | `STRING` | consumerQuotaMetricsId  
`IV_P_LIMITS_ID` | IMPORTING | `STRING` | limitsId  
`IV_P_CONSUMER_OVERRIDES_ID` | IMPORTING | `STRING` | consumerOverridesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_077` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GENERATE_SERVICE_IDENTITY_S

  * Description: serviceusage.services.generateServiceIdentity 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_V1BETA1ID` | IMPORTING | `STRING` | v1beta1Id  
`IV_P_V1BETA1ID1` | IMPORTING | `STRING` | v1beta1Id1  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_077` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CONSUMER_QUOTA_METRICS

  * Description: serviceusage.services.consumerQuotaMetrics.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_VIEW` | IMPORTING | `STRING` | view  
`IV_P_V1BETA1ID` | IMPORTING | `STRING` | v1beta1Id  
`IV_P_V1BETA1ID1` | IMPORTING | `STRING` | v1beta1Id1  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_CONSUMER_QUOTA_METRICS_ID` | IMPORTING | `STRING` | consumerQuotaMetricsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_018` | ConsumerQuotaMetric  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_LIMITS

  * Description: serviceusage.services.consumerQuotaMetrics.limits.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_VIEW` | IMPORTING | `STRING` | view  
`IV_P_V1BETA1ID` | IMPORTING | `STRING` | v1beta1Id  
`IV_P_V1BETA1ID1` | IMPORTING | `STRING` | v1beta1Id1  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_CONSUMER_QUOTA_METRICS_ID` | IMPORTING | `STRING` | consumerQuotaMetricsId  
`IV_P_LIMITS_ID` | IMPORTING | `STRING` | limitsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | ConsumerQuotaLimit  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_OPERATIONS

  * Description: serviceusage.operations.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_OPERATIONS_ID` | IMPORTING | `STRING` | operationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_077` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### IMPORT_ADMIN_OVERRIDES_CONS

  * Description: services.consumerQuotaMetrics.importAdminOverrides 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_V1BETA1ID` | IMPORTING | `STRING` | v1beta1Id  
`IV_P_V1BETA1ID1` | IMPORTING | `STRING` | v1beta1Id1  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IS_INPUT` | IMPORTING | `TY_051` | ImportAdminOverridesRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_077` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### IMPORT_CONSUMER_OVERRIDES_C

  * Description: services.consumerQuotaMetrics.importConsumerOverrides 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_V1BETA1ID` | IMPORTING | `STRING` | v1beta1Id  
`IV_P_V1BETA1ID1` | IMPORTING | `STRING` | v1beta1Id1  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IS_INPUT` | IMPORTING | `TY_052` | ImportConsumerOverridesRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_077` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_ADMIN_OVERRIDES

  * Description: services.consumerQuotaMetrics.limits.adminOverrides.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_V1BETA1ID` | IMPORTING | `STRING` | v1beta1Id  
`IV_P_V1BETA1ID1` | IMPORTING | `STRING` | v1beta1Id1  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_CONSUMER_QUOTA_METRICS_ID` | IMPORTING | `STRING` | consumerQuotaMetricsId  
`IV_P_LIMITS_ID` | IMPORTING | `STRING` | limitsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_056` | ListAdminOverridesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_CONSUMER_OVERRIDES

  * Description: services.consumerQuotaMetrics.limits.consumerOverrides.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_V1BETA1ID` | IMPORTING | `STRING` | v1beta1Id  
`IV_P_V1BETA1ID1` | IMPORTING | `STRING` | v1beta1Id1  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_CONSUMER_QUOTA_METRICS_ID` | IMPORTING | `STRING` | consumerQuotaMetricsId  
`IV_P_LIMITS_ID` | IMPORTING | `STRING` | limitsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_057` | ListConsumerOverridesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_CONSUMER_QUOTA_METRICS

  * Description: serviceusage.services.consumerQuotaMetrics.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_VIEW` | IMPORTING | `STRING` | view  
`IV_P_V1BETA1ID` | IMPORTING | `STRING` | v1beta1Id  
`IV_P_V1BETA1ID1` | IMPORTING | `STRING` | v1beta1Id1  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_058` | ListConsumerQuotaMetricsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_OPERATIONS

  * Description: serviceusage.operations.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_NAME` | IMPORTING | `STRING` | name  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_059` | ListOperationsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_ADMIN_OVERRIDES

  * Description: services.consumerQuotaMetrics.limits.adminOverrides.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FORCE` | IMPORTING | `STRING` | force  
`IV_Q_FORCEONLY` | IMPORTING | `STRING` | forceOnly  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_V1BETA1ID` | IMPORTING | `STRING` | v1beta1Id  
`IV_P_V1BETA1ID1` | IMPORTING | `STRING` | v1beta1Id1  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_CONSUMER_QUOTA_METRICS_ID` | IMPORTING | `STRING` | consumerQuotaMetricsId  
`IV_P_LIMITS_ID` | IMPORTING | `STRING` | limitsId  
`IV_P_ADMIN_OVERRIDES_ID` | IMPORTING | `STRING` | adminOverridesId  
`IS_INPUT` | IMPORTING | `TY_088` | QuotaOverride  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_077` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_CONSUMER_OVERRIDES

  * Description: consumerQuotaMetrics.limits.consumerOverrides.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FORCE` | IMPORTING | `STRING` | force  
`IV_Q_FORCEONLY` | IMPORTING | `STRING` | forceOnly  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_V1BETA1ID` | IMPORTING | `STRING` | v1beta1Id  
`IV_P_V1BETA1ID1` | IMPORTING | `STRING` | v1beta1Id1  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_CONSUMER_QUOTA_METRICS_ID` | IMPORTING | `STRING` | consumerQuotaMetricsId  
`IV_P_LIMITS_ID` | IMPORTING | `STRING` | limitsId  
`IV_P_CONSUMER_OVERRIDES_ID` | IMPORTING | `STRING` | consumerOverridesId  
`IS_INPUT` | IMPORTING | `TY_088` | QuotaOverride  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_077` | Operation  
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

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
