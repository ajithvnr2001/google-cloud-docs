---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/handoff-es/
title: Dialogflow ES handoff \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:17:18.826656+00:00
---

# Dialogflow ES handoff  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/handoff-es/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Dialogflow ES handoff Stay organized with collections  Save and categorize content based on your preferences. 

Handoff is the process of transferring an end user conversation from a [Dialogflow ES agent](https://docs.cloud.google.com/dialogflow/es/docs/agents-overview) to a human agent. Dialogflow ES offers multiple ways to do this.

## Indicate handoff in your intent response

First, you must [create a Dialogflow ES agent](https://docs.cloud.google.com/dialogflow/es/docs/agents-manage#create). Design your Dialogflow ES agent so that matching certain [intents](https://docs.cloud.google.com/dialogflow/es/docs/reference/common-types#intents) tells Dialogflow ES to hand off the conversation to a human agent.

### Parameters

The [`endInteraction`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents) parameter tells Dialogflow ES to remove the Dialogflow ES agent from the conversation.

Dialogflow ES doesn't directly use the [`liveAgentHandoff`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents) parameter. It sends the boolean value to your webhook request when the intent is matched, or in response to your API call to detect intent. When your Dialogflow ES agent receives an intent with this parameter's value set, you can take any actions necessary to hand off the conversation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
