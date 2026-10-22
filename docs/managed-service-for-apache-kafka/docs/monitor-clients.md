---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/monitor-clients/
title: Monitor Kafka client applications \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:03.947816+00:00
---

# Monitor Kafka client applications  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/monitor-clients/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Monitor Kafka client applications Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to monitor the health of clients that produce or consume data in your Managed Service for Apache Kafka cluster.

It's important to monitor client applications as part of your overall reliability strategy. Metrics such as throughput, error rates, and consumer lag can tell you whether client applications are experiencing reliability issues. Problems might be caused by client configuration, uneven distribution of keys across partitions, or cluster issues that affect only a specific partition.

## Server-side metrics

While it's useful to monitor client behavior directly, server-side metrics don't require any additional instrumentation, and can help you to detect client-side issues that affect reliability.

Server-side metrics are especially useful for detecting load imbalances across brokers (hot brokers), and deviations in normal operations, such as spikes in latency.

### Throughput

Monitor the following throughput metrics and compare them against your expected throughput:

  * **Message rate** , per broker and per topic.
  * **Byte rate** , per broker and per topic.
  * **Request rates**. A misconfigured client might flood brokers with a high rate of small requests (0-1000 bytes per request), reducing throughput.
  * **Request latency**. Spikes in producer request latency might signal imbalanced load or a problem with client configuration.



Kafka offers throughput metrics per topic and for the cluster. These metrics don't always have the same values when aggregated for all topics. Use an aggregated metric for high-level monitoring and alerting, and look at per-topic metrics when you troubleshoot throughput problems. Isolate any issues to specific brokers.

### Request error rates

The [`topic_error_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/topic_error_count) metric tracks the number of failed fetch and produce requests on the server side. However, some classes of error aren't reflected in this metric. For example:

  * Misconfigured authorization settings might prevent a client from producing to a topic, without the error appearing in this metric.

  * Cluster failures might prevent a broker from responding to requests at all.




For this reason, you should also monitor errors on the client side, including request time-out errors.

### Consumer lag

Consumer lag measures how far behind a consumer client is from a particular offset. Aggregating this metric by topic, partition, and broker is useful for determining whether lag is due to specific brokers or partitions.

Consider creating an alert based on the maximum lag across the subset of topics that are critical for your workload.

### Custom dashboard queries

We recommend creating custom dashboards and alerts to monitor these signals. The following table shows [Prometheus Query Language (PromQL)](https://docs.cloud.google.com/monitoring/promql) queries that you can use to monitor client health.

Signal| PromQL query  
---|---  
Throughput: Message rates per broker | 
    
    
    sum by (resource_container, location, cluster_id, broker_index) (
      rate(
        {
          "managedkafka.googleapis.com/message_in_count",
          monitored_resource="managedkafka.googleapis.com/Topic"
        }[${__interval}]
      )
    )  
  
Throughput: Message rates per broker per topic, for the largest 5 topics  | 
    
    
    topk(5,
      sum by (resource_container, location, cluster_id, broker_index, topic_id) (
        rate(
          {
            "managedkafka.googleapis.com/message_in_count",
            monitored_resource="managedkafka.googleapis.com/Topic"
          }[${__interval}]
        )
      )
    )  
  
Throughput: Bandwidth per topic and broker | 
    
    
    sum by (resource_container, location, cluster_id, broker_index, topic_id) (
      rate(
        {
          "managedkafka.googleapis.com/byte_in_count",
          monitored_resource="managedkafka.googleapis.com/Topic"
        }[${__interval}]
      )
    )  
  
Request rate | 
    
    
    sum by (resource_container, location, cluster_id, request) (
      rate(
        {
          "managedkafka.googleapis.com/request_count",
          monitored_resource="managedkafka.googleapis.com/Cluster",
          "request"="Produce"
        }[${__interval}]
      )
    )  
  
Request rate, cluster totals | 
    
    
    sum by (resource_container, location, cluster_id, request) (
      rate(
        {
          "managedkafka.googleapis.com/topic_request_count",
          monitored_resource="managedkafka.googleapis.com/Topic",
          "request"="Produce"
        }[${__interval}]
      )
    )  
  
Request latency | 
    
    
    sum by (resource_container, location, cluster_id, broker_index, request) (
      avg_over_time(
        {
          "managedkafka.googleapis.com/request_latencies",
          monitored_resource="managedkafka.googleapis.com/Cluster",
          "percentile"="95",
          "request"="Produce"
        }[${__interval}]
      )
    )  
  
Request error counts | 
    
    
    sum by (resource_container, location, cluster_id, broker_index, request) (
      rate(
        {
          "managedkafka.googleapis.com/topic_error_count",
          monitored_resource="managedkafka.googleapis.com/Topic"
        }[${__interval}]
      )
    )  
  
Consumer lag: Top 5 partitions by offset lag | 
    
    
    topk(5,
      max by (resource_container, location, cluster_id, topic_id, partition_index) (
        max_over_time(
          {
            "managedkafka.googleapis.com/offset_lag",
            monitored_resource="managedkafka.googleapis.com/TopicPartitionConsumerGroup"
          }[${__interval}]
        )
      )
    )  
  
Consumer lag: Top 5 consumer groups by offset lag | 
    
    
    topk(5,
      max by (resource_container, location, cluster_id, consumer_group_id) (
        max_over_time(
          {
            "managedkafka.googleapis.com/offset_lag",
            monitored_resource="managedkafka.googleapis.com/TopicPartitionConsumerGroup"
          }[${__interval}]
        )
      )
    )  
  
## Client-side metrics

Sometimes client issues don't appear in server metrics. For example:

  * If authentication or networking is misconfigured, messages might accumulate in the client's internal queues. As requests time out, the messages are re-enqueued and retried.

  * If flow control is misconfigured, a client might produce more messages than the allocated number of threads can send. Although throughput might be consistent, a growing backlog of requests expire before they can be sent.




If your clients run on Compute Engine, Google Kubernetes Engine, or Cloud Run, you can use [log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics) in Cloud Monitoring to detect high error rates in logs. However, some Kafka clients hide exceptions that lead to prolonged retries, unless you configure higher log levels. Therefore, you should also monitor for increased request latencies.

Java clients expose many metrics through Java Management Extensions (JMX). For more information, see [Monitoring](https://kafka.apache.org/37/operations/monitoring/) in the Apache Kafka documentation. If possible, prioritize instrumenting your clients to report the following metrics:

  * Request error rates (`kafka.producer:type=producer-metrics,client-id="{client-id}"`)
  * Request average latency (`kafka.producer:type=producer-metrics,client-id="{client-id}"`)



Send these metrics to a monitoring solution if possible. If you can connect to the JMX ports on the machines that run the client instances, you can also read these metrics interactively.

## Mitigations

If you see issues in your client applications, consider the following mitigations:

  * Look for imbalanced load across brokers (hot brokers). Make sure that [auto rebalancing](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster#rebalancing-config) is enabled in your cluster.

  * If the request rate seems unusually high, check whether the client is sending a large number of small requests. Check the `max.request.size` and `batch.size` configurations on the producer.

  * Check the client configurations for authentication, networking, and flow control.

  * Excessive lag across all topics or partitions in a cluster might indicate the cluster is overloaded and should be scaled up.

  * Excessive lag across all topics or partitions in a broker might indicate the broker is overloaded. Try improving the key distribution or [reassign partitions](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/assign-partitions) to different brokers.




## What's next

  * [Monitor a Kafka clusters](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/monitor-cluster)
  * [Monitor Kafka clusters for reliability](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/monitor-reliability)
  * [Create and manage custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards)



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
