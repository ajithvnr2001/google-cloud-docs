---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-system-instructions/
title: Guide agent behavior with authored context \u00a0|\u00a0 Conversational Analytics API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:24:43.658748+00:00
---

# Guide agent behavior with authored context  |  Conversational Analytics API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-system-instructions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Guide agent behavior with authored context Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to best provide authored context to your Conversational Analytics API data agents by writing effective prompts through system instructions and, for some data sources, by additionally providing structured context. While providing authored context is optional, well-structured authored context can improve the accuracy and relevance of the responses that the API provides.

## What is authored context?

Authored context is guidance that developers can provide to shape the behavior of a data agent and to refine the API's responses. This guidance includes free-form system instructions and, for some data sources, structured context fields with information such as table descriptions and sample queries. To answer questions, the agent combines this authored context with information from data sources—such as BigQuery tables, Looker Explores, Data Studio, and database data sources—and with conversation history (for multi-turn conversations).

By providing clear guidance through structured contextual fields and free-form system instructions, you can improve the agent's ability to interpret user questions and generate useful and accurate responses. Well-defined context is especially useful if you're connecting to data such as BigQuery tables. For example, you can use authored context to provide the following types of guidance to an agent:

  * **Business-specific logic** : Define a "loyal" customer as one who has made more than five purchases within a certain timeframe.
  * **Response formatting** : Summarize all responses from your data agent in 20 words or fewer to save your users time.
  * **Data presentation** : Format all numbers to match the company's style guide.



## Provide authored context

The specific information that you can provide depends on your data source. For [BigQuery data](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-bq), [Looker data](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-looker), and database data, you can define both structured context and system instructions. For best results, first provide context to the agent through the available structured fields. You can then provide supplemental guidance by defining system instructions.

You provide structured context in API fields for details like table descriptions and sample queries. You provide system instructions as a YAML-formatted string by using the `system_instruction` parameter.

After you define your authored context, you can provide it to the API in one of the following calls:

  * **Creating a persistent data agent** : Include authored context within the `published_context` object in the request body to configure agent behavior that persists across multiple conversations. For more information, see [Create a data agent](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http#create_a_data_agent) (HTTP) or [Set up context for stateful or stateless chat](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk#set_up_context_for_stateful_or_stateless_chat) (Python SDK).
  * **Sending a stateless request** : Provide authored context within the `inline_context` object in a chat request to define the agent's behavior for that specific API call. For more information, see [Create a stateless multi-turn conversation](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http#create-a-stateless-multi-turn-conversation) (HTTP) or [Send a stateless chat request with inline context](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk#send_a_stateless_chat_request_with_inline_context) (Python SDK).
  * **Send a query data request** : For database data sources, provide the context set ID of the authored context within the `agent_context_reference` object in the query data request. For more information, see [Define data agent context for database data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-databases#cloud-sql-cloud-sql-for-postgresql).



## Best practice for building agents: Use version control for authored context

Use the [`stagingContext`, `publishedContext`, and `lastPublishedContext` fields](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#dataanalyticsagent) to control context versions when building agents with the Conversational Analytics API. The following use case illustrates how to use these fields to create a staging and production version of agent context.

Suppose you use an existing agent with the `publishedContext` field, but you need to make an update to the agent (for instance, making all charts green instead of blue).

To make your changes and test them before publishing, follow these steps:

  * Make the changes to the agent in the `stagingContext` field, and test the agent with the changes.
  * When the changes are ready, update the `publishedContext` field with the changes from `stagingContext`.
  * You can revert back to the old agent as needed by updating `publishedContext` to `lastPublishedContext`.



## Related resources

  * [Build a data agent using HTTP and Python](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http)
  * [Build a data agent using the Python SDK](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk)
  * [Define data agent context for BigQuery data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-bq)
  * [Define data agent context for Looker data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-looker)
  * [Define data agent context for database data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-databases)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
