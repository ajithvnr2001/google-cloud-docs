---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands/listHistory/
title: Method: projects.locations.brands.listHistory \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:37:59.372847+00:00
---

# Method: projects.locations.brands.listHistory  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands/listHistory/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)
  * [ Reference ](https://docs.cloud.google.com/food-ai/apis)



Send feedback 

#  Method: projects.locations.brands.listHistory Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * HistoryEntry
    * JSON representation



Lists history entries for a brand.

### HTTP request

`GET https://foodorderingaiagent.googleapis.com/v1/{parent=projects/*/locations/*/brands/*}:listHistory`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The brand to list history for. Format: projects/{project}/locations/{location}/brands/{brand}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of history entries to return.  
`pageToken` |  `string` Optional. A page token, received from a previous `brands.listHistory` call.  
`filter` |  `string` Optional. A filter expression to filter the results. Supported filters: - `user`: Filter by creator user. - `timestamp`: Filter by commit time. - `resourceType`: Filter by resource type.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[MenuService.ListBrandHistory](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands/listHistory#google.cloud.foodorderingaiagent.v1.MenuService.ListBrandHistory)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "brandHistory": [
        {
          object ([HistoryEntry](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands/listHistory#HistoryEntry))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`brandHistory[]` |  `object (`[HistoryEntry](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands/listHistory#HistoryEntry)`)` The history entries.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## HistoryEntry

History entry for a resource revision.

JSON representation  
---  
      
    
    {
      "commitTime": string,
      "createdBy": string,
      "revisionName": string,
      "resourceType": string,
      "action": enum ([RevisionAction](https://docs.cloud.google.com/food-ai/reference/rest/v1/RevisionAction)),
    
      // Union field resource_revision can be only one of the following:
      "brand": {
        object ([Brand](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands#Brand))
      },
      "store": {
        object ([Store](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores#Store))
      },
      "channelConfig": {
        object ([ChannelConfig](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.channelConfigs#ChannelConfig))
      },
      "configApplicationRule": {
        object ([ConfigApplicationRule](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.configApplicationRules#ConfigApplicationRule))
      }
      // End of list of possible types for union field resource_revision.
    }  
  
Fields  
---  
`commitTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time the revision was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`createdBy` |  `string` The user or service that created the revision.  
`revisionName` |  `string` The full resource name of the revision.  
`resourceType` |  `string` The type of the base resource (e.g., "Brand", "Store", "ChannelConfig").  
`action` |  `enum (`[RevisionAction](https://docs.cloud.google.com/food-ai/reference/rest/v1/RevisionAction)`)` The action that created this revision.  
Union field `resource_revision`. The resource revision. `resource_revision` can be only one of the following:  
`brand` |  `object (`[Brand](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands#Brand)`)` The brand at the time of the commit.  
`store` |  `object (`[Store](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores#Store)`)` The store at the time of the commit.  
`channelConfig` |  `object (`[ChannelConfig](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.channelConfigs#ChannelConfig)`)` The channel config at the time of the commit.  
`configApplicationRule` |  `object (`[ConfigApplicationRule](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.configApplicationRules#ConfigApplicationRule)`)` The config application rule at the time of the commit.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-21 UTC."],[],[]] 
