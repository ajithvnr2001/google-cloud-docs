---
url: https://docs.cloud.google.com/dataform/docs/schedule-runs/
title: Schedule runs \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:39.539195+00:00
---

# Schedule runs  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/schedule-runs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback 

#  Schedule runs Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to do the following in Dataform:

  * Schedule runs with workflow configurations.
  * Schedule runs with Workflows and Cloud Scheduler.
  * Schedule runs with Managed Service for Apache Airflow.
  * Automate runs with Cloud Build triggers.



The following table compares the methods:

Method | Goal | Trigger Type  
---|---|---  
Workflow configurations | Standard, time-based production runs within Dataform. | Time-based  
Workflows and Cloud Scheduler | Lightweight, serverless orchestration of Dataform alongside other APIs. | Time-based or event-driven  
Managed Airflow | Complex pipelines with dependencies outside of BigQuery. | Time-based or event-driven  
Cloud Build triggers | Automating releases immediately after a Git push. | Event-driven  
  
## Before you begin

To schedule runs with workflow configurations or schedule runs with workflows and Cloud Scheduler, do the following:

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Select or [create a repository](https://docs.cloud.google.com/dataform/docs/create-repository).

**Note:** The Dataform repositories list includes only repositories created for Dataform workflow development. Repositories for BigQuery Studio assets, such as notebooks or saved queries, are managed separately and don't appear in this list.
  3. Create a [release configuration](https://docs.cloud.google.com/dataform/docs/configure-compilation#create-release-configuration).




To schedule runs with Managed Service for Apache Airflow, do the following:

  1. Select or [create a Dataform repository](https://docs.cloud.google.com/dataform/docs/create-repository).
  2. [Grant Dataform access to BigQuery](https://docs.cloud.google.com/dataform/docs/access-control#grant-dataform-required-access).
  3. Select or [create a Dataform workspace](https://docs.cloud.google.com/dataform/docs/create-workspace).
  4. [Create at least one table](https://docs.cloud.google.com/dataform/docs/create-tables#create-table).
  5. Create a [Managed Airflow 2 environment](https://docs.cloud.google.com/composer/docs/composer-2/create-environments).



### Required roles

To get the permissions that you need to complete the tasks in this document, ask your administrator to grant you the following IAM roles: 

  * [Dataform Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.admin) (`roles/dataform.admin`) on repositories
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the custom service account
  * [Composer Worker ](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`) on the [Managed Airflow environment's service account](https://docs.cloud.google.com/composer/docs/composer-2/access-control#about-service)
  * Automate runs with Cloud Build: 
    * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`) on the custom service account
    * [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`) on the project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Important:** To schedule workflow runs, you must use a custom service account or user credentials for a Google Account .

To use a custom service account when creating a workflow configuration, [grant access to the custom service account](https://docs.cloud.google.com/dataform/docs/access-control#grant-dataform-required-access).

To use user credentials for a Google Account when creating a workflow configuration, [grant access to the Google Account](https://docs.cloud.google.com/dataform/docs/access-control#dataform-required-roles).

To enable scheduled executions for a workflow configuration, you must grant the `iam.serviceAccounts.actAs` permission to the [default Dataform service agent](https://docs.cloud.google.com/dataform/docs/access-control#about-service-accounts) for the custom service account used in the workflow configuration. This permission is available in the [Service Account User role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`). For more information, see [Use strict act-as mode](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode).

To enhance security for scheduling, see [Implement enhanced scheduling permissions](https://docs.cloud.google.com/dataform/docs/access-control#enhanced-scheduling-permissions).

To prevent users from scheduling or running workflows with end user credentials, organization administrators can [create a custom organization policy constraint](https://docs.cloud.google.com/dataform/docs/create-custom-constraints) that denies setting `end_user_auth_config`.

## Schedule runs with workflow configurations

This section shows you how to create a workflow configuration in Dataform to schedule and configure workflow runs. You can use workflow configurations to execute Dataform workflows on a schedule.

### About workflow configurations

To schedule Dataform runs of all or selected workflow actions in BigQuery, you can create workflow configurations. In a workflow configuration, you select a compilation release configuration, select workflow actions for execution, and set the run schedule.

Then, during a scheduled run of your workflow configuration, Dataform deploys your selection of actions from the latest compilation result in your release configuration to BigQuery. You can also manually trigger the run of a workflow configuration with the [Dataform API workflowConfigs](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowConfigs).

**Note:** If a scheduled workflow configuration run doesn't finish before the start of the next scheduled run, the next scheduled run is skipped and marked with an error.

A Dataform workflow configuration contains the following run settings:

  * ID of the workflow configuration.
  * Release configuration.
  * Service account.

This is the custom service account that's associated with the workflow configuration. You can select a custom service account that's associated with your Google Cloud project, or you can manually enter a different service account. By default, workflow configurations use the same service accounts as their [repositories](https://docs.cloud.google.com/dataform/docs/create-repository).

Service account credentials are the default authorization method for scheduled workflow configuration creation and executions.

**Note:** You can attach a maximum of 100 unique service accounts to all the workflow configurations in a repository.
  * Google Account user credentials

Google Account user credentials are the default authorization method for manual, non-scheduled workflow configuration creation and executions. For more information, see Authorize your Google Account.

**Note:** Organization administrators can disallow the use of end user credentials by creating a custom organization policy constraint that denies setting `end_user_auth_config`. For more information, see [Create custom organization policy constraints](https://docs.cloud.google.com/dataform/docs/create-custom-constraints).
  * Workflow actions to be executed:

    * All actions.
    * Selection of actions.
    * Selection of [tags](https://docs.cloud.google.com/dataform/docs/configure-additional-actions#add-execution-tags).
  * Run schedule and time zone.




### Create a workflow configuration

To create a Dataform workflow configuration, follow these steps:

  1. In your repository, go to **Releases & Scheduling**.
  2. In the **Workflow configurations** section, click **Create**.
  3. In the **Create workflow configuration** pane, in the **Configuration ID** field, enter a unique ID for the workflow configuration.

IDs can only include numbers, letters, hyphens, and underscores.

  4. In the **Release configuration** menu, select a [compilation release configuration](https://docs.cloud.google.com/dataform/docs/configure-compilation#create-release-configuration).

  5. In the **Authentication** section, authorize the workflow configuration with your Google Account user credentials or a service account.

     * To use your Google Account user credentials, select **Execute with my user credentials**.

Optional: In the **Extended access options** section, select the additional services that your workflow requires:

       * **Knowledge Catalog** : Allows Google Cloud Knowledge Catalog metadata updates.
       * **Google Drive** : Allows read-only access to Google Drive files.
       * **Bigtable** : Allows read-only access to Google Bigtable data.
     * To use a custom service account, select **Execute with selected service account** , and then select the service account associated with your Google Cloud project that you have access to. If you don't select a service account, the workflow configuration uses the service account of the repository.

**Note:** You can't run workflows with the default Dataform service agent. You must use either a custom service account or your Google Account user credentials.
  6. Optional: In the **Schedule frequency** field, enter the frequency of runs in the [unix-cron format](https://docs.cloud.google.com/scheduler/docs/configuring/cron-job-schedules#defining_the_job_schedule).

To verify that Dataform executes the latest compilation result in the corresponding release configuration, keep a minimum one-hour break between the time of compilation result creation and the time of scheduled execution.

  7. Optional: In the **Timezone** menu, select the time zone for runs.

The default time zone is UTC.

  8. Select the workflow actions to be executed:

     * To execute the entire workflow, click **All actions**.
     * To execute selected actions in the workflow, click **Selection of actions** , and then select actions.
     * To execute actions with selected tags, click **Selection of tags** , and then select tags.
     * Optional: To execute selected actions or tags and their dependencies, select the **Include dependencies** option.
     * Optional: To execute selected actions or tags and their dependents, select the **Include dependents** option.
     * Optional: To rebuild all tables from scratch, select the **Run with full refresh** option.

Without this option, Dataform updates incremental tables without rebuilding them from scratch.

     * Optional: Set the BigQuery query job priority with the **Execute as interactive job with high priority (default)** option. By default, BigQuery runs queries as [interactive query jobs](https://docs.cloud.google.com/bigquery/docs/running-queries#interactive-batch), which are intended to start running as quickly as possible. Clearing this option runs the queries as [batch query jobs](https://docs.cloud.google.com/bigquery/docs/running-queries#interactive-batch), which have lower priority.

  9. Click **Create**. If you selected **Execute with my user credentials** for your authentication method, you must authorize your Google Account.




For example, the following workflow configuration executes actions with the `hourly` tag every hour in the CEST timezone:

  * **Configuration ID** : `production-hourly`
  * **Release configuration** : -
  * **Frequency** : `0 * * * *`
  * **Timezone** : `Central European Summer Time (CEST)`
  * Selection of workflow actions: selection of tags, `hourly` tag



### Authorize your Google Account

To authenticate the resource with your [Google Account](https://docs.cloud.google.com/iam/docs/principals-overview#google-account) user credentials, you must manually grant permission for BigQuery pipelines to get the access token for your Google Account and access the source data on your behalf. You can grant manual approval with the OAuth dialog interface. If you select any **Extended access options** , you must grant access to those services—for example, Google Drive or Knowledge Catalog.

**Note:** Context-Aware Access (CAA) policies—including IP-based, geolocation-based, and device compliance policies—aren't supported when executing or scheduling BigQuery pipelines with user credentials for a Google Account, because the token requests originate from Google infrastructure. CAA policies block these executions unless the Dataform OAuth client ID is [exempted from the policies](https://docs.cloud.google.com/dataform/docs/troubleshooting#euc-permission-denied).

You only need to give permission to BigQuery pipelines once.

To revoke the permission that you granted, follow these steps:

  1. Go to your [Google Account page](https://myaccount.google.com/).
  2. Click **BigQuery Pipelines**.
  3. Click **Remove access**.

**Warning:** Revoking access permissions prevents any future pipeline runs that this Google Account owns across all regions.

Changing the workflow configuration owner by updating credentials also requires manual approval if the new Google Account owner has never created a workflow configuration before.

### Edit a workflow configuration

To edit a workflow configuration, follow these steps:

  1. In your repository, go to **Releases & Scheduling**.
  2. By the workflow configuration that you want to edit, click the more_vert **More** menu, and then click **Edit**.
  3. In the **Edit workflow configuration** pane, edit the workflow configuration settings, and then click **Save**.



### Delete a workflow configuration

To delete a workflow configuration, follow these steps:

  1. In your repository, go to **Releases & Scheduling**.
  2. By the workflow configuration that you want to delete, click the more_vert **More** menu, and then click **Delete**.
  3. In the **Delete release configuration** dialog, click **Delete**.



## Schedule runs with Workflows and Cloud Scheduler

This section shows you how to schedule runs of Dataform workflows using Workflows and Cloud Scheduler.

### About scheduled workflow runs

You can set the frequency of your Dataform workflow runs by creating a Cloud Scheduler job that triggers a Workflows workflow. Workflows executes services in an orchestration workflow that you define.

Workflows executes your Dataform workflow in a two-step process. First, it pulls your Dataform repository code from your Git provider and compiles it into a compilation result. Then, it uses the compilation result to create a Dataform workflow and executes it at the frequency that you set.

**Note:** When scheduling executions with Workflows, calling `createCompilationResult` with `gitCommitish` requires Dataform to clone your remote Git repository over the network on every run. Because external network connections can be temporarily unreliable during frequent or concurrent compilations, we recommend scheduling production workflows using [release configurations](https://docs.cloud.google.com/dataform/docs/configure-compilation#create-release-configuration), or configuring automated retries with exponential backoff in your orchestration workflow. For more information, see [Remote repository cannot be reached](https://docs.cloud.google.com/dataform/docs/troubleshooting#remote-repository-not-reached).

### Create a scheduled orchestration workflow

To schedule runs of your Dataform workflow, use Workflows to create an orchestration workflow and add a Cloud Scheduler job as a trigger.

  1. Workflows uses service accounts to give workflows access to Google Cloud resources. Create a [service account](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#service-account-invoker) and grant it the following permissions:

     * [Dataform Editor role](https://docs.cloud.google.com/dataform/docs/access-control#dataform.editor) (`roles/dataform.editor`).
     * [Service Account User role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the custom service account used in Dataform.
     * The minimum permissions required to manage your orchestration workflow. For more information, see [Grant a workflow permission to access Google Cloud resources](https://docs.cloud.google.com/workflows/docs/authentication).
  2. [Create an orchestration workflow](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#create_a_workflow) and use the following YAML source code as your workflow definition:
         
         main:
             steps:
             - init:
                 assign:
                 - repository: projects/PROJECT_ID/locations/REPOSITORY_LOCATION/repositories/REPOSITORY_ID
             - createCompilationResult:
                 call: http.post
                 args:
                     url: ${"https://dataform.googleapis.com/v1/" + repository + "/compilationResults"}
                     auth:
                         type: OAuth2
                     body:
                         gitCommitish: GIT_COMMITISH
                 result: compilationResult
             - createWorkflowInvocation:
                 call: http.post
                 args:
                     url: ${"https://dataform.googleapis.com/v1/" + repository + "/workflowInvocations"}
                     auth:
                         type: OAuth2
                     body:
                         compilationResult: ${compilationResult.body.name}
                 result: workflowInvocation
             - complete:
                 return: ${workflowInvocation.body.name}
         

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project.
     * REPOSITORY_LOCATION: the location of your Dataform repository.
     * REPOSITORY_ID: the name of your Dataform repository.
     * GIT_COMMITISH: the Git branch that you want to execute Dataform code from. For a newly created repository, replace with `main`.
  3. [Schedule the orchestration workflow using Cloud Scheduler](https://docs.cloud.google.com/workflows/docs/schedule-workflow).




### Customize the Dataform workflow create compilation result request

You can [update the existing orchestration workflow](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#update_a_workflow) and define the Dataform workflow create compilation result request settings in the YAML format. For more information about the settings, see the [`projects.locations.repositories.compilationResults` REST resource reference](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults).

For example, to add a `_dev` `schemaSuffix` setting to all actions during compilation, replace the `createCompilationResult` step body with the following code snippet:
    
    
        - createCompilationResult:
            call: http.post
            args:
                url: ${"https://dataform.googleapis.com/v1/" + repository + "/compilationResults"}
                auth:
                    type: OAuth2
                body:
                    gitCommitish: GIT_COMMITISH
                    **codeCompilationConfig:
                        schemaSuffix: dev**
    

You can also pass additional settings as runtime arguments in a Workflows run request and access those arguments using variables. For more information, see [Pass runtime arguments in an execution request](https://docs.cloud.google.com/workflows/docs/passing-runtime-arguments).

### Customize the Dataform workflow invocation request

You can [update the existing orchestration workflow](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#update_a_workflow) and define the Dataform workflow invocation request settings in the YAML format. For more information about the invocation request settings, see the [`projects.locations.repositories.workflowInvocations` REST resource reference](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations#WorkflowInvocation).

For example, to only execute actions with the `hourly` tag with all the transitive dependencies included, replace the `createWorkflowInvocation` body with the following code snippet:
    
    
        - createWorkflowInvocation:
            call: http.post
            args:
                url: ${"https://dataform.googleapis.com/v1/" + repository + "/workflowInvocations"}
                auth:
                    type: OAuth2
                body:
                    compilationResult: ${compilationResult.body.name}
                    invocationConfig:**includedTags:
                        - hourly
                        transitiveDependenciesIncluded: true**
    

You can also pass additional settings as runtime arguments in a Workflows run request and access those arguments using variables. For more information, see [Pass runtime arguments in an execution request](https://docs.cloud.google.com/workflows/docs/passing-runtime-arguments).

## Schedule runs with Managed Airflow

You can use [Managed Airflow 2](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview) to schedule Dataform runs. Dataform does not support [Managed Airflow 1](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview).

To manage schedules for Dataform runs with Managed Airflow 2, you can use [Dataform operators](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/dataform.html) in Airflow Directed Acyclic Graphs (DAGs). You can create an Airflow DAG that schedules Dataform workflow invocations.

Dataform provides various Airflow operators. These include operators for getting a compilation result, getting a workflow invocation, and canceling a workflow invocation. To view the complete list of available Dataform Airflow operators, see [Google Dataform Operators](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/dataform.html).

**Note:** When scheduling workflow executions with Managed Airflow, calling `DataformCreateCompilationResultOperator` with `git_commitish` requires Dataform to clone your remote Git repository over the network on every run. Because external network connections can be temporarily unreliable during frequent or concurrent compilations, we recommend scheduling production workflows using [release configurations](https://docs.cloud.google.com/dataform/docs/configure-compilation#create-release-configuration), or configuring automated retries with exponential backoff on your operator. For more information, see [Remote repository cannot be reached](https://docs.cloud.google.com/dataform/docs/troubleshooting#remote-repository-not-reached).

### Install the `google-cloud-dataform` PyPI package

If you use Managed Airflow 2 versions `2.0.25` and later, this package is preinstalled in your environment. You don't need to install it.

**Important:** Managed Airflow images with Airflow `2.3.3` use the public version `8.1.0` of the `apache-airflow-providers-google` package. Version `8.1.0` does not include Dataform connectors. Support for Dataform connectors will be available starting from version `8.3.0`, which will be released together with Managed Airflow images with Airflow `2.3.4`. For more information, see [Managed Airflow release notes](https://docs.cloud.google.com/composer/docs/release-notes#September_29_2022).

If you use earlier versions of Managed Airflow 2, [install the `google-cloud-dataform` PyPI package](https://docs.cloud.google.com/composer/docs/composer-2/install-python-dependencies#install-pypi).

In the PyPI packages section, specify version `==0.2.0`.

### Create an Airflow DAG that schedules Dataform workflow invocations

To manage scheduled runs of Dataform workflows with Managed Airflow 2, [write the DAG](https://docs.cloud.google.com/composer/docs/how-to/using/writing-dags) using [Dataform Airflow operators](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/dataform.html), then [upload it to your environment's bucket](https://docs.cloud.google.com/composer/docs/composer-2/manage-dags).

The following code sample shows an Airflow DAG that creates a Dataform compilation result and starts a Dataform workflow invocation:
    
    
    from datetime import datetime
    
    from airflow import models
    from airflow.models.baseoperator import chain
    from airflow.providers.google.cloud.operators.dataform import (
        DataformCreateCompilationResultOperator,
        DataformCreateWorkflowInvocationOperator,
    )
    
    DAG_ID = "dataform"
    PROJECT_ID = "PROJECT_ID"
    REPOSITORY_ID = "REPOSITORY_ID"
    REGION = "REGION"
    GIT_COMMITISH = "GIT_COMMITISH"
    
    with models.DAG(
        DAG_ID,
        schedule_interval='@once',  # Override to match your needs
        start_date=datetime(2022, 1, 1),
        catchup=False,  # Override to match your needs
        tags=['dataform'],
    ) as dag:
    
        create_compilation_result = DataformCreateCompilationResultOperator(
            task_id="create_compilation_result",
            project_id=PROJECT_ID,
            region=REGION,
            repository_id=REPOSITORY_ID,
            compilation_result={
                "git_commitish": GIT_COMMITISH,
            },
        )
        create_workflow_invocation = DataformCreateWorkflowInvocationOperator(
            task_id='create_workflow_invocation',
            project_id=PROJECT_ID,
            region=REGION,
            repository_id=REPOSITORY_ID,
             workflow_invocation={
                "compilation_result": "{{ task_instance.xcom_pull('create_compilation_result')['name'] }}"
            },
        )
    
    
    create_compilation_result >> create_workflow_invocation
    

Replace the following:

  * PROJECT_ID: your Dataform Google Cloud project ID.
  * REPOSITORY_ID: the name of your Dataform repository.
  * REGION: the region in which the Dataform repository is located.
  * COMPILATION_RESULT: the name of the compilation result you want to use for this workflow invocation.
  * GIT_COMMITISH: the Git commitish in the remote Git repository of the version of your code that you want to use—for example, a branch or a Git SHA.



The following code sample shows an Airflow DAG that performs the following:

  1. Creates a Dataform compilation result.
  2. Starts an asynchronous Dataform workflow invocation.
  3. Polls the status of your workflow until it enters the expected state by using `DataformWorkflowInvocationStateSensor`.


    
    
    from datetime import datetime
    
    from google.cloud.dataform_v1 import [WorkflowInvocation](https://docs.cloud.google.com/python/docs/reference/dataform/latest/google.cloud.dataform_v1.types.WorkflowInvocation.html)
    
    from airflow import models
    from airflow.models.baseoperator import chain
    from airflow.providers.google.cloud.operators.dataform import (
        DataformCreateCompilationResultOperator,
        DataformCreateWorkflowInvocationOperator,
    )
    from airflow.providers.google.cloud.sensors.dataform import DataformWorkflowInvocationStateSensor
    
    DAG_ID = "dataform"
    PROJECT_ID = "PROJECT_ID"
    REPOSITORY_ID = "REPOSITORY_ID"
    REGION = "REGION"
    GIT_COMMITISH = "GIT_COMMITISH"
    
    with models.DAG(
        DAG_ID,
        schedule_interval='@once',  # Override to match your needs
        start_date=datetime(2022, 1, 1),
        catchup=False,  # Override to match your needs
        tags=['dataform'],
    ) as dag:
    
        create_compilation_result = DataformCreateCompilationResultOperator(
            task_id="create_compilation_result",
            project_id=PROJECT_ID,
            region=REGION,
            repository_id=REPOSITORY_ID,
            compilation_result={
                "git_commitish": GIT_COMMITISH,
            },
        )
    
    create_workflow_invocation = DataformCreateWorkflowInvocationOperator(
        task_id='create_workflow_invocation',
        project_id=PROJECT_ID,
        region=REGION,
        repository_id=REPOSITORY_ID,
        asynchronous=True,
        workflow_invocation={
            "compilation_result": COMPILATION_RESULT
        }
    )
    
    is_workflow_invocation_done = DataformWorkflowInvocationStateSensor(
        task_id="is_workflow_invocation_done",
        project_id=PROJECT_ID,
        region=REGION,
        repository_id=REPOSITORY_ID,
        workflow_invocation_id=("{{ task_instance.xcom_pull('create_workflow_invocation')['name'].split('/')[-1] }}"),
        expected_statuses={[WorkflowInvocation](https://docs.cloud.google.com/python/docs/reference/dataform/latest/google.cloud.dataform_v1.types.WorkflowInvocation.html).State.SUCCEEDED},
    )
    
    
    create_compilation_result >> create_workflow_invocation
    

Replace the following:

  * PROJECT_ID: your Dataform Google Cloud project ID.
  * REPOSITORY_ID: the name of your Dataform repository.
  * REGION: the region in which the Dataform repository is located.
  * COMPILATION_RESULT: the name of the compilation result you want to use for this workflow invocation.
  * GIT_COMMITISH: the Git commitish in the remote Git repository of the version of your code that you want to use—for example, a branch or a Git SHA.



#### Add compilation configuration parameters

You can add additional compilation configuration parameters to the `create_compilation_result` Airflow DAG object. For more information about available parameters, see the [`CodeCompilationConfig` Dataform API reference](https://docs.cloud.google.com/dataform/reference/rest/v1/CodeCompilationConfig).

  * To add compilation configuration parameters to the `create_compilation_result` Airflow DAG object, add your selected parameters to the `code_compilation_config` field in the following format:
        
        create_compilation_result = DataformCreateCompilationResultOperator(
                task_id="create_compilation_result",
                project_id=PROJECT_ID,
                region=REGION,
                repository_id=REPOSITORY_ID,
                compilation_result={
                    "git_commitish": GIT_COMMITISH,
                    "code_compilation_config": { "PARAMETER": "PARAMETER_VALUE"}
                },
            )
        

Replace the following:

    * PROJECT_ID: your Dataform Google Cloud project ID.
    * REPOSITORY_ID: the name of your Dataform repository.
    * REGION: the region in which the Dataform repository is located.
    * GIT_COMMITISH: the Git commitish in the remote Git repository of the version of your code that you want to use—for example, a branch or a Git SHA.
    * PARAMETER: the selected [`CodeCompilationConfig` parameter](https://docs.cloud.google.com/dataform/reference/rest/v1/CodeCompilationConfig). You can add multiple parameters.
    * PARAMETER_VALUE: the value of the selected parameter.



The following code sample shows the `defaultDatabase` parameter added to the `create_compilation_result` Airflow DAG object:
    
    
        create_compilation_result = DataformCreateCompilationResultOperator(
            task_id="create_compilation_result",
            project_id=PROJECT_ID,
            region=REGION,
            repository_id=REPOSITORY_ID,
            compilation_result={
                "git_commitish": REMOTE_BRANCH,
                "code_compilation_config": { "default_database": "my-custom-gcp-project"}
            },
        )
    

#### Add workflow invocation configuration parameters

You can add additional workflow invocation configuration parameters to the `create_workflow_invocation` Airflow DAG object. For more information about available parameters, see the [`InvocationConfig` Dataform API reference](https://docs.cloud.google.com/dataform/reference/rest/v1/InvocationConfig).

  * To add workflow invocation configuration parameters to the `create_workflow_invocation` Airflow DAG object, add your selected parameters to the `invocation_config` field in the following format:
        
        create_workflow_invocation = DataformCreateWorkflowInvocationOperator(
                task_id='create_workflow_invocation',
                project_id=PROJECT_ID,
                region=REGION,
                repository_id=REPOSITORY_ID,
                workflow_invocation={
                    "compilation_result": "{{ task_instance.xcom_pull('create_compilation_result')['name'] }}",
                    "invocation_config": { "PARAMETER": PARAMETER_VALUE }
                },
            )
        
        

Replace the following:

    * PROJECT_ID: your Dataform Google Cloud project ID.
    * REPOSITORY_ID: the name of your Dataform repository.
    * REGION: the region in which the Dataform repository is located.
    * PARAMETER: the selected [`InvocationConfig` parameter](https://docs.cloud.google.com/dataform/reference/rest/v1/InvocationConfig). You can add multiple parameters.
    * PARAMETER_VALUE: the value of the selected parameter.



The following code sample shows the `includedTags[]` and `transitiveDependenciesIncluded` parameters added to the `create_workflow_invocation` Airflow DAG object:
    
    
        create_workflow_invocation = DataformCreateWorkflowInvocationOperator(
            task_id='create_workflow_invocation',
            project_id=PROJECT_ID,
            region=REGION,
            repository_id=REPOSITORY_ID,
            workflow_invocation={
                "compilation_result": "{{ task_instance.xcom_pull('create_compilation_result')['name'] }}",
                "invocation_config": { "included_tags": ["daily"], "transitive_dependencies_included": true }
            },
        )
    
    

## Automate runs with Cloud Build triggers

If you want to move beyond the time-based schedules in a release configuration, you can use a Cloud Build trigger to create an event-driven pipeline. This approach automatically compiles your code whenever a new commit is pushed to a Git branch and immediately triggers a Dataform workflow invocation to update your data.

### Prepare your resources

  1. In your Google Cloud project, enable the Dataform and Cloud Build APIs:

[Enable the Dataform API](https://console.cloud.google.com/apis/library/dataform.googleapis.com)

[Enable the Cloud Build API](https://console.cloud.google.com/apis/library/cloudbuild.googleapis.com)

  2. Ensure that you have the following:

     * A [custom service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) to use for compilation. Note the email address of the service account, for example, `dataform-compiler@PROJECT_NUMBER.iam.gserviceaccount.com`.

     * A [Dataform repository connected to a Git provider](https://docs.cloud.google.com/dataform/docs/connect-repository).

     * A [release configuration](https://docs.cloud.google.com/dataform/docs/configure-compilation#create-release-configuration) in your Dataform repository. Note the release configuration ID.

     * A [workflow configuration](https://docs.cloud.google.com/dataform/docs/schedule-runs#create-workflow-configuration) in your Dataform repository that uses your release configuration. Note the workflow configuration ID.




### Grant the required IAM permissions

Grant the [Dataform Admin role](https://docs.cloud.google.com/dataform/docs/access-control#dataform.admin) (`roles/dataform.admin`) to the custom service account in your Dataform repository. This role provides full access to the repository, including the permission to create compilation results, update release configurations, and start new workflow invocations. For details on how to grant an IAM role to an individual repository, see [Control access to an individual repository](https://docs.cloud.google.com/dataform/docs/access-control#control_access_to_an_individual_repository).

Grant the [Service Account User role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the workflow configuration's custom service account to the Cloud Build trigger's service account. For more information on this requirement, see [Use strict act-as mode](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode).

For Cloud Build to use your custom service account, you must grant the Cloud Build service agent the permission to act as that account. To grant impersonation permission to the Cloud Build service agent, do the following:

  1. In the Google Cloud console, go to the **Service Accounts** page.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select your custom service account.

  3. Go to the **Principals with access** tab.

  4. Click person_add **Grant Access**.

  5. In the **New principals** field, enter the email address of the Cloud Build service agent, which should be in this format:
         
         service-PROJECT_NUMBER@gcp-sa-cloudbuild.iam.gserviceaccount.com
         

Replace `PROJECT_NUMBER` with the numeral ID of your Google Cloud project. You can find your Google Cloud project ID in the Google Cloud console dashboard. For more information, see [Find the project name, number, and ID](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects).

  6. In the **Select a role** menu, select **Service Account User**.

  7. Click **Save**.




### Create the `cloudbuild.yaml` configuration file

In the root of your Git repository, create a `cloudbuild.yaml` file. Use this file to define the following multi-step script for creating a compilation result, updating the release configuration to set this compilation result as live, and starting a new workflow invocation.
    
    
    steps:
      - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk:latest'
        entrypoint: 'bash'
        args:
          - '-c'
          - |
            set -e -o pipefail # Exit script on any error
    
            # 1. Get the access token
            TOKEN=$(gcloud auth print-access-token)
    
            # 2. Define API endpoints and resource names
            RELEASE_CONFIG_RESOURCE="projects/${_PROJECT_ID}/locations/${_DATAFORM_LOCATION}/repositories/${_DATAFORM_REPO_ID}/releaseConfigs/${_RELEASE_CONFIG_ID}"
            COMPILATION_RESULTS_API="https://dataform.googleapis.com/v1/projects/${_PROJECT_ID}/locations/${_DATAFORM_LOCATION}/repositories/${_DATAFORM_REPO_ID}/compilationResults"
    
            # 3. Create the new compilation result
            echo "Creating new compilation result from $$RELEASE_CONFIG_RESOURCE..."
            CREATE_PAYLOAD="{\"releaseConfig\": \"$$RELEASE_CONFIG_RESOURCE\"}"
            curl --fail-with-body -X POST \
              -H "Authorization: Bearer $$TOKEN" \
              -H "Content-Type: application/json" \
              -d "$$CREATE_PAYLOAD" \
              "$$COMPILATION_RESULTS_API" | tee /workspace/compilation_response.json
    
      - name: 'alpine'
        entrypoint: 'bash'
        args:
          - '-c'
          - |
            set -e # Exit script on any error
    
            # 4. Parse compilation result name
            apk add --no-cache jq
            COMPILATION_NAME=$(jq -r '.name' < /workspace/compilation_response.json)
    
            echo "Successfully created compilation result: $$COMPILATION_NAME"
            echo $$COMPILATION_NAME > /workspace/compilation_result_name.txt
    
      - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk:latest'
        entrypoint: 'bash'
        args:
          - '-c'
          - |
            set -e # Exit script on any error
            # 5. Update the releaseConfig to set the new compilation result as 'live'
            COMPILATION_NAME=$(cat /workspace/compilation_result_name.txt)
            echo "Updating release config to set $$COMPILATION_NAME as live..."
            PATCH_PAYLOAD="{\"releaseCompilationResult\": \"$$COMPILATION_NAME\", \"gitCommitish\": \"$BRANCH_NAME\"}"
    
            RELEASE_CONFIG_RESOURCE="projects/${_PROJECT_ID}/locations/${_DATAFORM_LOCATION}/repositories/${_DATAFORM_REPO_ID}/releaseConfigs/${_RELEASE_CONFIG_ID}"
            RELEASE_CONFIG_PATCH_API="https://dataform.googleapis.com/v1/$${RELEASE_CONFIG_RESOURCE}"
            curl --fail-with-body -X PATCH \
              -H "Authorization: Bearer $(gcloud auth print-access-token)" \
              -H "Content-Type: application/json" \
              -d "$$PATCH_PAYLOAD" \
              "$$RELEASE_CONFIG_PATCH_API?updateMask=releaseCompilationResult"
    
            echo "Successfully updated release config."
    
      - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk:latest'
        entrypoint: 'bash'
        args:
          - '-c'
          - |
            set -e # Exit script on any error
            # 6. Launch a workflow config after recompiling the release config
            WORKFLOW_CONFIG_RESOURCE="projects/${_PROJECT_ID}/locations/${_DATAFORM_LOCATION}/repositories/${_DATAFORM_REPO_ID}/workflowConfigs/${_WORKFLOW_CONFIG_ID}"
            CREATE_WORKFLOW_PAYLOAD="{\"workflowConfig\": \"$$WORKFLOW_CONFIG_RESOURCE\"}"
    
            WORKFLOW_INVOCATIONS_API="https://dataform.googleapis.com/v1/projects/${_PROJECT_ID}/locations/${_DATAFORM_LOCATION}/repositories/${_DATAFORM_REPO_ID}/workflowInvocations"
            curl --fail-with-body -X POST \
              -H "Authorization: Bearer $(gcloud auth print-access-token)" \
              -H "Content-Type: application/json" \
              -d "$$CREATE_WORKFLOW_PAYLOAD" \
              "$$WORKFLOW_INVOCATIONS_API"
    
            echo "Successfully created a new workflow invocation."
    
    # Define substitution variables that can be set in the trigger
    substitutions:
      _DATAFORM_LOCATION: 'us-central1'  # Default, change if needed
      _DATAFORM_REPO_ID: ''              # Required: Set this in the trigger
      _RELEASE_CONFIG_ID: ''             # Required: Set this in the trigger
      _WORKFLOW_CONFIG_ID: ''            # Required: Set this in the trigger
      _PROJECT_ID: ${PROJECT_ID}         # Automatically uses the build's Project ID
    
    options:
      logging: CLOUD_LOGGING_ONLY
    

### Create the Cloud Build trigger

To create a trigger that runs your build configuration when code is pushed to your repository, do the following:

  1. In the Google Cloud console, open the Cloud Build **Triggers** page.

[Go to Triggers](https://console.cloud.google.com/cloud-build/triggers)

  2. If you haven't connected your Git repository, click **Connect repository** and follow the steps.

  3. Click **Create trigger**.

  4. Enter a name for the trigger.

  5. Select a region for the trigger.

  6. Select an event for the trigger.

  7. In the **Source** section, set the repository to your connected Git repository.

  8. Set the branch to your repository's main branch.

  9. In the **Configuration** section, select the Cloud Build configuration file, which can be a YAML or JSON file.

  10. Set the file location to `/cloudbuild.yaml` or the path to your file.

  11. In the **Substitution variables** section, add the following variables and values:

     * `_DATAFORM_REPO_ID`: your Dataform repository ID
     * `_RELEASE_CONFIG_ID`: your Dataform release configuration ID
     * `_WORKFLOW_CONFIG_ID`: your Dataform workflow configuration ID
     * Optional: `_DATAFORM_LOCATION`: your Dataform repository region, for example, `us-central1`
  12. In the **Service Account** section, select your custom service account.

  13. Click **Create**.




For more information, see [Create a build trigger](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers#build_trigger).

### Test the trigger

  1. Commit and push the `cloudbuild.yaml` file to the branch that your trigger is monitoring.
  2. To view the Cloud Build build, open the **Build History** page in the Google Cloud console.

[Go to Build History](https://console.cloud.google.com/cloud-build/builds)

  3. If the build is successful, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  4. Select your repository.

  5. Click **Releases & scheduling** and select your release configuration.

  6. In the **Manual / API compilation results** list, look for a new entry. The most recent successful compilation should be marked as the **Live compilation result** for the release configuration.

  7. Click **Workflow execution logs**.

  8. You should see a new workflow invocation launched using your selected workflow configuration.




## What's next

  * To learn how to configure Dataform compilation release configurations, see [Create a release configuration](https://docs.cloud.google.com/dataform/docs/configure-compilation#create-release-configuration).
  * To learn more about code lifecycle in Dataform, see [Introduction to code lifecycle in Dataform](https://docs.cloud.google.com/dataform/docs/configure-compilation#intro-code-lifecycle).
  * To learn more about the Dataform API, see [Dataform API](https://docs.cloud.google.com/dataform/reference/rest).
  * To learn more about Managed Airflow environments, see [Overview of Managed Airflow](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview).
  * To learn more about Workflows pricing, see [Workflows pricing](https://cloud.google.com/workflows/pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
