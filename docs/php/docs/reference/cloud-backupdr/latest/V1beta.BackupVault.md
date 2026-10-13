---
url: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupVault
title: Google Cloud Backup Dr V1beta Client - Class BackupVault (0.15.1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:19:08.104959+00:00
---

# Google Cloud Backup Dr V1beta Client - Class BackupVault (0.15.1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupVault

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Backup Dr V1beta Client - Class BackupVault (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.13.2  0.12.1  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.2  0.5.1  0.4.2  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Backup Dr V1beta Client class BackupVault.

Message describing a BackupVault object.

Generated from protobuf message `google.cloud.backupdr.v1beta.BackupVault`

## Namespace

Google \ Cloud \ BackupDR \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
Output only. Identifier. Name of the backup vault to create. It must have the format`"projects/{project}/locations/{location}/backupVaults/{backupvault}"`. `{backupvault}` cannot be changed after creation. It must be between 3-63 characters long and must be unique within the project and location.  
`↳ description` |  `string`   
Optional. The description of the BackupVault instance (2048 characters or less).  
`↳ labels` |  `array|Google\Protobuf\Internal\MapField`   
Optional. Resource labels to represent user provided metadata. No labels currently defined:  
`↳ create_time` |  `Google\Protobuf\Timestamp`   
Output only. The time when the instance was created.  
`↳ update_time` |  `Google\Protobuf\Timestamp`   
Output only. The time when the instance was updated.  
`↳ backup_minimum_enforced_retention_duration` |  `Google\Protobuf\Duration`   
Required. The default and minimum enforced retention for each backup within the backup vault. The enforced retention for each backup can be extended. Note: Longer minimum enforced retention period impacts potential storage costs post introductory trial. We recommend starting with a short duration of 3 days or less.  
`↳ backup_retention_inheritance` |  `int`   
Optional. Setting for how a backup's enforced retention end time is inherited.  
`↳ deletable` |  `bool`   
Output only. Set to true when there are no backups nested under this resource.  
`↳ etag` |  `string`   
Optional. Server specified ETag for the backup vault resource to prevent simultaneous updates from overwiting each other.  
`↳ state` |  `int`   
Output only. The BackupVault resource instance state.  
`↳ effective_time` |  `Google\Protobuf\Timestamp`   
Optional. Time after which the BackupVault resource is locked.  
`↳ backup_count` |  `int|string`   
Output only. The number of backups in this backup vault.  
`↳ service_account` |  `string`   
Output only. Service account used by the BackupVault Service for this BackupVault. The user should grant this account permissions in their workload project to enable the service to run backups and restores there.  
`↳ total_stored_bytes` |  `int|string`   
Output only. Total size of the storage used by all backup resources.  
`↳ uid` |  `string`   
Output only. Immutable after resource creation until resource deletion.  
`↳ annotations` |  `array|Google\Protobuf\Internal\MapField`   
Optional. User annotations. See <https://google.aip.dev/128#annotations> Stores small amounts of arbitrary data.  
`↳ access_restriction` |  `int`   
Optional. Restricts access to certain sources and destinations for data being sent into, or restored from, the backup vault. Defaults to WITHIN_ORGANIZATION if not provided during creation.  
`↳ encryption_config` |  `[BackupVault\EncryptionConfig](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupVault.EncryptionConfig)`   
Optional. The encryption config of the backup vault.  
  
### getName

Output only. Identifier. Name of the backup vault to create. It must have the format`"projects/{project}/locations/{location}/backupVaults/{backupvault}"`.

`{backupvault}` cannot be changed after creation. It must be between 3-63 characters long and must be unique within the project and location.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Output only. Identifier. Name of the backup vault to create. It must have the format`"projects/{project}/locations/{location}/backupVaults/{backupvault}"`.

`{backupvault}` cannot be changed after creation. It must be between 3-63 characters long and must be unique within the project and location.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDescription

Optional. The description of the BackupVault instance (2048 characters or less).

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasDescription

### clearDescription

### setDescription

Optional. The description of the BackupVault instance (2048 characters or less).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLabels

Optional. Resource labels to represent user provided metadata.

No labels currently defined:

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Internal\MapField` |   
  
### setLabels

Optional. Resource labels to represent user provided metadata.

No labels currently defined:

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array|Google\Protobuf\Internal\MapField`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreateTime

Output only. The time when the instance was created.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasCreateTime

### clearCreateTime

### setCreateTime

Output only. The time when the instance was created.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdateTime

Output only. The time when the instance was updated.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasUpdateTime

### clearUpdateTime

### setUpdateTime

Output only. The time when the instance was updated.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBackupMinimumEnforcedRetentionDuration

Required. The default and minimum enforced retention for each backup within the backup vault. The enforced retention for each backup can be extended.

Note: Longer minimum enforced retention period impacts potential storage costs post introductory trial. We recommend starting with a short duration of 3 days or less.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Duration|null` |   
  
### hasBackupMinimumEnforcedRetentionDuration

### clearBackupMinimumEnforcedRetentionDuration

### setBackupMinimumEnforcedRetentionDuration

Required. The default and minimum enforced retention for each backup within the backup vault. The enforced retention for each backup can be extended.

Note: Longer minimum enforced retention period impacts potential storage costs post introductory trial. We recommend starting with a short duration of 3 days or less.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Duration`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBackupRetentionInheritance

Optional. Setting for how a backup's enforced retention end time is inherited.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### hasBackupRetentionInheritance

### clearBackupRetentionInheritance

### setBackupRetentionInheritance

Optional. Setting for how a backup's enforced retention end time is inherited.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDeletable

Output only. Set to true when there are no backups nested under this resource.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### hasDeletable

### clearDeletable

### setDeletable

Output only. Set to true when there are no backups nested under this resource.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEtag

Optional. Server specified ETag for the backup vault resource to prevent simultaneous updates from overwiting each other.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasEtag

### clearEtag

### setEtag

Optional. Server specified ETag for the backup vault resource to prevent simultaneous updates from overwiting each other.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getState

Output only. The BackupVault resource instance state.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupVault.State).  
  
### setState

Output only. The BackupVault resource instance state.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupVault.State).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEffectiveTime

Optional. Time after which the BackupVault resource is locked.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasEffectiveTime

### clearEffectiveTime

### setEffectiveTime

Optional. Time after which the BackupVault resource is locked.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBackupCount

Output only. The number of backups in this backup vault.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### setBackupCount

Output only. The number of backups in this backup vault.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getServiceAccount

Output only. Service account used by the BackupVault Service for this BackupVault. The user should grant this account permissions in their workload project to enable the service to run backups and restores there.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setServiceAccount

Output only. Service account used by the BackupVault Service for this BackupVault. The user should grant this account permissions in their workload project to enable the service to run backups and restores there.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTotalStoredBytes

Output only. Total size of the storage used by all backup resources.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### setTotalStoredBytes

Output only. Total size of the storage used by all backup resources.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUid

Output only. Immutable after resource creation until resource deletion.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setUid

Output only. Immutable after resource creation until resource deletion.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAnnotations

Optional. User annotations. See <https://google.aip.dev/128#annotations> Stores small amounts of arbitrary data.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Internal\MapField` |   
  
### setAnnotations

Optional. User annotations. See <https://google.aip.dev/128#annotations> Stores small amounts of arbitrary data.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array|Google\Protobuf\Internal\MapField`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAccessRestriction

Optional. Restricts access to certain sources and destinations for data being sent into, or restored from, the backup vault. Defaults to WITHIN_ORGANIZATION if not provided during creation.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [AccessRestriction](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupVault.AccessRestriction).  
  
### setAccessRestriction

Optional. Restricts access to certain sources and destinations for data being sent into, or restored from, the backup vault. Defaults to WITHIN_ORGANIZATION if not provided during creation.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [AccessRestriction](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupVault.AccessRestriction).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEncryptionConfig

Optional. The encryption config of the backup vault.

**Returns**  
---  
**Type** | **Description**  
`[BackupVault\EncryptionConfig](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupVault.EncryptionConfig)|null` |   
  
### hasEncryptionConfig

### clearEncryptionConfig

### setEncryptionConfig

Optional. The encryption config of the backup vault.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[BackupVault\EncryptionConfig](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupVault.EncryptionConfig)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
