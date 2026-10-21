---
url: https://docs.cloud.google.com/pubsub/docs/bigtable-subscriptions/
title: Bigtable subscriptions \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:46:03.317716+00:00
---

# Bigtable subscriptions  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/bigtable-subscriptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Bigtable subscriptions Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Bigtable subscriptions let you write Pub/Sub messages to a [Bigtable](https://docs.cloud.google.com/bigtable/docs/overview) table. This document provides an overview of Bigtable subscriptions, including the subscription workflow, delivery semantics, and error handling.

To create a Bigtable subscription, see [Create a Bigtable subscription](https://docs.cloud.google.com/pubsub/docs/create-bigtable-subscription).

## Overview

A Bigtable subscription is a type of export subscription that writes messages to an existing Bigtable table as they are received. By using an export subscription, you don't need to configure a separate subscriber client.

Consider using a Bigtable subscription if you want to write messages to Bigtable, and the messages don't need additional processing, or the processing can be performed by a [Single Message Transform](https://docs.cloud.google.com/pubsub/docs/smts/smts-overview) (SMT).

If you need to perform more complex transformations before writing messages to Bigtable, we recommend using a Dataflow pipeline with a pull subscription. For more information, see [Read from Pub/Sub to Dataflow](https://docs.cloud.google.com/dataflow/docs/concepts/streaming-with-cloud-pubsub).

For more information about choosing a Pub/Sub subscription type, see [Choose a subscription type](https://docs.cloud.google.com/pubsub/docs/subscriber).

## Bigtable subscription workflow

The following image shows the workflow between a Bigtable subscription and Bigtable.

![A Bigtable subscription writes to a Bigtable table.](https://docs.cloud.google.com/static/pubsub/images/bigtable-subscription.png)

The workflow consists of the following steps:

  1. A publisher sends a message to a Pub/Sub topic.

  2. Pub/Sub forwards the message to the Bigtable subscription.

  3. The subscription sends a write request to Bigtable. In the write request, the subscription specifies an app profile that uses [single-cluster routing](https://docs.cloud.google.com/bigtable/docs/routing#single-cluster).

  4. Bigtable routes the message to the Bigtable cluster that contains the table.

  5. The write request is committed to the table.

  6. After a successful completion of a write operation, the Bigtable API returns a success response.




If a write operation fails, it's handled as follows:

  1. The Pub/Sub message is negatively acknowledged.

  2. Pub/Sub resends the message.

  3. If the message fails enough times, and a dead-letter topic is configured on the subscription, then the message is moved to the dead-letter topic.




## Delivery semantics

Bigtable subscriptions support _at-least-once_ delivery. If you require exact de-duplication of messages, consider implementing downstream processes to handle potential duplicates in Bigtable, or else use Dataflow's [exactly-once processing](https://docs.cloud.google.com/dataflow/docs/concepts/exactly-once) capabilities.

## Handle message failures

If a Pub/Sub message can't be written to Bigtable, the message can't be acknowledged. To forward such undeliverable messages, configure a [dead-letter topic](https://docs.cloud.google.com/pubsub/docs/dead-letter-topics#dead-letter_topic) on the Bigtable subscription. The Pub/Sub message forwarded to the dead-letter topic contains an attribute named `CloudPubSubDeadLetterSourceDeliveryErrorMessage` that contains the reason for the write failure.

If Pub/Sub can't write messages to Bigtable, then Pub/Sub backs off delivery of messages in a way similar to [push backoff](https://docs.cloud.google.com/pubsub/docs/push#push_backoff) behavior.

## Quotas and limits

Pub/Sub has quota limitations on the Bigtable subscriber throughput per region. For more information, see [Pub/Sub quotas and limits](https://docs.cloud.google.com/pubsub/quotas).

For information about Bigtable limits, see [Quotas and limits](https://docs.cloud.google.com/bigtable/quotas) in the Bigtable documentation.

## Pricing

To learn about the pricing for Bigtable subscriptions, see the [Pub/Sub pricing](https://cloud.google.com/pubsub/pricing) page.

## What's next

  * [Learn more about Bigtable](https://docs.cloud.google.com/bigtable/docs/overview)

  * [Create a Bigtable subscription](https://docs.cloud.google.com/pubsub/docs/create-bigtable-subscription)

  * [Choose a subscription type](https://docs.cloud.google.com/pubsub/docs/subscriber)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
