---
url: https://docs.cloud.google.com/memorystore/docs/valkey/supported-versions/
title: Supported versions \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:37.501586+00:00
---

# Supported versions  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/supported-versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Supported versions Stay organized with collections  Save and categorize content based on your preferences. 

Memorystore for Valkey is backed by open-source Valkey software. Memorystore for Valkey supports Valkey versions 7.2, 8.0, 9.0, and 9.1. The default version is 9.1.

You can find out which version your instance uses by [viewing details about the instance](https://docs.cloud.google.com/memorystore/docs/valkey/view-instance-information). You can also [upgrade the version of an instance](https://docs.cloud.google.com/memorystore/docs/valkey/upgrade-valkey-version#upgrade-version) to any newer version. For example, you can upgrade from version 7.2 to 9.1. For a history of Memorystore for Valkey product updates, see the [Release notes](https://docs.cloud.google.com/memorystore/docs/valkey/release-notes).

**Important:** After you upgrade the version of an instance, you can't downgrade the instance to an earlier version.

## Current versions

This table shows the supported Valkey versions and when each version was last updated:

Valkey major version | Last update  
---|---  
[ 9.1](https://docs.cloud.google.com/memorystore/docs/valkey/supported-versions#valkey_version_91) | July 27, 2026  
[9.0](https://docs.cloud.google.com/memorystore/docs/valkey/supported-versions#valkey_version_90) | March 11, 2026  
[8.0](https://docs.cloud.google.com/memorystore/docs/valkey/supported-versions#valkey_version_80) | October 2, 2024  
[7.2](https://docs.cloud.google.com/memorystore/docs/valkey/supported-versions#valkey_version_72) | August 30, 2024  
  
## Valkey version 9.1

Valkey 9.1's major features focus on throughput gains, database-level access control for users, and other commands.

The following table outlines Memorystore support of some major features introduced by Valkey 9.1:

Feature | Description  
---|---  
Throughput gains | Internal optimizations to I/O threading and string handling provide up to a 17% increase in the overall throughput (and up to a 30% increase for `GET` operations) for your instances.  
Database-level access control | By using access control lists (ACLs), you can restrict user access at the database level for your instances.  
New commands | The following commands are available with Valkey 9.1: 

  * [`HGETDEL`](https://valkey.io/commands/hgetdel/): return the value of a hash field and delete it in a single atomic operation
  * [`MSETNX`](https://valkey.io/commands/msetnx/): set multiple keys with a shared expiration time
  * [`CLUSTERSCAN`](https://valkey.io/commands/clusterscan/): scan for keys across all nodes of an instance

In addition, the [`HSETEX`](https://valkey.io/commands/hsetex/) command has support for the `NX` and `XX` parameters.  
  
## Valkey version 9.0

Valkey 9.0's major features focus on performance and scalability enhancements, including hash field expiration for more granular data management.

Performance improvements include memory prefetching for pipelining commands, zero-copy responses for large requests, the `COMMANDLOG` container command, and single instruction, multiple data (SIMD) optimizations for `BITCOUNT` and `hyperloglog` commands.

The following table outlines Memorystore support of some major features introduced by Valkey 9.0:

Feature | Description  
---|---  
Hash field expiration | This feature introduces finer-grained control over data expiration for individual hash fields, rather than just the entire hash key.  
Memory prefetching | This feature improves performance by prefetching memory for pipelined commands, potentially increasing throughput by up to 40%.  
Zero-copy responses | This feature reduces overhead by eliminating data copying for large requests, which can lead to up to a 20% increase in throughput.  
The `COMMANDLOG` command | `COMMANDLOG` is a container command for managing logs that record resource-intensive commands. You can use this command to identify latency, CPU, or network bottlenecks for your instances. `COMMANDLOG` also provides detailed tracking of slow-running, large-request, and large-reply commands. You can use this tracking to diagnose latency issues that [ `SLOWLOG`](https://valkey.io/commands/slowlog/) misses. This provides you with better observability into end-to-end latency for your instances.  
SIMD optimizations | This feature uses SIMD instructions to accelerate certain commands like `BITCOUNT` and `hyperloglog`, potentially improving throughput by up to 200%.  
By-polygon support for geospatial indexes | This feature adds support for using polygons in geospatial index queries.  
  
## Valkey version 8.0

The following table outlines Memorystore support of some major features introduced by Valkey 8.0:

Feature | Description  
---|---  
Asynchronous I/O threading for performance boost | This feature significantly improves performance by enabling parallel processing between the main thread and I/O threads. It offloads I/O tasks to the I/O threads, allowing them to run concurrently with the main thread, and optimizes memory access through efficient command batching.  
Reliability improvement for cluster scaling operations | This feature significantly improves the reliability and automation of the Valkey cluster re-sharding process by addressing failures during slot migration. These improvements prevent data loss and cluster inconsistencies, ensuring a more resilient system when failures occur.  
Enhanced memory efficiency through key embedding in the main dictionary | This enhancement significantly improves memory efficiency by embedding keys directly within dictionary entries, eliminating the need for separate key pointers. This change reduces memory overhead and enhances performance, particularly for large datasets.  
Improved Pub/Sub efficiency by using lightweight cluster messages | This feature introduces a new lightweight cluster message type to enhance the efficiency of Pub/Sub message propagation within a Valkey cluster. The new message type significantly reduces the overhead by minimizing the amount of node information included in each message.  
  
## Valkey version 7.2

The following table outlines Memorystore support of some major features introduced by Valkey 7.2:

Feature | Description  
---|---  
New command | Introduces the WAITAOF command that blocks the client until a specified number of Redises have synced all previous write commands to the AOF on disk.  
Memory optimization | Memory usage is significantly reduced for small list-type and set-type keys, with further optimizations for large sets. Memory management for cluster bus links with many pending messages is improved, and incremental reclamation of OS page cache for RDB files enhances memory efficiency.  
Performance optimization | Performance improvements include faster ZRANGE replies with integer scores and optimized double replies, particularly for sorted sets. Multi-key commands in cluster mode now execute more efficiently, and workloads without pipelining see improved command processing.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
