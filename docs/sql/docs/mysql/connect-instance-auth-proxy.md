---
url: https://docs.cloud.google.com/sql/docs/mysql/connect-instance-auth-proxy/
title: Quickstart: Connect to Cloud SQL for MySQL using the Cloud SQL Auth Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:52.331168+00:00
---

# Quickstart: Connect to Cloud SQL for MySQL using the Cloud SQL Auth Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/connect-instance-auth-proxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connect to Cloud SQL for MySQL using the Cloud SQL Auth Proxy

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/quickstart-proxy-test "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/quickstart-proxy-test "View this page for the SQL Server database engine")

This page shows you how to connect to Cloud SQL from a local test environment using the Cloud SQL Auth Proxy. The [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy) provides secure access to your Cloud SQL instance without the need for authorized networks or for configuring SSL. By using the Cloud SQL Auth Proxy, you can connect to your Cloud SQL instance securely.

The instructions on this page are for a test environment only and shouldn't be used for production environments. For more information on the configuration required for production environments, see [Use the Cloud SQL Auth Proxy in a production environment](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy#production-environment) and [Connect using the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/connect-auth-proxy).

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

  6. Enable the necessary Google Cloud APIs. 

### Console

In the Google Cloud console, go to the **APIs** page.

[Go to APIs](https://console.cloud.google.com/apis)

Enable the Cloud SQL Admin API. 

### gcloud

Click the following button to open Cloud Shell, which provides command-line access to your Google Cloud resources directly from the browser. Cloud Shell can be used to run the `gcloud` commands presented throughout this quickstart.

[Open Cloud Shell](https://docs.cloud.google.com/console/sql/instances?cloudshell=true)

Run the [`gcloud services enable`](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable) command as follows using Cloud Shell to enable the APIs required for this quickstart.:
         
         gcloud services enable sqladmin.googleapis.com

This command enables the following APIs:

     * Cloud SQL Admin API

  7. Make sure that you have the following role or roles on the project: Cloud SQL Admin (`roles/cloudsql.admin`) 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 



## Create a Cloud SQL instance

In this quickstart, you use the Google Cloud console. To use the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), curl, or PowerShell, see [Create instances](https://docs.cloud.google.com/sql/docs/mysql/create-instance).

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click **Create instance**.
  3. From the **Create instance** menu, select **New instance**.
  4. Click **Choose MySQL**.
  5. In the **Instance ID** field, enter `myinstance`.
  6. In the **Password** field, enter a password for the `root` user.
  7. Click **Create instance**.

You're returned to the instances list. You can click the new instance right away to see the details, but it won't be available for other operations until it initializes and starts.

**Note:** In this example, the instance is created using default settings, including a public IP address.


  1. Download the MySQL Community Server for your platform from the [MySQL Community Server download page](http://dev.mysql.com/downloads/mysql/).   
The Community Server includes the MySQL client. 
  2. Install the Community Server, following the directions on the download page. 



For more information about installing MySQL, see [Installing and Upgrading MySQL](https://dev.mysql.com/doc/refman/8.4/en/installing.html).

## Install the Cloud SQL Auth Proxy client

The Cloud SQL Auth Proxy binary you download depends on your operating system, and whether it uses a 32-bit or 64-bit kernel. Most newer hardware uses a 64-bit kernel. If you're unsure whether your machine is running a 32-bit or 64-bit kernel, then use the `uname -a` command for Linux or macOS. For Windows, see the [Windows documentation](https://support.microsoft.com/en-us/windows/32-bit-and-64-bit-windows-frequently-asked-questions-c6ca9541-8dce-4d48-0415-94a3faa2e13d).

Before you begin, you must determine your machine's architecture.

If running on Linux or Mac, you can find this by running the following command:
    
    
      uname -a
      

### Linux 64-bit

  1. Download the Cloud SQL Auth Proxy: 
         
         curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.2/cloud-sql-proxy.linux.amd64

  2. Make the Cloud SQL Auth Proxy executable: 
         
         chmod +x cloud-sql-proxy




### Linux 32-bit

  1. Download the Cloud SQL Auth Proxy: 
         
         curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.2/cloud-sql-proxy.linux.386

  2. If the `curl` command is not found, run `sudo apt install curl` and repeat the download command.
  3. Make the Cloud SQL Auth Proxy executable: 
         
         chmod +x cloud-sql-proxy




### macOS 64-bit

  1. Download the Cloud SQL Auth Proxy: 
         
         curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.2/cloud-sql-proxy.darwin.amd64

  2. Make the Cloud SQL Auth Proxy executable: 
         
         chmod +x cloud-sql-proxy




### Mac M1

  1. Download the Cloud SQL Auth Proxy: 
         
         curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.2/cloud-sql-proxy.darwin.arm64
           

  2. Make the Cloud SQL Auth Proxy executable: 
         
         chmod +x cloud-sql-proxy
           




### Windows 64-bit

Right-click <https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.2/cloud-sql-proxy.x64.exe> and select **Save Link As** to download the Cloud SQL Auth Proxy. Rename the file to `cloud-sql-proxy.exe`. 

### Windows 32-bit

Right-click <https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.2/cloud-sql-proxy.x86.exe> and select **Save Link As** to download the Cloud SQL Auth Proxy. Rename the file to `cloud-sql-proxy.exe`. 

### Cloud SQL Auth Proxy Docker image

The Cloud SQL Auth Proxy has different container images, such as `distroless`, `alpine`, and `buster`. The default Cloud SQL Auth Proxy container image uses [`distroless`](https://github.com/GoogleContainerTools/distroless), which contains no shell. If you need a shell or related tools, then download an image based on `alpine` or `buster`. For more information, see [Cloud SQL Auth Proxy Container Images](https://github.com/GoogleCloudPlatform/cloudsql-proxy#container-images).

You can pull the latest image to your local machine using Docker by using the following command:
    
    
    docker pull gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.26.2
    

**Note** : The Cloud SQL Auth Proxy uses a repository that supports the `gcr.io` domain but serves images from Artifact Registry. For more information, see [Transition from Container Registry](https://docs.cloud.google.com/artifact-registry/docs/transition/transition-from-gcr). 

### Other OS

For other operating systems not included here, you can [compile the Cloud SQL Auth Proxy from source](http://github.com/GoogleCloudPlatform/cloudsql-proxy). 

## Get the instance connection name

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click the instance name to open its **Overview** page.
  3. In the **Connect to this instance** section, copy the **Connection name**. The connection name is in the format `projectID:region:instanceID`.



## Start the Cloud SQL Auth Proxy

Start the Cloud SQL Auth Proxy in its own terminal so you can monitor its output. Replace `INSTANCE_CONNECTION_NAME` with the instance connection name you copied in the previous step.

For Linux environments, use this command to launch the Cloud SQL Auth Proxy: 
    
    
    ./cloud-sql-proxy INSTANCE_CONNECTION_NAME

In PowerShell on Windows, use this command to launch the Cloud SQL Auth Proxy: 
    
    
    .\cloud-sql-proxy.exe INSTANCE_CONNECTION_NAME

A message similar to the following appears:
    
    
    Listening on 127.0.0.1:3306 for INSTANCE_CONNECTION_NAME
    Ready for new connections
    

Run the following command:
    
    
    mysql -u root -p --host 127.0.0.1 --port 3306

At the `Enter password:` prompt, enter the password of your MySQL root user account.

Verify that the MySQL prompt appears. You have connected to your database using the mysql client.

Return to the terminal window where you started the Cloud SQL Auth Proxy. You should see a message similar to the following:

`New connection for _myInstance_`

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Select the `myinstance` instance to open the **Instance details** page.
  3. In the icon bar at the top of the page, click **Delete**.
  4. In the **Delete instance** window, type your instance's name and then click **Delete**.



### Optional cleanup steps

If you're not using the APIs that were enabled as part of this quickstart, you can disable them.

  * APIs that were enabled within this quickstart: 
    * Cloud SQL Admin API


  1. In the Google Cloud console, go to the **APIs** page.

[Go to APIs](https://console.cloud.google.com/apis)

  2. Select the Cloud SQL Admin API and then click the **Disable API** button.




## What's next

  * See how to [troubleshoot information for the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/connect-auth-proxy#troubleshooting).

  * Learn more [about the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy).



  * Learn more [about other connection options](https://docs.cloud.google.com/sql/docs/mysql/connect-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
