---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/queue-level-wrap-up-settings/
title: Queue-level wrap-up settings \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:05.308209+00:00
---

# Queue-level wrap-up settings  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/queue-level-wrap-up-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Queue-level wrap-up settings Stay organized with collections  Save and categorize content based on your preferences. 

Queue-level wrap-up settings allow you to customize the communication of wrap-up times for different queues within a contact center. This ensures that agents have adequate time to complete their tasks without compromising service level agreements or taking another call or chat before they are ready. This is particularly useful for queues that handle different types of issues, such as escalations or complex issues, which might require more time to handle.

You can define queue wrap-up settings either explicitly for a single leaf-queue or at a parent level, to share settings with all child leaf-queues.

## Define wrap-up queue level settings

Wrap-up settings are inherited by all queues globally by default, unless they are overridden (redefined) at the queue level or at the parent queue level. Global settings are defined in Operations Management.

To adjust the wrap-up settings for a queue you must go to that queue:

  1. On the Settings panel for that queue, go to **Wrap-up Settings**.
  2. Beside **Wrap-up** , click **Settings**. The **Wrap-up Settings** panel for that queue will open.



## Inherited settings

This indicates whether settings are inherited or redefined at the queue level, meaning they are explicitly defined at that queue level. **Redefined** indicates that the wrap-up settings for that specific queue have been customized and are different from the default settings inherited from the global or parent queue level.

### Reset to the Global

The button **Reset to the Global** is available when the queue wrap-up settings are **redefined** at the queue level and are not inherited from a parent queue. By clicking this button, the Admin can undo any changes made to the queue's settings and return to the settings inherited from the global level.

## Wrap-up settings

Settings and configuration pertaining to the wrap-up feature.

### Wrap-up exceeded

This setting lets you transition agents into a **Wrap-up Exceeded** status after they have gone beyond a wrap-up threshold time and have cleared all ongoing sessions. When an agents transitions to **Wrap-up Exceeded** status, an agent-level notification appears. This status can only be used when notes and disposition codes are enabled.

For more information see [Agent Statuses](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-status).

### Automatic wrap-up for calls

You can set automatic wrap-up for both inbound and outbound calls. This automatically ends a call session after a set period of time. This feature is typically used to help agents manage their time more efficiently and to help ensure that all sessions are properly documented and brought to a close.

To set automatic wrap-up for calls, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **IVR (Interactive Voice Response)** pane, click **Edit / View**.

  3. Click the queue that you want to edit.

  4. In the **Settings** pane, go to **Wrap-up settings** , and then click **Configure**. The **Wrap-up** pane appears.

  5. Do one of the following, or both, depending on your requirements:

     * To set automatic wrap-up for inbound calls, do the following:

       1. Click the **Automatic wrap-up for inbound calls** toggle to the on position.

       2. Set the number of seconds after which the agent's status switches to **Available**.

     * To set automatic wrap-up for outbound calls, do the following:

       1. Click the **Automatic wrap-up for outbound calls** toggle to the on position.

       2. Set the number of seconds after which the agent's status switches to **Available**.

  6. Click **Save**.




### Manual wrap-up

If an agent manually changes their status to **Wrap-up** in the agent adapter, by default, wrap-up activities are assigned to the agent's last completed call or chat session. You can also [configure manual wrap-up attribution](https://docs.cloud.google.com/contact-center/ccai-platform/docs/configure-disposition-timing#configure-manual-wrap-up).

### Disposition Codes and Notes

After **Automatic wrap-up for calls** is toggled **On** , the settings for disposition notes and codes become available. Disposition codes and notes are tools that allow agents to document the final outcome of a customer interaction.

The **codes** are used to classify and label inbound and outbound sessions, while the **notes** provide additional context about the session outcome. This feature helps to inform the team of the context of the session and streamline the follow-up process for efficiency.

For more information, refer to [Disposition Codes and Notes](https://docs.cloud.google.com/contact-center/ccai-platform/docs/disposition-note).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
