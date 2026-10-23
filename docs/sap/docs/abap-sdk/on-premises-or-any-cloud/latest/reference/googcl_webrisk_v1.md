---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_webrisk_v1/
title: Class /GOOG/CL_WEBRISK_V1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:01:33.610613+00:00
---

# Class /GOOG/CL_WEBRISK_V1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_webrisk_v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_WEBRISK_V1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_webrisk_v1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_webrisk_v1)



## Class
    
    
    /GOOG/CL_WEBRISK_V1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Web Risk API v1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `GoogleCloudWebriskV1ComputeThreatListDiffResponse` | PUBLIC  
`TY_002` | `GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksum` | PUBLIC  
`TY_003` | `GoogleCloudWebriskV1RawHashes` | PUBLIC  
`TY_004` | `GoogleCloudWebriskV1RawIndices` | PUBLIC  
`TY_005` | `GoogleCloudWebriskV1RiceDeltaEncoding` | PUBLIC  
`TY_006` | `GoogleCloudWebriskV1SearchHashesResponse` | PUBLIC  
`TY_007` | `GoogleCloudWebriskV1SearchHashesResponseThreatHash` | PUBLIC  
`TY_008` | `GoogleCloudWebriskV1SearchUrisResponse` | PUBLIC  
`TY_009` | `GoogleCloudWebriskV1SearchUrisResponseThreatUri` | PUBLIC  
`TY_010` | `GoogleCloudWebriskV1Submission` | PUBLIC  
`TY_011` | `GoogleCloudWebriskV1ThreatEntryAdditions` | PUBLIC  
`TY_012` | `GoogleCloudWebriskV1ThreatEntryRemovals` | PUBLIC  
`TY_014` | `GoogleLongrunningListOperationsResponse` | PUBLIC  
`TY_015` | `GoogleLongrunningOperation` | PUBLIC  
`TY_017` | `GoogleRpcStatus` | PUBLIC  
`TY_T_003` | `GoogleCloudWebriskV1RawHashes` | PUBLIC  
`TY_T_007` | `GoogleCloudWebriskV1SearchHashesResponseThreatHash` | PUBLIC  
`TY_T_015` | `GoogleLongrunningOperation` | PUBLIC  
`TY_T_INT4` | `Table of Integers` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | webrisk:v1 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://webrisk.googleapis.com | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250302 | PUBLIC  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.10 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
  
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
  
### CANCEL_OPERATIONS

  * Description: webrisk.projects.operations.cancel 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_OPERATIONS_ID` | IMPORTING | `STRING` | operationsId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### COMPUTE_DIFF_THREAT_LISTS

  * Description: webrisk.threatLists.computeDiff 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_CONSTRAINTSMAXDATABASEENT` | IMPORTING | `STRING` | constraints.maxDatabaseEntries  
`IV_Q_CONSTRAINTSMAXDIFFENTRIES` | IMPORTING | `STRING` | constraints.maxDiffEntries  
`IV_Q_CONSTRAINTSSUPPORTEDCOMPR` | IMPORTING | `STRING` | constraints.supportedCompressions  
`IV_Q_THREATTYPE` | IMPORTING | `STRING` | threatType  
`IV_Q_VERSIONTOKEN` | IMPORTING | `STRING` | versionToken  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | GoogleCloudWebriskV1ComputeThreatListDiffResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_SUBMISSIONS

  * Description: webrisk.projects.submissions.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IS_INPUT` | IMPORTING | `TY_010` | GoogleCloudWebriskV1Submission  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | GoogleCloudWebriskV1Submission  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_OPERATIONS

  * Description: webrisk.projects.operations.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_OPERATIONS_ID` | IMPORTING | `STRING` | operationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_OPERATIONS

  * Description: webrisk.projects.operations.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_OPERATIONS_ID` | IMPORTING | `STRING` | operationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_015` | GoogleLongrunningOperation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_OPERATIONS

  * Description: webrisk.projects.operations.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_014` | GoogleLongrunningListOperationsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SEARCH_HASHES

  * Description: webrisk.hashes.search 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_HASHPREFIX` | IMPORTING | `STRING` | hashPrefix  
`IV_Q_THREATTYPES` | IMPORTING | `STRING` | threatTypes  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_006` | GoogleCloudWebriskV1SearchHashesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SEARCH_URIS

  * Description: webrisk.uris.search 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_THREATTYPES` | IMPORTING | `STRING` | threatTypes  
`IV_Q_URI` | IMPORTING | `STRING` | uri  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_008` | GoogleCloudWebriskV1SearchUrisResponse  
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
