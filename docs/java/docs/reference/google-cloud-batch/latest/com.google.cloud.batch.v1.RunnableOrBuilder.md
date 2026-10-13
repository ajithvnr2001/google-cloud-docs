---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.RunnableOrBuilder
title: Interface RunnableOrBuilder (0.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:39:15.132791+00:00
---

# Interface RunnableOrBuilder (0.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.RunnableOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface RunnableOrBuilder (0.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.99.0 (latest)  0.95.0  0.94.0  0.93.0  0.91.0  0.88.0  0.87.0  0.85.0  0.83.0  0.82.0  0.81.0  0.80.0  0.78.0  0.76.0  0.75.0  0.74.0  0.73.0  0.72.0  0.70.0  0.68.0  0.67.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.2  0.2.2  0.1.1 
    
    
    public interface RunnableOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Labels for this Runnable.

`map<string, string> labels = 9;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAlwaysRun()
    
    
    public abstract boolean getAlwaysRun()

By default, after a Runnable fails, no further Runnable are executed. This flag indicates that this Runnable must be run even if the Task has already failed. This is useful for Runnables that copy output files off of the VM or for debugging.

The always_run flag does not override the Task's overall max_run_duration. If the max_run_duration has expired then no further Runnables will execute, not even always_run Runnables.

`bool always_run = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The alwaysRun.  
  
### getBackground()
    
    
    public abstract boolean getBackground()

Normally, a runnable that doesn't exit causes its task to fail. However, you can set this field to `true` to configure a background runnable. Background runnables are allowed continue running in the background while the task executes subsequent runnables. For example, background runnables are useful for providing services to other runnables or providing debugging-support tools like SSH servers.

Specifically, background runnables are killed automatically (if they have not already exited) a short time after all foreground runnables have completed. Even though this is likely to result in a non-zero exit status for the background runnable, these automatic kills are not treated as task failures.

`bool background = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The background.  
  
### getBarrier()
    
    
    public abstract Runnable.Barrier getBarrier()

Barrier runnable.

`.google.cloud.batch.v1.Runnable.Barrier barrier = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Runnable.Barrier](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Barrier)` | The barrier.  
  
### getBarrierOrBuilder()
    
    
    public abstract Runnable.BarrierOrBuilder getBarrierOrBuilder()

Barrier runnable.

`.google.cloud.batch.v1.Runnable.Barrier barrier = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Runnable.BarrierOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.BarrierOrBuilder)` |   
  
### getContainer()
    
    
    public abstract Runnable.Container getContainer()

Container runnable.

`.google.cloud.batch.v1.Runnable.Container container = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Runnable.Container](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Container)` | The container.  
  
### getContainerOrBuilder()
    
    
    public abstract Runnable.ContainerOrBuilder getContainerOrBuilder()

Container runnable.

`.google.cloud.batch.v1.Runnable.Container container = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Runnable.ContainerOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.ContainerOrBuilder)` |   
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Optional. DisplayName is an optional field that can be provided by the caller. If provided, it will be used in logs and other outputs to identify the script, making it easier for users to understand the logs. If not provided the index of the runnable will be used for outputs.

`string display_name = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Optional. DisplayName is an optional field that can be provided by the caller. If provided, it will be used in logs and other outputs to identify the script, making it easier for users to understand the logs. If not provided the index of the runnable will be used for outputs.

`string display_name = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getEnvironment()
    
    
    public abstract Environment getEnvironment()

Environment variables for this Runnable (overrides variables set for the whole Task or TaskGroup).

`.google.cloud.batch.v1.Environment environment = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Environment)` | The environment.  
  
### getEnvironmentOrBuilder()
    
    
    public abstract EnvironmentOrBuilder getEnvironmentOrBuilder()

Environment variables for this Runnable (overrides variables set for the whole Task or TaskGroup).

`.google.cloud.batch.v1.Environment environment = 7;`

**Returns**  
---  
**Type** | **Description**  
`[EnvironmentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.EnvironmentOrBuilder)` |   
  
### getExecutableCase()
    
    
    public abstract Runnable.ExecutableCase getExecutableCase()

**Returns**  
---  
**Type** | **Description**  
`[Runnable.ExecutableCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.ExecutableCase)` |   
  
### getIgnoreExitStatus()
    
    
    public abstract boolean getIgnoreExitStatus()

Normally, a runnable that returns a non-zero exit status fails and causes the task to fail. However, you can set this field to `true` to allow the task to continue executing its other runnables even if this runnable fails.

`bool ignore_exit_status = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The ignoreExitStatus.  
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.RunnableOrBuilder#com_google_cloud_batch_v1_RunnableOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Labels for this Runnable.

`map<string, string> labels = 9;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Labels for this Runnable.

`map<string, string> labels = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Labels for this Runnable.

`map<string, string> labels = 9;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLabelsOrThrow(String key)
    
    
    public abstract String getLabelsOrThrow(String key)

Labels for this Runnable.

`map<string, string> labels = 9;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getScript()
    
    
    public abstract Runnable.Script getScript()

Script runnable.

`.google.cloud.batch.v1.Runnable.Script script = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Runnable.Script](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script)` | The script.  
  
### getScriptOrBuilder()
    
    
    public abstract Runnable.ScriptOrBuilder getScriptOrBuilder()

Script runnable.

`.google.cloud.batch.v1.Runnable.Script script = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Runnable.ScriptOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.ScriptOrBuilder)` |   
  
### getTimeout()
    
    
    public abstract Duration getTimeout()

Timeout for this Runnable.

`.google.protobuf.Duration timeout = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The timeout.  
  
### getTimeoutOrBuilder()
    
    
    public abstract DurationOrBuilder getTimeoutOrBuilder()

Timeout for this Runnable.

`.google.protobuf.Duration timeout = 8;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### hasBarrier()
    
    
    public abstract boolean hasBarrier()

Barrier runnable.

`.google.cloud.batch.v1.Runnable.Barrier barrier = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the barrier field is set.  
  
### hasContainer()
    
    
    public abstract boolean hasContainer()

Container runnable.

`.google.cloud.batch.v1.Runnable.Container container = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the container field is set.  
  
### hasEnvironment()
    
    
    public abstract boolean hasEnvironment()

Environment variables for this Runnable (overrides variables set for the whole Task or TaskGroup).

`.google.cloud.batch.v1.Environment environment = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the environment field is set.  
  
### hasScript()
    
    
    public abstract boolean hasScript()

Script runnable.

`.google.cloud.batch.v1.Runnable.Script script = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the script field is set.  
  
### hasTimeout()
    
    
    public abstract boolean hasTimeout()

Timeout for this Runnable.

`.google.protobuf.Duration timeout = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the timeout field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
