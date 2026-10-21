---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs/list/
title: Method: projects.locations.brands.channelConfigs.list \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:27:34.961872+00:00
---

# Method: projects.locations.brands.channelConfigs.list  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)



Send feedback 

#  Method: projects.locations.brands.channelConfigs.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes



Lists ChannelConfigs.

### HTTP request

`GET https://foodorderingaiagent.googleapis.com/v1beta/{parent=projects/*/locations/*/brands/*}/channelConfigs`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent brand, which owns this collection of channel configs. Format: projects/{project}/locations/{location}/brands/{brand}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of channel configs to return. The service may return fewer than this value.  
`pageToken` |  `string` Optional. A page token, received from a previous `channelConfigs.list` call. Provide this to retrieve the subsequent page.  
`filter` |  `string` Optional. A filter expression that filters the results. The expression syntax is documented in <https://google.aip.dev/160>.The following fields are supported: - `type`Examples: - `type="AGENT_CUSTOMIZATION"`  
  
### Request body

The request body must be empty.

### Response body

Response message for `[MenuService.ListChannelConfigs](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs/list#google.cloud.foodorderingaiagent.v1beta.MenuService.ListChannelConfigs)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "channelConfigs": [
        {
          object ([ChannelConfig](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`channelConfigs[]` |  `object (`[ChannelConfig](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig)`)` The channel configs from the specified collection.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-01 UTC."],[],[]] 
