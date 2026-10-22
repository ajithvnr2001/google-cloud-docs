---
url: https://docs.cloud.google.com/memorystore/docs/memcached/memory-management-best-practices/
title: Memory management best practices \u00a0|\u00a0 Memorystore for Memcached \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:34.886388+00:00
---

# Memory management best practices  |  Memorystore for Memcached  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/memory-management-best-practices/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview)



Send feedback 

#  Memory management best practices Stay organized with collections  Save and categorize content based on your preferences. 

This page explains the [Reserved Memory](https://docs.cloud.google.com/memorystore/docs/memcached/memory-management-best-practices#reserved_memory) configuration for your Memcached instance, and when to [Increase Reserved Memory](https://docs.cloud.google.com/memorystore/docs/memcached/memory-management-best-practices#increase_reserved_memory) if needed. This page also explains the other best practices you need to know in order to effectively manage memory for your Memcached instance.

Memorystore adds extra memory to your instance, which is not visible to you, in order to accommodate overhead created by Memcached processes. However, depending on your specific workload, memory overhead can grow larger than the extra memory we provision for this purpose.

When memory usage grows larger than your total Memorystore system memory, an out of memory (OOM) condition can cause a full cache flush of data, which can disrupt your application and business.

The following sections outline general principles to follow when configuring a Memorystore for Memcached instance. The sections also cover the metrics and alerts you can use to monitor memory, and also explain actions you can take.

## Memory management concepts

#### Instance capacity

The instance capacity is the amount of memory you provision in GiB, and what you are billed for. Cache memory is not the same as instance capacity because cache memory isn't fixed. However, when you create your Memcached instance, instance capacity is equal to the cache memory by default.

For example, if you choose an instance capacity of 5 GiB, by default your instance has 5 GiB of space in which to store items.

#### Cache memory limit

Cache memory is the total size of memory available to be used as a cache by your Memcached instance. By default cache memory is equal to your instance capacity. However, adjusting Reserved Memory can reduce cache memory. For more details, see [Reserved Memory](https://docs.cloud.google.com/memorystore/docs/memcached/memory-management-best-practices#reserved_memory). Once cache memory is full, Memcached begins to evict items stored within the cache to make room for new writes.

Be aware that when viewing the [cache memory metric](https://docs.cloud.google.com/memorystore/docs/memcached/memory-management-best-practices#monitoring_your_instances_memory_usage), the reported cache memory for a Memcached node only includes space occupied by items. This means that Memcached may underestimate the total cache memory usage. Additional memory may be allocated by the cache as fragmentation within the slabs.

#### Memory overhead

Memory overhead is memory used by Memcached processes. It does not include items stored in memory for caching.

Memory overhead scales based on number of active connections, total items, and item size. Also, memory overhead is theoretically unbounded, so it has the potential to grow infinitely.

To account for memory overhead, Memorystore adds extra memory to your instance. However, the amount of extra memory we add is not visible to you. For the majority of workloads, memory overhead should not be problematic.

Without any configuration, an empty Memorystore for Memcached node's memory looks like the diagram seen below.

![placeholder](https://docs.cloud.google.com/static/memorystore/img/reserved_memory_1.png)

As your application adds items to the cache, Memcached accumulates overhead for processes like connection buffers and the internal hash table:

![placeholder](https://docs.cloud.google.com/static/memorystore/img/reserved_memory_2.png)

Since overhead growth is unbounded, some overhead for some workloads grows beyond the reserved limit, as seen below:

![placeholder](https://docs.cloud.google.com/static/memorystore/img/reserved_memory_3.png)

When overhead and items fill all available space, Memcached runs out of memory and the process must be terminated by the OS causing a full cache flush:

![placeholder](https://docs.cloud.google.com/static/memorystore/img/reserved_memory_4.png)

You may observe that memory overhead grows beyond the extra space Memorystore allocates for overhead by default (as indicated by high [System Memory Utilization](https://docs.cloud.google.com/memorystore/docs/memcached/memory-management-best-practices#system_memory_utilization)). In this circumstance, [increase the Reserved Memory](https://docs.cloud.google.com/memorystore/docs/memcached/memory-management-best-practices#increase_reserved_memory) parameter to create extra the overhead for your workload.

#### Reserved Memory

Reserved Memory is a [Memorystore configuration](https://docs.cloud.google.com/memorystore/docs/memcached/configuring-memcached) that allows you to increase the amount of space available to be used by memory overhead.

To raise the memory available to memory overhead, you increase Reserved Memory, which reduces available cache memory. You should add this extra space if your instance experiences memory pressure caused by high memory overhead.

Instances created after October 25, 2021 have a default Reserved Memory percentage of 10%. This value can be overridden by manually [updating the configuration](https://docs.cloud.google.com/memorystore/docs/memcached/configuring-memcached) on your instance. Decreasing the Reserved Memory on your instance can significantly increase the likelihood of OOM conditions.

The diagram below shows an instance that has created extra space for memory overhead by increasing Reserved Memory:

![placeholder](https://docs.cloud.google.com/static/memorystore/img/reserved_memory_5.png)

Once the Memcached cache reaches this reduced limit, it begins to evict items.

![placeholder](https://docs.cloud.google.com/static/memorystore/img/reserved_memory_6.png)

Once you start using the instance, depending on the [System Memory Utilization](https://docs.cloud.google.com/memorystore/docs/memcached/memory-management-best-practices#system_memory_utilization) metric, you may be required to increase the Reserved Memory on your instance to support your peak workload.

For more details, see [Managing system memory usage](https://docs.cloud.google.com/memorystore/docs/memcached/memory-management-best-practices#managing_system_memory_usage).

#### System Memory Utilization

System memory is equal to your provisioned instance capacity plus the additional space Memorystore adds for memory overhead.

[System Memory Utilization is a metric](https://docs.cloud.google.com/memorystore/docs/memcached/memory-management-best-practices#monitoring_your_instances_memory_usage) that shows you the percentage of all used memory (items stored plus memory overhead) as compared to system memory. It is a critical metric to monitor, because it shows you how close you are to completely filling up the available system memory for your instance. As the System Memory Utilization metric approaches 100%, the instance is more likely to experience an OOM condition. To ensure the instance has sufficient memory to support your workload, it is important to always have enough system memory available.

For workloads attempting to fill the cache to entirety and rely on Memcached evictions to manage which items are stored, you should expect to see higher System Memory Utilization, and you may want to preemptively [increase the Reserved Memory](https://docs.cloud.google.com/memorystore/docs/memcached/memory-management-best-practices#increase_reserved_memory) to guarantee that you have enough room for overhead.

##### Alerts for System Memory Utilization

You should [set an alert](https://docs.cloud.google.com/memorystore/docs/memcached/monitoring-instances#create-stackdriver-alert) to notify you if the System Memory Utilization metric exceeds 90%. If System Memory Utilization is high, you should proceed to monitor the System Memory Utilization metric more closely, and if it grows dramatically, you should consider taking steps to [manage system memory usage](https://docs.cloud.google.com/memorystore/docs/memcached/memory-management-best-practices#managing_system_memory_usage). Taking action when System Memory Utilization reaches high levels is important because it gives you time to mitigate instead of dealing with a cache flush caused by an OOM condition.

#### Eviction policy

Memcached uses an [optimized LRU algorithm](https://memcached.org/blog/modern-lru/) to evict items once they have filled the cache memory. For instructions on disabling cache evictions, see [Configuring Memcached instances](https://docs.cloud.google.com/memorystore/docs/memcached/configuring-memcached).

[Monitoring evictions](https://docs.cloud.google.com/memorystore/docs/memcached/memory-management-best-practices#monitoring_your_instances_memory_usage) shows you the number of keys Memcached removes due to size limitations. Items that are removed due to TTL expiry are not included in this metric. If you are seeing a large number of evictions, scaling up your instance may result in an increase to your cache hit ratio.

If evictions are not enabled, and your cache is completely full, setting items in your Memcached server may fail.

#### Cache-hit ratio

You should regularly monitor the [cache-hit ratio metric](https://docs.cloud.google.com/memorystore/docs/memcached/memory-management-best-practices#monitoring_your_instances_memory_usage) so that you know what percentage of key lookups are successfully returned by keys in your Memcached instance. Generally speaking, a higher cache-hit ratio is better than a lower cache-hit ratio because it means your cache is returning more cache requests.

You should make a note of your cache-hit ratio before you make any large configuration changes such as adjusting the Reserved Memory, adjusting key TTLs, or scaling your instance. Then, after you modify your instance, check the cache-hit ratio again to see how your change impacted this metric.

## Monitoring your instance's memory usage

The following metrics give you insight into your instance's memory usage. To learn how to view metrics and set alerts, see [Monitoring Memcached instances](https://docs.cloud.google.com/memorystore/docs/memcached/monitoring-instances).

#### Memory management related metrics

Metric | Full metric address  
---|---  
[Cache Memory](https://docs.cloud.google.com/memorystore/docs/memcached/memory-management-best-practices#cache_memory_limit) |  memcache.googleapis.com/node/cache_memory   
[System Memory Utilization](https://docs.cloud.google.com/memorystore/docs/memcached/memory-management-best-practices#system_memory_utilization) |  memcache.googleapis.com/node/memory/utilization   
[Cache-hit Ratio](https://docs.cloud.google.com/memorystore/docs/memcached/memory-management-best-practices#cache-hit_ratio) |  memcache.googleapis.com/node/hit_ratio   
[Evictions](https://docs.cloud.google.com/memorystore/docs/memcached/memory-management-best-practices#eviction_policy) |  memcache.googleapis.com/node/eviction_count   
  
## Managing system memory usage

If your instance is experiencing memory pressure or running into OOM errors, follow the steps below to resolve the issue:

  1. [Verify an OOM condition](https://docs.cloud.google.com/memorystore/docs/memcached/memory-management-best-practices#verifying_an_oom_condition).
  2. [Increase the Reserved Memory on your instance](https://docs.cloud.google.com/memorystore/docs/memcached/memory-management-best-practices#increase_reserved_memory).
  3. [Scale up the instance](https://docs.cloud.google.com/memorystore/docs/memcached/memory-management-best-practices#scale_up_the_instance).
  4. [Set TTLs on volatile keys](https://docs.cloud.google.com/memorystore/docs/memcached/memory-management-best-practices#set_ttls_on_volatile_keys).
  5. [Manually delete keys on your instance](https://docs.cloud.google.com/memorystore/docs/memcached/memory-management-best-practices#manually_delete_keys_on_your_instance).
  6. If you are still encountering OOM conditions, then [contact Google Cloud Platform Support](https://docs.cloud.google.com/support).



#### Verifying an OOM condition

When your instance reaches an OOM condition, the first signal is an instance restart. To see if a restart is caused by an OOM condition, view the _Uptime_ and _System Memory Utilization_ [metrics](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-metrics).

If System Memory Utilization was over 90% prior to Uptime dropping to zero, this means that the instance restart was likely caused by an OOM condition.

#### Increase Reserved Memory

Increasing Reserved Memory creates more space for memory overhead. It does this by reducing the Cache Memory limit of your instance. You should increase Reserved Memory if the System Memory Utilization metric exceeds 90%.

For instructions on adjusting the Reserved Memory configuration, see [Configuring Memcached instances](https://docs.cloud.google.com/memorystore/docs/memcached/configuring-memcached)

Increasing Reserved Memory reduces the memory available to store items, resulting in item eviction happening sooner. This can lower your instance's cache hit ratio. Items are not evicted if you have evictions disabled.

#### Scale up the instance

Follow the instructions at [Scaling Memcached instances](https://docs.cloud.google.com/memorystore/docs/memcached/scaling-instances) to increase your node count. If your application is configured to shard the keys across the nodes, this increases the overall item storage space available to your application and reduces the number of keys stored on each individual node.

#### Set TTLs on volatile keys

Configure your application to set TTLs on stored keys in Memcached. By default, Memcached periodically checks for expired keys and removes them, freeing space on your server and preventing further cache memory allocation.

#### Manually delete keys on your instance

You should consider deleting keys when faced with memory pressure. However, since open source Memcached does not free previously allocated memory, deleting keys merely reduces the chance of entering an OOM condition. It reduces the chance because new writes use the empty memory. Growing memory overhead can still cause an OOM condition because previously allocated memory is dedicated to storing items, and not usable by overhead.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
