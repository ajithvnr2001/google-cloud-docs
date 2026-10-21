---
url: https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer-eap/agent-designer/
title: Workflow Builder overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:39:19.454644+00:00
---

# Workflow Builder overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer-eap/agent-designer/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Workflow Builder overview Stay organized with collections  Save and categorize content based on your preferences. 

Workflow Builder is an interactive no-code, low-code platform for creating, managing, and turning on [chat agents](https://docs.cloud.google.com/gemini/enterprise/docs/concepts#ase-agents) and [workflows](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/workflows) in your Gemini Enterprise web app.

With Workflow Builder, you can:

  * **Create chat agents and workflows** using natural language prompts or the interactive visual editor.
  * **Build and orchestrate** deterministic or non-deterministic workflows using triggers, steps, and actions.
  * **Connect your chat agents and workflows to various data sources** (including Google, third-party, and custom data sources) and tools.
  * **Preview and simulate** the behavior of your workflows in the integrated testing environment.
  * **Publish, turn on, and share** chat agents and workflows with specific users or groups within your organization.
  * **Schedule workflow executions** to run tasks on a recurring basis.



## Agent types

The following table lists the types of agents that you can create using Workflow Builder:

Agent type | Description | Best for  
---|---|---  
Chat agents |  Designed for conversational interactions to complete specific tasks. Responses depend on user input and are primarily non-deterministic. Can be single-step or multi-step agents.  For more information about chat agents, see [Chat agent overview](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/chat-agents).  | 

  * Open-ended conversations without fixed steps. For example, a brainstorming assistant for project ideas.
  * Dynamic tasks where user input drives the flow. For example, a customer support agent where the next question depends on the user's issue.
  * Q&A, data lookup, or personalized assistance. For example, checking Jira ticket status or summarizing a specific email thread.

  
Workflows |  Executed as a sequence of steps or actions, combining AI automation with human intervention. Logic can be deterministic or non-deterministic.  For more information about workflows, see [Workflow overview](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/workflows).  | 

  * Multi-step processes with defined sequence logic. For example, automating an employee onboarding checklist across tools like Gmail and Google Calendar.
  * Tasks with AI automation and human approvals. For example, drafting a report with AI that requires a user sign-off before publishing.
  * Complex orchestrations with conditional logic. For example, routing sales leads to different teams based on region and budget.

  
  
## Agent controls and security

Gemini Enterprise provides centralized oversight and granular security for all AI agents and workflows within an organization.

While Workflow Builder empowers employees and non-admin users to build and deploy chat agents and workflows, these actions remain strictly governed by administrative policies. Specifically, the actions and tools available to any agent or workflow are limited to the data connectors, tools, and permissions provisioned by the Gemini Enterprise administrator. This ensures that agents and workflows operated by end users can only perform tasks and access information that are explicitly authorized, maintaining enterprise-grade compliance and data integrity.

## What's next

  * Learn how to [create a chat agent](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-chat-agent).
  * Learn how to [create a workflow](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-workflows).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
