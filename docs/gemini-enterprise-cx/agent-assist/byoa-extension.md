---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/byoa-extension/
title: User guide: Build your own GenAI assist extension \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:01.018896+00:00
---

# User guide: Build your own GenAI assist extension  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/byoa-extension/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  User guide: Build your own GenAI assist extension Stay organized with collections  Save and categorize content based on your preferences. 

You can create and use tools to connect with external systems using LLM-powered Agent Assist. Vertex AI Extensions provides the support for tools in Agent Assist. For this reason, if you intend to use a tool in Agent Assist, use the Vertex AI Extensions tool type.

This guide provides instructions for using Vertex AIExtensions to create a Build your own GenAI assist (BYOA) generator.

## Prerequisites

To use a Vertex AI Extensions tool, you must have access to the following:

  * Agent Assist console
  * Vertex AI for Vertex extension APIs
  * Cloud Storage for the API spec



## Create a Vertex AI extension

You must set up your own [Vertex AI extension](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/extensions/create-extension) which calls the API you want to use. You only need to create the extension and the backend will run it when needed.

## Create a tool

  1. Navigate to the Agent Assist console and choose a **Project**.

[Agent Assist console](https://agentassist.cloud.google.com)

  2. From the menu, select extension **Tool**.

  3. Create a tool.

  4. In the **Extension** field, add the Vertex extension resource.




## Create a BYOA generator

  1. Navigate to the Agent Assist console and choose a **Project**.

[Agent Assist console](https://agentassist.cloud.google.com)

  2. Click **Build-your-own-assist** > **Create**.

  3. Add the instructions for your generator.




## Create a conversation profile

  1. Navigate to the Agent Assist console and choose a **Project**.

[Agent Assist console](https://agentassist.cloud.google.com)

  2. Click conversion_path **Conversation profiles**.

  3. Click **\+ Create**.

  4. Add your BYOA generator.




## Test in the simulator

  1. Navigate to the Agent Assist console and choose a **Project**.

[Agent Assist console](https://agentassist.cloud.google.com)

  2. Click **Simulator**.

  3. Select the conversation profile you created.

  4. Click **Start**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
