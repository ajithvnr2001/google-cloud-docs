---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_fitness_v1/
title: Class /GOOG/CL_FITNESS_V1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:00:46.281821+00:00
---

# Class /GOOG/CL_FITNESS_V1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_fitness_v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_FITNESS_V1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_fitness_v1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_fitness_v1)



## Class
    
    
    /GOOG/CL_FITNESS_V1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Fitness API v1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `AggregateBucket` | PUBLIC  
`TY_002` | `AggregateBy` | PUBLIC  
`TY_003` | `AggregateRequest` | PUBLIC  
`TY_004` | `AggregateResponse` | PUBLIC  
`TY_005` | `Application` | PUBLIC  
`TY_006` | `BucketByActivity` | PUBLIC  
`TY_007` | `BucketBySession` | PUBLIC  
`TY_008` | `BucketByTime` | PUBLIC  
`TY_009` | `BucketByTimePeriod` | PUBLIC  
`TY_010` | `DataPoint` | PUBLIC  
`TY_011` | `DataSource` | PUBLIC  
`TY_012` | `DataType` | PUBLIC  
`TY_013` | `DataTypeField` | PUBLIC  
`TY_014` | `Dataset` | PUBLIC  
`TY_015` | `Device` | PUBLIC  
`TY_016` | `ListDataPointChangesResponse` | PUBLIC  
`TY_017` | `ListDataSourcesResponse` | PUBLIC  
`TY_018` | `ListSessionsResponse` | PUBLIC  
`TY_019` | `MapValue` | PUBLIC  
`TY_020` | `Session` | PUBLIC  
`TY_021` | `Value` | PUBLIC  
`TY_022` | `ValueMapValEntry` | PUBLIC  
`TY_T_001` | `AggregateBucket` | PUBLIC  
`TY_T_002` | `AggregateBy` | PUBLIC  
`TY_T_010` | `DataPoint` | PUBLIC  
`TY_T_011` | `DataSource` | PUBLIC  
`TY_T_013` | `DataTypeField` | PUBLIC  
`TY_T_014` | `Dataset` | PUBLIC  
`TY_T_020` | `Session` | PUBLIC  
`TY_T_021` | `Value` | PUBLIC  
`TY_T_022` | `ValueMapValEntry` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250305 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://fitness.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | fitness:v1 | PUBLIC  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix | /fitness/v1/users/ | PUBLIC  
  
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
  
### AGGREGATE_DATASET

  * Description: fitness.users.dataset.aggregate 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_USER_ID` | IMPORTING | `STRING` | userId  
`IS_INPUT` | IMPORTING | `TY_003` | AggregateRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_004` | AggregateResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_DATA_SOURCES

  * Description: fitness.users.dataSources.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_USER_ID` | IMPORTING | `STRING` | userId  
`IS_INPUT` | IMPORTING | `TY_011` | DataSource  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | DataSource  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_DATASETS

  * Description: fitness.users.dataSources.datasets.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_DATA_SOURCE_ID` | IMPORTING | `STRING` | dataSourceId  
`IV_P_DATASET_ID` | IMPORTING | `STRING` | datasetId  
`IV_P_USER_ID` | IMPORTING | `STRING` | userId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_DATA_SOURCES

  * Description: fitness.users.dataSources.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_DATA_SOURCE_ID` | IMPORTING | `STRING` | dataSourceId  
`IV_P_USER_ID` | IMPORTING | `STRING` | userId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | DataSource  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_SESSIONS

  * Description: fitness.users.sessions.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SESSION_ID` | IMPORTING | `STRING` | sessionId  
`IV_P_USER_ID` | IMPORTING | `STRING` | userId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_DATASETS

  * Description: fitness.users.dataSources.datasets.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_LIMIT` | IMPORTING | `STRING` | limit  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_DATA_SOURCE_ID` | IMPORTING | `STRING` | dataSourceId  
`IV_P_DATASET_ID` | IMPORTING | `STRING` | datasetId  
`IV_P_USER_ID` | IMPORTING | `STRING` | userId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_014` | Dataset  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_DATA_SOURCES

  * Description: fitness.users.dataSources.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_DATA_SOURCE_ID` | IMPORTING | `STRING` | dataSourceId  
`IV_P_USER_ID` | IMPORTING | `STRING` | userId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | DataSource  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_DATA_POINT_CHANGES

  * Description: fitness.users.dataSources.dataPointChanges.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_LIMIT` | IMPORTING | `STRING` | limit  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_DATA_SOURCE_ID` | IMPORTING | `STRING` | dataSourceId  
`IV_P_USER_ID` | IMPORTING | `STRING` | userId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_016` | ListDataPointChangesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_DATA_SOURCES

  * Description: fitness.users.dataSources.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_DATATYPENAME` | IMPORTING | `STRING` | dataTypeName  
`IV_P_USER_ID` | IMPORTING | `STRING` | userId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | ListDataSourcesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_SESSIONS

  * Description: fitness.users.sessions.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ACTIVITYTYPE` | IMPORTING | `STRING` | activityType  
`IV_Q_ENDTIME` | IMPORTING | `STRING` | endTime  
`IV_Q_INCLUDEDELETED` | IMPORTING | `STRING` | includeDeleted  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_STARTTIME` | IMPORTING | `STRING` | startTime  
`IV_P_USER_ID` | IMPORTING | `STRING` | userId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_018` | ListSessionsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_DATASETS

  * Description: fitness.users.dataSources.datasets.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_DATA_SOURCE_ID` | IMPORTING | `STRING` | dataSourceId  
`IV_P_DATASET_ID` | IMPORTING | `STRING` | datasetId  
`IV_P_USER_ID` | IMPORTING | `STRING` | userId  
`IS_INPUT` | IMPORTING | `TY_014` | Dataset  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_014` | Dataset  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_DATA_SOURCES

  * Description: fitness.users.dataSources.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_DATA_SOURCE_ID` | IMPORTING | `STRING` | dataSourceId  
`IV_P_USER_ID` | IMPORTING | `STRING` | userId  
`IS_INPUT` | IMPORTING | `TY_011` | DataSource  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | DataSource  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_SESSIONS

  * Description: fitness.users.sessions.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SESSION_ID` | IMPORTING | `STRING` | sessionId  
`IV_P_USER_ID` | IMPORTING | `STRING` | userId  
`IS_INPUT` | IMPORTING | `TY_020` | Session  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_020` | Session  
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
