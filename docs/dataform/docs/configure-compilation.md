---
url: https://docs.cloud.google.com/dataform/docs/configure-compilation/
title: Configure compilations \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:24:52.316237+00:00
---

# Configure compilations  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/configure-compilation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback 

#  Configure compilations Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to do the following in Dataform:

  * Understand the workflow lifecycle in Dataform.
  * Create workspace compilation overrides.
  * Configure compilation overrides with the Dataform API.
  * Create a release configuration.



## Before you begin

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Select or [create a repository](https://docs.cloud.google.com/dataform/docs/create-repository).

  3. Select or [create a development workspace](https://docs.cloud.google.com/dataform/docs/create-workspace).

  4. Optional: To override the default Google Cloud project in the release configuration, [grant your custom service account access](https://docs.cloud.google.com/dataform/docs/access-control#grant-dataform-required-access) in the project you plan to use.




### Required roles

To get the permissions that you need to complete the tasks in this document, ask your administrator to grant you the following IAM roles: 

  * [Dataform Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.admin) (`roles/dataform.admin`) on repositories
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the custom service account



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To enhance security for scheduling, see [Implement enhanced scheduling permissions](https://docs.cloud.google.com/dataform/docs/access-control#enhanced-scheduling-permissions).

To be able to update the release version of a release configuration for a Dataform repository, you must grant the `iam.serviceAccounts.actAs` permission to the Dataform service agent for every custom service account in the workflow configurations that are using this release configuration. This permission is available in the [Service Account User role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`). For more information, see [Grant the required IAM roles](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode#grant-iam-roles).

## Introduction to the workflow lifecycle in Dataform

This section describes the workflow lifecycle in Dataform and ways to configure compilation and execution within Dataform.

The Dataform workflow lifecycle consists of the following phases:

Development
    You [develop a workflow](https://docs.cloud.google.com/dataform/docs/sql-workflows) in a Dataform workspace.
Compilation
    

Dataform compiles the workflow code in your workspace to SQL in real time, creating a [compilation result](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults#resource:-compilationresult) of the workspace that you can run in BigQuery. Dataform uses the settings that you [define in your workflow settings file](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings) to create the compilation result.

Dataform compilation is hermetic to ensure compilation consistency, meaning that the same code compiles to the same SQL compilation result every time. Dataform compiles your code in a sandbox environment with no internet access. No additional actions, such as calling external APIs, are available during compilation.

Execution
    

In a [workflow invocation](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations), Dataform runs the workspace compilation result in BigQuery.

To tailor the Dataform workflow lifecycle to your needs, you can configure the compilation result to influence where and how Dataform runs your workflow. Then, you can manually trigger or schedule executions to influence when Dataform runs your whole workflow or its selected elements.

### Ways to configure Dataform compilation

By default, Dataform uses settings in the [workflow settings file](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings) to create compilation results. You can override the default settings with compilation overrides to create custom compilation results. You can then manually trigger an execution of a custom compilation result, or schedule executions.

Dataform provides the following options for configuring compilation results:

Workspace compilation overrides
    You can configure compilation overrides that apply to all workspaces in a repository. You can use workspace compilation overrides to create isolated development environments.
Release configurations
    You can create release configurations to configure templates for creating compilation results of a Dataform repository. You can then create a workflow configuration to schedule executions of compilation results created in a selected release configuration.
Dataform API compilation overrides
    You can pass Dataform API requests in the terminal to create and run a single compilation result with compilation overrides.

#### Configure workspace compilation overrides

With workspace compilation overrides, you can create compilation overrides for all workspaces in a Dataform repository. You can create one configuration of workspace compilation overrides for each repository.

When you manually trigger an execution in a workspace in a repository with workspace compilation overrides, Dataform applies these overrides to the compilation result of the workspace.

You can configure the following workspace compilation overrides:

  * Google Cloud project in which Dataform runs the contents of the workspace
  * Table prefix
  * Schema suffix



You can use workspace compilation overrides to create isolated development environments by isolating workspace compilation results in BigQuery with dynamic compilation overrides. Dynamic table prefix and schema suffix compilation overrides contain the `${workspaceName}` variable. When you trigger an execution in a workspace, Dataform replaces the `${workspaceName}` variable with the name of the current workspace, creating compilation overrides unique to the workspace.

Keep in mind that you cannot schedule executions of compilation results created with workspace compilation overrides.

#### Create release configurations

With release configurations, you can configure templates of settings for creating compilation results of repositories.

In a release configuration, you can configure compilation overrides of [workflow settings](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings), compilation variables, and the frequency of creating compilation results of your whole repository.

In a release configuration, you can configure the following compilation overrides:

  * Google Cloud project
  * Table prefix
  * Schema suffix
  * Value of a compilation variable



You can create multiple release configurations in a Dataform repository, one for each stage of your development lifecycle, creating isolated repository compilation results.

You can then [create workflow configurations to schedule executions](https://docs.cloud.google.com/dataform/docs/schedule-runs#workflow-configurations) of compilation results created in a selected release configuration.

You can also manually trigger the execution of a compilation result in a selected release configuration.

#### Configure a single compilation result with Dataform API compilation overrides

By passing Dataform API requests in the terminal, you can configure compilation overrides for a single compilation result.

In the [`compilationResults.create`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults/create) request, you can create a single compilation result of a Dataform workspace or a specified Git commitish.

In the [`CodeCompilationConfig` object](https://docs.cloud.google.com/dataform/reference/rest/v1/CodeCompilationConfig) of the `compilationResults.create` request, you can configure compilation overrides for the compilation request.

You can configure the following Dataform API compilation overrides:

  * Google Cloud project
  * Table prefix
  * Schema suffix
  * Value of a compilation variable



Keep in mind that Dataform API compilation overrides apply to a single compilation result and a single execution. You cannot use them to schedule Dataform executions.

You can run a compilation result in the [`workflowInvocations.create`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/create) request.

### Ways to configure Dataform execution

Dataform provides the following options for configuring execution:

Manual execution in a workspace
    You can manually trigger the instant execution of a workflow in a Dataform workspace, outside of any schedule. You can run selected actions in the workflow.
Workflow configurations
    You can schedule executions of compilation results created in a selected release configuration. You can select workflow actions to run, and set the frequency and time zone of executions.

#### Trigger instant execution in a workspace

In a Dataform workspace, you can manually trigger the instant execution of a workflow in your workspace, outside of any schedule.

You can manually run the following elements of the workflow in your workspace:

  * [All actions](https://docs.cloud.google.com/dataform/docs/trigger-execution#run-all-actions)
  * [Selected actions](https://docs.cloud.google.com/dataform/docs/trigger-execution#run-selected-actions)
  * [Actions with selected tags](https://docs.cloud.google.com/dataform/docs/trigger-execution#run-actions-selected-tags)



If your repository contains workspace compilation overrides, you can view what compilation overrides Dataform will apply to the workspace compilation result.

#### Create workflow configurations

With [workflow configurations](https://docs.cloud.google.com/dataform/docs/schedule-runs#workflow-configurations), you can schedule executions of compilation results from a selected release configuration. You can create multiple workflow configurations in a Dataform repository.

In a workflow configuration, you can configure the following execution settings:

  * Applied compilation release configuration.
  * Selection of workflow actions to be run.
  * Schedule and time zone of executions.



You can select the following workflow actions to be run:

  * All actions
  * Selected actions
  * Actions with selected tags



Then, during a scheduled execution of your workflow configuration, Dataform deploys your selection of actions from the applied compilation result to BigQuery.

Dataform release configurations and workflow configurations let you configure compilation and schedule executions within Dataform, without the need to rely on additional services.

### Expiration of lifecycle resources

Dataform stores compilation results and workflow invocations for a specific period of time.

#### Expiration of workflow invocations

[Workflow invocations](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations) expire after 90 days, or when you manually delete them.

In a [workflow configuration](https://docs.cloud.google.com/dataform/docs/schedule-runs#workflow-configurations), you can view a list of most recent workflow invocations created by the configuration. When a workflow invocation created by a workflow configuration expires, Dataform removes that workflow invocation from the list of recent invocations.

#### Expiration of compilation results

The expiration of [compilation results](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults#resource:-compilationresult) depends on whether they were created in a development workspace, in a release configuration, or by a workflow invocation.

When you develop a workflow in a Dataform workspace, Dataform compiles your code into a compilation result in real time to provide query validation. Compilation results created this way expire after 24 hours.

In a release configuration, the latest compilation result becomes the live compilation result. A new compilation result replaces the current live compilation result. Dataform retains the live compilation result until it is replaced with a new compilation result. A replaced compilation result expires in up to 24 hours.

Dataform removes expired compilation results from the list of past compilation results on the **Details** page of a release configuration.

Dataform retains compilation results created by workflow invocations for the whole life of the workflow invocation, up to 24 hours after workflow invocation expires or is deleted.

## Create workspace compilation overrides

This section shows you how to create workspace compilation overrides to isolate tables and views created from your Dataform workspaces in BigQuery. You can use workspace compilation overrides to create isolated Dataform development environments.

When you develop workflow code in a Dataform workspace, Dataform compiles the code in your workspace in real-time to create a [compilation result](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults#resource:-compilationresult) of the workspace. Dataform uses settings defined in the [workflow settings file](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings) to create the workspace compilation result. Then, when you [trigger execution](https://docs.cloud.google.com/dataform/docs/trigger-execution) in a workspace, Dataform runs the workspace compilation result in BigQuery.

To override the default settings set in [workflow settings](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings) for all workspaces in your repository, you can create workspace compilation overrides.

With workspace compilation overrides, you can override the following settings for all workspaces in your repository:

Project
    

The Google Cloud project in which Dataform runs the workspace compilation result, set in `workflow_settings.yaml` as `defaultProject` or in `dataform.json` as `defaultDatabase`.

**Note:** The BigQuery job responsible for the execution is created in the same Google Cloud project in which the Dataform repository is present.
Table prefix
    

The custom prefix added to all the table names in all the workspaces in the repository.

Schema suffix
    

The custom suffix appended to the schema of tables. Set as `defaultDataset` in `workflow_settings.yaml`, `defaultSchema` in `dataform.json`, or in the `schema` parameter in the `config` block of a table.

To create isolated development environments, you can isolate workspaces with unique compilation overrides. You can dynamically modify the table prefix and schema suffix compilation overrides with the `${workspaceName}` variable.

When you manually trigger execution in a workspace, the `${workspaceName}` variable injects the name of the workspace into the workspace compilation overrides.

When you set `${workspaceName}` as the table prefix, Dataform adds the name of the workspace to names of all tables in the workspace. After execution, in BigQuery, you can identify which workspace a table originates from.

When you set `${workspaceName}` as the schema suffix, Dataform appends the name of the workspace to `defaultSchema`, creating a custom schema dedicated to the workspace. After execution, in BigQuery, you can locate all the tables that are run from a specific workspace in the dedicated schema.

#### Example of dynamic workspace compilation overrides

The following example shows dynamic workspace compilation overrides applied to a repository that contains workspaces named after developers who work on the repository: `Sasha` and `Kai`.

The goal of workspace compilation overrides in this example is to create isolated development environments for Sasha and Kai.

The following default settings are set in `workflow_settings.yaml`:

  * `defaultProject` : `analytics`
  * `defaultDataset`: `dataform`



The following workspace compilation overrides create a dynamic table prefix and schema suffix for each workspace in the repository:

  * **Google Cloud Project ID** : `analytics_dev`
  * **Table prefix** : `${workspaceName}`
  * **Schema suffix** : `${workspaceName}`



When Sasha manually triggers execution in the `Sasha` workspace, Dataform runs its content with the following settings:

  * Google Cloud project: `analytics_dev`
  * Schema: `dataform_sasha`
  * Table names: `sasha_name`, for example, `sasha_orders`



When Kai manually triggers execution in the `Kai` workspace, Dataform runs its content with the following settings:

  * Google Cloud project: `analytics_dev`
  * Schema: `dataform_kai`
  * Table names: `kai_name`, for example, `kai_orders`



### Create workspace compilation overrides

To create Dataform workspace compilation overrides, follow these steps:

  1. In your repository, go to **Settings**.
  2. Click **Edit**.
  3. In the **Workspace compilation overrides** pane, in the **Google Cloud Project ID** field, enter the ID of the project.
  4. In the **Table prefix** field, enter a prefix for all table names. 
     1. Optional: To create a dynamic table prefix that is unique for each workspace, enter `${workspaceName}` as the table prefix.
  5. In the **Schema suffix** field, enter a suffix to append to the schema of the created table or view. 
     1. Optional: To create a dynamic schema suffix that is unique for each workspace, enter `${workspaceName}` as the table suffix.
  6. Click **Save**.



Dataform applies workspace compilation overrides to all the workspaces in your repository.

### Edit workspace compilation overrides

To edit Dataform workspace compilation overrides, follow these steps:

  1. In your repository, go to **Settings**.
  2. Click **Edit**.
  3. Edit workspace compilation overrides, and then click **Save**.



### Delete workspace compilation overrides

To delete Dataform workspace compilation overrides, follow these steps:

  1. In your repository, go to **Settings**.
  2. Click **Edit**.
  3. In the **Workspace compilation overrides** pane, click **Clear all** , and then click **Save**.



## Configure compilation overrides with the Dataform API

This section shows you how to create and run a compilation result with compilation overrides by using the Dataform API.

### About Dataform API compilation overrides

To run your workflow, Dataform compiles your code to SQL to create a [compilation result](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults). Then, during a [workflow invocation](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations), Dataform runs the compilation result in BigQuery.

By default, Dataform uses the settings in the [workflow settings file](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings) to create the compilation result. To isolate data run at different stages of your development lifecycle, you can override the default settings with compilation overrides.

By passing Dataform API requests in the terminal, you can create and run a single compilation result with compilation overrides. You can create a compilation result of a workspace or of a selected Git commitish.

To create a compilation result with compilation overrides, you need to raise the Dataform API [`compilationResults.create`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults/create) request. In the request, you need to specify a source, which should be a workspace or Git commitish, for Dataform to compile into the compilation result. In the [`CodeCompilationConfig` object](https://docs.cloud.google.com/dataform/reference/rest/v1/CodeCompilationConfig) of the `compilationResults.create` request, you can configure compilation overrides.

You can then run the created compilation result in a Dataform API [`workflowInvocations.create`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/create) request.

You can configure the following Dataform API compilation overrides:

Google Cloud project
    

The project in which Dataform runs the compilation result, set in the `workflow_settings.yaml` file as the `defaultProject` property or in the `dataform.json` file as the `defaultDatabase` property.

**Note:** The BigQuery job responsible for the execution is created in the same Google Cloud project in which the Dataform repository is present.
Table prefix
    

The custom prefix added to all table names in the compilation result.

Schema suffix
    

The custom suffix appended to the schema of tables defined in the `defaultDataset` property in the `workflow_settings.yaml` file, the `defaultSchema` property in the `dataform.json` file, or in the `schema` parameter in the `config` block of a table.

Value of a compilation variable
    

The value of a compilation variable to be used in the compilation result. You can use compilation variables to run tables conditionally.

As an alternative to Dataform API compilation overrides that you can only use for one compilation result, you can configure workspace compilation overrides in the Google Cloud console.

To learn about alternative ways to configure compilation overrides in Dataform, see Introduction to the workflow lifecycle in Dataform.

### Set a compilation result source

To raise the Dataform API [`compilationResults.create`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults/create) request, you need to specify a source for the compilation result.

You can set a Dataform workspace or a Git branch, Git tag, or Git commit SHA as the source in the [`compilationResults.create`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults/create) request.

#### Set a workspace as a compilation result source

  * In the [`compilationResults.create`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults/create) request, populate the `workspace` property with the path of a selected Dataform workspace in the following format:
        
        {
        "workspace": "projects/PROJECT_NAME/locations/LOCATION/repositories/REPOSITORY_NAME/workspaces/WORKSPACE_NAME"
        }
        

Replace the following:

    * `PROJECT_NAME`: the name of your Google Cloud project.
    * `LOCATION`: the location of your Dataform repository, set in workflow settings.
    * `REPOSITORY_NAME`: the name of your Dataform repository.
    * `WORKSPACE_NAME`: the name of your Dataform workspace.



The following code sample shows the `workspace` property in the `compilationResults.create` request set to a workspace called `"sales-test"`:
    
    
    {
    "workspace": "projects/analytics/locations/europe-west4/repositories/sales/workspaces/sales-test"
    }
    

#### Set a Git commitish as a compilation result source

  * In the [`compilationResults.create`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults/create) request, populate the `gitCommitish` property with the selected Git branch, tag, or commit SHA in the following format:
        
        {
          "gitCommitish": "GIT_COMMITISH"
        }
        

Replace `GIT_COMMITISH` with the selected Git branch, Git tag, or a Git commit SHA for the compilation result.




The following code sample shows the `gitCommitish` property in the `compilationResults.create` request set to `"staging"`:
    
    
    {
      "gitCommitish": "staging"
    }
    

### Override the default project

To create staging or production tables in a Google Cloud project separate from the project used for development, you can pass a different project ID in the [`CodeCompilationConfig` object](https://docs.cloud.google.com/dataform/reference/rest/v1/CodeCompilationConfig) in the Dataform API [`compilationResults.create`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults/create) request.

Passing a separate default project ID in the `compilationResults.create` request overrides the default project ID configured in the [workflow settings file](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings), but it does not override project IDs configured in individual tables.

  * To override the default project ID, set the `defaultDatabase` property to the selected project ID in the `CodeCompilationConfig` object in the following format:
        
        {
          "codeCompilationConfig": {
            "defaultDatabase": "PROJECT_NAME"
          }
        }
        

Replace `PROJECT_NAME` with the project ID that you want to set for the compilation result.


**Note:** The BigQuery job responsible for the execution is created in the same Google Cloud project in which the Dataform repository is present.

### Add a table prefix

To quickly identify tables from the compilation result, you can add a prefix to all the table names in the compilation result by passing the table prefix in the [`CodeCompilationConfig` object](https://docs.cloud.google.com/dataform/reference/rest/v1/CodeCompilationConfig) in the Dataform API [`compilationResults.create` request](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults/create).

  * To add a table prefix, set the `tablePrefix` property in the `CodeCompilationConfig` object in the following format:
        
        {
          "codeCompilationConfig": {
            "tablePrefix": "PREFIX",
          }
        }
        

Replace `PREFIX` with the prefix you want to append, for example, `staging`.

For example, if your table name is `table_name`, Dataform creates tables with the `staging_table_name` name.




### Append a schema suffix

To separate development, staging, and production data, you can append a suffix to schemas in a compilation result by passing the schema suffix in the [`CodeCompilationConfig` object](https://docs.cloud.google.com/dataform/reference/rest/v1/CodeCompilationConfig) in the Dataform API [`compilationResults.create` request](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults/create).

  * To append a schema suffix, set the `schemaSuffix` property in the `CodeCompilationConfig` object in the following format:
        
        {
          "codeCompilationConfig": {
            "schemaSuffix": "SUFFIX",
          }
        }
        

Replace `SUFFIX` with the suffix you want to append, for example, `_staging`.

For example, if your `defaultDataset` property in the `workflow_settings.yaml` file is set to `dataform`, Dataform creates tables in the `dataform_staging` schema.


**Note:** The `CodeCompilationConfig` `schemaSuffix` parameter overrides the schemas configured in the `config` block of individual files.

### Run selected files conditionally with compilation variables

To run a selected table only in a specific execution setting, you can [create a compilation variable](https://docs.cloud.google.com/dataform/docs/manage-repository#create-compilation-variables) for the execution setting and then pass its value in the [`CodeCompilationConfig` object](https://docs.cloud.google.com/dataform/reference/rest/v1/CodeCompilationConfig) in the Dataform API [`compilationResults.create` request](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults/create) .

To run a table conditionally in a specific execution setting by using the Dataform API, follow these steps:

  1. [Create a compilation variable and add it to selected tables](https://docs.cloud.google.com/dataform/docs/manage-repository#create-compilation-variables).
  2. Set the YOUR_VARIABLE and VALUE key-value pair in the `codeCompilationConfig` block of a [Dataform API](https://docs.cloud.google.com/dataform/reference/rest) compilation request in the following format:
         
         {
           "codeCompilationConfig": {
             "vars": {
               "YOUR_VARIABLE": "VALUE"
             }
           }
         }
         

  3. Replace `YOUR_VARIABLE` with the name of your variable, for example `executionSetting`.

  4. Replace `VALUE` with the value of the variable for this compilation result that fulfills the [`when` condition set in the selected tables](https://docs.cloud.google.com/dataform/docs/manage-repository#create-compilation-variables).




The following code sample shows the `executionSetting` variable passed to a [Dataform API](https://docs.cloud.google.com/dataform/reference/rest) compilation request:
    
    
    {
      "gitCommitish": "staging",
      "codeCompilationConfig": {
        "vars": {
          "executionSetting": "staging"
        }
      }
    }
    

### Run a compilation result with compilation overrides

  * To run the compilation result created by a [`compilationResults.create`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults/create) request, pass the compilation result ID returned by the `compilationResults.create` request in a [`workflowInvocations.create`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/create) request.



The following code sample shows a compilation result ID passed in a [`workflowInvocations.create`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/create) request:
    
    
    {
      "compilationResult": "projects/my-project-name/locations/europe-west4/repositories/my-repository-name/compilationResults/7646b4ed-ac8e-447f-93cf-63c43249ff11"
    }
    

## Create a release configuration

This section shows you how to create a release configuration in Dataform to configure templates of compilation settings, which you can run on a schedule. You can use release configurations to configure execution environments, for example, staging and production.

To run workflows in BigQuery, Dataform compiles SQL workflow code into a [compilation result](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults#resource:-compilationresult). This process happens automatically when you develop a workflow in a Dataform workspace.

Release configurations let you customize compilation results. You can use them to create execution environments, for example, staging.

#### Release configuration settings

In a release configuration, you can configure compilation overrides of [workflow settings](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings), set compilation variables, and set the frequency of creating compilation results.

A Dataform release configuration contains the following compilation settings:

Release settings
    The ID of the release, Git commitish for compilation results, and frequency of creating compilation results. Frequency is an optional setting. If set, the minimum frequency is 1 hour.
Compilation overrides
    Overrides of the Google Cloud project, table prefix, schema suffix, and [compilation variables](https://docs.cloud.google.com/dataform/docs/manage-repository#create-compilation-variables) defined in [workflow settings](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings).

#### How a release configuration works

Dataform creates compilation results from a release configuration at the specified frequency, or when you trigger compilation. Frequency is an optional setting and it is not required to create a release configuration. If set, the minimum frequency is 1 hour. You can manually trigger compilation on the **Release configuration details** page, or trigger compilation with the [Dataform API `releaseConfigs` method](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.releaseConfigs).

During compilation, Dataform pulls code from the specified Git commitish of your repository. Then, Dataform compiles the code with the applied compilation overrides (if there are any), and creates the compilation result. The latest compilation result created for the release configuration is the live compilation result.

You can schedule executions of compilation results from release configurations in [workflow configurations](https://docs.cloud.google.com/dataform/docs/schedule-runs#workflow-configurations). You can also run a selected release configuration outside of any schedule. During a workflow configuration execution, Dataform runs the live compilation result from the selected release configuration.

### Create a release configuration

To create a Dataform release configuration, follow these steps:

  1. In your repository, go to **Releases & Scheduling**.
  2. In the **Release configurations** section, click **Create**.
  3. In the **Create release configuration** pane, configure release settings.

     1. In the **Release ID** field, enter a unique ID for the release configuration.

IDs can only include numbers, letters, hyphens, and underscores.

     2. In the **Git commitish** field, enter the Git branch or Git commit SHA for the release.

In a Dataform repository not connected to a remote repository, the value is always `main`.

     3. Optional: In the **Frequency** field, select the frequency of creating compilation results.

If set, the minimum frequency is 1 hour.

To disable automatic releases, leave the **Frequency** field empty.

**Note:** On a Dataform repository that isn't connected to a third-party Git repository, the **Frequency** field is hidden.
  4. Optional: In the **Compilation overrides** section, configure compilation settings.

     1. In the **Google Cloud Project ID** field, enter the ID of the Google Cloud project in which you want to store the compilation result.
     2. In the **Schema suffix** field, enter a suffix to append to the schema configured in [workflow settings](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings).
     3. In the **Table prefix** field, enter a prefix for all table names.
  5. Optional: In the **Compilation variables** section, set the compilation variables.

     1. Click **Add variable**.
     2. In the **Key** field, enter the compilation variable.
     3. In the **Value** field, enter the value for the compilation variable.
     4. To add another compilation variable, click **Add variable**.
  6. Click **Create**.




If you override the default project, make sure [your custom service account has access](https://docs.cloud.google.com/dataform/docs/access-control#grant-dataform-required-access) to the project set in the release configuration.

For example, the following release configuration creates a `production` compilation result from the `main` branch every hour, without any compilation overrides:

  * **Release ID** : `production`
  * **Git commitish** : `main`
  * **Frequency** : hourly
  * No compilation overrides



### View details of a release configuration

You can view the following details of a release configuration:

  * Release settings 
    * Git commitish
    * Latest compilation result timestamp
    * Cron schedule
    * Compilation overrides
    * Compilation variables
  * Live compilation result 
    * Creation timestamp
    * Git commitish
    * Commit SHA
  * Past compilation results



To view details of a release configuration, follow these steps:

  1. In your repository, go to **Releases & Scheduling**.
  2. Select a release configuration.
  3. On the **Release configuration details** page, inspect the details of the release configuration.



The **Scheduled compilation results** table displays past compilation results created automatically by the release configuration.

The **Manual/API compilation results** table displays compilation results created manually or through calls to the Dataform API out of the latest 1,000 compilation results in the repository.

### Manually trigger compilation

To manually create a compilation result from a selected release configuration, follow these steps:

  1. In your repository, go to **Releases & Scheduling**.
  2. Select a release configuration.
  3. On the **Release configuration details** page, click **New compilation**.



If you're using the UI, a newly compiled result automatically goes live for your release configuration. If you're using the API, you must create a new compilation result from the release configuration and then [update the release configuration](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.releaseConfigs/patch) to set the `releaseCompilationResult` field with this new value.

Manual compilation results are displayed in the **Manual/API compilation results** table on the **Release configuration details** page.

### Trigger execution of a release configuration

To trigger execution of the live compilation result in a selected release configuration to BigQuery, follow these steps:

  1. In your repository, go to **Releases & Scheduling**.
  2. In the **Release configurations** section, click **Start execution**.
  3. In the **Execute manual workflow** pane, in the **Release configuration** list, select a release configuration.
  4. Select the workflow actions to be run: 
     1. To run the entire workflow, click **All actions**.
     2. To run selected actions in the workflow, click **Selection of actions** , and then select actions.
     3. To run actions with selected tags, click **Selection of tags** , and then select tags.
  5. Optional: To run selected actions or tags and their dependencies, select the **Include dependencies** option.
  6. Optional: To run selected actions or tags and their dependents, select the **Include dependents** option.
  7. Optional: To rebuild all tables from scratch, select the **Run with full refresh** option.

Without this option, Dataform updates incremental tables without rebuilding them from scratch.

  8. Click **Start execution**.




### Edit a release configuration

To edit a release configuration, follow these steps:

  1. In your repository, go to **Releases & Scheduling**.
  2. By the release configuration that you want to edit, click the more_vert **More** menu, and then click **Edit**.
  3. In the **Edit release configuration** pane, edit the release configuration settings, and then click **Save**.



### Delete a release configuration

To delete a release configuration, follow these steps:

  1. In your repository, go to **Releases & Scheduling**.
  2. By the release configuration that you want to delete, click the more_vert **More** menu, and then click **Delete**.
  3. In the **Delete release configuration** dialog, click **Delete**.



## What's next

  * To learn how to automate compilations and executions, see [Automate runs with Cloud Build triggers](https://docs.cloud.google.com/dataform/docs/schedule-runs#cloud-build-triggers).
  * To learn about best practices for the workflow lifecycle in Dataform, see [Best practices for the workflow lifecycle](https://docs.cloud.google.com/dataform/docs/managing-code-lifecycle).
  * To learn how to manually trigger execution in a workspace, see [Trigger execution](https://docs.cloud.google.com/dataform/docs/trigger-execution).
  * To learn how to create workflow configurations, see [Schedule runs with workflow configurations](https://docs.cloud.google.com/dataform/docs/schedule-runs#workflow-configurations).
  * To learn more about the Dataform API, see [Dataform API](https://docs.cloud.google.com/dataform/reference/rest).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
