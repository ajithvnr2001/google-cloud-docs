---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs.revisions
title: REST Resource: projects.locations.brands.channelConfigs.revisions \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:47:47.314068+00:00
---

# REST Resource: projects.locations.brands.channelConfigs.revisions  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs.revisions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)



Send feedback 

#  REST Resource: projects.locations.brands.channelConfigs.revisions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ChannelConfigRevision
    * JSON representation
  * Methods



## Resource: ChannelConfigRevision

A revision of a channel configuration.

JSON representation  
---  
      
    
    {
      "name": string,
      "snapshot": {
        object ([ChannelConfig](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig))
      },
      "createTime": string,
      "createdBy": string,
      "alternateIds": [
        string
      ],
      "action": enum ([RevisionAction](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/RevisionAction))
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the channel config revision. Format: projects/{project}/locations/{location}/brands/{brand}/channelConfigs/{channelConfig}/revisions/{revision}  
`snapshot` |  `object (`[ChannelConfig](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig)`)` Output only. The state of the channel config resource at this revision.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the revision was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`createdBy` |  `string` Output only. The email of the user who recently created the resource.  
`alternateIds[]` |  `string` Output only. Alternate IDs for this revision.  
`action` |  `enum (`[RevisionAction](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/RevisionAction)`)` Output only. The action that created this revision.  
  
## Methods  
  
---  
  
### `[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs.revisions/delete)`

|  Deletes the specified ChannelConfigRevision.  
  
### `[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs.revisions/get)`

|  Gets a ChannelConfigRevision.  
  
### `[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs.revisions/list)`

|  Lists ChannelConfigRevisions.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-23 UTC."],[],[]] 
