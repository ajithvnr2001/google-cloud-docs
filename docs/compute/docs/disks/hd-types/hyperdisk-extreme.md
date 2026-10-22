---
url: https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme/
title: About Hyperdisk Extreme \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:41:42.211909+00:00
---

# About Hyperdisk Extreme  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About Hyperdisk Extreme Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the features and performance limits of Hyperdisk Extreme volumes. Hyperdisk Extreme is designed for applications that require more than 160,000 IOPS or 2,400 MiB/s of bandwidth from a single volume, such as high-performance databases.

You can specify up to 350,000 IOPS for a single Hyperdisk Extreme volume. You can't provision a throughput level for Hyperdisk Extreme volumes. Each volume gets 250 MiB/s of throughput with every 1,000 IOPS, up to 5,000 MiB/s. 

Hyperdisk Extreme volumes are designed for sub-millisecond latencies.

## Use cases

Hyperdisk Extreme is a good fit for the following use cases:

  * SAP HANA
  * High-end SQL Server, Oracle
  * In-memory RDBMS that require more than 160,000 IOPS



## Machine series support

You can use Hyperdisk Extreme with the following machine series:

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
  * [G4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series)
  * [M1](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m1_machine_types)
  * [M2](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m2_machine_types)
  * [M3](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m3_machine_types)
  * [M4](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m4_machine_types)
  * [M4N](https://docs.cloud.google.com/compute/docs/network-optimized-machines#m4n_series)
  * [N2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_series)
  * [X4](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x4_series)
  * [X5](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x5_series)
  * [Z3](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_series)
  * [Z4D](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4d_series)
  * [Z4M](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4m_series)



### Restrictions for machine series support

  * A3 machine types require at least 104 vCPUs so `a3-highgpu-1g` and `a3-highgpu-2g` aren't supported.
  * C3 machine type require at least 88 vCPUs.
  * C3D machine types require at least 60 vCPUs.
  * C4 and G4 machine types require at least 96 vCPUs.
  * M1 machine types require at least 80 vCPUs.
  * C4A, C4D, M3, and M4 machine types require at least 64 vCPUs.
  * N2 machine types require at least 80 vCPUs; Custom N2 machine types aren't supported



## About provisioned performance

You don't have to provision performance when you create Hyperdisk volumes. If you don't provision performance, Compute Engine creates the volume with default values that you can modify later. For details about default values, see Default IOPS and throughput values. 

You can specify an IOPS limits for a Hyperdisk Extreme volume when you create the volume, and you can modify the provisioned IOPS after you create the volume. You can't specify an IOPS level if you don't specify a size.

**Important:** A Hyperdisk volume can't reach its provisioned performance unless you attach it to a compute instance that supports that level of performance, or higher. For detailed performance limits for all supported instances by machine type, see Performance limits when attached to an instance. 

For details about performance for Hyperdisk volumes, see [About Hyperdisk performance](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-performance).

## Size and performance limits

The following limits apply to the size, throughput, and IOPS values you can specify for a Hyperdisk Extreme volume.

  * Size: between 64 GiB and 64 TiB. The default size is 1 TiB.
  * IOPS: between 128 and 350,000 IOPS. However, for volumes less than 1 TiB, the range of IOPS values you can specify varies by size. For examples, see Limits for provisioned IOPS.
  * Throughput: you can't specify a throughput limit for Hyperdisk Extreme volumes. Instead, the throughput depends on the provisioned IOPS. Each Hyperdisk Extreme volume is provisioned with 250 MiB/s of throughput for every 1,000 IOPS, up to a maximum of 5,000 MiB/s.



### Limits for provisioned IOPS

The IOPS level you can specify for a Hyperdisk Extreme volume depends on the disk's size, according to the following formulas, where `x` is the volume's size in GiB.

  * Minimum IOPS: `2x`
  * Maximum IOPS: 
    * 64 GiB to 291 GiB: `1,200x`
    * 292 GiB to 64 TiB: 350,000 IOPS



This table provides the range of IOPS values that you can provision for common volume sizes. If a size value isn't listed, use the preceding formula to calculate the maximum allowable IOPS.

Volume size (GiB) | Minimum IOPS | Maximum IOPS  
---|---|---  
64 | 128 | 76,800  
150 | 300 | 180,000  
200 | 400 | 240,000  
290 | 580 | 348,000  
300 | 600 | 350,000  
1,000 | 2,000 | 350,000  
  
### Default size, IOPS, and throughput values

If you don't specify a size or IOPS value when you create a Hyperdisk Extreme volume, Compute Engine provisions the volume with default values.

The default size is 1 TiB.

The default IOPS and throughput are based on the following formulas.

  * Default IOPS depends on the provisioned size, as follows:

    * if you don't specify a size: 100,000 IOPS
    * if you specify a size: `MIN((350,000), 100x)`, where `x` is the volume's size in GiB.
  * Default throughput depends on the provisioned IOPS, as follows:

    * if you don't specify an IOPS limit: 5,000 MiB/s
    * if you specify an IOPS limit: 250 MiB/s per 1,000 IOPS, up to 5,000 MiB/s.

**Important:** A Hyperdisk volume can't reach its provisioned performance unless you attach it to a compute instance that supports that level of performance, or higher. For detailed performance limits for all supported instances by machine type, see Performance limits when attached to an instance. 

## Change the provisioned IOPS or size

You can change the provisioned performance and size of a Hyperdisk Extreme volume at most once every 4 hours. For instructions on modifying size or performance, see [Modify the size and provisioned performance of a Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks).

## Performance limits when attached to an instance

This section lists the specific performance limits for each machine type that supports Hyperdisk Extreme. You can specify up to 350,000 IOPS for a single Hyperdisk Extreme volume. You can't provision a throughput level for Hyperdisk Extreme volumes. Each volume gets 250 MiB/s of throughput with every 1,000 IOPS, up to 5,000 MiB/s. 

This section lists the maximum performance that Hyperdisk Extreme volumes can achieve for each supported instance. A Hyperdisk Extreme volume's performance when it's attached to an instance can't exceed the limits for the instance's machine type. The performance limits are also shared across all Hyperdisk Extreme volumes attached to the same instance, regardless of each volume's provisioned performance. 

### Achieve higher performance with multiple Hyperdisk Extreme volumes

Certain instances can exceed the maximum performance for a single Hyperdisk Extreme volume— 350,000 IOPS or 5,000 MiB/s. An instance can only achieve these higher limits if you attach multiple Hyperdisk Extreme volumes to the instance.

If an instance's performance limit in the following table exceeds 350,000 IOPS or 5,000 MiB/s, then the instance can only achieve that limit if you attach multiple Hyperdisk Extreme volumes. For example, the performance limit for a `c3-*-176` instance using Hyperdisk Extreme is 500,000 IOPS and 10,000 MiB/s. To achieve this maximum performance you must attach at least two Hyperdisk Extreme volumes to the instance. 

**Important:** Hyperdisk performance is half-duplex, so the IOPS and throughput limits are shared between read and write operations. This means that if a machine type has a 50,000 IOPS limit, then the sum of the reads and writes every second can't exceed 50,000. To reach the IOPS limits, you must use an I/O size of 4 KB. Maximum throughput limits require an I/O size of at least 256 KB. 

Instance machine type | Maximum IOPS | Maximum throughput (MiB/s)  
---|---|---  
A3 (A3+H100)   
`a3-highgpu-4g` | 350,000 | 5,000  
`a3-megagpu-8g` | 400,000 | 8,000  
`a3-highgpu-8g` | 400,000 | 8,000  
`a3-edgegpu-8g` | 400,000 | 8,000  
A3 (A3+H200)   
`a3-ultragpu-8g`2 | 500,000 | 10,000  
A4 2  
`a4-highgpu-8g`2 | 500,000 | 10,000  
A4X 2  
`a4x-highgpu-4g`2 | 500,000 | 12,500  
A4X Max 2  
`a4x-maxgpu-4g-metal`2 | 500,000 | 12,500  
C3 1  
`c3-*-88`1 | 350,000 | 5,000  
`c3-*-176`1 | 500,000 | 10,000  
`c3-*-192-metal`1 | 500,000 | 10,000  
C3D   
`c3d-*-60`1 | 350,000 | 5,000  
`c3d-*-90`1 | 350,000 | 5,000  
`c3d-*-180`1 | 350,000 | 5,000  
`c3d-*-360`1 | 350,000 | 5,000  
C4 2  
`c4-*-96`2 | 350,000 | 5,000  
`c4-*-144`2 | 350,000 | 5,000  
`c4-*-192`2 | 500,000 | 10,000  
`c4-*-288`2 | 500,000 | 10,000  
`c4-*-288-metal`2 | 500,000 | 10,000  
C4A   
`c4a-*-64` | 350,000 | 5,000  
`c4a-*-72` | 350,000 | 5,000  
`c4a-*-96-metal` | 350,000 | 5,000  
C4D 2  
`c4d-*-64`2 | 350,000 | 5,000  
`c4d-*-96`2 | 350,000 | 5,000  
`c4d-*-192`2 | 350,000 | 5,000  
`c4d-*-384`2 | 500,000 | 10,000  
C4N 2,3  
`c4n-*-2`2 | 80,000 | 1,000  
`c4n-*-4`2 | 100,000 | 1,000  
`c4n-*-8`2 | 120,000 | 1,800  
`c4n-*-16`2 | 160,000 | 3,000  
`c4n-*-24`2 | 240,000 | 4,000  
`c4n-*-48`2 | 380,000 | 8,000  
`c4n-*-96`2 | 500,000 | 12,500  
`c4n-*-192`2,3 | 1,000,000 | 25,000  
G4   
`g4-standard-96` | 350,000 | 5,000  
`g4-standard-192` | 350,000 | 5,000  
`g4-standard-384` | 500,000 | 10,000  
M2   
`m2-*-208` | 100,000 | 3,815  
`m2-*-416` | 100,000 | 3,815  
M3 1  
`m3-*-64`1 | 350,000 | 5,000  
`m3-*-128`1 | 450,000 | 6,870  
M4 2  
`m4-*-64`2 | 200,000 | 3,600  
`m4-*-112`2 | 350,000 | 5,000  
`m4-*-224`2 | 500,000 | 10,000  
M4N 2  
`m4n-*-2`1 | 80,000 | 1000  
`m4n-*-4`1 | 100,000 | 1,000  
`m4n-*-8`1 | 120,000 | 1,600  
`m4n-*-16`2 | 160,000 | 3,000  
`m4n-*-28`2 | 280,000 | 5,000  
`m4n-*-32`2 | 320,000 | 6,000  
`m4n-*-56`2 | 400,000 | 10,000  
`m4n-*-64`2 | 420,000 | 11,500  
`m4n-*-112`2 | 500,000 | 12,500  
`m4n-*-224`2,3 | 1,000,000 | 25,000  
N2   
`n2-*-80`1 | 160,000 | 5,000  
`n2-*-96` | 160,000 | 5,000  
`n2-*-128` | 160,000 | 5,000  
X4   
`x4-480-*-metal`1 | 400,000 | 10,000  
`x4-960-*-metal`1 | 400,000 | 10,000  
`x4-1440-24t-metal`1 | 400,000 | 10,000  
`x4-1920-32t-metal`1 | 400,000 | 10,000  
X5   
`x5-*-688-metal` | 1,000,000 | 25,000  
`x5-*-1376-metal` | 1,000,000 | 25,000  
`x5-*-2064-metal` | 1,000,000 | 25,000  
Z3 1  
`z3-*-88`1 | 350,000 | 5,000  
`z3-*-176`1 | 350,000 | 5,000  
`z3-*-192-metal`1 | 500,000 | 10,000  
Z4D 2  
`z4d-*-64`2 | 200,000 | 5,000  
`z4d-*-96`2 | 250,000 | 6,250  
`z4d-*-192`2 | 500,000 | 12,500  
`z4d-*-384`2,3 | 1,000,000 | 25,000  
`z4d-*-384-metal`2,3 | 1,000,000 | 25,000  
Z4M 2  
`z4m-*-48`2 | 125,000 | 3,125  
`z4m-*-192`2,3 | 500,000 | 12,500  
`z4m-*-192-metal`2,3 | 500,000 | 12,500  
  
1 If using Hyperdisk Extreme with an instance that uses Microsoft Windows, refer to the [known issues for Windows VM instances](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#known_issues_for_windows_vm_instances).  
2 Also offers steady state performance. For more information, see [Performance limits for machine types with steady state performance](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#steady-state).  
3 The disk performance for this machine type is based on having 2 physical NICs per instance. Compute Engine automatically maps attached disks to a physical NIC in a balanced round-robin fashion.  


## Share a Hyperdisk Extreme volume between VMs

You can use multi-writer mode to simultaneously attach a Hyperdisk Extreme volume to multiple instances, while each instance maintains write access. This feature enables high availability for workloads like Microsoft SQL Server Failover Cluster Infrastructure.

To learn more, see [Share a disk between VMs](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms).

## Disaster protection for Hyperdisk Extreme volumes

You can back up a Hyperdisk Extreme volume with [instant snapshots](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots) and [standard snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots). Snapshots back up the data on a Hyperdisk Extreme volume at a specific point in time.

You can protect your data in the unlikely event of a regional outage by enabling Asynchronous Replication. Asynchronous Replication maintains a copy of the data on your volume in another region. For example, to protect a Hyperdisk Extreme volume in `us-west1`, you can use Asynchronous Replication to replicate the volume to a secondary volume in the `us-east4` region. If the volume in `us-west1` became unavailable, then you could use the secondary volume in `us-east4`. 

### Cross-zonal replication

Hyperdisk Extreme volumes are always zonal and you can't replicate Hyperdisk Extreme volumes to another zone. To replicate data to another zone within the same region, you must use [Hyperdisk Balanced High Availability](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha) volumes. 

To create a Hyperdisk Balanced High Availability volume from an existing Hyperdisk Extreme volume, see [Creating a regional clone of a zonal disk](https://docs.cloud.google.com/compute/docs/disks/clone-duplicate-disks#zonal-to-regional).

## Regional availability for Hyperdisk Extreme

Hyperdisk Extreme is available in all zones and regions.

## Limitations

Hyperdisk Extreme volumes have the following limitations:

  * Hyperdisk Extreme volumes are zonal and can be accessed from only the zone where they are located.
  * Except for network-optimized instances such as C4N, Hyperdisk Extreme volumes can only be attached to machines with 60 or more vCPUs.
  * You can't create an image from a Hyperdisk Extreme volume.
  * You can't create a machine image from a Hyperdisk Extreme volume.
  * You can't use a Hyperdisk Extreme volume as a boot disk.
  * You can change a Hyperdisk Extreme volume's size and performance every 4 hours.
  * Windows instances running on `n2-standard-80` machine types can reach at most 80,000 IOPS across all Hyperdisk Extreme volumes that are attached to the instance. To reach up to 160,000 IOPS with N2 instances running Windows, choose one of the following machine types:

    * `n2-highmem-80`
    * `n2-highcpu-80`
    * `n2-standard-96`
    * `n2-highmem-96`
    * `n2-highcpu-96`
    * `n2-highmem-128`
    * `n2-standard-128`



## What's next

  * [Add a Hyperdisk volume to your VM](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
