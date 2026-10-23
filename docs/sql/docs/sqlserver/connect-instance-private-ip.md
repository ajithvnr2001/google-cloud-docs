---
url: https://docs.cloud.google.com/sql/docs/sqlserver/connect-instance-private-ip/
title: Quickstart: Connect to a Cloud SQL for SQL Server instance with private IP \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:55.925107+00:00
---

# Quickstart: Connect to a Cloud SQL for SQL Server instance with private IP  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/connect-instance-private-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connect to a Cloud SQL for SQL Server instance with private IP

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/quickstart-private-ip "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/quickstart-private-ip "View this page for the PostgreSQL database engine") | SQL Server

This page shows you how to create and connect to a SQL Server instance using a private IP. The resources created in this quickstart typically cost less than a dollar, assuming you complete the steps, including the clean up, in a timely manner.

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
  7. Enable the necessary Google Cloud APIs. 

### Console

In the Google Cloud console, go to the **APIs** page.

[Go to APIs](https://console.cloud.google.com/apis)

Enable the Cloud SQL Admin API. By enabling this API, you can run the Cloud SQL Auth Proxy. 

### gcloud

Click the following button to open Cloud Shell, which provides command-line access to your Google Cloud resources directly from the browser. Cloud Shell can be used to run the `gcloud` commands presented throughout this quickstart.

[Open Cloud Shell](https://docs.cloud.google.com/console/sql/instances?cloudshell=true)

Run the [`gcloud services enable`](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable) command as follows using Cloud Shell to enable the APIs required for this quickstart.:
         
         gcloud services enable sqladmin.googleapis.com

This command enables the following APIs:

     * Cloud SQL Admin API. By enabling this API, you can run the Cloud SQL Auth Proxy.




### Required roles

To get the permissions that you need to set up Cloud SQL with a private IP address, ask your administrator to grant you the following IAM roles on the project that you want to set up and connect to: 

  * Create or delete an instance, database, and user: Cloud SQL Administrator role (`roles/cloudsql.admin`). 
  * Create or delete an IAM service account: IAM Service Account Administrator role (`roles/iam.serviceAccountAdmin`). 
  * Create or delete a compute instance: 
    * [Compute Administrator role ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)
    * Compute Instance Administrator role (`roles/compute.instanceAdmin.v1`). 
  * Create a connection: 
    * [Service Networking Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/servicenetworking#servicenetworking.networksAdmin\)) (`roles/servicenetworking.networksAdmin)`)
    * Service Usage Admin (`roles/serviceusage.serviceUsageAdmin`). 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Overview

There are many ways to connect to a Cloud SQL instance with a private IP address, depending on where the source is located. The key factor is that the source machine must be in the same VPC network as the Cloud SQL instance. If the source is not in Google Cloud or not in the same Google Cloud project, then you have to [configure connectivity](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip#vpn) differently than we show here.

In this quickstart, we configure connectivity through the most direct path. The source and target are in the same Google Cloud project and in the same VPC network. We create a Cloud SQL instance with a private IP address (the target) and a Compute Engine VM (the source). We use the VM to install and use the tools required to connect from the VM to the Cloud SQL instance.

Perform the following actions:

  1. Create a Cloud SQL instance with a private IP address. 

Find and save the instance's `connection name` for later use.

  2. Create a Compute Engine VM.
  3. Open two SSH connections to the Compute Engine VM. 

You'll use the first window to install the sqlcmd and install and start the Cloud SQL Auth Proxy. Then you'll use the second window to connect to the Cloud SQL instance by connecting to the Cloud SQL Auth Proxy.

  4. In SSH window #1, do the following: 
     1. Install the sqlcmd client.
     2. Install the Cloud SQL Auth Proxy. 

The Cloud SQL Auth Proxy acts as a connector between the sqlcmd client and the Cloud SQL instance.

     3. Start the Cloud SQL Auth Proxy. 

On success, the Cloud SQL Auth Proxy listens for connection requests.

  5. In SSH window #2, connect to the Cloud SQL instance by having the sqlcmd client connect to the Cloud SQL Auth Proxy. 

On success, you see your sqlcmd prompt in this window, and a successful connection message in SSH window #1, where the Cloud SQL Auth Proxy is running.

  6. Clean up.



## Create a Cloud SQL instance with a private IP address

To create an instance that uses private IP connections, do the following: 

  1. In the Google Cloud console, go to the **Cloud SQL Get Started** page.

[Go to Cloud SQL Get Started](https://console.cloud.google.com/sql/get-started)

  2. In the **Get started** section, select the SQL Server tab and click **Create Sandbox instance**.
  3. If you're prompted to enable the **Compute API** , click the **Enable API** button.
  4. In the **Instance info** section, enter a name for the **Instance ID**.
  5. Enter a password for the sqlserver user. Take note of the password you create, because you'll need it later.
  6. In the **Choose region and zonal availability** section, select the **Single zone** option.
  7. Expand **Show configuration options**.
  8. Expand **Connections**.
  9. Clear **Public IP**.
  10. Select **Private IP**.
  11. Select **Private Service Access (PSA)**.
  12. From the **VPC Network** drop-down, select **default**.
  13. If you're using a new project, you're prompted by the message: **Network connection is not set up** , and a box titled **Network setup confirmation required** directs you to [VPC documentation for setting up PSA](https://docs.cloud.google.com/vpc/docs/configure-private-services-access).
     1. In the Google Cloud console, go to the **VPC networks** page: 

[Go to VPC networks](https://console.cloud.google.com/quickstart-private-ip)

     2. Select the **default** VPC network.
     3. Set a firewall rule that allows access to TCP port 22:
        1. Select the **Firewall** tab.
        2. At **VPC firewall rules** , select **Create VPC firewall rule**.
        3. Give the firewall rule a name.
        4. Under **Targets** , select **All instances in the network**.
        5. Under **Source IPv4 ranges** , enter `0.0.0.0/0`.
        6. Under **Protocols and Ports** , check **TCP** and then in the **Ports** box directly below, enter `22`.
        7. Select **Create**.
     4. [Allocate an IP address range](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#procedure):
        1. Select the **Private services access** tab.
        2. On the **Private services access** tab, select the **Allocated IP ranges for services** tab.
        3. Click **Allocate IP range**.
        4. Enter a **Name** and optionally a **Description** for the allocated range.
        5. To let Google select an available range, select **Automatic**.
        6. Enter a prefix length between `16` and 124 (the number of addresses allocated is equal to 2 to the (32 - prefix length).
        7. Click **Allocate** to create the allocated range.
     5. [Create a private connection](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#creating-connection):
        1. On the **Private services access** tab, switch to the **Private connections to services** tab.
        2. Click the **Create Connection** button.
        3. In the **Assigned allocation** drop-down in the **Create a private connection box** , select the name of the IP address range that you just created.
        4. Click **Connect**.
     6. When the connection has been created, return to where you were creating your Cloud SQL instance and click **Confirm connection**.
  14. When the PSA connection is successfully created, click **Create instance**.



You're taken to the instance Overview page as the new instance is being created.

After the instance creation is complete, scroll to the **Connect to this instance** section and save the instance's **Connection name**. The `connection name` is in the format `projectID:region:instanceID`. You'll use this `connection name` later when starting the Cloud SQL Auth Proxy.

## Create a Compute Engine VM

Follow these steps to create a VM: 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.
  3. Enter a **Name** for the instance.
  4. Select **Data protection** in the navigation pane and select **No backups**.
  5. Select **Security** in the navigation pane, and under **Access scopes** , select **Allow full access to all Cloud APIs**.
  6. Click **Create** and wait for the VM to finish being created.



## Open two SSH connections to the Compute Engine VM

We use two windows in the VM. The first window is used to install the sqlcmd client and the Cloud SQL Auth Proxy, get the instance connection name, and use this name to start the proxy. The second window is used to connect to the Cloud SQL instance through the proxy.

  1. Expand the **SSH** menu in the **Connect** column for your Compute Engine VM instance.
  2. Select **Open in browser window** to open SSH window #1. 

It might take a few seconds for the prompt in the window to become available for you.

  3. When the prompt appears, enter `pwd` to verify that you're in the `/home/$USER` directory. 

You'll install the sqlcmd client and the Cloud SQL Auth Proxy, and also start the Cloud SQL Auth Proxy, in this window.

  4. Select **Open in browser window** again to open SSH window #2. 

You'll use this window to connect to your Cloud SQL instance.




## Install the sqlcmd client

Use SSH window #1 for this step.

Install the SQL Server command-line tools (mssql-tools) for Ubuntu using [ these instructions](https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-setup-tools?view=sql-server-2017#ubuntu). 

## Install the Cloud SQL Auth Proxy

Use SSH window #1 for this step.

  1. Install `wget`: 
         
         sudo apt-get install wget
             

  2. Download the Cloud SQL Auth Proxy: 
         
         wget https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.8.2/cloud-sql-proxy.linux.amd64 \
         -O cloud-sql-proxy
           

  3. Make the Cloud SQL Auth Proxy executable: 
         
         chmod +x cloud-sql-proxy
           




## Start the Cloud SQL Auth Proxy

Use SSH window #1 for this step.

Start the Cloud SQL Auth Proxy so you can monitor its output. Replace `INSTANCE_CONNECTION_NAME` with the `connection name` you copied when you created the Cloud SQL instance.
    
    
    ./cloud-sql-proxy --private-ip INSTANCE_CONNECTION_NAME

**Note:** By default, the Cloud SQL Auth Proxy attempts to connect to your Cloud SQL instance using a public IPv4 address. If the instance has only private IP or the instance has both public and private IP configured, and you want the Cloud SQL Auth Proxy to use the private IP address, you must provide the `--private-ip` option when you start the Cloud SQL Auth Proxy.

If you see an error that the address is already in use, it means that a local instance of the database is running, and you need to stop it. Find the `SERVICE_NAME` by running the command `ps -ef | grep sqlcmd` and then run the command:
    
    
    sudo service SERVICE_NAME stop
       

When the Cloud SQL Auth Proxy starts successfully, a message similar to the following appears in the SSH window:
    
    
    Listening on 127.0.0.1:1433 for _myInstance_
    Ready for new connections
    

## Connect to your Cloud SQL instance

Use SSH window #2 for this step.

Run the following command, replacing `USER_NAME` with your SQL Server username.
    
    
    sqlcmd -S 127.0.0.1 -U USER_NAME

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

  3. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  4. Select your instance's name.

  5. Select **Delete** from the **More actions** menu.




## What's next

Based on your needs, you can learn more about [creating Cloud SQL instances](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance).

You also can learn about creating [SQL Server users](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users) and [databases](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-databases) for your Cloud SQL instance.

Additionally, you can learn about connecting to a Cloud SQL instance from other Google Cloud applications:

  * [From an application running on App Engine standard environment](https://docs.cloud.google.com/sql/docs/sqlserver/connect-app-engine)
  * [From an application running on GKE](https://docs.cloud.google.com/sql/docs/sqlserver/connect-kubernetes-engine)
  * [From Cloud Run](https://docs.cloud.google.com/sql/docs/sqlserver/connect-run)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
