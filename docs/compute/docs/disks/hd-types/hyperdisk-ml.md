---
url: https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-ml/
title: About Hyperdisk ML \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:27.711981+00:00
---

# About Hyperdisk ML  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-ml/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About Hyperdisk ML Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the features of Hyperdisk ML, which offers the highest throughput of all Google Cloud Hyperdisk types. Google recommends using Hyperdisk ML for machine learning and for workloads that require high read throughput on immutable datasets. The high throughput Hyperdisk ML provides results in faster data load times, shorter accelerator idle times and lower compute costs.

For large inference, training and HPC workloads, you can attach a single Hyperdisk ML volume to multiple compute instances in read-only mode.

You can specify up to 2 TiB/s (2,097,152 MiB/s) of throughput for a single Hyperdisk ML volume. You can't provision an IOPS level, but each MiB/s of provisioned throughput comes with 16 IOPS, up to 33,554,432 IOPS. 

For more information about Hyperdisk and the other Hyperdisk types, see [About Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).

To create a Hyperdisk ML volume, see [Create a Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk).

## Use cases

Hyperdisk ML is a good fit for the following use cases:

  * HPC workloads
  * Machine learning
  * Accelerator-optimized workloads



## Machine series support

You can use Hyperdisk ML with the following machine series:

  * [A2](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-vms)
  * [A3 (H100)](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus)
  * [A3 (H200)](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus)
  * [A4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms)
  * [A4X](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms)
  * [A4X Max](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms)
  * [C3](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_series)
  * [C3D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3d_machine_types)
  * [C4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series)
  * [C4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series)
  * [C4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4d_series)
  * [C4N](https://docs.cloud.google.com/compute/docs/network-optimized-machines#c4n_series)
  * [G2](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-vms)
  * [G4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series)
  * [M4N](https://docs.cloud.google.com/compute/docs/network-optimized-machines#m4n_series)
  * [N4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4_series)
  * [N4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series)
  * [N4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4d_series)
  * [TPU v5e](https://docs.cloud.google.com/tpu/docs/v5e)
  * [TPU v5p](https://docs.cloud.google.com/tpu/docs/v5p)
  * [TPU v6e](https://docs.cloud.google.com/tpu/docs/v6e)
  * [TPU7x](https://docs.cloud.google.com/tpu/docs/tpu7x)
  * [X5](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x5_series)
  * [Z4D](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4d_series)



### Limitations for attaching Hyperdisk ML volumes to 4th generation instances

You can't attach Hyperdisk ML volumes created before February 4, 2026 to [4th generation machines](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology), for example, C4 or G4 machines.

To work around this limitation, [create a snapshot of the disk](https://docs.cloud.google.com/compute/docs/disks/create-snapshots#create_snapshots), then [create a new disk from your snapshot](https://docs.cloud.google.com/compute/docs/disks/restore-snapshot#create-disk-from-snapshot). You can attach the new disk to any supported instance.

## About provisioned performance

You don't have to provision performance when you create Hyperdisk volumes. If you don't provision performance, Compute Engine creates the volume with default values that you can modify later. For details about default values, see Default IOPS and throughput values. 

If you know your performance needs, you can specify IOPS and throughput limits for a Hyperdisk ML volume when you create the volume, and you can change the provisioned values after you create the volume. You can't specify an IOPS or throughput level if you don't specify a size.

**Important:** A Hyperdisk volume can't reach its provisioned performance unless you attach it to a compute instance that supports that level of performance, or higher. For detailed performance limits for all supported instances by machine type, see Performance limits when attached to an instance. 

## Size and performance limits

The following limits apply to the size, throughput, and IOPS values you can specify for a Hyperdisk ML volume.

  * **Size** : between 4 GiB and 64 TiB. The default size is 100 GiB.

  * **Throughput** : between 400 MiB/s and 2 TiB/s (2,097,152 MiB/s). Both the minimum and maximum throughput have their own limits based on the size of the volume, as follows:

    * Minimum throughput: for volumes that are 4 to 3,341 GiB in size, the minimum value is 400 MiB/s. For volumes that are 3,342 GiB or greater in size, the minimum value depends on the size and ranges between 401 to 7,680 MiB/s.

    * Maximum throughput: for volumes that are 1,311 GiB or greater in size, the maximum value is 2 TiB/s (2,097,152 MiB/s). For volumes that are 1,310 GiB or smaller in size, the maximum value depends on the size and ranges between 6,400 to 2,097,152 MiB/s. 

For examples, see Limits for provisioned throughput.

  * **IOPS** : you can't specify an IOPS limit for Hyperdisk ML volumes. Instead, the provisioned IOPS depends on the provisioned throughput. Each Hyperdisk ML volume is provisioned with 16 IOPS for each MiB/s of throughput, up to a maximum of 33,554,432 IOPS.




### Limits for provisioned throughput

The following table lists the limits for provisioned throughput for common volume sizes. If a size isn't listed, use the following formula to calculate the allowable values, where `x` is the volume's size in GiB:

  * Minimum configurable throughput: `MAX (400, 0.12x)`
  * Maximum configurable throughput: `MIN (2,097,152, 1600x)`

Size | Min throughput (MiB/s) | Max throughput (MiB/s)  
---|---|---  
4 | 400 | 6,400  
10 | 400 | 16,000  
50 | 400 | 80,000  
64 | 400 | 102,400  
100 | 400 | 160,000  
300 | 400 | 480,000  
500 | 400 | 800,000  
1,000 | 400 | 1,600,000  
5,000 | 600 | 2,097,152  
25,000 | 3,000 | 2,097,152  
64,000 | 7,680 | 2,097,152  
  
### Default size, IOPS, and throughput values

If you don't specify a size or throughput limit when you create a Hyperdisk ML volume, Compute Engine assigns default values.

The default size for Hyperdisk ML volumes is 100 GiB.

The default IOPS and throughput are based on the following formulas.

  * Default throughput: `MAX (24x, 400)` MiB/s, where `x` is the volume's size in GiB.
  * Default IOPS: `16t`, where `t` is the default throughput. You can't directly configure the IOPS limit.

**Important:** A Hyperdisk volume can't reach its provisioned performance unless you attach it to a compute instance that supports that level of performance, or higher. For detailed performance limits for all supported instances by machine type, see Performance limits when attached to an instance. 

## Change the provisioned performance or size

You can change the provisioned size every 4 hours and its throughput every 6 hours. For instructions on modifying size or performance, see [Modify the size and provisioned performance of a Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks).

## Performance limits when attached to an instance

This section lists the performance limits for Hyperdisk ML. You can specify up to 2 TiB/s (2,097,152 MiB/s) of throughput for a single Hyperdisk ML volume. You can't provision an IOPS level, but each MiB/s of provisioned throughput comes with 16 IOPS, up to 33,554,432 IOPS. 

This section lists the maximum performance that Hyperdisk ML volumes can achieve for each supported instance. A Hyperdisk ML volume's performance when it's attached to an instance can't exceed the limits for the instance's machine type. The performance limits are also shared across all Hyperdisk ML volumes attached to the same instance, regardless of each volume's provisioned performance. 

### Scenarios that require multiple instances to reach provisioned performance

The provisioned throughput for a Hyperdisk ML volume is shared between each instance the volume is attached to, up to the maximum limit for the machine type that's listed in the following table. If a Hyperdisk ML volume's provisioned performance is higher than an instance's performance limit, the volume can achieve its provisioned performance only if it is attached to multiple instances.

For example, suppose you have a Hyperdisk ML volume provisioned with 500,000 MiB/s of throughput and you want to attach the volume to `a3-ultragpu-8` instances. A single `a3-ultragpu-8` instance can't acheieve more than 4,000 MiB/s of throughput. Therefore, to achieve the volume's provisioned throughput, you must attach the volume to at least 125 (500,000/4,000) `a3-ultragpu-8` instances. On the other hand, for the `a2-highgpu-1g` machine type, you would need 272 instances. 

**Important:** Hyperdisk performance is half-duplex, so the IOPS and throughput limits are shared between read and write operations. This means that if a machine type has a 50,000 IOPS limit, then the sum of the reads and writes every second can't exceed 50,000. To reach the IOPS limits, you must use an I/O size of 4 KB. Maximum throughput limits require an I/O size of at least 256 KB. 

Instance machine type | Maximum IOPS | Maximum throughput (MiB/s)  
---|---|---  
A2   
`a2-*-1g` | 28,800 | 1,800  
`a2-*-2g` | 38,400 | 2,400  
`a2-*-4g` | 38,400 | 2,400  
`a2-*-8g` | 38,400 | 2,400  
`a2-megagpu-16g` | 38,400 | 2,400  
A3 (A3+H100)   
`a3-*-1g` | 6,400 | 400  
`a3-*-2g` | 28,800 | 1,800  
`a3-*-4g` | 38,400 | 2,400  
`a3-*-8g` | 76,800 | 4,800  
A3 (A3+H200)   
`a3-ultragpu-8g`1 | 160,000 | 10,000  
A4 1  
`a4-highgpu-8g`1 | 160,000 | 10,000  
A4X 1  
`a4x-highgpu-4g`1 | 200,000 | 12,500  
A4X Max 1  
`a4x-maxgpu-4g-metal`1 | 200,000 | 12,500  
C3   
`c3-*-4` | 6,400 | 400  
`c3-*-8` | 12,800 | 800  
`c3-*-22` | 28,800 | 1,800  
`c3-*-44` | 38,400 | 2,400  
`c3-*-88` | 76,800 | 4,800  
`c3-*-176` | 160,000 | 10,000  
`c3-*-192-metal` | 76,800 | 4,800  
C3D   
`c3d-*-4` | 6,400 | 400  
`c3d-*-8` | 12,800 | 800  
`c3d-*-16` | 19,200 | 1,200  
`c3d-*-30` | 19,200 | 1,200  
`c3d-*-60` | 38,400 | 2,400  
`c3d-*-90` | 38,400 | 2,400  
`c3d-*-180` | 38,400 | 2,400  
`c3d-*-360` | 38,400 | 2,400  
C4 1  
`c4-*-2`1 | 6,400 | 400  
`c4-*-4`1 | 6,400 | 400  
`c4-*-8`1 | 12,800 | 800  
`c4-*-16`1 | 25,600 | 1600  
`c4-*-24`1 | 25,600 | 1,600  
`c4-*-32`1 | 25,600 | 1,600  
`c4-*-48`1 | 38,400 | 2,400  
`c4-*-96`1 | 80,000 | 5,000  
`c4-*-144`1 | 100,000 | 6,250  
`c4-*-192`1 | 160,000 | 10,000  
`c4-*-288`1 | 160,000 | 10,000  
`c4-*-288-lssd-metal`1 | 200,000 | 12,500  
C4A   
`c4a-*-1` | 6,400 | 400  
`c4a-*-2` | 12,800 | 800  
`c4a-*-4` | 12,800 | 800  
`c4a-*-8` | 16,000 | 1,000  
`c4a-*-16` | 25,600 | 1,600  
`c4a-*-32` | 38,400 | 2,400  
`c4a-*-48` | 52,800 | 3,300  
`c4a-*-64` | 70,400 | 4,400  
`c4a-*-72` | 80,000 | 5,000  
`c4a-*-72` | 80,000 | 5,000  
`c4a-*-96-metal` | 80,000 | 5,000  
C4D 1  
`c4d-*-2`1 | 6,400 | 400  
`c4d-*-4`1 | 6,400 | 400  
`c4d-*-8`1 | 12,800 | 800  
`c4d-*-16`1 | 19,200 | 1,200  
`c4d-*-32`1 | 25,600 | 1,600  
`c4d-*-48`1 | 25,600 | 1,600  
`c4d-*-64`1 | 38,400 | 2,400  
`c4d-*-96`1 | 50,000 | 3,125  
`c4d-*-192`1 | 100,000 | 6,250  
`c4d-*-384`1 | 160,000 | 10,000  
`c4d-*-384-metal`1 | 160,000 | 10,000  
C4N 1  
`c4n-*-2`1 | 12,800 | 800  
`c4n-*-4`1 | 12,800 | 800  
`c4n-*-8`1 | 25,600 | 1,600  
`c4n-*-16`1 | 44,800 | 2,800  
`c4n-*-24`1 | 51,200 | 3,200  
`c4n-*-48`1 | 100,000 | 6,250  
`c4n-*-96`1 | 160,000 | 10,000  
`c4n-*-192`1 | 320,000 | 20,000  
G2   
`g2-standard-4` | 12,800 | 800  
`g2-standard-8` | 19,200 | 1,200  
`g2-standard-12` | 28,800 | 1,800  
`g2-standard-16` | 38,400 | 2,400  
`g2-standard-24` | 38,400 | 2,400  
`g2-standard-32` | 38,400 | 2,400  
`g2-standard-48` | 38,400 | 2,400  
`g2-standard-96` | 38,400 | 2,400  
G4   
`g4-standard-6` | 6,400 | 400  
`g4-standard-12` | 12,800 | 800  
`g4-standard-24` | 19,200 | 1,200  
`g4-standard-48` | 25,600 | 1,600  
`g4-standard-96` | 44,800 | 2,800  
`g4-standard-192` | 76,800 | 4,800  
`g4-standard-384` | 160,000 | 10,000  
M4N 1,2  
`m4n-*-16`1 | 28,800 | 1,800  
`m4n-*-28`1 | 50,000 | 3,125  
`m4n-*-32`1 | 57,600 | 3,600  
`m4n-*-56`1 | 100,000 | 6,250  
`m4n-*-64`1 | 115,200 | 7,200  
`m4n-*-112`1 | 160,000 | 10,000  
`m4n-*-224`1,2 | 320,000 | 20,000  
N4   
`n4-*-2` | 3,840 | 240  
`n4-*-4` | 3,840 | 240  
`n4-*-8` | 7,680 | 480  
Custom N4 types with 10 to 14 vCPUs | 7,680 | 480  
`n4-*-16` | 19,200 | 1,200  
Custom N4 types with 18 to 30 vCPUs | 19,200 | 1,200  
`n4-*-32` | 25,600 | 1,600  
Custom N4 types with 34 to 46 vCPUs | 25,600 | 1,600  
`n4-*-48` | 38,400 | 2,400  
Custom N4 types with 50 to 62 vCPUs | 38,400 | 2,400  
`n4-*-64` | 38,400 | 2,400  
Custom N4 types with 66 to 78 vCPUs | 38,400 | 2,400  
`n4-*-80` | 38,400 | 2,400  
N4A   
`n4a-*-1` | 3,840 | 240  
`n4a-*-2` | 3,840 | 240  
`n4a-*-4` | 3,840 | 240  
`n4a-*-8` | 7,680 | 480  
`n4a-*-16` | 19,200 | 1,200  
`n4a-*-32` | 25,600 | 1,600  
`n4a-*-48` | 38,400 | 2,400  
`n4a-*-64` | 38,400 | 2400  
N4D   
`n4d-*-2` | 3,840 | 240  
`n4d-*-4` | 3,840 | 240  
`n4d-*-8` | 7,680 | 480  
`n4d-*-16` | 19,200 | 1,200  
`n4d-*-32` | 25,600 | 1,600  
`n4d-*-48` | 38,400 | 2,400  
`n4d-*-64` | 38,400 | 2,400  
`n4d-*-80` | 38,400 | 2,400  
`n4d-*-96` | 38,400 | 2,400  
TPU v5e   
`ct5lp-hightpu-1t` | 19,200 | 1,200  
`ct5lp-hightpu-4t` | 28,800 | 1,800  
`ct5lp-hightpu-8t` | 28,800 | 1,800  
TPU v5p   
`ct5p-hightpu-4t` | 76,800 | 4,800  
TPU v6e   
`ct6e-standard-1t` | 19,200 | 1,200  
`ct6e-standard-4t` | 38,400 | 2,400  
`ct6e-standard-8t` | 38,400 | 2,400  
TPU7x 1  
`tpu7x-standard-4t`1 | 96,000 | 6,000  
X5   
`x5-688-*-metal` | 320,000 | 20,000  
`x5-1376-*-metal` | 320,000 | 20,000  
`x5-2064-*-metal` | 320,000 | 20,000  
Z4D   
`z4d-*-8` | 12,800 | 800  
`z4d-*-16` | 19,200 | 1,200  
`z4d-*-32` | 33,600 | 2,100  
`z4d-*-48` | 51,200 | 3,200  
`z4d-*-64` | 67,200 | 4,200  
`z4d-*-96` | 100,000 | 6,250  
`z4d-*-192` | 200,000 | 12,500  
`z4d-*-384`2 | 400,000 | 25,000  
  
1 Also offers steady state performance. For more information, see [Performance limits for machine types with steady state performance](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#steady-state).  
2 The disk performance for this machine type depends on having 2 network interfaces (vNIC). Compute Engine automatically maps attached disks to a physical NIC in a balanced round-robin fashion.  


## Regional availability for Hyperdisk ML

Hyperdisk ML is available in regions that have supported machine series.

## Disaster protection for Hyperdisk ML volumes

You can back up a Hyperdisk ML volume with [standard snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots). Snapshots back up the data on a Hyperdisk ML volume at a specific point in time.

### Cross-zonal replication

Hyperdisk ML volumes are always zonal and you can't replicate Hyperdisk ML volumes to another zone. To replicate data to another zone within the same region, you must use [Hyperdisk Balanced High Availability](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha) volumes. 

## Share a Hyperdisk ML volume between instances

For accelerator-optimized machine learning workloads, you can attach the same Hyperdisk ML volume to multiple instances. This enables concurrent read-only access to a single volume from multiple instances. This is more cost effective than having multiple disks with the same data.

There are no additional costs associated with sharing a disk between instances. Attaching a disk in read-only mode to multiple instances doesn't affect the disk's performance. Each VM can still reach the maximum disk performance possible for the VM's machine series.

### Limitations for sharing Hyperdisk ML between instances

  * Hyperdisk ML volumes don't support multi-writer mode; you can share a Hyperdisk ML volume among multiple instances if the volume is in read-only mode.
  * Hyperdisk ML volumes can't be attached to single instance in read-only mode.
  * If you share a Hyperdisk ML volume in read-only mode, you can't re-enable write access to the disk.
  * You can attach a Hyperdisk ML volume to up to 100 instances during every 30-second interval.
  * For Hyperdisk ML volumes, the maximum number of instances depends on
the provisioned size, as follows: 
    * Volumes with up to 512 GiB of capacity: 2,500 instances 
    * Volumes with capacity between 513 GiB to 1.5 TiB: 1,000 instances 
    * Volumes with capacity between 1.501 TiB and 2 TiB: 600 instances 
    * Volumes with capacity between 2.001 TiB and 4 TiB: 300 instances 
    * Volumes with capacity of 4.001 TiB and 16 TiB: 128 instances 
    * Volumes with capacity of 16.001 TiB or more: 30 instances 



If the volume is attached to more than 20 instances, then you must provision at least 20 MiB/s of throughput for each instance. For example, if you attach a disk to 500 instances, you must provision the volume with at least 10,000 MiB/s of throughput.

To learn more, see [Read-only mode for Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms#ro-about).

## Pricing

You're billed for the total provisioned size and throughput of your Hyperdisk ML volumes until you delete them. Charges incur even if the volume isn't attached to any instances or if the instance is suspended or stopped. For more information, see [Disk pricing](https://docs.cloud.google.com/compute/disks-image-pricing#disk).

## Limitations

  * Hyperdisk ML volumes are zonal and can only be accessed from the zone where you created the volume.
  * You can't create a [machine image](https://docs.cloud.google.com/compute/docs/machine-images) from a Hyperdisk volume.
  * You can't create an instant snapshot from a Hyperdisk ML volume.
  * You can't use Hyperdisk ML as boot disks.
  * You can't create a Hyperdisk ML disk in read-write-single mode from a snapshot or a disk image. You must create the disk in read-only-many mode.
  * You can change a Hyperdisk ML volume's size every 4 hours, and its throughput every 6 hours.



## What's next

[Add a Hyperdisk ML volume to your VM](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
