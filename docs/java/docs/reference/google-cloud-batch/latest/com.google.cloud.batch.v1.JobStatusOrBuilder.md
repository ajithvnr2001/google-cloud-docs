---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobStatusOrBuilder
title: Interface JobStatusOrBuilder (0.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:39:13.052047+00:00
---

# Interface JobStatusOrBuilder (0.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobStatusOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface JobStatusOrBuilder (0.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.99.0 (latest)  0.95.0  0.94.0  0.93.0  0.91.0  0.88.0  0.87.0  0.85.0  0.83.0  0.82.0  0.81.0  0.80.0  0.78.0  0.76.0  0.75.0  0.74.0  0.73.0  0.72.0  0.70.0  0.68.0  0.67.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.2  0.2.2  0.1.1 
    
    
    public interface JobStatusOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsTaskGroups(String key)
    
    
    public abstract boolean containsTaskGroups(String key)

Aggregated task status for each TaskGroup in the Job. The map key is TaskGroup ID.

`map<string, .google.cloud.batch.v1.JobStatus.TaskGroupStatus> task_groups = 4; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getRunDuration()
    
    
    public abstract Duration getRunDuration()

The duration of time that the Job spent in status RUNNING.

`.google.protobuf.Duration run_duration = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The runDuration.  
  
### getRunDurationOrBuilder()
    
    
    public abstract DurationOrBuilder getRunDurationOrBuilder()

The duration of time that the Job spent in status RUNNING.

`.google.protobuf.Duration run_duration = 5;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getState()
    
    
    public abstract JobStatus.State getState()

Job state

`.google.cloud.batch.v1.JobStatus.State state = 1;`

**Returns**  
---  
**Type** | **Description**  
`[JobStatus.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobStatus.State)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Job state

`.google.cloud.batch.v1.JobStatus.State state = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getStatusEvents(int index)
    
    
    public abstract StatusEvent getStatusEvents(int index)

Job status events

`repeated .google.cloud.batch.v1.StatusEvent status_events = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StatusEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.StatusEvent)` |   
  
### getStatusEventsCount()
    
    
    public abstract int getStatusEventsCount()

Job status events

`repeated .google.cloud.batch.v1.StatusEvent status_events = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getStatusEventsList()
    
    
    public abstract List<StatusEvent> getStatusEventsList()

Job status events

`repeated .google.cloud.batch.v1.StatusEvent status_events = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[StatusEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.StatusEvent)>` |   
  
### getStatusEventsOrBuilder(int index)
    
    
    public abstract StatusEventOrBuilder getStatusEventsOrBuilder(int index)

Job status events

`repeated .google.cloud.batch.v1.StatusEvent status_events = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StatusEventOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.StatusEventOrBuilder)` |   
  
### getStatusEventsOrBuilderList()
    
    
    public abstract List<? extends StatusEventOrBuilder> getStatusEventsOrBuilderList()

Job status events

`repeated .google.cloud.batch.v1.StatusEvent status_events = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.batch.v1.StatusEventOrBuilder>` |   
  
### getTaskGroups() (deprecated)
    
    
    public abstract Map<String,JobStatus.TaskGroupStatus> getTaskGroups()

Use [#getTaskGroupsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobStatusOrBuilder#com_google_cloud_batch_v1_JobStatusOrBuilder_getTaskGroupsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[TaskGroupStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobStatus.TaskGroupStatus)>` |   
  
### getTaskGroupsCount()
    
    
    public abstract int getTaskGroupsCount()

Aggregated task status for each TaskGroup in the Job. The map key is TaskGroup ID.

`map<string, .google.cloud.batch.v1.JobStatus.TaskGroupStatus> task_groups = 4; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getTaskGroupsMap()
    
    
    public abstract Map<String,JobStatus.TaskGroupStatus> getTaskGroupsMap()

Aggregated task status for each TaskGroup in the Job. The map key is TaskGroup ID.

`map<string, .google.cloud.batch.v1.JobStatus.TaskGroupStatus> task_groups = 4; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[TaskGroupStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobStatus.TaskGroupStatus)>` |   
  
### getTaskGroupsOrDefault(String key, JobStatus.TaskGroupStatus defaultValue)
    
    
    public abstract JobStatus.TaskGroupStatus getTaskGroupsOrDefault(String key, JobStatus.TaskGroupStatus defaultValue)

Aggregated task status for each TaskGroup in the Job. The map key is TaskGroup ID.

`map<string, .google.cloud.batch.v1.JobStatus.TaskGroupStatus> task_groups = 4; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[JobStatus.TaskGroupStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobStatus.TaskGroupStatus)`  
  
**Returns**  
---  
**Type** | **Description**  
`[JobStatus.TaskGroupStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobStatus.TaskGroupStatus)` |   
  
### getTaskGroupsOrThrow(String key)
    
    
    public abstract JobStatus.TaskGroupStatus getTaskGroupsOrThrow(String key)

Aggregated task status for each TaskGroup in the Job. The map key is TaskGroup ID.

`map<string, .google.cloud.batch.v1.JobStatus.TaskGroupStatus> task_groups = 4; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[JobStatus.TaskGroupStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobStatus.TaskGroupStatus)` |   
  
### hasRunDuration()
    
    
    public abstract boolean hasRunDuration()

The duration of time that the Job spent in status RUNNING.

`.google.protobuf.Duration run_duration = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the runDuration field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
