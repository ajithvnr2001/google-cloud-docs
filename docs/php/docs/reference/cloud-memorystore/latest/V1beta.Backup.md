---
url: https://docs.cloud.google.com/php/docs/reference/cloud-memorystore/latest/V1beta.Backup
title: Google Cloud Memorystore V1beta Client - Class Backup (0.13.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:03:47.355143+00:00
---

# Google Cloud Memorystore V1beta Client - Class Backup (0.13.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-memorystore/latest/V1beta.Backup

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Memorystore V1beta Client - Class Backup (0.13.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.3 (latest)  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.2  0.5.1  0.4.2  0.3.0  0.2.0  0.1.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Memorystore V1beta Client class Backup.

Backup of an instance.

Generated from protobuf message `google.cloud.memorystore.v1beta.Backup`

## Namespace

Google \ Cloud \ Memorystore \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
Identifier. Full resource path of the backup. the last part of the name is the backup id with the following format: [YYYYMMDDHHMMSS]_[Shorted Instance UID] OR customer specified while backup instance. Example: 20240515123000_1234  
`↳ create_time` |  `Google\Protobuf\Timestamp`   
Output only. The time when the backup was created.  
`↳ instance` |  `string`   
Output only. Instance resource path of this backup.  
`↳ instance_uid` |  `string`   
Output only. Instance uid of this backup.  
`↳ total_size_bytes` |  `int|string`   
Output only. Total size of the backup in bytes.  
`↳ expire_time` |  `Google\Protobuf\Timestamp`   
Output only. The time when the backup will expire.  
`↳ engine_version` |  `string`   
Output only. valkey-7.5/valkey-8.0, etc.  
`↳ backup_files` |  `array<[BackupFile](https://docs.cloud.google.com/php/docs/reference/cloud-memorystore/latest/V1beta.BackupFile)>`   
Output only. List of backup files of the backup.  
`↳ node_type` |  `int`   
Output only. Node type of the instance.  
`↳ replica_count` |  `int`   
Output only. Number of replicas for the instance.  
`↳ shard_count` |  `int`   
Output only. Number of shards for the instance.  
`↳ backup_type` |  `int`   
Output only. Type of the backup.  
`↳ state` |  `int`   
Output only. State of the backup.  
`↳ encryption_info` |  `[EncryptionInfo](https://docs.cloud.google.com/php/docs/reference/cloud-memorystore/latest/V1beta.EncryptionInfo)`   
Output only. Encryption information of the backup.  
`↳ uid` |  `string`   
Output only. System assigned unique identifier of the backup.  
  
### getName

Identifier. Full resource path of the backup. the last part of the name is the backup id with the following format: [YYYYMMDDHHMMSS]_[Shorted Instance UID] OR customer specified while backup instance. Example: 20240515123000_1234

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Identifier. Full resource path of the backup. the last part of the name is the backup id with the following format: [YYYYMMDDHHMMSS]_[Shorted Instance UID] OR customer specified while backup instance. Example: 20240515123000_1234

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreateTime

Output only. The time when the backup was created.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasCreateTime

### clearCreateTime

### setCreateTime

Output only. The time when the backup was created.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getInstance

Output only. Instance resource path of this backup.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setInstance

Output only. Instance resource path of this backup.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getInstanceUid

Output only. Instance uid of this backup.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setInstanceUid

Output only. Instance uid of this backup.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTotalSizeBytes

Output only. Total size of the backup in bytes.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### setTotalSizeBytes

Output only. Total size of the backup in bytes.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getExpireTime

Output only. The time when the backup will expire.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasExpireTime

### clearExpireTime

### setExpireTime

Output only. The time when the backup will expire.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEngineVersion

Output only. valkey-7.5/valkey-8.0, etc.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setEngineVersion

Output only. valkey-7.5/valkey-8.0, etc.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBackupFiles

Output only. List of backup files of the backup.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[BackupFile](https://docs.cloud.google.com/php/docs/reference/cloud-memorystore/latest/V1beta.BackupFile)>` |   
  
### setBackupFiles

Output only. List of backup files of the backup.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[BackupFile](https://docs.cloud.google.com/php/docs/reference/cloud-memorystore/latest/V1beta.BackupFile)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getNodeType

Output only. Node type of the instance.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [NodeType](https://docs.cloud.google.com/php/docs/reference/cloud-memorystore/latest/V1beta.Instance.NodeType).  
  
### setNodeType

Output only. Node type of the instance.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [NodeType](https://docs.cloud.google.com/php/docs/reference/cloud-memorystore/latest/V1beta.Instance.NodeType).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getReplicaCount

Output only. Number of replicas for the instance.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setReplicaCount

Output only. Number of replicas for the instance.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getShardCount

Output only. Number of shards for the instance.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setShardCount

Output only. Number of shards for the instance.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBackupType

Output only. Type of the backup.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [BackupType](https://docs.cloud.google.com/php/docs/reference/cloud-memorystore/latest/V1beta.Backup.BackupType).  
  
### setBackupType

Output only. Type of the backup.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [BackupType](https://docs.cloud.google.com/php/docs/reference/cloud-memorystore/latest/V1beta.Backup.BackupType).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getState

Output only. State of the backup.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-memorystore/latest/V1beta.Backup.State).  
  
### setState

Output only. State of the backup.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-memorystore/latest/V1beta.Backup.State).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEncryptionInfo

Output only. Encryption information of the backup.

**Returns**  
---  
**Type** | **Description**  
`[EncryptionInfo](https://docs.cloud.google.com/php/docs/reference/cloud-memorystore/latest/V1beta.EncryptionInfo)|null` |   
  
### hasEncryptionInfo

### clearEncryptionInfo

### setEncryptionInfo

Output only. Encryption information of the backup.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[EncryptionInfo](https://docs.cloud.google.com/php/docs/reference/cloud-memorystore/latest/V1beta.EncryptionInfo)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUid

Output only. System assigned unique identifier of the backup.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setUid

Output only. System assigned unique identifier of the backup.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
