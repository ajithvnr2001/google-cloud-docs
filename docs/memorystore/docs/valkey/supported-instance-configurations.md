---
url: https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations/
title: Supported instance configurations \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:55.753362+00:00
---

# Supported instance configurations  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Supported instance configurations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes maxmemory policies and other configurations available for Memorystore for Valkey.

For instructions on how to modify the configurations listed on this page, see [Configure an instance](https://docs.cloud.google.com/memorystore/docs/valkey/configure-instances).

## Maxmemory policies

When your instance memory is full, and a new write comes in, Valkey evicts keys to make room for the write based on your instance's maxmemory policy. The default maxmemory policy for Memorystore for Valkey is `volatile-lru`. You can also use one of the following maxmemory policies:

  * `noeviction`: Returns an error when the instance reaches maxmemory. Does not overwrite or evict any data.
  * `allkeys-lfu`: Evicts the least frequently used (LFU) keys from the entire keyset.
  * `allkeys-lru`: Evicts the least recently used (LRU) keys from the entire keyset.
  * `volatile-lfu`: Evicts the least-frequently-used keys that are set with TTL (time to live) expirations.
  * `volatile-lru`: Evicts the least recently used (LRU) keys that are set with TTL expirations.
  * `allkeys-random`: Evicts random keys from the entire keyspace.
  * `volatile-random`: Evicts random keys from among those set with TTL expirations.
  * `volatile-ttl`: Evicts the keys with the shortest TTL from among those set with TTL expirations.



## Modifiable configuration parameters

You can modify the following parameters when creating or updating a Memorystore for Valkey instance.

Parameter | Description | Acceptable values  
---|---|---  
**maxmemory-clients** | This configuration allows users to control maximum memory usage of clients.  
  
Total memory usage of normal/pubsub clients. If the limit is hit, the client with most memory usage will be evicted.  | Acceptable values are integer percent values between `0%` and `100%`. Represents the percentage of instance maxmemory to which client storage is limited.  
  
Default value depends on the node type. For more information, see [Node characteristics](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#node_characteristics).   
**maxmemory** | Designates an adjustable limit at which your eviction policy takes effect. You set the maxmemory limit at the individual node level, but the setting applies to all nodes. For example, suppose that you have an instance with 3 nodes, use a 58 GB `highmem-xlarge` node type, and want to set `maxmemory` to 90% of your total instance capacity. To do this, you set `maxmemory` to 52.2 GB, which is 90% of your node capacity. This applies to all nodes, which sets the total instance maxmemory limit at 90%. For more information about default reserved overhead, see [keyspace capacity and reserved overhead](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#keyspace_capacity_and_reserved_overhead).  | Maxmemory limit for your instance.  
  
It supports the following units:  
  
`b` (default)  
`k`  
`kb`  
`m`  
`mb`  
`g`  
`gb`  
  
**maxmemory-policy** | Specifies the behavior Valkey follows when the instance data reaches the `maxmemory` limit. For more information about each policy, see [Maxmemory policies](https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations#maxmemory_policies) .  |  `noeviction`  
`allkeys-lru`  
`volatile-lru` (default)  
`allkeys-random`  
`volatile-random`  
`volatile-ttl`  
`volatile-lfu`   
`allkeys-lfu`  
  
**notify-keyspace-events** | Allows clients to subscribe to notifications on certain keyspace events.  |  `""`  
No event (default)  
`K`  
Keyspace events, published with __keyspace@<db>__ prefix.  
`E`  
Keyevent events, published with __keyevent@<db>__ prefix.  
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
  
**slowlog-log-slower-than** | Lets you configure the slow log. Specifies the execution time threshold (in microseconds). Whenever a command exceeds this threshold, it is added to the slow log.  | Default value is 10000.  
  
A value of zero forces the logging of every command. Whereas, a value of -1 disables the slow log. Any other negative value is rejected.   
**maxclients** | Lets you configure the maxclients configuration for your instance. For information about the max clients limit and default for your instance, see [Max clients](https://docs.cloud.google.com/memorystore/docs/valkey/quotas#max_clients). | Default value depends on the node type. For more information, see [Node characteristics](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#node_characteristics).   
**databases** | Lets you configure the number of databases for your instance. Memorystore for Valkey supports this parameter for [Cluster Mode Disabled instances](https://docs.cloud.google.com/memorystore/docs/valkey/cluster-mode-enabled-and-disabled) only.  **Important** : You can set this configuration parameter only when you [ create an instance](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances). After you create the instance, you can't modify the settings for this parameter. | The default setting is 16 databases. You can configure this up to 100 databases.   
**cluster-databases** | Lets you configure the number of databases for your instance, version 9.0 and later. Memorystore for Valkey supports this parameter for [Cluster Mode Enabled instances](https://docs.cloud.google.com/memorystore/docs/valkey/cluster-mode-enabled-and-disabled) only. **Important** : You can set this configuration parameter only when you [ create an instance](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances). After you create the instance, you can't modify the settings for this parameter. | The default setting is 1 database. You can configure this up to 100 databases.   
  
## Unmodifiable configuration parameters

Memorystore for Valkey sets the value of the `proto-bulk-max-len` configuration parameter to 256 MB. You can't change this value.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
