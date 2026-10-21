---
url: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/edit-chat-agent/
title: Edit a chat agent \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:37:01.741170+00:00
---

# Edit a chat agent  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/edit-chat-agent/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Edit a chat agent Stay organized with collections  Save and categorize content based on your preferences. 

You can update or modify your chat agent using the conversational chat interface or the visual flow builder.

## Open chat agent in edit view

To begin editing any part of your chat agent, you must first open it in edit view:

### App

  1. Open your Gemini Enterprise web app in a browser.
  2. In the web app navigation menu, click ![Agents
icon](https://docs.cloud.google.com/static/gemini/enterprise/docs/workflow-builder/images/button_magic_icon.png)**Agents**.

The **Agent Gallery** page appears displaying all the prebuilt agents and custom-built agents.

  3. Go to the **Your agents** section, find the chat agent you want to edit.

  4. Click more_vert **Actions menu** and select **Edit**.

The chat agent opens in edit view.




## Edit agent details and subagent logic

You can edit your chat agent's logic, instructions, and configuration in two ways:

  * Use the chat pane for conversational, no-code updates
  * Use the flow builder for manual control

**Important:** The main agent node stores the overall details of your chat agent. Editing the main node details (name, description, instructions) will also update the overall details for your chat agent.

### Edit using conversational chat

Use the chat pane of the canvas to use Gemini AI and update your chat agent's instructions or behaviors.

### App

  1. In the left chat pane, enter a prompt detailing the changes you want to make to the agent's function or behavior.

Example prompt: `Change the main agent's model to Gemini-2.5-flash and update its instructions to be more direct.`

Gemini updates the agent logic and instructions based on your prompt.

  2. Click the **Preview** tab and interact with the agent to verify and evaluate the changes.

  3. Click **Update** to save and relaunch the chat agent.




### Edit using the flow builder

Use the **Flow** tab to visually edit the chat agent flow, Gemini model, data sources, and instructions for the main agent node or any subagents nodes.

### App

To edit the main agent node, do the following:

  1. In the Workflow Builder canvas, click the **Flow** tab.
  2. Click the main agent node to open its details pane.
  3. Edit the agent's **Name** , **Gemini model** , **Description** , **Instructions** , and **Data sources**.
  4. You can also add or remove subagents from this pane.

**Warning:** Removing a subagent may disrupt your agent's flow and control logic.
  5. Click **Update** to save and relaunch the agent.




To edit a subagent node, do the following:

  1. In the Workflow Builder canvas, click the **Flow** tab.
  2. Click the subagent node that you want to edit.
  3. Edit the subagent **Name** , **Gemini model** , **Description** , **Instructions** , and **Data sources**.
  4. Click **Update** to save and relaunch the chat agent.



## What's next

  * Learn how to [use a chat agent](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/use-chat-agent).
  * Learn how to [schedule chat agent runs](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/schedule-chat-agent).
  * Learn how to [share a chat agent](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/share-chat-agent).
  * Learn how to [delete a chat agent](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/delete-chat-agent).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
