---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/restrict-queue-transfers/
title: Restrict queue transfers \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:12.435164+00:00
---

# Restrict queue transfers  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/restrict-queue-transfers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Restrict queue transfers Stay organized with collections  Save and categorize content based on your preferences. 

CCAI Platform lets you restrict the queues and teams that can transfer a session, and the queues and teams that can receive a transferred session. This lets you control the ability of agents to transfer sessions and receive transferred sessions based on the queues or teams that they belong to. You can configure transfer restrictions for IVR sessions, mobile call and chat sessions, and web chat sessions.

## Configure queue transfer restrictions

You can configure transfer restrictions based on the queues that agents belong to.

To configure queue transfer restrictions, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Depending on the channel that you want, do one of the following:

     * In the **IVR (Interactive Voice Response)** pane, click **Edit / View**.

     * In the **Mobile** pane, click **Edit / View**.

     * In the **Web** pane, click **Edit / View**.

  3. Click the queue that you want to edit.

  4. In the **Settings** pane, next to **Transfer Restrictions** , click **Configure**.

  5. Click the **Transfer Restrictions** toggle to the on position.

  6. To configure incoming transfers, click one of the following:

     * **All queues** : this allows transfers into this queue from any other queue. Agents can receive transfers from any queue.

     * **No queues** : this prevents transfers into this queue from any other queue. Agents won't receive transfers from other queues.

  7. To configure outgoing transfers, click **Allow transfers from this queue to** , and then click one of the following:

     * **All queues** : this allows transfers from this queue into any other queue. Agents can transfer calls into any other queue.

     * **No queues** : this prevents transfers from this queue into any other queue. Agents can't transfer into other queues.

     * **Selected queues** : this allows transfers from this queue into only the queues that you specify. Agents can transfer only to specified queues. After clicking this, do the following:

       1. Click the **Search or select queue** field. A list of queues appears. To narrow your search, type the first few letters of the queue that you want.

       2. Click a queue that you want to allow transfers into.

       3. Optional: Select the **Link selected queues from other languages** checkbox to include queues for associated languages (for queues with multiple languages). For more information, see [Enabling multiple languages for IVR, mobile, and web channels](https://docs.cloud.google.com/contact-center/ccai-platform/docs/enable-multiple-languages).

       4. Click **Add Queue**. A queue appears in the **Transfer allowed to** list for each agent type that is associated with the queue that you specified. If you selected the **Link selected queues from other languages** checkbox, a queue also appears for each language that is associated with the queue.

       5. Optional: Deselect any queues that you don't want to allow transfers to.

       6. To select additional queues to transfer into, repeat these steps.

  8. To prevent transfers within this queue, click the **Do not allow transfers within the same queue** toggle to the on position.

  9. Click **Save**.




## Configure team transfer restrictions

You can configure transfer restrictions based on the teams that agents belong to.

To configure team transfer restrictions, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Users and Teams**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Do one of the following:

     * To create a new team, do the following:

       1. For **Teams** , click **Add a Team**. The **Add Team** dialog appears.

       2. Configure the settings in the dialog as shown in [Add, view, and edit teams](https://docs.cloud.google.com/contact-center/ccai-platform/docs/add-configure-teams).

     * To edit an existing team, do the following:

       * For **Teams** , next to the team that you want to edit, click edit **Edit**. The **Edit Team** dialog appears.
  3. Go to **Transfer restriction**.

  4. To configure incoming transfers, click one of the following:

     * **All teams** : this allows transfers to this team from any other team. Agents can receive transfers from any team.

     * **No teams** : this prevents transfers to this team from any other team. Agents won't receive transfers from other teams.

  5. To configure outgoing transfers, click **Allow transfers from this team to** , and then click one of the following:

     * **All teams** : this allows transfers from this team to any other team. Agents can transfer calls to any other team.

     * **No teams** : this prevents transfers from this team to any other team. Agents can't transfer to other teams.

     * **Selected teams** : this allows transfers from this team to only the teams that you specify. Agents can transfer only to specified teams. After clicking this, do the following:

       1. Click the **Search or select team** field. A list of teams appears. To narrow your search, type the first few letters of the team that you want.

       2. Click a team that you want to allow transfers to.

       3. Click **Add Team**. A team appears in the **Transfer allowed to** list for each role that is associated with the team that you specified.

       4. Optional: Deselect any teams that you don't want to allow transfers to.

       5. To select additional teams to transfer into, repeat these steps.

  6. To prevent transfers within this team, click the **Do not allow transfers within the same team** toggle to the on position.

  7. Click **Save**.




## Configuration inheritance

When you configure transfer restrictions for a queue, all subordinate queues inherit the configuration. You can click any subordinate queue and change its configuration so it no longer matches its parent. You can reset the configuration of a subordinate queue to match its parent at any time.

To reset the transfer configuration of a subordinate queue to match its parent, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Depending on the channel that you want, do one of the following:

     * In the **IVR (Interactive Voice Response)** pane, click **Edit / View**.

     * In the **Mobile** pane, click **Edit / View**.

     * In the **Web** pane, click **Edit / View**.

  3. Click the subordinate queue that you want to reset.

  4. Click **Reset to parent** , and then click **Save**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
