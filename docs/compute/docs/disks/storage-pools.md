---
url: https://docs.cloud.google.com/compute/docs/disks/storage-pools/
title: Hyperdisk Storage Pools overview \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:33.697905+00:00
---

# Hyperdisk Storage Pools overview  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/storage-pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Hyperdisk Storage Pools overview Stay organized with collections  Save and categorize content based on your preferences. 

This document discusses the features and limits of Hyperdisk Storage Pools. Storage Pools are the recommended [Hyperdisk pools](https://docs.cloud.google.com/compute/docs/disks/pools) for most workloads and help you simplify disk management and reduce costs.

With Storage Pools, you purchase capacity and performance in bulk, then create disks in the pool to consume the storage.

If your workload requires more than 5 PiB of capacity or 1 TiB/s or more of provisioned throughput within a single project and zone, use a [Hyperdisk Exapool](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-exapools) instead.

## When to use Hyperdisk Storage Pools

Google recommends Storage Pools for large enterprise workloads, such as enterprise apps or DBMS, that require 20 TiB or more of provisioned disk capacity within a single project and zone.

Example workloads for **Hyperdisk Storage Pools** :

  * AI/ML and HPC simulation workloads with 1,000 GPU instances using Hyperdisk Balanced volumes in conjunction with Local SSD as shared cache.
  * Workload spread across several databases and applications, with 100 TiB of provisioned capacity across multiple volumes used by both databases and applications.



## Hyperdisk Storage Pool features

Storage Pools have the following features:

  * **Capacity and performance[thin provisioning](https://en.wikipedia.org/wiki/Thin_provisioning)**: Capacity and performance are allocated as needed instead of allocating all the resources in advance. This helps to avoid low utilization rates of storage resources, where large amounts of disk space or performance are allocated, but not used.
  * **Data reduction** : Storage Pools use a variety of data reduction technologies to increase storage efficiency. Data reduction depends greatly on the type of data stored. Data that is already compressed or encrypted before it is stored in a disk in a Hyperdisk Storage Pool won't yield additional reduction.



## How Hyperdisk Storage Pools work

You create a Storage Pool with the aggregate capacity and performance that your workloads will need, and then create disks in the Storage Pool. You can then attach the disks to your virtual machine (VM) instances. When you create the disks, you can create them with a much larger size or provisioned performance limit than is needed. This simplifies planning and provides room for growth later, without necessitating changing the disk's provisioned size or performance at a later date.

If your workloads grow and your disks need more capacity or performance, you can increase the provisioned capacity and performance of the Storage Pool. The amount of disk space or performance used by the individual disks in the Storage Pool can then increase up to the limit you specified when you created the disk. By creating the disks in an Advanced capacity or Advanced performance Storage Pool with a much larger size or performance limit initially, and allocating additional space and performance through the Storage Pool, you consolidate disk storage management and reduce costs.

If an Advanced capacity Storage Pool reaches 100% utilization and there is no free space left in the Storage Pool, writes to all disks in the Storage Pool fail until you reduce the used space in the Storage Pool by deleting data or disks. Most commercial software interprets the errors returned when the pool space is exhausted in a manner similar to hardware failures.

It's important that you actively manage and monitor your Storage Pool to avoid out of space errors. You should also understand how your workload will respond if it encounters an out of space error for a disk in a Storage Pool.

When the aggregate performance utilization of all the disks in the Storage Pool reaches the total amount of performance provisioned for the Storage Pool, the disks can encounter performance contention. If contention for performance resources is detected in an Advanced performance Storage Pool for any disks in the pools, then the auto-grow feature attempts to automatically increase the IOPS available to disks in the Storage Pool to prevent performance issues.

## Provisioning types for Hyperdisk Storage Pools

When creating a Hyperdisk Storage Pool, you can configure it with either standard or advanced provisioning for capacity and performance.

**Note:** Hyperdisk Storage Pools are logical administrative and billing boundaries; they don't reserve or dedicate isolated physical hardware in the zone. Regardless of the chosen provisioning type, you can't create or resize disks within a Storage Pool unless the zone has sufficient physical capacity. If the zone doesn't have enough physical capacity for the required disk type, then creating or resizing a disk in the Storage Pool might fail with a `ZONE_RESOURCE_POOL_EXHAUSTED` error even if you haven't exceeded the Storage Pool's provisioned capacity.

### Standard capacity Storage Pools

With Standard capacity provisioning, you create disks in the Storage Pool until the total provisioned capacity of all disks in the Storage Pool reaches the Storage Pool's provisioned capacity. Disks in a Standard capacity Storage Pool consume capacity similarly to non-Storage Pool disks.

### Advanced capacity Storage Pools

Disks in an Advanced capacity Storage Pool consume capacity differently than disks in a Standard capacity Storage Pool and non-Storage Pool disks. Advanced capacity Storage Pools offer thin-provisioning and data reduction for capacity, enabling you to provision disks with more capacity than you have purchased. Disks in an Advanced capacity Storage Pools consume capacity based only on the number of bytes written to your disks after data reduction, which means you can provision more capacity to your end users and applications than you have purchased in your Storage Pool.

With Advanced capacity, you create disks in the Storage Pool where the cumulative size of all the disks can exceed the provisioned capacity of the Storage Pool by up to 1,000%. The used capacity of the Storage Pool is defined by the amount of data written and not by the amount of provisioned disk capacity.

You can fill disks in an Advanced capacity Storage Pool up to their provisioned size as long as the data written to all disks in the Storage Pool doesn't exceed the Storage Pool capacity. If the Storage Pool utilization reaches 80% of the pool provisioned capacity, the auto-grow feature attempts to automatically add capacity to the Storage Pool. **If the Storage Pool's capacity is fully used, then writes to all Storage Pool disks will fail until you delete data or delete disks to lower the used capacity of the Storage Pool.** Most software applications interpret the errors returned when the pool space is exhausted in a manner similar to hardware failures, so it's important to both:

  * Monitor your Storage Pool to avoid running out of disk space
  * Understand how your workload responds if it does happen



Storage Pools don't have visibility into your file system, so deleted data is considered to still be in use until your operating system (OS) marks it unused with a `DISCARD` or `TRIM` command. All Google-provided OS images are configured to do this by default, as are most common third-party OS images, but you should confirm this if you are not using a Google-provided OS image. More information on verifying or configuring this feature is available at [Disable lazy initialization and enable DISCARD commands](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance#formatting_parameters).

### Standard performance Storage Pools

Standard performance provisioning is the best option for the following types of workloads: 

  * Workloads that can't succeed if performance is limited by Storage Pool resources
  * Workloads where the disks in the Storage Pool are likely to have correlated performance spikes, for example, data disks for databases that are at peak utilization every morning.



With Standard performance provisioning, thin-provisioning isn't available. Also, disks created in a Standard performance Storage Pool don't share performance resources with the rest of the Storage Pool. The aggregate amount of performance of all disks created in the Storage Pool can't exceed the total provisioned IOPS or throughput of the Storage Pool.

When creating the Storage Pool, you provision enough performance in the Storage Pool to cover the combined peak performance needs of all the disks in the Storage Pool. When you create disks in the Storage Pool, you provision an amount of performance that covers the peak performance requirements of that disk. You can continue creating disks in the Storage Pool until the total provisioned IOPS of all disks reaches the Storage Pool's provisioned amount.

In a Hyperdisk Balanced Storage Pool with Standard performance, the first 3,000 IOPS and 140 MiB/s of throughput of each disk in the Storage Pool (the _baseline performance_) don't consume Storage Pool resources. When you create disks in the Storage Pool, any IOPS and throughput in excess of the baseline values consume IOPS and throughput from the Storage Pool.

### Advanced performance Storage Pools

Advanced performance provisioning is best suited for workloads that don't have highly correlated peak usage times. If your workloads all peak at the same time, the Advanced performance Storage Pool can reach the performance limits of the Storage Pool, resulting in contention for performance resources.

Advanced performance IOPS and throughput provisioning lets you share a pool of provisioned performance across all disks in a Storage Pool. The Storage Pool dynamically allocates performance resources as the disks in the Storage Pool read and write data. Only the amount of IOPS and throughput used by a disk in the Storage Pool consumes Storage Pool performance.

Because Advanced performance Storage Pools are thinly provisioned, you can allocate more IOPS or throughput to the disks in the Storage Pool than you have provisioned for the Storage Pool—up to 500% of the IOPS or throughput provisioned for the Storage Pool. For example, if you provision 100,000 IOPS for a Storage Pool, you could have 10 disks in the Storage Pool, each provisioned with 50,000 IOPS.

In a Hyperdisk Balanced Storage Pool with Advanced performance provisioning, the disks don't have baseline performance. Every read and write operation of a Hyperdisk Balanced disk in the Storage Pool consumes provisioned Storage Pool resources.

At any given moment, when the aggregate performance used by all the disks in the Storage Pool reaches the total amount of performance provisioned for the Storage Pool, the disks can contend with each other for performance resources. As a result, the disks are not able to achieve the maximum performance levels that you provisioned for the disks. When contention for resources is detected for a prolonged period of time, Compute Engine attempts to automatically add performance to the Storage Pool. When using Advanced performance Storage Pools, you should:

  * Monitor your Storage Pools to avoid running out of provisioned performance
  * Understand how your workload responds if it does happen



**Example**

Assume that you have a Hyperdisk Balanced Storage Pool with 100,000 provisioned IOPS.

With Standard performance provisioning:

  * You can provision up to 100,000 of aggregate IOPS when creating Hyperdisk Balanced disks in the Storage Pool.
  * You are charged for the 100,000 IOPS of Hyperdisk Balanced Storage Pool provisioned performance.
  * Like disks created outside of a storage pool, Hyperdisk Balanced disks in Standard performance Storage Pools are automatically provisioned with up to 3,000 baseline IOPS and 140 MiB/s of baseline throughput. This baseline performance isn't counted against the provisioned performance for the Storage Pool. Only when you add disks to the Storage Pool with provisioned performance that's above the baseline does it count against the provisioned performance for the Storage Pool, for example:

    * A disk provisioned with 3,000 IOPS uses 0 pool IOPS and the pool still has 100,000 provisioned IOPS available for other disks.
    * A disk provisioned with 13,000 IOPS uses 10,000 pool IOPS and the pool has 90,000 provisioned IOPS remaining that you can allocate to other disks in the Storage Pool. 



With Advanced performance provisioning:

  * You can provision up to 500,000 IOPS of aggregate Hyperdisk performance when creating disks in the Storage Pool.
  * You are charged for 100,000 IOPS provisioned by the Storage Pool.
  * If you create a single disk (`Disk1`) in the Storage Pool that has 5,000 IOPS, you don't consume any IOPS from the Storage Pool provisioned IOPS. However, the amount of IOPS that you can provision to new disks created in the Storage Pool is now 495,000.
  * If `Disk1` starts to read and write data, and if it uses its maximum of 5,000 IOPS in a given minute, then 5,000 IOPS is consumed from the Storage Pool provisioned IOPS. Any other disks that you created in the same storage pool can use an aggregated maximum of 95,000 IOPS in that same minute without running into contention.



## Types of Hyperdisk Storage Pools

The type of Hyperdisk Storage Pool that you create determines the type of disks that you can create in the Storage Pool.

  * **Hyperdisk Throughput Storage Pool** : When creating the Storage Pool, you specify the capacity and throughput to provision for the Storage Pool. Each Hyperdisk Throughput disk you create in the Storage Pool uses some of the provisioned capacity and throughput.
  * **Hyperdisk Balanced Storage Pool** : When creating the Storage Pool, you specify the capacity, throughput, and IOPS to provision for the Storage Pool. Each Hyperdisk Balanced disk that you create in the Storage Pool with provisioned capacity and performance above the [baseline values](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#baseline_performance) uses some of the Storage Pool provisioned capacity and performance.



### Hyperdisk Throughput Storage Pools

You can use Hyperdisk Throughput Storage Pools to manage your Hyperdisk Throughput disk usage.

#### Machine type support

Hyperdisk Throughput Storage Pools are supported with the same machine series that support Hyperdisk Throughput. For a list of the supported machine series, see [Machine type support for Hyperdisk Throughput](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput#machine-series).

#### Hyperdisk Throughput Storage Pool regional availability

Hyperdisk Throughput Storage Pools can be used in any zone that offers Hyperdisk Throughput disks. For a list of the available regions, see [Regional availability for Hyperdisk Throughput](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput#supported-regions).

You can also check for the latest updates to the available regions and zones by using the following command:
    
    
    gcloud compute storage-pool-types list --filter="name=hyperdisk-throughput"
    

### Hyperdisk Balanced Storage Pools

You can use Hyperdisk Balanced Storage Pools to manage your Hyperdisk Balanced disk usage.

In Hyperdisk Balanced Storage Pools with Standard performance provisioning, Hyperdisk Balanced disks only consume IOPS and throughput in excess of the baseline values of 3,000 IOPS and 140 MiB/s throughput per disk. For example:

  * If you provision a Hyperdisk Balanced disk with 3,000 IOPS and 140 MiB/s throughput in a Storage Pool with Standard performance provisioning, the disk doesn't consume any IOPS or throughput from the Storage Pool.
  * If you provision a Hyperdisk Balanced disk with 4,000 IOPS and 180 MiB/s of throughput in a Storage Pool with Standard performance provisioning, the disk consumes 1,000 IOPS and 40 MiB/s of throughput from the Storage Pool.



#### Machine type support

Hyperdisk Balanced Storage Pools are supported with the same machine series that support Hyperdisk Balanced. For a list of the supported machine series, see [Machine series support for Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#machine-series).

#### Hyperdisk Balanced Storage Pool regional availability

Hyperdisk Balanced Storage Pools can be used in any zone that offers Hyperdisk Balanced. For a list of the available regions, see [Regional availability for Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#supported-regions).

You can also check for the latest updates to the available regions and zones by using the following command:
    
    
    gcloud compute storage-pool-types list --filter="name=hyperdisk-balanced"
    

## Limits for Storage Pools

The following tables list the limits for the different storage pool types.

### Hyperdisk Balanced Storage Pool

Limit | Value  
---|---  
Maximum Storage Pool provisioned capacity | 5 PiB  
Minimum Storage Pool provisioned capacity | 10 TiB  
Storage capacity increments | multiples of 1 TiB  
Maximum number of Hyperdisk Storage Pools per project, per region | 20  
Maximum number of disks in a Hyperdisk Storage Pool | 10,000  
Maximum IOPS per Storage Pool | 4,194,304  
Maximum IOPS per GiB | 

  * 30 for Standard performance
  * 6 for Advanced performance

  
Minimum IOPS per Storage Pool | 

  * 0 for Standard performance
  * 10,000 for Advanced performance

  
IOPS increments | multiples of 10,000  
Maximum throughput per Storage Pool | 1 TiB/s  
Maximum throughput per GiB of capacity | 1 MiB/s  
Minimum throughput per Storage Pool | 1 GiB/s  
Throughput increments | Multiples of 1 GiB/s  
Frequency of Storage Pool capacity changes | Twice in a 24 hour period  
Frequency of Storage Pool performance changes | Twice in a 24 hour period  
  
### Hyperdisk Throughput Storage Pool

Limit | Value  
---|---  
Maximum Storage Pool provisioned capacity | 5 PiB  
Minimum Storage Pool provisioned capacity | 10 TiB  
Storage capacity increments | multiples of 1 TiB  
Maximum number of Hyperdisk Storage Pools per project, per region | 20  
Maximum number of disks in a Hyperdisk Storage Pool | 10,000  
Maximum throughput per Storage Pool | 18 GiB/s  
Maximum throughput per TiB of capacity | 18 MiB/s  
Minimum throughput per Storage Pool | 100 MiB/s  
Minimum throughput per TiB of capacity | 10 MiB/s  
Throughput increments | multiples of 10 MiB/s  
Frequency of Storage Pool capacity changes | Twice in a 24 hour period  
Frequency of Storage Pool performance changes | Twice in a 24 hour period  
  
## Performance

Performance for disks in a Storage Pool is the same as for disks that were not created in a Storage Pool.

## Limitations of Storage Pools

Hyperdisk Storage Pools have the following limitations:

**Resource limits** :

  * You can create a Hyperdisk Storage Pool with up to 5 PiB of provisioned capacity.
  * You can create a maximum of 5 Storage Pools per hour.
  * You can create a maximum of 10 Storage Pools per day.
  * You can create at most 20 Storage Pools per project, per region. This limit is shared between a project's Hyperdisk Balanced Storage Pools and Hyperdisk Throughput Storage Pools that are in the same region.
  * You can't change the provisioning model for a pool. For example, you can't change a Standard capacity Storage Pool to an Advanced capacity Storage Pool or an Advanced performance Storage Pool to a Standard performance Storage Pool.
  * Pools are zonal resources.
  * You can create up to 10,000 disks in a Storage Pool.
  * You can use Hyperdisk Storage Pools with only Compute Engine. Cloud SQL instances can't use Hyperdisk Storage Pools.
  * You can change the provisioned capacity or performance of a Storage Pool at most two times in a 24 hour period.
  * You can create only Hyperdisk Balanced disks in a Hyperdisk Balanced pool, and you can create only Hyperdisk Throughput disks in a Hyperdisk Throughput pool.
  * You must contact your account team to change the provisioned capacity, IOPS, or throughput of an Exapool.
  * You must contact your account team to delete an Exapool.



**Limits for disks in a pool** :

  * Only new disks in the same project and zone can be created in a pool.
  * You can't move disks in or out of a pool; you have to recreate the disk from a standard snapshot. For more information, see [Change the disk type](https://docs.cloud.google.com/compute/docs/disks/migrate-to-hyperdisk).
  * To create boot disks in a pool, you must use a Hyperdisk Balanced Storage Pool or Hyperdisk Balanced Exapool.
  * Pools don't support [regional disks](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk).
  * You can't [clone](https://docs.cloud.google.com/compute/docs/disks/create-disk-from-source#clone), [create instant snapshots](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots) of, or [configure Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about) for disks in a pool.



## Reservations

You can reserve Storage Pools capacity together with compute instances by using future reservations for capacity blocks. You can also attach disks from a Storage Pool to compute instances that consume a reservation.

For more information, see [Reservations for pools](https://docs.cloud.google.com/compute/docs/disks/pools#reservations).

## Pricing

Hyperdisk Storage Pools are billed monthly for the provisioned Storage Pool capacity, throughput and IOPS. You are not billed for the provisioned IOPS, throughput, or capacity for the disks created in the Storage Pool.

With a Standard capacity and Standard performance Storage Pools, capacity and provisioned performance is priced at the same rate as the underlying disk. For example, the price for Standard capacity for a Hyperdisk Balanced Storage Pool is the same price as standalone Hyperdisk Balanced disk capacity.

Advanced capacity and Advanced performance Storage Pools are priced higher because of thin-provisioning and data reduction. Even with this premium, the savings from thin-provisioning and data reduction can still reduce your total block storage costs through increased efficiency and utilization.

For more pricing information, see [Disk pricing](https://docs.cloud.google.com/compute/disks-image-pricing#section-2).

### Committed use discounts with Hyperdisk Storage Pools

Hyperdisk Storage Pools are not eligible for:

  * Resource-based committed use discounts (CUDs)
  * Sustained use discounts (SUDs)



## What's next?

  * Learn how to [create a Hyperdisk Storage Pool](https://docs.cloud.google.com/compute/docs/disks/create-storage-pools).
  * Learn how to move existing disks to a Storage Pool, as described in [Change the disk type](https://docs.cloud.google.com/compute/docs/disks/migrate-to-hyperdisk).
  * Review [Disk pricing](https://docs.cloud.google.com/compute/disks-image-pricing#disk) information.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
