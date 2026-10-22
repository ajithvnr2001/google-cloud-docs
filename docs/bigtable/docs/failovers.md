---
url: https://docs.cloud.google.com/bigtable/docs/failovers/
title: Failovers \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:54.964223+00:00
---

# Failovers  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/failovers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Failovers

If a Bigtable cluster becomes unresponsive, replication makes it possible for incoming traffic to fail over to another cluster in the same instance. Failovers can be either manual or automatic, depending on the [app profile](https://docs.cloud.google.com/bigtable/docs/app-profiles) an application is using and how the app profile is configured. 

This page explains how manual and automatic failovers work in an instance that uses replication. To learn how to complete a failover, see [Managing failovers](https://docs.cloud.google.com/bigtable/docs/managing-failovers). 

Before you read this page, you should be familiar with the [overview of Bigtable replication](https://docs.cloud.google.com/bigtable/docs/replication-overview). You should also be familiar with the available [routing options](https://docs.cloud.google.com/bigtable/docs/routing).

## Manual failovers

If an app profile uses single-cluster routing to direct all requests to one cluster, you must use your own judgement to decide when to start failing over to a different cluster.

Here are some signals that might indicate that it would be helpful to fail over to a different cluster:

  * The cluster starts to return a large number of transient system errors.
  * A large number of requests start timing out.
  * The average response latency increases to an unacceptable level.



**Note** : Bigtable reverts to eventual consistency after a failover. If you fail over to a cluster, and there are writes that have not been replicated to that cluster, some reads will return stale data until replication is complete.

Because these signals can appear for many different reasons, failing over to a different cluster is not guaranteed to resolve the underlying issue. [Monitor your instance](https://docs.cloud.google.com/bigtable/docs/monitoring-instance) before and after the failover to verify that the metrics have improved.

For details about how to complete a manual failover, see [Completing a manual failover](https://docs.cloud.google.com/bigtable/docs/managing-failovers#manual).

## Automatic failovers

If an app profile uses multi-cluster routing, Bigtable handles failovers automatically. When the nearest cluster is unable to handle a request, Bigtable routes traffic to the nearest cluster that is available.

Automatic failovers can occur even if a cluster is unavailable for a very short period of time. For example, if Bigtable routes a request to one cluster, and that cluster is excessively slow to reply or returns a transient error, Bigtable will typically retry that request on another cluster.

If you use multi-cluster routing and you send a request with a deadline, then Bigtable automatically fails over when necessary to help you meet the deadline. If the deadline approaches and the initial cluster hasn't sent a response, then Bigtable reroutes the request to the next closest cluster. The deadline you set influences how quickly this happens: a shorter deadline triggers an earlier failover, while a longer deadline allows more time before failing over.

Make sure that your deadline is long enough to let the failover request complete successfully on a subsequent cluster, especially if the subsequent cluster is in a different region.

Bigtable uses an internal _last write wins_ algorithm to handle any data conflicts that might occur as a result of failover before replication has completed. See [Conflict resolution](https://docs.cloud.google.com/bigtable/docs/writes#conflict-resolution) for more details.

If you are using replication with multi-cluster routing to achieve high availability (HA) for your application, you should locate your client servers or VMs _in or near more than one Google Cloud region_. This recommendation applies even if your application server is not hosted by Google Cloud, because your data enters the Google Cloud network through the Google Cloud region that is closest to your application server. Like any request, a failover completes more quickly over shorter distances.

Many automatic failovers are so brief that you won't notice them. You can check the **Automatic Failovers** graph in the Google Cloud console to see the number of requests that were automatically rerouted over a given period of time: open the [list of instances](https://console.cloud.google.com/bigtable/instances), click the instance name, then click **System insights**.

## What's next

  * Learn how to [complete a manual failover](https://docs.cloud.google.com/bigtable/docs/managing-failovers#manual).
  * Find out how to [monitor your instance](https://docs.cloud.google.com/bigtable/docs/monitoring-instance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
