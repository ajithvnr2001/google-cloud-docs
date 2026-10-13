---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AdditionalDetail
title: Database Center v1beta API - Class AdditionalDetail (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:49.635037+00:00
---

# Database Center v1beta API - Class AdditionalDetail (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AdditionalDetail

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Database Center v1beta API - Class AdditionalDetail (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta08 (latest)  1.0.0-beta07 
    
    
    public sealed class AdditionalDetail : IMessage<AdditionalDetail>, IEquatable<AdditionalDetail>, IDeepCloneable<AdditionalDetail>, IBufferMessage, IMessage

Reference documentation and code samples for the Database Center v1beta API class AdditionalDetail.

Details related to signal.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AdditionalDetail

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AdditionalDetail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AdditionalDetail), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AdditionalDetail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AdditionalDetail), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AdditionalDetail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AdditionalDetail), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DatabaseCenter.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta)

## Assembly

Google.Cloud.DatabaseCenter.V1Beta.dll

## Constructors 

### AdditionalDetail()
    
    
    public AdditionalDetail()

### AdditionalDetail(AdditionalDetail)
    
    
    public AdditionalDetail(AdditionalDetail other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AdditionalDetail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AdditionalDetail)`  
  
  
## Properties 

### AutomatedBackupPolicyInfo
    
    
    public AutomatedBackupPolicyInfo AutomatedBackupPolicyInfo { get; set; }

Automated backup policy information applies to signals with type SIGNAL_TYPE_NO_AUTOMATED_BACKUP_POLICY.

**Property Value**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicyInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AutomatedBackupPolicyInfo)` |   
  
### BackupRunInfo
    
    
    public BackupRunInfo BackupRunInfo { get; set; }

Backup run information applies to signals with types SIGNAL_TYPE_LAST_BACKUP_FAILED and SIGNAL_TYPE_LAST_BACKUP_OLD.

**Property Value**  
---  
**Type** | **Description**  
`[BackupRunInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.BackupRunInfo)` |   
  
### DeletionProtectionInfo
    
    
    public DeletionProtectionInfo DeletionProtectionInfo { get; set; }

Deletion protection information applies to signals with type [SIGNAL_TYPE_NO_DELETION_PROTECTION][google.cloud.databasecenter.v1beta.SignalType.SIGNAL_TYPE_NO_DELETION_PROTECTION]

**Property Value**  
---  
**Type** | **Description**  
`[DeletionProtectionInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DeletionProtectionInfo)` |   
  
### DetailCase
    
    
    public AdditionalDetail.DetailOneofCase DetailCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[AdditionalDetail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AdditionalDetail)[DetailOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AdditionalDetail.DetailOneofCase)` |   
  
### InefficientQueryInfo
    
    
    public InefficientQueryInfo InefficientQueryInfo { get; set; }

Inefficient query information applies to signals with type [SIGNAL_TYPE_INEFFICIENT_QUERY][google.cloud.databasecenter.v1beta.SignalType.SIGNAL_TYPE_INEFFICIENT_QUERY].

**Property Value**  
---  
**Type** | **Description**  
`[InefficientQueryInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.InefficientQueryInfo)` |   
  
### MaintenanceRecommendationInfo
    
    
    public MaintenanceRecommendationInfo MaintenanceRecommendationInfo { get; set; }

Maintenance recommendation information applies to signals with type SIGNAL_TYPE_RECOMMENDED_MAINTENANCE_POLICIES.

**Property Value**  
---  
**Type** | **Description**  
`[MaintenanceRecommendationInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.MaintenanceRecommendationInfo)` |   
  
### OutdatedMinorVersionInfo
    
    
    public OutdatedMinorVersionInfo OutdatedMinorVersionInfo { get; set; }

Outdated minor version information applies to signals with type SIGNAL_TYPE_OUTDATED_MINOR_VERSION.

**Property Value**  
---  
**Type** | **Description**  
`[OutdatedMinorVersionInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.OutdatedMinorVersionInfo)` |   
  
### RecommendationInfo
    
    
    public RecommendationInfo RecommendationInfo { get; set; }

Recommendation information applies to recommendations.

**Property Value**  
---  
**Type** | **Description**  
`[RecommendationInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.RecommendationInfo)` |   
  
### ResourceSuspensionInfo
    
    
    public ResourceSuspensionInfo ResourceSuspensionInfo { get; set; }

Resource suspension information applies to signals with type [SIGNAL_TYPE_RESOURCE_SUSPENDED][google.cloud.databasecenter.v1beta.SignalType.SIGNAL_TYPE_RESOURCE_SUSPENDED].

**Property Value**  
---  
**Type** | **Description**  
`[ResourceSuspensionInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.ResourceSuspensionInfo)` |   
  
### SccInfo
    
    
    public SCCInfo SccInfo { get; set; }

SCC information applies to SCC signals.

**Property Value**  
---  
**Type** | **Description**  
`[SCCInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.SCCInfo)` |   
  
### ShortBackupRetentionInfo
    
    
    public RetentionSettingsInfo ShortBackupRetentionInfo { get; set; }

Short backup retention information applies to signals with type SIGNAL_TYPE_SHORT_BACKUP_RETENTION.

**Property Value**  
---  
**Type** | **Description**  
`[RetentionSettingsInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.RetentionSettingsInfo)` |   
  
### SignalEventTime
    
    
    public Timestamp SignalEventTime { get; set; }

Event time when signal was recorded by source service.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### SignalSource
    
    
    public SignalSource SignalSource { get; set; }

Where the signal is coming from.

**Property Value**  
---  
**Type** | **Description**  
`[SignalSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.SignalSource)` |   
  
### SignalType
    
    
    public SignalType SignalType { get; set; }

Type of the signal.

**Property Value**  
---  
**Type** | **Description**  
`[SignalType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.SignalType)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
