---
url: https://docs.cloud.google.com/dataform/docs/best-practices-repositories/
title: Best practices for repositories \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:46.929385+00:00
---

# Best practices for repositories  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/best-practices-repositories/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback 

#  Best practices for repositories Stay organized with collections  Save and categorize content based on your preferences. 

This document presents the following information about Dataform repositories:

  * Overview of repository best practices in Dataform
  * Overview of repository size
  * Splitting repositories
  * Structuring code in a repository
  * Best practices for compilation and scheduling



## Overview of repository best practices in Dataform

This section presents an overview of best practices for managing repository size, repository structure, and code lifecycle in Dataform.

### Best practices for repository size

Repository size impacts multiple aspects of development in Dataform, such as the following:

  * Collaboration
  * Codebase readability
  * Development processes
  * Workflow compilation
  * Workflow execution



Dataform enforces [API quotas and limits on compilation resources](https://docs.cloud.google.com/dataform/docs/quotas). A large repository size can cause your repository to exceed these quotas and limits. This can lead to the failed compilation and execution of your workflow.

To mitigate that risk, we recommend splitting large repositories. When you split a large repository, you divide a large workflow into a number of smaller workflows housed in different repositories and connected by cross-repository dependencies.

This approach lets you adhere to Dataform quotas and limits, implement fine-grained processes and permissions, and improve codebase readability and collaboration. However, managing split repositories can be more challenging than managing a single repository.

To learn more about the impact of repository size in Dataform, see Overview of repository size. To learn more about best practices for splitting repositories, see Splitting repositories.

### Best practices for repository structure

We recommend structuring files in the `definitions` directory to reflect the stages of your workflow. Keep in mind that you can adopt a custom structure that best fits your needs.

The following recommended structure of `definitions` subdirectories reflects the key stages of most workflows:

  * `sources` for storing data source declarations.
  * `intermediate` for storing data transformation logic.
  * `output` for storing definitions of output tables.
  * `extras` (optional) for storing additional files.



The names of all the files in Dataform must conform to BigQuery table naming guidelines. We recommend that the names of files in the `definitions` directory in a Dataform repository reflect the subdirectory structure.

To learn more about best practices for structuring and naming files in a repository, see Structuring code in a repository.

### Best practices for code lifecycle

The default code lifecycle in Dataform consists of the following phases:

  * Development of workflow code in Dataform workspaces.

You can develop with [Dataform core](https://docs.cloud.google.com/dataform/docs/overview#dataform-core) or [exclusively with JavaScript](https://docs.cloud.google.com/dataform/docs/javascript-in-dataform).

  * Compilation of your code into a [compilation result](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults#resource:-compilationresult) using settings from your [workflow settings file](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings).

You can configure custom compilation results with release configurations and workspace compilation overrides.

With [release configurations](https://docs.cloud.google.com/dataform/docs/configure-compilation#create-release-configuration), you can configure custom compilation results of your whole repository. You can later schedule their execution in [workflow configurations](https://docs.cloud.google.com/dataform/docs/schedule-runs#workflow-configurations).

With [workspace compilation overrides](https://docs.cloud.google.com/dataform/docs/configure-compilation#create-workspace-compilation-overrides), you can configure compilation overrides for all the workspaces in your repository, creating custom compilation results of each workspace.

  * Execution of the compilation result in BigQuery.

You can schedule executions or repository compilation results with [workflow configurations](https://docs.cloud.google.com/dataform/docs/schedule-runs#workflow-configurations).




To manage code lifecycle in Dataform, you can create execution environments such as development, staging, and production.

To learn more about code lifecycle in Dataform, see [Introduction to code lifecycle in Dataform](https://docs.cloud.google.com/dataform/docs/configure-compilation#intro-code-lifecycle).

You can select to keep your execution environments in a single repository, or in multiple repositories.

#### Execution environments in a single repository

You can create isolated execution environments such as development, staging, and production in a single Dataform repository with [workspace compilation overrides](https://docs.cloud.google.com/dataform/docs/configure-compilation#create-workspace-compilation-overrides) and [release configurations](https://docs.cloud.google.com/dataform/docs/configure-compilation#create-release-configuration).

You can create isolated execution environments the following ways:

  * Split development and production tables by schema.
  * Split development and production tables by schema and Google Cloud project.
  * Split development, staging, and production tables by Google Cloud project.



Then, you can schedule executions in staging and production environments with [workflow configurations](https://docs.cloud.google.com/dataform/docs/schedule-runs#workflow-configurations). We recommend triggering executions manually in the development environment.

To learn more about best practices for managing the workflow lifecycle in Dataform, see [Best practices for the workflow lifecycle](https://docs.cloud.google.com/dataform/docs/managing-code-lifecycle).

#### Code lifecycle in multiple repositories

To tailor [Identity and Access Management permissions](https://docs.cloud.google.com/dataform/docs/access-control#control-access-to-dataform-with-iam) to each stage of the code lifecycle, you can create multiple copies of a repository and store them in different Google Cloud projects.

Each Google Cloud project serves as an execution environment that corresponds to a stage of your code lifecycle—for example, development and production.

In this approach, we recommend keeping the codebase of the repository the same in all projects. To customize compilation and execution in each copy of the repository, use [workspace compilation overrides](https://docs.cloud.google.com/dataform/docs/configure-compilation#create-workspace-compilation-overrides), [release configurations](https://docs.cloud.google.com/dataform/docs/configure-compilation#create-release-configuration), and [workflow configurations](https://docs.cloud.google.com/dataform/docs/schedule-runs#workflow-configurations).

## Overview of repository size

This section helps you understand how repository size impacts workflow development and Dataform compilation resources usage, and how to estimate the compilation resources usage of your repository.

### About repository size in Dataform

The size of a repository impacts the following aspects of development in Dataform:

  * **Collaboration.** Multiple collaborators working on a large repository can create an excessive number of pull requests, increasing the risk of merge conflicts.

  * **Codebase readability.** A larger number of files that make up a workflow in a single repository can make it difficult to navigate through the repository.

  * **Development processes.** Some areas of a large workflow in a single repository might require custom permissions or processes, such as scheduling, that are different from the permissions and processes applied to the rest of the workflow. A large repository size makes it difficult to tailor development processes to specific areas of the workflow.

  * **Workflow compilation.** Dataform enforces usage limits on compilation resources. A large repository size can lead to exceeding these limits, causing the compilation to fail.

  * **Workflow execution.** During execution, Dataform runs repository code inside your workspace and deploys assets to BigQuery. The larger the repository, the more time it takes Dataform to run it.




If the large size of your repository negatively impacts your development in Dataform, you can split the repository into multiple smaller repositories.

### About repository compilation resource limits

During development, Dataform compiles all the repository code inside your workspace to generate a representation of the workflow in your repository. This is called a _compilation result_. Dataform enforces usage limits on compilation resources.

Your repository might exceed the usage limits for the following reasons:

  * An infinite loop bug in the repository code.
  * A memory leak bug in the repository code.
  * A large repository size, approximately more than 1000 workflow actions.

**Tip:** Update [Dataform core](https://docs.cloud.google.com/dataform/docs/manage-repository#manage-dataform-core-package) to the latest version to lower the risk of exceeding compilation limits.

For more information on usage limits on compilation resources, see [Dataform compilation resource limits](https://docs.cloud.google.com/dataform/docs/quotas#compilation-limits).

#### Estimate the compilation resource usage of your repository

You can estimate usage of the following compilation resources for your repository:

  * [CPU time](https://en.wikipedia.org/wiki/CPU_time) usage.
  * [Wall time](https://en.wikipedia.org/wiki/Elapsed_real_time) usage.
  * Maximum total serialized data size of the generated graph of actions defined in your repository.



To obtain a rough approximation of the current compilation time usage for the compilation of your repository, you can time the compilation of your Dataform workflow on a local Linux or macOS machine.

  * To time the compilation of your workflow, inside your repository, run the Dataform CLI command `dataform compile` in the following format:
        
        time dataform compile
        

The following code sample shows a result of executing the `time dataform compile` command:
        
        real    0m3.480s
        user    0m1.828s
        sys     0m0.260s
        




You can treat the `real` result as a rough indicator of the wall time usage and the `user` result as a rough indicator of the CPU time usage for the compilation of your repository.

To obtain a rough approximation of the total size of the generated graph of actions in your repository, you can write the output of the graph to a JSON file. You can treat the size of the uncompressed JSON file as a rough indicator of the total graph size.

  * To write the output of the compiled graph of your workflow to a JSON file, inside your repository, run the following Dataform CLI command:
        
        dataform compile --json > graph.json
        




## Splitting repositories

This section discusses strategies for splitting a Dataform repository and managing cross-repository dependencies.

Repositories are the core units in Dataform. A repository stores all the SQLX and JavaScript files that make up your workflow, as well as the Dataform configuration files and packages. You can store a workflow in a single repository, or split a workflow between multiple repositories.

Splitting a repository in Dataform comes with the following advantages:

  * Adhering to [Dataform compilation resource limits](https://docs.cloud.google.com/dataform/docs/quotas#compilation-limits). Splitting a large workflow into multiple smaller repositories lowers the risk of exceeding Dataform limits on compilation resources.
  * Fine-graining processes. You can set processes, such as continuous integration (CI) rules, individually for each split fragment of your workflow and the team developing it.
  * Fine-graining permissions. You can set permissions individually for each split fragment of your workflow and the team developing it to enhance the overall security of the workflow.
  * Improving collaboration by minimizing the number of collaborators working on each split fragment of your workflow.
  * Improving codebase readability. Splitting the files that make up a large workflow into multiple repositories makes it easier to navigate each repository individually than to navigate the entire workflow at once.
  * Speeding up the workflow execution of each split fragment of your workflow in comparison to the execution of the entire workflow.



Splitting a repository in Dataform comes with the following downsides:

  * Custom continuous integration and continuous development (CI/CD) configuration required for each Dataform repository and its corresponding Git repository.
  * Custom scheduling configuration required for each Dataform repository and its corresponding Git repository.
  * Difficulty in managing dependencies between the objects of your workflow housed in multiple repositories.
  * Lack of comprehensive directed acyclic graph (DAG) visualization of the SQL workflow split between multiple repositories. In each repository, the generated DAG represents only a portion of the complete workflow.



### Strategies for splitting a repository

When you split a repository, you divide the files that make up a parent SQL workflow into smaller child workflows housed in separate Dataform repositories.

You might choose to split a repository in one of the following ways:

  * One repository per development team.
  * One repository per domain—for example, sales, marketing, or logistics.
  * One central repository and one repository per domain that uses the contents of the central repository as data sources.



To house the parent workflow in a third-party Git hosting platform, you need to individually connect each of the separate repositories containing child workflows to a dedicated third-party Git repository.

### Managing cross-repository dependencies

The most efficient way to split a repository is to divide the parent SQL workflow into self-contained child workflows, creating independent repositories. An independent repository does not use the contents of a different repository as a data source. This approach does not require managing cross-repository dependencies.

When you cannot avoid cross-repository dependencies, you can manage them by splitting a repository into a succession of repositories, in which a repository depends on its predecessor and is a data source for its successor. The succession of repositories and their dependencies must best reflect the structure of your parent workflow.

You can create dependencies between repositories with [Dataform data source declarations](https://docs.cloud.google.com/dataform/docs/declare-source). You can declare a [BigQuery table type](https://docs.cloud.google.com/bigquery/docs/tables-intro) from a different Dataform repository as a data source in the repository being edited. After you declare a data source, you can reference it like any other Dataform workflow action and use it to develop your workflow.

When you schedule the execution of a workflow split between repositories with cross-repository dependencies, you must run the repositories one by one in the order of cross-repository dependencies.

We recommend avoiding splitting a repository into a group of repositories with two-way dependencies. A two-way dependency between repositories occurs when a repository is a data source for a different repository and also uses that repository as a data source. Two-way dependencies between repositories complicate the scheduling and execution of the parent workflow, as well as development processes.

## Structuring code in a repository

This section describes best practices for structuring and naming workflow files in the root `definitions` directory of a Dataform repository. The recommended structure of the `definitions` directory reflects the stages of a workflow. You can adopt any structure that fits your business needs.

You might want to structure the workflow code in the `definitions` directory for the following reasons:

  * Improving collaboration on the codebase by designating teams to selected parts of your workflow.
  * Improving maintainability of the workflow in case of organizational changes.
  * Improving navigation through your codebase.
  * Improving scalability of the codebase.
  * Minimizing administrative overhead for your team.



### Recommended structure of the `definitions` directory

The root `definitions` directory in a Dataform repository contains code that creates elements of your workflow. You can organize files in the `definitions` directory into a structure of directories that reflects the structure of the workflow.

When you develop a workflow, you declare source tables and transform them to create output tables that you can use for business or analytics purposes.

You can distinguish three key stages of a workflow:

  1. Declaration of data sources.
  2. Transformation of source data.
  3. Definition of output tables from the transformed source data.



The following structure of subdirectories in the `definitions` directory reflects the key stages of a workflow:

`sources`
    Data source declarations and basic transformation of source data—for example, filtering.
`intermediate`
    Tables and actions that read from `sources` and transform data before you use the transformed data to define `outputs` tables. Tables typically not exposed to additional processes or tools, such as business intelligence (BI) tools, after Dataform runs them to BigQuery.
`outputs`
    Definitions of tables consumed by processes or tools, such as BI, after Dataform runs them in BigQuery.
`extra`
    Files outside of the main pipeline of your workflow—for example, files that contain workflow data prepared for additional use, like machine learning. An optional and custom subdirectory.

#### Best practices for `sources`

The `sources` subdirectory contains the first stage of your workflow: the declaration and basic transformation of source data.

In the `sources` subdirectory, store data source declarations and tables that filter, categorize, cast, or rename columns.

Avoid storing tables that combine data from multiple sources.

Transform `sources` data in tables stored in the `intermediate` subdirectory.

If you declare data sources from multiple pools—for example, Google Ads or Google Analytics—dedicate a subdirectory to each pool.

The following sample shows a subdirectory structure of `sources` with two source pools:
    
    
    definitions/
        sources/
            google_ads/
                google_ads_filtered.sqlx
                google_ads_criteria_metrics.sqlx
                google_ads_criteria_metrics_filtered.sqlx
                google_ads_labels.sqlx
                google_ads_labels_filtered.sqlx
            google_analytics/
                google_analytics_users.sqlx
                google_analytics_users_filtered.sqlx
                google_analytics_sessions.sqlx
    

If you declare multiple data source tables within the same schema, you can consolidate their declarations into a single JavaScript file.

For more information about creating data source declarations with JavaScript, see [Create workflows exclusively with JavaScript](https://docs.cloud.google.com/dataform/docs/javascript-in-dataform#create-workflows-with-javascript).

The following code sample shows multiple data sources within one schema, declared in a single JavaScript file:
    
    
    [
      "source_table_1",
      "source_table_2",
      "source_table_3"
    ].forEach((name) =>
      declare({
        database: "gcp_project",
        schema: "source_dataset",
        name,
      })
    );
    

To protect your workflow against data source changes, you can create a view for each data source declaration—for example, `analytics_users_filtered.sqlx`. The view can contain the basic filtering and formatting of the source data. Store the views in the `sources` subdirectory.

Then, when you create `intermediate` or `outputs` tables, reference the views instead of raw source tables. This approach lets you test the source tables. In case a source table changes, you can modify its view—for example, by adding filters or recasting data.

#### Best practices for `intermediate`

The `intermediate` subdirectory contains the second stage of your workflow: the transformation and aggregation of the source data from one or multiple sources.

In the `intermediate` subdirectory, store files that significantly transform source data from one or multiple sources in the `sources` subdirectory—for example, tables that join data. Tables in the `intermediate` subdirectory typically query data from source tables or other `intermediate` tables.

Use `intermediate` tables to create `outputs` tables. Typically, `intermediate` tables are not used for additional purposes—for example, data analytics—after Dataform runs them to BigQuery. You can think of `intermediate` tables as the data transformation logic that enables the creation of output tables.

We recommend that you [document](https://docs.cloud.google.com/dataform/docs/create-tables#add-table-documentation) and [test](https://docs.cloud.google.com/dataform/docs/assertions) all `intermediate` tables.

#### Best practices for `outputs`

The `outputs` subdirectory contains the final stage of your workflow: the creation of output tables for your business purposes from the transformed data.

In the `outputs` directory, store tables that you plan to use in additional processes or tools after Dataform runs them to BigQuery—for example, reports or dashboards. Tables in the `outputs` directory typically query data from the `intermediate` tables.

Group `outputs` tables by the business entity they are related to, for example—marketing, orders, or analytics. Dedicate a subdirectory to each business entity.

To store output tables separately in BigQuery, you can configure a dedicated schema for output tables. For instructions to configure table schema, see [Override table settings](https://docs.cloud.google.com/dataform/docs/create-tables#override-table-settings).

The following sample shows a subdirectory structure of `outputs` with `sales` and `marketing` business entities:
    
    
    definitions/
        outputs/
            orders/
                orders.sqlx
                returns.sqlx
            sales/
                sales.sqlx
                revenue.sqlx
            marketing/
                campaigns.sqlx
    
    

We recommend that you [document](https://docs.cloud.google.com/dataform/docs/create-tables#add-table-documentation) and [test](https://docs.cloud.google.com/dataform/docs/assertions) all `outputs` tables.

### Naming strategy

The names of all the files in Dataform must conform to [BigQuery table naming guidelines](https://docs.cloud.google.com/bigquery/docs/tables#table_naming).

We recommend that the names of the files in the `definitions` directory in a Dataform repository reflect the subdirectory structure.

In the `sources` subdirectory, the filenames should point to the source that the file is related to. Add the name of the source as a prefix to the filenames—for example, `analytics_filtered.sqlx`

In the `intermediate` subdirectory, the filenames should identify the subdirectory, so that collaborators can clearly distinguish `intermediate` files. Select a unique prefix and apply it only to files in the `intermediate` directory—for example, `stg_ads_concept.sqlx`.

In the `outputs` subdirectory, the filenames should be concise—for example, `orders.sqlx`. If you have `outputs` tables with the same names in different entity subdirectories, add a prefix that identifies the entity —for example, `sales_revenue.sqlx` or `ads_revenue.sqlx`.

The following example shows a subdirectory structure inside the `definitions` directory with filenames that conform to the recommended naming strategy:
    
    
    definitions/
        sources/
            google_analytics.sqlx
            google_analytics_filtered.sqlx
        intermediate/
            stg_analytics_concept.sqlx
        outputs/
            customers.sqlx
            sales/
                sales.sqlx
                sales_revenue.sqlx
            ads/
                campaigns.sqlx
                ads_revenue.sqlx
    

## Best practices for compilation and scheduling

When configuring scheduled executions and orchestration workflows for your repository, follow these best practices to ensure reliable compilation:

  * **Use release configurations for scheduled production executions** : A [release configuration](https://docs.cloud.google.com/dataform/docs/configure-compilation#create-release-configuration) compiles your repository code on a predictable schedule and stores the resulting compilation result. When your production execution pipelines run, they execute against this saved result immediately without initiating network requests to your remote Git repository.
  * **Limit commitish compilation to development and low-frequency tasks** : Calling `CreateCompilationResult` directly on a Git commitish, such as `main` or a specific Git tag, requires Dataform to clone the repository over the network on every invocation. Avoid configuring production cron jobs or orchestration DAGs to repeatedly compile from a Git commitish at high frequencies.
  * **Configure automated retries and stagger schedules** : If your architecture requires compiling from a Git commitish in external schedulers, configure automated retries with exponential backoff and stagger concurrent cron timers. For detailed retry code examples and troubleshooting steps, see [Remote repository cannot be reached](https://docs.cloud.google.com/dataform/docs/troubleshooting#remote-repository-not-reached).



## What's next

  * To learn more about the code lifecycle in Dataform and different ways to configure it, see [Introduction to code lifecycle in Dataform](https://docs.cloud.google.com/dataform/docs/configure-compilation#intro-code-lifecycle).
  * To learn more about best practices for the workflow lifecycle, see [Best practices for the workflow lifecycle](https://docs.cloud.google.com/dataform/docs/managing-code-lifecycle).
  * To learn more about compilation resource limits, see [Dataform compilation resource limits](https://docs.cloud.google.com/dataform/docs/quotas#compilation-limits).
  * To learn how to connect a Dataform repository to a third-party Git repository, see [Connect to a third-party Git repository](https://docs.cloud.google.com/dataform/docs/connect-repository).
  * To learn more about workflows in Dataform, see [Overview of workflows](https://docs.cloud.google.com/dataform/docs/sql-workflows).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
