---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.BackupPlan.Types.Schedule
title: Backup for GKE v1 API - Class BackupPlan.Types.Schedule (2.9.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:23:18.515471+00:00
---

# Backup for GKE v1 API - Class BackupPlan.Types.Schedule (2.9.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.BackupPlan.Types.Schedule

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Backup for GKE v1 API - Class BackupPlan.Types.Schedule (2.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.9.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.BackupPlan.Types.Schedule)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.8.0/Google.Cloud.GkeBackup.V1.BackupPlan.Types.Schedule)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.7.0/Google.Cloud.GkeBackup.V1.BackupPlan.Types.Schedule)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.6.0/Google.Cloud.GkeBackup.V1.BackupPlan.Types.Schedule)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.5.0/Google.Cloud.GkeBackup.V1.BackupPlan.Types.Schedule)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.4.0/Google.Cloud.GkeBackup.V1.BackupPlan.Types.Schedule)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.3.0/Google.Cloud.GkeBackup.V1.BackupPlan.Types.Schedule)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.2.0/Google.Cloud.GkeBackup.V1.BackupPlan.Types.Schedule)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.1.0/Google.Cloud.GkeBackup.V1.BackupPlan.Types.Schedule)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.0.0/Google.Cloud.GkeBackup.V1.BackupPlan.Types.Schedule)
  * [ 1.0.0-beta01 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/1.0.0-beta01/Google.Cloud.GkeBackup.V1.BackupPlan.Types.Schedule)


    
    
    public sealed class BackupPlan.Types.Schedule : IMessage<BackupPlan.Types.Schedule>, IEquatable<BackupPlan.Types.Schedule>, IDeepCloneable<BackupPlan.Types.Schedule>, IBufferMessage, IMessage

Reference documentation and code samples for the Backup for GKE v1 API class BackupPlan.Types.Schedule.

Defines scheduling parameters for automatically creating Backups via this BackupPlan.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BackupPlan.Types.Schedule

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BackupPlan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.BackupPlan)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.BackupPlan.Types)[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.BackupPlan.Types.Schedule), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BackupPlan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.BackupPlan)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.BackupPlan.Types)[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.BackupPlan.Types.Schedule), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BackupPlan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.BackupPlan)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.BackupPlan.Types)[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.BackupPlan.Types.Schedule), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.GkeBackup.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1)

## Assembly

Google.Cloud.GkeBackup.V1.dll

## Constructors 

### Schedule()
    
    
    public Schedule()

### Schedule(Schedule)
    
    
    public Schedule(BackupPlan.Types.Schedule other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BackupPlan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.BackupPlan)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.BackupPlan.Types)[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.BackupPlan.Types.Schedule)`  
  
  
## Properties 

### CronSchedule
    
    
    public string CronSchedule { get; set; }

Optional. A standard [cron](https://wikipedia.com/wiki/cron) string that defines a repeating schedule for creating Backups via this BackupPlan. This is mutually exclusive with the [rpo_config][google.cloud.gkebackup.v1.BackupPlan.Schedule.rpo_config] field since at most one schedule can be defined for a BackupPlan. If this is defined, then [backup_retain_days][google.cloud.gkebackup.v1.BackupPlan.RetentionPolicy.backup_retain_days] must also be defined.

Default (empty): no automatic backup creation will occur.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NextScheduledBackupTime
    
    
    public Timestamp NextScheduledBackupTime { get; set; }

Output only. Start time of next scheduled backup under this BackupPlan by either cron_schedule or rpo config.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Paused
    
    
    public bool Paused { get; set; }

Optional. This flag denotes whether automatic Backup creation is paused for this BackupPlan.

Default: False

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### RpoConfig
    
    
    public RpoConfig RpoConfig { get; set; }

Optional. Defines the RPO schedule configuration for this BackupPlan. This is mutually exclusive with the [cron_schedule][google.cloud.gkebackup.v1.BackupPlan.Schedule.cron_schedule] field since at most one schedule can be defined for a BackupPLan. If this is defined, then [backup_retain_days][google.cloud.gkebackup.v1.BackupPlan.RetentionPolicy.backup_retain_days] must also be defined.

Default (empty): no automatic backup creation will occur.

**Property Value**  
---  
**Type** | **Description**  
`[RpoConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.RpoConfig)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
