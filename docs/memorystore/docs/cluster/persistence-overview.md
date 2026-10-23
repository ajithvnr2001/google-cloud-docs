---
url: https://docs.cloud.google.com/memorystore/docs/cluster/persistence-overview/
title: Persistence overview \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:57.790075+00:00
---

# Persistence overview  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/persistence-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Persistence overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of persistence for Memorystore for Redis Cluster.

Memorystore for Redis Cluster supports two types of persistence:

  * [AOF persistence](https://docs.cloud.google.com/memorystore/docs/cluster/about-aof-persistence)
  * [RDB persistence](https://docs.cloud.google.com/memorystore/docs/cluster/about-rdb-persistence)

**Note:** You can either enable AOF or RDB persistence for your instance, not both.

For the best instance availability and data durability, we recommend enabling both persistence and [high availability](https://docs.cloud.google.com/memorystore/docs/cluster/ha-and-replicas). While persistence and high availability overlap in the protection they offer, they have different strengths that complement each other. HA can be considered the first line of defense against individual node failures and zonal outages. Persistence provides disaster recovery for rare events when all nodes in a shard fail and HA is unable to help.

## Choosing a persistence type

Choosing between AOF and RDB persistence comes down to a choice between performance and data durability. These tradeoffs are generally true of all managed Redis services because of the nature of AOF and RDB persistence in OSS Redis.

If your top priority is data durability and preserving the highest percentage of writes sent to your Redis server, we recommend choosing AOF persistence. AOF's ability to persist data every second (or for every write) offers superior data durability compared to RDB snapshots which save data on an hourly basis.

If performance is your top priority, we recommend using RDB persistence because it usually places lower performance demands on your instance than AOF persistence does for a similarly sized instance. If you are comfortable with some staleness in your data on recovery and you want the performance that RDB persistence provides for a similarly sized instance, then RDB persistence is the better choice for you.

It is possible to have both high throughput with the durability of AOF persistence. To get both you can enable AOF persistence and also choose a high shard count. A high shard count provides more vCPUs which improves performance. However, some latency increase is expected for AOF in any configuration.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
