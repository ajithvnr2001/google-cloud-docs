---
url: https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-pubsub/
title: Migrate from Pub/Sub Lite to Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:14:09.004060+00:00
---

# Migrate from Pub/Sub Lite to Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/lite/docs/publish-receive-messages-console)



Send feedback 

#  Migrate from Pub/Sub Lite to Pub/Sub Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Pub/Sub Lite is deprecated. Effective January 31, 2027, Pub/Sub Lite will be turned down.   


  * Current customers: Pub/Sub Lite remains functional until January 31, 2027.   
If you have not used Pub/Sub Lite within the 90-day period preceding July 15, 2025 (April 15, 2025 - July 15, 2025), you won't be able to access Pub/Sub Lite starting on July 15, 2025. 
  * New customers: Pub/Sub Lite is no longer available for new customers after September 24, 2024.



You can migrate your Pub/Sub Lite service to [Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-managed-service-for-apache-kafka) or [Pub/Sub](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-pubsub).

This document provides information on how to migrate your Pub/Sub Lite applications and data from Pub/Sub Lite to Pub/Sub.

To migrate to Pub/Sub, you use the Pub/Sub Lite [export subscription](https://docs.cloud.google.com/pubsub/lite/docs/export-pubsub) feature. The export subscription feature converts messages from a Pub/Sub Lite to a Pub/Sub message, using a type of subscription called an _export subscription_.

## Differences between Pub/Sub Lite and Pub/Sub

Pub/Sub and Pub/Sub Lite are both horizontally scalable messaging services, but each service has key differences in how they work. To understand these differences in detail, read [Choose Pub/Sub or Pub/Sub Lite](https://docs.cloud.google.com/pubsub/docs/choosing-pubsub-or-lite).

The following sections outline some of the key differences between each service that are relevant when migrating between services. These include the following considerations:

  * Data locality and replication
  * Delivery modes
  * Parallelism and ordering
  * Replay and purge
  * Capacity management and Pricing



### Data locality and replication

  * **Pub/Sub Lite**. Regional Pub/Sub Lite topics replicate data to a secondary zone within the same region. Zonal Pub/Sub Lite topics store data in a single zone without replication.

  * **Pub/Sub**. Pub/Sub replicates data across three zones within a region.




**Key migration point**

It's important to understand how each service replicates data differently.

When using Pub/Sub, you can ensure that your data is stored in preferred regions by using Pub/Sub [message storage policies](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction).

  * Pub/Sub doesn't provide control over the specific zones where messages are stored. Instead, it always replicates data across three zones within a region as dictated by the message storage policy.

  * If you don't specify a message storage policy, Pub/Sub automatically determines where messages are stored based on your [Resource Location Restriction organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). If you don't explicitly set an organization policy, Pub/Sub allows all regions and automatically selects one to store messages in.




### Delivery modes

  * **Pub/Sub Lite**. For message delivery, Pub/Sub Lite only supports the [StreamingPull RPC](https://docs.cloud.google.com/pubsub/docs/pull#streamingpull_api) API.

  * **Pub/Sub**. For message delivery, Pub/Sub offers [multiple message delivery options](https://docs.cloud.google.com/pubsub/docs/subscription-overview), including StreamingPull message delivery.




**Key migration point**

If you want to replicate Pub/Sub Lite behavior in Pub/Sub (for example, low latency and high efficiency), implement your consumer clients using the StreamingPull API. Alternatively, you can implement your Pub/Sub subscription using other available delivery modes such as [Push delivery](https://docs.cloud.google.com/pubsub/docs/push).

### Parallelism and ordering

  * **Pub/Sub Lite**. Pub/Sub Lite supports parallelism per partition.

  * **Pub/Sub**. Pub/Sub supports parallelism per message.




**Key migration point**

Pub/Sub isn't a partition-based solution. Pub/Sub messages can also be processed concurrently, meaning that the message order is not guaranteed. If your application requires message ordering, use Pub/Sub [ordering keys](https://docs.cloud.google.com/pubsub/docs/ordering).

When using the export subscription in Pub/Sub Lite, the Pub/Sub Lite key is used as the ordering key in the Pub/Sub Message. This ensures that the messages continue to be delivered in order.

To ensure compatibility with Pub/Sub messages, verify that your Pub/Sub Lite keys contain only UTF-8 encoded characters.

  * Pub/Sub Lite keys are stored as bytes.
  * Pub/Sub ordering keys are stored as strings.



Pub/Sub ordering keys have a maximum publisher throughput of 1 MBps. Message ordering in Pub/Sub is only guaranteed within a single region. To receive ordered messages in Pub/Sub, you must explicitly enable message ordering in the subscription settings.

### Replay and purge

  * **Pub/Sub Lite**. Pub/Sub Lite supports the [seek](https://docs.cloud.google.com/pubsub/docs/replay-overview) feature without requiring additional configuration.

  * **Pub/Sub**. Pub/Sub supports the seek feature but requires additional configuration to set it up.




**Key migration point**

To enable the seek feature, Pub/Sub requires you to explicitly configure settings on both the topic and the subscription.

  * Topic: You must configure a message retention duration
  * Subscription: You must configure an acknowledged message retention.



Configuring these settings is crucial if you need exact parity with Pub/Sub Lite or if your migration requires message replay or purging. Regardless of your specific requirements, the ability to seek and reprocess messages is a valuable safeguard during a phased migration. It enables rollback and minimizes data loss if unexpected issues arise.

### Capacity management and Pricing

  * **Pub/Sub Lite**. Pub/Sub Lite capacity is manually provisioned by configuring storage and throughput capacity using [Pub/Sub Lite reservations](https://docs.cloud.google.com/pubsub/lite/docs/reservations).

  * **Pub/Sub**. Pub/Sub is fully managed and scales automatically.




**Key migration point**

When transitioning to Pub/Sub, you can manage capacity and pricing by setting quota overrides or by requesting a quota change for your Pub/Sub resources.

The primary reason to manage Pub/Sub capacity is to adhere to strict cost requirements. If you don't have any strict cost limits, Pub/Sub can efficiently manage resources without much intervention. Pub/Sub is billed based on usage. For detailed information, see [Pub/Sub pricing](https://docs.cloud.google.com/pubsub/pricing).

## Plan a migration

To migrate from Pub/Sub Lite to Pub/Sub, you can use the Pub/Sub Lite export subscription feature. Export subscription lets you migrate your Pub/Sub Lite application in phases. Adopting a phased approach lets you update, test, and monitor your migration iteratively, minimizing the risk of errors and downtime.

### Before you begin

  * Evaluate your existing Pub/Sub Lite application and map out the corresponding Pub/Sub features that you need.
  * Ensure that Pub/Sub meets all of your functional and business requirements.



## Phased migration workflow

The following steps provide an overview of the export subscription migration workflow.

  1. Create the relevant Pub/Sub [topics](https://docs.cloud.google.com/pubsub/docs/create-topic) and a [subscription](https://docs.cloud.google.com/pubsub/docs/subscriber) to the topic.
  2. Create a Pub/Sub Lite [export subscription](https://docs.cloud.google.com/pubsub/lite/docs/export-pubsub).
  3. Subscribe to both Pub/Sub and Pub/Sub Lite subscriptions.
  4. Gradually update publishers to send messages to the Pub/Sub topic instead of the Pub/Sub Lite topic.
  5. Verify that the migrated workload is working as intended.
  6. Turn down Pub/Sub Lite publishers and subscribers.



## Migration phases

The following sections provide details on each step in the phased migration workflow.

### Create Pub/Sub topics and subscriptions

Create a corresponding Pub/Sub topic and its subscription. In this phase, you configure required topics and subscriptions settings, such as message retention, message acknowledgment and message storage policies.

If required, establish and set up quotas to prevent overuse and unexpected billing. Most importantly, we strongly recommend you to set up a dead-letter Pub/Sub Lite topic to capture any messages that fail to migrate successfully to Pub/Sub. This lets you troubleshoot errors and identify the root cause of export failures and resend failed messages to the correct topic, ensuring no data loss.

### Create Pub/Sub Lite export subscriptions

For every topic, create a Pub/Sub Lite export subscription to export messages from the Pub/Sub Lite topic to its corresponding Pub/Sub topic. Instead of individually setting throughput capacity for each export subscription, use a Pub/Sub Lite [reservation](https://docs.cloud.google.com/pubsub/lite/docs/reservations) to efficiently manage throughput for all your export subscriptions collectively. By the end of this phase, your Pub/Sub Lite and Pub/Sub topics both receive the same messages from the point the export subscriptions were created.

You can then use the Pub/Sub topics to incrementally develop and test your subscriber clients in isolated phases. This approach minimizes disruption to your existing Pub/Sub Lite applications.

### Dual-subscribe to Pub/Sub Lite and Pub/Sub topics

In a development environment, update your subscriber clients to read messages directly from Pub/Sub topics, using the appropriate [Pub/Sub client library](https://docs.cloud.google.com/pubsub/docs/reference/libraries). Unlike Pub/Sub Lite, Pub/Sub offers multiple. Unlike Pub/Sub Lite, Pub/Sub offers multiple delivery modes (pull and push), so choose the one that best aligns with your application's requirements.

  * To emulate the same behavior as Pub/Sub Lite, configure your Pub/Sub instance with the StreamingPull API.

  * In a system with multiple consumer applications, gradually migrate each application one-by-one. For each subscriber application, run the Pub/Sub Lite subscriber and the new Pub/Sub subscriber in parallel, so you can verify the behavior and performance of the new subscriber. Closely monitor both subscribers to ensure message delivery consistency, error handling and overall functionality. After all subscribers are successfully migrated and validated, decommission the old Pub/Sub Lite subscriber clients.




### Update publishers

After all your subscribers are successfully consuming messages from Pub/Sub, you can gradually update your publishers to send messages directly to Pub/Sub topics. To do this, update your publishers to use the [Pub/Sub client libraries](https://docs.cloud.google.com/pubsub/docs/reference/libraries). This ensures that you can gradually shift traffic from Pub/Sub Lite to Pub/Sub.

### Turn down Pub/Sub Lite

After you have successfully migrated all your subscribers and publishers to Pub/Sub, you can shut down your Pub/Sub Lite resources. This helps you avoid incurring unnecessary costs for unused infrastructure.

## What's next

  * [Learn more about Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
