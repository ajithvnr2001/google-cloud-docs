---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/agent/
title: Agents \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:20.662213+00:00
---

# Agents  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Agents Stay organized with collections  Save and categorize content based on your preferences. 

The term _agent_ can mean different things. In a _Multi-Agent System_ , which forms a hierarchical agent tree, the entire agent tree is referred to as the _agent application_.

An agent application is composed of one or more agents, where each agent can be either the _root agent_ or a _sub-agent_.

A _root agent_ (also known as steering agent) acts as the primary entry point and orchestrator for the overall agent application. It typically handles the main interaction with the end-user, it is responsible for understanding the overall goals, and it delegates specific tasks to appropriate _sub-agents_.

A _sub-agent_ (also known as child agent) is a more specialized agent designed to handle a specific task, domain, or capability. For example, a sub-agent could be tasked with searching a specific database or analyzing a particular type of data. Sub-agents promote modularity and reusability in your agent application.

Root agents can invoke sub-agents, and sub-agents can invoke other sub-agents.

![Route and sub-agent diagram](https://docs.cloud.google.com/static/gemini-enterprise-cx/cx-agent-studio/images/root-sub-agent.png)

## Create an agent application and root agent

To create an agent application and root agent:

  1. Open the [CX Agent Studio console](https://ces.cloud.google.com).
  2. Select your project.
  3. Click **Create** or **Create agent**.
  4. Provide an agent application name.
  5. Click **Create**. If this is the first agent application you have created for the project, creation may take 1-2 minutes. The agent builder is shown and, a root agent is created for you.
  6. Click the plus sign in the top right corner of the root agent.
  7. Click **Add instructions** to add [instructions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/instruction) for the root agent.
  8. Click **Add tool** to add [tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool) for the root agent.



## Create a sub-agent

To create a sub-agent:

  1. Click the plus sign at the bottom of the root agent.
  2. Click **Add sub-agent**.



## Manage agent applications

To manage agent applications for your project:

  1. Open the [CX Agent Studio console](https://ces.cloud.google.com).
  2. Select your project. The list of agent applications for your project are shown.



For each agent application, the following information and actions are available:

  * Click the agent application name to open the application in the agent builder.
  * **Deployed to** column shows the number of channels the application is deployed to.
  * **Sessions** column shows the number of sessions in the past 24 hours that use a deployment channel.
  * **Escalation** column shows the number of escalations in the past 24 hours that use a deployment channel.
  * The latest update time for the agent application is shown.
  * You can click the context menu for a particular agent application, then **Import agent** , **Export agent** , or **Delete agent**. For more information, see [Export and import](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/export).



## Language support

You should design your agents using English, but agents can automatically detect the language of end-user input, and they will automatically respond using the same language. For the list of supported languages, see the [languages reference](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/language).

## Model support

CX Agent Studio uses Gemini foundation models to power generative reasoning, instruction following, and multimodal capabilities. You can select a global model for the entire agent application or override it for specific sub-agents.

Models in CX Agent Studio are performance-tuned for customer experience, potentially differing from [standard Vertex AI offerings](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models).

**Note:** All models in CX Agent Studio are considered General Availability (GA) unless explicitly marked as "Preview" in the UI. This launch stage is specific to CX Agent Studio and operates independently of a model's status in other Google Cloud products.

For CX Agent Studio, the following models are supported:

Model | Optimization | Launch stage  
---|---|---  
`composite-v1` | Voice Optimized | GA  
[`gemini-3.7-flash`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-7-flash) | Text Optimized | GA  
[`gemini-3.5-flash`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-5-flash) | Text Optimized | GA  
[`gemini-3-flash`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-flash) | Text Optimized | Preview  
[`gemini-2.5-flash`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/2-5-flash) | Text Optimized | GA  
`gemini-3.1-flash-live` | Voice Optimized | GA  
  
### Gemini Composite V1 model

The Gemini Composite V1 model is engineered for enterprise voice agents. It combines three sub-component models to deliver strict instruction adherence, superior tool execution, and exceptional voice stability:

This composite model is a combination of three underlying sub-component models:

  * **Listener Model:** Converts incoming audio into transcripts with real-time noise rejection.
  * **Thinking Model:** Processes inputs, enforces instructions, and executes backend tools.
  * **Speaker Model:** Converts text responses into natural, low-latency speech.

**Note:** Automatic updates may trigger a change of minor version of the composite model or the sub-components.

## Agent application settings

See [settings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/settings).

## Agent settings

See [settings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/settings).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
