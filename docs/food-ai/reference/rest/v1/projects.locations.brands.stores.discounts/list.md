---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.discounts/list/
title: Method: projects.locations.brands.stores.discounts.list \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:08.368151+00:00
---

# Method: projects.locations.brands.stores.discounts.list  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.discounts/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)
  * [ Reference ](https://docs.cloud.google.com/food-ai/apis)



Send feedback 

#  Method: projects.locations.brands.stores.discounts.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes



Lists discounts.

### HTTP request

`GET https://foodorderingaiagent.googleapis.com/v1/{parent=projects/*/locations/*/brands/*/stores/*}/discounts`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent store, which owns this collection of discounts. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of discounts to return. The service may return fewer than this value.  
`pageToken` |  `string` Optional. A page token, received from a previous `discounts.list` call. Provide this to retrieve the subsequent page.  
`filter` |  `string` Optional. Filter expression based on AIP-160.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[MenuService.ListDiscounts](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.discounts/list#google.cloud.foodorderingaiagent.v1.MenuService.ListDiscounts)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "discounts": [
        {
          object ([Discount](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.discounts#Discount))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`discounts[]` |  `object (`[Discount](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.discounts#Discount)`)` The discounts from the specified collection.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-15 UTC."],[],[]] 
