---
url: https://docs.cloud.google.com/bigtable/docs/replication-settings/
title: Examples of replication configurations \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:13.939345+00:00
---

# Examples of replication configurations  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/replication-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Examples of replication configurations

This page describes some common use cases for Bigtable replication and presents the settings that you can use to support these use cases.

  * Isolate batch analytics workloads from other applications
  * Create high availability (HA)
  * Provide near-real-time backup
  * Maintain high availability and regional resilience
  * Store data close to your users



This page also explains how to decide what settings to use for other use cases.

Before you read this page, you should be familiar with the [overview of Bigtable replication](https://docs.cloud.google.com/bigtable/docs/replication-overview). 

Before you add clusters to an instance, you should be aware of the restrictions that apply when you change [garbage collection policies](https://docs.cloud.google.com/bigtable/docs/garbage-collection#changes) on replicated tables.

In most cases, [enable autoscaling](https://docs.cloud.google.com/bigtable/docs/autoscaling) for your instance's clusters. Autoscaling lets Bigtable automatically add and remove nodes to a cluster based on workload.

If you choose manual node allocation instead, provision enough nodes in _every cluster in an instance_ to ensure that each cluster can handle replication in addition to the load it receives from applications. If a cluster does not have enough nodes, replication delay can increase, the cluster can experience performance issues due to memory buildup, and writes to other clusters in the instance might be rejected.

Examples in this document describe creating an instance, but you can also add clusters to an existing instance.

## Isolate batch analytics workloads from other applications

When you use a single cluster to run a batch analytics job that performs numerous large reads alongside an application that performs a mix of reads and writes, the large batch job can slow things down for the application's users. With replication, you can use app profiles with single-cluster routing to route batch analytics jobs and application traffic to different clusters, so that batch jobs don't affect your applications' users. 

**To isolate two workloads:**

  1. Create an instance with two clusters.

  2. [Create two app profiles](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#creating-app-profile), one called `live-traffic` and another called `batch-analytics`.

If your cluster IDs are `cluster-a` and `cluster-b`, the `live-traffic` app profile should route requests to `cluster-a` and the `batch-analytics` app profile should route requests to `cluster-b`. This configuration provides [read-your-writes consistency](https://docs.cloud.google.com/bigtable/docs/replication-overview#consistency-model) for applications using the same app profile, but not for applications using different app profiles.

You can enable [single-row transactions](https://docs.cloud.google.com/bigtable/docs/app-profiles#single-row-transactions) in the `live-traffic` app profile if necessary. There's no need to enable single-row transactions in the `batch-analytics` app profile, assuming that you will only use this app profile for reads.

  3. Use the `live-traffic` app profile to run a live-traffic workload.

  4. While the live-traffic workload is running, use the `batch-analytics` app profile to run a read-only batch workload.




**To isolate two smaller workloads from one larger workload:**

  1. Create an instance with three clusters.

These steps assume that your clusters use the IDs `cluster-a`, `cluster-b`, and `cluster-c`.

  2. Create the following app profiles:

     * `live-traffic-app-a`: Single-cluster routing from your application to `cluster-a`
     * `live-traffic-app-b`: Single-cluster routing from your application to `cluster-b`
     * `batch-analytics`: Single-cluster routing from the batch analytics job to `cluster-c`
  3. Use the live-traffic app profiles to run live-traffic workloads.

  4. While the live-traffic workloads are running, use the `batch-analytics` app profile to run a read-only batch workload.




## Create high availability (HA)

If an instance has only one cluster, your data's durability and availability are limited to the zone where that cluster is located. Replication can improve both durability and availability by storing separate copies of your data in multiple [zones or regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) and automatically failing over between clusters if needed. 

To configure your instance for a high availability (HA) use case, [create a new app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#creating-app-profile) that uses multi-cluster routing, or [update the default app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#updating-app-profile) to use multi-cluster routing. This configuration provides [eventual consistency](https://docs.cloud.google.com/bigtable/docs/replication-overview#consistency-model). You won't be able to enable [single-row transactions](https://docs.cloud.google.com/bigtable/docs/app-profiles#single-row-transactions) because single-row transactions can cause [data conflicts](https://docs.cloud.google.com/bigtable/docs/app-profiles#single-row-conflicts) when you use multi-cluster routing.

**Important:** To ensure high availability during a regional failure, locate your client in or near **more than one** of the Google Cloud regions where your Bigtable clusters are. This strategy ensures that you are able to send and receive data to and from Bigtable even if a region that your client or application is in or near experiences a failure. This recommendation applies even if Google Cloud does not host your application, because your data enters the Google Cloud network through the Google Cloud region that is closest to your application server.

Configurations to improve availability include the following.

  * **Clusters in three or more different regions (_recommended configuration_).** The recommended configuration for HA is an instance that has _N+2_ clusters that are each in a different region. For example, if the minimum number of clusters that you need to serve your data is 2, then you need an instance with four clusters to maintain HA. This configuration provides uptime even in the rare case that two regions become unavailable. We recommend that you spread the clusters across multiple continents.

Example configuration: 

    * `cluster-a` in zone `us-central1-a` in Iowa
    * `cluster-b` in zone `europe-west1-d` in Belgium
    * `cluster-c` in zone `asia-east1-b` in Taiwan
  * **Two clusters in the same region but different zones.** This option provides high availability within the region's availability, the ability to fail over without generating cross-region replication costs, and no increased latency on failover. Your data in a replicated Bigtable instance is available as long as any of the zones it is replicated to are available.

For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

Example configuration: 

    * `cluster-a` in zone `australia-southeast1-a` in Sydney
    * `cluster-b` in zone `australia-southeast1-b` in Sydney
  * **Two clusters in different regions.** This multi-region configuration provides high availability like the preceding multi-zone configuration, but your data is available even if you cannot connect to one of the regions.

You are charged for [replicating writes between regions](https://docs.cloud.google.com/bigtable/pricing#replication-ongoing).

Example configuration: 

    * `cluster-a` in zone `asia-northeast1-c` in Tokyo
    * `cluster-b` in zone `asia-east2-b` in Hong Kong
  * **Two clusters in region A and a third cluster in region B.** This option makes your data available even if you cannot connect to one of the regions, and it provides additional capacity in region A.

You are charged for [replicating writes between regions](https://docs.cloud.google.com/bigtable/pricing#replication-ongoing). If you write to region A, you are charged once because you have only one cluster in region B. If you write to region B, you are charged twice because you have two clusters in region A.

Example configuration: 

    * `cluster-a` in zone `europe-west1-b` in Belgium
    * `cluster-b` in zone `europe-west1-d` in Belgium
    * `cluster-c` in zone `europe-north1-c` in Finland



## Provide near-real-time backup

In some cases—for example, if you can't afford to read stale data—you'll always need to route requests to a single cluster. However, you can still use replication by handling requests with one cluster and keeping another cluster as a near-real-time backup. If the serving cluster becomes unavailable, you can minimize downtime by manually failing over to the backup cluster. 

To configure your instance for this use case, [create an app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#creating-app-profile) that uses single-cluster routing or [update the default app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#updating-app-profile) to use single-cluster routing. The cluster that you specified in your app profile handles incoming requests. The other cluster acts as a backup in case you need to fail over. This arrangement is sometimes known as an active-passive configuration, and it provides both [strong consistency and read-your-writes consistency](https://docs.cloud.google.com/bigtable/docs/replication-overview#consistency-model). You can enable [single-row transactions](https://docs.cloud.google.com/bigtable/docs/app-profiles#single-row-transactions) in the app profile if necessary.

To implement this configuration:

  1. Use an app profile with single-cluster routing to run a workload.

  2. Use the Google Cloud console to [monitor the instance's clusters](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#console-overview) and confirm that only one cluster is handling incoming requests.

The other cluster will still use CPU resources to perform replication and other maintenance tasks.

  3. [Update the app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#updating-app-profile) so that it points to the second cluster in your instance.

You receive a warning about losing [read-your-writes consistency](https://docs.cloud.google.com/bigtable/docs/replication-overview#consistency-model), which also means that you lose strong consistency.

If you enabled single-row transactions, you also receive a warning about the potential for data loss. You lose data if you send [conflicting writes](https://docs.cloud.google.com/bigtable/docs/app-profiles#single-row-conflicts) while the failover is occurring.

  4. Continue to monitor your instance. You should see that the second cluster is handling incoming requests.




## Maintain high availability and regional resilience

Let's say you have concentrations of customers in two distinct regions within a continent. You want to serve each concentration of customers with Bigtable clusters as close to the customers as possible. You want your data to be highly available within each region, and you might want a failover option if one or more of your clusters is not available.

For this use case, you can create an instance with two clusters in region A and two clusters in region B. This configuration provides high availability even if you cannot connect to a Google Cloud region. It also provides regional resilience because even if a zone becomes unavailable, the other cluster in that zone's region is still available.

You can choose to use multi-cluster routing or single-cluster routing for this use case, depending on your business needs.

To configure your instance for this use case:

  1. Create a Bigtable instance with four clusters: two in region A and two in region B. Clusters in the same region must be in different zones.

Example configuration: 

     * `cluster-a` in zone `asia-south1-a` in Mumbai
     * `cluster-b` in zone `asia-south1-c` in Mumbai
     * `cluster-c` in zone `asia-northeast1-a` in Tokyo
     * `cluster-d` in zone `asia-northeast1-b` in Tokyo
  2. Place an application server near each region.




You can choose to use multi-cluster routing or single-cluster routing for this use case, depending on your business needs. If you use multi-cluster routing, Bigtable handles failovers automatically. If you use single-cluster routing, you use your own judgment to decide when to fail over to a different cluster.

### Single-cluster routing option

You can use single-cluster routing for this use case if you don't want your Bigtable cluster to automatically fail over if a zone or region becomes unavailable. This option is a good choice if you want to manage the costs and latency that might occur if Bigtable starts routing traffic to and from a distant region, or if you prefer to make failover decisions based on your own judgment or business rules.

To implement this configuration, [create at least one app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#creating-app-profile) that uses single-cluster routing for each application that sends requests to the instance. You can route the app profiles to any cluster in the Bigtable instance. For example, if you have three applications running in Mumbai and six in Tokyo, you can configure one app profile for the Mumbai application to route to `asia-south1-a` and two that route to `asia-south1-c`. For the Tokyo application, configure three app profiles that route to `asia-northeast1-a` and three that route to `asia-northeast1-b`.

**Note:** Multiple app profiles can route to the same cluster, and an instance can have clusters that no app profiles route requests to.

With this configuration, if one or more clusters become unavailable, you can [perform a manual failover](https://docs.cloud.google.com/bigtable/docs/failovers#manual) or choose to let your data be temporarily unavailable in that zone until the zone is available again.

### Multi-cluster routing option

If you're implementing this use case and you want Bigtable to automatically fail over to one region if your application cannot reach the other region, use [multi-cluster routing](https://docs.cloud.google.com/bigtable/docs/app-profiles#routing).

To implement this configuration, [create a new app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#creating-app-profile) that uses multi-cluster routing for each application, or [update the default app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#updating-app-profile) to use multi-cluster routing.

This configuration provides [eventual consistency](https://docs.cloud.google.com/bigtable/docs/replication-overview#consistency-model). If a region becomes unavailable, Bigtable requests are automatically sent to the other region. When this happens, you are [charged for the network traffic](https://docs.cloud.google.com/bigtable/pricing#network) to the other region, and your application might experience higher latency because of the greater distance.

## Store data close to your users

If you have users around the globe, you can reduce latency by running your application near your users and putting your data as close to your application as possible. With Bigtable, you can create an instance that has clusters in several Google Cloud regions, and your data is automatically replicated in each region.

For this use case, use app profiles with single-cluster routing. Multi-cluster routing is undesirable for this use case because of the distance between clusters. If a cluster becomes unavailable and its multi-cluster app profile automatically reroutes traffic across a great distance, your application might experience unacceptable latency and incur unexpected, additional network costs.

To configure your instance for this use case:

  1. Create an instance with clusters in three distinct geographic regions, such as the United States, Europe, and Asia.

  2. Place an application server near each region.

  3. Create app profiles similar to the following:

     * `clickstream-us`: Single-cluster routing to the cluster in the United States
     * `clickstream-eu`: Single-cluster routing to the cluster in Europe
     * `clickstream-asia`: Single-cluster routing to the cluster in Asia



In this setup, your application uses the app profile for the closest cluster. Writes to any cluster are automatically replicated to the other two clusters.

## Other use cases

If you have a use case that isn't described on this page, use the following questions to help you decide how to configure your app profiles:

  * **Do you need to perform[single-row transactions](https://docs.cloud.google.com/bigtable/docs/app-profiles#single-row-transactions),** such as read-modify-write operations (including increments and appends) and check-and-mutate operations (also known as conditional mutations or conditional writes)?

If so, your app profiles must use [single-cluster routing](https://docs.cloud.google.com/bigtable/docs/app-profiles#routing) to prevent data loss, and you must [handle failovers manually](https://docs.cloud.google.com/bigtable/docs/failovers#manual).

**Important:** If you have additional app profiles that point to other clusters, it's best to disable single-row transactions in the additional app profiles. If you enable single-row transactions in multiple app profiles, you must ensure that you don't send conflicting writes to your clusters, which could result in data loss. [Learn more about conflicting writes](https://docs.cloud.google.com/bigtable/docs/routing#single-row-conflicts). 
  * **Do you want Bigtable to handle failovers automatically?**

If so, your app profiles must use [multi-cluster routing](https://docs.cloud.google.com/bigtable/docs/app-profiles#routing). If a cluster can't process an incoming request, Bigtable automatically fails over to the other clusters. [Learn more about automatic failovers](https://docs.cloud.google.com/bigtable/docs/failovers#automatic).

To prevent data loss, you can't enable [single-row transactions](https://docs.cloud.google.com/bigtable/docs/app-profiles#single-row-transactions) when you use multi-cluster routing. [Learn more](https://docs.cloud.google.com/bigtable/docs/app-profiles#single-row-conflicts).

  * **Do you want to maintain a backup or spare cluster in case your primary cluster is not available?**

If so, use [single-cluster routing](https://docs.cloud.google.com/bigtable/docs/app-profiles#routing) in your app profiles, and [fail over to the backup cluster manually](https://docs.cloud.google.com/bigtable/docs/failovers#manual) if necessary.

This configuration also makes it possible to use [single-row transactions](https://docs.cloud.google.com/bigtable/docs/app-profiles#single-row-transactions) if necessary.

  * **Do you want to send different kinds of traffic to different clusters?**

If so, use [single-cluster routing](https://docs.cloud.google.com/bigtable/docs/app-profiles#routing) in your app profiles, and direct each type of traffic to its own cluster. [Fail over between clusters manually](https://docs.cloud.google.com/bigtable/docs/failovers#manual) if necessary.

You can enable [single-row transactions](https://docs.cloud.google.com/bigtable/docs/app-profiles#single-row-transactions) in your app profiles if necessary.

**Important:** If you enable single-row transactions in multiple app profiles, you must ensure that you don't send conflicting writes to your clusters, which could result in data loss. [Learn more about conflicting writes](https://docs.cloud.google.com/bigtable/docs/routing#single-row-conflicts). 



## What's next

  * [Learn more about app profiles.](https://docs.cloud.google.com/bigtable/docs/app-profiles)
  * [Create an app profile or update an existing app profile.](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#creating-app-profile)
  * [Find out how failovers work.](https://docs.cloud.google.com/bigtable/docs/failovers)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
