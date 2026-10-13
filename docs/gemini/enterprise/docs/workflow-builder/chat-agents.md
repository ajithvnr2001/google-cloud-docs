---
url: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/chat-agents/
title: Chat agent overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:54:44.322121+00:00
---

# Chat agent overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/chat-agents/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Chat agent overview Stay organized with collections  Save and categorize content based on your preferences. 

A _chat agent_ is a type of agent that you can build using [Workflow Builder](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder) in your Gemini Enterprise web app. These agents are designed to interact with users in a conversational manner to complete a specific task. Chat agent responses depend on the user's input, making them primarily non-deterministic in nature.

Chat agents are ideal for the following use cases:

  * Open-ended conversations without fixed steps. For example, a brainstorming assistant for project ideas.
  * Dynamic tasks where user input drives the flow. For example, a customer support agent where the next question depends on the user's issue.
  * Q&A, data lookup, or personalized assistance. For example, checking Jira ticket status or summarizing a specific email thread.



## Before you begin

Before exploring these features, do the following:

  * Ensure that a Gemini Enterprise administrator has enabled the **Enable chat agents** feature toggle in your app's feature management settings. For more information, see [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).
  * Ensure you have a Gemini Enterprise web app with the necessary data stores connected. For more information, see [About apps and data stores](https://docs.cloud.google.com/gemini/enterprise/docs/apps-data-stores).



## Chat agent canvas

The chat agent canvas is an interactive interface that you can use to build and refine your chat agent. The canvas is divided into two main modes:

  * **Chat mode** : the chat mode provides a conversational interface to build and refine your agent using natural language prompts. It's perfect for no-code users who want to use Gemini's intelligence to quickly develop and adjust their agent's details, instructions, or behaviors.

![The chat mode UI](https://docs.cloud.google.com/static/gemini/enterprise/docs/workflow-builder/images/chat-mode.png)

  * **Designer mode** : the designer mode provides a visual representation of your agent and is organized into two panes:

    * **Chat pane** : this pane is similar to the chat mode, where you can interact with your agent in a conversational manner while viewing the changes to the agent in the designer pane.
    * **Designer pane** : this pane provides a visual representation of your agent and is further divided into the following tabs:

      * **Flow** : presents a visual representation of your agent's workflow and control logic. Use the **Flow** tab to view the overall details of your main agent, manage the main agent and all individual sub-agents, and to design complex, multi-step agents.
      * **Schedule** : provides configuration options to set one or more execution schedules for your agent.
      * **Preview** : provides a live, interactive test environment for your agent. Use the **Preview** tab to test the agent's functionality and response as you build.

![The designer mode UI](https://docs.cloud.google.com/static/gemini/enterprise/docs/workflow-builder/images/designer-mode.png)




## Chat agent components

Chat agents can be single-step or multi-step agents. Single-step chat agents consist of a single agent node, which contains the logic for the agent. Multi-step chat agents are made up of a main agent node that is connected to one or more sub-agent nodes. Each sub-agent node is an independent agent with its own logic.

## What's next

  * Learn how to [create a chat agent](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-chat-agent).
  * Learn how to [create a workflow](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-workflows).
  * Learn how to [use a chat agent](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/use-chat-agent).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
