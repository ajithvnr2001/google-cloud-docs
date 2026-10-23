---
url: https://docs.cloud.google.com/memorystore/docs/valkey/general-best-practices/
title: Best practices for Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:31.048516+00:00
---

# Best practices for Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/general-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Best practices for Memorystore for Valkey Stay organized with collections  Save and categorize content based on your preferences. 

This page provides guidance on using Memorystore for Valkey optimally. This page also points out potential issues to avoid.

## Memory management best practices

This section describes strategies for managing instance memory so that Memorystore for Valkey works efficiently for your application.

### Memory management concepts

  * **Memory usage** : the amount of memory that your instance uses. You have a fixed memory capacity. You can use [metrics](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics) to monitor how much memory you're using.

  * **Eviction policy** : Memorystore for Valkey uses the `volatile-lru` eviction policy. You can use Valkey commands like the `EXPIRE` command to set evictions for keys.




### Monitor memory usage for an instance

To monitor the memory usage for a Memorystore for Valkey instance, we recommend that you view the [`/instance/memory/maximum_utilization`](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics#instance-level_metrics) metric. If the memory usage of the instance approaches 80% and you expect data usage to grow, then [scale up the size of the instance](https://docs.cloud.google.com/memorystore/docs/valkey/scale-instance-capacity#scale_the_node_type) to make room for new data.

If the instance has high memory usage, then do the following to improve performance:

  * [Scale up the instance size](https://docs.cloud.google.com/memorystore/docs/valkey/scale-instance-capacity#scale_the_node_type).
  * Lower the [`maxmemory`](https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations#modifiable_configuration_parameters) configuration parameter.



If you run into issues, then contact [Google Cloud Customer Care](https://docs.cloud.google.com/support).

### Scale shards in Cluster Mode Enabled

When you [scale the number of shards](https://docs.cloud.google.com/memorystore/docs/valkey/scale-instance-capacity) in an instance, we recommend that you scale during periods of low writes. Scaling during periods of high usage can put memory pressure on your instance because of memory overhead that's caused by replication or slot migration.

If your Valkey use case uses key evictions, then scaling to a smaller instance size can reduce your cache hit ratio. In this circumstance, however, you don't need to worry about losing data, since key eviction is expected.

For Valkey use cases where you don't want to lose keys, you should only scale down to a smaller instance that still has enough room for your data. Your new target shard count should allow for at least 1.5 times the memory used by data. In other words, you should provision enough shards for 1.5 times the amount of data in your instance. You can use the [`/instance/memory/total_used_memory` metric](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics) to see how much data is stored in your instance.

## CPU usage best practices

If an unexpected zonal outage occurs, this leads to reduced CPU resources for your instance due to lost capacity from nodes in the unavailable zone. We recommend using [highly available](https://docs.cloud.google.com/memorystore/docs/valkey/ha-and-replicas) instances. Using multiple replicas per shard (as opposed to one replica per shard) provides additional CPU resources during an outage. You can have up to five replicas per shard.

Additionally, we recommend managing node CPU usage so that nodes have enough CPU overhead to handle additional traffic from lost capacity if an unexpected zonal outage happens. You should monitor CPU usage for primaries and replicas using the [Main Thread CPU Seconds `/instance/cpu/maximum_utilization`](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics) metric.

Depending on the number of replicas you provision per node, we recommend the following `/instance/cpu/maximum_utilization` CPU usage targets:

  * For instances with one replica per node, target a `/instance/cpu/maximum_utilization` value of 0.5 seconds for the primary and 0.5 seconds for the replica.
  * For instances with two replicas per node or greater, target a `/instance/cpu/maximum_utilization` value of 0.9 seconds for the primary and 0.5 seconds for each replica.



If values for the metric exceed these recommendations, then we recommend scaling up the number of shards in your instance. If you have fewer than five replicas for your instance, then you can also scale up the number of replicas, up to a maximum of five replicas.

If your instance either experiences high CPU utilization or the instance's resources become exhausted (for example, by having too many connections), then the instance might misbehave and external metrics might be missing.

### Resource-intensive Valkey commands

We strongly recommend that you avoid using Valkey commands that are resource-intensive. Using these commands might result in the following performance issues:

  * High latency and client timeouts
  * Memory pressure caused by commands that increase memory usage
  * Data loss during node replication and synchronization because the Valkey main thread is blocked
  * Starved health checks, observability, and replication



The following table lists examples of Valkey commands that are resource-intensive and provides you with alternatives that are resource-efficient.

**Tip** : In addition to being resource-intensive, as your total data size increases, so does the cost of using these commands.

To find which long-running commands you use, use [`SLOWLOG`](https://valkey.io/commands/slowlog/). This tool provides you with a list of commands that take the longest to run. As a result, you know the commands that cause latency issues. To determine resource-efficient alternatives for these commands, refer to the following table.

**Category** | **Resource-intensive command** | **Resource-efficient alternative**  
---|---|---  
Run for the entire keyspace | `KEYS` | `SCAN`  
Run for a variable-length keyset | `LRANGE` | Limit the size of the range that you use for a query.  
`ZRANGE` | Limit the size of the range that you use for a query.  
`HGETALL` | `HSCAN`  
`SMEMBERS` | `SSCAN`  
Block the running of a script | `EVAL` | Ensure that your script doesn't run indefinitely.  
`EVALSHA` | Ensure that your script doesn't run indefinitely.  
Remove files and links | `DELETE` | `UNLINK`  
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

To determine when to scale based on memory usage, monitor the `/instance/memory/average_utilization` and `/instance/memory/maximum_utilization` metrics. For more information about these metrics, see [Supported monitoring metrics](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics).

If your instance meets either of the following conditions, then consider triggering a scale-out operation:

  * The average memory utilization of your instance exceeds the suggested threshold of 70%.
  * The maximum memory utilization exceeds 80% and the average memory utilization exceeds 50%.



If your instance meets either of the following conditions, then consider triggering a scale-in operation:

  * The average memory utilization of your instance drops below the suggested threshold of 50%.
  * The maximum memory utilization drops below 60% and the average memory utilization drops below 40%.



### CPU utilization scaling

To determine when to scale based on CPU usage, monitor the `/instance/cpu/average_utilization` and `/instance/cpu/maximum_utilization` metrics.

If your instance meets either of the following conditions, then consider triggering a scale-out operation:

  * The average CPU utilization of your instance exceeds the suggested threshold of 70%.
  * The maximum CPU utilization exceeds 80% and the average CPU utilization exceeds 50%.



If your instance meets either of the following conditions, then consider triggering a scale-in operation:

  * The average CPU utilization of your instance drops below the suggested threshold of 50%.
  * The maximum CPU utilization drops below 60% and the average CPU utilization drops below 40%.



### Scaling to mitigate hotspots

Memorystore for Valkey provides average and maximum variations of the same metric, which you can use to identify hotspots for that metric family. The maximum value represents the instance node that's most heavily loaded, while the average value represents the load for the entire instance. If the maximum value is significantly higher than the average value, then this indicates that a specific node is loaded disproportionately (a hotspot). To resolve this issue, we recommend that you scale out your instance. For more information, see [Scale instance capacity](https://docs.cloud.google.com/memorystore/docs/valkey/scale-instance-capacity).

When you observe a significant divergence between the average and maximum variations, you can run the `INFO memory` and `INFO cpu` commands against the instance nodes to gather real-time data directly from the instance. For more information about using these commands, see [INFO](https://valkey.io/commands/info/) in the Valkey documentation.

## Valkey client best practices

### Avoid connection overload on Valkey

To mitigate the impact caused by a sudden influx of connection, we recommend the following:

  * Determine the client connection pool size that's best for you. A good starting size for each client is one connection per Valkey node. You can then benchmark to see if more connections helps without saturating the maximum allowed connection count.

  * When the client disconnects from the server because the server times out, retry with exponential backoff with jitter. This helps to avoid multiple clients overloading the server simultaneously.




### Detect and handle unresponsive connections

We strongly recommend configuring your client application to detect unresponsive connections to Memorystore for Valkey. When an unresponsive connection is detected, the client must reset it. To build a resilient application, we recommend the following client configurations:

  * **Configure TCP keep-alive parameters** : set the `TCP keepalive time`, `TCP keepalive interval`, and `TCP keepalive probes` parameters so that clients detect and drop unresponsive connections proactively, even when connections are idle. For example, if you set the `TCP keepalive time` parameter to 30 seconds, `TCP keepalive interval` to 10 seconds, and `TCP keepalive probes` to 3, then clients reset unresponsive idle connections within a minute.
  * **Configure TCP user timeouts** : set this timeout in your clients to reset connections that have outstanding requests and stop responding. For example, if you set the timeout to 15 seconds, then clients reset unresponsive connections that have outstanding requests after 15 seconds.



### For Cluster Mode Enabled instances

Your application must use a cluster-aware Valkey client when connecting to a Memorystore for Valkey Cluster Mode Enabled instance. For examples of cluster-aware clients and sample configurations, see [Client library code samples](https://docs.cloud.google.com/memorystore/docs/valkey/client-library-code-samples). Your client must maintain a map of hash slots to the corresponding nodes in the instance to send requests to the correct nodes. This prevents performance overhead that's caused by redirections.

#### Client mapping

Clients must obtain a complete list of slots and the mapped nodes in the following situations:

  * When the client is initialized, it must populate the initial slot to nodes mapping.

  * When a `MOVED` redirection is received from the server, such as in the situation of a failover when all slots served by the former primary node are taken over by the replica, or re-sharding when slots are being moved from the source primary to the target primary node.

  * When a `CLUSTERDOWN` error is received from the server or connections to a particular server run into timeouts persistently.

  * When a `READONLY` error is received from the server. This can happen when a primary is demoted to a replica.

  * Additionally, clients should periodically refresh the topology to keep the clients warmed up for any changes and learn about changes that may not result in redirections or errors from the server, such as when new replica nodes are added. Note that any stale connections should also be closed as part of the topology refresh to reduce the need to handle failed connections during command runtime.




#### Client discovery

Client discovery is usually done by issuing a `SLOTS`, `NODES`, or `CLUSTER SHARDS` command to the Valkey server. We recommend using the `CLUSTER SHARDS` command. `CLUSTER SHARDS` replaces the `SLOTS` command (deprecated), by providing a more efficient and extensible representation of the instance.

The size of the response for the client discovery commands can vary based on the instance size and topology. Larger instances with more nodes produce a larger response. As a result, it's important to ensure that the number of clients doing the node topology discovery doesn't grow unbounded.

These node topology refreshes are expensive on the Valkey server but are also important for application availability. Therefore it is important to ensure that each client makes a single discovery request at any given time (and caches result in-memory), and the number of clients making the requests be kept bounded to avoid overloading the server.

For example, when the client application starts up or loses connection from the server and must perform node discovery, one common mistake is that the client application makes several reconnection and discovery requests without adding [exponential backoff](https://docs.cloud.google.com/memorystore/docs/valkey/exponential-backoff) upon retry. This can render the Valkey server unresponsive for a prolonged period of time, causing very high CPU utilization.

#### Use a discovery endpoint for node discovery

Use the Memorystore for Valkey discovery endpoint to perform node discovery. The discovery endpoint is highly available and is load balanced across all the nodes in the instance. Moreover, the discovery endpoint attempts to route the node discovery requests to nodes with the most up-to-date topology view.

### For Cluster Mode Disabled instances

When your application connects to a Cluster Mode Disabled instance, the application must connect to the primary endpoint to write to the instance and to retrieve the most recent writes. Your application can also connect to the reader endpoint to read from replicas and to isolate traffic from the primary node.

Because Cluster Mode Disabled instances only have one shard, they don't use an in-memory topology. Therefore, topology refresh isn't applicable.

During failovers and maintenance events, connections to the instance drop. To ensure that your application reconnects successfully after these events, implement a retry mechanism with exponential backoff.

You can use the create-before-destroy strategy when you perform maintenance on your instance. For more information about this strategy, see [Create-before-destroy lifecycle strategy](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance#create-before-destroy_lifecycle_strategy).

If you use this strategy, then you might receive the following error message:

`READONLY You can't write against a read only replica.`

To resolve this issue, stop the connection to your instance. Then, recreate the connection.

## Persistence best practices

This section explains best practices for [persistence](https://docs.cloud.google.com/memorystore/docs/valkey/persistence-overview).

### RDB persistence and adding replicas

For best results of backing up your instance with RDB snapshots or adding replicas to your instance, use the following best practices:

#### Memory management

RDB snapshots use a process fork and ['copy-on-write' mechanism](https://valkey.io/topics/persistence/) to take a snapshot of node data. Depending on the pattern of writes to nodes, the used memory of the nodes grows as pages touched by the writes are copied. The memory footprint can be up to double the size of the data in the node.

To ensure that nodes have sufficient memory to complete the snapshot, keep or set [`maxmemory`](https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations#modifiable_configuration_parameters) at 80% of the node capacity so that 20% is reserved for overhead. This memory overhead, in addition to monitoring snapshots, helps you manage your workload to have successful snapshots. Also, when you add replicas, lower write traffic as much as possible. For more information, see Monitor memory usage for an instance.

**Note** : If you add a replica to an instance that uses more than 80% of the instance's maximum memory, then the operation fails and you receive an error message.

To resolve this issue, reduce your instance's memory usage in one of the following ways:

  * Lower your instance's memory footprint to less than 80% of the node's maximum allowed memory.
  * [Scale the node type](https://docs.cloud.google.com/memorystore/docs/valkey/scale-instance-capacity#scale_the_node_type) for your instance so that it has more memory.



After your instance's memory usage is below the 80% threshold, add the replica again.

#### Stale snapshots

Recovering nodes from a stale snapshot can cause performance issues for your application as it tries to reconcile a significant amount of stale keys or other changes to your database such as a schema change. If you are concerned about recovering from a stale snapshot, you can disable the RDB persistence feature. Once you re-enable persistence, a snapshot is taken at the next scheduled snapshot interval.

#### Performance impact of RDB snapshots

Depending on your workload pattern RDB snapshots can impact the performance of the instance and increase latency for your applications. You can minimize the performance impact of RDB snapshots by scheduling them to run during periods of low instance traffic if you are comfortable with less frequent snapshots.

For example, if your instance has low traffic from 1 AM to 4 AM, you can set the start time to 3 AM and set the interval to 24 hours.

If your system has a constant load and requires frequent snapshots, then we recommend that you carefully evaluate the performance impact and weigh the benefits of using RDB snapshots for the workload.

#### Add a replica

Adding a replica requires an RDB snapshot. For more information about RDB snapshots, see Memory management.

## When to use a single-zone instance

If you configure an instance so that it doesn't use replicas, then we recommend that you use a [single-zone instance](https://docs.cloud.google.com/memorystore/docs/valkey/single-zone-instances). Here's why:

### Cost and performance

If minimizing your cost and having peak performance for your clients that are located in the same region are your primary drivers, then we recommend that you choose a single-zone instance.

### Minimize your outage impact

When you choose a single-zone instance, zonal outages are less likely to impact your instance. By placing all nodes within a single zone, the chance of a zonal outage affecting your server drops from 100% to 33%. There's a 33% chance that the zone where your instance is located goes down, as opposed to a 100% chance that nodes, which are located in the unavailable zone, are impacted.

### Rapid recovery

If a zonal outage occurs for a single-zone instance, then Memorystore for Valkey streamlines the recovery of your data. You can provision a new instance in a functioning zone quickly and redirect your application for minimally interrupted operations.

## Capacity planning best practices

To ensure that you can successfully provision resources and build resilient architectures, we recommend the following capacity planning best practices:

  * **Deploy across multiple locations** : if you can't create an instance in your preferred zone because of temporary resource constraints, then try creating the instance either in a different zone within the same region or in a different region.
  * **Use cross-region access** : configure your clients to access your instances that are located in different regions. If you need to provision an instance that's in a different region because of local resource constraints, then your clients can connect to the instance.
  * **Use cross-region replication** : to promote a secondary instance in an alternate region to a primary read or write instance for disaster recovery, perform a switchover.



## Enable Transport Layer Security (TLS)

This section explains the security benefits and performance implications of using Transport Layer Security (TLS), along with recommendations for its enablement.

### Security benefits

By using TLS, you get the following security benefits:

  * [**Identity and Access Management (IAM) authentication**](https://docs.cloud.google.com/memorystore/docs/valkey/about-iam-auth): TLS uses this type of authentication to protect against server spoofing attacks, such as person-in-the-middle attacks.
  * [**In-transit encryption**](https://docs.cloud.google.com/memorystore/docs/valkey/about-in-transit-encryption): Google Cloud's built-in encryption protects traffic within Google's network at an infrastructure level. However, this involves trusting both Google's host and network stacks. Although this encryption is transparent and enabled by default, it's not end-to-end. On the other hand, TLS uses in-transit encryption at the application layer. This end-to-end encryption gives you more control over your encryption keys and processes.
  * [**Authentication token protection**](https://docs.cloud.google.com/memorystore/docs/valkey/about-iam-auth#security_and_privacy): If you use IAM authentication, then enabling TLS minimizes the risk of exposing and leaking your authentication tokens.



### Performance implications

TLS impacts performance in the following ways:

  * [**Establish connections**](https://docs.cloud.google.com/memorystore/docs/valkey/connect-instance): A client and server that have established a TLS session can resume the session without repeating the resource-intensive process of establishing the connection between the client and the server. By enabling TLS resumption, you reduce the overhead of establishing a connection between the client and the server.

If you don't establish TLS resumption, then establishing connections is resource-intensive. For both new and existing connections, many connections between the client and the server might lead to connection timeouts. This can cause a snowball effect because Memorystore for Valkey attempts to re-establish timed-out connections, which increases the resources it uses to establish connections.

  * [**Encrypt and decrypt data**](https://docs.cloud.google.com/memorystore/docs/valkey/security-overview): Data encryption and decryption involve CPU-intensive operations that impact both the client and the server. This can reduce your instance's capacity and increase the instance's latency.




### Recommendations

When considering whether to enable TLS, we recommend that you evaluate your security policies while considering the benefits and drawbacks of TLS. If you choose to enable TLS, then keep the following considerations in mind:

  * Enabling TLS resumption mitigates overhead for establishing connections. A connection between the client and the server is required only for the initial connection. However, a sudden expansion of the client's instance size might result in a brief disruption that's caused by each new client host's initial full handshake.
  * Although some [client libraries](https://docs.cloud.google.com/memorystore/docs/valkey/apis) might not offer built-in controls to enable TLS, you can use custom code to integrate this functionality into your instances.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
