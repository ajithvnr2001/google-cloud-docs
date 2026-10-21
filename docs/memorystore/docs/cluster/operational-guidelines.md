---
url: https://docs.cloud.google.com/memorystore/docs/cluster/operational-guidelines/
title: Operational guidelines \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:36:22.935951+00:00
---

# Operational guidelines  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/operational-guidelines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Operational guidelines Stay organized with collections  Save and categorize content based on your preferences. 

The Memorystore for Redis Cluster [Service Level Agreement (SLA)](https://cloud.google.com/memorystore/sla) excludes outages "caused by factors outside of Google's reasonable control". This page describes some of the user-controlled configurations and workloads that can cause an outage for a cluster in Memorystore for Redis Cluster to be excluded.

## Introduction

Memorystore strives to give you as much control over how your cluster is configured and used as possible. This includes some configurations or workload patterns that increase the risk of downtime for your cluster. If your cluster becomes unhealthy and Memorystore determines that it was out of compliance with the operational limits and best practices as described on this page, then the downtime period isn't covered by (or doesn't count against) the Memorystore [SLA](https://cloud.google.com/memorystore/sla).

This list of operational limits and best practices is presented to inform you which configurations and workload patterns present these risks, ways to avoid them, and ways to mitigate the risks when the configuration is required for your business environment.

## Excluded configurations

This section lists configurations that can cause your cluster to be excluded from the Memorystore SLA.

### General configuration requirements

  * If you configure a cluster without [high availability](https://docs.cloud.google.com/memorystore/docs/cluster/ha-and-replicas) (0 replicas), then the SLA doesn't apply. The Memorystore SLA covers only clusters that are configured for high availability.
  * If you [disable or destroy the primary key version](https://docs.cloud.google.com/memorystore/docs/cluster/about-cmek#disable-or-destroy-a-cmek-key-version) for a cluster, then the cluster is excluded from the Memorystore SLA.



### Resource constraints

The following resource constraints must be avoided to retain SLA coverage:

  * **CPU overloaded:** If your CPU utilization is consistently high, your cluster isn't properly sized for your workload or you are using Redis commands improperly. If CPU resources are overloaded, you might not be covered by the [SLA](https://cloud.google.com/memorystore/sla).

  * **Memory overloaded:** If your memory usage is consistently high, your cluster isn't properly sized for your workload, and might not be covered by the [SLA](https://cloud.google.com/memorystore/sla).




### The `redis-shared-core-nano` node type

The Memorystore SLA doesn't apply to clusters that use the `redis-shared-core-nano` [node type](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#choose_a_node_type). The node type isn't suitable for most production workloads because it has insufficient performance and is too small for most production use cases.

## Best practices

[Best practices for Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster/general-best-practices) are published to ensure that you receive the best possible experience with Memorystore. Downtime events which result from you not following the published best practices might not be covered by the [SLA](https://cloud.google.com/memorystore/sla).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
