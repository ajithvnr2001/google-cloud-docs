---
url: https://docs.cloud.google.com/memorystore/docs/valkey/troubleshoot-issues/
title: Troubleshoot issues \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:43.135196+00:00
---

# Troubleshoot issues  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/troubleshoot-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Troubleshoot issues Stay organized with collections  Save and categorize content based on your preferences. 

This page explains various error scenarios, and provides guidance for resolving the errors.

## Replication scenarios

This section explains replication issues that might occur with your instance.

### How do you monitor replication lags?

Memorystore for Valkey has the [`/instance/replication/maximum_offset_diff`](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics#instance-level_metrics) metric. This metric monitors the maximum replication offset difference (in bytes) for a node in a primary instance.

By keeping the replication offset difference low, replicas can perform incremental sync operations more frequently and at a lower cost than full sync operations.

We recommend that you set a threshold for the `maximum_offset_diff` metric. If the threshold is exceeded, then Memorystore for Valkey can notify you by an alert.

Based on the [node type](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#choose-node-type) for your instance, we recommend that you set the threshold, as follows:

  * If the node type is `shared-core-nano`, `custom-pico`, `custom-micro`, `custom-mini`, `standard-small`, `highmem-medium`, `highcpu-medium`, or `standard-large`, then set the threshold to be less than 64 MB.

  * If the node type is `highmem-xlarge` or `highmem-2xlarge`, then set the threshold to be less than 1 GB.


**Caution** : We recommend that you use the `shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Valkey in a production environment, then we recommend using another node type. For more information about these node types, see [Choose a node type](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#choose-node-type).

### What do you do if there's a replication lag between your primary instance and its replicas?

There might be a significant replication lag if the primary instance has too many write operations, and the replicas can't catch up to replicate these operations. To resolve this issue, we recommend that you scale the capacity of the instance by [increasing the number of shards for the instance](https://docs.cloud.google.com/memorystore/docs/valkey/scale-instance-capacity#scale_the_shard_count).

## CPU usage scenarios

This section explains CPU usage issues that your instance might encounter.

### What do you do if the output buffer of your instance runs out of space?

If the output buffer of your Memorystore for Valkey instance runs out of space, then do the following:

  * Set a smaller value for the [`maxmemory`](https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations#modifiable_configuration_parameters) parameter.
  * Use the [`allkeys-lru`](https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations#maxmemory_policies) `maxmemory` policy.



When the memory of your instance is full, and a new write comes in, Memorystore for Valkey evicts keys to make room for the write, based on your instance's `maxmemory` policy. The `allkeys-lru` policy evicts the least recently used (LRU) keys from the entire keyset.

We recommend that you monitor your instance's `maxmemory` and used memory. This helps you to know if your instance reaches the provisioned instance capacity. Also, by reducing the value for the `maxmemory` parameter, you get more space for the overhead.

### Why might external metrics be missing for your instance?

If your instance either experiences high CPU utilization or the instance's resources become exhausted (for example, by having too many connections), then the instance might misbehave and external metrics might be missing.

### How do you isolate the source of your instance's latency?

To determine whether the latency that you experience originates from your instance, your client application, or your network environment, use the `valkey-cli` tool to run a continuous latency test.

To isolate the source of your instance's latency, do the following:

  1. Connect to a Compute Engine VM that's located in the same region and VPC network as your instance.

  2. If it's not already installed, then install the `valkey-cli` tool on your VM.

     * For Debian or Ubuntu-based VMs, run the following command:
           
           sudo apt-get install valkey-tools
           

     * For RHEL or CentOS-based VMs, run the following command:
           
           sudo yum install valkey-tools
           

  3. To measure the instance's latency in milliseconds, run the following command:
         
         redis-cli --latency -h ENDPOINT_ADDRESS -p PORT
         

If your instance uses in-transit encryption, then append the `--tls` flag and specify your certificate authorities (CAs) to connect.

Make the following replacements:

     * ENDPOINT_ADDRESS: the IP address of your instance's endpoint.
     * PORT: the port number that's reserved for your instance's endpoint. Typically, this port number is 6379.
  4. Let the command run for a few minutes. The tool continuously pings the server and calculates the minimum, maximum, and average latency values.

  5. To stop the command and view the results, press `Ctrl+C`.




If the command outputs a consistently low average latency (typically 1 millisecond or less), then the instance is healthy and responding quickly.

If the command shows consistently low latency, but your client application still experiences delays, then the following issues might cause the latency:

  * **Network** : Traffic routed across different regions or zones between your client and the instance might introduce significant network delays.
  * **Client** : High CPU or memory utilization on the client, exhausted connection pools, or application logic bottlenecks might increase the total round-trip time that the client experiences.



## Memory management scenarios

This section explains memory management issues that your instance might encounter.

### Which metric can you use to determine that your instance is under memory stress?

To monitor the [memory usage](https://docs.cloud.google.com/memorystore/docs/valkey/general-best-practices#monitor-memory-usage) for a Memorystore for Valkey instance, we recommend that you view the [`/instance/memory/maximum_utilization`](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics#instance-level_metrics) metric. If the memory usage of the instance approaches 80% and you expect data usage to grow, then [scale up the size of the instance](https://docs.cloud.google.com/memorystore/docs/valkey/scale-instance-capacity) to improve performance and to make room for new data.

## Monitoring scenarios

This section explains monitoring issues that your instance might encounter.

### How do you set up alerts for Memorystore for Valkey?

You can use [Cloud Monitoring](https://docs.cloud.google.com/monitoring) to set alerts to notify you if any metrics exceed thresholds that you set for your instance. For more information about setting alerts in Cloud Monitoring, see [Set a Monitoring alert for memory usage](https://docs.cloud.google.com/memorystore/docs/valkey/monitor-instances#create-stackdriver-alert).

## Connection management scenarios

This section explains connection management issues that your instance might encounter.

### If you reach your connection limit or receive a connection timeout, then what do you do?

When you reach your connection limit, your client fails to connect to your server. This is known as a _connection rejection_.

If this happens, then do the following:

  * Use the [`/instance/node/stats/rejected_connections_count`](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics#node-level_metrics) metric to determine the number of connections that Memorystore for Valkey rejects because the instance node reaches the maximum clients limit.
  * Use the [`/instance/node/clients/connected_clients`](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics#node-level_metrics) metric to determine the number of clients connected to the instance node. This way, you can see if all of the nodes in the instance are under the limit.
  * Stop any leaked or undesired connections by using the [`client kill`](https://valkey.io/commands/client-kill/) command.
  * Reduce the connection count or pool size in the client application. For more information, see the documentation associated with the client application.
  * Adjust the maximum clients limit. For more information, see [Configure an instance](https://docs.cloud.google.com/memorystore/docs/valkey/configure-instances).
  * [Scale your instance up to a larger node type](https://docs.cloud.google.com/memorystore/docs/valkey/scale-instance-capacity#scale_the_node_type) so that your instance has a higher connection limit.



## Timeout scenarios

This section explains timeout issues that your instance might encounter.

### If you receive an I/O timeout, then what do you do?

When a read or write operation in Memorystore for Valkey fails to complete within a specified time, then an I/O timeout occurs. This timeout might happen because of various reasons. For example, one or more nodes of your instance might be overloaded.

If you receive an I/O timeout, then do the following:

  * Use the [`instance/cpu/maximum_utilization`](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics#instance-level_metrics) metric to determine the CPU utilization for a node in your instance, from 0.0 (0%) to 1.0 (100%). We recommend that all nodes have a CPU utilization percentage of less than 80%. For more information, see [CPU usage best practices](https://docs.cloud.google.com/memorystore/docs/valkey/general-best-practices#cpu_usage_best_practices).
  * When the client disconnects from the server because the server times out, retry with [exponential backoff](https://docs.cloud.google.com/memorystore/docs/valkey/exponential-backoff) and with [Jitter](https://jitter.video/). This helps to avoid multiple clients overloading the server simultaneously.



## Connectivity error scenarios

This section explains connectivity issues your instance might encounter.

### Connection error caused by firewall rules

If you don't allow the correct ports on your firewall, then your instance might encounter connection errors because the firewall might block the ports that Memorystore for Valkey uses.

For all of your instance's Private Service Connect endpoints, you must allow TCP port 6379, as well as TCP ports 11000 through 13047. For more information about these endpoints, see [Reserved network addresses](https://docs.cloud.google.com/memorystore/docs/valkey/networking#reserved_network_addresses).

### Connection error caused by organization policies

You can have an [organization policy](https://docs.cloud.google.com/vpc/docs/private-service-connect-security#org-policies) that blocks your Private Service Connect connections to your Memorystore for Valkey instance.

If your organization policy uses the `.restrictPrivateServiceConnectProducer` policy, then allowlist the `672235397475` folder number, which is a folder specifically for Memorystore for Valkey. For example:
    
    
    name: organizations/Consumer-org-1/policies/compute.restrictPrivateServiceConnectProducer
    spec:
        rules:
          - values:
              allowedValues:
              - under:folders/672235397475
    

If your organization policy uses the `.disablePrivateServiceConnectCreationForConsumers` policy, then allowlist `SERVICE_PRODUCERS`. For example:
    
    
    name: organizations/Consumer-org-1/policies/compute.disablePrivateServiceConnectCreationForConsumers
    spec:
        rules:
          - values:
              allowedValues:
              - SERVICE_PRODUCERS
    

### Connection error caused by unresponsive connections

We strongly recommend configuring your client application to detect unresponsive connections to Memorystore for Valkey. When an unresponsive connection is detected, the client must reset it. To build a resilient application, we recommend the following client configurations:

  * **Configure TCP keep-alive parameters** : set the `TCP keepalive time`, `TCP keepalive interval`, and `TCP keepalive probes` parameters so that clients detect and drop unresponsive connections proactively, even when connections are idle. For example, if you set the `TCP keepalive time` parameter to 30 seconds, `TCP keepalive interval` to 10 seconds, and `TCP keepalive probes` to 3, then clients reset unresponsive idle connections within a minute.
  * **Configure TCP user timeouts** : set this timeout in your clients to reset connections that have outstanding requests and stop responding. For example, if you set the timeout to 15 seconds, then clients reset unresponsive connections that have outstanding requests after 15 seconds.



### Handling errors for Cluster Mode Disabled instances

  * If the application connects to the read endpoint of an instance which has no read replicas, then the connection closes and the `ERR no replicas found` error message appears. In this case, either try to connect the application to the primary endpoint or add read replicas to the instance.

  * In the event of a failover, the existing connections from your application closes and the `ERR role change occurred` error message appears. You also see this error message if your application connects to the read endpoint of an instance, and all read replicas of the instance are failing. In this case, the application must retry the connection with [exponential backoff](https://docs.cloud.google.com/memorystore/docs/valkey/exponential-backoff).




## Persistence scenarios

This section explains persistence issues that might occur with your instance.

### Your write traffic exceeds Memorystore for Valkey's ability to compact and reclaim space through AOF rewriting

If this situation occurs, then the Append-Only File (AOF) grows faster than the rewrite process can manage. This leads to disk exhaustion, causes write failures, and blocks operations that require replica creation and full synchronization.

Memorystore for Valkey implemented guardrails to regulate the write throughput. This ensures that AOF rewriting can keep pace with sustained high-write workloads.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
