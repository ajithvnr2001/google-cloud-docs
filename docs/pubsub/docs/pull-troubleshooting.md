---
url: https://docs.cloud.google.com/pubsub/docs/pull-troubleshooting/
title: Troubleshooting a pull subscription \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:14.705347+00:00
---

# Troubleshooting a pull subscription  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/pull-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Troubleshooting a pull subscription Stay organized with collections  Save and categorize content based on your preferences. 

This document provides some common troubleshooting tips for Pub/Sub pull subscriptions. Read more about pull subscriptions in the [Pull subscriber guide](https://docs.cloud.google.com/pubsub/docs/pull).

To effectively monitor your Pub/Sub subscription, it is recommended to first look at the [delivery latency health score](https://docs.cloud.google.com/pubsub/docs/monitoring#delivery_latency_health) ([subscription/delivery_latency_health_score](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/subscription/delivery_latency_health_score)) to check which factors can contribute to an unexpected or increased latency.

## Oldest unacked message age keeps increasing

The [`oldest_unacked_message_age`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/subscription/oldest_unacked_message_age) is a critical metric for monitoring the health of Pub/Sub subscriptions. It measures the age, in seconds, of the oldest message in a subscription's backlog that has not yet been acknowledged (acked) by a subscriber. This metric offers valuable insights into potential processing delays or bottlenecks.

[Monitoring message backlog](https://docs.cloud.google.com/pubsub/docs/monitoring#monitoring_the_backlog) ensures timely and efficient message processing. By tracking the oldest unacked message age, you can proactively identify situations where consumers are falling behind. This practice allows for early intervention to address potential issues related to degraded performance.

Some of the [common backlog issues](https://docs.cloud.google.com/pubsub/docs/monitoring#common_backlog_issues) that you can investigate include:

### Client configuration issues

When both the `oldest_unacked_message_age` and `num_undelivered_messages` metrics increase simultaneously, it could mean that the subscribers are not keeping up with the message volume. In this situation, focus your investigation on the subscriber components:

  * Client health: Analyze resource utilization on machines hosting subscriber clients, like CPU, memory, and network bandwidth. Look for pressure points that might impede processing efficiency.

  * Client code: Review recent code changes and examine error logs. Bugs or inefficiencies in the subscriber code can significantly impact message processing rates. Note that there could be issues in specific messages. For example, multiple messages might need to access the same row in a database simultaneously. This behavior can lead to contention and high latency.

  * Quota limitations: Verify that you haven't exceeded any Pub/Sub quotas or limitations imposed by your hosting service. If the subscribers are hosted in Google Cloud, review [Compute Engine](https://docs.cloud.google.com/compute/quotas-limits) or [GKE](https://docs.cloud.google.com/kubernetes-engine/quotas) resource quotas to prevent potential bottlenecks.




### Subscriber negatively acknowledged the messages

When a subscriber negatively acknowledges (nacks) a message, it signals to Pub/Sub that the message couldn't be processed successfully. Pub/Sub then attempts to redeliver the same message. Repeated nacks for a message leads to duplicates and potentially a high delay in message delivery.

Note that nacking a message won't guarantee that the next pull fetches a different message. Pub/Sub's redelivery policy might continue to redeliver nacked messages before new ones. Therefore, don't rely on nacks as a method of filtering or skipping specific messages. Instead, set a [retry policy](https://docs.cloud.google.com/pubsub/docs/handling-failures#subscription_retry_policy), preferably an [exponential backoff](https://docs.cloud.google.com/pubsub/docs/handling-failures#exponential_backoff), as a way to back off on individual messages that are likely to be processable later but need a little longer time before redelivery.

If you need to intentionally skip certain messages, the recommended approach is to ack them, even if you won't process them. This removes them from the subscription, avoids unnecessary redeliveries, and reduces resource consumption. Leaving messages unacknowledged, whether intentionally or not, creates backlog issues and duplicate deliveries.

## High delivery latency

Delivery latency in Pub/Sub is the time it takes for a message from a publisher to reach a subscriber. Some possible causes of a high delivery latency are described in the next sections.

### Not enough subscribers

For clients using StreamingPull, to achieve consistently low latency, maintain multiple open StreamingPull connections to your subscription. Without active subscriber connections, Pub/Sub cannot deliver messages promptly. A single stream could be a single point of failure, increasing the risk of delays. The [`subscription/open_streaming_pulls`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/subscription/open_streaming_pulls) metric provides visibility into the number of active streaming connections. Use this to make sure you consistently have enough streams to handle incoming messages.

For clients using unary pull, to achieve consistently low latency, maintain multiple outstanding pull requests to your subscription. Infrequent requests could potentially accumulate messages in the backlog and increase latency. This approach helps minimize gaps in connectivity and improve delivery latency.

The high-level client library is recommended for cases where you require high throughput and low latency with minimal operational overhead and processing cost. By default, the high-level client library uses the StreamingPull API, since it tends to be a better choice for minimizing latency. The high-level client libraries contain prebuilt functions and classes that handle the underlying API calls for authentication, throughput and latency optimization, message formatting, and other features.

### Client configuration issues

See [Client configuration issues](https://docs.cloud.google.com/pubsub/docs/pull-troubleshooting#client_configuration_issues).

### High backlog

Note that a message backlog of [unacked messages](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/subscription/num_undelivered_messages) in a Pub/Sub subscription inherently increases end-to-end latency because messages are not getting processed immediately by subscribers.

### Ordering keys and exactly-once delivery

Ordering keys and exactly-once delivery are valuable features, however they require additional coordination within Pub/Sub to ensure correct delivery. This coordination can reduce availability and increase latency. While the difference is minimal in the steady state, any necessary coordination steps could result in temporary increases in latency or an increased error rate. If ordering is enabled, messages with an ordering key cannot be delivered until earlier ones with the same ordering key are ACKed.

Consider whether message ordering or exactly-once delivery are absolutely essential for your application. If low latency is your top priority, minimizing the use of these features could help reduce message processing delays.

### Increase in message size

A sudden increase in the message size could potentially increase the transfer time between Pub/Sub and your client, and slow down the processing time of the messages in the client side.

If you observe an increase in delivery latency, you can check message sizes using the [`topic/message_sizes`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/topic/message_sizes) metric, grouping by `topic_id`. Correlate any spikes in message size with observed performance issues.

## Missing messages

If you suspect messages are not being successfully delivered to your subscriber, one of the following reasons might be the contributing factor.

### Message distribution in Pub/Sub subscriptions with multiple consumers

In Pub/Sub, messages might be distributed unevenly across consumers on the same subscription. Pub/Sub load balances messages across all active clients, but the primary goal is to maximize overall message processing throughput and minimize backlog, rather than to ensure a perfectly even distribution. The system dynamically directs more messages towards consumers that demonstrate higher capacity – those that acknowledge messages quickly and are not constrained by their flow control settings. Consumers processing messages at different speeds or operating under different conditions (e.g., resource availability, network latency) will likely handle different volumes of messages. Typically, faster and more responsive consumers will receive and process a larger share of the message load.

This distribution method across multiple consumers means that the order in which messages are received and processed can vary. Consequently, unless [message ordering](https://docs.cloud.google.com/pubsub/docs/ordering) is enabled for the subscription and publishers include ordering keys, messages are not guaranteed to be processed by consumers in the order they were published.

Note that messages could be outstanding to clients already, and a backlog of unacknowledged messages doesn't necessarily mean you'll receive those messages on your next pull request. Be aware that a consumer may be someone using pull in the Google Cloud console or Google Cloud CLI, or running a custom subscriber locally to check messages.

For unary Pull clients, you might observe some pull requests returning zero messages. As discussed in the not enough subscribers section, it is recommended to maintain multiple outstanding pull requests, as some requests could return fewer than the maximum number of messages configured, or even zero messages, even if a backlog exists. This is because other consumers might be holding leases on the available messages.

If a consumer fails to acknowledge a message within the acknowledgment deadline, or if it negatively acknowledges (NACKs) the message, Pub/Sub will attempt to redeliver it. This redelivery attempt can be made to any active consumer on the subscription, not necessarily the one that received it initially. Therefore, a particular message ID might be delivered to, and its processing attempted by, multiple different consumers connected to the subscription over its lifetime until one of them successfully acknowledges it.

If you suspect unexpected message distribution behaviors, investigate whether there are multiple consumers concurrently attached to the subscription and inspect their individual performance metrics and configurations.

### Filter on the subscription

Check if the subscription has a [filter](https://docs.cloud.google.com/pubsub/docs/subscription-message-filter) attached to it. If so, you only receive the messages that match the filter. The Pub/Sub service automatically acknowledges the messages that don't match the filter. Consider [how filters affect backlog metrics](https://docs.cloud.google.com/pubsub/docs/subscription-message-filter#filters-metrics).

### Using the option `returnImmediately`

If your client is using unary Pull, check if the [`returnImmediately`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions/pull#request-body) field is set to true. This is a deprecated field that tells the Pub/Sub service to respond to the pull request immediately even if it returns with no messages. This can result in pull requests returning with 0 messages even when there is a backlog.

### Client configuration issues

If you are using the Java client library and are initializing your subscriber with a custom gRPC channel using the [`setChannelProvider()`](https://github.com/googleapis/java-pubsub/blob/4119cc03895873f94ddef10850753fb59384a8fc/google-cloud-pubsub/src/main/java/com/google/cloud/pubsub/v1/Subscriber.java#L546-L557) method, you should ensure that the `maxInboundMessageSize` setting is at least 20MB (matching the [library's default value](https://github.com/googleapis/java-pubsub/blob/9a1c17e50e5fc9a807532d289a7f6e8b5d412f59/google-cloud-pubsub/src/main/java/com/google/cloud/pubsub/v1/Subscriber.java#L97)) when building your `TransportChannelProvider`. When this value is less than 10MB, messages that are larger than `maxInboundMessageSize` won't be received properly. Some common methods for configuring this setting are [`InstantiatingGrpcChannelProvider.Builder.setMaxInboundMessageSize()`](https://docs.cloud.google.com/java/docs/reference/gax/2.52.0/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder#com_google_api_gax_grpc_InstantiatingGrpcChannelProvider_Builder_setMaxInboundMessageSize_java_lang_Integer_) and [`ManagedChannelBuilder.maxInboundMessageSize()`](https://grpc.github.io/grpc-java/javadoc/io/grpc/ManagedChannelBuilder.html#maxInboundMessageSize\(int\)).

## Dealing with duplicates

A subscriber might receive duplicate messages in the following cases:

  * Redelivery. A client negatively acknowledged a message or the acknowledgment deadline expired. This behavior is expected.

  * Duplicate delivery. A message is re-sent after a successful acknowledgment or before the acknowledgment deadline expires. Subscriptions with [exactly-once delivery](https://docs.cloud.google.com/pubsub/docs/exactly-once-delivery) enabled don't receive duplicate deliveries.

  * Duplicate messages from the publisher. The publisher sends a message twice due to the publisher's application logic. The Pub/Sub service treats these as distinct Pub/Sub messages and assigns them unique message IDs.




If the message IDs are the same, it means that Pub/Sub re-sent or redelivered the message. If the message IDs are different, it means the duplication occurred upstream at the publisher.

### Expired acknowledgment deadlines

Message duplication in Pub/Sub often occurs when subscribers can't ack messages within the ack deadline. This causes the messages to be redelivered, creating the impression of duplicates. You can measure the rate at which subscribers miss the ack deadline using the [`subscription/expired_ack_deadlines_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/subscription/expired_ack_deadlines_count) metric. Learn more about how to [Monitor acknowledgment deadline expiration](https://docs.cloud.google.com/pubsub/docs/monitoring#monitoring_exp).

To reduce the duplication rate, extend message deadlines.

  * Client libraries handle deadline extension automatically, but there are default limits on the maximum extension deadline that you can configure.
  * If you are building your own client library, use the [`modifyAckDeadline`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions/modifyAckDeadline) method to extend the acknowledgment deadline.



If messages are pulled in the subscriber faster than they can be processed and acked, some messages might expire and require deadline extensions. However, if the subscriber remains overwhelmed, repeated deadline extensions eventually fail. In the worst-case scenario, this can lead to a subscriber overflowing with duplicates, exacerbating the backlog. Expiring duplicates then generate new duplicates.

To avoid overwhelming the subscriber, reduce the number of messages that the subscriber pulls at a time. This way the subscriber has fewer messages to process within the deadline. Fewer messages expire and fewer messages are redelivered.

To reduce the number of messages that the subscriber pulls at a time, you need to reduce the maximum number of outstanding messages setting in your subscriber's [flow control](https://docs.cloud.google.com/pubsub/docs/flow-control) configuration. There is no one-size-fits-all value, so you must adjust the maximum outstanding messages limit based on your throughput and subscriber capacity. Consider that each application processes messages differently and takes a different amount of time to ack a message.

### Forcing retries

To force Pub/Sub to retry a message, send a `nack` request. If you are not using the high-level [client libraries](https://docs.cloud.google.com/pubsub/docs/reference/libraries), send a [`modifyAckDeadline`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions/modifyAckDeadline) request with an `ackDeadlineSeconds` set to 0.

### Ordering keys

When Pub/Sub redelivers a message with an [ordering key](https://docs.cloud.google.com/pubsub/docs/ordering), it also redelivers all subsequent messages with the same ordering key, even if they were previously acknowledged. This is done to preserve the order of the sequence. However, there's no strict guarantee that dependent messages are only sent after the successful acking of prior messages in the sequence.

### Subscriber is nacking the messages

See [subscriber is nacking the messages](https://docs.cloud.google.com/pubsub/docs/pull-troubleshooting#subscriber_negatively_acknowledged_the_messages).

### Seek operations

When you perform a [seek operation](https://docs.cloud.google.com/pubsub/docs/replay-overview) to a timestamp or a snapshot, Pub/Sub redelivers messages that were published after the timestamp or included in the snapshot. This redelivery is expected behavior and occurs even if exactly-once delivery is enabled on the subscription. For more information, see [Seek with exactly-once delivery](https://docs.cloud.google.com/pubsub/docs/replay-overview#seek_exactly_once).

### Downstream deduplication

Subscribers and other downstream systems might deduplicate messages. For example, Dataflow supports [exactly-once delivery](https://docs.cloud.google.com/dataflow/docs/concepts/exactly-once). If you see duplicate messages appear downstream unexpectedly, the cause might be in the subscriber rather than Pub/Sub.

## Troubleshooting a StreamingPull subscription

### Relationship between the request latency metric and end-to-end delivery latency

For StreamingPull, the metric [serviceruntime.googleapis.com/api/request_latencies](https://docs.cloud.google.com/apis/docs/monitoring#using) represents the time for which the stream is open. The metric is not helpful for determining end-to-end delivery latency.

Instead of using the request latency metric, use the [delivery latency health score](https://docs.cloud.google.com/pubsub/docs/monitoring#delivery_latency_health) to check which factors are contributing to an increased end-to-end delivery latency.

### StreamingPull Connections Close with a non-OK Status

StreamingPull streams always close with a non-OK status. Unlike an error status for unary RPCs, this status for StreamingPull is just an indication that the stream is disconnected. The requests are not failing. Therefore, while the StreamingPull API might have a surprising 100% error rate, this behavior is by design.

Since StreamingPull streams always close with an error, it isn't helpful to examine stream termination metrics while diagnosing errors. Rather, focus on the StreamingPull response metric [`subscription/streaming_pull_response_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/subscription/streaming_pull_response_count), grouped by `response_code` or `response_class`.

Look for these errors:

  * **Failed precondition** errors can occur if there are messages in the subscription backlog that are encrypted with a disabled Cloud KMS key. To resume pulling, [restore access to the key](https://docs.cloud.google.com/pubsub/docs/encryption#disabling_and_re-enabling_keys).

  * **Unavailable errors** can occur when Pub/Sub is unable to process a request. This is most likely a transient condition and the client library retries the requests. No action on your part is necessary if you are using a client library.

  * **Not found errors** can occur when the subscription is deleted or if it never existed in the first place. The latter case happens if you provided an invalid subscription path.




## Additional references

  * [Troubleshoot pull subscriptions with gcpdiag](https://docs.cloud.google.com/pubsub/docs/gcpdiag-pull-troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
