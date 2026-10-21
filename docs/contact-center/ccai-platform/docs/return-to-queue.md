---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/return-to-queue/
title: Return to queue \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:09.223585+00:00
---

# Return to queue  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/return-to-queue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Return to queue Stay organized with collections  Save and categorize content based on your preferences. 

When a call is unexpectedly disconnected, the Return to queue capability gives end-users the option to return to the queue that they were in before the call started. If the queue is configured for first in first out (FIFO), the call goes to the front of the queue, to be connected by the next available agent. Otherwise, the call is prioritized so that it goes to the front or near the front of the queue.

There are two Return to queue workflows: the immediate offer workflow and the redial offer workflow. For more information, see Return to queue workflows.

The Return to queue capability is available only for IVR calls.

## Configure Return to queue globally

To configure Return to queue globally, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Call**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Call Details** pane.

  3. In the **Return to Queue After Disconnection** section, select the **Return consumer to the top of the same queue after disconnection** checkbox.

  4. In the **Call disconnection timeframe** field, enter the maximum call length where a call can be sent back to the queue after disconnection. A call that's longer than this can't be sent back to the queue. For a call that's shorter than the call disconnection timeframe, the end-user is offered the option to return to their queue in the following cases:

     * The call was disconnected by the agent. This is the immediate offer workflow.

     * The call was disconnected due to a network or system issue and the end-user calls back within the callback timeframe. This is the redial offer workflow.

  5. In the **Callback timeframe** field, enter the amount of time, after an end-user is disconnected due to a network or system issue, that they have to call back to be offered the option to return to the queue that they were in. An end-user who calls back after this amount of time can't be sent back to the queue.

  6. Optional: To prevent calls from specific phone numbers from being sent back to the queue, do the following:

     1. In the **Phone Number** field, enter a phone number, and then click **Add number**.

     2. To add more phone numbers to the list, repeat the previous step.

End-users who call from numbers on this list won't be offered the option to return to the queue that they were in.

**Note:** To remove a number from the list, click close **close icon**.
  7. Click **Save Call Details**.




## Configure Return to queue at the queue level

You can configure the Return to queue capability for one or more queues. This overrides the global setting for those queues. For example, you could set a longer callback timeframe for a high-priority support queue.

To configure Return to queue at the queue level, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **IVR (Interactive Voice Response)** pane, click **Edit / View**.

  3. Click the queue that you want to edit.

  4. In the **Settings** pane, for **Return to Queue after disconnection** , click **Configure**. The **Return to Queue after disconnection** dialog appears.

  5. Select the **Return consumer to the top of the same queue after disconnection** checkbox.

  6. In the **Call disconnection timeframe** field, enter the maximum call length where a call can be sent back to the queue after disconnection. A call that's longer than this can't be sent back to the queue. For a call that's shorter than the call disconnection timeframe, the end-user is offered the option to return to their queue in the following cases:

     * The call was disconnected by the agent. This is the immediate offer workflow.

     * The call was disconnected due to a network or system issue and the end-user calls back within the callback timeframe. This is the redial offer workflow.

  7. In the **Callback timeframe** field, enter the amount of time, after an end-user is disconnected due to a network or system issue, that they have to call back to be offered the option to return to the queue that they were in. An end-user who calls back after this amount of time can't be sent back to the queue.

  8. Click **Save**.




## Optional: Configure audible messages

By default, CCAI Platform is configured to read out text-to-speech messages to end-users when their calls are unexpectedly disconnected. You can edit the text of these text-to-speech messages, or you can upload a recording that plays instead.

To configure audible messages, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Languages & Messages**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Return to Queue After Disconnection Messages** section.

  3. To configure the **Return to queue confirmation** message, do one of the following. This message plays when the agent disconnects and the end-user is still on the call. This is the immediate offer workflow.

     * To change the text-to-speech message, edit the text in the text field. The system reads out the `@{QUEUE}` variable as the queue that the end-user came from.

     * To upload an audio recording to read out instead of using the text-to-speech message, click **Upload** and then upload a MP3 or WAV file with your message.

  4. To configure the **Return to queue confirmation on callback** message, do one of the following. When the call ends due to a network or system issue, this message plays if the end-user calls back within the callback timeframe. This is the redial offer workflow.

     * To change the text-to-speech message, edit the text in the text field. The system reads out the `@{QUEUE}` variable as the queue that the end-user came from.

     * To upload an audio recording to read out instead of using the text-to-speech message, click **Upload** and then upload a MP3 or WAV file with your message.

  5. Click **Save**.




## Return to queue workflows

There are two Return to queue workflows:

  * Immediate offer workflow

  * Redial offer workflow




### Immediate offer workflow

In the immediate offer workflow, the call is disconnected by the agent and the end-user stays on the call. For more information, see Configure Return to queue globally and Configure Return to queue at the queue level.

Here's the immediate offer workflow:

  1. A call is disconnected by an agent within the call disconnection timeframe and the end-user stays on the call. If a call is disconnected beyond the disconnection timeframe, the call can't be returned to the queue.

  2. The end-user hears the **Return to queue confirmation** message and does one of the following:

     * **Presses 1** : The end-user is routed back to the queue that they were in. If the queue is configured for first in first out (FIFO), the call goes to the front of the queue, to be connected by the next available agent. Otherwise, the call is prioritized so that it goes to the front or near the front of the queue.

     * **Presses 0** : The end-user returns to the top-level menu readout, unless:

       * The end-user called into a direct access point. In that case, they return to that queue instead of the top level.

       * The end-user called into the inbound phone number of a queue. In that case, they return to that queue instead of the top level.


**Note:** If the queue has a virtual agent, the returning call skips the virtual agent and escalates to a human agent.

### Redial offer workflow

In the redial offer workflow, the call is disconnected by a network or system issue and the end-user calls back. For more information, see Configure Return to queue globally and Configure Return to queue at the queue level.

Here's the redial offer workflow:

  1. A call is disconnected by a network or system issue within the call disconnection timeframe. If a call is disconnected beyond the disconnection timeframe, the call can't be returned to the queue.

  2. The end-user calls back within the callback timeframe. If the end-user calls back beyond the callback timeframe, the call can't be returned to the queue.

  3. The end-user hears the **Return to queue confirmation on callback** message and does one of the following:

     * **Presses 1** : The end-user is routed back to the queue that they were in. If the queue is configured for first in first out (FIFO), the call goes to the front of the queue, to be connected by the next available agent. Otherwise, the call is prioritized so that it goes to the front or near the front of the queue.

     * **Presses 0** : The end-user returns to the top-level menu readout.


**Note:** If the queue has a virtual agent, the returning call skips the virtual agent and escalates to a human agent.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
