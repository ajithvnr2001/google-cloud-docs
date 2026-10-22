---
url: https://docs.cloud.google.com/pubsub/docs/replay-overview/
title: Replay and purge messages with seek \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:37.951467+00:00
---

# Replay and purge messages with seek  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/replay-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Replay and purge messages with seek Stay organized with collections  Save and categorize content based on your preferences. 

After you acknowledge messages in Pub/Sub, these messages become inaccessible to the subscriber client. In addition, subscriber clients must process every message in a subscription even if only a subset is needed.

The **seek** feature extends subscriber capabilities by allowing you to alter the acknowledgment state of messages in bulk. For example, you can replay previously acknowledged messages or purge messages in bulk. In addition, you can copy the acknowledgment state of one subscription to another by using seek in combination with a **snapshot**.

For a quick demonstration of how these features work, see [Replay a message in Pub/Sub by seeking to a snapshot or timestamp](https://docs.cloud.google.com/pubsub/docs/replay-api-messages).

## Snapshot and seek overview

A Pub/Sub snapshot is a durable, consistent, and reliable point-in-time view of the message acknowledgment (ack) state of a subscription. A snapshot records the acknowledgment state of all the messages within a subscription at the moment of its creation. A snapshot retains the unacknowledged messages of the source subscription at the time of creation of the snapshot, and any messages published to the topic after the snapshot is created.

The lifetime of a snapshot is determined by the existing backlog of the source subscription. The lifetime equals 7 days minus the age of the oldest unacknowledged message in the subscription. For example, consider a snapshot of a subscription with a backlog where the oldest unacknowledged message is 1 day old. The snapshot expires after 6 days. This timeline is necessary for snapshots to offer strong at-least-once delivery guarantee.

The maximum possible lifetime of a snapshot is seven days. You cannot create a snapshot that would expire in less than 1 hour after the time of its creation.

The seek feature lets you seek to a specific snapshot or timestamp for a subscription. This feature lets you control how Pub/Sub can deliver messages from a specific point in time or from a specific snapshot.

To seek to a time in the past and replay previously-acknowledged messages, you must configure message retention on the topic, or configure the subscription to retain acknowledged messages. For more information, see the following:

  * [Enable topic message retention](https://docs.cloud.google.com/pubsub/docs/create-topic#enable_message_retention)
  * [Configure message retention for a subscription](https://docs.cloud.google.com/pubsub/docs/subscription-message-retention)



### Eventual consistency of seek operations

Seek operations are strictly consistent in regard to the message delivery guarantee. This means that any message that is to become unacknowledged based on the seek condition is guaranteed to be eventually delivered after the seek operation succeeds. However, delivered messages don't instantly become consistent with the seek operation. So a message that was published before the seek timestamp or that is acknowledged in a snapshot might be delivered after the seek operation. In a sense, message delivery operates as an eventually consistent system with respect to the seek operation; it might take as long as a minute for the operation to take full effect.

### Use cases for seek operations

  * **Update subscriber code safely.** A concern with deploying new subscriber code is that the new executable may erroneously acknowledge messages, leading to message loss. Incorporating snapshots into your deployment process gives you a way to recover from bugs in new subscriber code.
  * **Recover from unexpected subscriber problems.** In cases where subscriber problems are not associated with a specific deployment event, you might not have a relevant snapshot. In this case, if you have enabled _acknowledged message retention_ for a subscription, seeking to a time in the past gives you a way to recover from the error.
  * **Save processing time and cost.** Perform a bulk acknowledgment on a large backlog of messages that are no longer relevant.
  * **Test subscriber code on known data.** When testing subscriber code for performance and consistency, it is useful to use the same data in every run. Snapshots enable consistent data with strong semantics. In addition, snapshots can be applied to any subscription on a given topic, including a newly created one.



## Create a snapshot

You can create a snapshot using the console, the Google APIs, or the Google Cloud CLI CLI.

### Console

To create a snapshot, follow these steps:

  1. In the Google Cloud console, go to the **Snapshots** page.

[Go to the snapshots page](https://console.cloud.google.com/cloudpubsub/snapshot)

  2. Click **Create snapshot**.

  3. For **Select a Pub/Sub subscription** , select a subscription.

  4. For **Snapshot ID** , enter a name for the snapshot.

For more information on how to name Pub/Sub resources, see [Guidelines to name a topic, subscription, schema, or snapshot](https://docs.cloud.google.com/pubsub/docs/pubsub-basics#resource_names).

  5. Click **Create** to create the snapshot.




You can also create a snapshot from the **Subscriptions** page. If you create a snapshot immediately after creating a subscription, you might get an error due to the propagation delay for the newly-created subscription.

### gcloud

To create a snapshot, use the following [`gcloud pubsub snapshots create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/snapshots/create) command:
    
    
    gcloud pubsub snapshots create \
        --project=PROJECT_ID \
        --subscription=SUBSCRIPTION_ID \
        SNAPSHOT_ID

Replace the following:

  * PROJECT_ID. Specifies the ID of the project.

  * SUBSCRIPTION_ID. Specifies the ID of the subscription.

  * SNAPSHOT_ID. Specifies the ID of the snapshot.




## Seek to a timestamp

Seeking to a time marks every message received by Pub/Sub before the time as acknowledged, and all messages received after the time as unacknowledged.

You can perform the following types of seek operations based on timestamps:

  * To purge all messages, you can seek to a time in the future.

  * To replay and reprocess previously acknowledged messages, seek to a time in the past.




The message publication time is generated by the Pub/Sub servers (see [`publishTime`](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#google.pubsub.v1.PubsubMessage.FIELDS.google.protobuf.Timestamp.google.pubsub.v1.PubsubMessage.publish_time) in the API reference). This approach is imprecise due to the following reasons:

  * Possible clock skew among Pub/Sub servers.

  * The fact that Pub/Sub has to work with the arrival time of the publish request rather than when an event occurred in the source system.




You can seek to a timestamp using the console, the Google APIs, or the Google Cloud CLI CLI. Before you seek to a timestamp on a subscription, ensure that message retention is enabled on the subscription.

### Console

To seek to a timestamp, follow these steps:

  1. In the Google Cloud console, go to the **Subscription** page.

[Go to Subscription](https://console.cloud.google.com/cloudpubsub/subscription)

  2. Click a subscription which has message retention enabled.

  3. In the subscription details page, click **Replay messages**.

  4. For **Seek** , click **To a previous time point**.

  5. Select an appropriate date and time and then click **Seek**.




### gcloud

To seek to a timestamp, use the following [`gcloud pubsub subscriptions seek`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/seek) command:
    
    
    gcloud pubsub subscriptions seek SUBSCRIPTION_ID \
        --time=TIME \

Replace the following:

  * TIME: the time to which you want to perform the seek operation.
  * SUBSCRIPTION_ID: the ID of the subscription.



For more information about supported time formats, see [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes).

## Seek to a snapshot

You can replay unacknowledged messages by using a snapshot to seek to any of the topic's subscriptions.

Unlike with seeking to a time, you don't need to perform any special subscription configuration to seek to a snapshot. You just need to create the snapshot ahead of time. For example, you might create a snapshot when deploying new subscriber code, in case you need to recover from unexpected or erroneous acknowledgments.

If the backlog in the subscription is too old and the resulting snapshot would expire in less than 1 hour, the seek operation fails.

You can seek to a snapshot using the console, the Google APIs, or the Google Cloud CLI CLI.

### Console

To seek to a snapshot, follow these steps:

  1. In the Google Cloud console, go to the **Subscription** page.

[Go to Subscription](https://console.cloud.google.com/cloudpubsub/subscription)

  2. Click a subscription.

  3. In the subscription details page, click **Replay messages**.

  4. For **Seek** , click **To a snapshot**.

  5. Select an appropriate snapshot and then click **Seek**.




### gcloud

To seek to a snapshot, use the following [`gcloud pubsub subscriptions seek`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/seek) command:
    
    
    gcloud pubsub subscriptions seek SUBSCRIPTION_ID \
        --snapshot=SNAPSHOT_ID

Replace the following:

  * SNAPSHOT_ID: the ID of a snapshot. The snapshot's topic must be the same as that of the subscription.
  * SUBSCRIPTION_ID: the ID of the subscription.



## Seek with filters

You can replay messages from subscriptions with filters. If you seek to a timestamp using a subscription with a filter, the Pub/Sub service only redelivers the messages that match the filter.

A snapshot of a subscription with a filter contains the following messages:

  * All messages that are newer than the snapshot, including messages that don't match the filter.
  * Unacknowledged messages that are older than the snapshot.

**Note:** The snapshot might contain messages that are older than the snapshot and don't match the filter.

If you seek to a snapshot using a subscription with a filter, the Pub/Sub service only redelivers the messages in the snapshot that match the filter of the subscription making the seek request.

For more information about filters, see [Filtering messages](https://docs.cloud.google.com/pubsub/docs/filtering).

## Seek with dead-letter topics

If you seek messages in a subscription with a dead-letter topic, Pub/Sub sets the delivery attempts to `0`. The messages that you receive from these subscriptions have a field that tallies the number of delivery attempts.

For more information about dead-letter topics, see [Forwarding to dead-letter topics](https://docs.cloud.google.com/pubsub/docs/dead-letter-topics).

## Seek with retry policies

If you seek messages in a subscription with a retry policy, Pub/Sub resets the delay between the following:

  1. The acknowledgment deadline expiring or the subscriber sending a negative acknowledgment.
  2. Pub/Sub resending the message.



For more information about retry policies, see [Using retry policies](https://docs.cloud.google.com/pubsub/docs/subscription-properties#retry_policies).

## Seek with exactly once delivery

If you seek messages in a subscription with exactly once delivery, Pub/Sub resends the previously acknowledged messages that are eligible for delivery. Any acknowledgments, for a delivery made before the seek operation, will fail. Seek operations are [eventually consistent](https://docs.cloud.google.com/pubsub/docs/replay-overview#seek_eventual_consistency).

For more information about retry policies, see [Exactly once delivery](https://docs.cloud.google.com/pubsub/docs/exactly-once-delivery).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
