---
url: https://docs.cloud.google.com/dataform/docs/managing-code-lifecycle/
title: Best practices for the workflow lifecycle \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:50:40.418116+00:00
---

# Best practices for the workflow lifecycle  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/managing-code-lifecycle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback 

#  Best practices for the workflow lifecycle Stay organized with collections  Save and categorize content based on your preferences. 

This document describes best practices for managing the workflow lifecycle in Dataform: creating development, staging, and production environments, and configuring compilation and execution settings for each environment.

To create a standardized lifecycle of Dataform workflows that maintains data hygiene and optimizes development processes, we recommend that you:

  * Create execution environments to isolate tables created during development from tables available to end users.

  * Configure release and workflow configurations to run workflows in a production environment, and optionally in a staging environment.




This document describes solutions for isolating development tables with [workspace compilation overrides](https://docs.cloud.google.com/dataform/docs/configure-compilation#create-workspace-compilation-overrides) and configuring staging and production environments [release configurations](https://docs.cloud.google.com/dataform/docs/configure-compilation#create-release-configuration) and [workflow configurations](https://docs.cloud.google.com/dataform/docs/schedule-runs#workflow-configurations).

These solutions let you create execution environments within a single Dataform repository and Google Cloud project. You may choose to have multiple copies of a Dataform repository, housed in different Google Cloud project, with each project corresponding to a stage of your code lifecycle, for example, development, staging, and production. This approach lets you customize [Identity and Access Management permissions](https://docs.cloud.google.com/dataform/docs/access-control) at each stage of your code lifecycle.

## Best practices for isolated execution environments

We recommend that you isolate tables created during development workflow executions from production tables in BigQuery. This ensures that end users can navigate to production tables and eliminates the risk of end users accessing incorrect data by accident.

You can create isolated execution environments the following ways:

Split development and production tables by schema
    Recommended for small teams. Dataform creates development and production tables in different schemas in BigQuery. Dataform runs all development tables in schemas that have the same suffix, which marks that they were created during development. Developers can overwrite each other's development tables.
Split development and production tables by schema and Google Cloud project
    Recommended for medium-sized teams. Dataform creates development and production tables in different schemas and projects in BigQuery. Dataform published all development tables in a dedicated development Google Cloud project. Each Dataform developer has their own unique schema for development tables. This solution eliminates the risk of developers accidentally overwriting each other's development tables. The downside to this approach is that deleting development tables and schemas, and re-creating all tables in each environment may require more time.
Split development, staging, and production tables per Google Cloud project
    Recommended for large teams or teams that require a staging environment. Dataform runs tables from each environment in a dedicated Google Cloud project in BigQuery. This solution gives you the most control over the code lifecycle.

All solutions require a single Dataform repository [connected to a single third-party remote repository](https://docs.cloud.google.com/dataform/docs/connect-repository).

In all solutions, developers [manually trigger runs](https://docs.cloud.google.com/dataform/docs/trigger-execution) of development tables inside their Dataform workspaces. Dataform automatically compiles production and staging tables in a release configuration, and runs them at the frequency set in a workflow configuration.

## Split development and production by schema

This solution creates two execution environments in which Dataform will run your workflows: development and production. To split development and production tables by schema, you need to configure workflow settings, workspace compilation overrides, and a release configuration. To schedule production runs, you need to create a workflow configuration.

Dataform runs all the development tables in the schemas that have the same suffix, which marks that they were created during development. Dataform runs all the production tables in the schemas without any suffix.

The following table shows a configuration that splits development and production tables by schema, with one development schema:

Setting | Development | Production  
---|---|---  
Google Cloud project  | `enterprise-analytics` | `enterprise-analytics`  
Git branch | name of the workspace | `main`  
Workspace compilation overrides | schema suffix: `dev` | -  
Release configuration  | - | `production`  
Workflow configuration  | - | `production`  
  
In this solution, development and production tables are stored in a single Google Cloud project.

Developers trigger execution manually in their Dataform workspaces. In all manually triggered executions, Dataform runs tables in schemas that have the same suffix, which marks that they were created during development. Developers need to be aware that they can overwrite each other's tables.

In Dataform, developers commit and push their changes to their custom branches of the remote repository. Then, in the third-party Git hosting platform, they submit pull requests. Approval of a pull request merges changes to the `main` branch of the remote repository.

Dataform automatically compiles production tables from the `main` branch of the remote repository into a compilation result according to the `production` release configuration settings.

Dataform automatically runs the `production` compilation result according to the schedule set in the `production` workflow configuration.

To implement this solution, configure the following Dataform settings:

### Workflow settings

Depending on your version of Dataform core, workflow settings are stored in `workflow_settings.yaml` or `dataform.json`. For more information, see [Configure Dataform workflow settings](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings).

In `workflow_settings.yaml` configure the following settings:
    
    
    defaultProject: enterprise-analytics
    defaultDataset: analytics
    

In `dataform.json`, configure the following settings:
    
    
    {
    defaultSchema: "analytics",
    defaultDatabase: "enterprise-analytics"
    }
    

### Workspace overrides

Schema suffix: `"dev"`

### Release configuration

Git commitish: `"main"`

To schedule runs of `production` compilation results, [create a workflow configuration](https://docs.cloud.google.com/dataform/docs/schedule-runs#create-workflow-configuration).

### Sample development process

In this example, developers Sasha and Kai work in the same Dataform repository. The Dataform repository is connected to a remote third-party Git repository.

They commit and push changes to custom branches in the remote repository, called `sasha` and `kai`.

The following table shows applied environment settings for Sasha, Kai, and the production environment:

Setting | Sasha | Kai | Production  
---|---|---|---  
Google Cloud project | `enterprise-analytics` | `enterprise-analytics` | `enterprise-analytics`  
Git branch | `sasha` | `kai` | `main`  
Schema | `analytics_dev` | `analytics_dev` | `analytics`  
  
Sasha creates a new table and deploys it to production in the following process:

  1. In a Dataform workspace, Sasha creates the `user_stats` table.
  2. In the workspace, Sasha manually triggers execution of the table.
  3. Dataform creates the `enterprise-analytics.analytics_dev.user_stats` table in the `analytics_dev` schema in the `enterprise-analytics` Google Cloud project in BigQuery.
  4. In the workspace, Sasha commits the change and pushes it to the `sasha` branch in the remote Git repository.
  5. In the remote repository, Sasha submits a pull request.
  6. In the remote repository, Kai reviews and approves the pull request, merging the change to the `main` branch.
  7. Dataform automatically updates the compilation result in the `production` release at the specified frequency. During the next update of the `production` compilation result, Dataform adds the `enterprise-analytics.analytics.user_stats` table to the compilation result.
  8. During a scheduled execution of a workflow configuration, Dataform runs the `enterprise-analytics.analytics.user_stats` table in the `analytics` schema in the `enterprise-analytics` Google Cloud project in BigQuery.
  9. The `user_stats` table is available to end users in the `analytics` schema in the `enterprise-analytics` Google Cloud project in BigQuery.



## Split development and production by schema and project

This solution creates two execution environments: development and production. To split development and production tables by schema and Google Cloud project, you need to configure workflow settings, workspace compilation overrides, and a release configuration. To schedule production runs, you need to create a workflow configuration.

In this solution, Dataform runs development in a dedicated development Google Cloud project, in schemas with a different schema suffix for each workspace.

Dataform runs all production tables in BigQuery a dedicated production Google Cloud project with no schema suffix.

The following table shows a configuration that splits development and production tables by schema and Google Cloud project, with one development schema per a Dataform workspace:

Setting | Development | Production  
---|---|---  
Google Cloud project  | `enterprise-dev` | `enterprise-prod`  
Git branch | name of the workspace | `main`  
Workspace compilation overrides | schema suffix: `${workspaceName}` | -  
Release configuration  | - | `production`  
Workflow configuration  | - | `production`  
  
In this solution, Dataform runs development and production tables in different schemas and Google Cloud projects in BigQuery.

Developers trigger execution manually in their Dataform workspaces. Each developer works in their dedicated workspace, named after them, for example, `sasha`.

When a developer triggers execution in their workspace, Dataform appends the workspace name as the schema suffix to all schemas. Then, Dataform runs tables in the custom schema.

For example, Dataform creates tables from the `sasha` workspace in the `analytics_sasha` schema in BigQuery. This way, each developer stores their development tables in their own schema(s). There is no risk of accidentally overwriting tables of other developers.

In Dataform, developers commit and push their changes to their custom branches of the remote repository. Then, in the third-party Git hosting platform, they submit pull requests. Approval of a pull request merges changes to the `main` branch of the remote repository.

Dataform automatically compiles production tables from the `main` branch of the remote repository into a compilation result according to the `production` release configuration settings.

Dataform automatically runs the `production` compilation result according to the schedule set in the `production` workflow configuration.

To implement this solution, configure the following Dataform settings:

### Workflow settings

Depending on your version of Dataform core, workflow settings are stored in `workflow_settings.yaml` or `dataform.json`. For more information, see [Configure Dataform workflow settings](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings).

In `workflow_settings.yaml`, configure the following settings:
    
    
    defaultProject: enterprise-dev
    defaultDataset: analytics
    

In `dataform.json`, configure the following settings:
    
    
    {
    defaultSchema: "analytics",
    defaultDatabase: "enterprise-dev"
    }
    

### Workspace overrides

Schema suffix: `"${workspaceName}"`

### Release configuration

  * Git commitish: `"main"`
  * Google Cloud project ID: `"enterprise-prod"`



To schedule runs of `production` compilation results, [create a workflow configuration](https://docs.cloud.google.com/dataform/docs/schedule-runs#create-workflow-configuration) with a custom schedule that best fits your needs.

### Sample development process

In this example, developers Sasha and Kai work on the same Dataform repository. The Dataform repository is connected to a remote third-party Git repository.

Sasha works in their dedicated workspace called `sasha`, and Kai works in their dedicated workspace called `Kai`. They commit and push changes to custom branches in the remote repository, called `sasha` and `kai`.

The following table shows applied environment settings for Sasha, Kai, and the production environment:

Setting | Sasha | Kai | Production  
---|---|---|---  
Google Cloud project | `enterprise-dev` | `enterprise-dev` | `enterprise-prod`  
Git branch | `sasha` | `kai` | `main`  
Workspace compilation overrides | schema suffix: `${workspaceName}` | schema suffix: `${workspaceName}` | -  
Release configuration  | - | - | `production`  
Workflow configuration  | - | - | `production`  
  
Sasha creates a new table and deploys it to production in the following process:

  1. In the `sasha` Dataform workspace, Sasha creates the `user_stats` table.
  2. In the `sasha` workspace, Sasha manually triggers execution of the table.
  3. Dataform runs the `enterprise-dev.analytics_sasha.user_stats` table in the `analytics_sasha` schema in the `enterprise-dev` Google Cloud project in BigQuery.
  4. In the `sasha` workspace, Sasha commits the change and pushes it to the `sasha` branch in the remote Git repository.
  5. In the remote repository, Sasha submits a pull request.
  6. In the remote repository, Kai reviews and approves the pull request, merging the change to the `main` branch.
  7. Dataform automatically updates the compilation result in the `production` release at the specified frequency. During the next update of the `production` compilation result, Dataform adds the `enterprise-prod.analytics.user_stats` table to the compilation result.
  8. During a scheduled execution of a workflow configuration, Dataform runs the `enterprise-prod.analytics.user_stats` table in the `analytics` schema in the `enterprise-prod` Google Cloud project in BigQuery.
  9. The `user_stats` table is available to end users in the `analytics` schema in the `enterprise-prod` Google Cloud project in BigQuery.



It is also possible to split development and production data source declarations by project and split development and production data source declarations by schema and project.

## Split development, staging, and production by schema and project

This solution creates three execution environments: development, staging, and production. All environments are split by Google Cloud project. Additionally, development is split from staging and production by schema.

To split development, staging and production tables by schema and Google Cloud project, you need to configure workflow settings, workspace compilation overrides, and two release configurations. To schedule staging and production executions, you need to create two separate workflow configurations.

In this solution, Dataform runs development tables in BigQuery in multiple development schemas, one per Dataform workspace, in a dedicated development Google Cloud project.

Dataform runs all staging tables in BigQuery in a dedicated staging Google Cloud project in schemas that have the same suffix, which marks that they were created in staging.

Dataform runs all production tables in BigQuery in a dedicated production Google Cloud project in schemas that have the same suffix, which marks that they were created in production.

The following table shows an example configuration that splits development, staging, and production tables by schema and Google Cloud project, with one development schema per a Dataform workspace:

Setting | Development | Staging | Production  
---|---|---|---  
Google Cloud project | `enterprise-dev` | `enterprise-staging` | `enterprise-prod`  
Git branch | name of the workspace | `main` | `prod`  
Workspace compilation overrides | schema suffix: `${workspaceName}` | - | -  
Release configuration  | - | `staging` | `production`  
Workflow configuration  | - | `staging` | `production`  
  
In this solution, Dataform runs development, staging, and production tables in different Google Cloud projects in BigQuery. Additionally, Dataform runs development tables in multiple custom schemas, one per workspace. Dataform runs staging and production tables in the same schema, but in different Google Cloud projects.

Developers trigger execution manually in their Dataform workspaces. Each developer works in their dedicated workspace, named after them, for example, `sasha`.

Each workspace corresponds to a custom BigQuery schema, named after the workspace. When a developer triggers execution in their workspace, Dataform appends the workspace name as the schema suffix to the default schema. Then, Dataform runs tables in the custom schema in BigQuery.

For example, Dataform runs tables from the `sasha` workspace in the `analytics_sasha` schema in BigQuery. This way, each developer stores their development tables in their own schema. There is no risk of accidentally overwriting tables of other developers.

In Dataform, developers commit and push their changes to their custom branches of the remote repository. Then, in the third-party Git hosting platform, they submit pull requests to the `main` branch. Approval of a pull request merges changes to the `main` branch of the remote repository.

Dataform automatically compiles staging tables from the `main` branch of the remote repository into a compilation result according to the `staging` release configuration settings.

Dataform automatically runs the `staging` compilation result according to the schedule set in the `staging` workflow configuration.

To promote tables from staging to production, in the third-party Git hosting platform, developers submit pull requests from the `main` branch to the `prod` branch. Approval of a pull request merges changes to the `prod` branch of the remote repository.

Dataform automatically compiles production tables from the `prod` branch of the remote repository into a compilation result according to the `production` release configuration settings.

Dataform automatically runs the `production` compilation result according to the schedule set in the `production` workflow configuration.

To implement this solution, configure the following Dataform settings:

### Workflow settings

Depending on your version of Dataform core, workflow settings are stored in `workflow_settings.yaml` or `dataform.json`. For more information, see [Configure Dataform workflow settings](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings).

In `workflow_settings.yaml`, configure the following settings:
    
    
    defaultProject: enterprise-dev
    defaultDataset: analytics
    

In `dataform.json`, configure the following settings:
    
    
    {
    defaultSchema: "analytics",
    defaultDatabase: "enterprise-dev"
    }
    

### Workspace overrides

Schema suffix: `"${workspaceName}"`

### `staging` release configuration

  * Git commitish: `"main"`
  * Google Cloud project ID: `"enterprise-staging"`



### `prod` release configuration

  * Git commitish: `"prod"`
  * Google Cloud project ID: `"enterprise-prod"`



To schedule runs of `staging` and `production` compilation results, [create two separate workflow configurations](https://docs.cloud.google.com/dataform/docs/schedule-runs#create-workflow-configuration) with custom schedules that best fit your needs.

### Sample development process

In this example, developers Sasha and Kai work in the same Dataform repository. The Dataform repository is connected to a remote third-party Git repository.

Sasha works in their dedicated workspace called `sasha`, and Kai works in their dedicated workspace called `Kai`. They commit and push changes to custom branches in the remote repository, called `sasha` and `kai`.

The following table shows applied environment settings for Sasha, Kai, and the production environment:

Setting | Sasha | Kai | Staging | Production  
---|---|---|---|---  
Google Cloud project | `enterprise-dev` | `enterprise-dev` | `enterprise-staging` | `enterprise-prod`  
Git branch | `sasha` | `kai` | `main` | `prod`  
Schema | `analytics_sasha` | `analytics_kai` | `analytics` | `analytics`  
  
Sasha creates a new table and deploys it to production in the following process:

  1. In the `sasha` Dataform workspace, Sasha creates the `user_stats` table.
  2. In the `sasha` workspace, Sasha manually triggers execution of the table.
  3. Dataform runs the `enterprise-dev.analytics_sasha.user_stats` table in the `analytics_sasha` schema in the `enterprise-dev` Google Cloud project in BigQuery.
  4. In the `sasha` workspace, Sasha commits the change and pushes it to the `sasha` branch in the remote Git repository.
  5. In the remote repository, Sasha submits a pull request to the `main` branch.
  6. In the remote repository, Kai reviews and approves the pull request, merging the change to the `main` branch.
  7. Dataform automatically updates the compilation result in the `staging` release at the specified frequency. During the next update of the `staging` compilation result, Dataform adds the `enterprise-staging.analytics.user_stats` table to the compilation result.
  8. During a scheduled execution of a workflow configuration, Dataform runs the `enterprise-staging.analytics.user_stats` table in the `analytics` schema in the `enterprise-staging` Google Cloud project in BigQuery.
  9. In the remote repository, Sasha submits a pull request to the `prod` branch.
  10. In the remote repository, Kai reviews and approves the pull request, merging the change to the `prod` branch.
  11. Dataform automatically updates the compilation result in the `production` release at the specified frequency. During the next update of the `production` compilation result, Dataform adds the `enterprise-prod.analytics.user_stats` table to the compilation result.
  12. During a scheduled execution of a workflow configuration, Dataform runs the `enterprise-prod.analytics.user_stats` table in the `analytics` schema in the `enterprise-prod` Google Cloud project in BigQuery.
  13. The `user_stats` table is available to end users in the `analytics` schema in the `enterprise-prod` Google Cloud project in BigQuery.



## Split development and production data source declarations by project

This solution separates development and production data source declarations by project. Instead of declaring a data source with a static project, you can dynamically modify data source declarations using variables from the workflow settings file. This is useful when your data sources are isolated into separate development and production projects.

In this example, the project variable from the workflow settings file is injected to the data source declaration using the `dataform.projectConfig.vars.projectVar` Dataform variable:

In the `source_declaration.sqlx` file, configure the following settings:
    
    
    config {
      type: "declaration",
      database: dataform.projectConfig.vars.projectVar,
      schema: "source_schema",
      name: "source_name",
    }
    

When a workflow executes, Dataform injects the default project value or any configured project compilation overrides into the declaration. When you reference this data source in the workflow, it points to either the development or production data source, depending on the execution environment.

This solution requires consistent naming conventions for development and production source schemas and tables. If you need different naming conventions, use [custom compilation variables](https://docs.cloud.google.com/dataform/docs/manage-repository#create-compilation-variables).

## Split development and production data source declarations by schema and project

**Important:** You must split development and production data source declarations by project before you can split development and production data source declarations by schema and project.

This solution separates development and production data source declarations by project and schema. In addition to using the project variable from the workflow settings file, custom compilation variables are defined to represent a custom source schema name and a custom source table suffix. The default values for these variables are aligned to the development data source and can be overridden with compilation override values for the production data source, depending on the workflow execution environment.

In the `workflow_settings.yaml` file, configure the following settings:
    
    
    defaultProject: development
    defaultLocation: US
    defaultDataset: development
    defaultAssertionDataset: dataform_assertions
    dataformCoreVersion: 3.0.0
    vars:
     sourceSchema: schema_DEV
     sourceNameSuffix: _DEV
    

In the `source_declaration.sqlx` file, configure the following settings:
    
    
    config {
      type: "declaration",
      database: dataform.projectConfig.vars.projectVar,
      schema: dataform.projectConfig.vars.sourceSchema,
      name: "source_name"+dataform.projectConfig.vars.sourceNameSuffix,
    }
    

Variable | Development (default) | Production (overrides)  
---|---|---  
projectVar | `development` | `production`  
sourceSchema | `schema_DEV` | `schema_PROD`  
sourceNameSuffix | `_DEV` | `_PROD`  
Compiled data source | `development.schema_DEV.source_name_DEV` | `production.schema_PROD.source_name_PROD`  
  
In this example, splitting development and production data sources by project and schema is achieved through the `projectVar` variable and `sourceSchema` custom variable, respectively. Optionally, source table separation is achieved through a suffix appended to the table name.

The preceding example requires the data sources to be created beforehand in the separate development and production projects, and requires that the source schemas and table names follow consistent naming conventions. Additionally, when referencing a source table, the reference needs to be modified to use the `${ref("source_name"+dataform.projectConfig.vars.sourceNameSuffix)}` custom compilation variable in order for the references to be resolved correctly.

## What's next

  * To learn more about code lifecycle in Dataform and different ways to configure it, see [Introduction to code lifecycle in Dataform](https://docs.cloud.google.com/dataform/docs/configure-compilation#intro-code-lifecycle).
  * To learn how to create Dataform workspace compilation overrides, see [Create workspace compilation overrides](https://docs.cloud.google.com/dataform/docs/configure-compilation#create-workspace-compilation-overrides).
  * To learn how to create a Dataform release configuration, see [Create a release configuration](https://docs.cloud.google.com/dataform/docs/configure-compilation#create-release-configuration).
  * To learn how to create a Dataform workflow configuration, see [Schedule runs with workflow configurations](https://docs.cloud.google.com/dataform/docs/schedule-runs#workflow-configurations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
