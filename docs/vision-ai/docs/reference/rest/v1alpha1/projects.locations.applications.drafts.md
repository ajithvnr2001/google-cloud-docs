---
url: https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/projects.locations.applications.drafts
title: REST Resource: projects.locations.applications.drafts \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:14:07.642806+00:00
---

# REST Resource: projects.locations.applications.drafts  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/projects.locations.applications.drafts

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Reference ](https://docs.cloud.google.com/vision-ai/docs/reference/rest)



Send feedback 

#  REST Resource: projects.locations.applications.drafts Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Draft
    * JSON representation
  * Methods



## Resource: Draft

Message describing Draft object

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "displayName": string,
      "description": string,
      "draftApplicationConfigs": {
        object ([ApplicationConfigs](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/ApplicationConfigs))
      }
    }  
  
Fields  
---  
`name` |  `string` name of resource  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. [Output only] Create timestampA timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. [Output only] Create timestampA timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`labels` |  `map (key: string, value: string)` Labels as key value pairsAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`displayName` |  `string` Required. A user friendly display name for the solution.  
`description` |  `string` A description for this application.  
`draftApplicationConfigs` |  `object (`[ApplicationConfigs](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/ApplicationConfigs)`)` The draft application configs which haven't been updated to an application.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/projects.locations.applications.drafts/create)`

|  Creates a new Draft in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/projects.locations.applications.drafts/delete)`

|  Deletes a single Draft.  
  
### `[get](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/projects.locations.applications.drafts/get)`

|  Gets details of a single Draft.  
  
### `[list](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/projects.locations.applications.drafts/list)`

|  Lists Drafts in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/projects.locations.applications.drafts/patch)`

|  Updates the parameters of a single Draft.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
