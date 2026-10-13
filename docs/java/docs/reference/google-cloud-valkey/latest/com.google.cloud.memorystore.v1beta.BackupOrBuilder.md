---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1beta.BackupOrBuilder
title: Interface BackupOrBuilder (0.45.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:58:57.079792+00:00
---

# Interface BackupOrBuilder (0.45.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1beta.BackupOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BackupOrBuilder (0.45.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.45.0 (latest)  0.41.0  0.40.0  0.39.0  0.37.0  0.34.0  0.33.0  0.31.0  0.29.0  0.28.0  0.26.0  0.24.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.14.0  0.13.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface BackupOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBackupFiles(int index)
    
    
    public abstract BackupFile getBackupFiles(int index)

Output only. List of backup files of the backup.

` repeated .google.cloud.memorystore.v1beta.BackupFile backup_files = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupFile](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1beta.BackupFile)` |   
  
### getBackupFilesCount()
    
    
    public abstract int getBackupFilesCount()

Output only. List of backup files of the backup.

` repeated .google.cloud.memorystore.v1beta.BackupFile backup_files = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getBackupFilesList()
    
    
    public abstract List<BackupFile> getBackupFilesList()

Output only. List of backup files of the backup.

` repeated .google.cloud.memorystore.v1beta.BackupFile backup_files = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[BackupFile](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1beta.BackupFile)>` |   
  
### getBackupFilesOrBuilder(int index)
    
    
    public abstract BackupFileOrBuilder getBackupFilesOrBuilder(int index)

Output only. List of backup files of the backup.

` repeated .google.cloud.memorystore.v1beta.BackupFile backup_files = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupFileOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1beta.BackupFileOrBuilder)` |   
  
### getBackupFilesOrBuilderList()
    
    
    public abstract List<? extends BackupFileOrBuilder> getBackupFilesOrBuilderList()

Output only. List of backup files of the backup.

` repeated .google.cloud.memorystore.v1beta.BackupFile backup_files = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.memorystore.v1beta.BackupFileOrBuilder>` |   
  
### getBackupType()
    
    
    public abstract Backup.BackupType getBackupType()

Output only. Type of the backup.

` .google.cloud.memorystore.v1beta.Backup.BackupType backup_type = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Backup.BackupType](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1beta.Backup.BackupType)` | The backupType.  
  
### getBackupTypeValue()
    
    
    public abstract int getBackupTypeValue()

Output only. Type of the backup.

` .google.cloud.memorystore.v1beta.Backup.BackupType backup_type = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for backupType.  
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. The time when the backup was created.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The time when the backup was created.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getEncryptionInfo()
    
    
    public abstract EncryptionInfo getEncryptionInfo()

Output only. Encryption information of the backup.

` .google.cloud.memorystore.v1beta.EncryptionInfo encryption_info = 14 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[EncryptionInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1beta.EncryptionInfo)` | The encryptionInfo.  
  
### getEncryptionInfoOrBuilder()
    
    
    public abstract EncryptionInfoOrBuilder getEncryptionInfoOrBuilder()

Output only. Encryption information of the backup.

` .google.cloud.memorystore.v1beta.EncryptionInfo encryption_info = 14 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[EncryptionInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1beta.EncryptionInfoOrBuilder)` |   
  
### getEngineVersion()
    
    
    public abstract String getEngineVersion()

Output only. valkey-7.5/valkey-8.0, etc.

`string engine_version = 7 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The engineVersion.  
  
### getEngineVersionBytes()
    
    
    public abstract ByteString getEngineVersionBytes()

Output only. valkey-7.5/valkey-8.0, etc.

`string engine_version = 7 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for engineVersion.  
  
### getExpireTime()
    
    
    public abstract Timestamp getExpireTime()

Output only. The time when the backup will expire.

`.google.protobuf.Timestamp expire_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The expireTime.  
  
### getExpireTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getExpireTimeOrBuilder()

Output only. The time when the backup will expire.

`.google.protobuf.Timestamp expire_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getInstance()
    
    
    public abstract String getInstance()

Output only. Instance resource path of this backup.

` string instance = 3 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The instance.  
  
### getInstanceBytes()
    
    
    public abstract ByteString getInstanceBytes()

Output only. Instance resource path of this backup.

` string instance = 3 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for instance.  
  
### getInstanceUid()
    
    
    public abstract String getInstanceUid()

Output only. Instance uid of this backup.

` string instance_uid = 4 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The instanceUid.  
  
### getInstanceUidBytes()
    
    
    public abstract ByteString getInstanceUidBytes()

Output only. Instance uid of this backup.

` string instance_uid = 4 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for instanceUid.  
  
### getName()
    
    
    public abstract String getName()

Identifier. Full resource path of the backup. the last part of the name is the backup id with the following format: [YYYYMMDDHHMMSS]_[Shorted Instance UID] OR customer specified while backup instance. Example: 20240515123000_1234

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. Full resource path of the backup. the last part of the name is the backup id with the following format: [YYYYMMDDHHMMSS]_[Shorted Instance UID] OR customer specified while backup instance. Example: 20240515123000_1234

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getNodeType()
    
    
    public abstract Instance.NodeType getNodeType()

Output only. Node type of the instance.

` .google.cloud.memorystore.v1beta.Instance.NodeType node_type = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Instance.NodeType](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1beta.Instance.NodeType)` | The nodeType.  
  
### getNodeTypeValue()
    
    
    public abstract int getNodeTypeValue()

Output only. Node type of the instance.

` .google.cloud.memorystore.v1beta.Instance.NodeType node_type = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for nodeType.  
  
### getReplicaCount()
    
    
    public abstract int getReplicaCount()

Output only. Number of replicas for the instance.

`int32 replica_count = 10 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The replicaCount.  
  
### getShardCount()
    
    
    public abstract int getShardCount()

Output only. Number of shards for the instance.

`int32 shard_count = 11 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The shardCount.  
  
### getState()
    
    
    public abstract Backup.State getState()

Output only. State of the backup.

` .google.cloud.memorystore.v1beta.Backup.State state = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Backup.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1beta.Backup.State)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. State of the backup.

` .google.cloud.memorystore.v1beta.Backup.State state = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getTotalSizeBytes()
    
    
    public abstract long getTotalSizeBytes()

Output only. Total size of the backup in bytes.

`int64 total_size_bytes = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The totalSizeBytes.  
  
### getUid()
    
    
    public abstract String getUid()

Output only. System assigned unique identifier of the backup.

` string uid = 15 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The uid.  
  
### getUidBytes()
    
    
    public abstract ByteString getUidBytes()

Output only. System assigned unique identifier of the backup.

` string uid = 15 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for uid.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. The time when the backup was created.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasEncryptionInfo()
    
    
    public abstract boolean hasEncryptionInfo()

Output only. Encryption information of the backup.

` .google.cloud.memorystore.v1beta.EncryptionInfo encryption_info = 14 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the encryptionInfo field is set.  
  
### hasExpireTime()
    
    
    public abstract boolean hasExpireTime()

Output only. The time when the backup will expire.

`.google.protobuf.Timestamp expire_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the expireTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
