---
url: https://docs.cloud.google.com/alloydb/docs/quickstart/integrate-kubernetes/
title: Connect from Google Kubernetes Engine (GKE) to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:39.720836+00:00
---

# Connect from Google Kubernetes Engine (GKE) to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/quickstart/integrate-kubernetes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Connect from Google Kubernetes Engine (GKE) to AlloyDB for PostgreSQL Stay organized with collections  Save and categorize content based on your preferences. 

To securely connect a containerized application in a Google Kubernetes Engine Autopilot cluster to an AlloyDB for PostgreSQL instance, you can deploy the [AlloyDB Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/overview) as a sidecar container over a private IP network connection.

AlloyDB is a fully managed, PostgreSQL-compatible database service in Google Cloud, and Google Kubernetes Engine helps you automatically deploy, scale, and manage Kubernetes workloads.

## Objectives

  * Build a Docker image for AlloyDB.
  * Run an application in Google Kubernetes Engine.
  * Connect to an AlloyDB instance using AlloyDB Auth Proxy and internal IP.



## Costs

This tutorial uses billable components of Google Cloud, including:

  * AlloyDB
  * Google Kubernetes Engine
  * Artifact Registry



Use the [pricing calculator](https://cloud.google.com/products/calculator/) to generate a cost estimate based on your projected usage.

## Before you begin

###  Console 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Verify that you have the permissions required to complete this tutorial.
  7. Enable the Cloud APIs required to create and connect to AlloyDB.

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=alloydb.googleapis.com,compute.googleapis.com,cloudresourcemanager.googleapis.com,cloudbuild.googleapis.com,containerregistry.googleapis.com,servicenetworking.googleapis.com,artifactregistry.googleapis.com,container.googleapis.com)

     1. In the **Confirm project** step, click **Next** to confirm the name of the project you are going to make changes to.

     2. In the **Enable APIs** step, click **Enable** to enable the following:

        * AlloyDB API
        * Artifact Registry API
        * Compute Engine API
        * Cloud Resource Manager API
        * Cloud Build API
        * Container Registry API
        * Kubernetes Engine API
        * Service Networking API
**Note:** If you've already enabled any or all of these APIs, you won't see them listed here. 




###  gcloud 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Verify that you have the permissions required to complete this tutorial.



For the purposes of this tutorial, use the sample vote-collecting web application named `gke-alloydb-app`.

### Required roles

To get the permissions that you need to complete the tasks in this tutorial, ask your administrator to grant you the following IAM roles on your project: 

  * [Databases Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)
  * [Kubernetes Engine Cluster Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.clusterAdmin) (`roles/container.clusterAdmin`)
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
  * [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`)
  * [Artifact Registry Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Launch Cloud Shell

[Cloud Shell](https://docs.cloud.google.com/shell/docs) is a shell environment for managing resources hosted on Google Cloud.

Cloud Shell comes preinstalled with the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) and [kubectl](https://kubernetes.io/docs/reference/kubectl/) command-line tools. The gcloud CLI provides the primary command-line interface for Google Cloud. `kubectl` provides the primary command-line interface for running commands against Kubernetes clusters.

###  Console 

To launch Cloud Shell, complete the following steps.

  1. Go to the Google Cloud console.

[Google Cloud console](https://console.cloud.google.com/)

  2. Click ![Activate Cloud Shell button](https://docs.cloud.google.com/static/shell/docs/images/activate-cloud-shell-button.svg)**Activate Cloud Shell** at the top of the Google Cloud console.

  3. In the **Authorize Cloud Shell** dialog, click **Authorize**.

A Cloud Shell session opens inside a frame lower on the console. Use this shell to run `gcloud` and `kubectl` commands.

     1. Before you run commands, set your default project in the Google Cloud CLI using the following command:
            
            gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your [project ID](https://support.google.com/googleapi/answer/7014113).




###  gcloud 

  1. To launch Cloud Shell, complete the following steps.

  2. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  3. To initialize the environment, set your default project in the Google Cloud CLI using the following command:
         
         gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your [project ID](https://support.google.com/googleapi/answer/7014113).

  4. Enable the Cloud APIs necessary to create and connect to AlloyDB for PostgreSQL.
         
         gcloud services enable alloydb.googleapis.com \
             compute.googleapis.com \
             cloudresourcemanager.googleapis.com \
             cloudbuild.googleapis.com \
             containerregistry.googleapis.com \
             servicenetworking.googleapis.com \
             artifactregistry.googleapis.com \
             container.googleapis.com


**Note:** If you've already enabled any or all of these APIs, you won't see them listed here.

## Create an AlloyDB cluster and its primary instance

Your AlloyDB cluster comprises a number of nodes within a Google Virtual Private Cloud (VPC). When you create a cluster, you also configure private services access between one of your VPCs and the Google-managed VPC containing your new cluster. We recommend that you use an internal IP access to avoid exposure of the database to the public internet.

To connect to an AlloyDB for PostgreSQL cluster from outside its configured VPC, you configure Private Service Access configuration in the VPC for AlloyDB and use the default VPC network to run queries from an application deployed on a GKE cluster.

###  Console 

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. In the **Configure your cluster** section, in the **Cluster ID** field, enter an ID for your cluster. It must begin with a lowercase letter and can contain lowercase letters, numbers, and hyphens, such as `alloydb-cluster`.

  3. In the **Password** field, enter the CLUSTER_PASSWORD to use for the default `postgres` database user while creating the cluster.

  4. In the **Database version** field, select the major `POSTGRES_VERSION` for your new AlloyDB cluster.

  5. Select a REGION for your cluster, such as `us-central1`.

  6. In the **Configure your primary instance** section, do the following:

     1. In the **Instance ID** field, enter the INSTANCE_ID for your primary instance such as `alloydb-primary`.

     2. Select a machine series, for example, `N2`.

     3. Select a machine type and specify the number of virtual processing units NUM_CPU, such as `2`.

     4. To ensure an IP range is assigned to service peering, configure the **Private Services Access (PSA)** connection:

        1. In the **Network** list, select `default`.

        2. If an IP range like `default-ip-range` is already reserved, select it from the **Allocated IP range** list.

        3. If no IP range is assigned, click **Allocate custom IP range** to allocate a new internal IP_RANGE_NAME and [configure the connection](https://docs.cloud.google.com/alloydb/docs/configure-connectivity#create-ip-ranges).

  7. Click **Create cluster**.




Wait for the AlloyDB instance to get created. This can take several minutes.

###  gcloud 

  1. In the Cloud Shell, check if the unused IP addresses (IPv4) range is already assigned to service peering:
         
         gcloud services vpc-peerings list --network=default

Skip the next step if your output looks similar to the following:
         
         network: projects/493573376485/global/networks/default
         peering: servicenetworking-googleapis-com
         reservedPeeringRanges:
         - default-ip-range
         service: services/servicenetworking.googleapis.com
         

In this output, the value of `reservedPeeringRanges` is `default-ip-range`, which you can use as IP_RANGE_NAME to create a private connection in step 3.

  2. (Skip when using the default value of `reservedPeeringRanges`) To allocate unused IP addresses in the VPC, use the following command:
         
         gcloud compute addresses create IP_RANGE_NAME \
             --global \
             --purpose=VPC_PEERING \
             --prefix-length=16 \
             --description="VPC private service access" \
             --network=default

Replace `IP_RANGE_NAME` with your name for available internal IP addresses within an AlloyDB subnet, such as `alloydb-gke-psa-01`.

  3. To configure service access using the allocated IP range, run the following command:
         
         gcloud services vpc-peerings connect \
             --service=servicenetworking.googleapis.com \
             --ranges=IP_RANGE_NAME \
             --network=default

  4. To deploy the AlloyDB cluster, run the following command:
         
         gcloud alloydb clusters create CLUSTER_ID \
             --database-version=POSTGRES_VERSION \
             --password=CLUSTER_PASSWORD \
             --network=default \
             --region=REGION \
             --project=PROJECT_ID

Replace the following:

     * `CLUSTER_ID`: the ID of the cluster that you are creating. It must begin with a lowercase letter and can contain lowercase letters, numbers, and hyphens, such as `alloydb-cluster`.
     * `VERSION`: the major version of PostgreSQL that you want the cluster's database servers to be compatible with. Choose one of the following:

       * `14`: for compatibility with PostgreSQL 14

       * `15`: for compatibility with PostgreSQL 15

       * `16`: for compatibility with PostgreSQL 16

       * `17`: for compatibility with PostgreSQL 17, which is the supported default PostgreSQL version

       * `18`, for compatibility with PostgreSQL 18

     * `CLUSTER_PASSWORD`: the password to use for the default `postgres` user.

     * `PROJECT_ID`: the ID of your Google Cloud project where you want to place the cluster.

     * `REGION`: the name of the region where the AlloyDB cluster is created, such as `us-central1`.

  5. To deploy the AlloyDB primary instance, run the following:
         
         gcloud alloydb instances create INSTANCE_ID \
             --instance-type=PRIMARY \
             --cpu-count=NUM_CPU \
             --region=REGION \
             --cluster=CLUSTER_ID \
             --project=PROJECT_ID

Replace the following:

     * `INSTANCE_ID` with the name of the AlloyDB instance of your choice, such as `alloydb-primary`.
     * `CLUSTER_ID` with the name of the AlloyDB cluster, such as `alloydb-cluster`.
     * `NUM_CPU` with the number of virtual processing units, such as `2`.
     * `PROJECT_ID` with the ID of your Google Cloud project.
     * `REGION` with the name of the region where the AlloyDB cluster is created, such as `us-central1`.

Wait for the AlloyDB instance to get created. This can take several minutes.




## Connect to your primary instance and create an AlloyDB database and user

To create a database and a database user on your primary instance, complete the following steps:

###  Console 

  1. If you're not in your newly created cluster **Overview** page, then in the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. To display the cluster **Overview** page, click the CLUSTER_ID cluster name.

  3. In the navigation menu, click **AlloyDB Studio**.

  4. On the **Sign in to AlloyDB Studio** page, do the following:

     1. In the **Database** list, select `postgres`.

     2. In the **User** list, select `postgres`.

     3. In the **Password** field, enter `CLUSTER_PASSWORD` you created in Create an AlloyDB cluster and its primary instance.

     4. Click **Authenticate**. The **Explorer** pane displays a list of the objects in your database.

  5. In the **Editor 1** tab, complete the following:

     1. Create an AlloyDB database:
            
            CREATE DATABASE DATABASE_NAME;
            

Replace `DATABASE_NAME` with the name of your choice, such as `tutorial_db`.

     2. Click **Run**. Wait for the `Statement executed successfully` message to display in the **Results** pane.

     3. Click **Clear**.

     4. Create an AlloyDB database user and password:
            
            CREATE USER USERNAME WITH PASSWORD 'DATABASE_PASSWORD';
            

Replace the following:

        * `USERNAME`: the name of the AlloyDB user, such as `tutorial_user`.

        * `DATABASE_PASSWORD`: the password for your AlloyDB database, such as `tutorial`.

     5. Click **Run**. Wait for the `Statement executed successfully` message to display in the **Results** pane.

  6. In the **Explorer** pane of the AlloyDB Studio, click _manage_accounts_ **Switch user/database**.

  7. On the **Sign in to AlloyDB Studio** page, do the following:

     1. In the **Database** list, select `DATABASE_NAME`, such as `tutorial_db`.

     2. In the **User** list, select `postgres`.

     3. In the **Password** field, enter `CLUSTER_PASSWORD` you created in Create an AlloyDB cluster and its primary instance.

     4. Click **Authenticate**. The **Explorer** pane displays a list of the objects in your database.

  8. In the **Editor 1** tab, complete the following:

     1. Grant all permissions to the AlloyDB database user:
            
            GRANT ALL PRIVILEGES ON DATABASE "DATABASE_NAME" to "USERNAME";
            

     2. Click **Run**. Wait for the `Statement executed successfully` message to display in the **Results** pane.

     3. Click **Clear**.

     4. Grant permissions to the AlloyDB database user on the public schema:
            
            GRANT CREATE ON SCHEMA public TO "USERNAME";
            

     5. Click **Run**. Wait for the `Statement executed successfully` message to display in the **Results** pane.

  9. Take note of the database name, username, and password. You use this information in Create a Kubernetes secret.




###  gcloud 

  1. To create an AlloyDB database user, run the following command in the Cloud Shell:
         
         gcloud alloydb users create USERNAME \
             --cluster=CLUSTER_ID \
             --region=REGION \
             --password=DATABASE_PASSWORD

Replace the following:

     * `USERNAME`: the name of the AlloyDB user, such as `tutorial_user`.
     * `CLUSTER_ID`: the ID of the cluster, such as `alloydb-cluster`.
     * `REGION`: the region where the cluster is located, such as `us-central1`.
     * `DATABASE_PASSWORD`: the password for your AlloyDB database, such as `tutorial`.
  2. To create a database and grant permissions, you must connect to the cluster and run SQL commands. In the Cloud Shell, use the `psql` client to connect to your instance.

**Note:** To connect to an AlloyDB instance from the Cloud Shell, you must use the [AlloyDB Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/overview). For a simpler setup, you can perform these steps using AlloyDB Studio in the Google Cloud console.
  3. Once connected to your instance as the `postgres` user, create the database:
         
         CREATE DATABASE DATABASE_NAME;
         

Replace `DATABASE_NAME` with the name of your choice, such as `tutorial_db`.

  4. Grant all permissions to the AlloyDB database user on the new database:
         
         GRANT ALL PRIVILEGES ON DATABASE "DATABASE_NAME" to "USERNAME";
         

  5. Connect to the new database and grant permissions on the `public` schema:
         
         \c DATABASE_NAME
         GRANT CREATE ON SCHEMA public TO "USERNAME";
         

  6. Take note of the database name, username, and password. You use this information in Create a Kubernetes secret.




## Create a GKE Autopilot cluster

A cluster contains at least one _cluster control plane_ machine and multiple worker machines called _nodes_. Nodes are Compute Engine virtual machine (VM) instances that run the Kubernetes processes required to make them part of the cluster. You deploy applications to clusters, and the applications run on the nodes.

###  Console 

  1. In the Google Cloud console, go to the **Kubernetes Clusters** page.

[Go to Kubernetes Clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Click **Create**.

  3. Specify `GKE_CLUSTER_ID` for your Autopilot cluster in the **Name** field of the **Cluster Basics** page, such as `ap-cluster`.

  4. In the **Region** field, select `REGION`, such as `us-central1`.

  5. Click **Create**.

Wait for the GKE cluster to get created. This can take several minutes.




###  gcloud 

Create an Autopilot cluster:
    
    
    gcloud container clusters create-auto GKE_CLUSTER_ID \
        --location=REGION

Replace the following:

  * `GKE_CLUSTER_ID`: the name of the Autopilot cluster, such as `ap-cluster`.
  * `REGION`: the name of the region where the GKE cluster is deployed, such as `us-central1`.



Wait for the GKE cluster to get created. This can take several minutes.

## Connect to AlloyDB using the AlloyDB Auth Proxy

We recommend that you use [AlloyDB Auth Proxy](https://cloud.google.com/alloydb/docs/auth-proxy/overview) to connect to AlloyDB. The AlloyDB Auth Proxy provides strong encryption and authentication using Identity and Access Management (IAM), which can help keep your database secure.

When you connect using the AlloyDB Auth Proxy, it is added to your Pod using the `sidecar` container pattern. The AlloyDB Auth Proxy container is in the same Pod as your application, which enables the application to connect to the AlloyDB Auth Proxy using `localhost`, increasing security and performance.

### Grant Artifact Registry access to the default Compute Engine service account

Grant the Artifact Registry Reader (`roles/artifactregistry.reader`) role to the default Compute Engine service account so that your Google Kubernetes Engine nodes can pull container images from Artifact Registry.

###  Console 

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. On the **Permissions for project "` PROJECT_ID`"** page, find the row containing the default compute service account `PROJECT_NUMBER-compute@developer.gserviceaccount.com` and click _edit_ **Edit principal** in that row.

To get the `PROJECT_NUMBER` that is an automatically generated unique identifier for your project, do the following:

     1. Go to the [**Dashboard**](https://console.cloud.google.com/home) page in the Google Cloud console.

[ Go to Dashboard](https://console.cloud.google.com/home)

     2. Click the **Select from** drop-down list at the top of the page. In the **Select from** window that appears, select your project.

The `PROJECT_NUMBER` is displayed on the project Dashboard **Project info** card.

  3. Click add**Add another role**.

  4. To grant the `roles/artifactregistry.reader` role, click **Select a role** and choose `Artifact Registry` from **By product or service** , and choose `Artifact Registry Reader` from **Roles**.

  5. Click **Save**. The principal is granted the role.




###  gcloud 

Grant the Artifact Registry Reader role (`roles/artifactregistry.reader`) on the project to the default Compute Engine service account:
    
    
    PROJECT_NUMBER=$(gcloud projects describe PROJECT_ID --format="value(projectNumber)")
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="serviceAccount:$PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
        --role="roles/artifactregistry.reader" \
        --condition=None

Replace `PROJECT_ID` with your project ID.

### Configure Workload Identity Federation for GKE for the sample application

Configure Google Kubernetes Engine to authenticate the AlloyDB Auth Proxy by using [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity). With Workload Identity Federation for GKE, you create a Kubernetes ServiceAccount for your application in the Google Kubernetes Engine cluster and grant IAM roles to that Kubernetes ServiceAccount. Create a Kubernetes ServiceAccount that is unique to each application so that you can limit permissions on a per-application basis.

###  Console 

  1. To launch Cloud Shell, complete the following steps.

  2. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  3. In the Cloud Shell, get credentials for your cluster:
         
         gcloud container clusters get-credentials GKE_CLUSTER_ID --region REGION --project PROJECT_ID

This command configures `kubectl` to use the GKE cluster that you created.

  4. In the editor of your choice, complete the following steps:

     1. Open `service-account.yaml` using nano, for example:
            
            nano service-account.yaml

     2. In the editor, paste the following content:
            
            apiVersion: v1
            kind: ServiceAccount
            metadata:
              name: KUBERNETES_SERVICEACCOUNT
            

Replace `KUBERNETES_SERVICEACCOUNT` with the Kubernetes ServiceAccount name, such as `alloydb-sa`.

     3. Press `Control+O`, hit `ENTER` to save the changes, and press `Control+X` to exit the editor.

  5. Create a Kubernetes ServiceAccount for your sample application:
         
         kubectl apply -f service-account.yaml

  6. To grant IAM roles to the Kubernetes ServiceAccount, complete the following steps in the Google Cloud console:

     1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

     2. Select your project.

     3. Click **Grant access**.

     4. In the **New principals** field, enter the following:

`principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/default/sa/KUBERNETES_SERVICEACCOUNT`

Replace the following:

        * `PROJECT_NUMBER`: your project number.
        * `PROJECT_ID`: your project ID.
        * `KUBERNETES_SERVICEACCOUNT`: the Kubernetes ServiceAccount name, such as `alloydb-sa`.
     5. To grant the `roles/alloydb.client` role, in the **Select a role** list, choose **AlloyDB for PostgreSQL** > **AlloyDB Client**.

     6. Click add**Add another role**.

     7. To grant the `roles/serviceusage.serviceUsageConsumer` role, in the **Select a role** list, choose **Service Usage** > **Service Usage Consumer**.

     8. Click **Save**.




###  gcloud 

  1. In the Google Cloud console, open **Cloud Shell**.

[Open Cloud Shell](https://shell.cloud.google.com/?show=ide%2Cterminal)

  2. In the Cloud Shell, get credentials for your cluster:
         
         gcloud container clusters get-credentials GKE_CLUSTER_ID --region REGION --project PROJECT_ID

This command configures `kubectl` to use the GKE cluster that you created.

  3. In the editor of your choice, complete the following steps:

     1. Open `service-account.yaml` using nano, for example:
            
            nano service-account.yaml

     2. In the editor, paste the following content:
            
            apiVersion: v1
            kind: ServiceAccount
            metadata:
              name: KUBERNETES_SERVICEACCOUNT
            

Replace `KUBERNETES_SERVICEACCOUNT` with the Kubernetes ServiceAccount name, such as `alloydb-sa`.

     3. Press `Control+O`, hit `ENTER` to save the changes, and press `Control+X` to exit the editor.

  4. Create a Kubernetes ServiceAccount for your sample application:
         
         kubectl apply -f service-account.yaml

  5. Grant the AlloyDB Client (`roles/alloydb.client`) and Service Usage Consumer (`roles/serviceusage.serviceUsageConsumer`) roles on the project to the Kubernetes ServiceAccount:
         
         PROJECT_ID="PROJECT_ID"
         KUBERNETES_SERVICEACCOUNT="KUBERNETES_SERVICEACCOUNT"
         PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format="value(projectNumber)")
         gcloud projects add-iam-policy-binding $PROJECT_ID \
             --member="principal://iam.googleapis.com/projects/$PROJECT_NUMBER/locations/global/workloadIdentityPools/$PROJECT_ID.svc.id.goog/subject/ns/default/sa/$KUBERNETES_SERVICEACCOUNT" \
             --role="roles/alloydb.client" \
             --condition=None
         gcloud projects add-iam-policy-binding $PROJECT_ID \
             --member="principal://iam.googleapis.com/projects/$PROJECT_NUMBER/locations/global/workloadIdentityPools/$PROJECT_ID.svc.id.goog/subject/ns/default/sa/$KUBERNETES_SERVICEACCOUNT" \
             --role="roles/serviceusage.serviceUsageConsumer" \
             --condition=None

Replace the following:

     * `PROJECT_ID`: your project ID.
     * `KUBERNETES_SERVICEACCOUNT`: the Kubernetes ServiceAccount name, such as `alloydb-sa`.



### Populate the Artifact Registry with an image of the sample application

To build a container image of the sample application and push it to a repository, complete the following steps.

###  Console 

  1. In the Google Cloud console, go to the **Artifact Registry** page.

[Go to Artifact Registry](https://console.cloud.google.com/artifacts)

  2. To create a repository, click add.

  3. In the **Name** field, enter `REPOSITORY_ID`, such as `gke-alloydb-sample-app`.

  4. In the **Format** section, select **Docker**.

  5. In the **Location type** section, select **Region** and choose `REGION`, such as `us-central1`.

  6. Click **Create**.

  7. To build the sample application image, launch Cloud Shell, complete the following steps.

  8. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

     1. In the Cloud Shell, clone the repository with the sample `gke-alloydb-app` application code from GitHub:
            
            git clone https://github.com/GoogleCloudPlatform/alloydb-auth-proxy && cd alloydb-auth-proxy/examples/go

     2. In the **Authorize Cloud Shell** dialog, click **Authorize**. This prompt doesn't appear if you have done this step previously.

     3. To build the Docker container and publish it to the Artifact Registry, run the following command:
            
            gcloud builds submit --tag REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY_ID/SAMPLE_APPLICATION --project PROJECT_ID

Replace the following:

        * `PROJECT_ID`: the ID of your project.
        * `REPOSITORY_ID`: the name of your repository, such as `gke-alloydb-sample-app`.
        * `SAMPLE_APPLICATION`: the name of your sample web application, such as `gke-alloydb-app`.



###  gcloud 

  1. In Cloud Shell, use the following command to clone the repository with the sample `gke-alloydb-app` application code from GitHub:
         
         git clone https://github.com/GoogleCloudPlatform/alloydb-auth-proxy && cd alloydb-auth-proxy/examples/go

  2. Create a repository in the Artifact Registry for Docker images:
         
         gcloud artifacts repositories create REPOSITORY_ID --location REGION --repository-format=docker --project PROJECT_ID

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `REPOSITORY_ID`: the name of your repository, such as `gke-alloydb-sample-app`.
  3. In the **Authorize Cloud Shell** dialog, click **Authorize**. This prompt doesn't appear if you have done this step previously.

  4. To build a Docker container and publish it to the Artifact Registry, use the following command:
         
         gcloud builds submit --tag  REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY_ID/SAMPLE_APPLICATION --project PROJECT_ID

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `REPOSITORY_ID`: the name of your repository, such as `gke-alloydb-sample-app`.
     * `SAMPLE_APPLICATION`: the name of your sample web application, such as `gke-alloydb-app`.



### Create a Kubernetes secret

You create Kubernetes secrets for the database, user, and user password to be used by the sample application. The values of each secret are based on the values specified in the Connect to your primary instance and create an AlloyDB database and user step of this tutorial. For more information, see [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/).

###  Console 

In your open Cloud Shell, use a Kubernetes `SECRET`, such as `gke-alloydb-secret` to store the connection information:
    
    
    kubectl create secret generic SECRET \
      --from-literal=database=DATABASE_NAME \
      --from-literal=username=USERNAME \
      --from-literal=password=DATABASE_PASSWORD

###  gcloud 

Use a Kubernetes `SECRET`, such as `gke-alloydb-secret` to store the connection information:
    
    
    kubectl create secret generic SECRET \
      --from-literal=database=DATABASE_NAME \
      --from-literal=username=USERNAME \
      --from-literal=password=DATABASE_PASSWORD

### Deploy and run the AlloyDB Proxy in a sidecar pattern

We recommend that you run the AlloyDB Proxy in a `sidecar` pattern as an additional container sharing a Pod with your application for the following reasons:

  * Prevents your SQL traffic from being exposed locally. The AlloyDB Proxy provides encryption on outgoing connections, but you need to limit exposure for incoming connections.
  * Prevents a single point of failure. Each application's access to your database is independent from the others, making it more resilient.
  * Limits access to the AlloyDB Proxy, allowing you to use IAM permissions per application rather than exposing the database to the entire cluster.
  * Lets you scope resource requests more accurately. Because the AlloyDB Proxy consumes resources linearly to usage, this pattern lets you more accurately scope and request resources to match your applications as it scales.
  * Lets you configure your application to connect using `127.0.0.1` on the DB_PORT you specified in the command section.



After you create a GKE cluster and build a container image for your application, deploy your containerized application to the GKE cluster.

###  Console 

In this tutorial, you deploy the sample vote-collecting web application, `gke-alloydb-app`, that uses AlloyDB as the Datastore.

  1. Get the connection URI (`INSTANCE_URI`) for the AlloyDB primary instance:

     1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

     2. To display the cluster **Overview** page, click your cluster name in the **Resource name** column.

     3. In the **Instances in your cluster** section, locate your primary instance and go to the **Connectivity** section (or click **View connectivity configuration**).

     4. In the **Connection URI** field, click the **Copy to clipboard** content_copy button.

You specify this `INSTANCE_URI` in the `proxy_sidecar_deployment.yaml` definition file in step 2.b of this section.

  2. In your open Cloud Shell, complete the following steps:

     1. Open `proxy_sidecar_deployment.yaml` using the editor of your choice, for example, nano:
            
            nano proxy_sidecar_deployment.yaml

     2. In the editor, paste the following content:
            
            apiVersion: apps/v1
            kind: Deployment
            metadata:
              name: gke-alloydb
            spec:
              selector:
                matchLabels:
                  app: SAMPLE_APPLICATION
              template:
                metadata:
                  labels:
                    app: SAMPLE_APPLICATION
                spec:
                  serviceAccountName: KUBERNETES_SERVICEACCOUNT
                  containers:
                  - name: SAMPLE_APPLICATION
                    # Replace <PROJECT_ID> and <REGION> with your project ID and region.
                    image: REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY_ID/SAMPLE_APPLICATION:latest
                    imagePullPolicy: Always
                    # This app listens on port 8080 for web traffic by default.
                    ports:
                    - containerPort: 8080
                    env:
                    - name: PORT
                      value: "8080"
                    - name: INSTANCE_HOST
                      value: "127.0.0.1"
                    - name: DB_PORT
                      value: "5432"
                    - name: DB_USER
                      valueFrom:
                        secretKeyRef:
                          name: SECRET
                          key: username
                    - name: DB_PASS
                      valueFrom:
                       secretKeyRef:
                          name: SECRET
                          key: password
                    - name: DB_NAME
                      valueFrom:
                        secretKeyRef:
                          name: SECRET
                          key: database
                  - name: alloydb-proxy
                    # This uses the latest version of the AlloyDB Auth proxy
                    image: gcr.io/alloydb-connectors/alloydb-auth-proxy:1.10.1
                    command:
                      - "/alloydb-auth-proxy"
                      #AlloyDB instance name as parameter for the AlloyDB proxy
                      - "INSTANCE_URI"
                    securityContext:
                      runAsNonRoot: true
                    resources:
                      requests:
                        memory: "2Gi"
                        cpu:    "1"
            

Replace `KUBERNETES_SERVICEACCOUNT` with your Kubernetes ServiceAccount name and replace `INSTANCE_URI` with the path that you copied in step 1.

     3. Press `Control+O`, hit `ENTER` to save the changes, and press `Control+X` to exit the editor.

  3. To deploy the `gke-alloydb-app` application, apply the definition file:
         
         kubectl apply -f proxy_sidecar_deployment.yaml

  4. To verify that the application is running, go to the **Workloads** page in the Google Cloud console:

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload/overview)

Check that the status for the **gke-alloydb** deployment is **OK**.

  5. To connect to the sample application using an external load balancer, complete the following steps in your open Cloud Shell:

     1. Open `service.yaml`:
            
            nano service.yaml

     2. Paste the following content:
            
            apiVersion: v1
            kind: Service
            metadata:
              name: SAMPLE_APPLICATION
            spec:
              type: LoadBalancer
              selector:
                app: SAMPLE_APPLICATION
              ports:
              - port: 80
                targetPort: 8080
            

Replace `SAMPLE_APPLICATION` with your application name, such as `gke-alloydb-app`.

     3. Save and exit the editor, then apply the service:
            
            kubectl apply -f service.yaml

  6. To get the external IP address of your application, go to the **Services & Ingress** page in the Google Cloud console:

[Go to Services & Ingress](https://console.cloud.google.com/kubernetes/discovery)

  7. Use the value in the **External endpoints** column to access the application at the following URL:

`http://EXTERNAL_IP`




###  gcloud 

In this tutorial, you deploy the sample vote-collecting web application, `gke-alloydb-app`, that uses AlloyDB as the Datastore.

  1. Get the instance connection INSTANCE_URI for the AlloyDB primary instance you want AlloyDB proxy to connect to:
         
         gcloud alloydb instances describe INSTANCE_ID \
            --cluster=CLUSTER_ID \
            --region=REGION \
            --format="value(name)"

Replace the following:

     * `INSTANCE_ID`: name for the instance, such as `alloydb-primary`.
     * `CLUSTER_ID`: name for the cluster, such as `alloydb-cluster`.

The output contains the INSTANCE_URI you specify in the `proxy_sidecar_deployment.yaml` definition file in step 2.b of this section.

  2. In the editor of your choice, for example, nano, complete the following steps:

     1. Open `proxy_sidecar_deployment.yaml` using the editor of your choice, for example, nano:
            
            nano proxy_sidecar_deployment.yaml

     2. In the editor, paste the following content:
            
            apiVersion: apps/v1
            kind: Deployment
            metadata:
              name: gke-alloydb
            spec:
              selector:
                matchLabels:
                  app: SAMPLE_APPLICATION
              template:
                metadata:
                  labels:
                    app: SAMPLE_APPLICATION
                spec:
                  serviceAccountName: KUBERNETES_SERVICEACCOUNT
                  containers:
                  - name: SAMPLE_APPLICATION
                    # Replace <PROJECT_ID> and <REGION> with your project ID and region.
                    image: REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY_ID/SAMPLE_APPLICATION:latest
                    imagePullPolicy: Always
                    # This app listens on port 8080 for web traffic by default.
                    ports:
                    - containerPort: 8080
                    env:
                    - name: PORT
                      value: "8080"
                    # This project uses environment variables to determine
                    # how you would like to run your application
                    # To use the Go connector (recommended) - use INSTANCE NAME
                    # To use TCP - Setting INSTANCE_HOST will use TCP (e.g., 127.0.0.1)
                    - name: INSTANCE_HOST
                      value: "127.0.0.1"
                    - name: DB_PORT
                      value: "5432"
                    # To use Automatic IAM Authentication (recommended)
                    # use DB_IAM_USER instead of DB_USER
                    # you may also remove the DB_PASS environment variable
                    - name: DB_USER
                      valueFrom:
                        secretKeyRef:
                          name: SECRET
                          key: username
                    - name: DB_PASS
                      valueFrom:
                       secretKeyRef:
                          name: SECRET
                          key: password
                    - name: DB_NAME
                      valueFrom:
                        secretKeyRef:
                          name: SECRET
                          key: database
                 # If you are using the Go connector (recommended), you can
                  # remove alloydb-proxy (everything below this line)
                  - name: alloydb-proxy
                    # This uses the latest version of the AlloyDB Auth proxy
                    # It is recommended to use a specific version for production environments.
                    # See: https://github.com/GoogleCloudPlatform/alloydb-auth-proxy
                    image: gcr.io/alloydb-connectors/alloydb-auth-proxy:1.10.1
                    command:
                      - "/alloydb-auth-proxy"
                      #AlloyDB instance name as parameter for the AlloyDB proxy
                      # Use <INSTANCE_URI>
                      - "INSTANCE_URI"
                    securityContext:
                      # The default AlloyDB Auth proxy image runs as the
                      # "nonroot" user and group (uid: 65532) by default.
                      runAsNonRoot: true
                    resources:
                      requests:
                        # The proxy's memory use scales linearly with the number of active
                        # connections. Fewer open connections will use less memory. Adjust
                        # this value based on your application's requirements.
                        memory: "2Gi"
                        # The proxy's CPU use scales linearly with the amount of IO between
                        # the database and the application. Adjust this value based on your
                        # application's requirements.
                        cpu:    "1"
            

Replace `KUBERNETES_SERVICEACCOUNT` with your Kubernetes ServiceAccount name and replace `INSTANCE_URI` with the path to your AlloyDB primary instance from step 1, such as `projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID/instances/INSTANCE_ID`.

     3. Press `Control+O`, hit `ENTER` to save the changes, and press `Control+X` to exit the editor.

  3. To deploy the `gke-alloydb-app` application, apply the `proxy_sidecar_deployment.yaml` definition file that you created in the previous step:
         
         kubectl apply -f proxy_sidecar_deployment.yaml

  4. Verify that the status for both containers in the Pod is `running`:
         
         kubectl get pods

Sample output:
         
         NAME                          READY   STATUS    RESTARTS   AGE
          gke-alloydb-8d59bb4cc-62xgh   2/2     Running   0          2m53s
         

  5. To connect to the sample `gke-alloydb-app` application, use a service — for example, an external HTTP load balancer. In the editor of your choice, follow these steps:

     1. Open `service.yaml` using nano, for example:
            
            nano service.yaml

     2. In the nano editor, paste the following content:
            
            apiVersion: v1
            kind: Service
            metadata:
              name: SAMPLE_APPLICATION
            spec:
              type: LoadBalancer
              selector:
                app: SAMPLE_APPLICATION
              ports:
              - port: 80
                targetPort: 8080
            

Replace `SAMPLE_APPLICATION` with the name of your sample web application, such as `gke-alloydb-app`.

     3. Press `Control+O`, hit `ENTER` to save the changes, and press `Control+X` to exit the editor.

  6. To deploy the service `gke-alloydb-app` application, apply the `service.yaml` file:
         
         kubectl apply -f service.yaml

  7. To get the service details including the external IP address of the service, use the following command:
         
         kubectl get service

Sample output:
         
         NAME              TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)        AGE
         gke-alloydb-app   LoadBalancer   34.118.229.246   35.188.16.172   80:32712/TCP   45s
         kubernetes        ClusterIP      34.118.224.1     <none>          443/TCP        85m
         

  8. Use the value of the external IP from the previous step to access the sample application at the following URL:
         
         http://EXTERNAL-IP
         




### Sample configuration files

###  proxy_sidecar_deployment.yaml 
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: <YOUR-DEPLOYMENT-NAME>
    spec:
      selector:
        matchLabels:
          app: <YOUR-APPLICATION-NAME>
      template:
        metadata:
          labels:
            app: <YOUR-APPLICATION-NAME>
        spec:
          serviceAccountName: <YOUR-KSA-NAME>
          containers:
          # Your application container goes here.
          - name: <YOUR-APPLICATION-NAME>
            image: <YOUR-APPLICATION-IMAGE-URL>
            env:
            - name: DB_HOST
              # The port value here (5432) should match the --port flag below.
              value: "localhost:5432"
            - name: DB_USER
              valueFrom:
                secretKeyRef:
                  name: <YOUR-DB-SECRET>
                  key: username
            - name: DB_PASS
              valueFrom:
                secretKeyRef:
                  name: <YOUR-DB-SECRET>
                  key: password
            - name: DB_NAME
              valueFrom:
                secretKeyRef:
                  name: <YOUR-DB-SECRET>
                  key: database
          # The Auth Proxy sidecar goes here.
          - name: alloydb-auth-proxy
            # Make sure you have automation that upgrades this version regularly.
            # A new version of the Proxy is released monthly with bug fixes,
            # security updates, and new features.
            image: gcr.io/alloydb-connectors/alloydb-auth-proxy:1.10.1
            args:
              # If you're connecting over public IP, enable this flag.
              # - "--public-ip"
    
              # If you're connecting with PSC, enable this flag:
              # - "--psc"
    
              # If you're using auto IAM authentication, enable this flag:
              # - "--auto-iam-authn"
    
              # Enable structured logging with Google's LogEntry format:
              - "--structured-logs"
    
              # Listen on localhost:5432 by default.
              - "--port=5432"
              # Specify your instance URI, e.g.,
              # "projects/myproject/locations/us-central1/clusters/mycluster/instances/myinstance"
              - "<INSTANCE-URI>"
    
            securityContext:
              # The default AlloyDB Auth Proxy image runs as the "nonroot" user and
              # group (uid: 65532) by default.
              runAsNonRoot: true
            # You should use resource requests/limits as a best practice to prevent
            # pods from consuming too many resources and affecting the execution of
            # other pods. You should adjust the following values based on what your
            # application needs. For details, see
            # https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
            resources:
              requests:
                # The proxy's memory use scales linearly with the number of active
                # connections. Fewer open connections will use less memory. Adjust
                # this value based on your application's requirements.
                memory: "2Gi"
                # The proxy's CPU use scales linearly with the amount of IO between
                # the database and the application. Adjust this value based on your
                # application's requirements.
                cpu:    "1"

###  service.yaml 
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: <YOUR-SERVICE-NAME>
    spec:
      type: LoadBalancer
      selector:
        app: <YOUR-APPLICATION-NAME>
      ports:
      - port: 80
        targetPort: 8080

###  service-account.yaml 
    
    
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      name: <YOUR-KSA-NAME> # TODO(developer): replace this value

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources.

### Delete the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial.

To delete the project:

  1. In the Google Cloud console, go to the **Manage resources** page.

[ Manage resources](https://console.cloud.google.com/cloud-resource-manager)

  2. In the project list, select the project that you want to delete, and then click **Delete**.

  3. In the dialog, type your `PROJECT_ID`, and then click **Shut down** to delete the project.




## What's next

  * [About the AlloyDB Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/overview)
  * [Internal IP overview](https://docs.cloud.google.com/alloydb/docs/private-ip)
  * [Google Kubernetes Engine documentation](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
