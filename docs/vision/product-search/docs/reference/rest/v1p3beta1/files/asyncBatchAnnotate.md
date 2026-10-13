---
url: https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p3beta1/files/asyncBatchAnnotate/
title: Method: files.asyncBatchAnnotate \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:43:07.552653+00:00
---

# Method: files.asyncBatchAnnotate  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p3beta1/files/asyncBatchAnnotate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search)
  * [ Reference ](https://docs.cloud.google.com/vision/product-search/docs/apis)



#  Method: files.asyncBatchAnnotate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Request body
    * JSON representation
  * Response body
  * Authorization Scopes
  * AsyncAnnotateFileRequest
    * JSON representation
  * InputConfig
    * JSON representation
  * GcsSource
    * JSON representation
  * OutputConfig
    * JSON representation
  * GcsDestination
    * JSON representation



Run asynchronous image detection and annotation for a list of generic files, such as PDF files, which may contain multiple pages and multiple images per page. Progress and results can be retrieved through the `google.longrunning.Operations` interface. `Operation.metadata` contains `OperationMetadata` (metadata). `Operation.response` contains `AsyncBatchAnnotateFilesResponse` (results).

### HTTP request

`POST https://vision.googleapis.com/v1p3beta1/files:asyncBatchAnnotate`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "requests": [
        {
          object([AsyncAnnotateFileRequest](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p3beta1/files/asyncBatchAnnotate#AsyncAnnotateFileRequest))
        }
      ]
    }  
  
Fields  
---  
`requests[]` |  `object(`[AsyncAnnotateFileRequest](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p3beta1/files/asyncBatchAnnotate#AsyncAnnotateFileRequest)`)` Individual async file annotation requests for this batch.   
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/Shared.Types/Operation)`.

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
        object([InputConfig](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p3beta1/files/asyncBatchAnnotate#InputConfig))
      },
      "features": [
        {
          object([Feature](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p3beta1/Feature))
        }
      ],
      "imageContext": {
        object([ImageContext](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p3beta1/ImageContext))
      },
      "outputConfig": {
        object([OutputConfig](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p3beta1/files/asyncBatchAnnotate#OutputConfig))
      }
    }  
  
Fields  
---  
`inputConfig` |  `object(`[InputConfig](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p3beta1/files/asyncBatchAnnotate#InputConfig)`)` Required. Information about the input file.   
`features[]` |  `object(`[Feature](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p3beta1/Feature)`)` Required. Requested features.   
`imageContext` |  `object(`[ImageContext](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p3beta1/ImageContext)`)` Additional context that may accompany the image(s) in the file.   
`outputConfig` |  `object(`[OutputConfig](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p3beta1/files/asyncBatchAnnotate#OutputConfig)`)` Required. The desired output location and metadata (e.g. format).   
  
## InputConfig

The desired input location and metadata.

JSON representation  
---  
      
    
    {
      "gcsSource": {
        object([GcsSource](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p3beta1/files/asyncBatchAnnotate#GcsSource))
      },
      "mimeType": string
    }  
  
Fields  
---  
`gcsSource` |  `object(`[GcsSource](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p3beta1/files/asyncBatchAnnotate#GcsSource)`)` The Google Cloud Storage location to read the input from.   
`mimeType` |  `string` The type of the file. Currently only "application/pdf" and "image/tiff" are supported. Wildcards are not supported.   
  
## GcsSource

The Google Cloud Storage location where the input will be read from.

JSON representation  
---  
      
    
    {
      "uri": string
    }  
  
Fields  
---  
`uri` |  `string` Google Cloud Storage URI for the input file. This must only be a Google Cloud Storage object. Wildcards are not currently supported.   
  
## OutputConfig

The desired output location and metadata.

JSON representation  
---  
      
    
    {
      "gcsDestination": {
        object([GcsDestination](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p3beta1/files/asyncBatchAnnotate#GcsDestination))
      },
      "batchSize": number
    }  
  
Fields  
---  
`gcsDestination` |  `object(`[GcsDestination](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p3beta1/files/asyncBatchAnnotate#GcsDestination)`)` The Google Cloud Storage location to write the output(s) to.   
`batchSize` |  `number` The max number of response protos to put into each output JSON file on Google Cloud Storage. The valid range is [1, 100]. If not specified, the default value is 20.For example, for one pdf file with 100 pages, 100 response protos will be generated. If `batchSize` = 20, then 5 json files each containing 20 response protos will be written under the prefix `gcsDestination`.`uri`.Currently, batchSize only applies to GcsDestination, with potential future support for other output configurations.  
  
## GcsDestination

The Google Cloud Storage location where the output will be written to.

JSON representation  
---  
      
    
    {
      "uri": string
    }  
  
Fields  
---  
`uri` |  `string` Google Cloud Storage URI where the results will be stored. Results will be in JSON format and preceded by its corresponding input URI. This field can either represent a single file, or a prefix for multiple outputs. Prefixes must end in a `/`.Examples:

  * File: <gs://bucket-name/filename.json>
  * Prefix: <gs://bucket-name/prefix/here/>
  * File: <gs://bucket-name/prefix/here>

If multiple outputs, each response is still AnnotateFileResponse, each of which contains some subset of the full list of AnnotateImageResponse. Multiple outputs can happen if, for example, the output JSON is too large and overflows into multiple sharded files.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
