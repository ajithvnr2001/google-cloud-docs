---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets
title: REST Resource: projects.locations.datasets \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:27:58.377010+00:00
---

# REST Resource: projects.locations.datasets  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  REST Resource: projects.locations.datasets Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Dataset
    * JSON representation
  * Type
  * Methods



## Resource: Dataset

Dataset resource represents a collection of conversations that may be bounded (Static Dataset, e.g. golden dataset for training), or unbounded (Dynamic Dataset, e.g. live traffic, or agent training traffic)

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "type": enum ([Type](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets#Type)),
      "ttl": string,
      "createTime": string,
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` Immutable. Identifier. Resource name of the dataset. Format: projects/{project}/locations/{location}/datasets/{dataset}  
`displayName` |  `string` Display name for the dataaset  
`description` |  `string` Dataset description.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets#Type)`)` Dataset usage type.  
`ttl` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Option TTL for the dataset.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Dataset create time.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Dataset update time.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Type

Type of datasat: For evals or sampled from live traffic.

Enums  
---  
`TYPE_UNSPECIFIED` | Default value for unspecified.  
`EVAL` | For evals only.  
`LIVE` | Dataset with new conversations coming in regularly (Insights legacy conversations and AI trainer)  
  
## Methods  
  
---  
  
### `[bulkDeleteFeedbackLabels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets/bulkDeleteFeedbackLabels)`

|  Delete feedback labels in bulk using a filter.  
  
### `[bulkDownloadFeedbackLabels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets/bulkDownloadFeedbackLabels)`

|  Download feedback labels in bulk from an external source.  
  
### `[bulkUploadFeedbackLabels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets/bulkUploadFeedbackLabels)`

|  Upload feedback labels from an external source in bulk.  
  
### `[listAllFeedbackLabels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets/listAllFeedbackLabels)`

|  List all feedback labels by project number.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
