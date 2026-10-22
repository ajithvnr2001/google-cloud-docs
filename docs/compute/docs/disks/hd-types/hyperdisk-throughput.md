---
url: https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput/
title: About Hyperdisk Throughput \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:41:41.191174+00:00
---

# About Hyperdisk Throughput  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About Hyperdisk Throughput Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the features of Hyperdisk Throughput. Hyperdisk Throughput is best for cost-sensitive and analytics workloads that require up to 2,400 MiB/s of throughput per volume. It's also a good fit for workloads that use sequential I/O and large block sizes.

For more information about Hyperdisk and the other Hyperdisk types, see [About Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).

You can specify up to 2,400 MiB/s of throughput for a single Hyperdisk Throughput volume. You can't provision an IOPS level, but each MiB/s of provisioned throughput comes with 4 IOPS, up to 9,600 IOPS.   
Hyperdisk Throughput has a latency profile similar to hard-disk based storage, with average read latency of 10 to 30 milliseconds.

To create a new Hyperdisk Throughput volume, see [Create a Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk).

## Use cases

Hyperdisk Throughput is a good fit for the following use cases:

  * Analytic workloads like Kafka and Hadoop
  * Cold storage
  * Data drives for cost-sensitive workloads



## Machine series support

You can use Hyperdisk Throughput with the following machine series. You can't use Hyperdisk Throughput on bare metal instances, with the exception of C4D and A4X Max bare metal instances.

  * [A3 (H100)](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus)
  * [A4X Max](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms)
  * [C3](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_series)
  * [C3D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3d_machine_types)
  * [C4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series)
  * [C4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series)
  * [C4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4d_series)
  * [C4N](https://docs.cloud.google.com/compute/docs/network-optimized-machines#c4n_series)
  * [G2](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-vms)
  * [G4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series)
  * [H3](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h3_series)
  * [M3](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m3_machine_types)
  * [M4N](https://docs.cloud.google.com/compute/docs/network-optimized-machines#m4n_series)
  * [N2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_series)
  * [N2D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2d_machines)
  * [N4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4_series)
  * [N4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series)
  * [N4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4d_series)
  * [T2D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2d_machines)
  * [X5](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x5_series)
  * [Z3](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_series)
  * [Z4D](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4d_series)
  * [Z4M](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4m_series)



### Limitations for attaching Hyperdisk Throughput volumes to 4th generation instances

If you create a Hyperdisk Throughput volume and attach it to a [4th generation instance](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology) like C4, C4A, or N4, then you can only attach that volume to other 4th generation instances.

If you attach a Hyperdisk Throughput volume to a 1st, 2nd, or 3rd generation instance, you can't attach it to a 4th generation instance. Conversely, you can't attach Hyperdisk Throughput volumes that were attached to 4th generation instances to other instance types. In these scenarios, you must create a new Hyperdisk Throughput volume from the existing Hyperdisk Throughput volume, then attach the new volume to the instance.

For example, if you detach a Hyperdisk Throughput volume from a C4 instance, then you can't attach it to a G2 instance. You must create a new Hyperdisk Throughput volume.

To create a new Hyperdisk Throughput volume from an existing volume, follow the steps in [Change the type, placement, or location of a disk](https://docs.cloud.google.com/compute/docs/disks/migrate-to-hyperdisk#migrate-to-hd), or use the [gcloud compute disks convert](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/convert) command.

## About provisioned performance

You don't have to provision performance when you create Hyperdisk volumes. If you don't provision performance, Compute Engine creates the volume with default values that you can modify later. For details about default values, see Default IOPS and throughput values. 

If you know your performance needs, you can specify IOPS and throughput limits for a Hyperdisk Throughput volume when you create the volume, and you can change the provisioned values after you create the volume. You can't specify an IOPS or throughput level if you don't specify a size.

**Important:** A Hyperdisk volume can't reach its provisioned performance unless you attach it to a compute instance that supports that level of performance, or higher. For detailed performance limits for all supported instances by machine type, see Performance limits when attached to an instance. 

## Size and performance limits

The following limits apply to the size and throughput values you can specify for a Hyperdisk Throughput volume.

  * Size: 2 TiB to 32 TiB. The default size is 2 TiB.
  * Throughput: 20 to 2,400 MiB/s, with the following restrictions: 
    * Minimum throughput: provisioned throughput must be at least 5 times the volume's size in TiB, but not less than 20 MiB/s.
    * Maximum throughput: provisioned throughput can be at most 90 times the volume's size in TiB, up to a maximum of 2,400 MiB/s. For examples, see Limits for provisioned throughput.
  * IOPS: you can't specify an IOPS limit for Hyperdisk Throughput volumes. Instead, the provisioned IOPS depends on the provisioned throughput. Each Hyperdisk Throughput volume is provisioned with 4 IOPS for each MiB/s of throughput, up to a maximum of 9,600 IOPS.



### Limits for provisioned throughput

The following table lists the limits for configurable throughput for common volume sizes. If a size isn't listed, use the following formula to calculate the allowable values, where `x` is the volume's size in TiB:

  * Minimum configurable throughput: `MAX (20, 5x)`
  * Maximum configurable throughput: `MIN (90x, 2400)`

Size (TiB) | Minimum throughput (MiB/s) | Maximum throughput (MiB/s)  
---|---|---  
2 | 20 | 180  
5 | 25 | 450  
10 | 50 | 900  
27 | 135 | 2,400  
32 | 160 | 2,400  
  
### Default size, IOPS, and throughput values

If you don't specify a size or throughput value when you create a Hyperdisk Throughput volume, Compute Engine assigns default values.

The default size for Hyperdisk Throughput volumes is 2 TiB.

The default throughput and IOPS are based on the following formulas, where `x` is the volume's size in TiB.

  * Default throughput: `MIN (90x, 2,400)` MiB/s
  * Default IOPS: `4t`, where `t` is the default throughput. You can't directly configure the IOPS limit.

**Important:** A Hyperdisk volume can't reach its provisioned performance unless you attach it to a compute instance that supports that level of performance, or higher. For detailed performance limits for all supported instances by machine type, see Performance limits when attached to an instance. 

## Change the provisioned performance or size

You can change the provisioned size every 6 hours and its¬ throughput every 4 hours. To learn how to modify size or performance, see [Modify the size and provisioned performance of a Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks).

## Hyperdisk Throughput performance limits when attached to an instance

This section lists the performance limits for Hyperdisk Throughput. You can specify up to 2,400 MiB/s of throughput for a single Hyperdisk Throughput volume. You can't provision an IOPS level, but each MiB/s of provisioned throughput comes with 4 IOPS, up to 9,600 IOPS. 

This section lists the maximum performance that Hyperdisk Throughput volumes can achieve for each supported instance. A Hyperdisk Throughput volume's performance when it's attached to an instance can't exceed the limits for the instance's machine type. The performance limits are also shared across all Hyperdisk Throughput volumes attached to the same instance, regardless of each volume's provisioned performance. 

### Achieve higher performance with multiple Hyperdisk Throughput volumes

Certain instances can exceed the maximum performance for a single Hyperdisk Throughput volume—2,400 MiB/s. An instance can achieve these higher limits if you attach multiple Hyperdisk Throughput volumes to the instance. 

If an instance's performance limit in the following table exceeds 2,400 MiB/s, then the instance can achieve that limit only if you attach multiple Hyperdisk Throughput volumes. For example, the performance limit for a `a3-*-8g` instance using Hyperdisk Throughput volumes is 3,000 MiB/s. Therefore, to achieve 3,000 MiB/s of throughput, you must attach at least two Hyperdisk Throughput volumes to the instance. 

**Important:** To reach the IOPS limits, you must use an I/O size of 4 KB. Maximum throughput limits require an I/O size of at least 256 KB. Hyperdisk performance is half-duplex, so the IOPS and throughput limits are shared between read and write operations. This means that if a machine type has a 50,000 IOPS limit, then the sum of the reads and writes every second can't exceed 50,000. 

The performance limits also apply to [custom machine types](https://docs.cloud.google.com/compute/docs/machine-resource#custom-types). 

Instance machine type | Maximum IOPS | Maximum throughput (MiB/s)  
---|---|---  
A3 (A3+H100)   
`a3-*-1g` | 4,800 | 1,200  
`a3-*-2g` | 9,600 | 2,400  
`a3-*-4g` | 9,600 | 2,400  
`a3-*-8g` | 12,000 | 3,000  
A4X Max   
`a4x-maxgpu-4g-metal` | 40,000 | 10,000  
C3   
`c3-*-4` | 960 | 240  
`c3-*-8` | 3,200 | 800  
`c3-*-22` | 4,800 | 1,200  
`c3-*-44` | 7,200 | 1,800  
`c3-*-88` | 9,600 | 2,400  
`c3-*-176` | 19,200 | 4,800  
C3D   
`c3d-*-4` | 960 | 240  
`c3d-*-8` | 3,200 | 800  
`c3d-*-16` | 4,800 | 1,200  
`c3d-*-30` | 7,200 | 1,800  
`c3d-*-60` | 9,600 | 2,400  
`c3d-*-90` | 9,600 | 2,400  
`c3d-*-180` | 9,600 | 2,400  
`c3d-*-360` | 9,600 | 2,400  
C4 1  
`c4-*-2`1 | 1,600 | 400  
`c4-*-4`1 | 1,600 | 400  
`c4-*-8`1 | 3,200 | 800  
`c4-*-16`1 | 4,000 | 1,000  
`c4-*-24`1 | 4,800 | 1,200  
`c4-*-32`1 | 6,400 | 1,600  
`c4-*-48`1 | 9,600 | 2,400  
`c4-*-64`1 | 12,800 | 3,200  
`c4-*-96`1 | 20,000 | 5,000  
`c4-*-144`1 | 20,000 | 5,000  
`c4-*-192`1 | 40,000 | 10,000  
`c4-*-288`1 | 40,000 | 10,000  
C4A   
`c4a-*-1` | 1,600 | 400  
`c4a-*-2` | 3,200 | 800  
`c4a-*-4` | 3,200 | 800  
`c4a-*-8` | 4,000 | 1,000  
`c4a-*-16` | 6,400 | 1,600  
`c4a-*-32` | 9,600 | 2,400  
`c4a-*-48` | 13,200 | 3,300  
`c4a-*-64` | 17,600 | 4,400  
`c4a-*-72` | 20,000 | 5,000  
`c4a-*-96-metal` | 20,000 | 5,000  
C4D   
`c4d-*-2` | 1,600 | 400  
`c4d-*-4` | 1,600 | 400  
`c4d-*-8` | 3,200 | 800  
`c4d-*-16` | 4,800 | 1,200  
`c4d-*-32` | 6,400 | 1,600  
`c4d-*-48` | 6,400 | 1,600  
`c4d-*-64` | 9,600 | 2,400  
`c4d-*-96` | 12,500 | 3,125  
`c4d-*-192` | 25,000 | 6,250  
`c4d-*-384` | 50,000 | 12,500  
`c4d-*-384-metal` | 40,000 | 10,000  
C4N   
`c4n-*-2` | 3,200 | 800  
`c4n-*-4` | 3,200 | 800  
`c4n-*-8` | 6,400 | 1,600  
`c4n-*-16` | 11,200 | 2,800  
`c4n-*-24` | 12,800 | 3,200  
`c4n-*-48` | 25,000 | 6,250  
`c4n-*-96` | 40,000 | 10,000  
`c4n-*-192` | 80,000 | 20,000  
G2   
`g2-standard-4` | 960 | 240  
`g2-standard-8` | 3,200 | 800  
`g2-standard-12` | 3,200 | 800  
`g2-standard-16` | 4,800 | 1,200  
`g2-standard-24` | 4,800 | 1,200  
`g2-standard-32` | 7,200 | 1,800  
`g2-standard-48` | 9,600 | 2,400  
`g2-standard-96` | 9,600 | 2,400  
G4   
`g4-standard-6` | 1,600 | 400  
`g4-standard-12` | 3,200 | 800  
`g4-standard-24` | 4,800 | 1,200  
`g4-standard-48` | 6,400 | 1,600  
`g4-standard-96` | 11,200 | 2,800  
`g4-standard-192` | 19,200 | 4,800  
`g4-standard-384` | 40,000 | 10,000  
H3   
`h3-standard-88` | 960 | 240  
M3   
`m3-*-32` | 7,200 | 1,800  
`m3-*-64` | 9,600 | 2,400  
`m3-*-128` | 9,600 | 2,400  
M4N 1,2  
`m4n-*-2`1 | 3,200 | 800  
`m4n-*-4`1 | 3,200 | 800  
`m4n-*-8`1 | 3,600 | 900  
`m4n-*-16`1 | 7,200 | 1,800  
`m4n-*-28`1 | 12,500 | 3,125  
`m4n-*-32`1 | 14,400 | 3,600  
`m4n-*-56`1 | 25,000 | 6,250  
`m4n-*-64`1 | 28,800 | 7,200  
`m4n-*-112`1 | 40,000 | 10,000  
`m4n-*-224`1,2 | 80,000 | 20,000  
N2   
`n2-*-2` | 800 | 200  
`n2-*-4` | 960 | 240  
Custom N2 types with 6 vCPUs | 960 | 240  
`n2-*-8` | 3,200 | 800  
Custom N2 types with 10 to 14 vCPUs | 3,200 | 800  
`n2-*-16` | 4,800 | 1,200  
Custom N2 types with 18 to 30 vCPUs | 4,800 | 1,200  
`n2-*-32` | 7,200 | 1,800  
Custom N2 types with 36 to 44 vCPUs | 7,200 | 1,800  
`n2-*-48` | 9,600 | 2,400  
Custom N2 types with 52 to 60 vCPUs | 9,600 | 2,400  
`n2-*-64` | 12,000 | 3,000  
Custom N2 types with 68 to 76 vCPUs | 12,000 | 3,000  
`n2-*-80` | 12,000 | 3,000  
`n2-*-96` | 12,000 | 3,000  
`n2-*-128` | 9,600 | 2,400  
N2D   
`n2d-*-2` | 800 | 200  
`n2d-*-4` | 960 | 240  
`n2d-*-8` | 3,200 | 800  
`n2d-*-16` | 4,800 | 1,200  
`n2d-*-32` | 7,200 | 1,800  
`n2d-*-48` | 9,600 | 2,400  
`n2d-*-64` | 9,600 | 2,400  
`n2d-*-80` | 9,600 | 2,400  
`n2d-*-96` | 9,600 | 2,400  
`n2d-*-128` | 9,600 | 2,400  
`n2d-*-224` | 9,600 | 2,400  
N4   
`n4-*-2` | 960 | 240  
`n4-*-4` | 960 | 240  
Custom N4 types with 6 vCPUs | 960 | 240  
`n4-*-8` | 1,920 | 480  
Custom N4 types with 10 to 14 vCPUs | 1,920 | 480  
`n4-*-16` | 4,800 | 1,200  
Custom N4 types with 18 to 30 vCPUs | 4,800 | 1,200  
`n4-*-32` | 6,400 | 1,600  
Custom N4 types with 34 to 46 vCPUs | 6,400 | 1,600  
`n4-*-48` | 9,600 | 2,400  
Custom N4 types with 50 to 62 vCPUs | 9,600 | 2,400  
`n4-*-64` | 9,600 | 2,400  
Custom N4 types with 66 to 78 vCPUs | 9,600 | 2,400  
`n4-*-80` | 9,600 | 2,400  
N4A   
`n4a-*-1` | 960 | 240  
`n4a-*-2` | 960 | 240  
Custom N4A types with 3 vCPUs | 960 | 240  
`n4a-*-4` | 960 | 240  
Custom N4A types with 5 to 7 vCPUs | 960 | 240  
`n4a-*-8` | 1,920 | 480  
Custom N4A types with 9 to 15 vCPUs | 1,920 | 480  
`n4a-*-16` | 4,800 | 1,200  
Custom N4A types with 17 to 31 vCPUs | 4,800 | 1,200  
`n4a-*-32` | 6,400 | 1,600  
Custom N4A types with 33 to 47 vCPUs | 6,400 | 1,600  
`n4a-*-48` | 9,600 | 2,400  
Custom N4A types with 49 to 63 vCPUs | 9,600 | 2,400  
`n4a-*-64` | 9,600 | 2,400  
N4D   
`n4d-*-2` | 960 | 240  
`n4d-*-4` | 960 | 240  
`n4d-*-8` | 1,920 | 480  
`n4d-*-16` | 4,800 | 1,200  
`n4d-*-32` | 6,400 | 1,600  
`n4d-*-48` | 9,600 | 2,400  
`n4d-*-64` | 9,600 | 2,400  
`n4d-*-80` | 9,600 | 2,400  
`n4d-*-96` | 9,600 | 2,400  
T2D   
`t2d-*-1` | 800 | 200  
`t2d-*-2` | 800 | 200  
`t2d-*-4` | 960 | 240  
`t2d-*-8` | 3,200 | 800  
`t2d-*-16` | 4,800 | 1,200  
`t2d-*-32` | 7,200 | 1,800  
`t2d-*-48` | 9,600 | 2,400  
`t2d-*-60` | 9,600 | 2,400  
X5   
`x5-*-688-metal` | 80,000 | 20,000  
`x5-*-1376-metal` | 80,000 | 20,000  
`x5-*-2064-metal` | 80,000 | 20,000  
Z3   
`z3-*-8` | 3,200 | 800  
`z3-*-14` | 3,200 | 800  
`z3-*-16` | 3,200 | 800  
`z3-*-22` | 4,800 | 1,200  
`z3-*-32` | 4,800 | 1,200  
`z3-*-44` | 7,200 | 1,800  
`z3-*-88` | 9,600 | 2,400  
`z3-*-176` | 9,600 | 2,400  
Z4D 1  
`z4d-*-8`1 | 3,200 | 800  
`z4d-*-16`1 | 4,800 | 1,200  
`z4d-*-32`1 | 8,400 | 2,100  
`z4d-*-48`1 | 12,800 | 3,200  
`z4d-*-64`1 | 16,800 | 4,200  
`z4d-*-96`1 | 25,000 | 6,250  
`z4d-*-192`1 | 50,000 | 12,500  
`z4d-*-384`1,2 | 100,000 | 25,000  
`z4d-*-384-metal`1,2 | 100,000 | 25,000  
Z4M 1  
`z4m-*-16`1 | 6,400 | 1,600  
`z4m-*-32`1 | 8,400 | 2,100  
`z4m-*-48`1 | 12,500 | 3,125  
`z4m-*-192`1,2 | 50,000 | 12,500  
`z4m-*-192-metal`1,2 | 50,000 | 12,500  
  
1 Also offers steady state performance. For more information, see [Performance limits for machine types with steady state performance](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#steady-state).  
2 The disk performance for this machine type is based on having 2 physical NICs per instance. Compute Engine automatically maps attached disks to a physical NIC in a balanced round-robin fashion.  


## Disaster protection for Hyperdisk Throughput volumes

You can back up a Hyperdisk Throughput volume with [standard snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots). Snapshots back up the data on a Hyperdisk Throughput volume at a specific point in time.

### Cross-zonal replication

Hyperdisk Throughput volumes are always zonal and you can't replicate Hyperdisk Throughput volumes to another zone. To replicate data to another zone within the same region, you must use [Hyperdisk Balanced High Availability](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha) volumes. 

## Regional availability for Hyperdisk Throughput

Hyperdisk Throughput is available in all zones and regions.

## Hyperdisk Throughput Storage Pools

You can use Hyperdisk Throughput Storage Pools to simplify planning, avoid overprovisioning storage, and reduce costs. Hyperdisk Throughput Storage Pools let you to purchase Hyperdisk Throughput storage in bulk. To learn more, see [About Hyperdisk Storage Pools](https://docs.cloud.google.com/compute/docs/disks/storage-pools).

## Pricing

You're billed for the total provisioned size and throughput of your Hyperdisk Throughput volumes until you delete them. You incur charges even if the volume isn't attached to any instances or if the instance is suspended or stopped. For more information, see [Disk pricing](https://docs.cloud.google.com/compute/disks-image-pricing#disk).

## Limitations

  * Hyperdisk Throughput volumes are zonal and can only be accessed from the zone where the volume was created.
  * You can't create a [machine image](https://docs.cloud.google.com/compute/docs/machine-images) from a Hyperdisk Throughput volume.
  * You can't create an instant snapshot from a Hyperdisk Throughput volume.
  * You can't use Hyperdisk Throughput volumes as boot disks.
  * You can change a Hyperdisk Throughput volume's size every 6 hours. You can change its throughput every 4 hours.
  * To use Hyperdisk Throughput with N4, C4, or C4A instances, see the Limitations for attaching Hyperdisk Throughput volumes to N4, C4, or C4A instances.



## What's next

  * [Add a Hyperdisk Throughput volume to your VM](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk)
  * Learn about [Hyperdisk Storage Pools](https://docs.cloud.google.com/compute/docs/disks/storage-pools)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
