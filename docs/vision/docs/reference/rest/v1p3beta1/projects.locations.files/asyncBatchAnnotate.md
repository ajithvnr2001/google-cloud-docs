---
url: https://docs.cloud.google.com/vision/docs/reference/rest/v1p3beta1/projects.locations.files/asyncBatchAnnotate/
title: Method: projects.locations.files.asyncBatchAnnotate \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:58.151580+00:00
---

# Method: projects.locations.files.asyncBatchAnnotate  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/reference/rest/v1p3beta1/projects.locations.files/asyncBatchAnnotate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Reference ](https://docs.cloud.google.com/vision/docs/apis)



Send feedback 

#  Method: projects.locations.files.asyncBatchAnnotate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization Scopes
  * Try it!



Run asynchronous image detection and annotation for a list of generic files, such as PDF files, which may contain multiple pages and multiple images per page. Progress and results can be retrieved through the `google.longrunning.Operations` interface. `Operation.metadata` contains `OperationMetadata` (metadata). `Operation.response` contains `AsyncBatchAnnotateFilesResponse` (results).

### HTTP request

`POST https://vision.googleapis.com/v1p3beta1/{parent=projects/*/locations/*}/files:asyncBatchAnnotate`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Optional. Target project and location to make a call.Format: `projects/{project-id}/locations/{location-id}`.If no parent is specified, a region will be chosen automatically.Supported location-ids: `us`: USA country only, `asia`: East asia areas, like Japan, Taiwan, `eu`: The European Union.Example: `projects/project-A/locations/eu`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "requests": [
        {
          object ([AsyncAnnotateFileRequest](https://docs.cloud.google.com/vision/docs/reference/rest/v1p3beta1/AsyncAnnotateFileRequest))
        }
      ]
    }  
  
Fields  
---  
`requests[]` |  `object (`[AsyncAnnotateFileRequest](https://docs.cloud.google.com/vision/docs/reference/rest/v1p3beta1/AsyncAnnotateFileRequest)`)` Required. Individual async file annotation requests for this batch.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/vision/docs/reference/rest/Shared.Types/Operation)`.

### Authorization Scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-vision`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
