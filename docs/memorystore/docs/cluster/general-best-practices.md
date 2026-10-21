---
url: https://docs.cloud.google.com/memorystore/docs/cluster/general-best-practices/
title: Best practices for Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:24.574570+00:00
---

# Best practices for Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/general-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Best practices for Memorystore for Redis Cluster Stay organized with collections  Save and categorize content based on your preferences. 

This page provides guidance on optimally using Memorystore for Redis Cluster. This page also points out potential issues to avoid.

**Note:** To view Redis cluster client configuration examples, see [Client library code samples](https://docs.cloud.google.com/memorystore/docs/cluster/client-library-code-samples).

## Memory management best practices

This section describes strategies for managing memory for clusters so that Memorystore for Redis Cluster works efficiently for your client applications.

### Memory management concepts

  * **Write load** \- The volume and speed at which you add or update keys on your Redis cluster. Your write load can range from normal to very high depending on your Redis use case and application usage patterns.

  * **Eviction policy** \- Memorystore for Redis Cluster uses the `volatile-lru` eviction policy. You can use commands like [EXPIRE](https://redis.io/commands/expire/) command to set evictions for keys.




### Monitor a cluster that has a normal write load

View the [`/cluster/memory/maximum_utilization`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics) metric. If `/cluster/memory/maximum_utilization` is at 100% or lower, your Redis cluster performs well when you use a normal write load.

However, if your memory usage approaches 100% and you expect data usage to grow, you should scale up your cluster size to make room for new data.

### Monitor a cluster that has a high write load

View the [`/cluster/memory/maximum_utilization`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics) metric. Depending on severity of your high write load, your cluster can experience performance issues at the following thresholds:

  * Very high write loads can experience issues if `/cluster/memory/maximum_utilization` reaches 65% or higher.

  * Moderately high write loads can experience issues if `/cluster/memory/maximum_utilization` reaches 85% or higher.




In these scenarios you should scale up your cluster size to improve performance.

If you run into issues, or are concerned that your cluster has a high write load, then reach out to [Google Cloud Support](https://docs.cloud.google.com/support).

### Scale shards

When you [scale the number of shards](https://docs.cloud.google.com/memorystore/docs/cluster/scale-instance-capacity) in a cluster, you should scale during periods of low writes. Scaling during periods of high write load can put memory pressure on your cluster because of memory overhead that's caused by replication or slot migration.

If your Redis use case uses key evictions, scaling to a smaller cluster size can reduce your cache hit ratio. In this circumstance, however, you don't need to worry about losing data, since key eviction is expected.

For Redis use cases where you don't want to lose keys, you should only scale down to a smaller cluster that still has enough room for your data. Your new target shard count should allow for at least 1.5 times the memory used by data. In other words, you should provision enough shards for 1.5 times the amount of data in your cluster. You can use the [`/cluster/memory/total_used_memory` metric](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics) to see how much data is stored in your cluster.

## CPU usage best practices

If an unexpected zonal outage occurs, this leads to reduced CPU resources for your cluster due to lost capacity from nodes in the unavailable zone. We recommend using [high available](https://docs.cloud.google.com/memorystore/docs/cluster/ha-and-replicas) clusters. Using multiple replicas per shard (as opposed to one replica per shard) provides additional CPU resources during an outage. You can have up to five replicas per shard.

Additionally, we recommend managing node CPU usage so that nodes have enough CPU overhead to handle additional traffic from lost capacity if an unexpected zonal outage happens. You should monitor CPU usage for primaries and replicas using the [Main Thread CPU Seconds `/cluster/cpu/maximum_utilization`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics) metric.

Depending on the number of replicas you provision per node, we recommend the following `/cluster/cpu/maximum_utilization` CPU usage targets:

  * For clusters with one replica per node, target a `/cluster/cpu/maximum_utilization` value of 0.5 seconds for the primary and 0.5 seconds for the replica.
  * For clusters with two replicas per node or greater, target a `/cluster/cpu/maximum_utilization` value of 0.9 seconds for the primary and 0.5 seconds for each replica.



If values for the metric exceed these recommendations, then we recommend scaling up the number of shards in your cluster. If you have fewer than five replicas for your cluster, then you can also scale up the number of replicas, up to a maximum of five replicas.

If your cluster either experiences high CPU utilization or the cluster's resources become exhausted (for example, by having too many connections), then the cluster might misbehave and external metrics might be missing.

### Resource-intensive Redis commands

We strongly recommend that you avoid using Redis commands that are resource-intensive. Using these commands might result in the following performance issues:

  * High latency and client timeouts
  * Memory pressure caused by commands that increase memory usage
  * Data loss during node replication and synchronization because the Redis main thread is blocked
  * Starved health checks, observability, and replication



The following table lists examples of Redis commands that are resource-intensive and provides you with alternatives that are resource-efficient.

**Tip** : In addition to being resource-intensive, as your total data size increases, so does the cost of using these commands.

To find which long-running commands you use, use [`SLOWLOG`](https://redis.io/docs/latest/commands/slowlog/). This tool provides you with a list of commands that take the longest to run. As a result, you know the commands that cause latency issues. To determine resource-efficient alternatives for these commands, refer to the following table.

**Category** | **Resource-intensive command** | **Resource-efficient alternative**  
---|---|---  
Run for the entire keyspace | `KEYS` | `SCAN`  
Run for a variable-length keyset | `LRANGE` | Limit the size of the range that you use for a query.  
`ZRANGE` | Limit the size of the range that you use for a query.  
`HGETALL` | `HSCAN`  
`SMEMBERS` | `SSCAN`  
Block the running of a script | `EVAL` | Ensure that your script doesn't run indefinitely.  
`EVALSHA` | Ensure that your script doesn't run indefinitely.  
Remove files and links | `DEL` | `UNLINK`  
Publish and subscribe | `PUBLISH` | `SPUBLISH`  
`SUBSCRIBE` | `SSUBSCRIBE`  
  
## Best practices for scaling thresholds

Scaling threshold scenarios fall into the following categories:

  * Scaling for memory utilization
  * Scaling for CPU utilization
  * Scaling to mitigate hotspots



If your workload relies on evicting keys, then Google doesn't recommend scaling in for either CPU or memory utilization. In these workloads, memory utilization frequently reaches its maximum capacity before evictions occur automatically. The resulting memory spikes block scale-in operations.

The following sections detail common scenarios and metric thresholds that might warrant scaling.

### Memory utilization scaling

To determine when to scale based on memory usage, monitor the `/cluster/memory/average_utilization` and `/cluster/memory/maximum_utilization` metrics. For more information about these metrics, see [Supported monitoring metrics](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics).

If your cluster meets either of the following conditions, then consider triggering a scale-out operation:

  * The average memory utilization of your cluster exceeds the suggested threshold of 70%.
  * The maximum memory utilization exceeds 80% and the average memory utilization exceeds 50%.



If your cluster meets either of the following conditions, then consider triggering a scale-in operation:

  * The average memory utilization of your cluster drops below the suggested threshold of 50%.
  * The maximum memory utilization drops below 60% and the average memory utilization drops below 40%.



### CPU utilization scaling

To determine when to scale based on CPU usage, monitor the `/cluster/cpu/average_utilization` and `/cluster/cpu/maximum_utilization` metrics.

If your cluster meets either of the following conditions, then consider triggering a scale-out operation:

  * The average CPU utilization of your cluster exceeds the suggested threshold of 70%.
  * The maximum CPU utilization exceeds 80% and the average CPU utilization exceeds 50%.



If your cluster meets either of the following conditions, then consider triggering a scale-in operation:

  * The average CPU utilization of your cluster drops below the suggested threshold of 50%.
  * The maximum CPU utilization drops below 60% and the average CPU utilization drops below 40%.



### Scaling to mitigate hotspots

Memorystore for Redis Cluster provides average and maximum variations of the same metric, which you can use to identify hotspots for that metric family. The maximum value represents the cluster node that's most heavily loaded, while the average value represents the load for the entire cluster. If the maximum value is significantly higher than the average value, then this indicates that a specific node is loaded disproportionately (a hotspot). To resolve this issue, we recommend that you scale out your cluster. For more information, see [Scale cluster capacity](https://docs.cloud.google.com/memorystore/docs/cluster/scale-instance-capacity).

When you observe a significant divergence between the average and maximum variations, you can run the `INFO memory` and `INFO cpu` commands against the cluster nodes to gather real-time data directly from the cluster. For more information about using these commands, see [INFO](https://redis.io/commands/info/) in the Redis documentation.

## Redis client best practices

Your application must use a cluster-aware Redis client when connecting to a cluster. For examples of cluster-aware clients and sample configurations, see [Client library code samples](https://docs.cloud.google.com/memorystore/docs/cluster/client-library-code-samples). Your client must maintain a map of hash slots to the corresponding nodes in the cluster to send requests to the right nodes and avoid the performance overhead caused by cluster redirections.

### Client mapping

Clients must obtain a complete list of slots and the mapped nodes in the following situations:

  * When the client is initialized, it must populate the initial slot to nodes mapping.

  * When a `MOVED` redirection is received from the server, such as in the situation of a failover when all slots served by the former primary node are taken over by the replica, or re-sharding when slots are being moved from the source primary to the target primary node.

  * When a `CLUSTERDOWN` error is received from the server or connections to a particular server run into timeouts persistently.

  * When a `READONLY` error is received from the server. This can happen when a primary is demoted to replica.

  * Additionally, clients should periodically refresh the topology to keep the clients warmed up for any changes and learn about changes that may not result in redirections or errors from the server, such as when new replica nodes are added. Note that any stale connections should also be closed as part of the topology refresh to reduce the need to handle failed connections during command runtime.




### Client discovery

Client discovery is usually done by issuing a `CLUSTER SLOT`, `CLUSTER NODE`, or `CLUSTER SHARDS` command to the Redis server. We recommend using the `CLUSTER SHARDS` command. `CLUSTER SHARDS` replaces the `CLUSTER SLOTS` command (deprecated), by providing a more efficient and extensible representation of the cluster.

The size of the response for the cluster client discovery commands can vary based on the cluster size and topology. Larger clusters with more nodes produce a larger response. As a result, it's important to ensure that the number of clients doing the cluster topology discovery doesn't grow unbounded.

These topology refreshes are expensive on the Redis server but are also important for application availability. Therefore it is important to ensure that each client makes a single discovery request at any given time (and caches result in-memory), and the number of clients making the requests be kept bounded to avoid overloading the server.

For example, when the client application starts up or loses connection from the server and must perform cluster discovery, one common mistake is that the client application makes several reconnection and discovery requests without adding [exponential backoff](https://docs.cloud.google.com/memorystore/docs/redis/exponential-backoff) upon retry. This can render the Redis server unresponsive for a prolonged period of time, causing very high CPU utilization.

### Avoid discovery overload on Redis

To mitigate the impact caused by a sudden influx of connection and discovery requests, we recommend the following:

  * Implement a client connection pool with a finite and small size to bound the number of concurrent incoming connections from the client application.

  * When the client disconnects from the server due to timeout, retry with exponential backoff with jitter. This helps to avoid multiple clients overwhelming the server at the same time.

  * Use the Memorystore for Redis Cluster discovery endpoint to perform cluster discovery. The discovery endpoint is highly available and is load balanced across all the nodes in the cluster. Moreover, the discovery endpoint attempts to route the cluster discovery requests to nodes with the most up-to-date topology view.




### Detect and handle unresponsive connections

We strongly recommend configuring your client application to detect unresponsive connections to Memorystore for Redis Cluster. When an unresponsive connection is detected, the client must reset it. To build a resilient application, we recommend the following client configurations:

  * **Configure TCP keep-alive parameters** : set the `TCP keepalive time`, `TCP keepalive interval`, and `TCP keepalive probes` parameters so that clients detect and drop unresponsive connections proactively, even when connections are idle. For example, if you set the `TCP keepalive time` parameter to 30 seconds, `TCP keepalive interval` to 10 seconds, and `TCP keepalive probes` to 3, then clients reset unresponsive idle connections within a minute.
  * **Configure TCP user timeouts** : set this timeout in your clients to reset connections that have outstanding requests and stop responding. For example, if you set the timeout to 15 seconds, then clients reset unresponsive connections that have outstanding requests after 15 seconds.



## Persistence best practices

This section explains best practices for [persistence](https://docs.cloud.google.com/memorystore/docs/cluster/persistence-overview).

### RDB persistence and adding replicas

For best results of backing up your cluster with RDB snapshots or adding replicas to your cluster, use the following best practices:

#### Memory management

RDB snapshots use a process fork and ['copy-on-write' mechanism](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/) to take a snapshot of node data. Depending on the pattern of writes to nodes, the used memory of the nodes grows as pages touched by the writes are copied. The memory footprint can be up to double the size of the data in the node.

To ensure that nodes have sufficient memory to complete the snapshot, keep or set [`maxmemory`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-instance-configurations#modifiable_configuration_parameters) at 80% of the node capacity so that 20% is reserved for overhead. This memory overhead, in addition to monitoring snapshots, helps you manage your workload to have successful snapshots. Also, when you add replicas, lower write traffic as much as possible. See Monitor a cluster that has a high write load to learn more. 

**Note** : If you add a replica to a cluster that uses more than 80% of the cluster's maximum memory, then the operation fails and you receive an error message.

To resolve this issue, reduce your cluster's memory usage in one of the following ways:

  * Lower your cluster's memory footprint to less than 80% of the node's maximum allowed memory.
  * [Scale the node type](https://docs.cloud.google.com/memorystore/docs/cluster/scale-instance-capacity#scale_the_node_type) for your cluster so that it has more memory.



After your cluster's memory usage is below the 80% threshold, add the replica again.

#### Stale snapshots

Recovering nodes from a stale snapshot can cause performance issues for your application as it tries to reconcile a significant amount of stale keys or other changes to your database such as a schema change. If you are concerned about recovering from a stale snapshot, you can disable the RDB persistence feature. Once you re-enable persistence, a snapshot is taken at the next scheduled snapshot interval.

#### Performance impact of RDB snapshots

Depending on your workload pattern RDB snapshots can impact the performance of the cluster and increase latency for your applications. You can minimize the performance impact of RDB snapshots by scheduling them to run during periods of low cluster traffic if you are comfortable with less frequent snapshots.

For example, if your cluster has low traffic from 1 AM to 4 AM, you can set the start time to 3 AM and set the interval to 24 hours.

If your system has a constant load and requires frequent snapshots, you should carefully evaluate the performance impact, and weigh the benefits of using RDB snapshots for the workload.

#### Add a replica

Adding a replica requires an RDB snapshot. For more information about RDB snapshots, see Memory management.

## When to use a single-zone cluster

If you configure a cluster so that it doesn't use replicas, then we recommend that you use a [single-zone cluster](https://docs.cloud.google.com/memorystore/docs/cluster/single-zone-instances). Here's why:

### Cost and performance

If minimizing your cost and having peak performance for your clients that are located in the same region are your primary drivers, then we recommend that you choose a single-zone cluster.

### Minimize your outage impact

When you choose a single-zone cluster, zonal outages are less likely to impact your cluster. By placing all nodes within a single zone, the chance of a zonal outage affecting your server drops from 100% to 33%. There's a 33% chance that the zone where your cluster is located goes down, as opposed to a 100% chance that nodes, which are located in the unavailable zone, are impacted.

### Rapid recovery

If a zonal outage occurs for a single-zone cluster, then Memorystore for Redis Cluster streamlines the recovery of your data. You can provision a new cluster in a functioning zone quickly and redirect your application for minimally interrupted operations.

## Capacity planning best practices

To ensure that you can successfully provision resources and build resilient architectures, we recommend the following capacity planning best practices:

  * **Deploy across multiple locations** : if you can't create a cluster in your preferred zone because of temporary resource constraints, then try creating the cluster either in a different zone within the same region or in a different region.
  * **Use cross-region access** : configure your clients to access your clusters that are located in different regions. If you need to provision a cluster that's in a different region because of local resource constraints, then your clients can connect to the cluster.
  * **Use cross-region replication** : to promote a secondary cluster in an alternate region to a primary read or write cluster for disaster recovery, perform a switchover.



## Lettuce best practices

This section describes best practices for using [Lettuce](https://lettuce.io/) to connect to a cluster.

### Update parameter values

When you use Lettuce, change the `validateClusterNodeMembership` parameter to `false`. Otherwise, when the topology changes, you might get `unknownPartition` errors.

## Enable Transport Layer Security (TLS)

This section explains the security benefits and performance implications of using Transport Layer Security (TLS), along with recommendations for its enablement.

### Security benefits

By using TLS, you get the following security benefits:

  * [**Identity and Access Management (IAM) authentication**](https://docs.cloud.google.com/memorystore/docs/cluster/about-iam-auth): TLS uses this type of authentication to protect against server spoofing attacks, such as person-in-the-middle attacks.
  * [**In-transit encryption**](https://docs.cloud.google.com/memorystore/docs/cluster/about-in-transit-encryption): Google Cloud's built-in encryption protects traffic within Google's network at an infrastructure level. However, this involves trusting both Google's host and network stacks. Although this encryption is transparent and enabled by default, it's not end-to-end. On the other hand, TLS uses in-transit encryption at the application layer. This end-to-end encryption gives you more control over your encryption keys and processes.
  * [**Authentication token protection**](https://docs.cloud.google.com/memorystore/docs/cluster/about-iam-auth#security_and_privacy): If you use IAM authentication, then enabling TLS minimizes the risk of exposing and leaking your authentication tokens.



### Performance implications

TLS impacts performance in the following ways:

  * [**Establish connections**](https://docs.cloud.google.com/memorystore/docs/cluster/connect-cluster-instance): A client and server that have established a TLS session can resume the session without repeating the resource-intensive process of establishing the connection between the client and the server. By enabling TLS resumption, you reduce the overhead of establishing a connection between the client and the server.

If you don't establish TLS resumption, then establishing connections is resource-intensive. For both new and existing connections, many connections between the client and the server might lead to connection timeouts. This can cause a snowball effect because Memorystore for Redis Cluster attempts to re-establish timed-out connections, which increases the resources it uses to establish connections.

  * [**Encrypt and decrypt data**](https://docs.cloud.google.com/memorystore/docs/cluster/security-overview): Data encryption and decryption involve CPU-intensive operations that impact both the client and the server. This can reduce your cluster's capacity and increase the cluster's latency.




### Recommendations

When considering whether to enable TLS, we recommend that you evaluate your security policies while considering the benefits and drawbacks of TLS. If you choose to enable TLS, then keep the following considerations in mind:

  * Enabling TLS resumption mitigates overhead for establishing connections. A connection between the client and the server is required only for the initial connection. However, a sudden expansion of the client's cluster size might result in a brief disruption that's caused by each new client host's initial full handshake.
  * Although some [client libraries](https://docs.cloud.google.com/memorystore/docs/cluster/apis) might not offer built-in controls to enable TLS, you can use custom code to integrate this functionality into your clusters.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
