---
url: https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1/projects.locations.products/get/
title: Method: projects.locations.products.get \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:08:02.985035+00:00
---

# Method: projects.locations.products.get  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1/projects.locations.products/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search)
  * [ Reference ](https://docs.cloud.google.com/vision/product-search/docs/apis)



#  Method: projects.locations.products.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization Scopes



Gets information associated with a Product.

Possible errors:

  * Returns NOT_FOUND if the Product does not exist.



### HTTP request

`GET https://vision.googleapis.com/v1/{name=projects/*/locations/*/products/*}`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Resource name of the Product to get.Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID`  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Product](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1/projects.locations.products#Product)`.

### Authorization Scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-vision`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
