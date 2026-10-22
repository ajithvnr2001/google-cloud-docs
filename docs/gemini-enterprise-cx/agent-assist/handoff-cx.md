---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/handoff-cx/
title: Dialogflow CX handoff \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:55.153694+00:00
---

# Dialogflow CX handoff  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/handoff-cx/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Dialogflow CX handoff Stay organized with collections  Save and categorize content based on your preferences. 

Handoff is the process of transferring an end user conversation from a [Dialogflow CX agent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent) to a human agent. When an end user asks to speak with a human agent, Dialogflow CX invokes the [built in event](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in) `flow-failed-human-escalation`, which activates the [symbolic transition target](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#symbolic) `END_FLOW_WITH_HUMAN_ESCALATION`.

## End flow

Dialogflow CX ends conversations with the `END_FLOW` transition, which initiates the [handler call stack](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#handler-flow-stack). When the call stack is empty, `END_FLOW_WITH_HUMAN_ESCALATION` ends the Dialogflow CX session and transfers the conversation to a human agent.

## Telephony integration

Follow the instructions to [setup your Google Cloud telephony integration](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/cloud-setup) to enable handoff.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
