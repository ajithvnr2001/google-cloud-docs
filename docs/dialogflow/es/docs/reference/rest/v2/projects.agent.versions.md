---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.versions
title: REST Resource: projects.agent.versions \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:17.199035+00:00
---

# REST Resource: projects.agent.versions  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.versions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  REST Resource: projects.agent.versions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Version
    * JSON representation
    * VersionStatus
  * Methods



## Resource: Version

You can create multiple versions of your agent and publish them to separate environments.

When you edit an agent, you are editing the draft agent. At any point, you can save the draft agent as an agent version, which is an immutable snapshot of your agent.

When you save the draft agent, it is published to the default environment. When you create agent versions, you can publish them to custom environments. You can create a variety of custom environments for:

  * testing
  * development
  * production
  * etc.



For more information, see the [versions and environments guide](https://cloud.google.com/dialogflow/docs/agents-versions).

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "versionNumber": integer,
      "createTime": string,
      "status": enum ([VersionStatus](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.versions#Version.VersionStatus))
    }  
  
Fields  
---  
`name` |  `string` Output only. The unique identifier of this agent version. Supported formats:

  * `projects/<Project ID>/agent/versions/<Version ID>`
  * `projects/<Project ID>/locations/<Location ID>/agent/versions/<Version ID>`

  
`description` |  `string` Optional. The developer-provided description of this version.  
`versionNumber` |  `integer` Output only. The sequential number of this version. This field is read-only which means it cannot be set by create and update methods.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The creation time of this version. This field is read-only, i.e., it cannot be set by create and update methods.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`status` |  `enum (`[VersionStatus](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.versions#Version.VersionStatus)`)` Output only. The status of this version. This field is read-only and cannot be set by create and update methods.  
  
### VersionStatus

The status of a version.

Enums  
---  
`VERSION_STATUS_UNSPECIFIED` | Not specified. This value is not used.  
`IN_PROGRESS` | Version is not ready to serve (e.g. training is in progress).  
`READY` | Version is ready to serve.  
`FAILED` | Version training failed.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.versions/create)`

|  Creates an agent version.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.versions/delete)`

|  Delete the specified agent version.  
  
### `[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.versions/get)`

|  Retrieves the specified agent version.  
  
### `[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.versions/list)`

|  Returns the list of all versions of the specified agent.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.versions/patch)`

|  Updates the specified agent version.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-21 UTC."],[],[]] 
