---
url: https://docs.cloud.google.com/pubsub/docs/subscription-message-retention/
title: Configure message retention for a subscription \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:46:06.402243+00:00
---

# Configure message retention for a subscription  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/subscription-message-retention/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Configure message retention for a subscription Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how a Pub/Sub subscription retains published messages and how to configure this behavior. You might change the default settings for the following reasons:

  * To adjust how long unacknowledged messages remain available to a subscription before they are deleted.
  * To enable replaying previously-acknowledged messages.



## Overview

When you create a subscription, Pub/Sub begins retaining published messages on behalf of the subscription. By default, Pub/Sub discards a message from a subscription as soon as the message is acknowledged, and retains unacknowledged messages for 7 days.

You can set the retention duration when you create or update the subscription. The minimum retention duration is 10 minutes, and the maximum is 31 days.

You can also enable the subscription to retain _acknowledged_ messages, up to the configured retention duration. Retaining acknowledged messages lets you replay previously-acknowledged messages for as long as they are retained. For more information about replaying messages, see [Replay and purge messages with seek](https://docs.cloud.google.com/pubsub/docs/replay-overview).

If a subscription is configured to retain acknowledged messages, storage costs for the acknowledged messages retained by the subscription are billed to the subscription's project.

If you also enable message retention on the subscription's topic, then messages are deleted from the subscription only when their age exceeds the maximum of the subscription retention and topic retention durations. For more information, see [Enable topic message retention](https://docs.cloud.google.com/pubsub/docs/create-topic#enable_message_retention).

## Configure message retention

To create a subscription that retains acknowledged messages, perform the following steps:

### Console

  1. In the Google Cloud console, go to the **Pub/Sub subscriptions** page.

[Go to the subscriptions page](https://console.cloud.google.com/cloudpubsub/subscription)

  2. Click **Create subscription**.

  3. In the **Subscription ID** field, enter an ID for your subscription.

  4. In the **Message retention duration** section, select the number of days, hours, and minutes to retain messages.

  5. Select the **Retain acknowledged messages** checkbox.

  6. Click **Create subscription**.




### gcloud

Use the [`gcloud pubsub subscriptions create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create):
    
    
    gcloud pubsub subscriptions create SUBSCRIPTION_ID \
      --message-retention-duration=5d \
      --retain-acked-messages
    

Replace `SUBSCRIPTION_ID` with the ID of the subscription.

If you omit the `--message-retention-duration` flag, messages are retained for the default duration of 7 days.

To update the message retention settings on an existing subscription, perform the following steps:

### Console

  1. Select your subscription from the **Pub/Sub subscriptions** page.

[Go to the subscriptions page](https://console.cloud.google.com/cloudpubsub/subscription)

  2. Click **Edit** at the top of the subscription details page.

  3. In the **Message retention duration** section, update the number of days, hours, and minutes to retain messages.

  4. Select or clear the **Retain acknowledged messages** checkbox.

  5. Click **Update** to save the changes to the subscription.




### gcloud

Use the [`gcloud pubsub subscriptions update`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update) command:
    
    
    gcloud pubsub subscriptions update SUBSCRIPTION_ID \
      --message-retention-duration=1d \
      --retain-acked-messages
    

To disable retention of acknowledged messages, use the `update` command with the `--no-retain-acked-messages` flag:
    
    
    gcloud pubsub subscriptions update SUBSCRIPTION_ID \
      --no-retain-acked-messages
    

**Note:** When you modify either the message retention duration or subscription expiration policy, the expiration period must be set to a value greater than the message retention duration. The default message retention duration is 7 days and the default expiration period is 31 days.

## What's next

  * [Subscription overview](https://docs.cloud.google.com/pubsub/docs/subscription-overview)
  * [Replay and purge messages with seek](https://docs.cloud.google.com/pubsub/docs/replay-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
