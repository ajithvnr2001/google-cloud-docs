---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/monitor-reliability/
title: Monitor Kafka clusters for reliability \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:03.471480+00:00
---

# Monitor Kafka clusters for reliability  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/monitor-reliability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Monitor Kafka clusters for reliability Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to monitor a Managed Service for Apache Kafka cluster to ensure the reliability of your Kafka workloads.

## Overview

_Reliability_ is the ability of a system to perform correctly, consistently over time. For Kafka-based workloads, reliability encompasses both the Kaka clusters themselves, as well as the client applications that produce and consume messages.

Managed Service for Apache Kafka is designed to tolerate and recover from many common failures. For example, the service places replicas in different zones for fault-tolerance, and automatically restarts brokers that fail. However, other factors that affect reliability fall outside of the service's direct control, such as:

  * Client configuration
  * Load on the cluster, including average load and spikes
  * The number of partitions and replicas
  * Topic configurations, such as [message retention](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/edit-topic#retention)



To achieve reliable operations, it's important to monitor the cluster for these operational parameters and keep them within recommended ranges. The following sections describe some key metrics that are important for reliability.

## Monitor cluster capacity

To avoid overloading a cluster, monitor the following signals. Create [alerts](https://docs.cloud.google.com/monitoring/alerts) to notify you if they fall outside of the recommended range for an extended period.

  * **CPU utilization**. Try to keep CPU utilization under 80% on all brokers.

  * **Broker disk utilization** : Make sure that broker disk utilization stays less than 80%.

  * **Disk size**. As a safe starting point, we recommend having at least `2*(segment.bytes)` per partition per broker. In practice, actual disk requirements are often considerably lower.

By default, a segment file is closed and moved to remote storage after 7 days. It is common for most partitions to receive fewer than `segment.bytes` of data over that period, meaning that most partitions use fewer than `segment.bytes` of disk space. Before increasing disk size, monitor disk utilization as you create more partitions on the cluster.

  * **Partition count**. Try to maintain fewer than 4000 partitions per broker, and fewer than 100,000 partitions per cluster.




If your cluster is low on capacity, consider the following mitigations:

  * Increase the cluster's vCPU count. For more information, see [Update a Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/update-cluster).

  * Scale up the cluster to add more brokers. For information about how the service provisions brokers, see [Broker provisioning](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers#broker-provisioning).

  * Increase the broker disk size. For more information, see [Configure broker disk size](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/configure-disk-size).




The following table shows [Prometheus Query Language (PromQL)](https://docs.cloud.google.com/monitoring/promql) queries for these metrics that you can add to a custom [Cloud Monitoring dashboard](https://docs.cloud.google.com/monitoring/dashboards).

Signal| PromQL query  
---|---  
CPU utilization | 
    
    
    rate(
      {
        "managedkafka.googleapis.com/cpu/core_usage_time",
        monitored_resource="managedkafka.googleapis.com/Cluster"
      }[${__interval}]
    )
    / min_over_time(
      {
        "managedkafka.googleapis.com/cpu/limit",
        monitored_resource="managedkafka.googleapis.com/Cluster"
      }[${__interval}]
    )  
  
Broker disk utilization | 
    
    
    max_over_time(
      {
        "managedkafka.googleapis.com/disk/used_bytes",
        monitored_resource="managedkafka.googleapis.com/Cluster"
      }[${__interval}]
    )
    / min_over_time(
      {
        "managedkafka.googleapis.com/disk/limit",
        monitored_resource="managedkafka.googleapis.com/Cluster"
      }[${__interval}]
    )  
  
Segment size per partition | 
    
    
    # Assumes that segment files are 225 MiB. Check your cluster configuration.
    2*225*(1024*1024) * max_over_time(
      {
        "managedkafka.googleapis.com/partitions",
        monitored_resource="managedkafka.googleapis.com/Cluster"
      }[${__interval}]
    )
    / min_over_time(
      {
        "managedkafka.googleapis.com/disk/limit",
        monitored_resource="managedkafka.googleapis.com/Cluster"
      }[${__interval}]
    )  
  
Partitions per broker | 
    
    
    max by (resource_container, location, cluster_id, broker_index) (
      max_over_time(
        {
          "managedkafka.googleapis.com/partitions",
          monitored_resource="managedkafka.googleapis.com/Cluster"
        }[${__interval}]
      )
    )  
  
Partitions per cluster | 
    
    
    max by (resource_container, location, cluster_id) (
      max_over_time(
        {
          "managedkafka.googleapis.com/partitions",
          monitored_resource="managedkafka.googleapis.com/Cluster"
        }[${__interval}]
      )
    )  
  
## Monitor partition balance across brokers

Uneven load can prevent a Kafka cluster from serving client requests properly. The number of partitions assigned to a single broker should stay within about 10% of the average partition count per broker. Look for outliers in this metric.

To maintain balanced partitions, consider enabling [auto rebalancing on scale up](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster#rebalancing-config) in your cluster.

The following table shows PromQL queries that you can use to monitor partition imbalances.

Signal| PromQL query  
---|---  
Partition counts per broker | 
    
    
    sum by (resource_container, location, cluster_id, broker_index) (
      avg_over_time(
        {
          "managedkafka.googleapis.com/partitions",
          monitored_resource="managedkafka.googleapis.com/Cluster"
        }[${__interval}]
      )
    )  
  
Partition imbalance | 
    
    
    sum by (resource_container, location, cluster_id, broker_index) (
      avg_over_time(
        {
          "managedkafka.googleapis.com/partitions",
          monitored_resource="managedkafka.googleapis.com/Cluster"
        }[${__interval}]
      )
    )
    / on (resource_container, location, cluster_id)
      group_left avg by (resource_container, location, cluster_id) (
      avg_over_time(
        {
          "managedkafka.googleapis.com/partitions",
          monitored_resource="managedkafka.googleapis.com/Cluster"
        }[${__interval}]
      )
    ) - 1  
  
## Monitor partition replication

Data replication is critical to ensure that your workloads are fault-tolerant. In a healthy cluster, every partition in a topic has the full number of replicas, based on the topic's configured [replication factor](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-topic#replication-factor).

Use the following signals to monitor partition replication:

  * **Under minimum in-sync replicas (ISRs)**. If a partition has fewer in-sync ISRs than the configured minimum ([`min.insync.replicas`](https://kafka.apache.org/37/configuration/topic-level-configs/#topicconfigs_min.insync.replicas)), there is a serious risk of data loss and availability. Typically, this situation is caused by insufficient capacity on one or more brokers, or by infrastructure failures.

  * **Under-replicated partitions**. A partition is under-replicated when the number of in-sync replicas falls below the replication factor. If a partition remains under-replicated for 10s of minutes, there might be a problem with the brokers, storage capacity, or something else.

During a rolling restart, brokers become unavailable as they are restarted, causing temporary under-replication. This situation is expected and doesn't require intervention.




The following table shows PromQL queries that you can use to monitor replication.

Signal| PromQL query  
---|---  
Under minimum ISRs | 
    
    
    max by (
      resource_container,
      location,
      cluster_id
    ) (
      max_over_time(
        {
          "managedkafka.googleapis.com/broker/under_min_isr_partitions",
          monitored_resource="managedkafka.googleapis.com/Cluster"
        }[${__interval}]
      )
    )  
  
Under replication  | 
    
    
    max by (
      resource_container,
      location,
      cluster_id
    ) (
      min_over_time(
        {
          "managedkafka.googleapis.com/broker/under_replicated_partitions",
          monitored_resource="managedkafka.googleapis.com/Cluster"
        }[10m:${__interval}]
      )
    )  
  
## What's next

  * [Monitor a Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/monitor-cluster)
  * [Monitor Kafka client applications](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/monitor-clients)
  * [Plan the size of your Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/plan-cluster-size)
  * [Create and manage custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards)



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
