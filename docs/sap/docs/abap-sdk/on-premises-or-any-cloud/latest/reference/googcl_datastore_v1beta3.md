---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_datastore_v1beta3/
title: Class /GOOG/CL_DATASTORE_V1BETA3 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:14:14.945625+00:00
---

# Class /GOOG/CL_DATASTORE_V1BETA3  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_datastore_v1beta3/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_DATASTORE_V1BETA3 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_datastore_v1beta3)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_datastore_v1beta3)



## Class
    
    
    /GOOG/CL_DATASTORE_V1BETA3

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Cloud Datastore API v1beta3`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `Aggregation` | PUBLIC  
`TY_002` | `AggregationQuery` | PUBLIC  
`TY_003` | `AggregationResult` | PUBLIC  
`TY_004` | `AggregationResultBatch` | PUBLIC  
`TY_005` | `AllocateIdsRequest` | PUBLIC  
`TY_006` | `AllocateIdsResponse` | PUBLIC  
`TY_008` | `Avg` | PUBLIC  
`TY_009` | `BeginTransactionRequest` | PUBLIC  
`TY_010` | `BeginTransactionResponse` | PUBLIC  
`TY_011` | `CommitRequest` | PUBLIC  
`TY_012` | `CommitResponse` | PUBLIC  
`TY_014` | `Count` | PUBLIC  
`TY_015` | `Entity` | PUBLIC  
`TY_016` | `EntityResult` | PUBLIC  
`TY_017` | `ExecutionStats` | PUBLIC  
`TY_018` | `ExplainMetrics` | PUBLIC  
`TY_019` | `ExplainOptions` | PUBLIC  
`TY_029` | `GqlQuery` | PUBLIC  
`TY_030` | `GqlQueryParameter` | PUBLIC  
`TY_031` | `Key` | PUBLIC  
`TY_032` | `KindExpression` | PUBLIC  
`TY_033` | `LatLng` | PUBLIC  
`TY_034` | `LookupRequest` | PUBLIC  
`TY_035` | `LookupResponse` | PUBLIC  
`TY_036` | `Mutation` | PUBLIC  
`TY_037` | `MutationResult` | PUBLIC  
`TY_038` | `PartitionId` | PUBLIC  
`TY_039` | `PathElement` | PUBLIC  
`TY_040` | `PlanSummary` | PUBLIC  
`TY_041` | `Projection` | PUBLIC  
`TY_043` | `PropertyMask` | PUBLIC  
`TY_044` | `PropertyOrder` | PUBLIC  
`TY_045` | `PropertyReference` | PUBLIC  
`TY_046` | `Query` | PUBLIC  
`TY_047` | `QueryResultBatch` | PUBLIC  
`TY_048` | `ReadOnly` | PUBLIC  
`TY_049` | `ReadOptions` | PUBLIC  
`TY_050` | `ReadWrite` | PUBLIC  
`TY_051` | `ReserveIdsRequest` | PUBLIC  
`TY_053` | `RollbackRequest` | PUBLIC  
`TY_055` | `RunAggregationQueryRequest` | PUBLIC  
`TY_056` | `RunAggregationQueryResponse` | PUBLIC  
`TY_057` | `RunQueryRequest` | PUBLIC  
`TY_058` | `RunQueryResponse` | PUBLIC  
`TY_059` | `Sum` | PUBLIC  
`TY_060` | `TransactionOptions` | PUBLIC  
`TY_061` | `Value` | PUBLIC  
`TY_062` | `FindNearest` | PUBLIC  
`TY_063` | `PropertyTransform` | PUBLIC  
`TY_T_001` | `Aggregation` | PUBLIC  
`TY_T_003` | `AggregationResult` | PUBLIC  
`TY_T_016` | `EntityResult` | PUBLIC  
`TY_T_030` | `GqlQueryParameter` | PUBLIC  
`TY_T_031` | `Key` | PUBLIC  
`TY_T_032` | `KindExpression` | PUBLIC  
`TY_T_036` | `Mutation` | PUBLIC  
`TY_T_037` | `MutationResult` | PUBLIC  
`TY_T_039` | `PathElement` | PUBLIC  
`TY_T_041` | `Projection` | PUBLIC  
`TY_T_044` | `PropertyOrder` | PUBLIC  
`TY_T_045` | `PropertyReference` | PUBLIC  
`TY_T_061` | `Value` | PUBLIC  
`TY_T_063` | `PropertyTransform` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250226 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://datastore.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | datastore:v1beta3 | PUBLIC  
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
  
### ALLOCATE_IDS_PROJECTS

  * Description: datastore.projects.allocateIds 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECT_ID` | IMPORTING | `STRING` | projectId  
`IS_INPUT` | IMPORTING | `TY_005` | AllocateIdsRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_006` | AllocateIdsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### BEGIN_TRANSACTION_PROJECTS

  * Description: datastore.projects.beginTransaction 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECT_ID` | IMPORTING | `STRING` | projectId  
`IS_INPUT` | IMPORTING | `TY_009` | BeginTransactionRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | BeginTransactionResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### COMMIT_PROJECTS

  * Description: datastore.projects.commit 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECT_ID` | IMPORTING | `STRING` | projectId  
`IS_INPUT` | IMPORTING | `TY_011` | CommitRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | CommitResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LOOKUP_PROJECTS

  * Description: datastore.projects.lookup 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECT_ID` | IMPORTING | `STRING` | projectId  
`IS_INPUT` | IMPORTING | `TY_034` | LookupRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_035` | LookupResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RESERVE_IDS_PROJECTS

  * Description: datastore.projects.reserveIds 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECT_ID` | IMPORTING | `STRING` | projectId  
`IS_INPUT` | IMPORTING | `TY_051` | ReserveIdsRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### ROLLBACK_PROJECTS

  * Description: datastore.projects.rollback 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECT_ID` | IMPORTING | `STRING` | projectId  
`IS_INPUT` | IMPORTING | `TY_053` | RollbackRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RUN_AGGREGATION_QUERY_PROJE

  * Description: datastore.projects.runAggregationQuery 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECT_ID` | IMPORTING | `STRING` | projectId  
`IS_INPUT` | IMPORTING | `TY_055` | RunAggregationQueryRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_056` | RunAggregationQueryResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RUN_QUERY_PROJECTS

  * Description: datastore.projects.runQuery 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECT_ID` | IMPORTING | `STRING` | projectId  
`IS_INPUT` | IMPORTING | `TY_057` | RunQueryRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_058` | RunQueryResponse  
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
