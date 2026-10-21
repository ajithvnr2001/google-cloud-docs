---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_servconsmana_v1beta1/
title: Class /GOOG/CL_SERVCONSMANA_V1BETA1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:13:38.212468+00:00
---

# Class /GOOG/CL_SERVCONSMANA_V1BETA1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_servconsmana_v1beta1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_SERVCONSMANA_V1BETA1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_servconsmana_v1beta1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_servconsmana_v1beta1)



## Class
    
    
    /GOOG/CL_SERVCONSMANA_V1BETA1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Service Consumer Management API v1beta1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_051` | `Operation` | PUBLIC  
`TY_063` | `Status` | PUBLIC  
`TY_070` | `V1Beta1ConsumerQuotaLimit` | PUBLIC  
`TY_071` | `V1Beta1ConsumerQuotaMetric` | PUBLIC  
`TY_072` | `V1Beta1ImportProducerOverridesRequest` | PUBLIC  
`TY_073` | `V1Beta1ImportProducerQuotaPoliciesRequest` | PUBLIC  
`TY_074` | `V1Beta1ListConsumerQuotaMetricsResponse` | PUBLIC  
`TY_075` | `V1Beta1ListProducerOverridesResponse` | PUBLIC  
`TY_076` | `V1Beta1ListProducerQuotaPoliciesResponse` | PUBLIC  
`TY_077` | `V1Beta1OverrideInlineSource` | PUBLIC  
`TY_078` | `V1Beta1PolicyInlineSource` | PUBLIC  
`TY_079` | `V1Beta1ProducerQuotaPolicy` | PUBLIC  
`TY_080` | `V1Beta1QuotaBucket` | PUBLIC  
`TY_081` | `V1Beta1QuotaOverride` | PUBLIC  
`TY_082` | `V1Beta1RolloutInfo` | PUBLIC  
`TY_T_070` | `V1Beta1ConsumerQuotaLimit` | PUBLIC  
`TY_T_071` | `V1Beta1ConsumerQuotaMetric` | PUBLIC  
`TY_T_079` | `V1Beta1ProducerQuotaPolicy` | PUBLIC  
`TY_T_080` | `V1Beta1QuotaBucket` | PUBLIC  
`TY_T_081` | `V1Beta1QuotaOverride` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | serviceconsumermanagement:v1beta1 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://serviceconsumermanagement.googleapis.com | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250227 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.10 | PUBLIC  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
  
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
  
### CREATE_PRODUCER_OVERRIDES

  * Description: consumerQuotaMetrics.limits.producerOverrides.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FORCE` | IMPORTING | `STRING` | force  
`IV_Q_FORCEJUSTIFICATION` | IMPORTING | `STRING` | forceJustification  
`IV_Q_FORCEONLY` | IMPORTING | `STRING` | forceOnly  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_SERVICES_ID1` | IMPORTING | `STRING` | servicesId1  
`IV_P_SERVICES_ID2` | IMPORTING | `STRING` | servicesId2  
`IV_P_CONSUMER_QUOTA_METRICS_ID` | IMPORTING | `STRING` | consumerQuotaMetricsId  
`IV_P_LIMITS_ID` | IMPORTING | `STRING` | limitsId  
`IS_INPUT` | IMPORTING | `TY_081` | V1Beta1QuotaOverride  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_051` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_PRODUCER_QUOTA_POLIC

  * Description: consumerQuotaMetrics.limits.producerQuotaPolicies.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FORCE` | IMPORTING | `STRING` | force  
`IV_Q_FORCEJUSTIFICATION` | IMPORTING | `STRING` | forceJustification  
`IV_Q_VALIDATEONLY` | IMPORTING | `STRING` | validateOnly  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_SERVICES_ID1` | IMPORTING | `STRING` | servicesId1  
`IV_P_SERVICES_ID2` | IMPORTING | `STRING` | servicesId2  
`IV_P_CONSUMER_QUOTA_METRICS_ID` | IMPORTING | `STRING` | consumerQuotaMetricsId  
`IV_P_LIMITS_ID` | IMPORTING | `STRING` | limitsId  
`IS_INPUT` | IMPORTING | `TY_079` | V1Beta1ProducerQuotaPolicy  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_051` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_PRODUCER_OVERRIDES

  * Description: consumerQuotaMetrics.limits.producerOverrides.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FORCE` | IMPORTING | `STRING` | force  
`IV_Q_FORCEJUSTIFICATION` | IMPORTING | `STRING` | forceJustification  
`IV_Q_FORCEONLY` | IMPORTING | `STRING` | forceOnly  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_SERVICES_ID1` | IMPORTING | `STRING` | servicesId1  
`IV_P_SERVICES_ID2` | IMPORTING | `STRING` | servicesId2  
`IV_P_CONSUMER_QUOTA_METRICS_ID` | IMPORTING | `STRING` | consumerQuotaMetricsId  
`IV_P_LIMITS_ID` | IMPORTING | `STRING` | limitsId  
`IV_P_PRODUCER_OVERRIDES_ID` | IMPORTING | `STRING` | producerOverridesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_051` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_PRODUCER_QUOTA_POLIC

  * Description: consumerQuotaMetrics.limits.producerQuotaPolicies.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FORCE` | IMPORTING | `STRING` | force  
`IV_Q_FORCEJUSTIFICATION` | IMPORTING | `STRING` | forceJustification  
`IV_Q_VALIDATEONLY` | IMPORTING | `STRING` | validateOnly  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_SERVICES_ID1` | IMPORTING | `STRING` | servicesId1  
`IV_P_SERVICES_ID2` | IMPORTING | `STRING` | servicesId2  
`IV_P_CONSUMER_QUOTA_METRICS_ID` | IMPORTING | `STRING` | consumerQuotaMetricsId  
`IV_P_LIMITS_ID` | IMPORTING | `STRING` | limitsId  
`IV_P_PRODUCER_QUOTA_POLICIES_I` | IMPORTING | `STRING` | producerQuotaPoliciesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_051` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CONSUMER_QUOTA_METRICS

  * Description: serviceconsumermanagement.services.consumerQuotaMetrics.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_VIEW` | IMPORTING | `STRING` | view  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_SERVICES_ID1` | IMPORTING | `STRING` | servicesId1  
`IV_P_SERVICES_ID2` | IMPORTING | `STRING` | servicesId2  
`IV_P_CONSUMER_QUOTA_METRICS_ID` | IMPORTING | `STRING` | consumerQuotaMetricsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_071` | V1Beta1ConsumerQuotaMetric  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_LIMITS

  * Description: services.consumerQuotaMetrics.limits.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_VIEW` | IMPORTING | `STRING` | view  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_SERVICES_ID1` | IMPORTING | `STRING` | servicesId1  
`IV_P_SERVICES_ID2` | IMPORTING | `STRING` | servicesId2  
`IV_P_CONSUMER_QUOTA_METRICS_ID` | IMPORTING | `STRING` | consumerQuotaMetricsId  
`IV_P_LIMITS_ID` | IMPORTING | `STRING` | limitsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_070` | V1Beta1ConsumerQuotaLimit  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_OPERATIONS

  * Description: serviceconsumermanagement.operations.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_OPERATIONS_ID` | IMPORTING | `STRING` | operationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_051` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### IMPORT_PRODUCER_OVERRIDES_C

  * Description: services.consumerQuotaMetrics.importProducerOverrides 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_SERVICES_ID1` | IMPORTING | `STRING` | servicesId1  
`IV_P_SERVICES_ID2` | IMPORTING | `STRING` | servicesId2  
`IS_INPUT` | IMPORTING | `TY_072` | V1Beta1ImportProducerOverridesRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_051` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### IMPORT_PRODUCER_QUOTA_POLIC

  * Description: services.consumerQuotaMetrics.importProducerQuotaPolicies 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_SERVICES_ID1` | IMPORTING | `STRING` | servicesId1  
`IV_P_SERVICES_ID2` | IMPORTING | `STRING` | servicesId2  
`IS_INPUT` | IMPORTING | `TY_073` | V1Beta1ImportProducerQuotaPoliciesRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_051` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_CONSUMER_QUOTA_METRICS

  * Description: services.consumerQuotaMetrics.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_VIEW` | IMPORTING | `STRING` | view  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_SERVICES_ID1` | IMPORTING | `STRING` | servicesId1  
`IV_P_SERVICES_ID2` | IMPORTING | `STRING` | servicesId2  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_074` | V1Beta1ListConsumerQuotaMetricsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_PRODUCER_OVERRIDES

  * Description: services.consumerQuotaMetrics.limits.producerOverrides.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_SERVICES_ID1` | IMPORTING | `STRING` | servicesId1  
`IV_P_SERVICES_ID2` | IMPORTING | `STRING` | servicesId2  
`IV_P_CONSUMER_QUOTA_METRICS_ID` | IMPORTING | `STRING` | consumerQuotaMetricsId  
`IV_P_LIMITS_ID` | IMPORTING | `STRING` | limitsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_075` | V1Beta1ListProducerOverridesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_PRODUCER_QUOTA_POLICIE

  * Description: consumerQuotaMetrics.limits.producerQuotaPolicies.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_SERVICES_ID1` | IMPORTING | `STRING` | servicesId1  
`IV_P_SERVICES_ID2` | IMPORTING | `STRING` | servicesId2  
`IV_P_CONSUMER_QUOTA_METRICS_ID` | IMPORTING | `STRING` | consumerQuotaMetricsId  
`IV_P_LIMITS_ID` | IMPORTING | `STRING` | limitsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_076` | V1Beta1ListProducerQuotaPoliciesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_PRODUCER_OVERRIDES

  * Description: consumerQuotaMetrics.limits.producerOverrides.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FORCE` | IMPORTING | `STRING` | force  
`IV_Q_FORCEJUSTIFICATION` | IMPORTING | `STRING` | forceJustification  
`IV_Q_FORCEONLY` | IMPORTING | `STRING` | forceOnly  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_SERVICES_ID1` | IMPORTING | `STRING` | servicesId1  
`IV_P_SERVICES_ID2` | IMPORTING | `STRING` | servicesId2  
`IV_P_CONSUMER_QUOTA_METRICS_ID` | IMPORTING | `STRING` | consumerQuotaMetricsId  
`IV_P_LIMITS_ID` | IMPORTING | `STRING` | limitsId  
`IV_P_PRODUCER_OVERRIDES_ID` | IMPORTING | `STRING` | producerOverridesId  
`IS_INPUT` | IMPORTING | `TY_081` | V1Beta1QuotaOverride  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_051` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_PRODUCER_QUOTA_POLICI

  * Description: consumerQuotaMetrics.limits.producerQuotaPolicies.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FORCE` | IMPORTING | `STRING` | force  
`IV_Q_FORCEJUSTIFICATION` | IMPORTING | `STRING` | forceJustification  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_Q_VALIDATEONLY` | IMPORTING | `STRING` | validateOnly  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_SERVICES_ID1` | IMPORTING | `STRING` | servicesId1  
`IV_P_SERVICES_ID2` | IMPORTING | `STRING` | servicesId2  
`IV_P_CONSUMER_QUOTA_METRICS_ID` | IMPORTING | `STRING` | consumerQuotaMetricsId  
`IV_P_LIMITS_ID` | IMPORTING | `STRING` | limitsId  
`IV_P_PRODUCER_QUOTA_POLICIES_I` | IMPORTING | `STRING` | producerQuotaPoliciesId  
`IS_INPUT` | IMPORTING | `TY_079` | V1Beta1ProducerQuotaPolicy  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_051` | Operation  
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
