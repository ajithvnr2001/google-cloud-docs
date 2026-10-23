---
url: https://docs.cloud.google.com/memorystore/docs/memcached/supported-monitoring-metrics/
title: Supported monitoring metrics for Memorystore for Memcached \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:56.119385+00:00
---

# Supported monitoring metrics for Memorystore for Memcached  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/supported-monitoring-metrics/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview)



Send feedback 

#  Supported monitoring metrics for Memorystore for Memcached Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the metrics available for Memorystore for Memcached, and describes what each metric tracks. These metrics are available in both the Google Cloud console and in Cloud Monitoring.

To learn how to view metrics using Cloud Monitoring, see [Monitoring Memcached instances](https://docs.cloud.google.com/memorystore/docs/memcached/monitoring-instances).

## Memcached metrics

Cloud Monitoring metric name | Google Cloud console metric name | Full endpoint URL | Description  
---|---|---|---  
Active Connections | Active Connections | memcache.googleapis.com/node/active_connections | Number of active client connections to the Memcached node.  
CPU Usage Percent | CPU Usage Percent | memcache.googleapis.com/node/cpu/utilization | CPU usage percent by Memcached node.  
CPU Usage Time | CPU Usage Time | memcache.googleapis.com/node/cpu/usage_time | CPU usage time by Memcached processes, grouped by mode, e.g. user/kernel.  
Eviction Count | Eviction Count | memcache.googleapis.com/node/eviction_count | Count of items getting evicted from a Memcached node.  
Hit Ratio | Hit Ratio | memcache.googleapis.com/node/hit_ratio | Ratio of cache hits to cache misses for the Memcached node excluding set operations. Reported as a percentage.  
Items | Items | memcache.googleapis.com/node/items | Count of items stored in the Memcached node.  
Memory Usage | 

  * Memory Usage 
  * Unused Memory 

| memcache.googleapis.com/node/cache_memory | The memory usage of all of the nodes in your cluster, broken down by:  


  * used memory
  * unused memory

Memcached stores items in memory in chunks and slab classes. Depending on your item size distribution, it's possible that some memory will never be used. See the open source Memcached [documentation](https://www.github.com/memcached/memcached/wiki/UserInternals) to understand how memory management works in Memcached.  
Operation Count | 

  * Operation Count 
  * Get Operations 
  * Set Operations 
  * Delete Operations 

| memcache.googleapis.com/node/operation_count | Count of the operations sent to a Memcached node, broken down by the response type:   


  * `get` operations
  * `set` operations
  * `delete` operations

  
Received Bytes | Received Bytes | memcache.googleapis.com/node/received_bytes_count | Bytes of memory received by the Memcached node from the network. These are the Memcached requests coming from client VMs.  
Sent Bytes | Sent Bytes | memcache.googleapis.com/node/sent_bytes_count | Bytes of memory sent by the Memcache node to the network. These are the Memcache responses.  
System Memory Utilization | System Memory Utilization | memcache.googleapis.com/node/memory/utilization | Shows you what percentage of the total system memory is being used by items in the cache and memory overhead. See [System Memory Utilization](https://docs.cloud.google.com/memorystore/docs/memcached/memory-management-best-practices#system_memory_utilization) for more information.  
Uptime | Uptime | memcache.googleapis.com/node/uptime | How long the Memcached node has been up, in seconds.  
  
## Known Issues

  * For the `operation_count` metric, the `gat/gats` command currently does not show up in the Google Cloud console or in Cloud Monitoring. OSS Memcached doesn't update its `get` counters on `gat/gats` at this point. 
  * For the `operation_count` metric, the `touch` command does not currently get reported. 
  * For the `operation_count` metric, `cas` operations are reported under `set` operations.



## What's next

  * [Monitor your Memcached instances](https://docs.cloud.google.com/memorystore/docs/memcached/monitoring-instances).
  * View the [audit logs](https://docs.cloud.google.com/memorystore/docs/memcached/audit-logging) for your Memcached instance.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
