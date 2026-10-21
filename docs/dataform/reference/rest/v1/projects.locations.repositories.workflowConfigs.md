---
url: https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowConfigs
title: REST Resource: projects.locations.repositories.workflowConfigs \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:42:05.947452+00:00
---

# REST Resource: projects.locations.repositories.workflowConfigs  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowConfigs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Dataform ](https://docs.cloud.google.com/dataform)
  * [ Reference ](https://docs.cloud.google.com/dataform/docs/authentication)



Send feedback 

#  REST Resource: projects.locations.repositories.workflowConfigs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: WorkflowConfig
    * JSON representation
  * ScheduledExecutionRecord
    * JSON representation
  * Methods



## Resource: WorkflowConfig

Represents a Dataform workflow configuration.

JSON representation  
---  
      
    
    {
      "name": string,
      "releaseConfig": string,
      "invocationConfig": {
        object ([InvocationConfig](https://docs.cloud.google.com/dataform/reference/rest/v1/InvocationConfig))
      },
      "cronSchedule": string,
      "timeZone": string,
      "recentScheduledExecutionRecords": [
        {
          object ([ScheduledExecutionRecord](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowConfigs#ScheduledExecutionRecord))
        }
      ],
      "disabled": boolean,
      "createTime": string,
      "updateTime": string,
      "internalMetadata": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The workflow config's name.  
`releaseConfig` |  `string` Required. The name of the release config whose releaseCompilationResult should be executed. Must be in the format `projects/*/locations/*/repositories/*/releaseConfigs/*`.  
`invocationConfig` |  `object (`[InvocationConfig](https://docs.cloud.google.com/dataform/reference/rest/v1/InvocationConfig)`)` Optional. If left unset, a default InvocationConfig will be used.  
`cronSchedule` |  `string` Optional. Optional schedule (in cron format) for automatic execution of this workflow config.  
`timeZone` |  `string` Optional. Specifies the time zone to be used when interpreting cronSchedule. Must be a time zone name from the [time zone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). If left unspecified, the default is `UTC`.  
`recentScheduledExecutionRecords[]` |  `object (`[ScheduledExecutionRecord](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowConfigs#ScheduledExecutionRecord)`)` Output only. Records of the 10 most recent scheduled execution attempts, ordered in descending order of `executionTime`. Updated whenever automatic creation of a workflow invocation is triggered by cronSchedule.  
`disabled` |  `boolean` Optional. Disables automatic creation of workflow invocations.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp of when the WorkflowConfig was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp of when the WorkflowConfig was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`internalMetadata` |  `string` Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.  
  
## ScheduledExecutionRecord

A record of an attempt to create a workflow invocation for this workflow config.

JSON representation  
---  
      
    
    {
      "executionTime": string,
    
      // Union field result can be only one of the following:
      "workflowInvocation": string,
      "errorStatus": {
        object ([Status](https://docs.cloud.google.com/dataform/reference/rest/Shared.Types/ListOperationsResponse#Status))
      }
      // End of list of possible types for union field result.
    }  
  
Fields  
---  
`executionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp of this execution attempt.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `result`. The result of this execution attempt. `result` can be only one of the following:  
`workflowInvocation` |  `string` The name of the created workflow invocation, if one was successfully created. Must be in the format `projects/*/locations/*/repositories/*/workflowInvocations/*`.  
`errorStatus` |  `object (`[Status](https://docs.cloud.google.com/dataform/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` The error status encountered upon this attempt to create the workflow invocation, if the attempt was unsuccessful.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowConfigs/create)`

|  Creates a new WorkflowConfig in a given Repository.  
  
### `[delete](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowConfigs/delete)`

|  Deletes a single WorkflowConfig.  
  
### `[get](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowConfigs/get)`

|  Fetches a single WorkflowConfig.  
  
### `[list](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowConfigs/list)`

|  Lists WorkflowConfigs in a given Repository.  
  
### `[patch](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowConfigs/patch)`

|  Updates a single WorkflowConfig.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-28 UTC."],[],[]] 
