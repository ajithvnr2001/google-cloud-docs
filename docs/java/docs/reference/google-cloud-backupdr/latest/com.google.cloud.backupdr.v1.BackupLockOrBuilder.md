---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupLockOrBuilder
title: Interface BackupLockOrBuilder (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:17:38.678950+00:00
---

# Interface BackupLockOrBuilder (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupLockOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BackupLockOrBuilder (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface BackupLockOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBackupApplianceLockInfo()
    
    
    public abstract BackupApplianceLockInfo getBackupApplianceLockInfo()

If the client is a backup and recovery appliance, this contains metadata about why the lock exists.

`.google.cloud.backupdr.v1.BackupApplianceLockInfo backup_appliance_lock_info = 3;`

**Returns**  
---  
**Type** | **Description**  
`[BackupApplianceLockInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupApplianceLockInfo)` | The backupApplianceLockInfo.  
  
### getBackupApplianceLockInfoOrBuilder()
    
    
    public abstract BackupApplianceLockInfoOrBuilder getBackupApplianceLockInfoOrBuilder()

If the client is a backup and recovery appliance, this contains metadata about why the lock exists.

`.google.cloud.backupdr.v1.BackupApplianceLockInfo backup_appliance_lock_info = 3;`

**Returns**  
---  
**Type** | **Description**  
`[BackupApplianceLockInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupApplianceLockInfoOrBuilder)` |   
  
### getClientLockInfoCase()
    
    
    public abstract BackupLock.ClientLockInfoCase getClientLockInfoCase()

**Returns**  
---  
**Type** | **Description**  
`[BackupLock.ClientLockInfoCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupLock.ClientLockInfoCase)` |   
  
### getLockUntilTime()
    
    
    public abstract Timestamp getLockUntilTime()

Required. The time after which this lock is not considered valid and will no longer protect the Backup from deletion.

`.google.protobuf.Timestamp lock_until_time = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The lockUntilTime.  
  
### getLockUntilTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getLockUntilTimeOrBuilder()

Required. The time after which this lock is not considered valid and will no longer protect the Backup from deletion.

`.google.protobuf.Timestamp lock_until_time = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getServiceLockInfo()
    
    
    public abstract ServiceLockInfo getServiceLockInfo()

Output only. Contains metadata about the lock exist for Google Cloud native backups.

` .google.cloud.backupdr.v1.ServiceLockInfo service_lock_info = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ServiceLockInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ServiceLockInfo)` | The serviceLockInfo.  
  
### getServiceLockInfoOrBuilder()
    
    
    public abstract ServiceLockInfoOrBuilder getServiceLockInfoOrBuilder()

Output only. Contains metadata about the lock exist for Google Cloud native backups.

` .google.cloud.backupdr.v1.ServiceLockInfo service_lock_info = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ServiceLockInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ServiceLockInfoOrBuilder)` |   
  
### hasBackupApplianceLockInfo()
    
    
    public abstract boolean hasBackupApplianceLockInfo()

If the client is a backup and recovery appliance, this contains metadata about why the lock exists.

`.google.cloud.backupdr.v1.BackupApplianceLockInfo backup_appliance_lock_info = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the backupApplianceLockInfo field is set.  
  
### hasLockUntilTime()
    
    
    public abstract boolean hasLockUntilTime()

Required. The time after which this lock is not considered valid and will no longer protect the Backup from deletion.

`.google.protobuf.Timestamp lock_until_time = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the lockUntilTime field is set.  
  
### hasServiceLockInfo()
    
    
    public abstract boolean hasServiceLockInfo()

Output only. Contains metadata about the lock exist for Google Cloud native backups.

` .google.cloud.backupdr.v1.ServiceLockInfo service_lock_info = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the serviceLockInfo field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
