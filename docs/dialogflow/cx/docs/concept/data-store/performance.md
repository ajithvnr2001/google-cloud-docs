---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/performance/
title: Data store performance improvements \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:36.856137+00:00
---

# Data store performance improvements  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/performance/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Data store performance improvements Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides recommendations for monitoring and improving the performance of data store handlers.

## Track your agent's performance

You can monitor your agents [conversation history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/conversation-history) and you can use the [analytics tool](https://docs.cloud.google.com/dialogflow/cx/docs/concept/analytics) for agent statistics.

## Run self-service evaluation

You can run [self-service evaluation](https://github.com/GoogleCloudPlatform/dfcx-scrapi/blob/main/examples/vertex_ai_conversation/README.md) which will assess the quality of your data store agent and recommend changes.

## Improve agent responses

If you find some responses during testing that don't meet your expectations, try the following.

  * You can overwrite an answer by adding an [FAQ entry](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store#structured) for a specific question.
  * If you are experiencing low quality answers with a structured FAQ, try using unstructured FAQ.
  * Use the [parse and chunk configurations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store#parse-chunk) to optimize responses.
  * To ban certain phrases, see [agent settings: banned phrases](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-generative-banned).
  * To customize Responsible AI (RAI) content filtering, see [agent settings: safety filters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-generative-safety).
  * To fine-tune your agent's response based on information from earlier in the conversation, you can configure [search conditions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/performance/). This feature is only available for data store tools.



## Optimization of data store tools used by Playbooks

This setting accelerates a data store's [RAG](https://cloud.google.com/use-cases/retrieval-augmented-generation) response and improves latency by not rewriting the user query nor dynamically populating tool parameters. This means that the user query is passed to the data store as-is and no filters or user metadata-related parameters are populated.

You can enable this feature in the Dialogflow CX console by selecting the playbook, then clicking the **Settings** tab. You have the option of configuring the Playbook to continue processing any follow-up actions immediately or waiting for the next end-user input.

If enabled, the following Playbook instructions are still honored:

  * When to answer the user query using the data store(s).
  * When not to answer user query using the data store(s) and instead provide an alternate response.
  * Any instructions that are defensive such as, for example, "don't answer questions about competitors".



If enabled, the following Playbook instructions are **ignored**. Don't activate this setting if you have any of the following query requirements:

  * Specific data store filters to be populated using the instructions.
  * Instructions to apply any user personalization metadata passed by filters.
  * Any other instructions to rewrite the user query before querying the data store.



## Handle conversation digressions

An end-user may ask clarifying questions during a conversation. For example, during credit card information collection, they may want to clarify what a CVV is. In this case, your agent should answer the question and return to collecting the necessary credit card information. To accomplish this, you can create a data store handler with data stores that answer the question, apply that handler to the flow start page of the flow that handles credit card information collection, and set a transition target for this handler to return to the "current page".

## Handle undesired intent matches

If your agent is matching intents when it should be using a data store handler, you can try the following to correct this:

  * Delete or modify training phrases that are vague, so that all of your training phrases precisely handle the desired intention and do not conflict with your data store content.
  * Use [negative examples](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#negative) to avoid intent matching.



## Data store filtering

In some cases, you may only want certain data stores available for queries, depending on session parameter values. For example, you may have unique data stores for product categories. To accomplish data store filtering for product categories:

  * Set session parameters to product categories.
  * Create condition routes that check the values of the session parameters and transition to a specific page that has the desired data store handler.
  * The data store handler should transition back to the calling page, so that the conversation can continue.



## Data store search configuration

For more information about fine-tuning your data store search results, see the [data store search configuration](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/search-configure) pa

[ Previous arrow_back  Data store tool settings  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/settings)

[ Next Data store hybrid agents  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/hybrid)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
