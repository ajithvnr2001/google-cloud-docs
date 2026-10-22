---
url: https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced/
title: About Hyperdisk Balanced \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:41:37.052689+00:00
---

# About Hyperdisk Balanced  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About Hyperdisk Balanced Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the features of Hyperdisk Balanced, the general-purpose Hyperdisk type. Hyperdisk Balanced is the best fit for most workloads and offers the best combination of price and performance for total cost of ownership. For more information about Hyperdisk and the other Hyperdisk types, see [About Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).

You can specify up to 160,000 IOPS and 2,400 MiB/s of throughput for a single Hyperdisk Balanced volume. Hyperdisk Balanced is designed for sub-millisecond latencies.

To create a new Hyperdisk Balanced volume, see [Create a Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk).

## Use cases

Hyperdisk Balanced is a good fit for most workloads, including the following use cases:

  * Databases, like MySQL and PostgreSQL
  * Virtual Desktop Infrastructure (VDI)
  * Line of business (LOB) applications
  * Instance boot disks, if the machine series or TPU supports only Hyperdisk. The boot disk for such instances must be a Hyperdisk Balanced or Hyperdisk Balanced High Availability volume.



## Machine series support

You can use Hyperdisk Balanced with the following machine series:

  * [A3 (H100)](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus)
  * [A3 (H200)](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus)
  * [A4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms)
  * [A4X](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms)
  * [A4X Max](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms)
  * [C2D](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#c2d_machine_types)1
  * [C3](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_series)
  * [C3D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3d_machine_types)
  * [C4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series)
  * [C4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series)
  * [C4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4d_series)
  * [C4N](https://docs.cloud.google.com/compute/docs/network-optimized-machines#c4n_series)
  * [E2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#e2_machine_types)1
  * [G4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series)
  * [H3](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h3_series)
  * [H4D](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_series)
  * [M1](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m1_machine_types)
  * [M2](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m2_machine_types)
  * [M3](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m3_machine_types)
  * [M4](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m4_machine_types)
  * [M4N](https://docs.cloud.google.com/compute/docs/network-optimized-machines#m4n_series)
  * [N1](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_machines)1
  * [N2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_series)1
  * [N2D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2d_machines)1
  * [N4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4_series)
  * [N4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series)
  * [N4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4d_series)
  * [TPU v6e](https://docs.cloud.google.com/tpu/docs/v6e)
  * [TPU7x](https://docs.cloud.google.com/tpu/docs/tpu7x)
  * [X4](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x4_series)
  * [X5](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x5_series)
  * [Z3](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_series)
  * [Z4D](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4d_series)
  * [Z4M](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4m_series)



1To design your workload for flexibility and use Hyperdisk Balanced or Hyperdisk Balanced High Availability with this machine series, [contact your account team](https://docs.cloud.google.com/tam). 

### Design for flexibility on older machine series

Hyperdisk Balanced and Hyperdisk Balanced High Availability are also available with select previous generation machine families to help you design for flexibility across multiple generations.

  * Hyperdisk Balanced and Hyperdisk Balanced High Availability on previous generations are intended for long-term disks that will survive beyond the duration of the instance.

  * For use-cases in which the life of the disk coincides with the life of the instance, for example a boot disk, use the block storage defaults: Persistent Disk with 1st- and 2nd-generation machine series, and Hyperdisk with more recent generation instances. For example, if you need a boot disk with an N2 instance, then you should use a Balanced or SSD Persistent Disk volume instead of a Hyperdisk volume.




To use Hyperdisk Balanced with these machine series, [contact your account team](https://docs.cloud.google.com/tam).

## About provisioned performance for Hyperdisk Balanced

You don't have to provision performance when you create Hyperdisk volumes. If you don't provision performance, Compute Engine creates the volume with default values that you can modify later. For details about default values, see Default IOPS and throughput values. 

If you know your performance needs, you can specify IOPS and throughput limits for a Hyperdisk Balanced volume when you create the volume, and you can change the provisioned values after you create the volume. You can't specify an IOPS or throughput level if you don't specify a size.

**Important:** A Hyperdisk volume can't reach its provisioned performance unless you attach it to a compute instance that supports that level of performance, or higher. For detailed performance limits for all supported instances by machine type, see Performance limits when attached to an instance. 

### Size and performance limits

The following limits apply to the size, IOPS, and throughput values you can specify for a Hyperdisk Balanced volume.

  * Size: between 4 GiB and 64 TiB. The default size is 100 GiB.

**[Preview](https://cloud.google.com/products#product-launch-stages)** : C4 supports a maximum Hyperdisk Balanced volume size of 128 TiB. For access to this feature, contact [hyperdisk-questions@google.com](mailto:hyperdisk-questions@google.com). 
  * IOPS: between 3,000 and 160,000 IOPS. For volumes less than 320 GiB, the range of IOPS values you can specify varies by size. For details, see Limits for provisioned IOPS.

  * Throughput: between 140 and 2,400 MiB/s of throughput, but the throughput value depends on how much IOPS you provision. For details, see Limits for provisioned throughput.




### Limits for provisioned IOPS

You can choose the IOPS limit for a Hyperdisk Balanced volume according to the following limits. The minimum and maximum limits vary by size.

  * Minimum configurable IOPS: 
    * 4 or 5 GiB volumes: IOPS is fixed at 2,000 and 2,500 IOPS, respectively.
    * 6 GiB to 64 TiB: at least 3,000 IOPS.
  * Maximum configurable IOPS: 
    * 6 to 319 GiB volumes: the maximum IOPS limit depends on the volume's size. See the following table for more information.
    * 320 GiB to 64 TiB volumes: at most 160,000 IOPS.



To calculate the range of configurable IOPS values for a specific volume size, use these formulas:

  * Minimum IOPS: 3,000 IOPS  

  * Maximum IOPS: `MIN (500x, 160,000)` MiB/s, where `x` is the volume's size.



The following table lists the limits for configurable IOPS for common volume sizes.

Size (GiB) | Configurable IOPS values  
---|---  
4 | 2,000  
5 | 2,500  
10 | 3,000 to 5,000  
50 | 3,000 to 25,000  
150 | 3,000 to 75,000  
319 | 3,000 to 159,500  
320 or more | 3,000 to 160,000  
  
### Limits for provisioned throughput

The throughput limit that you specify must be within a range of allowed values. The range depends on the volume's provisioned IOPS. To determine the range of throughput limits for a given IOPS value `P`, use the following formulas.

  * Minimum throughput: `MAX (140, P/256)` MiB/s
  * Maximum throughput: `MIN (2,400, P/4)` MiB/s



The following table lists the limits for some provisioned IOPS values and the corresponding throughput ranges. If a size isn't listed, use the preceding formula to calculate the allowable values.

Provisioned IOPS | Configurable throughput (MiB/s)  
---|---  
2,000 | 140 to 500  
2,500 | 140 to 625  
3,000 | 140 to 750  
4,000 | 140 to 1,000  
8,000 | 140 to 2,000  
32,000 | 140 to 2,400  
40,000 | 156 to 2,400  
64,000 | 250 to 2,400  
150,000 | 585 to 2,400  
160,000 | 625 to 2,400  
  
### Default size, IOPS, and throughput values

If you don't specify a size, IOPS, or throughput value when you create a Hyperdisk Balanced volume, Compute Engine assigns default values.

The default size for Hyperdisk Balanced volumes is 100 GiB.

The default IOPS and throughput are based on the following formulas, where `x` is the volume's size in GiB.

  * Default IOPS: 
    * Volumes 6 GiB or less: `500x`IOPS
    * Volumes between 6 GiB and 26.666667 TiB: `6x + 3,000` IOPS
    * Volumes larger than 26.666667 TiB: 160,000 IOPS
  * Default throughput: 
    * Volumes 6 GiB or less: `140` MiB/s
    * Volumes larger than 6 GiB: `MIN (2,400, (1.5x + 140))` MiB/s

**Important:** A Hyperdisk volume can't reach its provisioned performance unless you attach it to a compute instance that supports that level of performance, or higher. For detailed performance limits for all supported instances by machine type, see Performance limits when attached to an instance. 

## Baseline performance

Hyperdisk Balanced volumes include baseline, or free performance. The first 3,000 IOPS and 140 MiB/s of throughput that you provision for a volume are free. Performance you provision above the baseline amounts is _billable performance_ , and is not free. If you provision a volume with 5,000 IOPS, you're billed for 2,000 IOPS. Similar principles apply to throughput. 

Baseline performance is also included with Hyperdisk Balanced volumes that you create in the following Hyperdisk Storage Pools:

  * Standard performance Hyperdisk Storage Pools
  * Standard capacity Hyperdisk Storage Pools
  * Advanced capacity Hyperdisk Storage Pools



Hyperdisk Balanced volumes in Advanced performance Hyperdisk Storage Pools don't include baseline performance.

### Baseline performance and quota

Baseline IOPS and throughput don't affect the IOPS and throughput quota for a project's Hyperdisk Balanced and Hyperdisk Balanced High Availability volumes.

For example, if your project has a quota of 500,000 IOPS and you create a Hyperdisk Balanced volume with 3,000 IOPS, then you still have a quota of 500,000 IOPS after you create the volume. If you also create a Hyperdisk Balanced High Availability volume with 4,000 IOPS, then the project would have a remaining IOPS quota of 499,000.

## Change the provisioned performance or size

You can change the provisioned size of a Hyperdisk Balanced volume at most twice within a 4-hour window, and you can change the provisioned performance at most once every 4 hours. To learn how to modify size or performance, see [Modify the size and provisioned performance of a Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks).

## Hyperdisk Balanced performance limits when attached to an instance

This section lists the performance limits for each machine type that supports Hyperdisk Balanced. You can specify up to 160,000 IOPS and 2,400 MiB/s of throughput for a single Hyperdisk Balanced volume. 

This section lists the maximum performance that Hyperdisk Balanced volumes can achieve for each supported instance. A Hyperdisk Balanced volume's performance when it's attached to an instance can't exceed the limits for the instance's machine type. The performance limits are also shared across all Hyperdisk Balanced volumes attached to the same instance, regardless of each volume's provisioned performance. 

### Achieve higher performance with multiple Hyperdisk Balanced volumes

If an instance's performance limit exceeds 160,000 IOPS or 2,400 MiB/s, then the instance can only achieve that limit if you attach multiple Hyperdisk Balanced volumes. For example, the performance limit for a `c4a-*-72` instance using Hyperdisk Balanced is 240,000 IOPS and 5,000 MiB/s. To achieve this maximum performance you must attach at least two Hyperdisk Balanced volumes to the instance. 

**Important:** To reach the IOPS limits, you must use an I/O size of 4 KB. Maximum throughput limits require an I/O size of at least 256 KB.   
Hyperdisk performance is half-duplex, so the IOPS and throughput limits are shared between read and write operations. This means that if a machine type has a 50,000 IOPS limit, then the sum of the reads and writes every second can't exceed 50,000. 

The performance limits also apply to [custom machine types](https://docs.cloud.google.com/compute/docs/machine-resource#custom-types). 

Instance machine type | Maximum IOPS | Maximum throughput (MiB/s)  
---|---|---  
A3 (A3+H100)   
`a3-megagpu-8g` | 160,000 | 4,800  
`a3-highgpu-1g` | 120,000 | 1,800  
`a3-highgpu-2g` | 160,000 | 2,400  
`a3-highgpu-4g` | 160,000 | 4,800  
`a3-highgpu-8g` | 160,000 | 4,800  
`a3-edgegpu-8g` | 160,000 | 4,800  
A3 (A3+H200)   
`a3-ultragpu-8g`1 | 320,000 | 10,000  
A4 1  
`a4-highgpu-8g`1 | 320,000 | 10,000  
A4X 1  
`a4x-highgpu-4g`1 | 320,000 | 10,000  
A4X Max 1  
`a4x-maxgpu-4g-metal`1 | 320,000 | 12,500  
C3   
`c3-*-4` | 25,000 | 400  
`c3-*-8` | 50,000 | 800  
`c3-*-22` | 120,000 | 1,800  
`c3-*-44` | 160,000 | 2,400  
`c3-*-88` | 160,000 | 4,800  
`c3-*-176` | 160,000 | 10,000  
`c3-*-192-metal` | 160,000 | 10,000  
C3D   
`c3d-*-4` | 25,000 | 400  
`c3d-*-8` | 50,000 | 800  
`c3d-*-16` | 75,000 | 1,200  
`c3d-*-30` | 75,000 | 1,200  
`c3d-*-60` | 160,000 | 2,400  
`c3d-*-90` | 160,000 | 2,400  
`c3d-*-180` | 160,000 | 2,400  
`c3d-*-360` | 160,000 | 2,400  
C4 1  
`c4-*-2`1 | 50,000 | 400  
`c4-*-4`1 | 50,000 | 400  
`c4-*-8`1 | 50,000 | 800  
`c4-*-16`1 | 100,000 | 1,600  
`c4-*-24`1 | 100,000 | 1,600  
`c4-*-32`1 | 100,000 | 1,600  
`c4-*-48`1 | 160,000 | 2,400  
`c4-*-96`1 | 240,000 | 4,800  
`c4-*-144`1 | 240,000 | 6,250  
`c4-*-192`1 | 320,000 | 10,000  
`c4-*-288`1 | 320,000 | 12,500  
`c4-*-288-metal`1 | 320,000 | 12,500  
C4A   
`c4a-*-1` | 25,000 | 400  
`c4a-*-2` | 50,000 | 800  
`c4a-*-4` | 50,000 | 800  
`c4a-*-8` | 50,000 | 1,000  
`c4a-*-16` | 80,000 | 1,600  
`c4a-*-32` | 120,000 | 2,400  
`c4a-*-48` | 160,000 | 3,300  
`c4a-*-64` | 240,000 | 4,400  
`c4a-*-72` | 240,000 | 5,000  
`c4a-*-96-metal` | 240,000 | 5,000  
C4D 1  
`c4d-*-2`1 | 22,500 | 400  
`c4d-*-4`1 | 50,000 | 400  
`c4d-*-8`1 | 50,000 | 800  
`c4d-*-16`1 | 75,000 | 1,200  
`c4d-*-32`1 | 75,000 | 1,600  
`c4d-*-48`1 | 75,000 | 1,600  
`c4d-*-64`1 | 160,000 | 2,400  
`c4d-*-96`1 | 160,000 | 3,125  
`c4d-*-192`1 | 240,000 | 6,250  
`c4d-*-384`1 | 320,000 | 12,500  
`c4d-*-384-metal`1 | 320,000 | 10,000  
C4N 1,2  
`c4n-*-2`1 | 50,000 | 800  
`c4n-*-4`1 | 50,000 | 800  
`c4n-*-8`1 | 100,000 | 1,600  
`c4n-*-16`1 | 150,000 | 2,800  
`c4n-*-24`1 | 180,000 | 3,200  
`c4n-*-48`1 | 280,000 | 6,250  
`c4n-*-96`1 | 320,000 | 10,000  
`c4n-*-192`1,2 | 640,000 | 20,000  
G4   
`g4-standard-6` | 50,000 | 400  
`g4-standard-12` | 50,000 | 800  
`g4-standard-24` | 75,000 | 1,200  
`g4-standard-48` | 75,000 | 1,600  
`g4-standard-96` | 160,000 | 2,800  
`g4-standard-192` | 240,000 | 4,800  
`g4-standard-384` | 320,000 | 10,000  
H3   
`h3-standard-88` | 15,000 | 240  
H4D 1  
`h4d-*-192`1 | 15,000 | 240  
M1   
`m1-ultramem-40` | 60,000 | 1,200  
`m1-ultramem-80` | 100,000 | 2,400  
`m1-megamem-96` | 100,000 | 4,000  
`m1-ultramem-160` | 100,000 | 4,000  
M2   
`m2-*-208` | 100,000 | 2,400  
`m2-*-416` | 100,000 | 4,000  
M3   
`m3-*-32` | 160,000 | 2,400  
`m3-*-64` | 160,000 | 4,800  
`m3-*-128` | 160,000 | 4,800  
M4 1  
`m4-*-16`1 | 100,000 | 1,600  
`m4-*-28`1 | 100,000 | 1,600  
`m4-*-32`1 | 120,000 | 1,800  
`m4-*-56`1 | 160,000 | 3,125  
`m4-*-64`1 | 180,000 | 3,600  
`m4-*-112`1 | 240,000 | 5,000  
`m4-*-224`1 | 320,000 | 10,000  
M4N 1,2  
`m4n-*-2`1 | 50,000 | 800  
`m4n-*-4`1 | 50,000 | 800  
`m4n-*-8`1 | 100,000 | 900  
`m4n-*-16`1 | 120,000 | 1,800  
`m4n-*-28`1 | 125,000 | 3,125  
`m4n-*-32`1 | 144,000 | 3,600  
`m4n-*-56`1 | 200,000 | 6,250  
`m4n-*-64`1 | 280,000 | 7,200  
`m4n-*-112`1 | 320,000 | 10,000  
`m4n-*-224`1,2 | 640,000 | 20,000  
N4   
`n4-*-2` | 30,000 | 240  
`n4-*-4` | 30,000 | 240  
Custom N4 types with 6 vCPUs | 30,000 | 240  
`n4-*-8` | 30,000 | 480  
Custom N4 types with 10 to 14 vCPUs | 30,000 | 480  
`n4-*-16` | 80,000 | 1,200  
Custom N4 types with 18 to 30 vCPUs | 80,000 | 1,200  
`n4-*-32` | 100,000 | 1,600  
Custom N4 types with 34 to 46 vCPUs | 100,000 | 1,600  
`n4-*-48` | 160,000 | 2,400  
Custom N4 types with 50 to 62 vCPUs | 160,000 | 2,400  
`n4-*-64` | 160,000 | 2,400  
Custom N4 types with 66 to 78 vCPUs | 160,000 | 2,400  
`n4-*-80` | 160,000 | 2,400  
N4A   
`n4a-*-1` | 15,000 | 240  
`n4a-*-2` | 30,000 | 240  
Custom N4A types with 3 vCPUs | 30,000 | 240  
`n4a-*-4` | 30,000 | 240  
Custom N4A types with 5 to 7 vCPUs | 30,000 | 240  
`n4a-*-8` | 30,000 | 480  
Custom N4A types with 9 to 15 vCPUs | 30,000 | 480  
`n4a-*-16` | 80,000 | 1,200  
Custom N4A types with 17 to 31 vCPUs | 80,000 | 1,200  
`n4a-*-32` | 100,000 | 1,600  
Custom N4A types with 33 to 47 vCPUs | 100,000 | 1,600  
`n4a-*-48` | 160,000 | 2,400  
Custom N4A types with 49 to 63 vCPUs | 160,000 | 2,400  
`n4a-*-64` | 160,000 | 2,400  
N4D   
`n4d-*-2` | 30,000 | 240  
`n4d-*-4` | 30,000 | 240  
`n4d-*-8` | 30,000 | 480  
`n4d-*-16` | 80,000 | 1,200  
`n4d-*-32` | 100,000 | 1,600  
`n4d-*-48` | 160,000 | 2,400  
`n4d-*-64` | 160,000 | 2,400  
`n4d-*-80` | 160,000 | 2,400  
`n4d-*-96` | 160,000 | 2,400  
TPU v6e   
`ct6e-standard-1t` | 75,000 | 1,200  
`ct6e-standard-4t` | 160,000 | 2,400  
`ct6e-standard-8t` | 160,000 | 2,400  
TPU7x 1  
`tpu7x-standard-4t`1 | 320,000 | 6,000  
X4   
`x4-*-480-metal` | 160,000 | 4,800  
`x4-*-960-metal` | 160,000 | 4,800  
`x4-24t-1440-metal` | 160,000 | 4,800  
`x4-32t-1920-metal` | 160,000 | 4,800  
X5   
`x5-*-688-metal` | 640,000 | 20,000  
`x5-*-1376-metal` | 640,000 | 20,000  
`x5-*-2064-metal` | 640,000 | 20,000  
Z3   
`z3-*-8` | 50,000 | 800  
`z3-*-14` | 100,000 | 1,600  
`z3-*-16` | 100,000 | 1,600  
`z3-*-22` | 120,000 | 1,800  
`z3-*-32` | 160,000 | 2,400  
`z3-*-44` | 160,000 | 2,400  
`z3-*-88` | 160,000 | 4,800  
`z3-*-176` | 160,000 | 4,800  
`z3-*-192-metal` | 160,000 | 4,800  
Z4D 1  
`z4d-*-8`1 | 50,000 | 800  
`z4d-*-16`1 | 75,000 | 1,200  
`z4d-*-32`1 | 100,000 | 2,100  
`z4d-*-48`1 | 125,000 | 3,200  
`z4d-*-64`1 | 160,000 | 4,200  
`z4d-*-96`1 | 160,000 | 6,250  
`z4d-*-192`1 | 320,000 | 12,500  
`z4d-*-384`1,2 | 640,000 | 25,000  
`z4d-*-384-metal`1,2 | 640,000 | 25,000  
Z4M 1  
`z4m-*-16`1 | 75,000 | 1,600  
`z4m-*-32`1 | 100,000 | 2,100  
`z4m-*-48`1 | 125,000 | 3,125  
`z4m-*-192`1,2 | 320,000 | 12,500  
`z4m-*-192-metal`1,2 | 320,000 | 12,500  
  
1 Also offers steady state performance. For more information, see [Performance limits for machine types with steady state performance](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#steady-state).  
2 The disk performance for this machine type is based on having 2 physical NICs per instance. Compute Engine automatically maps attached disks to a physical NIC in a balanced round-robin fashion.  


## Disaster recovery protection for Hyperdisk Balanced volumes

You can back up a Hyperdisk Balanced volume with [instant snapshots](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots) and [standard snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots). Snapshots back up the data on a Hyperdisk Balanced volume at a specific point in time.

### Replication across multiple regions

You can protect your data in the unlikely event of a regional outage by enabling Asynchronous Replication. Asynchronous Replication maintains a copy of the data on your volume in another region. For example, to protect a Hyperdisk Balanced volume in `us-west1`, you can use Asynchronous Replication to replicate the volume to a secondary volume in the `us-east4` region. If the volume in `us-west1` became unavailable, then you could use the secondary volume in `us-east4`. 

### Cross-zonal replication

Hyperdisk Balanced volumes are always zonal and you can't replicate Hyperdisk Balanced volumes to another zone. To replicate data to another zone within the same region, you must use [Hyperdisk Balanced High Availability](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha) volumes. 

To create a Hyperdisk Balanced High Availability volume from an existing Hyperdisk Balanced volume, see [Creating a regional clone of a zonal disk](https://docs.cloud.google.com/compute/docs/disks/clone-duplicate-disks#zonal-to-regional).

## Regional availability for Hyperdisk Balanced

Hyperdisk Balanced is available in all zones and regions.

## Hyperdisk Balanced Storage Pools

To simplify planning, avoid overprovisioning storage, and reduce costs, consider using Hyperdisk Balanced Storage Pools. Hyperdisk Balanced Storage Pools let you purchase Hyperdisk Balanced storage and performance in bulk. To learn more, see [About Hyperdisk Storage Pools](https://docs.cloud.google.com/compute/docs/disks/storage-pools).

## Share a Hyperdisk Balanced volume between VMs

You can use multi-writer mode to attach a Hyperdisk Balanced volume to multiple instances, while each instance maintains write access. This feature enables high availability for workloads like Microsoft SQL Server Failover Cluster Infrastructure.

To learn more, see [Share a disk between VMs](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms).

## Pricing

You are billed for the total provisioned size, IOPS, and throughput of your Hyperdisk Balanced volumes until you delete them. Charges incur even if the volume isn't attached to any instances or if the instance is suspended or stopped. For more information see [Disk pricing](https://docs.cloud.google.com/compute/disks-image-pricing#disk).

## Limitations for Hyperdisk Balanced

  * Hyperdisk Balanced volumes are zonal and can only be accessed from the zone where the volume was created. If you need to access a Hyperdisk volume from more than one zone, create a Hyperdisk Balanced High Availability volume.
  * You can't create a [machine image](https://docs.cloud.google.com/compute/docs/machine-images) from a Hyperdisk volume.
  * Hyperdisk Balanced volumes in multi-writer mode have additional [limitations](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms#mw-limitations).
  * Hyperdisk Balanced volumes in Confidential mode have additional [limitations](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#limitations).
  * You can change a Hyperdisk Balanced volume's performance every 4 hours. You can change its provisioned size at most twice within a 4-hour window.



## What's next

  * [Add a Hyperdisk Balanced volume to your VM](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk)
  * Learn about [Hyperdisk Storage Pools](https://docs.cloud.google.com/compute/docs/disks/storage-pools)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
