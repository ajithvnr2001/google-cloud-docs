---
url: https://docs.cloud.google.com/pubsub/docs/choose_lite_or_pubsub/
title: Choose Pub/Sub or Pub/Sub Lite \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:39:08.293192+00:00
---

# Choose Pub/Sub or Pub/Sub Lite  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/choose_lite_or_pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/lite/docs/publish-receive-messages-console)



Send feedback 

#  Choose Pub/Sub or Pub/Sub Lite Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Pub/Sub Lite is deprecated. Effective January 31, 2027, Pub/Sub Lite will be turned down.   


  * Current customers: Pub/Sub Lite remains functional until January 31, 2027.   
If you have not used Pub/Sub Lite within the 90-day period preceding July 15, 2025 (April 15, 2025 - July 15, 2025), you won't be able to access Pub/Sub Lite starting on July 15, 2025. 
  * New customers: Pub/Sub Lite is no longer available for new customers after September 24, 2024.



You can migrate your Pub/Sub Lite service to [Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-managed-service-for-apache-kafka) or [Pub/Sub](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-pubsub).

This document is intended to help you choose between Pub/Sub and Pub/Sub Lite. This document requires your familiarity with the basic concepts of Pub/Sub such as topics and subscriptions. If you are new to Pub/Sub, read [What is Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) first.

Pub/Sub and Pub/Sub Lite are horizontally scalable and managed messaging services. These services can handle high volume and support large storage requirements. Pub/Sub is usually the default solution for most application integration and analytics use cases. It is feature-rich and fully managed. Pub/Sub Lite is recommended for applications where messaging throughput is more stable, workloads can benefit from a partition-based system, and cost is of a significant concern.

**Pub/Sub offers a broader range of features** , per-message parallelism, global routing, and automatically scaling resource capacity. In terms of message replication, Pub/Sub guarantees synchronous replication.

**Pub/Sub Lite is a partition-based solution** that trades off operational workload, global availability, and some features for cost efficiency. Pub/Sub Lite requires you to manually reserve and manage resource capacity. Within Pub/Sub Lite, you can choose zonal or regional Lite topics. Regional Lite topics offer the same availability SLA as Pub/Sub topics.

Note the reliability differences between the two services in terms of message replication. Pub/Sub supports synchronous data replication and uses three zones. Regional Lite topics replicate data to a secondary zone. Zonal Lite topics replicate data in only one zone.

## Business requirements checklist

The following questions can help you choose the right Pub/Sub messaging service:

  * **Are reliability, minimal operational cost, and ease of development your top priorities?** Use Pub/Sub.

  * **Are you willing to incur some additional operational overhead in terms of managing the topic capacity, can work with availability risks inherent to zonal services, and require low cost?** Use zonal Lite topics.

  * **Do you require some protection against zonal failures, are willing to incur an additional operational overhead in terms of managing the topic capacity, and require the lowest per throughput cost?** Use regional Lite topics.




To know more about the cost differences between Pub/Sub and Pub/Sub Lite, see the [pricing](https://cloud.google.com/pubsub/pricing) page.

## Features comparison table

Feature | Pub/Sub | Pub/Sub Lite  
---|---|---  
Access Transparency | Yes | No  
Capacity | Automatically provisioned | Provision before you use  
Client library languages | Java, Python, Go, Node.js, C++, C#, PHP, Ruby, SAP, ABAP | Java, Python, Go  
Cross-project subscriptions | Yes | No  
Customer managed encryption keys | Yes | No  
Dead letter topics | Yes | No  
Exactly-once delivery | Yes | No  
Integrations | 

  * [Dataflow](https://docs.cloud.google.com/dataflow/docs/concepts/streaming-with-cloud-pubsub)
  * [Cloud Run functions](https://docs.cloud.google.com/functions/docs/calling/pubsub)
  * [Cloud Logging](https://docs.cloud.google.com/logging/docs/export/pubsub)
  * [Kafka Connect](https://docs.cloud.google.com/pubsub/docs/connect_kafka)
  * [Apache Flink](https://github.com/apache/flink-connector-gcp-pubsub)

| 

  * [Dataflow](https://docs.cloud.google.com/pubsub/lite/docs/stream-messages-dataflow)
  * [Apache Spark](https://docs.cloud.google.com/pubsub/lite/docs/write-messages-apache-spark)
  * [Apache Flink](https://github.com/googleapis/java-pubsublite-flink)
  * [Apache Kafka](https://docs.cloud.google.com/pubsub/lite/docs/kafka-migration)
  * [Kafka Connect](https://docs.cloud.google.com/pubsub/lite/docs/lite_connect_kafka)

  
Message filtering | Yes for message attributes | No  
Message replication | Yes | No  
Message routing | Global | Zonal or regional  
Message schema validation | Yes | No  
Multi-zone in single region | No | Single zone or dual zone in a single region  
Ordered delivery | Per-key ordering | Per-partition ordering  
Message acknowledgment tracking | Per message | Per-partition cursor  
Pricing | Pay for what you use | Pay for the capacity that you provision  
REST endpoints | Yes | No  
Resource namespace | Global | Zonal or regional  
Retention period | Up to 31 days | Unlimited  
Service endpoints | Global and regional | Regional  
Storage | Unlimited | Unlimited  
Subscription | 

  * [Pull](https://docs.cloud.google.com/pubsub/docs/pull)
  * [Push](https://docs.cloud.google.com/pubsub/docs/push)
  * [BigQuery subscription](https://docs.cloud.google.com/pubsub/docs/bigquery)
  * [Cloud Storage subscription](https://docs.cloud.google.com/pubsub/docs/cloudstorage)

| 

  * [Standard subscription](https://docs.cloud.google.com/pubsub/lite/docs/subscriptions)
  * [Export subscription](https://docs.cloud.google.com/pubsub/lite/docs/export-pubsub)

  
  
## Data replication

Pub/Sub topics replicate data to three zones within a region. For more information about Pub/Sub data replication, see [Data replication in a topic](https://docs.cloud.google.com/pubsub/docs/admin#data_replication_in_a_topic).

Regional Pub/Sub Lite topics replicate data to two zones within a region. Zonal Pub/Sub Lite topics store data in a single zone within a region. For more information about Pub/Sub Lite data replication, see [Data replication in a Lite topic](https://docs.cloud.google.com/pubsub/lite/docs/topics#data_replication_in_a_lite_topic).

## Message routing

Both Pub/Sub and Pub/Sub Lite can publish and subscribe from all regions, and even outside of Google Cloud.

**Pub/Sub routes messages globally**. Applications hosted in any region can publish messages to a single topic. The messages are processed in the nearest region permitted by your organization policies and forwarded to subscribers independently of the source.

**Pub/Sub Lite routes messages within a region or a zone**. Subscribers must connect to the instance of the service in the region where the topic is located. As a result, publishers and subscribers must maintain network connectivity to the same region to communicate. Publishers can publish data to any topic from anywhere, but this may require connecting to a remote region, adding network latency. Subscribers that need aggregate data published to topics in different locations must connect to every relevant local service instance to read the messages.

## Resource namespace

**Pub/Sub topics and subscriptions are global resources**. The Pub/Sub service can store messages in [any region](https://cloud.google.com/about/locations) allowed by a topic storage policy. In addition, a topic and a subscription to that topic can be stored in different projects, allowing for fine-grained billing and access control. Finally, subscribers get the same data regardless of which service endpoint they use to connect to Pub/Sub or which service endpoint was used by the publisher of the data.

**Zonal Lite topics and subscriptions are zonal resources.** These resources must be in the same Cloud project and zone.

**Regional Lite topics and subscriptions are regional resources.** These resources must be in the same Cloud project and region.

For a list of regions and zones that Pub/Sub Lite supports, see [Pub/Sub Lite locations](https://docs.cloud.google.com/pubsub/lite/docs/locations).

## Capacity management

**Pub/Sub scales automatically.** Capacity for message publishing is automatically provisioned, so you can send and receive message at any rate, up to the quotas you configure for your project.

**Pub/Sub Lite is manually provisioned.** You must configure the number of partitions per Lite topic. You must also provision storage and throughput capacity. Throughput capacity can be provisioned using [Lite reservations](https://docs.cloud.google.com/pubsub/lite/docs/reservations).

## Delivery Modes

**Pub/Sub supports multiple message delivery modes.** These include [Pull](https://docs.cloud.google.com/pubsub/docs/pull) (traditional polling), [Push](https://docs.cloud.google.com/pubsub/docs/push) (HTTPS POST), [StreamingPull](https://docs.cloud.google.com/pubsub/docs/pull#streamingpull) (bidirectional RPC, for lowest latency and highest efficiency), and pull over HTTP REST and gRPC.

**Pub/Sub Lite only supports streaming gRPC pull message delivery.** To request messages, subscribers establish bidirectional streaming connections with each partition.

## Parallelism

**Pub/Sub uses per-message parallelism.** This enables concurrent processing of any number of messages, from one or thousands of clients for a single subscription.

**Pub/Sub Lite uses partition-based parallelism.** This forces a client to process each data partition in linear order on a single client instance. This limits the maximum number of client instances to at most the number of partitions.

## Streaming pipelines

Both Pub/Sub and Pub/Sub Lite are integrated with Dataflow for serverless stream processing and data integration. Pub/Sub allows Dataflow to scale more flexibly and supports [Dataflow SQL](https://docs.cloud.google.com/dataflow/docs/samples/join-streaming-data-with-sql).

To get started with Dataflow and Pub/Sub or Pub/Sub Lite, try these tutorials:

  * [Pub/Sub: Stream processing with Dataflow](https://docs.cloud.google.com/pubsub/docs/stream-messages-dataflow)
  * [Pub/Sub Lite: Using Pub/Sub Lite with Dataflow](https://docs.cloud.google.com/pubsub/lite/docs/stream-messages-dataflow)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
