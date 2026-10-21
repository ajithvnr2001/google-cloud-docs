---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores/batchUpdate/
title: Method: projects.locations.brands.stores.batchUpdate \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:07.054981+00:00
---

# Method: projects.locations.brands.stores.batchUpdate  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores/batchUpdate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)
  * [ Reference ](https://docs.cloud.google.com/food-ai/apis)



Send feedback 

#  Method: projects.locations.brands.stores.batchUpdate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * UpdateStoreRequest
    * JSON representation



Batch updates stores.

### HTTP request

`POST https://foodorderingaiagent.googleapis.com/v1/{parent=projects/*/locations/*/brands/*}/stores:batchUpdate`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource shared by all stores being updated. Format: projects/{project}/locations/{location}/brands/{brand} If this is set, the parent of all of the stores specified in `requests` must match this field.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "requests": [
        {
          object ([UpdateStoreRequest](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores/batchUpdate#UpdateStoreRequest))
        }
      ]
    }  
  
Fields  
---  
`requests[]` |  `object (`[UpdateStoreRequest](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores/batchUpdate#UpdateStoreRequest)`)` Required. The request message specifying the resources to update. A maximum of 1000 stores can be modified in a batch.  
  
### Response body

Response message for `[MenuService.BatchUpdateStores](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores/batchUpdate#google.cloud.foodorderingaiagent.v1.MenuService.BatchUpdateStores)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "stores": [
        {
          object ([Store](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores#Store))
        }
      ]
    }  
  
Fields  
---  
`stores[]` |  `object (`[Store](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores#Store)`)` Stores updated.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## UpdateStoreRequest

Request message for `[MenuService.UpdateStore](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores/patch#google.cloud.foodorderingaiagent.v1.MenuService.UpdateStore)`.

JSON representation  
---  
      
    
    {
      "store": {
        object ([Store](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores#Store))
      },
      "updateMask": string,
      "allowMissing": boolean
    }  
  
Fields  
---  
`store` |  `object (`[Store](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores#Store)`)` Required. The store to update.The store's `name` field is used to identify the store to update. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. The list of fields to updateThis is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`allowMissing` |  `boolean` Optional. If set to true, and the store is not found, a new store will be created. In this situation, `updateMask` is ignored.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-16 UTC."],[],[]] 
