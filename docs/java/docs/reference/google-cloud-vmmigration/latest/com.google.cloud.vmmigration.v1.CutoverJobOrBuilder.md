---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.CutoverJobOrBuilder
title: Interface CutoverJobOrBuilder (1.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:35:00.908278+00:00
---

# Interface CutoverJobOrBuilder (1.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.CutoverJobOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CutoverJobOrBuilder (1.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.99.0 (latest)  1.95.0  1.94.0  1.93.0  1.91.0  1.88.0  1.87.0  1.85.0  1.83.0  1.82.0  1.80.0  1.78.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.70.0  1.68.0  1.67.0  1.64.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.5  1.2.0  1.1.1  1.0.5 
    
    
    public interface CutoverJobOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getComputeEngineDisksTargetDetails()
    
    
    public abstract ComputeEngineDisksTargetDetails getComputeEngineDisksTargetDetails()

Output only. Details of the target Persistent Disks in Compute Engine.

` .google.cloud.vmmigration.v1.ComputeEngineDisksTargetDetails compute_engine_disks_target_details = 20 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ComputeEngineDisksTargetDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ComputeEngineDisksTargetDetails)` | The computeEngineDisksTargetDetails.  
  
### getComputeEngineDisksTargetDetailsOrBuilder()
    
    
    public abstract ComputeEngineDisksTargetDetailsOrBuilder getComputeEngineDisksTargetDetailsOrBuilder()

Output only. Details of the target Persistent Disks in Compute Engine.

` .google.cloud.vmmigration.v1.ComputeEngineDisksTargetDetails compute_engine_disks_target_details = 20 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ComputeEngineDisksTargetDetailsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ComputeEngineDisksTargetDetailsOrBuilder)` |   
  
### getComputeEngineTargetDetails()
    
    
    public abstract ComputeEngineTargetDetails getComputeEngineTargetDetails()

Output only. Details of the target VM in Compute Engine.

` .google.cloud.vmmigration.v1.ComputeEngineTargetDetails compute_engine_target_details = 14 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ComputeEngineTargetDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ComputeEngineTargetDetails)` | The computeEngineTargetDetails.  
  
### getComputeEngineTargetDetailsOrBuilder()
    
    
    public abstract ComputeEngineTargetDetailsOrBuilder getComputeEngineTargetDetailsOrBuilder()

Output only. Details of the target VM in Compute Engine.

` .google.cloud.vmmigration.v1.ComputeEngineTargetDetails compute_engine_target_details = 14 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ComputeEngineTargetDetailsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ComputeEngineTargetDetailsOrBuilder)` |   
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. The time the cutover job was created (as an API call, not when it was actually created in the target).

`.google.protobuf.Timestamp create_time = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The time the cutover job was created (as an API call, not when it was actually created in the target).

`.google.protobuf.Timestamp create_time = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getEndTime()
    
    
    public abstract Timestamp getEndTime()

Output only. The time the cutover job had finished.

`.google.protobuf.Timestamp end_time = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The endTime.  
  
### getEndTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getEndTimeOrBuilder()

Output only. The time the cutover job had finished.

`.google.protobuf.Timestamp end_time = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getError()
    
    
    public abstract Status getError()

Output only. Provides details for the errors that led to the Cutover Job's state.

`.google.rpc.Status error = 9 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.Status` | The error.  
  
### getErrorOrBuilder()
    
    
    public abstract StatusOrBuilder getErrorOrBuilder()

Output only. Provides details for the errors that led to the Cutover Job's state.

`.google.rpc.Status error = 9 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.StatusOrBuilder` |   
  
### getName()
    
    
    public abstract String getName()

Output only. The name of the cutover job.

`string name = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Output only. The name of the cutover job.

`string name = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getProgressPercent()
    
    
    public abstract int getProgressPercent()

Output only. The current progress in percentage of the cutover job.

`int32 progress_percent = 13 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The progressPercent.  
  
### getState()
    
    
    public abstract CutoverJob.State getState()

Output only. State of the cutover job.

` .google.cloud.vmmigration.v1.CutoverJob.State state = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[CutoverJob.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.CutoverJob.State)` | The state.  
  
### getStateMessage()
    
    
    public abstract String getStateMessage()

Output only. A message providing possible extra details about the current state.

`string state_message = 10 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The stateMessage.  
  
### getStateMessageBytes()
    
    
    public abstract ByteString getStateMessageBytes()

Output only. A message providing possible extra details about the current state.

`string state_message = 10 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for stateMessage.  
  
### getStateTime()
    
    
    public abstract Timestamp getStateTime()

Output only. The time the state was last updated.

`.google.protobuf.Timestamp state_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The stateTime.  
  
### getStateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getStateTimeOrBuilder()

Output only. The time the state was last updated.

`.google.protobuf.Timestamp state_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. State of the cutover job.

` .google.cloud.vmmigration.v1.CutoverJob.State state = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getSteps(int index)
    
    
    public abstract CutoverStep getSteps(int index)

Output only. The cutover steps list representing its progress.

` repeated .google.cloud.vmmigration.v1.CutoverStep steps = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CutoverStep](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.CutoverStep)` |   
  
### getStepsCount()
    
    
    public abstract int getStepsCount()

Output only. The cutover steps list representing its progress.

` repeated .google.cloud.vmmigration.v1.CutoverStep steps = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getStepsList()
    
    
    public abstract List<CutoverStep> getStepsList()

Output only. The cutover steps list representing its progress.

` repeated .google.cloud.vmmigration.v1.CutoverStep steps = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CutoverStep](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.CutoverStep)>` |   
  
### getStepsOrBuilder(int index)
    
    
    public abstract CutoverStepOrBuilder getStepsOrBuilder(int index)

Output only. The cutover steps list representing its progress.

` repeated .google.cloud.vmmigration.v1.CutoverStep steps = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CutoverStepOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.CutoverStepOrBuilder)` |   
  
### getStepsOrBuilderList()
    
    
    public abstract List<? extends CutoverStepOrBuilder> getStepsOrBuilderList()

Output only. The cutover steps list representing its progress.

` repeated .google.cloud.vmmigration.v1.CutoverStep steps = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.vmmigration.v1.CutoverStepOrBuilder>` |   
  
### getTargetVmDetailsCase()
    
    
    public abstract CutoverJob.TargetVmDetailsCase getTargetVmDetailsCase()

**Returns**  
---  
**Type** | **Description**  
`[CutoverJob.TargetVmDetailsCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.CutoverJob.TargetVmDetailsCase)` |   
  
### hasComputeEngineDisksTargetDetails()
    
    
    public abstract boolean hasComputeEngineDisksTargetDetails()

Output only. Details of the target Persistent Disks in Compute Engine.

` .google.cloud.vmmigration.v1.ComputeEngineDisksTargetDetails compute_engine_disks_target_details = 20 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the computeEngineDisksTargetDetails field is set.  
  
### hasComputeEngineTargetDetails()
    
    
    public abstract boolean hasComputeEngineTargetDetails()

Output only. Details of the target VM in Compute Engine.

` .google.cloud.vmmigration.v1.ComputeEngineTargetDetails compute_engine_target_details = 14 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the computeEngineTargetDetails field is set.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. The time the cutover job was created (as an API call, not when it was actually created in the target).

`.google.protobuf.Timestamp create_time = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasEndTime()
    
    
    public abstract boolean hasEndTime()

Output only. The time the cutover job had finished.

`.google.protobuf.Timestamp end_time = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the endTime field is set.  
  
### hasError()
    
    
    public abstract boolean hasError()

Output only. Provides details for the errors that led to the Cutover Job's state.

`.google.rpc.Status error = 9 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the error field is set.  
  
### hasStateTime()
    
    
    public abstract boolean hasStateTime()

Output only. The time the state was last updated.

`.google.protobuf.Timestamp state_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the stateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
