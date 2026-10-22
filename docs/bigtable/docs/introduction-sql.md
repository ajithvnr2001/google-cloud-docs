---
url: https://docs.cloud.google.com/bigtable/docs/introduction-sql/
title: Introduction to SQL \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:50.097297+00:00
---

# Introduction to SQL  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/introduction-sql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Introduction to SQL

In addition to its Admin and Data APIs, Bigtable supports SQL queries. You can use SQL to query your Bigtable data in the following ways:

  * For low-latency application development, GoogleSQL for Bigtable
  * For batch processing and ETL, Spark SQL
  * To analyze data from multiple sources, BigQuery



## GoogleSQL for Bigtable

GoogleSQL is a query language used by multiple Google Cloud services, including Spanner and BigQuery. You can create and run GoogleSQL queries, including queries that use [pipe syntax](https://docs.cloud.google.com/bigtable/docs/reference/sql/pipe-syntax), in [Bigtable Studio](https://docs.cloud.google.com/bigtable/docs/manage-data-using-console) in the Google Cloud console, or you can run them programmatically using one of the client libraries for Bigtable that support SQL queries. For more information, see [Use SQL with a Bigtable client library](https://docs.cloud.google.com/bigtable/docs/googlesql-overview#client-libraries).

GoogleSQL for Bigtable is similar to the Cassandra query Language (CQL) in many ways, and it includes a map data type, designed to query the Bigtable data stored in column families, columns, and cells.

To get started, see the [GoogleSQL for Bigtable overview](https://docs.cloud.google.com/bigtable/docs/googlesql-overview).

## Spark SQL

For data science use cases or other batch processing and ETL, the Bigtable Spark connector lets you read and write Bigtable data using Spark SQL. For more information, see [Use the Bigtable Spark connector](https://docs.cloud.google.com/bigtable/docs/use-bigtable-spark-connector).

## BigQuery

If you want to blend data from multiple sources, including Bigtable, and run batch, ad hoc analytics, you can create BigQuery external tables and run SQL queries from BigQuery. For more information, see [Query and analyze Bigtable data with BigQuery](https://docs.cloud.google.com/bigtable/docs/bigquery-analysis).

## What's next

  * [Write SQL with Gemini assistance.](https://docs.cloud.google.com/bigtable/docs/write-sql-gemini)
  * [Learn how to run queries in the Google Cloud console without SQL.](https://docs.cloud.google.com/bigtable/docs/query-builder)
  * [Explore the GoogleSQL for Bigtable reference documentation.](https://docs.cloud.google.com/bigtable/docs/reference/sql/functions-all)
  * [Compare tables and views.](https://docs.cloud.google.com/bigtable/docs/tables-and-views)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
