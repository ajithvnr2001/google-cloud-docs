---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.BackupConfigurationOrBuilder
title: Interface BackupConfigurationOrBuilder (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:41:16.075855+00:00
---

# Interface BackupConfigurationOrBuilder (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.BackupConfigurationOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BackupConfigurationOrBuilder (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public interface BackupConfigurationOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBackupRetentionSettings()
    
    
    public abstract BackupRetentionSettings getBackupRetentionSettings()

Backup retention settings.

`.google.cloud.sql.v1beta4.BackupRetentionSettings backup_retention_settings = 10;`

**Returns**  
---  
**Type** | **Description**  
`[BackupRetentionSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.BackupRetentionSettings)` | The backupRetentionSettings.  
  
### getBackupRetentionSettingsOrBuilder()
    
    
    public abstract BackupRetentionSettingsOrBuilder getBackupRetentionSettingsOrBuilder()

Backup retention settings.

`.google.cloud.sql.v1beta4.BackupRetentionSettings backup_retention_settings = 10;`

**Returns**  
---  
**Type** | **Description**  
`[BackupRetentionSettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.BackupRetentionSettingsOrBuilder)` |   
  
### getBackupTier()
    
    
    public abstract BackupConfiguration.BackupTier getBackupTier()

Output only. Backup tier that manages the backups for the instance.

` optional .google.cloud.sql.v1beta4.BackupConfiguration.BackupTier backup_tier = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[BackupConfiguration.BackupTier](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.BackupConfiguration.BackupTier)` | The backupTier.  
  
### getBackupTierValue()
    
    
    public abstract int getBackupTierValue()

Output only. Backup tier that manages the backups for the instance.

` optional .google.cloud.sql.v1beta4.BackupConfiguration.BackupTier backup_tier = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for backupTier.  
  
### getBinaryLogEnabled()
    
    
    public abstract BoolValue getBinaryLogEnabled()

(MySQL only) Whether binary log is enabled. If backup configuration is disabled, binarylog must be disabled as well.

`.google.protobuf.BoolValue binary_log_enabled = 4;`

**Returns**  
---  
**Type** | **Description**  
`[BoolValue](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValue.html)` | The binaryLogEnabled.  
  
### getBinaryLogEnabledOrBuilder()
    
    
    public abstract BoolValueOrBuilder getBinaryLogEnabledOrBuilder()

(MySQL only) Whether binary log is enabled. If backup configuration is disabled, binarylog must be disabled as well.

`.google.protobuf.BoolValue binary_log_enabled = 4;`

**Returns**  
---  
**Type** | **Description**  
`[BoolValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValueOrBuilder.html)` |   
  
### getEnabled()
    
    
    public abstract BoolValue getEnabled()

Whether this configuration is enabled.

`.google.protobuf.BoolValue enabled = 2;`

**Returns**  
---  
**Type** | **Description**  
`[BoolValue](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValue.html)` | The enabled.  
  
### getEnabledOrBuilder()
    
    
    public abstract BoolValueOrBuilder getEnabledOrBuilder()

Whether this configuration is enabled.

`.google.protobuf.BoolValue enabled = 2;`

**Returns**  
---  
**Type** | **Description**  
`[BoolValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValueOrBuilder.html)` |   
  
### getKind()
    
    
    public abstract String getKind()

This is always `sql#backupConfiguration`.

`string kind = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kind.  
  
### getKindBytes()
    
    
    public abstract ByteString getKindBytes()

This is always `sql#backupConfiguration`.

`string kind = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kind.  
  
### getLocation()
    
    
    public abstract String getLocation()

Location of the backup

`string location = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The location.  
  
### getLocationBytes()
    
    
    public abstract ByteString getLocationBytes()

Location of the backup

`string location = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for location.  
  
### getPointInTimeRecoveryEnabled()
    
    
    public abstract BoolValue getPointInTimeRecoveryEnabled()

Whether point in time recovery is enabled.

`.google.protobuf.BoolValue point_in_time_recovery_enabled = 7;`

**Returns**  
---  
**Type** | **Description**  
`[BoolValue](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValue.html)` | The pointInTimeRecoveryEnabled.  
  
### getPointInTimeRecoveryEnabledOrBuilder()
    
    
    public abstract BoolValueOrBuilder getPointInTimeRecoveryEnabledOrBuilder()

Whether point in time recovery is enabled.

`.google.protobuf.BoolValue point_in_time_recovery_enabled = 7;`

**Returns**  
---  
**Type** | **Description**  
`[BoolValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValueOrBuilder.html)` |   
  
### getReplicationLogArchivingEnabled() (deprecated)
    
    
    public abstract BoolValue getReplicationLogArchivingEnabled()

**Deprecated.** _google.cloud.sql.v1beta4.BackupConfiguration.replication_log_archiving_enabled is deprecated. See google/cloud/sql/v1beta4/cloud_sql_resources.proto;l=183_

Optional. Deprecated: replication_log_archiving_enabled is deprecated and will be removed from a future version of the API. Use point_in_time_recovery_enabled instead.

` .google.protobuf.BoolValue replication_log_archiving_enabled = 5 [deprecated = true, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[BoolValue](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValue.html)` | The replicationLogArchivingEnabled.  
  
### getReplicationLogArchivingEnabledOrBuilder() (deprecated)
    
    
    public abstract BoolValueOrBuilder getReplicationLogArchivingEnabledOrBuilder()

Optional. Deprecated: replication_log_archiving_enabled is deprecated and will be removed from a future version of the API. Use point_in_time_recovery_enabled instead.

` .google.protobuf.BoolValue replication_log_archiving_enabled = 5 [deprecated = true, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[BoolValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValueOrBuilder.html)` |   
  
### getStartTime()
    
    
    public abstract String getStartTime()

Start time for the daily backup configuration in UTC timezone in the 24 hour format - `HH:MM`.

`string start_time = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The startTime.  
  
### getStartTimeBytes()
    
    
    public abstract ByteString getStartTimeBytes()

Start time for the daily backup configuration in UTC timezone in the 24 hour format - `HH:MM`.

`string start_time = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for startTime.  
  
### getTransactionLogRetentionDays()
    
    
    public abstract Int32Value getTransactionLogRetentionDays()

The number of days of transaction logs we retain for point in time restore, from 1-7.

`.google.protobuf.Int32Value transaction_log_retention_days = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Int32Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int32Value.html)` | The transactionLogRetentionDays.  
  
### getTransactionLogRetentionDaysOrBuilder()
    
    
    public abstract Int32ValueOrBuilder getTransactionLogRetentionDaysOrBuilder()

The number of days of transaction logs we retain for point in time restore, from 1-7.

`.google.protobuf.Int32Value transaction_log_retention_days = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Int32ValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int32ValueOrBuilder.html)` |   
  
### getTransactionalLogStorageState()
    
    
    public abstract BackupConfiguration.TransactionalLogStorageState getTransactionalLogStorageState()

Output only. This value contains the storage location of transactional logs for the database for point-in-time recovery.

` optional .google.cloud.sql.v1beta4.BackupConfiguration.TransactionalLogStorageState transactional_log_storage_state = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[BackupConfiguration.TransactionalLogStorageState](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.BackupConfiguration.TransactionalLogStorageState)` | The transactionalLogStorageState.  
  
### getTransactionalLogStorageStateValue()
    
    
    public abstract int getTransactionalLogStorageStateValue()

Output only. This value contains the storage location of transactional logs for the database for point-in-time recovery.

` optional .google.cloud.sql.v1beta4.BackupConfiguration.TransactionalLogStorageState transactional_log_storage_state = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for transactionalLogStorageState.  
  
### hasBackupRetentionSettings()
    
    
    public abstract boolean hasBackupRetentionSettings()

Backup retention settings.

`.google.cloud.sql.v1beta4.BackupRetentionSettings backup_retention_settings = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the backupRetentionSettings field is set.  
  
### hasBackupTier()
    
    
    public abstract boolean hasBackupTier()

Output only. Backup tier that manages the backups for the instance.

` optional .google.cloud.sql.v1beta4.BackupConfiguration.BackupTier backup_tier = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the backupTier field is set.  
  
### hasBinaryLogEnabled()
    
    
    public abstract boolean hasBinaryLogEnabled()

(MySQL only) Whether binary log is enabled. If backup configuration is disabled, binarylog must be disabled as well.

`.google.protobuf.BoolValue binary_log_enabled = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the binaryLogEnabled field is set.  
  
### hasEnabled()
    
    
    public abstract boolean hasEnabled()

Whether this configuration is enabled.

`.google.protobuf.BoolValue enabled = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the enabled field is set.  
  
### hasPointInTimeRecoveryEnabled()
    
    
    public abstract boolean hasPointInTimeRecoveryEnabled()

Whether point in time recovery is enabled.

`.google.protobuf.BoolValue point_in_time_recovery_enabled = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pointInTimeRecoveryEnabled field is set.  
  
### hasReplicationLogArchivingEnabled() (deprecated)
    
    
    public abstract boolean hasReplicationLogArchivingEnabled()

**Deprecated.** _google.cloud.sql.v1beta4.BackupConfiguration.replication_log_archiving_enabled is deprecated. See google/cloud/sql/v1beta4/cloud_sql_resources.proto;l=183_

Optional. Deprecated: replication_log_archiving_enabled is deprecated and will be removed from a future version of the API. Use point_in_time_recovery_enabled instead.

` .google.protobuf.BoolValue replication_log_archiving_enabled = 5 [deprecated = true, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the replicationLogArchivingEnabled field is set.  
  
### hasTransactionLogRetentionDays()
    
    
    public abstract boolean hasTransactionLogRetentionDays()

The number of days of transaction logs we retain for point in time restore, from 1-7.

`.google.protobuf.Int32Value transaction_log_retention_days = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the transactionLogRetentionDays field is set.  
  
### hasTransactionalLogStorageState()
    
    
    public abstract boolean hasTransactionalLogStorageState()

Output only. This value contains the storage location of transactional logs for the database for point-in-time recovery.

` optional .google.cloud.sql.v1beta4.BackupConfiguration.TransactionalLogStorageState transactional_log_storage_state = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the transactionalLogStorageState field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
