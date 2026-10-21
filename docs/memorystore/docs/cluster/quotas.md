---
url: https://docs.cloud.google.com/memorystore/docs/cluster/quotas/
title: Quotas and limits \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:23:08.285926+00:00
---

# Quotas and limits  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Resources ](https://docs.cloud.google.com/memorystore/docs/cluster/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document contains the current resource capacity limits and per-minute API request quotas for Memorystore for Redis Cluster.

## Cluster limits

Memorystore for Redis Cluster enforces the following usage limits:

Limit | Value  
---|---  
Databases per cluster | 1  
[Usage units per cluster](https://docs.cloud.google.com/memorystore/docs/cluster/quotas#cluster_usage_units) | 250  
  
### Max clients

_Max clients_ is the maximum number of client connections that you can have for each node of a [node type](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#choose_a_node_type) without experiencing performance issues.

To make sure that you don't exceed the maximum number of client connections, we recommend that you monitor the [`/cluster/node/clients/connected_clients`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#node-level_metrics) metric.

The following table lists the node types that are available for Memorystore for Redis Cluster, and the default and maximum number of client connections that you can have for each node type.

Node type | Default number of client connections | Maximum number of client connections1  
---|---|---  
redis-shared-core-nano | 5,000 | 5,000  
redis-standard-small | 16,000 | 32,000  
redis-highmem-medium | 32,000 | 64,000  
redis-highcpu-medium | 32,000 | 64,000  
redis-standard-large | 32,000 | 64,000  
redis-highmem-xlarge | 64,000 | 64,000  
redis-highmem-2xlarge | 64,000 | 64,000  
**Caution** : We recommend that you use the `redis-shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Redis Cluster in a production environment, then we recommend using another node type. For more information about these node types, see [Choose a node type](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#choose_a_node_type).

1 For instructions on adjusting the maximum client connection limit, see [Configure a cluster](https://docs.cloud.google.com/memorystore/docs/cluster/configure-instances).

### Cluster usage units

The per-project cluster usage units for a cluster in Memorystore for Redis Cluster is calculated by the following formula:

Cluster usage units = (shard_count) * (1 + replica_count)

The regional quota for Memorystore for Redis Cluster limits the total amount of usage units that you can provision across all of your clusters in a region.

For example, if you provision three clusters in your project with 3 shards and 1 replica each in `us-central1`, then you consume 18 units out of the total regional unit quota for `us-central1`.

## Per-minute API requests quota

**Note:**

  * You cannot request a quota increase for Memorystore for Redis Cluster API operations, such as the `create`, `update`, and `delete` operations. There is no limit to the number of Redis commands you can run, such as Redis `SET`, `GET`, and `DEL`.
  * To reduce the number of API requests made if an error is encountered, see [Exponential backoff](https://docs.cloud.google.com/memorystore/docs/redis/exponential-backoff).



The per-minute quotas for Memorystore for Redis API requests and operations are as follows, and are subject to change:

API Requests Quota | Value  
---|---  
Create or delete Redis Cluster requests per project per minute | 10  
Redis Cluster requests per project per minute | 60  
  
Create or delete Redis Cluster requests include:

  * Create operations (`gcloud redis clusters create`)
  * Delete operations (`gcloud redis clusters delete`)



Memorystore for Redis Cluster API operations include:

  * Get operations (`gcloud redis clusters describe`)
  * List operations (`gcloud redis clusters list`)
  * Create operations (`gcloud redis clusters create`)
  * Delete operations (`gcloud redis clusters delete`)
  * Update operations (`gcloud redis clusters update`)



This quota is for redis.googleapis.com requests/operations, not OSS Redis protocol/commands. These limits apply to each Google Cloud console project and are shared across all applications and IP addresses using that project.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
