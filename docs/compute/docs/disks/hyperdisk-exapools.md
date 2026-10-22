---
url: https://docs.cloud.google.com/compute/docs/disks/hyperdisk-exapools/
title: Hyperdisk Exapools overview \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:12:47.005751+00:00
---

# Hyperdisk Exapools overview  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/hyperdisk-exapools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Hyperdisk Exapools overview Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the features and limits of Exapools. Hyperdisk Exapools are [Hyperdisk pools](https://docs.cloud.google.com/compute/docs/disks/pools) that are designed for workloads where Hyperdisk Storage Pools don't provide sufficient Hyperdisk storage in a single zone. With Exapools, you purchase storage and performance in bulk, then create disks in the pool to consume the storage.

**Note:** Hyperdisk Exapools are generally available with an allowlist. To get access to this feature, [contact your account team](https://docs.cloud.google.com/tam).

## When to use Hyperdisk Exapools

Exapools are for large scale workloads with tens of thousands of disks in a single zone that require between 500 TiB and 2.5 EiB of durable block storage. If your workload requires a lower scale of capacity or performance, use a [Hyperdisk Storage Pool](https://docs.cloud.google.com/compute/docs/disks/storage-pools) or create disks outside of a pool.

Exapools offer storage and performance at the largest scale available in Compute Engine, while also offering cost savings by letting you provision more performance and capacity than you need, but only charging you for what you use.

Hyperdisk Exapools are ideal for large scale AI, machine learning (ML), and large distributed parallel file system workloads. The following are some example workloads:

Example workloads for **Hyperdisk Exapools** :

  * AI/ML workloads spanning 4,000 TPU VMs and using 2 PiB of Hyperdisk Balanced with provisioned performance of 20,000,000 IOPS and 3 TiB/s throughput, driving concurrent aggregate peak throughput of 500 GiB/s.
  * AI/ML training workloads with 15,000 GPU instances using Hyperdisk Balanced for boot and scratch disks with a total capacity of 8 PiB, driving a concurrent aggregate peak throughput of 1 TiB/s.
  * Parallel file system with 6 PiB or more of capacity and concurrent aggregate peaks of 800 GiB/s of read heavy throughput.



## How Exapools work

You create an Exapool with the aggregate capacity and performance that all of your workload's disks within a zone will need, then you create disks in the pool as needed. You can use disks in an Exapool as boot disks or data disks for your Compute Engine instances and containers.

When you create a disk in an Exapool, you allocate some of the pool's resources (size and performance) to the disk. When you delete a disk in a pool, the resources allocated to the disk are returned to the pool for use by other disks.

For example, suppose you create a Hyperdisk Balanced Exapool with 50 PiB of capacity. If you create 100 10 TiB disks in the pool, the remaining available capacity of the pool decreases by 1,000 TiB.

## Exapool types

When you create an Exapool, you must choose a Hyperdisk type for the disks that will be in the pool. The following types are available:

  * Hyperdisk Balanced Exapools: all the disks in the Exapool are [Hyperdisk Balanced volumes](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced).
  * Hyperdisk Throughput Exapool: all the disks in the Exapool are [Hyperdisk Throughput volumes](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput).



For more information about choosing a Hyperdisk type, see [Choose a Hyperdisk type for your workload](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#when-to-use).

### Machine series support

Hyperdisk Throughput Exapools and Hyperdisk Balanced Exapools are supported with the same machine series that support Hyperdisk Throughput and Hyperdisk Balanced, respectively. For a list of the supported machine series, see [Machine series support for Hyperdisk Throughput](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput#machine-series) and [Machine series support for Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#machine-series).

## Performance and capacity provisioning for Exapools

The provisioning type of a pool determines how disks in the pool consume resources.

Exapools use advanced provisioning for both capacity and performance, which offers the most cost and time savings.

**Note:** Exapools are logical administrative and billing boundaries; they don't reserve or dedicate isolated physical hardware in the zone. Regardless of the provisioning type you choose, you can't create or resize disks within a Exapool unless the zone has sufficient physical capacity. If the zone doesn't have enough physical capacity for the required disk type, then creating or resizing a disk in the Exapool might fail with a `ZONE_RESOURCE_POOL_EXHAUSTED` error even if you haven't exceeded the Exapool's provisioned capacity.

### Advanced capacity provisioning

All Exapools use advanced capacity provisioning, which offers the following benefits:

  * Thin provisioning: Compute Engine allocates data to disks in the pool as needed, not when the disk is provisioned.
  * Overprovisioning: You can provision the disks in the pool with up to 50x more capacity than you purchased for the Exapool. This simplifies capacity planning and avoids downtime for manual disk resizing.

**Note:** Exapools don't offer autogrow for capacity or performance, and doesn't offer data compression.

For a detailed explanation of advanced capacity provisioning, see [Advanced capacity provisioning](https://docs.cloud.google.com/compute/docs/disks/pools#adv-cap).

### Advanced performance provisioning

Exapools use advanced performance provisioning, which offers the following benefits:

  * Thin provisioning: Compute Engine allocates performance resources to the disks in the pool as needed. Only the amount of IOPS and throughput used by a disk in an Exapool consumes performance.
  * Overprovisioning: the total performance for all the disks in a pool can be up to 50 times the pool's provisioned write performance.
  * Shared performance: Disks in an Exapool share the pool's provisioned performance up to each disk's limit, saving costs for disks with different peak usage times.



For a detailed explanation of advanced performance provisioning, see [Advanced performance provisioning](https://docs.cloud.google.com/compute/docs/disks/pools#adv-perf).

## Purchase capacity and performance

An Exapool's provisioned performance, or how much IOPS and throughput you can allocate to disks within the pool, depends on the following factors:

  * The number of capacity units in the pool
  * The disk type of the Exapool



### How capacity units work

A capacity unit includes 1 GiB of capacity and a fixed amount of performance (IOPS and throughput) per GiB. For example, to add 1 PiB of capacity to a pool, you purchase 1,048,576 capacity units (1,048,576 GiB = 1 PiB). Exapools offer three capacity unit types to choose from. The amount of performance added to the pool depends on the type of capacity units:

  * Capacity-optimized units: offer a balanced rate of IOPS and throughput for both reads and writes.
  * Read-optimized units: offer the highest rate of read operations and throughput per GiB.
  * Write-optimized units: offer the highest rate of write operations and throughput per GiB.



If your workload has more read operations than writes, or if it requires more read throughput than write throughput, you'll achieve the best value by purchasing read-optimized units.

You can combine different types of capacity units when you provision or expand an Exapool. The type and number of capacity units you purchase for a pool is referred to as the _blend of capacity units_.

An Exapool's blend of units doesn't affect the performance of the disks in the Exapool. The blend of units affects only the following factors:

  * How you're billed for the Exapool.
  * The maximum provisioned performance for the Exapool.



### Choose a blend of capacity units for an Exapool

To meet your workload's needs most cost-effectively, work with your [account team](https://docs.cloud.google.com/tam) to choose a blend of capacity units that best fits your workload. For example, you can create an Exapool with a high number of read-optimized units for all the read-intensive disks in a project.

### Capacity unit ratios for Hyperdisk Throughput Exapools

Hyperdisk Throughput Exapools have the following performance ratios based on the amount of capacity purchased:

Capacity unit type | Capacity units purchased | Exapool capacity (TiB) | Read throughput (MiB/s) | Write throughput (MiB/s)   
---|---|---|---|---  
Capacity-optimized | 1,024 | 1 | 0.97 | 0.10  
Read-optimized | 1,024 | 1 | 3.38 | 0.10  
Write-optimized | 1,024 | 1 | 0.97 | 1.84  
  
### Capacity unit ratios for Hyperdisk Balanced Exapool

Hyperdisk Balanced Exapools have the following performance ratios based on the amount of capacity purchased:

Capacity unit type | Capacity units purchased | Exapool Capacity (TiB) | Read throughput (MiB/s) | Write throughput (MiB/s) | Read IOPS | Write IOPS  
---|---|---|---|---|---|---  
Capacity-optimized | 1,024 | 1 | 5.12 | 1.02 | 275 | 102  
Read-optimized | 1,024 | 1 | 378.88 | 30.72 | 21,311 | 3,072  
Write-optimized | 1,024 | 1 | 220.16 | 71.68 | 12,288 | 6,656  
  
### How capacity units affect disk performance

An Exapool's blend of capacity units doesn't affect how disks in the Exapool consume performance. You aren't billed differently for the individual read and write operations of the disks in the pool. Purchasing units of a specific type doesn't restrict the disks to a fixed amount of read or write IOPS. Also, when you create a disk in an Exapool, you don't specify a read IOPS or write IOPS limit, you only specify a provisioned IOPS limit.

For example, consider two Hyperdisk Balanced Exapools, `Pool-1` and `Pool-2.` Both have 100,000,000 capacity-optimized units. `Pool-1` also has 5,000,000 write-optimized units, while `Pool-2` has 5,000,000 read-optimized units.

Since both pools have a total of 105,000,000 units, they'll have the same total capacity of 100.1 PiB (105,000,000 GiB). However, because they have different types of capacity units, the pools have different maximum performance limits and costs. There's no performance difference between disks in both pools.

### Example

Suppose a Hyperdisk Balanced Exapool has 12,400,000 capacity units, consisting of:

  * 5,000,000 capacity-optimized units
  * 2,400,000 read-optimized units
  * 5,000,000 write-optimized units



The Exapool has 12,109.4 TiB of capacity (1 TiB for every 1,024 units).

The Exapool has 151,488,476 IOPS, calculated as follows:

  * IOPS from 5,000,000 capacity-optimized units: 1,840,820 (1,342,773 read IOPS + 498,047 write IOPS)

  * IOPS from 2,400,000 read-optimized units: 57,147,656 (49,947,656 read IOPS + 7,200,000 write IOPS)

  * IOPS from 5,000,000 write-optimized units: 92,500,000 (60,000,000 read IOPS + 32,500,000 write IOPS)




## Review performance and capacity utilization

Compute Engine offers metrics that you can use to monitor your Exapools. These metrics answer questions like:

  * How much read and write IOPS is left in the Exapool?
  * How much capacity has been allocated to disks in the Exapool?
  * How many disks are in the Exapool?



You can view these metrics in Cloud Monitoring. To learn more, see [Monitor Hyperdisk pools](https://docs.cloud.google.com/compute/docs/disks/monitor-pool-performance).

## Size and performance limits for Hyperdisk Exapools

This section lists the limits for each Exapool type.

Property | Hyperdisk Balanced Exapools | Hyperdisk Throughput Exapools  
---|---|---  
Minimum capacity | 500 TiB | 500 PiB  
Maximum capacity | 1 EiB | 5 EiB  
Maximum throughput | 10 TiB/s | 10 TiB/s  
Maximum number of disks per pool | 500,000 | 500,000  
Capacity increments | 1 TiB | 1 PiB  
Maximum Exapools per project per zone | 1 | 1  
Performance ratios | 32KB I/O size for read and write throughput; 4KB I/O size for read and write IOPS | 1MB I/O size for reads, 256K I/O size for writes  
  
### Size and performance limits for disks within an Exapool

Disks in an Exapool have the same size and performance limits as disks that aren't in a pool, as follows:

Hyperdisk type | Max provisionable performance per disk | Customizable throughput | Customizable IOPS  
---|---|---|---  
Hyperdisk Balanced | 160,000 IOPS;  
2,400 MiB/s throughput | Yes | Yes  
Hyperdisk Throughput | 2,400 MiB/s throughput | Yes | No; 4 IOPS per MiB/s of throughput, up to 9,600 IOPS  
  
You can specify a performance limit for the disk at creation time and modify the performance limit while the disk is in use.

For details of the size and performance limits, see [Size and performance limits for Hyperdisk Throughput](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput#size_limits) and [Size and performance limits for Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#size_limits).

## Regional availability

Hyperdisk Balanced Exapools and Hyperdisk Throughput Exapools are available in all zones.

## Encryption

Encrypting disks in a Hyperdisk pool works the same way as encrypting disks outside of a pool.

For more information, see [About disk encryption](https://docs.cloud.google.com/compute/docs/disks/disk-encryption).

## Reservations

You can reserve Exapools capacity together with compute instances by using future reservations for capacity blocks. You can also attach disks from an Exapool to compute instances that consume a reservation.

For more information, see [Reservations for pools](https://docs.cloud.google.com/compute/docs/disks/pools#reservations).

## Pricing

You're billed for Exapools based on the number and type of capacity and performance units you purchased for the pool. You aren't billed for the provisioned IOPS, throughput, or capacity for the disks created in the pool.

Compute Engine offers resource-based committed use discounts (CUDs) for your Hyperdisk Exapools. You can receive these discounts by purchasing 1-year or 3-year block storage commitments. To learn more about how block storage commitments work, see [Block storage commitments](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#block_storage_commitments) in the resource-based CUDs documentation. For instructions on how to purchase a block storage commitment, see [Purchase block storage commitments](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-block-storage-commitments).

To compare on-demand prices with 1-year and 3-year CUD prices, see [Disk pricing](https://docs.cloud.google.com/compute/disks-image-pricing?e=48754805#section-2).

## Limitations

The following limitations apply to Exapools.

  * You must [contact your account team](https://docs.cloud.google.com/tam) to create, modify, or delete a Hyperdisk Exapool.
  * The amount of performance you can provision for an Exapool depends on the type and number of capacity units for the Exapool. However, performance for disks created in an Exapool is independent of the pool's blend of capacity units. 
  * You can't use Confidential mode for Hyperdisk Balanced volumes in an Exapool.
  * Exapools only use advanced capacity and advanced performance provisioning. They don't support standard capacity or standard performance provisioning.
  * Exapools don't use data compression.
  * Exapools don't support autogrow for performance or capacity. You must monitor your Exapool's utilization of performance and capacity yourself. To increase the pool's performance or capacity, you must [contact your account team](https://docs.cloud.google.com/tam). 
  * Only new disks in the same project and zone can be created in a pool.
  * You can't move disks in or out of a pool; you have to recreate the disk from a standard snapshot. For more information, see [Change the disk type](https://docs.cloud.google.com/compute/docs/disks/migrate-to-hyperdisk).
  * To create boot disks in a pool, you must use a Hyperdisk Balanced Storage Pool or Hyperdisk Balanced Exapool.
  * Pools don't support [regional disks](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk).
  * You can't [clone](https://docs.cloud.google.com/compute/docs/disks/create-disk-from-source#clone), [create instant snapshots](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots) of, or [configure Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about) for disks in a pool.



## What's next

  * [Contact your account team](https://docs.cloud.google.com/tam) to create an Exapool
  * [View the properties of a Hyperdisk pool](https://docs.cloud.google.com/compute/docs/disks/manage-storage-pools)
  * [Add disks in a pool to VMs](https://docs.cloud.google.com/compute/docs/disks/use-storage-pool-capacity)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
