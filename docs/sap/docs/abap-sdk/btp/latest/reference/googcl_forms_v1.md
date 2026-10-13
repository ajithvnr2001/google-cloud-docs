---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_forms_v1/
title: Class /GOOG/CL_FORMS_V1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:31.657311+00:00
---

# Class /GOOG/CL_FORMS_V1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_forms_v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_FORMS_V1 Stay organized with collections  Save and categorize content based on your preferences. 

SAP BTP edition v1.1keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_forms_v1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_forms_v1)



## Class
    
    
    /GOOG/CL_FORMS_V1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Google Forms API v1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `Answer` | PUBLIC  
`TY_002` | `BatchUpdateFormRequest` | PUBLIC  
`TY_003` | `BatchUpdateFormResponse` | PUBLIC  
`TY_004` | `ChoiceQuestion` | PUBLIC  
`TY_005` | `CloudPubsubTopic` | PUBLIC  
`TY_006` | `CorrectAnswer` | PUBLIC  
`TY_007` | `CorrectAnswers` | PUBLIC  
`TY_008` | `CreateItemRequest` | PUBLIC  
`TY_009` | `CreateItemResponse` | PUBLIC  
`TY_010` | `CreateWatchRequest` | PUBLIC  
`TY_011` | `DateQuestion` | PUBLIC  
`TY_012` | `DeleteItemRequest` | PUBLIC  
`TY_014` | `ExtraMaterial` | PUBLIC  
`TY_015` | `Feedback` | PUBLIC  
`TY_016` | `FileUploadAnswer` | PUBLIC  
`TY_017` | `FileUploadAnswers` | PUBLIC  
`TY_018` | `FileUploadQuestion` | PUBLIC  
`TY_019` | `Form` | PUBLIC  
`TY_020` | `FormResponse` | PUBLIC  
`TY_021` | `FormSettings` | PUBLIC  
`TY_022` | `Grade` | PUBLIC  
`TY_023` | `Grading` | PUBLIC  
`TY_024` | `Grid` | PUBLIC  
`TY_025` | `Image` | PUBLIC  
`TY_026` | `ImageItem` | PUBLIC  
`TY_027` | `Info` | PUBLIC  
`TY_028` | `Item` | PUBLIC  
`TY_029` | `ListFormResponsesResponse` | PUBLIC  
`TY_030` | `ListWatchesResponse` | PUBLIC  
`TY_031` | `Location` | PUBLIC  
`TY_032` | `MediaProperties` | PUBLIC  
`TY_033` | `MoveItemRequest` | PUBLIC  
`TY_034` | `Option` | PUBLIC  
`TY_036` | `Question` | PUBLIC  
`TY_037` | `QuestionGroupItem` | PUBLIC  
`TY_038` | `QuestionItem` | PUBLIC  
`TY_039` | `QuizSettings` | PUBLIC  
`TY_041` | `Request` | PUBLIC  
`TY_042` | `Response` | PUBLIC  
`TY_043` | `RowQuestion` | PUBLIC  
`TY_044` | `ScaleQuestion` | PUBLIC  
`TY_045` | `TextAnswer` | PUBLIC  
`TY_046` | `TextAnswers` | PUBLIC  
`TY_048` | `TextLink` | PUBLIC  
`TY_049` | `TextQuestion` | PUBLIC  
`TY_050` | `TimeQuestion` | PUBLIC  
`TY_051` | `UpdateFormInfoRequest` | PUBLIC  
`TY_052` | `UpdateItemRequest` | PUBLIC  
`TY_053` | `UpdateSettingsRequest` | PUBLIC  
`TY_054` | `Video` | PUBLIC  
`TY_055` | `VideoItem` | PUBLIC  
`TY_056` | `VideoLink` | PUBLIC  
`TY_057` | `Watch` | PUBLIC  
`TY_058` | `WatchTarget` | PUBLIC  
`TY_059` | `WriteControl` | PUBLIC  
`TY_T_006` | `CorrectAnswer` | PUBLIC  
`TY_T_014` | `ExtraMaterial` | PUBLIC  
`TY_T_016` | `FileUploadAnswer` | PUBLIC  
`TY_T_020` | `FormResponse` | PUBLIC  
`TY_T_028` | `Item` | PUBLIC  
`TY_T_034` | `Option` | PUBLIC  
`TY_T_036` | `Question` | PUBLIC  
`TY_T_041` | `Request` | PUBLIC  
`TY_T_042` | `Response` | PUBLIC  
`TY_T_045` | `TextAnswer` | PUBLIC  
`TY_T_057` | `Watch` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version | 1.1 | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20241029 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://forms.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | forms:v1 | PUBLIC  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | OOOOWW | PUBLIC  
  
## Methods

For general information about a method in ABAP SDK for Google Cloud, see [API method](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/developer#api_method). 

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
  
### BATCH_UPDATE_FORMS

  * Description: forms.forms.batchUpdate 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FORM_ID` | IMPORTING | `STRING` | formId  
`IS_INPUT` | IMPORTING | `TY_002` | BatchUpdateFormRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | BatchUpdateFormResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_FORMS

  * Description: forms.forms.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_019` | Form  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_019` | Form  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_WATCHES

  * Description: forms.forms.watches.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FORM_ID` | IMPORTING | `STRING` | formId  
`IS_INPUT` | IMPORTING | `TY_010` | CreateWatchRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_057` | Watch  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_WATCHES

  * Description: forms.forms.watches.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FORM_ID` | IMPORTING | `STRING` | formId  
`IV_P_WATCH_ID` | IMPORTING | `STRING` | watchId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_FORMS

  * Description: forms.forms.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FORM_ID` | IMPORTING | `STRING` | formId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_019` | Form  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_RESPONSES

  * Description: forms.forms.responses.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FORM_ID` | IMPORTING | `STRING` | formId  
`IV_P_RESPONSE_ID` | IMPORTING | `STRING` | responseId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_020` | FormResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_RESPONSES

  * Description: forms.forms.responses.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_FORM_ID` | IMPORTING | `STRING` | formId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_029` | ListFormResponsesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_WATCHES

  * Description: forms.forms.watches.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FORM_ID` | IMPORTING | `STRING` | formId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_030` | ListWatchesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RENEW_WATCHES

  * Description: forms.forms.watches.renew 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FORM_ID` | IMPORTING | `STRING` | formId  
`IV_P_WATCH_ID` | IMPORTING | `STRING` | watchId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_057` | Watch  
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
