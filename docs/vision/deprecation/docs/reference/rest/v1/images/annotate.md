---
url: https://docs.cloud.google.com/vision/deprecation/docs/reference/rest/v1/images/annotate/
title: Method: images.annotate \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:19:07.845006+00:00
---

# Method: images.annotate  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/deprecation/docs/reference/rest/v1/images/annotate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Reference ](https://docs.cloud.google.com/vision/deprecation/docs/reference/rest)



Send feedback 

#  Method: images.annotate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization Scopes
  * Try it!



Run image detection and annotation for a batch of images.

### HTTP request

`POST https://alpha-vision.googleapis.com/v1/images:annotate`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "requests": [
        {
          object([AnnotateImageRequest](https://docs.cloud.google.com/vision/deprecation/docs/reference/rest/v1/AnnotateImageRequest))
        }
      ]
    }  
  
Fields  
---  
`requests[]` |  `object(`[AnnotateImageRequest](https://docs.cloud.google.com/vision/deprecation/docs/reference/rest/v1/AnnotateImageRequest)`)` Individual image annotation requests for this batch.   
  
### Response body

If successful, the response body contains data with the following structure:

Response to a batch image annotation request.

JSON representation  
---  
      
    
    {
      "responses": [
        {
          object([AnnotateImageResponse](https://docs.cloud.google.com/vision/deprecation/docs/reference/rest/v1/AnnotateImageResponse))
        }
      ]
    }  
  
Fields  
---  
`responses[]` |  `object(`[AnnotateImageResponse](https://docs.cloud.google.com/vision/deprecation/docs/reference/rest/v1/AnnotateImageResponse)`)` Individual responses to image annotation requests within the batch.   
  
### Authorization Scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-vision`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## Try it!

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-29 UTC."],[],[]] 
