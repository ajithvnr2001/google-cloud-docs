---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_cloudsupport_v2beta/
title: Class /GOOG/CL_CLOUDSUPPORT_V2BETA \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:00:54.965242+00:00
---

# Class /GOOG/CL_CLOUDSUPPORT_V2BETA  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_cloudsupport_v2beta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_CLOUDSUPPORT_V2BETA Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_cloudsupport_v2beta)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_cloudsupport_v2beta)



## Class
    
    
    /GOOG/CL_CLOUDSUPPORT_V2BETA

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Google Cloud Support API v2beta`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `Actor` | PUBLIC  
`TY_002` | `Attachment` | PUBLIC  
`TY_003` | `Blobstore2Info` | PUBLIC  
`TY_004` | `Case` | PUBLIC  
`TY_005` | `CaseClassification` | PUBLIC  
`TY_007` | `Comment` | PUBLIC  
`TY_008` | `CompositeMedia` | PUBLIC  
`TY_009` | `ContentTypeInfo` | PUBLIC  
`TY_010` | `CreateAttachmentRequest` | PUBLIC  
`TY_011` | `DiffChecksumsResponse` | PUBLIC  
`TY_012` | `DiffDownloadResponse` | PUBLIC  
`TY_013` | `DiffUploadRequest` | PUBLIC  
`TY_014` | `DiffUploadResponse` | PUBLIC  
`TY_015` | `DiffVersionResponse` | PUBLIC  
`TY_016` | `DownloadParameters` | PUBLIC  
`TY_017` | `EmailMessage` | PUBLIC  
`TY_018` | `EscalateCaseRequest` | PUBLIC  
`TY_019` | `Escalation` | PUBLIC  
`TY_020` | `FeedItem` | PUBLIC  
`TY_021` | `ListAttachmentsResponse` | PUBLIC  
`TY_022` | `ListCasesResponse` | PUBLIC  
`TY_023` | `ListCommentsResponse` | PUBLIC  
`TY_024` | `Media` | PUBLIC  
`TY_025` | `ObjectId` | PUBLIC  
`TY_026` | `Product` | PUBLIC  
`TY_027` | `SearchCaseClassificationsResponse` | PUBLIC  
`TY_028` | `SearchCasesResponse` | PUBLIC  
`TY_029` | `ShowFeedResponse` | PUBLIC  
`TY_030` | `TextContent` | PUBLIC  
`TY_T_002` | `Attachment` | PUBLIC  
`TY_T_004` | `Case` | PUBLIC  
`TY_T_005` | `CaseClassification` | PUBLIC  
`TY_T_007` | `Comment` | PUBLIC  
`TY_T_008` | `CompositeMedia` | PUBLIC  
`TY_T_020` | `FeedItem` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250305 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://cloudsupport.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | cloudsupport:v2beta | PUBLIC  
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
  
### CLOSE_CASES

  * Description: cloudsupport.cases.close 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_V2BETA_ID` | IMPORTING | `STRING` | v2betaId  
`IV_P_V2BETA_ID1` | IMPORTING | `STRING` | v2betaId1  
`IV_P_CASES_ID` | IMPORTING | `STRING` | casesId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_004` | Case  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_CASES

  * Description: cloudsupport.cases.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_V2BETA_ID` | IMPORTING | `STRING` | v2betaId  
`IV_P_V2BETA_ID1` | IMPORTING | `STRING` | v2betaId1  
`IS_INPUT` | IMPORTING | `TY_004` | Case  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_004` | Case  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_COMMENTS

  * Description: cloudsupport.cases.comments.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_V2BETA_ID` | IMPORTING | `STRING` | v2betaId  
`IV_P_V2BETA_ID1` | IMPORTING | `STRING` | v2betaId1  
`IV_P_CASES_ID` | IMPORTING | `STRING` | casesId  
`IS_INPUT` | IMPORTING | `TY_007` | Comment  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | Comment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DOWNLOAD_MEDIA

  * Description: cloudsupport.media.download 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_V2BETA_ID` | IMPORTING | `STRING` | v2betaId  
`IV_P_V2BETA_ID1` | IMPORTING | `STRING` | v2betaId1  
`IV_P_CASES_ID` | IMPORTING | `STRING` | casesId  
`IV_P_ATTACHMENTS_ID` | IMPORTING | `STRING` | attachmentsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_024` | Media  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### ESCALATE_CASES

  * Description: cloudsupport.cases.escalate 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_V2BETA_ID` | IMPORTING | `STRING` | v2betaId  
`IV_P_V2BETA_ID1` | IMPORTING | `STRING` | v2betaId1  
`IV_P_CASES_ID` | IMPORTING | `STRING` | casesId  
`IS_INPUT` | IMPORTING | `TY_018` | EscalateCaseRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_004` | Case  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CASES

  * Description: cloudsupport.cases.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_V2BETA_ID` | IMPORTING | `STRING` | v2betaId  
`IV_P_V2BETA_ID1` | IMPORTING | `STRING` | v2betaId1  
`IV_P_CASES_ID` | IMPORTING | `STRING` | casesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_004` | Case  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_ATTACHMENTS

  * Description: cloudsupport.cases.attachments.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_V2BETA_ID` | IMPORTING | `STRING` | v2betaId  
`IV_P_V2BETA_ID1` | IMPORTING | `STRING` | v2betaId1  
`IV_P_CASES_ID` | IMPORTING | `STRING` | casesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_021` | ListAttachmentsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_CASES

  * Description: cloudsupport.cases.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_PRODUCTLINE` | IMPORTING | `STRING` | productLine  
`IV_P_V2BETA_ID` | IMPORTING | `STRING` | v2betaId  
`IV_P_V2BETA_ID1` | IMPORTING | `STRING` | v2betaId1  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | ListCasesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_COMMENTS

  * Description: cloudsupport.cases.comments.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_V2BETA_ID` | IMPORTING | `STRING` | v2betaId  
`IV_P_V2BETA_ID1` | IMPORTING | `STRING` | v2betaId1  
`IV_P_CASES_ID` | IMPORTING | `STRING` | casesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_023` | ListCommentsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_CASES

  * Description: cloudsupport.cases.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_V2BETA_ID` | IMPORTING | `STRING` | v2betaId  
`IV_P_V2BETA_ID1` | IMPORTING | `STRING` | v2betaId1  
`IV_P_CASES_ID` | IMPORTING | `STRING` | casesId  
`IS_INPUT` | IMPORTING | `TY_004` | Case  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_004` | Case  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SEARCH_CASES

  * Description: cloudsupport.cases.search 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_PARENT` | IMPORTING | `STRING` | parent  
`IV_Q_QUERY` | IMPORTING | `STRING` | query  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_028` | SearchCasesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SEARCH_CASE_CLASSIFICATIONS

  * Description: cloudsupport.caseClassifications.search 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_PRODUCTPRODUCTLINE` | IMPORTING | `STRING` | product.productLine  
`IV_Q_QUERY` | IMPORTING | `STRING` | query  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_027` | SearchCaseClassificationsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SHOW_FEED_CASES

  * Description: cloudsupport.cases.showFeed 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ORDERBY` | IMPORTING | `STRING` | orderBy  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_V2BETA_ID` | IMPORTING | `STRING` | v2betaId  
`IV_P_V2BETA_ID1` | IMPORTING | `STRING` | v2betaId1  
`IV_P_CASES_ID` | IMPORTING | `STRING` | casesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_029` | ShowFeedResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPLOAD_MEDIA

  * Description: cloudsupport.media.upload 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_V2BETA_ID` | IMPORTING | `STRING` | v2betaId  
`IV_P_V2BETA_ID1` | IMPORTING | `STRING` | v2betaId1  
`IV_P_CASES_ID` | IMPORTING | `STRING` | casesId  
`IS_INPUT` | IMPORTING | `TY_010` | CreateAttachmentRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | Attachment  
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
