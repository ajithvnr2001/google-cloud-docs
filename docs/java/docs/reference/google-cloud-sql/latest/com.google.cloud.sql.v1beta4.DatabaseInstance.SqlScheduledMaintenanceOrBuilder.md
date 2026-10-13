---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.DatabaseInstance.SqlScheduledMaintenanceOrBuilder
title: Interface DatabaseInstance.SqlScheduledMaintenanceOrBuilder (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:27.290035+00:00
---

# Interface DatabaseInstance.SqlScheduledMaintenanceOrBuilder (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.DatabaseInstance.SqlScheduledMaintenanceOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DatabaseInstance.SqlScheduledMaintenanceOrBuilder (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public static interface DatabaseInstance.SqlScheduledMaintenanceOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCanDefer() (deprecated)
    
    
    public abstract boolean getCanDefer()

**Deprecated.** _google.cloud.sql.v1beta4.DatabaseInstance.SqlScheduledMaintenance.can_defer is deprecated. See google/cloud/sql/v1beta4/cloud_sql_resources.proto;l=672_

`bool can_defer = 2 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The canDefer.  
  
### getCanReschedule()
    
    
    public abstract boolean getCanReschedule()

If the scheduled maintenance can be rescheduled.

`bool can_reschedule = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The canReschedule.  
  
### getScheduleDeadlineTime()
    
    
    public abstract Timestamp getScheduleDeadlineTime()

Maintenance cannot be rescheduled to start beyond this deadline.

`optional .google.protobuf.Timestamp schedule_deadline_time = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The scheduleDeadlineTime.  
  
### getScheduleDeadlineTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getScheduleDeadlineTimeOrBuilder()

Maintenance cannot be rescheduled to start beyond this deadline.

`optional .google.protobuf.Timestamp schedule_deadline_time = 4;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getStartTime()
    
    
    public abstract Timestamp getStartTime()

The start time of any upcoming scheduled maintenance for this instance.

`.google.protobuf.Timestamp start_time = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The startTime.  
  
### getStartTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getStartTimeOrBuilder()

The start time of any upcoming scheduled maintenance for this instance.

`.google.protobuf.Timestamp start_time = 1;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasScheduleDeadlineTime()
    
    
    public abstract boolean hasScheduleDeadlineTime()

Maintenance cannot be rescheduled to start beyond this deadline.

`optional .google.protobuf.Timestamp schedule_deadline_time = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the scheduleDeadlineTime field is set.  
  
### hasStartTime()
    
    
    public abstract boolean hasStartTime()

The start time of any upcoming scheduled maintenance for this instance.

`.google.protobuf.Timestamp start_time = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the startTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
