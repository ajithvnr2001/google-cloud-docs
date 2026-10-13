---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers
title: REST Resource: projects.jobTriggers \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:28.635851+00:00
---

# REST Resource: projects.jobTriggers  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  REST Resource: projects.jobTriggers Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: JobTrigger
    * JSON representation
    * Trigger
      * JSON representation
    * Schedule
      * JSON representation
    * Manual
    * Status
  * Methods



## Resource: JobTrigger

Contains a configuration to make API calls on a repeating basis. See <https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-job-triggers> to learn more.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "triggers": [
        {
          object ([Trigger](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers#JobTrigger.Trigger))
        }
      ],
      "errors": [
        {
          object ([Error](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Error))
        }
      ],
      "createTime": string,
      "updateTime": string,
      "lastRunTime": string,
      "status": enum ([Status](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers#JobTrigger.Status)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "inspectJob": {
        object ([InspectJobConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Output only. Unique resource name for the triggeredJob, assigned by the service when the triggeredJob is created, for example `projects/dlp-test-project/jobTriggers/53234423`.  
`displayName` |  `string` Display name (max 100 chars)  
`description` |  `string` User provided description (max 256 chars)  
`triggers[]` |  `object (`[Trigger](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers#JobTrigger.Trigger)`)` A list of triggers which will be OR'ed together. Only one in the list needs to trigger for a job to be started. The list may contain only a single Schedule trigger and must have at least one object.  
`errors[]` |  `object (`[Error](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Error)`)` Output only. A stream of errors encountered when the trigger was activated. Repeated errors may result in the JobTrigger automatically being paused. Will return the last 100 errors. Whenever the JobTrigger is modified this list will be cleared.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The creation timestamp of a triggeredJob.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last update timestamp of a triggeredJob.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastRunTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp of the last time this trigger executed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`status` |  `enum (`[Status](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers#JobTrigger.Status)`)` Required. A status for this trigger.  
The configuration details for the specific type of job to run. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`inspectJob` |  `object (`[InspectJobConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig)`)` For inspect jobs, a snapshot of the configuration.  
End of mutually exclusive fields.  
  
### Trigger

What event needs to occur for a new job to be started.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "schedule": {
        object ([Schedule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers#JobTrigger.Schedule))
      },
      "manual": {
        object ([Manual](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers#JobTrigger.Manual))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
What event needs to occur for a new job to be started. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`schedule` |  `object (`[Schedule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers#JobTrigger.Schedule)`)` Create a job on a repeating basis based on the elapse of time.  
`manual` |  `object (`[Manual](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers#JobTrigger.Manual)`)` For use with hybrid jobs. Jobs must be manually created and finished.  
End of mutually exclusive fields.  
  
### Schedule

Schedule for inspect job triggers.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "recurrencePeriodDuration": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Type of schedule. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`recurrencePeriodDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` With this option a job is started on a regular periodic basis. For example: every day (86400 seconds).A scheduled start time will be skipped if the previous execution has not ended when its scheduled time occurs.This value must be set to a time duration greater than or equal to 1 day and can be no longer than 60 days.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
End of mutually exclusive fields.  
  
### Manual

This type has no fields.

Job trigger option for hybrid jobs. Jobs must be manually created and finished.

### Status

Whether the trigger is currently active. If PAUSED or CANCELLED, no jobs will be created with this configuration. The service may automatically pause triggers experiencing frequent errors. To restart a job, set the status to HEALTHY after correcting user errors.

Enums  
---  
`STATUS_UNSPECIFIED` | Unused.  
`HEALTHY` | Trigger is healthy.  
`PAUSED` | Trigger is temporarily paused.  
`CANCELLED` | Trigger is cancelled and can not be resumed.  
  
## Methods  
  
---  
  
### `[activate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers/activate)`

|  Activate a job trigger.  
  
### `[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers/create)`

|  Creates a job trigger to run DLP actions such as scanning storage for sensitive information on a set schedule.  
  
### `[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers/delete)`

|  Deletes a job trigger.  
  
### `[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers/get)`

|  Gets a job trigger.  
  
### `[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers/list)`

|  Lists job triggers.  
  
### `[patch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers/patch)`

|  Updates a job trigger.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-05 UTC."],[],[]] 
