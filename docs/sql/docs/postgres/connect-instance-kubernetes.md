---
url: https://docs.cloud.google.com/sql/docs/postgres/connect-instance-kubernetes/
title: Quickstart: Connect to Cloud SQL for PostgreSQL from Google Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:56.988016+00:00
---

# Quickstart: Connect to Cloud SQL for PostgreSQL from Google Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/connect-instance-kubernetes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connect to Cloud SQL for PostgreSQL from Google Kubernetes Engine

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/connect-instance-kubernetes "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/connect-instance-kubernetes "View this page for the SQL Server database engine")

This page shows you how to deploy a sample app on [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) connected to a PostgreSQL instance using the Google Cloud console and a client application. The resources created in this quickstart typically cost less than one dollar (USD), assuming you complete the steps, including the clean up, in a timely manner.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Verify that you have the permissions required to complete this guide. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Artifact Registry, Cloud Build, Cloud SQL Admin, Compute Engine, Kubernetes Engine, Service Networking APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,cloudbuild.googleapis.com,sqladmin.googleapis.com,compute.googleapis.com,container.googleapis.com,servicenetworking.googleapis.com)

  6. [Install](https://docs.cloud.google.com/sdk/docs/install) the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  7. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  8. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  9. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  10. Verify that you have the permissions required to complete this guide. 

  11. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  12. Enable the Artifact Registry, Cloud Build, Cloud SQL Admin, Compute Engine, Kubernetes Engine, Service Networking APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,cloudbuild.googleapis.com,sqladmin.googleapis.com,compute.googleapis.com,container.googleapis.com,servicenetworking.googleapis.com)

  13. [Install](https://docs.cloud.google.com/sdk/docs/install) the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  14. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  15. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




### Required roles

To get the permissions that you need to complete the tasks described in this quickstart, ask your administrator to grant you the following IAM roles on your quickstart project: 

  * Create, update, or delete all Cloud SQL instances, databases, and users: 
    * [Cloud SQL Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)
    * [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`)
  * Create a Cloud SQL instance with private IP (private services access connection): [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkadmin) (`roles/compute.networkadmin`) 
  * Create and manage a Google Kubernetes Engine cluster: [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`) 
  * Create and manage service accounts for the project: 
    * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
    * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceAccountAdmin#serviceAccountAdmin) (`roles/serviceAccountAdmin`)
  * Create a repository in Artifact Registry for the project: [Artifact Registry Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`) 
  * Submit and build applications in Cloud Build: 
    * [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuilds#cloudbuilds.builds.editor) (`roles/cloudbuilds.builds.editor`)
    * [Storage Object Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectCreator) (`roles/storage.objectCreator`)
    * [Storage Bucket Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.bucketViewer) (`roles/storage.bucketViewer`)
    * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
    * [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Set up Cloud SQL

### Create a Cloud SQL instance

#### Public IP

### Console

####  Create an instance with a public IP address 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click **Create Instance**.
  3. Click **PostgreSQL**.
  4. Enter `quickstart-instance` for **Instance ID**.
  5. Enter a password for the postgres user. Save this password for future use.
  6. Click the **Single zone** option for **Choose region and zonal availability**.
  7. Click and expand the **Show Configurations** section.
  8. Click and expand the **Machine Configuration** section: 
     1. In the **Machine** menu, select the machine series or type that you want to use, such as **N2**.
     2. Select the vCPU and RAM that you want to use, such as **2 vCPU, 16 GB**.
  9. Click **Create Instance** and wait until the instance initializes and starts.




### gcloud

####  Create an instance with a public IP address 

Before running the [`gcloud sql instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) command as follows, replace DB_ROOT_PASSWORD with the password of your database user.

Optionally, modify the values for the following parameters:

  * **\--database_version** : The database engine type and version. If left unspecified, the API default is used. See the [gcloud database versions](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create#--database-version) documentation to see the currently available versions.
  * **\--cpu** : The number of cores desired in the machine.
  * **\--memory** : Whole number value indicating how much memory is desired in the machine. A size unit should be provided (for example, 3072MB or 9GB). If no units are specified, GB is assumed.
  * **\--region** : Regional location of the instance (for example asia-east1, us-east1). If left unspecified, the default `us-central` is used. See the full list of [regions](https://docs.cloud.google.com/sql/docs/instance-locations).



Run the [`gcloud sql instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) command to create a Cloud SQL instance. 
    
    
    gcloud sql instances create quickstart-instance \
    --database-version=POSTGRES_13 \
    --cpu=1 \
    --memory=4GB \
    --region=us-central \
    --root-password=DB_ROOT_PASSWORD

#### Private IP

### Console

####  Create an instance with a private IP address and SSL enabled 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click **Create instance**.
  3. Click **PostgreSQL**.
  4. Enter `quickstart-instance` for **Instance ID**.
  5. Enter a password for the postgres user. Save this password for future use.
  6. Click the **Single zone** option for **Choose region and zonal availability**.
  7. Click and expand **Show configuration options**.
  8. Click and expand the **Machine Configuration** section: 
     1. In the **Machine** menu, select the machine series or type that you want to use, such as **N2**.
     2. Select the vCPU and RAM that you want to use, such as **2 vCPU, 16 GB**.
  9. In **Connections** , select **Private IP**.
  10. Select **default** in the **Network** drop-down menu.
  11. If you see a dialog stating **Private services access connection required** , click the **Set Up Connection** button.
     * In the **Enable Service Networking API** dialog, click the **Enable API** button.
     * In the **Allocate an IP range** dialog, select **Use an automatically allocated IP range** and click **Continue**.
     * In the **Create a connection** dialog, click **Create Connection**.
  12. Clear the **Public IP** checkbox to create an instance only with a private IP.
  13. Click **Create instance** and then wait for the instance to initialize and start.
  14. Click **Connections**.
  15. In the **Security** section, select **Allow only SSL connections** to enable SSL connections.
  16. In the **Allow only SSL connections** dialog, click **Save** and then wait for the instance to restart.



### gcloud

####  Create an instance with a private IP address and SSL enabled 

Creating an instance with a private IP address only requires configuring [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) to enable connections from other Google Cloud services, such as GKE. 

  1. Run the [`gcloud compute addresses create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create) command to allocate an IP range for a private services access connection:
    
    gcloud compute addresses create google-managed-services-default \
    --global \
    --purpose=VPC_PEERING \
    --prefix-length=16 \
    --description="peering range for Google" \
    --network=default

  2. Run the [`gcloud services vpc-peerings connect`](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/connect) command to create the private services access connection:
    
    gcloud services vpc-peerings connect \
    --service=servicenetworking.googleapis.com \
    --ranges=google-managed-services-default \
    --network=default

  3. Before running the [`gcloud sql instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) command to create an instance as follows, replace DB_ROOT_PASSWORD with the password of your database user.

Optionally, modify the values for the following parameters:

     * **\--database_version** : The database engine type and version. If left unspecified, the API default is used. See [gcloud database versions](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create#--database-version) for a list of currently available versions.
     * **\--cpu** : The number of cores in the machine.
     * **\--memory** : A whole number indicating how much memory to include in the machine. A size unit can be provided (for example, 3072MB or 9GB). If no units are specified, GB is assumed.
     * **\--region** : The regional location of the instance (for example asia-east1, us-east1). If left unspecified, the default `us-central1` is used. See the full list of [regions](https://docs.cloud.google.com/sql/docs/instance-locations).

Run the [`gcloud sql instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) command to create a Cloud SQL instance with a private IP address. 
    
    gcloud beta sql instances create quickstart-instance \
    --database-version=POSTGRES_13 \
     --cpu=1 \
     --memory=4GB \
     --region=us-central \
     --root-password=DB_ROOT_PASSWORD \
     --no-assign-ip \
    --network=default

  4. Run the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command to allow only SSL connections for the instance. 
    
    gcloud sql instances patch quickstart-instance --require-ssl




### Create a database

Take the following steps to create a database:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Select `quickstart-instance`.
  3. From the SQL navigation menu, select **Databases**.
  4. Click add_box **Create database**.
     1. In the **Database name** field of the **New database** dialog, enter `quickstart-db`.
     2. Click **Create**.



### gcloud

Run the [`gcloud sql databases create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/databases/create) command to create a database.
    
    
    gcloud sql databases create quickstart-db --instance=quickstart-instance

### Create a user

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Users** from the SQL navigation menu.
  4. Click **Add user account**. 
  5. In the **Add a user account to instance _instance_name_** page, add the following information: 
     * **Username** : Set to `quickstart-user`
     * **Password** : Specify a password for your database user. Make a note of this for use in a later step of this quickstart.
  6. Click **Add**.



### gcloud

Before running the command as follows, replace DB_PASS with a password for your database user. Make a note of this for use in a later step of this quickstart. 

Run the [`gcloud sql users create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/users/create) command to create the user.
    
    
    gcloud sql users create quickstart-user \
    --instance=quickstart-instance \
    --password=DB_PASS

Username length limits are the same for Cloud SQL as for on-premises PostgreSQL. 

## Create a GKE cluster

### Console

  1. In the Google Cloud console, go to the **Google Kubernetes Engine** page.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes)

  2. Click **Create**.
  3. Click **Configure** for GKE Autopilot.
  4. For **Name** , specify the cluster name as `gke-cloud-sql-quickstart`.
  5. Click **Create**.



### gcloud

Run the [`gcloud container clusters create-auto`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto) command to create the cluster.
    
    
    gcloud container clusters create-auto gke-cloud-sql-quickstart \
        --region us-central1

## Clone a Cloud SQL sample app from GitHub by using Cloud Shell

With a Cloud SQL instance, a database, and a GKE cluster, you can now clone and configure a sample application that connects to your Cloud SQL instance. The sample application is stored in GitHub. The remaining steps in this quickstart require using Cloud Shell, the `gcloud`, and [`kubectl`](https://kubernetes.io/docs/reference/kubectl/overview/). The `gcloud` and `kubectl` tools are pre-installed in Cloud Shell.

### Go

  1. In Cloud Shell Editor, open the sample app's source code.   
[Open Cloud Shell Editor](https://docs.cloud.google.com/console/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/golang-samples&working_dir=cloudsql/postgres/database-sql)
  2. In the `Open in Cloud Shell` dialog, click **Confirm** to download the sample app code and open the sample app directory in Cloud Shell Editor. 



### Java

  1. In Cloud Shell Editor, open the sample app's source code.   
[Open Cloud Shell Editor](https://docs.cloud.google.com/console/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/java-docs-samples&working_dir=cloud-sql/postgres/servlet)
  2. In the `Open in Cloud Shell` dialog, click **Confirm** to download the sample app code and open the sample app directory in Cloud Shell Editor. 



### Node.js

  1. In Cloud Shell Editor, open the sample app's source code.   
[Open Cloud Shell Editor](https://docs.cloud.google.com/console/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/nodejs-docs-samples&working_dir=cloud-sql/postgres/knex)
  2. In the `Open in Cloud Shell` dialog, click **Confirm** to download the sample app code and open the sample app directory in Cloud Shell Editor. 



### Python

  1. In Cloud Shell Editor, open the sample app's source code.   
[Open Cloud Shell Editor](https://docs.cloud.google.com/console/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/python-docs-samples&working_dir=cloud-sql/postgres/sqlalchemy)
  2. In the `Open in Cloud Shell` dialog, click **Confirm** to download the sample app code and open the sample app directory in Cloud Shell Editor. 



## Enable the GKE cluster

Enable the GKE cluster you just created as the default cluster to be used for the remaining commands in this quickstart.

Run the [`gcloud container clusters get-credentials`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/get-credentials) command as follows to enable the GKE cluster. 
    
    
    gcloud container clusters get-credentials gke-cloud-sql-quickstart \
      --region us-central1

## Set up a service account

Create and configure a Google Cloud service account to be used by GKE so that it has the **Cloud SQL Client** role with permissions to connect to Cloud SQL. 

  1. Run the [`gcloud iam service-accounts create`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/create) command as follows to create a new service account: 
         
         gcloud iam service-accounts create gke-quickstart-service-account \
           --display-name="GKE Quickstart Service Account"

  2. Run the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command as follows to add the **Cloud SQL Client** role to the Google Cloud service account you just created. Replace YOUR_PROJECT_ID with the project ID. 
         
         gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
           --member="serviceAccount:gke-quickstart-service-account@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/cloudsql.client"

  3. The sample app uses logging, so run the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command as follows to add the **Log Writer** role to the Google Cloud service account you just created. Replace YOUR_PROJECT_ID with the project ID. 
         
         gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
           --member="serviceAccount:gke-quickstart-service-account@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/logging.logWriter"

  4. The service account must be able to pull images from the artifactory repository, so run the   
[`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command as follows to add the **Artifact Registry Reader** role to the service account. Replace YOUR_PROJECT_ID with the project ID. 
         
         gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
           --member="serviceAccount:gke-quickstart-service-account@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/artifactregistry.reader"




Create a Kubernetes service account configured to have access to Cloud SQL by binding it to the Google Cloud service account using [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity). 

  1. Create a Kubernetes Service Account. 
     1. Update the [`service-account.yaml`](https://github.com/GoogleCloudPlatform/golang-samples/blob/main/cloudsql/postgres/database-sql/service-account.yaml) file in Cloud Shell Editor. Replace `<YOUR-KSA-NAME>` with `ksa-cloud-sql`.
     2. Run the [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply) command as follows in Cloud Shell: 
            
            kubectl apply -f service-account.yaml

  2. Run the [`gcloud iam service-accounts add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding) command as follows to enable IAM binding of the Google Cloud Service Account and the Kubernetes Service Account. Make the following replacements: 
     * YOUR_PROJECT_ID with the project ID.
     * YOUR_K8S_NAMESPACE with `default`, which is the default namespace for clusters created in GKE.
     * YOUR_KSA_NAME with `ksa-cloud-sql`.
    
    gcloud iam service-accounts add-iam-policy-binding \
      --role="roles/iam.workloadIdentityUser" \
      --member="serviceAccount:YOUR_PROJECT_ID.svc.id.goog[YOUR_K8S_NAMESPACE/YOUR_KSA_NAME]" \
      gke-quickstart-service-account@YOUR_PROJECT_ID.iam.gserviceaccount.com

  3. Run the [`kubectl annotate`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#annotate) command as follows to annotate the Kubernetes Service Account with IAM binding. Make the following replacements: 
     * YOUR_KSA_NAME with `ksa-cloud-sql`.
     * YOUR_PROJECT_ID with the project ID.
    
    kubectl annotate serviceaccount \
      YOUR_KSA_NAME  \
      iam.gke.io/gcp-service-account=gke-quickstart-service-account@YOUR_PROJECT_ID.iam.gserviceaccount.com




## Configure secrets

Run the [`kubectl create secret generic`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#-em-secret-generic-em-) command as follows to create Kubernetes secrets for the database, user, and user password to be used by the sample app. The values of each secret are based on the values specified in the previous steps of this quickstart. Replace DB_PASS with the password of the `quickstart-user` that you created in the previous **Create a user** quickstart step.
    
    
    kubectl create secret generic gke-cloud-sql-secrets \
      --from-literal=database=quickstart-db \
      --from-literal=username=quickstart-user \
      --from-literal=password=DB_PASS

## Build the sample app

### Go

  1. Return to the Cloud Shell Editor, and click **Open Terminal** to open a Cloud Shell prompt.
  2. At the Cloud Shell prompt, run the following [`gcloud artifacts repositories create`](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create) command to create a repository in the Artifact Registry named gke-cloud-sql-repo in the same region as your cluster. Replace YOUR_PROJECT_ID with the project ID. 
         
         gcloud artifacts repositories create gke-cloud-sql-repo \
           --project=YOUR_PROJECT_ID \
           --repository-format=docker \
           --location=us-central1 \
           --description="GKE Quickstart sample app"

  3. Change directories to the location where you previously cloned the Cloud SQL sample app from GitHub. The sample app directory contains a `Dockerfile` for the sample app. For example, to change directories to the directory of the sample app, you might run a command like the following: 
         
         cd ~/cloudshell_open/golang-samples/cloudsql/postgres/database-sql
           

  4. Run the [`gcloud builds submit`](https://docs.cloud.google.com/sdk/gcloud/reference/builds/submit) command as follows to build a Docker container and publish it to Artifact Registry. Replace YOUR_PROJECT_ID with the project ID. 
         
         gcloud builds submit \
           --tag us-central1-docker.pkg.dev/YOUR_PROJECT_ID/gke-cloud-sql-repo/gke-sql .




### Java

  1. Return to the Cloud Shell Editor, and click **Open Terminal** to open a Cloud Shell prompt.
  2. At the Cloud Shell prompt, run the following [`gcloud artifacts repositories create`](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create) command to create a repository in the Artifact Registry named gke-cloud-sql-repo in the same region as your cluster. Replace YOUR_PROJECT_ID with the project ID. 
         
         gcloud artifacts repositories create gke-cloud-sql-repo \
           --project=YOUR_PROJECT_ID \
           --repository-format=docker \
           --location=us-central1 \
           --description="GKE Quickstart sample app"

  3. Change directories to the location where you previously cloned the Cloud SQL sample app from GitHub. The sample app directory contains a `pom.xml` for the sample app. For example, to change directories to the directory of the sample app, you might run a command like the following: 
         
         cd ~/cloudshell_open/java-docs-samples/cloud-sql/postgres/servlet
           

  4. Run the `mvn` command as follows to build a Docker container and publish it to Artifact Registry. Replace YOUR_PROJECT_ID with the project ID. 
         
         mvn clean package com.google.cloud.tools:jib-maven-plugin:2.8.0:build \
           -Dimage=us-central1-docker.pkg.dev/YOUR_PROJECT_ID/gke-cloud-sql-repo/gke-sql \
           -DskipTests -Djib.to.credHelper=gcloud




### Node.js

  1. Return to the Cloud Shell Editor, and click **Open Terminal** to open a Cloud Shell prompt.
  2. At the Cloud Shell prompt, run the following [`gcloud artifacts repositories create`](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create) command to create a repository in the Artifact Registry named gke-cloud-sql-repo in the same region as your cluster. Replace YOUR_PROJECT_ID with the project ID. 
         
         gcloud artifacts repositories create gke-cloud-sql-repo \
           --project=YOUR_PROJECT_ID \
           --repository-format=docker \
           --location=us-central1 \
           --description="GKE Quickstart sample app"

  3. Change directories to the location where you previously cloned the Cloud SQL sample app from GitHub. The sample app directory contains a `Dockerfile` for the sample app. For example, to change directories to the directory of the sample app, you might run a command like the following: 
         
         cd ~/cloudshell_open/nodejs-docs-samples/cloud-sql/postgres/knex
           

  4. Run the [`gcloud builds submit`](https://docs.cloud.google.com/sdk/gcloud/reference/builds/submit) command as follows to build a Docker container and publish it to Artifact Registry. Replace YOUR_PROJECT_ID with the project ID. 
         
         gcloud builds submit \
           --tag us-central1-docker.pkg.dev/YOUR_PROJECT_ID/gke-cloud-sql-repo/gke-sql .




### Python

  1. Return to the Cloud Shell Editor, and click **Open Terminal** to open a Cloud Shell prompt.
  2. At the Cloud Shell prompt, run the following [`gcloud artifacts repositories create`](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create) command to create a repository in the Artifact Registry named gke-cloud-sql-repo in the same region as your cluster. Replace YOUR_PROJECT_ID with the project ID. 
         
         gcloud artifacts repositories create gke-cloud-sql-repo \
           --project=YOUR_PROJECT_ID \
           --repository-format=docker \
           --location=us-central1 \
           --description="GKE Quickstart sample app"

  3. Change directories to the location where you previously cloned the Cloud SQL sample app from GitHub. The sample app directory contains a `Dockerfile` for the sample app. For example, to change directories to the directory of the sample app, you might run a command like the following: 
         
         cd ~/cloudshell_open/python-docs-samples/cloud-sql/postgres/sqlalchemy
           

  4. Run the [`gcloud builds submit`](https://docs.cloud.google.com/sdk/gcloud/reference/builds/submit) command as follows to build a Docker container and publish it to Artifact Registry. Replace YOUR_PROJECT_ID with the project ID. 
         
         gcloud builds submit \
           --tag us-central1-docker.pkg.dev/YOUR_PROJECT_ID/gke-cloud-sql-repo/gke-sql .




## Deploy the sample app

#### Public IP

With the sample app configuration in place, you can now deploy the sample app. 

### Go

The deployed sample app connects to your Cloud SQL instance using the [Cloud SQL proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy) running in a Kubernetes sidecar pattern. The sidecar pattern is accomplished by deploying a [workload](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-workloads-overview) with an additional container that shares the same Kubernetes pod as the sample app's container. 

  1. Get the Cloud SQL instance connection name by running the [`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command: 
         
         gcloud sql instances describe quickstart-instance --format='value(connectionName)'

  2. Update the `deployment.yaml` file in Cloud Shell Editor. Make the following replacements: 
     * `<YOUR_KSA_NAME>` with `ksa-cloud-sql`.
     * `<LOCATION>` with `us-central1`.
     * `<YOUR_PROJECT_ID>` with the project ID.
     * `<YOUR-DB-SECRET>` with `gke-cloud-sql-secrets`.
     * `<INSTANCE_CONNECTION_NAME>` with the Cloud SQL instance connection name retrieved from the `gcloud` command on the previous step. The format is **project_id:region:instance_name**. The instance connection name is also visible in the Cloud SQL instance **Overview** page. 
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: gke-cloud-sql-quickstart
    spec:
      selector:
        matchLabels:
          app: gke-cloud-sql-app
      template:
        metadata:
          labels:
            app: gke-cloud-sql-app
        spec:
          serviceAccountName: <YOUR-KSA-NAME>
          containers:
          - name: gke-cloud-sql-app
            # Replace <LOCATION> with your Artifact Registry location (e.g., us-central1).
            # Replace <YOUR_PROJECT_ID> with your project ID.
            image: <LOCATION>-docker.pkg.dev/<YOUR_PROJECT_ID>/gke-cloud-sql-repo/gke-sql:latest
            # This app listens on port 8080 for web traffic by default.
            ports:
            - containerPort: 8080
            env:
            - name: PORT
              value: "8080"
            # This project uses environment variables to determine
            # how you would like to run your application
            # To use the Go Connector (recommended) - use INSTANCE_CONNECTION_NAME (proj:region:instance)
            # To use TCP - Setting INSTANCE_HOST will use TCP (e.g., 127.0.0.1)
            # To use Unix, use INSTANCE_UNIX_SOCKET (e.g., /cloudsql/proj:region:instance)
            - name: INSTANCE_HOST
              value: "127.0.0.1"
            - name: DB_PORT
              value: "5432"
            # For Automatic IAM Authentication with the Go Connector
            # use DB_IAM_USER instead of DB_USER (recommended)
            # You may also remove the DB_PASS environment variable if
            # you use Automatic IAM Authentication
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
          # If you are using the Go Connector (recommended), you can
          # remove cloud-sql-proxy (everything below this line)
          - name: cloud-sql-proxy
            # This uses the latest version of the Cloud SQL Proxy
            # It is recommended to use a specific version for production environments.
            # See: https://github.com/GoogleCloudPlatform/cloudsql-proxy
            image: gcr.io/cloud-sql-connectors/cloud-sql-proxy:latest
            args:
              # If connecting from a VPC-native GKE cluster, you can use the
              # following flag to have the proxy connect over private IP
              # - "--private-ip"
    
              # If you are not connecting with Automatic IAM, you can delete
              # the following flag.
              - "--auto-iam-authn"
    
              # tcp should be set to the port the proxy should listen on
              # and should match the DB_PORT value set above.
              # Defaults: MySQL: 3306, Postgres: 5432, SQLServer: 1433
              - "--port=5432"
              - "<INSTANCE_CONNECTION_NAME>"
            securityContext:
              # The default Cloud SQL proxy image runs as the
              # "nonroot" user and group (uid: 65532) by default.
              runAsNonRoot: true
    

  3. Run the [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply) command as follows in Cloud Shell to deploy the sample app: 
         
         kubectl apply -f deployment.yaml

  4. Run the [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply) command as follows to add a load balancer in front of the deployment, so that you can access it through the internet: 
         
         kubectl apply -f service.yaml

  5. Run the [`kubectl get`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get) command as follows to get the service details: 
         
         kubectl get services

  6. Copy the **External IP** address once it becomes available in the service details, which may take a few minutes.
  7. View the deployed sample app. Open a browser window and go to the service's **External IP** address. 

![View deployed sample app](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)




### Java

The deployed sample app connects to your Cloud SQL instance using the [Cloud SQL Java connector](https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory). 

  1. Get the Cloud SQL instance connection name by running the [`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command: 
         
         gcloud sql instances describe quickstart-instance --format='value(connectionName)'

  2. Update the `deployment.yaml` file in Cloud Shell Editor. Make the following replacements: 
     * `<YOUR_KSA_NAME>` with `ksa-cloud-sql`.
     * `<LOCATION>` with `us-central1`.
     * `<YOUR_PROJECT_ID>` with the project ID.
     * `<YOUR-DB-SECRET>` with `gke-cloud-sql-secrets`.
     * `<INSTANCE_CONNECTION_NAME>` with the Cloud SQL instance connection name retrieved from the `gcloud` command on the previous step. The format is **project_id:region:instance_name**. The instance connection name is also visible in the Cloud SQL instance **Overview** page. 
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: gke-cloud-sql-quickstart
    spec:
      selector:
        matchLabels:
          app: gke-cloud-sql-app
      template:
        metadata:
          labels:
            app: gke-cloud-sql-app
        spec:
          # For more information about using Kubernetes service accounts see: 
          # https://cloud.google.com/kubernetes-engine/docs/how-to/kubernetes-service-accounts
          serviceAccountName: <YOUR-KSA-NAME> # TODO(developer): replace this value.
          containers:
          - name: gke-cloud-sql-app
            # Replace <LOCATION> with your Artifact Registry location (e.g., us-central1).
            # Replace <YOUR_PROJECT_ID> with your project ID.
            image: <LOCATION>-docker.pkg.dev/<YOUR_PROJECT_ID>/gke-cloud-sql-repo/gke-sql:latest
            # This app listens on port 8080 for web traffic by default.
            ports:
            - containerPort: 8080
            env:
            - name: PORT
              value: "8080"
            - name: INSTANCE_CONNECTION_NAME
              value: <INSTANCE_CONNECTION_NAME>
            - name: DB_HOST
              value: "127.0.0.1"
            - name: DB_PORT
              value: "5432"  
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
    

  3. Run the [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply) command as follows in Cloud Shell to deploy the sample app: 
         
         kubectl apply -f deployment.yaml

  4. Run the [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply) command as follows to add a load balancer in front of the deployment, so that you can access it through the internet: 
         
         kubectl apply -f service.yaml

  5. Run the [`kubectl get`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get) command as follows to get the service details: 
         
         kubectl get services

  6. Copy the **External IP** address once it becomes available in the service details, which may take a few minutes.
  7. View the deployed sample app. Open a browser window and go to the service's **External IP** address. 

![View deployed sample app](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)




### Node.js

The deployed sample app connects to your Cloud SQL instance using the [Cloud SQL proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy) running in a Kubernetes sidecar pattern. The sidecar pattern is accomplished by deploying a [workload](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-workloads-overview) with an additional container that shares the same Kubernetes pod as the sample app's container. 

  1. Get the Cloud SQL instance connection name by running the [`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command: 
         
         gcloud sql instances describe quickstart-instance --format='value(connectionName)'

  2. Update the `deployment.yaml` file in Cloud Shell Editor. Make the following replacements: 
     * `<YOUR_KSA_NAME>` with `ksa-cloud-sql`.
     * `<LOCATION>` with `us-central1`.
     * `<YOUR_PROJECT_ID>` with the project ID.
     * `<YOUR-DB-SECRET>` with `gke-cloud-sql-secrets`.
     * `<INSTANCE_CONNECTION_NAME>` with the Cloud SQL instance connection name retrieved from the `gcloud` command on the previous step. The format is **project_id:region:instance_name**. The instance connection name is also visible in the Cloud SQL instance **Overview** page. 
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: gke-cloud-sql-quickstart
    spec:
      selector:
        matchLabels:
          app: gke-cloud-sql-app
      template:
        metadata:
          labels:
            app: gke-cloud-sql-app
        spec:
          serviceAccountName: <YOUR-KSA-NAME>
          containers:
          - name: gke-cloud-sql-app
            # Replace <LOCATION> with your Artifact Registry location (e.g., us-central1).
            # Replace <YOUR_PROJECT_ID> with your project ID.
            image: <LOCATION>-docker.pkg.dev/<YOUR_PROJECT_ID>/gke-cloud-sql-repo/gke-sql:latest
            # This app listens on port 8080 for web traffic by default.
            ports:
            - containerPort: 8080
            env:
            - name: PORT
              value: "8080"
            # This project uses environment variables to determine
            # how you would like to run your application
            # To use the Node.js connector (recommended) - use INSTANCE_CONNECTION_NAME (proj:region:instance)
            # To use TCP - Setting INSTANCE_HOST will use TCP (e.g., 127.0.0.1)
            # To use Unix, use INSTANCE_UNIX_SOCKET (e.g., /cloudsql/proj:region:instance)
            - name: INSTANCE_HOST
              value: "127.0.0.1"
            - name: DB_PORT
              value: "5432"
            # For Automatic IAM Authentication with the Node.js Connector
            # use DB_IAM_USER instead of DB_USER (recommended)
            # You may also remove the DB_PASS environment variable if
            # you use Automatic IAM Authentication
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
          # If you are using the Node.js Connector (recommended), you can
          # remove cloud-sql-proxy (everything below this line)
          - name: cloud-sql-proxy
            # This uses the latest version of the Cloud SQL proxy
            # It is recommended to use a specific version for production environments.
            # See: https://github.com/GoogleCloudPlatform/cloudsql-proxy 
            image: gcr.io/cloud-sql-connectors/cloud-sql-proxy:latest
            args:
              # If connecting from a VPC-native GKE cluster, you can use the
              # following flag to have the proxy connect over private IP
              # - "--private-ip"
    
              # If you are not connecting with Automatic IAM, you can delete
              # the following flag.
              - "--auto-iam-authn"
    
              # tcp should be set to the port the proxy should listen on
              # and should match the DB_PORT value set above.
              # Defaults: MySQL: 3306, Postgres: 5432, SQLServer: 1433
              - "--port=5432"
              - "<INSTANCE_CONNECTION_NAME>"
            securityContext:
              # The default Cloud SQL proxy image runs as the
              # "nonroot" user and group (uid: 65532) by default.
              runAsNonRoot: true
    

  3. Run the [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply) command as follows in Cloud Shell to deploy the sample app: 
         
         kubectl apply -f deployment.yaml

  4. Run the [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply) command as follows to add a load balancer in front of the deployment, so that you can access it through the internet: 
         
         kubectl apply -f service.yaml

  5. Run the [`kubectl get`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get) command as follows to get the service details: 
         
         kubectl get services

  6. Copy the **External IP** address once it becomes available in the service details, which may take a few minutes.
  7. View the deployed sample app. Open a browser window and go to the service's **External IP** address. 

![View deployed sample app](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)




### Python

The deployed sample app connects to your Cloud SQL instance using the [Cloud SQL proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy) running in a Kubernetes sidecar pattern. The sidecar pattern is accomplished by deploying a [workload](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-workloads-overview) with an additional container that shares the same Kubernetes pod as the sample app's container. 

  1. Get the Cloud SQL instance connection name by running the [`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command: 
         
         gcloud sql instances describe quickstart-instance --format='value(connectionName)'

  2. Update the `deployment.yaml` file in Cloud Shell Editor. Make the following replacements: 
     * `<YOUR_KSA_NAME>` with `ksa-cloud-sql`.
     * `<LOCATION>` with `us-central1`.
     * `<YOUR_PROJECT_ID>` with the project ID.
     * `<YOUR-DB-SECRET>` with `gke-cloud-sql-secrets`.
     * `<INSTANCE_CONNECTION_NAME>` with the Cloud SQL instance connection name retrieved from the `gcloud` command on the previous step. The format is **project_id:region:instance_name**. The instance connection name is also visible in the Cloud SQL instance **Overview** page. 
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: gke-cloud-sql-quickstart
    spec:
      selector:
        matchLabels:
          app: gke-cloud-sql-app
      template:
        metadata:
          labels:
            app: gke-cloud-sql-app
        spec:
          serviceAccountName: <YOUR-KSA-NAME>
          containers:
          - name: gke-cloud-sql-app
            # Replace <LOCATION> with your Artifact Registry location (e.g., us-central1).
            # Replace <YOUR_PROJECT_ID> with your project ID.
            image: <LOCATION>-docker.pkg.dev/<YOUR_PROJECT_ID>/gke-cloud-sql-repo/gke-sql:latest
            # This app listens on port 8080 for web traffic by default.
            ports:
            - containerPort: 8080
            env:
            - name: PORT
              value: "8080"
            # This project uses environment variables to determine
            # how you would like to run your application
            # To use the Python Connector (recommended) - use INSTANCE_CONNECTION_NAME (proj:region:instance)
            # To use TCP - Setting INSTANCE_HOST will use TCP (e.g., 127.0.0.1)
            # To use Unix, use INSTANCE_UNIX_SOCKET (e.g., /cloudsql/proj:region:instance)
            - name: INSTANCE_HOST
              value: "127.0.0.1"
            - name: DB_PORT
              value: "5432"
            # For Automatic IAM Authentication with the Python Connector
            # use DB_IAM_USER instead of DB_USER (recommended)
            # You may also remove the DB_PASS environment variable if
            # you use Automatic IAM Authentication
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
          # If you are using the Python Connector (recommended), you can
          # remove cloud-sql-proxy (everything below this line)
          - name: cloud-sql-proxy
            # This uses the latest version of the Cloud SQL proxy
            # It is recommended to use a specific version for production environments.
            # See: https://github.com/GoogleCloudPlatform/cloudsql-proxy 
            image: gcr.io/cloud-sql-connectors/cloud-sql-proxy:latest
            args:
              # If connecting from a VPC-native GKE cluster, you can use the
              # following flag to have the proxy connect over private IP
              # - "--private-ip"
    
              # If you are not connecting with Automatic IAM, you can delete
              # the following flag.
              - "--auto-iam-authn"
    
              # tcp should be set to the port the proxy should listen on
              # and should match the DB_PORT value set above.
              # Defaults: MySQL: 3306, Postgres: 5432, SQLServer: 1433
              - "--port=5432"
              - "<INSTANCE_CONNECTION_NAME>"
            securityContext:
              # The default Cloud SQL proxy image runs as the
              # "nonroot" user and group (uid: 65532) by default.
              runAsNonRoot: true
    

  3. Run the [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply) command as follows in Cloud Shell to deploy the sample app: 
         
         kubectl apply -f deployment.yaml

  4. Run the [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply) command as follows to add a load balancer in front of the deployment, so that you can access it through the internet: 
         
         kubectl apply -f service.yaml

  5. Run the [`kubectl get`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get) command as follows to get the service details: 
         
         kubectl get services

  6. Copy the **External IP** address once it becomes available in the service details, which may take a few minutes.
  7. View the deployed sample app. Open a browser window and go to the service's **External IP** address. 

![View deployed sample app](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)




#### Private IP

With the sample app configuration in place, you can now deploy the sample app. 

### Go

The deployed sample app connects to your Cloud SQL instance using the [Cloud SQL proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy) running in a Kubernetes sidecar pattern. The sidecar pattern is accomplished by deploying a [workload](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-workloads-overview) with an additional container that shares the same Kubernetes pod as the sample app's container. 

  1. Get the Cloud SQL instance connection name by running the [`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command: 
         
         gcloud sql instances describe quickstart-instance --format='value(connectionName)'

  2. Update the `deployment.yaml` file in Cloud Shell Editor. Make the following replacements and edits: 
     * Replace `<YOUR_KSA_NAME>` with `ksa-cloud-sql`.
     * Replace `<LOCATION>` with `us-central1`.
     * Replace `<YOUR_PROJECT_ID>` with the project ID.
     * Replace `<YOUR-DB-SECRET>` with `gke-cloud-sql-secrets`.
     * Replace `<INSTANCE_CONNECTION_NAME>` with the Cloud SQL instance connection name retrieved from the `gcloud` command on the previous step. The format is **project_id:region:instance_name**. The instance connection name is also visible in the Cloud SQL instance **Overview** page. 
     * Enable the Cloud SQL Auth proxy to connect to your Cloud SQL instance using its private IP address. Uncomment the `"--private-ip"` flag by removing the `#` comment symbol and its trailing whitespace. The uncommented flag should look like this: 
           
           - "--private-ip"
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: gke-cloud-sql-quickstart
    spec:
      selector:
        matchLabels:
          app: gke-cloud-sql-app
      template:
        metadata:
          labels:
            app: gke-cloud-sql-app
        spec:
          serviceAccountName: <YOUR-KSA-NAME>
          containers:
          - name: gke-cloud-sql-app
            # Replace <LOCATION> with your Artifact Registry location (e.g., us-central1).
            # Replace <YOUR_PROJECT_ID> with your project ID.
            image: <LOCATION>-docker.pkg.dev/<YOUR_PROJECT_ID>/gke-cloud-sql-repo/gke-sql:latest
            # This app listens on port 8080 for web traffic by default.
            ports:
            - containerPort: 8080
            env:
            - name: PORT
              value: "8080"
            # This project uses environment variables to determine
            # how you would like to run your application
            # To use the Go Connector (recommended) - use INSTANCE_CONNECTION_NAME (proj:region:instance)
            # To use TCP - Setting INSTANCE_HOST will use TCP (e.g., 127.0.0.1)
            # To use Unix, use INSTANCE_UNIX_SOCKET (e.g., /cloudsql/proj:region:instance)
            - name: INSTANCE_HOST
              value: "127.0.0.1"
            - name: DB_PORT
              value: "5432"
            # For Automatic IAM Authentication with the Go Connector
            # use DB_IAM_USER instead of DB_USER (recommended)
            # You may also remove the DB_PASS environment variable if
            # you use Automatic IAM Authentication
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
          # If you are using the Go Connector (recommended), you can
          # remove cloud-sql-proxy (everything below this line)
          - name: cloud-sql-proxy
            # This uses the latest version of the Cloud SQL Proxy
            # It is recommended to use a specific version for production environments.
            # See: https://github.com/GoogleCloudPlatform/cloudsql-proxy
            image: gcr.io/cloud-sql-connectors/cloud-sql-proxy:latest
            args:
              # If connecting from a VPC-native GKE cluster, you can use the
              # following flag to have the proxy connect over private IP
              # - "--private-ip"
    
              # If you are not connecting with Automatic IAM, you can delete
              # the following flag.
              - "--auto-iam-authn"
    
              # tcp should be set to the port the proxy should listen on
              # and should match the DB_PORT value set above.
              # Defaults: MySQL: 3306, Postgres: 5432, SQLServer: 1433
              - "--port=5432"
              - "<INSTANCE_CONNECTION_NAME>"
            securityContext:
              # The default Cloud SQL proxy image runs as the
              # "nonroot" user and group (uid: 65532) by default.
              runAsNonRoot: true
    

  3. Run the [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply) command as follows in Cloud Shell to deploy the sample app: 
         
         kubectl apply -f deployment.yaml

  4. Run the [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply) command as follows to add a load balancer in front of the deployment, so that you can access it through the internet: 
         
         kubectl apply -f service.yaml

  5. Run the [`kubectl get`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get) command as follows to get the service details: 
         
         kubectl get services

  6. Copy the **External IP** address once it becomes available in the service details, which may take a few minutes.
  7. View the deployed sample app. Open a browser window and go to the service's **External IP** address. 

![View deployed sample app](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)




### Java

The deployed sample app connects to your Cloud SQL instance using the [Cloud SQL Java connector](https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory). 

  1. Get the Cloud SQL instance connection name by running the [`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command: 
         
         gcloud sql instances describe quickstart-instance --format='value(connectionName)'

  2. Update the `deployment.yaml` file in Cloud Shell Editor. Make the following replacements: 
     * `<YOUR_KSA_NAME>` with `ksa-cloud-sql`.
     * `<LOCATION>` with `us-central1`.
     * `<YOUR_PROJECT_ID>` with the project ID.
     * `<YOUR-DB-SECRET>` with `gke-cloud-sql-secrets`.
     * `<INSTANCE_CONNECTION_NAME>` with the Cloud SQL instance connection name retrieved from the `gcloud` command on the previous step. The format is **project_id:region:instance_name**. The instance connection name is also visible in the Cloud SQL instance **Overview** page. 
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: gke-cloud-sql-quickstart
    spec:
      selector:
        matchLabels:
          app: gke-cloud-sql-app
      template:
        metadata:
          labels:
            app: gke-cloud-sql-app
        spec:
          # For more information about using Kubernetes service accounts see: 
          # https://cloud.google.com/kubernetes-engine/docs/how-to/kubernetes-service-accounts
          serviceAccountName: <YOUR-KSA-NAME> # TODO(developer): replace this value.
          containers:
          - name: gke-cloud-sql-app
            # Replace <LOCATION> with your Artifact Registry location (e.g., us-central1).
            # Replace <YOUR_PROJECT_ID> with your project ID.
            image: <LOCATION>-docker.pkg.dev/<YOUR_PROJECT_ID>/gke-cloud-sql-repo/gke-sql:latest
            # This app listens on port 8080 for web traffic by default.
            ports:
            - containerPort: 8080
            env:
            - name: PORT
              value: "8080"
            - name: INSTANCE_CONNECTION_NAME
              value: <INSTANCE_CONNECTION_NAME>
            - name: DB_HOST
              value: "127.0.0.1"
            - name: DB_PORT
              value: "5432"  
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
    

  3. Run the [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply) command as follows in Cloud Shell to deploy the sample app: 
         
         kubectl apply -f deployment.yaml

  4. Run the [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply) command as follows to add a load balancer in front of the deployment, so that you can access it through the internet: 
         
         kubectl apply -f service.yaml

  5. Run the [`kubectl get`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get) command as follows to get the service details: 
         
         kubectl get services

  6. Copy the **External IP** address once it becomes available in the service details, which may take a few minutes.
  7. View the deployed sample app. Open a browser window and go to the service's **External IP** address. 

![View deployed sample app](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)




### Node.js

The deployed sample app connects to your Cloud SQL instance using the [Cloud SQL proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy) running in a Kubernetes sidecar pattern. The sidecar pattern is accomplished by deploying a [workload](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-workloads-overview) with an additional container that shares the same Kubernetes pod as the sample app's container. 

  1. Get the Cloud SQL instance connection name by running the [`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command: 
         
         gcloud sql instances describe quickstart-instance --format='value(connectionName)'

  2. Update the `deployment.yaml` file in Cloud Shell Editor. Make the following replacements and edits: 
     * Replace `<YOUR_KSA_NAME>` with `ksa-cloud-sql`.
     * Replace `<LOCATION>` with `us-central1`.
     * Replace `<YOUR_PROJECT_ID>` with the project ID.
     * Replace `<YOUR-DB-SECRET>` with `gke-cloud-sql-secrets`.
     * Replace `<INSTANCE_CONNECTION_NAME>` with the Cloud SQL instance connection name retrieved from the `gcloud` command on the previous step. The format is **project_id:region:instance_name**. The instance connection name is also visible in the Cloud SQL instance **Overview** page. 
     * Enable the Cloud SQL Auth proxy to connect to your Cloud SQL instance using its private IP address. Uncomment the `"--private-ip"` flag by removing the `#` comment symbol and its trailing whitespace. The uncommented flag should look like this: 
           
           - "--private-ip"
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: gke-cloud-sql-quickstart
    spec:
      selector:
        matchLabels:
          app: gke-cloud-sql-app
      template:
        metadata:
          labels:
            app: gke-cloud-sql-app
        spec:
          serviceAccountName: <YOUR-KSA-NAME>
          containers:
          - name: gke-cloud-sql-app
            # Replace <LOCATION> with your Artifact Registry location (e.g., us-central1).
            # Replace <YOUR_PROJECT_ID> with your project ID.
            image: <LOCATION>-docker.pkg.dev/<YOUR_PROJECT_ID>/gke-cloud-sql-repo/gke-sql:latest
            # This app listens on port 8080 for web traffic by default.
            ports:
            - containerPort: 8080
            env:
            - name: PORT
              value: "8080"
            # This project uses environment variables to determine
            # how you would like to run your application
            # To use the Node.js connector (recommended) - use INSTANCE_CONNECTION_NAME (proj:region:instance)
            # To use TCP - Setting INSTANCE_HOST will use TCP (e.g., 127.0.0.1)
            # To use Unix, use INSTANCE_UNIX_SOCKET (e.g., /cloudsql/proj:region:instance)
            - name: INSTANCE_HOST
              value: "127.0.0.1"
            - name: DB_PORT
              value: "5432"
            # For Automatic IAM Authentication with the Node.js Connector
            # use DB_IAM_USER instead of DB_USER (recommended)
            # You may also remove the DB_PASS environment variable if
            # you use Automatic IAM Authentication
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
          # If you are using the Node.js Connector (recommended), you can
          # remove cloud-sql-proxy (everything below this line)
          - name: cloud-sql-proxy
            # This uses the latest version of the Cloud SQL proxy
            # It is recommended to use a specific version for production environments.
            # See: https://github.com/GoogleCloudPlatform/cloudsql-proxy 
            image: gcr.io/cloud-sql-connectors/cloud-sql-proxy:latest
            args:
              # If connecting from a VPC-native GKE cluster, you can use the
              # following flag to have the proxy connect over private IP
              # - "--private-ip"
    
              # If you are not connecting with Automatic IAM, you can delete
              # the following flag.
              - "--auto-iam-authn"
    
              # tcp should be set to the port the proxy should listen on
              # and should match the DB_PORT value set above.
              # Defaults: MySQL: 3306, Postgres: 5432, SQLServer: 1433
              - "--port=5432"
              - "<INSTANCE_CONNECTION_NAME>"
            securityContext:
              # The default Cloud SQL proxy image runs as the
              # "nonroot" user and group (uid: 65532) by default.
              runAsNonRoot: true
    

  3. Run the [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply) command as follows in Cloud Shell to deploy the sample app: 
         
         kubectl apply -f deployment.yaml

  4. Run the [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply) command as follows to add a load balancer in front of the deployment, so that you can access it through the internet: 
         
         kubectl apply -f service.yaml

  5. Run the [`kubectl get`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get) command as follows to get the service details: 
         
         kubectl get services

  6. Copy the **External IP** address once it becomes available in the service details, which may take a few minutes.
  7. View the deployed sample app. Open a browser window and go to the service's **External IP** address. 

![View deployed sample app](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)




### Python

The deployed sample app connects to your Cloud SQL instance using the [Cloud SQL proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy) running in a Kubernetes sidecar pattern. The sidecar pattern is accomplished by deploying a [workload](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-workloads-overview) with an additional container that shares the same Kubernetes pod as the sample app's container. 

  1. Get the Cloud SQL instance connection name by running the [`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command: 
         
         gcloud sql instances describe quickstart-instance --format='value(connectionName)'

  2. Update the `deployment.yaml` file in Cloud Shell Editor. Make the following replacements and edits: 
     * Replace `<YOUR_KSA_NAME>` with `ksa-cloud-sql`.
     * Replace `<LOCATION>` with `us-central1`.
     * Replace `<YOUR_PROJECT_ID>` with the project ID.
     * Replace `<YOUR-DB-SECRET>` with `gke-cloud-sql-secrets`.
     * Replace `<INSTANCE_CONNECTION_NAME>` with the Cloud SQL instance connection name retrieved from the `gcloud` command on the previous step. The format is **project_id:region:instance_name**. The instance connection name is also visible in the Cloud SQL instance **Overview** page. 
     * Enable the Cloud SQL Auth proxy to connect to your Cloud SQL instance using its private IP address. Uncomment the `"--private-ip"` flag by removing the `#` comment symbol and its trailing whitespace. The uncommented flag should look like this: 
           
           - "--private-ip"
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: gke-cloud-sql-quickstart
    spec:
      selector:
        matchLabels:
          app: gke-cloud-sql-app
      template:
        metadata:
          labels:
            app: gke-cloud-sql-app
        spec:
          serviceAccountName: <YOUR-KSA-NAME>
          containers:
          - name: gke-cloud-sql-app
            # Replace <LOCATION> with your Artifact Registry location (e.g., us-central1).
            # Replace <YOUR_PROJECT_ID> with your project ID.
            image: <LOCATION>-docker.pkg.dev/<YOUR_PROJECT_ID>/gke-cloud-sql-repo/gke-sql:latest
            # This app listens on port 8080 for web traffic by default.
            ports:
            - containerPort: 8080
            env:
            - name: PORT
              value: "8080"
            # This project uses environment variables to determine
            # how you would like to run your application
            # To use the Python Connector (recommended) - use INSTANCE_CONNECTION_NAME (proj:region:instance)
            # To use TCP - Setting INSTANCE_HOST will use TCP (e.g., 127.0.0.1)
            # To use Unix, use INSTANCE_UNIX_SOCKET (e.g., /cloudsql/proj:region:instance)
            - name: INSTANCE_HOST
              value: "127.0.0.1"
            - name: DB_PORT
              value: "5432"
            # For Automatic IAM Authentication with the Python Connector
            # use DB_IAM_USER instead of DB_USER (recommended)
            # You may also remove the DB_PASS environment variable if
            # you use Automatic IAM Authentication
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
          # If you are using the Python Connector (recommended), you can
          # remove cloud-sql-proxy (everything below this line)
          - name: cloud-sql-proxy
            # This uses the latest version of the Cloud SQL proxy
            # It is recommended to use a specific version for production environments.
            # See: https://github.com/GoogleCloudPlatform/cloudsql-proxy 
            image: gcr.io/cloud-sql-connectors/cloud-sql-proxy:latest
            args:
              # If connecting from a VPC-native GKE cluster, you can use the
              # following flag to have the proxy connect over private IP
              # - "--private-ip"
    
              # If you are not connecting with Automatic IAM, you can delete
              # the following flag.
              - "--auto-iam-authn"
    
              # tcp should be set to the port the proxy should listen on
              # and should match the DB_PORT value set above.
              # Defaults: MySQL: 3306, Postgres: 5432, SQLServer: 1433
              - "--port=5432"
              - "<INSTANCE_CONNECTION_NAME>"
            securityContext:
              # The default Cloud SQL proxy image runs as the
              # "nonroot" user and group (uid: 65532) by default.
              runAsNonRoot: true
    

  3. Run the [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply) command as follows in Cloud Shell to deploy the sample app: 
         
         kubectl apply -f deployment.yaml

  4. Run the [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply) command as follows to add a load balancer in front of the deployment, so that you can access it through the internet: 
         
         kubectl apply -f service.yaml

  5. Run the [`kubectl get`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get) command as follows to get the service details: 
         
         kubectl get services

  6. Copy the **External IP** address once it becomes available in the service details, which may take a few minutes.
  7. View the deployed sample app. Open a browser window and go to the service's **External IP** address. 

![View deployed sample app](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Select the `quickstart-instance` instance to open the **Instance details** page.
  3. In the icon bar at the top of the page, click **Delete**.
  4. In the **Delete instance** dialog box, type `quickstart-instance`, and then click **Delete** to delete the instance.
  5. In the Google Cloud console, go to the **Google Kubernetes Engine** page.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes)

  6. Click the checkbox next to the `gke-cloud-sql-quickstart` service name.
  7. Click the **Delete** button at the top of the Google Kubernetes Engine page.



### Optional cleanup steps

If you're not using the Google Cloud service account you created for this quickstart, you can remove it.

  1. In the Google Cloud console, go to the **Service accounts** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Select the checkbox for the IAM account named `gke-quickstart-service-account`.
  3. Click **Remove** and confirm the removal.



If you're not using the APIs that were enabled as part of this quickstart, you can disable them.

  * APIs that were enabled within this quickstart: 
    * Compute Engine API
    * Cloud SQL Admin API
    * Google Kubernetes Engine API
    * Artifact Registry API
    * Cloud Build API


  1. In the Google Cloud console, go to the **APIs** page.

[Go to APIs](https://console.cloud.google.com/apis)

  2. Select any API that you would like to disable and then click the **Disable API** button.




## What's next

Based on your needs, you can learn more about [creating Cloud SQL instances](https://docs.cloud.google.com/sql/docs/postgres/create-instance). 

You also can learn about creating [PostgreSQL users](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users) and [databases](https://docs.cloud.google.com/sql/docs/postgres/create-manage-databases) for your Cloud SQL instance.

Also see the [Cloud SQL pricing information](https://cloud.google.com/sql/pricing).

Learn more about:

  * All of the [connectivity options](https://docs.cloud.google.com/sql/docs/postgres/connect-overview#connection_options) in Cloud SQL.
  * Configuring your Cloud SQL instance with a [public IP](https://docs.cloud.google.com/sql/docs/postgres/configure-ip) address.
  * Configuring your Cloud SQL instance with a [private IP](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip) address.



Additionally, you can learn about connecting to a Cloud SQL instance from other Google Cloud applications:

  * [From an application running on App Engine standard environment](https://docs.cloud.google.com/sql/docs/postgres/connect-app-engine)
  * [From an application running on Compute Engine](https://docs.cloud.google.com/sql/docs/postgres/connect-compute-engine)
  * [From an application running on GKE](https://docs.cloud.google.com/sql/docs/postgres/connect-kubernetes-engine)
  * [From Cloud Run](https://docs.cloud.google.com/sql/docs/postgres/connect-run)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
