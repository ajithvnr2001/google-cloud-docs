---
url: https://docs.cloud.google.com/pubsub/docs/migrating-from-kafka-to-pubsub/
title: Migrate from Kafka to Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:01.737974+00:00
---

# Migrate from Kafka to Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/migrating-from-kafka-to-pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Migrate from Kafka to Pub/Sub Stay organized with collections  Save and categorize content based on your preferences. 

This document is useful if you are considering migrating from self-managed [Apache Kafka](https://kafka.apache.org/) to [Pub/Sub](https://docs.cloud.google.com/pubsub/docs), because it can help you review and consider features, pricing, and use cases. Each section identifies a common Kafka use case and offers practical guidance for achieving the same capabilities in Pub/Sub.

## Overview of Pub/Sub

Pub/Sub is an asynchronous messaging service. Pub/Sub decouples services that produce events from services that process events. You can [use Pub/Sub as messaging-oriented middleware or event ingestion and delivery for streaming analytics pipelines](https://docs.cloud.google.com/pubsub/docs/overview#scenarios). In both scenarios, a publisher application creates and sends messages to a topic. Subscriber applications create a subscription to a topic to receive messages from it. A subscription is a named entity that represents an interest in receiving messages on a particular topic.

Pub/Sub runs in all [Google Cloud regions](https://cloud.google.com/about/locations). Pub/Sub directs publisher traffic to the nearest Google Cloud data center where data storage is allowed, as defined in the [resource location restriction](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction) policy.

[Pub/Sub can integrate with many Google Cloud services](https://docs.cloud.google.com/pubsub/docs/overview#pubsub-integrations) such as [Dataflow](https://docs.cloud.google.com/dataflow), [Cloud Storage](https://docs.cloud.google.com/storage), and [Cloud Run](https://docs.cloud.google.com/run/docs/triggering/pubsub-push). You can configure these services to serve as data sources that can publish messages to Pub/Sub, or as data sinks that can receive messages from Pub/Sub.

## Overview of Kafka

Apache Kafka is an open source, distributed, event-streaming platform, and it enables applications to publish, subscribe to, store, and process streams of events. The Kafka server is run as a cluster of machines that client applications interact with to read, write, and process events. You can use Kafka to decouple applications, send and receive messages, track activities, aggregate log data, and process streams.

Within the Kafka cluster, some nodes in the cluster are designated as brokers. Brokers receive messages from producers and store them on disk. Stored messages are organized by topic and partitioned across several different brokers in the cluster. New events published to a topic are appended to the end of one of the topic's partitions. Consumers can then fetch messages from brokers, which are read from disk and sent to the consumer.

## Understanding the differences between Kafka and Pub/Sub

The following diagram shows the differences in scaling strategy between Kafka and Pub/Sub:

![Scaling strategy with partitions for Kafka and no partitions for Pub/Sub.](https://docs.cloud.google.com/static/pubsub/images/migrating-from-kafka-to-pubsub-1-scaling.svg)

In the preceding diagram, each _M_ represents a message. Kafka brokers manage multiple ordered partitions of messages, represented by the horizontal rows of messages. Consumers read messages from a particular partition that has a capacity based on the machine that hosts that partition. Pub/Sub does not have partitions, and consumers instead read from a topic that autoscales according to demand. You configure each Kafka topic with the number of partitions that you require to handle the expected consumer load. Pub/Sub scales automatically based on demand.

### Comparing features

The following table compares Apache Kafka features with Pub/Sub features:

| Apache Kafka | Pub/Sub  
---|---|---  
Message ordering | Yes within partitions | Yes within [topics](https://docs.cloud.google.com/pubsub/docs/ordering)  
Message deduplication | Yes | Yes using [Dataflow](https://docs.cloud.google.com/dataflow/docs/concepts/streaming-with-cloud-pubsub#efficient_deduplication)  
Push subscriptions | No | [Yes](https://docs.cloud.google.com/pubsub/docs/push)  
Dead-letter queue  
(unprocessable message queue) | As of version 2.0 | [Yes](https://docs.cloud.google.com/pubsub/docs/dead-letter-topics)  
Transactions | Yes | No  
Message storage | Limited only by available machine storage | [31 days](https://docs.cloud.google.com/pubsub/quotas#resource_limits).  
A topic can retain published messages, including acknowledged messages, for a maximum of 31 days. This is configurable by the [`message_retention_duration`](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#google.pubsub.v1.Topic.FIELDS.google.protobuf.Duration.google.pubsub.v1.Topic.message_retention_duration) property of the topic.  
Message replay | Yes | [Yes](https://docs.cloud.google.com/pubsub/docs/replay-overview)  
Locality | Local cluster can replicate using [MirrorMaker](https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=27846330) | Global distributed service with [configurable message storage locations](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction)  
Logging and monitoring | Self-managed | Automated with [Cloud Logging](https://docs.cloud.google.com/logging) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring)  
Stream processing | Yes with [KSQL](https://ksqldb.io/) | Yes with [Dataflow](https://docs.cloud.google.com/dataflow)  
  
### Understanding Pub/Sub message storage and replay

By default, Pub/Sub [retains unacknowledged messages for up to 7 days](https://docs.cloud.google.com/pubsub/quotas#resource_limits), but you can configure Pub/Sub subscriptions [to retain acknowledged messages](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions/create#body.request_body.FIELDS.retain_acked_messages) for up to 7 days too, depending on the age of the oldest message (acknowledged or unacknowledged) in the subscription. By retaining acknowledged messages, you can replay some or all of those messages based on a timestamp. When you [replay messages based on a timestamp](https://docs.cloud.google.com/pubsub/docs/replay-overview#seek_to_a_time) , all messages that were received after the timestamp are marked as unacknowledged. The unacknowledged messages are then redelivered.

You can [create snapshots](https://docs.cloud.google.com/pubsub/docs/replay-overview#seek_to_a_snapshot) of individual subscriptions on demand without needing to configure your subscription in advance. For example, you can create a snapshot when deploying new subscriber code because you might need to recover from unexpected or erroneous acknowledgments.

### Built-in failsafe with dead-letter topics

Pub/Sub provides features similar to [Kafka 2.0 error handling](https://www.confluent.io/blog/kafka-connect-deep-dive-error-handling-dead-letter-queues/) and to how [Kafka Connect](https://docs.confluent.io/platform/current/connect/index.html) handles dead-letter topics. To notify Pub/Sub that a message was delivered successfully, subscribers to Pub/Sub topics can acknowledge messages that they receive and process. If your subscribers are unable to process messages for some time, Pub/Sub can [automatically forward these messages to a dead-letter topic](https://docs.cloud.google.com/pubsub/docs/dead-letter-topics) and store them for access later. You can [configure the number of attempts that Pub/Sub makes to deliver the messages](https://docs.cloud.google.com/pubsub/docs/dead-letter-topics#setting-a-dead-letter-topic) before it sends the message to the dead-letter topic.

### Deduplicating messages in Pub/Sub using Dataflow

Pub/Sub delivers each published message at least once for every subscription. In general, accommodating more-than-once delivery requires your subscriber to be [idempotent](http://wikipedia.org/wiki/Idempotence#Computer_science_meaning) when processing messages. If your existing subscribers are unable to operate idempotently, then you can [incorporate Dataflow to deduplicate messages](https://github.com/GoogleCloudPlatform/dataflow-pubsub-dedup). If your subscribers see a high rate of duplicate messages, this can indicate that they are not properly acknowledging messages, or that your acknowledgment deadline is too short.

### Message ordering in Pub/Sub

If your Kafka subscriber applications rely on message ordering, you can support this requirement in Pub/Sub when you use [ordering keys](https://docs.cloud.google.com/pubsub/docs/ordering). Currently, ordering is guaranteed for messages published in [a given region](https://cloud.google.com/about/locations). To take advantage of message ordering, ensure that your publishers and subscribers use [locational endpoints](https://docs.cloud.google.com/pubsub/docs/reference/service_apis_overview#service_endpoints) to route your messages to the correct region.

### Understanding responsibilities of self-hosted versus managed service

The following table compares what feature is self-hosted with Kafka and what feature is managed by Google by using Pub/Sub:

| Apache Kafka | Pub/Sub  
---|---|---  
Availability | Manually deploy Kafka to additional locations | Deployed in all Google Cloud regions for high availability and low latency  
Disaster recovery | Design and maintain your own backup and replication | Managed by Google  
Infrastructure management | Manually deploy and operate virtual machines (VMs) or machines. You must maintain consistent versioning and patches. | Managed by Google  
Capacity planning | Manually plan storage and compute needs in advance | Managed by Google  
Support | None | 24-hour on-call staff and support available  
  
### Pub/Sub message size limits and workarounds

Kafka and Pub/Sub both perform well when handling large volumes of small messages. Kafka places no hard limit on message size and lets you configure the allowed message size, while [Pub/Sub limits messages to 10 MB](https://docs.cloud.google.com/pubsub/quotas#resource_limits). You can indirectly send larger payloads by first storing the object in [Cloud Storage](https://docs.cloud.google.com/storage), as shown in the following diagram:

![Publisher stores object in Cloud Storage.](https://docs.cloud.google.com/static/pubsub/images/migrating-from-kafka-to-pubsub-2-large-volumes.svg)

The preceding image shows that when the publisher stores the object in Cloud Storage, it publishes a message containing the URL to that stored object. When the subscriber receives the message containing the URL, it downloads the file from Cloud Storage and continues processing as usual.

### Kafka and Pub/Sub cost comparison

The way you estimate and manage costs in Pub/Sub is different than in Kafka. The costs of a Kafka cluster on-premises or in cloud include the cost of machines, disk, networking, inbound and outbound messages, as well as the overhead costs of managing and maintaining these systems and their related infrastructure. When managing a Kafka cluster, machines often need to be manually upgraded and patched, cluster capacity often needs to be planned, and implementing disaster recovery involves extensive planning and testing. You need to infer and aggregate all these various costs to determine your true total cost of ownership (TCO).

[Pub/Sub pricing](https://cloud.google.com/pubsub/pricing) includes the data transfer from publishers and to subscribers, and the cost of temporarily storing unacknowledged messages. You pay for exactly the resources that you consume, automatically scaling its capacity according to the requirements of your application and budget.

### Architecting for reliability

Pub/Sub is a global managed service that runs in all [Google Cloud regions](https://docs.cloud.google.com/docs/geography-and-regions). Pub/Sub topics are global, meaning that they are visible and accessible from any Google Cloud location. However, any given message is stored in a single Google Cloud region that is closest to the publisher and allowed by the resource location policy. Thus, a topic can have messages stored in different regions throughout Google Cloud. Pub/Sub is resistant to zonal outages. During a regional outage, messages stored in that particular region might be inaccessible until service is restored. Depending on your availability requirements, you can use [locational service endpoints](https://docs.cloud.google.com/pubsub/docs/reference/service_apis_overview#service_endpoints) to implement a failover policy if a regional outage occurs.

### Security and authentication

[Apache Kafka supports multiple authentication mechanisms](https://www.confluent.io/blog/apache-kafka-security-authorization-authentication-encryption/) including client certificates-based authentication, Kerberos, LDAP, and username and password. For authorization, Kafka supports using access control lists (ACLs) to determine which producers and consumers have access to which topics.

Pub/Sub supports [authentication](https://docs.cloud.google.com/pubsub/docs/authentication) for Google Cloud user accounts and service accounts. Granular access control to Pub/Sub topics and subscriptions is governed by [Identity and Access Management (IAM)](https://docs.cloud.google.com/pubsub/docs/access-control) in Google Cloud. Pub/Sub operations are [rate limited](https://docs.cloud.google.com/pubsub/quotas#high-volume_operations) when using user accounts. If you need to make high volume transactions, you can use service accounts to interact with Pub/Sub.

## Planning your migration to Pub/Sub

Any migration to Google Cloud begins with [assessing your workloads](https://docs.cloud.google.com/solutions/migration-to-gcp-assessing-and-discovering-your-workloads) and [building your foundation](https://docs.cloud.google.com/solutions/migration-to-google-cloud-building-your-foundation).

### Phased migration using the Pub/Sub Kafka Connector

The [Pub/Sub Kafka connector](https://github.com/googleapis/java-pubsub-group-kafka-connector) lets you migrate your Kafka infrastructure to Pub/Sub in phases.

You can configure the Pub/Sub connector to forward all messages on specific topics from Kafka to Pub/Sub. Then, you can update individual subscriber applications to receive messages on those topics from Pub/Sub, while your publisher applications continue to publish messages to Kafka. This phased approach lets you update, test, and monitor subscriber applications in an iterative way that minimizes risk of error and downtime.

This section includes two diagrams that can help you visualize this process in two distinct phases. The following diagram shows the configuration during the migration phase:

![Stage one of migration.](https://docs.cloud.google.com/static/pubsub/images/migrating-from-kafka-to-pubsub-3-connector-phase-1.svg)

In the preceding diagram, current subscribers continue to receive messages from Kafka, and you update the subscribers one by one to receive messages from Pub/Sub instead.

After all subscribers to a particular topic have been updated to receive messages from Pub/Sub, you can then update the publisher applications for that topic to publish messages to Pub/Sub. Then, you can test and monitor the message flows end-to-end in order to verify the setup.

The following diagram shows the configuration after all subscribers are receiving messages from Pub/Sub:

![Stage two of migration.](https://docs.cloud.google.com/static/pubsub/images/migrating-from-kafka-to-pubsub-4-connector-phase-2.svg)

Over time, all your publishers are updated to publish directly to Pub/Sub, and then your migration is complete. Many teams use this approach to update their applications in parallel. Kafka can coexist alongside Pub/Sub for as long as needed in order to ensure a successful migration.

### Monitoring Pub/Sub

During and after your migration from Kafka to Pub/Sub, it's important to monitor your applications. Pub/Sub exports metrics by using [Cloud Monitoring](https://docs.cloud.google.com/monitoring), which can help provide visibility into the performance, uptime, and overall health of your applications. For example, you can ensure that your subscribers are keeping up with the flow of messages by [monitoring the number of undelivered messages](https://docs.cloud.google.com/pubsub/docs/monitoring#monitoring_the_backlog). To monitor undelivered messages, you create alerts when the timestamp of the oldest unacknowledged message extends beyond a certain threshold. You can also monitor the health of the Pub/Sub service itself by [monitoring the send request count metric](https://docs.cloud.google.com/pubsub/docs/monitoring#keeping_publishers_healthy) and examining the response codes.

## What's next

  * [Stream analytics with Pub/Sub](https://docs.cloud.google.com/solutions/stream-analytics).
  * [Pub/Sub API reference](https://docs.cloud.google.com/pubsub/docs/apis).
  * [Pub/Sub Monitoring documentation](https://docs.cloud.google.com/pubsub/docs/monitoring).
  * [Architecting disaster recovery for cloud infrastructure outages](https://docs.cloud.google.com/solutions/disaster-recovery/architecture#pubsub).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
