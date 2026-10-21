---
url: https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms/
title: Share disks between instances \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:30.228206+00:00
---

# Share disks between instances  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Share disks between instances Stay organized with collections  Save and categorize content based on your preferences. 

You can access the same disk from multiple virtual machine (VM) instances by attaching the disk to each instance. You can attach a disk in read-only mode or multi-writer mode to an instance.

With **read-only mode** , multiple instances can only read data from the disk. None of the instances can write to the disk. Sharing a disk in read-only mode between instances is less expensive than having copies of the same data on multiple disks.

With **multi-writer mode** , multiple instances can read and write to the same disk. This is useful for highly-available (HA) shared file systems and databases like SQL Server Failover Cluster Infrastructure (FCI).

You can share a zonal disk only between instances in the same zone. Regional disks can be shared only with instances in the same zones as the disk's replicas.

There are no additional costs associated with sharing a disk between instances. Compute Engine instances don't have to use the same machine type to share a disk, but each instance must use a machine type that supports disk sharing.

This document discusses multi-writer and read-only disk sharing in Compute Engine, including the supported disk types and performance considerations.

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Enable disk sharing

You can attach an existing Hyperdisk or Persistent Disk volume to multiple instances. However, for Hyperdisk volumes, you must first put the disk in multi-writer or read-only mode by setting its access mode.

A Hyperdisk volume's access mode is a property that determines how instances can access the disk.

The available access modes are as follows:

  * Single-writer mode (`READ_WRITE_SINGLE`): This is the default access mode. Allows the disk to be attached to at most one instance at any time. The instance has read-write access to the disk.
  * Read-only mode (`READ_ONLY_MANY`): enables simultaneous attachments to multiple instances in read-only mode. Instances can't write to the disk in this mode. Required for read-only sharing.
  * Multi-writer mode (`READ_WRITE_MANY`): enables simultaneous attachments to multiple instances in read-write mode. Required for multi-writer sharing.



Support for each access mode varies by Hyperdisk type, as stated in the following table. You can't set the access mode for Hyperdisk Throughput volumes.

Hyperdisk type | Supported access modes | Hyperdisk Balanced  
Hyperdisk Balanced High Availability | 

  * Single-writer mode
  * Multi-writer mode

  
---|---  
Hyperdisk Extreme | 

  * Single-writer mode
  * Multi-writer mode

  
Hyperdisk ML | 

  * Single-writer mode
  * Read-only mode

  
Hyperdisk Throughput  
| 

  * Single-writer mode

  
  
For disks that can be shared between instances, you can set the access mode at or after disk creation. For instructions on setting the access mode, see [set the disk's access mode](https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks#change_access_mode).

## Read-only mode for Hyperdisk and Persistent Disk

This section discusses sharing a single disk in read-only mode between multiple instances.

**Note:** A disk's read-only setting applies to all instances that the disk is attached to. You can't attach a disk in read-write mode to one instance and attach the same disk in read-only mode to another instance.

### Supported disk types for read-only mode

You can attach these disk types to multiple instances in read-only mode:

  * Hyperdisk ML
  * Zonal and regional Balanced Persistent Disk
  * SSD Persistent Disk
  * Standard Persistent Disk



### Performance in read-only mode

Attaching a disk in read-only mode to multiple instances doesn't affect the disk's performance. Each instance can still reach the maximum disk performance possible for the instance's machine type.

### Limitations for sharing disks in read-only mode

  * A zonal Persistent Disk or Hyperdisk ML volume must be in the same zone as all the instances that you want to attach the volume to. For a regional Persistent Disk volume, all the instances must be in the same zone as one of the disk's replicas. 
  * If you share a Hyperdisk ML volume in read-only mode, you can't re-enable write access to the disk.
  * You can attach a Hyperdisk ML volume to up to 100 instances during every 30-second interval.
  * The maximum number of instances a disk can be attached to varies by disk type:

    * For Hyperdisk ML volumes, the maximum number of instances depends on the provisioned size, as follows:

      * Volumes with up to 512 GiB of capacity: 2,500 instances 
      * Volumes with capacity between 513 GiB to 1.5 TiB: 1,000 instances 
      * Volumes with capacity between 1.501 TiB and 2 TiB: 600 instances 
      * Volumes with capacity between 2.001 TiB and 4 TiB: 300 instances 
      * Volumes with capacity of 4.001 TiB and 16 TiB: 128 instances 
      * Volumes with capacity of 16.001 TiB or more: 30 instances 
    * Zonal or regional Balanced Persistent Disk volumes in read-only mode support at most 10 instances.
    * For SSD Persistent Disk, Google recommends at most 100 instances.
    * For Standard Persistent Disk volumes, the recommended maximum is 10 instances.



### How to share a disk in read-only mode between instances

If you're not using Hyperdisk ML, attach the disk to multiple instances by following the instructions in [Attach a non-boot disk to an instance](https://docs.cloud.google.com/compute/docs/disks/attach-disks#attach_disk).

To attach a Hyperdisk ML volume in read-only mode to multiple instances, you must first set the disk's access mode to [read-only mode](https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks#change_access_mode). After you set the access mode, [attach the Hyperdisk ML volume to your instances](https://docs.cloud.google.com/compute/docs/disks/attach-disks#attach_disk).

## Multi-writer mode for Hyperdisk

Disks in multi-writer mode are suitable for use cases like the following:

  * Implementing SQL Server FCI.
  * Clustered file systems where multiple instances all write to the same disk
  * Highly available systems in active-active or active-passive mode. Attaching the same disk to multiple instances can prevent disruptions because if one instance fails, other instances still have access to the disk and can continue to run the workload.



If your primary goal is shared file storage among compute instances, consider one of the following options:

  * [Filestore](https://docs.cloud.google.com/filestore/docs/overview), Google's managed file storage solution
  * [Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction)
  * [A network file server](https://cloud.google.com/solutions/filers-on-compute-engine) on Compute Engine



### Supported Hyperdisk and machine series for multi-writer mode

The following table lists the Hyperdisk types that support multi-writer mode. For each Hyperdisk type, the table also lists the supported machine series for multi-writer mode, and the maximum number of instances that can be simultaneously attached to a single volume.

**Note:** You can't attach volumes in multi-writer mode to bare metal instances, with the exception of Hyperdisk Balanced volumes attached to C3 instances.Hyperdisk type | Supported machine types | Maximum number of instances  
---|---|---  
Hyperdisk Balanced | 

  * [C4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series) 1
  * [C4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series)
  * [C3](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_series), including bare metal instances. 
  * [C3D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3d_series)
  * [H3](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h3_series)
  * [M3](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m3_series)
  * [M2](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m2_series)
  * [M1](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m1_series)
  * [N4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4_series)
  * [N4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series) ([Preview](https://cloud.google.com/products#product-launch-stages)) 
  * [N4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4d_series)
  * [Z3](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_series)

| 8  
Hyperdisk Balanced High Availability | 

  * [C4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series) 1
  * [C4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series)
  * [C3](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_series)
  * [C3D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3d_series)
  * [M3](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m3_series)
  * [N4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4_series)
  * [N4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series) ([Preview](https://cloud.google.com/products#product-launch-stages)) 
  * [N4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4d_series)
  * [Z3](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_series)

| 8  
Hyperdisk Extreme | 

  * [C4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series) 1
  * [C3](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_series)
  * [M3](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m3_series)
  * [N2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_series)

| 16  
  
1C4 instances created before May 1, 2026 don't support multi-writer mode. 

### Supported file systems for multi-writer mode

**Warning:** If you use single-instance file systems, such as EXT4, XFS, or NTFS, on a disk in multi-writer mode, you might experience data loss if multiple VMs access the disk at the same time. To mitigate this issue, you can use a clustering software that ensures exclusive access to a single VM at a time, such as SQL Server FCI using NTFS. Otherwise, avoid using single-instance file systems for shared storage.

To access a disk from multiple instances, use one of the following options:

  * [Persistent Reservations (PR)](https://www.kernel.org/doc/Documentation/block/pr.txt), especially for HA systems such as SQL Server FCI and NetApp ONTAP. Google recommends using PR commands to provide I/O fencing and maintain data integrity. For a list of the supported PR commands, see I/O fencing with persistent reservations.
  * Clustered file systems that support multiple instances writing to the same volume. Examples of such file systems include OCFS2, VMFS and GFS2.
  * Scale-out software systems like Lustre and IBM Spectrum Scale.
  * Your own synchronization mechanism to coordinate concurrent reads and writes.



### Hyperdisk performance in multi-writer mode

The information in this section applies to the following disk types:

  * All Hyperdisk Extreme disks in multi-writer mode
  * Hyperdisk Balanced and Hyperdisk Balanced High Availability disks in multi-writer mode created after February 26, 2026.



When you attach a disk of any of the following types to multiple instances, Compute Engine employs _usage-based performance_ : an instance receives a portion the disk's provisioned performance only while the instance is actively using the disk. A single instance could consume the entire provisioned performance of the disk if all the other attached instances are idle.

Usage-based multi-writer performance lets you reduce costs if each instance uses the disk at a different time. This is because you can provision the multi-writer disk with the maximum performance that the most demanding instance requires, instead of provisioning for the combined performance of all the instances.

The amount of performance allocated to each instance depends on how much disk performance the instance requires. The maximum performance for each instance is ultimately limited by the disk's provisioned performance and the instance's performance limits.

### Performance for Hyperdisk Balanced and Hyperdisk Balanced High Availability volumes in multi-writer mode before February 26, 2026

If your Hyperdisk Balanced and Hyperdisk Balanced High Availability volumes were in multi-writer mode before February 26, 2026, Google recommends that you enable usage-based performance by performing one of the following tasks:

  * [detaching and reattaching the disk](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk) from each instance to which it is attached
  * [stopping and restarting each instance to which the disk is attached](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance)



If you don't enable usage-based consumption, performance is divided evenly across each instance, even among instances that aren't running or that aren't actively using the disk.

For example, suppose you attach a Hyperdisk Balanced volume provisioned with 100,000 IOPS to 2 instances. Each instance can consume at most 50,000 IOPS, regardless of the activity level of the other instance. Similarly, if you attach the volume to 8 instances, each instance can consume at most 12,500 IOPS.

### Limitations for sharing Hyperdisk volumes in multi-writer mode

  * You can't attach volumes in multi-writer mode to bare metal instances, with the exception of Hyperdisk Balanced volumes attached to C3 instances.
  * C4 instances created before May 1, 2026, don't support multi-writer mode. To attach a Hyperdisk volume that's in multi-writer mode to a C4 instance, the instance must have been created after May 1, 2026.
  * For zonal Hyperdisk volumes, all the instances attached to the volume must be in the same zone. For regional Hyperdisk volumes, the instances must be in the same zone as one of the volume's replicas.
  * You can attach a single Hyperdisk Balanced or Hyperdisk Balanced High Availability volume in multi-writer mode to at most 8 instances. You can attach a single Hyperdisk Extreme volume in multi-writer mode to at most 16 instances.
  * You can't create machine images or disk images from Hyperdisk volumes in multi-writer mode. 
  * You can't create a Hyperdisk volume in multi-writer mode when you're creating or editing an instance. You must create the Hyperdisk volume separately first, and then attach it to the instance.
  * You can make the following changes to a Hyperdisk volume that's in multi-writer mode, even if the volume is attached to multiple instances:

    * Modify its provisioned IOPS or throughput
    * Attach the disk to additional instances
    * Increase the volume's size

When you modify the provisioned performance or attach the disk to additional instances, Compute Engine redistributes the Hyperdisk volume's provisioned performance across all the attached instances. This process might take up to 6 hours to complete.

  * You can't create an image from a Hyperdisk volume in multi-writer mode.

  * You can't enable auto-delete for Hyperdisk volumes in multi-writer mode.

  * You can't use a Hyperdisk volume in multi-writer mode as the boot disk for an instance.

  * Hyperdisk volumes in multi-writer mode can't be used with instances on sole tenancy nodes.

  * You must use the same interface type as the instance's boot disk.

  * You can't change the machine type of an instance that's attached to a disk in multi-writer mode.

  * Storage pools support only Hyperdisk Balanced volumes in multi-writer mode. Storage pools don't support Hyperdisk Balanced High Availability and Hyperdisk Extreme volumes.

  * You can use [Windows Server Failover Clusters](https://docs.cloud.google.com/compute/docs/tutorials/running-windows-server-failover-clustering) with Hyperdisk volumes in multi-writer mode on machine types that use SCSI or NVMe storage interfaces. However, when using machine types with the NVMe storage interface, the following limitations apply:

    * You must use a Windows Server from 2022 or later.
    * You must create each clustered disk directly on a Hyperdisk volume that's in multi-writer mode. Striping or pooling of Hyperdisk volumes that are in multi-writer mode isn't supported.



### I/O fencing with persistent reservations

Google recommends using persistent reservations (PR) with disks in multi writer mode to provide I/O fencing. Persistent reservations manage access to the disk between instances. This prevents data corruption from instances simultaneously writing to the same portion of the disk.

Hyperdisk volumes in multi-writer mode support [NVMe (spec 1.2.1)](https://nvmexpress.org/wp-content/uploads/NVM_Express_1_2_1_Gold_20160603-1.pdf#page=199) reservations.

#### Supported reservation modes

The following reservation modes are supported:

  1. **Write Exclusive** : there will be a single reservation holder and a single writer. All other registrants and non-registrants will only have read access.
  2. **Exclusive Access** : there will be a single reservation holder which will be the reader and the writer. All other registrants and non-registrants won't have read or write access.
  3. **Write Exclusive - Registrants Only** : there will be a single reservation holder. All registrants will have read and write access to the disk. The non-registrants will only have read access.
  4. **Exclusive Access - Registrant Only** : there will be a single reservation holder. All registrants will have read and write access to the disk. The non-registrants won't have read or write access.
  5. **Write Exclusive - All registrants** : all registrants will be reservation holders and have read and write access to the disk. The non-registrants will only have read access.
  6. **Exclusive Access - All registrants** : all registrants will be reservation holders and have read and write access to the disk. The non-registrants won't have read or write access.



[NVMe `Get Features - Host Identifier`](https://nvmexpress.org/wp-content/uploads/NVM_Express_1_2_1_Gold_20160603-1.pdf#page=135) is supported. The instance number is used as the default Host ID.

The following NVMe reservation features are not supported:

  * Set Features - Host Identifier
  * Reservation notifications: 
    * Get Log Page
    * Reservation Notification Mask



#### Supported commands

NVMe reservations support the following commands:

  * Reservation Register Action (`RREGA`) - Replace/Register/Unregister - `IEKEY`
  * Reservation Acquire Action (`RACQA`) - Acquire/Preempt - `IEKEY`
  * Reservation Release Action (`RRELA`) - Release/Clear - `IEKEY`
  * Reservation Report
  * Reservation capabilities (`RESCAP`) field in the identify namespace data structure.



NVMe reservations don't support the following commands:

  * Preempt and Abort
  * Disabling Persist Through Power Loss (PTPL). PTPL is always enabled.



## How to share a disk in multi-writer mode

Before you attach a disk in multi-writer mode to multiple instances, you must set the disk's access mode to multi-writer. You can set the access mode for a disk when you create it.

You can also set the access mode for an existing disk, but you must first detach the disk from all instances.

To create and use a new disk in multi-writer mode, follow these steps:

  1. Create the disk, setting its access mode to multi-writer. For instructions, see [Add a Hyperdisk to your instance](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk#create_disk).
  2. [Attach the disk to each instance](https://docs.cloud.google.com/compute/docs/disks/attach-disks#attach_disk).



To use an existing disk in multi-writer mode, follow these steps:

  1. Detach the disk from all instances.
  2. [Set the disk's access mode to multi-writer](https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks#change_access_mode).
  3. [Attach the disk to each instance](https://docs.cloud.google.com/compute/docs/disks/attach-disks#attach_disk).



## Multi-writer mode for Persistent Disk volumes

**Caution:** Google recommends that you use Hyperdisk Balanced volumes in multi-writer mode instead of SSD Persistent Disk volumes.

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can attach an SSD Persistent Disk volume in multi-writer mode to up to two N2 virtual machine (VM) instances simultaneously so that both VMs can read and write to the disk.

If you have more than 2 N2 VMs or you're using any other machine series, you can use one of the following options:

  * [Connect your instances to Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction#tools)
  * Connect your instances to [Filestore](https://docs.cloud.google.com/filestore)
  * [Create a network file server](https://cloud.google.com/solutions/filers-on-compute-engine) on Compute Engine



To enable multi-writer mode for new Persistent Disk volumes, create a new Persistent Disk volume and specify the `--multi-writer` flag in the gcloud CLI or the `multiWriter` property in the Compute Engine API.

Persistent Disk volumes in multi-writer mode provide a shared block storage capability and present an infrastructural foundation for building distributed storage systems and similar highly available services. When using Persistent Disk volumes in multi-writer mode, use a [scale-out storage software system](https://docs.cloud.google.com/architecture/filers-on-compute-engine) that has the ability to coordinate access to Persistent Disk devices across multiple VMs. Examples of these storage systems include [Lustre](https://docs.cloud.google.com/architecture/filers-on-compute-engine#DDN) and IBM Spectrum Scale. Most single VM file systems such as EXT4, XFS, and NTFS are not designed to be used with shared block storage.

For more information, see Best practices in this document. If you require a fully managed file storage, you can [mount a Filestore file share on your Compute Engine instances](https://docs.cloud.google.com/filestore/docs/mounting-fileshares).

Persistent Disk volumes in multi-writer mode support a subset of [SCSI-3](https://www.t10.org/scsi-3.htm) Persistent Reservations (SCSI PR) commands. High-availability applications can use these commands for I/O fencing and failover configurations.

The following SCSI PR commands are supported:

  * IN {REPORT CAPABILITIES, READ FULL STATUS, READ RESERVATION, READ KEYS}
  * OUT {REGISTER, REGISTER AND IGNORE EXISTING KEY, RESERVE, PREEMPT, CLEAR, RELEASE}



For instructions, see Share an SSD Persistent Disk volume in multi-writer mode between VMs.

### Supported Persistent Disk types for multi-writer mode

You can simultaneously attach SSD Persistent Disk in multi-writer mode to up to 2 N2 VMs.

### Best practices for multi-writer mode

  * I/O fencing using SCSI PR commands results in a crash consistent state of Persistent Disk data. Some file systems don't have crash consistency and therefore might become corrupt if you use SCSI PR commands.
  * Many file systems such as EXT4, XFS, and NTFS are not designed to be used with shared block storage and don't have mechanisms to synchronize or perform operations that originate from multiple VM instances.
  * Before you use Persistent Disk volumes in multi-writer mode, ensure that you understand your file system and how it can be safely used with shared block storage and simultaneous access from multiple instances.



### Persistent Disk performance in multi-writer mode

Persistent Disk volumes created in multi-writer mode have specific IOPS and throughput limits.

| Zonal SSD persistent disk multi-writer mode  
---|---  
Maximum sustained IOPS  
**Read IOPS per GB** | 30  
**Write IOPS per GB** | 30  
**Read IOPS per instance** | 15,000–100,000*  
**Write IOPS per instance** | 15,000–100,000*  
Maximum sustained throughput (MB/s)  
**Read throughput per GB** | 0.48  
**Write throughput per GB** | 0.48  
**Read throughput per instance** | 240–1,200*  
**Write throughput per instance** | 240–1,200*  
  
* Persistent disk IOPS and throughput performance depends on disk size, instance vCPU count, and I/O block size, among [other factors](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance#performance_factors). 

Attaching a multi-writer disk to multiple virtual machine instances does not affect aggregate performance or cost. Each machine gets a share of the per-disk performance limit.   
  
To learn how to share persistent disks between multiple VMs, see [Share persistent disks between VMs](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms). 

### Restrictions for sharing a disk in multi-writer mode

  * Multi-writer mode is only supported for [SSD type Persistent Disk volumes](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#disk-types).
  * You can create a Persistent Disk volume in multi-writer mode in any zone, but you can only attach that disk to VMs in the following locations: 
    * `australia-southeast1`
    * `europe-west1`
    * `us-central1` (`us-central1-a` and `us-central1-c` zones only)
    * `us-east1` (`us-east1-d` zone only)
    * `us-west1` (`us-west1-b` and `us-west1-c` zones only)
  * Attached VMs must have an [N2 machine type](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_machine_types).
  * Minimum disk size is 10 GiB.
  * Disks in multi-writer mode don't support attaching more than 2 VMs at a time. Multi-writer mode Persistent Disk volumes don't support [Persistent Disk metrics](https://docs.cloud.google.com/compute/docs/disks/review-disk-metrics).
  * Disks in multi-writer mode cannot change to read-only mode.
  * You can't create images from Persistent Disk volumes in multi-writer mode.
  * Lower IOPS limits. See [disk performance](https://docs.cloud.google.com/compute/docs/disks/performance#type_comparison) for details.
  * You can't resize a multi-writer Persistent Disk volume.
  * When creating an instance using the Google Cloud CLI, you can't create a multi-writer Persistent Disk volume using the [`--create-disk`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/create#--create-disk) flag.



### Share an SSD Persistent Disk volume in multi-writer mode between VMs

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Caution:** Google recommends you use Hyperdisk Balanced volumes in multi-writer mode.

You can share an SSD Persistent Disk volume in multi-writer mode between N2 VMs in the same zone. See [Persistent Disk multi-writer mode](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#pdspecs_rw) for details about how this mode works. You can create and attach multi-writer Persistent Disk volumes using the following process:

###  gcloud 

Create and attach a zonal Persistent Disk volume by using the [gcloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute):

  1. Use the [`gcloud beta compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/disks/create) command to create a zonal Persistent Disk volume. Include the `--multi-writer` flag to indicate that the disk must be shareable between the VMs in multi-writer mode.
         
         gcloud beta compute disks create DISK_NAME \
            --size DISK_SIZE \
            --type pd-ssd \
            --multi-writer
         

Replace the following:

     * `DISK_NAME`: the name of the new disk
     * `DISK_SIZE`: the size, in GB, of the new disk Acceptable sizes range from 1 GB to 65,536 GB for SSD Persistent Disk volumes, or 200 GB to 65,536 GB for standard Persistent Disk volumes in multi-writer mode.
  2. After you create the disk, attach it to any running or stopped VM with an N2 machine type. Use the [`gcloud compute instances attach-disk` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk):
         
         gcloud compute instances attach-disk INSTANCE_NAME \
            --disk DISK_NAME
         

Replace the following:

     * `INSTANCE_NAME`: the name of the N2 VM where you are adding the new zonal Persistent Disk volume
     * `DISK_NAME`: the name of the new disk that you are attaching to the VM
  3. Repeat the [`gcloud compute instances attach-disk` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk) but replace INSTANCE_NAME with the name of your second VM.




After you create and attach a new disk to an instance, format and mount the disk using a [shared-disk file system](https://en.wikipedia.org/wiki/Clustered_file_system#SHARED-DISK). Most file systems are not capable of using shared storage. Confirm that your file system supports these capabilities before you use it with multi-writer Persistent Disk. You cannot mount the disk to multiple VMs using the same process you would normally use to mount the disk to a single VM.

###  REST 

Use the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/beta) to create and attach an SSD Persistent Disk volume to N2 VMs in multi-writer mode.

  1. In the API, construct a `POST` request to create a zonal Persistent Disk volume using the [`disks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/disks/insert). Include the `name`, `sizeGb`, and `type` properties. To create this new disk as an empty and unformatted non-boot disk, don't specify a source image or a source snapshot for this disk. Include the `multiWriter` property with a value of `True` to indicate that the disk must be sharable between the VMs in multi-writer mode.
         
         POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/zones/ZONE/disks
         
         {
         "name": "DISK_NAME",
         "sizeGb": "DISK_SIZE",
         "type": "zones/ZONE/diskTypes/pd-ssd",
         "multiWriter": "True"
         }
         

Replace the following:

     * `PROJECT_ID`: your project ID
     * `ZONE`: the zone where your VM and new disk are located
     * `DISK_NAME`: the name of the new disk
     * `DISK_SIZE`: the size, in GB, of the new disk Acceptable sizes range from 1 GB to 65,536 GB for SSD Persistent Disk volumes, or 200 GB to 65,536 GB for standard Persistent Disk volumes in multi-writer mode.
  2. To attach the disk to an instance, construct a `POST` request to the `compute.instances.attachDisk` method. Include the URL to the zonal Persistent Disk volume that you just created:
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/attachDisk
         
         {
         "source": "/compute/v1/projects/PROJECT_ID/zones/ZONE/disks/DISK_NAME"
         }
         

Replace the following:

     * `PROJECT_ID`: your project ID
     * `ZONE`: the zone where your VM and new disk are located
     * `INSTANCE_NAME`: the name of the VM where you are adding the new Persistent Disk volume.
     * `DISK_NAME`: the name of the new disk
  3. To attach the disk to a second VM, repeat the [`instances.attachDisk`](https://docs.cloud.google.com/compute/docs/reference/rest/beta/disks/insert) command from the previous step. Set the `INSTANCE_NAME` to the name of the second VM.




After you create and attach a new disk to an instance, format and mount the disk using a [shared-disk file system](https://en.wikipedia.org/wiki/Clustered_file_system#SHARED-DISK). Most file systems are not capable of using shared storage. Confirm that your file system supports these capabilities before you use it with multi-writer Persistent Disk.

## What's next

  * Learn about [cross-zonal synchronous disk replication](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk).
  * Learn about [Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
