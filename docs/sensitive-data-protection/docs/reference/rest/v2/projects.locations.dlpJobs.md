---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs
title: REST Resource: projects.locations.dlpJobs \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:34.747907+00:00
---

# REST Resource: projects.locations.dlpJobs  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  REST Resource: projects.locations.dlpJobs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DlpJob
    * JSON representation
  * Methods



## Resource: DlpJob

Combines all of the information about a DLP job.

JSON representation  
---  
      
    
    {
      "name": string,
      "type": enum ([DlpJobType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob.DlpJobType)),
      "state": enum ([JobState](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob.JobState)),
      "createTime": string,
      "startTime": string,
      "endTime": string,
      "lastModified": string,
      "jobTriggerName": string,
      "errors": [
        {
          object ([Error](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Error))
        }
      ],
      "actionDetails": [
        {
          object ([ActionDetails](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob.ActionDetails))
        }
      ],
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "riskDetails": {
        object ([AnalyzeDataSourceRiskDetails](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob.AnalyzeDataSourceRiskDetails))
      },
      "inspectDetails": {
        object ([InspectDataSourceDetails](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob.InspectDataSourceDetails))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Output only. The server-assigned name.  
`type` |  `enum (`[DlpJobType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob.DlpJobType)`)` The type of job.  
`state` |  `enum (`[JobState](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob.JobState)`)` Output only. State of a job.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time when the job was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time when the job started.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time when the job finished.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastModified` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time when the job was last modified by the system.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`jobTriggerName` |  `string` Output only. If created by a job trigger, the resource name of the trigger that instantiated the job.  
`errors[]` |  `object (`[Error](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Error)`)` Output only. A stream of errors encountered running the job.  
`actionDetails[]` |  `object (`[ActionDetails](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob.ActionDetails)`)` Output only. Events that should occur after the job has completed.  
Job details. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`riskDetails` |  `object (`[AnalyzeDataSourceRiskDetails](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob.AnalyzeDataSourceRiskDetails)`)` Results from analyzing risk of a data source.  
`inspectDetails` |  `object (`[InspectDataSourceDetails](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob.InspectDataSourceDetails)`)` Results from inspecting a data source.  
End of mutually exclusive fields.  
  
## Methods  
  
---  
  
### `[cancel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs/cancel)`

|  Starts asynchronous cancellation on a long-running DlpJob.  
  
### `[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs/create)`

|  Creates a new job to inspect storage or calculate risk metrics.  
  
### `[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs/delete)`

|  Deletes a long-running DlpJob.  
  
### `[finish](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs/finish)`

|  Finish a running hybrid DlpJob.  
  
### `[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs/get)`

|  Gets the latest state of a long-running DlpJob.  
  
### `[hybridInspect](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs/hybridInspect)`

|  Inspect hybrid content and store findings to a job.  
  
### `[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs/list)`

|  Lists DlpJobs that match the specified filter in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-05 UTC."],[],[]] 
