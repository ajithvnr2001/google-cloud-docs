---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores/list/
title: Method: projects.locations.brands.stores.list \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:02:15.760401+00:00
---

# Method: projects.locations.brands.stores.list  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)
  * [ Reference ](https://docs.cloud.google.com/food-ai/apis)



Send feedback 

#  Method: projects.locations.brands.stores.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes



Lists stores.

### HTTP request

`GET https://foodorderingaiagent.googleapis.com/v1/{parent=projects/*/locations/*/brands/*}/stores`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent brand, which owns this collection of stores. Format: projects/{project}/locations/{location}/brands/{brand}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of menus to return. The service may return fewer than this value.  
`pageToken` |  `string` Optional. A page token, received from a previous `ListMenus` call. Provide this to retrieve the subsequent page.  
`filter` |  `string` Optional. Filter expression based on AIP-160. Allows filtering stores based on various attributes. Supported Filter Fields:

  * status (String): The status of the store. Operators: =, != Example: `status = "ACTIVE"` (enum value)
  * updateTime (Timestamp): The last updated time of the store. Timestamps expect an RFC-3339 formatted string (e.g. 2012-04-21T11:30:00-04:00). UTC offsets are supported Operators: =, !=, >, >=, <, <= Example: `updateTime >= "2025-10-01T00:00:00Z"`
  * tags (String): Tags associated with the store. Operator: : (HAS) Example: `tags:"store-tag"`
  * city (String): The city of the store. Operators: =, != Example: `city = "Mountain View"`
  * state (String): The state of the store address. Operators: =, != Example: `state = "CA"`

Logical Operators:Conditions can be combined using `AND`, `OR`, and `NOT`. Parentheses `()` can be used to group expressions to control the order of evaluation. Example: `status = "ACTIVE" AND state = "CA"`  
  
### Request body

The request body must be empty.

### Response body

Response message for `[MenuService.ListStores](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores/list#google.cloud.foodorderingaiagent.v1.MenuService.ListStores)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "stores": [
        {
          object ([Store](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores#Store))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`stores[]` |  `object (`[Store](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores#Store)`)` The stores from the specified collection.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-16 UTC."],[],[]] 
