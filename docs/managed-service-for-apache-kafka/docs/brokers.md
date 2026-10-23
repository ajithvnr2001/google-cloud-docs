---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/
title: Overview of brokers in Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:19.786815+00:00
---

# Overview of brokers in Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Overview of brokers in Managed Service for Apache Kafka Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how Managed Service for Apache Kafka provisions brokers for your Kafka cluster.

## Overview

A Kafka cluster is made up of one or more _brokers_. Producer applications send messages to brokers, and consumer applications connect to brokers to read messages. Multiple consumers can read messages in parallel, typically using a [consumer group](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/consumer-groups). Each partition in a topic is assigned a leader broker. The leader is responsible for replicating the partition data that it receives to other brokers.

Managed Service for Apache Kafka automatically creates brokers for you. Although you can't directly configure the number of brokers, you can scale up your cluster to add brokers.

## Broker provisioning

When you create a Managed Service for Apache Kafka cluster, the service provisions at least one broker in each of three zones. The number of brokers is calculated as follows:

`number of brokers = max(3, ceiling(vCPUs / 15))`

For example, a cluster with 75 vCPUs starts with 5 brokers.

Brokers are distributed as evenly across zones as possible, and all brokers have the same number of vCPUs, which might be a fractional value. Each broker has a minimum of one vCPU.

The service automatically provisions disk capacity for the brokers. Optionally, you can configure the disk capacity per broker when you create the cluster and increase it later. For more information, see [Configure broker disk size](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/configure-disk-size).

## Scaling the cluster

As you increase the size of the cluster, additional vCPUs are distributed among the existing brokers, up to a limit of 15 vCPUs per broker. If cluster size exceeds 15 vCPUs per broker, the service provisions a new broker. The brokers are equally distributed among the three zones, with a maximum difference of one.

If you decrease the cluster size, vCPUs are distributed across the existing brokers, down to a minimum of one vCPU per broker. Brokers are never deleted during the lifetime of a cluster. Once a new broker is provisioned, it can be scaled down to one vCPU, but is never deleted.

## Rebalancing broker partitions

Often, the reason for scaling up a cluster is to reduce load on existing brokers, by reassigning some partitions to the new broker. This process is called _rebalancing_. Rebalancing can be performed automatically or manually.

  * **Automatic rebalancing**. Automatic rebalancing is a cluster-wide setting. When a new broker is provisioned, if automatic rebalancing is enabled, the service automatically rebalances the partitions from existing brokers. The rebalancing algorithm is based on the partition count, and aims to keep approximately the same number of partitions per broker. It doesn't take into account the actual traffic served by each partition. For more information, see [Rebalancing configuration](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster#rebalancing-config).

  * **Manual rebalancing**. You can manually rebalance partitions by changing the partition assignment. You might do this because automatic rebalancing is disabled, or because a partition receives significantly more traffic than other partitions (called a _hot partition_). For more information, see [Change the partition assignment](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/assign-partitions)




## What's next

  * [View the brokers in a cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/view-brokers)
  * [Configure broker disk size](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/configure-disk-size)
  * [Change a partition assignment](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/assign-partitions)
  * [Use quotas for load isolation](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/kafka-quotas)



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
