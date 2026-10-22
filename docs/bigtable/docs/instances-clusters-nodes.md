---
url: https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes/
title: Instances, clusters, and nodes \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:21.987516+00:00
---

# Instances, clusters, and nodes  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Instances, clusters, and nodes

To use Bigtable, you create _instances_ , which contain _clusters_ that your applications can connect to. Each cluster contains _nodes_ , the compute units that manage your data and perform maintenance tasks.

This page provides more information about Bigtable instances, clusters, and nodes.

  * To learn how to create an instance, see [Create an instance](https://docs.cloud.google.com/bigtable/docs/creating-instance).
  * To learn how to add or delete clusters, see [Modify an instance](https://docs.cloud.google.com/bigtable/docs/modifying-instance#clusters).
  * To learn how to monitor an instance and its clusters, see [Monitoring an instance](https://docs.cloud.google.com/bigtable/docs/monitoring-instance).
  * To learn how to update the number of nodes in a cluster, see [Add or remove nodes](https://docs.cloud.google.com/bigtable/docs/modifying-instance#nodes).



Before you read this page, you should be familiar with the [overview of Bigtable](https://docs.cloud.google.com/bigtable/docs/overview). 

## Instances

A Bigtable instance is a container for your data. Instances have one or more clusters, located in different zones. Each cluster has at least 1 node.

A table belongs to an instance, not to a cluster or node. If you have an instance with more than one cluster, you are using replication. This means you can't assign a table to an individual cluster or create unique garbage collection policies for each cluster in an instance. You also can't make each cluster store a different set of data in the same table.

An instance has a few important properties that you need to know about:

  * The _edition_ (Enterprise or Enterprise Plus)
  * The _storage type_ (SSD or HDD)
  * The _application profiles_ , which are primarily for instances that use replication



The following sections describe these properties.

### Editions

When you [create an instance](https://docs.cloud.google.com/bigtable/docs/creating-instance), you must choose an edition. The Enterprise edition is the established Bigtable service for demanding, multi-tenant workloads that require the highest levels of performance and global availability.

You can change an edition later to suit your evolving workloads. Changes to the edition of an instance take effect immediately. For more information, see [Editions overview](https://docs.cloud.google.com/bigtable/docs/editions-overview).

If you need sub-millisecond point-read latency, you can enable the integrated in-memory tier ([Preview](https://cloud.google.com/products#product-launch-stages)) for your cluster. The in-memory tier is available only with the Enterprise Plus edition. For more information, see [In-memory tier overview](https://docs.cloud.google.com/bigtable/docs/in-memory-overview).

### Storage types

When you create an instance, you must choose whether the instance's clusters will store data on solid-state drives (SSD) or hard disk drives (HDD). SSD is often, but not always, the most efficient and cost-effective choice.

The choice between SSD and HDD is permanent, and every cluster in your instance must use the same type of storage, so make sure you pick the right storage type for your use case. See [Choosing between SSD and HDD storage](https://docs.cloud.google.com/bigtable/docs/choosing-ssd-hdd) for more information to help you decide.

If you need to store historical data for reasons such as regulatory requirements, use Bigtable infrequent access storage as part of [tiered storage](https://docs.cloud.google.com/bigtable/docs/tiered-storage) ([Preview](https://cloud.google.com/products#product-launch-stages)). This option is available for SSD instances.

### Application profiles

After you [create an instance](https://docs.cloud.google.com/bigtable/docs/creating-instance), Bigtable uses the instance to store [application profiles](https://docs.cloud.google.com/bigtable/docs/app-profiles), or app profiles. For instances that use replication, app profiles control how your applications connect to the instance's clusters.

If your instance doesn't use replication, you can still use app profiles to provide separate identifiers for each of your applications, or each function within an application. You can then [view separate charts for each app profile in the Google Cloud console](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#console-monitoring-resources).

To learn more about app profiles, see [application profiles](https://docs.cloud.google.com/bigtable/docs/app-profiles). To learn how to set up your instance's app profiles, see [Configuring app profiles](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles).

## Clusters

A cluster represents the Bigtable service in a specific location. Each cluster belongs to a single Bigtable instance, and an instance can have clusters in up to 8 regions. When your application sends requests to a Bigtable instance, those requests are handled by one of the clusters in the instance.

Each cluster is located in a single zone. An instance can have clusters in up to 8 regions where Bigtable is available. Each [zone in a region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) can contain only one cluster. For example, if an instance has a cluster in `us-east1-b`, you can add a cluster in a different zone in the same region, such as `us-east1-c`, or a zone in a separate region, such as `europe-west2-a`. 

The number of clusters that you can create in an instance depends on the number of available zones in the regions that you choose. For example, if you create clusters in 8 regions that have 3 zones each, the maximum number of clusters that the instance can have is 24. For a list of zones and regions where Bigtable is available, see [Bigtable locations](https://docs.cloud.google.com/bigtable/docs/locations).

Bigtable instances that have only 1 cluster don't use replication. If you add a second cluster to an instance, Bigtable automatically starts replicating your data by keeping separate copies of the data in each of the clusters' zones and synchronizing updates between the copies. You can choose which cluster your applications connect to, which makes it possible to isolate different types of traffic from one another. You can also let Bigtable balance traffic between clusters. If a cluster becomes unavailable, you can fail over from one cluster to another. To learn more about how replication works, see the [replication overview](https://docs.cloud.google.com/bigtable/docs/replication-overview).

In most cases, you should [enable autoscaling](https://docs.cloud.google.com/bigtable/docs/autoscaling) for a cluster, so that Bigtable adds and removes nodes as needed to handle the cluster's workloads.

When you create a cluster, you can enable 2x node scaling, a configuration that sets the cluster to always scale in increments of two nodes. For more information, see [Node scaling factor](https://docs.cloud.google.com/bigtable/docs/scaling#node-scaling-factor).

## Nodes

Each cluster in an instance has 1 or more nodes, which are compute resources that Bigtable uses to manage your data.

The compute capacity and performance of a node depend on the instance edition. For more information, see [Understand performance](https://docs.cloud.google.com/bigtable/docs/performance).

Behind the scenes, Bigtable splits all of the data in a table into separate [_tablets_](https://docs.cloud.google.com/bigtable/docs/overview#architecture). Tablets are stored on disk, separate from the nodes but in the same zone as the nodes. A tablet is associated with a single node.

Each node is responsible for:

  * Keeping track of specific tablets on disk.
  * Handling incoming reads and writes for its tablets.
  * Performing maintenance tasks on its tablets, such as periodic [compactions](https://docs.cloud.google.com/bigtable/docs/overview#compactions).



A cluster must have enough nodes to support its current workload and the amount of data it stores. Otherwise, the cluster might not be able to handle incoming requests, and latency could go up. [Monitor your clusters' CPU and disk usage](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#cpu-and-disk), and [add nodes](https://docs.cloud.google.com/bigtable/docs/modifying-instance#nodes) to an instance when its metrics exceed the recommendations at [Plan your capacity](https://docs.cloud.google.com/bigtable/docs/performance#planning-your-capacity).

For more details about how Bigtable stores and manages data, see [Bigtable architecture](https://docs.cloud.google.com/bigtable/docs/overview#architecture).

For high-throughput read jobs, you can use Data Boost for Bigtable for compute instead of your cluster's nodes. Data Boost lets you send large read jobs and queries using serverless compute while your core application continues using cluster nodes for compute. For more information, see [Data Boost overview](https://docs.cloud.google.com/bigtable/docs/data-boost-overview).

For workloads of historical data that you don't need to access often, you can use the infrequent access tier in SSD instances.

### Nodes for replicated clusters

When your instance has more than one cluster, failover becomes a consideration when you configure the maximum number of nodes for autoscaling or manually allocate the nodes.

  * If you use [multi-cluster routing](https://docs.cloud.google.com/bigtable/docs/app-profiles#routing) in any of your app profiles, [automatic failover](https://docs.cloud.google.com/bigtable/docs/failovers#automatic) can occur in the event that one or more clusters is unavailable.

  * When you manually fail over from one cluster to another, or when automatic failover occurs, the receiving cluster should ideally have enough capacity to support the load. You can either always allocate enough nodes to support failover, which can be costly, or you can rely on autoscaling to add nodes when traffic fails over, but be aware that there might be a brief impact on performance while the cluster scales up.

  * If all of your app profiles use [single-cluster routing](https://docs.cloud.google.com/bigtable/docs/app-profiles#routing), each cluster can have a different number of nodes. Resize each cluster as needed based on the cluster's workload.

Because Bigtable stores a separate copy of your data with each cluster, each cluster must always have enough nodes to support your disk usage and to replicate writes between clusters.

You can still [fail over manually](https://docs.cloud.google.com/bigtable/docs/failovers#manual) from one cluster to another if necessary. However, if one cluster has many more nodes than another, and you need to fail over to the cluster with fewer nodes, you might need to [add nodes](https://docs.cloud.google.com/bigtable/docs/modifying-instance#nodes) first. There is no guarantee that additional nodes will be available when you need to fail over—the only way to reserve nodes in advance is to add them to your cluster.




## What's next

  * [Create a Bigtable instance.](https://docs.cloud.google.com/bigtable/docs/creating-instance)
  * [Monitor a Bigtable instance.](https://docs.cloud.google.com/bigtable/docs/monitoring-instance)
  * [Find out how replication works.](https://docs.cloud.google.com/bigtable/docs/replication-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
