---
url: https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/volume-performance-sizing/
title: Volume performance sizing \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:13:34.501893+00:00
---

# Volume performance sizing  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/volume-performance-sizing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Volume performance sizing Stay organized with collections  Save and categorize content based on your preferences. 

This page describes volume performance sizing.

## Importance of performance sizing

To correctly size your workloads for performance, you need to understand:

  * How much performance a single volume can deliver.

  * How to adjust a volume's performance.

  * How performance depends mainly on the service level of the underlying storage pool.




### Flex Unified and Flex File custom performance

Consider the following for Flex Unified and Flex File custom performance:

  * **Performance is shared** : the underlying storage pool provides the performance. All volumes in a Flex Unified or Flex File custom pool share the pool's total performance. Smaller volumes can use unused performance from larger ones. This applies to both default and ONTAP-mode.

  * **Configurable performance** : you can set the pool's performance independently of its capacity.

    * **Default** : 64 MiBps throughput and 1,024 IOPS per pool.

    * **Throughput scalability** : increase throughput up to 5 GiBps in 1 MiBps increments. Each extra MiBps adds 16 IOPS.

    * **IOPS** : provision up to 160,000 IOPS per pool.

  * **Large capacity pools** : the throughput can reach up to 22 GiBps.

  * **Limits** : the effective performance of the pool is capped by whichever limit, either throughput or IOPS, is reached first, depending on your application's block size.


**Note:** These throughput and IOPS limits assume large sequential reads. Small input/output (I/O) operations or writes reach lower limits. For more information, see [Performance benchmarks](https://docs.cloud.google.com/netapp/volumes/docs/performance/performance-benchmarks).**Note:** In regions with limited performance, you can provision throughput from 64 MiBps up to a maximum of 1.6 GiBps in 1 MiBps increments. Each MiBps of provisioned throughput includes 16 IOPS. You can provision additional IOPS beyond the included throughput of 16 IOPS as required up to a maximum of 90,000 IOPS. For more information about limited performance regions, see [Supported regions for Flex Unified limited performance](https://docs.cloud.google.com/netapp/volumes/docs/discover/service-levels#supported_regions_for_flex_unified_limited_performance).

### Flex File default performance

Consider the following for Flex File default performance:

  * **Performance is shared** : the underlying storage pool provides the performance. All volumes in the pool share its performance.

  * Similar to Flex Unified and Flex File custom performance, the block size determines which limit applies first: throughput or IOPS.

    * **Throughput** : 16 KiBps per GiB of pool capacity up to a maximum of 1.6 GiBps.

    * **IOPS** : 1,024 IOPS per TiB of pool capacity up to a maximum of 60,000 IOPS.


**Note:** These throughput and IOPS limits assume large sequential reads. Small I/O operations or writes reach lower limits. For more information, see [Performance benchmarks](https://docs.cloud.google.com/netapp/volumes/docs/performance/performance-benchmarks).

### Standard, Premium, and Extreme performance

For Standard, Premium, and Extreme service level volumes, the maximum throughput a volume can sustain is determined by its capacity and the service level of the storage pool that hosts it. You can increase or decrease your volume's maximum throughput by changing its capacity, or for Premium and Extreme service levels, by re-assigning it to a storage pool with a different service level.

The following throughput and IOPS limits assume large sequential reads. Small I/Os or writes reach lower limits. For more information, see [Performance benchmarks](https://docs.cloud.google.com/netapp/volumes/docs/performance/performance-benchmarks).

  * Performance scales with volume size and service level.

    * **Standard** : 16 MiBps per TiB volume capacity up to a maximum of 1.6 GiBps.

    * **Premium** : 64 MiBps per TiB volume capacity up to a maximum of 5 GiBps per volume. 30 GiBps for large capacity volumes.

    * **Extreme** : 128 MiBps per TiB volume capacity up to a maximum of 5 GiBps per volume. 30 GiBps for large capacity volumes.

  * **Linear scaling** : the throughput increases with volume size until it reaches the service level maximum.

  * **Adjusting performance** : to improve performance, you can increase the volume capacity or move to a higher service level, such as Premium or Extreme. For more control, use [Manual QoS](https://docs.cloud.google.com/netapp/volumes/docs/performance/optimize-performance#manual_qos) to allocate pool performance to specific volumes.




## Workload considerations

The volume performance sizing section describes the maximum performance a volume can deliver. Actual application performance depends on how the application performs I/O operations to the volume.

The key factors that determine application performance include:

  * **Workload mix** : reads, writes, metadata operations; sequential versus random access.

  * **Block size** : small blocks result in higher IOPS, and large blocks result in higher throughput. Use larger block sizes (64 KiB or more) for better efficiency.

  * **Latency** : lower network latency improves performance.

  * **I/O concurrency** : more parallel I/O operations increase performance.

  * **Access protocol** : the choice of protocol NFSv3, NFSv4, SMB, or iSCSI can affect performance.

  * **Client VM cache** : increasing the VM buffer cache can reduce read operations.




The following are the key formulas:

  * _IOPS = concurrency / latency_

  * _Throughput = IOPS * block size_




The following examples show how throughput and IOPS are calculated:

**Volume throughput example**

For a volume with the Premium service level and a capacity of 1,500 GiB, the maximum large sequential read throughput achievable with a concurrency of 8 is calculated using the following formula. For Premium volumes, throughput scales linearly with the volume capacity until it reaches its limit.

_(1,500 GiB x 64 KiBps/GiB) / 1,024 KiB/MiB = 93.75 MiBps_

**Throughput and IOPS example**

Consider a scenario where a user copies a large file using a single-threaded copy (`concurrency = 1`) in Windows File Explorer. The file is being moved from a local SSD to a 4 TiB Extreme volume, which has a 512 MiBps throughput limit. Assuming the Windows File Explorer uses a 128 KiB block size and the volume has a latency of 0.5 ms, the throughput and IOPS can be calculated using the following formula:

_IOPS = 1/0.0005s = 2,000 IOPS_

_Throughput = 2,000 IOPS * 128 KiB = 256,000 KiBps = 250 MiBps_

In this example, the File Explorer isn't capable of driving the throughput to reach the volume limit (512 MiBps). Additionally, if latency is one millisecond, throughput drops by 50% because latency directly impacts single-threaded applications. To drive this volume to its maximum performance potential, use multi-threaded applications that provide higher concurrency.

### Metadata operations

Metadata operations are small, protocol-specific operations. Metadata operation performance is primarily limited by latency. Examples of metadata operations include the following:

  * List contents of a folder

  * Delete a file

  * Set permissions




### Latency

Latency is the total amount of time it takes for an I/O operation to complete. This includes the wait time in queue and the service time where the I/O is acted upon. To improve your latency when using the Standard, Premium, and Extreme service levels, we recommend that you test the connection to NetApp Volumes from all the zones in your region and select the zone with the lowest latency.

#### Considerations

  * When a client's network bandwidth is smaller than required, the client latency reported by perfmon in Windows or `nfsiostat` in Linux is higher than the latency reported by NetApp Volumes because the I/O operation spends time queueing on the client.

  * Storage latency becomes high when a volume's throughput ceiling is lower than required for a given workload. This also causes the client latency to be higher because of the additional client-side queuing.

  * When the volume's throughput ceiling is reached, you can improve the client and storage latencies by increasing the throughput limit.




## What's next

Read about [storage pools](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/storage-pools/overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
