---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/deploy-pgvector/
title: Deploy a PostgreSQL vector database on GKE \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:33.114729+00:00
---

# Deploy a PostgreSQL vector database on GKE  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/deploy-pgvector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Deploy a PostgreSQL vector database on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial shows you how to deploy a [PostgreSQL](https://www.postgresql.org/) vector database cluster on Google Kubernetes Engine (GKE).

[PostgreSQL](https://www.postgresql.org/) comes with a range of modules and extensions that extend the database's functionality. In this tutorial, you install the [pgvector](https://github.com/pgvector/pgvector/) extension on an existing PostgreSQL cluster deployed to GKE. The Pgvector extension lets you store vectors in the database tables by adding vector types to PostgreSQL. Pgvector also provides similarity searches by running common SQL queries.

We simplify the PGvector extension deployment by first deploying the [CloudnativePG](https://cloudnative-pg.io/) operator, as the operator provides a bundled version of the extension.

This tutorial is intended for cloud platform [administrators and architects](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks#admins), [ML engineers](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks#data-ai-ml-engineer), and MLOps (DevOps) professionals interested in deploying PostgreSQL database clusters on GKE.

## Objectives

In this tutorial, you learn how to:

  * Deploy GKE infrastructure for PostgreSQL.
  * Install pgvector extension on the PostgreSQL cluster deployed to GKE.
  * Deploy and configure the CloudNativePG PostgreSQL operator with Helm.
  * Upload a demo dataset and run search queries with Jupyter Notebook.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [GKE](https://cloud.google.com/kubernetes-engine/pricing)
  * [Google Cloud Managed Service for Prometheus](https://cloud.google.com/stackdriver/pricing#mgd-prometheus-pricing-summary)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell/docs) to run commands. Cloud Shell is a shell environment for managing resources hosted on Google Cloud. It comes preinstalled with the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud), [kubectl](https://kubernetes.io/docs/reference/kubectl/), [Helm](https://helm.sh/) and [ Terraform](https://docs.cloud.google.com/docs/terraform) command-line tools. If you don't use Cloud Shell, you must install the Google Cloud CLI.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Resource Manager, Compute Engine, GKE, and IAM Service Account Credentials APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudresourcemanager.googleapis.com compute.googleapis.com container.googleapis.com iamcredentials.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the Cloud Resource Manager, Compute Engine, GKE, and IAM Service Account Credentials APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudresourcemanager.googleapis.com compute.googleapis.com container.googleapis.com iamcredentials.googleapis.com

  14. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/compute.securityAdmin, roles/compute.viewer, roles/container.clusterAdmin, roles/container.admin, roles/iam.serviceAccountAdmin, roles/iam.serviceAccountUser`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.



## Set up your environment

To set up your environment with Cloud Shell, follow these steps:

  1. Set environment variables for your project, region, and a Kubernetes cluster resource prefix:
         
         export PROJECT_ID=PROJECT_ID
         export KUBERNETES_CLUSTER_PREFIX=postgres
         export REGION=us-central1
         

     * Replace `PROJECT_ID` with your Google Cloud project ID.

This tutorial uses the `us-central1` region.

  2. Clone the sample code repository from GitHub:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples
         

  3. Navigate to the `postgres-pgvector` directory:
         
         cd kubernetes-engine-samples/databases/postgres-pgvector
         




## Create your cluster infrastructure

In this section, you run a Terraform script to create a private, highly-available, regional GKE cluster to deploy your PostgreSQL database.

You can choose to deploy PostgreSQL using a [Standard or Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode). Each has its own advantages and different pricing models.

###  Autopilot 

To deploy the Autopilot cluster infrastructure, run the following commands in the Cloud Shell:
    
    
    export GOOGLE_OAUTH_ACCESS_TOKEN=$(gcloud auth print-access-token)
    terraform -chdir=../postgresql-cloudnativepg/terraform/gke-autopilot init
    terraform -chdir=../postgresql-cloudnativepg/terraform/gke-autopilot apply \
    -var project_id=${PROJECT_ID} \
    -var region=${REGION} \
    -var cluster_prefix=${KUBERNETES_CLUSTER_PREFIX}
    

GKE replaces the following variables at runtime:

  * `GOOGLE_OAUTH_ACCESS_TOKEN` uses the `gcloud auth print-access-token` command to retrieve an access token that authenticates interactions with various Google Cloud APIs
  * `PROJECT_ID`, `REGION`, and `KUBERNETES_CLUSTER_PREFIX` are the environment variables defined in the Set up your environment section and assigned to the new relevant variables for the Autopilot cluster you are creating.



When prompted, type `yes`.

Terraform creates the following resources:

  * A custom VPC network and private subnet for the Kubernetes nodes.
  * A Cloud Router to access the internet through Network Address Translation (NAT).
  * A private GKE cluster in the `us-central1` region.
  * A `ServiceAccount` with logging and monitoring permissions for the cluster.
  * Google Cloud Managed Service for Prometheus configuration for cluster monitoring and alerting.



The output is similar to the following:
    
    
    ...
    Apply complete! Resources: 11 added, 0 changed, 0 destroyed.
    ...
    

###  Standard 

To deploy the Standard cluster infrastructure, run the following commands in the Cloud Shell:
    
    
    export GOOGLE_OAUTH_ACCESS_TOKEN=$(gcloud auth print-access-token)
    terraform -chdir=../postgresql-cloudnativepg/terraform/gke-standard init
    terraform -chdir=../postgresql-cloudnativepg/terraform/gke-standard apply \
    -var project_id=${PROJECT_ID} \
    -var region=${REGION} \
    -var cluster_prefix=${KUBERNETES_CLUSTER_PREFIX}
    

GKE replaces the following variables at runtime:

  * `GOOGLE_OAUTH_ACCESS_TOKEN` uses the `gcloud auth print-access-token` command to retrieve an access token that authenticates interactions with various Google Cloud APIs.
  * `PROJECT_ID`, `REGION`, and `KUBERNETES_CLUSTER_PREFIX` are the environment variables defined in Set up your environment section and assigned to the new relevant variables for the Standard cluster that you are creating.



When prompted, type `yes`. It might take several minutes for these commands to complete and for the cluster to show a ready status.

Terraform creates the following resources:

  * A custom VPC network and private subnet for the Kubernetes nodes.
  * A Cloud Router to access the internet through Network Address Translation (NAT).
  * A private GKE cluster in the `us-central1` region with autoscaling enabled (one to two nodes per zone).
  * A `ServiceAccount` with logging and monitoring permissions for the cluster.
  * Google Cloud Managed Service for Prometheus configuration for cluster monitoring and alerting.



The output is similar to the following:
    
    
    ...
    Apply complete! Resources: 14 added, 0 changed, 0 destroyed.
    ...
    

### Connect to the cluster

Configure `kubectl` to fetch credentials and communicate with your new GKE cluster:
    
    
    gcloud container clusters get-credentials \
        ${KUBERNETES_CLUSTER_PREFIX}-cluster --location ${REGION} --project ${PROJECT_ID}
    

## Deploy the CloudNativePG operator

Deploy the CloudNativePG to your Kubernetes cluster using a Helm chart:

  1. Check the version of Helm:
         
         helm version
         

Update the version if it's older than 3.13:
         
         curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
         

  2. Add the CloudNativePG operator Helm Chart repository:
         
         helm repo add cnpg https://cloudnative-pg.github.io/charts
         

  3. Deploy the CloudNativePG operator using the Helm command-line tool:
         
         helm upgrade --install cnpg \
             --namespace cnpg-system \
             --create-namespace \
             cnpg/cloudnative-pg
         

The output is similar to the following:
         
         Release "cnpg" does not exist. Installing it now.
         NAME: cnpg
         LAST DEPLOYED: Fri Oct 13 13:52:36 2023
         NAMESPACE: cnpg-system
         STATUS: deployed
         REVISION: 1
         TEST SUITE: None
         ...
         




## Deploy the PostgreSQL vector database

In this section, you deploy the PostgreSQL vector database.

  1. Create a namespace `pg-ns` for the database:
         
         kubectl create ns pg-ns
         

  2. Apply the manifest to deploy PostgreSQL cluster. The cluster manifest enables the pgvector extension.
         
         kubectl apply -n pg-ns -f manifests/01-basic-cluster/postgreSQL_cluster.yaml
         

The `postgreSQL_cluster.yaml` manifest describes the Deployment:
         
         apiVersion: postgresql.cnpg.io/v1
         kind: Cluster
         metadata:
           name: gke-pg-cluster
         spec:
           description: "Standard GKE PostgreSQL cluster"
           imageName: ghcr.io/cloudnative-pg/postgresql:16.2
           enableSuperuserAccess: true
           instances: 3
           startDelay: 300
           primaryUpdateStrategy: unsupervised
           postgresql:
             pg_hba:
               - host all all 10.48.0.0/20 md5
           bootstrap:
             initdb:
               postInitTemplateSQL:
                 - CREATE EXTENSION IF NOT EXISTS vector;
               database: app
           storage:
             storageClass: premium-rwo
             size: 2Gi
           resources:
             requests:
               memory: "1Gi"
               cpu: "1000m"
             limits:
               memory: "1Gi"
               cpu: "1000m"
           affinity:
             enablePodAntiAffinity: true
             tolerations:
             - key: cnpg.io/cluster
               effect: NoSchedule
               value: gke-pg-cluster
               operator: Equal
             additionalPodAffinity:
               preferredDuringSchedulingIgnoredDuringExecution:
               - weight: 1
                 podAffinityTerm:
                   labelSelector:
                     matchExpressions:
                     - key: app.component
                       operator: In
                       values:
                       - "pg-cluster"
                   topologyKey: topology.kubernetes.io/zone
           monitoring:
             enablePodMonitor: true

  3. Check the status of the cluster:
         
         kubectl get cluster -n pg-ns --watch
         

Wait for the output to show a status of `Cluster in healthy state` before you move to the next step.




## Run queries with a Vertex AI Colab Enterprise notebook

In this section, you upload vectors into a PostgreSQL table and run semantic search queries by using SQL syntax.

You connect to your PostgreSQL database by using Colab Enterprise. You use a dedicated runtime template to deploy to the `postgres-vpc`, so the notebook can communicate with resources in the GKE cluster.

For more information about Vertex AI Colab Enterprise, see [Colab Enterprise documentation](https://docs.cloud.google.com/colab/docs/introduction).

### Create a runtime template

To create a Colab Enterprise runtime template:

  1. In the Google Cloud console, go to the Colab Enterprise **Runtime Templates** page and make sure your project is selected:

[Go to Runtime Templates](https://console.cloud.google.com/vertex-ai/colab/runtime-templates)

  2. Click _add_box_ **New Template**. The **Create new runtime template** page appears.

  3. In the **Runtime basics** section: 

     * In the **Display name** field, enter `pgvector-connect`.
     * In the **Region** drop-down list, select `us-central1`. It's the same region as your GKE cluster.
  4. In the **Configure compute** section: 

     * In the **Machine type** drop-down list, select `e2-standard-2`.
     * In the **Disk size** field, enter `30`.
  5. In the **Networking and security** section:

     * In the **Network** drop-down list, select the network where your GKE cluster resides.
     * In the **Subnetwork** drop-down list, select a corresponding subnetwork.
     * Clear the **Enable public internet access** checkbox.
  6. To finish creating the runtime template, click **Create**. Your runtime template appears in the list on the **Runtime templates** tab.




### Create a runtime

To create a Colab Enterprise runtime:

  1. In the runtime templates list for the template you just created, in the **Actions** column, click _more_vert_ and then click **Create runtime**. The **Create Vertex AI Runtime** pane appears.

  2. To create a runtime based on your template, click **Create**.

  3. On the **Runtimes** tab that opens, wait for the status to transition to **Healthy**.




### Import the notebook

To import the notebook in Colab Enterprise:

  1. Go to the **My Notebooks** tab and click **Import**. The **Import notebooks** pane appears.

  2. In **Import source** , select **URL**.

  3. Under **Notebook URLs** , enter the following link:
         
         https://raw.githubusercontent.com/epam/kubernetes-engine-samples/internal_lb/databases/postgres-pgvector/manifests/02-notebook/vector-database.ipynb
         

  4. Click **Import**.




### Connect to the runtime and run queries

To connect to the runtime and run queries:

  1. In the notebook, next to the **Connect** button, click _arrow_drop_down_ **Additional connection options**. The **Connect to Vertex AI Runtime** pane appears.

  2. Select **Connect to a runtime** and then select **Connect to an existing Runtime**.

  3. Select the runtime that you launched and click **Connect**.

  4. To run the notebook cells, click the ![](https://docs.cloud.google.com/static/colab/images/icon-run-cell.png)**Run cell** button next to each code cell.




The notebook contains both code cells and text that describes each code block. Running a code cell executes its commands and displays an output. You can run the cells in order, or run individual cells as needed.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

The easiest way to avoid billing is to delete the project you created for this tutorial.

**Caution** : Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 



If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    
    gcloud projects delete PROJECT_ID

If you deleted the project, your clean up is complete. If you didn't delete the project, proceed to delete the individual resources.

### Delete individual resources

  1. Set environment variables.
         
         export PROJECT_ID=${PROJECT_ID}
         export KUBERNETES_CLUSTER_PREFIX=postgres
         export REGION=us-central1
         

  2. Run the `terraform destroy` command:
         
         export GOOGLE_OAUTH_ACCESS_TOKEN=$(gcloud auth print-access-token)
         terraform  -chdir=../postgresql-cloudnativepg/terraform/FOLDER destroy \
         -var project_id=${PROJECT_ID} \
         -var region=${REGION} \
         -var cluster_prefix=${KUBERNETES_CLUSTER_PREFIX}
         

Replace `FOLDER` with either `gke-autopilot` or `gke-standard`, depending on the type of GKE cluster you created.

When prompted, type `yes`.




## What's next

  * Explore how to deploy [PostgreSQL clusters on GKE using CloudNativePG operator](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/stateful-workloads/cloudnativepg).
  * Learn about the [best practices for deploying databases on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/database-options).
  * Discover solutions for running [data-intensive workloads with GKE](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
