---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_admin_datatrans/
title: Class /GOOG/CL_ADMIN_DATATRANS \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:23:52.547967+00:00
---

# Class /GOOG/CL_ADMIN_DATATRANS  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_admin_datatrans/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_ADMIN_DATATRANS Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_admin_datatrans)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_admin_datatrans)



## Class
    
    
    /GOOG/CL_ADMIN_DATATRANS

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Admin SDK API datatransfer_v1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `Application` | PUBLIC  
`TY_002` | `ApplicationDataTransfer` | PUBLIC  
`TY_003` | `ApplicationTransferParam` | PUBLIC  
`TY_004` | `ApplicationsListResponse` | PUBLIC  
`TY_005` | `DataTransfer` | PUBLIC  
`TY_006` | `DataTransfersListResponse` | PUBLIC  
`TY_T_001` | `Application` | PUBLIC  
`TY_T_002` | `ApplicationDataTransfer` | PUBLIC  
`TY_T_003` | `ApplicationTransferParam` | PUBLIC  
`TY_T_005` | `DataTransfer` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | admin:datatransfer_v1 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://admin.googleapis.com | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250304 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
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
  
### GET_APPLICATIONS

  * Description: datatransfer.applications.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_APPLICATION_ID` | IMPORTING | `STRING` | applicationId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | Application  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_TRANSFERS

  * Description: datatransfer.transfers.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_DATA_TRANSFER_ID` | IMPORTING | `STRING` | dataTransferId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | DataTransfer  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_TRANSFERS

  * Description: datatransfer.transfers.insert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_005` | DataTransfer  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | DataTransfer  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_APPLICATIONS

  * Description: datatransfer.applications.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_CUSTOMERID` | IMPORTING | `STRING` | customerId  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_004` | ApplicationsListResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_TRANSFERS

  * Description: datatransfer.transfers.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_CUSTOMERID` | IMPORTING | `STRING` | customerId  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_NEWOWNERUSERID` | IMPORTING | `STRING` | newOwnerUserId  
`IV_Q_OLDOWNERUSERID` | IMPORTING | `STRING` | oldOwnerUserId  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_STATUS` | IMPORTING | `STRING` | status  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_006` | DataTransfersListResponse  
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

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
