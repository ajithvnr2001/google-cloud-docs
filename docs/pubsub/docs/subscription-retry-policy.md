---
url: https://docs.cloud.google.com/pubsub/docs/subscription-retry-policy/
title: Subscription retry policy \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:40.998208+00:00
---

# Subscription retry policy  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/subscription-retry-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Subscription retry policy Stay organized with collections  Save and categorize content based on your preferences. 

A subscriber might fail to process messages for several reasons. For example, the subscriber could experience temporary problems retrieving necessary data, or it might receive a message in an unexpected format.

If Pub/Sub attempts to deliver a message but the subscriber can't acknowledge it, Pub/Sub automatically tries to resend the message. This redelivery attempt is known as the subscription retry policy. This isn't a feature that you can turn on or off. However, you can choose what type of retry policy you want to use.

## Before you begin

  * [Create a topic](https://docs.cloud.google.com/pubsub/docs/create-topic) that you are going to use with your subscription that contains a subscription retry policy.



## Required roles

To get the permissions that you need to manage topics and subscriptions, ask your administrator to grant you the Pub/Sub Editor(`roles/pubsub.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

You can configure access control at the project level and at the individual resource level. You can create a subscription in one project and attach it to a topic located in a different project. Ensure that you have the required permissions for each project.

## Types of retry policies

When you first create and configure your subscription, you can choose to use one of the following retry policies, _immediate redelivery_ or _exponential backoff_. By default, subscriptions use immediate redelivery.

**Note:** This feature is independent from [Push backoff](https://docs.cloud.google.com/pubsub/docs/push#push_backoff). You can use these two features together to better control the flow of messages. In this case, the total delay is the maximum combined value of both the push backoff value and the retry policy value. If you're noticing issues with message delivery, double check how your retry policy is interacting with push backoff.

### Immediate redelivery

By default, Pub/Sub tries resending the message immediately (and potentially to the same subscriber client). However, if the conditions that prevented the message acknowledgment haven't changed, immediate redelivery can cause issues. In this case, it's possible that Pub/Sub will resend multiple messages that can't be acknowledged.

To address immediate redelivery issues, Pub/Sub lets you configure an [exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff) policy.

### Exponential backoff

Exponential backoff lets you add progressively longer delays between retry attempts. After the first delivery failure, Pub/Sub waits for a minimum backoff time before retrying. For each consecutive message failure, more time is added to the delay, up to a maximum delay (0 and 600 seconds).

The maximum and minimum delay intervals are not fixed, and should be configured based on local factors to your application.

Note the following considerations about exponential backoff:

  * Exponential backoff triggers on the following actions: 
    * When a negative acknowledgment is received.
    * When the acknowledgment deadline of a message expires.
  * Exponential backoff is only applied per-message, rather than to all the messages in a subscription (global).
  * While using exponential backoff, Pub/Sub continues to deliver other messages, even if previous messages received negative acknowledgments (unless you're using ordered message delivery).



Use the retry policy to delay the delivery and processing of a subset of messages to accommodate a _transient_ inability to process some messages upon delivery. The feature is applied on a best-effort basis and each message is evaluated for retry policy separately.

We don't recommend using this feature to introduce intentional delays in message delivery. If you negatively acknowledge (nack) a large number of messages on a subscription configured with a retry policy, it is possible that some of those messages are delivered with less or no backoff. Pub/Sub might also slow down the delivery of all messages if you negatively acknowledge a large number of messages.

If you need to schedule deliveries, consider using [Cloud Tasks](https://docs.cloud.google.com/tasks/docs).

## Configure exponential backoff

### Console

When creating a new subscription, you can configure an exponential backoff retry policy using the following steps:

  1. In the Google Cloud console, go to the **Pub/Sub subscriptions** page.



[Go to subscriptions](https://console.cloud.google.com/cloudpubsub/subscription)

  1. Click **Create subscription**.

  2. In the **Subscription ID** field, enter a name.




For information on how to name a subscription, see [Guidelines to name a topic or a subscription](https://docs.cloud.google.com/pubsub/docs/pubsub-basics#resource_names).

  1. Choose or create a topic from the drop-down menu.



The subscription receives messages from the topic.

  1. Select a **Delivery type**.

  2. Under **Retry policy** , select **Retry after exponential backoff**.

  3. Enter a **Minimum backoff** and **Maximum backoff** between 0 and 600 seconds.




The default values are 10 seconds for minimum backoff, and 600 seconds for maximum backoff.

  1. Click **Create**.



### gcloud

To create a new subscription with an exponential backoff retry policy, run the following [`gcloud pubsub create`](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create) command.
    
    
    gcloud pubsub subscriptions create SUBSCRIPTION_ID \
      --topic=TOPIC_ID \
      --min-retry-delay=MIN_RETRY_DELAY \
      --max-retry-delay=MAX_RETRY_DELAY

Replace the following:

  * `SUBSCRIPTION_ID`: a unique ID for your subscription.
  * `TOPIC_ID`: the ID of the topic that you want to attach the subscription to.
  * `MIN_RETRY_DELAY`: the minimum backoff delay for the subscription.
  * `MAX_RETRY_DELAY`: the maximum backoff delay for the subscription.



## What's next

  * [Get the forwarded undeliverable messages](https://docs.cloud.google.com/pubsub/docs/pull-messages).
  * [Monitor Pub/Sub applications](https://docs.cloud.google.com/pubsub/docs/monitoring).
  * [Learn message delivery concepts](https://docs.cloud.google.com/pubsub/architecture#data_plane_-_the_life_of_a_message).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
