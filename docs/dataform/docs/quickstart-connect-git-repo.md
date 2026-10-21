---
url: https://docs.cloud.google.com/dataform/docs/quickstart-connect-git-repo/
title: Quickstart: Connect a Git repository and run a workflow \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:50:38.498908+00:00
---

# Quickstart: Connect a Git repository and run a workflow  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/quickstart-connect-git-repo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connect a Git repository and run a workflow

This quickstart walks you through the process of creating a Dataform repository, connecting it to an existing third-party Git repository, and running a workflow. You perform the following tasks using the Google Cloud console and the Dataform API:

  * Create a Dataform repository.
  * Connect the repository to the `dataform-co/dataform-example-project-bigquery` GitHub repository.
  * Create and initialize a development workspace.
  * Add a new view to the project.
  * Compile the project and execute the workflow in BigQuery.



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the BigQuery, Dataform, and Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=bigquery.googleapis.com,dataform.googleapis.com,secretmanager.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the BigQuery, Dataform, and Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=bigquery.googleapis.com,dataform.googleapis.com,secretmanager.googleapis.com)




### Required roles

To get the permissions that you need to perform all the tasks in this quickstart, ask your administrator to grant you the following IAM roles: 

  * [Dataform Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.admin) (`roles/dataform.admin`) on the project or repository
  * [BigQuery Data Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`) on the project or specific datasets
  * [BigQuery Job User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`) on the project
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the custom service account



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a Dataform repository

A repository is the main container for your Dataform project. Select one of the following options:

###  Console 

  1. Go to the BigQuery **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Click add **Create repository**.

  3. On the **Create repository** page, do the following:

     1. In the **Repository ID** field, enter `quickstart-repo`.
     2. In the **Region** list, select a region—for example, **`europe-west4`**.
     3. In the **Service account** list, select a custom service account for the repository.
     4. Click **Create**.
     5. Click **Go to repositories**.



You have successfully created a Dataform repository. Next, you can connect the Dataform repository to a remote Git repository.

###  API 

To create a repository, use the [`projects.locations.repositories.create` method](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/create). Run the API request with the following information:

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
  * `REPOSITORY_ID`: the unique identifier for your new Dataform repository—for example, `quickstart-repo`.
  * `SERVICE_ACCOUNT_NAME`: the ID of the custom service account created to run BigQuery jobs.



You have successfully created a Dataform repository. Next, you can connect the Dataform repository to a remote Git repository.

## Connect to the Git repository

To connect your Dataform repository to your project, select one of the following options:

###  Console 

  1. Go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Click add **Create secret**.

  3. In the **Name** field, enter `dataform-git-token`.

  4. In the **Secret value** field, enter your GitHub personal access token (PAT).

For instructions on how to create a PAT, see [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

We recommend setting an expiration date for your token according to your organization's security policies.

  5. Click **Create secret**.

  6. On the secret details page, click the **Permissions** tab, and then click **Grant access**.

  7. In the **New principals** field, enter your Dataform service agent: `service-PROJECT_NUMBER@gcp-sa-dataform.iam.gserviceaccount.com`.

Replace `PROJECT_NUMBER` with your Google Cloud project number. For details on finding your project number, see [Find the project name, number, and ID](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects).

  8. In the **Select a role** field, select **Secret Manager > Secret Manager Secret Accessor**.

  9. Click **Save**.

  10. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  11. Click **`quickstart-repo`**.

  12. On the repository page, click **Settings > Connect with Git**.

  13. In the **Link to remote repository** pane, select **HTTPS**.

  14. In the **Remote Git repository URL** field, enter `https://github.com/dataform-co/dataform-example-project-bigquery.git`.

  15. In the **Default remote branch name** field, enter `master`.

  16. In the **Secret** menu, select **`dataform-git-token`**.

  17. Click **Link**.




You have successfully connected your Dataform repository to a remote Git repository and granted the necessary permissions. Next, you can create and initialize a development workspace.

###  API 

  1. To store your Git personal access token, create a secret in Secret Manager with the [`projects.secrets.create` method](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets/create). Run the API request with the following information:

     * **Endpoint** : `POST https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets`
     * **Query parameter** : `secretId=dataform-git-token`
     * **Body** :
           
           {
             "replication": {
               "automatic": {}
             }
           }
           

Alternatively, in your terminal, run the following `curl` command:
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "replication": {
          "automatic": {}
        }
      }' \
      "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets?secretId=dataform-git-token"
    

  2. Add a version to the secret containing your GitHub personal access token (PAT). For instructions on how to create a PAT, see [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token). We recommend setting an expiration date for your token according to your organization's security policies.

To add a secret version, use the [`projects.secrets.addVersion` method](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets/addVersion). Run the API request with the following information:

     * **Endpoint** : `POST https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/dataform-git-token:addVersion`
     * **Body** :
           
           {
             "payload": {
               "data": "GITHUB_PAT"
             }
           }
           

Alternatively, in your terminal, run the following `curl` command:
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "payload": {
          "data": "$(echo -n "GITHUB_PAT" | base64)"
        }
      }' \
      "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/dataform-git-token:addVersion"
    

Replace `GITHUB_PAT` with your GitHub personal access token. The `curl` command automatically converts your PAT to a Base64-encoded string before sending the request.

  3. To let Dataform access the secret, grant the [Secret Manager Secret Accessor role](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`) to the Dataform service agent. To grant the role, select one of the following options:

###  gcloud 

Run the [`gcloud secrets add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/secrets/add-iam-policy-binding):
         
         gcloud secrets add-iam-policy-binding dataform-git-token \
             --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-dataform.iam.gserviceaccount.com" \
             --role="roles/secretmanager.secretAccessor"
         

Replace `PROJECT_NUMBER` with your Google Cloud project number. For details on finding your project number, see [Find the project name, number, and ID](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects).

###  Secret Manager API 

Use the [`projects.secrets.setIamPolicy` method](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets/setIamPolicy). Run the API request with the following information:

     * **Endpoint** : `POST https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/dataform-git-token:setIamPolicy`
     * **Body** :
           
           {
             "policy": {
               "bindings": [
                 {
                   "role": "roles/secretmanager.secretAccessor",
                   "members": [
                     "serviceAccount:service-PROJECT_NUMBER@gcp-sa-dataform.iam.gserviceaccount.com"
                   ]
                 }
               ]
             }
           }
           

Alternatively, in your terminal, run the following `curl` command:
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d '{
      "policy": {
        "bindings": [
          {
            "role": "roles/secretmanager.secretAccessor",
            "members": [
              "serviceAccount:service-PROJECT_NUMBER@gcp-sa-dataform.iam.gserviceaccount.com"
            ]
          }
        ]
      }
    }' \
    "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/dataform-git-token:setIamPolicy"
    

Replace `PROJECT_NUMBER` with your Google Cloud project number. For details on finding your project number, see [Find the project name, number, and ID](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects).

  4. To connect your repository to a remote Git repository, use the [`projects.locations.repositories.patch` method](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/patch). Run the API request with the following information:

     * **Endpoint** : `PATCH https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID`
     * **Query parameter** : `updateMask=gitRemoteSettings`

Alternatively, in your terminal, run the following `curl` command:
    
    curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "gitRemoteSettings": {
          "url": "https://github.com/dataform-co/dataform-example-project-bigquery.git",
          "defaultBranch": "master",
          "authenticationTokenSecretVersion": "projects/PROJECT_ID/secrets/dataform-git-token/versions/1"
        }
      }' \
      "https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID?updateMask=gitRemoteSettings"
    




You have successfully connected your Dataform repository to a remote Git repository and granted the necessary permissions. Next, you can create and initialize a development workspace.

## Create and initialize a development workspace

A workspace is an isolated development environment. To create and initialize a workspace, select one of the following options:

###  Console 

  1. Go to the BigQuery **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Click **`quickstart-repo`**.

  3. In your repository, go to the **Development Workspaces** tab.

  4. Click add **Create development workspace**.

  5. In the **Workspace ID** field, enter `dev-workspace`.

  6. Click **Create**.

  7. On the **Development Workspaces** tab, select the **`dev-workspace`** workspace.




You have successfully created and initialized a development workspace. Next, you can configure the workflow settings.

###  API 

To create a workspace, use the [`projects.locations.repositories.workspaces.create` method](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/create). Run the API request with the following information:

  * **Endpoint** : `POST https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/workspaces`
  * **Query parameter** : `workspaceId=WORKSPACE_ID`



Alternatively, in your terminal, run the following `curl` command:
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d "{}" \
      "https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/workspaces?workspaceId=WORKSPACE_ID"
    

Replace `WORKSPACE_ID` with the unique identifier for your new Dataform development workspace—for example, `dev-workspace`.

You have successfully created and initialized a development workspace. Next, you can configure the workflow settings.

## Configure workflow settings

In this section, you update the project ID in the `workflow_settings.yaml` file to ensure that Dataform executes the workflow in your Google Cloud project. To configure the workflow settings, select one of the following options:

###  Console 

  1. Go to the BigQuery **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Click **`quickstart-repo`**.

  3. In your repository, go to the **Development Workspaces** tab, and then click **`dev-workspace`**.

  4. In the **Files** pane, select **`workflow_settings.yaml`**.

  5. In the file, replace the value of `defaultProject` with your project ID.

The file is automatically saved.




You have successfully updated your workflow settings. Next, you can add a new source declaration to your project.

###  API 

  1. Create a local file named `workflow_settings.yaml` and paste the following configuration into the file:
         
         defaultProject: PROJECT_ID
         defaultDataset: dataform
         dataformCoreVersion: CORE_VERSION
         

Replace `CORE_VERSION` with the latest stable (non-beta) version of Dataform core—for example, `3.0.43`. You can find the latest version listed in [Releases](https://github.com/dataform-co/dataform/releases).

  2. In your terminal, encode the file content into a Base64 string:
         
         base64 -w 0 workflow_settings.yaml
         

  3. Copy the resulting output string to use in the `SETTINGS_DEFINITION` placeholder should you decide to use the alternative `curl` command later in these steps.

  4. To update your workflow settings, use the [`projects.locations.repositories.workspaces.writeFile` method](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/writeFile). Run the API request with the following information:

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




You have successfully updated your workflow settings. Next, you can add a new source declaration to your project.

## Create a source

In this section, you add a new SQLX source declaration to your project that defines an existing BigQuery dataset so that Dataform can reference it as a data source in your workflow. To create the new source, select one of the following options:

###  Console 

  1. Go to the BigQuery **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Click **`quickstart-repo`**.

  3. In your repository, go to the **Development Workspaces** tab, and then click **`dev-workspace`**.

  4. In the **Files** pane, select the **`definitions`** folder.

  5. Click more_vert **More file actions > Create file**.

  6. In the **Add a file path** field, enter `definitions/sources/tags.sqlx`.

  7. Click **Create file**.

  8. In the SQL editor for the new **`definitions/sources/tags.sqlx`** file, paste the following code:
         
         config {
           type: "declaration",
           database: "bigquery-public-data",
           schema: "stackoverflow",
           name: "tags"
         }
         




You have successfully created a source declaration. Next, you can add a new view to your project.

###  API 

  1. Create a local file named `tags.sqlx`.
  2. Paste the following code into the `tags.sqlx` file:
         
         config {
           type: "declaration",
           database: "bigquery-public-data",
           schema: "stackoverflow",
           name: "tags"
         }
         

  3. In your terminal, encode the file content into a single continuous string:
         
         base64 -w 0 tags.sqlx
         

  4. Copy the resulting output string to use in the `SOURCE_DEFINITION` placeholder should you decide to use the alternative `curl` command later in these steps.

  5. To create a source declaration file in your workspace, use the [`projects.locations.repositories.workspaces.writeFile` method](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/writeFile). Run the API request with the following information:

     * **Endpoint** : `POST https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/workspaces/WORKSPACE_ID:writeFile`

Alternatively, in your terminal, run the following `curl` command:
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "path": "definitions/sources/tags.sqlx",
        "contents": "SOURCE_DEFINITION"
      }' \
      "https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/workspaces/WORKSPACE_ID:writeFile"
    

Replace `SOURCE_DEFINITION` with the SQLX file's content as a Base64-encoded string.




You have successfully created a source declaration. Next, you can add a new view to your project.

## Create a view

In this section, you add a new SQLX file to your project that defines a [view](https://docs.cloud.google.com/bigquery/docs/views-intro). To create the new view, select one of the following options:

###  Console 

  1. Go to the BigQuery **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Click **`quickstart-repo`**.

  3. In your repository, go to the **Development Workspaces** tab, and then click **`dev-workspace`**.

  4. In the **Files** pane, select the **`definitions`** folder.

  5. Click more_vert **More file actions > Create file**.

  6. In the **Add a file path** field, enter `definitions/top_question_tags.sqlx`.

  7. Click **Create file**.

  8. In the SQL editor for the new **`definitions/top_question_tags.sqlx`** file, paste the following code:
         
         config {
           type: "view",
           name: "top_question_tags",
           tags: ["daily"],
           schema: "reporting",
         }
         
         select
             tag_name,
             count
         from ${ref("tags")}
         order by count desc
         limit 100
         




You have successfully created a view. Next, you can compile your project.

###  API 

  1. Create a local file named `top_question_tags.sqlx`.
  2. Paste the following code into the `top_question_tags.sqlx` file:
         
         config {
           type: "view",
           name: "top_question_tags",
           tags: ["daily"],
           schema: "reporting",
         }
         
         select
             tag_name,
             count
         from ${ref("tags")}
         order by count desc
         limit 100
         

  3. In your terminal, encode the file content into a single continuous string:
         
         base64 -w 0 top_question_tags.sqlx
         

  4. Copy the resulting output string to use in the `VIEW_DEFINITION` placeholder should you decide to use the alternative `curl` command later in these steps.

  5. To create a view definition file in your workspace, use the [`projects.locations.repositories.workspaces.writeFile` method](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/writeFile). Run the API request with the following information:

     * **Endpoint** : `POST https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/workspaces/WORKSPACE_ID:writeFile`

Alternatively, in your terminal, run the following `curl` command:
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "path": "definitions/top_question_tags.sqlx",
        "contents": "VIEW_DEFINITION"
      }' \
      "https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/workspaces/WORKSPACE_ID:writeFile"
    

Replace `VIEW_DEFINITION` with the SQLX file's content as a Base64-encoded string.




You have successfully created a view. Next, you can compile your project.

## Compile the project

Compilation converts SQLX files into a pure SQL execution graph. To compile the project, select one of the following options:

###  Console 

The Google Cloud console compiles your project automatically. You can verify the compilation in the [**Compiled graph** tab in your workspace](https://docs.cloud.google.com/dataform/docs/create-workspace#compiled-graph-tab).

You have successfully compiled your project and verified the execution graph. Next, you can execute your workflow in BigQuery.

###  API 

  1. To create a compilation result based on your workspace, use the [`projects.locations.repositories.compilationResults.create` method](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults/create). Run the API request with the following information:

     * **Endpoint** : `POST https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/compilationResults`

Alternatively, in your terminal, run the following `curl` command:
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "workspace": "projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/workspaces/WORKSPACE_ID"
      }' \
      "https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/compilationResults"
    

  2. To verify that your project compiled successfully, use the [`projects.locations.repositories.compilationResults.get` method](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults/get). Run the API request with the following information:

     * **Endpoint** : `GET https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/compilationResults/COMPILATION_ID`

Alternatively, in your terminal, run the following `curl` command:
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/compilationResults/COMPILATION_ID"
    

Replace `COMPILATION_ID` with the unique identifier for your compilation result. This ID is provided in the response of the compilation request in the previous step.

  3. In the response, check the `compilationErrors` field. If the list is empty, your project compiled successfully.




You have successfully compiled your project and verified the execution graph. Next, you can execute your workflow in BigQuery.

## Run the workflow

To trigger the execution of your workflow in BigQuery, select one of the following options:

###  Console 

  1. Go to the BigQuery **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Click **`quickstart-repo`**.

  3. In your repository, go to the **Development Workspaces** tab, and then click **`dev-workspace`**.

  4. In the toolbar, click **Start Execution > Execute actions**.

  5. Select **All actions**.

  6. Click **Start execution**.




You have successfully run your workflow.

###  API 

To trigger a workflow invocation, use the [`projects.locations.repositories.workflowInvocations.create` method](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/create). Run the API request with the following information:

  * **Endpoint** : `POST https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/workflowInvocations`



Alternatively, in your terminal, run the following `curl` command:
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "compilationResult": "projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/compilationResults/COMPILATION_ID"
      }' \
      "https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/workflowInvocations"
    

You have successfully run your workflow.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Delete the BigQuery datasets

To avoid incurring charges for BigQuery assets, delete the datasets created by this workflow, such as the datasets named `reporting` and `staging`.

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the **Explorer** panel, expand your project and select a dataset.

  3. Click the more_vert **Actions** menu, and then select **Delete**.

  4. In the **Delete dataset** dialog, enter `delete` into the field, and then click **Delete**.




### Delete the Secret Manager secret

To clean up your security resources, delete the secret used for the Git connection.

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Select the **`dataform-git-token`** secret.

  3. Click **Delete**.

  4. In the confirmation dialog, enter the secret name to confirm, and then click **Delete**.




### Delete the Dataform development workspace

Dataform development workspace creation incurs no costs, but to delete the development workspace, follow these steps:

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Click **`quickstart-repo`**.

  3. In the **Development Workspaces** tab, click the more_vert **More** menu by `dev-workspace`, and then select **Delete**.

  4. To confirm, click **Delete**.




### Delete the Dataform repository

Dataform repository creation incurs no costs, but to delete the repository, follow these steps:

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. By **`quickstart-repo`** , click the more_vert **More** menu, and then select **Delete**.

  3. In the **Delete repository** window, enter the name of the repository to confirm deletion.

  4. To confirm, click **Delete**.




## What's next

  * To learn how to declare data sources in Dataform, see [Declare a data source](https://docs.cloud.google.com/dataform/docs/declare-source).
  * To learn how to create views and tables in Dataform, see [Create tables](https://docs.cloud.google.com/dataform/docs/create-tables).
  * To learn more about version control in Dataform, see [Version control your code](https://docs.cloud.google.com/dataform/docs/manage-repository#version-control-your-code).
  * To learn how to schedule workflow runs, see [Schedule runs with workflow configurations](https://docs.cloud.google.com/dataform/docs/schedule-runs#workflow-configurations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
