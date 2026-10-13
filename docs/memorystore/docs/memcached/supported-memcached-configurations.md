---
url: https://docs.cloud.google.com/memorystore/docs/memcached/supported-memcached-configurations/
title: Supported Memcached configurations \u00a0|\u00a0 Memorystore for Memcached \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:57.078898+00:00
---

# Supported Memcached configurations  |  Memorystore for Memcached  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/supported-memcached-configurations/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview)



Send feedback 

#  Supported Memcached configurations Stay organized with collections  Save and categorize content based on your preferences. 

This page provides a list of Memorystore for Memcached's modifiable and unmodifiable Memcached configuration parameters, as well as the default values for the parameters.

## Modifiable configuration parameters

**Important:** Updating a node's configurations causes a cache flush on that node. Therefore, updates to node configuration parameters should be done in stages, as explained in [Configuring Memcached instances](https://docs.cloud.google.com/memorystore/docs/memcached/configuring-memcached).

You can modify the following parameters when creating or updating a Memorystore for Memcached instance. Updating parameters requires you to change and apply parameters in two separate steps. For more information about how to change these configurations, see [Configuring Memcached instances](https://docs.cloud.google.com/memorystore/docs/memcached/configuring-memcached).

Parameter | Acceptable values | Default value | Description  
---|---|---|---  
listen-backlog (-b) | 1-10000 | 1024 | Adjustable length of the connection backlog queue. The backlog is the number of network connection requests queued up to be processed by Memcached.  
disable-flush-all (-F) | true, false | false | Setting `disable-flush-all` to `true` disables the open source Memcached `flush-all` command. Modifying this configuration increments the `cmd_flush` counter, however a flush does not actually occur.   
disable-watch (-W) | true, false | false | **Memcached version 1.6.15, or later.** If set to `true` this parameter disables the use of watch commands. Watchers allow you to connect to Memcached and inspect what's going on internally. Fetches, mutations, connection events etc. can be observed by using watch <fetchers|mutation|evictions|connevents|deletions>.  
max-item-size (-I) | 524288-134217728 (bytes) | 1048576 |  The Memcached parameter `max-item-size` sets the maximum size limit for items stored in the instance. It is subject to a few additional constraints: 

  * **`max-item-size` must be greater than or equal to slab_chunk_max.** slab_chunk_max is set to 524288 bytes (512 KiB), and Memorystore for Memcached does not support changing this value. Therefore, the minimum value of max-item-size is 524288 bytes as opposed to the open source Memcached supported minimum (1024 bytes). 
  * `max-item-size` must be evenly divisible by slab_chunk_max (524288 bytes). 
  * `max-item-size` may not be more than half the total allocated size of the cache (the -m flag). 

  
slab-min-size (-n) | 1-1024 (bytes) | 48 | Sets the minimum item size and the size of the smallest Memcached slab.  
slab-growth-factor (-f) | 1.01-100.00 | 1.25 | `slab-growth-factor` is the multiplier used to calculate the size of Memcached chunks/slabs. Lowering this value can improve the efficiency of memory usage, but it depends on size of items to be stored and the available memory of the instance.  
protocol (-B) | auto, ascii | auto | The binding protocol. Designates which protocol clients attempting to connect to the server must use. Auto supports both binary and ascii protocol.   
disable-cas (-C) | true, false | false | If `disable-cas` is set to `true`, check and set (CAS) operations are disabled. Disabling CAS operations uses 8 fewer bytes for each item in the cache. Memcached uses the CAS operation to refresh an item's data if it hasn't been updated since the last retrieval.  
disable-evictions (-M) | true, false | false | If set to `true`, when out of memory, Memcached returns an error rather than evicting items. The instance won't accept writes until memory becomes available.  
max-reqs-per-event (-R) | 1-1000 | 20 | Limits the number of requests per event that a single client connection can make. After the client exceeds this value, the server prioritizes other clients before it continues to process the original client request.  
reserved-memory-percent | 0.0-50.0 | 10.0 | Sets your instance's Reserved Memory to the specified percentage to increase the amount of space available for memory overhead. This setting also reduces cache memory by the same percentage. Instances created before October 25, 2021 have a default value of 0. For more information, see [Memory management best practices](https://docs.cloud.google.com/memorystore/docs/memcached/memory-management-best-practices#reserved_memory).   
  
## Supported extended options

Parameter | Acceptable values | Default value | Description  
---|---|---|---  
track_sizes | true, false | false (disabled) | If `track-sizes` is set to `true`, users can run the Memcached `stats sizes` command. We do not recommend enabling this configuration in production environments.  
watcher_logbuf_size | 0-2097151 (kibibytes) | 262144 | The size of the write buffer per active watcher connected. Changing this configuration adjusts the size of the `watch` command's logging buffer size. To avoid losing logs, increase `watcher_logbuf_size` when it is full.  
worker_logbuf_size | 48-524288 (kibibytes) | 65536 | Controls the size of the buffer for each active worker. The background thread reads from these buffers.  
lru_crawler | true, false | true (enabled) | The `lru_crawler` configuration enables a background process that scans through slabs and removes the least recently used (lru) items from those slabs. This process is not CPU or memory intensive. Since it is enabled, the process will run at launch time until you set `lru_crawler` to `false`.  
idle_timeout | 0-86400 seconds | 0 (disabled) | Set to 0 (disabled) by default. This configurations sets time in seconds that clients can idle before timing out and disconnecting.  
lru_maintainer | true, false | true (enabled) | Enabled by default. `lru_maintainer` is a background process that determines how recently items are accessed in order to properly sort all items by "least recently used" (lru).  
maxconns_fast | true, false | false (disabled) | Manages how Memcached processes new connections when the maximum number of clients is reached. When `maxconns-fast` is set to `false`, connections exceeding the maximum connection limit are added to a queue. When `maxconns-fast` is set to `true`, connections exceeding the maximum connection limit are dropped and served an error message.  
hash_algorithm | jenkins, murmur3, xxh3 | murmur3 | Designates the hash algorithm that the instance uses. Only instances using Memcached version 1.6.15 or higher can use the xxh3 config.  
  
## Unmodifiable configuration parameters

The following table lists the Memcached configuration parameters that you cannot modify with Memorystore for Memcached, and the default values of the parameters. For more details, see the list of [native Memcached configuration parameters](https://github.com/memcached/memcached/blob/master/doc/memcached.1).

Parameter | Default value  
---|---  
port (-p) | 11211  
memory-limit (-m) | Memorystore sets this value to match the memory configured for each node in the instance node config. This configuration is unmodifiable; however, you can add Reserved Memory with the reserved memory configuration listed above.  
threads (-t) | Memorystore sets this value to match the number of CPUs for each instance node.  
conn-limit (-c) | 65000 per node  
verbose (-v) | true  
slab_automove | true (enabled)  
slab_reassign | true (enabled)  
enable-largepages (-L) | false (disabled)  
lock-memory (-k) | false (disabled)  
expirezero-does-not-evict | Not supported. Deprecated in Memcached 1.4.35.  
slab_chunk_max | 524288 bytes  
modern | true (enabled)  
  
## What's next

  * Learn how to [configure Memcached instances](https://docs.cloud.google.com/memorystore/docs/memcached/configuring-memcached).
  * [Monitor your Memcached instances](https://docs.cloud.google.com/memorystore/docs/memcached/monitoring-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
