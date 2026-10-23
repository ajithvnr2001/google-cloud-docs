---
url: https://docs.cloud.google.com/pubsub/docs/subscription-properties/
title: Subscription properties \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:36.056707+00:00
---

# Subscription properties  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/subscription-properties/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Subscription properties Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the properties that are common to all Pub/Sub subscription types. You can set these properties when you create or update a subscription.

## Message retention duration

The **Message retention duration** option specifies how long Pub/Sub retains messages after publication. After the message retention duration passes, Pub/Sub might discard the message independent of the acknowledgment state of the message. To retain _acknowledged_ messages for the message retention duration, see [Replaying and discarding messages](https://docs.cloud.google.com/pubsub/docs/replay-overview).

The following are the values for the **Message retention duration** option:

  * Default value = 7 days
  * Minimum value = 10 minutes
  * Maximum value = 31 days

**Note:** If you retain unacknowledged messages in a subscription for more than 24 hours, you incur additional charges. For more information, see [Storage costs](https://cloud.google.com/pubsub/pricing#storage_costs).

Unacknowledged messages can result from idle subscriptions, backup needs, or slow processing. If you are able to process the messages within 24 hours, the additional charges are not incurred. You can avoid new charges by managing these scenarios as follows:

  * **Idle subscriptions**. [Delete idle subscriptions](https://docs.cloud.google.com/pubsub/docs/delete-subscriptions) to avoid incurring subscription message retention charges.

  * **Backup storage**. If you are using subscription retention as backup storage, you can switch to another storage option such as [topic message retention](https://docs.cloud.google.com/pubsub/docs/topic-properties#message_retention_duration) or retaining acknowledged messages. Topic message retention stores messages just once at the topic level and they remain available for all the subscriptions to consume when needed.

  * **Processing delays**. Add more subscribers (if possible) to process the messages within a day.




### Retain acknowledged messages

If you specify **Message retention duration** , you can also specify if you want to retain acknowledged messages.

The **Retain acknowledged messages** option lets you retain acknowledged messages for the specified message retention duration. This option increases message storage fees. For more information, see [storage costs](https://cloud.google.com/pubsub/pricing).

## Expiration period

The **Expiration period** option lets you extend the expiration period of your subscription.

Subscriptions without any subscriber activity or changes made to the subscription properties expire. If Pub/Sub detects subscriber activity or if you update any of the subscription properties, the subscription deletion clock restarts. Examples of subscriber activities include open connections, active pulls, or successful pushes.

If you specify the expiration period, the value must be at least as long as the message retention duration specified in the Message retention duration option.

The following are the values for the **Expiration period** option:

  * Default value = 31 days
  * Minimum value = 1 day



To prevent a subscription from expiring, set the expiration period to `never expire`.

## Acknowledgment deadline

The **Acknowledgment deadline** option specifies the initial deadline after which an unacknowledged message is sent again. You can extend the acknowledgment deadline on a per-message basis by sending subsequent [ModifyAckDeadline](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions/modifyAckDeadline) requests.

The following are the values for the **Acknowledgment deadline** option:

  * Default value = 10 seconds
  * Minimum value = 10 seconds
  * Maximum value = 600 seconds



In some cases, Pub/Sub client libraries can control the rate of delivery and dynamically modify the acknowledgment deadline. In doing so, the message might get redelivered before the acknowledgment deadline that you set. To override this behavior, use `minDurationPerAckExtension` and `maxDurationPerAckExtension`. For more information on using these values, see [Exactly-once delivery support in client libraries](https://docs.cloud.google.com/pubsub/docs/exactly-once-delivery#exactly-once_delivery_support_in_client_libraries).

## Single Message Transforms (SMTs)

SMTs allow for lightweight modifications to message attributes and data directly within Pub/Sub. This feature enables data cleaning, filtering, or format conversion before the messages are delivered to a subscriber client.

For more information, see [SMTs Overview](https://docs.cloud.google.com/pubsub/docs/smts/smts-overview) and [Create a subscription with SMTs](https://docs.cloud.google.com/pubsub/docs/smts/create-subscription-smt).

## Subscription filter

Use the **Subscription filter** option to specify a string with a [filtering expression](https://docs.cloud.google.com/pubsub/docs/filtering#filtering_syntax). If a subscription has a filter, the subscription only delivers the messages that match the filter. The Pub/Sub service automatically acknowledges the messages that don't match the filter.

  * You can filter messages by their attributes, but not by the data in the message.

  * If unspecified, the subscription doesn't filter messages and subscribers receive all messages.

  * Filters cannot be changed or removed after you apply them.




When you receive messages from a subscription with a filter, you don't incur [egress fees](https://cloud.google.com/pubsub/pricing#egress_costs) for the messages that Pub/Sub automatically acknowledges. You incur [message delivery](https://cloud.google.com/pubsub/pricing##filtered_message_costs) fees and [seek-related storage](https://cloud.google.com/pubsub/pricing#storage_costs) fees for these messages.

For more information, see [Filter messages from a subscription](https://docs.cloud.google.com/pubsub/docs/subscription-message-filter).

## Message ordering

By default, Pub/Sub might not deliver messages in the order they are published. If **Message ordering** is enabled for a subscription, then all messages sent in the same region, with the same [ordering key](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage#FIELDS.ordering_key), are received in the order they are published.

For the messages to be received in order, the publisher must set the ordering key. Messages without an ordering key might not be received in order.

When using ordered delivery, acknowledgments for later messages are not processed until acknowledgments for earlier messages are processed. For more information, see [Order messages](https://docs.cloud.google.com/pubsub/docs/ordering).

## Dead letter topic

When a message can't be delivered after a set number of delivery attempts, or a subscriber can't acknowledge the message, Pub/Sub can republish the message to a configured dead-letter topic.

If you set a dead-letter topic, you can also specify the maximum number of delivery attempts. The default value is 5 delivery attempts. You can set the maximum number of attempts to any number between 5 and 100, inclusive.

If the dead-letter topic is in a different project than the subscription, you must also specify the project ID with the dead-letter topic.

For more information, see [Dead-letter topics](https://docs.cloud.google.com/pubsub/docs/dead-letter-topics).

## Retry policy

If the acknowledgment deadline expires or a subscriber responds with a negative acknowledgment, Pub/Sub can send the message again. This redelivery attempt is known as the subscription **Retry policy**.

By default, the retry policy for a subscription is set to use **Retry immediately**. With this option, Pub/Sub resends the message when the acknowledgment deadline expires or a subscriber responds with a negative acknowledgment.

You can also set the value to **Retry after exponential backoff delay**. In this case, you must specify the maximum and minimum backoff values.

Here are some guidelines to set the values for maximum and minimum backoff values:

  * If you set the maximum value for the backoff duration, the default value for the minimum backoff duration is 10 seconds.

  * If you set the minimum value for the backoff duration, the default value for the maximum backoff duration is 600 seconds.

  * The longest backoff duration that you can specify is 600 seconds.




### Retry policy and batched messages

If messages are in a batch, Pub/Sub starts the exponential backoff when one of the following occurs:

  * The subscriber sends a negative acknowledgment for every message in the batch.

  * The acknowledgment deadline expires.




### Retry policy and push subscription

If you receive messages from a push subscription, Pub/Sub might redeliver messages after the [push backoff](https://docs.cloud.google.com/pubsub/docs/push#push_backoff) instead of the exponential backoff duration. When the push backoff is longer than the exponential backoff duration, Pub/Sub redelivers unacknowledged messages after the push backoff.

**Note:** When you modify either the message retention duration or subscription expiration policy, the expiration period must be set to a value greater than the message retention duration. The default message retention duration is 7 days and the default expiration period is 31 days.

## What's next

  * [Subscription overview](https://docs.cloud.google.com/pubsub/docs/subscription-overview)
  * [Choose a subscription type](https://docs.cloud.google.com/pubsub/docs/subscriber)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
