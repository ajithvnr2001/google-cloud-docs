---
url: https://docs.cloud.google.com/lakehouse/docs/conversational-analytics/
title: Query Lakehouse tables with natural language \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:02.606271+00:00
---

# Query Lakehouse tables with natural language  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/conversational-analytics/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Query Lakehouse tables with natural language Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Conversational analytics in [BigQuery](https://docs.cloud.google.com/bigquery/docs/conversational-analytics) lets you query your open-format data using natural language prompts. This capability relies on the _Lakehouse runtime catalog_ within _borderless Lakehouse_ to automatically map your questions to the underlying table schemas so you can generate and execute SQL queries without writing the code manually.

When setting up your queries, you can use Data Agents to provide business glossaries and system instructions for greater accuracy.

## How conversational analytics works

Conversational analytics uses large language models (LLMs) to understand your natural language questions and map them to the schema of your tables. The process follows these steps:

  1. **Schema discovery** : The system retrieves metadata from the Lakehouse runtime catalog to understand table structures, column names, and data types.
  2. **SQL generation** : The LLM generates a SQL query that is compatible with the BigQuery engine and the underlying data format.
  3. **Execution** : BigQuery executes the generated SQL query directly against the open-format data in Google Cloud's _Lakehouse_.
  4. **Response** : The results are returned to the conversational interface, often accompanied by a summary or visualization.



For more information about conversational analytics, such as managing data agents, pricing, or best practices, see [Conversational analytics overview](https://docs.cloud.google.com/bigquery/docs/conversational-analytics).

### Supported formats

Conversational analytics translates your natural language questions into SQL queries. It supports the [open table formats supported by the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint), such as Apache Iceberg tables.

## Before you begin

Before you can query your data, register your external tables in the Lakehouse runtime catalog. The Lakehouse runtime catalog acts as the unified hub that connects BigQuery Studio to your external open-format data. Once connected, the tables become discoverable assets within BigQuery.

## Query tables with conversational analytics

  1. In the Google Cloud console, go to the **BigQuery Studio Agents Hub**.

[Go to Agents Hub](https://console.cloud.google.com/bigquery/agents)

  2. Create a **Data Agent** or start a direct conversation with an existing data agent.

  3. **Select your tables**.

Because the Lakehouse runtime catalog unifies all these different formats, the discovery experience is identical to finding standard BigQuery tables.

     1. **Search** : When you add your knowledge source, look up your table names in the table search and selection interface. You can use search keywords to filter results, including:

        * `TABLE_NAME`
        * `catalog: CATALOG_NAME`
        * `project: PROJECT_ID`
        * `namespace: NAMESPACE_NAME`
     2. **Verify the source** : Pay attention to the dataset portion of the fully qualified name. Tables created by external sources and managed by the Lakehouse runtime catalog will typically follow a format combining the catalog and namespace. For example: `PROJECT_ID.biglake_catalog.finance_namespace.my_iceberg_table` or `PROJECT_ID.sap_catalog.sales.delta_table`.

     3. **Select** : Add the selected table to your active conversational context.

  4. Ask questions in natural language. The system automatically translates your prompt into a federated SQL query.




## Improve query accuracy

To help conversational analytics better understand your schemas and terminology, use Data Agent configuration options. These options include business glossaries, verified SQL queries, and system instructions.

## What's next

  * Learn more about [conversational analytics in BigQuery](https://docs.cloud.google.com/bigquery/docs/conversational-analytics).
  * Learn how to [register external tables in the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog).
  * Learn more about [Data Agents](https://docs.cloud.google.com/bigquery/docs/create-data-agents).
  * Try the tutorial [Forecast demand from customer feedback using Lakehouse and AI](https://docs.cloud.google.com/lakehouse/docs/forecast-demand-customer-feedback-tutorial).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
