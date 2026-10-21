---
url: https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.backupCollections.backups
title: REST Resource: projects.locations.backupCollections.backups \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:04:34.865378+00:00
---

# REST Resource: projects.locations.backupCollections.backups  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.backupCollections.backups

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/valkey/apis)



Send feedback 

#  REST Resource: projects.locations.backupCollections.backups Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Backup
    * JSON representation
  * BackupFile
    * JSON representation
  * BackupType
  * State
  * Methods



## Resource: Backup

Backup of an instance.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "instance": string,
      "instanceUid": string,
      "totalSizeBytes": string,
      "expireTime": string,
      "engineVersion": string,
      "backupFiles": [
        {
          object ([BackupFile](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.backupCollections.backups#BackupFile))
        }
      ],
      "nodeType": enum ([NodeType](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/NodeType)),
      "replicaCount": integer,
      "shardCount": integer,
      "backupType": enum ([BackupType](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.backupCollections.backups#BackupType)),
      "state": enum ([State](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.backupCollections.backups#State)),
      "encryptionInfo": {
        object ([EncryptionInfo](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/EncryptionInfo))
      },
      "uid": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. Full resource path of the backup. the last part of the name is the backup id with the following format: [YYYYMMDDHHMMSS]_[Shorted Instance UID] OR customer specified while backup instance. Example: 20240515123000_1234  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the backup was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`instance` |  `string` Output only. Instance resource path of this backup.  
`instanceUid` |  `string` Output only. Instance uid of this backup.  
`totalSizeBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Total size of the backup in bytes.  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the backup will expire.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`engineVersion` |  `string` Output only. valkey-7.5/valkey-8.0, etc.  
`backupFiles[]` |  `object (`[BackupFile](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.backupCollections.backups#BackupFile)`)` Output only. List of backup files of the backup.  
`nodeType` |  `enum (`[NodeType](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/NodeType)`)` Output only. Node type of the instance.  
`replicaCount` |  `integer` Output only. Number of replicas for the instance.  
`shardCount` |  `integer` Output only. Number of shards for the instance.  
`backupType` |  `enum (`[BackupType](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.backupCollections.backups#BackupType)`)` Output only. Type of the backup.  
`state` |  `enum (`[State](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.backupCollections.backups#State)`)` Output only. State of the backup.  
`encryptionInfo` |  `object (`[EncryptionInfo](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/EncryptionInfo)`)` Output only. Encryption information of the backup.  
`uid` |  `string` Output only. System assigned unique identifier of the backup.  
  
## BackupFile

Backup is consisted of multiple backup files.

JSON representation  
---  
      
    
    {
      "fileName": string,
      "sizeBytes": string,
      "createTime": string
    }  
  
Fields  
---  
`fileName` |  `string` Output only. e.g: .rdb  
`sizeBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Size of the backup file in bytes.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the backup file was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## BackupType

Type of the backup.

Enums  
---  
`BACKUP_TYPE_UNSPECIFIED` | The default value, not set.  
`ON_DEMAND` | On-demand backup.  
`AUTOMATED` | Automated backup.  
  
## State

State of the backup.

Enums  
---  
`STATE_UNSPECIFIED` | The default value, not set.  
`CREATING` | The backup is being created.  
`ACTIVE` | The backup is active to be used.  
`DELETING` | The backup is being deleted.  
`SUSPENDED` | The backup is currently suspended due to reasons like project deletion, billing account closure, etc.  
  
## Methods  
  
---  
  
### `[delete](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.backupCollections.backups/delete)`

|  Deletes a specific backup.  
  
### `[export](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.backupCollections.backups/export)`

|  Exports a specific backup to a customer target Cloud Storage URI.  
  
### `[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.backupCollections.backups/get)`

|  Gets the details of a specific backup.  
  
### `[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.backupCollections.backups/list)`

|  Lists all backups owned by a backup collection.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-22 UTC."],[],[]] 
