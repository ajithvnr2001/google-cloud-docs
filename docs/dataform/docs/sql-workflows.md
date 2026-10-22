---
url: https://docs.cloud.google.com/dataform/docs/sql-workflows/
title: Overview of workflows \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:19.203739+00:00
---

# Overview of workflows  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/sql-workflows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback 

#  Overview of workflows Stay organized with collections  Save and categorize content based on your preferences. 

This document helps you understand the architecture and execution of workflows in Dataform.

You can use Dataform to develop, test, and version control workflows that you can run in BigQuery to transform data for analytics purposes. Dataform workflows power BigQuery pipelines, data preparations, notebooks, and saved queries.

You can develop workflows with [Dataform core](https://docs.cloud.google.com/dataform/docs/overview#dataform-core), using SQLX files and optionally JavaScript files, or with [JavaScript](https://docs.cloud.google.com/dataform/docs/javascript-in-dataform).

A workflow can consist of the following objects:

[Data source declarations](https://docs.cloud.google.com/dataform/docs/declare-source)
    Declarations of BigQuery data sources that let you reference these data sources in Dataform table definitions and SQL operations.
[Tables](https://docs.cloud.google.com/dataform/docs/create-tables)
    Tables that you create in Dataform based on the declared data sources or other tables in your workflow. Dataform supports the following table types: table, incremental table, view, and materialized view.
[Assertions](https://docs.cloud.google.com/dataform/docs/assertions)
    Data quality test queries that you can use to validate table data. Dataform runs assertions every time it updates your workflow and it alerts you if any assertions fail.
[Custom SQL operations](https://docs.cloud.google.com/dataform/docs/custom-sql)
    SQL statements that Dataform runs in BigQuery as they are, without modification.
[Includes](https://docs.cloud.google.com/dataform/docs/javascript-in-dataform#reuse_code_across_a_single_repository_with_includes)
    JavaScript files with definitions of variables and functions that you can reuse across your workflow.

## Developing with the Data Engineering Agent

The Data Engineering Agent helps you build and maintain SQL workflows by generating code and configurations from natural language prompts. Beyond SQL logic, the agent proactively populates your table configurations with Knowledge Catalog metadata, such as field descriptions, table overviews, and generic aspects like system and type information. This ensures your data assets are discoverable from the moment of creation.

For more information, see [Use the Data Engineering Agent to build and modify data pipelines](https://docs.cloud.google.com/bigquery/docs/data-engineering-agent-pipelines).

## Visualization of a workflow

You can view your workflow visualized in the form of a Directed Acyclic Graph (DAG). The DAG displays all objects of the workflow defined in your workspace, and the relationships between them. You can zoom in and out and use drag-and-drop navigation in the DAG. If there are compilation errors in your workflow, Dataform displays an error message instead of the DAG.

To view the DAG of your workflow, in your workspace, click **Compiled graph**.

## Execution of a workflow

You must associate a custom service account with a Dataform repository for workflow execution. All other repository operations are still performed by the default Dataform service agent.

In your development workspace, you can [manually trigger a run](https://docs.cloud.google.com/dataform/docs/trigger-execution) of your entire workflow, a selection of actions, or a selection of tags.

You can schedule runs with Dataform [release configurations](https://docs.cloud.google.com/dataform/docs/configure-compilation#create-release-configuration) and [workflow configurations](https://docs.cloud.google.com/dataform/docs/schedule-runs#workflow-configurations). First, create a release configuration to create compilation results of your repository. Then, create a workflow configuration, select a release configuration, select workflow actions that you want to run, and set the run schedule.

Alternatively, you can schedule runs either with [Managed Service for Apache Airflow](https://docs.cloud.google.com/dataform/docs/schedule-runs#composer), or with [Workflows and Cloud Scheduler](https://docs.cloud.google.com/dataform/docs/schedule-runs#workflows-cloud-scheduler).

During execution, Dataform runs SQL queries in BigQuery, following the order of object dependencies in your workflow. After execution, you can use your defined tables and views for all your analytics purposes in BigQuery.

### Execution configuration options

To run a specific group of your workflow actions, you can add [Dataform execution tags](https://docs.cloud.google.com/dataform/docs/configure-additional-actions#add-execution-tags) to the files you select. You can then [run only the files with a selected tag](https://docs.cloud.google.com/dataform/docs/trigger-execution#run-actions-selected-tags) when you manually trigger a run.

By default, Dataform runs your workflow with the execution settings defined in the `workflow_settings.yaml` file.

With [workspace compilation overrides](https://docs.cloud.google.com/dataform/docs/configure-compilation#create-workspace-compilation-overrides), you can turn workspaces into isolated execution environments. This means that when you manually trigger execution in a workspace, Dataform runs the output in an isolated location in BigQuery.

To create and run a single compilation result with compilation overrides you can pass requests [with the Dataform API](https://docs.cloud.google.com/dataform/docs/configure-compilation#configure-compilation-overrides-with-api).

With [release configurations](https://docs.cloud.google.com/dataform/docs/configure-compilation#create-release-configuration), you can configure compilation overrides for your whole repository, as well as the frequency of creating compilation results with the applied settings.

To learn more about ways to configure compilation and code lifecycle in Dataform, see [Introduction to code lifecycle in Dataform](https://docs.cloud.google.com/dataform/docs/configure-compilation#intro-code-lifecycle).

## What's next

  * To learn how to declare a data source, see [Declare a data source](https://docs.cloud.google.com/dataform/docs/declare-source).
  * To learn how to declare dependencies to define relationships between objects in your workflow, see [Set dependencies](https://docs.cloud.google.com/dataform/docs/dependencies).
  * To learn how to define custom SQL operations, see [Create operations](https://docs.cloud.google.com/dataform/docs/custom-sql).
  * To learn how to reuse variables and functions across your workflow with includes, see [Reuse code across a single repository with includes](https://docs.cloud.google.com/dataform/docs/javascript-in-dataform#reuse_code_across_a_single_repository_with_includes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
