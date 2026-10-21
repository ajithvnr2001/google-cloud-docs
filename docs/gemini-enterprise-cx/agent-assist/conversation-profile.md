---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile/
title: Create a conversation profile \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:44:28.328674+00:00
---

# Create a conversation profile  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Create a conversation profile Stay organized with collections  Save and categorize content based on your preferences. 

To start a conversation with an end user, create a conversation profile. This profile sets up parameters that control suggestions to a [Dialogflow virtual agent](https://docs.cloud.google.com/dialogflow/cx/docs) or a human agent during runtime. If it's a human agent, you can also configure the category of suggestions to appear: summarization with custom sections or (proactive) generative knowledge assist. To create a conversation profile, you can click the **Conversation Profile** tab in the Agent Assist console or you can use the console tutorials. For (proactive) generative knowledge assist feature you can use the Application programming interface (API) method as well.

**Note:** You can only use the Agent Assist console during design-time and model testing phases. Runtime operations must call the API directly. For instructions on how to send API calls, see the [Agent Assist how-to guides](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/how-to)

## Before you begin

  * To implement (proactive) generative knowledge assist, you must create a [flow-based data store agent](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/generative-knowledge-assist#create_a_flow-based_data_store_agent) or [playbook-based data store agent](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/generative-knowledge-assist#create_a_playbook-based_data_store_agent).
  * To implement summarization with custom sections, you must [create a summarization generator](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-with-custom-sections#create_a_summarization_generator).



## Create a conversation profile

Use the following resources to create a conversation profile:

  * Agent Assist console
  * Application programming interface (API)



We recommend that you use the console tutorials first, as follows.

  1. Navigate to the Agent Assist console. [Go to the Agent Assist console](https://agentassist.cloud.google.com/).
  2. Click **Get started** for the feature you'd like to use.
  3. Optional: Depending on which feature you're using, follow the steps in one of the following pages: 
     * [Summarization with custom sections](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-with-custom-sections)
     * [Generative knowledge assist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/generative-knowledge-assist)
  4. Verify the conversation profile in the [Agent Assist simulator](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/simulator).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
