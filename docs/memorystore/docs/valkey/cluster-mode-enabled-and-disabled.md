---
url: https://docs.cloud.google.com/memorystore/docs/valkey/cluster-mode-enabled-and-disabled/
title: Enable and disable cluster mode \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:50.575911+00:00
---

# Enable and disable cluster mode  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/cluster-mode-enabled-and-disabled/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Enable and disable cluster mode Stay organized with collections  Save and categorize content based on your preferences. 

This page explains the two available modes for Memorystore for Valkey: Cluster Mode Enabled and Cluster Mode Disabled.

  * **Cluster Mode Enabled:** Cluster Mode Enabled supports the OSS Valkey [cluster specification](https://valkey.io/topics/cluster-spec/). It lets you partition your data across multiple shards and is useful for applications with high volume or velocity of data.

  * **Cluster Mode Disabled:** While in Cluster Mode Disabled, your instance isn't partitioned and is hosted on a single shard. You can use this mode if the volume of data and write throughput can be handled by a single node and you prefer to use the [specific features](https://docs.cloud.google.com/memorystore/docs/valkey/cluster-mode-enabled-and-disabled#comparison) that aren't available in Cluster Mode Enabled.




You can only select between Cluster Mode Enabled and Disabled when you create an instance. The `server_mode` field in the output of the [INFO](https://valkey.io/commands/info/) command specifies the mode of the instance. After you create an instance with either Cluster Mode Enabled or Cluster Mode Disabled, you can't change the instance to the other mode. We recommend that you select Cluster Mode Enabled because this mode has better horizontal scaling characteristics.

## Compare Cluster Mode Enabled and Cluster Mode Disabled

Feature | Cluster Mode Enabled | Cluster Mode Disabled  
---|---|---  
Horizontal scaling | 1 to 250 shards | Not supported (single shard only)  
Client support | [Need a cluster-aware client to use the discovery endpoint](https://docs.cloud.google.com/memorystore/docs/valkey/client-library-code-samples#client_lib_cluster) | [Use any Valkey or Redis client](https://docs.cloud.google.com/memorystore/docs/valkey/client-library-code-samples#client_lib_cluster_disabled)  
Multi-key commands | Supported only in a single keyslot | Supported across all keys within a database  
[ Maximum writable capacity](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#maximum_writable_capacity_given_cluster_shape) | 14,500 GB | 58 GB  
Maximum databases per instance | 1 | 16 (configurable up to 100 databases)  
  
Regardless of whether you specify Cluster Mode Enabled or Cluster Mode Disabled for your Memorystore for Valkey instance, the following conditions apply:

  * You can [increase or decrease the size of the instance](https://docs.cloud.google.com/memorystore/docs/valkey/about-scaling-instance-capacity) only when you create it.
  * You can have a maximum of five [read replicas](https://docs.cloud.google.com/memorystore/docs/valkey/ha-and-replicas#replicas) for the instance.



## Which should I choose

When choosing between Cluster Mode Enabled and Cluster Mode Disabled, consider the following factors:

  * **Read and write throughput:** If your write throughput is fulfilled by a single node and your read throughput is fulfilled by a maximum of two replicas, then use a Cluster Mode Disabled instance. If the read and write throughput requirements are high, then use a Cluster Mode Enabled instance because this type of instance can spread the load across different nodes.
  * **Migrate from Memorystore for Redis:** If you're using a [Memorystore for Redis instance](https://docs.cloud.google.com/memorystore/docs/redis/memorystore-for-redis-overview) or a self-managed Redis instance, migrating to a Cluster Mode Disabled instance requires minimal changes as compared to migrating to a Cluster Mode Enabled instance. To migrate to a Cluster Mode Enabled instance, you must use a [cluster aware client](https://docs.cloud.google.com/memorystore/docs/valkey/client-library-code-samples#client_lib_cluster).



Memorystore for Valkey supports [ IAM authentication](https://docs.cloud.google.com/memorystore/docs/valkey/about-iam-auth), which is a more-secure authentication mechanism than the plain-text authentication that Memorystore for Redis supports.

  * **Multi-key queries:** A Cluster Mode Disabled instance supports multi-key operations (for example: MGET, MSET, EVAL) across keys within the database. For a Cluster Mode Enabled instance, multi-key operations are limited to a single hash slot.
  * **Namespacing:** With Cluster Mode Disabled, you can use multiple databases to bucket different kinds of data by using the `SELECT` command. This feature is useful if you want to use the same instance to power multiple applications or you might need to write different types of unrelated data. Multiple databases aren't supported by Cluster Mode Enabled. As a best practice, we recommend that you use multiple instances instead of multiple databases to ensure Quality of Service (QoS). Multiple databases on the same node provide logical isolation only.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
