---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_servicecontrol_v1/
title: Class /GOOG/CL_SERVICECONTROL_V1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:42.643299+00:00
---

# Class /GOOG/CL_SERVICECONTROL_V1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_servicecontrol_v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_SERVICECONTROL_V1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_servicecontrol_v1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_servicecontrol_v1)



## Class
    
    
    /GOOG/CL_SERVICECONTROL_V1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Service Control API v1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `AllocateInfo` | PUBLIC  
`TY_002` | `AllocateQuotaRequest` | PUBLIC  
`TY_003` | `AllocateQuotaResponse` | PUBLIC  
`TY_004` | `AttributeValue` | PUBLIC  
`TY_005` | `Attributes` | PUBLIC  
`TY_009` | `CheckError` | PUBLIC  
`TY_010` | `CheckInfo` | PUBLIC  
`TY_011` | `CheckRequest` | PUBLIC  
`TY_012` | `CheckResponse` | PUBLIC  
`TY_013` | `ConsumerInfo` | PUBLIC  
`TY_014` | `Distribution` | PUBLIC  
`TY_015` | `Exemplar` | PUBLIC  
`TY_016` | `ExplicitBuckets` | PUBLIC  
`TY_017` | `ExponentialBuckets` | PUBLIC  
`TY_019` | `HttpRequest` | PUBLIC  
`TY_020` | `LinearBuckets` | PUBLIC  
`TY_021` | `LogEntry` | PUBLIC  
`TY_022` | `LogEntryOperation` | PUBLIC  
`TY_023` | `LogEntrySourceLocation` | PUBLIC  
`TY_024` | `MetricValue` | PUBLIC  
`TY_025` | `MetricValueSet` | PUBLIC  
`TY_026` | `Money` | PUBLIC  
`TY_027` | `Operation` | PUBLIC  
`TY_031` | `QuotaError` | PUBLIC  
`TY_032` | `QuotaInfo` | PUBLIC  
`TY_033` | `QuotaOperation` | PUBLIC  
`TY_034` | `QuotaProperties` | PUBLIC  
`TY_035` | `ReportError` | PUBLIC  
`TY_036` | `ReportRequest` | PUBLIC  
`TY_037` | `ReportResponse` | PUBLIC  
`TY_041` | `ResourceInfo` | PUBLIC  
`TY_046` | `Status` | PUBLIC  
`TY_048` | `TraceSpan` | PUBLIC  
`TY_049` | `TruncatableString` | PUBLIC  
`TY_T_009` | `CheckError` | PUBLIC  
`TY_T_015` | `Exemplar` | PUBLIC  
`TY_T_021` | `LogEntry` | PUBLIC  
`TY_T_024` | `MetricValue` | PUBLIC  
`TY_T_025` | `MetricValueSet` | PUBLIC  
`TY_T_027` | `Operation` | PUBLIC  
`TY_T_031` | `QuotaError` | PUBLIC  
`TY_T_035` | `ReportError` | PUBLIC  
`TY_T_041` | `ResourceInfo` | PUBLIC  
`TY_T_048` | `TraceSpan` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
`TY _T_ /GOOG/NUM_DOUBLE` | `` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.10 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250228 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://servicecontrol.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | servicecontrol:v1 | PUBLIC  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
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
  
### ALLOCATE_QUOTA_SERVICES

  * Description: servicecontrol.services.allocateQuota 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SERVICE_NAME` | IMPORTING | `STRING` | serviceName  
`IS_INPUT` | IMPORTING | `TY_002` | AllocateQuotaRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | AllocateQuotaResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CHECK_SERVICES

  * Description: servicecontrol.services.check 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SERVICE_NAME` | IMPORTING | `STRING` | serviceName  
`IS_INPUT` | IMPORTING | `TY_011` | CheckRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | CheckResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REPORT_SERVICES

  * Description: servicecontrol.services.report 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SERVICE_NAME` | IMPORTING | `STRING` | serviceName  
`IS_INPUT` | IMPORTING | `TY_036` | ReportRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_037` | ReportResponse  
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
