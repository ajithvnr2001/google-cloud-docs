---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/GetBackupPlan/
title: MCP Tools Reference: backupdr.googleapis.com \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:42.282984+00:00
---

# MCP Tools Reference: backupdr.googleapis.com  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/GetBackupPlan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Reference ](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/reference)



Send feedback 

#  MCP Tools Reference: backupdr.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `GetBackupPlan`

Retrieves the details and configuration of a specific BackupPlan by name.

The following sample demonstrate how to use `curl` to invoke the `GetBackupPlan` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://backupdr.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "GetBackupPlan",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

The request message for getting a `BackupPlan`.

### GetBackupPlanRequest

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. The resource name of the `BackupPlan` to retrieve.Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}`  
  
## Output Schema

A `BackupPlan` specifies some common fields, such as `description` as well as one or more `BackupRule` messages. Each `BackupRule` has a retention policy and defines a schedule by which the system is to perform backup workloads.

### BackupPlan

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "labels": {
        string: string,
        ...
      },
      "createTime": string,
      "updateTime": string,
      "backupRules": [
        {
          object ([BackupRule](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlans#Output.Schema.BackupRule))
        }
      ],
      "maxCustomOnDemandRetentionDays": integer,
      "state": enum ([State](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlans#Output.Schema.State)),
      "resourceType": string,
      "etag": string,
      "backupVault": string,
      "backupVaultServiceAccount": string,
      "logRetentionDays": string,
      "supportedResourceTypes": [
        string
      ],
      "revisionId": string,
      "revisionName": string,
    
      // Union field resource_properties can be only one of the following:
      "diskBackupPlanProperties": {
        object ([DiskBackupPlanProperties](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlans#Output.Schema.DiskBackupPlanProperties))
      },
      "computeInstanceBackupPlanProperties": {
        object ([ComputeInstanceBackupPlanProperties](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlans#Output.Schema.ComputeInstanceBackupPlanProperties))
      }
      // End of list of possible types for union field resource_properties.
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The resource name of the `BackupPlan`.Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}`  
`description` |  `string` Optional. The description of the `BackupPlan` resource.The description allows for additional details about `BackupPlan` and its use cases to be provided. An example description is the following: "This is a backup plan that performs a daily backup at 6pm and retains data for 3 months". The description must be at most 2048 characters.  
`labels` |  `map (key: string, value: string)` Optional. This collection of key/value pairs allows for custom labels to be supplied by the user. Example, {"tag": "Weekly"}.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the `BackupPlan` was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the `BackupPlan` was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`backupRules[]` |  `object (`[BackupRule](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlans#Output.Schema.BackupRule)`)` Optional. The backup rules for this `BackupPlan`.  
`maxCustomOnDemandRetentionDays` |  `integer` Optional. Optional field to configure the maximum number of days for which a backup can be retained. This field is only applicable for on-demand backups taken with custom retention value.  
`state` |  `enum (`[State](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlans#Output.Schema.State)`)` Output only. The `State` for the `BackupPlan`.  
`resourceType` |  `string` Required. The resource type to which the `BackupPlan` will be applied. Examples include, "compute.googleapis.com/Instance", "sqladmin.googleapis.com/Instance", "alloydb.googleapis.com/Cluster", "compute.googleapis.com/Disk".  
`etag` |  `string` Optional. `etag` is returned from the service in the response. As a user of the service, you may provide an etag value in this field to prevent stale resources.  
`backupVault` |  `string` Required. Resource name of backup vault which will be used as storage location for backups. Format: projects/{project}/locations/{location}/backupVaults/{backupvault}  
`backupVaultServiceAccount` |  `string` Output only. The Google Cloud service account to be used by the BackupVault for taking backups. Specify the email address of the Backup Vault Service Account.  
`logRetentionDays` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Applicable only for Cloud SQL resource_type.Configures how long logs will be stored. It is defined in “days”. This value should be greater than or equal to minimum enforced log retention duration of the backup vault.  
`supportedResourceTypes[]` |  `string` Output only. All resource types to which backupPlan can be applied.  
`revisionId` |  `string` Output only. The user friendly revision ID of the `BackupPlanRevision`.Example: v0, v1, v2, etc.  
`revisionName` |  `string` Output only. The resource id of the `BackupPlanRevision`.Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision_id}`  
Union field `resource_properties`. Defines optional workload-specific properties for backups generated by this plan. `resource_properties` can be only one of the following:  
`diskBackupPlanProperties` |  `object (`[DiskBackupPlanProperties](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlans#Output.Schema.DiskBackupPlanProperties)`)` Optional. Defines optional properties specific to backups of disk-based resources, such as Compute Engine Persistent Disks. This includes settings like whether to perform a guest flush.  
`computeInstanceBackupPlanProperties` |  `object (`[ComputeInstanceBackupPlanProperties](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlans#Output.Schema.ComputeInstanceBackupPlanProperties)`)` Optional. Defines optional properties specific to backups of compute instance-based resources, such as Compute Engine. This includes settings like whether to perform a guest flush.  
  
### LabelsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### BackupRule

JSON representation  
---  
      
    
    {
      "ruleId": string,
      "backupRetentionDays": integer,
    
      // Union field backup_schedule_oneof can be only one of the following:
      "standardSchedule": {
        object ([StandardSchedule](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlans#Output.Schema.StandardSchedule))
      }
      // End of list of possible types for union field backup_schedule_oneof.
    }  
  
Fields  
---  
`ruleId` |  `string` Required. Immutable. The unique id of this `BackupRule`. The `rule_id` is unique per `BackupPlan`.The `rule_id` must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens. Pattern, /[a-z][a-z0-9-]{,62}/.  
`backupRetentionDays` |  `integer` Required. Configures the duration for which backup data will be kept. It is defined in “days”. The value should be greater than or equal to minimum enforced retention of the backup vault.Minimum value is 1 and maximum value is 36159 for custom retention on-demand backup. Minimum and maximum values are workload specific for all other rules. Note: Longer retention can lead to higher storage costs post introductory trial. We recommend starting with a short duration of 3 days or less.  
Union field `backup_schedule_oneof`. The schedule that defines the automated backup workloads for this `BackupRule`. `backup_schedule_oneof` can be only one of the following:  
`standardSchedule` |  `object (`[StandardSchedule](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlans#Output.Schema.StandardSchedule)`)` Optional. Defines a schedule that runs within the confines of a defined window of time.  
  
### StandardSchedule

JSON representation  
---  
      
    
    {
      "recurrenceType": enum ([RecurrenceType](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlans#Output.Schema.RecurrenceType)),
      "hourlyFrequency": integer,
      "daysOfWeek": [
        enum ([DayOfWeek](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlans#Output.Schema.DayOfWeek))
      ],
      "daysOfMonth": [
        integer
      ],
      "weekDayOfMonth": {
        object ([WeekDayOfMonth](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlans#Output.Schema.WeekDayOfMonth))
      },
      "months": [
        enum ([Month](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlans#Output.Schema.Month))
      ],
      "backupWindow": {
        object ([BackupWindow](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlans#Output.Schema.BackupWindow))
      },
      "timeZone": string
    }  
  
Fields  
---  
`recurrenceType` |  `enum (`[RecurrenceType](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlans#Output.Schema.RecurrenceType)`)` Required. Specifies the `RecurrenceType` for the schedule.  
`hourlyFrequency` |  `integer` Optional. Specifies frequency for hourly backups. A hourly frequency of 1 means jobs will run every 1 hour from start time till end time defined.This is required for `recurrence_type`, `HOURLY` and is not applicable otherwise. A validation error will occur if a value is supplied and `recurrence_type` is not `HOURLY`.The supported values for each resource type are as follows:

  * `compute.googleapis.com/Instance`: 1-23
  * `compute.googleapis.com/Disk`: 1-23
  * `sqladmin.googleapis.com/Instance`: 6-23
  * `alloydb.googleapis.com/Cluster`: 1-23
  * `file.googleapis.com/Instance`: 1-23

Refer to link <https://cloud.google.com/backup-disaster-recovery/docs/concepts/cloud_best_practices> for more details.  
`daysOfWeek[]` |  `enum (`[DayOfWeek](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlans#Output.Schema.DayOfWeek)`)` Optional. Specifies days of week like, MONDAY or TUESDAY, on which jobs will run.This is required for `recurrence_type`, `WEEKLY` and is not applicable otherwise. A validation error will occur if a value is supplied and `recurrence_type` is not `WEEKLY`.  
`daysOfMonth[]` |  `integer` Optional. Specifies days of months like 1, 5, or 14 on which jobs will run.Values for `days_of_month` are only applicable for `recurrence_type`, `MONTHLY` and `YEARLY`. A validation error will occur if other values are supplied.  
`weekDayOfMonth` |  `object (`[WeekDayOfMonth](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlans#Output.Schema.WeekDayOfMonth)`)` Optional. Specifies a week day of the month like, FIRST SUNDAY or LAST MONDAY, on which jobs will run. This will be specified by two fields in `WeekDayOfMonth`, one for the day, e.g. `MONDAY`, and one for the week, e.g. `LAST`.This field is only applicable for `recurrence_type`, `MONTHLY` and `YEARLY`. A validation error will occur if other values are supplied.  
`months[]` |  `enum (`[Month](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlans#Output.Schema.Month)`)` Optional. Specifies the months of year, like `FEBRUARY` and/or `MAY`, on which jobs will run.This field is only applicable when `recurrence_type` is `YEARLY`. A validation error will occur if other values are supplied.  
`backupWindow` |  `object (`[BackupWindow](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlans#Output.Schema.BackupWindow)`)` Required. A BackupWindow defines the window of day during which backup jobs will run. Jobs are queued at the beginning of the window and will be marked as `NOT_RUN` if they do not start by the end of the window.Note: running jobs will not be cancelled at the end of the window.  
`timeZone` |  `string` Required. The time zone to be used when interpreting the schedule. The value of this field must be a time zone name from the IANA tz database. See <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones> for the list of valid timezone names. For example, Europe/Paris.  
  
### WeekDayOfMonth

JSON representation  
---  
      
    
    {
      "weekOfMonth": enum ([WeekOfMonth](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlans#Output.Schema.WeekOfMonth)),
      "dayOfWeek": enum ([DayOfWeek](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlans#Output.Schema.DayOfWeek))
    }  
  
Fields  
---  
`weekOfMonth` |  `enum (`[WeekOfMonth](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlans#Output.Schema.WeekOfMonth)`)` Required. Specifies the week of the month.  
`dayOfWeek` |  `enum (`[DayOfWeek](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp/tools_list/ListBackupPlans#Output.Schema.DayOfWeek)`)` Required. Specifies the day of the week.  
  
### BackupWindow

JSON representation  
---  
      
    
    {
      "startHourOfDay": integer,
      "endHourOfDay": integer
    }  
  
Fields  
---  
`startHourOfDay` |  `integer` Required. The hour of day (0-23) when the window starts for example if value of start hour of day is 6 that mean backup window start at 6:00.  
`endHourOfDay` |  `integer` Required. The hour of day (1-24) when the window end for example if value of end hour of day is 10 that mean backup window end time is 10:00.End hour of day should be greater than start hour of day. 0 <= start_hour_of_day < end_hour_of_day <= 24End hour of day is not include in backup window that mean if end_hour_of_day= 10 jobs should start before 10:00.  
  
### DiskBackupPlanProperties

JSON representation  
---  
      
    
    {
      "guestFlush": boolean
    }  
  
Fields  
---  
`guestFlush` |  `boolean` Optional. Indicates whether to perform a guest flush operation before taking a disk backup. When set to false, the system will create crash-consistent backups. Default value is false.  
  
### ComputeInstanceBackupPlanProperties

JSON representation  
---  
      
    
    {
      "guestFlush": boolean
    }  
  
Fields  
---  
`guestFlush` |  `boolean` Optional. Indicates whether to perform a guest flush operation before taking a compute backup. When set to false, the system will create crash-consistent backups. Default value is false.  
  
### RecurrenceType

`RecurrenceTypes` enumerates the applicable periodicity for the schedule.

Enums  
---  
`RECURRENCE_TYPE_UNSPECIFIED` | recurrence type not set  
`HOURLY` | The `BackupRule` is to be applied hourly.  
`DAILY` | The `BackupRule` is to be applied daily.  
`WEEKLY` | The `BackupRule` is to be applied weekly.  
`MONTHLY` | The `BackupRule` is to be applied monthly.  
`YEARLY` | The `BackupRule` is to be applied yearly.  
  
### DayOfWeek

Represents a day of the week.

Enums  
---  
`DAY_OF_WEEK_UNSPECIFIED` | The day of the week is unspecified.  
`MONDAY` | Monday  
`TUESDAY` | Tuesday  
`WEDNESDAY` | Wednesday  
`THURSDAY` | Thursday  
`FRIDAY` | Friday  
`SATURDAY` | Saturday  
`SUNDAY` | Sunday  
  
### WeekOfMonth

`WeekOfMonth` enumerates possible weeks in the month, e.g. the first, third, or last week of the month.

Enums  
---  
`WEEK_OF_MONTH_UNSPECIFIED` | The zero value. Do not use.  
`FIRST` | The first week of the month.  
`SECOND` | The second week of the month.  
`THIRD` | The third week of the month.  
`FOURTH` | The fourth week of the month.  
`LAST` | The last week of the month.  
  
### Month

Represents a month in the Gregorian calendar.

Enums  
---  
`MONTH_UNSPECIFIED` | The unspecified month.  
`JANUARY` | The month of January.  
`FEBRUARY` | The month of February.  
`MARCH` | The month of March.  
`APRIL` | The month of April.  
`MAY` | The month of May.  
`JUNE` | The month of June.  
`JULY` | The month of July.  
`AUGUST` | The month of August.  
`SEPTEMBER` | The month of September.  
`OCTOBER` | The month of October.  
`NOVEMBER` | The month of November.  
`DECEMBER` | The month of December.  
  
### State

`State` enumerates the possible states for a `BackupPlan`.

Enums  
---  
`STATE_UNSPECIFIED` | State not set.  
`CREATING` | The resource is being created.  
`ACTIVE` | The resource has been created and is fully usable.  
`DELETING` | The resource is being deleted.  
`INACTIVE` | The resource has been created but is not usable.  
`UPDATING` | The resource is being updated.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-28 UTC."],[],[]] 
