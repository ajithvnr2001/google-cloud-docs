---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agents-with-crms/
title: Virtual agents with CRMs \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:33.420605+00:00
---

# Virtual agents with CRMs  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agents-with-crms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Virtual agents with CRMs Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to configure the behavior of CRMs with virtual agents.

## CRM integration configuration

The following setting only applies to the chat channel.

For sessions handled by virtual agents, the CRM behavior is set on the Operations Management page.

  1. Go to **Settings > Operation management > Virtual agent**

  2. Mark the checkbox, **Create CRM cases for chats attended by Virtual Agents** :

     * **All attended chats** : Each time an interaction is initiated by an end-user, a case is created in your CRM.

     * **Minimum chats** : Set the minimum chat message threshold. If the number of chats is less than this value, then a CRM case is not created. This can reduce the number of unnecessary cases.

  3. (Optional) Mark the checkbox **Close CRM cases when the chat session is resolved by a virtual agent.**

  4. To enable the gathering of a pre-configured metadata packet from your Web SDK when a chat is picked up by a virtual agent, mark the checkbox **Collect configured custom data in chat session.** The collected metadata is attached to the CRM ticket for that chat.

  5. Click **Save changes**.




## Configure the assignment of chat or call records created by virtual agents

When a CRM record is created by a virtual agent (VA) for a call or a chat, you can configure how the record is assigned. This capability is only available for Kustomer, Zendesk, Salesforce, MS Dynamics, and custom CRMs.

To configure the assignment of chat or call records created by a VA, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu** , and then click **Settings > Operation Management**.

  2. Go to the **Virtual Agent** pane.

  3. Do one of the following:

     * To assign chat records: under **Chats** , select one of the following options. Some options are not available with some CRM types.

       * **Assign to a default user** : chat records created by a VA are assigned to the default user. If you see this option but can't select it, you must set the default user for your CRM. For more information, see [CRM default admin user](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-mapping-settings#crm_default_admin_user).

       * **Leave unassigned** : chat records created by a VA are left unassigned.

       * **Assign to a specific user** : chat records created by a VA are assigned to a user that you specify. If you select this option, enter a user ID, and then click **Validate**.

     * To assign call records: under **Calls** , select one of the following options. Some options are not available with some CRM types.

       * **Assign to a default user** : call records created by a VA are assigned to the default user. If you see this option but can't select it, you must set the default user for your CRM. For more information, see [CRM default admin user](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-mapping-settings#crm_default_admin_user).

       * **Leave unassigned** : call records created by a VA are left unassigned.

       * **Assign to a specific user** : call records created by a VA are assigned to a user that you specify. If you select this option, enter a user ID, and then click **Validate**.

  4. Click **Save Changes**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
