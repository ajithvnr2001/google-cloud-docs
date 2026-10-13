---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GroupMaintenanceInfo
title: Compute Engine v1 API - Class GroupMaintenanceInfo (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:54:55.365461+00:00
---

# Compute Engine v1 API - Class GroupMaintenanceInfo (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GroupMaintenanceInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class GroupMaintenanceInfo (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class GroupMaintenanceInfo : IMessage<GroupMaintenanceInfo>, IEquatable<GroupMaintenanceInfo>, IDeepCloneable<GroupMaintenanceInfo>, IBufferMessage, IMessage

Reference documentation and code samples for the Compute Engine v1 API class GroupMaintenanceInfo.

Maintenance Info for ReservationBlocks.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GroupMaintenanceInfo

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GroupMaintenanceInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GroupMaintenanceInfo), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GroupMaintenanceInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GroupMaintenanceInfo), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GroupMaintenanceInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GroupMaintenanceInfo), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Constructors 

### GroupMaintenanceInfo()
    
    
    public GroupMaintenanceInfo()

### GroupMaintenanceInfo(GroupMaintenanceInfo)
    
    
    public GroupMaintenanceInfo(GroupMaintenanceInfo other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GroupMaintenanceInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GroupMaintenanceInfo)`  
  
  
## Properties 

### HasInstanceMaintenanceOngoingCount
    
    
    public bool HasInstanceMaintenanceOngoingCount { get; }

Gets whether the "instance_maintenance_ongoing_count" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasInstanceMaintenancePendingCount
    
    
    public bool HasInstanceMaintenancePendingCount { get; }

Gets whether the "instance_maintenance_pending_count" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMaintenanceOngoingCount
    
    
    public bool HasMaintenanceOngoingCount { get; }

Gets whether the "maintenance_ongoing_count" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMaintenancePendingCount
    
    
    public bool HasMaintenancePendingCount { get; }

Gets whether the "maintenance_pending_count" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSchedulingType
    
    
    public bool HasSchedulingType { get; }

Gets whether the "scheduling_type" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSubblockInfraMaintenanceOngoingCount
    
    
    public bool HasSubblockInfraMaintenanceOngoingCount { get; }

Gets whether the "subblock_infra_maintenance_ongoing_count" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSubblockInfraMaintenancePendingCount
    
    
    public bool HasSubblockInfraMaintenancePendingCount { get; }

Gets whether the "subblock_infra_maintenance_pending_count" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### InstanceMaintenanceOngoingCount
    
    
    public int InstanceMaintenanceOngoingCount { get; set; }

Describes number of instances that have ongoing maintenance.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### InstanceMaintenancePendingCount
    
    
    public int InstanceMaintenancePendingCount { get; set; }

Describes number of instances that have pending maintenance.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### MaintenanceOngoingCount
    
    
    public int MaintenanceOngoingCount { get; set; }

Progress for ongoing maintenance for this group of VMs/hosts. Describes number of hosts in the block that have ongoing maintenance.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### MaintenancePendingCount
    
    
    public int MaintenancePendingCount { get; set; }

Progress for ongoing maintenance for this group of VMs/hosts. Describes number of hosts in the block that have pending maintenance.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### SchedulingType
    
    
    public string SchedulingType { get; set; }

The type of maintenance for the reservation. Check the SchedulingType enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SubblockInfraMaintenanceOngoingCount
    
    
    public int SubblockInfraMaintenanceOngoingCount { get; set; }

Describes number of subblock Infrastructure that has ongoing maintenance. Here, Subblock Infrastructure Maintenance pertains to upstream hardware contained in the Subblock that is necessary for a VM Family(e.g. NVLink Domains). Not all VM Families will support this field.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### SubblockInfraMaintenancePendingCount
    
    
    public int SubblockInfraMaintenancePendingCount { get; set; }

Describes number of subblock Infrastructure that has pending maintenance. Here, Subblock Infrastructure Maintenance pertains to upstream hardware contained in the Subblock that is necessary for a VM Family (e.g. NVLink Domains). Not all VM Families will support this field.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### UpcomingGroupMaintenance
    
    
    public UpcomingMaintenance UpcomingGroupMaintenance { get; set; }

Maintenance information on this group of VMs.

**Property Value**  
---  
**Type** | **Description**  
`[UpcomingMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.UpcomingMaintenance)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
