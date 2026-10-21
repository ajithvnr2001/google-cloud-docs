---
url: https://docs.cloud.google.com/dataform/docs/workspaces/
title: Create a development workspace \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:01.964638+00:00
---

# Create a development workspace  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/workspaces/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback 

#  Create a development workspace Stay organized with collections  Save and categorize content based on your preferences. 

This document helps you to do the following:

  * Understand the concept of workspaces in Dataform and their capabilities.
  * Create a Dataform development workspace.
  * Initialize an empty Dataform development workspace.
  * Delete a Dataform development workspace.



## Overview of development workspaces

In Dataform, you interact with your workflow code in a development workspace, which is your own editable copy of a repository. In a workspace, you create, edit, or delete the contents of the repository without affecting others who work on the same repository, and then commit and push your changes to the repository.

You can develop your workflow with [Dataform core](https://docs.cloud.google.com/dataform/docs/overview#dataform-core) or [JavaScript](https://docs.cloud.google.com/dataform/docs/javascript-in-dataform). Dataform compiles your code into SQL queries in real time.

In a development workspace, you can perform the following tasks:

  * [Configure Dataform settings](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings).
  * [Create tables](https://docs.cloud.google.com/dataform/docs/create-tables#create-table) of all supported types.
  * [Document tables](https://docs.cloud.google.com/dataform/docs/create-tables#add-table-documentation).
  * [Partition tables](https://docs.cloud.google.com/dataform/docs/create-tables#create-table-partitions-clusters).
  * Add [BigQuery labels](https://docs.cloud.google.com/dataform/docs/create-tables#labels) and [policy tags](https://docs.cloud.google.com/dataform/docs/policy-tags) to tables.
  * [Override table settings](https://docs.cloud.google.com/dataform/docs/create-tables#override-table-settings).
  * [Configure additional actions](https://docs.cloud.google.com/dataform/docs/configure-additional-actions).
  * [Declare data sources](https://docs.cloud.google.com/dataform/docs/declare-source) for your workflow.
  * Add [custom SQL operations](https://docs.cloud.google.com/dataform/docs/custom-sql) and [tags](https://docs.cloud.google.com/dataform/docs/configure-additional-actions#add-execution-tags) to your workflow.
  * [Trigger execution](https://docs.cloud.google.com/dataform/docs/trigger-execution) of your workflow or its selected actions.
  * [Monitor execution logs](https://docs.cloud.google.com/dataform/docs/monitor-runs#monitor-execution-logs).



### Components of a development workspace

A Dataform development workspace consists of the tabs described in the following sections.

#### Code tab

You can use the development environment in the **Code** tab to explore files, develop queries, version control your changes, and trigger execution to BigQuery. The tab contains the following components that let you develop workflows:

  * **Files** pane: displays the file structure of your workspace and autosaves your edits to the file structure. Selected files open in the tabs of the development pane. In the **Type to search** field, you can search for files or directories in your workspace by their path.
  * **Version control** pane: displays the version control status of your workspace and the version control options.
  * **Development** pane: displays open files in tabs. Autosaves your changes to edited files.
  * **Run** button: runs a [preview of the compiled SQL query](https://docs.cloud.google.com/dataform/docs/preview-queries).
  * **Format** button: formats your Dataform core or JavaScript code.
  * **Compilation** status: displays the compilation status of the code in your workspace.
  * **Metadata** pane: displays the metadata of the edited file.
  * **Compiled queries** pane: compiles the queries in the edited file to SQL. If the query compilation fails, the pane displays the compilation errors. If the query compilation is successful, the pane displays the compiled queries and validates them through dry runs against BigQuery. If the query validation fails, the pane displays the validation errors. If the query validation is successful, the pane displays how many bytes the execution of the queries to BigQuery would use.
  * **Start execution** menu: displays the options for triggering the execution of the entire workflow in your workspace or its selected elements.



#### Compiled graph tab

In the **Compiled graph** tab, you can see the compiled workflow defined in your workspace as an interactive directed acyclic graph (DAG). The graph shows all the actions in your workflow and the relationships between them. If there are compilation errors in your workflow, the tab displays an error message instead of the graph.

You can zoom in and out and use drag-and-drop navigation in the graph.

You can filter the graph by the following properties:

  * Name
  * [Tag](https://docs.cloud.google.com/dataform/docs/configure-additional-actions#add-execution-tags)
  * Type 
    * Assertion
    * Declaration
    * Incremental table
    * Materialized view
    * Operations
    * Table
    * Unknown
    * View



You can select multiple filters at once. Dataform applies them with the `OR` condition.

You can click an action in the graph to view its details in the following panes:

  * **Metadata** pane: displays the full name, type, dependencies, and dependents of the selected action.
  * **Query** pane: displays the compiled SQL query of the selected action.



#### Executions tab

This tab displays the logs of all the executions triggered in the workspace. You can also view actions and their details for a selected execution. For more information, see [Monitor execution logs](https://docs.cloud.google.com/dataform/docs/monitor-runs#monitor-execution-logs).

### Version control in a workspace

In a workspace, you interact with the repository through Git-based version control. Edits you make to files in your workspace start off as uncommitted local changes that you can commit and then push to your repository so that they become available to all repository users.

If your repository is connected to a remote Git provider, you push changes from your workspace to your main development branch. You select the main branch when you connect your repository to the remote Git provider. In a non-connected Dataform repository, you push changes to the default branch.

You can also pull any changes from the Dataform repository or the remote repository and merge them with local changes in your development workspace. For more information about version control in Dataform, see [Version control your code](https://docs.cloud.google.com/dataform/docs/manage-repository#version-control-your-code).

## Before you begin

If you haven't done so already, [create a Dataform repository](https://docs.cloud.google.com/dataform/docs/create-repository).

### Required roles

To get the permissions that you need to create, initialize, and delete a development workspace, ask your administrator to grant you the [Dataform Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.editor) (`roles/dataform.editor`) IAM role on workspaces. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a Dataform development workspace

When you create a development workspace in a new repository for the first time, Dataform prompts you to initialize the development workspace with a set of configuration files that are required for Dataform to work.

An initialized development workspace contains the following directories and files:

  * `definitions/`: a directory for asset definitions, in Dataform core or JavaScript.

  * `includes/`: an empty directory for scripts and variables that you can reuse across the repository.

  * `workflow_settings.yaml`: the default Dataform configuration file containing the Google Cloud project ID and BigQuery schema to publish assets in. You can [override the default settings](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings) to customize them to your needs, but customization isn't a requirement to begin using Dataform.

  * `package.json`: the default Dataform dependencies configuration file with the latest version of `@dataform/core`. You can use this file to [import packages](https://docs.cloud.google.com/dataform/docs/use-packages#install-package).

  * `definitions/sample.sqlx`: a sample SQLX file to help you get started.




To create a new Dataform development workspace, follow these steps:

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Select the repository where you want to create the new development workspace.

**Note:** The Dataform repositories list includes only repositories created for Dataform workflow development. Repositories for BigQuery Studio assets, such as notebooks or saved queries, are managed separately and don't appear in this list.
  3. On your repository page, click **Create development workspace**.

  4. In the **Create development workspace** window, do the following:

     1. In the **Workspace ID** field, enter a unique ID for the development workspace.

IDs can only include numbers, letters, hyphens, and underscores.

     2. Click **Create**.


**Note:** If you enhance security by setting the `enable_private_workspace` field [(Preview)](https://cloud.google.com/products#product-launch-stages) to `true` in the [`projects.locations.updateConfig` Dataform API method](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations/updateConfig), only the workspace creator can read and write code in that Dataform workspace. This restriction also applies to viewing generated artifacts, such as compiled SQL, compilation errors, and run logs, for the workspace's compilations or workflow invocations. For more information, see [Enable private workspaces](https://docs.cloud.google.com/dataform/docs/access-control#enable-private-workspaces).

## Initialize the workspace in a Dataform repository

To initialize a Dataform development workspace, follow these steps:

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Select the repository where you want to initialize the empty workspace.

  3. In the **Development workspaces** tab, click the name of the empty workspace you want to initialize.

  4. On the development workspace page, click **Initialize workspace**.




## Delete a Dataform workspace

There are no costs associated with creating Dataform development workspaces. However, if you want to delete a development workspace, follow these steps:

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Select the repository that contains the workspace that you want to delete.

  3. To avoid deleting uncommitted changes, [commit and push changes to your Git repository](https://docs.cloud.google.com/dataform/docs/manage-repository#version-control-your-code).

  4. In the **Development workspaces** tab, select the development workspace that you want to delete, and then click **Delete selected workspaces**.

You can delete multiple workspaces at once.

  5. To confirm, click **Delete**.




## What's next

  * To learn how to version control your Dataform code, see [Version control your code](https://docs.cloud.google.com/dataform/docs/manage-repository#version-control-your-code).
  * To learn how to create a table, see [Create a table](https://docs.cloud.google.com/dataform/docs/create-tables#create-table).
  * To learn how to run a preview to test a SQL query, see [Preview SQL queries](https://docs.cloud.google.com/dataform/docs/preview-queries).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
