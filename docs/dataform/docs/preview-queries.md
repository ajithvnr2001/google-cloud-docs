---
url: https://docs.cloud.google.com/dataform/docs/preview-queries/
title: Preview SQL queries \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:22.688749+00:00
---

# Preview SQL queries  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/preview-queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback 

#  Preview SQL queries Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to preview output of a SQL query in a Dataform workspace before executing the query to BigQuery.

## About query preview in Dataform

When you develop a query in a SQLX or JavaScript file with [Dataform core](https://docs.cloud.google.com/dataform/docs/overview#dataform-core), Dataform compiles the query to SQL in real-time. To test the output of the compiled SQL query before you run it to BigQuery, you can preview the query in your Dataform workspace.

When you preview a query, Dataform runs a job in BigQuery to run your compiled query in a temporary destination table and display query results in your workspace. You can inspect the output of the query before you trigger execution to publish your table to BigQuery. The temporary table with the previewed query is automatically deleted in up to 24 hours. For more information about BigQuery jobs, see [Manage jobs](https://docs.cloud.google.com/bigquery/docs/managing-jobs).

**Warning:** Clicking **Run** to preview a query doesn't execute code within the `pre_operations` or `post_operations` blocks. Furthermore, any dependencies—for example, temporary tables—created within the `pre_operations` or `post_operations` blocks aren't available during the preview. Errors might occur in the main query body if it relies on these missing dependencies.

Running query preview in Dataform incurs billing in BigQuery. For more information about BigQuery pricing, see [BigQuery pricing](https://cloud.google.com/bigquery/pricing).

During query preview, Dataform uses your Google Account user credentials to run jobs in BigQuery. During workflow execution, [strict act-as mode](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode) requires Dataform to use a custom service account or Google Account user credentials to create or update assets in BigQuery.

Dataform displays results of all queries previewed during the current browser session in the **Query results** panel in your workspace. In the **Query results** panel, you can view the following information about each query previewed during the current browser session:

  * Job information 
    * BigQuery job ID
    * User running the preview
    * Location where the job runs, taken from your [workflow settings file](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings)
    * Creation, start, and end times of the BigQuery job
    * Duration of the BigQuery job
    * Bytes processed
    * Bytes billed in BigQuery
    * Job priority
    * Use of [legacy SQL](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/introduction) in the query
    * Temporary destination table of the query
  * Results of the query
  * JSON representation of the query output



Moreover, in the **Query results** panel, you can navigate to the source file of each previewed query, and navigate to BigQuery Studio to view the preview job.

## Before you begin

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Select or [create a repository](https://docs.cloud.google.com/dataform/docs/create-repository).

  3. Select or [create a development workspace](https://docs.cloud.google.com/dataform/docs/create-workspace).

  4. Create a SQL query, for example, [create a table](https://docs.cloud.google.com/dataform/docs/create-tables#create-table).




### Required roles

To get the permissions that you need to preview queries, ask your administrator to grant you the following IAM roles: 

  * [Dataform Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.editor) (`roles/dataform.editor`) on workspaces
  * [BigQuery Job User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`) on the project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Preview a query

To inspect query results in Dataform before execution, run a preview of a query in your workspace. If the file you edit contains multiple queries, select the query that you want to preview. You can preview one query at a time.

Running a preview is a little different for tables with assertions. For more information, see Preview a table with assertions.

To preview a SQL query and view query results in a Dataform workspace, follow these steps:

  1. In the **Files** pane, expand `definitions/`.
  2. Select a SQLX or JavaScript file.
  3. Click **Run**.

     1. If the file contains multiple queries, in the menu, select the query that you want to preview.
  4. Inspect results of the preview in the **Query results** panel.

     1. To inspect job details, select the **Job information** tab.
     2. To inspect query results, select the **Results** tab.
     3. To view the JSON output of the query, select the **JSON** tab.
     4. To view the preview job in SQL workspace, click the more_vert **More** menu > **View job in SQL workspace**.



### Preview a table with assertions

In a SQLX table definition file with assertions, you can preview the table creation query and the defined assertion queries.

Dataform treats the table definition query as the default query. To preview the table creation query, click **Run** in your workspace. To preview an assertion query, select it in the menu next to the **Run** button. You can preview one query at a time.

To preview a query in a table definition file with assertions in a Dataform workspace, follow these steps:

  1. In the **Files** pane, expand `definitions/`.
  2. Select a definition file of a table with assertions.
  3. Run a preview: 
     * To preview the table creation query, click **Run**.
     * To preview an assertion query, click the drop-down icon next to **Run** , and then select the query that you want to preview.
  4. Inspect results of the preview in the **Query results** panel. 
     1. To inspect job details, select the **Job information** tab.
     2. To inspect query results, select the **Results** tab.
     3. To view the JSON output of the query, select the **JSON** tab.
     4. To view the preview job in SQL workspace, click the more_vert **More** menu > **View job in SQL workspace**.



## What's next

  * To learn more about BigQuery pricing, see [BigQuery Pricing](https://cloud.google.com/bigquery/pricing).
  * To learn more about Dataform pricing, see [Pricing](https://cloud.google.com/dataform/pricing).
  * To learn more about workspaces in Dataform, see [Create a development workspace](https://docs.cloud.google.com/dataform/docs/create-workspace).
  * To learn how to test table queries with assertions, see [Test tables with assertions](https://docs.cloud.google.com/dataform/docs/assertions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
