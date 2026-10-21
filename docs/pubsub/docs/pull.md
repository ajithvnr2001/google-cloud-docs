---
url: https://docs.cloud.google.com/pubsub/docs/pull/
title: Pull subscriptions \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:46:04.043074+00:00
---

# Pull subscriptions  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/pull/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Pull subscriptions Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of a pull subscription, its workflow, and associated properties.

In a pull subscription, a subscriber client requests messages from the Pub/Sub server.

The pull mode can use one of the two service APIs, Pull or StreamingPull. To run the chosen API, you can select a Google-provided high-level client library, or a low-level auto-generated client library. You can also choose between asynchronous and synchronous message processing.

**Note:** For most use cases, we recommend the Google-provided high-level client library with the StreamingPull API and asynchronous message processing.

## Before you begin

Before reading this document, ensure that you're familiar with the following:

  * How [Pub/Sub works](https://docs.cloud.google.com/pubsub/docs/overview) and the different Pub/Sub terms.

  * The different [kinds of subscriptions](https://docs.cloud.google.com/pubsub/docs/subscription-overview) that Pub/Sub supports and why you might want to use a pull subscription.




## Pull subscription workflow

For a pull subscription, your subscriber client initiates requests to a Pub/Sub server to retrieve messages. The subscriber client uses one of the following APIs:

  * [REST `Pull`API](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions/pull)
  * [RPC `PullRequest` API](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#google.pubsub.v1.PullRequest)
  * [RPC `StreamingPullRequest` API](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#streamingpullrequest)



Most subscriber clients don't make these requests directly. Instead, the clients rely on the Google Cloud-provided high-level client library that performs streaming pull requests internally and delivers messages asynchronously. For a subscriber client that needs greater control over how messages are pulled, Pub/Sub uses a low-level and automatically generated gRPC library. This library makes pull or streaming pull requests directly. These requests can be synchronous or asynchronous.

The following two images show the workflow between a subscriber client and a pull subscription.

![Flow of messages for a pull subscription](https://docs.cloud.google.com/static/pubsub/images/subscriber_pull.png)**Figure 1.** Workflow for a pull subscription

  
  
![Flow of messages for a
streamingPull subscription](https://docs.cloud.google.com/static/pubsub/images/subscriber_streamingpull.png)**Figure 2.** Workflow for a streaming pull subscription

#### Pull workflow

The pull workflow is as follows and references Figure 1:

  1. The subscriber client explicitly calls the `pull` method, which requests messages for delivery. This request is the `PullRequest` as shown in the image.
  2. The Pub/Sub server responds with zero or more messages and acknowledgment IDs. A response with zero messages or with an error does not necessarily indicate that there are no messages available to receive. This response is the `PullResponse` as shown in the image.

  3. The subscriber client explicitly calls the `acknowledge` method. The client uses the returned acknowledgment ID to acknowledge that the message is processed and need not be delivered again.




For a single streaming pull request, a subscriber client can have multiple responses returned due to the open connection. In contrast, only one response is returned for each pull request.

## Properties of a pull subscription

The properties that you configure for a pull subscription determine how you write messages to your subscription. For more information, see [subscription properties](https://docs.cloud.google.com/pubsub/docs/subscription-properties).

## Pub/Sub service APIs

The Pub/Sub pull subscription can use one of the following two APIs for retrieving messages:

  * Pull
  * StreamingPull



Use unary Acknowledge and ModifyAckDeadline RPCs when you receive messages using these APIs. The two Pub/Sub APIs are described in the following sections.

### StreamingPull API

Where possible, the Pub/Sub client libraries use [StreamingPull](https://grpc.io/docs/what-is-grpc/core-concepts/#bidirectional-streaming-rpc) for maximum throughput and lowest latency. Although you might never use the StreamingPull API directly, it's important to know how it differs from the Pull API.

The StreamingPull API relies on a persistent bidirectional connection to receive multiple messages as they become available. The following is the workflow:

  1. The client sends a request to the server to establish a connection. If the connection quota is exceeded, the server returns a resource exhausted error. The client library retries the out-of-quota errors automatically.

  2. If there is no error or the connection quota is available again, the server continuously sends messages to the connected client.

  3. If or when the throughput quota is exceeded, the server stops sending messages. However, the connection is not broken. Whenever there's sufficient throughput quota available again, the stream resumes.

  4. The client or the server eventually closes the connection.




The StreamingPull API keeps an open connection. The Pub/Sub servers recurrently close the connection after a time period to avoid a long-running sticky connection. The client library automatically reopens a StreamingPull connection.

Messages are sent to the connection when they are available. The StreamingPull API thus minimizes latency and maximizes throughput for messages.

**Note:** The PHP client library does not support the StreamingPull API.

Read more about the StreamingPull RPC methods: [StreamingPullRequest](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#google.pubsub.v1.StreamingPullRequest) and [StreamingPullResponse](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#google.pubsub.v1.StreamingPullResponse).

### Pull API

This API is a traditional unary RPC that is based on a request and response model. A single pull response corresponds to a single pull request. The following is the workflow:

  1. The client sends a request to the server for messages. If the throughput quota is exceeded, the server returns a resource exhausted error.

  2. If there is no error or the throughput quota is available again, the server replies with zero or more messages and acknowledgment IDs.




**When using the unary Pull API, a response with zero messages or with an error does not necessarily indicate that there are no messages available to receive.**

Using the Pull API does not guarantee low latency and a high throughput of messages. To achieve high throughput and low latency with the Pull API, you must have multiple simultaneous outstanding requests. New requests are created when old requests receive a response. Architecting such a solution is error-prone and hard to maintain. We recommend that you use the StreamingPull API for such use cases.

Use the Pull API instead of the StreamingPull API only if you require strict control over the following:

  * The number of messages that the subscriber client can process
  * The client memory and resources



You can also use this API when your subscriber is a proxy between Pub/Sub and another service that operates in a more pull-oriented way.

Read more about the Pull REST methods: [Method: projects.subscriptions.pull](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions/pull).

Read more about the Pull RPC methods: [PullRequest](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#google.pubsub.v1.PullRequest) and [PullResponse](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#pullresponse).

## Types of message processing modes

Choose one of the following pull modes for your subscriber clients.

### Asynchronous pull mode

Asynchronous pull mode decouples the receiving of messages from the processing of messages in a subscriber client. This mode is the default for most subscriber clients. Asynchronous pull mode can use the StreamingPull API or unary Pull API. Asynchronous pull can also use the high-level client library or low-level auto-generated client library.

You can learn more about client libraries later in this document.

### Synchronous pull mode

In synchronous pull mode, the receiving and processing of messages occur in sequence and are not decoupled from each other. Hence, similar to StreamingPull versus unary Pull APIs, asynchronous processing offers lower latency and higher throughput than synchronous processing.

Use synchronous pull mode only for applications where low latency and high throughput are not the most important factors as compared to some other requirements. For example, an application might be limited to using only the synchronous programming model. Or, an application with resource constraints might require more exact control over memory, network, or CPU. In such cases, use synchronous mode with the unary Pull API.

## Pub/Sub client libraries

Pub/Sub offers a high-level and a low-level auto-generated client library.

### High-level Pub/Sub client library

The high-level client library provides options for controlling the acknowledgment deadlines by using lease management. These options are more granular than when you configure the acknowledgment deadlines by using the console or the CLI at the subscription level. The high-level client library also implements support for features such as ordered delivery, exactly-once delivery, and flow control.

We recommend using asynchronous pull and the StreamingPull API with the high-level client library. Not all languages that are supported for Google Cloud also support the Pull API in the high-level client library.

To use the high-level client libraries, see [Pub/Sub client libraries](https://docs.cloud.google.com/pubsub/docs/reference/libraries).

### Low-level auto-generated Pub/Sub client library

A low-level client library is available for cases where you must use the Pull API directly. You can use synchronous or asynchronous processing with the low-level auto-generated client library. You must manually code features such as ordered delivery, exactly-once delivery, flow control, and lease management when you use the low-level auto-generated client library.

You can use the synchronous processing model when you use the low-level auto-generated client library for all supported languages. You might use the low-level auto-generated client library and synchronous pull in cases where using the Pull API directly makes sense. For example, you might have existing application logic that relies on this model.

To use the low-level auto-generated client libraries directly, see [ Pub/Sub APIs overview](https://docs.cloud.google.com/pubsub/docs/reference/service_apis_overview).

## What's next

  * Create a pull [subscription](https://docs.cloud.google.com/pubsub/docs/create-subscription) for your topic.

  * [Receive messages from a pull subscription](https://docs.cloud.google.com/pubsub/docs/pull-messages)

  * Troubleshoot a [pull subscription](https://docs.cloud.google.com/pubsub/docs/pull-troubleshooting).

  * Create or modify a subscription with [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions).

  * Create or modify a subscription with [REST APIs](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions).

  * Create or modify a subscription with [RPC APIs](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
