---
url: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupConfigInfo
title: Google Cloud Backup Dr V1beta Client - Class BackupConfigInfo (0.15.1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:00:02.659242+00:00
---

# Google Cloud Backup Dr V1beta Client - Class BackupConfigInfo (0.15.1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupConfigInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Backup Dr V1beta Client - Class BackupConfigInfo (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.13.2  0.12.1  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.2  0.5.1  0.4.2  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Backup Dr V1beta Client class BackupConfigInfo.

BackupConfigInfo has information about how the resource is configured for Backup and about the most recent backup to this vault.

Generated from protobuf message `google.cloud.backupdr.v1beta.BackupConfigInfo`

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
`↳ gcp_backup_config` |  `[GcpBackupConfig](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.GcpBackupConfig)`   
Configuration for a Google Cloud resource.  
`↳ backup_appliance_backup_config` |  `[BackupApplianceBackupConfig](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupApplianceBackupConfig)`   
Configuration for an application backed up by a Backup Appliance.  
`↳ last_backup_state` |  `int`   
Output only. The status of the last backup to this BackupVault  
`↳ last_successful_backup_consistency_time` |  `Google\Protobuf\Timestamp`   
Output only. If the last backup were successful, this field has the consistency date.  
`↳ last_backup_error` |  `[Google\Rpc\Status](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Rpc.Status.html)`   
Output only. If the last backup failed, this field has the error message.  
  
### getGcpBackupConfig

Configuration for a Google Cloud resource.

**Returns**  
---  
**Type** | **Description**  
`[GcpBackupConfig](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.GcpBackupConfig)|null` |   
  
### hasGcpBackupConfig

### setGcpBackupConfig

Configuration for a Google Cloud resource.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[GcpBackupConfig](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.GcpBackupConfig)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBackupApplianceBackupConfig

Configuration for an application backed up by a Backup Appliance.

**Returns**  
---  
**Type** | **Description**  
`[BackupApplianceBackupConfig](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupApplianceBackupConfig)|null` |   
  
### hasBackupApplianceBackupConfig

### setBackupApplianceBackupConfig

Configuration for an application backed up by a Backup Appliance.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[BackupApplianceBackupConfig](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupApplianceBackupConfig)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLastBackupState

Output only. The status of the last backup to this BackupVault

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [LastBackupState](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupConfigInfo.LastBackupState).  
  
### setLastBackupState

Output only. The status of the last backup to this BackupVault

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [LastBackupState](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupConfigInfo.LastBackupState).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLastSuccessfulBackupConsistencyTime

Output only. If the last backup were successful, this field has the consistency date.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasLastSuccessfulBackupConsistencyTime

### clearLastSuccessfulBackupConsistencyTime

### setLastSuccessfulBackupConsistencyTime

Output only. If the last backup were successful, this field has the consistency date.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLastBackupError

Output only. If the last backup failed, this field has the error message.

**Returns**  
---  
**Type** | **Description**  
`[Google\Rpc\Status](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Rpc.Status.html)|null` |   
  
### hasLastBackupError

### clearLastBackupError

### setLastBackupError

Output only. If the last backup failed, this field has the error message.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Rpc\Status](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Rpc.Status.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBackupConfig

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
