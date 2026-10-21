---
url: https://docs.cloud.google.com/bigtable/docs/app-profiles/
title: App profiles overview \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:11.990377+00:00
---

# App profiles overview  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/app-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# App profiles overview

**Note:** This page includes features that are available only in the Enterprise Plus edition. For more information, see [Editions overview](https://docs.cloud.google.com/bigtable/docs/editions-overview).

An application profile, or _app profile_ , stores settings that tell your Bigtable instance how to handle incoming requests from an application. When your application connects to a Bigtable instance, it uses either the default app profile or an app profile specified by you. Bigtable uses that app profile for requests that the application sends over that connection.

An app profile is either a standard app profile or a Data Boost app profile, depending on the type of compute it uses. A _standard app profile_ uses provisioned cluster nodes for compute and is typically used for application-serving traffic. A _Data Boost app profile_ uses serverless compute, which is designed for high-throughput read jobs and queries. For more information about Data Boost, read the [Data Boost overview](https://docs.cloud.google.com/bigtable/docs/data-boost-overview).

This page describes app profiles and provides guidance on using them.

For code samples showing how to use an app profile in your application, see [Connect with a custom app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#connecting).

## Use a separate app profile for each workload

When you create a Bigtable instance, a default app profile is created automatically, and its settings depend on the number of clusters the instance has. To take full advantage of the benefits of app profiles, you should create and use additional app profiles and use a different app profile for each application or workload.

App profiles are especially important for instances that have two or more clusters, but even if your instance has only one cluster, you should use a unique app profile for each application that you run, or for different components within a single application.

The following sections describe the benefits of creating and using multiple app profiles.

### Workload isolation

Using separate app profiles lets you use different Bigtable compute and routing policies for different purposes. For example, consider a situation when you want to prevent a batch read job (workload A) from increasing CPU usage on clusters that handle an application's steady reads and writes (workload B). You can take one of the following approaches:

  * Create a standard app profile for workload B that routes to a cluster group that excludes one cluster. Then you create a separate standard app profile for workload A that specifies [single-cluster routing](https://docs.cloud.google.com/bigtable/docs/routing#single-cluster) to the cluster that workload B doesn't send requests to.

  * Use a standard app profile, which uses cluster nodes for compute, configured to route to any cluster for workload B, and create a Data Boost app profile for use against a single cluster with workload A. Data Boost uses serverless compute, while the application traffic uses cluster nodes for compute.




You can change the settings for one application or function without affecting other applications that connect to the same data.

### Observability

Using separate app profiles for different workloads gives you better insight into your applications' usage of Bigtable, because metrics are available per app profile. This increase in observability can be helpful in the following ways:

  * You're able to look at latency at the app profile level to help you determine which application might be impacting overall performance.

  * Monitoring the [CPU utilization per app profile](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#cpu) for a workload using a standard app profile can help you troubleshoot CPU utilization issues or make decisions about the size or location of the cluster, so you can optimize usage and reduce costs.

  * Metrics at the app profile level are useful if you need to [seek support](https://docs.cloud.google.com/bigtable/docs/support/getting-support), because you're better able to share the exact workload that is causing an issue.




You can use the Bigtable Google Cloud console to view separate graphs of your Bigtable metrics for each app profile. To learn which metrics that are available at the profile level, see the table at [System insights charts for Bigtable resources](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#console-monitoring-resources).

## Standard app profiles

A standard app profile routes traffic to an instance's clusters using the clusters' nodes.

### Routing

A standard app profile defines the [routing policy](https://docs.cloud.google.com/bigtable/docs/routing) that Bigtable uses and controls whether [single-row transactions](https://docs.cloud.google.com/bigtable/docs/routing#single-row-transactions) are allowed. A standard app profile also lets you specify the [priority level](https://docs.cloud.google.com/bigtable/docs/request-priorities) for requests sent using the app profile.

### Request priority

You can specify the priority that Bigtable should give to a standard app profile's data requests. To review the priority levels that are available, see [Configure request priorities](https://docs.cloud.google.com/bigtable/docs/request-priorities).

## In-memory tier app profiles

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

On Enterprise Plus clusters, you can configure app profiles to read traffic from the in-memory tier. An app profile that's configured to use the in-memory tier uses single-cluster routing by default.

## Data Boost app profiles

A Data Boost app profile lets you use Data Boost's serverless compute to isolate high-throughput jobs and queries from app serving traffic. A Data Boost app profile doesn't let you configure request priority, and the only routing policy available is single-cluster. For more information, see the [Data Boost overview](https://docs.cloud.google.com/bigtable/docs/data-boost-overview).

Enterprise Plus edition extends Data Boost capabilities to support:

  * Isolated SQL queries
  * Data analytics on HDD clusters or tables with tiered storage enabled



## App profile changes

If you need to change the routing policy or request priority for a workload, you can update the app profile that is used for the workload. You can also convert an app profile from standard to Data Boost isolation or from Data Boost to standard isolation. Converting a standard app profile to use Data Boost removes the request priority settings from the app profile as well as any routing policies that aren't single-cluster.

Changes to an app profile are effective immediately.

However, in many cases, instead of modifying an app profile that is in use, you should create a new app profile with a different configuration, like you would for a new use case, and then change your application code to use the new app profile. Creating a new app profile to make changes for a workload ensures that you don't inadvertently change the app profile for any other workloads that use the app profile.

If you change an app profile from standard to Data Boost, the type of compute that is used for the app profile's traffic is changed to serverless, along with pricing. For more information, see the [Data Boost overview](https://docs.cloud.google.com/bigtable/docs/data-boost-overview) and [Bigtable pricing](https://cloud.google.com/bigtable/pricing).

Similarly, if you change an app profile from Data Boost to standard, traffic that is sent by the app profile starts using cluster nodes for compute. This means that all clusters that the app profile routes to must have enough nodes to satisfy CPU usage requirements. For more information, see [Nodes](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes#nodes).

To see how to view, create, and update app profiles, see [Create and configure app profiles](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles).

## Default app profile

When you create an instance, Bigtable automatically creates a default app profile for the instance. The default app profile is a standard app profile, but you can convert it to a Data Boost profile. If your application does not specify an app profile, or if you use the HBase shell to connect to your instance, Bigtable uses the settings in the default app profile.

The settings in an instance's default app profile depend on the number of clusters the instance had when you first created it:

  * If you created the instance with 1 cluster, the `default` app profile uses [single-cluster routing](https://docs.cloud.google.com/bigtable/docs/routing#single-cluster), and it enables [single-row transactions](https://docs.cloud.google.com/bigtable/docs/routing#single-row-transactions). This ensures that adding additional clusters later doesn't change the behavior of your existing applications.
  * If you created the instance with 2 or more clusters, the `default` app profile uses [multi-cluster routing](https://docs.cloud.google.com/bigtable/docs/routing#multi-cluster) to any cluster. Single-row transactions are never allowed with multi-cluster routing.



The default app profile does not change when you add or remove clusters. You must manually [update the default app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#updating-app-profile) to change its settings. However, as a best practice you should **create and use a new app profile** instead of changing the default app profile.

## Custom app profiles

A _custom app profile_ is an app profile that you create and configure. An instance can have up to 2,000 app profiles. Every app profile that is not the default is considered a custom app profile.

## What's next

  * [Monitor a standard app profile's CPU usage.](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#cpu)
  * [Find the right replication settings for your use case](https://docs.cloud.google.com/bigtable/docs/replication-settings).
  * [Create and manage app profiles for your instance](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
