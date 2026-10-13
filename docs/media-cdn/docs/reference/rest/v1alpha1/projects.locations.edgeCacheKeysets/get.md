---
url: https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1alpha1/projects.locations.edgeCacheKeysets/get/
title: Method: projects.locations.edgeCacheKeysets.get \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:15:45.341542+00:00
---

# Method: projects.locations.edgeCacheKeysets.get  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1alpha1/projects.locations.edgeCacheKeysets/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Reference ](https://docs.cloud.google.com/media-cdn/docs/apis)



Send feedback 

#  Method: projects.locations.edgeCacheKeysets.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes



Gets details of a single EdgeCacheKeyset.

### HTTP request

`GET https://networkservices.googleapis.com/v1alpha1/{name=projects/*/locations/*/edgeCacheKeysets/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the `[EdgeCacheKeyset](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1alpha1/projects.locations.edgeCacheKeysets#EdgeCacheKeyset)` resource to get. Must be in the format `projects/*/locations/global/edgeCacheKeysets/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `networkservices.edgeCacheKeysets.get`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[EdgeCacheKeyset](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1alpha1/projects.locations.edgeCacheKeysets#EdgeCacheKeyset)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-30 UTC."],[],[]] 
