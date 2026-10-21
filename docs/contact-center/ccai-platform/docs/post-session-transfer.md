---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/post-session-transfer/
title: Post-session transfers \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:09.805702+00:00
---

# Post-session transfers  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/post-session-transfer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Post-session transfers Stay organized with collections  Save and categorize content based on your preferences. 

You can configure Contact Center AI Platform (CCAI Platform) to transfer call or chat sessions to a virtual agent when the session is ended by the agent or the end-user. You can configure your virtual agent to do post-session tasks like surveys or order status inquiries.

You must have a virtual agent configured for any channel that you configure for post-session transfers.

Post-session transfers are available for web SDK V3. They're not available for the mobile SDKs.

## Enable post-session transfers for chats globally

To enable post-session transfers for chats globally, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Chat**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Post-session Transfers** pane, and then click the toggle to the on position.

  3. For **Chat Type** , select the type of chat to transfer to a virtual agent.

  4. In the **Virtual Agent Name** field, click a virtual agent to receive the post-session transfer.

  5. To add data parameters, do the following:

     1. Click the **Data Parameters** toggle to the on position.

     2. Click **Add Parameter**. The **Add Parameter** dialog appears.

     3. Fill in the fields according to the instructions in [Pass data parameters to Virtual Agents and Virtual Task Assistants](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-pass-data-parameters#data-parameters-to-vas-and-virtual-task-assistants) , and then click **Save**.

     4. To add more data parameters, repeat these steps.

  6. For **Data Records** , use the checkboxes to determine whether the data parameters are added to the session metadata file, to CRM records, or both.

  7. Optional: Select the **Ask consumer to opt-in before the transfer** checkbox to let the end-user opt in or out of the session transfer.

  8. Click **Save**.




## Enable post-session transfers for calls globally

To enable post-session transfers for calls globally, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Call**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Post-session Transfers** pane, and then click the toggle to the on position.

  3. For the **Call Type** , select the type of call to transfer to a virtual agent.

  4. In the **Virtual Agent Name** field, click a virtual agent to receive the post-session transfer.

  5. To add data parameters, do the following:

     1. Click the **Data Parameters** toggle to the on position.

     2. Click **Add Parameter**. The **Add Parameter** dialog appears.

     3. Fill in the fields according to the instructions in [Pass data parameters to Virtual Agents and Virtual Task Assistants](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-pass-data-parameters#data-parameters-to-vas-and-virtual-task-assistants), and then click **Save**.

     4. Repeat to add any additional parameters.

  6. For **Data Records** , use the checkboxes to determine whether the data parameters are added to the session metadata file, to CRM records, or both.

  7. Click **Save**.




## Enable post-session transfers for chats at the queue level

Post session transfers are only available for chat sessions at the queue level.

To enable post-session transfers for chats at the queue level, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **Web** pane, click **Edit / View**.

  3. Click the queue that you want to edit.

  4. In the **Settings** pane, go to **Post-session Transfer** , and then click **Configure**.

  5. Click the **Chat Routing** toggle to the on position.

  6. In the **Virtual Agent Name** field, click a virtual agent to receive the post-session transfer.

  7. To add data parameters, do the following:

     1. Click the **Data Parameters** toggle to the on position.

     2. Click **Add Parameter**. The **Add Parameter** dialog appears.

     3. Fill in the fields according to the instructions in [Pass data parameters to Virtual Agents and Virtual Task Assistants](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-pass-data-parameters#data-parameters-to-vas-and-virtual-task-assistants), and then click **Save**.

     4. Repeat to add any additional parameters.

  8. For **Data Records** , use the checkboxes to determine whether the data parameters are added to the session metadata file, to CRM records, or both.

  9. Optional: Select the **Ask consumer to opt-in before the transfer** checkbox to let the end-user opt in or out of the session transfer.

  10. Click **Save**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
