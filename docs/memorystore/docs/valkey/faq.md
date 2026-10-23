---
url: https://docs.cloud.google.com/memorystore/docs/valkey/faq/
title: Memorystore for Valkey FAQ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:49.402726+00:00
---

# Memorystore for Valkey FAQ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Resources ](https://docs.cloud.google.com/memorystore/docs/valkey/resources)



Send feedback 

#  Memorystore for Valkey FAQ Stay organized with collections  Save and categorize content based on your preferences. 

In this page, you find answers to the following frequently asked questions (FAQ) about using Memorystore for Valkey:

  * How much CPU and memory do we recommend that you use?
  * How do you monitor how much CPU and memory that you use?
  * How do you set alerts to monitor your CPU and memory usage?
  * How many connections from your client application do we recommend that you keep open?
  * How do you monitor the number of your client connections for your instance?
  * What do you do if you have too many client connections?
  * Suppose you have an upcoming event that will spike traffic for your business? What do you do?
  * How do you secure your data?
  * What are the best practices for client code?
  * What are your options for data resiliency?
  * How do you get the best performance for your instance?
  * How can you optimize high availability for your instance?



## How much memory and CPU do we recommend that you use?

We recommend that your memory usage doesn't exceed 80% of the default `maxmemory`. We also recommend that you run at an average CPU utilization of 60%. This buffer ensures that you can tolerate the loss of a single availability zone, which is approximately one third of your total capacity. In this scenario, the average CPU utilization on the remaining nodes is approximately 90%.

## How do you monitor how much CPU and memory that you use?

To monitor the CPU usage for both your primary Memorystore for Valkey node and any of its read replicas, use the [`/instance/cpu/maximum_utilization`](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics#instance-level_metrics) metric. This metric measures the maximum CPU utilization across all nodes in your instance, from 0.0 (0%) to 1.0 (100%). For more information, see [CPU usage best practices](https://docs.cloud.google.com/memorystore/docs/valkey/general-best-practices#cpu_usage_best_practices).

To monitor the memory that your primary Memorystore for Valkey node and its read replicas use, use the [`/instance/node/memory/utilization`](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics#node-level_metrics) metric. This metric measures the memory utilization for a single node in your instance, from 0.0 (0%) to 1.0 (100%).

## How do you set alerts to monitor your CPU and memory usage?

To set monitoring alerts for your CPU and memory usage, use [Cloud Monitoring](https://docs.cloud.google.com/monitoring). For example, you can set an alert to notify you if the [`/instance/memory/maximum_utilization`](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics#instance-level_metrics) metric exceeds a threshold that you set. For more information, see [Set a Monitoring alert for memory usage](https://docs.cloud.google.com/memorystore/docs/valkey/monitor-instances#create-stackdriver-alert).

## How many connections from your client application do we recommend that you keep open?

We recommend that you use benchmarks for your client to determine the optimal setting. The recommended starting point from each client is one connection per Valkey node. For more information, see [Avoid connection overload on Valkey](https://docs.cloud.google.com/memorystore/docs/valkey/general-best-practices#avoid_connection_overload_on_valkey).

We also recommend that you enable pipelining for your client so that your client can process more requests and process them faster.

**Note:** If you use [blocking commands](https://valkey.io/topics/modules-blocking-ops/) such as `BLPOP` or `BRPOP`, then you might want to use more than one connection per Valkey node.

## How do you monitor the number of your client connections for your instance?

To monitor the number of client connections that you use, use the [`/instance/node/clients/connected_clients`](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics#node-level_metrics) metric. This metric measures the number of clients that are connected to each node of your instance.

## What do you do if you have too many client connections?

The maximum number of your client connections, which you can find by using the [`/instance/clients/maximum_connected_clients`](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics#instance-level_metrics) metric, must be less than the value that's associated with the [`maxclients`](https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations) parameter. If the values are equal, then do the following:

  * Stop any leaked or unnecessary connections by using the [`client kill`](https://valkey.io/commands/client-kill/) command.
  * Check the node type for your instance. If the [maximum number of clients for the node type](https://docs.cloud.google.com/memorystore/docs/valkey/quotas#max_clients) is equal to the maximum value that Memorystore for Valkey supports for the node type, then change your client's connection pool size or use a larger node type. For more information, see [Avoid connection overload on Valkey](https://docs.cloud.google.com/memorystore/docs/valkey/general-best-practices#avoid_connection_overload_on_valkey).



## Suppose you have an upcoming event that will spike traffic for your business? What do you do?

You can configure Memorystore for Valkey to meet your business needs. For this scenario, you can increase the capacity for your instance in the following ways:

  * You can [add shards to the instance](https://docs.cloud.google.com/memorystore/docs/valkey/scale-instance-capacity#scale_the_shard_count). This gives the instance more CPU usage to handle a larger volume of data or traffic. Your instance's capacity is determined by the number of shards in your instance. By adding shards, your application can handle an increased demand without performance degradation.
  * You can [change the node type to a larger node type](https://docs.cloud.google.com/memorystore/docs/valkey/scale-instance-capacity#scale_the_node_type). This gives the instance more memory. Your instance's capacity is determined by your instance's node type. For example, you can change the node type from a `standard-small` node type to a `highmem-medium` node type.



We recommend that you increase the capacity for your instance several days before the event. Also, to help you scale the capacity for your instance, and to increase the speed and reliability of scaling your instance, scale it during low periods of traffic. To learn how to monitor instance traffic, see [Monitor instances](https://docs.cloud.google.com/memorystore/docs/valkey/monitor-instances).

## How do you secure your data?

To secure your data, Memorystore for Valkey provides you with the following mechanisms:

  * [**Identity and Access Management (IAM) authentication**](https://docs.cloud.google.com/memorystore/docs/valkey/about-iam-auth): use IAM to help you manage login access for your users and service accounts. IAM-based authentication integrates with Valkey AUTH, letting you rotate credentials (IAM tokens) seamlessly without relying on static passwords.
  * [**In-transit encryption**](https://docs.cloud.google.com/memorystore/docs/valkey/about-in-transit-encryption): encrypt all Valkey traffic using the Transport Layer Security (TLS) protocol. When in-transit encryption is enabled, Valkey clients communicate across a connection securely. Valkey clients that aren't configured for TLS are blocked.



## What are the best practices for client code?

To use client code with Memorystore for Valkey optimally, we recommend that you use the following best practices:

  * To connect your application to a Memorystore for Valkey [Cluster Mode Enabled](https://docs.cloud.google.com/memorystore/docs/valkey/cluster-mode-enabled-and-disabled) instance, use a client that we recommend, such as [valkey-go](https://github.com/valkey-io/valkey-go), [iovalkey](https://github.com/valkey-io/iovalkey), [valkey-py](https://github.com/valkey-io/valkey-py), or [Valkey GLIDE](https://github.com/valkey-io/valkey-glide).

If you use a different client, then make sure that you use a cluster-aware Valkey client that maintains a map of hash slots to the corresponding nodes in the instance. As a result, requests can be sent to the correct nodes. This prevents performance overhead that's caused by redirections. For more information, see [Valkey client best practices](https://docs.cloud.google.com/memorystore/docs/valkey/general-best-practices#valkey_client_best_practices).

  * We recommend that you set your connection timeout intervals to five seconds and your request timeout intervals to 10 seconds. If you set your timeouts to smaller intervals, then Memorystore for Valkey might experience reconnection storms, which can put the service at risk.

  * Use [exponential backoff](https://docs.cloud.google.com/memorystore/docs/valkey/exponential-backoff) as a standard error handling strategy for network applications when the client retries a failed request periodically with increasing delays between requests.

  * Use our [client library code samples](https://docs.cloud.google.com/memorystore/docs/valkey/client-library-code-samples). As an example, the default values for the [valkey-go](https://github.com/valkey-io/valkey-go) client meet all of our recommendations so you don't have to configure anything for this client.




## What are your options for data resiliency?

Memorystore for Valkey provides you with the following features for data resiliency:

  * [**High availability**](https://docs.cloud.google.com/memorystore/docs/valkey/ha-and-replicas): Memorystore for Valkey provides redundant capacity in replica nodes. If a failure occurs, then Memorystore for Valkey can use this capacity to operate without any downtime.

  * [**Persistence**](https://docs.cloud.google.com/memorystore/docs/valkey/persistence-overview): When your environment crashes unexpectedly, Memorystore for Valkey restores the environment automatically. This is known as _persistence_.

Memorystore for Valkey offers the following type of persistence:

    * **Redis Database (RDB) persistence** : protect your data by saving snapshots of your data on durable storage. You choose the frequency of these snapshots by selecting a [snapshot interval](https://docs.cloud.google.com/memorystore/docs/valkey/about-rdb-persistence). If node failures occur, then you can recover data even when failover isn't possible.

**Note** : You can use RDB persistence to back up your data up as frequently as once per hour with a negligible performance impact.
    * **Append-Only File (AOF) persistence** : use this type of persistence when you want to prioritize data durability. AOF persistence stores data durably by recording every write command to a log file called the AOF file. If a system failure or restart occurs, then the server replays AOF file commands sequentially to restore your data.

**Note** : You can use AOF persistence to save your data with a frequency of between  
0 seconds and 30 seconds, depending on your configuration. We recommend keeping the frequency at 1 second, which is the default. Syncing every second provides the best compromise between instance performance and data durability.

With AOF persistence, you have some latency and throughput impact. However, if you set the `appendfsync` sync setting to `always`, then the impact to your latency and throughput might be significantly higher. This setting saves data to storage for every write.

  * [**Backups**](https://docs.cloud.google.com/memorystore/docs/valkey/backups): restore your Memorystore for Valkey instances to a specific point in time manually. In addition, you can use backups to export and analyze data.

Backups are useful for the following scenarios:

    * **Disaster recovery** : use backups as part of a disaster recovery plan. If a disaster occurs, then you can restore your data to a new Memorystore for Valkey instance.
    * **Data migration** : migrate data between different Memorystore for Valkey instances. You can consolidate data or move it to a different region. You can also restore backups from Memorystore for Valkey instances.
    * **Share data** : share data between different teams or applications. This enables collaboration, offline data analytics, and data exchange.
    * **Compliance** : create periodic backups of cache data for compliance purposes.
    * **Schedule backups** : In addition to creating an on-demand backup, you can configure a backup schedule for an instance. As a result, Memorystore for Valkey initiates periodic backups for the instance.
  * [**Cross-region replication**](https://docs.cloud.google.com/memorystore/docs/valkey/about-cross-region-replication): create secondary instances from a primary instance to make your instance available for reads in different regions. Secondary instances also provide redundancy for disaster recovery scenarios in case of regional outages.

Cross-region replication on Memorystore for Valkey provides you with the following benefits:

    * **Disaster recovery** : If the primary instance's region becomes unavailable, then you can detach or switchover to a secondary instance in another region to serve read and write requests. Secondary instances serve read requests without issuing a switchover or detach command.
    * **Geographically distributed data** : Distributing data geographically brings the data closer to you and decreases read latency.
    * **Geographic load balancing for read traffic** : If slow or overloaded connections occur in one region, then you can route traffic to another region.



## How do you get the best performance for your instance?

To optimize the performance for your Memorystore for Valkey instance, do the following:

  * Follow the best practices for [memory management](https://docs.cloud.google.com/memorystore/docs/valkey/general-best-practices#memory_management_best_practices) and [CPU usage](https://docs.cloud.google.com/memorystore/docs/valkey/general-best-practices#cpu_usage_best_practices) because these practices result in the best performance for your instance.
  * Use [audit logs](https://docs.cloud.google.com/memorystore/docs/valkey/audit-logging#available-logs) to monitor the access of your instance. As a result, you can determine whether there are any issues associated with administrator activity for the instance (the `Admin Activity` audit log) or users accessing instance data (the `Data Access` audit log).
  * Use [read replicas](https://docs.cloud.google.com/memorystore/docs/valkey/ha-and-replicas). In Memorystore for Valkey, replication is asynchronous. Therefore, the data in the primary node doesn't appear in the replicas immediately. If you can handle data that's slightly stale, then use read replicas. This provides you with substantial read throughput and latency improvements.
  * Avoid using resource-intensive Valkey commands. Using these commands might result in the following performance issues:

    * High latency and client timeouts
    * Memory pressure caused by commands that increase memory usage
    * Data loss during node replication and synchronization because the Valkey main thread is blocked
    * Starved health checks, observability, and replication

Instead of using these commands, use commands that are more resource-efficient. For example, for scanning your entire keyspace, don't use the `KEYS` command. Instead, use `SCAN`.

For more information about resource-intensive Valkey commands and their resource-efficient alternatives, see [Resource-intensive Valkey commands](https://docs.cloud.google.com/memorystore/docs/valkey/general-best-practices#resource-intensive-valkey-commands).

  * If your business needs allow you to set an expiration time for your data, then we recommend that you do so. Setting an expiration time reduces memory consumption.

  * [Upgrade the version](https://docs.cloud.google.com/memorystore/docs/valkey/upgrade-valkey-version) of your Memorystore for Valkey instance to the latest instance version. Newer software versions have reliability and performance improvements.

  * Modify the value of the `maxmemory-policy` parameter. This parameter specifies the behavior Valkey follows when your instance data reaches the `maxmemory` limit.

When your instance memory is full, and a new write comes in, Valkey evicts keys to make room for the write based on your instance's `maxmemory` policy. If the value of the  
`maxmemory-policy` parameter is set to `noeviction`, then Memorystore for Valkey returns an error when your instance reaches its maximum memory. However, Memorystore for Valkey doesn't overwrite or evict data. To improve the availability of your instance, change the value of the `maxmemory-policy` parameter so that Memorystore for Valkey can evict keys.

For more information about the different values that you can set for the `maxmemory-policy` parameter, see [Maxmemory policies](https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations#maxmemory_policies). For more information about updating this parameter, see [Update a configuration parameter](https://docs.cloud.google.com/memorystore/docs/valkey/configure-instances#update-configuration-parameter).

  * Tune your Memorystore for Valkey instance so that it has the cache hit ratio that you want. This helps you make your database the right size so that it can handle the appropriate percentage of hits.

To tune an instance, do the following:

    1. Use the [`total_keyspace_hits_count`](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics) and [`total_keyspace_misses_count`](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics) monitoring metrics to determine the total number of successful lookup of keys for the instance and the total number of failed lookup of keys for the instance, respectively.
    2. Divide the total number of hits by the total number of hits and misses   
(that is, hits/(hits + misses)). The quotient is your hit ratio.
    3. To tune the instance to get the hit ratio that's right for you, scale the instance. You can scale the shard count in or out, or scale the node type up or down. For more information, see [About scaling instance capacity](https://docs.cloud.google.com/memorystore/docs/valkey/about-scaling-instance-capacity).

Increasing the hit ratio improves latency and throughput for your system. Find the balance that works for your performance, scaling, and cost goals.

  * By default, we recommend that you run performance benchmarks against your instance to determine if more connections increases performance without connection saturation. The recommended starting point is to configure your client to open one connection to each Valkey node.

  * Enable pipelining for your client so that your client can process more requests and process them faster. To configure the pipelining, use the client library. For more information, see the documentation associated with this library.




## How can you optimize high availability for your instance?

We recommend that you create [highly available](https://docs.cloud.google.com/memorystore/docs/valkey/ha-and-replicas), multi-zone instances as opposed to single-zone instances because of the better reliability that they provide.

If you create a high-availability instance, then we recommend that you use the [`/instance/node/replication/offset`](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics#node-level_metrics) metric. By using this metric, you can monitor the replication offset (in bytes) for a single node in your instance. _Replication offset_ is the number of bytes that Memorystore for Valkey hasn't replicated between the primary node and the read replicas.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
