---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.BootDiskDefaults
title: VM Migration v1 API - Class BootDiskDefaults (2.9.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:21:29.628403+00:00
---

# VM Migration v1 API - Class BootDiskDefaults (2.9.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.BootDiskDefaults

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  VM Migration v1 API - Class BootDiskDefaults (2.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.9.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.BootDiskDefaults)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.8.0/Google.Cloud.VMMigration.V1.BootDiskDefaults)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.7.0/Google.Cloud.VMMigration.V1.BootDiskDefaults)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.6.0/Google.Cloud.VMMigration.V1.BootDiskDefaults)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.5.0/Google.Cloud.VMMigration.V1.BootDiskDefaults)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.4.0/Google.Cloud.VMMigration.V1.BootDiskDefaults)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.3.0/Google.Cloud.VMMigration.V1.BootDiskDefaults)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.2.0/Google.Cloud.VMMigration.V1.BootDiskDefaults)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.1.0/Google.Cloud.VMMigration.V1.BootDiskDefaults)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/2.0.0/Google.Cloud.VMMigration.V1.BootDiskDefaults)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/1.0.0/Google.Cloud.VMMigration.V1.BootDiskDefaults)


    
    
    public sealed class BootDiskDefaults : IMessage<BootDiskDefaults>, IEquatable<BootDiskDefaults>, IDeepCloneable<BootDiskDefaults>, IBufferMessage, IMessage

Reference documentation and code samples for the VM Migration v1 API class BootDiskDefaults.

BootDiskDefaults hold information about the boot disk of a VM.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BootDiskDefaults

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BootDiskDefaults](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.BootDiskDefaults), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BootDiskDefaults](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.BootDiskDefaults), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BootDiskDefaults](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.BootDiskDefaults), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.VMMigration.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1)

## Assembly

Google.Cloud.VMMigration.V1.dll

## Constructors 

### BootDiskDefaults()
    
    
    public BootDiskDefaults()

### BootDiskDefaults(BootDiskDefaults)
    
    
    public BootDiskDefaults(BootDiskDefaults other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BootDiskDefaults](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.BootDiskDefaults)`  
  
  
## Properties 

### DeviceName
    
    
    public string DeviceName { get; set; }

Optional. Specifies a unique device name of your choice that is reflected into the /dev/disk/by-id/google-* tree of a Linux operating system running within the instance. If not specified, the server chooses a default device name to apply to this disk, in the form persistent-disk-x, where x is a number assigned by Google Compute Engine. This field is only applicable for persistent disks.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DiskName
    
    
    public string DiskName { get; set; }

Optional. The name of the disk.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DiskType
    
    
    public ComputeEngineDiskType DiskType { get; set; }

Optional. The type of disk provisioning to use for the VM.

**Property Value**  
---  
**Type** | **Description**  
`[ComputeEngineDiskType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.ComputeEngineDiskType)` |   
  
### Encryption
    
    
    public Encryption Encryption { get; set; }

Optional. The encryption to apply to the boot disk.

**Property Value**  
---  
**Type** | **Description**  
`[Encryption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.Encryption)` |   
  
### Image
    
    
    public BootDiskDefaults.Types.DiskImageDefaults Image { get; set; }

The image to use when creating the disk.

**Property Value**  
---  
**Type** | **Description**  
`[BootDiskDefaults](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.BootDiskDefaults)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.BootDiskDefaults.Types)[DiskImageDefaults](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.BootDiskDefaults.Types.DiskImageDefaults)` |   
  
### SourceCase
    
    
    public BootDiskDefaults.SourceOneofCase SourceCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[BootDiskDefaults](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.BootDiskDefaults)[SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VMMigration.V1/latest/Google.Cloud.VMMigration.V1.BootDiskDefaults.SourceOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
