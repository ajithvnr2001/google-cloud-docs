---
url: https://docs.cloud.google.com/memorystore/docs/redis/supported-redis-configurations/
title: Supported Redis configurations \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:33:52.919198+00:00
---

# Supported Redis configurations  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/supported-redis-configurations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Supported Redis configurations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes maxmemory policies and other Redis configurations available for Memorystore for Redis. You do not need to restart your Redis instance if you adjust a configuration.

For instructions on how to modify the configurations listed below, see [Configuring Redis Instances](https://docs.cloud.google.com/memorystore/docs/redis/configuring-redis).

## Maxmemory policies

When your Redis instance memory is full, and a new write comes in, Redis evicts keys to make room for the write based on your instance's maxmemory policy. The **default maxmemory policy** for Memorystore for Redis is `volatile-lru`. You can also use one of the following maxmemory policies:

  * `noeviction`: Returns an error when the Redis instance reaches maxmemory. Does not overwrite or evict any data.
  * `allkeys-lfu`: Available in Redis version 4.0, or later. Evicts the least frequently used (LFU) keys from the entire keyset.
  * `allkeys-lru`: Evicts the least recently used (LRU) keys from the entire keyset.
  * `volatile-lfu`: Available in Redis version 4.0, or later. Evicts the least-frequently-used keys that are set with TTL (time to live) expirations.
  * `volatile-lru`: Evicts the least recently used (LRU) keys that are set with TTL expirations.
  * `allkeys-random`: Evicts random keys from the entire keyspace.
  * `volatile-random`: Evicts random keys from among those set with TTL expirations.
  * `volatile-ttl`: Evicts the keys with the shortest TTL from among those set with TTL expirations.



## Modifiable configuration parameters

You can modify the following parameters when creating or updating a Memorystore for Redis instance.

Parameter | Description | Acceptable values  
---|---|---  
**activedefrag** | **Redis version 4.0, or later.** Works to free up instance memory tied up by [standard OSS Redis memory fragmentation behavior](https://redis.io/topics/memory-optimization). | `no` (default)  
`yes`  
  
**databases** | To set this configuration, you must use the [Google Cloud CLI](https://docs.cloud.google.com/cli). In addition, you can set the configuration only when you [create an instance](https://docs.cloud.google.com/memorystore/docs/redis/create-manage-instances). After you create the instance, you can't modify the settings for this configuration.**Redis version 3.2, or later.** Specifies the number of databases on the Redis server. | `1-100`  
Default is `16`  
**lazyfree-lazy-eviction** | **Redis version 7.0, or later.** Enables/disables lazy free for eviction. `no` disables this configuration. For more information, see [REDIS.CONF](https://raw.githubusercontent.com/redis/redis/7.0/redis.conf) | `no` (default)  
`yes`  
  
**lazyfree-lazy-expire** | **Redis version 7.0, or later.** Enables/disables lazy free for expire. `no` disables this configuration. For more information, see [REDIS.CONF](https://raw.githubusercontent.com/redis/redis/7.0/redis.conf) | `no` (default)  
`yes`  
  
**lazyfree-lazy-user-del** | **Redis version 7.0, or later.** Enables/disables lazy free for user DEL. `no` disables this configuration. For more information, see [REDIS.CONF](https://raw.githubusercontent.com/redis/redis/7.0/redis.conf) | `no` (default)  
`yes`  
  
**lazyfree-lazy-user-flush** | **Redis version 7.0, or later.** Enables/disables the lazy free for user flush. `no` disables this configuration. For more information, see [REDIS.CONF](https://raw.githubusercontent.com/redis/redis/7.0/redis.conf) | `no` (default)  
`yes`  
  
**lfu-decay-time** | **Redis version 4.0, or later.** The time, in minutes, before the LFU frequency counter for a given key will be divided by two (or, if the counter is < 10, decremented by 1). See the [REDIS.CONF](https://raw.githubusercontent.com/antirez/redis/4.0/redis.conf) file for additional information. | Positive integers of the 'long' data type  
(default=1)  
**lfu-log-factor** | **Redis version 4.0, or later.** Determines how the frequency counter represents key hits. Before you modify the default configuration, read about how the `lfu-log-factor` configuration works in the [REDIS.CONF](https://raw.githubusercontent.com/antirez/redis/4.0/redis.conf) file. | Positive integers of the 'long' data type  
(default=10)  
**maxmemory-clients** | **Redis 7.0, or later.** This configuration allows users to control maximum memory usage of clients.  
  
Total memory usage of normal/pubsub clients. If the limit is hit, the client with most memory usage will be evicted | Default is `0%` (no limit). Acceptable values are integer percent values between `0%` and `100%`. Represents the percentage of instance maxmemory to which client storage is limited.  
**maxmemory-gb** |  Designates an adjustable limit at which your eviction policy takes effect. For example, if you have a 10 GB instance and you set `maxmemory-gb` to `8`, your eviction policy takes effect when your data occupies 8 GB of your instance memory. This leaves you 2 GB of memory as overhead. By default `maxmemory-gb` is set to your instance capacity. For details on how to best use the `maxmemory-gb` configuration, see the Memorystore [memory management best practices](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices).  
  
This configuration is displayed as `maxmemory-percent` in the Google Cloud console. When using the console, you set `maxmemory-percent` as percentage of your instance capacity instead of a specific number of GBs.  | Number of GB expressed as a whole number or decimal.  
Examples:  
`10` designates a `maxmemory-gb` of 10 GB.  
`1.5` designates a `maxmemory-gb` of 1.5 GB.  
`maxmemory-gb` can be reduced to a minimum of 20% of your instance capacity.   
**maxmemory-policy** | Specifies the behavior Redis follows when the instance data reaches the `maxmemory-gb` limit. Refer to [Maxmemory policies](https://docs.cloud.google.com/memorystore/docs/redis/redis-configs#maxmemory_policies) for a description of the behavior of each policy.  
  
For additional information about the open source Redis maxmemory policies, see the open source Redis [LRU cache page](http://redis.io/topics/lru-cache) | `noeviction`  
`allkeys-lru`  
`volatile-lru` (default)  
`allkeys-random`  
`volatile-random`  
`volatile-ttl`  
`volatile-lfu` (Redis version 4.0 and higher)  
`allkeys-lfu` (Redis version 4.0 and higher)  
``   
  
**notify-keyspace-events** | Allows clients to subscribe to notifications on certain keyspace events. See the [Redis Keyspace Notifications](http://redis.io/topics/notifications) page on the Redis site for more information. | `""` (default)  
`K`  
Keyspace events, published with __keyspace@__ prefix.  
`E`  
Keyevent events, published with __keyevent@__ prefix.  
`g`  
Generic commands (non-type specific) like DEL, EXPIRE, or RENAME  
`$`  
String commands  
`l`  
List commands  
`s`  
Set commands  
`h`  
Hash commands  
`z`  
Sorted set commands  
`x`  
Expired events (events generated every time a key expires)  
`e`  
Evicted events (events generated when a key is evicted for maxmemory)  
`A`  
Alias for g$lshzxe, so that the "AKE" string means all the events.  
  
`stream-node-max-bytes` | **Redis version 5.0, or later.** The Redis stream data structure uses a radix tree to store items. The `stream-node-max-bytes` parameter designates the maximum number of bytes available to store items in a single tree node. Once this limit is reached new items are stored in a new tree node. | Integers 0 and higher.  
(default=4096)  
0 designates a tree node of unlimited size.  
`stream-node-max-entries` | **Redis version 5.0, or later.** The Redis stream data structure uses a radix tree to store items. The `stream-node-max-entries` parameter designates the number of items that can be stored in a single node. When this limit is reached, new items are stored in a new tree node. | Integers 0 and higher.  
(default=100)  
0 designates a tree node with an unlimited number of items.  
`timeout` |  The number of seconds before idle client connections are terminated. However, if `timeout` is set to `0` idle clients do not timeout and remain connected until the client issues the termination.  | 0 (default)  
Integers >= 120  
Unit = **seconds**  
  
## Unmodifiable configuration parameters

The following table lists the Redis configuration parameters that you cannot modify in Memorystore for Redis and their default values. See the [Redis configuration](http://redis.io/topics/config) documentation for detailed information about these configuration parameters.

Parameter | Default Value  
---|---  
`lua-time-limit` | 5000  
`hash-max-ziplist-entries` | 2048  
`hash-max-ziplist-value` | 1024  
`list-max-ziplist-size` | -2  
`list-compress-depth .` | 0  
`set-max-intset-entries` | 512  
`zset-max-ziplist-entries` | 1024  
`zset-max-ziplist-value` | 1024  
`hll-sparse-max-byte` | 3000  
`activerehashing` | yes  
`hz` | 10  
`databases` | 16  
`maxclients` | 65000  
`slowlog-log-slower-than` | 10000  
`slowlog-max-len` | 128  
`repl-diskless-load` | swapdb  
`io-threads-do-reads` | yes  
  
## What's next

  * Learn more about Redis configurations on the open source [Redis configuration](https://redis.io/topics/config) page



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
