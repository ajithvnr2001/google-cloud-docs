---
url: https://docs.cloud.google.com/memorystore/docs/redis/redis-tiers/
title: Redis tier capabilities \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:45.968655+00:00
---

# Redis tier capabilities  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/redis-tiers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Redis tier capabilities Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the differences between the available Redis tiers.

Memorystore for Redis supports Basic and Standard Tiers. The Basic Tier is best suited for applications that use Redis as a cache and can withstand a cold restart and full cache flush. Standard Tier instances provide [High Availability](https://docs.cloud.google.com/memorystore/docs/redis/high-availability) using replication, read replicas, and automatic failover.

To help protect your data and provide a baseline level of persistence, RDB snapshots are enabled by default when you create a Memorystore for Redis instance using the Google Cloud console.

It is not possible to upgrade from Basic Tier to Standard Tier or the other way around. If you want to move data from an existing Basic Tier instance to a new Standard Tier instance, use [import and export](https://docs.cloud.google.com/memorystore/docs/redis/import-export-overview) to move your data.

## Tier architecture

The following diagrams show the architectures for the Memorystore for Redis service tiers.

### Basic Tier

![](https://docs.cloud.google.com/static/memorystore/img/basic-tier.png)

  * One Redis node
  * Ephemeral cache



### Standard Tier

![](https://docs.cloud.google.com/static/memorystore/img/standard-tier.png)

  * Provides [High Availability](https://docs.cloud.google.com/memorystore/docs/redis/high-availability) with replication
  * Fails over to replica in the case of primary node failure



### Standard Tier with read replicas

![](https://docs.cloud.google.com/static/memorystore/img/standard-tier-read-replicas.png)

  * Provides [High Availability](https://docs.cloud.google.com/memorystore/docs/redis/high-availability) with replication
  * Read replicas allow for distributed reads



## Feature comparison

Specifications | Basic Tier | Standard Tier (read replicas disabled) | Standard Tier (read replicas enabled)  
---|---|---|---  
**Description** | Provides a cache with no replication | Provides redundancy and availability using replication | Provides redundancy and availability using replication to backup data, and multiple Read replicas to increase read throughput  
**Max Redis primary size** | 300 GB | 300 GB | 300 GB  
**Max network bandwidth** | 16 Gbps | 16 Gbps | 16 Gbps total for writes. 16 Gbps per node for reads.1  
**I/O threads** | Yes2 | Yes2 | Yes2  
**Scale primary size** | Yes | Yes | Yes  
**Scale number of read replicas** | No | No | Yes  
**Cross-zone replication** | No | Yes3 | Yes3  
**Automatic failover** | No | Yes | Yes  
**Read replicas** | No | No | Yes  
**In-transit encryption** | Yes | Yes | Yes  
**Maintenance window** | Yes | Yes | Yes  
**Cloud Monitoring** | Yes | Yes | Yes  
  
1The maximum write throughput is 16 Gbps. Read throughput is dependent on the number of nodes (read replicas) in the instance, including the primary node. For example, if you have an instance with 1 primary node and 2 read replicas, the total read throughput is 48 Gbps.

2I/O threads are only available on M3 instances or higher running Redis version 6.x. For more information, see [Redis version 6.x](https://docs.cloud.google.com/memorystore/docs/redis/supported-versions#redis_version_6x).

3 For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
