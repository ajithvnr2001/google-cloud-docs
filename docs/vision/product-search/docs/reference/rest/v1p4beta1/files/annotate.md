---
url: https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p4beta1/files/annotate/
title: Method: files.annotate \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:03:15.508446+00:00
---

# Method: files.annotate  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p4beta1/files/annotate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search)
  * [ Reference ](https://docs.cloud.google.com/vision/product-search/docs/apis)



#  Method: files.annotate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization Scopes
  * AnnotateFileRequest
    * JSON representation
  * AnnotateFileResponse
    * JSON representation



Service that performs image detection and annotation for a batch of files. Now only "application/pdf", "image/tiff" and "image/gif" are supported.

This service will extract at most 5 (customers can specify which 5 in AnnotateFileRequest.pages) frames (gif) or pages (pdf or tiff) from each file provided and perform detection and annotation for each image extracted.

### HTTP request

`POST https://vision.googleapis.com/v1p4beta1/files:annotate`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "requests": [
        {
          object ([AnnotateFileRequest](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p4beta1/files/annotate#AnnotateFileRequest))
        }
      ]
    }  
  
Fields  
---  
`requests[]` |  `object (`[AnnotateFileRequest](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p4beta1/files/annotate#AnnotateFileRequest)`)` The list of file annotation requests. Right now we support only one AnnotateFileRequest in BatchAnnotateFilesRequest.   
  
### Response body

If successful, the response body contains data with the following structure:

A list of file annotation responses.

JSON representation  
---  
      
    
    {
      "responses": [
        {
          object ([AnnotateFileResponse](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p4beta1/files/annotate#AnnotateFileResponse))
        }
      ]
    }  
  
Fields  
---  
`responses[]` |  `object (`[AnnotateFileResponse](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p4beta1/files/annotate#AnnotateFileResponse)`)` The list of file annotation responses, each response corresponding to each AnnotateFileRequest in BatchAnnotateFilesRequest.   
  
### Authorization Scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-vision`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## AnnotateFileRequest

A request to annotate one single file, e.g. a PDF, TIFF or GIF file.

JSON representation  
---  
      
    
    {
      "inputConfig": {
        object ([InputConfig](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p4beta1/InputConfig))
      },
      "features": [
        {
          object ([Feature](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p4beta1/Feature))
        }
      ],
      "imageContext": {
        object ([ImageContext](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p4beta1/ImageContext))
      },
      "pages": [
        number
      ]
    }  
  
Fields  
---  
`inputConfig` |  `object (`[InputConfig](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p4beta1/InputConfig)`)` Required. Information about the input file.   
`features[]` |  `object (`[Feature](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p4beta1/Feature)`)` Required. Requested features.   
`imageContext` |  `object (`[ImageContext](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p4beta1/ImageContext)`)` Additional context that may accompany the image(s) in the file.   
`pages[]` |  `number` Pages of the file to perform image annotation.Pages starts from 1, we assume the first page of the file is page 1. At most 5 pages are supported per request. Pages can be negative.Page 1 means the first page. Page 2 means the second page. Page -1 means the last page. Page -2 means the second to the last page.If the file is GIF instead of PDF or TIFF, page refers to GIF frames.If this field is empty, by default the service performs image annotation for the first 5 pages of the file.  
  
## AnnotateFileResponse

Response to a single file annotation request. A file may contain one or more images, which individually have their own responses.

JSON representation  
---  
      
    
    {
      "inputConfig": {
        object ([InputConfig](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p4beta1/InputConfig))
      },
      "responses": [
        {
          object ([AnnotateImageResponse](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p4beta1/AnnotateImageResponse))
        }
      ],
      "totalPages": number
    }  
  
Fields  
---  
`inputConfig` |  `object (`[InputConfig](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p4beta1/InputConfig)`)` Information about the file for which this response is generated.   
`responses[]` |  `object (`[AnnotateImageResponse](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p4beta1/AnnotateImageResponse)`)` Individual responses to images found within the file.   
`totalPages` |  `number` This field gives the total number of pages in the file.   
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
