---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/plan-flexcache-volumes/
title: Plan the FlexCache volumes \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:30.492467+00:00
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

This page provides details about how to plan your FlexCache volumes.

When planning your FlexCache volume, consider the following guidelines for capacity, performance, and network impact:

**Cache volume capacity**

For maximum performance, we recommend a FlexCache volume size that is between 15% and 50% of the origin volume's size. Performance might degrade if the cache-to-origin size ratio exceeds 50%.

**Cache volume performance**

For FlexCache volume in Premium and Extreme service level storage pools, its performance is determined by its size and service level.

The maximum throughput calculation by service level:

  * **Premium service level** : Volume capacity (GiB) x 64 KiBps

  * **Extreme service level** : Volume capacity (GiB) x 128 KiBps




If the FlexCache volume receives too little performance due to its size, you can use the [Manual QoS](https://docs.cloud.google.com/netapp/volumes/docs/performance/optimize-performance#manual_qos) feature to reassign performance from other volumes in the same pool to the FlexCache volume.

For example, to achieve a throughput of 500 MiBps, you need to provision either 7.8 TiB of Premium volume or 3.9 TiB of Extreme volume.

For FlexCache volumes in Flex Unified pools, the volumes share the pool's performance with all other volumes in the pool. You can assign more throughput and IOPS to the pool as needed.

**Network performance**

The network performance is determined by the following factors:

  * **Cache read hits** : these are served quickly with low latency directly from the cache volume.

  * **Cache misses** : the data must be retrieved from the origin. Their performance depends on the throughput and latency of the network between the cache and origin volumes. Consider [prefetching data](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/overview#cache_prepopulation) to improve performance for resource-intensive compute jobs.

  * **Writes** : all write operations are directed to the origin. Their throughput and latency depend on the network connection between the cache and origin.




## What's next

[Create a FlexCache volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/create-flexcache-volume).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
