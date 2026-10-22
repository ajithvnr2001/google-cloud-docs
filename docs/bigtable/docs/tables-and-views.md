---
url: https://docs.cloud.google.com/bigtable/docs/tables-and-views/
title: Tables and views \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:51.860036+00:00
---

# Tables and views  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/tables-and-views/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Tables and views

Bigtable stores your data in tables and lets you create specialized views—logical views, continuous materialized views, and authorized views—of your tables. Depending on your use case, these views help you simplify SQL query patterns, precompute aggregations, and enforce fine-grained access control.

## Tables

A Bigtable _table_ is a sorted key-value map that stores data in rows and columns. Each row is indexed by a single, unique _row key._ Columns that are related to one another are typically grouped into a _column family_.

Bigtable has a flexible data model, and its tables are _sparse_. This means that if a column is unused in a row, no data is stored for the column. You don't need to store NULL values for unused columns like you would with a relational database. In a Bigtable table, a given row might have one column and the row next to it 100 columns.

In a row, a column can contain multiple cells, each identified by the four-tuple (row key, column family, column qualifier, timestamp). Storing multiple cells in a column provides a record of how the stored data for that row and column has changed over time.

A Bigtable table doesn't support joins, and transactions are supported only within a single row.

A table is an instance-level resource that is automatically replicated to every cluster in the instance. Data retention is controlled with _garbage collection_ policies that are set at the column-family level.

For more information, see the [Bigtable overview](https://docs.cloud.google.com/bigtable/docs/overview) and [Schema design best practices](https://docs.cloud.google.com/bigtable/docs/schema-design).

## Views

Bigtable supports the following types of table views: logical views, continuous materialized views, and authorized views. Views let you share table data with particular users and groups without giving them access to the underlying source data.

### Logical views

A _logical view_ – often referred to as just a _view_ – is the result of a SQL query. It functions as a virtual table that can be queried by other SQL queries. For more information, see [Create and manage logical views](https://docs.cloud.google.com/bigtable/docs/create-manage-logical-views).

#### Parameterized views

A _parameterized view_ is a type of logical view that dynamically filters data ranges based on application context. This approach protects your applications from SQL injection and reduces the need for multiple static views.

For more information, see [Parameterized views overview](https://docs.cloud.google.com/bigtable/docs/parameterized-views-overview).

### Continuous materialized views

A _continuous materialized view_ is created by continuously running a SQL query against a Bigtable table. Bigtable creates a new table based on the query output and keeps it in sync with the source table.

Continuous materialized views can help improve query performance. The new table – the continuous materialized view – has a different schema than the source table, containing pre-aggregated or transformed data that is optimized for different queries than those used on the source table.

Continuous materialized views are read-only. You are charged for storage of a continuous materialized view as well as for the processing work that goes into creating the second table, keeping it in sync with the source table, and replicating it.

For more information, see [Continuous materialized views](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views).

### Authorized views

_Authorized views_ are views of tables that you configure to include specific table data and then grant access to separately from access to the source table. An authorized view is defined by a JSON-formatted definition file.

Unlike continuous materialized views or logical views, Bigtable authorized views can be used to control both read and write access.

Authorized views are useful in cases where you store data for multiple customers in a Bigtable table, and you want to grant each customer access only to a subset of the table that contains their data.

Authorized views don't incur additional storage costs.

For more information, see the [Authorized views overview](https://docs.cloud.google.com/bigtable/docs/authorized-views).

### Comparisons

The following table provides additional information about how Bigtable table views differ from each other.

| **Logical views** | **Parameterized views** | **Continuous materialized views** | **Authorized views**  
---|---|---|---|---  
**Structure** | Virtual table representing the results of a SQL query | Virtual table representing the results of a SQL query | Read-only table based on a source table | Subset of a table  
**Definition** | SQL query | SQL query using `VIEW_PARAMETERS()` | SQL query | JSON definition file  
**Consistency with source table** | Consistent when the query is run | Consistent when the query is run | Eventually consistent  | Consistent when the query is run  
**Query options** | Must use SQL | SQL | SQL or Bigtable Data API | Bigtable Data API  
**Writeable** | No | No | No | Yes  
**Storage** | Data remains in the source table | Data remains in the source table | Data is duplicated, aggregated, or transformed and stored in a new read-only table | Data remains in the source table  
**Usage costs** | Compute processing to execute the query | Compute processing to execute the query | Compute processing when syncing, storage costs | Compute processing to execute the query  
  
## What's next

  * [Instances, clusters, and nodes](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes)
  * [Introduction to SQL in Bigtable](https://docs.cloud.google.com/bigtable/docs/introduction-sql)
  * [Bigtable access control with IAM](https://docs.cloud.google.com/bigtable/docs/access-control)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
