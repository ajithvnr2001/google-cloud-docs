---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_clouvideint_v1p1beta1/
title: Class /GOOG/CL_CLOUVIDEINT_V1P1BETA1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:10.236349+00:00
---

# Class /GOOG/CL_CLOUVIDEINT_V1P1BETA1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_clouvideint_v1p1beta1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_CLOUVIDEINT_V1P1BETA1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_clouvideint_v1p1beta1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_clouvideint_v1p1beta1)



## Class
    
    
    /GOOG/CL_CLOUVIDEINT_V1P1BETA1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Cloud Video Intelligence API v1p1beta1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_061` | `GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoRequest` | PUBLIC  
`TY_066` | `GoogleCloudVideointelligenceV1p1beta1_ExplicitContentDetecti` | PUBLIC  
`TY_070` | `GoogleCloudVideointelligenceV1p1beta1_FaceDetectionConfig` | PUBLIC  
`TY_074` | `GoogleCloudVideointelligenceV1p1beta1_LabelDetectionConfig` | PUBLIC  
`TY_082` | `GoogleCloudVideointelligenceV1p1beta1_ObjectTrackingConfig` | PUBLIC  
`TY_085` | `GoogleCloudVideointelligenceV1p1beta1_PersonDetectionConfig` | PUBLIC  
`TY_086` | `GoogleCloudVideointelligenceV1p1beta1_ShotChangeDetectionCon` | PUBLIC  
`TY_087` | `GoogleCloudVideointelligenceV1p1beta1_SpeechContext` | PUBLIC  
`TY_090` | `GoogleCloudVideointelligenceV1p1beta1_SpeechTranscriptionCon` | PUBLIC  
`TY_092` | `GoogleCloudVideointelligenceV1p1beta1_TextDetectionConfig` | PUBLIC  
`TY_099` | `GoogleCloudVideointelligenceV1p1beta1_VideoContext` | PUBLIC  
`TY_100` | `GoogleCloudVideointelligenceV1p1beta1_VideoSegment` | PUBLIC  
`TY_167` | `GoogleLongrunning_Operation` | PUBLIC  
`TY_168` | `GoogleRpc_Status` | PUBLIC  
`TY_T_087` | `GoogleCloudVideointelligenceV1p1beta1_SpeechContext` | PUBLIC  
`TY_T_100` | `GoogleCloudVideointelligenceV1p1beta1_VideoSegment` | PUBLIC  
`TY_T_INT4` | `Table of Integers` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | videointelligence:v1p1beta1 | PUBLIC  
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
`IS_INPUT` | IMPORTING | `TY_061` | GoogleCloudVideointelligenceV1p1beta1_AnnotateVideoRequest  
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

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
