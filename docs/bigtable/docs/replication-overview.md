---
url: https://docs.cloud.google.com/bigtable/docs/replication-overview/
title: Replication overview \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:06.599377+00:00
---

# Replication overview  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/replication-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Replication overview

Replication for Bigtable lets you increase the availability and durability of your data by copying it across multiple regions or multiple zones within the same region. You can also isolate workloads by routing different types of requests to different clusters.

This page explains how replication works in Bigtable and describes some common use cases for replication. It also explains the consistency model that Bigtable uses when replication is enabled and describes what happens when one cluster fails over to another.

  * For examples of settings you can use to implement common use cases, see [Examples of replication configurations](https://docs.cloud.google.com/bigtable/docs/replication-settings). 
  * To learn how to create an instance that uses replication, see [Create an instance](https://docs.cloud.google.com/bigtable/docs/creating-instance).
  * To learn how to enable replication for an existing instance, see [Add a cluster](https://docs.cloud.google.com/bigtable/docs/modifying-instance#clusters-adding).
  * To understand the costs associated with replication, see [Pricing](https://docs.cloud.google.com/bigtable/pricing).



Before you read this page, you should be familiar with the [overview of Bigtable](https://docs.cloud.google.com/bigtable/docs/overview). 

## How replication works

To use replication in a Bigtable instance, [create a new instance](https://docs.cloud.google.com/bigtable/docs/creating-instance) with more than one cluster or [add clusters](https://docs.cloud.google.com/bigtable/docs/modifying-instance#clusters-adding) to an existing instance.

Bigtable instances can have clusters located in up to 8 Bigtable regions, and in each of those 8 regions, the instance can contain only one cluster per zone. For example, if you create an instance in 8 regions that each have 3 zones, your instance can have up to 24 clusters.

Each [zone in a region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) can contain only one cluster. Having clusters in different zones or regions lets you access your instance's data even if one Google Cloud zone or region becomes unavailable.

When you create an instance with more than one cluster, Bigtable immediately starts to synchronize your data between the clusters, creating a separate, independent copy of your data in each zone where your instance has a cluster. Similarly, when you add a new cluster to an existing instance, Bigtable copies your existing data from the original cluster's zone to the new cluster's zone, then synchronizes changes to your data between the zones.

Bigtable replicates any changes to your data, including all of the following types of changes:

  * Updates to the data in existing tables
  * New and deleted tables
  * Added and removed column families
  * Changes to a column family's garbage collection policy



Replication has some latency, and consistency between clusters is eventual.

Bigtable treats each cluster in your instance as a primary cluster, so you can perform reads and writes in each cluster. You can also set up your instance so that requests from different types of applications are routed to different clusters.

Before you add clusters to an instance, you should be aware of the restrictions that apply when you change [garbage collection policies](https://docs.cloud.google.com/bigtable/docs/garbage-collection#replication) for replicated tables.

## Performance

Using replication has performance implications that you should plan for when you create a replicated instance or enable replication by adding a cluster to a single-cluster instance. For example, replicated clusters in different regions typically have higher replication latency than replicated clusters in the same region. Additionally, clusters in instances that have more than one cluster often need more nodes to handle the added work of handling replication. To learn more, see [Understand performance](https://docs.cloud.google.com/bigtable/docs/performance).

## Use cases

This section describes some common use cases for Bigtable replication. To find the best configuration settings for each use case, as well as implementation tips for other use cases, see [Examples of Replication Settings](https://docs.cloud.google.com/bigtable/docs/replication-settings).

### Isolate serving applications from batch reads

When you use a single cluster to run a batch analytics job that performs numerous large reads alongside an application that performs a mix of reads and writes, the large batch job can slow things down for the application's users. With replication, you can use app profiles with single-cluster routing to route batch analytics jobs and application traffic to different clusters, so that batch jobs don't affect your applications' users. [Learn more about implementing this use case](https://docs.cloud.google.com/bigtable/docs/replication-settings#batch-vs-serve-details).

### Improve availability

If an instance has only one cluster, your data's durability and availability are limited to the zone where that cluster is located. Replication can improve both durability and availability by storing separate copies of your data in multiple [zones or regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) and automatically failing over between clusters if needed. [Learn more about implementing this use case](https://docs.cloud.google.com/bigtable/docs/replication-settings#high-availability-details).

### Provide near-real-time backup

In some cases—for example, if you can't afford to read stale data—you'll always need to route requests to a single cluster. However, you can still use replication by handling requests with one cluster and keeping another cluster as a near-real-time backup. If the serving cluster becomes unavailable, you can minimize downtime by manually failing over to the backup cluster. [Learn more about implementing this use case](https://docs.cloud.google.com/bigtable/docs/replication-settings#backup-details).

### Ensure your data has a global presence

You can set up replication in locations across the world to put your data closer to your customers. For example, you can create an instance with replicated clusters in the US, Europe, and Asia and set up app profiles to route application traffic to the nearest cluster. [Learn more about implementing this use case](https://docs.cloud.google.com/bigtable/docs/replication-settings).

## Consistency models

This section explains the consistency models that Bigtable can provide for replication, depending on the routing policy that you use.

### Eventual consistency

By default, replication for Bigtable is [eventually consistent](https://en.wikipedia.org/wiki/Eventual_consistency). This term means that when you write a change to one cluster, you can eventually read that change from the other clusters in the instance, but only after the change is replicated among the clusters.

**Note:** When using replication, reads and writes to the same cluster are consistent. Reads and writes to different clusters are eventually consistent. If an instance doesn't use replication, Bigtable provides [strong consistency](https://en.wikipedia.org/wiki/Strong_consistency) because it sends all reads and writes to the same cluster.

If your instance is responsive, the latency for replication is typically a few seconds or minutes, not hours. However, if you're writing a large amount of data to a cluster, or if a cluster is overloaded or temporarily unavailable, it can take time for replication to catch up. Also, replication can take more time if your clusters are far apart. As a result, it's not normally safe to assume that you're always reading the latest value that was written, or that waiting a few seconds after a write gives Bigtable enough time to replicate the change.

### Read-your-writes consistency

You can achieve read-your-writes consistency with single-cluster routing, and you can attain a high rate of read-your-writes consistency by using multi-cluster routing with row-affinity routing or when your instance's clusters are each in a different region.

#### Single-cluster routing

If you use [single-cluster routing](https://docs.cloud.google.com/bigtable/docs/app-profiles#routing), Bigtable can provide [read-your-writes consistency](https://en.wikipedia.org/wiki/Consistency_model#Read-your-writes_consistency) when replication is enabled. This consistency model ensures that an application never reads data that is older than its most recent writes.

Each app profile that you use must be configured for single-cluster routing, and all of the app profiles must route requests to the same cluster. You can use the instance's additional clusters at the same time for other purposes.

### Multi-cluster routing with one cluster per region

With multi-cluster routing, Bigtable always routes requests to the nearest cluster. If each cluster in your instance is in different Bigtable region, and you use an app profile configured for multi-cluster routing, then your data has read-your-writes consistency within the source region unless failover occurs.

### Row-affinity routing

To achieve a higher rate of read-your-writes consistency with multi-cluster routing to an instance that has more than one cluster in a region, you can use an app profile configured for [row-affinity routing (sticky routing)](https://docs.cloud.google.com/bigtable/docs/app-profiles#row-affinity).

With row-affinity routing, Bigtable automatically routes your single-row read and write requests to a specific cluster based on the row key of the request. You can't manually set the mapping between the row key and the cluster. The consistency isn't guaranteed because requests might still fail over for various reasons, including when a cluster is unhealthy, network issues are present, or the cluster has received too many requests.

### Strong consistency

For some replication use cases, Bigtable can also provide [strong consistency](https://en.wikipedia.org/wiki/Strong_consistency), which ensures that all of your applications see your data in the same state. To gain strong consistency, you use the [single-cluster routing](https://docs.cloud.google.com/bigtable/docs/app-profiles#routing) app-profile configuration for read-your-writes consistency that is described earlier, but you _must not_ use the instance's additional clusters unless you need to fail over to a different cluster. Review the [examples of replication settings](https://docs.cloud.google.com/bigtable/docs/replication-settings) to see if this is possible for your use case.

**Note** : Bigtable reverts to eventual consistency after a failover. If you fail over to a cluster, and there are writes that have not been replicated to that cluster, some reads will return stale data until replication is complete.

## Conflict resolution

Each cell value in a Bigtable table is uniquely identified by the four-tuple (row key, column family, column qualifier, timestamp). See [Bigtable storage model](https://docs.cloud.google.com/bigtable/docs/overview#storage-model) for more details on these identifiers. In the event that two writes with the exact same four-tuple are sent to two different clusters, Bigtable automatically resolves the conflict using an internal _last write wins_ algorithm based on the server-side time. The Bigtable "last write wins" implementation is deterministic, and when replication catches up, all clusters have the same value for the four-tuple. 

## Application profiles

If an instance uses replication, you use application profiles, or _app profiles_ , to specify routing policies. App profiles also determine whether you can perform single-row transactions, which include read-modify-write operations (including increments and appends) and check-and-mutate operations (also known as conditional mutations or conditional writes).

For details, see [Application Profiles](https://docs.cloud.google.com/bigtable/docs/app-profiles). For examples of settings you can use to implement common use cases, see [Examples of replication configurations](https://docs.cloud.google.com/bigtable/docs/replication-settings). 

## Routing policies

Every app profile has a _routing policy_ that controls which clusters handle incoming requests from your applications. Options for routing policies include the following:

  * **Single-cluster routing** : Sends all requests to a single cluster that you specify.
  * **Multi-cluster routing** : 
    * **Any cluster routing** : Sends requests to the nearest cluster in the instance.
    * **Cluster group routing** : Restricts all requests to clusters that you specify.
    * **Row-affinity routing** : Sends a single-row read or write request to a specific cluster based on the row key of the request. For more information, see [Row-affinity routing](https://docs.cloud.google.com/bigtable/docs/app-profiles#row-affinity).



## Failovers

If a Bigtable cluster becomes unresponsive, replication makes it possible for incoming traffic to fail over to another cluster in the same instance. Failovers can be either manual or automatic, depending on the [app profile](https://docs.cloud.google.com/bigtable/docs/app-profiles) an application is using and how the app profile is configured. For details, see [Failovers](https://docs.cloud.google.com/bigtable/docs/failovers).

## Dropping row ranges when replication is enabled

The Cloud Bigtable Admin API lets you to [drop a contiguous range of rows](https://docs.cloud.google.com/bigtable/docs/reference/admin/rpc/google.bigtable.admin.v2#google.bigtable.admin.v2.BigtableTableAdmin.DropRowRange) from a table based on their row keys. In instances that don't use replication, Bigtable can drop a row range quickly and efficiently. However, when replication is enabled, dropping a row range is significantly slower and much less efficient.

**Important:** If possible, avoid dropping a row range in an instance that uses replication. If you must drop a row range, be aware that it might take a very long time for Bigtable to complete the operation, and CPU usage will increase during the operation.

## What's next

  * [Find the right replication settings for your use case](https://docs.cloud.google.com/bigtable/docs/replication-settings).
  * [Create an instance that uses replication](https://docs.cloud.google.com/bigtable/docs/creating-instance).
  * [Enable replication for an existing instance](https://docs.cloud.google.com/bigtable/docs/modifying-instance#clusters-adding).
  * [Learn about the replication settings in app profiles](https://docs.cloud.google.com/bigtable/docs/app-profiles).
  * [Find out how to complete a manual failover](https://docs.cloud.google.com/bigtable/docs/managing-failovers#manual).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
