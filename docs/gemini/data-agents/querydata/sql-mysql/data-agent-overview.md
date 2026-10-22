---
url: https://docs.cloud.google.com/gemini/data-agents/querydata/sql-mysql/data-agent-overview/
title: QueryData overview \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:45.500521+00:00
---

# QueryData overview  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/querydata/sql-mysql/data-agent-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)



Send feedback 

#  QueryData overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

QueryData lets you interact with your data using conversational language and _data agents_ that you build to help you query your data. Data agents are AI-powered assistants and applications that can understand user intent, query your operational data, and return accurate, grounded answers. QueryData generates queries for your database using context sets, which are collections of curated blueprints, business logic, and schema information. This context allows QueryData to translate natural language questions into accurate queries for your target use cases.

## When to use QueryData

QueryData is ideal for applications such as:

  * **Customer service automation** : Handle high-volume inquiries like "Where is my order?" or "What is my current balance?".
  * **E-commerce shopping assistants** : Help users navigate large product catalogs with natural language queries like "Show me running shoes under $100."
  * **Field operations tools** : Allow mobile employees to query inventory levels, part availability, or service ticket details in real-time.



## Core concepts

To reliably translate conversational questions into database queries, QueryData relies on the following key concepts:

### QueryData and the Conversational Analytics API

The `QueryData` endpoint in the [Conversational Analytics API](https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/overview#key_api_operations) is an agentic tool that enables programmatic natural language to SQL query generation for your databases. Within a conversational application or multi-agent workflow, the `QueryData` endpoint handles schema interpretation and query synthesis. Your agent harness (such as Antigravity, Agent Development Kit (ADK), or LangChain) manages the conversation history, user state, and tool orchestration to contextualize the user's input before sending a natural language request to the `QueryData` endpoint.

### Context sets

A _context set_ is a collection of database-specific knowledge, curated query patterns, and business rules associated with your database instance. Instead of relying solely on general LLM knowledge or raw table schemas, QueryData uses context sets to understand the nuances of your data model and organization-specific terminology.

A context set contains three primary building blocks:

  * **Query blueprints** : Curated pairs of representative natural language questions and their corresponding, pre-validated SQL queries. Blueprints provide canonical examples that define how specific business intents map to SQL statements.
  * **Query facets** : Modular SQL predicates and filter conditions (such as date ranges, threshold calculations, or business flags). Facets allow QueryData to dynamically combine multiple filtering criteria into a query without needing separate blueprints for every combination.
  * **Value searches** : Semantic and string-matching queries that ground informal phrases to exact values stored in database columns. Value searches help resolve ambiguities (for example, mapping "Bay Area" to `San Francisco`, or "Heathrow" to `London Heathrow Airport`) using exact matches, trigram string similarity, or semantic vector embeddings.



### Parameterized secure views

To help ensure that AI-generated queries respect row-level security and multi-tenant isolation, you can use parameterized secure views, which restrict the generated SQL to only access data rows that the authenticated application user is authorized to view. For more information, see [Secure and control access to application data using parameterized secure views](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-mysql/secure-app-data-parameterized-secure-views-qd). 

## How QueryData works

When your agent or application sends a natural language request (such as a user's question that the agent has contextualized with conversation history or user state), QueryData performs the following steps:

  1. **Value resolution** : QueryData runs value search queries against the database to map entities in the prompt (such as names, cities, or categories) to specific database column values.
  2. **Intent matching and disambiguation** : QueryData matches the contextualized request against the curated query blueprints and facets that you defined in the context set. If the request is underspecified or ambiguous, then QueryData can return a disambiguation question so that your agent or application can ask the user for clarification.
  3. **Query synthesis** : Using the matched blueprint structure, applied facets, and resolved values, QueryData synthesizes a complete SQL query for your database engine.
  4. **Query execution** : The generated query executes against the database to return results.



## Author and manage context sets

To author and manage context sets, do the following:

  1. **Author context** : Define the query blueprints, facets, and value searches for your database. For more information, see [Context sets overview](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-mysql/context-sets-overview). You can also use the [context engineering agent](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-mysql/build-context-sets) to automate context creation.
  2. **Manage in Google Cloud console** : Create and manage context sets in Cloud SQL Studio to make them available for query generation.
  3. **Integrate with your applications** : Connect your applications or AI agents to QueryData using [MCP Toolbox](https://github.com/googleapis/mcp-toolbox) or direct API calls.



## Pricing

You are charged at [Cloud SQL for MySQL compute pricing](https://cloud.google.com/sql/pricing) for queries that run when you create context sets and use QueryData with your data agents or database data sources. There is no additional charge for creating and using context sets and QueryData during the [Preview](https://cloud.google.com/products#product-launch-stages) period. For more information, see [Data Cloud Agent pricing](https://cloud.google.com/products/data-agents/pricing).

## What's next

  * Learn how to [test QueryData in Cloud SQL Studio](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-mysql/inspect-data-agent).
  * Learn how to [create and manage context sets](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-mysql/manage-data-agents).
  * Learn how to [build context sets with the context engineering agent](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-mysql/build-context-sets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
