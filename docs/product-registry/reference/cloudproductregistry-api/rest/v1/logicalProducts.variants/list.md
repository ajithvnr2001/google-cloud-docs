---
url: https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/logicalProducts.variants/list/
title: Method: logicalProducts.variants.list \u00a0|\u00a0 Cloud Product Registry API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:46:00.645479+00:00
---

# Method: logicalProducts.variants.list  |  Cloud Product Registry API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/logicalProducts.variants/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Product Registry API ](https://docs.cloud.google.com/product-registry)
  * [ APIs & Reference ](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest)



Send feedback 

#  Method: logicalProducts.variants.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation



Lists LogicalProductVariants matching given criteria.

### HTTP request

`GET https://cloudproductregistry.googleapis.com/v1/{parent=logicalProducts/*}/variants`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent logical product id. Format: logicalProducts/{logicalProduct}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of logical product variants to return. The service may return fewer than this value. If unspecified, at most 100 logical product variants will be returned. The maximum value is 500; values above 500 will be coerced to 500.  
`pageToken` |  `string` Optional. A page token, received from a previous `variants.list` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `variants.list` must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

Response message for variants.list.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "logicalProductVariants": [
        {
          object ([LogicalProductVariant](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/logicalProducts.variants#LogicalProductVariant))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`logicalProductVariants[]` |  `object (`[LogicalProductVariant](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/logicalProducts.variants#LogicalProductVariant)`)` Matched LogicalProductVariants  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-06 UTC."],[],[]] 
