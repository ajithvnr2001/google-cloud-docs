---
url: https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification/
title: Cluster and node specification \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:04:07.476267+00:00
---

# Cluster and node specification  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Cluster and node specification Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the cluster and node specifications for Memorystore for Redis Cluster instances. For instructions on how to create an instance, see [Create instances](https://docs.cloud.google.com/memorystore/docs/cluster/create-instances).

**Note:** The terms _node_ and _shard_ are used interchangeably on this page to refer to a single Redis shard.

## Choose a node type

The shards in your cluster all use the same node type of your choosing. The best node type for your cluster depends on your requirements for price, performance, and keyspace capacity.

The `redis-shared-core-nano` node type is for small workloads. This node type provides variable [performance](https://docs.cloud.google.com/compute/docs/general-purpose-machines#sharedcore) and doesn't have an SLA, making it unsuitable for production workloads.

The `redis-standard-small` node type lets you provision small clusters, and grow your cluster by smaller increments at potentially lower costs than other node types. `redis-standard-small` also offers the advantage of distributing your keyspace across more nodes with a higher total vCPU count. This offers improved price-performance compared to `redis-highmem-medium`, as long as the total keyspace capacity of the smaller nodes is sufficient for your data needs.

If you have workloads that require a higher rate of processing power relative to memory, then choose the `redis-highcpu-medium` node type. If you need more capacity than what `redis-highmem-medium` provides, then we recommend choosing the `redis-standard-large`, `redis-highmem-xlarge`, or `redis-highmem-2xlarge` node types. When you add vCPUs to increasingly larger nodes (scaling up), Redis performance might not scale linearly. Instead, to get a better price performance, we recommend that you [scale out](https://docs.cloud.google.com/memorystore/docs/cluster/about-scaling-instance-capacity) by adding more nodes to a cluster.

**Caution** : We recommend that you use the `redis-shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Redis Cluster in a production environment, then we recommend using another node type.

## Node type specification

The node capacity and characteristics depend on which node type you choose:

### Keyspace capacity and reserved overhead

Node type | Default writable keyspace capacity | Total node capacity  
---|---|---  
redis-shared-core-nano | 1.12 GB | 1.4 GB  
redis-standard-small | 5.2 GB | 6.5 GB  
redis-highmem-medium | 10.4 GB | 13 GB  
redis-highcpu-medium | 10.4 GB | 13 GB  
redis-standard-large | 20.8 GB | 26 GB  
redis-highmem-xlarge | 46.4 GB | 58 GB  
redis-highmem-2xlarge | 88 GB | 110 GB  
  
Memorystore automatically sets aside a portion of your instance capacity to help prevent Out Of Memory (OOM) errors. This ensures a smooth experience reading and writing keys. Memory limits and storage details are as follows:

  * **Customizing your storage:** While we recommend using the default settings, you have the option to adjust the amount of reserved storage using the `maxmemory` configuration. For information about `maxmemory`, see [Supported instance configurations](https://docs.cloud.google.com/memorystore/docs/cluster/supported-instance-configurations).

  * **How much storage do you get?** Refer to the previous table's _Default writable keyspace capacity_ column. This shows how much storage is available for your keys by default.

  * **Maximizing storage** If you want the maximum possible storage, the _total node capacity_ column shows the storage limit when you set the `maxmemory` config to 100%. However, don't recommend choosing a `maxmemory` value higher than the default setting.

  * The `redis-shared-core-nano` node type has a hard limit of 1.12 GB, and can't be changed with the `maxmemory` configuration.




### Node characteristics

Node type | vCPU count | SLA offered | Default number of client connections | Maximum number of client connections | Maximum memory for clients (maxmemory-clients [ configuration](https://docs.cloud.google.com/memorystore/docs/cluster/supported-instance-configurations#modifiable_configuration_parameters))  
---|---|---|---|---|---  
redis-shared-core-nano | 0.5 | No | 5,000 | 5,000 | 12%  
redis-standard-small | 2 | Yes | 16,000 | 32,000 | 7%  
redis-highmem-medium | 2 | Yes | 32,000 | 64,000 | 7%  
redis-highcpu-medium | 8 | Yes | 32,000 | 64,000 | 7%  
redis-standard-large | 8 | Yes | 32,000 | 64,000 | 7%  
redis-highmem-xlarge | 8 | Yes | 64,000 | 64,000 | 4%  
redis-highmem-2xlarge | 16 | Yes | 64,000 | 64,000 | 4%  
  
The more virtual CPUs (vCPUs) that you select for your cluster, the better the performance. If your cluster runs resource-intensive workloads, then select a node type with a higher vCPU (for example, `redis-highmem-xlarge`). If your cluster performs less-demanding tasks, then select a node type with a lower vCPU (for example, `redis-highmem-medium`).

## Scale an instance

As part of creating a Memorystore for Redis Cluster instance, you choose a node type for the instance and specify the number of shards for the instance. After you create the instance, and as the capacity needs for your instance change, you might need to scale the instance in the following ways:

  * Change the number of shards for your instance. This is _horizontal scaling_. You scale an instance horizontally by performing one of the following actions: 
    * Add shards to the instance. This is scaling the instance _out_.
    * Remove shards from the instance. This is scaling the instance _in_.
  * Change the node type for your instance. This is _vertical scaling_. To scale an instance vertically, change the node type of the instance to one of the following node types: 
    * Change to a larger node type. This is scaling the instance _up_.
    * Change to a smaller node type. This is scaling the instance _down_.

**Note:** For more information about horizontal and vertical scaling, see [About scaling cluster capacity](https://docs.cloud.google.com/memorystore/docs/cluster/about-scaling-instance-capacity). For more information about changing the capacity of your instance by scaling the node type or the shard count, see [Scale cluster capacity](https://docs.cloud.google.com/memorystore/docs/cluster/scale-instance-capacity).

## Cluster specification

This section shows minimum and maximum cluster capacities given the cluster shape, node type, and replica count.

### Minimum writable capacity

Writable capacity is the amount of storage available for writing keys. It is equal to the size of one instance node. Therefore, depending on the node type, the minimum writable capacity is between 1.4 GB and 110 GB. The minimum writable capacity isn't affected by the number of replicas you choose.

### Maximum writable capacity

Node type and size | Max capacity given cluster shape of 250 primary nodes and 0 replicas per node | Max capacity given cluster shape of 125 primary nodes and 1 replicas per node | Max capacity given cluster shape of 83 primary nodes and 2 replicas per node | Max capacity given cluster shape of 62 primary nodes and 3 replicas per node | Max capacity given cluster shape of 50 primary nodes and 4 replicas per node | Max capacity given cluster shape of 41 primary nodes and 5 replicas per node  
---|---|---|---|---|---|---  
redis-shared-core-nano - 1.4 GB | 350 GB | 175 GB | 116.2 GB | 86.8 GB | 70 GB | 57.4 GB  
redis-standard-small - 6.5 GB | 1,625 GB | 812.5 GB | 539.5 GB | 403 GB | 325 GB | 266.5 GB  
redis-highmem-medium - 13 GB | 3,250 GB | 1,625 GB | 1,079 GB | 806 GB | 650 GB | 533 GB  
redis-highcpu-medium - 13 GB | 3,250 GB | 1,625 GB | 1,079 GB | 806 GB | 650 GB | 533 GB  
redis-standard-large - 26 GB | 6,500 GB | 3,250 GB | 2,158 GB | 1,612 GB | 1,300 GB | 1,066 GB  
redis-highmem-xlarge - 58 GB | 14,500 GB | 7,250 GB | 4,814 GB | 3,596 GB | 2,900 GB | 2,378 GB  
redis-highmem-2xlarge - 110 GB | 27,500 GB | 13,750 GB | 9,130 GB | 6,820 GB | 5,500 GB | 4,510 GB  
  
## Performance

Using the [OSS memtier benchmarking tool](https://github.com/RedisLabs/memtier_benchmark) in the `us-central1` region yielded 120,000 - 130,000 operations per second per 2 vCPU node (`redis-standard-small` and `redis-highmem-medium`) with microseconds latency and 1KiB data size.

We recommend that you perform your own benchmarking with real workloads or synthetic workloads that resemble your production traffic. In addition, we recommend that you size your clusters with a buffer (or "headroom") for workload spikes or unexpected traffic. For more guidance, see [Best practices for Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster/general-best-practices).

## Cluster endpoints

This section explains the two endpoints each instance has.

### Discovery endpoint

Each instance has a discovery endpoint to which your client connects. It is a combination of an IP address and port number. For instructions on how to find your cluster's discovery endpoint, see [View your cluster's discovery endpoint](https://docs.cloud.google.com/memorystore/docs/cluster/connect-cluster-instance#view_your_clusters_discovery_endpoint).

Your client also uses it for node discovery. Your client uses the discovery endpoint to retrieve your instance's cluster topology to bootstrap OSS Redis cluster clients, and keep them updated in steady state. The resulting cluster topology provides Redis node endpoints (IP and port combinations) to be cached in-memory by the Redis cluster client. Your client then takes care of the updates and redirections automatically with no other application change required. For information on client discovery behavior and best practices, see [Client discovery](https://docs.cloud.google.com/memorystore/docs/cluster/general-best-practices#client_discovery).

The discovery endpoint is highly available because it is backed by multiple Redis nodes across multiple-zones to serve the cluster topology. Serving topology through the endpoint is robust even when faced with backend node failures or node updates.

Your discovery endpoint has the following behavior:

  1. Your cluster's discovery endpoint remains unchanged throughout the lifecycle of the cluster instance, even during maintenance, or by any other action you take such as scaling in or out or changing replica counts.

  2. Redis node endpoints can change and can be recycled as nodes are added and removed over time. Ideally, you should use a Redis cluster client that can handle these changes automatically through topology refreshes and redirections. Examples of Redis cluster clients can be found at [Client library code samples](https://docs.cloud.google.com/memorystore/docs/cluster/client-library-code-samples). Your application shouldn't have dependencies or assumptions that node endpoints will remain unchanged for a given cluster.




### Data endpoint

In addition to the discovery endpoint, each cluster has a data endpoint. This endpoint is reserved for Memorystore for Redis Cluster to use to connect your client to nodes in the cluster. Therefore, don't connect to this endpoint directly.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
