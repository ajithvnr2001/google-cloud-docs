---
url: https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices/
title: Memory management best practices \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:37.836844+00:00
---

# Memory management best practices  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Memory management best practices Stay organized with collections  Save and categorize content based on your preferences. 

A Memorystore for Redis instance, if not correctly managed and configured, can experience memory pressure which can impact application performance. This page describes best practices that you can use to efficiently manage your instance's memory usage.

**In this topic:**

  * [Memory management concepts](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#memory_management_concepts) \- key concepts you need to know to help you keep your Memorystore instance healthy.

  * [Memory intensive operations](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#memory_intensive_operations) \- operations that can cause memory pressure.

  * [Monitor your instance's memory usage](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#monitor_your_instances_memory_usage) \- metrics that you should monitor to learn about how your instance uses memory.

  * [Resolving an out of memory condition](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#resolving_an_out_of_memory_condition) \- steps to take when resolving issues related to an out of memory condition.

  * [Right-size your Memorystore instance](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#right-size_your_cloud_memorystore_instance) \- rather than creating an over-provisioned instance, learn how to right-size your instance.




## Memory management concepts

This section introduces concepts that you need to understand in order to manage your instance's memory usage.

#### Instance capacity

  * The instance capacity is the amount of memory you provision in Gigabytes (GB), and what you are charged for. For more details on selecting the right instance capacity, see [Right-size your Memorystore instance](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#right-size_your_cloud_memorystore_instance).



#### Maxmemory configuration

  * [Maxmemory](https://redis.io/topics/lru-cache#maxmemory-configuration-directive) is a Redis configuration that allows you to set the memory limit at which your eviction policy takes effect. Memorystore for Redis designates this configuration as `maxmemory-gb`. When you create an instance, `maxmemory-gb` is set to the instance capacity. Depending on the system memory usage ratio metric, you might be required to lower the `maxmemory-gb` limit to provide memory overhead for workload spikes.

For more details, see [Manage your system memory usage ratio](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#manage_your_system_memory_usage_ratio).

To learn how to adjust `maxmemory-gb`, see [Configuring Redis instances](https://docs.cloud.google.com/memorystore/docs/redis/configuring-redis).




#### System memory usage ratio

  * The **system memory usage ratio** metric allows you to measure the memory usage of an instance relative to the system memory. System memory is managed automatically by Memorystore to handle memory usage spikes caused by [memory intensive operations](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#memory_intensive_operations) and memory fragmentation which is common in open source Redis.

If the system memory usage ratio metric exceeds 80%, this indicates that the instance is under memory pressure and you should follow the instructions at [Manage your system memory usage ratio](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#manage_your_system_memory_usage_ratio). If you do not take action and your memory usage continues to grow, you risk an instance crash due to insufficient memory. Your system memory usage ratio metric might exceed 80% due to [memory fragmentation](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#memory_fragmentation). Alternatively, if the metric spikes quickly to 80% or higher, you might have used one of the [memory intensive operations](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#memory_intensive_operations).

You should have a system memory usage ratio of 50% or less during [maintenance updates](https://docs.cloud.google.com/memorystore/docs/redis/about-maintenance). Also, sometimes [exporting](https://docs.cloud.google.com/memorystore/docs/redis/import-export-overview) requires a system memory usage ratio of 50% or less.




#### Used memory

  * The **used memory** metric shows how much data is in your Memorystore instance. The used memory of an instance can grow up to the `maxmemory-gb` configuration limit. When used memory exceeds your `maxmemory-gb` limit, your eviction policy takes effect.



#### Eviction policy

  * Your instance's eviction policy (also known as maxmemory policy) determines how Redis evicts keys when your instance data reaches the `maxmemory-gb` limit. Redis evicts keys as part of the normal cache use case. Key eviction happens as a background process, therefore keys are not evicted immediately after the `maxmemory-gb` limit is reached. A high write-rate might outpace key eviction resulting in an out of memory condition.

The default eviction policy of a Memorystore instance is [`volatile-lru`](https://redis.io/topics/lru-cache). If you are using a `volatile-*` eviction policy, make sure you are setting TTLs on keys that you want to expire, otherwise Redis has no keys to evict.

For a list of eviction policies, see [Maxmemory policies](https://docs.cloud.google.com/memorystore/docs/redis/redis-configs#maxmemory_policies).

To learn how to change your eviction policy, see [Configuring Redis instances](https://docs.cloud.google.com/memorystore/docs/redis/configuring-redis).




#### Memory fragmentation

  * [Memory fragmentation](https://redis.io/topics/memory-optimization#memory-allocation) can cause your Memorystore instance to run out of memory even when the used memory to `maxmemory-gb` ratio is low. Memory fragmentation happens when the operating system allocates [memory pages](https://en.wikipedia.org/wiki/Page_\(computer_memory\)) which Redis cannot fully utilize after repeated write and delete operations. The accumulation of such pages can result in the system running out of memory and eventually causes the Redis server to crash. The `activedefrag` Redis configuration can help to reduce fragmentation.



#### Active defragmentation

  * Redis versions 4.0 and higher provide an `activedefrag` configuration. If possible, you should create your Memorystore instance using Redis 4.0. Memorystore sets `activedefrag` to "no" by default. Setting `activedefrag` to "yes" comes with a CPU trade off, but it can help mitigate memory fragmentation, which contributes to out of memory issues.

If the system memory usage ratio metric [indicates memory fragmentation](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#memory_fragmentation), you should turn on `activedefrag`. Otherwise, `activedefrag` remains an optional setting.




## Memory intensive operations

The following operations use significant memory, especially when run in conjunction with a high write-rate:

### Export operation

The Memorystore [export](https://docs.cloud.google.com/memorystore/docs/redis/import-export-overview) feature uses the Redis [BGSAVE](https://redis.io/commands/bgsave) operation, which uses copy-on-write. Depending on the size of the data, write volume, and keys touched, the required memory for an export can be double the size of the space your data occupies. Therefore, for exports to succeed, you might need to reduce the `maxmemory-gb` limit to 50% of your instance capacity during exports.

### Scaling and version upgrade operations

[Scaling](https://docs.cloud.google.com/memorystore/docs/redis/scaling-behavior#standard_tier_scaling_behavior) or [Upgrading](https://docs.cloud.google.com/memorystore/docs/redis/version-upgrade-behavior#standard_tier_instance_upgrade_behavior) during periods of high write-load can put memory pressure on your instance due to memory overhead caused by replication. Also, a high read-load can increase the size of Redis's output buffer, leading to increased memory pressure. If a scale or upgrade operation fails due to memory pressure, you should:

  * Reduce the `maxmemory-gb` to 50% of your instance capacity before a scale/upgrade operation. If possible, you should also lower maxmemory during periods of low instance traffic, because doing so reduces the negative impact lowering maxmemory has on your [cache-hit ratio](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#cache-hit_ratio).
  * Scale/upgrade during periods of low-writes.



### Maintenance

[Maintenance](https://docs.cloud.google.com/memorystore/docs/redis/maintenance-policy) also adds memory pressure to your instance. You should take measures so that the System Memory Usage Ratio metric is at 50% or lower at the time of the scheduled maintenance. You can do this by scheduling for a time when instance traffic is low, or by temporarily scaling up your instance size during the maintenance window so that the System Memory Usage Ratio metric is at 50% or lower.

## Monitor your instance's memory usage

Monitor the metrics and set the alerts outlined in this section. These metrics and alerts give you insight into your instance's memory usage. To learn how to view metrics and set alerts, see [Monitoring Redis instances](https://docs.cloud.google.com/memorystore/docs/redis/monitoring-instances).

#### Memory Management Related Metrics

Metric | Full metric address  
---|---  
Maxmemory | redis.googleapis.com/stats/memory/maxmemory  
Memory usage | redis.googleapis.com/stats/memory/usage  
Memory usage ratio | redis.googleapis.com/stats/memory/usage_ratio  
System memory overload duration | redis.googleapis.com/stats/memory/system_memory_overload_duration  
System memory usage ratio | redis.googleapis.com/stats/memory/system_memory_usage_ratio  
Cache hit ratio | redis.googleapis.com/stats/memory/cache_hit_ratio  
Expirable keys | redis.googleapis.com/keyspace/keys_with_expiration  
Expired keys | redis.googleapis.com/stats/expired_keys  
Evicted keys | redis.googleapis.com/stats/evicted_keys  
  
#### Memory Usage Ratio

The **memory usage ratio** metric indicates how close your working set size is to reaching the `maxmemory-gb` limit. Unless the eviction policy is set to no-eviction, the instance data reaching maxmemory does not always indicate a problem. However, key eviction is a background process that takes time. If you have a high write-rate, you could run out of memory before Redis has time to evict keys to free up space.

#### System memory usage ratio

System memory usage ratio is a critical metric to monitor. To ensure the instance has sufficient memory to support your workload and other memory intensive operations, it is important to always have enough system memory available.

[Set an alert](https://docs.cloud.google.com/memorystore/docs/redis/monitoring-instances#system-memory-stackdriver-alert) to notify you if the system memory usage ratio metric reaches 80%. If it reaches 80%, you should begin to monitor the system memory usage ratio metric more closely. If system memory usage ratio continues to grow dramatically, you should turn on activedefrag, lower maxmemory, and consider scaling your instance.

Once system memory usage ratio hits 100%, any operation that further increases your instance's memory footprint is blocked and Redis returns the following error:

`-OOM command not allowed under OOM prevention.`

See [Manage your system memory usage ratio](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#manage_your_system_memory_usage_ratio) for more details.

#### System memory overload duration

If your memory usage is too high, Memorystore blocks writes to your instance to keep your instance healthy. **System memory overload duration** tracks how long your instance is in the blocked-writes state.

You should [Set an alert](https://docs.cloud.google.com/memorystore/docs/redis/monitoring-instances#system-memory-stackdriver-alert) for this metric so that you know when your writes are being blocked for your instance. Also, you can refer back to this metric to troubleshoot receiving the `-OOM command not allowed under OOM prevention.` error.

#### Cache-hit ratio

You should regularly monitor your cache-hit ratio so that you know what percentage of key lookups are successfully returned by keys in your Redis instance. Generally speaking, a higher cache-hit ratio is better than a lower cache-hit ratio. You should make a note of your cache-hit ratio before you make any large configuration changes such as adjusting the `maxmemory-gb` limit, changing your eviction policy, or scaling your instance. Then, after you modify your instance, check the cache-hit ratio again to see how your change impacted this metric.

#### Expirable keys and Expired keys

The Stackdriver metric **expirable keys** monitors the number of keys that are set for expiration. If there are no expirable keys, it can be an indication that you are not setting TTLs on keys. In such cases, when your instance data reaches the `maxmemory-gb` limit, there are no keys to evict which can result in an out of memory condition if you're using a `volatile-*` eviction policy.

Another metric you can monitor is **expired keys**. If the metric shows many expired keys, but you still see memory pressure on your instance, you should lower `maxmemory-gb`.

## Resolving an out of memory condition

Below are some best practices you should follow if your instance is experiencing memory pressure or running into out of memory errors.

  1. If you are using a `volatile-*` eviction policy, make sure you are setting [TTLs](https://redis.io/commands/ttl) on keys that you want to expire. See [Eviction policy](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#eviction_policy) for more details.

  2. For instances running Redis 4.0 and higher:

     1. Turn on `activedefrag` for your instance. See [Active defragmentation](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#active_defragmentation) for more details.
  3. Learn how to use metrics to problem-solve out of memory conditions, and gain insight into your instance's memory usage: [Monitor your instance's memory usage](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#monitor_your_system_memory_usage), [Manage your system memory usage ratio](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#manage_your_system_memory_usage_ratio).

  4. Learn how to to adjust maxmemory when running [Memory intensive operations](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#memory_intensive_operations).

  5. If the [system memory usage ratio](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#system_memory_usage_ratio) metric exceeds 80% reduce your instance's `maxmemory-gb` limit. See [Manage your system memory usage ratio](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#manage_your_system_memory_usage_ratio) for more details.

  6. Consider [scaling up your instance](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#scale_up_your_instance) capacity.

  7. If you are still encountering OOM conditions, then contact [Google Cloud Platform Support](https://cloud.google.com/support/).




## Right-size your Memorystore instance

This section covers three distinct approaches that help you right-size your instance based on your workload:

  * [Determine the initial size of a Memorystore instance](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#determine_the_initial_size_of_a_cloud_memorystore_instance) explains how to estimate your instance size before you create it.
  * [Monitor your instance's memory usage](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#monitor_your_instances_memory_usage) outlines metrics that provide helpful information regarding how your instance is using memory.
  * [Manage your system memory usage ratio](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#manage_your_system_memory_usage_ratio) explains what to do if the system memory usage ratio exceeds 80%.



### Determine the initial size of a Memorystore instance

First, you should choose whether you want a Standard Tier or Basic Tier instance. To learn more about Memorystore for Redis tiers, refer to [Redis tier capabilities](https://docs.cloud.google.com/memorystore/docs/redis/redis-tiers). Once you have selected the right tier for your application, follow these steps to determine what instance size you need:

  1. Determine the size of your data.

     * Estimate the number of keys, and the average size of keys, that your application will write to your Redis instance. Multiply these values to get a rough estimate of the instance size you need.
  2. Choose an eviction policy.

     * If you use the `noeviction` maxmemory policy your instance size must be big enough to hold your peak workload and working set. If you run out of memory with this maxmemory policy, your instance can enter an out of memory condition.
     * Other eviction policies do not influence the instance size you should provision.
  3. Provision extra memory for Standard Tier instances

     * Unlike Basic Tier instances, Standard Tier instances reserve 10% of instance capacity as a replication buffer. If you choose a Standard Tier instance, make sure you take the data estimation from step one and provision an extra 10% for the replication buffer.
  4. Estimate your average and peak write-rate

     * If possible, estimate the write-rate, and size of keys that your application will use. The write-rate compared with the rate of key-removal determines how fast your instance will grow over time.
  5. Scale up to reach your desired [cache-hit ratio](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#cache-hit_ratio)

     * Monitor the cache-hit ratio, and if you are not getting as many successful cache-hits as you want, this means you either need to increase your instance size, or make sure that your application is writing the keys to your Memorystore instance that are being requested, and not fulfilled.



### Determine if your instance is blocking writes due to an out of memory condition

If you get the following error:

`-OOM command not allowed under OOM prevention.`

Then check if:

  1. The system memory usage ratio metric exceeded 80% right before your instance started experiencing issues.
  2. The system memory usage ratio grew very rapidly before issues with your instance occurred.
  3. The [system memory overload duration](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#system_memory_overload_duration) metric showed values above zero during the same period where you experienced blocked writes.



If so, this likely indicates that the instance is blocking writes due to an out of memory condition.

### Manage your system memory usage ratio

[Set an alert](https://docs.cloud.google.com/memorystore/docs/redis/monitoring-instances#create-stackdriver-alert) to notify you if the **system memory usage ratio** metric exceeds 80%. If system memory usage ratio exceeds 80%, you should take appropriate action so that the instance does not run out of memory. Depending on the write volume and key access pattern, system memory usage can potentially increase to 100% quickly. Memorystore provides the following ways to manage the **system memory usage ratio** :

  * Turn on `activedefrag` for instances running Redis version 4.0 and higher.
  * Lower the `maxmemory-gb` limit of your instance.
  * Scale up the instance.
  * Choose the appropriate eviction policy.
  * Set TTLs on volatile keys.
  * Manually delete keys from your instance.



#### Turn on activedefrag

If the **system memory usage ratio** exceeds 80%, turn on `activedefrag` (for instances running Redis version 4.0 and higher). Defragmentation can take hours to release fragmented memory. If write traffic is high, defragmentation alone may not be enough to stop your instance from running out of memory. Therefore, you may need to implement the following recommendations:

#### Lower the maxmemory limit of your instance

If system memory usage ratio exceeds 80% you should lower `maxmemory-gb`, but first view how the system memory usage ratio has changed over time to determine what new `maxmemory-gb` limit to set.

**Scenario 1:** System memory usage ratio has been gradually and slowly climbing. Fragmentation is a likely issue, and you should lower `maxmemory-gb` in small increments until system memory usage ratio stabilizes below 80%.

**Scenario 2:** System memory usage ratio spiked rapidly, and you see a significant write-load on your instance. A [Memory intensive operation](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#memory_intensive_operations) likely caused the spike. In this situation you should lower the `maxmemory-gb` limit in larger increments to ensure that the instance either avoids entering an out of memory condition, or recovers from an out of memory condition. You should take note that lowering maxmemory can reduce your instances [cache-hit ratio](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#cache-hit_ratio). A much lower cache-hit ratio indicates that you should scale up your instance so that your application can profit from the advantages of using Redis. To learn how to adjust the `maxmemory-gb` configuration, see [Configuring Redis instances](https://docs.cloud.google.com/memorystore/docs/redis/configuring-redis).

#### Scale up your instance

**Important:** During scaling, Memorystore maintains the ratio of `maxmemory-gb` to instance capacity. By default this ratio is 1:1 and `maxmemory-gb` is equal to the instance capacity. If you reduce the `maxmemory-gb` limit and scale your instance, the lowered ratio for `maxmemory-gb` is applied to your new instance size.

Follow the instructions at [Scaling Redis instances](https://docs.cloud.google.com/memorystore/docs/redis/scaling-instances) to increase your instance capacity.

##### Maxmemory scaling example:

If you have a 10 GB instance with `maxmemory-gb` set to 8 GB, you have 8 GB for storing keys and 2 GB of memory overhead. If you scale the instance to 20 GB, `maxmemory-gb` is scaled to 16 GB. Therefore, your instance now has 16 GB of memory for storing keys, and 4 GB of overhead. See [Scaling Redis instances](https://docs.cloud.google.com/memorystore/docs/redis/scaling-instances) for instructions on how to increase or decrease the size of your instance.

#### Choose the appropriate eviction policy

If you are storing volatile data, choose one of the `volatile-*` [eviction policies](https://docs.cloud.google.com/memorystore/docs/redis/redis-configs#maxmemory_policies). If you are storing data that isn't volatile, choose one of the `allkeys-*` policies.

#### Manually delete keys from your instance

You can improve out of memory conditions by deleting keys from your instance manually. This is a temporary solution that helps you improve your instance health.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
