---
url: https://docs.cloud.google.com/vision/docs/reference/rest/v1p3beta1/projects.locations.products.referenceImages/delete/
title: Method: projects.locations.products.referenceImages.delete \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:10:57.923123+00:00
---

# Method: projects.locations.products.referenceImages.delete  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/reference/rest/v1p3beta1/projects.locations.products.referenceImages/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Reference ](https://docs.cloud.google.com/vision/docs/apis)



Send feedback 

#  Method: projects.locations.products.referenceImages.delete Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization Scopes
  * Try it!



Permanently deletes a reference image.

The image metadata will be deleted right away, but search queries against ProductSets containing the image may still work until all related caches are refreshed.

The actual image files are not deleted from Google Cloud Storage.

Possible errors:

none

### HTTP request

`DELETE https://vision.googleapis.com/v1p3beta1/{name=projects/*/locations/*/products/*/referenceImages/*}`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` The resource name of the reference image to delete.Format is:`projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID/referenceImages/IMAGE_ID`  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body will be empty.

### Authorization Scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-vision`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## Try it!

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
