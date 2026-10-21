---
url: https://docs.cloud.google.com/pubsub/docs/cloudstorage/
title: Cloud Storage subscriptions \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:20:56.258104+00:00
---

# Cloud Storage subscriptions  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/cloudstorage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Cloud Storage subscriptions Stay organized with collections  Save and categorize content based on your preferences. 

A Cloud Storage subscription is a type of export subscription that writes messages to an existing Cloud Storage bucket as they are received. You don't need to configure a separate subscriber client. Use the Google Cloud console, the Google Cloud CLI, the client libraries, or the Pub/Sub API to create, update, list, detach, or delete a Cloud Storage subscription.

**Key Point:** Understand the workflow for a Cloud Storage subscription and read about the permissions, properties, quotas, and pricing related to the subscription.

Without the Cloud Storage subscription type, you need a pull or push subscription and a subscriber (such as Dataflow) that reads messages and writes them to a Cloud Storage bucket. The overhead of running a Dataflow job is not necessary when messages don't require additional processing before storing them in a Cloud Storage bucket; you can use a Cloud Storage subscription instead.

For lightweight modifications to messages or attributes, you can attach a [Single Message Transform](https://docs.cloud.google.com/pubsub/docs/smts/smts-overview) to your Cloud Storage subscription. However, a Dataflow pipeline is recommended for Pub/Sub systems where more complex data transformation is required before the data is stored in a Cloud Storage bucket, especially if you want to window or aggregate across messages.

To learn how to stream data from Pub/Sub to Cloud Storage with transformation by using Dataflow, see [Stream messages from Pub/Sub by using Dataflow](https://docs.cloud.google.com/pubsub/docs/stream-messages-dataflow).

## Before you begin

Before reading this document, ensure that you're familiar with the following:

  * How [Pub/Sub works](https://docs.cloud.google.com/pubsub/docs/overview) and the different Pub/Sub terms.

  * What are the different [kinds of subscriptions](https://docs.cloud.google.com/pubsub/docs/subscriber) and why you might want to use a Cloud Storage subscription.

  * How [Cloud Storage](https://docs.cloud.google.com/storage/docs) works.




### Cloud Storage subscription workflow

The following image shows the workflow between a Cloud Storage subscription and Cloud Storage.

![Flow of messages for a Cloud Storage subscription](https://docs.cloud.google.com/static/pubsub/images/cloud-storage-subscription.png)

**Figure 1.** Workflow for a Cloud Storage subscription

Here is a brief description of the workflow that references Figure 1:

  1. Pub/Sub uses the Cloud Storage API to send data to the Cloud Storage bucket. After a successful completion of a write operation, the API returns an `OK` response.

  2. The messages are sent in batches to the Cloud Storage bucket. A single batch corresponds to an [object](https://docs.cloud.google.com/storage/docs/objects) that is stored in the Cloud Storage bucket. You can configure the batch settings based on the object size and time elapsed since the object was created.

  3. The workflow to write an object to a Cloud Storage bucket requires two `OK` responses. The first `OK` response is sent when a message is successfully written to an object. The second `OK` response is sent when the object containing the message is finalized. A message only becomes visible in the bucket after the Cloud Storage object containing it has been successfully finalized.

  4. If there are any failures during the write operation, the Pub/Sub message itself is negatively acknowledged. The message is then resent. If the message write operation fails enough times and you have a dead-letter topic configured on the subscription, then the message is moved to the dead-letter topic.




### Properties of a Cloud Storage subscription

When you create a Cloud Storage subscription, you must specify some additional properties. These properties include common subscription properties, filename and format requirements, storage requirements and more. To learn more about these properties, see [Cloud Storage subscription properties](https://docs.cloud.google.com/pubsub/docs/create-cloudstorage-subscription#subscription_properties).

### Handle message failures

When a Pub/Sub message cannot be written to a Cloud Storage bucket, the message cannot be acknowledged. To forward such undeliverable messages, configure a [dead-letter topic](https://docs.cloud.google.com/pubsub/docs/handling-failures#dead-letter_topic) on the Cloud Storage subscription.

If Pub/Sub cannot write messages to Cloud Storage, then Pub/Sub backs off delivery of messages in a way similar to [push backoff behavior](https://docs.cloud.google.com/pubsub/docs/push#push_backoff). 

### Quotas

Quota limitations apply to the Cloud Storage subscriber throughput for each region. For information about the quotas for Cloud Storage subscriptions, see export subscriber quota limits in [Pub/Sub quotas and limits](https://docs.cloud.google.com/pubsub/quotas).

### Pricing

For information about the pricing for Cloud Storage subscriptions, see the [Pub/Sub pricing page](https://cloud.google.com/pubsub/pricing#cloudstorage).

## What's next

  * Create a [Cloud Storage subscription](https://docs.cloud.google.com/pubsub/docs/create-cloudstorage-subscription).
  * Troubleshoot a [Cloud Storage subscription](https://docs.cloud.google.com/pubsub/docs/cloudstorage-troubleshooting).

  * Explore Pub/Sub configuration tools:

    * [`gcloud` CLI commands](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions)
    * [Pub/Sub APIs](https://docs.cloud.google.com/pubsub/docs/reference/service_apis_overview)
    * [Pub/Sub client libraries](https://docs.cloud.google.com/pubsub/docs/reference/libraries)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
