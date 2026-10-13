---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy
title: AlloyDB v1beta API - Class AutomatedBackupPolicy (1.0.0-beta19) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:09:08.041463+00:00
---

# AlloyDB v1beta API - Class AutomatedBackupPolicy (1.0.0-beta19)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  AlloyDB v1beta API - Class AutomatedBackupPolicy (1.0.0-beta19) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta19 (latest)  1.0.0-beta18 
    
    
    public sealed class AutomatedBackupPolicy : IMessage<AutomatedBackupPolicy>, IEquatable<AutomatedBackupPolicy>, IDeepCloneable<AutomatedBackupPolicy>, IBufferMessage, IMessage

Reference documentation and code samples for the AlloyDB v1beta API class AutomatedBackupPolicy.

Message describing the user-specified automated backup policy.

All fields in the automated backup policy are optional. Defaults for each field are provided if they are not set.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AutomatedBackupPolicy

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AutomatedBackupPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AutomatedBackupPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AutomatedBackupPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AlloyDb.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta)

## Assembly

Google.Cloud.AlloyDb.V1Beta.dll

## Constructors 

### AutomatedBackupPolicy()
    
    
    public AutomatedBackupPolicy()

### AutomatedBackupPolicy(AutomatedBackupPolicy)
    
    
    public AutomatedBackupPolicy(AutomatedBackupPolicy other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AutomatedBackupPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy)`  
  
  
## Properties 

### BackupWindow
    
    
    public Duration BackupWindow { get; set; }

The length of the time window during which a backup can be taken. If a backup does not succeed within this time window, it will be canceled and considered failed.

The backup window must be at least 5 minutes long. There is no upper bound on the window. If not set, it defaults to 1 hour.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### Enabled
    
    
    public bool Enabled { get; set; }

Whether automated automated backups are enabled. If not set, defaults to true.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### EncryptionConfig
    
    
    public EncryptionConfig EncryptionConfig { get; set; }

Optional. The encryption config can be specified to encrypt the backups with a customer-managed encryption key (CMEK). When this field is not specified, the backup will use the cluster's encryption config.

**Property Value**  
---  
**Type** | **Description**  
`[EncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.EncryptionConfig)` |   
  
### HasEnabled
    
    
    public bool HasEnabled { get; }

Gets whether the "enabled" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

Labels to apply to backups created using this configuration.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Location
    
    
    public string Location { get; set; }

The location where the backup will be stored. Currently, the only supported option is to store the backup in the same region as the cluster.

If empty, defaults to the region of the cluster.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### QuantityBasedRetention
    
    
    public AutomatedBackupPolicy.Types.QuantityBasedRetention QuantityBasedRetention { get; set; }

Quantity-based Backup retention policy to retain recent backups.

**Property Value**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy.Types)[QuantityBasedRetention](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy.Types.QuantityBasedRetention)` |   
  
### RetentionCase
    
    
    public AutomatedBackupPolicy.RetentionOneofCase RetentionCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy)[RetentionOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy.RetentionOneofCase)` |   
  
### ScheduleCase
    
    
    public AutomatedBackupPolicy.ScheduleOneofCase ScheduleCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy)[ScheduleOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy.ScheduleOneofCase)` |   
  
### TimeBasedRetention
    
    
    public AutomatedBackupPolicy.Types.TimeBasedRetention TimeBasedRetention { get; set; }

Time-based Backup retention policy.

**Property Value**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy.Types)[TimeBasedRetention](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy.Types.TimeBasedRetention)` |   
  
### WeeklySchedule
    
    
    public AutomatedBackupPolicy.Types.WeeklySchedule WeeklySchedule { get; set; }

Weekly schedule for the Backup.

**Property Value**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy.Types)[WeeklySchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy.Types.WeeklySchedule)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
