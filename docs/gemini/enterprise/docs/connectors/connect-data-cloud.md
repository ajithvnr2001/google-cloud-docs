---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-data-cloud/
title: Connect to Data Cloud \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:42.568421+00:00
---

# Connect to Data Cloud  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-data-cloud/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Connect to Data Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Gemini Enterprise Data Cloud connectors let you connect your Gemini Enterprise apps directly to Google Cloud analytical and operational data sources. The following Data Cloud connectors are available:

  * BigQuery (available in [data ingestion mode](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-bigquery#data-ingestion) and [federated query mode](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-bigquery#federated-query) ([Preview](https://cloud.google.com/products#product-launch-stages)))
  * Spanner (available in [data ingestion mode](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-spanner#data-ingestion) and [federated query mode](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-spanner#federated-query) ([Preview](https://cloud.google.com/products#product-launch-stages)))
  * Cloud SQL (available in [data ingestion mode](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-cloud-sql#data-ingestion) and [federated query mode](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-cloud-sql#federated-query) ([Preview](https://cloud.google.com/products#product-launch-stages)))
  * AlloyDB for PostgreSQL (available in [data ingestion mode](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-alloydb#data-ingestion) and [federated query mode](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-alloydb#federated-query) ([Preview](https://cloud.google.com/products#product-launch-stages)))



When you connect a BigQuery, Spanner, Cloud SQL, or AlloyDB for PostgreSQL data store in **federated query mode** , [Knowledge Catalog](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-knowledge-catalog) ([Preview](https://cloud.google.com/products#product-launch-stages)) is automatically enabled on the **Assistant** tab of your Gemini Enterprise app—rather than as a separate data store—to give the agent tools to search for data that the user has access to and look up context.

## Use cases

Data Cloud connectors are built to power conversational analytics, enabling business users and analysts to ask questions in natural language, explore data, and generate insights in Gemini Enterprise apps. Example use cases include:

  * **BigQuery analytics** : Use natural language prompts to query and analyze structured data residing in BigQuery or that can be consumed in BigQuery. 
  * **Real-time operational database insights (Spanner, Cloud SQL, and AlloyDB for PostgreSQL)** : Run live analytical queries and authorized database operations across relational and distributed databases.



## How Data Cloud connectors work

In data ingestion mode, Data Cloud connectors copy data from the data source into the Gemini Enterprise data store.

In federated query mode, Data Cloud connectors query your data in place without copying or indexing it into a Gemini Enterprise data store:

  1. **Model Context Protocol (MCP) and per-user authentication** : Each Data Cloud connector is powered by a first-party (1P) MCP server. When a user asks a question, Gemini Enterprise authenticates the request using the user's own credentials (Identity and Access Management (IAM) permissions or OAuth 2.1) and executes queries directly against the underlying data source.
  2. **Semantic discovery and context retrieval with Knowledge Catalog** : When a user asks a data question, the Gemini Enterprise root agent uses built-in [Knowledge Catalog](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-knowledge-catalog) tools to search for data assets that the user has access to and look up context—including relevant tables, schemas, business glossary terms, and enriched metadata (derived from technical metadata, historical query patterns, and LLM inference).
  3. **Live query formulation and execution** : Using the schema and business context retrieved from Knowledge Catalog, the agent formulates a SQL query and invokes the connector's MCP tools to return governed, real-time results.

**Important:** **Data Cloud connectors are not scoped to specific resources.** When you attach a Data Cloud connector (such as the BigQuery connector) to an app, the connector is not restricted to a single dataset, table, or database instance—it can access **all resources in that data source that the authenticated user has permission to view or query**. To guide the agent toward specific datasets or business definitions, use Knowledge Catalog metadata, custom instructions, and agent skills. If your workload requires strict deterministic scoping to a specific database or table set for high accuracy, consider creating a scoped data agent for conversational analytics and publishing it to Gemini Enterprise instead.

## Benefits of first-party Data Cloud connectors over custom MCP servers

Compared to connecting to public or self-managed MCP servers using a generic custom MCP server data store, first-party Data Cloud connectors provide the following advantages:

  1. **Built-in skills for higher response quality** : First-party connectors include pre-configured agent skills tailored to each data engine — such as advanced SQL and AI function generation for BigQuery and databases — to improve query accuracy and response quality.
  2. **Streamlined setup and managed authentication** : First-party connectors provide a guided setup experience with managed authentication for Google Cloud databases and BigQuery, removing the need to deploy MCP middleware or manage your own OAuth client configuration for Google Cloud services. In addition, connector-specific settings — such as deterministically specifying a default Google Cloud billing project for BigQuery query execution — help administrators enforce governance and manage query costs.



## When to use Data Cloud connectors versus conversational analytics data agents

You can connect data to Gemini Enterprise using **Data Cloud connectors** (low-friction, broad-access connections directly in Gemini Enterprise) or **conversational analytics data agents** (purpose-built domain experts scoped to curated datasets for high accuracy).

The following table compares the two approaches to help you choose the approach for your use case:

Characteristic | Data Cloud connectors | Conversational analytics data agents  
---|---|---  
Best for | Broad, low-friction data access across multiple databases, data warehouses, and BI sources directly within Gemini Enterprise without upfront schema curation. | Curated, domain-specific analytics where high query accuracy is essential and a dedicated expert agent requires strict, deterministic scoping to specific data.  
Query accuracy and verification | Formulates queries dynamically across a broad schema using catalog metadata and general skills. Query accuracy can vary on complex or normalized relational database schemas without explicit table scoping or verified queries. | Uses curated schemas, focused table and column scoping, and verified queries (golden SQL) to provide high query accuracy and deterministic results on targeted datasets.  
Resource scoping | Broad access: Accesses all resources in the connected data source that the authenticated user has permission to query (guided by Knowledge Catalog and skills). | Deterministic scoping: Deterministically restricts the agent to a specific set of pre-selected datasets or tables.  
Multi-source queries and context | Can join and query across multiple connected data sources in a single conversation; the Gemini Enterprise root agent retains full context across the entire conversation and across all Gemini Enterprise experiences (chat, prompts, agent and workflow designers, and projects). | Each data agent is limited to a single data source (for example, a BigQuery data agent only queries BigQuery); users must discover and route to the specific agent, and subagent handoffs may not retain full root conversation context.  
Setup and maintenance | Quick configuration: Configure one connector per data source type to make all user-accessible data available immediately without manual schema curation. | Upfront curation trade-off: Requires selecting tables, defining metrics and KPIs, and authoring verified queries. This upfront curation yields deterministic, reliable query results.  
Performance and billing considerations | Discovering tables across a broad data estate can introduce additional latency and relies on well-maintained metadata and skills for accuracy. | Domain-curated context can yield higher accuracy on targeted workloads, but conversational analytics data agents incur data token charges.  
  
### Create and publish conversational analytics data agents

To achieve high query accuracy on relational databases and targeted business metrics, you can create and publish scoped conversational analytics data agents to Gemini Enterprise:

  * [Publish Spanner data agents to Gemini Enterprise](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/spanner/create-data-agents#publish-agent-gemini-enterprise)
  * [Publish Cloud SQL data agents to Gemini Enterprise](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-postgres/create-data-agents#publish-agent-gemini-enterprise)
  * [Publish AlloyDB for PostgreSQL data agents to Gemini Enterprise](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/alloydb/create-data-agents#publish-agent-gemini-enterprise)
  * [Conversational analytics in BigQuery](https://docs.cloud.google.com/bigquery/docs/conversational-analytics)



## Limitations

  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * Federated queries on relational databases have no table scoping or verified queries. Query accuracy can vary on complex transactional database (for example, AlloyDB for PostgreSQL, Cloud SQL, Spanner) schemas.



## What's next

  * To learn how the built-in analytical harness works and how to provide organizational context with skills and Knowledge Catalog, see [Best practices for Data Cloud connectors that use conversational analytics](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-best-practices).
  * To learn about supported security controls (DRZ, CMEK, and VPC Service Controls) and organization policy configuration, see [Secure Data Cloud connectors](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-security).
  * To learn how Knowledge Catalog works with Data Cloud connectors and how to manage it in your app's assistant configuration, see [Connect to Knowledge Catalog](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-knowledge-catalog).
  * To create and configure a connector with BigQuery, see [Connect to BigQuery](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-bigquery).
  * To create and configure a connector with Spanner, see [Connect to Spanner](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-spanner).
  * To create and configure a connector with Cloud SQL, see [Connect to Cloud SQL](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-cloud-sql).
  * To create and configure a connector with AlloyDB for PostgreSQL, see [Connect to AlloyDB for PostgreSQL](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-alloydb).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
