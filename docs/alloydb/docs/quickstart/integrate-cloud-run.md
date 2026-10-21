---
url: https://docs.cloud.google.com/alloydb/docs/quickstart/integrate-cloud-run/
title: Quickstart: Connect from Cloud Run \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:02.193471+00:00
---

# Quickstart: Connect from Cloud Run  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/quickstart/integrate-cloud-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connect from Cloud Run

This quickstart guides you through the process of deploying a sample application on a [Cloud Run](https://docs.cloud.google.com/run/docs) service by using the Google Cloud console and a client application. This sample application connects Cloud Run to AlloyDB for PostgreSQL.

## Sample application code

The sample application code for this quickstart is located in the `examples/go` directory of the [`GoogleCloudPlatform/alloydb-auth-proxy`](https://github.com/GoogleCloudPlatform/alloydb-auth-proxy) GitHub repository.

The application is written in the Go programming language and serves as a tool for collecting votes. The main logic is contained in the `main.go` file, which starts a web server and handles user requests.

The database connection is configured using environment variables, which you set up when you create the Cloud Run service. These variables tell the application how to connect to your AlloyDB instance, including the database name, user, password, and the instance's IP address. The code uses these variables to establish a secure connection to your AlloyDB database.

### Code repository

The `alloydb-auth-proxy` repository contains the [AlloyDB Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/overview), a tool that helps you securely connect to your AlloyDB instances. The repository also includes related libraries and examples, such as the Go application used in this quickstart.

You don't need the entire `alloydb-auth-proxy` project to connect to AlloyDB from Cloud Run. The `cloudshell_open` command clones the entire repository for your convenience, but the only files used to build the container for this quickstart are located in the `examples/go` directory.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Compute Engine, Cloud Run, AlloyDB, Cloud Resource Manager, Service Networking, Cloud Build, and Container Registry APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=alloydb.googleapis.com,compute.googleapis.com,cloudresourcemanager.googleapis.com,cloudbuild.googleapis.com,containerregistry.googleapis.com,servicenetworking.googleapis.com,run.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Compute Engine, Cloud Run, AlloyDB, Cloud Resource Manager, Service Networking, Cloud Build, and Container Registry APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=alloydb.googleapis.com,compute.googleapis.com,cloudresourcemanager.googleapis.com,cloudbuild.googleapis.com,containerregistry.googleapis.com,servicenetworking.googleapis.com,run.googleapis.com)

  10. Make sure that you have an AlloyDB cluster and primary instance. For more information, see [Create a cluster and its primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create).



### Required roles

To get the permissions that you need to connect from Cloud Run, ask your administrator to grant you the following IAM roles on your project: 

  * [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [AlloyDB Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)
  * [Artifact Registry Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`)
  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)
  * [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)
  * [Container Analysis Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.admin) (`roles/containeranalysis.admin`)
  * [Service Account Token Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`)
  * [Monitoring Metric Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter) (`roles/monitoring.metricWriter`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Connect to your instance and create a database

  1. If you are not in your newly created cluster **Overview** page, then in the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. To display the cluster **Overview** page, click the `my-cluster` cluster name.

  3. In the navigation menu, click **AlloyDB Studio**.

  4. In the **Database** list in **Log in to your database** , select `postgres`.

  5. In the **User** drop-down list, select `postgres`.

  6. In the **Password** field, enter the password you created in [Create a cluster and its primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create).

  7. Click **Authenticate**. The **Explorer** pane displays a list of the objects in your database.

  8. In the **Untitled query** tab, create a database:
         
         CREATE DATABASE quickstart_db;
         

  9. Click **Run**. Wait for the `Statement executed successfully` message to display in the **Results** pane.




## Find your project ID

  1. Go to the **Dashboard** page in the Google Cloud console.

[ Go to Dashboard](https://console.cloud.google.com/home)

  2. Find the project ID on the **Project info** card.

  3. Take note of your project ID. You need it for the following step of this quickstart.




## Populate Artifact Registry with an image of the sample application

  1. In the Google Cloud console, open **Cloud Shell**.

[Open Cloud Shell](https://shell.cloud.google.com/?show=ide%2Cterminal)

  2. In Cloud Shell Editor, use the following command to clone the repository with the sample application code from GitHub:
         
         cloudshell_open --repo_url \
         "https://github.com/GoogleCloudPlatform/alloydb-auth-proxy" \
         --dir \
         "examples/go" \
         --force_new_clone

  3. Create a repository in Artifact Registry for docker images:
         
         gcloud artifacts repositories create cloud-run-source-deploy --location us-central1 --repository-format=docker --project PROJECT_ID

Replace `PROJECT_ID` with the ID of your project.

  4. In the **Authorize Cloud Shell** dialog, click **Authorize**. This prompt does not appear if you have done this step previously.

  5. To build a Docker container and publish it to Artifact Registry, use the following command:
         
         gcloud builds submit --tag  us-central1-docker.pkg.dev/PROJECT_ID/cloud-run-source-deploy/run-sql --project PROJECT_ID

Replace `PROJECT_ID` with the ID of your project.

The sample application code for this quickstart is located in the `examples/go` directory of the [`GoogleCloudPlatform/alloydb-auth-proxy`](https://github.com/GoogleCloudPlatform/alloydb-auth-proxy) GitHub repository. The `cloudshell_open` command in the previous step automatically clones this repository and opens the correct directory for you.




## Find the IP address for your new instance

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Find the row in the table whose **Resource name** is `my-primary`.

  3. Take note of that row's **Private IP address**. You need it for the following step of this quickstart.

The example format of the IP address is `172.19.209.2:5432`.

**Note:** If you are using a Free Trial cluster, the **Clusters** page might not display the private IP address. You can run the following command in **Cloud Shell** to find your primary instance's private IP address: 
         
         gcloud alloydb instances describe INSTANCE_ID \
         --cluster=CLUSTER_ID \
         --region=LOCATION \
         --format="value(ipAddress)"




## Create a service for Cloud Run

  1. In the Google Cloud console, go to the **Cloud Run** page.

[Go to Cloud Run](https://console.cloud.google.com/run?enableapi=true)

  2. In the **Services** tab, click **Deploy Container**.

  3. In the **Create service** page, select the **Deploy one revision from an existing container image** option.

  4. In the **Container image URL** field, click **Select**.

  5. In the **Select container image** pane, complete the following steps:

     1. Select the **Artifact registry** tab.
     2. Expand `us-central1-docker.pkg.dev/PROJECT_ID/cloud-run-source-deploy`.
     3. Expand `run-sql`.
     4. Select the latest image.
     5. Click **Select**.
  6. In the **Service name** field, enter `quickstart-service`.

  7. Make sure `us-central1 (Iowa)` is selected in the **Region** list by default.

  8. In the **Authentication** section, select **Allow public access**.

  9. Ensure that **CPU is only allocated during request processing** is selected in the **CPU allocation and pricing** section.

  10. Expand the **Container(s), Volumes, Networking, Security** section.

  11. In the **Container(s)** tab, select the **Variables & secrets** tab and complete the following steps:

     1. In the **Environment variables** section, click **Add variable**.

     2. Enter the following in the `Name` and `Value` fields:

        * `DB_NAME`: `quickstart_db`
        * `DB_USER`: `postgres`
        * `DB_PASS`: The password that you entered when you [created the cluster](https://docs.cloud.google.com/alloydb/docs/cluster-create).
        * `DB_PORT`: `5432`
        * `INSTANCE_HOST`: The IP address of your cluster's primary instance, which you found in Find the IP address for your new instance. Don't include the port number—for example, set to `172.19.209.2`, and not `172.19.209.2:5432`.
  12. Switch from the **Container(s)** tab to the **Networking** tab and complete the following steps:

     1. Select the **Connect to a VPC for outbound traffic** checkbox.

     2. Select the **Send traffic directly to a VPC** option.

     3. In the **Network** drop-down list, choose the `default` value.

     4. In the **Subnet** drop-down list, ensure that the `default` value is selected.

  13. Click **Create** to create the Cloud Run service.

After the Cloud Run service is deployed, the **quickstart-service** page displays the URL of the sample application in the **URL** field.

The application uses AlloyDB as its data store.




## View the sample application

  1. In the Google Cloud console, go to the **Cloud Run** page.

[Go to Cloud Run](https://console.cloud.google.com/run?enableapi=true)

  2. On the **quickstart-service** page, click _content_copy_ **Copy to clipboard** to copy the application URL.

  3. In a new browser tab, paste the copied application URL and click **Enter**.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Clean up the cluster

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Next to the `my-cluster` cluster that you want to delete, click _more_vert_ **Actions** , and then click _delete_ **Delete**.

  3. In the **Delete cluster** dialog that appears, type `my-cluster` in the **my-cluster** field, confirming that you want to delete it.

  4. Click **Delete**.




### Clean up the service

  1. In the Google Cloud console, go to the **Cloud Run** page.

[Go to Cloud Run](https://console.cloud.google.com/run?enableapi=true)

  2. Select the checkbox next to the `quickstart-service` service name.

  3. Click _delete_ **Delete** at the top of the **Cloud Run** page.

  4. In the **Delete quickstart-service** dialog that appears, click **Delete** to confirm.




## What's next

  * [Enable project access to AlloyDB](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect)

  * [Grant AlloyDB access to other users](https://docs.cloud.google.com/alloydb/docs/user-grant-access)

  * [Enable private services access](https://docs.cloud.google.com/alloydb/docs/configure-connectivity)

  * [Create a cluster and its primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
