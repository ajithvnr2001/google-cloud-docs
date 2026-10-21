---
url: https://docs.cloud.google.com/compute/docs/disks/pools/
title: Hyperdisk pools overview \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:29.457809+00:00
---

# Hyperdisk pools overview  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Hyperdisk pools overview Stay organized with collections  Save and categorize content based on your preferences. 

This document discusses the features and benefits of Hyperdisk pools in Compute Engine and how to choose the right pool for your workloads.

You can simplify disk management and reduce costs with Hyperdisk pools. Hyperdisk pools let you purchase capacity and performance in bulk instead of for individual disks. You can then create disks in the pool to consume the purchased resources. Disks that are in a pool can be used as boot disks and data disks for your instances and containers.

## When to use pools

For large scale workloads with high concurrent performance needs, Google recommends pools.

Compute Engine offers two types of pools: Hyperdisk Storage Pools and Hyperdisk Exapools. To choose a pool type, see How to choose a pool type.

As a general guideline, if your workload has one or more of the following requirements within a single project and zone, you should support the workload by using Hyperdisk pools:

Workload type | Thresholds for using Hyperdisk pools | Recommended pool type  
---|---|---  
Accelerator (GPU / TPU) instances with attached boot and scratch disks Parallel file systems like HDFS or Lustre with high concurrent usage | 

  * 1 PiB or more of provisioned capacity per zone
  * 1 TiB/s or more of provisioned throughput performance
  * 10 million (10,000,000) or more provisioned IOPS

| 

  * Hyperdisk Exapools
  * Hyperdisk Storage Pools

  
Large enterprise workloads such as enterprise apps, DBMS, or line of business apps AI/ML and HPC simulation workloads | 

  * 20 TiB or more of provisioned capacity per zone

| 

  * Hyperdisk Storage Pools

  
  
The following are examples of workloads that are suitable for a Hyperdisk pools:

  * Example workloads for **Hyperdisk Exapools** :

    * AI/ML workloads spanning 4,000 TPU VMs and using 2 PiB of Hyperdisk Balanced with provisioned performance of 20,000,000 IOPS and 3 TiB/s throughput, driving concurrent aggregate peak throughput of 500 GiB/s.
    * AI/ML training workloads with 15,000 GPU instances using Hyperdisk Balanced for boot and scratch disks with a total capacity of 8 PiB, driving a concurrent aggregate peak throughput of 1 TiB/s.
    * Parallel file system with 6 PiB or more of capacity and concurrent aggregate peaks of 800 GiB/s of read heavy throughput.
  * Example workloads for **Hyperdisk Storage Pools** :

    * AI/ML and HPC simulation workloads with 1,000 GPU instances using Hyperdisk Balanced volumes in conjunction with Local SSD as shared cache.
    * Workload spread across several databases and applications, with 100 TiB of provisioned capacity across multiple volumes used by both databases and applications.



Aggregate peak usage is the total peak capacity and performance consumed by all the disks in a workload, which is different from the sum of the provisioned performance for all the disks. To calculate your concurrent aggregate peak usage, see [Review disk performance metrics](https://docs.cloud.google.com/compute/docs/disks/review-disk-metrics).

## Disk management issues addressed by pools

Pools help reduce costs and simplify resource forecasting and disk management, especially in the following scenarios:

  * **Migrating from on-premise SAN** : Pools help simplify and shorten the transition to Google Cloud by avoiding complex per-disk capacity and performance forecasting.
  * **Combating underutilization** : Disks are frequently provisioned for peak performance, which can lead to waste. With pools, you can use thin provisioning to allocate resources as needed. Pools help you to increase your block storage utilization while also simplifying your operations.
  * **Higher costs and complex disk management** : Pools are designed to avoid the downtime needed to resize disks when performance or capacity needs increase, while still reducing the total cost of ownership. This reduces the complexity of managing hundreds or thousands of individual disks.



## Benefits of pools

Hyperdisk pools offer the following benefits:

  * Simplified cost management: predict billing more accurately based on the pool's provisioned resources rather than individual disks.
  * Shared performance: share the provisioned performance across all disks in a pool, so you don't have to purchase performance for each disk.
  * Increased efficiency and resource utilization: 
    * Allocate resources to your disks on an as-needed basis with [thin provisioning](https://en.wikipedia.org/wiki/Thin_provisioning), lowering costs and reducing waste.
    * Provision disks for their peak performance needs and still avoid paying for unused resources.
    * Reduce underutilization by measuring a pool's consumed capacity based on data written to its disks, not the disks' provisioned capacity.
    * Use data reduction strategies to more efficiently store data on disks, lowering costs.
  * Flexible disk management: increase or decrease the capacity of the pool instead of resizing individual disks.



## How pools work

A pool is a pre-purchased collection of Hyperdisk resources—capacity, throughput, and IOPS— within a zone. When you create disks for your workload, you create the disks within the pool, allocating some of the pool's resources to each new disk.

You don't pay for each individual disk's provisioned capacity or performance, only what was purchased for the pool. When you delete a disk in a pool, its allocated resources are returned to the pool for use by other disks.

There is no change to how workloads use Hyperdisk volumes when using Hyperdisk pools. Data on individual disks in a pool maintain the same isolation they would have if the disks were not created in a pool.

## How to choose a pool type

Compute Engine offers Hyperdisk Storage Pools and Hyperdisk Exapools. The type of pool that you use depends on the scale of your workload.

  * [Hyperdisk Storage Pools](https://docs.cloud.google.com/compute/docs/disks/storage-pools): for Enterprise workloads that require 20 TiB or more of capacity within a single zone and project, Google recommends using Hyperdisk Storage Pools.

  * [Hyperdisk Exapools](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-exapools): for very large workloads that require 1 TiB/s or more of provisioned performance. To use Exapools, you must [contact your account team](https://docs.cloud.google.com/tam).




### Supported Hyperdisk types for pools

When you create a pool, you specify a Hyperdisk type for the pool. All the disks in the pool must be the same Hyperdisk type. Hyperdisk Exapools and Hyperdisk Storage Pools support the following Hyperdisk types:

  * [Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced)
  * [Hyperdisk Throughput](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput)



To learn about the differences between Hyperdisk types, see [Choose a Hyperdisk type](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#when-to-use).

## Provisioning types for pools

When you create a pool, you select provisioning types for capacity and performance. The provisioning type that you select determines which pool features are available. Hyperdisk pools offer the following provisioning types:

  * Standard capacity provisioning: simplifies cost management by letting you purchase aggregate capacity.

  * Advanced capacity provisioning: removes the need to resize disks or create very large disks.

  * Standard performance provisioning: prevents contention in disks with correlated performance spikes.

  * Advanced performance provisioning: prevents contention in disks with different peak utilization times.


**Note:** pools are logical administrative and billing boundaries; they don't reserve or dedicate isolated physical hardware in the zone. Regardless of the provisioning type you choose, you can't create or resize disks within a pool unless the zone has sufficient physical capacity. If the zone doesn't have enough physical capacity for the required disk type, then creating or resizing a disk in the pool might fail with a `ZONE_RESOURCE_POOL_EXHAUSTED` error even if you haven't exceeded the pool's provisioned capacity.

A pool that uses advanced capacity provisioning is referred to as an _advanced capacity pool_ , while a pool that uses standard capacity provisioning is referred to as a _standard capacity pool_.

For Hyperdisk Storage Pools, you can use standard or advanced capacity provisioning. You can also combine different provisioning types for capacity and performance. For example, you can create a Storage Pool that uses advanced provisioning for capacity and standard provisioning for performance.

For Hyperdisk Exapools, you can use only advanced provisioning for capacity and performance.

## Standard and advanced capacity provisioning

Advanced provisioning offers cost savings, more flexible disk management, and more efficient consumption of pool resources than standard provisioning. Disks in a standard capacity pool don't offer any additional cost-saving features.

The following table highlights the differences between standard capacity and advanced capacity provisioning.

Feature | Standard capacity | Advanced capacity | Benefit of advanced capacity  
---|---|---|---  
Capacity consumption | Based on provisioned capacity at creation | Based on actual bytes written (post-data reduction) | Higher efficiency: you pay only for what you use in the pool, and not what's provisioned to the disks. Reduces wasted space.  
Overprovisioning | Not available | Total disk capacity can exceed the pool's capacity | Simplified capacity planning and disk management: provision disks for peak future needs without paying for it upfront. Avoids the downtime associated with frequent disk resizing.  
Pool resize condition | Sum of provisioned disk capacities reaches pool capacity | Actual written data (post-reduction) reaches pool capacity | Improved capacity utilization: pool capacity is usable until it's filled with data, not just allocated to disks.  
Autogrow support | Not available | Available for Storage Pools (at 80% utilization); not available for Exapools | Proactive management: prevent out-of-space errors by automatically adding capacity based on write volume.  
Cost basis | Sum of capacity provisioned to individual disks | Total performance provisioned for the pool | Lower costs: lower your overall cost by provisioning for initial estimated consumption.  
  
### Standard capacity provisioning

Standard capacity provisioning is the best option for workloads with any of the following properties:

  * The main goal is to simplify capacity planning and cost management.
  * The capacity requirements for each disk are fixed.
  * Disks are created and deleted frequently. With pools, you only need to purchase capacity once and the disks can be created and deleted as needed.



Disks in pools that use standard capacity provisioning have the following properties:

  * Capacity consumption is measured based on how much is provisioned, not how much data is written to the disk. For example, if you create a 1 TiB disk in a pool with standard capacity, the pool's available capacity is reduced by 1 TiB, even if the disk doesn't contain any data.
  * A pool that uses standard capacity provisioning is considered full if all the provisioned capacity has been _allocated_ to disks within the pool. You can't provision any more capacity to the disks or create new disks. You must provision more capacity to the pool or delete some disks. This is true even if all the disks are blank.



### Advanced capacity provisioning

Disks in an advanced capacity pool consume capacity differently than disks in a standard capacity pool and disks that aren't in a pool.

Disks in pools that use advanced capacity provisioning have the following features:

  * Overprovisioning
  * Thin provisioning
  * Data reduction
  * Autogrow



#### Overprovisioning capacity

Overprovisioning capacity lets you provision the disks for their peak capacity, without provisioning the pool for the total combined capacity of the disks. This lets you generously provision performance for the disks, reduce costs, and avoid downtime from resizing.

The total provisioned capacity of the disks depends on the type of pool and its provisioned capacity. For Hyperdisk Storage Pools, the overprovisioning limit is 5x the pool's provisioned capacity. For Hyperdisk Exapools, the overprovisioning limit is 50x the pool's provisioned capacity. Each disk can consume up to its provisioned performance and capacity. However, the cumulative consumption across all the disks in the pool can't exceed the pool's provisioned capacity.

#### Thin provisioning for capacity

Capacity is allocated to disks as needed, and not when the disk is provisioned. Thus, the pool isn't full when all the provisioned space has been allocated to disks. The pool is full when all the provisioned space has been utilized by written data.

#### Data reduction

To reduce the space used by written data, Compute Engine applies data reduction strategies to the data your applications write to reduce the data written to the disks.

#### Autogrow for advanced capacity pools

If Compute Engine detects that 80% of an advanced capacity pools's provisioned capacity is utilized, Compute Engine attempts an _autogrow_ , an increase of the provisioned capacity of the pool.

**Note:** Autogrow isn't attempted when the total capacity _provisioned_ to the disks in the pool reaches or exceeds 80% of the pool's capacity. Rather, autogrow is attempted when the _data written_ to all disks in the pool reaches or exceeds 80% of the pool capacity.

If autogrow fails and the pool's capacity is fully used by written data, then writes to all the pool's disks will fail until you perform one of the actions:

  * Increase the pool's provisioned capacity.
  * Delete disks in the pool.
  * Delete data on disks in the pool.



If you delete data on disks in the pool to free up space, keep in mind the following:

  * Most software applications interpret the errors returned when the pool space is exhausted in a manner similar to hardware failures. You must monitor your pool to avoid running out of disk space. You should also understand how your workload responds if it runs out of disk space.

  * Pools don't have visibility into your file system, so deleted data is considered to be in use until your operating system (OS) marks it unused with a `DISCARD` or `TRIM` command. All Google-provided OS images are configured to do this by default. If you aren't using a Google-provided OS image, confirm that this feature is available. To learn more, see [Disable lazy initialization and enable DISCARD commands](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance#formatting_parameters).




### Compare capacity provisioning types

For the following examples, suppose you have two Hyperdisk Throughput Storage Pools, `std-pool` and `adv-pool`, that are provisioned with standard capacity and advanced capacity provisioning, respectively. Each pool is provisioned with 100 TiB of capacity.

#### Overprovisioning capacity example

Because of overprovisioning, the maximum cumulative capacity of all the disks in `adv-pool` is 500 TiB, but only 100 TiB for `std-pool`.

#### Thin provisioning capacity example

Suppose you create one blank 20 TiB disk in each pool. Because of thin provisioning, the consumed capacity for `adv-pool`, or how much data has been written to all the disks in the pool, is 0. This is because the disk you created is blank. For `std-pool`, the blank disk consumes 20 TiB of capacity. Using advanced capacity provisioning, your applications can write more data before you have to increase the capacity of the pool.

#### Capacity consumption example

Suppose you write 500 GiB of data to the disks in each pool. `adv-pool` still has 99.5 TiB of free space for new data, while `std-pool` has 80 TiB of space. This is because for `adv-pool`, data consumption is based on usage, not provisioned capacity.

#### Increasing capacity example

If an advanced capacity pool's consumed capacity approaches its maximum, you can increase the pool's capacity without resizing individual disks. For example, consider the following scenario.

  * The capacity of `adv-pool` is 100 TiB, but it contains 50 5 TiB disks, for a total provisioned capacity of 250 TiB.
  * Each disk writes 1 TiB of data.
  * Your application's demand indicates that each disk will write an additional 3 TiB of data, and the anticipated total capacity is now 200 TiB.
  * The pool's actual capacity is 100 TiB and only has 50 TiB capacity remaining.



With `adv-pool`, you can increase the pool's capacity to 500 TiB without resizing the individual disks since they are all provisioned to 5 TiB.

With `std-pool`, you'd have to increase both the capacity of the pool and each individual disk.

## Standard and advanced performance provisioning

When you create a pool, you must choose a provisioning type for performance. The provisioning type you choose determines which pool features are available.

For Hyperdisk Storage Pools, you can choose standard or advanced performance provisioning. You can also combine different provisioning types for capacity and performance. For example, you can create a pool that uses advanced provisioning for capacity and standard provisioning for performance.

For Hyperdisk Exapools, you can use only advanced performance provisioning.

The following table highlights the differences between standard performance and advanced performance provisioning.

Feature | Standard performance | Advanced performance | Benefit of advanced performance  
---|---|---|---  
Pool consumption | Based on _provisioned_ IOPS or throughput | Based on _used_ IOPS or throughput | More efficient use of provisioned pool performance: provision for aggregate use, not for peak performance of each disk.  
Performance sharing | Not supported | Disks share the pool's performance resources | Improved utilization: performance not used by idle disks is available for active disks.  
Overprovisioning | Not supported | Total disk provisioned performance can exceed the pool's provisioned performance | Simplified performance planning and disk management: provision disks for peak future needs without paying for it upfront. Avoids frequent disk performance updates.  
Risk of contention | Low risk; ideal for correlated peaks | Higher risk; contention is possible if many disks peak simultaneously | Lower costs: enables cost savings and efficiency when disks don't simultaneously require peak performance  
Cost basis | Sum of performance provisioned to individual disks | Total performance provisioned for the pool | Lower costs: provision for the expected aggregate peak usage rather than the sum of individual disk peaks  
  
### Standard performance provisioning

Standard performance provisioning is the best option for workloads with any of the following properties:

  * Workloads that can't succeed if performance is limited by pool resources.
  * Workloads where the disks in the pool are likely to have correlated performance spikes, for example, data disks for databases that are at peak utilization every morning.



Disks in a standard performance pool have the following properties:

  * Performance consumption is measured based on how much is provisioned to the disk, and not how much performance the disk is actively consuming. For example, if you provision a disk with 500 MiB/s of throughput in a standard performance pool, the pool's available performance is reduced, even if the disk is idle.
  * If all the pool's performance has been _provisioned_ to disks within the pool, you can't create new disks in the pool or add more performance to existing disks. This is true even if all the disks are idle. To create new disks, you must provision more performance to the pool, reduce the provisioned performance of some disks, or delete some disks.



### Advanced performance provisioning

Advanced performance pools are suited for disks that don't have correlated peak usage times. Disks in pools that use advanced performance provisioning have the following properties:

  * Overprovisioning
  * Thin provisioning
  * Autogrow



#### Overprovisioning for performance

Overprovisioning lets you provision the disks for their peak performance, without provisioning the pool for the total combined performance of the disks. Each disk can consume performance up to its provisioned limit. However, at any moment, the total concurrent performance of the pool can't exceed the pool's provisioned performance.

For Hyperdisk Storage Pools, the overprovisioning limit is 5x the pool's provisioned performance. For Hyperdisk Exapools, the overprovisioning limit is 50x the pool's provisioned write performance.

#### Thin provisioning and shared performance

Performance is allocated to disks as needed, not when the disk is provisioned. Also, the disks in an advanced performance pool can share its provisioned performance, up to the provisioned performance limit for each disk. This can provide cost savings for disks that have different peak usage times.

#### Autogrow for pool performance

**Note:** Hyperdisk Exapools don't support autogrow.

The disks in an advanced performance pool can contend with each other for performance resources if the total performance they consume at the same time reaches the pool's provisioned performance.

Contention for performance means that the disks might not achieve their maximum provisioned performance. If Compute Engine detects contention for performance resources for a prolonged period of time, Compute Engine attempts to automatically add performance to the pool.

Autogrow isn't attempted when the total performance _provisioned_ to the disks in the pool is 80% or more of the pool's performance. Rather, autogrow is attempted when the _disks are consuming_ 80% or more of the pool's performance at the same time.

When using advanced performance pools, you should:

  * Monitor your pools to avoid running out of provisioned performance.
  * Understand how your workload responds if it runs out of provisioned performance.



### Compare performance provisioning types

For the following examples, suppose you're designing a workload with 1,000 disks, where each disk needs to be provisioned with 10,000 IOPS, and you need to choose a performance provisioning type.

#### Overprovisioning for performance example

Suppose that the cumulative performance requirement for all the disks is 10,000,000 IOPS.

For a standard performance pool, you must provision and pay for 10,000,000 IOPS.

For an advanced performance pool, you can provision it with 1,000,000 IOPS. Because the pool supports overprovisioning, you can provision each disk with 10,000 IOPS for a total of 10,000,000 IOPS. However, you only pay for the 1,000,000 IOPS provisioned for the pool.

#### Shared performance example

Suppose that even though each disk needs 10,000 IOPS, they peak at different times. You determine that disks in the pool need up to 1,000,000 IOPS at any given time.

For a standard performance pool, you have to provision and pay for 10,000,000 IOPS (10,000 IOPS per disk), even though the disks never need more than 1,000,000 IOPS at a time.

For an advanced performance pool with 1,000,000 IOPS, the disks can share the pool's performance. Since the disks have different performance peaks, they can simultaneously consume up to 1,000,000 IOPS, even though the total provisioned performance is 10,000,000 IOPS.

## Reservations for pools

You can use pools with [reservations of Compute Engine zonal resources](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type) as follows:

  * **Reserve storage pool capacity together with compute resources** : to reserve storage pool capacity together with GPU, TPU, or H4D instances, you use _future reservations for capacity blocks_. Google delivers your requested compute resources and an auto-created Storage Pool or Exapool together at your chosen start time.

  * **Attach disks from an independent storage pool to reserved compute instances** : if you create a Storage Pool or Exapool separately outside of a reservation, then you can still attach disks from that pool to compute instances that consume a compute reservation. You can attach these disks when you launch the compute instance or attach them to a running compute instance. For more information, see [Consume reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-consume).




## Pricing

You're billed for Hyperdisk pools based on the capacity and performance you purchased for the pool. You aren't billed for the provisioned IOPS, throughput, or capacity for the disks created in the storage pool.

Hyperdisk Exapools are eligible for resource-based committed use discounts (CUDs) with a minimum 1-year or up to 3-year commitment. When you purchase a 1- or 3-year Exapool, you automatically qualify for resource-based CUDs in 1- or 3-year commitments.

Hyperdisk Storage Pools aren't eligible for CUDs or sustained use discounts (SUDs).

For more information, see [Disk pricing](https://docs.cloud.google.com/compute/disks-image-pricing?e=48754805#section-2).

## What's next

  * For more information about Hyperdisk Storage Pools, see [About Hyperdisk Storage Pools](https://docs.cloud.google.com/compute/docs/disks/storage-pools)
  * For more information about Exapools, see [Hyperdisk Exapools overview](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-exapools)
  * Learn how to [Create a pool](https://docs.cloud.google.com/compute/docs/disks/create-storage-pools)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
