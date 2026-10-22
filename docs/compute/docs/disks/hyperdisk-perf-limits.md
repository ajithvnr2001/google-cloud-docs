---
url: https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits/
title: Performance limits for machine series that support Hyperdisk \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:41:40.371242+00:00
---

# Performance limits for machine series that support Hyperdisk  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Performance limits for machine series that support Hyperdisk Stay organized with collections  Save and categorize content based on your preferences. 

To meet your workload's specific IOPS and throughput requirements, both the Google Cloud Hyperdisk type and the machine type that your workload uses must support that level of performance or higher. This document lists performance limits by machine series and Google Cloud Hyperdisk type.

For a detailed discussion of how Hyperdisk performance works, see [About Hyperdisk performance](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-performance).

For Persistent Disk performance limits, see [Performance limits by machine type for Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/performance#machine-type-disk-limits).

## Determine which limits apply

The performance limit that applies to your scenario depends on the instance's machine type, and the number and type of Hyperdisk volumes you attached to the instance.

Choose from the following scenarios to determine which limits to consult.

  * You're using multiple Hyperdisk types with the same instance and you want to know the maximum performance for all the disks attached to the instance.

For example, suppose you have one Hyperdisk Balanced volume and two Hyperdisk Throughput volumes attached to a C3 virtual machine (VM) instance that has 22 vCPUs. The applicable performance limits are listed in the Performance limits by machine type section of this document.

  * You attached one or more Hyperdisk volumes of the same type to an instance and you want to know the maximum performance all the volumes can reach.

For example, suppose you attached three Hyperdisk Balanced volumes to a C3 instance that has 8 vCPUs. The applicable performance limits for the three volumes are listed in the Performance limits by Hyperdisk type section of this document.




## Terminology

In this document, machine types are denoted in this format: `M-*-N`, where: 

  * `M` is the machine series, for example, `C3`
  * `*` represents all memory and CPU configurations, for example, `standard` or `highcpu`
  * `N` is the number of vCPUs, CPUs, or the GPU designation, for example, 22 for an instance with 22 vCPUs, or `8g` for an instance with 8 GPUs 

This format includes the following machine types, wherever available: 
  * bare metal machine types (`*-metal`)
  * machine types that come with attached Local SSD disks (`*-lssd`, `*-standardlssd`, or `*-highlssd`).



For example, `c3-*-176` refers to C3 machine types with 176 vCPUs, like `c3-standard-176`, `c3-highcpu-176`, `c3-highmem-176`, and `c3-standard-176-lssd`. For more information, see [Compute Engine terminology](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology). 

## Performance limits by machine type

If you use different Hyperdisk types with a single instance, the following table lists the maximum performance you can expect. This limit is shared among all Hyperdisk and, if supported, Persistent Disk volumes attached to the instance. To learn more about how these limits work, see [How instance performance limits affect performance](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-performance#instance-perf-limits).

The performance limits also apply to [custom N2, N2D, N4, N4A, and N4D machine types](https://docs.cloud.google.com/compute/docs/machine-resource#custom-types).

Select a machine series to display the performance limits for its machine types.

A2A3 (H100)A3 (H200)A4A4XA4X MaxC3C3DC4C4AC4DC4NG2G4H3H4DM1M2M3M4M4NN2N2DN4N4AN4DT2DTPU v6eTPU7xX4X5Z3Z4DZ4MInstance machine type | Maximum IOPS | Maximum throughput (MiB/s)  
---|---|---  
A2   
`a2-ultragpu-1g` | 30,000 | 1,800  
`a2-ultragpu-2g` | 60,000 | 2,400  
`a2-ultragpu-4g` | 120,000 | 2,400  
`a2-ultragpu-8g` | 160,000 | 4,800  
A3 (H100)   
`a3-edgegpu-8g` | 400,000 | 8,000  
`a3-highgpu-1g` | 120,000 | 1,800  
`a3-highgpu-2g` | 160,000 | 2,400  
`a3-highgpu-4g` | 350,000 | 5,000  
`a3-highgpu-8g` | 400,000 | 8,000  
`a3-megagpu-8g` | 400,000 | 8,000  
A3 (H200) 1  
`a3-ultragpu-8g`1 | 500,000 | 10,000  
A4 1  
`a4-highgpu-8g` | 500,000 | 10,000  
A4X   
`a4x-highgpu-4g` | 500,000 | 10,000  
A4X Max   
`a4x-maxgpu-4g-metal` | 500,000 | 12,500  
C3   
`c3-*-4` | 25,000 | 400  
`c3-*-8` | 50,000 | 800  
`c3-*-22` | 120,000 | 1,800  
`c3-*-44` | 160,000 | 2,400  
`c3-*-88` | 350,000 | 5,000  
`c3-*-176` | 500,000 | 10,000  
`c3-*-192-metal` | 500,000 | 10,000  
C3D   
`c3d-*-4` | 25,000 | 400  
`c3d-*-8` | 50,000 | 800  
`c3d-*-16` | 75,000 | 1,200  
`c3d-*-30` | 93,750 | 1,200  
`c3d-*-60` | 350,000 | 5,000  
`c3d-*-90` | 350,000 | 5,000  
`c3d-*-180` | 350,000 | 5,000  
`c3d-*-360` | 350,000 | 5,000  
C4 1  
`c4-*-2`1 | 50,000 | 400  
`c4-*-4`1 | 50,000 | 400  
`c4-*-8`1 | 50,000 | 800  
`c4-*-16`1 | 100,000 | 1,600  
`c4-*-24`1 | 100,000 | 1,600  
`c4-*-32`1 | 100,000 | 1,600  
`c4-*-48`1 | 160,000 | 2,400  
`c4-*-96`1 | 350,000 | 5,000  
`c4-*-144`1 | 350,000 | 5,000  
`c4-*-192`1 | 500,000 | 10,000  
`c4-*-288`1 | 500,000 | 12,500  
`c4-*-288-lssd-metal`1 | 400,000 | 12,500  
C4A   
`c4a-*-1` | 25,000 | 400  
`c4a-*-2` | 50,000 | 800  
`c4a-*-4` | 50,000 | 800  
`c4a-*-8` | 50,000 | 1,000  
`c4a-*-16` | 80,000 | 1,600  
`c4a-*-32` | 120,000 | 2,400  
`c4a-*-48` | 160,000 | 3,300  
`c4a-*-64` | 350,000 | 5,000  
`c4a-*-72` | 350,000 | 5,000  
`c4a-*-96-metal` | 350,000 | 5,000  
C4D 1  
`c4d-*-2`1 | 22,500 | 400  
`c4d-*-4`1 | 50,000 | 400  
`c4d-*-8`1 | 50,000 | 800  
`c4d-*-16`1 | 75,000 | 1,200  
`c4d-*-32`1 | 75,000 | 1,600  
`c4d-*-48`1 | 75,000 | 1,600  
`c4d-*-64`1 | 350,000 | 5,000  
`c4d-*-96`1 | 350,000 | 5,000  
`c4d-*-192`1 | 350,000 | 5,000  
`c4d-*-384`1 | 500,000 | 10,000  
C4N 1  
`c4n-*-2` | 80,000 | 1,000  
`c4n-*-4` | 100,000 | 1,000  
`c4n-*-8` | 120,000 | 1,800  
`c4n-*-16` | 160,000 | 3,000  
`c4n-*-24` | 240,000 | 4,000  
`c4n-*-48` | 380,000 | 8,000  
`c4n-*-96` | 500,000 | 12,500  
`c4n-*-192` | 1,000,000 | 25,000  
G2   
`g2-standard-4` | 15,000 | 800  
`g2-standard-8` | 19,200 | 1,200  
`g2-standard-12` | 28,800 | 1,800  
`g2-standard-16` | 38,400 | 2,400  
`g2-standard-24` | 38,400 | 2,400  
`g2-standard-32` | 60,000 | 2,400  
`g2-standard-48` | 60,000 | 2,400  
`g2-standard-96` | 100,000 | 2,400  
G4   
`g4-standard-6` | 50,000 | 400  
`g4-standard-12` | 50,000 | 800  
`g4-standard-24` | 75,000 | 1,200  
`g4-standard-48` | 75,000 | 1,600  
`g4-standard-96` | 350,000 | 5,000  
`g4-standard-192` | 350,000 | 5,000  
`g4-standard-384` | 500,000 | 10,000  
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
`m3-*-64` | 350,000 | 5,000  
`m3-*-128` | 450,000 | 6,870  
M4 1  
`m4-*-2`1 | 80,000 | 1,000  
`m4-*-4`1 | 100,000 | 1,600  
`m4-*-8`1 | 100,000 | 1,600  
`m4-*-16`1 | 100,000 | 1,600  
`m4-*-28`1 | 100,000 | 1,600  
`m4-*-32`1 | 120,000 | 1,800  
`m4-*-56`1 | 160,000 | 2,400  
`m4-*-64`1 | 200,000 | 3,000  
`m4-*-112`1 | 350,000 | 5,000  
`m4-*-224`1 | 500,000 | 10,000  
M4N 1  
`m4n-*-2` | 80,000 | 1,000  
`m4n-*-4` | 100,000 | 1,000  
`m4n-*-8` | 120,000 | 1,600  
`m4n-*-16` | 160,000 | 3,000  
`m4n-*-28` | 280,000 | 5,000  
`m4n-*-32` | 320,000 | 6,000  
`m4n-*-56` | 400,000 | 10,000  
`m4n-*-64` | 420,000 | 11,500  
`m4n-*-112` | 500,000 | 12,500  
`m4n-*-224` | 1,000,000 | 25,000  
N2   
`n2-*-2` | 15,000 | 240  
`n2-*-4` | 15,000 | 240  
Custom N2 types with 6 vCPUs | 15,000 | 240  
`n2-*-8` | 30,000 | 800  
Custom N2 types with 10 to 14 vCPUs | 30,000 | 800  
`n2-*-16` | 60,000 | 1,200  
Custom N2 types with 18 to 30 vCPUs | 60,000 | 1,200  
`n2-*-32` | 120,000 | 2,400  
Custom N2 types with 36 to 44 vCPUs | 120,000 | 2,400  
`n2-*-48` | 120,000 | 2,400  
Custom N2 types with 52 to 60 vCPUs | 120,000 | 2,400  
`n2-*-64` | 160,000 | 4,800  
Custom N2 types with 68 to 76 vCPUs | 160,000 | 4,800  
`n2-*-80` | 160,000 | 5,000  
`n2-*-96` | 160,000 | 5,000  
`n2-*-128` | 160,000 | 5,000  
N2D   
`n2d-*-2` | 15,000 | 240  
`n2d-*-4` | 15,000 | 240  
`n2d-*-8` | 30,000 | 800  
`n2d-*-16` | 60,000 | 1,200  
`n2d-*-32` | 120,000 | 2,400  
`n2d-*-48` | 120,000 | 2,400  
`n2d-*-64` | 160,000 | 4,800  
`n2d-*-80` | 160,000 | 4,800  
`n2d-*-96` | 160,000 | 4,800  
`n2d-*-128` | 160,000 | 4,800  
`n2d-*-224` | 160,000 | 4,800  
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
T2D   
`t2d-*-1`2 | 15,000 | 240  
`t2d-*-2`2 | 15,000 | 240  
`t2d-*-4`2 | 15,000 | 240  
`t2d-*-8` | 15,000 | 800  
`t2d-*-16` | 25,000 | 1,200  
`t2d-*-32` | 60,000 | 1,200  
`t2d-*-48` | 60,000 | 1,200  
`t2d-*-60` | 60,000 | 1,200  
TPU v6e   
`ct6e-standard-1t` | 75,000 | 1,200  
`ct6e-standard-4t` | 160,000 | 2,400  
`ct6e-standard-8t` | 160,000 | 2,400  
TPU7x 1  
`tpu7x-standard-4t` | 320,000 | 6,000  
X4   
`x4-*-480` | 160,000 | 4,800  
`x4-*-960` | 400,000 | 10,000  
`x4-*-1440` | 400,000 | 10,000  
`x4-*-1920` | 400,000 | 10,000  
X5   
`x5-*-688` | 1,000,000 | 20,000  
`x5-*-1376` | 1,000,000 | 20,000  
`x5-*-2064` | 1,000,000 | 20,000  
`x5-*-2752` | 1,000,000 | 20,000  
Z3   
`z3-*-14` | 100,000 | 1,600  
`z3-*-16` | 100,000 | 1,600  
`z3-*-22` | 120,000 | 1,800  
`z3-*-32` | 160,000 | 2,400  
`z3-*-44` | 160,000 | 2,400  
`z3-*-88` | 350,000 | 5,000  
`z3-*-176` | 350,000 | 5,000  
`z3-*-192-metal` | 500,000 | 10,000  
Z4D 1  
`z4d-*-8`1 | 50,000 | 800  
`z4d-*-16`1 | 75,000 | 1,200  
`z4d-*-32`1 | 100,000 | 2,100  
`z4d-*-48`1 | 125,000 | 3,200  
`z4d-*-64`1 | 350,000 | 5,000  
`z4d-*-96`1 | 350,000 | 6,250  
`z4d-*-192`1 | 500,000 | 12,500  
`z4d-*-384`1 | 1,000,000 | 25,000  
`z4d-*-384-metal`1 | 1,000,000 | 25,000  
Z4M 1  
`z4m-*-16`1 | 75,000 | 1,600  
`z4m-*-32`1 | 100,000 | 2,100  
`z4m-*-48`1 | 125,000 | 3,125  
`z4m-*-192`1 | 500,000 | 12,500  
`z4m-*-192-metal`1 | 500,000 | 12,500  
  
1 Also offers steady state performance. For these limits, see Performance limits for machine types with steady state performance.  
2 The actual throughput limits are 240 MB/s for read operations and 204 MB/s for write operations.  


### Performance limits for machine types with steady state performance

Certain machine types offer steady state performance, a minimum performance level that the instance can sustain. The steady state performance is shared between all volumes attached to the instance. For more information, see [Steady state performance](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-performance#steady-state).

The following table lists the steady state performance limits for the available machine types. If the steady state and maximum performance limits are the same, then the machine type can sustain this performance level in most cases.

#### Steady state performance for Hyperdisk Extreme on network-optimized machine series

Network-optimized machine series, like C4N or M4N, offer higher steady state performance when you attach at least one Hyperdisk Extreme volume to the instance. The following table displays two steady-state performance limits for these machine series. One limit applies when you attach Hyperdisk Extreme volumes to the instance. The other limit applies when no Hyperdisk Extreme volumes are attached.

You can achieve the steady-state limit for the instance even if you attach other Hyperdisk types to the instance. To achieve the steady state limit, the total provisioned performance across all Hyperdisk Extreme volumes that you attach to the instance must be equal to or greater than the steady state limit.

Instance machine type | Steady state IOPS | Steady state  
throughput (MiB/s) | Maximum IOPS | Maximum throughput (MiB/s)  
---|---|---|---|---  
A3 (H200)   
`a3-ultragpu-8g` | 500,000 | 10,000| 500,000 | 10,000  
A4   
`a4-highgpu-8g` | 500,000 | 10,000| 500,000 | 10,000  
C4   
`c4-*-2` | 6,200 | 120| 50,000 | 400  
`c4-*-4` | 12,500 | 240| 50,000 | 400  
`c4-*-8` | 25,000 | 480| 50,000 | 800  
`c4-*-16` | 50,000 | 1,000| 100,000 | 1,600  
`c4-*-24` | 75,000 | 1,200| 100,000 | 1,600  
`c4-*-32` | 100,000 | 1,600| 100,000 | 1,600  
`c4-*-48` | 160,000 | 2,400| 160,000 | 2,400  
`c4-*-96` | 350,000 | 5,000| 350,000 | 5,000  
`c4-*-144` | 350,000 | 5,000| 350,000 | 5,000  
`c4-*-192` | 500,000 | 10,000| 500,000 | 10,000  
`c4-*-288` | 500,000 | 12,500| 500,000 | 12,500  
C4D   
`c4d-*-2` | 2,800 | 65| 22,500 | 400  
`c4d-*-4` | 6,200 | 120| 50,000 | 400  
`c4d-*-8` | 12,500 | 240| 50,000 | 800  
`c4d-*-16` | 25,000 | 480| 75,000 | 1,200  
`c4d-*-32` | 50,000 | 1,000| 75,000 | 1,600  
`c4d-*-48` | 75,000 | 1,400| 75,000 | 1,600  
`c4d-*-64` | 350,000 | 5,000| 350,000 | 5,000  
`c4d-*-96` | 350,000 | 5,000| 350,000 | 5,000  
`c4d-*-192` | 350,000 | 5,000| 350,000 | 5,000  
`c4d-*-384` | 500,000 | 10,000| 500,000 | 10,000  
C4N  | Steady state IOPS   
At least one Hyperdisk Extreme volume attached / None attached | Steady state throughput (MiB/s)   
At least one Hyperdisk Extreme volume attached / None attached | Maximum IOPS | Maximum throughput (MiB/s)  
`c4n-*-2` |  20,000 / 10,420  |  350 / 260  | 80,000 | 1,000  
`c4n-*-4` |  40,000 / 20,840  |  700 / 520  | 100,000 | 1,000  
`c4n-*-8` |  80,000 / 41,670  |  1,400 / 1,050  | 120,000 | 1,800  
`c4n-*-16` |  160,000 / 83,340  |  3,000 / 2,090  | 160,000 | 3,000  
`c4n-*-24` |  240,000 / 125,000  |  4,000 / 3,130  | 240,000 | 4,000  
`c4n-*-48` |  380,000 / 250,000  |  8,000 / 6,250  | 380,000 | 8,000  
`c4n-*-96` |  500,000 / 320,000  |  12,500 / 10,000  | 500,000 | 12,500  
`c4n-*-192` |  1,000,000 / 640,000  |  25,000 / 20,000  | 1,000,000 | 25,000  
H4D   
`h4d-*-192` | 15,000 | 240| 15,000 | 240  
M4   
`m4-*-2` | 50,000 | 1,000| 80,000 | 1,000  
`m4-*-4` | 50,000 | 1,000| 100,000 | 1,600  
`m4-*-8` | 50,000 | 1,000| 100,000 | 1,600  
`m4-*-16` | 50,000 | 1,000| 100,000 | 1,600  
`m4-*-28` | 50,000 | 1,000| 100,000 | 1,600  
`m4-*-32` | 90,000 | 1,600| 120,000 | 1,800  
`m4-*-56` | 160,000 | 2,400| 160,000 | 2,400  
`m4-*-64` | 160,000 | 2,900| 200,000 | 3,000  
`m4-*-112` | 350,000 | 5,000| 350,000 | 5,000  
`m4-*-224` | 500,000 | 10,000| 500,000 | 10,000  
M4N  | Steady state IOPS   
At least one Hyperdisk Extreme volume attached / None attached | Steady state throughput (MiB/s)   
At least one Hyperdisk Extreme volume attached / None attached | Maximum IOPS | Maximum throughput (MiB/s)  
`m4n-*-2` |  160,000 / 72,000  |  3,000 / 1,800  | 80,000 | 1,000  
`m4n-*-4` |  160,000 / 72,000  |  3,000 / 1,800  | 100,000 | 1,000  
`m4n-*-8` |  160,000 / 72,000  |  3,000 / 1,800  | 120,000 | 1,600  
`m4n-*-16` |  160,000 / 72,000  |  3,000 / 1,800  | 160,000 | 3,000  
`m4n-*-28` |  280,000 / 125,000  |  5,000 / 3,125  | 280,000 | 5,000  
`m4n-*-32` |  320,000 / 143,000  |  6,000 / 3,600  | 320,000 | 6,000  
`m4n-*-56` |  400,000 / 250,000  |  10,000 / 6,250  | 400,000 | 10,000  
`m4n-*-64` |  420,000 / 286,000  |  11,500 / 7,200  | 420,000 | 11,500  
`m4n-*-112` |  500,000 / 500,000  |  12,500 / 12,500  | 500,000 | 12,500  
`m4n-*-224` |  1,000,000 / 1,000,000  |  25,000 / 25,000  | 1,000,000 | 25,000  
TPU7x   
`tpu7x-standard-4t` | 320,000 | 6,000| 320,000 | 6,000  
Z4D   
`z4d-*-8` | 20,833 | 520| 50,000 | 800  
`z4d-*-16` | 41,667 | 1,040| 75,000 | 1,200  
`z4d-*-32` | 83,333 | 2,080| 100,000 | 2,100  
`z4d-*-48` | 125,000 | 3,125| 125,000 | 3,200  
`z4d-*-64` | 166,667 | 4,200| 350,000 | 5,000  
`z4d-*-96` | 250,000 | 6,250| 350,000 | 6,250  
`z4d-*-192` | 500,000 | 12,500| 500,000 | 12,500  
`z4d-*-384` | 1,000,000 | 25,000| 1,000,000 | 25,000  
`z4d-*-384-metal` | 1,000,000 | 25,000| 1,000,000 | 25,000  
Z4M   
`z4m-*-16` | 41,667 | 1,040| 75,000 | 1,600  
`z4m-*-32` | 83,333 | 2,083| 100,000 | 2,100  
`z4m-*-48` | 125,000 | 3,125| 125,000 | 3,125  
`z4m-*-192` | 500,000 | 12,500| 500,000 | 12,500  
`z4m-*-192-metal` | 500,000 | 12,500| 500,000 | 12,500  
  
## Performance limits by Hyperdisk type

For the performance limits by machine type for each Hyperdisk type, see the following sections:

  * Hyperdisk Balanced
  * Hyperdisk Balanced High Availability
  * Hyperdisk Extreme
  * Hyperdisk ML
  * Hyperdisk Throughput



### Hyperdisk Balanced performance limits

This section lists the maximum performance that Hyperdisk Balanced volumes can achieve for each supported instance. A Hyperdisk Balanced volume's performance when it's attached to an instance can't exceed the limits for the instance's machine type. The performance limits are also shared across all Hyperdisk Balanced volumes attached to the same instance, regardless of each volume's provisioned performance. 

#### Achieve higher performance with multiple Hyperdisk Balanced volumes

If an instance's performance limit exceeds 160,000 IOPS or 2,400 MiB/s, then the instance can only achieve that limit if you attach multiple Hyperdisk Balanced volumes. For example, the performance limit for a `c4a-*-72` instance using Hyperdisk Balanced is 240,000 IOPS and 5,000 MiB/s. To achieve this maximum performance you must attach at least two Hyperdisk Balanced volumes to the instance. 

To learn more about Hyperdisk Balanced, see [About Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced).

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


### Hyperdisk Balanced High Availability performance limits

This section lists the maximum performance that Hyperdisk Balanced High Availability volumes can achieve for each supported instance. A Hyperdisk Balanced High Availability volume's performance when it's attached to an instance can't exceed the limits for the instance's machine type. The performance limits are also shared across all Hyperdisk Balanced High Availability volumes attached to the same instance, regardless of each volume's provisioned performance. 

#### Achieve higher performance with multiple Hyperdisk Balanced High Availability volumes

Certain instances can exceed the maximum performance for a single Hyperdisk Balanced High Availability volume— 100,000 IOPS or 2,400 MiB/s. An instance can achieve these higher limits if you attach multiple Hyperdisk Balanced High Availability volumes to the instance. 

If an instance's performance limit in the following table exceeds 100,000 IOPS or 2,400 MiB/s, then the instance can achieve that limit only if you attach multiple Hyperdisk Balanced High Availability volumes. For example, the performance limit for a `c4a-*-72` instance using Hyperdisk Balanced High Availability is 240,000 IOPS and 5,000 MiB/s. To achieve this maximum performance you must attach at least three Hyperdisk Balanced High Availability volumes to the instance. 

For information about Hyperdisk Balanced High Availability features, see [About Hyperdisk Balanced High Availability](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha).

**Important:** To reach the IOPS limits, you must use an I/O size of 4 KB. Maximum throughput limits require an I/O size of at least 256 KB.   
Hyperdisk performance is half-duplex, so the IOPS and throughput limits are shared between read and write operations. This means that if a machine type has a 50,000 IOPS limit, then the sum of the reads and writes every second can't exceed 50,000. 

The performance limits also apply to [custom machine types](https://docs.cloud.google.com/compute/docs/machine-resource#custom-types). 

Instance machine type | Maximum IOPS | Maximum throughput (MiB/s)  
---|---|---  
A3 (A3+H100)   
`a3-highgpu-1g` | 120,000 | 1,800  
`a3-highgpu-2g` | 160,000 | 2,400  
`a3-highgpu-4g` | 160,000 | 4,800  
`a3-highgpu-8g` | 160,000 | 4,800  
`a3-edgegpu-8g` | 160,000 | 4,800  
`a3-megagpu-8g` | 160,000 | 4,800  
A3 (A3+H200)   
`a3-ultragpu-8g` | 320,000 | 10,000  
C3   
`c3-*-4` | 25,000 | 400  
`c3-*-8` | 50,000 | 800  
`c3-*-22` | 120,000 | 1,800  
`c3-*-44` | 160,000 | 2,400  
`c3-*-88` | 160,000 | 4,800  
`c3-*-176` | 160,000 | 10,000  
C3D   
`c3d-*-4` | 25,000 | 400  
`c3d-*-8` | 50,000 | 800  
`c3d-*-16` | 75,000 | 1,200  
`c3d-*-30` | 93,750 | 1,200  
`c3d-*-60` | 160,000 | 2,400  
`c3d-*-90` | 160,000 | 2,500  
`c3d-*-180` | 160,000 | 2,500  
`c3d-*-360` | 160,000 | 2,500  
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
C4D   
`c4d-*-2` | 22,500 | 400  
`c4d-*-4` | 50,000 | 400  
`c4d-*-8` | 50,000 | 800  
`c4d-*-16` | 75,000 | 1,200  
`c4d-*-32` | 75,000 | 1,600  
`c4d-*-48` | 75,000 | 1,600  
`c4d-*-64` | 160,000 | 2,400  
`c4d-*-96` | 160,000 | 3,125  
`c4d-*-192` | 240,000 | 6,250  
`c4d-*-384` | 320,000 | 12,500  
C4N   
`c4n-*-2` | 50,000 | 800  
`c4n-*-4` | 50,000 | 800  
`c4n-*-8` | 100,000 | 1,600  
`c4n-*-16` | 150,000 | 2,800  
`c4n-*-24` | 180,000 | 3,200  
`c4n-*-48` | 280,000 | 6,250  
`c4n-*-96` | 320,000 | 10,000  
`c4n-*-192` | 640,000 | 20,000  
G4   
`g4-standard-6` | 50,000 | 400  
`g4-standard-12` | 50,000 | 800  
`g4-standard-24` | 75,000 | 1,200  
`g4-standard-48` | 75,000 | 1,600  
`g4-standard-96` | 160,000 | 2,800  
`g4-standard-192` | 240,000 | 4,800  
`g4-standard-384` | 320,000 | 10,000  
M3   
`m3-*-32` | 160,000 | 2,400  
`m3-*-64` | 160,000 | 4,800  
`m3-*-128` | 160,000 | 4,800  
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
`n4a-*-4` | 30,000 | 240  
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
X5   
`x5-*-688-metal` | 640,000 | 20,000  
`x5-*-1376-metal` | 640,000 | 20,000  
`x5-*-2064-metal` | 640,000 | 20,000  
Z3   
`z3-*-88` | 160,000 | 4,800  
`z3-*-176` | 160,000 | 4,800  
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


### Hyperdisk Extreme performance limits

This section lists the maximum performance that Hyperdisk Extreme volumes can achieve for each supported instance. A Hyperdisk Extreme volume's performance when it's attached to an instance can't exceed the limits for the instance's machine type. The performance limits are also shared across all Hyperdisk Extreme volumes attached to the same instance, regardless of each volume's provisioned performance. 

#### Achieve higher performance with multiple Hyperdisk Extreme volumes

Certain instances can exceed the maximum performance for a single Hyperdisk Extreme volume— 350,000 IOPS or 5,000 MiB/s. An instance can only achieve these higher limits if you attach multiple Hyperdisk Extreme volumes to the instance.

If an instance's performance limit in the following table exceeds 350,000 IOPS or 5,000 MiB/s, then the instance can only achieve that limit if you attach multiple Hyperdisk Extreme volumes. For example, the performance limit for a `c3-*-176` instance using Hyperdisk Extreme is 500,000 IOPS and 10,000 MiB/s. To achieve this maximum performance you must attach at least two Hyperdisk Extreme volumes to the instance. 

For more information about Hyperdisk Extreme, see [About Hyperdisk Extreme](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme).

**Important:** To reach the IOPS limits, you must use an I/O size of 4 KB. Maximum throughput limits require an I/O size of at least 256 KB. Hyperdisk performance is half-duplex, so the IOPS and throughput limits are shared between read and write operations. This means that if a machine type has a 50,000 IOPS limit, then the sum of the reads and writes every second can't exceed 50,000. 

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


### Hyperdisk ML performance limits

This section lists the maximum performance that Hyperdisk ML volumes can achieve for each supported instance. A Hyperdisk ML volume's performance when it's attached to an instance can't exceed the limits for the instance's machine type. The performance limits are also shared across all Hyperdisk ML volumes attached to the same instance, regardless of each volume's provisioned performance. 

#### Scenarios that require multiple instances to reach provisioned performance

The provisioned throughput for a Hyperdisk ML volume is shared between each instance the volume is attached to, up to the maximum limit for the machine type that's listed in the following table. If a Hyperdisk ML volume's provisioned performance is higher than an instance's performance limit, the volume can achieve its provisioned performance only if it is attached to multiple instances.

For example, suppose you have a Hyperdisk ML volume provisioned with 500,000 MiB/s of throughput and you want to attach the volume to `a3-ultragpu-8` instances. A single `a3-ultragpu-8` instance can't acheieve more than 4,000 MiB/s of throughput. Therefore, to achieve the volume's provisioned throughput, you must attach the volume to at least 125 (500,000/4,000) `a3-ultragpu-8` instances. On the other hand, for the `a2-highgpu-1g` machine type, you would need 272 instances. 

For more information about Hyperdisk ML, see [About Hyperdisk ML](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-ml).

**Important:** To reach the IOPS limits, you must use an I/O size of 4 KB. Maximum throughput limits require an I/O size of at least 256 KB. Hyperdisk performance is half-duplex, so the IOPS and throughput limits are shared between read and write operations. This means that if a machine type has a 50,000 IOPS limit, then the sum of the reads and writes every second can't exceed 50,000. 

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
`c4n-*-192`1,2 | 320,000 | 20,000  
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
`m4n-*-2`1 | 12,800 | 800  
`m4n-*-4`1 | 12,800 | 800  
`m4n-*-8`1 | 14,400 | 900  
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
Z4D 1  
`z4d-*-8`1 | 12,800 | 800  
`z4d-*-16`1 | 19,200 | 1,200  
`z4d-*-32`1 | 33,600 | 2,100  
`z4d-*-48`1 | 51,200 | 3,200  
`z4d-*-64`1 | 67,200 | 4,200  
`z4d-*-96`1 | 100,000 | 6,250  
`z4d-*-192`1 | 200,000 | 12,500  
`z4d-*-384`1,2 | 400,000 | 25,000  
`z4d-*-384-metal`1,2 | 400,000 | 25,000  
Z4M 1  
`z4m-*-16`1 | 25,600 | 1,600  
`z4m-*-32`1 | 33,600 | 2,100  
`z4m-*-48`1 | 50,000 | 3,125  
`z4m-*-192`1,2 | 200,000 | 12,500  
`z4m-*-192-metal`1,2 | 200,000 | 12,500  
  
1 Also offers steady state performance. For more information, see [Performance limits for machine types with steady state performance](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#steady-state).  
2 The disk performance for this machine type is based on having 2 physical NICs per instance. Compute Engine automatically maps attached disks to a physical NIC in a balanced round-robin fashion.  


### Hyperdisk Throughput performance limits

This section lists the maximum performance that Hyperdisk Throughput volumes can achieve for each supported instance. A Hyperdisk Throughput volume's performance when it's attached to an instance can't exceed the limits for the instance's machine type. The performance limits are also shared across all Hyperdisk Throughput volumes attached to the same instance, regardless of each volume's provisioned performance. 

#### Achieve higher performance with multiple Hyperdisk Throughput volumes

Certain instances can exceed the maximum performance for a single Hyperdisk Throughput volume—2,400 MiB/s. An instance can achieve these higher limits if you attach multiple Hyperdisk Throughput volumes to the instance. 

If an instance's performance limit in the following table exceeds 2,400 MiB/s, then the instance can achieve that limit only if you attach multiple Hyperdisk Throughput volumes. For example, the performance limit for a `a3-*-8g` instance using Hyperdisk Throughput volumes is 3,000 MiB/s. Therefore, to achieve 3,000 MiB/s of throughput, you must attach at least two Hyperdisk Throughput volumes to the instance. 

For more information about Hyperdisk Throughput, see [About Hyperdisk Throughput](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput).

**Important:** To reach the IOPS limits, you must use an I/O size of 4 KB. Maximum throughput limits require an I/O size of at least 256 KB.   
Hyperdisk performance is half-duplex, so the IOPS and throughput limits are shared between read and write operations. This means that if a machine type has a 50,000 IOPS limit, then the sum of the reads and writes every second can't exceed 50,000. 

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


## Hyperdisk size and attachment limits per instance

The following sections describe the limits to the size and number of Hyperdisk volumes you can attach to a single instance. The limits discussed don't apply to any Local SSD disks attached to the same instance.

### Summary of Hyperdisk per-instance limits

**Maximum total capacity per instance** : The maximum total capacity of all the volumes attached to an instance is between 257 TiB to 512 TiB, depending on various factors. For details, see Maximum total capacity per instance.

**Maximum number of volumes attached to an instance** : Compute Engine limits the number of Hyperdisk volumes that you can attach to a single instance. The following limits apply in order. When both limits apply, the first rule in the list is enforced.

  1. The number of Hyperdisk volumes that you can attach to the instance: 8 to 128; depending on the Hyperdisk type and the instance's machine type.
  2. The number of Hyperdisk and Persistent Disk volumes that you can attach to the instance: 128. For more information, see Maximum number of disks, across all types.



The following examples demonstrate how the limits work.

#### Examples

Suppose you have a `c3-*-96` instance. The following limits apply.

  * Maximum number of Hyperdisk volumes across all types: 128\. However, for each Hyperdisk type, the limits are as follows: 
    * Hyperdisk Throughput: 64
    * Hyperdisk ML: 64
    * Hyperdisk Extreme: 8
    * Hyperdisk Balanced or Hyperdisk Balanced High Availability: 32
  * Maximum number of Persistent Disk and Hyperdisk volumes that you can attach to the instance: 128
  * Maximum combined total capacity of all volumes: 512 TiB



The following examples illustrate these limits.

  * **Maximum number of a single type of Hyperdisk per instance** : If you attach 8 Hyperdisk Extreme volumes to the instance, then you can attach up to 123 more Hyperdisk volumes to the instance. However, you can attach only 3 more Hyperdisk Extreme volumes to the instance because the maximum number of Hyperdisk Extreme volumes 8.

  * **Maximum number of Hyperdisk volumes per instance** : 128. If you attach 8 Hyperdisk Extreme volumes to the instance, you can attach up to 120 more Hyperdisk volumes to the instance.

  * **Maximum number of disks or volumes per instance, across all types** : 128. If you attach a combined total of 128 Hyperdisk volumes to the instance, then you can't attach any more Hyperdisk or Persistent Disk volumes. However, if you attach only 64 Hyperdisk volumes to the instance, then you can still attach up to 64 Persistent Disk or Hyperdisk volumes to the instance.




### Maximum total capacity per instance

The maximum total disk capacity (in TiB) across all Hyperdisk and Persistent Disk types that you attach to an instance depends on the number of vCPUs that the instance has. The capacity limits are as follows:

  * For machine types with less than 32 vCPUs:

    * 257 TiB for all Hyperdisk or all Persistent Disk
    * 257 TiB for a mixture of Hyperdisk and Persistent Disk
  * For machine types with 32 or more vCPUs:

    * 512 TiB for all Hyperdisk
    * 512 TiB for a mixture of Hyperdisk and Persistent Disk
    * 257 TiB for all Persistent Disk



You can attach a combination of Hyperdisk and Persistent Disk volumes to a single instance but the total disk capacity for Persistent Disk can't exceed 257 TiB.

### Maximum number of disks per instance, across all types

The maximum number of individual Hyperdisk, and, if supported, Persistent Disk volumes that you can attach to an instance is 128. If you attach 28 Hyperdisk volumes to an instance, you can still attach 100 more Hyperdisk or Persistent Disk volumes to the same instance.

### Maximum Hyperdisk volumes per instance

The number of Hyperdisk volumes you can attach to an instance depends on the machine type, with separate limits for each Hyperdisk type.

For disk attachment limits for TPUs, see [TPU support for Hyperdisk and Persistent Disk](https://docs.cloud.google.com/tpu/docs/attach-durable-block-storage-compute).

For all other machine series, the limits are detailed in the **Supported disk types** section within the documentation for each machine series. To view these limits, refer to the corresponding links in the following table.

General purpose  
machine types | Storage-optimized  
machine types | Compute-optimized  
machine types | Network-optimized  
machine types | Memory-optimized  
machine types | Accelerator-optimized  
machine types  
---|---|---|---|---|---  
  
  * [C3](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_disks)
  * [C3D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3d_disks)
  * [C4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#supported_disk_types_for_c4)
  * [C4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#supported_disk_types_for_c4a)
  * [C4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#supported_disk_types_for_c4d)
  * [N2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_disks)
  * [N2D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2d_disks)
  * [N4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#supported_disk_types_for_n4)
  * [N4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#supported_disk_types_for_n4a)
  * [N4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#supported_disk_types_for_n4d)
  * [T2D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2d_disks)

| 

  * [Z3](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_disks)
  * [Z4D](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4d_disks)
  * [Z4M](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4m_disks)

| 

  * [H3](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h3_disks)
  * [H4D](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_disks)

| 

  * [C4N](https://docs.cloud.google.com/compute/docs/network-optimized-machines#c4n_disks)

| 

  * [M1](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m1_disks)
  * [M2](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m2_disks)
  * [M3](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m3_disks)
  * [M4](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m4_disks)
  * [X4](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x4_disks)
  * [X5](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x5_disks)

| 

  * [A2](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-disks)
  * [A3+H100](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-disks)
  * [A3+H200](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-disks)
  * [A4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-disks)
  * [A4X](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-disks)
  * [A4X Max](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-disks)
  * [G2](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-disks)
  * [G4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-disks)

  
  
## What's next

  * [Optimize the performance of your Hyperdisk volumes](https://docs.cloud.google.com/compute/docs/disks/optimize-hyperdisk)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
