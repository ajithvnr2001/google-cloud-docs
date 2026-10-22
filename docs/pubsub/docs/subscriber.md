---
url: https://docs.cloud.google.com/pubsub/docs/subscriber/
title: Choose a subscription type \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:47.900010+00:00
---

# Choose a subscription type  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/subscriber/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Choose a subscription type Stay organized with collections  Save and categorize content based on your preferences. 

This document helps you choose the appropriate type of Pub/Sub subscription suited to your business requirements.

Pub/Sub offers the following types of subscriptions:

  * **Pull subscriptions** use a subscriber client to request messages from the Pub/Sub server.

  * **Push subscriptions** use the Pub/Sub server to initiate requests to your subscriber application to deliver messages.

  * **Export subscriptions** export your messages directly to a Google Cloud resource. These subscriptions include the following:

    * **BigQuery subscriptions** export data to a BigQuery table.

    * **Bigtable subscriptions** ([Preview](https://cloud.google.com/products#product-launch-stages)) export data to a Bigtable table.

    * **Cloud Storage subscriptions** export data to a Cloud Storage bucket.




## Pub/Sub subscription comparison table

The following table offers some guidance in choosing the appropriate delivery mechanism for your application:

Features supported by Pub/Sub subscriptions  
---  
Use case | **Pull subscription** | 

  * Large volume of messages (GBs per second).
  * Efficiency and throughput of message processing is critical.
  * Environments where it's not feasible to set up a public HTTPS endpoint with a non-self-signed SSL certificate.

  
**Push subscription** | 

  * Multiple topics that must be processed by the same webhook.
  * [App Engine Standard](https://docs.cloud.google.com/appengine/docs/standard/overview) or [ Cloud Run functions](https://docs.cloud.google.com/run/docs/functions/overview) subscribers.
  * Environments where it's not feasible to set up Google Cloud dependencies such as credentials and the client library.

  
**Export subscription** | 

  * Large volume of messages that can scale up to multiple millions of messages per second.
  * Sending messages directly to a Google Cloud resource without any additional processing.

  
Endpoints | **Pull subscription** |  Any device on the internet that has authorized credentials can call the Pub/Sub API.   
**Push subscription** |  An HTTPS server with non-self-signed certificate accessible on the public web. The receiving endpoint might be decoupled from the Pub/Sub subscription, so that messages from multiple subscriptions are sent to a single endpoint.  
**Export subscription** |  The subscription writes to a Google Cloud resource, such as a BigQuery table or Cloud Storage bucket.   
Load balancing | **Pull subscription** |  Multiple subscribers can make pull calls to the same subscription. Each subscriber receives a subset of messages.   
**Push subscription** |  Push endpoints can be load balancers.  
**Export subscription** |  The Pub/Sub service automatically balances the load.   
Configuration | **Pull subscription** |  No configuration is necessary.  
**Push subscription** | 

  * No configuration is necessary for App Engine apps in the same project as the subscriber.
  * Verification of push endpoints is not required in the Google Cloud console.
  * Endpoints must be reachable using DNS names and have SSL certificates installed.

  
**Export subscription** |  The Google Cloud resource that the subscription exports to must exist and be configured with the appropriate permissions.   
Flow control | **Pull subscription** |  The subscriber client controls the rate of delivery. The subscriber can dynamically modify the acknowledgment deadline, allowing message processing to take an arbitrarily long time.   
**Push subscription** |  The Pub/Sub server automatically implements flow control. Clients don't need to handle message flow. However, it's possible to indicate that the client can't handle the current message load, by passing back an HTTP error.   
**Export subscription** |  Pub/Sub automatically implements flow control to optimize writing messages to the destination Google Cloud resource.   
Efficiency and throughput | **Pull subscription** |  Achieves high throughput at low CPU and bandwidth by allowing batched delivery, acknowledgments, and massively parallel consumption. Might be inefficient if frequent polling is used to minimize message delivery time.   
**Push subscription** |  Delivers one message per request and limits the maximum number of outstanding messages.   
**Export subscription** |  Pub/Sub dynamically handles scalability.   
  
## When to use an export subscription

Without an export subscription, you need a pull or push subscription and a subscriber (such as Dataflow) to read messages and write them to a Google Cloud resource. The overhead of running a Dataflow job is not necessary when messages don't require additional processing before being stored.

Export subscriptions have the following advantages:

  * **Simple deployment.** You can set up an export subscription through a single workflow in the console, Google Cloud CLI, client library, or Pub/Sub API.

  * **Low costs.** Reduces the additional cost and latency of similar Pub/Sub pipelines that include Dataflow jobs. This cost optimization is useful for messaging systems that don't require additional processing before storage.

  * **Minimal monitoring.** Export subscriptions are part of the multi-tenant Pub/Sub service and don't require you to run separate monitoring jobs.

  * **Flexibility**. Export subscriptions provide features that aren't available in the Google-provided Dataflow templates. For example:

    * A BigQuery subscription can use the schema of the topic to which it is attached.

    * A Cloud Storage subscription offers configurable file batching options based on file size and elapsed time.

    * A Bigtable subscription ([Preview](https://cloud.google.com/products#product-launch-stages)) has a built-in option to write message metadata to a dedicated column family.




However, if your application needs to perform data transformations that can't be implemented using [Single Message Transforms](https://docs.cloud.google.com/pubsub/docs/smts/smts-overview) (SMTs), before writing the messages to a destination, then we recommend using a Dataflow pipeline.

To learn how to stream data from Pub/Sub to BigQuery with transformation by using Dataflow, see [Stream from Pub/Sub to BigQuery](https://docs.cloud.google.com/dataflow/docs/tutorials/dataflow-stream-to-bigquery).

To learn how to stream data from Pub/Sub to Cloud Storage with transformation by using Dataflow, see [Stream messages from Pub/Sub by using Dataflow](https://docs.cloud.google.com/pubsub/docs/stream-messages-dataflow).

## What's next

Understand the workflow for each subscription type:

  * [Pull](https://docs.cloud.google.com/pubsub/docs/pull)

  * [Push](https://docs.cloud.google.com/pubsub/docs/push)

  * [BigQuery](https://docs.cloud.google.com/pubsub/docs/bigquery)

  * [Bigtable](https://docs.cloud.google.com/pubsub/docs/bigtable-subscriptions)

  * [Cloud Storage](https://docs.cloud.google.com/pubsub/docs/cloudstorage)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
