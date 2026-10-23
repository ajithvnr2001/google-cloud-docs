---
url: https://docs.cloud.google.com/memorystore/docs/cluster/about-aof-persistence/
title: About AOF persistence \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:47:01.427041+00:00
---

# About AOF persistence  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/about-aof-persistence/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  About AOF persistence Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of Append-Only File (AOF) persistence for Memorystore for Redis Cluster.

Memorystore for Redis Cluster also supports Redis Database (RDB) persistence. You must choose either AOF or RDB persistence because you can't enable both persistence modes at the same time. For more information about choosing between the two modes, see [Persistence overview](https://docs.cloud.google.com/memorystore/docs/cluster/persistence-overview).

To ensure that your cluster remains resilient during maintenance or unexpected failures, we recommend using a highly available cluster in addition to enabling AOF persistence. For more information, see [High availability and replicas](https://docs.cloud.google.com/memorystore/docs/cluster/ha-and-replicas).

## AOF persistence overview

AOF persistence prioritizes data durability. It stores data by recording every write command to a log file called the AOF file. If a system failure or restart occurs, then the server replays AOF file commands sequentially to restore your data. Unlike RDB persistence, you can't pause AOF persistence.

If you enable or disable AOF persistence for a cluster, then you might need to perform maintenance on the cluster.

To learn how to enable and disable AOF persistence, see [Manage persistence](https://docs.cloud.google.com/memorystore/docs/cluster/manage-persistence).

### Sync setting

The sync setting for AOF persistence (`appendfsync`) determines how often Memorystore for Redis Cluster saves in-memory cached data to durable storage. We recommend keeping the sync setting at 1 second, which is the default. Syncing every second provides the best compromise between the cluster's performance and the data's durability.

Before Memorystore for Redis Cluster saves AOF logs to durable storage, it stores them in memory. If a system failure or restart occurs during this time, then Memorystore for Redis Cluster might lose these in-memory writes. The sync setting lets you choose how often Memorystore for Redis Cluster saves data to durable storage and provides the following options:

  * `always`: saves data to storage for every write
  * `everysec`: saves data to storage every second
  * `no`: Memorystore for Redis Cluster flushes data to storage on its own schedule, which typically happens every 30 seconds.



Syncing for every write (`always`) provides the best data durability. However, this comes with a performance tradeoff. We recommend syncing every second (`everysec`), which provides a good balance between data durability and cluster performance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
