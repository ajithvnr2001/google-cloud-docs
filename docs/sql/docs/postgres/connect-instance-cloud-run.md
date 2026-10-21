---
url: https://docs.cloud.google.com/sql/docs/postgres/connect-instance-cloud-run/
title: Quickstart: Connect to Cloud SQL for PostgreSQL from Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:40.909889+00:00
---

# Quickstart: Connect to Cloud SQL for PostgreSQL from Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/connect-instance-cloud-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connect to Cloud SQL for PostgreSQL from Cloud Run

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/connect-instance-cloud-run "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/connect-instance-cloud-run "View this page for the SQL Server database engine")

Learn how to deploy a sample app on [Cloud Run](https://docs.cloud.google.com/run/docs) connected to a PostgreSQL instance by using the Google Cloud console and a client application.

Assuming that you complete all the steps in a timely manner, the resources created in this quickstart typically cost less than one dollar (USD).

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?walkthrough_id=sql--postgres--quickstart-cloud-run)

* * *

## Before you begin

**Note:** The name you use for your project must be between 4 and 30 characters. When you type the name, the form suggests a project ID, which you can edit. The project ID must be between 6 and 30 characters, with a lowercase letter as the first character. You can use a dash, lowercase letter, or digit for the remaining characters, but the last character cannot be a dash. 

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

  6. Verify that you have the permissions required to complete this quickstart.
  7. Enable the Cloud APIs necessary to run a Cloud SQL sample app on Cloud Run. 

### Console

Click **Enable APIs** to enable the APIs required for this quickstart.

[Enable APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,sqladmin.googleapis.com,run.googleapis.com,containerregistry.googleapis.com,cloudbuild.googleapis.com,servicenetworking.googleapis.com)

This enables the following APIs:

     * Compute Engine API
     * Cloud SQL Admin API
     * Cloud Run API
     * Container Registry API
     * Cloud Build API
     * Service Networking API

### gcloud

Click the following button to open Cloud Shell, which provides command-line access to your Google Cloud resources directly from the browser. Cloud Shell can be used to run the `gcloud` commands presented throughout this quickstart.

[Open Cloud Shell](https://docs.cloud.google.com/console/sql/instances?cloudshell=true)

Run the following `gcloud` command using Cloud Shell:
    
    gcloud services enable compute.googleapis.com sqladmin.googleapis.com run.googleapis.com \
    artifactregistry.googleapis.com cloudbuild.googleapis.com servicenetworking.googleapis.com

This command enables the following APIs:

     * Compute Engine API
     * Cloud SQL Admin API
     * Cloud Run API
     * Artifact Registry API
     * Cloud Build API
     * Service Networking API




### Required roles

To get the permissions that you need to deploy a sample app on [Cloud Run](https://docs.cloud.google.com/run/docs) connected to a PostgreSQL instance, ask your administrator to grant you the following IAM roles on the project that you want to use: 

  * Create or delete an Artifact Registry repository: [Artifact Registry Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.writer) (`roles/artifactregistry.writer`) 
  * Create or delete an instance, database, and user: Cloud SQL Administrator role (`roles/cloudsql.admin`). 
  * Create or delete an IAM service account: Service Account Administrator role (`roles/iam.serviceAccountAdmin`). 
  * Create a connection: 
    * [Service Networking Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.networksAdmin\)) (`roles/servicenetworking.networksAdmin)`)
    * Service Usage Admin (`roles/serviceusage.serviceUsageAdmin`). 
  * View objects and their metadata: Storage Object Viewer (roles/storage.objectViewer) 
  * Provide permissions to administer policies on projects.: Project IAM Admin (roles/resourcemanager.projectIamAdmin). 
  * Read and write access to all Cloud Run resources: Cloud Run Developer (roles/run.developer). 
  * Deploy and manage Cloud Run source deployed resources: Cloud Run Source Developer (roles/run.sourceDeveloper). 
  * To allow public access: Cloud Run Admin (roles/run.admin). 
  * To run operations as the service account: Service Account User (roles/iam.serviceAccountUser). 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Set up Cloud SQL

### Create a Cloud SQL instance

#### Public IP

Take the following steps to set up a Cloud SQL instance that you connect to over public IP:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click **Create instance**.
  3. From the **Create instance** menu, select **New instance**.
  4. Click **Choose PostgreSQL**.
  5. Make sure that **Enterprise Plus** is selected as the Cloud SQL edition for your instance.
  6. In the **Instance ID** field, enter `quickstart-instance`.
  7. In the **Password** field, enter a password for the postgres user. Save this password for future use.
  8. In the **Choose region and zonal availability** section, select **Single zone**.
  9. Click the **Show configuration options** menu.
  10. Expand the **Machine configuration** node.
  11. From the **Machine shapes** region, select the **4 vCPU, 32 GB** shape.
  12. Click **Create instance** and then wait until the instance initializes and starts.



### gcloud

Before running the command as follows, replace DB_ROOT_PASSWORD with the password of your database user.

Optionally, modify the values for the following parameters:

  * **\--database-version** : The database engine type and version. If left unspecified, the API default is used. See the [gcloud database versions](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create#--database-version) documentation to see the current available versions.
  * **\--cpu** : The number of cores desired in the machine.
  * **\--memory** : Whole number value indicating how much memory is desired in the machine. A size unit should be provided (for example, 3072MB or 9GB). If no units are specified, GB is assumed.
  * **\--region** : Regional location of the instance (for example asia-east1, us-east1). If left unspecified, the default `us-central` is used. 



Run the [`gcloud sql instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) command to create a Cloud SQL instance. 
    
    
    gcloud sql instances create quickstart-instance \
    --database-version=POSTGRES_14 \
     --cpu=1 \
     --memory=4GB \
     --region=us-central \
     --root-password=DB_ROOT_PASSWORD

#### Private IP

Take the following steps to set up a Cloud SQL instance that you connect to over private IP:

### Console

####  Allocate an IP address range and create a private connection to configure private services access for Cloud SQL 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks)

  2. Select the `default` VPC network.
  3. Select the **Private service connection** tab.
  4. Select the **Allocated IP ranges for services** tab.
  5. Click **Allocate IP range**.
  6. For the **Name** of the allocated range, specify `google-managed-services-default`.
  7. Select the **Automatic** option for IP range and specify the prefix length as `16`.
  8. Click **Allocate** to create the allocated range.
  9. Select the **Private connections to services** tab for the `default` VPC network.
  10. Click **Create connection** to create a private connection between your network and a service producer.
  11. For the **Assigned allocation** , select `google-managed-services-default`.
  12. Click **Connect** to create the connection.



####  Create an instance with private IP address and SSL enabled 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click **Create instance**.
  3. From the **Create instance** menu, select **New instance**.
  4. Click **Choose PostgreSQL**.
  5. Make sure that **Enterprise Plus** is selected as the Cloud SQL edition for your instance.
  6. In the **Instance ID** field, enter `quickstart-instance`.
  7. In the **Password** field, enter a password for the postgres user. Save this password for future use.
  8. In the **Choose region and zonal availability** section, select **Single zone**.
  9. Click the **Show configuration options** menu.
  10. Expand the **Machine configuration** node.
  11. From the **Machine shapes** region, select the **4 vCPU, 32 GB** shape.
  12. Expand the **Connections** node.
  13. Clear the **Public IP** checkbox to create an instance only with a private IP address.
  14. Select the **Private IP** checkbox.
  15. Select the **Private Service Access (PSA)** checkbox.
  16. In the **VPC Network *** dropdown, select **default**.
  17. In the **Security** section, make sure that **Allow only SSL connections** is selected to enable SSL connections.
  18. Click **Create instance** and then wait for the instance to initialize and start.



### gcloud

####  Allocate an IP address range and create a private connection to configure private services access for Cloud SQL 

  1. Run the [`gcloud compute addresses create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create) command to allocate an IP address range. 
         
         gcloud compute addresses create google-managed-services-default \
         --global --purpose=VPC_PEERING --prefix-length=16 \
         --description="peering range for Google" --network=default

  2. Run the [`gcloud services vpc-peerings connect`](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/connect) command to create a private connection to the allocated IP address range. Replace YOUR_PROJECT_ID with your project's project ID. 
         
         gcloud services vpc-peerings connect --service=servicenetworking.googleapis.com \
         --ranges=google-managed-services-default --network=default \
         --project=YOUR_PROJECT_ID




####  Create an instance with private IP address and SSL enabled 

  1. Before running the command as follows, replace DB_ROOT_PASSWORD with the password of your database user.

Optionally, modify the values for the following parameters:

     * **\--database-version** : The database engine type and version. If left unspecified, the API default is used. See the [gcloud database versions](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create#--database-version) documentation to see the current available versions.
     * **\--cpu** : The number of cores in the machine.
     * **\--memory** : A whole number value indicating how much memory to include in the machine. A size unit can be provided (for example, 3072MB or 9GB). If no units are specified, GB is assumed.
     * **\--region** : The regional location of the instance (for example asia-east1, us-east1). If left unspecified, the default `us-central1` is used. See the full list of [regions](https://docs.cloud.google.com/sql/docs/instance-locations).

Run the [`gcloud sql instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) command to create a Cloud SQL instance with a Private IP address. 
    
    gcloud sql instances create quickstart-instance \
    --database-version=POSTGRES_14 \
     --cpu=1 \
     --memory=4GB \
     --region=us-central \
     --root-password=DB_ROOT_PASSWORD \
     --no-assign-ip \
    --network=default

  2. Run the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command to enable **only allow SSL connections** for the instance. 
    
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

Take the following steps to create a user:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Users** from the SQL navigation menu.
  4. Click **Add user account**. 
  5. On the **Add a user account to instance _instance_name_** page, add the following information: 
     * In the **Username** field, enter `quickstart-user`
     * In the **Password** field, specify a password for your database user. Make a note of this for use in a later step of this quickstart.
  6. Click **Add**.



### gcloud

Before running the following command, make the following replacements:

  1. PASSWORD with a password for your database user. Make a note of this for use in a later step of this quickstart. 



Run the [`gcloud sql users create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/users/create) command to create the user.
    
    
    gcloud sql users create quickstart-user \
    --instance=quickstart-instance \
    --password=PASSWORD

Username length limits are the same for Cloud SQL as for on-premises PostgreSQL. 

## Deploy sample app to Cloud Run

### Configure a Cloud Run service account

Configure the [ Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) used by Cloud Run so that it has the **Cloud SQL Client** and **Storage Object Viewer** roles. 

### Console

  1. In the Google Cloud console, go to the **IAM Service accounts** page.

[Go to IAM Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click the **Actions** more_vert menu beside the service accound, then click **Manage access**.
  3. Click **Add another role** , then find and select the **Cloud SQL Client** (`roles/cloudsql.client`) in the **Role** dropdown.
  4. Click **Add another role** , then find and select the **Storage Object Viewer** (`roles/storage.objectViewer`) in the **Role** dropdown.
  5. Click **Save**.



### gcloud

  1. Run the following `gcloud` command to get a list of your project's service accounts: 
         
         gcloud iam service-accounts list

  2. Copy the **EMAIL** Compute Engine default service account.
  3. Run the following command to add the **Cloud SQL Client** role to the **Compute Engine default service account** : 
         
         gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
           --member="serviceAccount:SERVICE_ACCOUNT_EMAIL" \
           --role="roles/cloudsql.client"

  4. Run the following command to add the **Storage Object Viewer** role to the **Compute Engine default service account** : 
         
         gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
           --member="serviceAccount:SERVICE_ACCOUNT_EMAIL" \
           --role="roles/storage.objectViewer"




### Configure a Cloud SQL sample app

With a Cloud SQL instance, database, and service account with client permissions, you can now configure a sample application to connect to your Cloud SQL instance.

#### Public IP

For public IP paths, Cloud Run provides encryption and connects using the Cloud SQL Auth Proxy through Unix sockets. 

### Go

  1. In Cloud Shell Editor, open the sample app's source code. 

[Open Cloud Shell Editor](https://docs.cloud.google.com/console/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/golang-samples&working_dir=cloudsql/postgres/database-sql)

  2. In the **Open in Cloud Shell** dialog, click **Confirm** to download the sample app code and open the sample app directory in Cloud Shell Editor. 
  3. Create an Artifact Registry Docker repository named `run-sql` in the same region as your Cloud SQL instance. Replace YOUR_PROJECT_ID with your project ID and YOUR_REGION_NAME with your region name. 
         
         gcloud artifacts repositories create run-sql \
             --project=YOUR_PROJECT_ID \
             --repository-format=docker \
             --location=YOUR_REGION_NAME \
             --description="Quickstart Cloud SQL sample app"
           

  4. Run the following command in Cloud Shell to build a Docker container and publish it to Artifact Registry. Replace YOUR_PROJECT_ID with your project ID and YOUR_REGION_NAME with your region name. 
         
         gcloud builds submit --tag YOUR_REGION_NAME-docker.pkg.dev/YOUR_PROJECT_ID/run-sql/run-sql




### Java

  1. In Cloud Shell Editor, open the sample app's source code. 

[Open Cloud Shell Editor](https://docs.cloud.google.com/console/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/java-docs-samples&working_dir=cloud-sql/postgres/servlet)

  2. In the **Open in Cloud Shell** dialog, click **Confirm** to download the sample app code and open the sample app directory in Cloud Shell Editor. 
  3. Create an Artifact Registry Docker repository named `run-sql` in the same region as your Cloud SQL instance. Replace YOUR_PROJECT_ID with your project ID and YOUR_REGION_NAME with your region name. 
         
         gcloud artifacts repositories create run-sql \
             --project=YOUR_PROJECT_ID \
             --repository-format=docker \
             --location=YOUR_REGION_NAME \
             --description="Quickstart Cloud SQL sample app"
           

  4. Run the `mvn` command as follows in Cloud Shell to build a Docker container and publish it to Artifact Registry. Replace YOUR_PROJECT_ID with your project ID and YOUR_REGION_NAME with your region name. 
         
         mvn clean package com.google.cloud.tools:jib-maven-plugin:2.8.0:build \
          -Dimage=YOUR_REGION_NAME-docker.pkg.dev/YOUR_PROJECT_ID/run-sql/run-sql \
          -DskipTests -Djib.to.credHelper=gcloud




### Node.js

  1. In Cloud Shell Editor, open the sample app's source code. 

[Open Cloud Shell Editor](https://docs.cloud.google.com/console/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/nodejs-docs-samples&working_dir=cloud-sql/postgres/knex)

  2. In the **Open in Cloud Shell** dialog, click **Confirm** to download the sample app code and open the sample app directory in Cloud Shell Editor. 
  3. Create an Artifact Registry Docker repository named `run-sql` in the same region as your Cloud SQL instance. Replace YOUR_PROJECT_ID with your project ID and YOUR_REGION_NAME with your region name. 
         
         gcloud artifacts repositories create run-sql \
             --project=YOUR_PROJECT_ID \
             --repository-format=docker \
             --location=YOUR_REGION_NAME \
             --description="Quickstart Cloud SQL sample app"
           

  4. Run the following command in Cloud Shell to build a Docker container and publish it to Artifact Registry. Replace YOUR_PROJECT_ID with your project ID and YOUR_REGION_NAME with your region name. 
         
         gcloud builds submit --tag YOUR_REGION_NAME-docker.pkg.dev/YOUR_PROJECT_ID/run-sql/run-sql




### Python

  1. In Cloud Shell Editor, open the sample app's source code. 

[Open Cloud Shell Editor](https://docs.cloud.google.com/console/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/python-docs-samples&working_dir=cloud-sql/postgres/sqlalchemy)

  2. In the **Open in Cloud Shell** dialog, click **Confirm** to download the sample app code and open the sample app directory in Cloud Shell Editor. 
  3. Create an Artifact Registry Docker repository named `run-sql` in the same region as your Cloud SQL instance. Replace YOUR_PROJECT_ID with your project ID and YOUR_REGION_NAME with your region name. 
         
         gcloud artifacts repositories create run-sql \
             --project=YOUR_PROJECT_ID \
             --repository-format=docker \
             --location=YOUR_REGION_NAME \
             --description="Quickstart Cloud SQL sample app"
           

  4. Run the following command in Cloud Shell to build a Docker container and publish it to Artifact Registry. Replace YOUR_PROJECT_ID with your project ID and YOUR_REGION_NAME with your region name. 
         
         gcloud builds submit --tag YOUR_REGION_NAME-docker.pkg.dev/YOUR_PROJECT_ID/run-sql/run-sql




#### Private IP

For private IP paths, your application connects directly to your instance through [Direct VPC egress or a VPC connector](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc). This method uses a TCP socket to connect directly to the Cloud SQL instance without using the Cloud SQL Auth Proxy. 

### Go

####  Create and download SSL server and client certificates 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click the `quickstart-instance` to see its **Overview** page
  3. Click the **Connections** tab.
  4. Under the **Security** section, click **Create client certificate**.
  5. In the **Create a client certificate** dialog, enter `quickstart-key` as the name and click **Create**.
  6. In the **New SSL certificate created** dialog, click each download link to download the certificates. Then, click **Close**.

**Important:** Store this private key securely. If you lose it, you must create a new client certificate.




####  Build sample app with SSL certificates 

  1. In Cloud Shell Editor, open the sample app's source code.   
[Open Cloud Shell Editor](https://docs.cloud.google.com/console/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/golang-samples&working_dir=cloudsql/postgres/database-sql)
  2. In the **Open in Cloud Shell** dialog, click **Confirm** to download the sample app code and open the sample app directory in Cloud Shell Editor. 
  3. Upload SSL certs files to **certs** folder. 
     1. Right-click **certs** folder in Cloud Shell Editor and select **Upload Files**
     2. Select following files on your local machine:
        * `client-key.pem`
        * `client-cert.pem`
        * `server-ca.pem`
     3. With the three SSL certificate files selected, click **Open** to complete the process of uploading the files to Cloud Shell Editor.
  4. Create an Artifact Registry Docker repository named `run-sql` in the same region as your Cloud SQL instance. Replace YOUR_PROJECT_ID with your project ID and YOUR_REGION_NAME with your region name. 
         
         gcloud artifacts repositories create run-sql \
             --project=YOUR_PROJECT_ID \
             --repository-format=docker \
             --location=YOUR_REGION_NAME \
             --description="Quickstart Cloud SQL sample app"
           

  5. Run the following command in Cloud Shell to build a Docker container and publish it to Artifact Registry. Replace YOUR_PROJECT_ID with your project ID and YOUR_REGION_NAME with your region name. 
         
         gcloud builds submit --tag YOUR_REGION_NAME-docker.pkg.dev/YOUR_PROJECT_ID/run-sql/run-sql




### Java

####  Create and download SSL server and client certificates 

For Java users, the Java Connector already provides a secure connection so that creating and downloading SSL server and client certificates is unnecessary. 

####  Build Sample App 

  1. In Cloud Shell Editor, open the sample app's source code.   
[Open Cloud Shell Editor](https://docs.cloud.google.com/console/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/java-docs-samples&working_dir=cloud-sql/postgres/servlet)
  2. In the **Open in Cloud Shell** dialog, click **Confirm** to download the sample app code and open the sample app directory in Cloud Shell Editor. 
  3. Create an Artifact Registry Docker repository named `run-sql` in the same region as your Cloud SQL instance. Replace YOUR_PROJECT_ID with your project ID and YOUR_REGION_NAME with your region name. 
         
         gcloud artifacts repositories create run-sql \
             --project=YOUR_PROJECT_ID \
             --repository-format=docker \
             --location=YOUR_REGION_NAME \
             --description="Quickstart Cloud SQL sample app"
           

  4. Run the following command in Cloud Shell to build a Docker container and publish it to Artifact Registry. Replace YOUR_PROJECT_ID with your project ID and YOUR_REGION_NAME with your region name. 
         
         gcloud builds submit --tag YOUR_REGION_NAME-docker.pkg.dev/YOUR_PROJECT_ID/run-sql/run-sql




### Node.js

####  Create and download SSL server and client certificates 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click the `quickstart-instance` to see its **Overview** page
  3. Click the **Connections** tab.
  4. Under the **Security** section, click **Create client certificate**.
  5. In the **Create a client certificate** dialog, enter `quickstart-key` as the name and click **Create**.
  6. In the **New SSL certificate created** dialog, click each download link to download the certificates. Then, click **Close**.

**Important:** Store this private key securely. If you lose it, you must create a new client certificate.




####  Build sample app with SSL certificates 

  1. In Cloud Shell Editor, open the sample app's source code.   
[Open Cloud Shell Editor](https://docs.cloud.google.com/console/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/nodejs-docs-samples&working_dir=cloud-sql/postgres/knex)
  2. In the **Open in Cloud Shell** dialog, click **Confirm** to download the sample app code and open the sample app directory in Cloud Shell Editor. 
  3. Upload SSL certs files to **certs** folder. 
     1. Right-click **certs** folder in Cloud Shell Editor and select **Upload Files**
     2. Select following files on your local machine:
        * `client-key.pem`
        * `client-cert.pem`
        * `server-ca.pem`
     3. With the three SSL certificate files selected, click **Open** to complete the process of uploading the files to Cloud Shell Editor.
  4. Create an Artifact Registry Docker repository named `run-sql` in the same region as your Cloud SQL instance. Replace YOUR_PROJECT_ID with your project ID and YOUR_REGION_NAME with your region name. 
         
         gcloud artifacts repositories create run-sql \
             --project=YOUR_PROJECT_ID \
             --repository-format=docker \
             --location=YOUR_REGION_NAME \
             --description="Quickstart Cloud SQL sample app"
           

  5. Run the following command in Cloud Shell to build a Docker container and publish it to Artifact Registry. Replace YOUR_PROJECT_ID with your project ID and YOUR_REGION_NAME with your region name. 
         
         gcloud builds submit --tag YOUR_REGION_NAME-docker.pkg.dev/YOUR_PROJECT_ID/run-sql/run-sql




### Python

####  Create and download SSL server and client certificates 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click the `quickstart-instance` to see its **Overview** page
  3. Click the **Connections** tab.
  4. Under the **Security** section, click **Create client certificate**.
  5. In the **Create a client certificate** dialog, enter `quickstart-key` as the name and click **Create**.
  6. In the **New SSL certificate created** dialog, click each download link to download the certificates. Then, click **Close**.

**Important:** Store this private key securely. If you lose it, you must create a new client certificate.




####  Build sample app with SSL certificates 

  1. In Cloud Shell Editor, open the sample app's source code.   
[Open Cloud Shell Editor](https://docs.cloud.google.com/console/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/python-docs-samples&working_dir=cloud-sql/postgres/sqlalchemy)
  2. In the **Open in Cloud Shell** dialog, click **Confirm** to download the sample app code and open the sample app directory in Cloud Shell Editor. 
  3. Upload SSL certs files to **certs** folder. 
     1. Right-click **certs** folder in Cloud Shell Editor and select **Upload Files**
     2. Select following files on your local machine:
        * `client-key.pem`
        * `client-cert.pem`
        * `server-ca.pem`
     3. With the three SSL certificate files selected, click **Open** to complete the process of uploading the files to Cloud Shell Editor.
  4. Create an Artifact Registry Docker repository named `run-sql` in the same region as your Cloud SQL instance. Replace YOUR_PROJECT_ID with your project ID and YOUR_REGION_NAME with your region name. 
         
         gcloud artifacts repositories create run-sql \
             --project=YOUR_PROJECT_ID \
             --repository-format=docker \
             --location=YOUR_REGION_NAME \
             --description="Quickstart Cloud SQL sample app"
           

  5. Run the following command in Cloud Shell to build a Docker container and publish it to Artifact Registry. Replace YOUR_PROJECT_ID with your project ID and YOUR_REGION_NAME with your region name. 
         
         gcloud builds submit --tag YOUR_REGION_NAME-docker.pkg.dev/YOUR_PROJECT_ID/run-sql/run-sql




### Deploy the sample app

The steps to deploy the sample to Cloud Run depend on the type of IP address you assigned to your Cloud SQL instance.

The image connection method varies based on which environment variables are set. 

  * To connect using TCP, set the value for the `INSTANCE_HOST` environment variable. This connection method [honors the certificates and ports configured as environment variables](https://github.com/GoogleCloudPlatform/java-docs-samples/blob/61c9d9eb1797583e04f8525848e0535643a62440/cloud-sql/mysql/servlet/src/main/java/com/example/cloudsql/TcpConnectionPoolFactory.java#L70-L78).
  * To connect using Unix sockets, set the value for the `INSTANCE_UNIX_SOCKET` environment variable. 

Don't set the value for the `INSTANCE_HOST` environment variable.

Unix sockets aren't natively supported in Java. If your application is written using Java, you must use the Cloud SQL Java Connector.

  * To connect using one of the [Cloud SQL Language Connectors](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors), set the value for the `INSTANCE_CONNECTION_NAME ` environment variable. 

Don't set the values for the following environment variables:

    * `INSTANCE_HOST`
    * `INSTANCE_UNIX_SOCKET`
    * `DB_PORT`
    * `DB_ROOT_CERT`
    * `DB_CERT`
    * `DB_KEY`
These values aren't used because the Cloud SQL Language Connector already provides a secure connection using Cloud SQL Auth Proxy server, which establishes connections to Cloud SQL on port `3307`. 



#### Public IP

### Console

**Note:** If you are using the Console to [deploy a function](https://docs.cloud.google.com/run/docs/deploy-functions), you must enable the required APIs, have the required roles granted to you, and click on the form for **Write a function**. 

  1. In the Google Cloud console, go to the **Cloud Run** page.

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Click **Create container** and select **Service** to display the _Create service_ form.

  3. Click the **Select** button in the **Container image URL** input field.
     1. Select the `gcr.io/YOUR_PROJECT_ID/run-sql` container image you created in the previous step.
  4. In the **Service name** field, enter `quickstart-service`.
  5. In the **Authentication** section, select the `Allow public access` option. If you don't have permissions (Cloud Run Admin role) to select this, the service will deploy and require authentication.
  6. Expand the **Container, Variables & Secrets, Connections, Security ** section.
  7. Create the following `Environment variables` by clicking **Add Variable** under **Environment variables**. Set the values for the environment variables, as follows:
     * **INSTANCE_UNIX_SOCKET** : Set to `/cloudsql/YOUR_PROJECT_ID:us-central1:quickstart-instance`.
     * **INSTANCE_CONNECTION_NAME** : Set to your instance's **Connection name** that appears on the [Cloud SQL instances](https://console.cloud.google.com/sql) page in the Google Cloud console.
     * **DB_NAME** : Set to `quickstart-db`
     * **DB_USER** : Set to `quickstart-user`
     * **DB_PASS** : Set to the password of the `quickstart-user` that you created in the previous **Create a user** quickstart step.
  8. Enable connecting to Cloud SQL:

     * Click the **Connections** tab.
     * Click the **Add Connection** button under the **Cloud SQL connections** section.
     * Select the `quickstart-instance` you previously created from the drop-down menu.

![Add Cloud SQL connection](https://docs.cloud.google.com/static/run/docs/images/cloudsql-connection.png)

  9. Click **Create** to create the Cloud Run service.

  10. After the Cloud Run service is deployed, the **Service details** page displays the URL of the running service at the top of the page. Click the **URL** link to see the deployed sample app on Cloud Run connected to Cloud SQL. 

![View deployed sample app.](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)




### gcloud

  1. Before running the following command, make the following replacements:

     * YOUR_PROJECT_ID with your project ID.
     * INSTANCE_CONNECTION_NAME with your instance's **Connection name** that appears on the [Cloud SQL instances](https://console.cloud.google.com/sql) page in the Google Cloud console.

     * DB_PASS with the password of the `quickstart-user` that you created in the previous **Create a user** quickstart step. 

Run the [`gcloud run deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy) command as follows to create the Cloud Run service. Environment variables vary depending on the [connection method](https://docs.cloud.google.com/sql/docs/postgres/connect-instance-cloud-run#deploy_the_sample_app) you want to use:
    
    gcloud run deploy run-sql --image gcr.io/YOUR_PROJECT_ID/run-sql \
        --add-cloudsql-instances INSTANCE_CONNECTION_NAME \
        --set-env-vars INSTANCE_CONNECTION_NAME="INSTANCE_CONNECTION_NAME" \
        --set-env-vars DB_NAME="quickstart-db" \
        --set-env-vars DB_USER="quickstart-user" \
        --set-env-vars DB_PASS="DB_PASS"

Enter the numeric choice provided for `us-central1` when prompted to specify a region.

  2. When you see a confirmation message that the Cloud Run service has been deployed, click the **Service URL** link in the message to see the sample app on Cloud Run that is connected to Cloud SQL. 

![View deployed sample app.](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)




#### Private IP

### Console

**Note:** If you are using the Console to [deploy a function](https://docs.cloud.google.com/run/docs/deploy-functions), you must enable the required APIs, have the required roles granted to you, and click on the form for **Write a function**. 

  1. In the Google Cloud console, go to the **Cloud Run** page.

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Click **Create container** and select **Service** to display the _Create service_ form.

  3. Retain the option to deploy from an existing container image and click **Select** to specify the `gcr.io/YOUR_PROJECT_ID/run-sql` container image you created in the previous step.
  4. Enter `quickstart-service` for the **Service name**.
  5. In the **Authentication** section, select the `Allow public access` option. If you the `Allow public access` option. If you don't have permissions (Cloud Run Admin role) to select this, the service will deploy and require authentication.
  6. Expand the **Container, Variables & Secrets, Connections, Security ** section.
  7. Create the following environment variables by clicking **Add variable** under **Environment variables**. Set the values for the environment variables, as follows:
     * `DB_NAME`: Set to `quickstart-db`.
     * `DB_USER`: Set to `quickstart-user`.
     * `DB_PASS`: Set to the password of the `quickstart-user` that you specified in the previous **Create a user** quickstart step.
     * `INSTANCE_CONNECTION_NAME`: Set to your instance's **Connection name** that appears on the [Cloud SQL instances](https://console.cloud.google.com/sql) page in the Google Cloud console.
     * `DB_PORT`: Set to `5432`.
     * `DB_ROOT_CERT`: Set to `certs/server-ca.pem`.
     * `DB_CERT`: Set to `certs/client-cert.pem`.
     * `DB_KEY`: Set to `certs/client-key.pem`.
     * `PRIVATE_IP`: Set to `TRUE`.
  8. Enable connecting to Cloud SQL:

     1. Click **Connections**.
     2. Click **Add Connection** in the **Cloud SQL connections** section.
     3. Select the `quickstart-instance` Cloud SQL instance that you previously created.
     4. From the **Networking** tab, select **Connect to a VPC for outbound traffic** , then select **default** in both the **Network** and **Subnet** fields.
     5. Select the option **Route all traffic to the VPC**.
  9. Click **Create** to create the Cloud Run service.

  10. After the Cloud Run service is deployed, the **Service details** page displays the URL of the running service at the top of the page. Click the **URL** link to see the deployed sample app on Cloud Run connected to Cloud SQL. 

![View deployed sample app](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)




### gcloud

  1. Before running the following command, make the following replacements:

     * YOUR_PROJECT_ID with your project ID.
     * INSTANCE_CONNECTION_NAME with your instance's **Connection name** that appears on the [Cloud SQL instances](https://console.cloud.google.com/sql) page in the Google Cloud console. 
     * DB_PASS with the password of the `quickstart-user` that you created in the previous **Create a user** quickstart step. 

Run the [`gcloud run deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy) command as follows to create the Cloud Run service. Environment variables vary depending on the [connection method](https://docs.cloud.google.com/sql/docs/postgres/connect-instance-cloud-run#deploy_the_sample_app) you want to use:
    
    gcloud run deploy run-sql --image gcr.io/YOUR_PROJECT_ID/run-sql \
        --add-cloudsql-instances INSTANCE_CONNECTION_NAME \
        --vpc-egress=all-traffic \
        --network=default \
        --subnet=default \
        --set-env-vars DB_NAME="quickstart-db" \
        --set-env-vars DB_USER="quickstart-user" \
        --set-env-vars DB_PASS="DB_PASS" \
        --set-env-vars INSTANCE_CONNECTION_NAME="INSTANCE_CONNECTION_NAME"
      

Enter the numeric choice provided for `us-central1` when prompted to specify a region.

  2. When you see a confirmation message that the Cloud Run service has been deployed, click the **Service URL** link in the message to see the sample app on Cloud Run that is connected to Cloud SQL. 

![View deployed sample app](https://docs.cloud.google.com/static/sql/images/tabs-vs-spaces-app-screen-shot.png)




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Select the `quickstart-instance` instance to open the **Instance details** page.
  3. In the icon bar at the top of the page, click **Delete**.
  4. In the **Delete instance** dialog box, type `quickstart-instance`, and then click **Delete** to delete the instance. 
  5. In the Google Cloud console, go to the **Cloud Run** page.

[Go to Cloud Run](https://console.cloud.google.com/run)

  6. Select the checkbox next to the `quickstart-service` service name.
  7. Click **Delete** at the top of the Cloud Run page. 



### Optional cleanup steps

If you're not using the **Cloud SQL client** role that you assigned to the Compute Engine service account, you can remove it.

  1. In the Google Cloud console, go to the **Service accounts** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Click the edit icon (which looks like a pencil) for the IAM account named **Compute Engine default service account**.
  3. Delete the **Cloud SQL client** role.
  4. Click **Save**.



If you're not using the APIs that were enabled as part of this quickstart, you can disable them.

  * APIs that were enabled within this quickstart: 
    * Compute Engine API
    * Cloud SQL Admin API
    * Cloud Run API
    * Container Registry API
    * Cloud Build API


  1. In the Google Cloud console, go to the **APIs** page.

[Go to APIs](https://console.cloud.google.com/apis)

  2. Select any API that you would like to disable and then click the **Disable API** button.




## What's next

Based on your needs, you can learn more about [creating Cloud SQL instances](https://docs.cloud.google.com/sql/docs/postgres/create-instance). 

You also can learn about creating [PostgreSQL users](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users#creating) and [databases](https://docs.cloud.google.com/sql/docs/postgres/create-manage-databases#create) for your Cloud SQL instance.

For more information about pricing, see [Cloud SQL for PostgreSQL pricing](https://cloud.google.com/sql/pricing).

Learn more about:

  * Configuring your Cloud SQL instance with a [public IP](https://docs.cloud.google.com/sql/docs/postgres/configure-ip) address.
  * Configuring your Cloud SQL instance with a [private IP](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip) address.



Additionally, you can learn about connecting to a Cloud SQL instance from other Google Cloud applications:

  * [From an application running on App Engine standard environment](https://docs.cloud.google.com/sql/docs/postgres/connect-app-engine)
  * [From an application running on Compute Engine](https://docs.cloud.google.com/sql/docs/postgres/connect-compute-engine)
  * [From an application running on GKE](https://docs.cloud.google.com/sql/docs/postgres/connect-kubernetes-engine)
  * [From Cloud Run](https://docs.cloud.google.com/sql/docs/postgres/connect-run)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
