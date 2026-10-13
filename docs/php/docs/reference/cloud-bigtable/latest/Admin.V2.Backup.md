---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Backup
title: Cloud Bigtable V2 Client - Class Backup (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:34.444695+00:00
---

# Cloud Bigtable V2 Client - Class Backup (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Backup

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class Backup (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class Backup.

A backup of a Cloud Bigtable table.

Generated from protobuf message `google.bigtable.admin.v2.Backup`

## Namespace

Google \ Cloud \ Bigtable \ Admin \ V2

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
A globally unique identifier for the backup which cannot be changed. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}/ backups/[_a-zA-Z0-9][-_.a-zA-Z0-9]*` The final segment of the name must be between 1 and 50 characters in length. The backup is stored in the cluster identified by the prefix of the backup name of the form `projects/{project}/instances/{instance}/clusters/{cluster}`.  
`↳ source_table` |  `string`   
Required. Immutable. Name of the table from which this backup was created. This needs to be in the same instance as the backup. Values are of the form `projects/{project}/instances/{instance}/tables/{source_table}`.  
`↳ source_backup` |  `string`   
Output only. Name of the backup from which this backup was copied. If a backup is not created by copying a backup, this field will be empty. Values are of the form: projects/  
`↳ expire_time` |  `Google\Protobuf\Timestamp`   
Required. The expiration time of the backup. When creating a backup or updating its `expire_time`, the value must be greater than the backup creation time by: - At least 6 hours - At most 90 days Once the `expire_time` has passed, Cloud Bigtable will delete the backup.  
`↳ start_time` |  `Google\Protobuf\Timestamp`   
Output only. `start_time` is the time that the backup was started (i.e. approximately the time the [CreateBackup](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__createBackup__) request is received). The row data in this backup will be no older than this timestamp.  
`↳ end_time` |  `Google\Protobuf\Timestamp`   
Output only. `end_time` is the time that the backup was finished. The row data in the backup will be no newer than this timestamp.  
`↳ size_bytes` |  `int|string`   
Output only. Size of the backup in bytes.  
`↳ state` |  `int`   
Output only. The current state of the backup.  
`↳ encryption_info` |  `[EncryptionInfo](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.EncryptionInfo)`   
Output only. The encryption information for the backup.  
`↳ backup_type` |  `int`   
Indicates the backup type of the backup.  
`↳ hot_to_standard_time` |  `Google\Protobuf\Timestamp`   
The time at which the hot backup will be converted to a standard backup. Once the `hot_to_standard_time` has passed, Cloud Bigtable will convert the hot backup to a standard backup. This value must be greater than the backup creation time by: - At least 24 hours This field only applies for hot backups. When creating or updating a standard backup, attempting to set this field will fail the request.  
  
### getName

A globally unique identifier for the backup which cannot be changed. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}/ backups/[_a-zA-Z0-9][-_.a-zA-Z0-9]*` The final segment of the name must be between 1 and 50 characters in length.

The backup is stored in the cluster identified by the prefix of the backup name of the form `projects/{project}/instances/{instance}/clusters/{cluster}`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

A globally unique identifier for the backup which cannot be changed. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}/ backups/[_a-zA-Z0-9][-_.a-zA-Z0-9]*` The final segment of the name must be between 1 and 50 characters in length.

The backup is stored in the cluster identified by the prefix of the backup name of the form `projects/{project}/instances/{instance}/clusters/{cluster}`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSourceTable

Required. Immutable. Name of the table from which this backup was created.

This needs to be in the same instance as the backup. Values are of the form `projects/{project}/instances/{instance}/tables/{source_table}`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setSourceTable

Required. Immutable. Name of the table from which this backup was created.

This needs to be in the same instance as the backup. Values are of the form `projects/{project}/instances/{instance}/tables/{source_table}`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSourceBackup

Output only. Name of the backup from which this backup was copied. If a backup is not created by copying a backup, this field will be empty. Values are of the form: projects/

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setSourceBackup

Output only. Name of the backup from which this backup was copied. If a backup is not created by copying a backup, this field will be empty. Values are of the form: projects/

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getExpireTime

Required. The expiration time of the backup.

When creating a backup or updating its `expire_time`, the value must be greater than the backup creation time by:

  * At least 6 hours
  * At most 90 days Once the `expire_time` has passed, Cloud Bigtable will delete the backup.



**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasExpireTime

### clearExpireTime

### setExpireTime

Required. The expiration time of the backup.

When creating a backup or updating its `expire_time`, the value must be greater than the backup creation time by:

  * At least 6 hours
  * At most 90 days Once the `expire_time` has passed, Cloud Bigtable will delete the backup.



**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStartTime

Output only. `start_time` is the time that the backup was started (i.e. approximately the time the [CreateBackup](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__createBackup__) request is received). The row data in this backup will be no older than this timestamp.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasStartTime

### clearStartTime

### setStartTime

Output only. `start_time` is the time that the backup was started (i.e. approximately the time the [CreateBackup](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__createBackup__) request is received). The row data in this backup will be no older than this timestamp.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEndTime

Output only. `end_time` is the time that the backup was finished. The row data in the backup will be no newer than this timestamp.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasEndTime

### clearEndTime

### setEndTime

Output only. `end_time` is the time that the backup was finished. The row data in the backup will be no newer than this timestamp.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSizeBytes

Output only. Size of the backup in bytes.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### setSizeBytes

Output only. Size of the backup in bytes.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getState

Output only. The current state of the backup.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Backup.State).  
  
### setState

Output only. The current state of the backup.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Backup.State).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEncryptionInfo

Output only. The encryption information for the backup.

**Returns**  
---  
**Type** | **Description**  
`[EncryptionInfo](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.EncryptionInfo)|null` |   
  
### hasEncryptionInfo

### clearEncryptionInfo

### setEncryptionInfo

Output only. The encryption information for the backup.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[EncryptionInfo](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.EncryptionInfo)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBackupType

Indicates the backup type of the backup.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [BackupType](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Backup.BackupType).  
  
### setBackupType

Indicates the backup type of the backup.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [BackupType](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Backup.BackupType).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getHotToStandardTime

The time at which the hot backup will be converted to a standard backup.

Once the `hot_to_standard_time` has passed, Cloud Bigtable will convert the hot backup to a standard backup. This value must be greater than the backup creation time by:

  * At least 24 hours This field only applies for hot backups. When creating or updating a standard backup, attempting to set this field will fail the request.



**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasHotToStandardTime

### clearHotToStandardTime

### setHotToStandardTime

The time at which the hot backup will be converted to a standard backup.

Once the `hot_to_standard_time` has passed, Cloud Bigtable will convert the hot backup to a standard backup. This value must be greater than the backup creation time by:

  * At least 24 hours This field only applies for hot backups. When creating or updating a standard backup, attempting to set this field will fail the request.



**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
