---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-capture-record-id/
title: Get the record ID in Dialogflow \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:21.415398+00:00
---

# Get the record ID in Dialogflow  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-capture-record-id/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Get the record ID in Dialogflow Stay organized with collections  Save and categorize content based on your preferences. 

During a virtual agent interaction, you might need to capture the CRM record ID to manage webhooks to the CRM. This page explains how to do that.

## Before you begin

Before you can assign chat or call records to a default user, you need to set a default user for your CRM. For more information, see [CRM default administrator user](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-default-admin).

## Configure the assignment of chat or call records created by a virtual agent

To configure the assignment of chat or call records created by a virtual agent, follow these steps:

  1. In the (CCAI Platform) portal, click **Settings > Operation Management**. If you don't see the settings menu, click menu**Menu** , and then click **Settings > Operation Management**.
  2. Go to the **Virtual Agent > Customer support agents** pane.
  3. To assign call records, under **Calls** , select one of the following options. Some options are not available with some CRM types. 
     * **Assign to a default user**. Call records created by a virtual agent are assigned to the default user. If this setting appears but is inactive, set the default user for your CRM to activate the setting. For more information, see [CRM default administrator user](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-default-admin).
     * **Leave unassigned**. Call records created by a virtual agent are left unassigned.
     * **Assign to a specific user**. Call records created by a virtual agent are assigned to a user that you specify. If you select this option, enter a user ID, and then click **Validate**.
  4. To assign chat records, under **Chats** , select one of the following options. Some options are not available with some CRM types. 
     * **Assign to a default user**. Chat records created by a virtual agent are assigned to the default user. If this setting appears but is inactive, set the default user for your CRM to activate the setting. For more information, see [CRM default administrator user](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-default-admin).
     * **Leave unassigned**. Chat records created by a virtual agent are left unassigned.
     * **Assign to a specific user**. Chat records created by a virtual agent are assigned to a user that you specify. If you select this option, enter a user ID, and then click **Validate**.
  5. Click **Save Changes**.



## Create a webhook

To create a webhook, follow these steps:

  1. In Dialogflow CX, create a flexible webhook with a method type of `GET`. For more information, see [Flexible webhooks](https://cloud.google.com/dialogflow/cx/docs/concept/webhook#flexible).
  2. In the webhook URL, enter the following:
         
         https://YOUR_CCAAS_HOST/manager/api/v1/$session.params.channel?id[]=$session.params.id
         

  3. In the webhook response configuration, map your selected Dialogflow CX parameter to the `[0].out_ticket_id` field path.

  4. Place the webhook in your virtual agent in a position where you need to retrieve the record ID.




Google recommends that you don't put this webhook on your initial start page. This could cause increased latency in creating the ticket.

## Pass data parameters

When assigning the virtual agent to a queue, set up the following parameters to be sent:

  1. From session metadata, set parameter `id` to **Call ID** for IVR queues or **Chat ID** for chat queues.
  2. Set parameter `channel` to the fixed value `"calls"` for IVR queues or `"chats"` for chat queues. Alternatively, you can omit the `channel` parameter and use separate webhooks for calls and chats.



For more information on passing data parameters, see [Pass data parameters](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-pass-data-parameters).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
