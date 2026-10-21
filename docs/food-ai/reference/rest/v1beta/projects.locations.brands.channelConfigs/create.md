---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs/create/
title: Method: projects.locations.brands.channelConfigs.create \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:23:09.087612+00:00
---

# Method: projects.locations.brands.channelConfigs.create  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)



Send feedback 

#  Method: projects.locations.brands.channelConfigs.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes



Creates a ChannelConfig.

### HTTP request

`POST https://foodorderingaiagent.googleapis.com/v1beta/{parent=projects/*/locations/*/brands/*}/channelConfigs`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent brand, which owns this collection of channel configs. Format: projects/{project}/locations/{location}/brands/{brand}  
  
### Query parameters

Parameters  
---  
`channelConfigId` |  `string` Optional. The ID to use for the channel config, which will become the final component of the channel config's resource name.This value should only contain lower-case letters, numbers, and hyphens, with a 63 character maximum. The first character must be a letter, and the last character must be a letter or number.  
  
### Request body

The request body contains an instance of `[ChannelConfig](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig)`.

### Response body

If successful, the response body contains a newly created instance of `[ChannelConfig](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs#ChannelConfig)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-16 UTC."],[],[]] 
