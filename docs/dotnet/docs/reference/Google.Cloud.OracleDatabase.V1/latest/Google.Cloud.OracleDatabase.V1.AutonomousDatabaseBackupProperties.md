---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseBackupProperties
title: Oracle Database@Google Cloud v1 API - Class AutonomousDatabaseBackupProperties (1.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:06:27.388110+00:00
---

# Oracle Database@Google Cloud v1 API - Class AutonomousDatabaseBackupProperties (1.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseBackupProperties

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Oracle Database@Google Cloud v1 API - Class AutonomousDatabaseBackupProperties (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class AutonomousDatabaseBackupProperties : IMessage<AutonomousDatabaseBackupProperties>, IEquatable<AutonomousDatabaseBackupProperties>, IDeepCloneable<AutonomousDatabaseBackupProperties>, IBufferMessage, IMessage

Reference documentation and code samples for the Oracle Database@Google Cloud v1 API class AutonomousDatabaseBackupProperties.

Properties of the Autonomous Database Backup resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AutonomousDatabaseBackupProperties

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AutonomousDatabaseBackupProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseBackupProperties), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AutonomousDatabaseBackupProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseBackupProperties), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AutonomousDatabaseBackupProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseBackupProperties), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.OracleDatabase.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1)

## Assembly

Google.Cloud.OracleDatabase.V1.dll

## Constructors 

### AutonomousDatabaseBackupProperties()
    
    
    public AutonomousDatabaseBackupProperties()

### AutonomousDatabaseBackupProperties(AutonomousDatabaseBackupProperties)
    
    
    public AutonomousDatabaseBackupProperties(AutonomousDatabaseBackupProperties other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AutonomousDatabaseBackupProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseBackupProperties)`  
  
  
## Properties 

### AvailableTillTime
    
    
    public Timestamp AvailableTillTime { get; set; }

Output only. Timestamp until when the backup will be available.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### CompartmentId
    
    
    public string CompartmentId { get; set; }

Output only. The OCID of the compartment.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DatabaseSizeTb
    
    
    public float DatabaseSizeTb { get; set; }

Output only. The quantity of data in the database, in terabytes.

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### DbVersion
    
    
    public string DbVersion { get; set; }

Output only. A valid Oracle Database version for Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EndTime
    
    
    public Timestamp EndTime { get; set; }

Output only. The date and time the backup completed.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### IsAutomaticBackup
    
    
    public bool IsAutomaticBackup { get; set; }

Output only. Indicates if the backup is automatic or user initiated.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### IsLongTermBackup
    
    
    public bool IsLongTermBackup { get; set; }

Output only. Indicates if the backup is long term backup.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### IsRestorable
    
    
    public bool IsRestorable { get; set; }

Output only. Indicates if the backup can be used to restore the Autonomous Database.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### KeyStoreId
    
    
    public string KeyStoreId { get; set; }

Optional. The OCID of the key store of Oracle Vault.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### KeyStoreWallet
    
    
    public string KeyStoreWallet { get; set; }

Optional. The wallet name for Oracle Key Vault.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### KmsKeyId
    
    
    public string KmsKeyId { get; set; }

Optional. The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### KmsKeyVersionId
    
    
    public string KmsKeyVersionId { get; set; }

Optional. The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation. Autonomous Database Serverless does not use key versions, hence is not applicable for Autonomous Database Serverless instances.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### LifecycleDetails
    
    
    public string LifecycleDetails { get; set; }

Output only. Additional information about the current lifecycle state.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### LifecycleState
    
    
    public AutonomousDatabaseBackupProperties.Types.State LifecycleState { get; set; }

Output only. The lifecycle state of the backup.

**Property Value**  
---  
**Type** | **Description**  
`[AutonomousDatabaseBackupProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseBackupProperties)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseBackupProperties.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseBackupProperties.Types.State)` |   
  
### Ocid
    
    
    public string Ocid { get; set; }

Output only. OCID of the Autonomous Database backup. <https://docs.oracle.com/en-us/iaas/Content/General/Concepts/identifiers.htm#Oracle>

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RetentionPeriodDays
    
    
    public int RetentionPeriodDays { get; set; }

Optional. Retention period in days for the backup.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### SizeTb
    
    
    public float SizeTb { get; set; }

Output only. The backup size in terabytes.

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### StartTime
    
    
    public Timestamp StartTime { get; set; }

Output only. The date and time the backup started.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Type
    
    
    public AutonomousDatabaseBackupProperties.Types.Type Type { get; set; }

Output only. The type of the backup.

**Property Value**  
---  
**Type** | **Description**  
`[AutonomousDatabaseBackupProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseBackupProperties)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseBackupProperties.Types)[Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseBackupProperties.Types.Type)` |   
  
### VaultId
    
    
    public string VaultId { get; set; }

Optional. The OCID of the vault.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
