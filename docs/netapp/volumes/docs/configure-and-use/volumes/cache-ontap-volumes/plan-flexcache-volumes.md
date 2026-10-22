---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/plan-flexcache-volumes/
title: Plan the FlexCache volumes \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:18:20.134406+00:00
---

# Plan the FlexCache volumes  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/plan-flexcache-volumes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Plan the FlexCache volumes Stay organized with collections  Save and categorize content based on your preferences. 

Planning your FlexCache volumes lets you optimize read latency and throughput for your workloads. Before you create a volume, review the guidelines for cache capacity, volume performance, and network performance.

  * **Cache volume capacity**

To maintain optimal performance when sizing your FlexCache volume, consider the following recommendations:

    * **Recommended cache volume size** : Size the cache volume between 10% and 15% of the origin volume's size. A cache-to-origin size ratio greater than 15% isn't required for performance and might degrade performance if it exceeds 30%.

    * **Initial provisioning** : Provision the cache at the target size when you create it to ensure optimal performance.

**Caution:** Don't start with a smaller cache and increase its size later, because doing so might degrade performance.
  * **Cache volume performance**

For a FlexCache volume in a Premium or Extreme service level storage pool, the volume's size and service level determine its performance.

Use the following formulas to calculate the maximum throughput for a FlexCache volume based on its service level:

    * **Premium service level** : Provisioned volume capacity (GiB) × 64 KiBps

    * **Extreme service level** : Provisioned volume capacity (GiB) × 128 KiBps

If the FlexCache volume's size provides insufficient throughput, you can use the [Manual QoS](https://docs.cloud.google.com/netapp/volumes/docs/performance/optimize-performance#manual_qos) feature to allocate throughput from other volumes in the same pool to the FlexCache volume.

For example, to achieve a throughput of 500 MiBps, provision either a 7.8 TiB Premium volume or a 3.9 TiB Extreme volume.

For FlexCache volumes in Flex Unified pools, the volumes share the pool's performance with all other volumes in the pool. You can assign more throughput and IOPS to the pool as needed.

  * **Network performance**

The following factors determine the network performance for FlexCache volumes:

    * **Cache read hits** : The cache volume serves these requests locally with low latency.

    * **Cache misses** : The cache volume must retrieve the data from the origin volume. The performance for cache misses depends on the throughput and latency of the network between the cache and origin volumes. Consider [prefetching data](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/overview#cache_prepopulation) to improve performance for resource-intensive compute jobs.

    * **Writes** : The cache volume directs all write operations to the origin volume. Write throughput and latency depend on the network connection between the cache and origin volumes.




## What's next

[Create a FlexCache volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/create-flexcache-volume).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
