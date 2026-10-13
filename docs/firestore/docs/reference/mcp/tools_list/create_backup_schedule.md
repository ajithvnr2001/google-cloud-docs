---
url: https://docs.cloud.google.com/firestore/docs/reference/mcp/tools_list/create_backup_schedule/
title: MCP Tools Reference: firestore.googleapis.com \u00a0|\u00a0 Firestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:28:39.208316+00:00
---

# MCP Tools Reference: firestore.googleapis.com  |  Firestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/reference/mcp/tools_list/create_backup_schedule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback 

#  MCP Tools Reference: firestore.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `create_backup_schedule`

Create a Firestore backup schedule.

The following code sample shows how to use `curl` to call the `create_backup_schedule` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://firestore.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "create_backup_schedule",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

The request for `FirestoreAdmin.CreateBackupSchedule`.

### CreateBackupScheduleRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "backupSchedule": {
        object ([BackupSchedule](https://docs.cloud.google.com/firestore/docs/reference/mcp/tools_list/create_backup_schedule#Input.Schema.BackupSchedule))
      }
    }  
  
Fields  
---  
`parent` |  `string` Required. The parent database.Format `projects/{project}/databases/{database}`  
`backupSchedule` |  `object (`[BackupSchedule](https://docs.cloud.google.com/firestore/docs/reference/mcp/tools_list/create_backup_schedule#Input.Schema.BackupSchedule)`)` Required. The backup schedule to create.  
  
### BackupSchedule

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "retention": string,
    
      // Union field recurrence can be only one of the following:
      "dailyRecurrence": {
        object (DailyRecurrence)
      },
      "weeklyRecurrence": {
        object ([WeeklyRecurrence](https://docs.cloud.google.com/firestore/docs/reference/mcp/tools_list/create_backup_schedule#Input.Schema.WeeklyRecurrence))
      }
      // End of list of possible types for union field recurrence.
    }  
  
Fields  
---  
`name` |  `string` Output only. The unique backup schedule identifier across all locations and databases for the given project.This will be auto-assigned.Format is `projects/{project}/databases/{database}/backupSchedules/{backup_schedule}`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp at which this backup schedule was created and effective since.No backups will be created for this schedule before this time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp at which this backup schedule was most recently updated. When a backup schedule is first created, this is the same as create_time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`retention` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` At what relative time in the future, compared to its creation time, the backup should be deleted, e.g. keep backups for 7 days.The maximum supported retention period is 14 weeks.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
Union field `recurrence`. A oneof field to represent when backups will be taken. `recurrence` can be only one of the following:  
`dailyRecurrence` |  `object (`DailyRecurrence`)` For a schedule that runs daily.  
`weeklyRecurrence` |  `object (`[WeeklyRecurrence](https://docs.cloud.google.com/firestore/docs/reference/mcp/tools_list/create_backup_schedule#Input.Schema.WeeklyRecurrence)`)` For a schedule that runs weekly on a specific day.  
  
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
  
### Duration

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Signed seconds of the span of time. Must be from -315,576,000,000 to +315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`nanos` |  `integer` Signed fractions of a second at nanosecond resolution of the span of time. Durations less than one second are represented with a 0 `seconds` field and a positive or negative `nanos` field. For durations of one second or more, a non-zero value for the `nanos` field must be of the same sign as the `seconds` field. Must be from -999,999,999 to +999,999,999 inclusive.  
  
### WeeklyRecurrence

JSON representation  
---  
      
    
    {
      "day": enum ([DayOfWeek](https://docs.cloud.google.com/firestore/docs/reference/mcp/tools_list/create_backup_schedule#Input.Schema.DayOfWeek))
    }  
  
Fields  
---  
`day` |  `enum (`[DayOfWeek](https://docs.cloud.google.com/firestore/docs/reference/mcp/tools_list/create_backup_schedule#Input.Schema.DayOfWeek)`)` The day of week to run.DAY_OF_WEEK_UNSPECIFIED is not allowed.  
  
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
  
## Output Schema

A backup schedule for a Cloud Firestore Database.

This resource is owned by the database it is backing up, and is deleted along with the database. The actual backups are not though.

### BackupSchedule

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "retention": string,
    
      // Union field recurrence can be only one of the following:
      "dailyRecurrence": {
        object (DailyRecurrence)
      },
      "weeklyRecurrence": {
        object ([WeeklyRecurrence](https://docs.cloud.google.com/firestore/docs/reference/mcp/tools_list/create_backup_schedule#Input.Schema.WeeklyRecurrence))
      }
      // End of list of possible types for union field recurrence.
    }  
  
Fields  
---  
`name` |  `string` Output only. The unique backup schedule identifier across all locations and databases for the given project.This will be auto-assigned.Format is `projects/{project}/databases/{database}/backupSchedules/{backup_schedule}`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp at which this backup schedule was created and effective since.No backups will be created for this schedule before this time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp at which this backup schedule was most recently updated. When a backup schedule is first created, this is the same as create_time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`retention` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` At what relative time in the future, compared to its creation time, the backup should be deleted, e.g. keep backups for 7 days.The maximum supported retention period is 14 weeks.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
Union field `recurrence`. A oneof field to represent when backups will be taken. `recurrence` can be only one of the following:  
`dailyRecurrence` |  `object (`DailyRecurrence`)` For a schedule that runs daily.  
`weeklyRecurrence` |  `object (`[WeeklyRecurrence](https://docs.cloud.google.com/firestore/docs/reference/mcp/tools_list/create_backup_schedule#Input.Schema.WeeklyRecurrence)`)` For a schedule that runs weekly on a specific day.  
  
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
  
### Duration

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Signed seconds of the span of time. Must be from -315,576,000,000 to +315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`nanos` |  `integer` Signed fractions of a second at nanosecond resolution of the span of time. Durations less than one second are represented with a 0 `seconds` field and a positive or negative `nanos` field. For durations of one second or more, a non-zero value for the `nanos` field must be of the same sign as the `seconds` field. Must be from -999,999,999 to +999,999,999 inclusive.  
  
### WeeklyRecurrence

JSON representation  
---  
      
    
    {
      "day": enum ([DayOfWeek](https://docs.cloud.google.com/firestore/docs/reference/mcp/tools_list/create_backup_schedule#Input.Schema.DayOfWeek))
    }  
  
Fields  
---  
`day` |  `enum (`[DayOfWeek](https://docs.cloud.google.com/firestore/docs/reference/mcp/tools_list/create_backup_schedule#Input.Schema.DayOfWeek)`)` The day of week to run.DAY_OF_WEEK_UNSPECIFIED is not allowed.  
  
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
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-10 UTC."],[],[]] 
