---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_language_v2/
title: Class /GOOG/CL_LANGUAGE_V2 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:00:13.952480+00:00
---

# Class /GOOG/CL_LANGUAGE_V2  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_language_v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_LANGUAGE_V2 Stay organized with collections  Save and categorize content based on your preferences. 

SAP BTP edition v1.1keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_language_v2)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_language_v2)



## Class
    
    
    /GOOG/CL_LANGUAGE_V2

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Cloud Natural Language API v2`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `AnalyzeEntitiesRequest` | PUBLIC  
`TY_002` | `AnalyzeEntitiesResponse` | PUBLIC  
`TY_003` | `AnalyzeSentimentRequest` | PUBLIC  
`TY_004` | `AnalyzeSentimentResponse` | PUBLIC  
`TY_005` | `AnnotateTextRequest` | PUBLIC  
`TY_006` | `AnnotateTextResponse` | PUBLIC  
`TY_007` | `ClassificationCategory` | PUBLIC  
`TY_008` | `ClassifyTextRequest` | PUBLIC  
`TY_009` | `ClassifyTextResponse` | PUBLIC  
`TY_010` | `Document` | PUBLIC  
`TY_011` | `Entity` | PUBLIC  
`TY_012` | `EntityMention` | PUBLIC  
`TY_014` | `ModerateTextRequest` | PUBLIC  
`TY_015` | `ModerateTextResponse` | PUBLIC  
`TY_016` | `Sentence` | PUBLIC  
`TY_017` | `Sentiment` | PUBLIC  
`TY_018` | `TextSpan` | PUBLIC  
`TY_019` | `AnnotateTextRequestFeatures` | PUBLIC  
`TY_T_007` | `ClassificationCategory` | PUBLIC  
`TY_T_011` | `Entity` | PUBLIC  
`TY_T_012` | `EntityMention` | PUBLIC  
`TY_T_016` | `Sentence` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | language:v2 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://language.googleapis.com | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20241117 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.5 | PUBLIC  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version | 1.0 | PUBLIC  
  
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
  
### ANALYZE_ENTITIES_DOCUMENTS

  * Description: language.documents.analyzeEntities 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_001` | AnalyzeEntitiesRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | AnalyzeEntitiesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### ANALYZE_SENTIMENT_DOCUMENTS

  * Description: language.documents.analyzeSentiment 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_003` | AnalyzeSentimentRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_004` | AnalyzeSentimentResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### ANNOTATE_TEXT_DOCUMENTS

  * Description: language.documents.annotateText 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_005` | AnnotateTextRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_006` | AnnotateTextResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CLASSIFY_TEXT_DOCUMENTS

  * Description: language.documents.classifyText 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_008` | ClassifyTextRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_009` | ClassifyTextResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MODERATE_TEXT_DOCUMENTS

  * Description: language.documents.moderateText 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_014` | ModerateTextRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_015` | ModerateTextResponse  
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
