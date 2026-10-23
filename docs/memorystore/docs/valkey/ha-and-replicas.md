---
url: https://docs.cloud.google.com/memorystore/docs/valkey/ha-and-replicas/
title: High availability and replicas \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:14.232240+00:00
---

# High availability and replicas  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/ha-and-replicas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  High availability and replicas Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how Memorystore for Valkey's architecture provides and supports high availability (HA). This page also explains how you can improve instance performance and stability with HA configurations that we recommend.

**Note:** For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

## High availability

Memorystore for Valkey is built on a highly available architecture where your clients access managed Memorystore for Valkey nodes directly. Your clients do this by connecting to individual endpoints, as described in [Connect to a Memorystore for Valkey instance](https://docs.cloud.google.com/memorystore/docs/valkey/connect-instance).

Connecting to shard(s) directly provides the following benefits:

  * Direct connection avoids intermediate hops, which minimizes the round-trip time (client latency) between your client and the Memorystore for Valkey node.

  * In Cluster Mode Enabled, direct connection avoids any single point of failure because each shard is designed to fail independently. For example, if traffic from multiple clients overloads a slot (keyspace chunk), shard failure limits the impact to the shard responsible for serving the slot.




### Recommended configurations

We recommend that you create highly available multi-zone instances as opposed to single-zone instances because of the better reliability they provide. However, if you choose to provision an instance without replicas, we recommend that you choose a single-zone instance. For more information, see [When to use a single-zone instance](https://docs.cloud.google.com/memorystore/docs/valkey/general-best-practices#when-to-use-a-single-zone-instance).

To enable high availability for your instance, you must provision at least 1 replica for every shard. You can do this when [Creating the instance](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances), or you can [Scale the replica count](https://docs.cloud.google.com/memorystore/docs/valkey/scale-replica-count) to at least 1 replica per shard. Replicas provide [Automatic failover](https://docs.cloud.google.com/memorystore/docs/valkey/ha-and-replicas#automatic_failover) during planned maintenance and unexpected shard failure.

We recommend that you configure your client according to the guidance in [Client best practices](https://docs.cloud.google.com/memorystore/docs/valkey/general-best-practices#client_best_practices). Using recommended best practices allows your client to handle the following items for your instance automatically and without any downtime:

  * The role (automatic failovers)
  * The endpoint (node replacement)
  * Cluster Mode Enabled-related slot assignment changes (consumer scale out and in)



## Replicas

A highly available Memorystore for Valkey instance is a regional resource. Memorystore for Valkey distributes the primary and replica VMs of shards across multiple zones to safeguard against a zonal outage. Memorystore for Valkey supports instances with 0-5 replicas per shard.

You can use replicas to increase read throughput at the cost of potential data staleness.

  * **Cluster Mode Enabled:** Use the `READONLY` command to establish a connection that allows your client to read from replicas.
  * **Cluster Mode Disabled:** Connect to the [reader endpoint](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#reader_endpoint) to connect to any of the available replicas.



### Cluster Mode Enabled Instance examples

The following diagrams illustrate examples for Cluster Mode Enabled instances:

### Instance example with three shards and zero replicas per shard

![A Memorystore for Valkey Cluster Mode Enabled instance with no replicas per shard, and nodes divided evenly across three zones.](https://docs.cloud.google.com/static/memorystore/img/valkey-ha1.png)

### Instance example with three shards and one replica per shard

![A Memorystore for Valkey Cluster Mode Enabled instance with one replica per shard, and nodes divided evenly across three zones.](https://docs.cloud.google.com/static/memorystore/img/valkey-ha2.png)

### Instance example with three shards and multiple replicas per shard

![A Memorystore for Valkey Cluster Mode Enabled instance with multiple replicas per shard, and nodes divided evenly across three zones.](https://docs.cloud.google.com/static/memorystore/img/valkey-ha3.png)

### Cluster Mode Disabled Instance examples

The following diagram illustrates an example for Cluster Mode Disabled instances:

#### Instance example with multiple replicas

![A Memorystore for Valkey Cluster Mode Disabled instance with multiple replicas and nodes divided evenly across three zones.](https://docs.cloud.google.com/static/memorystore/img/valkey_cluster_mode_disabled.png)

## How a failover affects your application

When Memorystore for Valkey promotes a replica to the primary instance, it drops existing connections to the primary endpoint of the instance. During automated repairs and maintenance events, the instance is unavailable for an average of 30 seconds.

After the instance becomes available, Memorystore for Valkey uses the same connection string or IP address to redirect your application to the new primary instance automatically. You don't need to update your application.

During a failover, if there are connections to the read endpoint, then Memorystore for Valkey drops connections to the replica that it promotes to the primary instance. However, Memorystore for Valkey doesn't drop the connections to the other replicas. After the failover is complete and the new replica is available, Memorystore for Valkey redirects connections to the new replica.

## Automatic failover

Automatic failovers within a shard can occur due to [maintenance](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance) or an unexpected failure of the primary node. During a failover a replica is promoted to be the primary. You can configure replicas explicitly. The service can also temporarily provision extra replicas during internal maintenance to avoid any downtime.

Automatic failovers prevent data loss during maintenance updates. For more information about automatic failover behavior during maintenance, see [Automatic failover behavior during maintenance](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance#automatic_failover_behavior_during_maintenance).

### Failover and node repair duration

Automatic failovers can take time on the order of tens of seconds for unplanned events such as a primary node process crash, or a hardware failure. During this time the system detects the failure, and elects a replica to be the new primary.

Node repair can take time on the order of minutes for the service to replace the failed node. This is true for all primary and replica nodes. For instances that aren't highly available (no replicas provisioned), repairing a failed primary node also takes time on the order of minutes.

### Client behavior during an unplanned failover

Client connections are likely to be reset depending on the nature of the failure. After automatic recovery, you can retry your connections with [exponential backoff](https://docs.cloud.google.com/memorystore/docs/valkey/exponential-backoff) to avoid overloading primary and replica nodes.

Clients using replicas for read throughput might experience a temporary degradation in capacity until the failed node is automatically replaced.

### Lost writes

During a failover resulting from an unexpected failure, acknowledged writes may be lost due to the asynchronous nature of Valkey's replication protocol.

Client applications can leverage the Valkey WAIT command to improve real world data safety.

### Keyspace impact of a single zone outage

This section describes the impact of a single zone outage on a Memorystore for Valkey instance.

#### Multi-zone instances

  * **HA instances:** If a zone has an outage, the entire keyspace is available for reads and writes, but since some read replicas are unavailable, the read capacity is reduced. We strongly recommend over-provisioning cluster capacity so that the instance has enough read capacity, in the rare event of a single zone outage. Once the outage is over, replicas in the affected zone are restored and the read capacity of the cluster returns to its configured value. For more information, see [Patterns for scalable and reliable apps](https://docs.cloud.google.com/architecture/scalable-and-resilient-apps).

  * **Non-HA instances (no replicas):** If a zone has a outage, the portion of the keyspace that is provisioned in the affected zone undergoes a data flush, and is unavailable for writes or reads for the duration of the outage. Once the outage is over, primaries in the affected zone are restored and the capacity of the cluster returns to its configured value.




#### Single-zone instances

  * **Both HA and Non-HA instances:** If the zone that the instance is provisioned in has an outage, the cluster is unavailable and data is flushed. If a different zone has an outage, the cluster continues to serve read and write requests.



## Best practices

This section describes best practices for high availability and replicas.

#### Add a replica

Adding a replica requires an RDB snapshot. RDB snapshots use a process fork and ['copy-on-write' mechanism](https://valkey.io/topics/persistence/) to take a snapshot of node data. Depending on the pattern of writes to nodes, the used memory of the nodes grows as pages touched by the writes are copied. The memory footprint can be up to double the size of the data in the node.

To ensure that nodes have sufficient memory to complete the snapshot, keep or set [`maxmemory`](https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations#modifiable_configuration_parameters) at 80% of the node capacity so that 20% is reserved for overhead. This memory overhead, in addition to monitoring snapshots, helps you manage your workload to have successful snapshots. Also, when you add replicas, lower write traffic as much as possible. For more information, see [Monitor memory usage for an instance](https://docs.cloud.google.com/memorystore/docs/valkey/general-best-practices#monitor-memory-usage).

**Note** : If you add a replica to an instance that uses more than 80% of the instance's maximum memory, then the operation fails and you receive an error message.

To resolve this issue, reduce your instance's memory usage in one of the following ways:

  * Lower your instance's memory footprint to less than 80% of the node's maximum allowed memory.
  * [Scale the node type](https://docs.cloud.google.com/memorystore/docs/valkey/scale-instance-capacity#scale_the_node_type) for your instance so that it has more memory.



After your instance's memory usage is below the 80% threshold, add the replica again.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
