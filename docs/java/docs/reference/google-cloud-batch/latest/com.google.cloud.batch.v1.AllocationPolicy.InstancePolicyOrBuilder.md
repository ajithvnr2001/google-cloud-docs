---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrBuilder
title: Interface AllocationPolicy.InstancePolicyOrBuilder (0.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:39:09.607985+00:00
---

# Interface AllocationPolicy.InstancePolicyOrBuilder (0.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AllocationPolicy.InstancePolicyOrBuilder (0.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.99.0 (latest)  0.95.0  0.94.0  0.93.0  0.91.0  0.88.0  0.87.0  0.85.0  0.83.0  0.82.0  0.81.0  0.80.0  0.78.0  0.76.0  0.75.0  0.74.0  0.73.0  0.72.0  0.70.0  0.68.0  0.67.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.2  0.2.2  0.1.1 
    
    
    public static interface AllocationPolicy.InstancePolicyOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAccelerators(int index)
    
    
    public abstract AllocationPolicy.Accelerator getAccelerators(int index)

The accelerators attached to each VM instance.

`repeated .google.cloud.batch.v1.AllocationPolicy.Accelerator accelerators = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AllocationPolicy.Accelerator](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.Accelerator)` |   
  
### getAcceleratorsCount()
    
    
    public abstract int getAcceleratorsCount()

The accelerators attached to each VM instance.

`repeated .google.cloud.batch.v1.AllocationPolicy.Accelerator accelerators = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAcceleratorsList()
    
    
    public abstract List<AllocationPolicy.Accelerator> getAcceleratorsList()

The accelerators attached to each VM instance.

`repeated .google.cloud.batch.v1.AllocationPolicy.Accelerator accelerators = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Accelerator](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.Accelerator)>` |   
  
### getAcceleratorsOrBuilder(int index)
    
    
    public abstract AllocationPolicy.AcceleratorOrBuilder getAcceleratorsOrBuilder(int index)

The accelerators attached to each VM instance.

`repeated .google.cloud.batch.v1.AllocationPolicy.Accelerator accelerators = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AllocationPolicy.AcceleratorOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.AcceleratorOrBuilder)` |   
  
### getAcceleratorsOrBuilderList()
    
    
    public abstract List<? extends AllocationPolicy.AcceleratorOrBuilder> getAcceleratorsOrBuilderList()

The accelerators attached to each VM instance.

`repeated .google.cloud.batch.v1.AllocationPolicy.Accelerator accelerators = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.batch.v1.AllocationPolicy.AcceleratorOrBuilder>` |   
  
### getBootDisk()
    
    
    public abstract AllocationPolicy.Disk getBootDisk()

Boot disk to be created and attached to each VM by this InstancePolicy. Boot disk will be deleted when the VM is deleted. Batch API now only supports booting from image.

`.google.cloud.batch.v1.AllocationPolicy.Disk boot_disk = 8;`

**Returns**  
---  
**Type** | **Description**  
`[AllocationPolicy.Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.Disk)` | The bootDisk.  
  
### getBootDiskOrBuilder()
    
    
    public abstract AllocationPolicy.DiskOrBuilder getBootDiskOrBuilder()

Boot disk to be created and attached to each VM by this InstancePolicy. Boot disk will be deleted when the VM is deleted. Batch API now only supports booting from image.

`.google.cloud.batch.v1.AllocationPolicy.Disk boot_disk = 8;`

**Returns**  
---  
**Type** | **Description**  
`[AllocationPolicy.DiskOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.DiskOrBuilder)` |   
  
### getDisks(int index)
    
    
    public abstract AllocationPolicy.AttachedDisk getDisks(int index)

Non-boot disks to be attached for each VM created by this InstancePolicy. New disks will be deleted when the VM is deleted. A non-boot disk is a disk that can be of a device with a file system or a raw storage drive that is not ready for data storage and accessing.

`repeated .google.cloud.batch.v1.AllocationPolicy.AttachedDisk disks = 6;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AllocationPolicy.AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.AttachedDisk)` |   
  
### getDisksCount()
    
    
    public abstract int getDisksCount()

Non-boot disks to be attached for each VM created by this InstancePolicy. New disks will be deleted when the VM is deleted. A non-boot disk is a disk that can be of a device with a file system or a raw storage drive that is not ready for data storage and accessing.

`repeated .google.cloud.batch.v1.AllocationPolicy.AttachedDisk disks = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDisksList()
    
    
    public abstract List<AllocationPolicy.AttachedDisk> getDisksList()

Non-boot disks to be attached for each VM created by this InstancePolicy. New disks will be deleted when the VM is deleted. A non-boot disk is a disk that can be of a device with a file system or a raw storage drive that is not ready for data storage and accessing.

`repeated .google.cloud.batch.v1.AllocationPolicy.AttachedDisk disks = 6;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.AttachedDisk)>` |   
  
### getDisksOrBuilder(int index)
    
    
    public abstract AllocationPolicy.AttachedDiskOrBuilder getDisksOrBuilder(int index)

Non-boot disks to be attached for each VM created by this InstancePolicy. New disks will be deleted when the VM is deleted. A non-boot disk is a disk that can be of a device with a file system or a raw storage drive that is not ready for data storage and accessing.

`repeated .google.cloud.batch.v1.AllocationPolicy.AttachedDisk disks = 6;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AllocationPolicy.AttachedDiskOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.AttachedDiskOrBuilder)` |   
  
### getDisksOrBuilderList()
    
    
    public abstract List<? extends AllocationPolicy.AttachedDiskOrBuilder> getDisksOrBuilderList()

Non-boot disks to be attached for each VM created by this InstancePolicy. New disks will be deleted when the VM is deleted. A non-boot disk is a disk that can be of a device with a file system or a raw storage drive that is not ready for data storage and accessing.

`repeated .google.cloud.batch.v1.AllocationPolicy.AttachedDisk disks = 6;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.batch.v1.AllocationPolicy.AttachedDiskOrBuilder>` |   
  
### getMachineType()
    
    
    public abstract String getMachineType()

The Compute Engine machine type.

`string machine_type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The machineType.  
  
### getMachineTypeBytes()
    
    
    public abstract ByteString getMachineTypeBytes()

The Compute Engine machine type.

`string machine_type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for machineType.  
  
### getMinCpuPlatform()
    
    
    public abstract String getMinCpuPlatform()

The minimum CPU platform. See <https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform>.

`string min_cpu_platform = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The minCpuPlatform.  
  
### getMinCpuPlatformBytes()
    
    
    public abstract ByteString getMinCpuPlatformBytes()

The minimum CPU platform. See <https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform>.

`string min_cpu_platform = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for minCpuPlatform.  
  
### getProvisioningModel()
    
    
    public abstract AllocationPolicy.ProvisioningModel getProvisioningModel()

The provisioning model.

`.google.cloud.batch.v1.AllocationPolicy.ProvisioningModel provisioning_model = 4; `

**Returns**  
---  
**Type** | **Description**  
`[AllocationPolicy.ProvisioningModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.ProvisioningModel)` | The provisioningModel.  
  
### getProvisioningModelValue()
    
    
    public abstract int getProvisioningModelValue()

The provisioning model.

`.google.cloud.batch.v1.AllocationPolicy.ProvisioningModel provisioning_model = 4; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for provisioningModel.  
  
### getReservation()
    
    
    public abstract String getReservation()

Optional. If not specified (default), VMs will consume any applicable reservation. If "NO_RESERVATION" is specified, VMs will not consume any reservation. Otherwise, if specified, VMs will consume only the specified reservation.

`string reservation = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The reservation.  
  
### getReservationBytes()
    
    
    public abstract ByteString getReservationBytes()

Optional. If not specified (default), VMs will consume any applicable reservation. If "NO_RESERVATION" is specified, VMs will not consume any reservation. Otherwise, if specified, VMs will consume only the specified reservation.

`string reservation = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for reservation.  
  
### hasBootDisk()
    
    
    public abstract boolean hasBootDisk()

Boot disk to be created and attached to each VM by this InstancePolicy. Boot disk will be deleted when the VM is deleted. Batch API now only supports booting from image.

`.google.cloud.batch.v1.AllocationPolicy.Disk boot_disk = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bootDisk field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
