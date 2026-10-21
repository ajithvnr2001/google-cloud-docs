---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.assessmentRules
title: REST Resource: projects.locations.assessmentRules \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:45:58.614427+00:00
---

# REST Resource: projects.locations.assessmentRules  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.assessmentRules

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  REST Resource: projects.locations.assessmentRules Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: AssessmentRule
    * JSON representation
  * SampleRule
    * JSON representation
  * ScheduleInfo
    * JSON representation
  * Methods



## Resource: AssessmentRule

The CCAI Insights project wide assessment rule. This assessment rule will be applied to all conversations from the previous sampling cycle that match the sample rule defined in the assessment rule. One project can have multiple assessment rules.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "active": boolean,
      "sampleRule": {
        object ([SampleRule](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.assessmentRules#SampleRule))
      },
      "scheduleInfo": {
        object ([ScheduleInfo](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.assessmentRules#ScheduleInfo))
      },
      "displayName": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the assessment rule. Format: projects/{project}/locations/{location}/assessmentRules/{assessmentRule}  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which this assessment rule was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The most recent time at which this assessment rule was updated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`active` |  `boolean` If true, apply this rule to conversations. Otherwise, this rule is inactive.  
`sampleRule` |  `object (`[SampleRule](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.assessmentRules#SampleRule)`)` The sample rule for the assessment rule.  
`scheduleInfo` |  `object (`[ScheduleInfo](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.assessmentRules#ScheduleInfo)`)` Schedule info for the assessment rule.  
`displayName` |  `string` Display Name of the assessment rule.  
  
## SampleRule

Message for sampling conversations.

JSON representation  
---  
      
    
    {
      "dimension": string,
      "conversationFilter": string,
    
      // Union field SampleVolume can be only one of the following:
      "samplePercentage": number,
      "sampleRow": string
      // End of list of possible types for union field SampleVolume.
    }  
  
Fields  
---  
`dimension` |  `string` Optional. Group by dimension to sample the conversation. If no dimension is provided, the sampling will be applied to the project level. Current supported dimensions is 'qualityMetadata.agent_info.agent_id'.  
`conversationFilter` |  `string` To specify the filter for the conversions that should apply this sample rule. An empty filter means this sample rule applies to all conversations.  
Union field `SampleVolume`. Determines how the conversations are selected. `SampleVolume` can be only one of the following:  
`samplePercentage` |  `number` Percentage of conversations that we should sample based on the dimension between [0, 100].  
`sampleRow` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of the conversations that we should sample based on the dimension.  
  
## ScheduleInfo

Message for schedule info.

JSON representation  
---  
      
    
    {
      "startTime": string,
      "endTime": string,
      "schedule": string,
      "timeZone": string
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Start time of the schedule. If not specified, will start as soon as the schedule is created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` End time of the schedule. If not specified, will keep scheduling new pipelines for execution util the schedule is no longer active or deleted.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`schedule` |  `string` The groc expression. Format: `every [number] [time_unit] [synchronized]` Time units can be: minutes, hours Synchronized is optional and indicates that the schedule should be synchronized to the start of the interval: every 5 minutes synchronized means 00:00, 00:05 ... Otherwise the start time is random within the interval. Example: `every 5 minutes` could be 00:02, 00:07, 00:12, ...  
`timeZone` |  `string` The timezone to use for the groc expression. If not specified, defaults to UTC.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.assessmentRules/create)`

|  Creates an assessment rule.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.assessmentRules/delete)`

|  Deletes an assessment rule.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.assessmentRules/get)`

|  Get an assessment rule.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.assessmentRules/list)`

|  Lists assessment rules.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.assessmentRules/patch)`

|  Updates an assessment rule.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
