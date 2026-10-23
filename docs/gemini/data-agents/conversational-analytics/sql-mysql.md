---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-mysql/
title: Conversational analytics for Cloud SQL for MySQL overview \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:31.541233+00:00
---

# Conversational analytics for Cloud SQL for MySQL overview  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-mysql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)



Send feedback 

#  Conversational analytics for Cloud SQL for MySQL overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Conversational analytics in Cloud SQL for MySQL lets you chat with agents about your database data using natural language. To get answers about your data, you:

  * Create _data agents_ for a set of knowledge sources, such as tables and views, that you select.
  * [Optional] Create context and instructions for an agent to configure the data agent to effectively answer questions for specific use cases.



Before customizing an agent, we recommend that you first work with the context and instructions that the agent creates.

Conversational analytics provides **the following types of context** :

  * Guided – you create this context in the Google Cloud console. This option is well suited for users who don't want to write code directly.
  * Advanced – you create this context in the Gemini CLI or in your IDE. We recommend this approach for users who want more control of agent quality. This context resuses the context [for the QueryData method](https://docs.cloud.google.com/sql/docs/mysql/data-agent-overview#agent-context). 



After you [create data agents](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-mysql/create-data-agents#create-data-agent), you can then have conversations with them to ask questions about Cloud SQL for MySQL data by using natural language.

Conversational analytics is powered by [Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/overview).

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

## Data agents

Data agents consist of one or more knowledge sources, and a set of instructions specific to a use case for processing that database data. When you create a data agent, you can configure it using the following options:

  * Use _knowledge sources_ such as tables and views with a data agent.
  * Provide custom table and field metadata to describe the database data in the most appropriate way for the given use case.
  * Provide instructions for interpreting and querying the data, such as defining the following: 
    * Synonyms and business terms for field names
    * Most important fields and defaults for filtering and grouping
  * Using either guided or advanced context generation, provide structured contexts that the data agent can use to shape an agent's response structure and to learn the business logic that your organization uses.



### Manage data agents

You can create, manage, and work with the following types of data agents on the **Conversations** page in the Google Cloud console:

  * A predefined sample agent for each Google Cloud project.
  * A list of your drafted, created, and published agents.
  * A list of agents that other people create and share with you.



For more information, see [Create data agents](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-mysql/create-data-agents). 

Other services in the project that support data agents, such as the [Conversational Analytics API](https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/overview), can access data agents that you create in Cloud SQL for MySQL . You can also access an agent created in the Google Cloud console by calling it using the Conversational Analytics API.

## Conversations

Conversations are persisted chats with a data agent or database data source. You can ask data agents multi-part questions that use common terms like "sales" or "most popular," without having to specify table field names or define conditions to filter the database data.

The chat response returned to you provides the following features:

  * The answer to your question as text, code, or charts (where appropriate)
  * The agent's reasoning behind the results.
  * Metadata about the conversation, such as the agent and database data sources used.



When you create a direct conversation with a database data source, the [Conversational Analytics API](https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/overview) interprets your question without the context and processing instructions that a data agent offers. Because of this, direct conversation results can be less accurate. Use data agents for cases that require greater accuracy.

You can create and manage conversations in Cloud SQL for MySQL using the Google Cloud console. For more information, see [Analyze data with conversations](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-mysql/create-conversations). 

## Security

You can manage access to conversational analytics in Cloud SQL for MySQL using [Conversational Analytics API IAM roles and permissions](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/access-control). For information about the roles needed for specific operations, see the [data agent required roles](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-mysql/create-data-agents#before-begin) and the [conversation required roles](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-mysql/create-conversations#before-begin). 

## Locations

When you use conversational analytics to create an agent, the control plane—which plans, manages the workflow, and calls tools (orchestration)—uses only a global endpoint. The data plane—which fetches, retrieves, and processes the actual database records and vector documents—uses a regional endpoint.

## Pricing

You are charged at [Cloud SQL for MySQL compute pricing](https://cloud.google.com/sql/pricing) for queries that run when you create data agents and have conversations with data agents or database data sources. There is no additional charge for creating and using data agents and conversations during the [Preview](https://cloud.google.com/products#product-launch-stages) period.

## Dynamic shared quota

Dynamic Shared Quota (DSQ) in Vertex AI manages capacity for the Gemini model. Unlike conventional quotas, DSQ lets you access a large shared pool of resources without a fixed per-project limit for model throughput.

Performance, such as latency, can vary depending on the overall system load. During times of high demand across the shared pool, you might occasionally experience temporary `429 Resource Exhausted` errors. These errors indicate that the shared pool capacity is momentarily constrained, but not that you have reached a specific quota limit on your project. To check on the capacity, retry the request after a short delay.

## What's next

  * Learn more about the [Conversational Analytics API](https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/overview).
  * [Create data agents](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-mysql/create-data-agents).
  * [Analyze data with conversations](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-mysql/create-conversations). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
