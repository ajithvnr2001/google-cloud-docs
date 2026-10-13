---
url: https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/logicalProducts.variants/lookupEntity/
title: Method: logicalProducts.variants.lookupEntity \u00a0|\u00a0 Cloud Product Registry API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:46:00.742061+00:00
---

# Method: logicalProducts.variants.lookupEntity  |  Cloud Product Registry API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/logicalProducts.variants/lookupEntity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Product Registry API ](https://docs.cloud.google.com/product-registry)
  * [ APIs & Reference ](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest)



Send feedback 

#  Method: logicalProducts.variants.lookupEntity Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body



Look up entities.

### HTTP request

`GET https://cloudproductregistry.googleapis.com/v1/{lookupUri=logicalProducts/*/variants/*}:lookupEntity`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`lookupUri` |  `string` Required. Entity uri to look up. Supported Formats: logicalProducts/{logicalProduct} logicalProducts/{logicalProduct}/variants/{variant} productSuites/{productSuite}  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[LookupEntityResponse](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/LookupEntityResponse)`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-06 UTC."],[],[]] 
