---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/queue_priority/
title: Queue priority \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:40.634390+00:00
---

# Queue priority  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/queue_priority/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Queue priority Stay organized with collections  Save and categorize content based on your preferences. 

The **queue priority** feature lets you assign priority values to selected queues. Call or chat sessions from higher priority queues will then be routed to available agents first. A **session** is one single communication stream between an end-user and a human or virtual agent using either call or chat. Sessions typically have multiple interactions.

You can also enable prioritization by wait time, in which case the priority of a given session will automatically increase based on wait time until the session has reached the highest available priority.

## Queue priority behavior

The following list explains queue priority behavior:

  * When an agent is assigned to multiple queues, calls and chats route to the agent based on routing order.

  * Queue priority values range from +10 to -5. The default value is 0.

  * You can configure queue priority for queues without sub-queues. If a queue contains a sub-queue, you can't configure queue priority for the parent queue.

  * The system can automatically increase the priority of calls or chats based on wait time, using time intervals. These automatic increases can be call-specific or chat-specific.

  * If you disable queue priority at the global level, it's also disabled at the queue level.

  * When you reactivate queue priority, the system reapplies previously configured queue priority levels per queue and any queue-level wait-time prioritization settings.




### Example routing

  * **Example 1:** An agent is assigned to queue A (priority 1) and queue B (priority 2). If a transferred call arrives in queue B and an inbound call in queue A, the agent gets the call from queue B first. The type of call (transfer in this case) is considered before priority values assigned to the queues.

Transferred calls always have a higher priority compared to inbound calls _within the same queue_. If there are multiple transfers into a given queue, the call transferred from a queue _with a higher priority value assigned_ keeps the higher priority among transferred calls in the destination queue.

  * **Example 2:** Continuing the previous example, an agent is assigned to 2 queues, queue A (priority 1) and queue B (priority 2). If a regular inbound call arrives in queue A and a regular inbound call arrives in queue B, the agent will receive the call from queue A first. Both calls are the same type and therefore have the same priority, so the _priority value assigned to the queues_ determines call routing.




## Routing prioritization

![A table is shown with the priorities for different types of chats or calls shown.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/routing-prioritization.png)

  * Call or chat priority is determined first by type then by queue (high or low priority).

  * Call or chat wait time prioritization can increase priority of lower value calls or chats types only.




## Enable queue priority

  1. In the CCAI Platform portal, go to **Settings** > **Operation Management**.

  2. Scroll to **Queue Priority** and toggle **Enable Queue Priority** to **On**.

  3. Optional: Click **Enable Wait Time Prioritization for Calls** or **Enable Wait Time Prioritization for Chats** if you want to increase the priority of that session type by one level for each interval of time that you set in this section. 

These settings ensure that a lower priority (regular inbound) sessions won't get continuously pushed back in the queue if other high priority sessions keep coming in. You can set any value greater than 10 and less than 3,600 seconds.

  4. Click **Set Queue Priority** to save.




## Set queue priority level

Queue priority level is always set individually for queue.

  1. In the CCAI Platform portal, go to **Settings** > **Queue.**

  2. Choose a channel and click **Edit/View** to go to the editing section for queue menus within that channel. This feature is available for the **IVR** , **SMS** , **Web** , **Mobile** , and **Social (WhatsApp**) channels.

  3. Select a leaf queue and toggle **Queue Priority** to **On**.

  4. Slide the call priority slider left or right to lower or raise priority level for sessions in this queue.

  5. Click **Save Queue Priority**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
