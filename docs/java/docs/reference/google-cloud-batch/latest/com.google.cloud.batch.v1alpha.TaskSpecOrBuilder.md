---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.TaskSpecOrBuilder
title: Interface TaskSpecOrBuilder (0.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:46:37.432063+00:00
---

# Interface TaskSpecOrBuilder (0.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.TaskSpecOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface TaskSpecOrBuilder (0.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.99.0 (latest)  0.95.0  0.94.0  0.93.0  0.91.0  0.88.0  0.87.0  0.85.0  0.83.0  0.82.0  0.81.0  0.80.0  0.78.0  0.76.0  0.75.0  0.74.0  0.73.0  0.72.0  0.70.0  0.68.0  0.67.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.2  0.2.2  0.1.1 
    
    
    public interface TaskSpecOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsEnvironments(String key) (deprecated)
    
    
    public abstract boolean containsEnvironments(String key)

Deprecated: please use environment(non-plural) instead.

`map<string, string> environments = 6 [deprecated = true];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getComputeResource()
    
    
    public abstract ComputeResource getComputeResource()

ComputeResource requirements.

`.google.cloud.batch.v1alpha.ComputeResource compute_resource = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ComputeResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ComputeResource)` | The computeResource.  
  
### getComputeResourceOrBuilder()
    
    
    public abstract ComputeResourceOrBuilder getComputeResourceOrBuilder()

ComputeResource requirements.

`.google.cloud.batch.v1alpha.ComputeResource compute_resource = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ComputeResourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ComputeResourceOrBuilder)` |   
  
### getEnvironment()
    
    
    public abstract Environment getEnvironment()

Environment variables to set before running the Task.

`.google.cloud.batch.v1alpha.Environment environment = 10;`

**Returns**  
---  
**Type** | **Description**  
`[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Environment)` | The environment.  
  
### getEnvironmentOrBuilder()
    
    
    public abstract EnvironmentOrBuilder getEnvironmentOrBuilder()

Environment variables to set before running the Task.

`.google.cloud.batch.v1alpha.Environment environment = 10;`

**Returns**  
---  
**Type** | **Description**  
`[EnvironmentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.EnvironmentOrBuilder)` |   
  
### getEnvironments() (deprecated)
    
    
    public abstract Map<String,String> getEnvironments()

Use [#getEnvironmentsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.TaskSpecOrBuilder#com_google_cloud_batch_v1alpha_TaskSpecOrBuilder_getEnvironmentsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getEnvironmentsCount() (deprecated)
    
    
    public abstract int getEnvironmentsCount()

Deprecated: please use environment(non-plural) instead.

`map<string, string> environments = 6 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getEnvironmentsMap() (deprecated)
    
    
    public abstract Map<String,String> getEnvironmentsMap()

Deprecated: please use environment(non-plural) instead.

`map<string, string> environments = 6 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getEnvironmentsOrDefault(String key, String defaultValue) (deprecated)
    
    
    public abstract String getEnvironmentsOrDefault(String key, String defaultValue)

Deprecated: please use environment(non-plural) instead.

`map<string, string> environments = 6 [deprecated = true];`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getEnvironmentsOrThrow(String key) (deprecated)
    
    
    public abstract String getEnvironmentsOrThrow(String key)

Deprecated: please use environment(non-plural) instead.

`map<string, string> environments = 6 [deprecated = true];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLifecyclePolicies(int index)
    
    
    public abstract LifecyclePolicy getLifecyclePolicies(int index)

Lifecycle management schema when any task in a task group is failed. Currently we only support one lifecycle policy. When the lifecycle policy condition is met, the action in the policy will execute. If task execution result does not meet with the defined lifecycle policy, we consider it as the default policy. Default policy means if the exit code is 0, exit task. If task ends with non-zero exit code, retry the task with max_retry_count.

`repeated .google.cloud.batch.v1alpha.LifecyclePolicy lifecycle_policies = 9;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LifecyclePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.LifecyclePolicy)` |   
  
### getLifecyclePoliciesCount()
    
    
    public abstract int getLifecyclePoliciesCount()

Lifecycle management schema when any task in a task group is failed. Currently we only support one lifecycle policy. When the lifecycle policy condition is met, the action in the policy will execute. If task execution result does not meet with the defined lifecycle policy, we consider it as the default policy. Default policy means if the exit code is 0, exit task. If task ends with non-zero exit code, retry the task with max_retry_count.

`repeated .google.cloud.batch.v1alpha.LifecyclePolicy lifecycle_policies = 9;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLifecyclePoliciesList()
    
    
    public abstract List<LifecyclePolicy> getLifecyclePoliciesList()

Lifecycle management schema when any task in a task group is failed. Currently we only support one lifecycle policy. When the lifecycle policy condition is met, the action in the policy will execute. If task execution result does not meet with the defined lifecycle policy, we consider it as the default policy. Default policy means if the exit code is 0, exit task. If task ends with non-zero exit code, retry the task with max_retry_count.

`repeated .google.cloud.batch.v1alpha.LifecyclePolicy lifecycle_policies = 9;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[LifecyclePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.LifecyclePolicy)>` |   
  
### getLifecyclePoliciesOrBuilder(int index)
    
    
    public abstract LifecyclePolicyOrBuilder getLifecyclePoliciesOrBuilder(int index)

Lifecycle management schema when any task in a task group is failed. Currently we only support one lifecycle policy. When the lifecycle policy condition is met, the action in the policy will execute. If task execution result does not meet with the defined lifecycle policy, we consider it as the default policy. Default policy means if the exit code is 0, exit task. If task ends with non-zero exit code, retry the task with max_retry_count.

`repeated .google.cloud.batch.v1alpha.LifecyclePolicy lifecycle_policies = 9;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LifecyclePolicyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.LifecyclePolicyOrBuilder)` |   
  
### getLifecyclePoliciesOrBuilderList()
    
    
    public abstract List<? extends LifecyclePolicyOrBuilder> getLifecyclePoliciesOrBuilderList()

Lifecycle management schema when any task in a task group is failed. Currently we only support one lifecycle policy. When the lifecycle policy condition is met, the action in the policy will execute. If task execution result does not meet with the defined lifecycle policy, we consider it as the default policy. Default policy means if the exit code is 0, exit task. If task ends with non-zero exit code, retry the task with max_retry_count.

`repeated .google.cloud.batch.v1alpha.LifecyclePolicy lifecycle_policies = 9;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.batch.v1alpha.LifecyclePolicyOrBuilder>` |   
  
### getMaxRetryCount()
    
    
    public abstract int getMaxRetryCount()

Maximum number of retries on failures. The default, 0, which means never retry. The valid value range is [0, 10].

`int32 max_retry_count = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The maxRetryCount.  
  
### getMaxRunDuration()
    
    
    public abstract Duration getMaxRunDuration()

Maximum duration the task should run before being automatically retried (if enabled) or automatically failed. Format the value of this field as a time limit in seconds followed by `s`&mdash;for example, `3600s` for 1 hour. The field accepts any value between 0 and the maximum listed for the `Duration` field type at <https://protobuf.dev/reference/protobuf/google.protobuf/#duration>; however, the actual maximum run time for a job will be limited to the maximum run time for a job listed at <https://cloud.google.com/batch/quotas#max-job-duration>.

`.google.protobuf.Duration max_run_duration = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The maxRunDuration.  
  
### getMaxRunDurationOrBuilder()
    
    
    public abstract DurationOrBuilder getMaxRunDurationOrBuilder()

Maximum duration the task should run before being automatically retried (if enabled) or automatically failed. Format the value of this field as a time limit in seconds followed by `s`&mdash;for example, `3600s` for 1 hour. The field accepts any value between 0 and the maximum listed for the `Duration` field type at <https://protobuf.dev/reference/protobuf/google.protobuf/#duration>; however, the actual maximum run time for a job will be limited to the maximum run time for a job listed at <https://cloud.google.com/batch/quotas#max-job-duration>.

`.google.protobuf.Duration max_run_duration = 4;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getRunnables(int index)
    
    
    public abstract Runnable getRunnables(int index)

Required. The sequence of one or more runnables (executable scripts, executable containers, and/or barriers) for each task in this task group to run. Each task runs this list of runnables in order. For a task to succeed, all of its script and container runnables each must meet at least one of the following conditions:

  * The runnable exited with a zero status.
  * The runnable didn't finish, but you enabled its `background` subfield.
  * The runnable exited with a non-zero status, but you enabled its `ignore_exit_status` subfield.



`repeated .google.cloud.batch.v1alpha.Runnable runnables = 8;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Runnable)` |   
  
### getRunnablesCount()
    
    
    public abstract int getRunnablesCount()

Required. The sequence of one or more runnables (executable scripts, executable containers, and/or barriers) for each task in this task group to run. Each task runs this list of runnables in order. For a task to succeed, all of its script and container runnables each must meet at least one of the following conditions:

  * The runnable exited with a zero status.
  * The runnable didn't finish, but you enabled its `background` subfield.
  * The runnable exited with a non-zero status, but you enabled its `ignore_exit_status` subfield.



`repeated .google.cloud.batch.v1alpha.Runnable runnables = 8;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getRunnablesList()
    
    
    public abstract List<Runnable> getRunnablesList()

Required. The sequence of one or more runnables (executable scripts, executable containers, and/or barriers) for each task in this task group to run. Each task runs this list of runnables in order. For a task to succeed, all of its script and container runnables each must meet at least one of the following conditions:

  * The runnable exited with a zero status.
  * The runnable didn't finish, but you enabled its `background` subfield.
  * The runnable exited with a non-zero status, but you enabled its `ignore_exit_status` subfield.



`repeated .google.cloud.batch.v1alpha.Runnable runnables = 8;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Runnable](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Runnable)>` |   
  
### getRunnablesOrBuilder(int index)
    
    
    public abstract RunnableOrBuilder getRunnablesOrBuilder(int index)

Required. The sequence of one or more runnables (executable scripts, executable containers, and/or barriers) for each task in this task group to run. Each task runs this list of runnables in order. For a task to succeed, all of its script and container runnables each must meet at least one of the following conditions:

  * The runnable exited with a zero status.
  * The runnable didn't finish, but you enabled its `background` subfield.
  * The runnable exited with a non-zero status, but you enabled its `ignore_exit_status` subfield.



`repeated .google.cloud.batch.v1alpha.Runnable runnables = 8;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RunnableOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.RunnableOrBuilder)` |   
  
### getRunnablesOrBuilderList()
    
    
    public abstract List<? extends RunnableOrBuilder> getRunnablesOrBuilderList()

Required. The sequence of one or more runnables (executable scripts, executable containers, and/or barriers) for each task in this task group to run. Each task runs this list of runnables in order. For a task to succeed, all of its script and container runnables each must meet at least one of the following conditions:

  * The runnable exited with a zero status.
  * The runnable didn't finish, but you enabled its `background` subfield.
  * The runnable exited with a non-zero status, but you enabled its `ignore_exit_status` subfield.



`repeated .google.cloud.batch.v1alpha.Runnable runnables = 8;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.batch.v1alpha.RunnableOrBuilder>` |   
  
### getVolumes(int index)
    
    
    public abstract Volume getVolumes(int index)

Volumes to mount before running Tasks using this TaskSpec.

`repeated .google.cloud.batch.v1alpha.Volume volumes = 7;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Volume](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Volume)` |   
  
### getVolumesCount()
    
    
    public abstract int getVolumesCount()

Volumes to mount before running Tasks using this TaskSpec.

`repeated .google.cloud.batch.v1alpha.Volume volumes = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getVolumesList()
    
    
    public abstract List<Volume> getVolumesList()

Volumes to mount before running Tasks using this TaskSpec.

`repeated .google.cloud.batch.v1alpha.Volume volumes = 7;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Volume](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Volume)>` |   
  
### getVolumesOrBuilder(int index)
    
    
    public abstract VolumeOrBuilder getVolumesOrBuilder(int index)

Volumes to mount before running Tasks using this TaskSpec.

`repeated .google.cloud.batch.v1alpha.Volume volumes = 7;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VolumeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.VolumeOrBuilder)` |   
  
### getVolumesOrBuilderList()
    
    
    public abstract List<? extends VolumeOrBuilder> getVolumesOrBuilderList()

Volumes to mount before running Tasks using this TaskSpec.

`repeated .google.cloud.batch.v1alpha.Volume volumes = 7;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.batch.v1alpha.VolumeOrBuilder>` |   
  
### hasComputeResource()
    
    
    public abstract boolean hasComputeResource()

ComputeResource requirements.

`.google.cloud.batch.v1alpha.ComputeResource compute_resource = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the computeResource field is set.  
  
### hasEnvironment()
    
    
    public abstract boolean hasEnvironment()

Environment variables to set before running the Task.

`.google.cloud.batch.v1alpha.Environment environment = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the environment field is set.  
  
### hasMaxRunDuration()
    
    
    public abstract boolean hasMaxRunDuration()

Maximum duration the task should run before being automatically retried (if enabled) or automatically failed. Format the value of this field as a time limit in seconds followed by `s`&mdash;for example, `3600s` for 1 hour. The field accepts any value between 0 and the maximum listed for the `Duration` field type at <https://protobuf.dev/reference/protobuf/google.protobuf/#duration>; however, the actual maximum run time for a job will be limited to the maximum run time for a job listed at <https://cloud.google.com/batch/quotas#max-job-duration>.

`.google.protobuf.Duration max_run_duration = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the maxRunDuration field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
