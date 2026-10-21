---
url: https://docs.cloud.google.com/knowledge-catalog/docs/data-insights-structured-data/
title: About data insights for structured data \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:37:02.181292+00:00
---

# About data insights for structured data  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/data-insights-structured-data/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  About data insights for structured data Stay organized with collections  Save and categorize content based on your preferences. 

The Knowledge Catalog (formerly Dataplex Universal Catalog) data insights feature automatically generates descriptions, relationship graphs, and SQL queries from your table and dataset metadata. This information helps you quickly understand data structure, content, and relationships without extensive manual setup. To investigate further, you can ask follow-up questions in [data canvas](https://docs.cloud.google.com/bigquery/docs/data-canvas).

When exploring a new, unfamiliar table, data analysts often face difficulty knowing how to start writing queries. The problem can involve uncertainties about the data structure and key patterns in the data. The Knowledge Catalog data insights feature offers an automated way to explore and understand your data. This lets you uncover patterns, assess data quality, and perform statistical analysis.

**Note:** To provide feedback on this feature, email [dataplex-data-insights-help@google.com](mailto:dataplex-data-insights-help@google.com).

## Overview

Data insights use Gemini to analyze your metadata and generate the following:

  * Descriptions: AI-generated summaries explaining the purpose of the dataset or namespace, the structure of the table, and the details of specific columns.

  * Sample queries: Tailored SQL queries designed specifically for the schema and content of your dataset, namespace, or table.

  * Relationship graphs: Visualizations that show the connections and dependencies between different tables within your dataset or namespace.




## Supported resources

Data insights are available for the following structured data types:

  * BigQuery datasets, tables, and views
  * Borderless Lakehouse tables (including Apache Iceberg, Apache Hive, and SAP BDC)
  * External tables
  * Apache Iceberg REST Catalog tables
  * Apache Iceberg namespaces (represented as datasets in BigQuery)
  * Apache Hive catalog tables
  * SAP Business Data Cloud (BDC) tables



## Example of an insights run

Data insights automatically generates natural language queries and their SQL equivalents based on a table's metadata.

Consider a table called `telco_churn` with the following schema:

Field name | Type  
---|---  
CustomerID | `STRING`  
Gender | `STRING`  
Tenure | `INT64`  
InternetService | `STRING`  
StreamingTV | `STRING`  
OnlineBackup | `STRING`  
Contract | `STRING`  
TechSupport | `STRING`  
PaymentMethod | `STRING`  
MonthlyCharges | `FLOAT`  
Churn | `BOOLEAN`  
  
The following are some of the sample queries that data insights generates for this table:

  * Identify customers who have subscribed to all premium services and have been a customer for more than 50 months.
        
        SELECT
          CustomerID,
          Contract,
          Tenure
        FROM
          agentville_datasets.telco_churn
        WHERE
          OnlineBackup = 'Yes'
          AND TechSupport = 'Yes'
          AND StreamingTV = 'Yes'
          AND Tenure > 50;
        

  * Identify which internet service has the most churned customers.
        
        SELECT
          InternetService,
          COUNT(DISTINCT CustomerID) AS total_customers
        FROM
          agentville_datasets.telco_churn
        WHERE
          Churn = TRUE
        GROUP BY
          InternetService
        ORDER BY
          total_customers DESC
        LIMIT 1;
        

  * Identify churn rates by segment among high-value customers.
        
        SELECT
          Contract,
          InternetService,
          Gender,
          PaymentMethod,
          COUNT(DISTINCT CustomerID) AS total_customers,
          SUM(CASE WHEN Churn = TRUE THEN 1 ELSE 0 END) AS churned_customers,
          (SUM(CASE WHEN Churn = TRUE THEN 1 ELSE 0 END) / COUNT(DISTINCT CustomerID))
          * 100 AS churn_rate
        FROM
          agentville_datasets.telco_churn
        WHERE
          MonthlyCharges > 100
        GROUP BY
          Contract,
          InternetService,
          Gender,
          PaymentMethod;
        




## Modes for generating data insights

When generating data insights, Knowledge Catalog provides two modes:

Mode | Description | Usage  
---|---|---  
**Generate and publish** |  Persists generated data insights into Knowledge Catalog as metadata aspects. You must have the necessary permissions to publish. When you use **Generate and publish** , the following actions occur:

  * Stores table and column descriptions in Knowledge Catalog.
  * Captures suggested queries and questions as reusable aspects.
  * Makes published insights accessible to all users who have appropriate Knowledge Catalog access, ensuring shared organizational knowledge.
  * Lets you edit and save descriptions directly in Knowledge Catalog.

|  Use this mode for enterprise-wide data documentation that persists and is reusable, or when building catalog-driven governance workflows.  
**Generate without publishing** |  Creates data insights such as descriptions, natural language questions, and SQL queries on demand. **Generate without publishing** doesn't publish insights to Knowledge Catalog. |  Use this mode for quick, ad hoc exploration to avoid cluttering the catalog.  
  
## Pricing

For details about pricing for this feature, see [Data Cloud Agent pricing](https://cloud.google.com/products/data-agents/pricing).

To track token consumption for data insights scan jobs and build custom dashboards in Cloud Monitoring, see [Monitor data insights token usage](https://docs.cloud.google.com/knowledge-catalog/docs/monitor-insights-token-usage).

## Locations

You can use data insights in all [BigQuery locations](https://docs.cloud.google.com/bigquery/docs/locations). To learn about where Gemini in BigQuery processes your data, see [Where Gemini in BigQuery processes your data](https://docs.cloud.google.com/bigquery/docs/gemini-locations).

## Limitations

  * For multi-cloud customers, data from other clouds isn't available.
  * Data insights doesn't support `Geo` or `JSON` column types.
  * Insights runs don't guarantee the presentation of queries every time. To increase the likelihood of generating more engaging queries, regenerate insights in BigQuery Studio.



## What's next

  * Learn how to [generate insights in BigQuery](https://docs.cloud.google.com/bigquery/docs/data-insights#insights-bigquery-table).
  * Learn how to [monitor data insights token usage](https://docs.cloud.google.com/knowledge-catalog/docs/monitor-insights-token-usage).
  * Learn how to [generate a data profiling scan](https://docs.cloud.google.com/knowledge-catalog/docs/use-data-profiling).
  * Learn how to [write queries with Gemini assistance in BigQuery](https://docs.cloud.google.com/bigquery/docs/write-sql-gemini).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
