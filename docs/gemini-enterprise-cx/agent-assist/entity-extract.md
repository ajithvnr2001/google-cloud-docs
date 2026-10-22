---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/entity-extract/
title: Real-time entity extraction \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:37.698879+00:00
---

# Real-time entity extraction  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/entity-extract/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Real-time entity extraction Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can request real-time entity extraction during an Agent Assist conversation. This feature automatically extracts data that matches any Dialogflow [system entity](https://docs.cloud.google.com/dialogflow/docs/reference/system-entities) in end-user expressions.

For example, if the end-user says "I want three tickets for Friday", "3" will be extracted as a `@sys.number` entity, and "Friday" will be extracted as a `@sys.date` entity. Agent Assist provides this data to your system during the conversation, so you can display it on the human agent's user interface. You can then use this data to provide the human agent with additional tools, such as a button to schedule an event when a date is extracted.

## Enable real-time entity extraction

To enable real-time entity extraction, set the `human_agent_assistant_config.message_analysis_config.enable_entity_extraction` field to `true` when creating or updating a [`ConversationProfile`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversationProfiles).

## Get extracted data

When you call the `analyzeContent` or `streamingAnalyzeContent` method for the [`Participant`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversations.participants) resource, the `message.message_annotations.parts` field of the response contains the extracted data.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
