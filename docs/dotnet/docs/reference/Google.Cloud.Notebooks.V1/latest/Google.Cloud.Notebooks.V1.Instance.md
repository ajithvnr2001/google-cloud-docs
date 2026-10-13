---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance
title: Vertex AI Notebooks v1 API - Class Instance (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:50:17.133405+00:00
---

# Vertex AI Notebooks v1 API - Class Instance (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI Notebooks v1 API - Class Instance (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/2.5.0/Google.Cloud.Notebooks.V1.Instance)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/2.4.0/Google.Cloud.Notebooks.V1.Instance)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/2.3.0/Google.Cloud.Notebooks.V1.Instance)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/2.2.0/Google.Cloud.Notebooks.V1.Instance)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/2.1.0/Google.Cloud.Notebooks.V1.Instance)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/2.0.0/Google.Cloud.Notebooks.V1.Instance)
  * [ 1.0.0-beta04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/1.0.0-beta04/Google.Cloud.Notebooks.V1.Instance)


    
    
    public sealed class Instance : IMessage<Instance>, IEquatable<Instance>, IDeepCloneable<Instance>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI Notebooks v1 API class Instance.

The definition of a notebook instance.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Instance

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Notebooks.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1)

## Assembly

Google.Cloud.Notebooks.V1.dll

## Constructors 

### Instance()
    
    
    public Instance()

### Instance(Instance)
    
    
    public Instance(Instance other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance)`  
  
  
## Properties 

### AcceleratorConfig
    
    
    public Instance.Types.AcceleratorConfig AcceleratorConfig { get; set; }

The hardware accelerator used on this instance. If you use accelerators, make sure that your configuration has [enough vCPUs and memory to support the `machine_type` you have selected](https://cloud.google.com/compute/docs/gpus/#gpus-list).

**Property Value**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance.Types)[AcceleratorConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance.Types.AcceleratorConfig)` |   
  
### BootDiskSizeGb
    
    
    public long BootDiskSizeGb { get; set; }

Input only. The size of the boot disk in GB attached to this instance, up to a maximum of 64000 GB (64 TB). The minimum recommended value is 100 GB. If not specified, this defaults to 100.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### BootDiskType
    
    
    public Instance.Types.DiskType BootDiskType { get; set; }

Input only. The type of the boot disk attached to this instance, defaults to standard persistent disk (`PD_STANDARD`).

**Property Value**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance.Types)[DiskType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance.Types.DiskType)` |   
  
### CanIpForward
    
    
    public bool CanIpForward { get; set; }

Optional. Flag to enable ip forwarding or not, default false/off. <https://cloud.google.com/vpc/docs/using-routes#canipforward>

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### ContainerImage
    
    
    public ContainerImage ContainerImage { get; set; }

Use a container image to start the notebook instance.

**Property Value**  
---  
**Type** | **Description**  
`[ContainerImage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.ContainerImage)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. Instance creation time.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Creator
    
    
    public string Creator { get; set; }

Output only. Email address of entity that sent original CreateInstance request.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CustomGpuDriverPath
    
    
    public string CustomGpuDriverPath { get; set; }

Specify a custom Cloud Storage path where the GPU driver is stored. If not specified, we'll automatically choose from official GPU drivers.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DataDiskSizeGb
    
    
    public long DataDiskSizeGb { get; set; }

Input only. The size of the data disk in GB attached to this instance, up to a maximum of 64000 GB (64 TB). You can choose the size of the data disk based on how big your notebooks and data are. If not specified, this defaults to 100.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### DataDiskType
    
    
    public Instance.Types.DiskType DataDiskType { get; set; }

Input only. The type of the data disk attached to this instance, defaults to standard persistent disk (`PD_STANDARD`).

**Property Value**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance.Types)[DiskType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance.Types.DiskType)` |   
  
### DiskEncryption
    
    
    public Instance.Types.DiskEncryption DiskEncryption { get; set; }

Input only. Disk encryption method used on the boot and data disks, defaults to GMEK.

**Property Value**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance.Types)[DiskEncryption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance.Types.DiskEncryption)` |   
  
### Disks
    
    
    public RepeatedField<Instance.Types.Disk> Disks { get; }

Output only. Attached disks to notebook instance.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance.Types)[Disk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance.Types.Disk)` |   
  
### EnvironmentCase
    
    
    public Instance.EnvironmentOneofCase EnvironmentCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance)[EnvironmentOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance.EnvironmentOneofCase)` |   
  
### InstallGpuDriver
    
    
    public bool InstallGpuDriver { get; set; }

Whether the end user authorizes Google Cloud to install GPU driver on this instance. If this field is empty or set to false, the GPU driver won't be installed. Only applicable to instances with GPUs.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### InstanceName
    
    
    public InstanceName InstanceName { get; set; }

[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.InstanceName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance#Google_Cloud_Notebooks_V1_Instance_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.InstanceName)` |   
  
### InstanceOwners
    
    
    public RepeatedField<string> InstanceOwners { get; }

Input only. The owner of this instance after creation. Format: `alias@example.com`

Currently supports one owner only. If not specified, all of the service account users of your VM instance's service account can use the instance.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### KmsKey
    
    
    public string KmsKey { get; set; }

Input only. The KMS key used to encrypt the disks, only applicable if disk_encryption is CMEK. Format: `projects/{project_id}/locations/{location}/keyRings/{key_ring_id}/cryptoKeys/{key_id}`

Learn more about [using your own encryption keys](https://docs.cloud.google.com/kms/docs/quickstart).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

Labels to apply to this instance. These can be later modified by the setLabels method.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MachineType
    
    
    public string MachineType { get; set; }

Required. The [Compute Engine machine type](https://cloud.google.com/compute/docs/machine-types) of this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Metadata
    
    
    public MapField<string, string> Metadata { get; }

Custom metadata to apply to this instance.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. The name of this notebook instance. Format: `projects/{project_id}/locations/{location}/instances/{instance_id}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Network
    
    
    public string Network { get; set; }

The name of the VPC that this instance is in. Format: `projects/{project_id}/global/networks/{network_id}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NicType
    
    
    public Instance.Types.NicType NicType { get; set; }

Optional. The type of vNIC to be used on this interface. This may be gVNIC or VirtioNet.

**Property Value**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance.Types)[NicType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance.Types.NicType)` |   
  
### NoProxyAccess
    
    
    public bool NoProxyAccess { get; set; }

If true, the notebook instance will not register with the proxy.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### NoPublicIp
    
    
    public bool NoPublicIp { get; set; }

If true, no public IP will be assigned to this instance.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### NoRemoveDataDisk
    
    
    public bool NoRemoveDataDisk { get; set; }

Input only. If true, the data disk will not be auto deleted when deleting the instance.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### PostStartupScript
    
    
    public string PostStartupScript { get; set; }

Path to a Bash script that automatically runs after a notebook instance fully boots up. The path must be a URL or Cloud Storage path (`gs://path-to-file/file-name`).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ProxyUri
    
    
    public string ProxyUri { get; set; }

Output only. The proxy endpoint that is used to access the Jupyter notebook.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ReservationAffinity
    
    
    public ReservationAffinity ReservationAffinity { get; set; }

Optional. The optional reservation affinity. Setting this field will apply the specified [Zonal Compute Reservation](https://cloud.google.com/compute/docs/instances/reserving-zonal-resources) to this notebook instance.

**Property Value**  
---  
**Type** | **Description**  
`[ReservationAffinity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.ReservationAffinity)` |   
  
### ServiceAccount
    
    
    public string ServiceAccount { get; set; }

The service account on this instance, giving access to other Google Cloud services. You can use any service account within the same project, but you must have the service account user permission to use the instance.

If not specified, the [Compute Engine default service account](https://cloud.google.com/compute/docs/access/service-accounts#default_service_account) is used.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServiceAccountScopes
    
    
    public RepeatedField<string> ServiceAccountScopes { get; }

Optional. The URIs of service account scopes to be included in Compute Engine instances.

If not specified, the following [scopes](https://cloud.google.com/compute/docs/access/service-accounts#accesscopesiam) are defined:

  * <https://www.googleapis.com/auth/cloud-platform>
  * <https://www.googleapis.com/auth/userinfo.email> If not using default scopes, you need at least: <https://www.googleapis.com/auth/compute>



**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ShieldedInstanceConfig
    
    
    public Instance.Types.ShieldedInstanceConfig ShieldedInstanceConfig { get; set; }

Optional. Shielded VM configuration. [Images using supported Shielded VM features](https://cloud.google.com/compute/docs/instances/modifying-shielded-vm).

**Property Value**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance.Types)[ShieldedInstanceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance.Types.ShieldedInstanceConfig)` |   
  
### State
    
    
    public Instance.Types.State State { get; set; }

Output only. The state of this instance.

**Property Value**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance.Types.State)` |   
  
### Subnet
    
    
    public string Subnet { get; set; }

The name of the subnet that this instance is in. Format: `projects/{project_id}/regions/{region}/subnetworks/{subnetwork_id}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Tags
    
    
    public RepeatedField<string> Tags { get; }

Optional. The Compute Engine tags to add to runtime (see [Tagging instances](https://cloud.google.com/compute/docs/label-or-tag-resources#tags)).

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. Instance update time.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### UpgradeHistory
    
    
    public RepeatedField<Instance.Types.UpgradeHistoryEntry> UpgradeHistory { get; }

The upgrade history of this instance.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance.Types)[UpgradeHistoryEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.Instance.Types.UpgradeHistoryEntry)` |   
  
### VmImage
    
    
    public VmImage VmImage { get; set; }

Use a Compute Engine VM image to start the notebook instance.

**Property Value**  
---  
**Type** | **Description**  
`[VmImage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.VmImage)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
