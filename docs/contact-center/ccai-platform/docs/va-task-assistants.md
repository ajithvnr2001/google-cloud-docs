---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-task-assistants/
title: Create virtual task assistants \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:38.821474+00:00
---

# Create virtual task assistants  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-task-assistants/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Create virtual task assistants Stay organized with collections  Save and categorize content based on your preferences. 

You can create virtual task assistants that perform repetitive tasks for your human agents. After you create a task assistant, an agent can transfer a call or a chat to the task assistant to complete the task. The agent waits on hold until the task is completed, then the call or chat is transferred back to the agent. While the agent is on hold, they can mute or end the call or chat. Unlike virtual agents, virtual task assistants cannot be assigned to a queue. A virtual task assistant can only be assigned to a task. Virtual task assistants aren't available for the SMS channel.

For compliance with the Health Insurance Portability and Accountability Act of 1996 (HIPAA) and to protect the end user's personally identifiable information, virtual task assistants don't record or create transcripts of calls or chats.

## Before you begin

Before you can create a virtual task assistant, you must create and integrate a Dialogflow agent. This is the same requirement as for creating a virtual agent. For more information, see [Create and integrate Dialogflow agents](https://docs.cloud.google.com/contact-center/ccai-platform/docs/create-a-dialogflow-agent).

## Create a virtual task assistant

To create a virtual task assistant, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Virtual Agent**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Click **Add virtual agent** > **Task Assistant**. The **Add a Virtual Task Assistant** pane appears.

  3. In the **Virtual Agent** field, enter a name for your virtual agent. This is an internal name that's used for administration and reporting. Google recommends giving each of your virtual agents a unique internal name. This name is visible to end-users only if you don't set up a [virtual agent alias](https://docs.cloud.google.com/contact-center/ccai-platform/docs/use-va-aliases).

  4. To set up a virtual agent alias, do the following.

     1. Select the **Virtual Agent Alias** checkbox.

     2. In the **Virtual Agent Alias** field, enter a name. When the checkbox is selected, the virtual agent alias is the name that end-users see when they interact with this virtual agent. Otherwise, end-users see the internal virtual agent name from step 3.

**Note:** If you have multiple virtual agents, Google recommends giving them the same virtual agent alias. That way, when a session with an end-user is transferred to multiple virtual agents, the virtual agents appear to the end-user to have the same name. This creates the impression that a single virtual agent is handling a session. For more information, see [Virtual agent aliases](https://docs.cloud.google.com/contact-center/ccai-platform/docs/use-va-aliases).
  5. To upload a custom avatar for your task assistant, do the following:

     1. Click ![The edit avatar button](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-avatar.png)**Update**.

     2. Navigate to an image for your avatar, and then click **Open**. The **Select area to use** dialog appears.

     3. Crop your image, and then click **CROP**.

  6. In the **Choose Virtual Agent platform** list, select a platform.

  7. In the **Choose workflow** list, select a workflow. A workflow represents an authenticated Dialogflow agent.

  8. For **Channel** , select **Chat** or **Voice**. The **Menu** checkboxes that are available for your selected channel are automatically selected.

  9. For **Menu** , change your selections if needed.

  10. For **Language** , select one or more languages for your task assistant.

  11. To add data parameters, do the following:

     1. For **Data parameters** , click **Add Parameter**. The **Add Parameter** dialog appears.

     2. Fill in the fields according to the instructions in [Pass data parameters to Virtual Agents and Virtual Task Assistants](https://docs.cloud.google.com/contact-center/ccai-platform/docs/pass-data-parameters#data-parameters-to-vas-and-virtual-task-assistants), and then click **Save**.

     3. To add more data parameters, repeat these steps.

  12. Click **Save**.

  13. To turn on your virtual task assistant, do the following:

     1. Click **Back to Virtual Agents**.

     2. In the **Virtual Agents** pane, find your new virtual agent, and then click the toggle to the on position.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
