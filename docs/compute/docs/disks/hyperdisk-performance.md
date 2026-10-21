---
url: https://docs.cloud.google.com/compute/docs/disks/hyperdisk-performance/
title: Google Cloud Hyperdisk performance overview \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:30.853833+00:00
---

# Google Cloud Hyperdisk performance overview  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/hyperdisk-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Google Cloud Hyperdisk performance overview Stay organized with collections  Save and categorize content based on your preferences. 

This document discusses how Google Cloud Hyperdisk performance works so that you can understand your Hyperdisk volumes' performance and select the right Hyperdisk type for your workload.

Hyperdisk is Google Cloud's recommended durable block storage option. To learn more about Hyperdisk, see [About Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).

For detailed performance limits, see [Hyperdisk performance limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits).

To review the current or past performance of a Hyperdisk volume, see [Review disk performance metrics](https://docs.cloud.google.com/compute/docs/disks/review-disk-metrics).

## Terminology and units

Hyperdisk performance, as discussed in this document, refers to IOPS and throughput.

  * _IOPS_ stands for input/output operations per second. This is the number of individual reads and writes the volume performs or can perform within a second.
  * _Throughput_ refers to how many bytes can be read from or written to a volume in a second. Throughput is measured in MiB/s.



Size measurements are in GiB or TiB.

### Machine type terminology

The term _compute instance_ refers to a virtual machine (VM) instance or bare metal instance. A compute instance's _machine type_ is the specific combination of its properties, like its machine series and number of vCPUs.

In this document, machine types are denoted in this format: `M-*-N`, where: 

  * `M` is the machine series, for example, `C3`
  * `*` represents all memory and CPU configurations, for example, `standard` or `highcpu`
  * `N` is the number of vCPUs, CPUs, or the GPU designation, for example, 22 for an instance with 22 vCPUs, or `8g` for an instance with 8 GPUs 

This format includes the following machine types, wherever available: 
  * bare metal machine types (`*-metal`)
  * machine types that come with attached Local SSD disks (`*-lssd`, `*-standardlssd`, or `*-highlssd`).



For example, `c3-*-176` refers to C3 machine types with 176 vCPUs, like `c3-standard-176`, `c3-highcpu-176`, `c3-highmem-176`, and `c3-standard-176-lssd`. For more information, see [Compute Engine terminology](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology). 

## Summary of Hyperdisk performance

When you attach Hyperdisk volumes to an instance, the maximum achievable performance depends on the scenario, as outlined in the following table.

Number of Hyperdisk  
volumes | Maximum performance  
---|---  
1 | The volume's performance is the lesser of: 

  * The volume's provisioned performance
  * The machine type's performance limit for the Hyperdisk type. 

  
2 or more of the same Hyperdisk type | The total performance for all the volumes is the lesser of: 

  * The sum of the provisioned performance of each volume
  * The machine type's performance limit for the Hyperdisk type

  
2 or more Hyperdisk types | The total performance for all the volumes is the lesser of: 

  * The sum of the provisioned performance of each volume
  * The performance limits for the instance's machine type

  
  
For limits by Hyperdisk type, see [ Performance limits by Hyperdisk type](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-by-hd-type).

For limits by machine type, see [ Performance limits by machine type](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#machine-type-limits).

## About provisioned performance for Hyperdisk

You can specify a target performance level for a Hyperdisk volume. The IOPS or throughput value you specify, or provision, is referred to as the _provisioned performance_.

**Important:** For a Hyperdisk volume to reach its provisioned performance, you must attach it to an instance that supports that level of performance or higher.

You can provision a volume's performance when you create the volume. You can also increase or decrease the performance while the volume is in use without having to increase the volume's size.

The provisioned performance isn't a guaranteed level of performance. Rather, it's the target performance level that you expect the volume to need during peak usage times. Actual performance depends on the limits of the instance that uses the volume and several other factors.

### Default performance levels

Provisioning a performance level for a Hyperdisk volume is optional. If you don't specify a value, for example, because you're not sure how much IOPS or throughput your workload needs, Compute Engine creates the volume with default values. You can increase or decrease the value later. Default values vary by Hyperdisk type and are listed in the **Default IOPS and throughput values** section for [Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#default-perf), [Hyperdisk Balanced High Availability](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha#default-perf), [Hyperdisk Extreme](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme#default-perf), [Hyperdisk Throughput](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput#default-perf), or [Hyperdisk ML](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-ml#default-perf).

## Limits for provisioned performance

The maximum performance you can provision depends on the Hyperdisk type and the size of the volume.

### Limit for the Hyperdisk type

Each Hyperdisk type has a maximum level of performance that you can provision. Some Hyperdisk types let you provision IOPS, throughput, or both. If you can't provision throughput, the throughput for the volume depends on the provisioned IOPS. Likewise, if you can't provision IOPS, the IOPS for the volume depends on the throughput you provision.

For example, you can provision throughput for Hyperdisk ML volumes, but not IOPS. The IOPS-to-throughput rate for Hyperdisk ML is 16 IOPS per MiB/s of provisioned throughput. So if you create a Hyperdisk ML volume with 100,000 MiB/s of throughput, then the volume is provisioned with 1,600,000 IOPS.

### Size based limits

The maximum performance you can provision changes with the volume's size. For example, for a 10 TiB Hyperdisk Balanced volume, you can provision 3,000 to 160,000 IOPS, but for a 50 GiB volume, you can provision 3,000 to 25,000 IOPS.

For details about the size-based limits for each Hyperdisk type, see the **Size and performance limits** section on the [Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#size_limits), [Hyperdisk Balanced High Availability](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha#size_limits), [Hyperdisk Extreme](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme#size_limits), [Hyperdisk Throughput](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput#size_limits), and [Hyperdisk ML](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-ml#size_limits) pages.

The following table lists the maximum performance you can provision for each Hyperdisk type.

**Note:** Hyperdisk performance is half-duplex, so the IOPS and throughput limits are shared between read and write operations. This means that if a machine type has a 50,000 IOPS limit, then the sum of the reads and writes every second can't exceed 50,000. 

Hyperdisk type | Max provisionable performance per volume | Customizable throughput | Customizable IOPS  
---|---|---|---  
Hyperdisk Balanced | 160,000 IOPS  
2,400 MiB/s  | Yes | Yes  
Hyperdisk Balanced High Availability | 100,000 IOPS  
2,400 MiB/s | Yes | Yes  
Hyperdisk Extreme | 350,000 IOPS | No; 250 MiB/s per 1,000 IOPS, up to 5,000 MiB/s | Yes  
Hyperdisk ML | 2,097,152 MiB/s | Yes | No; 16 IOPS per MiB/s of throughput, up to 33,554,432 IOPS  
Hyperdisk Throughput | 2,400 MiB/s | Yes | No; 4 IOPS per MiB/s of throughput, up to 9,600 IOPS.  
  
## Steady state performance

For workloads that are sensitive to performance variability, consider using a machine series that offers _steady state performance_. The steady state performance limit is the performance level an instance can sustain across all attached volumes. By comparison, the maximum performance level is the highest performance level that an instance can achieve.

Steady state performance limits don't constitute a service level agreement (SLA).

For a Hyperdisk volume to achieve a specific steady state performance limit, its provisioned performance must be equal to or greater than the steady state limit.

The steady state performance limit is shared across all the disks attached to the instance.

### Machine series that offer steady state performance

The following machine series offer steady state performance:

  * [A3 (H200)](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus)
  * [A4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms)
  * [C4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series)
  * [C4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4d_series)
  * [C4N](https://docs.cloud.google.com/compute/docs/network-optimized-machines#c4n_series)
  * [H4D](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_series)
  * [M4](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m4_machine_types)
  * [M4N](https://docs.cloud.google.com/compute/docs/network-optimized-machines#m4n_series)
  * [TPU7x](https://docs.cloud.google.com/tpu/docs/tpu7x)
  * [Z4D](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4d_series)
  * [Z4M](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4m_series)



## Configure a workload to meet provisioned performance

A Hyperdisk volume's actual performance—the observed performance when attached to an instance—can't exceed the following limits:

  * The volume's provisioned performance
  * The instance-specific performance limits, including specific limits for the Hyperdisk type



Therefore, to make sure your volume can reach its provisioned performance, consider the following factors:

  * Choose a machine type that supports the volume's provisioned performance _for the Hyperdisk type_. Review the guidance in Instance specific performance limits for each Hyperdisk type.

  * If you want to use different Hyperdisk types with the instance, review the information in Maximum performance limits for the machine type.




Factors like I/O size and application design, while not performance limits, also affect performance. For more information on these factors, see Workload specific factors that affect performance.

## How instance performance limits affect Hyperdisk performance

Each compute instance has the following performance limits, based on its machine type:

  * A performance limit for the Hyperdisk type
  * An overall performance limit for the instance



Each limit applies in specific situations.

### Instance performance limits for each Hyperdisk type

Each instance has a performance limit for _all Hyperdisk volumes of a given type_ that you attach to the instance.

**When this limit applies** : When you attach 1 or more Hyperdisk volumes of the same type to an instance. For each volume to reach its provisioned performance, the instance performance limit must be greater than the sum of all the volumes' provisioned performance. Otherwise, the volumes' performance can't exceed the instance's performance limit.

#### Example

Suppose you have a Hyperdisk Throughput volume, `hdt-disk-1`, that has 600 MiB/s of provisioned throughput and you want to attach it to a `c3-*-4` instance.

`c3-*-4` instances have the following throughput limits:

Hyperdisk type | Max throughput (MiB/s)  
---|---  
Hyperdisk Balanced |  400   
Hyperdisk Extreme | Not supported  
Hyperdisk Throughput |  240   
Hyperdisk Balanced High Availability |  400   
Hyperdisk ML |  400   
  
If you attach `hdt-disk-1` to the VM, the volume's actual performance can't exceed 240 MiB/s. If you attach a Hyperdisk Balanced volume instead, the Hyperdisk Balanced volume's performance can't exceed 400 MiB/s.

If you attach 2 Hyperdisk Balanced volumes to the VM, the combined performance of both Hyperdisk Balanced volumes still can't exceed 400 MiB/s. This is true regardless of the provisioned performance of both volumes.

The performance limits for each Hyperdisk by machine type are listed in [Performance limits by Hyperdisk type](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-by-hd-type).

### Overall performance limit for an instance

Each instance has an overall performance limit that it can reach. This limit is shared among all volumes attached to the instance.

**When this limit applies** : When you attach more than one type of Hyperdisk to an instance. The combined actual performance of all the volumes can't exceed the performance limit for the instance, regardless of the provisioned performance of each volume.

If the instance supports Persistent Disk, all attached Persistent Disk volumes also share the same limit.

#### Example

Suppose you have a `c3-*-22` instance, which has a max throughput of 1,800 MiB/s.

You attach the following resources to the VM:

  * 2 Hyperdisk Balanced volumes, each with 900 MiB/s provisioned throughput.
  * 1 Hyperdisk Throughput volume with 500 MiB/s provisioned throughput



The combined performance across all the volumes can't exceed 1,800 MiB/s.

For a list of the limits, see [Performance limits by machine type](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#machine-type-limits).

## Workload-specific factors that affect performance

This section discusses workload-specific factors that affect the throughput and IOPS limits that your Hyperdisk volumes can achieve. For more information about how to improve performance, see [Optimize Hyperdisk performance](https://docs.cloud.google.com/compute/docs/disks/optimize-hyperdisk).

To reach the maximum IOPS and throughput levels offered by Hyperdisk volumes, you must consider the following workload parameters:

  * **I/O size** : You must use specific block sizes to reach the IOPS and throughput limits, as follows: 
    * Maximum IOPS limits require an I/O size of 4 KB.
    * Maximum throughput limits require a I/O size of at least 256 KB.
  * **Queue length** : Queue length is the number of pending requests for a volume. To reach maximum performance limits, you must adjust your queue length according to the I/O size, IOPS, and latency sensitivity of your workload. Optimal queue length varies for each workload, but typically should be larger than 256. 
  * **Number of attached volumes** : For best performance results, we recommend attaching 8 or fewer volumes to a single instance. 



## What's next

  * View [performance limits for Hyperdisk types](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-by-hd-type)
  * View [performance limits for all machine types](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#machine-type-limits)
  * Learn how to [optimize the performance of your Hyperdisk volumes](https://docs.cloud.google.com/compute/docs/disks/optimize-hyperdisk)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
