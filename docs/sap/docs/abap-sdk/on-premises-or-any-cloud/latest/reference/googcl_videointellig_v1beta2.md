---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_videointellig_v1beta2/
title: Class /GOOG/CL_VIDEOINTELLIG_V1BETA2 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:32.494578+00:00
---

# Class /GOOG/CL_VIDEOINTELLIG_V1BETA2  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_videointellig_v1beta2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_VIDEOINTELLIG_V1BETA2 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_videointellig_v1beta2)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_videointellig_v1beta2)



## Class
    
    
    /GOOG/CL_VIDEOINTELLIG_V1BETA2

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Cloud Video Intelligence API v1beta2`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_031` | `GoogleCloudVideointelligenceV1beta2_AnnotateVideoRequest` | PUBLIC  
`TY_036` | `GoogleCloudVideointelligenceV1beta2_ExplicitContentDetection` | PUBLIC  
`TY_040` | `GoogleCloudVideointelligenceV1beta2_FaceDetectionConfig` | PUBLIC  
`TY_044` | `GoogleCloudVideointelligenceV1beta2_LabelDetectionConfig` | PUBLIC  
`TY_052` | `GoogleCloudVideointelligenceV1beta2_ObjectTrackingConfig` | PUBLIC  
`TY_055` | `GoogleCloudVideointelligenceV1beta2_PersonDetectionConfig` | PUBLIC  
`TY_056` | `GoogleCloudVideointelligenceV1beta2_ShotChangeDetectionConfi` | PUBLIC  
`TY_057` | `GoogleCloudVideointelligenceV1beta2_SpeechContext` | PUBLIC  
`TY_060` | `GoogleCloudVideointelligenceV1beta2_SpeechTranscriptionConfi` | PUBLIC  
`TY_062` | `GoogleCloudVideointelligenceV1beta2_TextDetectionConfig` | PUBLIC  
`TY_069` | `GoogleCloudVideointelligenceV1beta2_VideoContext` | PUBLIC  
`TY_070` | `GoogleCloudVideointelligenceV1beta2_VideoSegment` | PUBLIC  
`TY_167` | `GoogleLongrunning_Operation` | PUBLIC  
`TY_168` | `GoogleRpc_Status` | PUBLIC  
`TY_T_057` | `GoogleCloudVideointelligenceV1beta2_SpeechContext` | PUBLIC  
`TY_T_070` | `GoogleCloudVideointelligenceV1beta2_VideoSegment` | PUBLIC  
`TY_T_INT4` | `Table of Integers` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | videointelligence:v1beta2 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://videointelligence.googleapis.com | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250210 | PUBLIC  
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
  
### ANNOTATE_VIDEOS

  * Description: videointelligence.videos.annotate 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_031` | GoogleCloudVideointelligenceV1beta2_AnnotateVideoRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_167` | GoogleLongrunning_Operation  
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
