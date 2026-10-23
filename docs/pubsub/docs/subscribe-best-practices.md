---
url: https://docs.cloud.google.com/pubsub/docs/subscribe-best-practices/
title: Best practices to subscribe to a Pub/Sub topic \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:39.875981+00:00
---

# Best practices to subscribe to a Pub/Sub topic  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/subscribe-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Best practices to subscribe to a Pub/Sub topic Stay organized with collections  Save and categorize content based on your preferences. 

In subscribing, a subscriber client receives messages from a Pub/Sub topic. Here are some best practices for subscribing to Pub/Sub. 

This document assumes that you are already familiar with the process of subscribing to a Pub/Sub topic and receiving messages in your subscriber client.

If you're new to Pub/Sub, see one of the Quickstart guides and learn how to run Pub/Sub using the [console](https://docs.cloud.google.com/pubsub/docs/publish-receive-messages-console), [Google Cloud CLI](https://docs.cloud.google.com/pubsub/docs/publish-receive-messages-gcloud), or the [client libraries](https://docs.cloud.google.com/pubsub/docs/publish-receive-messages-client-library).

## Choose the right subscription

Pub/Sub offers standard subscriptions such as _push_ and _pull_ subscriptions. In addition to the standard subscriptions, Pub/Sub also offers _export_ subscriptions that lets you store messages directly to a Google Cloud resource, without requiring Dataflow as an intermediary. For example, BigQuery subscriptions store messages in a BigQuery table.

Push subscriptions are recommended for the following scenarios:

  * You cannot include any code in your subscriber application that imports the client library as a dependency.

  * The subscriber client cannot make any outgoing requests.

  * You want to use the same instance to process messages from different topics and subscriptions where the subscriber client doesn't know the list of subscriptions.




For general cases, we recommend using the [high-level client library](https://docs.cloud.google.com/pubsub/docs/reference/libraries). If you're instead using unary pull, don't set `[returnImmediately](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions/pull#request-body)` to `true`. Setting it to `true` adversely impacts pull performance. The field `returnImmediately` is now deprecated.

  * To compare all the subscription types and choose the one that best fits your business needs, see the [Pub/Sub subscription comparison table](https://docs.cloud.google.com/pubsub/docs/subscriber#subscription_type_comparison).

  * To learn about the benefits of an export subscription, see [When to use an export subscription](https://docs.cloud.google.com/pubsub/docs/subscriber#export_subscription).




## Process messages before acknowledging them

By default, Pub/Sub discards a message from a subscription after the message is acknowledged. If you don't process a message before sending an acknowledgment and the processing fails, the service does not redeliver the message. The exception is when you have configured retaining acknowledged messages or topic retention and you perform a [seek operation](https://docs.cloud.google.com/pubsub/docs/replay-overview).

If you have high-latency subscribers, you might need to set custom values for [flow control](https://docs.cloud.google.com/pubsub/docs/flow-control) and [lease management](https://docs.cloud.google.com/pubsub/docs/lease-management).

## Preserve message IDs

To make troubleshooting easier, publishers and subscribers should preserve the message IDs of published messages. You can either store the ID of each published message or enable logging of message IDs as needed. Keeping the message IDs makes it easier to troubleshoot duplicate messages, redeliveries, data loss, and other common issues. For more information, see [Dealing with duplicates](https://docs.cloud.google.com/pubsub/docs/pull-troubleshooting#dealing_with_duplicates).

## Configure subscriber flow control for transient traffic spikes

Flow control on the subscriber side lets you prevent subscribers from being overloaded by traffic spikes. It can allow time for autoscaling mechanisms to respond to an increased load or it can spread the processing of the load over a longer period of time. The former method saves latency, while the latter saves costs.

To configure [flow control](https://docs.cloud.google.com/pubsub/docs/flow-control), you must set appropriate values for `maximum outstanding messages` and `total outstanding message bytes`. The default values for these flow control variables and the names of the variables might differ across client libraries.

  * **Maximum outstanding messages** defines the maximum number of messages delivered to the client for which Pub/Sub has not received acknowledgments or negative acknowledgments.

  * **Total outstanding message bytes** defines the maximum total size of messages delivered to the client for which Pub/Sub has not received acknowledgments or negative acknowledgments.




If the limit for one of these options is crossed, the subscriber client does not pull more messages. This behavior continues until the messages that are already pulled get acknowledged or negatively acknowledged. In this way, you can trade off throughput with the cost associated with running more subscribers.

## Handle duplicate deliveries

By default, Pub/Sub provides at-least-once delivery of messages to subscribers. That means messages can be delivered multiple times, even if they were acknowledged. The following sections discuss how to address common redelivery scenarios.

### Consistent redelivery of many messages

If you are experiencing cases where many messages are always getting redelivered, then your subscribers are overloaded or they are not acknowledging the messages before the deadline expires.

If you are using a pull subscription, you might need to set custom values to [flow control](https://docs.cloud.google.com/pubsub/docs/flow-control) values or increase the lease extension periods using [lease management](https://docs.cloud.google.com/pubsub/docs/lease-management).

If you are using push subscriptions, you might need to increase the acknowledgement deadline setting. You can also follow best practices regarding how to [maintain a healthy subscription](https://docs.cloud.google.com/pubsub/docs/monitoring#maintain_a_healthy_subscription).

### Occasional redelivery of messages

When you see messages get redelivered before the acknowledgement deadline has passed or after the messages were acknowledged within a few seconds, Pub/Sub is behaving as expected. You shouldn't see these redelivery spikes frequently, but when redeliveries do occur, they are likely to occur on several messages simultaneously. Your system must be built to tolerate these occasional duplicates.

### Repeated redelivery of a few messages

When you see a small number of messages get delivered several times, first confirm that you are acknowledging them. If you are not, figure out why your subscriber is not handling the messages properly. You might want to configure a [dead letter topic](https://docs.cloud.google.com/pubsub/docs/handling-failures#dead_letter_topic) to prevent further redelivery. If you are acknowledging the message, Pub/Sub might still be operating as expected. While very rare, it is still possible for a small number of messages to get delivered multiple times if there are internal network or hardware disruptions. The service attempts to self-heal in these cases, but it can take several minutes for the remedies to activate.

Your system must be tolerant to redeliveries. You can reduce their likelihood by ensuring you process and acknowledge messages as quickly as possible.

If your application can't tolerate any duplicates, you can enable [exactly-once delivery](https://docs.cloud.google.com/pubsub/docs/exactly-once-delivery). Remember that this feature is only available for pull subscriptions and that it also results in higher publish-to-subscribe latency. Evaluate whether the trade-off of higher latency is acceptable for your use case before enabling this feature.

## Best practices for ordered messaging in subscribing

If you use message ordering, ensure the following:

  * **Choose either StreamingPull or Pull subscriptions.** For a push subscription, Pub/Sub supports only one outstanding message for each ordering key at a time. Sending parallel push requests in such a scenario would be similar to sending multiple batches of messages for the same ordering key to pull subscribers simultaneously. Therefore, push subscriptions are not recommended for topics where multiple messages are frequently published with the same ordering key or where latency is extremely important.

  * **Enable message ordering in the subscription**. On the publisher side, if you send messages with an ordering key and in the same region, you can configure the subscribers to receive those messages in order. On the subscriber side, enable the message ordering property for only those subscriptions for which you want to receive ordered messages. Depending on the property status, each subscription attached to the topic can determine if they need ordered delivery without impacting each other.

  * **Acknowledge messages in order**. When using ordered delivery, acknowledgments for later messages are not processed until acknowledgments for earlier messages are processed per ordering key. For example, if you have messages 1, 2, and 3 with the same ordering key and you receive them all and only acknowledge message 3, the service does not consider message 3 as acknowledged until messages 1 and 2 are also acknowledged. If the acknowledgments for messages 1 and 2 are never received, then messages 1, 2, and 3 are all redelivered.




## Summary of best practices

The following table summarizes the best practices recommended in this document:

Topic | Task  
---|---  
[Choose a subscription type](https://docs.cloud.google.com/pubsub/docs/subscriber) | Choose the right subscription type for your business needs. If supported by your subscription, also use the high-level client library.  
[Replay an acknowledged message](https://docs.cloud.google.com/pubsub/docs/replay-overview) | Process a message before you acknowledge it. Or, configure for a seek operation so that you don't lose acknowledged messages.   
[Flow control](https://docs.cloud.google.com/pubsub/docs/flow-control) | Configure flow control in your subscriber settings to ensure that subscribers don't get overloaded until autoscaling kicks in or time passes.  
[ Handle duplicate deliveries and preserve message IDs](https://docs.cloud.google.com/pubsub/docs/pull-troubleshooting#dealing_with_duplicates) | Preserve or enable logging of the received `messageId` to simplify troubleshooting duplicates, redeliveries, and missing messages.  
[Ordering messages](https://docs.cloud.google.com/pubsub/docs/ordering) | When using ordered messaging, choose StreamingPull or Pull, enable message ordering in the subscription, and acknowledge messages in order.  
  
## What's next

  * [Best practices to publish to a Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/publish-best-practices).

  * [Best practices for using Pub/Sub metrics as a scaling signal](https://docs.cloud.google.com/pubsub/docs/metrics-autoscaling-best-practices).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
