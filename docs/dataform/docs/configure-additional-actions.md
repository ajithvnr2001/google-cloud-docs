---
url: https://docs.cloud.google.com/dataform/docs/configure-additional-actions/
title: Configure additional actions \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:46.852212+00:00
---

# Configure additional actions  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/configure-additional-actions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback 

#  Configure additional actions Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to do the following:

  * Define a SQL statement to be run before table creation.
  * Define a SQL statement to be run after table creation.
  * Disable table creation.
  * Add execution tags.



## Before you begin

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Select or [create a repository](https://docs.cloud.google.com/dataform/docs/create-repository).

  3. Select or [create a development workspace](https://docs.cloud.google.com/dataform/docs/create-workspace).

  4. [Create a table](https://docs.cloud.google.com/dataform/docs/create-tables#create-table).

  5. Define a SQLX file of any of the following types:

     * [`type: table`](https://docs.cloud.google.com/dataform/docs/create-tables#create-table)
     * [`type: view`](https://docs.cloud.google.com/dataform/docs/create-tables#create-table)
     * [`type: incremental`](https://docs.cloud.google.com/dataform/docs/create-tables#create-table)
     * [`type: assertion`](https://docs.cloud.google.com/dataform/docs/assertions)
     * [`type: operations`](https://docs.cloud.google.com/dataform/docs/custom-sql)



### Required roles

To get the permissions that you need to complete the tasks in this document, ask your administrator to grant you the following IAM roles: 

  * [Dataform Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.editor) (`roles/dataform.editor`) on the workspace
  * To synchronize metadata to Knowledge Catalog: [Dataplex Catalog Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`) on the project or `@bigquery` entry group 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Define a SQL statement to be run before table creation

You can configure Dataform to run one or more SQL statements before creating a selected table in BigQuery. To run a SQL statement before Dataform creates a selected table, add your statement to the `pre_operations` block in the table definition SQLX file.

To create a custom SQL statement that's run before Dataform creates a specific table, follow these steps:

  1. Go to your development workspace.
  2. In the **Files** pane, expand `definitions/`.
  3. Open a SQLX table definition file.
  4. Outside the `config` block, enter `pre_operations { ... }`.
  5. Inside `pre_operations { ... }`, add your SQL statement.
  6. Optional: To add multiple statements, separate them with `---`.
  7. Optional: Click **Format**.



The following code sample shows a `pre_operations` statement that creates a temporary function that can be used in the select statement:
    
    
    pre_operations {
      CREATE TEMP FUNCTION AddFourAndDivide(x INT64, y INT64)
        RETURNS FLOAT64
        AS ((x + 4) / y);
    }
    

## Define a SQL statement to be run after table creation

You can configure Dataform to run one or more SQL statements after creating a selected table in BigQuery. To run a SQL statement after Dataform creates a selected table, add your statement to the `post_operations` block in the table definition SQLX file. You can add multiple SQL statements to the `post_operations` block.

To create a custom SQL statement that's run after Dataform creates a specific table, follow these steps:

  1. Go to your development workspace.
  2. In the **Files** pane, expand `definitions/`.
  3. Open a SQLX table definition file.
  4. Outside the `config` block, enter `post_operations { ... }`.
  5. Inside `post_operations { ... }`, add your SQL statement.
  6. Optional: Click **Format**.



The following code sample shows `post_operations` statements that grant groups access to the created table:
    
    
      post_operations {
        GRANT `roles/bigquery.dataViewer`
        ON
        TABLE ${self()}
        TO "group:allusers@example.com", "user:otheruser@example.com"
      }
    

### Automated metadata enrichment

Dataform supports automated metadata enrichment for BigQuery tables and views created with SQLX workflows. When a table action completes successfully, Dataform attempts to write the defined metadata to the corresponding Knowledge Catalog entry. This process is decoupled from the SQL execution in the following ways:

  * **Latency** : the sync is asynchronous, meaning, your BigQuery jobs don't wait for the Knowledge Catalog update to finish.
  * **Reliability** : if the sync fails (for example, due to API rate limits), Dataform retries the update automatically. A failed metadata update doesn't cause your Dataform action or workflow to fail.



The following code sample shows you how to define metadata for Knowledge Catalog in the config block of a SQLX file:
    
    
    config {
      type: "table",
      metadata: {
        overview: "This table provides standardized trip data.",
        extraProperties: {
          generic: {
            system: "BigQuery",
            type: "table"
          }
        }
      }
    }
    

To check the status of a metadata update, follow the instructions in [Inspect workspace execution logs](https://docs.cloud.google.com/dataform/docs/monitor-runs#inspect-workspace-execution-logs).

To view the enriched metadata, you can search for your BigQuery tables and views in Knowledge Catalog. For more information, see [Search for resources](https://docs.cloud.google.com/dataplex/docs/search-assets#search-data-assets).

## Disable table creation

To stop Dataform from creating a selected table in BigQuery, you can disable the table in its SQLX table definition file. Dataform keeps a disabled table in the dependency graph, but it does not compile and create it. This can be useful, for example, if a table fails and you don't want your whole workflow to fail while you fix the issue.

To disable a table, follow these steps:

  1. Go to your development workspace.
  2. In the **Files** pane, expand `definitions/`.
  3. Select a SQLX table definition file.
  4. In the `config` block of the file, enter `disabled: true`.
  5. Optional: Click **Format**.



The following code sample shows a disabled table:
    
    
    config {
      type: "table",
      disabled: true
    }
    
    select * from ${ref("source_data")}
    

## Add execution tags

This section shows you how to add tags to [Dataform core](https://docs.cloud.google.com/dataform/docs/overview#dataform-core) SQLX files to categorize your workflow.

To organize the components of your workflow into collections, you can add custom tags to SQLX files of the following types:

  * `table`
  * `view`
  * `incremental`
  * `assertion`
  * `operations`



During a workflow run, you can [run only files with a selected tag](https://docs.cloud.google.com/dataform/docs/trigger-execution).

With [Managed Service for Apache Airflow](https://docs.cloud.google.com/dataform/docs/schedule-runs#composer) or [Workflows together with Cloud Scheduler](https://docs.cloud.google.com/dataform/docs/schedule-runs#workflows-cloud-scheduler), you can create a schedule that runs a Dataform workflow with a selected tag at a specific interval.

### Add a tag

You can add multiple tags to a SQLX file.

To add a tag to a SQLX file, follow these steps:

  1. Go to your development workspace.
  2. In the **Files** pane, expand `definitions/`.
  3. Select a SQLX file.
  4. In the `config` block, add a tag in the following format:
         
         tags: ["CUSTOM_TAG"]
         

Replace `CUSTOM_TAG` with your tag.

  5. Optional: To add multiple tags, separate them with a comma (`,`).

  6. Optional: Click **Format**.




The following code sample shows the `user_counts` view with the `daily` and `hourly` tags:
    
    
    config {
      type: "view",
      name: "user_counts",
      tags: ["daily", "hourly"]
    }
    

## What's next

  * To learn how to configure Dataform settings in `workflow_settings.yaml`, see [Configure Dataform workflow settings](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings).
  * To learn how to test table data with assertions, see [Test data quality](https://docs.cloud.google.com/dataform/docs/assertions).
  * To learn how to reuse code with includes, see [Reuse code across a single repository with includes](https://docs.cloud.google.com/dataform/docs/javascript-in-dataform#reuse_code_across_a_single_repository_with_includes).
  * To learn to manually trigger executions, see [Manually trigger runs](https://docs.cloud.google.com/dataform/docs/trigger-execution).
  * To learn how to add BigQuery policy tags in Dataform, see [Control column access](https://docs.cloud.google.com/dataform/docs/policy-tags).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
