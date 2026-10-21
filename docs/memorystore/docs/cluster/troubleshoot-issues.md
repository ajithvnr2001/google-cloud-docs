---
url: https://docs.cloud.google.com/memorystore/docs/cluster/troubleshoot-issues/
title: Troubleshoot issues \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:04:14.888731+00:00
---

# Troubleshoot issues  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/troubleshoot-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Troubleshoot issues Stay organized with collections  Save and categorize content based on your preferences. 

This page explains various error scenarios, and provides guidance for resolving the errors.

## Replication scenarios

This section explains replication issues that might occur with your cluster.

### How do you monitor replication lags?

Memorystore for Redis Cluster has the [`/cluster/replication/maximum_offset_diff`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#cloud-monitoring-cluster-metrics) metric. This metric monitors the maximum replication offset difference (in bytes) for a node in a primary cluster.

By keeping the replication offset difference low, replicas can perform incremental sync operations more frequently and at a lower cost than full sync operations.

We recommend that you set a threshold for the `maximum_offset_diff` metric. If the threshold is exceeded, then Memorystore for Redis Cluster can notify you by an alert.

Based on the [node type](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#choose_a_node_type) for your cluster, we recommend that you set the threshold, as follows:

  * If the node type is `redis-shared-core-nano`, `redis-standard-small`, `redis-highmem-medium`, `redis-highcpu-medium`, or `redis-standard-large`, then set the threshold to be less than 64 MB.

  * If the node type is `redis-highmem-xlarge` or `redis-highmem-2xlarge`, then set the threshold to be less than 1 GB.


**Caution** : We recommend that you use the `redis-shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Redis Cluster in a production environment, then we recommend using another node type. For more information about these node types, see [Choose a node type](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#choose_a_node_type).

## Connectivity error scenarios

This section explains connectivity issues that your cluster might encounter.

### Connection error caused by firewall rules

If you don't allow the correct ports on your firewall, then your cluster might encounter connection errors because the firewall might block the ports that Memorystore for Redis Cluster uses.

For all of your cluster's Private Service Connect endpoints, you must allow TCP port 6379, as well as TCP ports 11000 through 13047. For more information about these endpoints, see [Reserved network addresses](https://docs.cloud.google.com/memorystore/docs/cluster/networking#reserved_network_addresses).

### Connection error caused by organization policies

You might have an organization policy that blocks your Private Service Connect connections to your cluster.

If your organization policy uses the `.restrictPrivateServiceConnectProducer` policy, then allow the `961333125034` folder, which is a folder specifically for Memorystore for Redis Cluster. For example:
    
    
    name: organizations/Consumer-org-1/policies/compute.restrictPrivateServiceConnectProducer
    spec:
        rules:
          - values:
              allowedValues:
              - under:folders/961333125034
    

If your organization policy uses the `.disablePrivateServiceConnectCreationForConsumers` policy, then allow `SERVICE_PRODUCERS`. For example:
    
    
    name: organizations/Consumer-org-1/policies/compute.disablePrivateServiceConnectCreationForConsumers
    spec:
        rules:
          - values:
              allowedValues:
              - SERVICE_PRODUCERS
    

### Connection error caused by unresponsive connections

We strongly recommend configuring your client application to detect unresponsive connections to Memorystore for Redis Cluster. When an unresponsive connection is detected, the client must reset it. To build a resilient application, we recommend the following client configurations:

  * **Configure TCP keep-alive parameters** : set the `TCP keepalive time`, `TCP keepalive interval`, and `TCP keepalive probes` parameters so that clients detect and drop unresponsive connections proactively, even when connections are idle. For example, if you set the `TCP keepalive time` parameter to 30 seconds, `TCP keepalive interval` to 10 seconds, and `TCP keepalive probes` to 3, then clients reset unresponsive idle connections within a minute.
  * **Configure TCP user timeouts** : set this timeout in your clients to reset connections that have outstanding requests and stop responding. For example, if you set the timeout to 15 seconds, then clients reset unresponsive connections that have outstanding requests after 15 seconds.



## CPU usage scenarios

This section explains CPU usage issues that your cluster might encounter.

### The output buffer of your cluster runs out of space

If the output buffer of your cluster runs out of space, then do the following:

  * Set a smaller value for the [`maxmemory`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-instance-configurations#modifiable_configuration_parameters) parameter.
  * Use the [`allkeys-lru`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-instance-configurations#maxmemory_policies) `maxmemory` policy.



When the memory of your cluster is full, and a new write comes in, Memorystore for Redis Cluster evicts keys to make room for the write, based on your cluster's `maxmemory` policy. The `allkeys-lru` policy evicts the least recently used (LRU) keys from the entire keyset.

We recommend that you monitor your cluster's `maxmemory` and used memory. This helps you to know if your cluster reaches the provisioned cluster capacity. Also, by reducing the value for the `maxmemory` parameter, you get more space for the overhead.

### Why might external metrics be missing for your cluster?

If your cluster either experiences high CPU utilization or the cluster's resources become exhausted (for example, by having too many connections), then the cluster might misbehave and external metrics might be missing.

### Isolate the source of your cluster's latency

To determine whether the latency that you experience originates from your cluster, your client application, or your network environment, use the `redis-cli` tool to run a continuous latency test.

To isolate the source of your cluster's latency, do the following:

  1. Connect to a Compute Engine VM that's located in the same region and VPC network as your cluster.

  2. If it's not already installed, then install the `redis-cli` tool on your VM.

     * For Debian or Ubuntu-based VMs, run the following command:
           
           sudo apt-get install redis-tools
           

     * For RHEL or CentOS-based VMs, run the following command:
           
           sudo yum install redis
           

  3. To measure the cluster's latency in milliseconds, run the following command:
         
         redis-cli --latency -h DISCOVERY_ENDPOINT_ADDRESS -p PORT
         

If your cluster uses in-transit encryption, then append the `--tls` flag and specify your certificate authorities (CAs) to connect.

Make the following replacements:

     * DISCOVERY_ENDPOINT_ADDRESS: the IP address of your cluster's discovery endpoint.
     * PORT: the port number that's reserved for your cluster's discovery endpoint. Typically, this port number is 6379.
  4. Let the command run for a few minutes. The tool continuously pings the server and calculates the minimum, maximum, and average latency values.

  5. To stop the command and view the results, press `Ctrl+C`.




If the command outputs a consistently low average latency (typically 1 millisecond or less), then the cluster is healthy and responding quickly.

If the command shows consistently low latency, but your client application still experiences delays, then the following issues might cause the latency:

  * **Network** : Traffic routed across different regions or zones between your client and the cluster might introduce significant network delays.
  * **Client** : High CPU or memory utilization on the client, exhausted connection pools, or application logic bottlenecks might increase the total round-trip time that the client experiences.



## Persistence scenarios

This section explains persistence issues that might occur with your cluster.

### Your write traffic exceeds Memorystore for Redis Cluster's ability to compact and reclaim space through AOF rewriting

If this situation occurs, then the Append-Only File (AOF) grows faster than the rewrite process can manage. This leads to disk exhaustion, causes write failures, and blocks operations that require replica creation and full synchronization.

Memorystore for Redis Cluster implemented guardrails to regulate the write throughput. This ensures that AOF rewriting can keep pace with sustained high-write workloads.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
