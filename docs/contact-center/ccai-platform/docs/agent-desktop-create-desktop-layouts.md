---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-create-desktop-layouts/
title: Create desktop layouts \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:39.734258+00:00
---

# Create desktop layouts  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-create-desktop-layouts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Create desktop layouts Stay organized with collections  Save and categorize content based on your preferences. 

With agent desktop, you can create customized desktop layouts for different use cases for your human agents. These include receiving inbound calls, placing outbound calls, handling chat sessions, and handling email sessions. Your layouts can contain call adapters, chat adapters, email adapters, and a wide variety of panels for other capabilities such as live transcripts, knowledge assist, and session data feeds. You can also [configure custom panels](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-configure-widgets) to use as widgets that you can drag into panels.

After you create a desktop layout, you can configure which layouts agents see, depending on session type and other factors. These factors include team membership and which queue a session arrives in. For more information, see [Set desktop layouts for agents](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-set-desktop-layouts).

## Create a desktop layout

To create a desktop layout, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Agent Desktop** pane.

  3. For **Desktop Layout** , click **Manage Desktop Layout Lists**. The **Desktop Layout Builder** page appears.

  4. Click **Add desktop layout**. The **Add desktop layout** dialog appears.

  5. In the **Desktop Layout Name** field, enter a name for your desktop layout.

  6. Optional: For **Panel Size Control** , clear the **Allow Agents To Control Size of Panels** checkbox if you don't want agents to change the panel sizes.

  7. Do one of the following:

     * To create a desktop layout for handling calls (and, optionally, chats or emails too), do the following:

       1. For **Channel** , select **Call Adapter**.

       2. Click **Next**. The **Desktop Layout Builder** page appears.

       3. To use an external call adapter, select the **External** checkbox.

       4. To display a chat adapter, select the **Chat Adapter** checkbox.

       5. To display an email adapter, select the **Email Adapter** checkbox.

       6. To customize the number and size of the panels, do any of the following:

          * Click ![Click to split a pane](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-agent-desktop-split-panel.png)**Split panel** to split a panel.

          * Click close **Close this panel** to close a panel.

          * Drag lines between panels to resize the panels.

       7. Drag a widget into a panel. For widgets that require Agent Assist, be sure to [set up Agent Assist](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-assist#set-up-agent-assist).

       8. Continue dragging widgets into panels until every panel has a widget. Drag the **Session Data Feed** widget into a panel if you want to capture data about sessions for later analysis. For more information, see [Session data feed](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-session-data-feed).

       9. Click **Save**. Your new layout appears in the **Desktop Layout** list.

     * To create a desktop layout exclusively for handling chats or emails, do the following:

       1. For **Channel** , select **Chat Adapter** or **Email Adapter** , depending on the type of session the layout is for.

       2. Click **Next**. The **Desktop Layout Builder** page appears.

       3. To customize the number and size of the panels, do any of the following:

          * Click ![Click to split a pane](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-agent-desktop-split-panel.png)**Split panel** to split a panel.

          * Click close **Close this panel** to close a panel.

          * Drag lines between panels to resize the panels.

       4. Drag a widget into a panel. For widgets that require Agent Assist, be sure to [set up Agent Assist](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-assist#set-up-agent-assist).

       5. Continue dragging widgets into panels until every panel has a widget. Drag the **Session Data Feed** widget into a panel if you want to capture data about sessions for later analysis. For more information, see [Session data feed](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-session-data-feed).

       6. Click **Save**. Your new layout appears in the **Desktop Layout** list.




## Edit a desktop layout

To edit a desktop layout, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Agent Desktop** pane.

  3. For **Desktop Layout** , click **Manage Desktop Layout Lists**. The **Desktop Layout Builder** page appears.

  4. For the desktop layout that you want to edit, click more_horiz **More** , and then click **Edit Layout**. The **Desktop Layout Builder** page appears.

  5. Make changes to the layout, and then click **Save**.




## Duplicate a desktop layout

To duplicate a desktop layout, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Agent Desktop** pane.

  3. For **Desktop Layout** , click **Manage Desktop Layout Lists**. The **Desktop Layout Builder** page appears.

  4. For the desktop layout that you want to duplicate, click more_horiz **More** , and then click **Duplicate**. A duplicate desktop layout appears.




## Rename a desktop layout

To rename a desktop layout, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Agent Desktop** pane.

  3. For **Desktop Layout** , click **Manage Desktop Layout Lists**. The **Desktop Layout Builder** page appears.

  4. For the desktop layout that you want to rename, click more_horiz **More** , and then click **Edit Layout Setting**. The **Edit desktop layout** dialog appears.

  5. In the **Desktop layout name** field, enter a new name.

  6. Optional: To change whether agents can control the size of panels, select or clear the **Allow agents to control size of panels** checkbox.

  7. Click **Save**.




## Delete a desktop layout

To delete a desktop layout, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Agent Desktop** pane.

  3. For **Desktop Layout** , click **Manage Desktop Layout Lists**. The **Desktop Layout Builder** page appears.

  4. For the desktop layout that you want to delete, click more_horiz **More** , and then click **Delete**. The **Delete layout** dialog appears.

  5. Click **Delete**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
