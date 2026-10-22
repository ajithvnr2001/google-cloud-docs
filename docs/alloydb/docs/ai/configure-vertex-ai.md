---
url: https://docs.cloud.google.com/alloydb/docs/ai/configure-vertex-ai/
title: Integrate with Agent Platform \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:46.496516+00:00
---

# Integrate with Agent Platform  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/ai/configure-vertex-ai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Integrate with Agent Platform Stay organized with collections  Save and categorize content based on your preferences. 

Integrating AlloyDB for PostgreSQL with Gemini Enterprise Agent Platform lets you run SQL queries that pass your database data directly to Agent Platform models for embeddings generation and online predictions.

These instructions are specific to using AlloyDB, and not AlloyDB Omni. To instead integrate a local installation of AlloyDB Omni using Agent Platform, see [Install AlloyDB Omni with AlloyDB AI](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/install-with-alloydb-ai).

For more information about using ML models with AlloyDB, see [Build generative AI applications using AlloyDB AI](https://docs.cloud.google.com/alloydb/docs/ai).

For more information about Agent Platform, see [Agent Platform overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Agent Platform API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com&redirect=https%3A//console.cloud.google.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Agent Platform API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com&redirect=https%3A//console.cloud.google.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




## About the AlloyDB service agent

When you use AlloyDB with other Google Cloud services, AlloyDB uses an Identity and Access Management (IAM) service agent to authenticate to those services. This service agent is an IAM principal that AlloyDB controls. You grant IAM roles to this service agent to let it access other Google Cloud services on your behalf.

## Grant the `Vertex AI User` role to the AlloyDB service agent

To enable database integration with Agent Platform, you grant the AlloyDB service agent the `Vertex AI User` role. This lets the AlloyDB service agent access Agent Platform on your behalf.

**Note:** To grant IAM roles, you must have the `resourcemanager.projects.setiamPolicy` permission. The `Owner` and `Project IAM Admin` roles include this permission. The `AlloyDB Admin` role also includes the permissions required to grant the `Vertex AI User` role to the service agent. If you don't have the necessary permissions, contact your organization's administrator.

Follow these steps to grant the AlloyDB service agent the `Vertex AI User` role:

Add Agent Platform permissions to the AlloyDB service agent for the project where the AlloyDB database's cluster is located:

### Console

  1. Go to the **Welcome** page in the Google Cloud console, and copy the project number of the project that has AlloyDB clusters or instances. You will use this project number in the next steps. 

[Go to Welcome](https://console.cloud.google.com/welcome)

  2. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector2/iam-admin/iam)

  3. Select the project that needs to call Agent Platform endpoints.

  4. Enable **Include Google-provided role grants**.

  5. Click person_add **Grant Access**.

  6. In the **New principals** field, enter the following:
         
         service-PROJECT_NUMBER@gcp-sa-alloydb.iam.gserviceaccount.com
             

Replace PROJECT_NUMBER with the project number.

  7. In the **Role** field, enter **Vertex AI User**.

  8. Click **Save**.




### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).
    
    
            gcloud projects add-iam-policy-binding PROJECT_ID   
    
            --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-alloydb.iam.gserviceaccount.com"   
    
            --role="roles/aiplatform.user"
      

Replace the following:

  * PROJECT_ID: The ID of the project that has the Agent Platform endpoint.
  * PROJECT_NUMBER: The project number of the project that has AlloyDB clusters or instances.

**Note:** The policy change takes effect within 60 seconds to 7 minutes.

## Verify installed extension

Verify if the `google_ml_integration` is installed in the database that contains the data that you want to run predictions on:

### Console

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. To display the cluster **Overview** page, click the name of the AlloyDB cluster in the **Resource name** column.

  3. In the navigation menu, click **AlloyDB Studio**.

  4. On the **Sign in to AlloyDB Studio** page, authenticate using the name of your database, username, and password.

**Note:** AlloyDB Studio connects to the primary instance of your cluster, which is where extension management and initial predictions are handled, even if you intend to invoke predictions from read pool instances later.
  5. In the **Editor 1** tab, complete the following:

     1. Verify the `google_ml_integration` extension version 1.4.2 or later is installed:
            
            SELECT extversion FROM pg_extension WHERE extname = 'google_ml_integration';

     2. Click **Run**. Wait for the extension version to display in the **Results** pane.




###  psql 

  1. Connect a `psql` client to the cluster's primary instance, as described in [Connect a `psql` client to an instance](https://docs.cloud.google.com/alloydb/docs/connect-psql).

**Note:** You must connect to the primary instance even if you intend to invoke predictions while connected to a read pool instance.
  2. At the `psql` command prompt, connect to the database: 
         
         \c DB_NAME

Replace `DB_NAME` with the name of the database on which you want to install the extension.

  3. Verify the `google_ml_integration` extension version 1.4.2 or later is installed: 
         
         SELECT extversion FROM pg_extension WHERE extname = 'google_ml_integration';




## What's next

  * [Work with embeddings](https://docs.cloud.google.com/alloydb/docs/ai/work-with-embeddings)

  * [Invoke predictions](https://docs.cloud.google.com/alloydb/docs/ai/invoke-predictions)

  * [Agent Platform quotas and limits](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/quotas)

  * [Call remote model endpoints](https://docs.cloud.google.com/alloydb/docs/ai/model-endpoint-overview)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
