---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-configure-announcements/
title: Configure announcements \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:41.199826+00:00
---

# Configure announcements  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-configure-announcements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Configure announcements Stay organized with collections  Save and categorize content based on your preferences. 

With announcements, you can communicate updates, alerts, and other important information directly to agents. Announcements appear in the agent desktop as notification banners that persist until the agent dismisses them. Announcements also appear in the agent's announcement list. For more information, see [Announcements](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-use-agent-desktop#announcements).

There are two types of announcements:

  * **One-time** : For one-time announcements, notification banners appear only once. An agent can remove one-time announcements from their announcement list.

  * **Persistent**. For persistent announcements, notification banners reappear every time an agent signs into the agent desktop. An agent can't remove persistent announcements from their announcement list.




You schedule announcements to be active during a specific timeframe. Outside of that timeframe, announcements are inactive. Inactive announcements don't display notification banners and don't appear in an agent's announcement list.

You can add translations of announcement titles and messages. If a translation is not available for an agent's specified language, English is displayed by default.

## Create an announcement

To create an announcement, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Announcements** pane, and then click **Manage announcements**. The **Announcements** page appears.

  3. Click **Create announcement**. The **Create announcement** pane appears.

  4. In the **Internal label** field, enter a label for your announcement. This label identifies announcements when you view or edit them, but it's not visible to agents.

  5. In the **Title (English US)** field, enter a title for your message in English.

  6. In the **Message (English US)** field, enter your message in English.

**Note:** You must have either a title or a message (or both) in your announcement.
  7. To add a translation, do the following:

     1. Click **Add Translation**. The **Add a translation** pane appears.

     2. Click the **Language** field, and then click the language for your translation.

     3. In the **Title** field, enter the title of your message in the translation language.

     4. In the **Message** field, enter your message in the translation language.

**Note:** You must have either a title or a message (or both) in your translation.
     5. Click **Add**.

  8. To add another translation, click **Add Translation** and repeat these steps with a different language.

  9. To set the announcement schedule, which determines the timeframe that the announcement is active, do the following:

     1. Click the **Time Zone** field, and then click the time zone for your schedule.

     2. In the **Start date and time** fields, enter the start date and start time in the indicated format.

     3. In the **End date and time** fields, enter the end date and end time in the indicated format.

     4. Optional: Click the **All day** checkbox to use a start date and an end date with no start time and end time. The time fields return to `00:00`.

  10. For **Notify** , specify whether the announcement is one-time or persistent. Persistent notification banners reappear every time an agent signs into the agent desktop. One-time notification banners appear only once.

  11. To specify which agents receive the announcement, do the following:

     1. To specify that all agents receive the announcement, select the **All agents** checkbox.

     2. To specify that agents assigned to certain queues receive the announcement, make sure that the **All agents** checkbox is cleared, and then do the following:

        1. Select the **Select Queues** checkbox. A field appears.

        2. In the field, type part of the queue name. Matching queues appear.

        3. Select the queue that you want.

        4. To select additional queues, repeat these steps.

     3. To specify that agents assigned to certain teams receive the announcement, follow a similar process using the **Select Teams** checkbox.

     4. To specify that certain agents receive the announcement, follow a similar process using the **Select Agents** checkbox.

**Note:** If an announcement is assigned to an agent in multiple ways (for example, by the queue and the team that the agent is assigned to), the agent doesn't receive extra notification banners.
  12. Click **Save**.




## Edit an announcement

You can edit an announcement. Be aware that making the following edits to an announcement can cause it to be resent:

  * Edit the title or message.

  * Edit the schedule of an expired announcement so that it becomes active.

  * Change an announcement from one-time to persistent.

  * Add a new assignment.




To edit an announcement, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Announcements** pane, and then click **Manage announcements**. The **Announcements** page appears.

  3. Do one of the following:

     * To edit an active announcement, click **Active**.

     * To edit an expired announcement, click **Expired**.

  4. For the announcement you want to edit, click more_horiz **More** , and then click **Edit announcement**. The **Edit announcement** pane appears.

  5. Make your changes to the announcement, and then click **Save**.




## Delete an announcement

To delete an announcement, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Announcements** pane, and then click **Manage announcements**. The **Announcements** page appears.

  3. Do one of the following:

     * To delete an active announcement, click **Active**.

     * To delete an expired announcement, click **Expired**.

  4. For the announcement you want to delete, click more_horiz **More** , and then click **Delete announcement**.

  5. In the confirmation dialog, click **Delete**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
