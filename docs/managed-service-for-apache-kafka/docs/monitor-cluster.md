---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/monitor-cluster/
title: Monitor a Google Cloud Managed Service for Apache Kafka cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:20.956343+00:00
---

# Monitor a Google Cloud Managed Service for Apache Kafka cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/monitor-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Monitor a Google Cloud Managed Service for Apache Kafka cluster Stay organized with collections  Save and categorize content based on your preferences. 

Managed Service for Apache Kafka collects metrics that you can use to monitor your Kafka clusters. This page describes how to view these metrics in the Google Cloud console.

## Overview

Managed Service for Apache Kafka exports several metrics available in the open-source Kafka distribution, as well as service-specific metrics like consumer group offset lag.

The metrics are organized into four resource categories:

  * **Cluster** : These metrics are useful for maintaining the overall health of a cluster.

  * **Topic** : These metrics include publisher and consumer rates and errors. They monitor the overall health of Kafka applications, and issues specific to a broker.

  * **Topic Partition** : These metrics are intended for monitoring and debugging performance problems specific to individual partitions, such as uneven key distribution.

  * **Topic Partition Consumer Group** : These metrics monitor the health of consumer applications, primarily consumer lag. Open-source Kafka error metrics for consumer groups are not available by partition, but only at the topic level.




Some metrics can be grouped by broker index. Based on the broker index, you can look up the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) where that broker is provisioned. For more information, see [View brokers](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/view-brokers).

## View metrics for a Kafka cluster

You can view the metrics in the following ways:

  * The **Cluster details** page includes monitoring dashboards for clusters, topics, and consumer groups. These dashboards contain predefined charts that let you see the overall health and performance of your cluster.

  * You can use [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) to view all available metrics, create custom charts, or aggregate metrics across multiple clusters.




### Required roles and permissions

To get the permissions that you need to view monitoring charts, ask your administrator to grant you the [Managed Kafka Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.Viewer) (`roles/managedkafka.Viewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Use the monitoring dashboards

To view the monitoring dashboards for a Managed Service for Apache Kafka cluster, perform the following steps:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

  2. Click the name of the cluster.

  3. To view metrics for the cluster, select the **Monitoring** tab.

  4. To view metrics for a topic in the cluster:

     1. Select the **Resources** tab.

     2. In the **Topics** list, click the name of the topic.

     3. In the **Topic details** page, select the **Monitoring** tab.

  5. To view metrics for a consumer group in the cluster:

     1. Select the **Resources** tab.

     2. In the **Consumer groups** list, click the name of the consumer group.

     3. In the **Consumer group details** page, select the **Monitoring** tab.




For more information, see [View a Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster).

### Use Metrics Explorer

To view Managed Service for Apache Kafka metrics by using Metrics Explorer, perform the following steps:

  1. In the Google Cloud console, go to the **Metrics explorer** page.

[Go to Metrics explorer](https://console.cloud.google.com/monitoring/metrics-explorer)

  2. In the **Configuration** section, click **Select a metric**.

  3. In the filter, enter `Apache Kafka`.

  4. In **Active resources** , select one of the following:

     * Apache Kafka Cluster

     * Apache Kafka Topic

     * Apache Kafka Topic Partition

     * Apache Kafka Topic Partition Consumer Group

  5. Select a metric and click **Apply**.




For more information about Metrics Explorer, see [Create charts with Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

## Managed Service for Apache Kafka metrics

The following tables list commonly used metrics for monitoring your Kafka cluster and cluster resources. For the complete list of available metrics, see [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#gcp-managedkafka).

The Managed Service for Apache Kafka service is identified by the service URL `managedkafka.googleapis.com`.

### Cluster metrics

The following metrics apply to clusters. To view the metrics for a specific cluster, filter by the `cluster_id` label.

Metric | Description | Equivalent MBean Name  
---|---|---  
[`cpu/core_usage_time`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/cpu/core_usage_time) | Cumulative CPU usage of the cluster in vCPU. This can be useful for understanding the overall cost of operation for the cluster. | N/A  
[`cpu/limit`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/cpu/limit) | Current CPU count configured for the cluster. Can be used to monitor CPU utilization as a ratio with the `cpu/usage` metric. | N/A  
[`memory/usage`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/memory/usage) | Current RAM usage on the cluster. Can be used to monitor RAM utilization as a ratio with the `memory/limit` metric. | N/A  
[`memory/limit`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/memory/limit) | Current configured RAM size of the cluster. Can be used to monitor RAM utilization as a ratio with the `memory/usage` metric. | N/A  
[`jvm/memory_area/bytes_used`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/jvm/memory_area/bytes_used) | Used bytes of a given JVM memory area (such as heap or non-heap) for brokers and controllers. | `java.lang:type=Memory,HeapMemoryUsage.used`  
`java.lang:type=Memory,NonHeapMemoryUsage.used`  
[`jvm/memory_area/bytes_committed`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/jvm/memory_area/bytes_committed) | Committed bytes of a given JVM memory area (such as heap or non-heap) for brokers and controllers. | `java.lang:type=Memory,HeapMemoryUsage.committed`  
`java.lang:type=Memory,NonHeapMemoryUsage.committed`  
[`cluster_byte_in_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/cluster_byte_in_count) | The total number of bytes from clients sent to all topics. | `kafka.server:type=BrokerTopicMetrics,name=BytesInPerSec`  
[`cluster_byte_out_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/cluster_byte_out_count) | The total number of bytes sent to clients from all topics. | `kafka.server:type=BrokerTopicMetrics,name=BytesOutPerSec`  
[`cluster_message_in_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/cluster_message_in_count) | The total number of messages that have been published to all topics. | `kafka.server:type=BrokerTopicMetrics,name=MessagesInPerSec`  
[`request_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/request_count) | The total number of requests made to the broker | `kafka.network:type=RequestMetrics,name=RequestsPerSec,request= {Produce|FetchConsumer|FetchFollower},version=([0-9]+)`  
[`request_byte_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/request_byte_count) | The total size, in bytes, of requests made to the Cluster. | `kafka.network:type=RequestMetrics,name=RequestBytes,request= ([-.\w]+)`  
[`partitions`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/partitions) | The current number of partitions handled by this cluster, broken down by broker. | `kafka.server:type=ReplicaManager,name=PartitionCount`  
[`request_latencies`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/request_latencies) | The number of milliseconds taken for each request, at various percentiles | `kafka.network:type=RequestMetrics,name=TotalTimeMs,request= {Produce|FetchConsumer|FetchFollower}`  
[`consumer_groups`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/consumer_groups) | The current number of Consumer Groups consuming from the broker | `kafka.server:type=GroupMetadataManager,name=NumGroups`  
[`offline_partitions`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/offline_partitions) | The number of offline topic partitions as observed by the controller. | `kafka.controller:type=KafkaController,name=OfflinePartitionCount`  
  
### Topic metrics

The following metrics apply to topics. To view the metrics for a specific topic, filter by the `cluster_id` and `topic_id` labels.

Metric | Description | Equivalent MBean name  
---|---|---  
[`message_in_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/message_in_count) | The total number of messages published to the topic. | `kafka.server:type=BrokerTopicMetrics,name=MessagesInPerSec, topic=([-.\w]+)`  
[`byte_in_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/byte_in_count) | The total number of bytes from clients sent to the topic. | `kafka.server:type=BrokerTopicMetrics,name=BytesInPerSec,topic=([-.\w]+)`  
[`topic_request_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/topic_request_count) | The total number of produce and fetch requests made to the topic. | `kafka.server:type=BrokerTopicMetrics,name=TotalProduceRequestsPerSec,topic=([-.\w]+)`  
`kafka.server:type=BrokerTopicMetrics,name=TotalFetchRequestsPerSec,topic=([-.\w]+)`  
[`topic_error_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/topic_error_count) | The total number of failed produce and failed fetch requests made to the topic. | `kafka.server:type=BrokerTopicMetrics,name=FailedProduceRequestsPerSec,topic=([-.\w]+)`  
`kafka.server:type=BrokerTopicMetrics,name=FailedFetchRequestsPerSec,topic=([-.\w]+)`  
[`byte_out_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/byte_out_count) | The total number of bytes sent to clients. | `kafka.server:type=BrokerTopicMetrics,name=BytesOutPerSec, topic=([-.\w]+)`  
  
### Partition metrics

The following metrics apply to partitions. To view the metrics for a specific partition in a topic, filter by the `cluster_id`, `topic_id`, and `partition_index` labels.

Metric | Description | Equivalent MBean name  
---|---|---  
[`consumer_lag`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/consumer_lag) | Replication lag in messages between leader and each follower replica.  | ` kafka.server:type=FetcherLagMetrics,name=ConsumerLag,clientId=([-.\w]+),topic=([-.\w]+),partition=([0-9]+) `  
[`log_segments`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/log_segments) | The current number of log segments. This is useful to make sure storage tiering remains healthy. | `kafka.log:type=Log,name=NumLogSegments,topic=([-.\w]+),partition=([0-9]+)`  
[`first_offset`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/first_offset) | The first offset for each partition in the topic. In combination with the `last_offset`, it can be used to monitor an upper bound on the total number of messages stored as well as to find the actual offset of the oldest message. | `kafka.log:type=Log,name=LogStartOffset,topic=([-.\w]+),partition=([0-9]+)`  
[`last_offset`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/last_offset) | The last offset in the partition. This can be used to find the latest offset for each partition over time. This can be useful in identifying the specific offset needed to reprocess data starting from a particular time in the past. | `kafka.log:type=Log,name=LogEndOffset,topic=([-.\w]+),partition=([0-9]+)`  
[`byte_size`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/byte_size) | The size of the partition on disk in bytes. | N/A  
  
### Consumer group metrics

The following metrics apply to consumer groups. To view the metrics for a specific consumer group, filter by the `consumer_group_id` label.

Metric | Description | Equivalent MBean name  
---|---|---  
[`offset_lag`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/offset_lag) | The difference between the latest offset and the last committed offset for the consumer group for each partition. This metric estimates how many produced messages the consumer has not yet successfully processed.  | N/A  
  
## What's next

  * View all [Managed Service for Apache Kafka metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#gcp-managedkafka)

  * [Audit logging](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/audit-logging)

  * [Monitor Kafka clusters for reliability](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/monitor-reliability)

  * [Monitor Kafka client applications](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/monitor-clients)




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
