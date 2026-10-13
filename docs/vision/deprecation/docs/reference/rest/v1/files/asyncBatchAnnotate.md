---
url: https://docs.cloud.google.com/vision/deprecation/docs/reference/rest/v1/files/asyncBatchAnnotate/
title: Method: files.asyncBatchAnnotate \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:50:11.403222+00:00
---

# Method: files.asyncBatchAnnotate  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/deprecation/docs/reference/rest/v1/files/asyncBatchAnnotate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Reference ](https://docs.cloud.google.com/vision/deprecation/docs/reference/rest)



Send feedback 

#  Method: files.asyncBatchAnnotate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Request body
    * JSON representation
  * Response body
  * Authorization Scopes
  * AsyncAnnotateFileRequest
    * JSON representation
  * Try it!



Run asynchronous image detection and annotation for a list of generic files, such as PDF files, which may contain multiple pages and multiple images per page. Progress and results can be retrieved through the `google.longrunning.Operations` interface. `Operation.metadata` contains `OperationMetadata` (metadata). `Operation.response` contains `AsyncBatchAnnotateFilesResponse` (results).

### HTTP request

`POST https://alpha-vision.googleapis.com/v1/files:asyncBatchAnnotate`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "requests": [
        {
          object([AsyncAnnotateFileRequest](https://docs.cloud.google.com/vision/deprecation/docs/reference/rest/v1/files/asyncBatchAnnotate#AsyncAnnotateFileRequest))
        }
      ]
    }  
  
Fields  
---  
`requests[]` |  `object(`[AsyncAnnotateFileRequest](https://docs.cloud.google.com/vision/deprecation/docs/reference/rest/v1/files/asyncBatchAnnotate#AsyncAnnotateFileRequest)`)` Individual async file annotation requests for this batch.   
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/vision/deprecation/docs/reference/rest/v1/locations.operations#Operation)`.

### Authorization Scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-vision`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## AsyncAnnotateFileRequest

An offline file annotation request.

JSON representation  
---  
      
    
    {
      "inputConfig": {
        object([InputConfig](https://docs.cloud.google.com/vision/deprecation/docs/reference/rest/v1/InputConfig))
      },
      "features": [
        {
          object([Feature](https://docs.cloud.google.com/vision/deprecation/docs/reference/rest/v1/Feature))
        }
      ],
      "imageContext": {
        object([ImageContext](https://docs.cloud.google.com/vision/deprecation/docs/reference/rest/v1/ImageContext))
      },
      "outputConfig": {
        object([OutputConfig](https://docs.cloud.google.com/vision/deprecation/docs/reference/rest/v1/OutputConfig))
      }
    }  
  
Fields  
---  
`inputConfig` |  `object(`[InputConfig](https://docs.cloud.google.com/vision/deprecation/docs/reference/rest/v1/InputConfig)`)` Required. Information about the input file.   
`features[]` |  `object(`[Feature](https://docs.cloud.google.com/vision/deprecation/docs/reference/rest/v1/Feature)`)` Required. Requested features.   
`imageContext` |  `object(`[ImageContext](https://docs.cloud.google.com/vision/deprecation/docs/reference/rest/v1/ImageContext)`)` Additional context that may accompany the image(s) in the file.   
`outputConfig` |  `object(`[OutputConfig](https://docs.cloud.google.com/vision/deprecation/docs/reference/rest/v1/OutputConfig)`)` Required. The desired output location and metadata (e.g. format).   
  
## Try it!

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-29 UTC."],[],[]] 
