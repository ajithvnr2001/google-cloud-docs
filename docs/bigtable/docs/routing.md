---
url: https://docs.cloud.google.com/bigtable/docs/routing/
title: Routing options \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:06.105113+00:00
---

# Routing options  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/routing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Routing options

**Note:** This page includes features that are available only in the Enterprise Plus edition. For more information, see [Editions overview](https://docs.cloud.google.com/bigtable/docs/editions-overview).

When you send requests from an application to Bigtable, you use an [app profile](https://docs.cloud.google.com/bigtable/docs/app-profiles) that tells Bigtable how to handle the requests. An app profile specifies the _routing policy_ for the requests. For instances that use replication, the routing policy controls which clusters receive the requests and how failovers are handled.

This document describes the routing policies that are available for a standard app profile.

Routing policies are especially important for [workload isolation](https://docs.cloud.google.com/bigtable/docs/app-profiles#workload-isolation) use cases, when you're not able to use [Data Boost](https://docs.cloud.google.com/bigtable/docs/data-boost-overview). You can configure them in conjunction with [request priorities](https://docs.cloud.google.com/bigtable/docs/request-priorities).

Routing policies don't affect replication, but you should be familiar with how [Bigtable replication](https://docs.cloud.google.com/bigtable/docs/replication-overview) works before you read this page. You should also read [Failovers](https://docs.cloud.google.com/bigtable/docs/failovers).

## Single-cluster routing

A single-cluster routing policy routes all requests to one cluster in your instance. If that cluster becomes unavailable, you must manually fail over to another cluster. Data Boost and in-memory tier ([Preview](https://cloud.google.com/products#product-launch-stages)) app profiles use single-cluster routing.

This is the only routing policy that lets you enable single-row transactions.

A replicated instance normally provides [eventual consistency](https://docs.cloud.google.com/bigtable/docs/replication-overview#consistency-model). However, you can achieve [read-your-writes consistency](https://en.wikipedia.org/wiki/Consistency_model#Read-your-writes_consistency) for a workload in a replicated instance if you configure an app profile for that workload to use single-cluster routing to send read and write requests to the same cluster. You can route traffic for additional workloads on the replicated instance to other clusters in the instance depending on your workload requirements.

## Multi-cluster routing

A multi-cluster routing policy routes requests that you send to an instance to the nearest region that the instance has a cluster in. If the cluster becomes unavailable, traffic automatically fails over to the nearest cluster that is available. The speed of an automatic failover depends on your request deadline. For more information, see [Automatic failovers](https://docs.cloud.google.com/bigtable/docs/failovers#automatic).

This configuration provides eventual consistency. You can't enable single-row transactions with multi-cluster routing, because single-row transactions can cause [data conflicts](https://docs.cloud.google.com/bigtable/docs/app-profiles#single-row-conflicts) when you use multi-cluster routing. For details, see [Single-row transactions](https://docs.cloud.google.com/bigtable/docs/app-profiles#single-row-transactions).

Use multi-cluster routing if you want high availability (HA). For recommended instance configurations and further details, see [Create high availability (HA)](https://docs.cloud.google.com/bigtable/docs/replication-settings#high-availability).

When you use multi-cluster routing, you can route requests to _any cluster_ in the instance or to a _cluster group_ that you define. If your workload consists mostly of single-row operations and you want to achieve a higher rate of read-your-writes consistency, you can enable _row-affinity routing_.

For more information about SQL-related routing considerations, see the Routing with SQL section of this document.

### Any cluster routing

Any cluster routing makes every cluster in the instance available to receive requests and for failover.

### Cluster group routing

If you want to exclude one or more of an instance's clusters from possible failover, you can use cluster group routing. This form of multi-cluster routing lets you specify a subset of clusters that an app profile can send traffic to. This can be helpful if you want to reserve a cluster for a separate workload.

### Row-affinity routing

Row-affinity routing automatically routes single-row read and write requests to a specific cluster based on the row key of the request.

You enable row-affinity routing by using the gcloud CLI, the Google Cloud console, the Bigtable client library for Java, or Terraform. For more information, see [Create an app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles).

If you want multi-cluster routing to achieve a higher rate of read-your-writes consistency, and most of your requests are single-row operations, you can use row-affinity routing (sticky routing). Bigtable uses the row key of the request to automatically determine which cluster to route the request to. You can't manually set the mapping between the row key and the cluster.

**Important:** With row-affinity routing, read-your-writes consistency is not guaranteed because requests can fail over for various reasons, including when a cluster is unavailable, network issues are present, or the cluster has received too many requests.

Row-affinity routing can be used only for single-row read or write requests. This includes requests that call `ReadRows` with one key specified, `MutateRow`, and `MutateRows` with one key specified, and `BulkMutateRow` with one key specified.

**Note:** Specifying a row range of one row in a `ReadRows` operation is not supported. In addition, specifying multiple updates to the same row in a `BulkMutateRow` operation is also not supported.

Read-your-writes consistency is not fully achieved with row-affinity routing in the following cases:

  * **Adding a cluster to the instance** : Row-affinity routing determines which cluster to route to based on the row key. If a new cluster is added or removed to the instance while row-affinity routing is enabled, the row key assignment might change. To ensure that cluster failover order remains the same despite changes to the instance's cluster list, we recommend using cluster groups by setting the `--restrict-to` flag.

With cluster groups, you cannot delete a cluster in an instance while it is in use by an app profile. Additionally, any new cluster added to the instance doesn't start receiving requests unless it is explicitly added to the app profile's cluster group.

  * **Failover** : If a cluster is unavailable or unhealthy, requests to the impacted cluster are directed to the next cluster according to the failover order. This rerouting can impact consistency.




For more information about failovers, see [Failovers](https://docs.cloud.google.com/bigtable/docs/failovers). To learn how to complete a failover, see [Managing failovers](https://docs.cloud.google.com/bigtable/docs/managing-failovers). 

## Routing with SQL

When you use SQL to query Bigtable, there are special considerations for how your requests are routed. The routing behavior for SQL queries differs from other types of Bigtable requests. Row-affinity routing directs single-row reads and writes automatically to a specific cluster based on the row key. Bigtable doesn't support this routing policy for SQL queries. This limitation means that you can't use row-affinity routing with the `ExecuteQuery` method, even if the query is designed to read a single row. If you send an `ExecuteQuery` request using an app profile with the `--row-affinity` flag enabled, the request succeeds, but row affinity isn't enforced.

## Single-row transactions

In Bigtable mutations, such as read, write, and delete requests, are always atomic at the row level. This includes mutations to multiple columns in a single row, as long as they are included in the same [mutation operation](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#mutaterowrequest). Bigtable doesn't support transactions that atomically update more than one row.

However, Bigtable supports some write operations that would require a transaction in other databases. In effect, Bigtable uses _single-row transactions_ to complete these operations. These operations include reads and writes, and all of the reads and writes are executed atomically, but the operations are still atomic only at the row level:

  * **Read-modify-write operations** , including [increments and appends](https://docs.cloud.google.com/bigtable/docs/writes#increments). A read-modify-write operation reads an existing value; increments or appends to the existing value; and writes the updated value to the table.
  * **Check-and-mutate operations** , also known as conditional mutations or [conditional writes](https://docs.cloud.google.com/bigtable/docs/writes#conditional). In a check-and-mutate operation, Bigtable checks a row to see if it meets a specified condition. If the condition is met, Bigtable writes new values to the row.

**Important:** If you enable single-row transactions in multiple app profiles, make sure that you don't send conflicting writes to different clusters, which could result in data loss.

### Conflicts between single-row transactions

Every cluster in a Bigtable instance is a primary cluster that accepts both reads and writes. As a result, **operations that require single-row transactions can cause problems in replicated instances.**

If your use case allows it, you can avoid these conflicts by using aggregates. When you send an add request to an aggregate field, the new value is merged with the existing value. Aggregates let you keep a running sum or counter. For more information, see [Aggregate values at write time](https://docs.cloud.google.com/bigtable/docs/aggregates).

To illustrate the problem that can arise when you don't use aggregates, suppose you have a table that you use to store data for a ticketing system. You use an integer counter to store the number of tickets that have been sold. Each time you sell a ticket, your app sends a [read-modify-write](https://docs.cloud.google.com/bigtable/docs/writes#increments) operation to increment the counter by 1.

If your instance has one cluster, client apps can sell tickets at the same time and increment the counters without data loss because the requests are handled atomically in the order they are received by that single cluster.

On the other hand, if your instance has multiple clusters and your app profile were to allow multi-cluster routing, simultaneous requests to increment the counter might each be sent to different clusters, then replicated to the other clusters in the instance. If you send two increment requests at the same time that are routed to different clusters, each finishes its transaction without "knowing" about the other. The counter on each cluster is incremented by one. When the data is replicated to the other cluster, Bigtable can't possibly know that you meant to increment by 2.

To help you avoid unintended results, Bigtable does the following:

  * Requires each app profile to specify whether it allows single-row transactions.
  * Prevents you from enabling single-row transactions in an app profile that uses multi-cluster routing, because there's no safe way to enable both of these features at once.
  * Warns you if you enable single-row transactions in two or more different app profiles that use single-cluster routing and point to different clusters. If you choose to create this type of configuration, you must ensure that you don't send conflicting read-modify-write or check-and-mutate requests to different clusters.



## What's next

  * [Review examples of replication settings.](https://docs.cloud.google.com/bigtable/docs/replication-settings)
  * [Learn how to manage failovers.](https://docs.cloud.google.com/bigtable/docs/managing-failovers)
  * [Change an app profile's routing policy.](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles)
  * [Review the criteria for direct connectivity.](https://docs.cloud.google.com/bigtable/docs/performance#direct-connectivity)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
