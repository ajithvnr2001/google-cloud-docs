---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub
title: Package com.google.cloud.pubsublite.cloudpubsub (1.16.5) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:16.731179+00:00
---

# Package com.google.cloud.pubsublite.cloudpubsub (1.16.5)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Package com.google.cloud.pubsublite.cloudpubsub (1.16.5) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.5 (latest)  1.16.2  1.15.21  1.14.8  1.13.8  1.12.22  1.11.2  1.10.0  1.9.4  1.8.0  1.7.1  1.6.3  1.5.5  1.4.12 

[GitHub Repository](https://github.com/googleapis/java-pubsublite/tree/main//google-cloud-pubsublite/src/main/java/com/google/cloud/pubsublite/cloudpubsub)  
---  
  
## Settings Classes

Settings classes can be used to configure credentials, endpoints, and retry settings for a Client. 

Settings |  Description  
---|---  
[com.google.cloud.pubsublite.cloudpubsub.FlowControlSettings](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.FlowControlSettings) |  Describes limits on bytes and messages outstanding for a single partition Pub/Sub Lite subscriber. These are hard limits enforced by the server.  
[com.google.cloud.pubsublite.cloudpubsub.PublisherSettings](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings) |  Settings for instantiating a Pub/Sub Lite publisher emulating the Cloud Pub/Sub Publisher API.  
[com.google.cloud.pubsublite.cloudpubsub.SubscriberSettings](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.SubscriberSettings) |  Settings for instantiating a Pub/Sub Lite subscriber emulating the Cloud Pub/Sub Subscriber API.  
  
## Classes

Class |  Description  
---|---  
[com.google.cloud.pubsublite.cloudpubsub.FlowControlSettings.Builder](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.FlowControlSettings.Builder) |   
[com.google.cloud.pubsublite.cloudpubsub.MessageTransforms](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.MessageTransforms) |  MessageTransforms details how to transform message representations from Cloud Pub/Sub to Pub/Sub Lite. Transformers are made public to allow user code that currently uses PubsubMessages to use  
[com.google.cloud.pubsublite.cloudpubsub.PublisherSettings.Builder](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings.Builder) |   
[com.google.cloud.pubsublite.cloudpubsub.SubscriberSettings.Builder](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.SubscriberSettings.Builder) |   
  
## Interfaces

Interface |  Description  
---|---  
[com.google.cloud.pubsublite.cloudpubsub.KeyExtractor](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.KeyExtractor) |  A KeyExtractor can extract the Pub/Sub Lite 'key' field used for message routing from a PubsubMessage. It will by default use the ordering_key field directly for this if it exists. An empty ByteString implies that the message should have no ordering key.  
[com.google.cloud.pubsublite.cloudpubsub.NackHandler](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.NackHandler) |  A NackHandler handles when nack() is called in a user's AckReplyConsumer. Pub/Sub Lite does not have a concept of 'nack'. When nack() is called in an AckReplyConsumerr, nack(message) is called with the nacked message.   
[com.google.cloud.pubsublite.cloudpubsub.PartitionSubscriberClientSupplier](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PartitionSubscriberClientSupplier) |  Supplies new SubscriberServiceClient instances.  
[com.google.cloud.pubsublite.cloudpubsub.Publisher](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.Publisher) |  Pub/Sub Lite publishers are streaming based and can experience permanent errors.  
[com.google.cloud.pubsublite.cloudpubsub.ReassignmentHandler](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.ReassignmentHandler) |  A ReassignmentHandler is called any time a new partition assignment is received from the server. It will be called with both the previous and new assignments as decided by the backend. The client library will not acknowledge the assignment until handleReassignment returns. The  
[com.google.cloud.pubsublite.cloudpubsub.Subscriber](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.Subscriber) |  A sub-interface of com.google.cloud.pubsub.v1.SubscriberInterface.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-26 UTC."],[],[]] 
