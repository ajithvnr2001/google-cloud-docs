---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AttachedDisk
title: Compute Engine v1 API - Class AttachedDisk (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:26:17.730896+00:00
---

# Compute Engine v1 API - Class AttachedDisk (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AttachedDisk

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class AttachedDisk (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class AttachedDisk : IMessage<AttachedDisk>, IEquatable<AttachedDisk>, IDeepCloneable<AttachedDisk>, IBufferMessage, IMessage

Reference documentation and code samples for the Compute Engine v1 API class AttachedDisk.

An instance-attached disk resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AttachedDisk

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AttachedDisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AttachedDisk), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AttachedDisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AttachedDisk), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AttachedDisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AttachedDisk), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Constructors 

### AttachedDisk()
    
    
    public AttachedDisk()

### AttachedDisk(AttachedDisk)
    
    
    public AttachedDisk(AttachedDisk other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AttachedDisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AttachedDisk)`  
  
  
## Properties 

### Architecture
    
    
    public string Architecture { get; set; }

Output only. [Output Only] The architecture of the attached disk. Valid values are ARM64 or X86_64. Check the Architecture enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AutoDelete
    
    
    public bool AutoDelete { get; set; }

Specifies whether the disk will be auto-deleted when the instance is deleted (but not when the disk is detached from the instance).

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Boot
    
    
    public bool Boot { get; set; }

Indicates that this is a boot disk. The virtual machine will use the first partition of the disk for its root filesystem.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### DeviceName
    
    
    public string DeviceName { get; set; }

Specifies a unique device name of your choice that is reflected into the/dev/disk/by-id/google-* tree of a Linux operating system running within the instance. This name can be used to reference the device for mounting, resizing, and so on, from within the instance.

If not specified, the server chooses a default device name to apply to this disk, in the form persistent-disk-x, where x is a number assigned by Google Compute Engine. This field is only applicable for persistent disks.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DiskEncryptionKey
    
    
    public CustomerEncryptionKey DiskEncryptionKey { get; set; }

Encrypts or decrypts a disk using acustomer-supplied encryption key.

If you are creating a new disk, this field encrypts the new disk using an encryption key that you provide. If you are attaching an existing disk that is already encrypted, this field decrypts the disk using the customer-supplied encryption key.

If you encrypt a disk using a customer-supplied key, you must provide the same key again when you attempt to use this resource at a later time. For example, you must provide the key when you create a snapshot or an image from the disk or when you attach the disk to a virtual machine instance.

If you do not provide an encryption key, then the disk will be encrypted using an automatically generated key and you do not need to provide a key to use the disk later.

Note:

Instance templates do not storecustomer-supplied encryption keys, so you cannot use your own keys to encrypt disks in amanaged instance group.

You cannot create VMs that have disks with customer-supplied keys using the bulk insert method.

**Property Value**  
---  
**Type** | **Description**  
`[CustomerEncryptionKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CustomerEncryptionKey)` |   
  
### DiskSizeGb
    
    
    public long DiskSizeGb { get; set; }

The size of the disk in GB.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### ForceAttach
    
    
    public bool ForceAttach { get; set; }

[Input Only] Whether to force attach the regional disk even if it's currently attached to another instance. If you try to force attach a zonal disk to an instance, you will receive an error.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### GuestOsFeatures
    
    
    public RepeatedField<GuestOsFeature> GuestOsFeatures { get; }

A list of features to enable on the guest operating system. Applicable only for bootable images. Read Enabling guest operating system features to see a list of available options.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[GuestOsFeature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GuestOsFeature)` |   
  
### HasArchitecture
    
    
    public bool HasArchitecture { get; }

Gets whether the "architecture" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasAutoDelete
    
    
    public bool HasAutoDelete { get; }

Gets whether the "auto_delete" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasBoot
    
    
    public bool HasBoot { get; }

Gets whether the "boot" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasDeviceName
    
    
    public bool HasDeviceName { get; }

Gets whether the "device_name" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasDiskSizeGb
    
    
    public bool HasDiskSizeGb { get; }

Gets whether the "disk_size_gb" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasForceAttach
    
    
    public bool HasForceAttach { get; }

Gets whether the "force_attach" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasIndex
    
    
    public bool HasIndex { get; }

Gets whether the "index" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasInterface
    
    
    public bool HasInterface { get; }

Gets whether the "interface" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasKind
    
    
    public bool HasKind { get; }

Gets whether the "kind" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMode
    
    
    public bool HasMode { get; }

Gets whether the "mode" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSavedState
    
    
    public bool HasSavedState { get; }

Gets whether the "saved_state" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSource
    
    
    public bool HasSource { get; }

Gets whether the "source" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasType
    
    
    public bool HasType { get; }

Gets whether the "type" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Index
    
    
    public int Index { get; set; }

Output only. [Output Only] A zero-based index to this disk, where 0 is reserved for the boot disk. If you have many disks attached to an instance, each disk would have a unique index number.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### InitializeParams
    
    
    public AttachedDiskInitializeParams InitializeParams { get; set; }

[Input Only] Specifies the parameters for a new disk that will be created alongside the new instance. Use initialization parameters to create boot disks or local SSDs attached to the new instance.

This property is mutually exclusive with the source property; you can only define one or the other, but not both.

**Property Value**  
---  
**Type** | **Description**  
`[AttachedDiskInitializeParams](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AttachedDiskInitializeParams)` |   
  
### Interface
    
    
    public string Interface { get; set; }

Specifies the disk interface to use for attaching this disk, which is either SCSI or NVME. For most machine types, the default is SCSI. Local SSDs can use either NVME or SCSI. In certain configurations, persistent disks can use NVMe. For more information, seeAbout persistent disks. Check the Interface enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Kind
    
    
    public string Kind { get; set; }

Output only. [Output Only] Type of the resource. Alwayscompute#attachedDisk for attached disks.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Licenses
    
    
    public RepeatedField<string> Licenses { get; }

Output only. [Output Only] Any valid publicly visible licenses.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Mode
    
    
    public string Mode { get; set; }

The mode in which to attach this disk, either READ_WRITE orREAD_ONLY. If not specified, the default is to attach the disk in READ_WRITE mode. Check the Mode enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SavedState
    
    
    public string SavedState { get; set; }

Output only. For LocalSSD disks on VM Instances in STOPPED or SUSPENDED state, this field is set to PRESERVED if the LocalSSD data has been saved to a persistent location by customer request. (see the discard_local_ssd option on Stop/Suspend). Read-only in the api. Check the SavedState enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ShieldedInstanceInitialState
    
    
    public InitialStateConfig ShieldedInstanceInitialState { get; set; }

Output only. [Output Only] shielded vm initial state stored on disk

**Property Value**  
---  
**Type** | **Description**  
`[InitialStateConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InitialStateConfig)` |   
  
### Source
    
    
    public string Source { get; set; }

Specifies a valid partial or full URL to an existing Persistent Disk resource. When creating a new instance boot disk, one ofinitializeParams.sourceImage orinitializeParams.sourceSnapshot or disks.source is required.

If desired, you can also attach existing non-root persistent disks using this property. This field is only applicable for persistent disks.

Note that for InstanceTemplate, specify the disk name for zonal disk, and the URL for regional disk.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public string Type { get; set; }

Specifies the type of the disk, either SCRATCH orPERSISTENT. If not specified, the default isPERSISTENT. Check the Type enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
