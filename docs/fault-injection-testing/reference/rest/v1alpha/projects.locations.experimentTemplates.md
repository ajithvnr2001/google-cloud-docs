---
url: https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experimentTemplates
title: REST Resource: projects.locations.experimentTemplates \u00a0|\u00a0 Fault Injection Testing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:11:42.880788+00:00
---

# REST Resource: projects.locations.experimentTemplates  |  Fault Injection Testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experimentTemplates

To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Reference ](https://docs.cloud.google.com/fault-injection-testing/apis)



Send feedback 

#  REST Resource: projects.locations.experimentTemplates Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ExperimentTemplate
    * JSON representation
  * Methods



## Resource: ExperimentTemplate

Template for a failure-injection experiment.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "duration": string,
      "createTime": string,
      "updateTime": string,
      "action": {
        object ([Action](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Action))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of this experiment template. Format: `projects/{project}/locations/{location}/experimentTemplates/{experimentTemplate}`  
`displayName` |  `string` Optional. Human-readable template name. Min length 0, max 1000.  
`description` |  `string` Optional. Optional user-provided description or notes. Min length 0. Max length 2000.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Required. How long the experiment is intended to run. Min duration is 0, max is 10 days.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the template was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the template was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`action` |  `object (`[Action](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Action)`)` Required. The action to be performed.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experimentTemplates/create)`

|  Creates a new experiment template.  
  
### `[delete](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experimentTemplates/delete)`

|  Deletes an experiment template.  
  
### `[get](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experimentTemplates/get)`

|  Retrieves the details of a specific experiment template.  
  
### `[list](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experimentTemplates/list)`

|  Lists all experiment templates in a specified project and location.  
  
### `[patch](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experimentTemplates/patch)`

|  Updates an existing experiment template.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-21 UTC."],[],[]] 
