---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands
title: REST Resource: projects.locations.brands \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:37:58.961304+00:00
---

# REST Resource: projects.locations.brands  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)
  * [ Reference ](https://docs.cloud.google.com/food-ai/apis)



Send feedback 

#  REST Resource: projects.locations.brands Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Brand
    * JSON representation
  * Methods



## Resource: Brand

A brand, which can be a restaurant chain or an individual restaurant.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "createTime": string,
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The brand name. Format: projects/{project}/locations/{location}/brands/{brand}  
`displayName` |  `string` Optional. Optional, human-readable display name for this brand for user interfaces.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time this brand was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time this brand was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Methods  
  
---  
  
### `[computeAnalyticsMetrics](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands/computeAnalyticsMetrics)`

|  Computes analytics metrics for a given brand for specified time period with optional store filter.  
  
### `[create](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands/create)`

|  Creates a brand.  
  
### `[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands/delete)`

|  Deletes the specified brand.  
  
### `[get](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands/get)`

|  Gets a brand.  
  
### `[list](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands/list)`

|  Lists brands.  
  
### `[listHistory](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands/listHistory)`

|  Lists history entries for a brand.  
  
### `[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands/patch)`

|  Updates the specified brand.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-21 UTC."],[],[]] 
