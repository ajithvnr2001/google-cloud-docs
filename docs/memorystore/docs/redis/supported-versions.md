---
url: https://docs.cloud.google.com/memorystore/docs/redis/supported-versions/
title: Supported versions \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:55.806865+00:00
---

# Supported versions  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/supported-versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Supported versions Stay organized with collections  Save and categorize content based on your preferences. 

Memorystore for Redis is backed by open-source Redis software. Memorystore for Redis supports Redis versions 3.2, 4.0, 5.0, 6.x, 7.0, and 7.2. The default version is 7.2.

You can find out which version your instance uses by [viewing details about the instance](https://docs.cloud.google.com/memorystore/docs/redis/create-manage-instances#view-instance-information). You can also [upgrade the version of an instance](https://docs.cloud.google.com/memorystore/docs/redis/upgrading-instance-version) to any newer version. For example, you can upgrade from version 3.2 to 7.2. For a history of Memorystore for Redis product updates, see the [Release notes](https://docs.cloud.google.com/memorystore/docs/redis/release-notes).

## Version support policy

Memorystore for Redis supports one patch version for every major OSS Redis version that's listed in the Current versions section of this page. During maintenance periods, the patch is kept up to date.

Memorystore for Redis monitors for any critical patches that it needs to apply to your instance. Memorystore for Redis rolls out critical security patches outside of the regular maintenance period. For more information, see [About maintenance](https://docs.cloud.google.com/memorystore/docs/redis/maintenance-policy).

## Current versions

This table shows the supported Redis versions, the patch levels for these versions, and when the versions were last updated:

Redis major version | Patch level | Last update  
---|---|---  
7.2 | 7.2.0 | February 29, 2024  
7.0 | 7.0.12 | July 17, 2023  
6.x | 6.2.14 | November 14, 2023  
5.0 | 5.0.14 | May 09, 2022  
4.0 | 4.0.14 | June 17, 2019  
3.2 | 3.2.13 | June 21, 2018  
  
### Redis version 7.2

The following table provides information about the vector search feature for Redis version 7.2:

Feature | Description | Supported in Memorystore for Redis  
---|---|---  
Vector search | Redis version 7.2 introduces vector data storage and vector data search. These capabilities integrate with the [LangChain](https://python.langchain.com/docs/get_started/introduction) framework. For more information, see [Vector search for generative AI applications](https://docs.cloud.google.com/memorystore/docs/redis/about-vector-search).  | Yes  
  
### Redis version 7.0

The following table outlines Memorystore for Redis support of some major features introduced by OSS Redis version 7.0.

In addition to the features listed in this section, instances that run Redis version 7.0 with in-transit encryption see [improved performance](https://docs.cloud.google.com/memorystore/docs/redis/about-in-transit-encryption#performance_impact_of_enabling_in-transit_encryption).

Feature | Description | Supported in Memorystore for Redis  
---|---|---  
Redis functions | Redis 7.0 introduces Redis functions, which provides improved Lua script capabilities on the Redis server. Before version 7.0, to use Lua scripts, you needed to use the `EVAL` command. Redis functions provides simplified and optimized scripting. For more information, see [Redis functions](https://redis.io/docs/latest/develop/programmability/functions-intro/) in the Redis documentation. | Yes  
Client eviction | [Client eviction](https://redis.io/docs/latest/develop/reference/clients/#client-eviction), added in Redis 7.0, disconnects clients if the total memory used by all client connections exceeds a user-specified limit. For more information about configuring this limit for Memorystore for Redis, see [Configure a Redis instance](https://docs.cloud.google.com/memorystore/docs/redis/configure-redis). | Yes  
Access Control List (ACL) improvements | Redis 7.0 introduces improved [ACL](https://redis.io/docs/latest/operate/oss_and_stack/management/security/acl/) functionality. | No  
Sharded Pub/Sub | Redis 7.0 introduces [sharded Pub/Sub](https://redis.io/docs/latest/develop/pubsub/#sharded-pubsub). | No  
Multi-part Append-only File (AOF) persistence | Redis 7.0 introduces multi-part AOF [persistence](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/). | No  
Redis modules | You can use Redis 7.0 to write [modules](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/install/) that can extend Redis' functionalities and implement new data types. | No  
  
### Redis version 6.x

The following table outlines Memorystore for Redis support of some major features introduced by OSS Redis version 6.x:

Feature | Description | Supported in Memorystore for Redis  
---|---|---  
Threaded I/O | With Redis 6.x, if multiple vCPUs are available, then some I/O operations can run in parallel. Memorystore for Redis leverages the optimal number of I/O threads for a configured capacity tier automatically. Starting with the M3 capacity tier, additional I/O threads are utilized, typically resulting in an improvement in query throughput performance. | Yes  
Longest common subsequence (LCS) command | The LCS command, supported from Redis version 6.x, lets users find non-contiguous common elements between strings. | Yes  
Redis database (RDB) diskless load for replicas | Redis 6.x makes diskless loading available for replicas. This lets a replica load the RDB from the socket instead of the disk, improving performance. For more information, see the [Redis 6.0 conf](https://raw.githubusercontent.com/redis/redis/6.0/redis.conf) file. | Yes  
Built-in traffic encryption | Redis 6.0 adds built-in SSL for encrypting traffic. Although Memorystore for Redis doesn't support this feature for OSS Redis version 6.0, Memorystore for Redis offers its own [in-transit encryption](https://docs.cloud.google.com/memorystore/docs/redis/in-transit-encryption). | No  
Access control lists (ACLs) | Redis ACLs let you restrict the users and actions that interact with the Redis instance. | No  
  
### Redis version 5.0

The following table outlines Memorystore for Redis support of some major features introduced by OSS Redis version 5.0:

Feature | Description | Supported in Memorystore for Redis  
---|---|---  
Redis streams | Redis 5.0 introduces the [streams](https://redis.io/docs/latest/develop/data-types/streams/) data structure. Streams support the List functionality, such as [`XADD`](https://redis.io/commands/xadd) and [`XDEL`](https://redis.io/commands/xdel). Streams also introduce the concept of _consumer groups_ , which let multiple clients consume different portions of the stream.  | Yes, through the `stream-node-max-bytes` and `stream-node-max-entries` [configuration parameters](https://docs.cloud.google.com/memorystore/docs/redis/redis-configs#modifiable_configuration_parameters).  
Sorted set commands | Redis 5.0 introduces the following sorted set commands: [`ZPOPMAX`](https://redis.io/commands/zpopmax), [`ZPOPMIN`](https://redis.io/commands/zpopmin), [`BZPOPMAX`](https://redis.io/commands/bzpopmax), and [`BZPOPMIN`](https://redis.io/commands/bzpopmin). These commands push and pop the highest or lowest values stored in your sorted set. | Yes  
  
### Redis version 4.0

The following table outlines Memorystore for Redis support of some major features introduced by OSS Redis version 4.0:

Feature | Description | Supported in Memorystore for Redis  
---|---|---  
Cache eviction improvements | Supports the Least Frequently Used (LFU) eviction policy. For more information, see [Eviction policy](https://redis.io/docs/latest/operate/rs/databases/memory-performance/eviction-policy/) in the Redis documentation. | Yes, through the `allkeys-lfu` and `volatile-lfu` [maxmemory policies](https://docs.cloud.google.com/memorystore/docs/redis/redis-configs#maxmemory_policies).  
Active defragmentation | Introduces the ability to defragment memory while Redis is running.  | Yes, through the `activedefrag` [configuration parameter](https://docs.cloud.google.com/memorystore/docs/redis/redis-configs#modifiable_configuration_parameters).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
