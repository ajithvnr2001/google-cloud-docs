---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/data-store/
title: Data store tools \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:07.675662+00:00
---

# Data store tools  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/data-store/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Data store tools Stay organized with collections  Save and categorize content based on your preferences. 

Data store tools can provide AI-generated agent responses based on website content and uploaded data. Your agent can find answers to end-users' questions from your [data stores](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store).

You can use data stores from any region in a tool, regardless of the agent's region. However, once you add a data store from a particular region, you can only add additional data stores from the same region to that same data store tool. You can, however, create another data store tool with data stores in a different region.

When creating a data store tool, you can select from existing data stores or create a new one. You can create [Website data stores](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/website-data-store) and [Cloud Storage data stores](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/cloud-storage-data-store) directly within CX Agent Studio with a simplified interface. Other data stores can be created from AI Applications.

## Settings

The following data store tool settings are available:

Configuration:

  * **Name** : Tool name
  * **Description** : Tool description
  * **Data stores** : Select or create one or more data stores



Advanced:

  * **Asynchronous execution** : When enabled, the agent will continue the session while the tool runs in the background.
  * **Filter** : Enable the LLM to filter only results that match the filter parameter. 
    * Never (Default): Agent will never use the filter parameter
    * Always: LLM can decide or not to use a filter
    * Auto (legacy): Agent will use filter for connector data store, but not for other types of data stores
  * **Modalities** : The following settings are provided for optimizing the experience of **Text** or **Voice**. The **Text** configuration is chosen unless the agent application is deployed to a telephony channel or the request originated from a voice session with the simulator. 
    * **Rewriter model** : See [rewriter model](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/settings#rewriter-model-selection)
    * **Rewriter prompt** : See [rewriter model](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/settings#rewriter-model-selection)
    * **Summarization model** : See [summarization model](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/settings#summarization-model-selection)
    * **Summarization prompt** : See [summarization model](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/settings#summarization-model-selection)
    * **Grounding score** : See [grounding](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/settings#grounding)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
