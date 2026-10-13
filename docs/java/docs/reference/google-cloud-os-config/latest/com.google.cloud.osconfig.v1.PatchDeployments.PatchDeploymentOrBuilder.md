---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PatchDeploymentOrBuilder
title: Interface PatchDeployments.PatchDeploymentOrBuilder (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:18:34.480759+00:00
---

# Interface PatchDeployments.PatchDeploymentOrBuilder (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PatchDeploymentOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface PatchDeployments.PatchDeploymentOrBuilder (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.6  2.4.3  2.3.2 
    
    
    public static interface PatchDeployments.PatchDeploymentOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. Time the patch deployment was created. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.

` .google.protobuf.Timestamp create_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Time the patch deployment was created. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.

` .google.protobuf.Timestamp create_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDescription()
    
    
    public abstract String getDescription()

Optional. Description of the patch deployment. Length of the description is limited to 1024 characters.

`string description = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Optional. Description of the patch deployment. Length of the description is limited to 1024 characters.

`string description = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getDuration()
    
    
    public abstract Duration getDuration()

Optional. Duration of the patch. After the duration ends, the patch times out.

`.google.protobuf.Duration duration = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The duration.  
  
### getDurationOrBuilder()
    
    
    public abstract DurationOrBuilder getDurationOrBuilder()

Optional. Duration of the patch. After the duration ends, the patch times out.

`.google.protobuf.Duration duration = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getInstanceFilter()
    
    
    public abstract PatchJobs.PatchInstanceFilter getInstanceFilter()

Required. VM instances to patch.

` .google.cloud.osconfig.v1.PatchInstanceFilter instance_filter = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchInstanceFilter)` | The instanceFilter.  
  
### getInstanceFilterOrBuilder()
    
    
    public abstract PatchJobs.PatchInstanceFilterOrBuilder getInstanceFilterOrBuilder()

Required. VM instances to patch.

` .google.cloud.osconfig.v1.PatchInstanceFilter instance_filter = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchInstanceFilterOrBuilder)` |   
  
### getLastExecuteTime()
    
    
    public abstract Timestamp getLastExecuteTime()

Output only. The last time a patch job was started by this deployment. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.

` .google.protobuf.Timestamp last_execute_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The lastExecuteTime.  
  
### getLastExecuteTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getLastExecuteTimeOrBuilder()

Output only. The last time a patch job was started by this deployment. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.

` .google.protobuf.Timestamp last_execute_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getName()
    
    
    public abstract String getName()

Unique name for the patch deployment resource in a project. The patch deployment name is in the form: `projects/{project_id}/patchDeployments/{patch_deployment_id}`. This field is ignored when you create a new patch deployment.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Unique name for the patch deployment resource in a project. The patch deployment name is in the form: `projects/{project_id}/patchDeployments/{patch_deployment_id}`. This field is ignored when you create a new patch deployment.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getOneTimeSchedule()
    
    
    public abstract PatchDeployments.OneTimeSchedule getOneTimeSchedule()

Required. Schedule a one-time execution.

` .google.cloud.osconfig.v1.OneTimeSchedule one_time_schedule = 6 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[PatchDeployments.OneTimeSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.OneTimeSchedule)` | The oneTimeSchedule.  
  
### getOneTimeScheduleOrBuilder()
    
    
    public abstract PatchDeployments.OneTimeScheduleOrBuilder getOneTimeScheduleOrBuilder()

Required. Schedule a one-time execution.

` .google.cloud.osconfig.v1.OneTimeSchedule one_time_schedule = 6 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[PatchDeployments.OneTimeScheduleOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.OneTimeScheduleOrBuilder)` |   
  
### getPatchConfig()
    
    
    public abstract PatchJobs.PatchConfig getPatchConfig()

Optional. Patch configuration that is applied.

` .google.cloud.osconfig.v1.PatchConfig patch_config = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchConfig)` | The patchConfig.  
  
### getPatchConfigOrBuilder()
    
    
    public abstract PatchJobs.PatchConfigOrBuilder getPatchConfigOrBuilder()

Optional. Patch configuration that is applied.

` .google.cloud.osconfig.v1.PatchConfig patch_config = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchConfigOrBuilder)` |   
  
### getRecurringSchedule()
    
    
    public abstract PatchDeployments.RecurringSchedule getRecurringSchedule()

Required. Schedule recurring executions.

` .google.cloud.osconfig.v1.RecurringSchedule recurring_schedule = 7 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[PatchDeployments.RecurringSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.RecurringSchedule)` | The recurringSchedule.  
  
### getRecurringScheduleOrBuilder()
    
    
    public abstract PatchDeployments.RecurringScheduleOrBuilder getRecurringScheduleOrBuilder()

Required. Schedule recurring executions.

` .google.cloud.osconfig.v1.RecurringSchedule recurring_schedule = 7 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[PatchDeployments.RecurringScheduleOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.RecurringScheduleOrBuilder)` |   
  
### getRollout()
    
    
    public abstract PatchJobs.PatchRollout getRollout()

Optional. Rollout strategy of the patch job.

` .google.cloud.osconfig.v1.PatchRollout rollout = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchRollout](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchRollout)` | The rollout.  
  
### getRolloutOrBuilder()
    
    
    public abstract PatchJobs.PatchRolloutOrBuilder getRolloutOrBuilder()

Optional. Rollout strategy of the patch job.

` .google.cloud.osconfig.v1.PatchRollout rollout = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchRolloutOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchRolloutOrBuilder)` |   
  
### getScheduleCase()
    
    
    public abstract PatchDeployments.PatchDeployment.ScheduleCase getScheduleCase()

**Returns**  
---  
**Type** | **Description**  
`[PatchDeployments.PatchDeployment.ScheduleCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PatchDeployment.ScheduleCase)` |   
  
### getState()
    
    
    public abstract PatchDeployments.PatchDeployment.State getState()

Output only. Current state of the patch deployment.

` .google.cloud.osconfig.v1.PatchDeployment.State state = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[PatchDeployments.PatchDeployment.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PatchDeployment.State)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. Current state of the patch deployment.

` .google.cloud.osconfig.v1.PatchDeployment.State state = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. Time the patch deployment was last updated. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.

` .google.protobuf.Timestamp update_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. Time the patch deployment was last updated. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.

` .google.protobuf.Timestamp update_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. Time the patch deployment was created. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.

` .google.protobuf.Timestamp create_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasDuration()
    
    
    public abstract boolean hasDuration()

Optional. Duration of the patch. After the duration ends, the patch times out.

`.google.protobuf.Duration duration = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the duration field is set.  
  
### hasInstanceFilter()
    
    
    public abstract boolean hasInstanceFilter()

Required. VM instances to patch.

` .google.cloud.osconfig.v1.PatchInstanceFilter instance_filter = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the instanceFilter field is set.  
  
### hasLastExecuteTime()
    
    
    public abstract boolean hasLastExecuteTime()

Output only. The last time a patch job was started by this deployment. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.

` .google.protobuf.Timestamp last_execute_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the lastExecuteTime field is set.  
  
### hasOneTimeSchedule()
    
    
    public abstract boolean hasOneTimeSchedule()

Required. Schedule a one-time execution.

` .google.cloud.osconfig.v1.OneTimeSchedule one_time_schedule = 6 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the oneTimeSchedule field is set.  
  
### hasPatchConfig()
    
    
    public abstract boolean hasPatchConfig()

Optional. Patch configuration that is applied.

` .google.cloud.osconfig.v1.PatchConfig patch_config = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the patchConfig field is set.  
  
### hasRecurringSchedule()
    
    
    public abstract boolean hasRecurringSchedule()

Required. Schedule recurring executions.

` .google.cloud.osconfig.v1.RecurringSchedule recurring_schedule = 7 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the recurringSchedule field is set.  
  
### hasRollout()
    
    
    public abstract boolean hasRollout()

Optional. Rollout strategy of the patch job.

` .google.cloud.osconfig.v1.PatchRollout rollout = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rollout field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. Time the patch deployment was last updated. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.

` .google.protobuf.Timestamp update_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
