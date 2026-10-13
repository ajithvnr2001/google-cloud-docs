---
url: https://docs.cloud.google.com/bigtable/docs/manage-data-using-console/
title: Manage your data using Bigtable Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:51.889157+00:00
---

# Manage your data using Bigtable Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/manage-data-using-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage your data using Bigtable Studio

This page explains how to explore and manage your Bigtable data using Bigtable Studio in the Google Cloud console.

Bigtable Studio includes an **Explorer** pane that integrates with the following:

  * Query builder, an interactive form that lets you build and run a query without writing code
  * Query editor, where you can create and execute SQL commands
  * SQL query results table



If you're new to Bigtable, learn how to [create an instance and write data with the `cbt` CLI ](https://docs.cloud.google.com/bigtable/docs/create-instance-write-data-cbt-cli).

## Required roles

To get the permissions that you need to query a table, ask your administrator to grant you the following IAM roles on the instance that contains the table: 

  * All: [Bigtable reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigtable#bigtable.reader) (`roles/bigtable.reader`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Explore your data

You can use the explorer to perform the following actions on your Bigtable resources:

Bigtable resource | Explorer actions  
---|---  
Table | 

  * Create a new table
  * Create a backup
  * Prevent deletion
  * Edit
  * Delete
  * View a sample query
  * View backups
  * Monitor by viewing system insights
  * Export to Cloud Storage

  
Column families | 

  * Add a column family to a table

  
Specific column family | 

  * Edit a garbage collection policy
  * Identify [aggregate](https://docs.cloud.google.com/bigtable/docs/aggregates) column families. Aggregate column families have a functions function icon and an aggregation type, such as `Sum`. To view the details of an aggregate column family, hover over its name. 

  
Authorized view | 

  * Open in the query builder
  * Grant access
  * Delete

  
Logical view | 

  * View definition in the query editor

  
Continuous materialized view | 

  * View definition in the query editor
  * Enable or disable deletion protection

  
  
To access the **Explorer** , follow these steps:

  1. In the Google Cloud console, open the **Bigtable instances** page.

[Go to instances list](https://console.cloud.google.com/bigtable)

  2. Select an instance from the list.

  3. In the navigation menu, click **Bigtable Studio**. The **Explorer** pane displays a list of tables and authorized views in the instance.




## Search resources

In the **Explorer** pane, use the **Search** field to search for all Bigtable resources except for authorized views and column families.

## Query your data in the query builder

The query builder is an interactive form that lets you send read requests to the Bigtable Data API from the Google Cloud console without needing to write code or SQL statements. For more information, see [Build queries in the console](https://docs.cloud.google.com/bigtable/docs/query-builder).

## Query your data with SQL in the query editor

Using the query editor, you can run any combination of SQL `SELECT` statements, including statements that use [pipe syntax](https://docs.cloud.google.com/bigtable/docs/reference/sql/pipe-syntax).

**Note:** You can't use a [Data Boost](https://docs.cloud.google.com/bigtable/docs/data-boost-overview) app profile with the query editor.

To query your data, follow these steps:

  1. In the Google Cloud console, open the **Bigtable instances** page.

[Go to instances list](https://console.cloud.google.com/bigtable)

  2. Select an instance from the list.

  3. In the navigation menu, click **Bigtable Studio**.

  4. Compose a query:

     1. Open a new tab by clicking add and then choosing **Editor**.
     2. When the query editor appears, write your query. If the query is valid SQL, a **Valid** message is displayed.
     3. Optional: To return all cells in the queried columns instead of only the most recent cell, append the table ID with `(with_history => TRUE)`.
  5. Optional: To format your statement in SQL style, click **Format**.

  6. Click **Run**. The results of your query appear in the **Results** table.

If your query targets tables with aggregate column families, GoogleSQL automatically decodes the aggregate cells for the results table:

     * **Sum** , **Min** , and **Max** : values are returned as structured JSON objects, such as `{ "sum_column": 8 }`.
     * **HyperLogLog (HLL)** : HLL values represent probabilistic sets. If you select a column that contains HLL data using SQL, the results are returned as raw bytes or base64. To estimate the unique cardinalities (counts) for HLL columns, you must use GoogleSQL [HLL++ functions](https://docs.cloud.google.com/bigtable/docs/reference/sql/hll_functions), such as `HLL_COUNT.EXTRACT` or `HLL_COUNT.MERGE`.
  7. To view a formatted display of a row's data, click the row in the results table. The **Row details** pane opens. Each column qualifier and its value are displayed on a new line. If you run the query using `(with_history => TRUE)`, each cell in a column is presented as a struct that includes the value and timestamp for the cell.

  8. Optional: To run only a selected portion of the text in the editor, highlight it, and then click **Run selected**. The results of the highlighted query appear in the **Results** table.




To remove all text from the query editor, click **Clear**.

For more information, including examples, about crafting SQL statements to query your Bigtable data, see the [GoogleSQL for Bigtable overview](https://docs.cloud.google.com/bigtable/docs/googlesql-overview).

## Export query results

You can export the results of your query in one of the following ways:

  * Download a local file in a CSV or JSON format.
  * Export to Google Sheets.
  * Copy to clipboard in a CSV, TSV, or JSON file format.



To export query results from the query editor or the query builder, follow these steps:

  1. In the Google Cloud console, open the **Bigtable instances** page.

[Go to instances list](https://console.cloud.google.com/bigtable)

  2. Select an instance from the list.

  3. In the navigation menu, click **Bigtable Studio**.

The **Explorer** pane displays a list of tables, views, and queries in the instance.

  4. Run your query from either the **Builder** or the **Editor** tab.

The results appear in the **Results** table.

  5. On the **Results** toolbar, click **Export**.

  6. From the menu, select one of the export options.

If you selected **Export to Google Sheets** , a dialog appears. Click **Open** to view your results in Google Sheets.




## Create views

Bigtable Studio lets you create and save views of your Bigtable tables. For details, see the documentation for each view type.

### Authorized views

You can use the query builder to create and save [authorized views](https://docs.cloud.google.com/bigtable/docs/authorized-views), which are table subsets that you grant access to separately from access to the table. You can also grant access and delete authorized views in Bigtable Studio, using the **Action** menu in the **Explorer** pane.

For more information, see [Create and manage authorized views](https://docs.cloud.google.com/bigtable/docs/authorized-views-create-manage).

### Continuous materialized views

You can use the query editor to create a continuous materialized view, a precomputed result of a continuously running SQL query that synchronizes with its source table with incremental updates. Continuous materialized views often contain aggregated data based on values in their source tables.

For more information, see the following documentation:

  * [Continuous materialized views](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views)
  * [Create and manage continuous materialized views](https://docs.cloud.google.com/bigtable/docs/manage-continuous-materialized-views)
  * [Continuous materialized view queries](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-view-queries)



### Logical views

You can use the query editor to create a logical view, a saved query that can be queried like a table. Logical view operations require permissions beyond those granted in `roles/bigtable.reader`. For more information, see [Create and manage logical views](https://docs.cloud.google.com/bigtable/docs/create-manage-logical-views).

#### Parameterized views

You can also use the query editor to create a _parameterized view_ , which extends the capabilities of logical views to filter down to specific data ranges based on application-provided context, especially in applications that use AI agents or large language models (LLMs). For more information, see [Parameterized views overview](https://docs.cloud.google.com/bigtable/docs/parameterized-views-overview).

## Saved queries

**Preview — Saved queries**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can use Bigtable Studio to create, save, and manage SQL scripts as saved queries. For more information, see the following documentation:

  * [Saved queries overview](https://docs.cloud.google.com/bigtable/docs/saved-queries)
  * [Create and manage saved queries](https://docs.cloud.google.com/bigtable/docs/create-manage-saved-queries)



## What's next

  * [Learn additional ways to use SQL with Bigtable.](https://docs.cloud.google.com/bigtable/docs/introduction-sql)
  * [Work through a quickstart using the `cbt` CLI .](https://docs.cloud.google.com/bigtable/docs/create-instance-write-data-cbt-cli)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
