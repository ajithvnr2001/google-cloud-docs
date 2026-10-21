---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.views
title: REST Resource: projects.locations.views \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:51:09.434988+00:00
---

# REST Resource: projects.locations.views  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.views

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  REST Resource: projects.locations.views Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: View
    * JSON representation
  * Methods



## Resource: View

The View resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "createTime": string,
      "updateTime": string,
      "value": string
    }  
  
Fields  
---  
`name` |  `string` Immutable. The resource name of the view. Format: projects/{project}/locations/{location}/views/{view}  
`displayName` |  `string` The human-readable display name of the view.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which this view was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The most recent time at which the view was updated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`value` |  `string` A filter to reduce conversation results to a specific subset. Refer to <https://cloud.google.com/gemini-enterprise-cx/insights/filtering> for details.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.views/create)`

|  Creates a view.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.views/delete)`

|  Deletes a view.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.views/get)`

|  Gets a view.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.views/list)`

|  Lists views.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.views/patch)`

|  Updates a view.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
