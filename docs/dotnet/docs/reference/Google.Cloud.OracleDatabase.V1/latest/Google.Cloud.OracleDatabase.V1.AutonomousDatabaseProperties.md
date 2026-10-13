---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties
title: Oracle Database@Google Cloud v1 API - Class AutonomousDatabaseProperties (1.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:06:30.408210+00:00
---

# Oracle Database@Google Cloud v1 API - Class AutonomousDatabaseProperties (1.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Oracle Database@Google Cloud v1 API - Class AutonomousDatabaseProperties (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class AutonomousDatabaseProperties : IMessage<AutonomousDatabaseProperties>, IEquatable<AutonomousDatabaseProperties>, IDeepCloneable<AutonomousDatabaseProperties>, IBufferMessage, IMessage

Reference documentation and code samples for the Oracle Database@Google Cloud v1 API class AutonomousDatabaseProperties.

The properties of an Autonomous Database.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AutonomousDatabaseProperties

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AutonomousDatabaseProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AutonomousDatabaseProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AutonomousDatabaseProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.OracleDatabase.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1)

## Assembly

Google.Cloud.OracleDatabase.V1.dll

## Constructors 

### AutonomousDatabaseProperties()
    
    
    public AutonomousDatabaseProperties()

### AutonomousDatabaseProperties(AutonomousDatabaseProperties)
    
    
    public AutonomousDatabaseProperties(AutonomousDatabaseProperties other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AutonomousDatabaseProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties)`  
  
  
## Properties 

### ActualUsedDataStorageSizeTb
    
    
    public double ActualUsedDataStorageSizeTb { get; set; }

Output only. The amount of storage currently being used for user and system data, in terabytes.

**Property Value**  
---  
**Type** | **Description**  
`[double](https://learn.microsoft.com/dotnet/api/system.double)` |   
  
### AllocatedStorageSizeTb
    
    
    public double AllocatedStorageSizeTb { get; set; }

Output only. The amount of storage currently allocated for the database tables and billed for, rounded up in terabytes.

**Property Value**  
---  
**Type** | **Description**  
`[double](https://learn.microsoft.com/dotnet/api/system.double)` |   
  
### AllowlistedIps
    
    
    public RepeatedField<string> AllowlistedIps { get; }

Optional. Immutable. The list of allowlisted IP addresses for the Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ApexDetails
    
    
    public AutonomousDatabaseApex ApexDetails { get; set; }

Output only. The details for the Oracle APEX Application Development.

**Property Value**  
---  
**Type** | **Description**  
`[AutonomousDatabaseApex](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseApex)` |   
  
### ArePrimaryAllowlistedIpsUsed
    
    
    public bool ArePrimaryAllowlistedIpsUsed { get; set; }

Output only. This field indicates the status of Data Guard and Access control for the Autonomous Database. The field's value is null if Data Guard is disabled or Access Control is disabled. The field's value is TRUE if both Data Guard and Access Control are enabled, and the Autonomous Database is using primary IP access control list (ACL) for standby. The field's value is FALSE if both Data Guard and Access Control are enabled, and the Autonomous Database is using a different IP access control list (ACL) for standby compared to primary.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### AutonomousContainerDatabaseId
    
    
    public string AutonomousContainerDatabaseId { get; set; }

Output only. The Autonomous Container Database OCID.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AvailableUpgradeVersions
    
    
    public RepeatedField<string> AvailableUpgradeVersions { get; }

Output only. The list of available Oracle Database upgrade versions for an Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### BackupRetentionPeriodDays
    
    
    public int BackupRetentionPeriodDays { get; set; }

Optional. Immutable. The retention period for the Autonomous Database. This field is specified in days, can range from 1 day to 60 days, and has a default value of 60 days.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### CharacterSet
    
    
    public string CharacterSet { get; set; }

Optional. Immutable. The character set for the Autonomous Database. The default is AL32UTF8.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ComputeCount
    
    
    public float ComputeCount { get; set; }

Optional. Immutable. The number of compute servers for the Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### ConnectionStrings
    
    
    public AutonomousDatabaseConnectionStrings ConnectionStrings { get; set; }

Output only. The connection strings used to connect to an Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[AutonomousDatabaseConnectionStrings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseConnectionStrings)` |   
  
### ConnectionUrls
    
    
    public AutonomousDatabaseConnectionUrls ConnectionUrls { get; set; }

Output only. The Oracle Connection URLs for an Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[AutonomousDatabaseConnectionUrls](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseConnectionUrls)` |   
  
### CpuCoreCount
    
    
    public int CpuCoreCount { get; set; }

Optional. Immutable. The number of CPU cores to be made available to the database.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### CustomerContacts
    
    
    public RepeatedField<CustomerContact> CustomerContacts { get; }

Optional. Immutable. The list of customer contacts.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[CustomerContact](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.CustomerContact)` |   
  
### DataGuardRoleChangedTime
    
    
    public Timestamp DataGuardRoleChangedTime { get; set; }

Output only. The date and time the Autonomous Data Guard role was changed for the standby Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### DataSafeState
    
    
    public AutonomousDatabaseProperties.Types.DataSafeState DataSafeState { get; set; }

Output only. The current state of the Data Safe registration for the Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[AutonomousDatabaseProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties.Types)[DataSafeState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties.Types.DataSafeState)` |   
  
### DataStorageSizeGb
    
    
    public int DataStorageSizeGb { get; set; }

Optional. Immutable. The size of the data stored in the database, in gigabytes.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### DataStorageSizeTb
    
    
    public int DataStorageSizeTb { get; set; }

Optional. Immutable. The size of the data stored in the database, in terabytes.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### DatabaseManagementState
    
    
    public AutonomousDatabaseProperties.Types.DatabaseManagementState DatabaseManagementState { get; set; }

Output only. The current state of database management for the Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[AutonomousDatabaseProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties.Types)[DatabaseManagementState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties.Types.DatabaseManagementState)` |   
  
### DbEdition
    
    
    public AutonomousDatabaseProperties.Types.DatabaseEdition DbEdition { get; set; }

Optional. Immutable. The edition of the Autonomous Databases.

**Property Value**  
---  
**Type** | **Description**  
`[AutonomousDatabaseProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties.Types)[DatabaseEdition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties.Types.DatabaseEdition)` |   
  
### DbVersion
    
    
    public string DbVersion { get; set; }

Optional. Immutable. The Oracle Database version for the Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DbWorkload
    
    
    public DBWorkload DbWorkload { get; set; }

Required. Immutable. The workload type of the Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[DBWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DBWorkload)` |   
  
### DisasterRecoveryRoleChangedTime
    
    
    public Timestamp DisasterRecoveryRoleChangedTime { get; set; }

Output only. The date and time the Disaster Recovery role was changed for the standby Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### EncryptionKey
    
    
    public EncryptionKey EncryptionKey { get; set; }

Optional. The encryption key used to encrypt the Autonomous Database. Updating this field will add a new entry in the `encryption_key_history_entries` field with the former version.

**Property Value**  
---  
**Type** | **Description**  
`[EncryptionKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.EncryptionKey)` |   
  
### EncryptionKeyHistoryEntries
    
    
    public RepeatedField<EncryptionKeyHistoryEntry> EncryptionKeyHistoryEntries { get; }

Output only. The history of the encryption keys used to encrypt the Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[EncryptionKeyHistoryEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.EncryptionKeyHistoryEntry)` |   
  
### FailedDataRecoveryDuration
    
    
    public Duration FailedDataRecoveryDuration { get; set; }

Output only. This field indicates the number of seconds of data loss during a Data Guard failover.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### HasArePrimaryAllowlistedIpsUsed
    
    
    public bool HasArePrimaryAllowlistedIpsUsed { get; }

Gets whether the "are_primary_allowlisted_ips_used" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasLocalAdgAutoFailoverMaxDataLossLimitDuration
    
    
    public bool HasLocalAdgAutoFailoverMaxDataLossLimitDuration { get; }

Gets whether the "local_adg_auto_failover_max_data_loss_limit_duration" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasLocalDataGuardEnabled
    
    
    public bool HasLocalDataGuardEnabled { get; }

Gets whether the "local_data_guard_enabled" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasRefreshableClone
    
    
    public bool HasRefreshableClone { get; }

Gets whether the "refreshable_clone" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### IsAutoScalingEnabled
    
    
    public bool IsAutoScalingEnabled { get; set; }

Optional. Immutable. This field indicates if auto scaling is enabled for the Autonomous Database CPU core count.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### IsLocalDataGuardEnabled
    
    
    [Obsolete]
    public bool IsLocalDataGuardEnabled { get; set; }

Output only. Deprecated: Please use `local_data_guard_enabled` instead. This field indicates whether the Autonomous Database has local (in-region) Data Guard enabled.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### IsStorageAutoScalingEnabled
    
    
    public bool IsStorageAutoScalingEnabled { get; set; }

Optional. Immutable. This field indicates if auto scaling is enabled for the Autonomous Database storage.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### LicenseType
    
    
    public AutonomousDatabaseProperties.Types.LicenseType LicenseType { get; set; }

Required. Immutable. The license type used for the Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[AutonomousDatabaseProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties.Types)[LicenseType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties.Types.LicenseType)` |   
  
### LifecycleDetails
    
    
    public string LifecycleDetails { get; set; }

Output only. The details of the current lifestyle state of the Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### LocalAdgAutoFailoverMaxDataLossLimit
    
    
    [Obsolete]
    public int LocalAdgAutoFailoverMaxDataLossLimit { get; set; }

Output only. Deprecated: Please use `local_adg_auto_failover_max_data_loss_limit_duration` instead. This field indicates the maximum data loss limit for an Autonomous Database, in seconds.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### LocalAdgAutoFailoverMaxDataLossLimitDuration
    
    
    public int LocalAdgAutoFailoverMaxDataLossLimitDuration { get; set; }

Optional. This field indicates the maximum data loss limit for an Autonomous Database, in seconds.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### LocalDataGuardEnabled
    
    
    public bool LocalDataGuardEnabled { get; set; }

Optional. Indicates whether the Autonomous Database has a local (in-region) standby database. Not applicable to cross-region Data Guard or dedicated Exadata infrastructure.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### LocalDisasterRecoveryType
    
    
    public AutonomousDatabaseProperties.Types.LocalDisasterRecoveryType LocalDisasterRecoveryType { get; set; }

Output only. This field indicates the local disaster recovery (DR) type of an Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[AutonomousDatabaseProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties.Types)[LocalDisasterRecoveryType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties.Types.LocalDisasterRecoveryType)` |   
  
### LocalStandbyDb
    
    
    public AutonomousDatabaseStandbySummary LocalStandbyDb { get; set; }

Output only. The details of the Autonomous Data Guard standby database.

**Property Value**  
---  
**Type** | **Description**  
`[AutonomousDatabaseStandbySummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseStandbySummary)` |   
  
### MaintenanceBeginTime
    
    
    public Timestamp MaintenanceBeginTime { get; set; }

Output only. The date and time when maintenance will begin.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### MaintenanceEndTime
    
    
    public Timestamp MaintenanceEndTime { get; set; }

Output only. The date and time when maintenance will end.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### MaintenanceScheduleType
    
    
    public AutonomousDatabaseProperties.Types.MaintenanceScheduleType MaintenanceScheduleType { get; set; }

Optional. Immutable. The maintenance schedule of the Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[AutonomousDatabaseProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties.Types)[MaintenanceScheduleType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties.Types.MaintenanceScheduleType)` |   
  
### MemoryPerOracleComputeUnitGbs
    
    
    public int MemoryPerOracleComputeUnitGbs { get; set; }

Output only. The amount of memory enabled per ECPU, in gigabytes.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### MemoryTableGbs
    
    
    public int MemoryTableGbs { get; set; }

Output only. The memory assigned to in-memory tables in an Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### MtlsConnectionRequired
    
    
    public bool MtlsConnectionRequired { get; set; }

Optional. Immutable. This field specifies if the Autonomous Database requires mTLS connections.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### NCharacterSet
    
    
    public string NCharacterSet { get; set; }

Optional. Immutable. The national character set for the Autonomous Database. The default is AL16UTF16.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NextLongTermBackupTime
    
    
    public Timestamp NextLongTermBackupTime { get; set; }

Output only. The long term backup schedule of the Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### OciUrl
    
    
    public string OciUrl { get; set; }

Output only. The Oracle Cloud Infrastructure link for the Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Ocid
    
    
    public string Ocid { get; set; }

Output only. OCID of the Autonomous Database. <https://docs.oracle.com/en-us/iaas/Content/General/Concepts/identifiers.htm#Oracle>

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OpenMode
    
    
    public AutonomousDatabaseProperties.Types.OpenMode OpenMode { get; set; }

Output only. This field indicates the current mode of the Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[AutonomousDatabaseProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties.Types)[OpenMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties.Types.OpenMode)` |   
  
### OperationsInsightsState
    
    
    public OperationsInsightsState OperationsInsightsState { get; set; }

Output only. This field indicates the state of Operations Insights for the Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsInsightsState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OperationsInsightsState)` |   
  
### PeerDbIds
    
    
    public RepeatedField<string> PeerDbIds { get; }

Output only. The list of OCIDs of standby databases located in Autonomous Data Guard remote regions that are associated with the source database.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PermissionLevel
    
    
    public AutonomousDatabaseProperties.Types.PermissionLevel PermissionLevel { get; set; }

Output only. The permission level of the Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[AutonomousDatabaseProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties.Types)[PermissionLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties.Types.PermissionLevel)` |   
  
### PrivateEndpoint
    
    
    public string PrivateEndpoint { get; set; }

Output only. The private endpoint for the Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PrivateEndpointIp
    
    
    public string PrivateEndpointIp { get; set; }

Optional. Immutable. The private endpoint IP address for the Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PrivateEndpointLabel
    
    
    public string PrivateEndpointLabel { get; set; }

Optional. Immutable. The private endpoint label for the Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RefreshableClone
    
    
    public bool RefreshableClone { get; set; }

Optional. Indicates if the Autonomous Database is a refreshable clone. This field is used in update flow to connect / disconnect a refreshable clone from its source database.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### RefreshableMode
    
    
    public AutonomousDatabaseProperties.Types.RefreshableMode RefreshableMode { get; set; }

Output only. The refresh mode of the cloned Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[AutonomousDatabaseProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties.Types)[RefreshableMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties.Types.RefreshableMode)` |   
  
### RefreshableState
    
    
    public AutonomousDatabaseProperties.Types.RefreshableState RefreshableState { get; set; }

Output only. The refresh State of the clone.

**Property Value**  
---  
**Type** | **Description**  
`[AutonomousDatabaseProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties.Types)[RefreshableState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties.Types.RefreshableState)` |   
  
### Role
    
    
    public AutonomousDatabaseProperties.Types.Role Role { get; set; }

Output only. The Data Guard role of the Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[AutonomousDatabaseProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties.Types)[Role](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseProperties.Types.Role)` |   
  
### ScheduledOperationDetails
    
    
    public RepeatedField<ScheduledOperationDetails> ScheduledOperationDetails { get; }

Output only. The list and details of the scheduled operations of the Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[ScheduledOperationDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ScheduledOperationDetails)` |   
  
### SecretId
    
    
    public string SecretId { get; set; }

Optional. Immutable. The ID of the Oracle Cloud Infrastructure vault secret.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServiceAgentEmail
    
    
    public string ServiceAgentEmail { get; set; }

Output only. An Oracle-managed Google Cloud service account on which customers can grant roles to access resources in the customer project.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SqlWebDeveloperUrl
    
    
    public string SqlWebDeveloperUrl { get; set; }

Output only. The SQL Web Developer URL for the Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### State
    
    
    public State State { get; set; }

Output only. The current lifecycle state of the Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.State)` |   
  
### SupportedCloneRegions
    
    
    public RepeatedField<string> SupportedCloneRegions { get; }

Output only. The list of available regions that can be used to create a clone for the Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TotalAutoBackupStorageSizeGbs
    
    
    public float TotalAutoBackupStorageSizeGbs { get; set; }

Output only. The storage space used by automatic backups of Autonomous Database, in gigabytes.

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### UsedDataStorageSizeTbs
    
    
    public int UsedDataStorageSizeTbs { get; set; }

Output only. The storage space used by Autonomous Database, in gigabytes.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### VaultId
    
    
    public string VaultId { get; set; }

Optional. Immutable. The ID of the Oracle Cloud Infrastructure vault.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
