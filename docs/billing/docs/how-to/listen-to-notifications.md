---
url: https://docs.cloud.google.com/billing/docs/how-to/listen-to-notifications/
title: Listen to your Pub/Sub notifications \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:40.846301+00:00
---

# Listen to your Pub/Sub notifications  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/listen-to-notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Listen to your Pub/Sub notifications Stay organized with collections  Save and categorize content based on your preferences. 

Example reference architecture

![Diagram of an example using budget alert programmatic notifications
            to automate a cost control response.](https://docs.cloud.google.com/static/billing/docs/images/budget-alert-diagram-pubsub2.png)**Figure 1** : An example of using budget alerts to automate cost control responses using Pub/Sub for programmatic notifications and Cloud Run functions to automate a response. 

This document explains how to listen to your programmatic budget notifications by subscribing to your Pub/Sub topic with [Cloud Run function](https://docs.cloud.google.com/functions/docs/concepts/events-triggers) triggers. Without a subscriber, Pub/Sub drops published messages and you can't retrieve them later. In this document, you'll learn how to complete the following tasks:

  1. Create a Cloud Run function that listens to notifications.
  2. View Cloud Run function events.
  3. Test a Cloud Run function.

**Note:** Although there are many ways you can [subscribe to your topic](https://docs.cloud.google.com/pubsub/docs/subscriber), the examples on this page use [Cloud Run functions](https://docs.cloud.google.com/functions/docs). Cloud Run functions lets you create functions that respond to cloud events without needing to manage a server or runtime environment.

## Before you begin

Before you begin, you must complete the following tasks:

  1. [Create a budget](https://docs.cloud.google.com/billing/docs/how-to/budgets)
  2. [Set up programmatic notifications](https://docs.cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications)



## Create a Cloud Run function

To create a Cloud Run function, complete the following steps:

  1. In the Google Cloud console, go to the **Cloud Run functions** page.

[Go to Cloud Run functions](https://console.cloud.google.com/functions)

  2. Click **Write a function**.

  3. Select **Use an inline editor to create a function**.

  4. Enter a **Service name** that's meaningful to your budget notification.

  5. Select the [region](https://docs.cloud.google.com/functions/docs/locations) where your Cloud Run functions will run. You can't edit this setting after you deploy your function.

  6. Click **Add trigger** and select **Cloud Pub/Sub**.

  7. If prompted, enable any required APIs.

  8. In the **Eventarc trigger** panel, complete the following steps:

     1. Enter a **Trigger name**.
     2. Set **Trigger type** to **Google sources**.
     3. Set **Event provider** to **Cloud Pub/Sub**.
     4. Select the **Cloud Pub/Sub topic** that you configured on your budget.
     5. Select a **Region**.
     6. Click **Save trigger**.
  9. Edit the **Identity-Aware Proxy** , **Billing** , **Service scaling** , **Ingress** , and **Container(s), Volume, Networking, Security** settings as needed, then click **Create**.

  10. Write code using the inline editor or upload a file that tells your function how to handle notifications.

See the following examples for code samples:

     * [Send notifications to Slack](https://docs.cloud.google.com/billing/docs/how-to/send-notifications-to-slack)
     * [Control resource usage with notifications](https://docs.cloud.google.com/billing/docs/how-to/control-usage)
     * [Disable billing usage with notifications](https://docs.cloud.google.com/billing/docs/how-to/disable-billing-with-notifications)

For details about the notifications your code will receive, see [Notification format](https://docs.cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications#notification-format).

  11. Set **Function entry point** to the correct function to execute:

  12. Click **DEPLOY**.




## View Cloud Run function events

After you deploy the Cloud Run function, click **LOGS** to view the logs from your function invocations.

## Test a Cloud Run function

As notifications are sent to Pub/Sub, subscribers receive the messages. To test a sample notification and ensure that your function is working as expected, [publish a message in Pub/Sub](https://docs.cloud.google.com/pubsub/docs/publisher) with the following object as the message body:
    
    
    {
        "budgetDisplayName": "name-of-budget",
        "alertThresholdExceeded": 1.0,
        "costAmount": 100.01,
        "costIntervalStart": "2019-01-01T00:00:00Z",
        "budgetAmount": 100.00,
        "budgetAmountType": "SPECIFIED_AMOUNT",
        "currencyCode": "USD"
    }
    

You can also add message attributes such as the billing account ID. For more information, see [Notification format](https://docs.cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications#notification-format).

## What's next

To learn more about how you can use programmatic notifications, review the following examples of programmatic cost control responses:

  * [Send notifications to Slack](https://docs.cloud.google.com/billing/docs/how-to/send-notifications-to-slack)
  * [Control resource usage with notifications](https://docs.cloud.google.com/billing/docs/how-to/control-usage)
  * [Disable billing usage with notifications](https://docs.cloud.google.com/billing/docs/how-to/disable-billing-with-notifications)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
