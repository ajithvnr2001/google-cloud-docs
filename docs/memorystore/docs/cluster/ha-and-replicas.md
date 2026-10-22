---
url: https://docs.cloud.google.com/memorystore/docs/cluster/ha-and-replicas/
title: High availability and replicas \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:12.642984+00:00
---

# High availability and replicas  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/ha-and-replicas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  High availability and replicas Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how Memorystore for Redis Cluster architecture provides and supports high availability (HA). This page also explains how you can improve cluster performance and stability with HA configurations that we recommend.

For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

## High availability

Memorystore for Redis Cluster is built on a highly available architecture where your clients directly access managed Memorystore for Redis Cluster VMs. Your clients do this by connecting to individual shard network addresses, as described in [Connect to a Memorystore for Redis Cluster instance](https://docs.cloud.google.com/memorystore/docs/cluster/connect-cluster-instance).

Connecting directly to shards provides the following benefits:

  * Direct connection avoids any single point of failure because each shard is designed to fail independently. For example, if traffic from multiple clients overloads a slot (keyspace chunk), shard failure limits the impact to the shard responsible for serving the slot.

  * Direct connection avoids intermediate hops, which minimizes round-trip time (client latency) between your client and the Redis VM.




### Recommended configurations

We recommend that you create highly available multi-zone instances as opposed to single-zone instances because of the better reliability they provide. However, if you choose to provision an instance without replicas, we recommend that you choose a single-zone instance. For more information, see [When to use a single-zone cluster](https://docs.cloud.google.com/memorystore/docs/cluster/general-best-practices#when-to-use-a-single-zone-cluster).

To enable high availability for your instance, you must provision at least 1 replica for every shard. You can do this when [Creating the instance](https://docs.cloud.google.com/memorystore/docs/cluster/create-instances), or you can [Scale the replica count](https://docs.cloud.google.com/memorystore/docs/cluster/scale-replica-count) to at least 1 replica per shard. Replicas provide [Automatic failover](https://docs.cloud.google.com/memorystore/docs/cluster/ha-and-replicas#automatic_failover) during planned maintenance and unexpected shard failure.

We recommend that you configure your client according to the guidance in [Redis client best practices](https://docs.cloud.google.com/memorystore/docs/cluster/general-best-practices#redis_client_best_practices). Using recommended best practices allows your OSS Redis client to automatically and gracefully handle the role (automatic failovers), and slot assignment changes (node replacement, consumer scale out/in) for your cluster without any downtime.

## Replicas

A highly available Memorystore for Redis Cluster instance is a regional resource. This means that the primary and the replica VMs of shards are distributed across multiple zones to safeguard against a zonal outage. Memorystore for Redis Cluster supports instances with 0-5 replicas per shard.

You can use replicas to increase read throughput by scaling reads. To do this, you must use the `READONLY` command to establish a connection that allows your client to read from replicas. For more details about reading from replicas, see [Scale with Redis Cluster](https://redis.io/docs/latest/operate/oss_and_stack/management/scaling/).

### Cluster example with 0 replicas per shard

![A Memorystore Cluster for Redis instance with no replicas per shard, and nodes divided evenly across three zones.](https://docs.cloud.google.com/static/memorystore/img/cluster-ha1.png)

### Cluster example with 1 replica per shard

![A Memorystore Cluster for Redis instance with one replica per shard, and nodes divided evenly across three zones.](https://docs.cloud.google.com/static/memorystore/img/cluster-ha2.png)

### Cluster example with multiple replicas per shard

![A Memorystore Cluster for Redis instance with multiple replicas per shard, and nodes divided evenly across three zones.](https://docs.cloud.google.com/static/memorystore/img/cluster-ha3.png)

## Automatic failover

Automatic failovers within a shard can occur due to [maintenance](https://docs.cloud.google.com/memorystore/docs/cluster/about-maintenance) or an unexpected failure of the primary node. During a failover a replica is promoted to be the primary. You can configure replicas explicitly. The service can also temporarily provision extra replicas during internal maintenance to avoid any downtime.

Automatic failovers prevent data loss during maintenance updates. For more information about automatic failover behavior during maintenance, see [Automatic failover behavior during maintenance](https://docs.cloud.google.com/memorystore/docs/cluster/about-maintenance#automatic_failover_behavior_during_maintenance).

### Failover and node repair duration

Automatic failovers can take time on the order of tens of seconds for unplanned events such as a primary node process crash, or a hardware failure. During this time the system detects the failure, and elects a replica to be the new primary.

Node repair can take time on the order of minutes for the service to replace the failed node. This is true for all primary and replica nodes. For instances that aren't highly available (no replicas provisioned), repairing a failed primary node also takes time on the order of minutes.

### Client behavior during an unplanned failover

Client connections are likely to be reset depending on the nature of the failure. After automatic recovery, you can retry your connections with [exponential backoff](https://docs.cloud.google.com/memorystore/docs/redis/exponential-backoff) to avoid overloading primary and replica nodes.

Clients using replicas for read throughput might experience a temporary degradation in capacity until the failed node is automatically replaced.

### Lost writes

During a failover resulting from an unexpected failure, acknowledged writes may be lost due to the asynchronous nature of Redis's replication protocol.

Client applications can leverage the Redis [WAIT](https://redis.io/commands/wait/) command to improve real world data safety. It is a best-effort approach that comes with trade-offs as explained in Redis `WAIT` command documentation.

### Keyspace impact of a single zone outage

This section describes the impact of a single zone outage on a Memorystore for Redis Cluster instance.

#### Multi-zone instances

  * **HA instances:** If a zone has an outage, the entire keyspace is available for reads and writes, but since some read replicas are unavailable, the read capacity is reduced. We strongly recommend over-provisioning cluster capacity so that the instance has enough read capacity, in the rare event of a single zone outage. Once the outage is over, replicas in the affected zone are restored and the read capacity of the cluster returns to its configured value. For more information, see [Patterns for scalable and reliable apps](https://docs.cloud.google.com/architecture/scalable-and-resilient-apps).

  * **Non-HA instances (no replicas):** If a zone has a outage, the portion of the keyspace that is provisioned in the affected zone undergoes a data flush, and is unavailable for writes or reads for the duration of the outage. Once the outage is over, primaries in the affected zone are restored and the capacity of the cluster returns to its configured value.




#### Single-zone instances

  * **Both HA and Non-HA instances:** If the zone that the instance is provisioned in has an outage, the cluster is unavailable and data is flushed. If a different zone has an outage, the cluster continues to serve read and write requests. Once the outage is over, the configured capacity of the cluster is restored.



## Best practices

This section describes best practices for high availability and replicas.

#### Add a replica

Adding a replica requires an RDB snapshot. RDB snapshots use a process fork and ['copy-on-write' mechanism](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/) to take a snapshot of node data. Depending on the pattern of writes to nodes, the used memory of the nodes grows as pages touched by the writes are copied. The memory footprint can be up to double the size of the data in the node.

To ensure that nodes have sufficient memory to complete the snapshot, keep or set [`maxmemory`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-instance-configurations#modifiable_configuration_parameters) at 80% of the node capacity so that 20% is reserved for overhead. This memory overhead, in addition to monitoring snapshots, helps you manage your workload to have successful snapshots. Also, when you add replicas, lower write traffic as much as possible. For more information, see [Monitor a cluster that has a high write load](https://docs.cloud.google.com/memorystore/docs/cluster/general-best-practices#monitor_a_cluster_that_has_a_high_write_load).

**Note** : If you add a replica to a cluster that uses more than 80% of the cluster's maximum memory, then the operation fails and you receive an error message.

To resolve this issue, reduce your cluster's memory usage in one of the following ways:

  * Lower your cluster's memory footprint to less than 80% of the node's maximum allowed memory.
  * [Scale the node type](https://docs.cloud.google.com/memorystore/docs/cluster/scale-instance-capacity#scale_the_node_type) for your cluster so that it has more memory.



After your cluster's memory usage is below the 80% threshold, add the replica again.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
