---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/kafka-quotas/
title: Use Kafka quotas for load isolation \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:29.689687+00:00
---

# Use Kafka quotas for load isolation  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/kafka-quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Use Kafka quotas for load isolation Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to control the broker resources in a Managed Service for Apache Kafka cluster by using quotas.

## Overview

Kafka lets you set quotas to limit bandwidth and request rates for different clients. You can use quotas to ensure that unanticipated spikes in load on one application don't affect other applications.

You can set the following quotas:

  * Network bandwidth for producers and consumers.
  * The percentage of I/O and network threads, as a way to limit request rates.



For more information about Kafka quotas, see [Quotas](https://kafka.apache.org/37/design/design/#quotas) in the Kafka documentation. Kafka quotas are distinct from the [Google Cloud quotas](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quotas) that apply to Managed Service for Apache Kafka.

## Set quotas

You can set quotas on [authenticated principals](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authn-types-kafka) and `client-id` groups. This page shows how to set quotas on a principal, but the same steps apply to `client-id` groups.

### Prerequisites

Before you start, install the Kafka command-line tools on a Compute Engine VM. The VM must be able to reach a subnet that is connected to your cluster. To create the VM and install the Kafka tools, follow the instructions in [Produce and consume messages with the Kafka command-line tools](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart).

### Set the network bandwidth quota

To set the network bandwidth quota, run the `kafka-configs.sh --alter` command as follows:
    
    
    kafka-configs.sh --alter \
      --entity-type users \
      --entity-name KAFKA_USER \
      --add-config 'producer_byte_rate=PRODUCER_LIMIT,consumer_byte_rate=CONSUMER_LIMIT' \
      --bootstrap-server=BOOTSTRAP_ADDRESS \
      --command-config client.properties
    

Replace the following.

  * KAFKA_USER: The principal to apply the quota to.
  * PRODUCER_LIMIT: The maximum producer byte rate, in bytes per second.
  * CONSUMER_LIMIT: The maximum consumer byte rate, in bytes per second.
  * BOOTSTRAP_ADDRESS: The cluster's [bootstrap address](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster#view-bootstrap-address).



### Set the request rate quota

To set the request rate quota, run the `kafka-configs.sh --alter` command as follows:
    
    
    kafka-configs.sh --alter \
      --entity-type users \
      --entity-name KAFKA_USER \
      --add-config 'request_percentage=REQUEST_RATE_LIMIT' \
      --bootstrap-server=BOOTSTRAP_ADDRESS \
      --command-config client.properties
    

Replace the following.

  * KAFKA_USER: The principal to apply the quota to.
  * REQUEST_RATE_LIMIT: The percentage of IO and network thread time allowed, from a total of `(num.io.threads + num.network.threads) * 100%`. The value can exceed 100.
  * BOOTSTRAP_ADDRESS: The cluster's [bootstrap address](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster#view-bootstrap-address).



## View quotas

To view the quotas that have been set for all principals, run the `kafka-configs.sh --describe` command as follows:
    
    
    kafka-configs.sh --describe --all \
      --entity-type users \
      --bootstrap-server=BOOTSTRAP_ADDRESS \
      --command-config client.properties
    

Replace BOOTSTRAP_ADDRESS with the cluster's [bootstrap address](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster#view-bootstrap-address).

## Remove quotas

To remove a quota for a principal, run the `kafka-configs.sh --alter` command as follows:
    
    
    kafka-configs.sh --alter \
      --entity-type users \
      --entity-name KAFKA_USER \
      --delete-config 'producer_byte_rate,consumer_byte_rate,request_percentage' \
      --bootstrap-server=BOOTSTRAP_ADDRESS \
      --command-config client.properties
    

Replace the following.

  * KAFKA_USER: The principal to remove the quota from.
  * BOOTSTRAP_ADDRESS: The cluster's [bootstrap address](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster#view-bootstrap-address).



## Example: Limit producer bandwidth

This section shows how to limit producer bandwidth, by setting the network bandwidth quota for the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account). This service account is attached by default to all Compute Engine VMs that you create.

**Tip:** To find the current [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials) in use, run the [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list) command.

  1. Define the following shell variables:
         
         export BOOTSTRAP=BOOTSTRAP_ADDRESS
         export TOPIC=TOPIC_NAME
         export KAFKA_USER=PROJECT_NUMBER-compute@developer.gserviceaccount.com
         

  2. To find the baseline throughput, use the `kafka-producer-perf-test.sh` command to run a performance test.
         
         kafka-producer-perf-test.sh \
           --topic test-topic \
           --num-records 1000000 --throughput 1000 --record-size 1024 \
           --print-metrics \
           --producer-props bootstrap.servers=$BOOTSTRAP \
           --producer.config client.properties
         

This command sends 1000000 records to the specified Kafka topic. The `--throughput` flag throttles the throughput to 1000 messages per second, and `--record-size` sets the message size to 1024 bytes. Therefore, the load for this test is `(1000 * 1024)` bytes per second, or about 1 MBps.

The output shows performance metrics for the test, similar to the following:
         
         5005 records sent, 1000.6 records/sec (0.98 MB/sec), 3.7 ms avg latency, 41.0 ms max latency.
         5002 records sent, 1000.2 records/sec (0.98 MB/sec), 3.3 ms avg latency, 23.0 ms max latency.
         

In this example, the throughput is approximately equal to the requested rate of 1 MBps.

  3. Suppose that you want to limit producers to 100 kBps. Set the producer throughput quota as follows:
         
         kafka-configs.sh --alter \
           --entity-type users \
           --entity-name $KAFKA_USER \
           --add-config 'producer_byte_rate=100000' \
           --bootstrap-server=$BOOTSTRAP \
           --command-config client.properties
         

  4. Repeat the performance test. The output shows lower throughput:
         
         118 records sent, 204.6 records/sec (0.20 MB/sec), 220.7 ms avg latency, 4348.0 ms max latency.
         60 records sent, 10.7 records/sec (0.01 MB/sec), 6145.2 ms avg latency, 9912.0 ms max latency.
         1020 records sent, 181.5 records/sec (0.18 MB/sec), 11693.7 ms avg latency, 14513.0 ms max latency.
         75 records sent, 13.0 records/sec (0.01 MB/sec), 16864.1 ms avg latency, 20219.0 ms max latency.
         1005 records sent, 183.9 records/sec (0.18 MB/sec), 22088.6 ms avg latency, 24679.0 ms max latency.
         75 records sent, 13.0 records/sec (0.01 MB/sec), 27030.4 ms avg latency, 30387.0 ms max latency.
         

In this example, the throughput varies from second to second, but in any 2-second window, throughput is consistent with the quota. Latency also increases, because the test is generating data faster than it can send it, due to the quota limit.

## What's next



  * [Overview of brokers in Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers)
  * [Authentication types for Kafka brokers](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authn-types-kafka)
  * [Monitor a Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/monitor-cluster)



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
