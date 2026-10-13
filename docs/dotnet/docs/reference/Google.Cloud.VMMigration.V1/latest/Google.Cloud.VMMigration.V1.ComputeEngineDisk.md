---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.ComputeEngineDisk
title: VM Migration v1 API - Class ComputeEngineDisk (2.9.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:40.829659+00:00
---

# VM Migration v1 API - Class ComputeEngineDisk (2.9.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.ComputeEngineDisk

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  VM Migration v1 API - Class ComputeEngineDisk (2.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.9.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.ComputeEngineDisk)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.8.0/Google.Cloud.VMMigration.V1.ComputeEngineDisk)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.7.0/Google.Cloud.VMMigration.V1.ComputeEngineDisk)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.6.0/Google.Cloud.VMMigration.V1.ComputeEngineDisk)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.5.0/Google.Cloud.VMMigration.V1.ComputeEngineDisk)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.4.0/Google.Cloud.VMMigration.V1.ComputeEngineDisk)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.3.0/Google.Cloud.VMMigration.V1.ComputeEngineDisk)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.2.0/Google.Cloud.VMMigration.V1.ComputeEngineDisk)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.1.0/Google.Cloud.VMMigration.V1.ComputeEngineDisk)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.0.0/Google.Cloud.VMMigration.V1.ComputeEngineDisk)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/1.0.0/Google.Cloud.VMMigration.V1.ComputeEngineDisk)


    
    
    public sealed class ComputeEngineDisk : IMessage<ComputeEngineDisk>, IEquatable<ComputeEngineDisk>, IDeepCloneable<ComputeEngineDisk>, IBufferMessage, IMessage

Reference documentation and code samples for the VM Migration v1 API class ComputeEngineDisk.

Compute Engine disk target details.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ComputeEngineDisk

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ComputeEngineDisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.ComputeEngineDisk), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ComputeEngineDisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.ComputeEngineDisk), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ComputeEngineDisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.ComputeEngineDisk), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.VMMigration.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1)

## Assembly

Google.Cloud.VMMigration.V1.dll

## Constructors 

### ComputeEngineDisk()
    
    
    public ComputeEngineDisk()

### ComputeEngineDisk(ComputeEngineDisk)
    
    
    public ComputeEngineDisk(ComputeEngineDisk other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ComputeEngineDisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.ComputeEngineDisk)`  
  
  
## Properties 

### DiskId
    
    
    public string DiskId { get; set; }

Optional. Target Compute Engine Disk ID. This is the resource ID segment of the Compute Engine Disk to create. In the resource name compute/v1/projects/{project}/zones/{zone}/disks/disk1 "disk1" is the resource ID for the disk.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DiskType
    
    
    public ComputeEngineDiskType DiskType { get; set; }

Required. The disk type to use.

**Property Value**  
---  
**Type** | **Description**  
`[ComputeEngineDiskType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.ComputeEngineDiskType)` |   
  
### ReplicaZones
    
    
    public RepeatedField<string> ReplicaZones { get; }

Optional. Replication zones of the regional disk. Should be of the form: projects/{target-project}/locations/{replica-zone} Currently only one replica zone is supported.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ReplicaZonesAsLocationNames
    
    
    public ResourceNameList<LocationName> ReplicaZonesAsLocationNames { get; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [ReplicaZones](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.ComputeEngineDisk#Google_Cloud_VMMigration_V1_ComputeEngineDisk_ReplicaZones) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ResourceNameList](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNameList-1.html)[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
### Zone
    
    
    public string Zone { get; set; }

Required. The Compute Engine zone in which to create the disk. Should be of the form: projects/{target-project}/locations/{zone}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ZoneAsLocationName
    
    
    public LocationName ZoneAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Zone](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.ComputeEngineDisk#Google_Cloud_VMMigration_V1_ComputeEngineDisk_Zone) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
