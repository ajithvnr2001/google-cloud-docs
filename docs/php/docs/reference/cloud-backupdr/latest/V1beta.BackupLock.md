---
url: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupLock
title: Google Cloud Backup Dr V1beta Client - Class BackupLock (0.15.1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:19:06.416793+00:00
---

# Google Cloud Backup Dr V1beta Client - Class BackupLock (0.15.1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupLock

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Backup Dr V1beta Client - Class BackupLock (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.13.2  0.12.1  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.2  0.5.1  0.4.2  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Backup Dr V1beta Client class BackupLock.

BackupLock represents a single lock on a Backup resource. An unexpired lock on a Backup prevents the Backup from being deleted.

Generated from protobuf message `google.cloud.backupdr.v1beta.BackupLock`

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
`↳ backup_appliance_lock_info` |  `[BackupApplianceLockInfo](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupApplianceLockInfo)`   
If the client is a backup and recovery appliance, this contains metadata about why the lock exists.  
`↳ service_lock_info` |  `[ServiceLockInfo](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ServiceLockInfo)`   
Output only. Contains metadata about the lock exist for Google Cloud native backups.  
`↳ lock_until_time` |  `Google\Protobuf\Timestamp`   
Required. The time after which this lock is not considered valid and will no longer protect the Backup from deletion.  
  
### getBackupApplianceLockInfo

If the client is a backup and recovery appliance, this contains metadata about why the lock exists.

**Returns**  
---  
**Type** | **Description**  
`[BackupApplianceLockInfo](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupApplianceLockInfo)|null` |   
  
### hasBackupApplianceLockInfo

### setBackupApplianceLockInfo

If the client is a backup and recovery appliance, this contains metadata about why the lock exists.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[BackupApplianceLockInfo](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupApplianceLockInfo)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getServiceLockInfo

Output only. Contains metadata about the lock exist for Google Cloud native backups.

**Returns**  
---  
**Type** | **Description**  
`[ServiceLockInfo](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ServiceLockInfo)|null` |   
  
### hasServiceLockInfo

### setServiceLockInfo

Output only. Contains metadata about the lock exist for Google Cloud native backups.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[ServiceLockInfo](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.ServiceLockInfo)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLockUntilTime

Required. The time after which this lock is not considered valid and will no longer protect the Backup from deletion.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasLockUntilTime

### clearLockUntilTime

### setLockUntilTime

Required. The time after which this lock is not considered valid and will no longer protect the Backup from deletion.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getClientLockInfo

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
