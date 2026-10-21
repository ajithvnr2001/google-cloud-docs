---
url: https://docs.cloud.google.com/dataform/docs/overview/
title: Dataform overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:35:01.053107+00:00
---

# Dataform overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback 

#  Dataform overview Stay organized with collections  Save and categorize content based on your preferences. 

This document introduces you to Dataform concepts and processes.

Dataform is a service for data analysts to develop, test, control versions, and schedule complex workflows for data transformation in BigQuery.

Dataform lets you manage data transformation in the Extraction, Loading, and Transformation (ELT) process for data integration. After raw data is extracted from source systems and loaded into BigQuery, Dataform helps you to transform it into a well-defined, tested, and documented suite of data tables.

Dataform lets you perform the following data transformation actions:

  * Develop and run workflows for data transformation.
  * Collaborate with team members on workflow development through Git.
  * Manage a large number of tables and their dependencies.
  * Declare source data and manage table dependencies.
  * View a visualization of the dependency tree of your workflow.
  * Manage data with SQL code in a central repository.
  * Reuse code with JavaScript.
  * Test data correctness with quality tests on source and output tables.
  * Version control SQL code.
  * Document data tables inside SQL code.



### Data transformation processes in Dataform

The data transformation workflow for Dataform is as follows:

  1. Dataform lets you create repositories to manage your code.
  2. Dataform lets you create workspaces for development.
  3. Dataform lets you develop workflows in a development workspace.
  4. Dataform compiles Dataform core into SQL.
  5. Dataform runs the dependency tree.



#### Dataform lets you create repositories to manage your code

In a Dataform repository, you use Dataform core, an extension of SQL, to write SQLX files in which you define your workflow. Dataform repositories support version control. You can link a Dataform repository to a [third-party Git provider](https://docs.cloud.google.com/dataform/docs/connect-repository).

#### Dataform lets you create workspaces for development

You can create development workspaces inside a Dataform repository for Dataform core development. In a development workspace, you can make changes to the repository, compile, test, and push them to the main repository through Git.

#### Dataform lets you develop Dataform core in a development workspace

In a development workspace, you can define and document tables, their dependencies, and transformation logic to build your workflow. You can also [configure actions in JavaScript](https://docs.cloud.google.com/dataform/docs/javascript-in-dataform).

#### Dataform compiles Dataform core

During compilation, Dataform performs the following tasks:

  * Compiles Dataform core into a workflow of Standard SQL.
  * Adds boilerplate SQL statements, such as `CREATE TABLE` or `INSERT`, to the code inline with your query configuration.
  * Transpiles (compiles source-to-source) JavaScript into SQL.
  * Resolves dependencies and checks for errors including missing or circular dependencies.
  * Builds the dependency tree of all actions to be run in BigQuery.



Dataform compilation is hermetic to verify compilation consistency, meaning that the same code compiles to the same SQL compilation result every time. Dataform compiles your code in a sandbox environment with no internet access. No additional actions, such as calling external APIs, are available during compilation.

To debug in real-time, you can inspect the compiled workflow of your project in an interactive graph in your development workspace.

#### Dataform runs the dependency tree

In BigQuery, Dataform performs the following tasks:

  * Runs SQL commands, following the order of the dependency tree.
  * Runs assertion queries against your tables and views to check data correctness.
  * Runs other SQL operations that you defined.
  * Updates metadata in Knowledge Catalog.



After the execution, you can use your tables and views for all your analytics purposes.

You can [view logs](https://docs.cloud.google.com/dataform/docs/monitor-runs#monitor-execution-logs) to see what tables were created, if assertions passed or failed, how long each action took to complete, and other information. You can also view the exact SQL code that was run in BigQuery.

## Dataform features

With Dataform, you can develop and deploy tables, incremental tables, or views to BigQuery. Dataform offers a web environment for the following activities:

  * Workflow development
  * Connection with GitHub, GitLab, Azure DevOps Services, and Bitbucket
  * Continuous integration and continuous deployment
  * Workflow execution



The following sections describe the main features of Dataform.

### Repositories

Each Dataform project is stored in a [repository](https://docs.cloud.google.com/dataform/docs/repositories). A Dataform repository houses a collection of JSON configuration files, SQLX files, and JavaScript files.

**Note:** The Dataform repositories list includes only repositories created for Dataform workflow development. Repositories for BigQuery Studio assets, such as notebooks or saved queries, are managed separately and don't appear in this list.

Dataform repositories contain the following types of files:

  * **Config files**

Config JSON or SQLX files let you configure your workflows. They contain general configuration, execution schedules, or schema for creating new tables and views.

  * **Definitions**

Definitions are SQLX and JavaScript files that define new tables, views, and [additional SQL operations](https://docs.cloud.google.com/dataform/docs/custom-sql) to run in BigQuery.

  * **Includes**

[Includes](https://docs.cloud.google.com/dataform/docs/javascript-in-dataform#reuse_code_across_a_single_repository_with_includes) are JavaScript files where you can define variables and functions to use in your project.




Each Dataform repository must be connected to a custom service account. You select a custom service account when you [create a repository](https://docs.cloud.google.com/dataform/docs/create-repository#create-repository). You can [edit the service account](https://docs.cloud.google.com/dataform/docs/create-repository#edit-service-account) later.

### Version control

Dataform uses the Git version control system to maintain a record of each change made to project files and to manage file versions.

Each Dataform repository can manage its own Git repository, or be connected to a remote Git repository. You can [connect a Dataform repository to a GitHub, GitLab, Azure DevOps Services, Bitbucket, or Secure Source Manager repository](https://docs.cloud.google.com/dataform/docs/connect-repository) (Secure Source Manager support is in [Preview](https://cloud.google.com/products#product-launch-stages)).

Users [version control their workflow code](https://docs.cloud.google.com/dataform/docs/manage-repository#version-control-your-code) inside Dataform workspaces. In a Dataform workspace, you can pull changes from the repository, commit all or selected changes, and push them to Git branches of the repository.

### Workflow development

In Dataform, you make changes to files and directories inside a [development workspace](https://docs.cloud.google.com/dataform/docs/create-workspace). A development workspace is a virtual, editable copy of the contents of a Git repository. Dataform preserves the state of files in your development workspace between sessions.

In a development workspace, you can [develop workflow actions](https://docs.cloud.google.com/dataform/docs/sql-workflows) by using Dataform core with SQLX and JavaScript, or [exclusively with JavaScript](https://docs.cloud.google.com/dataform/docs/javascript-in-dataform). You can automatically format your Dataform core or JavaScript code.

Each element of a Dataform workflow, such as a table or assertion, corresponds to an action that Dataform performs in BigQuery. For example, a table definition file is an action of creating or updating the table in BigQuery.

In a Dataform workspace, you can develop the following workflow actions:

  * [Source data declarations](https://docs.cloud.google.com/dataform/docs/declare-source)
  * [Tables and views](https://docs.cloud.google.com/dataform/docs/create-tables#create-table)
  * [Incremental tables](https://docs.cloud.google.com/dataform/docs/create-tables#configure-incremental-table)
  * [Table partitions and clusters](https://docs.cloud.google.com/dataform/docs/create-tables#create-table-partitions-clusters)
  * [Dependencies between actions](https://docs.cloud.google.com/dataform/docs/dependencies)
  * [Documentation of tables](https://docs.cloud.google.com/dataform/docs/create-tables#add-table-documentation)
  * [Custom SQL operations](https://docs.cloud.google.com/dataform/docs/custom-sql)
  * [BigQuery labels](https://docs.cloud.google.com/dataform/docs/create-tables#labels)
  * [BigQuery policy tags](https://docs.cloud.google.com/dataform/docs/policy-tags)
  * [Dataform tags](https://docs.cloud.google.com/dataform/docs/configure-additional-actions#add-execution-tags)
  * [Data quality tests, called assertions](https://docs.cloud.google.com/dataform/docs/assertions)



You can use JavaScript to reuse your Dataform workflow code in the following ways:

  * [Across a file with code encapsulation](https://docs.cloud.google.com/dataform/docs/javascript-in-dataform#reuse_code_across_a_single_sqlx_file_with_javascript_encapsulation)
  * [Across a repository with includes](https://docs.cloud.google.com/dataform/docs/javascript-in-dataform#reuse_code_across_a_single_repository_with_includes)
  * [Across repositories with packages](https://docs.cloud.google.com/dataform/docs/javascript-in-dataform#reuse_code_across_multiple_repositories_with_packages)



Dataform compiles the workflow code in your workspace in real-time. In your workspace, you can view the compiled queries and details of actions in each file. You can also view the compilation status and errors in the edited file or in the repository.

To test the output of a compiled SQL query before you run it to BigQuery, you can [run preview of the query](https://docs.cloud.google.com/dataform/docs/preview-queries) in your Dataform workspace.

To inspect the entire workflow defined in your workspace, you can [view an interactive compiled graph](https://docs.cloud.google.com/dataform/docs/create-workspace#compiled-graph-tab) that shows all compiled actions in your workflow and relationships between them.

### Workflow compilation

Dataform uses default compilation settings, [configured in the workflow settings file](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings), to compile the workflow code in your workspace to SQL in real-time, creating a compilation result of the workspace.

You can override compilation settings to customize how Dataform compiles your workflow into a compilation result.

With [workspace compilation overrides](https://docs.cloud.google.com/dataform/docs/configure-compilation#create-workspace-compilation-overrides), you can configure compilation overrides for all workspaces in a repository. You can set dynamic workspace overrides to create compilation results custom for each workspace, turning workspaces into isolated development environments. You can override the Google Cloud project in which Dataform runs the contents of a workspace, add a prefix to names of all compiled tables, and add a suffix to the default schema.

With [release configurations](https://docs.cloud.google.com/dataform/docs/configure-compilation#create-release-configuration), you can configure templates of compilation settings for creating compilation results of a Dataform repository. In a release configuration, you can override the Google Cloud project in which Dataform runs the compilation results, add a prefix to names of all compiled tables, add a suffix the default schema, and add compilation variables. You can also set the frequency of creating compilation results. To schedule runs of compilation results created in a selected release configuration, you can [create a workflow configuration](https://docs.cloud.google.com/dataform/docs/schedule-runs#create-workflow-configuration).

### Workflow run

During a workflow run, Dataform runs the compilation results of workflows to create or update assets in BigQuery.

To create or refresh the tables and views defined in your workflow in BigQuery, you can [start a workflow run manually](https://docs.cloud.google.com/dataform/docs/trigger-execution) in a development workspace or schedule runs.

When you trigger a workflow run, Dataform executes the actions in the order defined by their dependencies. For each action, Dataform performs the following steps:

  1. Executes the compiled SQL in BigQuery.
  2. Updates the action status in the execution log.
  3. Upon successful completion of an action, Dataform automatically initiates a metadata sync to Knowledge Catalog. This enrichment process updates Knowledge Catalog with the semantic metadata defined in your SQLX configuration. The sync happens asynchronously and utilizes a retry mechanism, ensuring that metadata updates don't impact your pipeline latency or lead to workflow failures if the Dataplex API is temporarily unavailable.



You can schedule Dataform runs in BigQuery in the following ways:

  * [Create workflow configurations](https://docs.cloud.google.com/dataform/docs/schedule-runs#create-workflow-configuration) to schedule runs of compilation results created in release configurations
  * [Schedule runs with Managed Service for Apache Airflow](https://docs.cloud.google.com/dataform/docs/schedule-runs#composer)
  * [Schedule runs with Workflows and Cloud Scheduler](https://docs.cloud.google.com/dataform/docs/schedule-runs#workflows-cloud-scheduler)



You can also [automate runs with Cloud Build triggers](https://docs.cloud.google.com/dataform/docs/schedule-runs#cloud-build-triggers).

To debug errors, you can monitor runs in the following ways:

  * [View detailed Dataform execution logs](https://docs.cloud.google.com/dataform/docs/monitor-runs#monitor-execution-logs)
  * [View audit logs for Dataform](https://docs.cloud.google.com/dataform/docs/monitor-runs#view-cloud-logging-logs-for-dataform)
  * [View Cloud Logging logs for Dataform](https://docs.cloud.google.com/dataform/docs/monitor-runs#view-cloud-logging-logs-for-dataform)



## Dataform core

Dataform core is an open source meta-language to create SQL tables and workflows. Dataform core extends SQL by providing a dependency management system, automated data quality testing, and data documentation.

You can use Dataform core for the following purposes:

  * Defining tables, views, materialized views, or incremental tables.
  * Defining data transformation logic.
  * Declaring source data and managing table dependencies.
  * Documenting table and column descriptions inside code.
  * Reusing functions and variables across different queries.
  * Writing data assertions to verify data consistency.



In Dataform, you use Dataform core to develop workflows and deploy assets to BigQuery.

Dataform core is part of the [open-source Dataform data modeling framework](https://github.com/dataform-co/dataform) that also includes [Dataform CLI](https://docs.cloud.google.com/dataform/docs/use-dataform-cli). You can compile and run Dataform core locally through the Dataform CLI outside of Google Cloud.

To use Dataform core, you write SQLX files. Each SQLX file contains a query that defines a database relation that Dataform creates and updates inside BigQuery.

Dataform compiles your Dataform core code in real time to create a SQL compilation result that you can run in BigQuery.

Dataform compilation is hermetic to verify compilation consistency, meaning that the same code compiles to the same SQL compilation result every time. Dataform compiles your code in a sandbox environment with no internet access. No additional actions, such as calling external APIs, are available during compilation.

### SQLX file config block

A SQLX file consists of a config block and a body. All config properties, and the config block itself, are optional. Given this, any plain SQL file is a valid SQLX file that Dataform runs as-is.

In the config block, you can perform the following actions:

  * Specify query metadata.
  * Document data. 
  * Define data quality tests.



#### Specify query metadata

You can configure how Dataform materializes queries into BigQuery, for example the output table type, the target database, or labels using the config metadata.

#### Document data

You can [document your tables](https://docs.cloud.google.com/dataform/docs/create-tables#add-table-documentation) and their fields directly in the config block. Documentation of your tables is pushed directly to BigQuery and Knowledge Catalog. You can parse this documentation and push it out to other tools.

The following code sample shows you how to define the output table type, document the table, and add metadata for Knowledge Catalog in a config block of a SQLX file:
    
    
    config {
      type: "table",
      description: "This table joins orders information from OnlineStore & payment information from PaymentApp",
      columns: {
        order_date: "The date when a customer placed their order",
        id: "Order ID as defined by OnlineStore",
        order_status: "The status of an order, for example, sent, delivered",
        customer_id: "Unique customer ID",
        payment_status: "The status of a payment, for example, pending, paid",
        payment_method: "How the customer chose to pay",
        item_count: "The number of items the customer ordered",
        amount: "The amount the customer paid"
      },
      metadata: {
        overview: "This table provides joined orders and payment data.",
        extraProperties: {
          generic: {
            system: "BigQuery",
            type: "table"
          }
        }
      }
    }
    

#### Define data quality tests

You can define data quality tests, called [assertions](https://docs.cloud.google.com/dataform/docs/assertions), to check for uniqueness, null values, or a custom condition. Dataform adds assertions defined in the config block to your workflow dependency tree after table creation. You can also define assertions outside the config block, in a separate SQLX file.

The following code sample shows you how to define a quality test in a config block of a SQLX file:
    
    
    config {
      assertions: {
        uniqueKey: ["id"]
      }
    }
    

### SQLX file body

In the body of a SQLX file, you can perform the following actions:

  * Define a table and its dependencies.
  * Define additional SQL operations to run in BigQuery.
  * Generate SQL code with JavaScript.



#### Define a table

To define a new table you can use SQL `SELECT` statements and the `ref` function.

The `ref` function is a SQLX built-in function that is critical to dependency management in Dataform. The `ref` function lets you reference tables defined in your Dataform project instead of hard coding the schema and table names of your data table.

Dataform uses the `ref` function to build a dependency tree of all the tables to be created or updated. After compiling, Dataform adds boilerplate statements like `CREATE`, `REPLACE`, or `INSERT`.

The following code sample shows you how to reference a table in a SQLX file with the `ref` function.
    
    
    config { type: "table" }
    
    SELECT
      order_date AS date,
      order_id AS order_id,
      order_status AS order_status,
      SUM(item_count) AS item_count,
      SUM(amount) AS revenue
    
    FROM ${ref("store_clean")}
    
    GROUP BY 1, 2, 3
    

The output is similar to the following:
    
    
    CREATE OR REPLACE TABLE Dataform.orders AS
    
    SELECT
      order_date AS date,
      order_id AS order_id,
      order_status AS order_status,
      SUM(item_count) AS item_count,
      SUM(amount) AS revenue
    
    FROM Dataform_stg.store_clean
    
    GROUP BY 1, 2, 3
    

For more information on additional dependency management, for example, executing code conditionally, using other Dataform core built-in functions, see the [Dataform core reference](https://docs.cloud.google.com/dataform/docs/reference/dataform-core-reference).

#### Define additional SQL operations

To configure Dataform to run one or more SQL statements before or after creating a table or view, you can [specify pre-query and post-query operations](https://docs.cloud.google.com/dataform/docs/custom-sql).

The following code sample shows you how to configure table or view access permissions in a post-query operation.
    
    
    SELECT * FROM ...
    
    post_operations {
      GRANT `roles/bigquery.dataViewer` ON TABLE ${self()} TO "group:someusers@dataform.co"
    }
    

#### Encapsulate SQL code

To define reusable functions to generate repetitive parts of SQL code, you can use JavaScript blocks. You can reuse code defined in a JavaScript block only inside the SQLX file where the block is defined. To reuse code across your entire repository, you can [create includes](https://docs.cloud.google.com/dataform/docs/javascript-in-dataform#reuse_code_across_a_single_repository_with_includes).

To dynamically modify a query, you can use inline JavaScript anywhere in the body.

The following code sample shows how to define a JavaScript block in a SQLX file and use it inline inside a query:
    
    
    js {
      const columnName = "foo";
    }
    
    SELECT 1 AS ${columnName} FROM "..."
    

## Limitations

Dataform has the following known limitations:

  * Dataform in Google Cloud runs on a plain V8 runtime and does not support additional capabilities and modules provided by Node.js. If your existing codebase requires any [Node.js modules](https://nodejs.org/en/docs), you need to remove these dependencies.

Projects without a name field in `package.json` generate diffs on `package-lock.json` every time packages are installed. To avoid this outcome, you need to add a `name` property in `package.json`.

  * `git`+`https://` URLs for dependencies in `package.json` are not supported.

Convert such URLs to plain `https://` archive URLs. For example, convert `git+https://github.com/dataform-co/dataform-segment.git#1.5` to `https://github.com/dataform-co/dataform-segment/archive/1.5.tar.gz`.

  * Manually running unit tests is not available.

  * Searching for file content in development workspaces is not available.

**Note:** For the list of egress IP address ranges to use when allow-listing Dataform IPs with third-party remote repositories, see [Dataform locations](https://docs.cloud.google.com/dataform/docs/locations).
  * As of [Dataform core `3.0.0.`](https://github.com/dataform-co/dataform/releases/tag/3.0.0), Dataform doesn't distribute a Docker image. You can build your own Docker image of Dataform, which you can use to run the equivalent of Dataform CLI commands. To build your own Docker image, see [Containerize an application](https://docs.docker.com/guides/workshop/02_our_app/) in the Docker documentation.

  * The following Dataform API methods don't comply with the [AIP.134](https://google.aip.dev/134) guidelines by treating the `*` wildcard entry as a bad request and by updating all fields instead of set fields when `field_mask` is omitted:

    * [`releaseConfigs - patch`](https://docs.cloud.google.com/dataform/reference/rest#rest-resource:-v1.projects.locations.repositories.releaseconfigs)
    * [`repositories - patch`](https://docs.cloud.google.com/dataform/reference/rest#rest-resource:-v1.projects.locations.repositories)
    * [`updateConfig`](https://docs.cloud.google.com/dataform/reference/rest#rest-resource:-v1.projects.locations)
    * [`workflowConfigs - patch`](https://docs.cloud.google.com/dataform/reference/rest#rest-resource:-v1.projects.locations.repositories.workflowconfigs)
  * If a scheduled workflow configuration run doesn't finish before the start of the next scheduled run, the next scheduled run is skipped and marked with an error.




## What's next

  * To learn more about the code lifecycle in Dataform, see [Introduction to code lifecycle in Dataform](https://docs.cloud.google.com/dataform/docs/configure-compilation#intro-code-lifecycle).
  * To learn more about Dataform repositories, see [Introduction to repositories](https://docs.cloud.google.com/dataform/docs/repositories).
  * To learn more about Dataform workspaces, see [Create a Dataform development workspace](https://docs.cloud.google.com/dataform/docs/create-workspace).
  * To learn more about developing workflows in Dataform, see [Overview of workflows](https://docs.cloud.google.com/dataform/docs/sql-workflows).
  * To learn more about the Dataform CLI, see [Use the Dataform CLI](https://docs.cloud.google.com/dataform/docs/use-dataform-cli).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
