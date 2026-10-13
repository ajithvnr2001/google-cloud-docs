---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.MaintenanceInfo
title: Database Center v1beta API - Class MaintenanceInfo (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:56.632964+00:00
---

# Database Center v1beta API - Class MaintenanceInfo (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.MaintenanceInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Database Center v1beta API - Class MaintenanceInfo (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta08 (latest)  1.0.0-beta07 
    
    
    public sealed class MaintenanceInfo : IMessage<MaintenanceInfo>, IEquatable<MaintenanceInfo>, IDeepCloneable<MaintenanceInfo>, IBufferMessage, IMessage

Reference documentation and code samples for the Database Center v1beta API class MaintenanceInfo.

MaintenanceInfo to capture the maintenance details of database resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > MaintenanceInfo

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[MaintenanceInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.MaintenanceInfo), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[MaintenanceInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.MaintenanceInfo), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[MaintenanceInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.MaintenanceInfo), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DatabaseCenter.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta)

## Assembly

Google.Cloud.DatabaseCenter.V1Beta.dll

## Constructors 

### MaintenanceInfo()
    
    
    public MaintenanceInfo()

### MaintenanceInfo(MaintenanceInfo)
    
    
    public MaintenanceInfo(MaintenanceInfo other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[MaintenanceInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.MaintenanceInfo)`  
  
  
## Properties 

### CurrentVersionReleaseDate
    
    
    public Date CurrentVersionReleaseDate { get; set; }

Output only. The date when the maintenance version was released.

**Property Value**  
---  
**Type** | **Description**  
`[Date](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date.html)` |   
  
### DenyMaintenanceSchedules
    
    
    public RepeatedField<ResourceMaintenanceDenySchedule> DenyMaintenanceSchedules { get; }

Optional. List of Deny maintenance period for the database resource.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[ResourceMaintenanceDenySchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.ResourceMaintenanceDenySchedule)` |   
  
### MaintenanceSchedule
    
    
    public ResourceMaintenanceSchedule MaintenanceSchedule { get; set; }

Optional. Maintenance window for the database resource.

**Property Value**  
---  
**Type** | **Description**  
`[ResourceMaintenanceSchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.ResourceMaintenanceSchedule)` |   
  
### MaintenanceVersion
    
    
    public string MaintenanceVersion { get; set; }

Output only. Current Maintenance version of the database resource. Example: "MYSQL_8_0_41.R20250531.01_15"

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PossibleFailureReasons
    
    
    public RepeatedField<PossibleFailureReason> PossibleFailureReasons { get; }

Output only. List of possible reasons why the maintenance is not completed. This is an optional field and is only populated if there are any reasons for failures recorded for the maintenance by DB Center. FAILURE maintenance status may not always have a failure reason.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[PossibleFailureReason](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.PossibleFailureReason)` |   
  
### PreviousMaintenanceVersion
    
    
    public string PreviousMaintenanceVersion { get; set; }

Output only. Previous maintenance version of the database resource. Example: "MYSQL_8_0_41.R20250531.01_15". This is available once a minor version maintenance is complete on a database resource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### State
    
    
    public MaintenanceState State { get; set; }

Output only. Resource maintenance state. This is to capture the current state of the maintenance.

**Property Value**  
---  
**Type** | **Description**  
`[MaintenanceState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.MaintenanceState)` |   
  
### UpcomingMaintenance
    
    
    public UpcomingMaintenance UpcomingMaintenance { get; set; }

Output only. Upcoming maintenance window for the database resource. This is only populated for an engine, if upcoming maintenance is scheduled for the resource. This schedule is generated per engine and engine version, and there is only one upcoming maintenance window at any given time. In case of upcoming maintenance, the maintenance_state will be set to SCHEDULED first, and then IN_PROGRESS when the maintenance window starts.

**Property Value**  
---  
**Type** | **Description**  
`[UpcomingMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.UpcomingMaintenance)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
