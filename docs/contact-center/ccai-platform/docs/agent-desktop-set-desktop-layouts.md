---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-set-desktop-layouts/
title: Configure desktop layouts for agents \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:30.670229+00:00
---

# Configure desktop layouts for agents  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-set-desktop-layouts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Configure desktop layouts for agents Stay organized with collections  Save and categorize content based on your preferences. 

You can configure which [desktop layout](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-create-desktop-layouts) that agents see when they answer an inbound call, place an outbound call, or handle a chat. You can configure this globally, at the queue level, and at the team level. Queue-level layout settings take priority over global settings. Team-level settings take priority over both queue-level settings and default settings. For more information, see [Create desktop layouts](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-create-desktop-layouts).

## Configure desktop layouts globally

You can configure desktop layouts globally for agents receiving inbound calls, placing outbound calls, and handling messages.

To configure desktop layouts globally, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Agent Desktop** page.

  3. For **Desktop Layout** , select a layout from each of the following fields:

     * **Default inbound voice layout** : sets the layout for receiving inbound calls

     * **Default outbound voice layout** : sets the layout for placing outbound calls

     * **Default messaging layout** : sets the layout for handling chats

  4. Click **Save Agent Desktop**. A confirmation dialog appears.

  5. Click **Save**.




## Configure desktop layouts at the queue level

You can configure desktop layouts at the queue level for agents receiving inbound calls and handling messages (mobile and web only). There is no queue-level option for setting layouts for placing outbound calls.

Desktop layout settings at the queue level take priority over global settings. For more information, see Configure desktop layouts globally.

To configure desktop layouts at the queue level, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Depending on the channel you want, do one of the following:

     * In the **IVR (Interactive Voice Response)** pane, click **Edit > View**.

     * In the **Mobile** pane, click **Edit / View**.

     * In the **Web** pane, click **Edit / View**.

     * In the **SMS Messaging** pane, click **Edit / View**.

     * In the **WhatsApp** pane, click **Edit / View**.

  3. Click the queue that you want to edit.

  4. In the **Settings** pane, for **Agent Desktop Layout** , click **Configure**. The **Agent Desktop Layout** pane appears. For **Desktop Layout List** , one or both of the following fields appears, depending on the channel:

     * **Default inbound voice layout** : sets the layout for receiving inbound calls (IVR, web, and mobile only)

     * **Default messaging layout** : sets the layout for handling chats (web, mobile, SMS, and WhatsApp only)

  5. Click the available field(s) to select the layout for the session type.

  6. Click **Save**.




## Configure desktop layouts at the team level

You can configure desktop layouts at the team level for agents receiving inbound calls, placing outbound calls, and handling messages.

Desktop layout settings at the team level take priority over queue-level settings and global settings. For more information, see Configure desktop layouts at the queue level and Configure desktop layouts globally.

To configure desktop layouts at the team level, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Users & Teams**. If you don't see the **Settings** menu, click menu **Menu**.

  2. For the team that you want to edit, click edit **Edit**. The **Edit Team** dialog appears.

  3. For **Agent Desktop Layout** , click expand_more to see the layout options.

  4. For **Agent desktop layout list** , select a layout from each of the following fields:

     * **Default inbound voice layout** : sets the layout for receiving inbound calls

     * **Default outbound voice layout** : sets the layout for placing outbound calls

     * **Default messaging layout** : sets the layout for handling chats

  5. Click **Save**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
