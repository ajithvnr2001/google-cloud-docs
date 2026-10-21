---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/assign-virtual-agents-to-queues/
title: Assign virtual agents to queues \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:20.098305+00:00
---

# Assign virtual agents to queues  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/assign-virtual-agents-to-queues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Assign virtual agents to queues Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to assign virtual agents to queues for the IVR, web, mobile, and SMS channels. Procedures for assigning chat virtual agents to queues and voice virtual agents to queues differ slightly.

You can assign a virtual agent to one or more queues. Google recommends assigning at least one human agent to any queue that has a virtual agent. This provides a direct escalation path to a human agent in the case of a virtual agent failure or a service interruption.

## Assign a chat virtual agent to a queue

The web, mobile chat, and SMS channels use chat virtual agents.

To assign a chat virtual agent to a queue:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**. The **Queue Menu Settings** page appears.

  2. Do one of the following, depending on the channel that you created your virtual agent for:

     * In the **Web** pane, click **Edit / View**.

     * In the **Mobile** pane, click **Edit / View**.

     * In the **SMS Messaging** pane, click **Edit / View**.

  3. Click the queue that you want to assign a virtual agent to.

  4. For **Channel Settings** , in the **Virtual Agent Chat** row, click **Assign Virtual Agent**.

  5. In the **Virtual Agent** list, select a chat virtual agent that you created in [Create virtual agents](https://docs.cloud.google.com/contact-center/ccai-platform/docs/create-virtual-agents). Only virtual agents that you turn on appear in this list.

  6. For **Hours of Operation** , select one of the following:

     * **24 Hours** : The virtual agent is available at any time. When there are no human agents available, escalations aren't possible.

     * **Queue hours** : The virtual agent is available only during the hours of operation for the queue. For more information, see [Hours of operation settings](https://docs.cloud.google.com/contact-center/ccai-platform/docs/hours-of-operation#hours-of-operation-settings).

  7. For web and mobile chat only: To display a button that lets end-users connect directly with a human agent, select the **Display Skip to human agent button** checkbox.

  8. For web and mobile chat only: To route high-priority users directly to human agents and skip the virtual agent, do the following:

     1. Set up [Priority user segments](https://docs.cloud.google.com/contact-center/ccai-platform/docs/priority-sgements) in your CRM.

     2. Click the **Exclude users from Virtual Agent workflow** toggle to the on position.

     3. In the **CRM Custom User Segment Field** list, select a field.

     4. In the **CRM Custom User Segment Value** field, enter a value.

End-users who belong to the specified user segment are routed directly to a human agent.

  9. To add data parameters, do the following:

     1. Click the **Pass Data Parameters** toggle to the on position.

     2. Click **Add Parameter**. The **Add Parameter** dialog appears.

     3. Fill in the fields according to the instructions in [Pass data parameters to Virtual Agents and Virtual Task Assistants](https://docs.cloud.google.com/contact-center/ccai-platform/docs/pass-data-parameters#data-parameters-to-vas-and-virtual-task-assistants), and then click **Save**.

     4. To add more data parameters, click **Add Parameter** , and then repeat these steps.

     5. To configure whether the data parameters are included in metadata files or CRM records, for **Data Records** , select or clear the checkboxes.

  10. Click **Save**.

  11. Click **Back to Settings** , and then select the **Virtual Agent Chat** checkbox. This lets incoming SMS sessions be routed to the virtual agent.




## Assign a voice virtual agent to a queue

The IVR and mobile voice channels use voice virtual agents.

To assign a voice virtual agent to a queue, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**. The **Queue Menu Settings** page appears.

  2. Do one of the following, depending on the channel that you created your virtual agent for:

     * In the **IVR (Interactive Voice Response)** pane, click **Edit / View**.

     * In the **Mobile** pane, click **Edit / View**.

  3. Click the queue that you want to assign a virtual agent to.

  4. For **Channel Settings** , in the **Virtual Agent** row, click **Assign Virtual Agent**.

  5. In the **Virtual Agent** list, select a voice virtual agent that you created in [Create virtual agents](https://docs.cloud.google.com/contact-center/ccai-platform/docs/create-virtual-agents). Only virtual agents that you turn on appear in this list.

  6. For **Hours of Operation** , select one of the following:

     * **24 Hours** : The virtual agent is available at any time. When there are no human agents available, escalations aren't possible.

     * **Queue hours** : The virtual agent is available only during the hours of operation for the queue. For more information, see [Hours of operation settings](https://docs.cloud.google.com/contact-center/ccai-platform/docs/hours-of-operation#hours-of-operation-settings).

  7. For IVR only: To set a keypad hot key that lets end-users connect directly with a human agent, do the following:

     1. Select the **Allow end user to skip virtual agent** checkbox.

     2. In the **Hot key option** list, select a hot key.

  8. Mobile voice only: To display a button that lets end-users connect directly with a human agent, select the **Display Skip to human agent button** checkbox.

  9. To add data parameters, do the following:

     1. Click the **Pass Data Parameters** toggle to the on position.

     2. Click **Add Parameter**. The **Add Parameter** dialog appears.

     3. Fill in the fields according to the instructions in [Pass data parameters to Virtual Agents and Virtual Task Assistants](https://docs.cloud.google.com/contact-center/ccai-platform/docs/pass-data-parameters#data-parameters-to-vas-and-virtual-task-assistants), and then click **Save**.

     4. To add more data parameters, click **Add Parameter** , and then repeat these steps.

     5. To configure whether the data parameters are included in metadata files or CRM records, for **Data Records** , select or clear the checkboxes.

  10. Click **Save**.

  11. Click **Back to Settings** , and then select the **Virtual Agent** checkbox. This lets incoming SMS sessions to be routed to the virtual agent.




## Assign voice virtual agent transfers to top-level queues

To enable this capability, make sure that the top-level queue ID is entered as the destination in Dialogflow CX. You can find queue IDs in the **Settings > Queue** menu. Make sure that any required leaf queues are active.

In the IVR, the end-user hears all the sub queue and leaf queue options under the top-level. If a top-level queue doesn't have active sub queues or leaf queues or is configured incorrectly, the [IVR Fallback](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Queue_and_Menu_Setup#custom-fallback-ivr-at-queue-level) mechanism takes action. It either redirects the caller to the previous queue (if human agents are available) or it conveys an error message before disconnecting the call (if the escalating queue lacks human agents).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
