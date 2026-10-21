---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus.entities/batchGet/
title: Method: projects.locations.menus.entities.batchGet \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:02:17.207347+00:00
---

# Method: projects.locations.menus.entities.batchGet  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus.entities/batchGet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)



Send feedback 

#  Method: projects.locations.menus.entities.batchGet Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes



Batch gets entities for a menu.

### HTTP request

`GET https://foodorderingaiagent.googleapis.com/v1beta/{parent=projects/*/locations/*/menus/*}/entities:batchGet`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the menu to retrieve entities from. Format: projects/{project}/locations/{location}/menus/{menu}  
  
### Query parameters

Parameters  
---  
`itemIds[]` |  `string` Optional. The IDs of the items to retrieve.  
`modifierIds[]` |  `string` Optional. The IDs of the modifier to retrieve.  
`modifierGroupIds[]` |  `string` Optional. The IDs of the modifier groups to retrieve.  
`categoryIds[]` |  `string` Optional. The IDs of the categories to retrieve.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[MenuService.BatchGetMenuEntities](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus.entities/batchGet#google.cloud.foodorderingaiagent.v1beta.MenuService.BatchGetMenuEntities)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "items": [
        {
          object ([Item](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#Item))
        }
      ],
      "modifiers": [
        {
          object ([Modifier](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#Modifier))
        }
      ],
      "modifierGroups": [
        {
          object ([ModifierGroup](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#ModifierGroup))
        }
      ],
      "categories": [
        {
          object ([MenuCategory](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#MenuCategory))
        }
      ]
    }  
  
Fields  
---  
`items[]` |  `object (`[Item](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#Item)`)` The items requested.  
`modifiers[]` |  `object (`[Modifier](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#Modifier)`)` The modifiers requested.  
`modifierGroups[]` |  `object (`[ModifierGroup](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#ModifierGroup)`)` The modifier groups requested.  
`categories[]` |  `object (`[MenuCategory](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#MenuCategory)`)` The categories requested.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-04 UTC."],[],[]] 
