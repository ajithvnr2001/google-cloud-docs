---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WorkspaceOrBuilder
title: Interface WorkspaceOrBuilder (0.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:25.676689+00:00
---

# Interface WorkspaceOrBuilder (0.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.WorkspaceOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface WorkspaceOrBuilder (0.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.98.0 (latest)  0.94.0  0.93.0  0.92.0  0.90.0  0.87.0  0.86.0  0.84.0  0.82.0  0.81.0  0.80.0  0.79.0  0.77.0  0.75.0  0.74.0  0.73.0  0.72.0  0.71.0  0.69.0  0.67.0  0.66.0  0.63.0  0.62.0  0.61.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.4 
    
    
    public interface WorkspaceOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. The timestamp of when the workspace was created.

`.google.protobuf.Timestamp create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The timestamp of when the workspace was created.

`.google.protobuf.Timestamp create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDataEncryptionState()
    
    
    public abstract DataEncryptionState getDataEncryptionState()

Output only. A data encryption state of a Git repository if this Workspace is protected by a KMS key.

` .google.cloud.dataform.v1beta1.DataEncryptionState data_encryption_state = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DataEncryptionState](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataEncryptionState)` | The dataEncryptionState.  
  
### getDataEncryptionStateOrBuilder()
    
    
    public abstract DataEncryptionStateOrBuilder getDataEncryptionStateOrBuilder()

Output only. A data encryption state of a Git repository if this Workspace is protected by a KMS key.

` .google.cloud.dataform.v1beta1.DataEncryptionState data_encryption_state = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DataEncryptionStateOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataEncryptionStateOrBuilder)` |   
  
### getDepth()
    
    
    public abstract int getDepth()

Optional. Input only. Immutable. The maximum depth of the Git repository to checkout for this workspace. If defined and greater than 0, the Git repository will be created as a shallow clone with the given depth, otherwise a full clone will be performed. This field is available only for GitHub, Gitlab and 1p repositories with enabled branch management.

` int32 depth = 10 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The depth.  
  
### getDisableMoves()
    
    
    public abstract boolean getDisableMoves()

Optional. If set to true, workspaces will not be moved if its linked Repository is moved. Instead, it will be deleted.

`optional bool disable_moves = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The disableMoves.  
  
### getEnableBranchManagement()
    
    
    public abstract boolean getEnableBranchManagement()

Immutable. Controls the enablement of branch checkout for the workspace.

When set to True, the workspace will be allowed to checkout branches.

`optional bool enable_branch_management = 9 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableBranchManagement.  
  
### getInternalMetadata()
    
    
    public abstract String getInternalMetadata()

Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.

`optional string internal_metadata = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The internalMetadata.  
  
### getInternalMetadataBytes()
    
    
    public abstract ByteString getInternalMetadataBytes()

Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.

`optional string internal_metadata = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for internalMetadata.  
  
### getName()
    
    
    public abstract String getName()

Identifier. The workspace's name.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The workspace's name.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getOriginalBranch()
    
    
    public abstract String getOriginalBranch()

Optional. Input only. Immutable. The name of the default upstream branch for all pull/push operations in the remote repository for this workspace. If empty, the HEAD branch from repository will be used.

` optional string original_branch = 7 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The originalBranch.  
  
### getOriginalBranchBytes()
    
    
    public abstract ByteString getOriginalBranchBytes()

Optional. Input only. Immutable. The name of the default upstream branch for all pull/push operations in the remote repository for this workspace. If empty, the HEAD branch from repository will be used.

` optional string original_branch = 7 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for originalBranch.  
  
### getPrivateResourceMetadata()
    
    
    public abstract PrivateResourceMetadata getPrivateResourceMetadata()

Output only. Metadata indicating whether this resource is user-scoped. For `Workspace` resources, the `user_scoped` field is always `true`.

` .google.cloud.dataform.v1beta1.PrivateResourceMetadata private_resource_metadata = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[PrivateResourceMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.PrivateResourceMetadata)` | The privateResourceMetadata.  
  
### getPrivateResourceMetadataOrBuilder()
    
    
    public abstract PrivateResourceMetadataOrBuilder getPrivateResourceMetadataOrBuilder()

Output only. Metadata indicating whether this resource is user-scoped. For `Workspace` resources, the `user_scoped` field is always `true`.

` .google.cloud.dataform.v1beta1.PrivateResourceMetadata private_resource_metadata = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[PrivateResourceMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.PrivateResourceMetadataOrBuilder)` |   
  
### getShallow()
    
    
    public abstract boolean getShallow()

Output only. If set to true, the workspace was created as a shallow clone. Will be set to true if the depth field is set to a value greater than 0, otherwise it will be set to false.

`optional bool shallow = 11 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The shallow.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. The timestamp of when the workspace was created.

`.google.protobuf.Timestamp create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasDataEncryptionState()
    
    
    public abstract boolean hasDataEncryptionState()

Output only. A data encryption state of a Git repository if this Workspace is protected by a KMS key.

` .google.cloud.dataform.v1beta1.DataEncryptionState data_encryption_state = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the dataEncryptionState field is set.  
  
### hasDisableMoves()
    
    
    public abstract boolean hasDisableMoves()

Optional. If set to true, workspaces will not be moved if its linked Repository is moved. Instead, it will be deleted.

`optional bool disable_moves = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the disableMoves field is set.  
  
### hasEnableBranchManagement()
    
    
    public abstract boolean hasEnableBranchManagement()

Immutable. Controls the enablement of branch checkout for the workspace.

When set to True, the workspace will be allowed to checkout branches.

`optional bool enable_branch_management = 9 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the enableBranchManagement field is set.  
  
### hasInternalMetadata()
    
    
    public abstract boolean hasInternalMetadata()

Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.

`optional string internal_metadata = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the internalMetadata field is set.  
  
### hasOriginalBranch()
    
    
    public abstract boolean hasOriginalBranch()

Optional. Input only. Immutable. The name of the default upstream branch for all pull/push operations in the remote repository for this workspace. If empty, the HEAD branch from repository will be used.

` optional string original_branch = 7 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the originalBranch field is set.  
  
### hasPrivateResourceMetadata()
    
    
    public abstract boolean hasPrivateResourceMetadata()

Output only. Metadata indicating whether this resource is user-scoped. For `Workspace` resources, the `user_scoped` field is always `true`.

` .google.cloud.dataform.v1beta1.PrivateResourceMetadata private_resource_metadata = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the privateResourceMetadata field is set.  
  
### hasShallow()
    
    
    public abstract boolean hasShallow()

Output only. If set to true, the workspace was created as a shallow clone. Will be set to true if the depth field is set to a value greater than 0, otherwise it will be set to false.

`optional bool shallow = 11 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the shallow field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
