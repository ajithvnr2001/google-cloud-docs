---
url: https://docs.cloud.google.com/cortex/docs/v6/deployment-step-four/
title: Step 4: Set up components \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:12:20.914156+00:00
---

# Step 4: Set up components  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/deployment-step-four/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Step 4: Set up components

This page describes the fourth step to deploy Cortex Framework Data Foundation, the core of Cortex Framework. In this step, you set up the required Google Cloud services to deploy.

**Note:** The steps outlined on this page are specifically designed for deploying Cortex Framework Data Foundation from the [official GitHub repository](https://github.com/GoogleCloudPlatform/cortex-data-foundation).

## Enable Google Cloud services

In this section you enable the following Google Cloud services in your Google Cloud project:

  * BigQuery instance and datasets
  * Cloud Build API
  * Cloud Storage Buckets
  * Service account
  * Cloud Resource Manager API
  * Workflow executions (if deploying [Cortex for Meridian](https://docs.cloud.google.com/cortex/docs/v6/meridian))
  * AI Platform (if deploying [Cortex for Meridian](https://docs.cloud.google.com/cortex/docs/v6/meridian))



Enable these Google Cloud services using [Cloud Shell](https://shell.cloud.google.com/?fromcloudshell=true&show=ide%2Cterminal):

  1. Copy and paste the following command:
         
         gcloud config set project SOURCE_PROJECT
         
         gcloud services enable bigquery.googleapis.com \
                               cloudbuild.googleapis.com \
                               composer.googleapis.com \
                               storage-component.googleapis.com \
                               cloudresourcemanager.googleapis.com \
                               dataflow.googleapis.com \
                               datacatalog.googleapis.com \
                               workflowexecutions.googleapis.com \
                               workflows.googleapis.com \
                               aiplatform.googleapis.com
         

Replace `SOURCE_PROJECT` with your source project ID.

**Note:** `workflowexecutions.googleapis.com`, `workflows.googleapis.com`, and `aiplatform.googleapis.com` are only needed with Cortex Framework for Meridian.
  2. Verify that Google Cloud services are enabled if you get a success message.




**Optional**. You can enable the following Google Cloud services in your Google Cloud Project:

  * [Managed Airflow](https://console.cloud.google.com/marketplace/product/google/composer.googleapis.com) for Change Data Capture (CDC) processing, hierarchy flattening (SAP only), and data replication (Non-SAP only) through Directed Acyclic Graphs ([DAGs](https://airflow.apache.org/docs/apache-airflow/stable/concepts/dags.html)). To set up an instance, see [Managed Airflow documentation](https://docs.cloud.google.com/composer/docs/how-to/managing/creating).
  * [Looker](https://docs.cloud.google.com/looker) for connecting to reporting templates.
  * [BigQuery sharing (formerly Analytics Hub)](https://docs.cloud.google.com/analytics-hub) linked datasets are used for some external sources, such as the Weather DAG. You might choose to fill this structure with any other available source of your choice for advanced scenarios.
  * [Dataflow](https://console.cloud.google.com/dataflow): Integration tool for many of the Marketing data sets like Google Ads.
  * For Cortex Framework with Meridian: 
    * Colab Enterprise: Running the Colab Enterprise notebook during and execution having access to the following:
    * The notebook and configuration file on Cloud Storage.
    * Query relevant BigQuery views and tables.
    * Write the results back to Cloud Storage.
    * Workflows: Running the Workflow and Cloud Build to trigger Colab Enterprise notebook executions.



## Grant permissions to the executing user

Grant the following permissions to the executing user, either using the Google Cloud console or the Google Cloud CLI, to execute the deployment in the project where Cloud Build is triggered:

  * Service Usage Consumer (`roles/serviceusage.serviceUsageConsumer`)
  * Storage Object Viewer (`roles/storage.objectViewer`)
  * Storage Admin (`roles/storage.admin`)
  * Cloud Build Editor (`roles/cloudbuild.builds.editor`)
  * Project Reader (`roles/reader`)
  * BigQuery Job User (`roles/bigquery.jobUser`)
  * BigQuery Data Editor (`roles/bigquery.dataEditor`)




###  Console 

  1. Open the IAM page in the Google Cloud console:

[Open the IAM page](https://console.cloud.google.com/iam-admin/roles)

  2. Select your project, and click **Continue**.

  3. Click **Grant access**.

  4. Enter the executing user's email address.

  5. Select the following roles from the drop-down menu:

     * Service Usage Consumer (`roles/serviceusage.serviceUsageConsumer`)
     * Storage Object Viewer (`roles/storage.objectViewer`)
     * Storage Admin (`roles/storage.admin`)
     * Cloud Build Editor (`roles/cloudbuild.builds.editor`)
     * Project Reader (`roles/reader`)
     * BigQuery Job User (`roles/bigquery.jobUser`)
     * BigQuery Data Editor (`roles/bigquery.dataEditor`)
  6. Click **Save**.


**Note:** If you don't see the Cloud Build roles in the drop-down menu, you may need to [enable the Cloud Build API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com&_ga=1.128224844.1904271179.1489680703).

###  gcloud 

To grant a role to a user, run the `add-iam-policy-binding` command:
    
    
      gcloud projects add-iam-policy-binding SOURCE_PROJECT \
        --member="user:USER_EMAIL" \
        --role="roles/serviceusage.serviceUsageConsumer"
      gcloud projects add-iam-policy-binding SOURCE_PROJECT \
        --member="user:USER_EMAIL" \
        --role="roles/storage.objectViewer"
      gcloud projects add-iam-policy-binding SOURCE_PROJECT \
        --member="user:USER_EMAIL" \
        --role="roles/storage.admin"
      gcloud projects add-iam-policy-binding SOURCE_PROJECT \
        --member="user:USER_EMAIL" \
        --role="roles/cloudbuild.builds.editor"
      gcloud projects add-iam-policy-binding SOURCE_PROJECT \
        --member="user:USER_EMAIL" \
        --role="roles/reader"
      gcloud projects add-iam-policy-binding SOURCE_PROJECT \
        --member="user:USER_EMAIL" \
        --role="roles/bigquery.jobUser"
      gcloud projects add-iam-policy-binding SOURCE_PROJECT \
        --member="user:USER_EMAIL" \
        --role="roles/bigquery.dataEditor"
    

Replace the following:

  * `SOURCE_PROJECT` with the source project ID.
  * `USER_EMAIL` with the executing user's email. For example, user:my-user@example.com. For a full list of principal, or `member`, types, see the [Policy Binding reference](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy#Binding).



## Create and configure the Cloud Build service account

Cloud Build uses a service account to execute builds on your behalf. This section guides you through creating a dedicated service account for Cortex Framework deployments and granting the necessary permissions to the Cloud Build service account.

**Note:** We have introduced changes to the default service account used to run builds. As a best practice, we recommend that you [specify your own service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts) to run your builds for Cortex Framework. For more information see [Cloud Build default service account change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates).

### Create a new service account

Create a dedicated service account for deploying Cortex Framework for enhanced security and control. After creating the new service account you can then specify this [service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts) during the deployment process using the `_BUILD_ACCOUNT` substitution parameter.

Before you begin, you need to enable the IAM API, set up authentication, and understand IAM service accounts and roles. For more information, see [Create service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-create).

Create this new service account using either the Google Cloud console or the Google Cloud CLI.

### Console

  1. Go the **Service accounts** page.

[Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts/create)

The remaining steps appear in the Google Cloud console.

  2. Select a Google Cloud project.

  3. Enter a service account and display name, with description and in the Google Cloud console. The Google Cloud console generates a service account ID based on this name. Edit the ID if necessary. You can't change the ID later. Use the following default values for the service account:

     * **Name** : "cortex-deployer".
     * **Description** : "Cortex Deployer Service Account".
     * **Display name** : "Cortex Deployer".
  4. Grant users access to this service account.

     1. Add the ID of all users (including your own) who can run the deployment through the service account.
     2. Assign the **Service Account Token Creator** role. For more information about this role, see [Service account roles](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role).
  5. Click **Done** to finish creating the service account.




If you already have a service account, follow these steps:

  1. Go to [Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts).
  2. Select the **Service account**.
  3. Click the **Principals with access** tab.
  4. Click **Grant Access**. 
     1. Add the ID of all users (including your own) who can run the deployment through the service account.
     2. Assign the **Service Account Token Creator** role.



### gcloud

  1. Create a service account through an IAM policy with the following command:
         
         gcloud iam service-accounts create cortex-deployer \
         --description="Cortex Deployer Service Account" \
         --display-name="Cortex Deployer"
         

  2. Add the IAM policy to your Google Cloud project with the following command:
         
         gcloud projects add-iam-policy-binding SOURCE_PROJECT \
         --member="serviceAccount:cortex-deployer@SOURCE_PROJECT.iam.gserviceaccount.com" \
         --role="roles/cloudbuild.builds.editor"
         

  3. Add the ID of all users (including your own) who can run the deployment through the service account, and assign them the _Service Account Token Creator_ role with the following command:
         
         gcloud iam service-accounts add-iam-policy-binding cortex-deployer@SOURCE_PROJECT.iam.gserviceaccount.com \
         --member="user:USER_EMAIL" \
         --role="roles/iam.serviceAccountTokenCreator"
         

Replace the following:

     * `SOURCE_PROJECT` with the source project for Cortex Framework Data Foundation deployment.
     * `USER_EMAIL` with the executing user email.



For more information about creating a new service account, see [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create#creating).

### Grant permissions

The Cloud Build service account needs specific permissions in your source project (and the target project if you are deploying to a separate project). Grant the following roles using either the Google Cloud console or the Google Cloud CLI:

  * Cloud Build service account (`roles/cloudbuild.builds.builder`)
  * Service account User (`roles/iam.serviceAccountUser`)
  * BigQuery Data Editor (`roles/bigquery.dataEditor`)
  * BigQuery Job User (`roles/bigquery.jobUser`)
  * Logs Writer (`roles/logging.logWriter`)
  * Colab Enterprise Admin (`roles/aiplatform.colabEnterpriseAdmin` \- if deploying [Cortex for Meridian](https://docs.cloud.google.com/cortex/docs/v6/meridian))
  * Storage Object User (`roles/storage.objectUser` \- if deploying [Cortex for Meridian](https://docs.cloud.google.com/cortex/docs/v6/meridian))
  * Workflows Editor (`roles/workflows.editor` \- if deploying [Cortex for Meridian](https://docs.cloud.google.com/cortex/docs/v6/meridian))




### Console

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam?supportedpurview=project)

  2. Select your source project.

  3. Click person_add **Grant access**.

  4. Add the default Cloud Build service account from the preceding step as a new principal.

  5. From the **Select a role** drop-down menu, search for _Cloud Build service account_ , then click _Cloud Build service account_.

  6. Repeat the previous step to add the rest of the roles:

     * _Service Account User_
     * _BigQuery Data Editor_
     * _BigQuery Job User_
     * _Logs Writer_
     * _Colab Enterprise Admin_ (if deploying [Cortex for Meridian](https://docs.cloud.google.com/cortex/docs/v6/meridian))
     * _Storage Object User_ (if deploying [Cortex for Meridian](https://docs.cloud.google.com/cortex/docs/v6/meridian))
     * _Workflows Editor_ (if deploying [Cortex for Meridian](https://docs.cloud.google.com/cortex/docs/v6/meridian))
  7. Click **Save**.

  8. Verify that the service account and the corresponding roles are listed in the IAM page. You have successfully granted an IAM role.




### gcloud

Use the following command to grant the roles to the Cloud Build service account:
    
    
      gcloud projects add-iam-policy-binding SOURCE_PROJECT \
          --member="serviceAccount:cortex-deployer@SOURCE_PROJECT.iam.gserviceaccount.com" \
          --role="roles/cloudbuild.builds.builder"
      gcloud projects add-iam-policy-binding SOURCE_PROJECT \
          --member="serviceAccount:cortex-deployer@SOURCE_PROJECT.iam.gserviceaccount.com" \
          --role="roles/iam.serviceAccountUser"
      gcloud projects add-iam-policy-binding SOURCE_PROJECT \
          --member="serviceAccount:cortex-deployer@SOURCE_PROJECT.iam.gserviceaccount.com" \
          --role="roles/bigquery.dataEditor"
      gcloud projects add-iam-policy-binding SOURCE_PROJECT \
          --member="serviceAccount:cortex-deployer@SOURCE_PROJECT.iam.gserviceaccount.com" \
          --role="roles/bigquery.jobUser"
      gcloud projects add-iam-policy-binding SOURCE_PROJECT \
          --member="serviceAccount:cortex-deployer@SOURCE_PROJECT.iam.gserviceaccount.com" \
          --role="roles/logging.logWriter"
      gcloud projects add-iam-policy-binding SOURCE_PROJECT \
          --member="serviceAccount:cortex-deployer@SOURCE_PROJECT.iam.gserviceaccount.com" \
          --role="roles/aiplatform.colabEnterpriseAdmin"
      gcloud projects add-iam-policy-binding SOURCE_PROJECT \
          --member="serviceAccount:cortex-deployer@SOURCE_PROJECT.iam.gserviceaccount.com" \
          --role="roles/storage.objectUser"
      gcloud projects add-iam-policy-binding SOURCE_PROJECT \
          --member="serviceAccount:cortex-deployer@SOURCE_PROJECT.iam.gserviceaccount.com" \
          --role="roles/workflows.editor"
    

Replace the following:

  * `SOURCE_PROJECT` with the source project ID.
  * `CLOUD_BUILD_SA` with the Cloud Build service account, in the format `CLOUD_BUILD_SA@SOURCE_PROJECT.gserviceaccount.com`.



For more information, see [Granting a role to the Cloud Build service account using the IAM page](https://docs.cloud.google.com/build/docs/securing-builds/configure-access-for-cloud-build-service-account) and [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

## Create an additional service account for Cortex for Meridian

A separate service account is necessary for Meridian when deploying Cortex Framework. _If you are not deploying for Meridian, you can skip this step_. A separate service account is required for the following:

  * Running the Workflow and Cloud Build to trigger Colab Enterprise notebook executions.
  * Running the Colab Enterprise notebook with access to: 
    * Notebook and configuration file on Cloud Storage.
    * Query relevant BigQuery views and tables.
    * Write the results back to Cloud Storage.



Use the following command to create a service account for Cortex for Meridian:
    
    
     gcloud iam service-accounts create cortex-meridian-colab-runner --project=SOURCE_PROJECT \
            --description="Cortex for Meridian Colab Runner Service Account" \
            --display-name="Cortex Meridian Runner"
    
    

Replace the following:

  * `SOURCE_PROJECT` with the project ID where Cortex for Meridian is deployed.
  * `cortex-meridian-colab-runner`: Optionally, you can use a different service account ID. Consider that `cortex-meridian-colab-runner` is the default, and changing it might require adjustments to other commands.



The minimum required roles for a dedicated service account for Cortex for Meridian are the following:

  * BigQuery Data Viewer (`roles/bigquery.dataViewer`)
  * BigQuery Job User (`roles/bigquery.jobUser`)
  * BigQuery Read Session User (`roles/bigquery.readSessionUser`)
  * Cloud Build Editor (`roles/cloudbuild.builds.editor`)
  * Colab Enterprise Admin (`roles/aiplatform.colabEnterpriseAdmin`)
  * Logs Writer (`roles/logging.logWriter`)
  * Notebook Runtime Admin (`aiplatform.notebookRuntimeAdmin`)
  * Storage Admin (`roles/storage.admin`)
  * Storage Object User (`roles/storage.objectUser`)
  * Vertex AI Colab Service Agent (`roles/aiplatform.colabServiceAgent`)



Use the following command to grant the roles to the dedicated service account for Cortex for Meridian:
    
    
    gcloud projects add-iam-policy-binding SOURCE_PROJECT \
        --member="serviceAccount:cortex-meridian-colab-runner@SOURCE_PROJECT.iam.gserviceaccount.com" \
        --role='roles/bigquery.dataViewer'
    
    gcloud projects add-iam-policy-binding SOURCE_PROJECT \
        --member="serviceAccount:cortex-meridian-colab-runner@SOURCE_PROJECT.iam.gserviceaccount.com" \
        --role='roles/bigquery.jobUser'
    
    gcloud projects add-iam-policy-binding SOURCE_PROJECT \
        --member="serviceAccount:cortex-meridian-colab-runner@SOURCE_PROJECT.iam.gserviceaccount.com" \
        --role='roles/bigquery.readSessionUser'
    
    gcloud projects add-iam-policy-binding SOURCE_PROJECT \
        --member="serviceAccount:cortex-meridian-colab-runner@SOURCE_PROJECT.iam.gserviceaccount.com" \
        --role='roles/cloudbuild.builds.editor'
    
    gcloud projects add-iam-policy-binding SOURCE_PROJECT \
        --member="serviceAccount:cortex-meridian-colab-runner@SOURCE_PROJECT.iam.gserviceaccount.com" \
        --role='roles/aiplatform.colabEnterpriseAdmin'
    
    gcloud projects add-iam-policy-binding SOURCE_PROJECT \
        --member="serviceAccount:cortex-meridian-colab-runner@SOURCE_PROJECT.iam.gserviceaccount.com" \
        --role='roles/logging.logWriter'
    
    gcloud projects add-iam-policy-binding SOURCE_PROJECT \
        --member="serviceAccount:cortex-meridian-colab-runner@SOURCE_PROJECT.iam.gserviceaccount.com" \
        --role='roles/aiplatform.notebookRuntimeAdmin'
    
    gcloud projects add-iam-policy-binding SOURCE_PROJECT \
        --member="serviceAccount:cortex-meridian-colab-runner@SOURCE_PROJECT.iam.gserviceaccount.com" \
        --role='roles/storage.admin'
    
    gcloud projects add-iam-policy-binding SOURCE_PROJECT \
        --member="serviceAccount:cortex-meridian-colab-runner@SOURCE_PROJECT.iam.gserviceaccount.com" \
        --role='roles/storage.objectUser'
    
    gcloud projects add-iam-policy-binding SOURCE_PROJECT \
        --member="serviceAccount:cortex-meridian-colab-runner@SOURCE_PROJECT.iam.gserviceaccount.com" \
        --role='roles/aiplatform.colabServiceAgent'
    

Replace the following:

  * `SOURCE_PROJECT` with the project ID where Cortex for Meridian is deployed.
  * `cortex-meridian-colab-runner` with your service account for Cortex for Meridian.



## Create a Storage bucket for storing DAG related files

A storage bucket is required to store processing DAG scripts and other temporary files generated during deployment. These scripts need to be manually moved into a Managed Airflow or Apache Airflow instance after deployment.

You can create the storage bucket from Google Cloud CLI or Google Cloud console with the following steps.

### Console

  1. Go to Cloud Storage.

[Cloud Storage](https://console.cloud.google.com/storage/create-bucket)

  2. Create a bucket in the same region as your BigQuery datasets.

  3. Select the created bucket.

  4. Go to the `Permissions` tab.

  5. Grant the permission `Storage Object Creator` to the user ID executing the Build command or to the [Service account you created](https://docs.cloud.google.com/cortex/docs/v6/optional-step-cloud-build-features#deployment_with_user_created_service_account). For more information, see [Set a new condition on a bucket: Console](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#console_3).




### gcloud

  1. Create a bucket from the Cloud Shell with the following command:
         
         gcloud storage buckets create gs://COMPOSER_DAG_BUCKET -l REGION/MULTI_REGION
         

Replace the following:

     * `COMPOSER_DAG_BUCKET` with the name for the new bucket.
     * `REGION/MULTI_REGION` with the same region as your BigQuery datasets.
  2. Use the following command to assign the permission `Storage Object Creator` to the service account:
         
         gcloud storage buckets add-iam-policy-binding gs://COMPOSER_DAG_BUCKET \
             --member="serviceAccount:cortex-deployer@SOURCE_PROJECT.iam.gserviceaccount.com" \
             --role=roles/storage.objectCreator
         

Replace the following:

     * `cortex-deployer` with the Cloud Build service account.
     * `COMPOSER_DAG_BUCKET` with the name for the new bucket.



## Create a Storage bucket for logs

You can create a specific bucket for the Cloud Build process to store the logs. This is useful if you want to restrict data that may be stored in logs to a specific region. You can create the storage bucket for logs from Google Cloud CLI or Google Cloud console.

### Console

To create a specific bucket for the logs, follow these steps:

  1. Go to Cloud Storage.

[Cloud Storage](https://console.cloud.google.com/storage/create-bucket)

  2. Create a bucket in the same region where the deployment would run.

  3. Select the created bucket.

  4. Go to the `Permissions` tab.

  5. Grant the permission `Storage Object Admin` to the user ID executing the Build command or to the [Service account you created](https://docs.cloud.google.com/cortex/docs/v6/optional-step-cloud-build-features#deployment_with_user_created_service_account). For more information, see [Set a new condition on a bucket: Console](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#console_3).




### gcloud

To create a specific bucket for the logs, use the following commands.

  1. Create a bucket from the Cloud Shell with the following command:
         
         gcloud storage buckets create gs://LOGS_BUCKET_NAME -l REGION/MULTI_REGION
         

Replace the following:

     * `REGION/MULTI_REGION` with the chosen region to create the bucket.
     * `LOGS_BUCKET_NAME` with the name for the new bucket.
  2. Use the following command to assign the permission `Storage Object Admin` to the service account:
         
         gcloud storage buckets add-iam-policy-binding gs://LOGS_BUCKET_NAME \
             --member="serviceAccount:cortex-deployer@SOURCE_PROJECT.iam.gserviceaccount.com" \
             --role=roles/storage.objectAdmin
         

Replace the following:

     * `cortex-deployer` with the Cloud Build default service account.
     * `LOGS_BUCKET_NAME` with the name for the new bucket.



## Next steps

After you complete this step, move on to the following deployment steps:

  1. [Establish workloads](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-one).
  2. [Clone repository](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-two).
  3. [Determine integration mechanism](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-three).
  4. [Set up components](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-four) (this page).
  5. [Configure deployment](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five).
  6. [Execute deployment](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-six).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
