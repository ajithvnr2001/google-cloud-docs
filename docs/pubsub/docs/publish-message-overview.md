---
url: https://docs.cloud.google.com/pubsub/docs/publish-message-overview/
title: Publish message overview \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:28.806140+00:00
---

# Publish message overview  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/publish-message-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Publish message overview Stay organized with collections  Save and categorize content based on your preferences. 

To publish a message with Pub/Sub, a publisher application creates and sends messages to a topic.

This document provides an overview of the publish workflow, including the concept of topics and messages.

## About topics

A Pub/Sub _topic_ is a named resource that represents a feed of messages. When a publisher sends a message, it targets a specific topic. The Pub/Sub service uses this topic name to route the message to all subscriptions attached to the topic. If there are multiple subscribers for a subscription, only one subscriber in the subscription receives the message.

Publishers don't have to know how many subscribers exist. They focus on the topic, ensuring the separation of concerns between message sending and message receiving.

Pub/Sub supports two kinds of topics: a standard topic and an import topic.

### Properties of a topic

When you create or update a topic, you can specify the topic properties.

For more information about the topic properties, see [Properties of a topic](https://docs.cloud.google.com/pubsub/docs/create-topic#properties_of_a_topic).

### About import topics

An import topic lets Pub/Sub ingest streaming data from another source and act as the publisher application that sends the data to the topic. You can enable ingestion on a topic by using the console, Google Cloud CLI, REST calls, or the client libraries. As part of managing the import topic, Google Cloud provides monitoring and scaling of the ingestion pipeline.

Without an import topic, streaming data into Pub/Sub from a data source requires an additional service. This additional service pulls data from the original source and publishes it to Pub/Sub. The additional service can be a streaming engine such as Apache Spark or a custom-written service. You must also configure, deploy, run, scale, and monitor this service.

The following is a list of important information regarding import topics:

  * Similar to a standard topic, you can still manually publish to an import topic.

  * You can only attach a single ingestion source to an import topic.




We recommend import topics for streaming data. If you are considering batch data ingestion into BigQuery instead of streaming data ingestion, you can try [BigQuery Data Transfer Service](https://docs.cloud.google.com/bigquery/docs/dts-introduction). If you want to ingest data into Cloud Storage, [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview) (STS) is a good option.

Pub/Sub supports the following sources for import topics:

  * [Amazon Kinesis Data Streams](https://docs.cloud.google.com/pubsub/docs/create-aws-kinesis-import-topic)
  * [Cloud Storage](https://docs.cloud.google.com/pubsub/docs/create-cloud-storage-import-topic)
  * [Azure Event Hubs](https://docs.cloud.google.com/pubsub/docs/create-azure-event-hub-import-topic)
  * [Amazon MSK](https://docs.cloud.google.com/pubsub/docs/create-amazon-msk-import-topic)
  * [Confluent Cloud](https://docs.cloud.google.com/pubsub/docs/create-confluent-cloud-import-topic)



### Data replication in a topic

A Pub/Sub topic uses three zones to store data. The service supports synchronous replication to at least two zones, and best-effort replication to an additional third zone. Pub/Sub replication is within just one region.

## About messages

A Pub/Sub _message_ is the data that moves through the service.

A message consists of fields with the message data and metadata. A message must contain either message data or at least one attribute.

  * **The message data** : This is the core content of the message and can be any text or binary data. It represents the actual information you want to communicate between publishers and subscribers. If you're using the [REST API](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage) directly, the message data must be base64-encoded. See the example in the REST tab in the [Publish messages](https://docs.cloud.google.com/pubsub/docs/publisher#rest) section.

  * **An ordering key** : This is an optional identifier that represents the entity for which messages must be ordered. Messages with the same ordering key are expected to be delivered to a subscriber in the order they were published. An ordering key is only required if you want ordered delivery of your messages. For more information about ordering keys, see [Order messages](https://docs.cloud.google.com/pubsub/docs/ordering).

  * **Attributes** : These are optional key-value pairs that provide additional context and information about the message. They can be used for routing, filtering, or enriching the message content. For example, you could add attributes such as timestamps or transaction IDs. For more information about attributes used in publishing messages, see [Use attributes to publish a message](https://docs.cloud.google.com/pubsub/docs/publisher#using-attributes).




The Pub/Sub service adds the following fields to the message:

  * A message ID unique to the topic
  * A timestamp for when the Pub/Sub service receives the message



When publishing messages using Pub/Sub client libraries, provide the message `data` as a byte array, such as a Node.js `Buffer`. If your data is a string, you must first encode it to bytes, for example by using UTF-8 encoding, before passing it to the client library.

If you're using the [REST API](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage) directly, the message data must be base64-encoded and sent as a string.

The following example shows a [JSON representation of a message](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage) sent by a client:
    
    
    {
      "data": "VGhpcyBpcyB0aGUgY29yZSBtZXNzYWdlIGNvbnRlbnQu",
      "attributes": {
        "category": "notification",
        "user_id": "12345",
        "priority": "medium"
      },
      "orderingKey": "12345"
    }
    

When a subscriber receives the message, it includes values for `messageId` and `publishTime`, added by the Pub/Sub service:
    
    
    {
      "data": "VGhpcyBpcyB0aGUgY29yZSBtZXNzYWdlIGNvbnRlbnQu",
      "attributes": {
        "category": "notification",
        "user_id": "12345",
        "priority": "medium"
      },
      "messageId": "19443130675731448",
      "publishTime": "2026-05-04T23:15:19.863Z",
      "orderingKey": "12345"
      }
    }
    

## Publish message workflow

To publish a message with Pub/Sub, a publisher application creates and sends messages to a **topic**.

  1. Create a message containing your data.
  2. Select any optional publishing attributes.
  3. Send a request to the Pub/Sub server to publish the message to a specified topic.
  4. The Pub/Sub service receives the message and processes it as follows:

     * The message is stored for distribution.

     * The message is replicated across multiple zones for durability and high availability.

     * Pub/Sub identifies subscribers with subscriptions matching the message's topic, and delivers a copy of the message to each.




Pub/Sub offers at-least-once message delivery and best-effort ordering to existing subscribers.

For more information about the Pub/Sub system, see [Overview of the Pub/Sub service](https://docs.cloud.google.com/pubsub/docs/pubsub-basics).

For more information about how Pub/Sub works, see [Architectural overview of Pub/Sub](https://docs.cloud.google.com/pubsub/architecture).

## What's next

  * [Create a standard topic](https://docs.cloud.google.com/pubsub/docs/create-topic)

  * [Publish messages to a topic](https://docs.cloud.google.com/pubsub/docs/publisher)

  * [Learn about schemas](https://docs.cloud.google.com/pubsub/docs/schemas)




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
