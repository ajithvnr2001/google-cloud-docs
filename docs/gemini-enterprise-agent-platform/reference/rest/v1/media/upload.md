---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/media/upload/
title: Method: media.upload \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:19:47.777392+00:00
---

# Method: media.upload  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/media/upload/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: media.upload Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : media.upload

Upload a file into a RagCorpus.

### Endpoint

  * Upload URI, for media upload requests:  


post  `https://{service-endpoint}/upload/v1/{parent}/ragFiles:upload`

  * Metadata URI, for metadata-only requests:  


post  `https://{service-endpoint}/v1/{parent}/ragFiles:upload`

Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The name of the RagCorpus resource into which to upload the file. Format: `projects/{project}/locations/{location}/ragCorpora/{ragCorpus}`

### Request body

The request body contains data with the following structure: | Fields  
  
`ragFile` `object (`[RagFile](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#RagFile)`)` Required. The RagFile to upload. | `uploadRagFileConfig` `object (`[UploadRagFileConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/media/upload#UploadRagFileConfig)`)` Required. The config for the RagFiles to be uploaded into the RagCorpus. `[VertexRagDataService.UploadRagFile](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/media/upload#google.cloud.aiplatform.v1.VertexRagDataService.UploadRagFile)`.

### Response body

Response message for `[VertexRagDataService.UploadRagFile](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/media/upload#google.cloud.aiplatform.v1.VertexRagDataService.UploadRagFile)`. If successful, the response body contains data with the following structure: | Fields  
  
`result` `Union type`  
  
The result of the upload. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`ragFile` `object (`[RagFile](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#RagFile)`)` The RagFile that had been uploaded into the RagCorpus. | `error` `object (`[Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` The error that occurred while processing the RagFile. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
    
      // result
      "ragFile": {
        object ([RagFile](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#RagFile))
      },
      "error": {
        object ([Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Status))
      }
      // Union type
    }  
  
## UploadRagFileConfig

Config for uploading RagFile.

Fields  
  
`ragFileTransformationConfig` `object (`[RagFileTransformationConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/RagFileTransformationConfig)`)` Specifies the transformation config for RagFiles. | JSON representation  
---  
      
    
    {
      "ragFileTransformationConfig": {
        object ([RagFileTransformationConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/RagFileTransformationConfig))
      }
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
