---
url: https://docs.cloud.google.com/sql/docs/sqlserver/connect-instance-auth-proxy/
title: Quickstart: Connect to Cloud SQL for SQL Server using the Cloud SQL Auth Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:49.753284+00:00
---

# Quickstart: Connect to Cloud SQL for SQL Server using the Cloud SQL Auth Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/connect-instance-auth-proxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connect to Cloud SQL for SQL Server using the Cloud SQL Auth Proxy

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/quickstart-proxy-test "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/quickstart-proxy-test "View this page for the PostgreSQL database engine") | SQL Server

This page shows you how to connect to Cloud SQL from a local test environment using the Cloud SQL Auth Proxy. The [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/sql-proxy) provides secure access to your Cloud SQL instance without the need for authorized networks or for configuring SSL. By using the Cloud SQL Auth Proxy, you can connect to your Cloud SQL instance securely.

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

In this quickstart, you use the Google Cloud console. To use the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), curl, or PowerShell, see [Create instances](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance).

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click **Create instance**.
  3. From the **Create instance** menu, select **New instance**.
  4. Click **Choose SQL Server**.
  5. In the **Instance ID** field, enter `myinstance`.
  6. In the **Password** field, enter a password for the `sqlserver` user.
  7. Click **Create instance**.

You're returned to the instances list. You can click the new instance right away to see the details, but it won't be available for other operations until it initializes and starts.

**Note:** In this example, the instance is created using default settings, including a public IP address.



### Debian/Ubuntu

For Debian/Ubuntu, install the applicable SQL Server command-line tools using [ these instructions](https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-setup-tools?view=sql-server-2017#ubuntu). 

### CentOS/RHEL

For CentOS/RHEL, install the applicable SQL Server command-line tools using [ these instructions](https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-setup-tools?view=sql-server-2017#install-tools-on-rhel-7). 

### openSUSE

For openSUSE, install the applicable SQL Server command-line tools using [ these instructions](https://docs.microsoft.com/en-us/sql/linux/quickstart-install-connect-suse?view=sql-server-2017#tools). 

### Other platforms

See the [ landing page](https://docs.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server-database-engine?view=sql-server-2017) for installing SQL Server, as well as the [ SQL Server downloads page](https://www.microsoft.com/en-us/sql-server/sql-server-downloads). 

## Install the Cloud SQL Auth Proxy client

For installation, see [ Installing the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/connect-auth-proxy#install).

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
    
    
    Listening on 127.0.0.1:1433 for INSTANCE_CONNECTION_NAME
    Ready for new connections
    

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




## What's next

  * See how to [troubleshoot information for the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/connect-auth-proxy#troubleshooting).

  * Learn more [about the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/sql-proxy).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
