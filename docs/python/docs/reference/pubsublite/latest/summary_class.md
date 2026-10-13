---
url: https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/summary_class/
title: Package Classes (1.13.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:20:00.095378+00:00
---

# Package Classes (1.13.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/summary_class/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Classes (1.13.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.13.0 (latest) ](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/summary_class/)
  * [ 1.12.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.12.0/summary_class/)
  * [ 1.11.1 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.11.1/summary_class/)
  * [ 1.10.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.10.0/summary_class/)
  * [ 1.9.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.9.0/summary_class/)
  * [ 1.8.3 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.8.3/summary_class/)
  * [ 1.7.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.7.0/summary_class/)
  * [ 1.6.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.6.0/summary_class/)
  * [ 1.5.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.5.0/summary_class/)
  * [ 1.4.3 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.4.3/summary_class/)
  * [ 1.3.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.3.0/summary_class/)
  * [ 1.2.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.2.0/summary_class/)
  * [ 1.1.4 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.1.4/summary_class/)
  * [ 1.0.2 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.0.2/summary_class/)
  * [ 0.6.1 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/0.6.1/summary_class/)
  * [ 0.5.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/0.5.0/summary_class/)
  * [ 0.4.1 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/0.4.1/summary_class/)
  * [ 0.3.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/0.3.0/summary_class/)
  * [ 0.2.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/0.2.0/summary_class/)
  * [ 0.1.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/0.1.0/summary_class/)



Summary of entries of Classes for pubsublite.

## Classes 

### [AdminClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient)

An admin client for Pub/Sub Lite. Only operates on a single region.

### [AsyncPublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.AsyncPublisherClient)

An AsyncPublisherClient publishes messages similar to Google Pub/Sub, but must be used in an async context. Any publish failures are unlikely to succeed if retried.

Must be used in an `async with` block or have **aenter**() awaited before use.

### [PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient)

A PublisherClient publishes messages similar to Google Pub/Sub. Any publish failures are unlikely to succeed if retried.

Must be used in a `with` block or have **enter**() called before use.

### [AsyncSubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.AsyncSubscriberClient)

An AsyncSubscriberClient reads messages similar to Google Pub/Sub, but must be used in an async context. Any subscribe failures are unlikely to succeed if retried.

Must be used in an `async with` block or have **aenter**() awaited before use.

### [SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient)

A SubscriberClient reads messages similar to Google Pub/Sub. Any subscribe failures are unlikely to succeed if retried.

Must be used in a `with` block or have **enter**() called before use.

### [BacklogLocation](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.BacklogLocation)

A location with respect to the message backlog. BEGINNING refers to the location of the oldest retained message. END refers to the location past all currently published messages, skipping the entire message backlog.

### [CloudRegion](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudRegion)

API documentation for `pubsublite.types.CloudRegion` class.

### [CloudZone](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudZone)

API documentation for `pubsublite.types.CloudZone` class.

### [EventTime](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.EventTime)

A user-defined event timestamp of a message.

### [FlowControlSettings](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.FlowControlSettings)

API documentation for `pubsublite.types.FlowControlSettings` class.

### [LocationPath](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.LocationPath)

API documentation for `pubsublite.types.LocationPath` class.

### [MessageMetadata](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.MessageMetadata)

Information about a message in Pub/Sub Lite.

### [Partition](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.Partition)

API documentation for `pubsublite.types.Partition` class.

### [PublishTime](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.PublishTime)

The publish timestamp of a message.

### [ReservationPath](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.ReservationPath)

API documentation for `pubsublite.types.ReservationPath` class.

### [SubscriptionPath](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.SubscriptionPath)

API documentation for `pubsublite.types.SubscriptionPath` class.

### [TopicPath](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.TopicPath)

API documentation for `pubsublite.types.TopicPath` class.

### [Cursor](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite_v1.Cursor)

A cursor that describes the position of a message within a topic partition.

### [Subscription](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite_v1.Subscription)

Metadata about a subscription resource.

### [DeliveryConfig](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite_v1.Subscription.DeliveryConfig)

The settings for a subscription's message delivery.

### [DeliveryRequirement](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite_v1.Subscription.DeliveryConfig.DeliveryRequirement)

When this subscription should send messages to subscribers relative to messages persistence in storage. For details, see `Creating Lite subscriptions <https://cloud.google.com/pubsub/lite/docs/subscriptions#creating_lite_subscriptions>`__.

### [Topic](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite_v1.Topic)

Metadata about a topic resource.

### [PartitionConfig](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite_v1.Topic.PartitionConfig)

The settings for a topic's partitions.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Capacity](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite_v1.Topic.PartitionConfig.Capacity)

The throughput capacity configuration for each partition.

### [ReservationConfig](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite_v1.Topic.ReservationConfig)

The settings for this topic's Reservation usage.

### [RetentionConfig](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite_v1.Topic.RetentionConfig)

The settings for a topic's message retention.

## Modules 

### [admin_client](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client)

API documentation for `pubsublite.admin_client` module.

### [publisher_client](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client)

API documentation for `pubsublite.cloudpubsub.publisher_client` module.

### [subscriber_client](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client)

API documentation for `pubsublite.cloudpubsub.subscriber_client` module.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
