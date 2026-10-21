---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus/list/
title: Method: projects.locations.menus.list \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:27:38.500893+00:00
---

# Method: projects.locations.menus.list  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)



Send feedback 

#  Method: projects.locations.menus.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * MenuView



Lists menus.

### HTTP request

`GET https://foodorderingaiagent.googleapis.com/v1beta/{parent=projects/*/locations/*}/menus`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent, which owns this collection of menus. Format: projects/{project}/locations/{location}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of menus to return. The service may return fewer than this value.  
`pageToken` |  `string` Optional. A page token, received from a previous `menus.list` call. Provide this to retrieve the subsequent page.  
`filter` |  `string` Optional. A filter expression that filters the results. The expression syntax is documented in <https://google.aip.dev/160>.The following fields are supported: - `store` \- `brand``store=projects/my-project/locations/us-central1/brands/my-brand/stores/my-store` \- `brand=projects/my-project/locations/us-central1/brands/my-brand`  
`view` |  `enum (`[MenuView](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus/list#MenuView)`)` Optional. The view to return for the menus.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[MenuService.ListMenus](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus/list#google.cloud.foodorderingaiagent.v1beta.MenuService.ListMenus)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "menus": [
        {
          object ([Menu](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#Menu))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`menus[]` |  `object (`[Menu](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus#Menu)`)` The menus from the specified collection.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## MenuView

Specifies the level of detail to return for menus.

Enums  
---  
`MENU_VIEW_UNSPECIFIED` | The default / unset value. The API will default to the FULL view.  
`MENU_VIEW_BASIC` | Include basic metadata about the menu.  
`MENU_VIEW_NAME_ONLY` | Only include the name of the menu  
`MENU_VIEW_FULL` | Include everything. This is the default value.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-21 UTC."],[],[]] 
