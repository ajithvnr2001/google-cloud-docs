---
url: https://docs.cloud.google.com/pubsub/docs/pubsub-basics/
title: Overview of the Pub/Sub service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:53.415202+00:00
---

# Overview of the Pub/Sub service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/pubsub-basics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Overview of the Pub/Sub service Stay organized with collections  Save and categorize content based on your preferences. 

Pub/Sub is a _publish/subscribe_ (_Pub/Sub_) _service_ , a messaging service where the senders of messages are decoupled from the receivers of messages. There are several key concepts in a Pub/Sub service which are explained with the help of the following figure.

![Figure showing
  different components of a Pub/Sub service and how they connect to each
  other.](https://docs.cloud.google.com/static/pubsub/images/pubsub-components.png)**Figure 1** Two publisher clients send two different messages to a common Pub/Sub topic. 

The following are the components of a Pub/Sub service:

  * **Publisher** (also called a producer): creates messages and sends (publishes) them to the messaging service on a specified topic.

  * **Message** : the data that moves through the service.

  * **Topic** : a named entity that represents a feed of messages.

  * **Schema** : a named entity that governs the data format of a Pub/Sub message.

  * **Subscription** : a named entity that represents an interest in receiving messages on a particular topic.

  * **Subscriber** (also called a consumer): receives messages on a specified subscription.




The following procedure discusses the workflow of the Pub/Sub service:

  1. Two publisher applications, **Publisher 1** and **Publisher 2** , send messages to a single Pub/Sub topic. **Publisher 1** sends message **A** and **Publisher 2** sends message **B**.

  2. The topic itself is attached to two subscriptions. These are **Subscription 1** and **Subscription 2**.

  3. The topic is also attached to a schema.

  4. Each subscription receives a copy of **A** and **B** messages from the topic.

  5. **Subscription 1** is connected to two subscriber applications, **Subscriber 1** and **Subscriber 2**. The two subscriber applications receive a subset of the messages from the topic. In this example, **Subscriber 1** receives **message B** while **Subscriber 2** receives **message A** from the topic.

  6. **Subscription 2** is only connected to a single subscriber application called **Subscriber 3**. Thus, **Subscriber 3** receives all the messages from the topic.




## Life of a message

Assume that a single publisher client is connected to a topic. The topic has a single subscription attached to it. A single subscriber is connected to the subscription.

![Figure showing
  how a message flows within Pub/Sub.](https://docs.cloud.google.com/static/pubsub/images/pub_sub_flow.svg)**Figure 2** A message flows from a publisher client to a subscriber client through Pub/Sub.

The following steps describe how a message flows in Pub/Sub:

  1. A publisher application sends a message to a Pub/Sub topic.

  2. The message is written to storage.

  3. Along with writing the message to storage, Pub/Sub delivers the message to all the attached subscriptions of the topic.

In this example, it's a single subscription.

  4. The subscription sends the message to an attached subscriber application.

  5. The subscriber sends an acknowledgment to Pub/Sub that they have processed the message.

After at least one subscriber for each subscription has acknowledged the message, Pub/Sub deletes the message from storage.




## Status of a message in Pub/Sub

While a message is outstanding to a subscriber, Pub/Sub doesn't try to deliver it to any other subscriber on the same subscription. The subscriber has a configurable, limited amount of time, known as the [ackDeadline](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions/modifyAckDeadline), to acknowledge the outstanding message. After the deadline passes, the message is no longer considered outstanding, and is available for delivery again.

There can be three states for a message in a Pub/Sub service:

  * **Acknowledged messages (acked).** After a subscriber application processes a message sent from a topic to a subscription, it sends an acknowledgment back to Pub/Sub. If all the subscriptions on a topic have acknowledged the message, the message is asynchronously deleted from the publish message source and from storage.

  * **Unacknowledged messages (unacked)**. If Pub/Sub doesn't receive an acknowledgment within the acknowledgment deadline, a message might be delivered more than once. For example, the subscriber might send an acknowledgment after the deadline expires or the acknowledgment might be lost due to transient network issues. An unacknowledged message continues to be delivered until the message retention duration expires since the message was published. At this point, the message expires.

  * **Negatively acknowledged messages (nacked)**. Nacking a message by a subscriber causes Pub/Sub to redeliver it immediately based on [default retry settings](https://docs.cloud.google.com/pubsub/docs/subscription-retry-policy#immediate_redelivery), which can be modified. When a subscriber nacks messages that are invalid or when it cannot process the messages, the subscriber helps ensure that these messages are not lost and that they are successfully processed. You can use [modifyAckDeadline](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions/modifyAckDeadline) with a value of 0 to nack a message.




## Choose a Pub/Sub publish and subscribe pattern

When there are multiple Pub/Sub publisher and subscriber clients, you must also choose the kind of publish and subscribe architecture that you want to set up.

![Figure showing
  different publish and subscribe patterns.](https://docs.cloud.google.com/static/pubsub/images/pubsub-patterns.png)**Figure 3** Publisher-subscriber relationships can be many-to-one (fan-in), many-to-many (load-balanced), and one-to-many (fan-out). 

Some of the supported Pub/Sub publish-subscribe patterns include the following:

  * **Fan in (many-to-one).** In this example, multiple publisher applications publish messages to a single topic. This single topic is attached to a single subscription. The subscription is, in turn, connected to a single subscriber application that gets all the published messages from the topic.

  * **Load balanced (many-to-many).** In this example, a single or multiple publisher applications publish messages to a single topic. This single topic is attached to a single subscription that is, in turn, connected to multiple subscriber applications. Each of the subscriber applications gets a subset of the published messages, and no two subscriber applications get the same subset of messages. In this load balancing case, you use multiple subscribers to process messages at scale. If more messages need to be supported, you add more subscribers to receive messages from the same subscription.

  * **Fan out (one-to-many).** In this example, a single or multiple publisher applications publish messages to a single topic. This single topic is attached to multiple subscriptions. Each subscription is connected to a single subscriber application. Each of the subscriber applications gets the same set of published messages from the topic. When a topic has multiple subscriptions, then every message has to be sent to a subscriber receiving messages on behalf of each subscription. If you need to perform different data operations on the same set of messages, fan out is a good option. You can also attach multiple subscribers to each subscription and get a load-balanced subset of messages for each subscriber.




## Choose a Pub/Sub configuration option

You can configure a Pub/Sub environment by using any one of the following options:

  * Google Cloud console
  * Google Cloud CLI
  * Cloud Client libraries (high-level client library)
  * REST and RPC APIs (low-level client library)



Your choice of a Pub/Sub configuration option depends on your use case.

If you're new to Google Cloud console and want to test Pub/Sub, then use the console or the `gcloud CLI`.

The high-level client library is recommended for cases where you require high throughput and low latency with minimal operational overhead and processing cost. By default, the high-level client library uses the [StreamingPull API](https://grpc.io/docs/what-is-grpc/core-concepts/#bidirectional-streaming-rpc). The high-level client libraries contain prebuilt functions and classes that handle the underlying API calls for authentication, throughput and latency optimization, message formatting, and other features.

The low-level client library is an auto-generated gRPC library and comes into play when you use the service APIs directly.

  * To use the high-level client libraries, see [Pub/Sub client libraries](https://docs.cloud.google.com/pubsub/docs/reference/libraries).

  * To use the low-level auto-generated client libraries directly, see [Pub/Sub APIs overview](https://docs.cloud.google.com/pubsub/docs/reference/service_apis_overview).




The following are some best practices for using the client libraries:

  * **Choose the right client library language.** The performance of the Pub/Sub client libraries varies by language. For example, the Java client library is more effective in scaling up vertically than the Python client library, and can handle more throughput. Java, C++, and Go are more efficient languages in terms of compute resources required to handle the publish or subscribe loads.

  * **Use the latest version of the client library.** The Pub/Sub client libraries are constantly being updated with new features and bug fixes. Make sure you are using the latest version of the client library for your language.

  * **Reuse publisher clients.** When publishing messages, it is more efficient to reuse the same publisher client instead of creating new publisher clients for each publish request. This is because the first publish request after creating a new publisher client requires some time to establish an authorized connection. In some languages like Node that don't have an explicit publisher client, reuse the object on which you call the publish method. For example, in Node, save and reuse the topic object.




## How to set up Pub/Sub

Here are the top-level steps to configure Pub/Sub:

  1. Create or choose a Google Cloud project where you can set up Pub/Sub.

  2. Enable the Pub/Sub API.

  3. Get the required roles and permissions to run Pub/Sub.

  4. Create a topic.

  5. If message structure is critical, define a schema for your messages.

  6. Attach the schema to the topic.

  7. Configure a publisher client that can publish messages to the topic.

  8. If required, configure advanced publishing options such as flow control, batch messaging, and concurrency control.

  9. Choose a subscription type based on how you want to receive messages.

  10. Create a subscription for the chosen topic.

  11. Configure a subscriber client that can receive messages from the subscription.

  12. If required, configure advanced message delivery options such as exactly-once delivery, lease management, ordered delivery, and flow control.

  13. Begin publishing messages from your publisher client to the topic.

  14. Simultaneously, set up your subscriber client to receive and process these messages.




## Guidelines to name a topic, subscription, schema, or snapshot

A Pub/Sub resource name uniquely identifies a Pub/Sub resource, such as a topic, subscription, schema or snapshot. The resource name must fit the following format:

`projects/project-identifier/collection/ID`

  * `project-identifier`: Must be the project ID or project number, available from the Google Cloud console. For example, `my-cool-project` is a project ID. `123456789123` is a project number.

  * `collection`: Must be one of `topics`, `subscriptions`, `schemas`, or `snapshots`.

  * `ID`: Must conform to the following guidelines:

    * Not begin with the string `goog`
    * Start with a letter
    * Contain between 3 and 255 characters
    * Contain only the following characters: Letters `[A-Za-z]`, numbers `[0-9]`, dashes `-`, underscores `_`, periods `.`, tildes `~`, plus signs `+`, and percent signs `%`

You can use the special characters in the preceding list in resource names without URL-encoding. However, you must ensure that any other special characters are properly encoded or decoded when you use them in URLs. For example, `mi-tópico` is an invalid _ID_. However, `mi-t%C3%B3pico` is valid. This format is important when you make REST calls.




**Note:** The [ client libraries](https://docs.cloud.google.com/pubsub/docs/reference/libraries) can take different approaches to naming resources, such as specifying the _project-identifier_ and the _ID_ in separate fields.

## What's next

  * To get started with configuring Pub/Sub using gcloud CLI, see [Quickstart: Publish and receive messages in Pub/Sub by using the gcloud CLI](https://docs.cloud.google.com/pubsub/docs/publish-receive-messages-gcloud).

  * To get started with configuring Pub/Sub using Google Cloud console, see [Quickstart: Publish and receive messages in Pub/Sub using the Google Cloud console](https://docs.cloud.google.com/pubsub/docs/publish-receive-messages-console).

  * To get started with configuring Pub/Sub using the client libraries, see [Quickstart: Publish and receive messages in Pub/Sub using the client library](https://docs.cloud.google.com/pubsub/docs/publish-receive-messages-client-library).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
