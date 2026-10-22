---
url: https://docs.cloud.google.com/compute/docs/disks/performance/
title: Persistent Disk performance overview \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:34.886908+00:00
---

# Persistent Disk performance overview  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Persistent Disk performance overview Stay organized with collections  Save and categorize content based on your preferences. 

If your workload has specific performance requirements, then you must choose a virtual machine (VM) instance that can reach that level of performance because the maximum performance limits vary by machine series and machine type. If you're using Persistent Disk volumes, you must also configure your volumes to reach the target performance level.

This document covers the performance limits for each machine series that supports Persistent Disk.

To learn how to optimize your Persistent Disk performance, see [Optimizing Persistent Disk performance](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance).

For a discussion of Google Cloud Hyperdisk performance, see [About performance for Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-performance). For Google Cloud Hyperdisk performance limits, see [Hyperdisk performance limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits).

## Choose a Persistent Disk type

When you create a Persistent Disk volume, you can select one of the following disk types:

  * **Balanced Persistent Disk** (`pd-balanced`) 
    * An alternative to SSD (Performance) Persistent Disk.
    * Balance of performance and cost. For most Compute Engine machine types, these disks have the same maximum IOPS as SSD Persistent Disk and lower IOPS per GiB. This disk type offers performance levels suitable for most general-purpose applications at a price point between that of standard and SSD Persistent Disk.
    * Uses solid-state drives (SSD).
  * **SSD (Performance) Persistent Disk** (`pd-ssd`) 
    * Suitable for enterprise applications and high-performance databases that require lower latency and more IOPS than standard Persistent Disk provides.
    * Uses solid-state drives (SSD).
  * **Standard Persistent Disk** (`pd-standard`) 
    * Suitable for large data processing workloads that primarily use sequential I/Os.
    * Uses standard hard disk drives (HDD).
  * **Extreme Persistent Disk** (`pd-extreme`) 
    * Offers consistently high performance for both random access workloads and bulk throughput.
    * Designed for high-end database workloads.
    * Lets you provision the target IOPS.
    * Uses solid-state drives (SSD).
    * Available with a limited number of [machine types](https://docs.cloud.google.com/compute/docs/disks/extreme-persistent-disk#machine_shape_support).



If you create a disk in the Google Cloud console, the default disk type is `pd-balanced`. If you create a disk using the gcloud CLI or the Compute Engine API, the default disk type is `pd-standard`.

Each Persistent Disk type has unique performance limits that depend on the [machine type](https://docs.cloud.google.com/compute/docs/machine-resource) and number of vCPUs in use.

## Terminology and units

Persistent Disk performance, as discussed in this document, refers to IOPS and throughput.

  * _IOPS_ stands for input/output operations per second. This is the number of individual reads and writes the volume performs or can perform within a second.
  * _Throughput_ refers to how many bytes can be read from or written to a volume in a second. Throughput is measured in MiB/s.



## How Persistent Disk performance limits work

The following summarizes Persistent Disk performance:

  * Performance depends on the machine type of the instance that you attach a Persistent Disk volume to, and increases with the instance's number of vCPUs.

  * A Persistent Disk volume's performance depends on its size. Each provisioned GiB of size includes a fixed amount of throughput and IOPS. For example, Standard Persistent Disk includes 0.12 MiB/s of throughput per GiB, so a 900 GiB volume has a maximum throughput of 108 MiB/s (`900 GiB * 0.12 MiB/s`).

  * Each Persistent Disk volume has a maximum limit that can be reached for its type, regardless of its size. For example, a zonal SSD Persistent Disk can reach at most 100,000 IOPS while Balanced Persistent Disk has a maximum of 80,000 IOPS.

  * A Persistent Disk volume's performance when attached to an instance might be higher if other Persistent Disk volumes of the same type are also attached to the instance and are idle. This is because performance is determined by the total size of all volumes of the same type that are attached to an instance.

For example, suppose you have two 250 GiB SSD Persistent Disk volumes. If you attach both volumes to the same instance and one is idle, then the other volume might be able to reach the performance limits of a 500 GiB volume.

  * Balanced Persistent Disk and SSD Persistent Disk also offer a minimum performance level regardless of size called baseline performance.




For the per-GiB performance limits, see Zonal Persistent Disk performance limits by type and Regional Persistent Disk performance by type.

For the performance limits by machine type, see Persistent Disk performance limits by machine series.

### Baseline performance for SSD and Balanced Persistent Disk

The following Persistent Disk types offer baseline IOPS and throughput performance in addition to the per GiB performance limits:

  * Balanced Persistent Disk
  * SSD Persistent Disk



Baseline performance is the same for all disk sizes and doesn't scale based on the number of disks of the same type that are attached to an instance. For example, if you have two zonal Balanced Persistent Disk attached to an instance, then they share a baseline performance of 3,000 IOPS.

To calculate the maximum expected performance of a Persistent Disk type, use the following formula. The combined disk size is the total size (in GiB) of all disks of the same type that are attached to the instance:

`Maximum performance = B + (G * X)`

Where:

  * `B` is the baseline performance for the Persistent Disk type.
  * `G` is the per GiB performance limit.
  * `X` is the combined disk size in GiB.



For example, the maximum IOPS of two 1,000 GiB zonal Balanced Persistent Disk attached to the same instance is 15,000. Baseline IOPS for Balanced Persistent Disk is 3,000; the per-GiB IOPS rate is 6; so the maximum total performance for the two volumes is calculated as follows:

`3,000 + (6 * 2,000 GiB combined disk size) = 15,000 IOPS`

The following table shows the baseline performance for Balanced and SSD Persistent Disk.

###  Zonal Persistent Disk 

The following table shows the baseline sustained IOPS and throughput for zonal Persistent Disk:

| Zonal  
Balanced  
PD | Zonal  
SSD PD  
---|---|---  
Baseline IOPS per instance | 3,000 | 6,000  
Baseline Throughput (MiB/s) per instance | 140 | 240  
  
###  Regional Persistent Disk 

Regional Persistent Disk are supported on only E2, N1, N2, and N2D instances. The following table shows the baseline sustained IOPS and throughput for regional Persistent Disk:

| Regional  
Balanced  
PD | Regional  
SSD PD  
---|---|---  
Baseline IOPS per instance | 3,000 | 6,000  
Baseline throughput (MiB/s) per instance | 140 | 240  
  
## Configure your Persistent Disk to meet performance requirements

To achieve a target performance level (IOPS or throughput) for your workload, you must choose a size for your Persistent Disk volume **and** a VM with a machine type that can reach that performance level.

The actual performance achieved by your volume is the lesser of the disk's performance limit and the VM's performance limit:

`Actual Performance = MIN (disk performance limit, VM machine type limit)`

The _disk performance limit_ is the maximum performance for the Persistent Disk volume based on its size. The _VM machine type limit_ is the VM's machine type's maximum performance limit, which also varies by Persistent Disk type.

To determine the minimum Persistent Disk size and machine type for your workload's requirements, follow these steps:

  1. **Determine the required disk size** : To find the minimum total disk size (in GiB) needed to meet your target IOPS and throughput, see Performance limits by size.
  2. **Determine the required VM machine type** : To select a machine type and vCPU count that supports your target IOPS and throughput, review the limits in Performance limits by machine series.



## Zonal Persistent Disk performance limits by type

This section lists the maximum performance limits for each zonal Persistent Disk type and the per-GiB performance rates.

Performance also depends on the disk size, machine type, and vCPU count.

For performance limits for common disk sizes, see Performance limits by size for zonal and regional Persistent Disk.

For performance limits by machine type, see Performance by machine type and vCPU count for zonal Persistent Disk.

### IOPS limits by type for zonal Persistent Disk

The following table shows IOPS limits for zonal Persistent Disk.

| Zonal  
Standard  
PD | Zonal  
Balanced  
PD | Zonal  
SSD PD | Zonal  
Extreme PD | Zonal   
SSD PD in  
multi-writer mode  
---|---|---|---|---|---  
Read IOPS per GiB | 0.75 | 6 | 30 | – | 30  
Write IOPS per GiB | 1.5 | 6 | 30 | – | 30  
Read IOPS per instance | 7,500 | 80,000 | 100,000 | 120,000 | 100,000  
Write IOPS per instance | 15,000 | 80,000 | 100,000 | 120,000 | 100,000  
  
### Throughput limits by type for zonal Persistent Disk

The following table shows the throughput limits for zonal Persistent Disk. Persistent Disk can achieve greater performance on instances with more vCPUs. For more information, read [Network egress caps on write throughput](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance#performance_factors).

| Zonal  
Standard  
PD | Zonal  
Balanced  
PD | Zonal  
SSD PD | Zonal  
Extreme PD | Zonal   
SSD PD in  
multi-writer mode  
---|---|---|---|---|---  
Throughput per GiB (MiB/s) | 0.12 | 0.28 | 0.48 | — | 0.48  
Read throughput per instance (MiB/s) | 1,200 | 1,2001 | 1,2001 | 4,0002 | 1,200  
Write throughput per instance (MiB/s) | 400 | 1,2001 | 1,2001 | 3,0002 | 1,200  
  
1T2A instances with 48 vCPUs can reach 1,800 MiB/s.   
2Requires an [N2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_series) instance with at least 64 vCPUs to achieve the stated performance limit. For maximum limits for all other machine types, see [Performance by machine type and vCPU count](https://docs.cloud.google.com/compute/docs/disks/performance#machine-type-disk-limits). 

## Regional Persistent Disk performance by type

This section shows the maximum and per-GiB IOPS and throughput limits for regional Persistent Disk.

For performance limits for common disk sizes, see Performance limits by size for zonal and regional Persistent Disk.

These conditions apply to the stated limits:

  * Performance depends on the machine type and vCPU count of the instance using the Persistent Disk volume.
  * Achieving the stated limits requires a compute instance with at least 64 vCPUs and an [N2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_series) machine type or an [N1](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_machines) machine type running on the Intel Skylake or newer CPU. Instances using other machine types, such as [N2D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2d_machines), have lower performance limits.
  * Instances using [E2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#e2_machine_types) machine types have lower performance limits because E2 machine types support a maximum of 32 vCPUs.
  * Read IOPS per instance and read throughput per instance might be lower when the disk is in [unreplicated mode](https://docs.cloud.google.com/compute/docs/disks/repd-failover#failures).



Regional Persistent Disk can achieve greater performance when you modify [factors that can affect performance](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance#performance_factors), like disk size and number of vCPUs.

### IOPS limits by type for regional Persistent Disk

The following table shows IOPS rates and maximums for regional Persistent Disk.

| Regional  
Standard  
PD | Regional  
Balanced  
PD | Regional  
SSD PD  
---|---|---|---  
**Read IOPS per GiB** | 0.75 | 6 | 30  
**Write IOPS per GiB** | 1.5 | 6 | 30  
Read IOPS per instance | 7,500 | 80,000* | 100,000#  
Write IOPS per instance | 15,000 | 60,000† | 80,000‡  
  
* For N2D, the maximum read IOPS per instance for Balanced Persistent Disk is 60,000. 

# For N2D, the maximum read IOPS per instance for SSD Persistent Disk is 70,000. 

† For N2D, the maximum write IOPS per instance for Balanced Persistent Disk is 50,000. 

‡ For N2D, the maximum write IOPS per instance for SSD Persistent Disk is 60,000. 

### Throughput limits by type for regional Persistent Disk

The following table shows the throughput limits for regional Persistent Disk.

| Regional  
Standard  
PD | Regional  
Balanced  
PD | Regional  
SSD PD  
---|---|---|---  
Throughput per GiB (MiB/s) | 0.12 | 0.28 | 0.48  
Read throughput per instance (MiB/s) | 1,200 | 1,200 | 1,200  
Write throughput per instance (MiB/s) | 200 | 600 | 1,000‡  
  
‡ For N2D, the maximum write throughput per instance for SSD Persistent Disk is 600 MiB/s. 

## Performance limits by size for zonal and regional Persistent Disk

To estimate the maximum performance you can expect from a Persistent Disk volume of a given size, review the following sections for each Persistent Disk type.

  * SSD Persistent Disk
  * Balanced Persistent Disk
  * Standard Persistent Disk
  * Extreme Persistent Disk



### SSD Persistent Disk performance limits by size

To determine the minimum size required for your SSD Persistent Disk volumes to reach a specific performance limit, review the information in this section.

The listed limits aren't guaranteed performance levels, but represent the maximum possible performance. To reach a particular limit, you must attach the volume to an instance that supports that level of performance. 

If a specific size isn't listed, calculate performance using the following formulas, where `x` is the combined total size (in GiB) of all SSD Persistent Disk volumes that are attached to the instance, and `instance_limit` is the performance limit for your VM's machine type and vCPU count.

  * IOPS: `MIN (instance_limit, (30x + 6,000))`
  * Throughput: `MIN (instance_limit, (0.48x + 240))`



Suppose you want to attach a 500 GiB zonal SSD Persistent Disk volume to an N2 instance that has 4 vCPUs. The `instance_limit`—the SSD Persistent Disk throughput limit for a 4-vCPU N2 instance is 240 MiB/s. Using the formula, the maximum throughput the disk can reach with the instance is: `MIN (240 MiB/s, 480 MiB/s (240 + (0.48 * 500))) `. 

To reach the maximum performance limit of 480 MiB/s, you must attach the disk to an N2 instance that has a SSD Persistent Disk throughput limit of at least 480 MiB/s. 

The following table lists SSD Persistent Disk performance limits for common disk sizes.

###  Zonal SSD Persistent Disk 

Performance limits by size for zonal SSD Persistent Disk Size (GiB) | Maximum (read/write) IOPS | Maximum (read/write) throughput (MiB/s)  
---|---|---  
10 | 6,300 | 244.8  
30 | 6,900 | 254.4  
50 | 7,500 | 264  
100 | 9,000 | 288  
150 | 10,500 | 312  
200 | 12,000 | 336  
300 | 15,000 | 384  
500 | 21,000 | 480  
750 | 28,500 | 600  
1,000 | 36,000 | 720  
2,000 | 66,000 | 1,200  
2,500 | 81,000 | 1,200  
3,334 | 100,000 | 1,200  
4,000 to 64,000 | 100,000 | 1,200  
  
###  Regional SSD Persistent Disk 

Performance limits by size for regional SSD Persistent Disk Size (GiB) | Maximum read IOPS | Maximum write IOPS | Maximum read throughput (MiB/s) | Maximum write throughput (MiB/s)  
---|---|---|---|---  
10 | 6,300 | 6,300 | 244.8 | 244.8  
30 | 6,900 | 6,900 | 254.4 | 254.4  
50 | 7,500 | 7,500 | 264 | 264  
100 | 9,000 | 9,000 | 288 | 288  
150 | 10,500 | 10,500 | 312 | 312  
200 | 12,000 | 12,000 | 336 | 336  
300 | 15,000 | 15,000 | 384 | 384  
500 | 21,000 | 21,000 | 480 | 480  
750 | 28,500 | 28,500 | 600 | 600  
1,000 | 36,000 | 36,000 | 720 | 720  
2,000 | 66,000 | 66,000 | 1,200 | 1,000  
2,500 | 81,000 | 80,000 | 1,200 | 1,000  
3,334 | 100,000 | 80,000 | 1,200 | 1,000  
4,000 to 64,000 | 100,000 | 80,000 | 1,200 | 1,000  
  
The **Size** column in the preceding table refers to the combined size of all SSD Persistent Disk volumes attached to the same instance. For example, the performance limit is the same whether you attach one 500 GiB SSD Persistent Disk volume to the instance, or five 100 GiB volumes. For more information, see [Multiple disks attached to a single compute instance](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance#multiple-disks). 

**IOPS for SSD Persistent Disk are half-duplex, but throughput is full-duplex**. This means that the combined total read and write IOPS can't exceed the stated limit, but a disk can reach both the stated read and write limits simultaneously.

### Balanced Persistent Disk performance limits by size

To determine the minimum size required for your Balanced Persistent Disk volumes to reach a specific performance limit, review the information in this section.

The listed limits aren't guaranteed performance levels, but represent the maximum possible performance. To reach a particular limit, you must attach the volume to an instance that supports that level of performance. 

If a specific size isn't listed, calculate performance using the following formulas, where `x` is the combined total size (in GiB) of all Balanced Persistent Disk volumes that are attached to the instance, and `instance_limit` is the performance limit for your instance's machine type and vCPU count.

  * IOPS: `MIN (instance_limit, (6x + 3,000), 80,000)`
  * Throughput: `MIN (instance_limit, (0.28x + 140), 1,200)`



Suppose you want to attach a 500 GiB zonal Balanced Persistent Disk volume to an N2 instance that has 4 vCPUs. The `instance_limit`—the Balanced Persistent Disk throughput limit for a 4-vCPU N2 instance is 240 MiB/s. Using the formula, the maximum throughput the disk can reach with the instance is: `MIN (240 MiB/s, 280 MiB/s (140 + (0.28 * 500))) `. 

To reach the maximum performance limit of 280 MiB/s, you must attach the disk to an N2 instance that has a Balanced Persistent Disk throughput limit of at least 280 MiB/s. 

The following table lists Balanced Persistent Disk performance limits for common disk sizes.

###  Zonal Balanced Persistent Disk 

Performance limits by size for zonal Balanced Persistent Disk Size (GiB) | Maximum IOPS | Maximum read throughput (MiB/s) | Maximum write throughput (MiB/s)  
---|---|---|---  
10 | 3,060 | 142.8 | 142.8  
30 | 3,180 | 148.4 | 148.4  
50 | 3,300 | 154 | 154  
100 | 3,600 | 168 | 168  
150 | 3,900 | 182 | 182  
300 | 4,800 | 224 | 224  
500 | 6,000 | 280 | 280  
1,000 | 9,000 | 420 | 420  
2,000 | 15,000 | 700 | 700  
2,500 | 18,000 | 840 | 840  
4,000 | 27,000 | 1,200 | 1,200  
5,000 | 33,000 | 1,200 | 1,200  
8,000 | 51,000 | 1,200 | 1,200  
10,000 | 63,000 | 1,200 | 1,200  
12,834 to 64,000 | 80,000 | 1,200 | 1,200  
  
### Regional Balanced Persistent Disk 

Performance limits by size for regional Balanced Persistent Disk Size (GiB) | Maximum read IOPS | Maximum write IOPS | Maximum read throughput (MiB/s) | Maximum write throughput (MiB/s)  
---|---|---|---|---  
10 | 3,060 | 3,060 | 142.8 | 142.8  
30 | 3,180 | 3,180 | 148.4 | 148.4  
50 | 3,300 | 3,300 | 154 | 154  
100 | 3,600 | 3,600 | 168 | 168  
150 | 3,900 | 3,900 | 182 | 182  
300 | 4,800 | 4,800 | 224 | 224  
500 | 6,000 | 6,000 | 280 | 280  
1,000 | 9,000 | 9,000 | 420 | 420  
2,000 | 15,000 | 15,000 | 700 | 600  
2,500 | 18,000 | 18,000 | 840 | 600  
3,334 | 23,004 | 23,004 | 1,074 | 600  
4,000 | 27,000 | 27,000 | 1,200 | 600  
5,000 | 33,000 | 33,000 | 1,200 | 600  
8,000 | 51,000 | 51,000 | 1,200 | 600  
10,000 | 63,000 | 60,000 | 1,200 | 600  
12,834 to 64,000 | 80,000 | 60,000 | 1,200 | 600  
  
The **Size** column in the preceding table refers to the combined size of all Balanced Persistent Disk volumes attached to the same instance. For example, the performance limit is the same whether you attach one 500 GiB Balanced Persistent Disk volume to the instance, or five 100 GiB volumes. For more information, see [Multiple disks attached to a single compute instance](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance#multiple-disks). 

**IOPS for Balanced Persistent Disk are half-duplex, but throughput is full duplex**. This means that the total read and write IOPS can't exceed the stated limit, but a disk can reach both the stated read and write limits simultaneously.

### Standard Persistent Disk performance limits by size

To determine the minimum size required for your Standard Persistent Disk volumes to reach a specific performance limit, review the information in this section.

The listed limits aren't guaranteed performance levels, but represent the maximum possible performance. To reach a particular limit, you must attach the volume to an instance that supports that level of performance. 

If a specific size isn't listed, calculate performance using the following formulas, where `x` is the combined total size (in GiB) of all Standard Persistent Disk volumes attached to the instance, and `instance_limit` is the performance limit for your instance's machine type and vCPU count.

  * Read IOPS: `MIN (instance_limit, 0.75x)`
  * Write IOPS: `MIN (instance_limit, 1.5x)`
  * Throughput: `MIN (instance_limit, 0.12x)`



For example, a 500 GiB Standard Persistent Disk volume can reach up to 60 MiB/s of throughput (`0.12 * 500`). If you attach it to a 4-vCPU N2 instance, which has a Standard Persistent Disk throughput limit, of 240 MiB/s, the throughput limit for the volume still won't exceed 60 MiB/s.

The following table lists Standard Persistent Disk performance limits for common disk sizes.

### Zonal Standard Persistent Disk 

Performance limits by size for zonal Standard Persistent Disk Size (GiB) | Maximum read IOPS | Maximum write IOPS | Maximum read throughput (MiB/s) | Maximum write throughput (MiB/s)  
---|---|---|---|---  
150 | 112.5 | 225 | 18 | 18  
200 | 150 | 300 | 24 | 24  
300 | 225 | 450 | 36 | 36  
500 | 375 | 750 | 60 | 60  
750 | 562.5 | 1,125 | 90 | 90  
1,000 | 750 | 1,500 | 120 | 120  
2,000 | 1,500 | 3,000 | 240 | 240  
2,500 | 1,875 | 3,750 | 300 | 300  
3,334 | 2,500 | 5,001 | 400 | 400  
4,000 | 3,000 | 6,000 | 480 | 400  
5,000 | 3,750 | 7,500 | 600 | 400  
8,000 | 6,000 | 12,000 | 960 | 400  
10,000 | 7,500 | 15,000 | 1,200 | 400  
12,834 | 7,500 | 15,000 | 1,200 | 400  
15,000 | 7,500 | 15,000 | 1,200 | 400  
  
### Regional Standard Persistent Disk 

Performance limits by size for regional Standard Persistent Disk Size (GiB) | Maximum read IOPS | Maximum write IOPS | Maximum read throughput (MiB/s) | Maximum write throughput (MiB/s)  
---|---|---|---|---  
150 | 112.5 | 225 | 18 | 18  
200 | 150 | 300 | 24 | 24  
300 | 225 | 450 | 36 | 36  
500 | 375 | 750 | 60 | 60  
750 | 562.5 | 1,125 | 90 | 90  
1,000 | 750 | 1,500 | 120 | 120  
2,000 | 1,500 | 3,000 | 240 | 200  
2,500 | 1,875 | 3,750 | 300 | 200  
3,334 | 2,500 | 5,001 | 400.08 | 200  
4,000 | 3,000 | 6,000 | 480 | 200  
5,000 | 3,750 | 7,500 | 600 | 200  
8,000 | 6,000 | 12,000 | 960 | 200  
10,000 | 7,500 | 15,000 | 1,200 | 200  
12,834 | 7,500 | 15,000 | 1,200 | 200  
15,000 | 7,500 | 15,000 | 1,200 | 200  
  
The **Size** column in the preceding table refers to the combined size of all Standard Persistent Disk volumes attached to the same instance. For example, the performance limit is the same whether you attach one 500 GiB Standard Persistent Disk volume to the instance, or five 100 GiB volumes. For more information, see [Multiple disks attached to a single compute instance](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance#multiple-disks). 

**IOPS and throughput for Standard Persistent Disk are half-duplex**. This means the combined total read and write IOPS or throughput at any time can't exceed the stated limit.

### Extreme Persistent Disk performance limits

Performance for Extreme Persistent Disk volumes is independent of the volume's size. You can specify a target IOPS level for a volume, from 2,500 to 120,000 IOPS.

You can't specify a throughput level for Extreme Persistent Disk volumes. Instead, throughput scales with the number of IOPS you provision at a rate of 256 KiB/s of throughput per I/O. For more information, see [Performance limits for Extreme Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/extreme-persistent-disk#performance_limits_and_workload_patterns).

## Latency and data transmission for Persistent Disk

Balanced Persistent Disk, SSD Persistent Disk, and Extreme Persistent Disk are designed for sub-millisecond latencies.

For Balanced and SSD (performance) Persistent Disk volumes, the read and write throughput limits are independent of each other. This means that a disk can reach both the stated read and write limits simultaneously.

For Standard Persistent Disk, the combined read and write throughput at any time can't exceed the stated limits.

For all Persistent Disk types, read and write IOPS are half-duplex, so the IOPS limit is shared between read and write operations. This means that if an SSD Persistent Disk volume has a 15,000 IOPS limit, then the sum of the reads and writes every second can't exceed 15,000. The volume can't deliver 15,000 read IOPS and 15,000 write IOPS at the same time.

## Sharing disks between instances

Attaching a disk to multiple instances in **read-only mode** or in **multi-writer** mode does not affect aggregate performance or cost. Each machine gets a share of the per-disk performance limit. Persistent Disk created in **multi-writer** mode have specific IOPS and throughput limits. To learn how to share Persistent Disk between multiple instances, see [Sharing Persistent Disk between instances](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms).

Persistent Disk I/O operations share a common path with network traffic within an instance's hypervisor. Therefore, if the instance has significant network traffic, the actual read bandwidth and IOPS consistency might be less than the listed maximum limits. Some variability in the performance limits is to be expected, especially when operating near the maximum IOPS limits with an I/O size of 16 KB. For a summary of bandwidth expectations, see [Bandwidth summary table](https://docs.cloud.google.com/compute/docs/network-bandwidth#summary-table).

## Persistent Disk performance limits by machine series

Persistent Disk performance scales with the size of the disk and with the number of vCPUs on your instance.

Performance scales until it reaches either the limits of the disk or the limits of the instance to which the disk is attached. The machine type and the number of vCPUs on the instance determine the per-instance limits.

For Balanced and SSD Persistent Disk volumes, the read and write throughput limits are independent of each other. For all Persistent Disk types, read and write operations share a single IOPS limit, so a disk can't reach the maximum read IOPS and the maximum write IOPS in the following tables at the same time. For more information, see Latency and data transmission for Persistent Disk.

The following tables show performance limits for zonal Persistent Disk according to the machine type and number of vCPUs on the instance to which the disk is attached. For a given Persistent Disk type, the limits are the maximum across all volumes of that type that are attached to the same instance.

### A2 Ultra instances

### pd-balanced

Machine type | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
a2-ultragpu-1g | 15,000 | 15,000 | 800 | 800  
a2-ultragpu-2g | 20,000 | 20,000 | 1,200 | 1,200  
a2-ultragpu-4g | 50,000 | 50,000 | 1,200 | 1,200  
a2-ultragpu-8g | 80,000 | 80,000 | 1,200 | 1,200  
  
### pd-ssd

Machine type | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
a2-ultragpu-1g | 15,000 | 15,000 | 800 | 800  
a2-ultragpu-2g | 25,000 | 25,000 | 1,200 | 1,200  
a2-ultragpu-4g | 60,000 | 60,000 | 1,200 | 1,200  
a2-ultragpu-8g | 100,000 | 100,000 | 1,200 | 1,200  
  
### pd-standard

Machine type | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
a2-ultragpu-1g | 15,000 | 5,000 | 400 | 800  
a2-ultragpu-2g | 15,000 | 7,500 | 400 | 1,200  
a2-ultragpu-4g | 15,000 | 7,500 | 400 | 1,200  
a2-ultragpu-8g | 15,000 | 7,500 | 400 | 1,200  
  
### A2 Standard instances

### pd-balanced

Machine type | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
a2-highgpu-1g | 15,000 | 15,000 | 800 | 800  
a2-highgpu-2g | 20,000 | 20,000 | 1,200 | 1,200  
a2-highgpu-4g | 50,000 | 50,000 | 1,200 | 1,200  
a2-highgpu-8g | 80,000 | 80,000 | 1,200 | 1,200  
a2-megagpu-16g | 80,000 | 80,000 | 1,200 | 1,200  
  
### pd-ssd

Machine type | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
a2-highgpu-1g | 15,000 | 15,000 | 800 | 800  
a2-highgpu-2g | 25,000 | 25,000 | 1,200 | 1,200  
a2-highgpu-4g | 60,000 | 60,000 | 1,200 | 1,200  
a2-highgpu-8g | 100,000 | 100,000 | 1,200 | 1,200  
a2-megagpu-16g | 100,000 | 100,000 | 1,200 | 1,200  
  
### pd-standard

Machine type | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
a2-highgpu-1g | 15,000 | 5,000 | 400 | 800  
a2-highgpu-2g | 15,000 | 7,500 | 400 | 1,200  
a2-highgpu-4g | 15,000 | 7,500 | 400 | 1,200  
a2-highgpu-8g | 15,000 | 7,500 | 400 | 1,200  
a2-megagpu-16g | 15,000 | 7,500 | 400 | 1,200  
  
### A3 Mega instances

### pd-balanced

Machine type | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MB/s) | Maximum read throughput (MB/s)  
---|---|---|---|---  
a3-megagpu-8g | 80,000 | 80,000 | 1,200 | 1,200  
  
### pd-ssd

Machine type | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MB/s) | Maximum read throughput (MB/s)  
---|---|---|---|---  
a3-megagpu-8g | 80,000 | 80,000 | 1,200 | 1,200  
  
### A3 High instances

**Note:** These machine types use the NVMe disk interface for Persistent Disk.

### pd-balanced

Machine type | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MB/s) | Maximum read throughput (MB/s)  
---|---|---|---|---  
a3-highgpu-1g | 15,000 | 15,000 | 1,200 | 1,200  
a3-highgpu-2g | 30,000 | 30,000 | 1,200 | 1,200  
a3-highgpu-4g | 60,000 | 60,000 | 1,200 | 1,200  
a3-highgpu-8g | 80,000 | 80,000 | 1,200 | 1,200  
  
### pd-ssd

Machine type | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MB/s) | Maximum read throughput (MB/s)  
---|---|---|---|---  
a3-highgpu-1g | 15,000 | 15,000 | 1,200 | 1,200  
a3-highgpu-2g | 30,000 | 30,000 | 1,200 | 1,200  
a3-highgpu-4g | 60,000 | 60,000 | 1,200 | 1,200  
a3-highgpu-8g | 80,000 | 80,000 | 1,200 | 1,200  
  
### A3 Edge instances

**Note:** These machine types use the NVMe disk interface for Persistent Disk.

### pd-balanced

Machine type | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MB/s) | Maximum read throughput (MB/s)  
---|---|---|---|---  
a3-edgegpu-8g | 80,000 | 80,000 | 1,200 | 1,200  
  
### pd-ssd

Machine type | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MB/s) | Maximum read throughput (MB/s)  
---|---|---|---|---  
a3-edgegpu-8g | 80,000 | 80,000 | 1,200 | 1,200  
  
### C2 instances

### pd-balanced

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
4 | 4,000 | 4,000 | 240 | 240  
8 | 4,000 | 4,000 | 240 | 240  
16 | 4,000 | 8,000 | 480 | 600  
30 | 8,000 | 15,000 | 480 | 600  
60 | 15,000 | 15,000 | 800 | 1,200  
  
### pd-ssd

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
4 | 4,000 | 4,000 | 240 | 240  
8 | 4,000 | 4,000 | 240 | 240  
16 | 4,000 | 8,000 | 480 | 600  
30 | 8,000 | 15,000 | 480 | 600  
60 | 15,000 | 30,000 | 800 | 1,200  
  
### pd-standard

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
4 | 4,000 | 3,000 | 240 | 240  
8 | 4,000 | 3,000 | 240 | 240  
16 | 4,000 | 3,000 | 240 | 240  
30 | 8,000 | 3,000 | 240 | 240  
60 | 15,000 | 3,000 | 240 | 240  
  
### C2D Instances

### pd-balanced

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
2 | 4,590 | 4,080 | 245 | 245  
4 | 4,590 | 4,080 | 245 | 245  
8 | 4,590 | 4,080 | 245 | 245  
16 | 4,590 | 8,160 | 245 | 326  
32 | 8,160 | 15,300 | 245 | 612  
56 | 8,160 | 15,300 | 245 | 612  
112 | 15,300 | 30,600 | 408 | 1,224  
  
### pd-ssd

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
2 | 4,590 | 4,080 | 245 | 245  
4 | 4,590 | 4,080 | 245 | 245  
8 | 4,590 | 4,080 | 245 | 245  
16 | 4,590 | 8,160 | 245 | 326  
32 | 8,160 | 15,300 | 245 | 612  
56 | 8,160 | 15,300 | 245 | 612  
112 | 15,300 | 30,600 | 408 | 1,224  
  
### pd-standard

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
2 | 4,590 | 3,060 | 245 | 245  
4 | 4,590 | 3,060 | 245 | 245  
8 | 4,590 | 3,060 | 245 | 245  
16 | 4,590 | 3,060 | 245 | 245  
32 | 8,160 | 3,060 | 245 | 245  
56 | 8,160 | 3,060 | 245 | 245  
112 | 15,300 | 3,060 | 245 | 245  
  
### C3D Instances

**Note:** These machine types use the NVMe disk interface for Persistent Disk.

### pd-balanced

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
4 | 15,000 | 15,000 | 240 | 240  
8 | 25,000 | 25,000 | 800 | 800  
16 | 25,000 | 25,000 | 1,200 | 1,200  
30 | 50,000 | 50,000 | 1,200 | 1,200  
60 | 80,000 | 80,000 | 1,200 | 1,200  
90 | 80,000 | 80,000 | 1,200 | 1,200  
180 | 80,000 | 80,000 | 1,200 | 1,200  
360 | 80,000 | 80,000 | 1,200 | 1,200  
  
### pd-ssd

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
4 | 15,000 | 15,000 | 240 | 240  
8 | 15,000 | 15,000 | 800 | 800  
16 | 25,000 | 25,000 | 1,200 | 1,200  
30 | 60,000 | 60,000 | 1,200 | 1,200  
60 | 80,000 | 80,000 | 1,200 | 1,200  
90 | 80,000 | 80,000 | 1,200 | 1,200  
180 | 80,000 | 80,000 | 1,200 | 1,200  
360 | 80,000 | 80,000 | 1,200 | 1,200  
  
### C3 Instances

**Note:** These machine types use the NVMe disk interface for Persistent Disk.

### pd-balanced

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
4 | 15,000 | 15,000 | 240 | 240  
8 | 15,000 | 15,000 | 240 | 240  
22 | 20,000 | 20,000 | 800 | 800  
44 | 50,000 | 50,000 | 1,200 | 1,200  
88 | 80,000 | 80,000 | 1,200 | 1,200  
176 | 80,000 | 80,000 | 1,200 | 1,200  
  
### pd-ssd

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
4 | 15,000 | 15,000 | 240 | 240  
8 | 15,000 | 15,000 | 240 | 240  
22 | 25,000 | 25,000 | 800 | 800  
44 | 60,000 | 60,000 | 1,200 | 1,200  
88 | 80,000 | 80,000 | 1,200 | 1,200  
176 | 80,000 | 80,000 | 1,200 | 1,200  
  
### E2 Instances

### pd-balanced

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
e2-medium1 | 10,000 | 12,000 | 200 | 200  
2-7 | 15,000 | 15,000 | 240 | 240  
8-15 | 15,000 | 15,000 | 8002 | 800  
16-31 | 20,000 | 20,000 | 1,0002 | 1,200  
32 or more | 50,000 | 50,000 | 1,0002 | 1,200  
  
1[E2 shared-core](https://docs.cloud.google.com/compute/docs/general-purpose-machines#e2-shared-core) machine types run two vCPUs simultaneously shared on one physical core for a specific fraction of time. 

2 For regional Balanced Persistent Disk, the maximum write throughput is 600 MiB/s. 

### pd-ssd

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
e2-medium1 | 10,000 | 12,000 | 200 | 200  
2-7 | 15,000 | 15,000 | 240 | 240  
8-15 | 15,000 | 15,000 | 800 | 800  
16-31 | 25,000 | 25,000 | 1,000 | 1,200  
32 or more | 60,000 | 60,000 | 1,000 | 1,200  
  
1[E2 shared-core](https://docs.cloud.google.com/compute/docs/general-purpose-machines#e2-shared-core) machine types run two vCPUs simultaneously shared on one physical core for a specific fraction of time. 

2 For regional SSD Persistent Disk, the maximum write IOPS is 80,000 and the maximum write throughput is 1,000 MiB/s. 

### pd-standard

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
e2-medium1 | 10,000 | 1,000 | 200 | 200  
2-7 | 15,000 | 3,000 | 2402 | 240  
8-15 | 15,000 | 5,000 | 4002 | 800  
16 or more | 15,000 | 7,500 | 4002 | 1,200  
  
1[E2 shared-core](https://docs.cloud.google.com/compute/docs/general-purpose-machines#e2-shared-core) machine types run two vCPUs simultaneously shared on one physical core for a specific fraction of time. 

2 For regional Standard Persistent Disk, the maximum write throughput is 200 MiB/s. 

### G2 Instances

**Note:** These machine types use the NVMe disk interface for Persistent Disk.

### pd-balanced

Machine type | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
g2-standard-4 | 15,000 | 15,000 | 240 | 240  
g2-standard-8 | 15,000 | 15,000 | 800 | 800  
g2-standard-12 | 15,000 | 15,000 | 800 | 800  
g2-standard-16 | 20,000 | 20,000 | 1,200 | 1,200  
g2-standard-24 | 20,000 | 20,000 | 1,200 | 1,200  
g2-standard-32 | 50,000 | 50,000 | 1,200 | 1,200  
g2-standard-48 | 50,000 | 50,000 | 1,200 | 1,200  
g2-standard-96 | 80,000 | 80,000 | 1,200 | 1,200  
  
### pd-ssd

Machine type | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
g2-standard-4 | 15,000 | 15,000 | 240 | 240  
g2-standard-8 | 15,000 | 15,000 | 800 | 800  
g2-standard-12 | 15,000 | 15,000 | 800 | 800  
g2-standard-16 | 25,000 | 25,000 | 1,200 | 1,200  
g2-standard-24 | 25,000 | 25,000 | 1,200 | 1,200  
g2-standard-32 | 60,000 | 60,000 | 1,200 | 1,200  
g2-standard-48 | 60,000 | 60,000 | 1,200 | 1,200  
g2-standard-96 | 100,000 | 100,000 | 1,200 | 1,200  
  
### H3 Instances

**Note:** These machine types use the NVMe disk interface for Persistent Disk.

### pd-balanced

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
88 | 15,000 | 15,000 | 240 | 240  
  
### N1 Instances

### pd-balanced

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
1 | 15,000 | 15,000 | 204 | 240  
2-7 | 15,000 | 15,000 | 240 | 240  
8-15 | 15,000 | 15,000 | 8001 | 800  
16-31 | 20,000 | 20,000 | 1,2001 | 1,200  
32-63 | 50,000 | 50,000 | 1,2001 | 1,200  
64 or more | 80,0001 | 80,000 | 1,2001 | 1,200  
  
1 For regional Balanced Persistent Disk, the maximum write IOPS is 60,000 and the maximum write throughput is 600 MiB/s. 

### pd-ssd

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
1 | 15,000 | 15,000 | 204 | 240 |   
2-7 | 15,000 | 15,000 | 240 | 240  
8-15 | 15,000 | 15,000 | 800 | 800  
16-31 | 25,000 | 25,000 | 1,2001 | 1,200  
32-63 | 60,000 | 60,000 | 1,2001 | 1,200  
64 or more | 100,0001 | 100,000 | 1,2001 | 1,200  
  
1 For regional SSD Persistent Disk, the maximum write IOPS is 80,000 and the maximum write throughput is 1,000 MiB/s. 

### pd-standard

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
1 | 15,000 | Up to 3,000 | 2041 | 240  
2-7 | 15,000 | 3,000 | 2401 | 240  
8-15 | 15,000 | 5,000 | 4001 | 800  
16 or more | 15,000 | 7,500 | 4001 | 1,200  
  
1 For regional Standard Persistent Disk, the maximum write throughput is 200 MiB/s. 

### N2 Instances

### pd-balanced

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
2-7 | 15,000 | 15,000 | 240 | 240  
8-15 | 15,000 | 15,000 | 8001 | 800  
16-31 | 20,000 | 20,000 | 1,2001 | 1,200  
32-63 | 50,000 | 50,000 | 1,2001 | 1,200  
64 or more | 80,0001 | 80,000 | 1,2001 | 1,200  
  
1 For regional Balanced Persistent Disk, the maximum write IOPS is 60,000 and the maximum write throughput is 600 MiB/s. 

### pd-ssd

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
2-7 | 15,000 | 15,000 | 240 | 240  
8-15 | 15,000 | 15,000 | 800 | 800  
16-31 | 25,000 | 25,000 | 1,2001 | 1,200  
32-63 | 60,000 | 60,000 | 1,2001 | 1,200  
64 or more | 100,0001 | 100,000 | 1,2001 | 1,200  
  
1 For regional SSD Persistent Disk, the maximum write IOPS is 80,000 and the maximum write throughput is 1,000 MiB/s. 

### pd-standard

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
2-7 | 15,000 | 3,000 | 2401 | 240  
8-15 | 15,000 | 5,000 | 4001 | 800  
16 or more | 15,000 | 7,500 | 4001 | 1,200  
  
1 For regional Standard Persistent Disk, the maximum write throughput is 200 MiB/s. 

### pd-extreme

Machine type | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
n2-standard-64 | 120,000 | 120,000 | 3,000 | 4,000  
n2-standard-80 | 120,000 | 120,000 | 3,000 | 4,000  
n2-standard-96 | 120,000 | 120,000 | 3,000 | 4,000  
n2-standard-128 | 120,000 | 120,000 | 3,000 | 4,000  
n2-highmem-64 | 120,000 | 120,000 | 3,000 | 4,000  
n2-highmem-80 | 120,000 | 120,000 | 3,000 | 4,000  
n2-highmem-96 | 120,000 | 120,000 | 3,000 | 4,000  
n2-highmem-128 | 120,000 | 120,000 | 3,000 | 4,000  
n2-highcpu-64 | 120,000 | 120,000 | 3,000 | 4,000  
n2-highcpu-80 | 120,000 | 120,000 | 3,000 | 4,000  
n2-highcpu-96 | 120,000 | 120,000 | 3,000 | 4,000  
  
N2 Instances with 96 or more vCPUs require the Intel Ice Lake CPU platform.

### N2D Instances

### pd-balanced

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
2-7 | 15,000 | 15,000 | 240 | 240  
8-15 | 15,000 | 15,000 | 8001 | 800  
16-31 | 20,000 | 20,000 | 1,2001 | 1,200  
32-63 | 50,000 | 50,000 | 1,2001 | 1,200  
64 or more | Up to 80,0001 | Up to 80,000 | 1,2001 | 1,200  
  
1 For regional Balanced Persistent Disk, the maximum write IOPS is 60,000 and the maximum write throughput is 600 MiB/s. 

### pd-ssd

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
2-7 | 15,000 | 15,000 | 240 | 240  
8-15 | 15,000 | 15,000 | 800 | 800  
16-31 | 25,000 | 25,000 | 1,2001 | 1,200  
32-63 | 60,000 | 60,000 | 1,2001 | 1,200  
64 or more | Up to 100,0001 | Up to 100,000 | 1,200 | 1,200  
  
1 For regional SSD Persistent Disk, the maximum write IOPS is 80,000 and the maximum write throughput is 1,000 MiB/s. 

### pd-standard

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
2-7 | 15,000 | 3,000 | 2401 | 240  
8-15 | 15,000 | 5,000 | 4001 | 800  
16 or more | 15,000 | 7,500 | 4001 | 1,200  
  
1 For regional Standard Persistent Disk, the maximum write throughput is 200 MiB/s. 

### M1 Instances

### pd-balanced

Machine type | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
m1-megamem-96 | 80,000 | 80,000 | 1,200 | 1,200  
m1-ultramem-40 | 60,000 | 60,000 | 1,200 | 1,200  
m1-ultramem-80 | 70,000 | 70,000 | 1,200 | 1,200  
m1-ultramem-160 | 70,000 | 70,000 | 1,200 | 1,200  
  
### pd-ssd

Machine type | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
m1-megamem-96 | 100,000 | 100,000 | 1,200 | 1,200  
m1-ultramem-40 | 60,000 | 60,000 | 1,200 | 1,200  
m1-ultramem-80 | 70,000 | 70,000 | 1,200 | 1,200  
m1-ultramem-160 | 70,000 | 70,000 | 1,200 | 1,200  
  
### pd-standard

Machine type | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
m1-megamem-96 | 15,000 | 7,500 | 400 | 1,200  
m1-ultramem-40 | 15,000 | 7,500 | 400 | 1,200  
m1-ultramem-80 | 15,000 | 7,500 | 400 | 1,200  
m1-ultramem-160 | 15,000 | 7,500 | 400 | 1,200  
  
### pd-extreme

Machine type | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
m1-megamem-96 | 90,000 | 90,000 | 2,200 | 2,200  
  
### M2 Instances

### pd-balanced

Machine type | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
m2-megamem-416 | 40,000 | 40,000 | 1,200 | 1,200  
m2-ultramem-208 | 40,000 | 40,000 | 1,200 | 1,200  
m2-ultramem-416 | 40,000 | 40,000 | 1,200 | 1,200  
m2-hypermem-416 | 40,000 | 40,000 | 1,200 | 1,200  
  
### pd-ssd

Machine type | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
m2-megamem-416 | 40,000 | 40,000 | 1,200 | 1,200  
m2-ultramem-208 | 40,000 | 40,000 | 1,200 | 1,200  
m2-ultramem-416 | 40,000 | 40,000 | 1,200 | 1,200  
m2-hypermem-416 | 40,000 | 40,000 | 1,200 | 1,200  
  
### pd-standard

Machine type | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
m2-megamem-416 | 15,000 | 7,500 | 400 | 1,200  
m2-ultramem-208 | 15,000 | 7,500 | 400 | 1,200  
m2-ultramem-416 | 15,000 | 7,500 | 400 | 1,200  
m2-hypermem-416 | 15,000 | 7,500 | 400 | 1,200  
  
### pd-extreme

Machine type | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
m2-megamem-416 | 40,000 | 40,000 | 1,200 | 2,200  
m2-ultramem-208 | 40,000 | 40,000 | 1,200 | 2,200  
m2-ultramem-416 | 40,000 | 40,000 | 1,200 | 2,200  
m2-hypermem-416 | 40,000 | 40,000 | 1,200 | 2,200  
  
### M3 Instances

**Note:** These machine types use the NVMe disk interface for Persistent Disk.

### pd-balanced

Machine type | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
m3-megamem-64 | 40,000 | 40,000 | 1,200 | 1,200  
m3-megamem-128 | 80,000 | 80,000 | 1,200 | 1,200  
m3-ultramem-32 | 40,000 | 40,000 | 1,200 | 1,200  
m3-ultramem-64 | 40,000 | 40,000 | 1,200 | 1,200  
m3-ultramem-128 | 80,000 | 80,000 | 1,200 | 1,200  
  
### pd-ssd

Machine type | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
m3-megamem-64 | 40,000 | 40,000 | 1,200 | 1,200  
m3-megamem-128 | 80,000 | 80,000 | 1,200 | 1,200  
m3-ultramem-32 | 40,000 | 40,000 | 1,200 | 1,200  
m3-ultramem-64 | 40,000 | 40,000 | 1,200 | 1,200  
m3-ultramem-128 | 80,000 | 80,000 | 1,200 | 1,200  
  
### pd-extreme

Machine type | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
m3-megamem-64 | 40,000 | 40,000 | 1,200 | 2,200  
m3-megamem-128 | 80,000 | 80,000 | 1,700 | 2,200  
m3-ultramem-32 | 40,000 | 40,000 | 1,200 | 2,200  
m3-ultramem-64 | 40,000 | 40,000 | 1,200 | 2,200  
m3-ultramem-128 | 80,000 | 80,000 | 1,700 | 2,200  
  
### T2D Instances

### pd-balanced

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
1 | 15,000 | 15,000 | 204 | 240  
2-7 | 15,000 | 15,000 | 240 | 240  
8-15 | 15,000 | 15,000 | 800 | 800  
16-31 | 20,000 | 20,000 | 1,200 | 1,200  
32-60 | 50,000 | 50,000 | 1,200 | 1,200  
  
### pd-ssd

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
1 | 15,000 | 15,000 | 204 | 240  
2-7 | 15,000 | 15,000 | 240 | 240  
8-15 | 15,000 | 15,000 | 800 | 800  
16-31 | 25,000 | 25,000 | 1,200 | 1,200  
32-60 | 60,000 | 60,000 | 1,200 | 1,200  
  
### pd-standard

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
1 | 15,000 | 3,000 | 204 | 240  
2-7 | 15,000 | 3,000 | 240 | 240  
8-15 | 15,000 | 5,000 | 400 | 800  
16 or more | 15,000 | 7,500 | 400 | 1,200  
  
### T2A Instances

**Note:** These machine types use the NVMe disk interface for Persistent Disk.

### pd-balanced

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
1 | 20,000 | 20,000 | 204 | 240  
2-7 | 20,000 | 20,000 | 240 | 240  
8-15 | 25,000 | 25,000 | 800 | 800  
16-31 | 25,000 | 25,000 | 1,200 | 1,200  
32-47 | 60,000 | 60,000 | 1,200 | 1,200  
48 | 80,000 | 80,000 | 1,800 | 1,800  
  
### pd-ssd

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
1 | 20,000 | 20,000 | 204 | 240  
2-7 | 20,000 | 20,000 | 240 | 240  
8-15 | 25,000 | 25,000 | 800 | 800  
16-31 | 25,000 | 25,000 | 1,200 | 1,200  
32-47 | 60,000 | 60,000 | 1,200 | 1,200  
48 | 80,000 | 80,000 | 1,800 | 1,800  
  
### pd-standard

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
1 | 15,000 | 1,000 | 204 | 240  
2-3 | 15,000 | 2,400 | 240 | 240  
4-7 | 15,000 | 3,000 | 240 | 240  
8-15 | 15,000 | 5,000 | 400 | 800  
16 or more | 15,000 | 7,500 | 400 | 1,200  
  
### TPU v5e instances

### pd-balanced

Machine type | Maximum IOPS  
(read/write) | Maximum throughput (read/write)  
(MiB/s)  
---|---|---  
`ct5lp-hightpu-1t` | 20,000 | 1,200  
`ct5lp-hightpu-4t` | 80,000 | 1,200  
`ct5lp-hightpu-8t` | 80,000 | 1,200  
  
### TPU v5p instances

### pd-balanced

Machine type | Maximum IOPS  
(read/write) | Maximum throughput (read/write)  
(MiB/s)  
---|---|---  
`ct5p-hightpu-4t` | 80,000 | 1,200  
  
### TPU v3 and TPU v4 instances

### pd-balanced

Machine type | Maximum IOPS  
(read/write) | Maximum throughput (read/write)  
(MiB/s)  
---|---|---  
`ct3-hightpu-4t` | 80,000 | 1,200  
`ct3p-hightpu-4t` | 80,000 | 1,200  
`ct4p-hightpu-4t` | 80,000 | 1,200  
  
### Z3 Instances

**Note:** These machine types use the NVMe disk interface for Persistent Disk.

### pd-balanced

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
8 to 14 | 15,000 | 15,000 | 240 | 240  
22 to 32 | 20,000 | 20,000 | 800 | 800  
44 | 50,000 | 50,000 | 1,200 | 1,200  
88 | 80,000 | 80,000 | 1,200 | 1,200  
176 | 80,000 | 80,000 | 1,200 | 1,200  
  
### pd-ssd

Number of vCPUs | Maximum write IOPS | Maximum read IOPS | Maximum write throughput (MiB/s) | Maximum read throughput (MiB/s)  
---|---|---|---|---  
8 to 14 | 15,000 | 15,000 | 240 | 240  
22 to 32 | 25,000 | 25,000 | 800 | 800  
44 | 60,000 | 60,000 | 1,200 | 1,200  
88 | 80,000 | 80,000 | 1,200 | 1,200  
176 | 80,000 | 80,000 | 1,200 | 1,200  
  
### Example

Consider a 1,000 GiB zonal SSD Persistent Disk attached to an N2 instance with 4 vCPUs. The read limit based solely on the size of the disk is 36,000 IOPS (6,000 baseline IOPS + (30 IOPS per GiB * 1,000 GiB)). However, the instance has only 4 vCPUs so the read limit is restricted to 15,000 IOPS.

## Review performance

You can review Persistent Disk performance metrics in [Cloud Monitoring](https://console.cloud.google.com/monitoring), Google Cloud's integrated monitoring solution.

To learn more, see [Reviewing Persistent Disk performance metrics](https://docs.cloud.google.com/compute/docs/disks/review-disk-metrics).

## Optimize disk performance

Keep the following factors in mind when reviewing the performance of your Persistent Disk volumes:

  * Persistent Disk are networked storage and generally have higher latency compared to physical disks or [Local SSDs](https://docs.cloud.google.com/compute/docs/disks/local-ssd). To reach the maximum performance limits of the Persistent Disk, you must issue enough I/O requests in parallel. To check if you're using a high enough queue depth to reach your required performance levels, see [I/O queue depth](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance#io-queue-depth).

  * Make sure that your application is issuing enough I/O requests to saturate the disk. Disk saturation occurs when the CPU time during I/O requests issued to the device is very high.

  * For workloads that primarily involve small (from 4 KB to 16 KB) random I/O requests, the limiting performance factor is I/O requests per second [(IOPS)](https://wikipedia.org/wiki/IOPS).

  * For workloads that primarily involve sequential or large (256 KB to 1 MB) random I/O requests, the limiting performance factor is [throughput](https://wikipedia.org/wiki/Throughput).




To increase disk performance, start with the following steps:

  * [Resize your Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk) to increase the per-disk IOPS and throughput limits. Persistent Disk don't have any reserved, unusable capacity, so you can use the full disk without performance degradation. However, certain file systems and applications might perform worse as the disk becomes full, so you might need to consider increasing the size of your disk to avoid such situations.

  * [Change the machine type](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance) and number of vCPUs on the instance to increase the per-instance IOPS and throughput limits.




After choosing the right disk size and machine type for your instance to resolve any performance bottlenecks, your application and OS might need additional tuning. For more information, see [Optimizing Persistent Disk performance](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance) and [Optimizing Local SSD performance](https://docs.cloud.google.com/compute/docs/disks/optimizing-local-ssd-performance).

## What's next

  * Benchmark your [Local SSDs](https://docs.cloud.google.com/compute/docs/disks/benchmarking-local-ssd-performance) and [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/benchmarking-pd-performance-linux) that are attached to Linux instances.
  * Optimize your [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance) and [Local SSD](https://docs.cloud.google.com/compute/docs/disks/optimizing-local-ssd-performance) performance.
  * Learn about [Persistent Disk](https://docs.cloud.google.com/compute/disks-image-pricing#persistentdisk) and [Local SSD](https://docs.cloud.google.com/compute/disks-image-pricing#localssdpricing) pricing.
  * Learn how to review your project log entries [using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
