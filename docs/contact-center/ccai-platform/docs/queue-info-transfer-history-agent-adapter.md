---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/queue-info-transfer-history-agent-adapter/
title: Transfer history and queue information in the agent adapter \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:12.445253+00:00
---

# Transfer history and queue information in the agent adapter  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/queue-info-transfer-history-agent-adapter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Transfer history and queue information in the agent adapter Stay organized with collections  Save and categorize content based on your preferences. 

When an agent receives an incoming call transfer, virtual agent call escalation, or call deflection, the call connection screens of the call adapter display source queue information. You can turn on transfer history to make the call adapter also display the destination queue, giving the agent additional context about the call. Turning on transfer history also makes session transfer history available in both the call adapter and chat adapter. The agent adapter displays queue information and transfer history in the same way for warm and cold transfers.

## Turn on transfer history

To turn on transfer history, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. For **Transfer History** , select the **Display transfer history in agent adapter** checkbox.

  3. Click **Save General**.




## Call adapter behavior

The call adapter always displays source queue information for transfers, escalations from virtual agents, and deflections. The call adapter displays destination queue information only if you turn on transfer history.

### Call transfers

When an agent receives an incoming call transfer, the source queue information appears in the call connection screens of the call adapter as follows:

  * If there were multiple transfers prior to the agent receiving the call, each transfer is represented by an item in a numbered list. Transfers are listed in chronological order.

  * If a transfer was routed through multiple queues before an agent answered it, the queue path is shown. The last queue in the queue path is the one where the agent answered the call.

  * If a transfer was direct to an agent, **Direct Transfer** is shown.




The following image shows the call connection screens for a call transfer. The queue information is highlighted.

![Queue information in the call connection screens of the agent
adapter](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/agent-adapter-call-transfers.png)

### Escalations from virtual agents

When an agent receives an escalation from a virtual agent, the source queue information appears in the call connection screens as follows:

  * The source queue is marked with **Escalated from {the virtual agent's label}**.

  * Any additional transfers are included in the list of source queues, as described in Call transfers.




### Deflections

When an agent receives a deflection, the source queue information appears in the call connection screens as follows:

  * The queue where the deflection was set up includes one of the following deflection reasons: **Deflected by After Hours** or **Deflected by Overcapacity**.

  * Any additional transfers are included in the list of source queues, as described in Call transfers.




### Destination queue information

The call adapter displays the destination queue for transfers, escalations from virtual agents, and deflections only if you turn on transfer history.

The destination queue information appears as follows:

  * If the transfer was direct to an agent, it's marked as a **Direct Transfer**.

  * If the transfer was an escalation from a virtual agent, it's marked with **Escalated from {the virtual agent's label}**.

  * If the transfer was a deflection, one of the following reasons is included: **Deflected by After Hours** or **Deflected by Overcapacity**.




## Transfer history

When you turn on transfer history, agents can view session transfer history in the call adapter and the chat adapter.

### View call transfer history

To view call transfer history, follow these steps:

  1. [Receive an inbound call](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-calls#receive-inbound-call).

  2. Click the **Details** tab.

  3. Click **Transfer History**. The **Transfer History** pane appears.




The transfer history appears as follows:

  * Transfers are listed in chronological order.

  * If a transfer passed through one or more queues before completion, the queue path is shown.

  * If the transfer was direct to an agent, it's marked with **Direct Transfer**.

  * If the transfer was an escalation from a virtual agent, it's marked with **Escalated from {the virtual agent's label}**.

  * If the transfer was a deflection, one of the following reasons is included: **Deflected by After Hours** or **Deflected by Overcapacity**.

  * Failed transfers and canceled transfers are marked as such.




### View chat transfer history

To view chat transfer history, follow these steps:

  1. [Answer a chat request](https://docs.cloud.google.com/contact-center/ccai-platform/docs/handle-a-chat#answer-a-chat-request). If there is a transfer history for this chat session, the **Transfers** link appears in the chat pane.

  2. Click **Transfers**. The **Transfer History** pane appears.




The transfer history appears as follows:

  * Transfers are listed in chronological order.

  * If a transfer passed through one or more queues before completion, the queue path is shown.

  * If the transfer was direct to an agent, it's marked with **Direct Transfer**.

  * If the transfer was an escalation from a virtual agent, it's marked with **Escalated from {the virtual agent's label}**.

  * Failed transfers and canceled transfers are marked as such.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
