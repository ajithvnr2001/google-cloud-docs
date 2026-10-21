---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_datastore_v1/
title: Class /GOOG/CL_DATASTORE_V1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:14:14.726256+00:00
---

# Class /GOOG/CL_DATASTORE_V1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_datastore_v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_DATASTORE_V1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_datastore_v1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_datastore_v1)



## Class
    
    
    /GOOG/CL_DATASTORE_V1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Cloud Datastore API v1`

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
`TY_008` | `BeginTransactionRequest` | PUBLIC  
`TY_009` | `BeginTransactionResponse` | PUBLIC  
`TY_010` | `CommitRequest` | PUBLIC  
`TY_011` | `CommitResponse` | PUBLIC  
`TY_013` | `Count` | PUBLIC  
`TY_015` | `Entity` | PUBLIC  
`TY_016` | `EntityResult` | PUBLIC  
`TY_019` | `GoogleDatastoreAdminV1EntityFilter` | PUBLIC  
`TY_020` | `GoogleDatastoreAdminV1ExportEntitiesRequest` | PUBLIC  
`TY_021` | `GoogleDatastoreAdminV1ImportEntitiesRequest` | PUBLIC  
`TY_022` | `GoogleDatastoreAdminV1Index` | PUBLIC  
`TY_023` | `GoogleDatastoreAdminV1IndexedProperty` | PUBLIC  
`TY_024` | `GoogleDatastoreAdminV1ListIndexesResponse` | PUBLIC  
`TY_031` | `GoogleLongrunningListOperationsResponse` | PUBLIC  
`TY_032` | `GoogleLongrunningOperation` | PUBLIC  
`TY_033` | `GqlQuery` | PUBLIC  
`TY_034` | `GqlQueryParameter` | PUBLIC  
`TY_035` | `Key` | PUBLIC  
`TY_036` | `KindExpression` | PUBLIC  
`TY_037` | `LatLng` | PUBLIC  
`TY_038` | `LookupRequest` | PUBLIC  
`TY_039` | `LookupResponse` | PUBLIC  
`TY_040` | `Mutation` | PUBLIC  
`TY_041` | `MutationResult` | PUBLIC  
`TY_042` | `PartitionId` | PUBLIC  
`TY_043` | `PathElement` | PUBLIC  
`TY_044` | `Projection` | PUBLIC  
`TY_046` | `PropertyOrder` | PUBLIC  
`TY_047` | `PropertyReference` | PUBLIC  
`TY_048` | `Query` | PUBLIC  
`TY_049` | `QueryResultBatch` | PUBLIC  
`TY_050` | `ReadOnly` | PUBLIC  
`TY_051` | `ReadOptions` | PUBLIC  
`TY_052` | `ReadWrite` | PUBLIC  
`TY_053` | `ReserveIdsRequest` | PUBLIC  
`TY_055` | `RollbackRequest` | PUBLIC  
`TY_057` | `RunAggregationQueryRequest` | PUBLIC  
`TY_058` | `RunAggregationQueryResponse` | PUBLIC  
`TY_059` | `RunQueryRequest` | PUBLIC  
`TY_060` | `RunQueryResponse` | PUBLIC  
`TY_061` | `Status` | PUBLIC  
`TY_062` | `TransactionOptions` | PUBLIC  
`TY_063` | `Value` | PUBLIC  
`TY_064` | `Avg` | PUBLIC  
`TY_065` | `Sum` | PUBLIC  
`TY_066` | `ExplainOptions` | PUBLIC  
`TY_067` | `ExecutionStats` | PUBLIC  
`TY_068` | `ExplainMetrics` | PUBLIC  
`TY_069` | `PlanSummary` | PUBLIC  
`TY_070` | `PropertyMask` | PUBLIC  
`TY_071` | `FindNearest` | PUBLIC  
`TY_072` | `PropertyTransform` | PUBLIC  
`TY_T_001` | `Aggregation` | PUBLIC  
`TY_T_003` | `AggregationResult` | PUBLIC  
`TY_T_016` | `EntityResult` | PUBLIC  
`TY_T_022` | `GoogleDatastoreAdminV1Index` | PUBLIC  
`TY_T_023` | `GoogleDatastoreAdminV1IndexedProperty` | PUBLIC  
`TY_T_032` | `GoogleLongrunningOperation` | PUBLIC  
`TY_T_034` | `GqlQueryParameter` | PUBLIC  
`TY_T_035` | `Key` | PUBLIC  
`TY_T_036` | `KindExpression` | PUBLIC  
`TY_T_040` | `Mutation` | PUBLIC  
`TY_T_041` | `MutationResult` | PUBLIC  
`TY_T_043` | `PathElement` | PUBLIC  
`TY_T_044` | `Projection` | PUBLIC  
`TY_T_046` | `PropertyOrder` | PUBLIC  
`TY_T_047` | `PropertyReference` | PUBLIC  
`TY_T_063` | `Value` | PUBLIC  
`TY_T_072` | `PropertyTransform` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | datastore:v1 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://datastore.googleapis.com | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250226 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.5 | PUBLIC  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version | 1.0 | PUBLIC  
  
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
`IS_INPUT` | IMPORTING | `TY_008` | BeginTransactionRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_009` | BeginTransactionResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CANCEL_OPERATIONS

  * Description: datastore.projects.operations.cancel 
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
  
### COMMIT_PROJECTS

  * Description: datastore.projects.commit 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECT_ID` | IMPORTING | `STRING` | projectId  
`IS_INPUT` | IMPORTING | `TY_010` | CommitRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | CommitResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_INDEXES

  * Description: datastore.projects.indexes.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECT_ID` | IMPORTING | `STRING` | projectId  
`IS_INPUT` | IMPORTING | `TY_022` | GoogleDatastoreAdminV1Index  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_032` | GoogleLongrunningOperation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_INDEXES

  * Description: datastore.projects.indexes.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_INDEX_ID` | IMPORTING | `STRING` | indexId  
`IV_P_PROJECT_ID` | IMPORTING | `STRING` | projectId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_032` | GoogleLongrunningOperation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_OPERATIONS

  * Description: datastore.projects.operations.delete 
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
  
### EXPORT_PROJECTS

  * Description: datastore.projects.export 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECT_ID` | IMPORTING | `STRING` | projectId  
`IS_INPUT` | IMPORTING | `TY_020` | GoogleDatastoreAdminV1ExportEntitiesRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_032` | GoogleLongrunningOperation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_INDEXES

  * Description: datastore.projects.indexes.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_INDEX_ID` | IMPORTING | `STRING` | indexId  
`IV_P_PROJECT_ID` | IMPORTING | `STRING` | projectId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | GoogleDatastoreAdminV1Index  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_OPERATIONS

  * Description: datastore.projects.operations.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_OPERATIONS_ID` | IMPORTING | `STRING` | operationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_032` | GoogleLongrunningOperation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### IMPORT_PROJECTS

  * Description: datastore.projects.import 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECT_ID` | IMPORTING | `STRING` | projectId  
`IS_INPUT` | IMPORTING | `TY_021` | GoogleDatastoreAdminV1ImportEntitiesRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_032` | GoogleLongrunningOperation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_INDEXES

  * Description: datastore.projects.indexes.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_PROJECT_ID` | IMPORTING | `STRING` | projectId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_024` | GoogleDatastoreAdminV1ListIndexesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_OPERATIONS

  * Description: datastore.projects.operations.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_031` | GoogleLongrunningListOperationsResponse  
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
`IS_INPUT` | IMPORTING | `TY_038` | LookupRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_039` | LookupResponse  
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
`IS_INPUT` | IMPORTING | `TY_053` | ReserveIdsRequest  
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
`IS_INPUT` | IMPORTING | `TY_055` | RollbackRequest  
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
`IS_INPUT` | IMPORTING | `TY_057` | RunAggregationQueryRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_058` | RunAggregationQueryResponse  
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
`IS_INPUT` | IMPORTING | `TY_059` | RunQueryRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_060` | RunQueryResponse  
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
