---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/outbound-sms-messaging/
title: Bulk SMS messaging \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:54:15.931325+00:00
---

# Bulk SMS messaging  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/outbound-sms-messaging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)



Send feedback 

#  Bulk SMS messaging Stay organized with collections  Save and categorize content based on your preferences. 

With Contact Center AI Platform, you can send an SMS message to a list of end-user phone numbers in a CSV file. Two possible use cases for a bulk outbound SMS are real-time notifications and marketing promotions.

An end-user can respond to the message and initiate a support session with an agent.

### Permissions

To send bulk SMS messages, your user must be assigned a role with the `Campaigns Manager` permission—for example, the Admin role. For more information, see [User roles and permissions](https://docs.cloud.google.com/contact-center/ccai-platform/docs/user-roles-permissions).

## Send bulk SMS messages

To send bulk SMS messages, follow these steps:

  1. Create a CSV file containing the phone numbers that you want to include in your bulk outbound SMS messaging. This file must include a `Phone number` column containing the phone numbers to send SMS messages to. All other columns are ignored.

  2. In the CCAI Platform portal, click **Settings > Campaigns**. If you don't see the **Settings** menu, click menu **Menu**.

  3. Click the **SMS** tab.

  4. For **Step 1: Upload CSV** , drag a CSV file into the field, or browse for the file.

  5. For **Step 2: Select an outbound phone number** , click the **Select a phone number** field, and then click the outbound phone number for your SMS messages.

  6. For **Step 3: Enter a message** , enter your message in the text field.

  7. Click **Send**. After your SMS messages are sent, the **Sending SMS is finished** dialog appears. An email is also sent to the user who sent the bulk SMS messages.

  8. Click **Send SMS** to return to the **Send SMS in bulk** dialog.




## End-user experience

If an end-user responds to the bulk SMS message, a support session begins with an agent. The agent and end-user can see the full chat history, including the original SMS message.

## Limit the time between bulk SMS messages

You can set the amount of time after a set of bulk SMS messages has been sent before the next set of bulk SMS messages can be sent. You can do this to limit the number of SMS messages that your end-users receive from you so they don't feel like you're sending them spam messages.

To limit the time between bulk SMS messages, do the following:

  1. In the CCAI Platform portal, click **Settings > Chat**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **SMS Expiration & Timeout Global Settings** pane.

  3. For **Queue selecting state Chat Expiration** , enter the number of minutes that you want. This is the amount of time that must expire after a set of bulk SMS messages has been sent before the next set of bulk SMS messages can be sent.

  4. Click **Save SMS Expiration and Timeout**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
