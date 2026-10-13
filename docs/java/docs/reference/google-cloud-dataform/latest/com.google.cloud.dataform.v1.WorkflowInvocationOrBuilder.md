---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WorkflowInvocationOrBuilder
title: Interface WorkflowInvocationOrBuilder (0.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:32:26.535786+00:00
---

# Interface WorkflowInvocationOrBuilder (0.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WorkflowInvocationOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface WorkflowInvocationOrBuilder (0.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.98.0 (latest)  0.94.0  0.93.0  0.92.0  0.90.0  0.87.0  0.86.0  0.84.0  0.82.0  0.81.0  0.80.0  0.79.0  0.77.0  0.75.0  0.74.0  0.73.0  0.72.0  0.71.0  0.69.0  0.67.0  0.66.0  0.63.0  0.62.0  0.61.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.4 
    
    
    public interface WorkflowInvocationOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCompilationResult()
    
    
    public abstract String getCompilationResult()

Immutable. The name of the compilation result to use for this invocation. Must be in the format `projects/*/locations/*/repositories/*/compilationResults/*`.

` string compilation_result = 2 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The compilationResult.  
  
### getCompilationResultBytes()
    
    
    public abstract ByteString getCompilationResultBytes()

Immutable. The name of the compilation result to use for this invocation. Must be in the format `projects/*/locations/*/repositories/*/compilationResults/*`.

` string compilation_result = 2 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for compilationResult.  
  
### getCompilationSourceCase()
    
    
    public abstract WorkflowInvocation.CompilationSourceCase getCompilationSourceCase()

**Returns**  
---  
**Type** | **Description**  
`[WorkflowInvocation.CompilationSourceCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WorkflowInvocation.CompilationSourceCase)` |   
  
### getDataEncryptionState()
    
    
    public abstract DataEncryptionState getDataEncryptionState()

Output only. Only set if the repository has a KMS Key.

` .google.cloud.dataform.v1.DataEncryptionState data_encryption_state = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DataEncryptionState](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataEncryptionState)` | The dataEncryptionState.  
  
### getDataEncryptionStateOrBuilder()
    
    
    public abstract DataEncryptionStateOrBuilder getDataEncryptionStateOrBuilder()

Output only. Only set if the repository has a KMS Key.

` .google.cloud.dataform.v1.DataEncryptionState data_encryption_state = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DataEncryptionStateOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataEncryptionStateOrBuilder)` |   
  
### getInternalMetadata()
    
    
    public abstract String getInternalMetadata()

Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.

`optional string internal_metadata = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The internalMetadata.  
  
### getInternalMetadataBytes()
    
    
    public abstract ByteString getInternalMetadataBytes()

Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.

`optional string internal_metadata = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for internalMetadata.  
  
### getInvocationConfig()
    
    
    public abstract InvocationConfig getInvocationConfig()

Immutable. If left unset, a default InvocationConfig will be used.

` .google.cloud.dataform.v1.InvocationConfig invocation_config = 3 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[InvocationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.InvocationConfig)` | The invocationConfig.  
  
### getInvocationConfigOrBuilder()
    
    
    public abstract InvocationConfigOrBuilder getInvocationConfigOrBuilder()

Immutable. If left unset, a default InvocationConfig will be used.

` .google.cloud.dataform.v1.InvocationConfig invocation_config = 3 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[InvocationConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.InvocationConfigOrBuilder)` |   
  
### getInvocationTiming()
    
    
    public abstract Interval getInvocationTiming()

Output only. This workflow invocation's timing details.

`.google.type.Interval invocation_timing = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`com.google.type.Interval` | The invocationTiming.  
  
### getInvocationTimingOrBuilder()
    
    
    public abstract IntervalOrBuilder getInvocationTimingOrBuilder()

Output only. This workflow invocation's timing details.

`.google.type.Interval invocation_timing = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`com.google.type.IntervalOrBuilder` |   
  
### getName()
    
    
    public abstract String getName()

Output only. The workflow invocation's name.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Output only. The workflow invocation's name.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPipelineConfig()
    
    
    public abstract PipelineConfig getPipelineConfig()

Output only. The pipeline options which defines the pipeline type and path within the Git repository.

` .google.cloud.dataform.v1.PipelineConfig pipeline_config = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[PipelineConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.PipelineConfig)` | The pipelineConfig.  
  
### getPipelineConfigOrBuilder()
    
    
    public abstract PipelineConfigOrBuilder getPipelineConfigOrBuilder()

Output only. The pipeline options which defines the pipeline type and path within the Git repository.

` .google.cloud.dataform.v1.PipelineConfig pipeline_config = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[PipelineConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.PipelineConfigOrBuilder)` |   
  
### getPrivateResourceMetadata()
    
    
    public abstract PrivateResourceMetadata getPrivateResourceMetadata()

Output only. Metadata indicating whether this resource is user-scoped. `WorkflowInvocation` resource is `user_scoped` only if it is sourced from a compilation result and the compilation result is user-scoped.

` .google.cloud.dataform.v1.PrivateResourceMetadata private_resource_metadata = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[PrivateResourceMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.PrivateResourceMetadata)` | The privateResourceMetadata.  
  
### getPrivateResourceMetadataOrBuilder()
    
    
    public abstract PrivateResourceMetadataOrBuilder getPrivateResourceMetadataOrBuilder()

Output only. Metadata indicating whether this resource is user-scoped. `WorkflowInvocation` resource is `user_scoped` only if it is sourced from a compilation result and the compilation result is user-scoped.

` .google.cloud.dataform.v1.PrivateResourceMetadata private_resource_metadata = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[PrivateResourceMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.PrivateResourceMetadataOrBuilder)` |   
  
### getResolvedCompilationResult()
    
    
    public abstract String getResolvedCompilationResult()

Output only. The resolved compilation result that was used to create this invocation. Will be in the format `projects/*/locations/*/repositories/*/compilationResults/*`.

` string resolved_compilation_result = 7 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The resolvedCompilationResult.  
  
### getResolvedCompilationResultBytes()
    
    
    public abstract ByteString getResolvedCompilationResultBytes()

Output only. The resolved compilation result that was used to create this invocation. Will be in the format `projects/*/locations/*/repositories/*/compilationResults/*`.

` string resolved_compilation_result = 7 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for resolvedCompilationResult.  
  
### getState()
    
    
    public abstract WorkflowInvocation.State getState()

Output only. This workflow invocation's current state.

` .google.cloud.dataform.v1.WorkflowInvocation.State state = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[WorkflowInvocation.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WorkflowInvocation.State)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. This workflow invocation's current state.

` .google.cloud.dataform.v1.WorkflowInvocation.State state = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getWorkflowConfig()
    
    
    public abstract String getWorkflowConfig()

Immutable. The name of the workflow config to invoke. Must be in the format `projects/*/locations/*/repositories/*/workflowConfigs/*`.

` string workflow_config = 6 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The workflowConfig.  
  
### getWorkflowConfigBytes()
    
    
    public abstract ByteString getWorkflowConfigBytes()

Immutable. The name of the workflow config to invoke. Must be in the format `projects/*/locations/*/repositories/*/workflowConfigs/*`.

` string workflow_config = 6 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for workflowConfig.  
  
### hasCompilationResult()
    
    
    public abstract boolean hasCompilationResult()

Immutable. The name of the compilation result to use for this invocation. Must be in the format `projects/*/locations/*/repositories/*/compilationResults/*`.

` string compilation_result = 2 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the compilationResult field is set.  
  
### hasDataEncryptionState()
    
    
    public abstract boolean hasDataEncryptionState()

Output only. Only set if the repository has a KMS Key.

` .google.cloud.dataform.v1.DataEncryptionState data_encryption_state = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the dataEncryptionState field is set.  
  
### hasInternalMetadata()
    
    
    public abstract boolean hasInternalMetadata()

Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.

`optional string internal_metadata = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the internalMetadata field is set.  
  
### hasInvocationConfig()
    
    
    public abstract boolean hasInvocationConfig()

Immutable. If left unset, a default InvocationConfig will be used.

` .google.cloud.dataform.v1.InvocationConfig invocation_config = 3 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the invocationConfig field is set.  
  
### hasInvocationTiming()
    
    
    public abstract boolean hasInvocationTiming()

Output only. This workflow invocation's timing details.

`.google.type.Interval invocation_timing = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the invocationTiming field is set.  
  
### hasPipelineConfig()
    
    
    public abstract boolean hasPipelineConfig()

Output only. The pipeline options which defines the pipeline type and path within the Git repository.

` .google.cloud.dataform.v1.PipelineConfig pipeline_config = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pipelineConfig field is set.  
  
### hasPrivateResourceMetadata()
    
    
    public abstract boolean hasPrivateResourceMetadata()

Output only. Metadata indicating whether this resource is user-scoped. `WorkflowInvocation` resource is `user_scoped` only if it is sourced from a compilation result and the compilation result is user-scoped.

` .google.cloud.dataform.v1.PrivateResourceMetadata private_resource_metadata = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the privateResourceMetadata field is set.  
  
### hasWorkflowConfig()
    
    
    public abstract boolean hasWorkflowConfig()

Immutable. The name of the workflow config to invoke. Must be in the format `projects/*/locations/*/repositories/*/workflowConfigs/*`.

` string workflow_config = 6 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the workflowConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
