---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/dialogflow-runtime-integration/
title: Dialogflow runtime integration \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:56.942100+00:00
---

# Dialogflow runtime integration  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/dialogflow-runtime-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Dialogflow runtime integration Stay organized with collections  Save and categorize content based on your preferences. 

You can opt in to the Dialogflow runtime integration feature to integrate data from other Dialogflow-powered Contact Center AI services into CX Insights. These services also include [Agent Assist](https://cloud.google.com/agent-assist/docs) and [virtual agents](https://docs.cloud.google.com/agent-assist/docs/agent-virtual).

## Dialogflow runtime integration use cases

We recommend that you enable this feature if you use Agent Assist or Virtual Agent to create conversations and you want to use [CX Insights features](https://docs.cloud.google.com/gemini-enterprise-cx/insights/how-to) on these conversations. For example, Dialogflow runtime integration is useful if you want to:

  * View your conversations and their metadata from a user interface.
  * Run more machine learning analytics on your conversations.
  * Export your conversations to BigQuery for custom analysis or visualization in Looker.



## How Dialogflow runtime integration works

### One-time sync for every new conversation

After you enable Dialogflow runtime integration, CX Insights will create a representation of this [conversation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1#conversation) and its [associated metadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1#runtimeannotation) each time you [complete a conversation](https://docs.cloud.google.com/agent-assist/docs/smart-reply#create_a_conversation) in Agent Assist or Virtual Agent. If the source conversation has a transcript, Insights will generate [additional metadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.analyses#callanalysismetadata) for it if you specified a percentage of conversations to be analyzed in your [analysis rule](https://docs.cloud.google.com/gemini-enterprise-cx/insights/analysis-rule) or [project settings](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/Settings). The default analysis percentage is 0.

If you modify the source data from Agent Assist or a Virtual Agent, the CX Insights representation of the data won't be affected. The opposite is also true.

### Synced data can be queried and exported from CX Insights

Conversations exported to CX Insights will be queryable from CX Insights along with their associated metadata. You can also [export conversation data to BigQuery](https://docs.cloud.google.com/gemini-enterprise-cx/insights/export) to perform your own raw queries.

## What's next

To enable Dialogflow runtime integration, see the [Dialogflow runtime integration quickstart](https://docs.cloud.google.com/gemini-enterprise-cx/insights/enable-dialogflow-runtime-integration).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
