---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.MachineImage
title: Compute Engine v1 API - Class MachineImage (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:45:03.481668+00:00
---

# Compute Engine v1 API - Class MachineImage (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.MachineImage

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class MachineImage (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class MachineImage : IMessage<MachineImage>, IEquatable<MachineImage>, IDeepCloneable<MachineImage>, IBufferMessage, IMessage

Reference documentation and code samples for the Compute Engine v1 API class MachineImage.

Represents a machine image resource.

A machine image is a Compute Engine resource that stores all the configuration, metadata, permissions, and data from one or more disks required to create a Virtual machine (VM) instance. For more information, seeMachine images.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > MachineImage

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[MachineImage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.MachineImage), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[MachineImage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.MachineImage), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[MachineImage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.MachineImage), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Constructors 

### MachineImage()
    
    
    public MachineImage()

### MachineImage(MachineImage)
    
    
    public MachineImage(MachineImage other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[MachineImage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.MachineImage)`  
  
  
## Properties 

### CreationTimestamp
    
    
    public string CreationTimestamp { get; set; }

Output only. [Output Only] The creation timestamp for this machine image inRFC3339 text format.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Description
    
    
    public string Description { get; set; }

An optional description of this resource. Provide this property when you create the resource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### GuestFlush
    
    
    public bool GuestFlush { get; set; }

[Input Only] Whether to attempt an application consistent machine image by informing the OS to prepare for the snapshot process.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasCreationTimestamp
    
    
    public bool HasCreationTimestamp { get; }

Gets whether the "creation_timestamp" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasDescription
    
    
    public bool HasDescription { get; }

Gets whether the "description" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasGuestFlush
    
    
    public bool HasGuestFlush { get; }

Gets whether the "guest_flush" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasId
    
    
    public bool HasId { get; }

Gets whether the "id" field is set

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
  
### HasLabelFingerprint
    
    
    public bool HasLabelFingerprint { get; }

Gets whether the "label_fingerprint" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasName
    
    
    public bool HasName { get; }

Gets whether the "name" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSatisfiesPzi
    
    
    public bool HasSatisfiesPzi { get; }

Gets whether the "satisfies_pzi" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSatisfiesPzs
    
    
    public bool HasSatisfiesPzs { get; }

Gets whether the "satisfies_pzs" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSelfLink
    
    
    public bool HasSelfLink { get; }

Gets whether the "self_link" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSourceInstance
    
    
    public bool HasSourceInstance { get; }

Gets whether the "source_instance" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasStatus
    
    
    public bool HasStatus { get; }

Gets whether the "status" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasTotalStorageBytes
    
    
    public bool HasTotalStorageBytes { get; }

Gets whether the "total_storage_bytes" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Id
    
    
    public ulong Id { get; set; }

Output only. [Output Only] A unique identifier for this machine image. The server defines this identifier.

**Property Value**  
---  
**Type** | **Description**  
`[ulong](https://learn.microsoft.com/dotnet/api/system.uint64)` |   
  
### InstanceProperties
    
    
    public InstanceProperties InstanceProperties { get; set; }

[Output Only] Properties of source instance

**Property Value**  
---  
**Type** | **Description**  
`[InstanceProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceProperties)` |   
  
### Kind
    
    
    public string Kind { get; set; }

Output only. [Output Only] The resource type, which is alwayscompute#machineImage for machine image.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### LabelFingerprint
    
    
    public string LabelFingerprint { get; set; }

A fingerprint for the labels being applied to this machine image, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels.

To see the latest fingerprint, make get() request to the machine image.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

Labels to apply to this machine image. These can be later modified by the setLabels method.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MachineImageEncryptionKey
    
    
    public CustomerEncryptionKey MachineImageEncryptionKey { get; set; }

Encrypts the machine image using acustomer-supplied encryption key.

After you encrypt a machine image using a customer-supplied key, you must provide the same key if you use the machine image later. For example, you must provide the encryption key when you create an instance from the encrypted machine image in a future request.

Customer-supplied encryption keys do not protect access to metadata of the machine image.

If you do not provide an encryption key when creating the machine image, then the machine image will be encrypted using an automatically generated key and you do not need to provide a key to use the machine image later.

**Property Value**  
---  
**Type** | **Description**  
`[CustomerEncryptionKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CustomerEncryptionKey)` |   
  
### Name
    
    
    public string Name { get; set; }

Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Params
    
    
    public MachineImageParams Params { get; set; }

Input only. [Input Only] Additional parameters that are passed in the request, but are not persisted in the resource.

**Property Value**  
---  
**Type** | **Description**  
`[MachineImageParams](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.MachineImageParams)` |   
  
### SatisfiesPzi
    
    
    public bool SatisfiesPzi { get; set; }

Output only. Reserved for future use.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### SatisfiesPzs
    
    
    public bool SatisfiesPzs { get; set; }

Output only. [Output Only] Reserved for future use.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### SavedDisks
    
    
    public RepeatedField<SavedDisk> SavedDisks { get; }

Output only. An array of Machine Image specific properties for disks attached to the source instance

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[SavedDisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SavedDisk)` |   
  
### SelfLink
    
    
    public string SelfLink { get; set; }

Output only. [Output Only] The URL for this machine image. The server defines this URL.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SourceDiskEncryptionKeys
    
    
    public RepeatedField<SourceDiskEncryptionKey> SourceDiskEncryptionKeys { get; }

[Input Only] Thecustomer-supplied encryption key of the disks attached to the source instance. Required if the source disk is protected by a customer-supplied encryption key.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[SourceDiskEncryptionKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SourceDiskEncryptionKey)` |   
  
### SourceInstance
    
    
    public string SourceInstance { get; set; }

The source instance used to create the machine image. You can provide this as a partial or full URL to the resource. For example, the following are valid values:
    
    
     - https://www.googleapis.com/compute/v1/projects/project/zones/zone/instances/instance
    

  * projects/project/zones/zone/instances/instance



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SourceInstanceProperties
    
    
    public SourceInstanceProperties SourceInstanceProperties { get; set; }

Output only. [Output Only] DEPRECATED: Please use instance_properties instead for source instance related properties. New properties will not be added to this field.

**Property Value**  
---  
**Type** | **Description**  
`[SourceInstanceProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SourceInstanceProperties)` |   
  
### Status
    
    
    public string Status { get; set; }

Output only. [Output Only] The status of the machine image. One of the following values:INVALID, CREATING, READY,DELETING, and UPLOADING. Check the Status enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### StorageLocations
    
    
    public RepeatedField<string> StorageLocations { get; }

The regional or multi-regional Cloud Storage bucket location where themachine image is stored.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TotalStorageBytes
    
    
    public long TotalStorageBytes { get; set; }

Output only. [Output Only] Total size of the storage used by the machine image.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
