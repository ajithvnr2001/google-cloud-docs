---
url: https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates/sanitizeModelResponse/
title: Method: projects.locations.templates.sanitizeModelResponse \u00a0|\u00a0 Model Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:46:30.191551+00:00
---

# Method: projects.locations.templates.sanitizeModelResponse  |  Model Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates/sanitizeModelResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Model Armor ](https://docs.cloud.google.com/model-armor)
  * [ Reference ](https://docs.cloud.google.com/model-armor/reference/libraries)



Send feedback 

#  Method: projects.locations.templates.sanitizeModelResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



Sanitizes Model Response.

### HTTP request

`POST https://modelarmor.googleapis.com/v1/{name=projects/*/locations/*/templates/*}:sanitizeModelResponse`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Represents resource name of template e.g. name=projects/sample-project/locations/us-central1/templates/templ01  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "modelResponseData": {
        object ([DataItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/DataItem))
      },
      "userPrompt": string,
      "multiLanguageDetectionMetadata": {
        object ([MultiLanguageDetectionMetadata](https://docs.cloud.google.com/model-armor/reference/rest/v1/MultiLanguageDetectionMetadata))
      },
      "streamingMode": enum ([StreamingMode](https://docs.cloud.google.com/model-armor/reference/rest/v1/StreamingMode))
    }  
  
Fields  
---  
`modelResponseData` |  `object (`[DataItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/DataItem)`)` Required. Model response data to sanitize.  
`userPrompt` |  `string` Optional. User Prompt associated with Model response.  
`multiLanguageDetectionMetadata` |  `object (`[MultiLanguageDetectionMetadata](https://docs.cloud.google.com/model-armor/reference/rest/v1/MultiLanguageDetectionMetadata)`)` Optional. Metadata related for multi language detection.  
`streamingMode` |  `enum (`[StreamingMode](https://docs.cloud.google.com/model-armor/reference/rest/v1/StreamingMode)`)` Optional. Streaming Mode for StreamSanitize* API.  
  
### Response body

Sanitized Model Response Response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "sanitizationResult": {
        object ([SanitizationResult](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult))
      }
    }  
  
Fields  
---  
`sanitizationResult` |  `object (`[SanitizationResult](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult)`)` Output only. Sanitization Result.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `modelarmor.templates.useToSanitizeModelResponse`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-19 UTC."],[],[]] 
