---
url: https://docs.cloud.google.com/looker/docs/enabling-redis-cache-on-customer-hosted-instance/
title: Enabling a Redis cache on a customer-hosted instance \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:20.122373+00:00
---

# Enabling a Redis cache on a customer-hosted instance  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/enabling-redis-cache-on-customer-hosted-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Enabling a Redis cache on a customer-hosted instance Stay organized with collections  Save and categorize content based on your preferences. 

Looker maintains a [cache](https://docs.cloud.google.com/looker/docs/caching-and-datagroups#how_looker_uses_cached_queries) as part of each instance. Looker's default cache is a custom caching solution that is based on several layers: in-memory, local disk, and remote disk. The Looker internal database is used as an index that identifies where cached objects are located in the system.

If you are hosting your own Looker instance, you can optionally configure Looker to use a separately hosted [Redis](https://redis.io/) cache. A Redis cache can provide the following benefits:

  * **Improved cache retrieval** — The primary improvement will be in consistent cache-retrieval times. As the number of nodes in a Looker cluster increases, the inter-node communication can degrade cache performance. The new Redis cache architecture consolidates the cache, which results in consistent cache-retrieval times no matter the size of your Looker cluster.
  * **Less load** — Additionally, the cache is in a separate tier from your Looker instance, which leads to less load on the Looker instance.
  * **Scalability** — Use of a Redis cache also allows the cache to scale independently of your Looker instance.



## Requirements

Looker supports Redis versions 4.0.x, 5.0.x, and 7.2.x. To use a Redis cache with Looker, your Redis instance must meet the following requirements:

  * The Redis instance must be accessible from the Looker instance.
  * The Redis instance must not be a cluster. However, you can use a replica instance for high availability.
  * The size of the Redis cache should be approximately equal to the size of your Looker cache. By default, the Looker cache is 2 GB per node; so, if you have a three-node Looker cluster, a 6 GB Redis cache is recommended.
  * The Redis `maxmemory-policy` configuration should be set to `volatile-lru`.
  * You will need to disable any Redis authentication. All data stored in Redis is encrypted in the Looker instance before being sent to the Redis server.
  * You can use a Redis option that is hosted on an AWS ElastiCache or a Google Memorystore, as long as it's not a Redis cluster configuration.



In addition, Looker's [GCM encryption](https://docs.cloud.google.com/looker/docs/migrating-to-aes-256-gcm-encryption) system is required to use Redis in Looker. You must update encryption for instances that use legacy encryption prior to enabling Redis. If you attempt to enable Redis without GCM encryption, Looker will fail to start with an error message similar to the following:
    
    
    2020-01-23 10:28:44.253 -0800 [ERROR|007e4|cache] :: Must enable GCM encryption to use Redis caching
    

For instructions on upgrading from legacy encryption to GCM encryption, see the [Migrating to AES-256 GCM encryption](https://docs.cloud.google.com/looker/docs/migrating-to-aes-256-gcm-encryption) documentation page.

## Setting an environment variable to enable the Redis cache

To enable the Redis cache, you must set the `LOOKER_REDIS_CACHE_DISCOVERY` environment variable to point to the Redis connection URL and then do a complete restart of your Looker instance, including all nodes in the cluster. We recommend that you shut your server down completely, modify your environment and startup scripts as needed to include the environment variable, and then start all the nodes.

To shut down Looker, run the following commands on each node:
    
    
    cd looker
    ./looker stop
    

Then, for example, if you have a local Redis instance on the same host at the default port, set the `LOOKER_REDIS_CACHE_DISCOVERY` environment variable as follows:
    
    
    export LOOKER_REDIS_CACHE_DISCOVERY=redis://localhost:6379
    

Then restart Looker:
    
    
    ./looker start
    

## Verifying that the Redis cache is enabled

To determine if your Redis cache is enabled, look for entries in your [Looker log](https://docs.cloud.google.com/looker/docs/admin-panel-server-log). There should be log entries similar to the following:
    
    
    2021-06-11 16:54:41.532 +0000 [INFO|007e4|RedissonClientPool] :: Creating client for redis://localhost:6379/
    ...
    2021-06-11 16:54:42.802 +0000 [INFO|007e4|cache] :: Creating render_cache DataShelf: redis
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
