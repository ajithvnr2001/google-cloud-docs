---
url: https://docs.cloud.google.com/pubsub/lite/docs/kafka-migration/
title: Migrate from Kafka to Pub/Sub Lite \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:39:10.389884+00:00
---

# Migrate from Kafka to Pub/Sub Lite  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/kafka-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/lite/docs/publish-receive-messages-console)



Send feedback 

#  Migrate from Kafka to Pub/Sub Lite Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Pub/Sub Lite is deprecated. Effective January 31, 2027, Pub/Sub Lite will be turned down.   


  * Current customers: Pub/Sub Lite remains functional until January 31, 2027.   
If you have not used Pub/Sub Lite within the 90-day period preceding July 15, 2025 (April 15, 2025 - July 15, 2025), you won't be able to access Pub/Sub Lite starting on July 15, 2025. 
  * New customers: Pub/Sub Lite is no longer available for new customers after September 24, 2024.



You can migrate your Pub/Sub Lite service to [Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-managed-service-for-apache-kafka) or [Pub/Sub](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-pubsub).

****

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document is useful if you're considering migrating from self-managed Apache Kafka to Pub/Sub Lite.

**Key Point:** Review Pub/Sub Lite features, pricing, and use cases as compared to Kafka, and then prepare for the migration.

## Overview of Pub/Sub Lite

Pub/Sub Lite is a high-volume messaging service built for low cost of operation. Pub/Sub Lite offers Zonal and Regional Storage along with pre-provisioned capacity. Within Pub/Sub Lite, you can choose zonal or regional Lite topics. Regional Lite topics offer the same availability SLA as Pub/Sub topics. However, there are reliability differences between Pub/Sub and Pub/Sub Lite in terms of [message replication](https://docs.cloud.google.com/pubsub/docs/choosing-pubsub-or-lite#data_replication).

To learn more about Pub/Sub and Pub/Sub Lite, see [What is Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview).

To learn more about Lite-supported regions and zones, see [Pub/Sub Lite locations](https://docs.cloud.google.com/pubsub/lite/docs/locations).

## Terminology in Pub/Sub Lite

The following are some key terms for Pub/Sub Lite.

  * **Message.** Data that moves through the Pub/Sub Lite service.

  * **Topic.** A named resource that represents a feed of messages. Within Pub/Sub Lite, you can choose to create a zonal or regional Lite topic. Pub/Sub Lite regional topics store data in two zones of a single region. Pub/Sub Lite zonal topics replicate data within just one zone.

  * **Reservation.** A named pool of throughput capacity shared by multiple Lite topics in a region.

  * **Subscription** A named resource that represents an interest in receiving messages from a particular Lite topic. A subscription is similar to a consumer group in Kafka that only connects to a single topic.

  * **Subscriber.** A client of Pub/Sub Lite that receives messages from a Lite topic and on a specified subscription. A subscription can have multiple subscriber clients. In such a case, the messages are load-balanced across the subscriber clients. In Kafka, a subscriber is called a consumer.

  * **Publisher.** An application that creates messages and sends (publishes) them to a specific Lite topic. A topic can have multiple publishers. In Kafka, a publisher is called a producer.




## Differences between Kafka and Pub/Sub Lite

While Pub/Sub Lite is conceptually similar to Kafka, it's a different system with a narrower API that is more focused on data ingestion. While the differences are immaterial for stream ingestion and processing, there are some specific use cases where these differences are important.

### Kafka as a database

Unlike Kafka, Pub/Sub Lite doesn't currently support transactional publishing or log compaction, although idempotence is supported. These Kafka features are more useful when you use Kafka as a database than as a messaging system. If you use Kafka primarily as a database, consider running your own Kafka cluster or using a managed Kafka solution such as [Confluent Cloud](https://docs.confluent.io/home/overview.html). If neither of these solutions are an option, you can also consider using a horizontally scalable database such as [Cloud Spanner](https://docs.cloud.google.com/spanner/docs).

### Kafka streams

[Kafka streams](https://docs.confluent.io/platform/current/streams/overview.html) is a data processing system built on top of Kafka. While it does allow injection of consumer clients, it requires access to all administrator operations. Kafka Streams also uses the transactional database properties of Kafka for storing internal metadata. So, Pub/Sub Lite cannot currently be used for Kafka Streams applications.

[Apache Beam](https://beam.apache.org/documentation/) is a similar streaming data processing system which is integrated with Kafka, Pub/Sub, and Pub/Sub Lite. You can run Beam pipelines in a fully-managed way with [Dataflow](https://docs.cloud.google.com/dataflow/docs), or on your preexisting [Apache Flink](https://beam.apache.org/documentation/runners/flink/) and [Apache Spark](https://beam.apache.org/documentation/runners/spark/) clusters.

### Monitor

Kafka clients can read server-side metrics. In Pub/Sub Lite, metrics relevant to publisher and subscriber behavior are managed through [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) with no additional configuration.

### Capacity management

The capacity of a Kafka topic is determined by the capacity of the cluster. Replication, key compaction, and batch settings determine the capacity required to service any given topic on the Kafka cluster. The throughput of a Kafka topic is limited by the capacity of the machines on which the brokers are running. By contrast, you must define both storage and throughput capacity for a Pub/Sub Lite topic. Pub/Sub Lite storage capacity is a configurable property of the topic. Throughput capacity is based on the capacity of the configured [reservation](https://docs.cloud.google.com/pubsub/lite/docs/reservations), and inherent or configured per-partition limits.

### Authentication and security

Apache Kafka supports several open authentication and encryption mechanisms. With Pub/Sub Lite, authentication is based on the [IAM system](https://docs.cloud.google.com/iam/docs). Security is assured through encryption at rest and in transit. Read more about Pub/Sub Lite authentication in the Migration workflow section, later in this document.

## Map Kafka properties to Pub/Sub Lite properties

Kafka has many configuration options that control topic structure, limits, and broker properties. Some common ones useful for data ingestion are discussed in this section, with their equivalents in Pub/Sub Lite. As Pub/Sub Lite is a managed system, you don't have to consider many broker properties.

### Topic configuration properties

**Kafka property** | **Pub/Sub Lite property** | **Description**  
---|---|---  
[retention.bytes](https://kafka.apache.org/documentation/#topicconfigs_retention.bytes) | Storage per partition  | All the partitions in a Lite topic have the same configured storage capacity. The total storage capacity of a Lite topic is the sum of the storage capacity of all the partitions in the topic.   
[retention.ms](https://kafka.apache.org/documentation/#topicconfigs_retention.ms) | Message retention period  | The maximum amount of time for which a Lite topic stores messages. If you don't specify a message retention period, the Lite topic stores messages until you exceed the storage capacity.   
[flush.ms](https://kafka.apache.org/documentation/#topicconfigs_flush.ms), [acks](https://kafka.apache.org/documentation/#producerconfigs_acks) | Not configurable in Pub/Sub Lite  | Publishes are not acknowledged until they are guaranteed to be persisted to replicated storage.   
[max.message.bytes](https://kafka.apache.org/documentation/#topicconfigs_max.message.bytes) | Not configurable in Pub/Sub Lite  | 3.5 MiB is the maximum message size that can be sent to Pub/Sub Lite. Message sizes are calculated in a [repeatable manner](https://docs.cloud.google.com/pubsub/pricing#throughput_costs_lite).   
[message.timestamp.type](https://kafka.apache.org/documentation/#topicconfigs_message.timestamp.type) | Not configurable in Pub/Sub Lite  | When using the consumer implementation, the event timestamp is chosen when present or the publish timestamp is used in its stead. Both publish and event timestamps are available when using Beam.   
  
To learn more about the Lite topic properties, see [Properties of a Lite topic](https://docs.cloud.google.com/pubsub/lite/docs/topics#provisioning_capacity).

### Producer configuration properties

Pub/Sub Lite supports the [Producer wire protocol](https://kafka.apache.org/protocol.html). Some properties change the behavior of the producer Cloud Client Libraries; some common ones are discussed in the following table.

**Kafka property** | **Pub/Sub Lite property** | **Description**  
---|---|---  
[auto.create.topics.enable](https://kafka.apache.org/documentation/#brokerconfigs_auto.create.topics.enable) | Not configurable in Pub/Sub Lite  | Create a topic and a subscription that is roughly equivalent to a consumer group for a single topic in Pub/Sub Lite. You can use the console, gcloud CLI, API, or the Cloud Client Libraries.   
[key.serializer](https://kafka.apache.org/documentation/#producerconfigs_key.serializer), [value.serializer](https://kafka.apache.org/documentation/#producerconfigs_value.serializer) | Not configurable in Pub/Sub Lite  | Required when using the Kafka Producer or equivalent library communicating using the wire protocol.  
[batch.size](https://kafka.apache.org/documentation/#producerconfigs_batch.size) | Supported in Pub/Sub Lite  | Batching is supported. The recommended value for this value is 10 MiB for best performance.   
[linger.ms](https://kafka.apache.org/documentation/#producerconfigs_linger.ms) | Supported in Pub/Sub Lite  | Batching is supported. The recommended value for this value is 50 ms for best performance.   
[max.request.size](https://kafka.apache.org/documentation/#producerconfigs_max.request.size) | Supported in Pub/Sub Lite  | The server imposes a limit of 20 MiB per batch. Set this value to lower than 20 MiB in your Kafka client.   
[enable.idempotence](https://kafka.apache.org/documentation/#producerconfigs_enable.idempotence) | Supported in Pub/Sub Lite   
[compression.type](https://kafka.apache.org/documentation/#producerconfigs_compression.type) | Not supported in Pub/Sub Lite  | You must explicitly set this value to `none`.   
  
### Consumer configuration properties

Pub/Sub Lite supports the [Consumer wire protocol](https://kafka.apache.org/protocol.html). Some properties change the behavior of the consumer Cloud Client Libraries; some common ones are discussed in the following table.

**Kafka property** | **Description**  
---|---  
[key.deserializer](https://kafka.apache.org/documentation/#consumerconfigs_key.deserializer), [value.deserializer](https://kafka.apache.org/documentation/#consumerconfigs_value.deserializer) | Required when using the Kafka Consumer or equivalent library communicating using the wire protocol.  
[auto.offset.reset](https://kafka.apache.org/documentation/#consumerconfigs_auto.offset.reset) | This configuration is not supported or needed. Subscriptions are guaranteed to have a defined offset location after they are created.   
[message.timestamp.type](https://kafka.apache.org/documentation/#topicconfigs_message.timestamp.type) | The publish timestamp is always available from Pub/Sub Lite and guaranteed to be non-decreasing on a per partition basis. Event timestamps may or may not be present depending on if they were attached to the message when published. Both publish and event timestamps are available at the same time when using Dataflow.   
[max.partition.fetch.bytes](https://kafka.apache.org/documentation/#consumerconfigs_max.partition.fetch.bytes), [max.poll.records](https://kafka.apache.org/documentation/#consumerconfigs_max.poll.records) | Imposes a soft limit on the number of records and bytes returned from poll() calls and the number of bytes returned from internal fetch requests. The default for `max.partition.fetch.bytes` of 1MiB may limit your client's throughput- consider raising this value.   
  
## Compare Kafka and Pub/Sub Lite features

The following table compares Apache Kafka features with Pub/Sub Lite features:

**Feature** | **Kafka** | **Pub/Sub Lite**  
---|---|---  
Message ordering  | Yes  | Yes   
Message deduplication  | Yes  | Yes using [Dataflow](https://docs.cloud.google.com/dataflow/docs/concepts/streaming-with-cloud-pubsub#efficient_deduplication)  
Push subscriptions  | No  | Yes using [Pub/Sub export](https://docs.cloud.google.com/pubsub/lite/docs/export-pubsub)  
Transactions  | Yes  | No   
Message storage  | Limited by available machine storage  | Unlimited   
Message replay  | Yes  | Yes   
Logging and monitoring  | Self-managed  | Automated with [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs)  
Stream processing  | Yes with [Kafka Streams](https://kafka.apache.org/documentation/streams/), [Apache Beam](https://beam.apache.org/documentation/), or [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs).  | Yes with Beam or Managed Service for Apache Spark.   
  
The following table compares what functionality is self-hosted with Kafka and what functionality is managed by Google by using Pub/Sub Lite:

**Feature** | **Kafka** | **Pub/Sub Lite**  
---|---|---  
Availability  | Manually deploy Kafka to additional locations.  | Deployed across the world. See [locations](https://docs.cloud.google.com/pubsub/lite/docs/locations).   
Disaster recovery  | Design and maintain your own backup and replication.  | Managed by Google.   
Infrastructure management  | Manually deploy and operate virtual machines (VMs) or machines. Maintain consistent versioning and patches.  | Managed by Google.   
Capacity planning  | Manually plan storage and compute needs in advance.  | Managed by Google. You can increase compute and storage at any time.   
Support  | None.  | 24-hour on-call staff and support available.   
  
## Kafka and Pub/Sub Lite cost comparison

The way you estimate and manage costs in Pub/Sub Lite is different than in Kafka. The costs for a Kafka cluster on-premises or in cloud include the cost of machines, disk, networking, inbound messages, and outbound messages. It also includes overhead costs for managing and maintaining these systems and their related infrastructure. When managing a Kafka cluster, you must manually upgrade the machines, plan cluster capacity, and implement disaster recovery that includes extensive planning and testing. You must aggregate all these various costs to determine your true total cost of ownership (TCO).

Pub/Sub Lite pricing includes the reservation cost (published bytes, subscribed bytes, [bytes handled by the Kafka proxy](https://cloud.google.com/pubsub/pricing#kafka-reservation-note)) and the cost of provisioned storage. You pay for exactly the resources that you reserve in addition to outbound message charges. You can use the [pricing calculator](https://cloud.google.com/products/calculator) to provide an estimate of your costs.

## Migration workflow

To migrate a topic from a Kafka cluster to Pub/Sub Lite, use the following instructions.

### Configure Pub/Sub Lite resources

  1. Create a Pub/Sub Lite [reservation](https://docs.cloud.google.com/pubsub/lite/docs/reservations) for the expected throughput for all the topics that you're migrating.

Use the Pub/Sub Lite [pricing calculator](https://cloud.google.com/products/calculator) to calculate the aggregate throughput metrics of your existing Kafka topics. For more information about how to create reservations, see [Create and manage Lite reservations](https://docs.cloud.google.com/pubsub/lite/docs/reservations).

  2. Create one Pub/Sub Lite topic for each corresponding topic in Kafka.

For more information about how to create Lite topics, see [Create and manage Lite topics](https://docs.cloud.google.com/pubsub/lite/docs/topics).

  3. Create one Pub/Sub Lite subscription for each corresponding consumer group and topic pair in the Kafka cluster.

For example, for a consumer group named `consumers` that consumes from `topic-a` and `topic-b`, you must create a subscription `consumers-a` attached to `topic-a` and a subscription `consumers-b` attached to `topic-b`. For more information about how to create subscriptions, see [Create and manage Lite subscriptions](https://docs.cloud.google.com/pubsub/lite/docs/subscriptions).




### Authenticate to Pub/Sub Lite

Based on the type of your Kafka client, choose one of the following methods:

  * Java-based Kafka clients running version 3.1.0 or later with rebuilding

  * Java-based Kafka clients running version 3.1.0 or later without rebuilding

  * All other clients without rebuilding




#### Java-based Kafka clients version 3.1.0 or later with rebuilding

For Java-based Kafka clients of version 3.1.0 or later that can be rebuilt on the instance where you're running the Kafka client:

  1. Install the `com.google.cloud:pubsublite-kafka-auth` package.

  2. Obtain the necessary parameters for authenticating to Pub/Sub Lite with the help of `com.google.cloud.pubsublite.kafka.ClientParameters.getParams`.

The `getParams()` method (see a [code sample](https://github.com/googleapis/java-pubsublite-kafka/blob/main/samples/snippets/src/main/java/pubsublite/KafkaProducerExample.java) ) initializes the following [JAAS](https://kafka.apache.org/documentation.html#security_sasl_jaasconfig) and [SASL](https://kafka.apache.org/documentation.html#security_sasl_config) configurations as parameters for authenticating to Pub/Sub Lite:
         
         security.protocol=SASL_SSL
         sasl.mechanism=OAUTHBEARER
         sasl.oauthbearer.token.endpoint.url=http://localhost:14293
         sasl.jaas.config=org.apache.kafka.common.security.oauthbearer.secured.OAuthBearerLoginCallbackHandler
         




#### Java-based Kafka clients running version 3.1.0 or later without rebuilding

For Kafka clients that support [KIP-768](https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=186877575#KIP768:ExtendSASL/OAUTHBEARERwithSupportforOIDC-TokenRetrievalLogic), we support configuration-only OAUTHBEARER authentication that uses a Python sidecar script. These versions include the [January 2022](https://kafka.apache.org/downloads) Java version 3.1.0 or later.

Perform the following steps on the instance where you're running your Kafka client:

  1. Install Python 3.6 or higher.

See [Installing Python](https://docs.cloud.google.com/python/docs/setup#installing_python).

  2. Install the Google authentication package: `pip install google-auth`

This library simplifies the various server-to-server authentication mechanisms to access Google APIs. See the [`google-auth` page](https://pypi.org/project/google-auth).

  3. Run the [`kafka_gcp_credentials.py`](https://github.com/googleapis/java-pubsublite-kafka/blob/main/kafka_gcp_credentials.py) script.

This script starts a local HTTP server and fetches the default Google Cloud credentials in the environment using [`google.auth.default()`](https://googleapis.dev/python/google-auth/latest/reference/google.auth.html#google.auth.default).

The [principal](https://docs.cloud.google.com/iam/docs/principal-identifiers) in the fetched credentials must have the `pubsublite.locations.openKafkaStream` permission for the Google Cloud project you are using and the location to which you are connecting. Pub/Sub Lite Publisher (`roles/pubsublite.publisher`) and Pub/Sub Lite Subscriber (`roles/pubsublite.subscriber`) roles have this required permission. Add these roles to your [principal](https://docs.cloud.google.com/pubsub/lite/docs/access-control#granting_roles).

The credentials are used in the [SASL/OAUTHBEARER authentication](https://kafka.apache.org/documentation.html#security_sasl_oauthbearer_brokerconfig) for the Kafka client.

The following parameters are required in your properties to authenticate to Pub/Sub Lite from the Kafka client:
         
         security.protocol=SASL_SSL
         sasl.mechanism=OAUTHBEARER
         sasl.oauthbearer.token.endpoint.url=localhost:14293
         sasl.login.callback.handler.class=org.apache.kafka.common.security.oauthbearer.secured.OAuthBearerLoginCallbackHandler
         sasl.jaas.config=org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule \
           required clientId="unused" clientSecret="unused" \
           extension_pubsubProject="PROJECT_ID";
         

Replace PROJECT_ID with the ID of your project running Pub/Sub Lite.




#### All other clients without rebuilding

For all other clients, perform the following steps:

  1. Download a [service account key JSON file](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys) for the service account that you intend to use for your client.

  2. Encode the service account file by using base64-encode to use as your authentication string.

On Linux or macOS systems, you can use the `base64` command (often installed by default) as follows:
         
         base64 < my_service_account.json > password.txt
         

You can use the contents of the password file for authentication with the following parameters.

### Java
         
         security.protocol=SASL_SSL
         sasl.mechanism=PLAIN
         sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required \
          username="PROJECT_ID" \
          password="contents of base64 encoded password file";
         

Replace PROJECT_ID with the ID of your project running Pub/Sub.

### librdkafka
         
         security.protocol=SASL_SSL
         sasl.mechanism=PLAIN
         sasl.username=PROJECT_ID
         sasl.password=contents of base64 encoded password file
         

Replace PROJECT_ID with the ID of your project running Pub/Sub..




### Clone data using Kafka Connect

The Pub/Sub Lite team maintains an implementation of a Kafka Connect Sink. You can configure this implementation to copy data from a Kafka topic to a Pub/Sub Lite topic using a Kafka Connect cluster.

To configure the connector to perform the data copy, see [Pub/Sub Group Kafka Connector](https://github.com/googleapis/java-pubsub-group-kafka-connector).

If you want to ensure that partition affinity is unaffected by the migration process, ensure that the kafka topic and Pub/Sub Lite topic have the same number of partitions, and that the `pubsublite.ordering.mode` property is set to `KAFKA`. This causes the connector to route messages to the Pub/Sub Lite partition with the same index as the kafka partition they were originally published to.

### Migrate consumers

Pub/Sub Lite's resource model is different than Kafka's. Most notably, unlike a consumer group, a subscription is an explicit resource and is associated with exactly one topic. Because of this difference, any place in the Kafka Consumer API that requires a `topic` to be passed, the full subscription path must be passed instead.

In addition to the SASL configurations for the Kafka client, the following settings are also required when using the Kafka Consumer API to interact with Pub/Sub Lite.
    
    
    bootstrap.servers=REGION-kafka-pubsub.googleapis.com:443
    group.id=unused
    

Replace REGION with the [region](https://docs.cloud.google.com/pubsub/lite/docs/locations) where your Pub/Sub Lite subscription exists.

Before starting the first Pub/Sub Lite consumer job for a given subscription, you can initiate (but don't wait on) an [admin seek](https://docs.cloud.google.com/pubsub/lite/docs/seek) operation to set the initial location for your consumer.

When you start your consumers, they reconnect to the current offset in the message backlog. Run both the old and new clients in parallel as long as it takes to verify their behavior, then turn down the old consumer clients.

### Migrate producers

In addition to the SASL configurations for the Kafka client, the following is also required as a producer param when using the Kafka Producer API to interact with Pub/Sub Lite.
    
    
    bootstrap.servers=REGION-kafka-pubsub.googleapis.com:443
    

Replace REGION with the [region](https://docs.cloud.google.com/pubsub/lite/docs/locations) where your Pub/Sub Lite topic exists.

After you migrate **all** the consumers of the topic to read from Pub/Sub Lite, move your producer traffic to write to Pub/Sub Lite directly.

Gradually migrate the producer clients to write to the Pub/Sub Lite topic instead of the Kafka topic.

Restart the producer clients to pick up new configurations.

### Turn down Kafka Connect

After you migrate **all** the producers to write to Pub/Sub Lite directly, the connector does not copy data anymore.

You can turn down the Kafka Connect instance.

## Troubleshoot Kafka connections

Since Kafka clients communicate through a bespoke wire protocol, we cannot provide error messages for failures in all requests. Rely on the error codes sent as part of the message.

You can see more details about errors that occur in the client by setting the logging level for the `org.apache.kafka` prefix to `FINEST`.

### Low throughput and increasing backlog

There are multiple reasons why you might be seeing low throughput and an increasing backlog. One reason might be insufficient capacity.

You can configure throughput capacity at the topic level or by using reservations. If insufficient throughput capacity for subscribe and publish is configured, the corresponding throughput for subscribe and publish is throttled.

This throughput error is signaled by the [`topic/flow_control_status`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-pubsublite) metric for publishers, and the [`subscription/flow_control_status`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-pubsublite) metric for subscribers. The metric provides the following states:

  * `NO_PARTITION_CAPACITY`: This message indicates that the per-partition throughput limit is reached.

  * `NO_RESERVATION_CAPACITY`: This message indicates that the per-reservation throughput limit is reached.




You can view the utilization graphs for the topic or reservation publish and subscribe quota and check whether utilization is at or near 100%.

To resolve this issue, increase the [throughput capacity](https://docs.cloud.google.com/pubsub/lite/docs/topics#throughput) of the topic or reservation.

### Topic authorization failed error message

Publishing by using the Kafka API requires the Lite service agent to have the right permissions to publish to the Pub/Sub Lite topic.

You get the error `TOPIC_AUTHORIZATION_FAILED` in your client in the event that you don't have the correct permissions to publish to the Pub/Sub Lite topic.

To resolve the issue, check if the Lite service agent for the project passed in the auth configuration.

### Invalid topic error message

Subscribing by using the Kafka API requires passing the full subscription path all places where a `topic` is expected in the Kafka Consumer API.

You get the error `INVALID_TOPIC_EXCEPTION` in your Consumer client if you don't pass a well formatted subscription path.

### Invalid request when not using reservations

Using kafka wire protocol support requires that all topics have an associated reservation in order to charge for usage.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
