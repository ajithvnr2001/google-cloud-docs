---
url: https://docs.cloud.google.com/dataform/docs/quickstart-create-workflow/
title: Quickstart: Create and run a workflow \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:48:42.700727+00:00
---

# Quickstart: Create and run a workflow  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/quickstart-create-workflow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and run a workflow in Dataform

This quickstart is intended for data engineers and data analysts who want to manage data transformations in BigQuery. In this quickstart, you'll learn how to create and run a Dataform workflow using Dataform core, a SQL-based framework to transform raw data into curated, tested, and documented data assets. By using Dataform, you can develop and version-control your data modeling pipelines in a central repository, ensuring reliability and scalability.

This quickstart walks you through the following process in Dataform to create a workflow and run it in BigQuery:

  * Create a Dataform repository.
  * Create and initialize a development workspace.
  * Create a view.
  * Create a table.
  * Run the workflow.
  * View execution logs in Dataform.
  * Clean up created assets.



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the BigQuery and Dataform APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=bigquery.googleapis.com,dataform.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the BigQuery and Dataform APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=bigquery.googleapis.com,dataform.googleapis.com)




### Required roles

To get the permissions that you need to perform all the tasks in this quickstart, ask your administrator to grant you the following IAM roles: 

  * [Dataform Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.admin) (`roles/dataform.admin`) on the project or repository
  * [BigQuery Data Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`) on the project or specific datasets
  * [BigQuery Job User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`) on the project
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the custom service account



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Grant required roles

To run workflows in BigQuery, you can use a custom service account or your Google Account.

Your custom service account must have the following required roles:

  * [BigQuery Data Editor](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor) (`roles/bigquery.dataEditor`) on projects or specific BigQuery datasets to which Dataform needs both read and write access. This usually includes the project hosting your Dataform repository.
  * [BigQuery Data Viewer](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataViewer) (`roles/bigquery.dataViewer`) on projects or specific BigQuery datasets to which Dataform needs read-only access.
  * [BigQuery Job User](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser) (`roles/bigquery.jobUser`) on the project hosting your Dataform repository.



To let Dataform use your custom service account, the default Dataform service agent must have the following roles on the custom service account resource:

  * [Service Account Token Creator](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role) (`roles/iam.serviceAccountTokenCreator`)
  * [Service Account User](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



To grant these roles, follow these steps:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin)

  2. Click **Grant access**.

  3. In the **New principals** field, enter your custom service account ID.

  4. In the **Select a role** menu, select the following roles one by one, using **Add another role** for each additional role:

     * **BigQuery Data Editor**
     * **BigQuery Data Viewer**
     * **BigQuery Job User**
  5. Click **Save**.

  6. In the Google Cloud console, go to the **Service accounts** page.

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  7. Select your custom service account.

  8. Go to **Principals with access** , and then click **Grant access**.

  9. In the **New principals** field, enter your default Dataform service agent ID.

Your default Dataform service agent ID is in the following format:
         
         service-PROJECT_NUMBER@gcp-sa-dataform.iam.gserviceaccount.com
         

Replace `PROJECT_NUMBER` with the numeral ID of your Google Cloud project. You can find your Google Cloud project ID in the Google Cloud console dashboard. For more information, see [Find the project name, number, and ID](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects).

  10. In the **Select a role** list, add the following roles:

     * **Service Account User**
     * **Service Account Token Creator**
  11. Click **Save**.




For more information on granting roles, see [Grant Dataform the required access](https://docs.cloud.google.com/dataform/docs/access-control#grant-dataform-required-access).

## Create a Dataform repository

A Dataform repository is a resource that represents a Git repository containing Dataform project code used to develop, version control, and orchestrate workflows. To create a repository, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the BigQuery **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Click add **Create repository**.

  3. On the **Create repository** page, do the following:

     1. In the **Repository ID** field, enter `quickstart-repository`.

     2. In the **Region** list, select **`europe-west4`**.

     3. In the **Service account** list, select a custom service account for the repository.

     4. In the **actAs permission checks** section, enforce permission checks on user actions for the repository.

     5. Click **Create**.

     6. Click **Go to repositories**.




You have successfully created a Dataform repository. Next, you can create and initialize a development workspace.

###  API 

To create a repository, use the [`projects.locations.repositories.create` method](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/create).

Run the API request with the following information:

  * **Endpoint** : `POST https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories`
  * **Query parameter** : `repositoryId=REPOSITORY_ID`



Alternatively, in your terminal, run the following `curl` command:
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{"serviceAccount": "SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com"}' \
      "https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories?repositoryId=REPOSITORY_ID"
    

Replace the following:

  * `PROJECT_ID`: the unique identifier of the Google Cloud project where you want to create the Dataform repository.
  * `LOCATION`: the Google Cloud region where you want to create the repository—for example, `europe-west4`.
  * `REPOSITORY_ID`: the unique identifier for your new Dataform repository—for example, `quickstart-repository`.
  * `SERVICE_ACCOUNT_NAME`: the ID of the custom service account created to run BigQuery jobs.



## Create and initialize a development workspace

A Dataform workspace is an isolated development environment—like a Git branch—where you can edit and compile code. To create a workspace, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the BigQuery **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Click **`quickstart-repository`**.

  3. Click add **Create development workspace**.

  4. In the **Create development workspace** window, do the following:

     1. In the **Workspace ID** field, enter `quickstart-workspace`.

     2. Click **Create**.

The development workspace page appears.

  5. Click **Initialize workspace**.


**Note:** Dataform initializes your workspace with a set of directories and configuration files that contain default settings for deploying workflows. You can override the default settings in the [workflow settings file](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings) to best suit your needs, but it is not a requirement to deploy workflows to BigQuery. This quickstart uses the default Dataform settings.

###  API 

  1. To create a Dataform workspace, use the [`projects.locations.repositories.workspaces.create` method](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/create).

Run the API request with the following information:

     * **Endpoint** : `POST https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/workspaces`
     * **Query parameter** : `workspaceId=WORKSPACE_ID`

Alternatively, in your terminal, run the following `curl` command:
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d "{}" \
      "https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/workspaces?workspaceId=WORKSPACE_ID"
    

Replace `WORKSPACE_ID` with the unique identifier for your Dataform development workspace—for example, `feature-branch-1`.

  2. To initialize your workspace with the necessary configuration, create a local file named `workflow_settings.yaml` and paste the following configuration:
         
         defaultProject: PROJECT_ID
         defaultDataset: dataform
         dataformCoreVersion: CORE_VERSION
         

Replace `CORE_VERSION` with the latest stable (non-beta) version of Dataform core—for example, `3.0.43`. You can find the latest version listed in [Releases](https://github.com/dataform-co/dataform/releases).

  3. In your terminal, run the following command to encode the file content into a single continuous string:
         
         base64 -w 0 workflow_settings.yaml
         

  4. Copy the resulting output string to use in the `SETTINGS_DEFINITION` placeholder should you decide to use the alternative `curl` command later in these steps.

  5. To create the configuration file in your workspace, use the [`projects.locations.repositories.workspaces.writeFile` method](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/writeFile).

Run the API request with the following information:

     * **Endpoint** : `POST https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/workspaces/WORKSPACE_ID:writeFile`

Alternatively, in your terminal, run the following `curl` command:
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "path": "workflow_settings.yaml",
        "contents": "SETTINGS_DEFINITION"
      }' \
      "https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/workspaces/WORKSPACE_ID:writeFile"
    

Replace `SETTINGS_DEFINITION` with the YAML file's content as a Base64-encoded string.




## Create a view

A Dataform view is an asset defined in a SQLX file that lets you transform data and serves as a source for other tables or views in your workflow. To create and define a view that you will later use as a data source for a table, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the BigQuery **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Click **`quickstart-repository`** , and then click **`quickstart-workspace`**.

  3. In the **Files** pane, next to **`definitions/`** , click the more_vert **More** menu.

  4. Click **Create file**.

  5. In the **Create new file** pane, do the following:

     1. In the **Add a file path** field, enter `definitions/quickstart-source.sqlx`.

     2. Click **Create file**.

  6. In the **Files** pane, expand the definitions folder.

  7. Click **`definitions/quickstart-source.sqlx`**.

  8. In the file, enter the following code snippet:
         
         config {
           type: "view"
         }
         
         SELECT
           "apples" AS fruit,
           2 AS count
         UNION ALL
         SELECT
           "oranges" AS fruit,
           5 AS count
         UNION ALL
         SELECT
           "pears" AS fruit,
           1 AS count
         UNION ALL
         SELECT
           "bananas" AS fruit,
           0 AS count
         

  9. Click **Format**.




###  API 

To create a view, you must first prepare your SQLX file content for the API request.

  1. Create a local file named `quickstart-source.sqlx` and paste the following SQL code snippet:
         
         config {
           type: "view"
         }
         
         SELECT
           "apples" AS fruit,
           2 AS count
         UNION ALL
         SELECT
           "oranges" AS fruit,
           5 AS count
         UNION ALL
         SELECT
           "pears" AS fruit,
           1 AS count
         UNION ALL
         SELECT
           "bananas" AS fruit,
           0 AS count
         

  2. In your terminal, run the following command to encode the file content into a single continuous string:
         
         base64 -w 0 quickstart-source.sqlx
         

  3. Copy the resulting output string to use in the `VIEW_DEFINITION` field in your JSON request body.

  4. To create and define the view definition file in your workspace, use the [`projects.locations.repositories.workspaces.writeFile` method](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/writeFile).

Run the API request with the following information:

     * **Endpoint** : `POST https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/workspaces/WORKSPACE_ID:writeFile`
     * **Request body** :
           
           {
             "path": "definitions/quickstart-source.sqlx",
             "contents": "VIEW_DEFINITION"
           }
           

Alternatively, in your terminal, save the request body content to a local file named `write_view.json`, and then run the following `curl` command:
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d @write_view.json \
      "https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/workspaces/WORKSPACE_ID:writeFile"
    

Replace `VIEW_DEFINITION` with the SQLX file's content as a Base64-encoded string.




## Create a table

A Dataform table is an asset defined in a SQLX file that stores transformed query results in BigQuery as part of your workflow. To define a table for your workflow, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the BigQuery **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Click **`quickstart-repository`** , and then click **`quickstart-workspace`**.

  3. In the **Files** pane, next to **`definitions/`** , click the more_vert **More** menu, and then select **Create file**.

  4. In the **Add a file path** field, enter `definitions/quickstart-table.sqlx`.

  5. Click **Create file**.

  6. In the **Files** pane, expand the **`definitions/`** directory.

  7. Select **`quickstart-table.sqlx`** , and then enter the following table type and `SELECT` statement:
         
         config {
           type: "table"
         }
         
         SELECT
           fruit,
           SUM(count) as count
         FROM ${ref("quickstart-source")}
         GROUP BY 1
         

  8. Click **Format**.

**Note:** In the preceding code snippet, the `ref` function refers to the data source. For more information, see [Create tables](https://docs.cloud.google.com/dataform/docs/create-tables#create-table).



After you define the table type, Dataform throws a query validation error because `quickstart-source` doesn't exist in BigQuery yet. This error is resolved when you run the workflow.

###  API 

To create a table, you must first prepare your SQLX file content for the API request.

  1. Create a local file named `quickstart-table.sqlx` and paste the following SQL code snippet:
         
         config {
           type: "table"
         }
         
         SELECT
           fruit,
           SUM(count) as count
         FROM ${ref("quickstart-source")}
         GROUP BY 1
         

  2. In your terminal, run the following command to encode the file content into a single continuous string:
         
         base64 -w 0 quickstart-table.sqlx
         

  3. Copy the resulting output string to use in the `TABLE_DEFINITION` field in your JSON request body.

  4. To define a table in your workspace, use the [`projects.locations.repositories.workspaces.writeFile` method](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/writeFile). This single API request replaces the manual steps of creating a SQLX file and defining the table structure and dependencies.

Run the API request with the following information:

     * **Endpoint** : `POST https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/workspaces/WORKSPACE_ID:writeFile`
     * **Request body** :
           
           {
             "path": "definitions/quickstart-table.sqlx",
             "contents": "TABLE_DEFINITION"
           }
           

Alternatively, in your terminal, save the request body content to a local file named `write_table.json`, and then run the following `curl` command:
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d @write_table.json \
      "https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/workspaces/WORKSPACE_ID:writeFile"
    

Replace `TABLE_DEFINITION` with the SQLX file's content as a Base64-encoded string.




## Run the workflow in BigQuery

To run the workflow, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the BigQuery **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Click **`quickstart-repository`** , and then click **`quickstart-workspace`**.

  3. Click **Start execution**.

  4. Click **All actions**.

  5. Click **Start execution**.

  6. In the dialog that opens, click **Allow** to give permission to **BigQuery Pipelines** to access your Google Account.

Dataform uses the default repository settings to create the contents of your workflow in a BigQuery dataset called `dataform`.




You have successfully created a Dataform workflow and run the workflow in BigQuery.

###  API 

To run your workflow in BigQuery, compile your SQLX files into standard SQL and then trigger an invocation.

  1. To create a compilation result based on your workspace, use the [`projects.locations.repositories.compilationResults.create` method](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults/create).

Run the API request with the following information:

     * **Endpoint** : `POST https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/compilationResults`

Alternatively, in your terminal, run the following `curl` command:
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "workspace": "projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/workspaces/WORKSPACE_ID"
      }' \
      "https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/compilationResults"
    

  2. From the response, note the compilation result ID in the `/compilationResults/COMPILATION_ID` format.

  3. To trigger a workflow invocation, use the [`projects.locations.repositories.workflowInvocations.create` method](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/create). Provide the ID of the compilation result you created.

Run the API request with the following information:

     * **Endpoint** : `POST https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/workflowInvocations`

Alternatively, in your terminal, run the following `curl` command:
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "compilationResult": "projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/compilationResults/COMPILATION_ID"
      }' \
      "https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/workflowInvocations"
    

Replace `COMPILATION_ID` with the unique identifier for your compilation result.




You have successfully created a Dataform workflow and run the workflow in BigQuery.

## View execution logs in Dataform

To view execution logs, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the BigQuery **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Click **`quickstart-repository`** , and then click **`quickstart-workspace`**.

  3. Click **Workflow Execution Logs**.

  4. To view execution details, click the latest execution.




###  API 

  1. To see a history of your executions, use the [`projects.locations.repositories.workflowInvocations.list` method](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/list).

Run the API request with the following information:

     * **Endpoint** : `GET https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/workflowInvocations`
     * **Query parameter** : to ensure that the most recent executions appear at the top of the results, use `?orderBy=create_time desc`.

Alternatively, in your terminal, run the following `curl` command:
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/workflowInvocations?orderBy=create_time%20desc"
    

  2. To view the detailed logs and status of a specific execution, use the [`projects.locations.repositories.workflowInvocations.query` method](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/query).

Run the API request with the following information:

     * **Endpoint** : `GET https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/workflowInvocations/WORKFLOW_INVOCATION_ID:query`

Alternatively, in your terminal, run the following `curl` command:
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/workflowInvocations/WORKFLOW_INVOCATION_ID:query"
    

Replace `WORKFLOW_INVOCATION_ID` with the unique identifier for a specific workflow execution. You can get this identifier from the results of a `workflowInvocations.list` request or from the `name` field of a `workflowInvocations.create` response.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Delete the dataset created in BigQuery

To avoid incurring charges for BigQuery assets, delete the dataset called `dataform`.

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the **Explorer** panel, expand your project and select `dataform`.

  3. Click the more_vert **Actions** menu, and then select **Delete**.

  4. In the **Delete dataset** dialog, enter `delete` into the field, and then click **Delete**.




### Delete the Dataform development workspace

Dataform development workspace creation incurs no costs, but to delete the development workspace, follow these steps:

  1. In the Google Cloud console, go to the BigQuery **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Click **`quickstart-repository`**.

  3. In the **Development workspaces** tab, click the more_vert **More** menu by `quickstart-workspace`, and then select **Delete**.

  4. To confirm, click **Delete**.




### Delete the Dataform repository

Dataform repository creation incurs no costs, but to delete the repository, follow these steps:

  1. In the Google Cloud console, go to the BigQuery **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. By **`quickstart-repository`** , click the more_vert **More** menu, and then select **Delete**.

  3. In the **Delete repository** window, enter the name of the repository to confirm deletion.

  4. To confirm, click **Delete**.




## What's next

  * To learn more about Dataform, see [Dataform overview](https://docs.cloud.google.com/dataform/docs/overview).
  * To learn how to connect a remote repository to a Dataform repository, see [Connect to a third-party Git repository](https://docs.cloud.google.com/dataform/docs/connect-repository).
  * To learn how to override default Dataform settings of your repository, see [Configure Dataform workflow settings](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings).
  * To learn more about managing datasets in BigQuery, see [Managing datasets](https://docs.cloud.google.com/bigquery/docs/managing-datasets).
  * To learn more about managing tables in BigQuery, see [Manage tables](https://docs.cloud.google.com/bigquery/docs/managing-tables).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
