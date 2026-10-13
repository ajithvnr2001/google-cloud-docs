---
url: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupApplianceLockInfo
title: Google Cloud Backup Dr V1beta Client - Class BackupApplianceLockInfo (0.15.1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:19:05.291222+00:00
---

# Google Cloud Backup Dr V1beta Client - Class BackupApplianceLockInfo (0.15.1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupApplianceLockInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Backup Dr V1beta Client - Class BackupApplianceLockInfo (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.13.2  0.12.1  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.2  0.5.1  0.4.2  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Backup Dr V1beta Client class BackupApplianceLockInfo.

BackupApplianceLockInfo contains metadata about the backupappliance that created the lock.

Generated from protobuf message `google.cloud.backupdr.v1beta.BackupApplianceLockInfo`

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
`↳ job_name` |  `string`   
The job name on the backup/recovery appliance that created this lock.  
`↳ backup_image` |  `string`   
The image name that depends on this Backup.  
`↳ sla_id` |  `int|string`   
The SLA on the backup/recovery appliance that owns the lock.  
`↳ backup_appliance_id` |  `int|string`   
Required. The ID of the backup/recovery appliance that created this lock.  
`↳ backup_appliance_name` |  `string`   
Required. The name of the backup/recovery appliance that created this lock.  
`↳ lock_reason` |  `string`   
Required. The reason for the lock: e.g. MOUNT/RESTORE/BACKUP/etc. The value of this string is only meaningful to the client and it is not interpreted by the BackupVault service.  
  
### getJobName

The job name on the backup/recovery appliance that created this lock.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasJobName

### setJobName

The job name on the backup/recovery appliance that created this lock.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBackupImage

The image name that depends on this Backup.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasBackupImage

### setBackupImage

The image name that depends on this Backup.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSlaId

The SLA on the backup/recovery appliance that owns the lock.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### hasSlaId

### setSlaId

The SLA on the backup/recovery appliance that owns the lock.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBackupApplianceId

Required. The ID of the backup/recovery appliance that created this lock.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### setBackupApplianceId

Required. The ID of the backup/recovery appliance that created this lock.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBackupApplianceName

Required. The name of the backup/recovery appliance that created this lock.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setBackupApplianceName

Required. The name of the backup/recovery appliance that created this lock.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLockReason

Required. The reason for the lock: e.g. MOUNT/RESTORE/BACKUP/etc. The value of this string is only meaningful to the client and it is not interpreted by the BackupVault service.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setLockReason

Required. The reason for the lock: e.g. MOUNT/RESTORE/BACKUP/etc. The value of this string is only meaningful to the client and it is not interpreted by the BackupVault service.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLockSource

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
