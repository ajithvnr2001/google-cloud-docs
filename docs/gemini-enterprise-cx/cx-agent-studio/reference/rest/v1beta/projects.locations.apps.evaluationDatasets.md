---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationDatasets
title: REST Resource: projects.locations.apps.evaluationDatasets \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:46.793548+00:00
---

# REST Resource: projects.locations.apps.evaluationDatasets  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationDatasets

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  REST Resource: projects.locations.apps.evaluationDatasets Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: EvaluationDataset
    * JSON representation
  * Methods



## Resource: EvaluationDataset

An evaluation dataset represents a set of evaluations that are grouped together basaed on shared tags.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "evaluations": [
        string
      ],
      "createTime": string,
      "updateTime": string,
      "etag": string,
      "createdBy": string,
      "lastUpdatedBy": string,
      "aggregatedMetrics": {
        object ([AggregatedMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of this evaluation dataset. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationDatasets/{evaluationDataset}`  
`displayName` |  `string` Required. User-defined display name of the evaluation dataset. Unique within an App.  
`evaluations[]` |  `string` Optional. Evaluations that are included in this dataset.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the evaluation dataset was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the evaluation dataset was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Output only. Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`createdBy` |  `string` Output only. The user who created the evaluation dataset.  
`lastUpdatedBy` |  `string` Output only. The user who last updated the evaluation dataset.  
`aggregatedMetrics` |  `object (`[AggregatedMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AggregatedMetrics)`)` Output only. The aggregated metrics for this evaluation dataset across all runs.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationDatasets/create)`

|  Creates an evaluation dataset.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationDatasets/delete)`

|  Deletes an evaluation dataset.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationDatasets/get)`

|  Gets details of the specified evaluation dataset.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationDatasets/list)`

|  Lists all evaluation datasets in the given app.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationDatasets/patch)`

|  Updates an evaluation dataset.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-01 UTC."],[],[]] 
