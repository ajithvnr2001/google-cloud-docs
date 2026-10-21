---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments
title: REST Resource: projects.patchDeployments \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:25:42.125297+00:00
---

# REST Resource: projects.patchDeployments  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: projects.patchDeployments Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: PatchDeployment
    * JSON representation
  * OneTimeSchedule
    * JSON representation
  * RecurringSchedule
    * JSON representation
  * Frequency
  * WeeklySchedule
    * JSON representation
  * MonthlySchedule
    * JSON representation
  * WeekDayOfMonth
    * JSON representation
  * State
  * Methods



## Resource: PatchDeployment

Patch deployments are configurations that individual patch jobs use to complete a patch. These configurations include instance filter, package repository settings, and a schedule. For more information about creating and managing patch deployments, see [Scheduling patch jobs](https://cloud.google.com/compute/docs/os-patch-management/schedule-patch-jobs).

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "instanceFilter": {
        object ([PatchInstanceFilter](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchInstanceFilter))
      },
      "patchConfig": {
        object ([PatchConfig](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig))
      },
      "duration": string,
      "createTime": string,
      "updateTime": string,
      "lastExecuteTime": string,
      "rollout": {
        object ([PatchRollout](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchRollout))
      },
      "state": enum ([State](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments#State)),
    
      // Union field schedule can be only one of the following:
      "oneTimeSchedule": {
        object ([OneTimeSchedule](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments#OneTimeSchedule))
      },
      "recurringSchedule": {
        object ([RecurringSchedule](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments#RecurringSchedule))
      }
      // End of list of possible types for union field schedule.
    }  
  
Fields  
---  
`name` |  `string` Unique name for the patch deployment resource in a project. The patch deployment name is in the form: `projects/{projectId}/patchDeployments/{patchDeploymentId}`. This field is ignored when you create a new patch deployment.  
`description` |  `string` Optional. Description of the patch deployment. Length of the description is limited to 1024 characters.  
`instanceFilter` |  `object (`[PatchInstanceFilter](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchInstanceFilter)`)` Required. VM instances to patch.  
`patchConfig` |  `object (`[PatchConfig](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig)`)` Optional. Patch configuration that is applied.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Duration of the patch. After the duration ends, the patch times out.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time the patch deployment was created. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time the patch deployment was last updated. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastExecuteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last time a patch job was started by this deployment. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`rollout` |  `object (`[PatchRollout](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchRollout)`)` Optional. Rollout strategy of the patch job.  
`state` |  `enum (`[State](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments#State)`)` Output only. Current state of the patch deployment.  
Union field `schedule`. Schedule for the patch. `schedule` can be only one of the following:  
`oneTimeSchedule` |  `object (`[OneTimeSchedule](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments#OneTimeSchedule)`)` Required. Schedule a one-time execution.  
`recurringSchedule` |  `object (`[RecurringSchedule](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments#RecurringSchedule)`)` Required. Schedule recurring executions.  
  
## OneTimeSchedule

Sets the time for a one time patch deployment. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.

JSON representation  
---  
      
    
    {
      "executeTime": string
    }  
  
Fields  
---  
`executeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. The desired patch job execution time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## RecurringSchedule

Sets the time for recurring patch deployments.

JSON representation  
---  
      
    
    {
      "timeZone": {
        object ([TimeZone](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/TimeZone))
      },
      "startTime": string,
      "endTime": string,
      "timeOfDay": {
        object ([TimeOfDay](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/TimeOfDay))
      },
      "frequency": enum ([Frequency](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments#Frequency)),
      "lastExecuteTime": string,
      "nextExecuteTime": string,
    
      // Union field schedule_config can be only one of the following:
      "weekly": {
        object ([WeeklySchedule](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments#WeeklySchedule))
      },
      "monthly": {
        object ([MonthlySchedule](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments#MonthlySchedule))
      }
      // End of list of possible types for union field schedule_config.
    }  
  
Fields  
---  
`timeZone` |  `object (`[TimeZone](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/TimeZone)`)` Required. Defines the time zone that `timeOfDay` is relative to. The rules for daylight saving time are determined by the chosen time zone.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The time that the recurring schedule becomes effective. Defaults to `createTime` of the patch deployment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The end time at which a recurring patch deployment schedule is no longer active.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`timeOfDay` |  `object (`[TimeOfDay](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/TimeOfDay)`)` Required. Time of the day to run a recurring deployment.  
`frequency` |  `enum (`[Frequency](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments#Frequency)`)` Required. The frequency unit of this recurring schedule.  
`lastExecuteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the last patch job ran successfully.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`nextExecuteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the next patch job is scheduled to run.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `schedule_config`. Configurations for this recurring schedule. Configurations must match frequency. `schedule_config` can be only one of the following:  
`weekly` |  `object (`[WeeklySchedule](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments#WeeklySchedule)`)` Required. Schedule with weekly executions.  
`monthly` |  `object (`[MonthlySchedule](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments#MonthlySchedule)`)` Required. Schedule with monthly executions.  
  
## Frequency

Specifies the frequency of the recurring patch deployments.

Enums  
---  
`FREQUENCY_UNSPECIFIED` | Invalid. A frequency must be specified.  
`WEEKLY` | Indicates that the frequency of recurrence should be expressed in terms of weeks.  
`MONTHLY` | Indicates that the frequency of recurrence should be expressed in terms of months.  
`DAILY` | Indicates that the frequency of recurrence should be expressed in terms of days.  
  
## WeeklySchedule

Represents a weekly schedule.

JSON representation  
---  
      
    
    {
      "dayOfWeek": enum ([DayOfWeek](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/DayOfWeek))
    }  
  
Fields  
---  
`dayOfWeek` |  `enum (`[DayOfWeek](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/DayOfWeek)`)` Required. Day of the week.  
  
## MonthlySchedule

Represents a monthly schedule. An example of a valid monthly schedule is "on the third Tuesday of the month" or "on the 15th of the month".

JSON representation  
---  
      
    
    {
    
      // Union field day_of_month can be only one of the following:
      "weekDayOfMonth": {
        object ([WeekDayOfMonth](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments#WeekDayOfMonth))
      },
      "monthDay": integer
      // End of list of possible types for union field day_of_month.
    }  
  
Fields  
---  
Union field `day_of_month`. One day in a month. `day_of_month` can be only one of the following:  
`weekDayOfMonth` |  `object (`[WeekDayOfMonth](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments#WeekDayOfMonth)`)` Required. Week day in a month.  
`monthDay` |  `integer` Required. One day of the month. 1-31 indicates the 1st to the 31st day. -1 indicates the last day of the month. Months without the target day will be skipped. For example, a schedule to run "every month on the 31st" will not run in February, April, June, etc.  
  
## WeekDayOfMonth

Represents one week day in a month. An example is "the 4th Sunday".

JSON representation  
---  
      
    
    {
      "weekOrdinal": integer,
      "dayOfWeek": enum ([DayOfWeek](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/DayOfWeek)),
      "dayOffset": integer
    }  
  
Fields  
---  
`weekOrdinal` |  `integer` Required. Week number in a month. 1-4 indicates the 1st to 4th week of the month. -1 indicates the last week of the month.  
`dayOfWeek` |  `enum (`[DayOfWeek](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/DayOfWeek)`)` Required. A day of the week.  
`dayOffset` |  `integer` Optional. Represents the number of days before or after the given week day of month that the patch deployment is scheduled for. For example if `weekOrdinal` and `dayOfWeek` values point to the second Tuesday of the month and the `dayOffset` value is set to `3`, patch deployment takes place three days after the second Tuesday of the month. If this value is negative, for example -5, patches are deployed five days before the second Tuesday of the month. Allowed values are in range [-30, 30].  
  
## State

Represents state of patch peployment.

Enums  
---  
`STATE_UNSPECIFIED` | The default value. This value is used if the state is omitted.  
`ACTIVE` | Active value means that patch deployment generates Patch Jobs.  
`PAUSED` | Paused value means that patch deployment does not generate Patch jobs. Requires user action to move in and out from this state.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments/create)`

|  Create an OS Config patch deployment.  
  
### `[delete](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments/delete)`

|  Delete an OS Config patch deployment.  
  
### `[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments/get)`

|  Get an OS Config patch deployment.  
  
### `[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments/list)`

|  Get a page of OS Config patch deployments.  
  
### `[patch](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments/patch)`

|  Update an OS Config patch deployment.  
  
### `[pause](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments/pause)`

|  Change state of patch deployment to "PAUSED".  
  
### `[resume](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments/resume)`

|  Change state of patch deployment back to "ACTIVE".  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-17 UTC."],[],[]] 
