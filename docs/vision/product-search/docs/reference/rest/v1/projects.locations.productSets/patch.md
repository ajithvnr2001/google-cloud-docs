---
url: https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1/projects.locations.productSets/patch/
title: Method: projects.locations.productSets.patch \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:42.521837+00:00
---

# Method: projects.locations.productSets.patch  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1/projects.locations.productSets/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search)
  * [ Reference ](https://docs.cloud.google.com/vision/product-search/docs/apis)



#  Method: projects.locations.productSets.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization Scopes



Makes changes to a ProductSet resource. Only displayName can be updated currently.

Possible errors:

  * Returns NOT_FOUND if the ProductSet does not exist.
  * Returns INVALID_ARGUMENT if displayName is present in updateMask but missing from the request or longer than 4096 characters.



### HTTP request

`PATCH https://vision.googleapis.com/v1/{productSet.name=projects/*/locations/*/productSets/*}`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Path parameters

Parameters  
---  
`productSet.name` |  `string` The resource name of the ProductSet.Format is: `projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID`.This field is ignored when creating a ProductSet.  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask)` format)` The `[FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask)` that specifies which fields to update. If updateMask isn't specified, all mutable fields are to be updated. Valid mask path is `displayName`.A comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[ProductSet](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1/projects.locations.productSets#ProductSet)`.

### Response body

If successful, the response body contains an instance of `[ProductSet](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1/projects.locations.productSets#ProductSet)`.

### Authorization Scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-vision`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
