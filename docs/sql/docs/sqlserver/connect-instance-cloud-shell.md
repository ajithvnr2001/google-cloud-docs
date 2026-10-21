---
url: https://docs.cloud.google.com/sql/docs/sqlserver/connect-instance-cloud-shell/
title: Quickstart: Connect to Cloud SQL for SQL Server from SSMS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:24.700802+00:00
---

# Quickstart: Connect to Cloud SQL for SQL Server from SSMS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/connect-instance-cloud-shell/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connect to Cloud SQL for SQL Server from SSMS

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/quickstart "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/quickstart "View this page for the PostgreSQL database engine") | SQL Server

This page shows you how to create and connect to a SQL Server instance and perform basic SQL operations by using the Google Cloud console and a client. The resources created in this quickstart typically cost less than a dollar, assuming you complete the steps, including the cleanup, in a timely manner.

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



## Connect to your instance by using SQL Server Management Studio

**Note:** SQL Server Management Studio (SSMS) is a Windows-based, integrated environment. Review the [ SSMS documentation](https://docs.microsoft.com/en-us/sql/ssms/sql-server-management-studio-ssms?view=sql-server-2017) if needed, including for [ Connecting to a SQL Server instance](https://docs.microsoft.com/en-us/sql/ssms/tutorials/connect-query-sql-server?view=sql-server-2017). Alternatively, you can use other database administration tools.

  1. Optional: If you're running a local instance of SQL Server, stop it before connecting to your Cloud SQL instance. Otherwise, you might encounter errors such as `address already in use`.
  2. Install the [](https://docs.cloud.google.com/sdk/docs)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). The [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) provides the gcloud CLI to interact with Cloud SQL and other Google Cloud services. The gcloud CLI uses the Admin API to access Cloud SQL, so you must [ Enable the Admin API](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api#enabling_the_api) before using the gcloud CLI to access Cloud SQL.
  3. In a bash shell command prompt or in Windows PowerShell, run the following command to initialize the gcloud CLI: 
         
         gcloud init
           

  4. Run the following command to authenticate the gcloud CLI: 
         
         gcloud auth login
           

  5. Download and install the Cloud SQL Auth Proxy (see [ Installing the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/connect-auth-proxy#install)). Note the location of the Cloud SQL Auth Proxy because you will run the Cloud SQL Auth Proxy in next step.
  6. Run the Cloud SQL Auth Proxy by using a bash shell command prompt (or by using Windows PowerShell). Specifically, run the following command, replacing `Instance-connection-name` with the corresponding value from the Google Cloud console's Overview tab (for your instance): 
         
         ./cloud-sql-proxy INSTANCE_CONNECTION_NAME
           




For more information about installing and using the Cloud SQL Auth Proxy, see [About the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/sql-proxy).

As described in the next section, now you can connect to your SQL Server instance by using SSMS and the localhost IP address.

### Connect using the SSMS Object Explorer

  1. In SSMS, select **Connect Object Explorer** from the **File** menu.

![Selecting the Object Explorer](https://docs.cloud.google.com/static/sql/images/quickstart-sql-server-0.png)

  2. Enter the following values in the **Connection** dialog:

     1. For Server Type, enter **Database Engine**.
     2. For Server Name, enter 127.0.0.1 as the IP address of your SQL Server instance.
     3. For Authentication, enter **SQL Server Authentication**.
     4. For Login, enter **sqlserver**.
     5. For Password, enter the password used when the instance was created.
  3. Click the **Connect** button.



## Create a database and upload data

  1. In the SSMS Object Explorer window, right-click the **Databases** node under your instance and select **New Database**.

![Selecting New Database](https://docs.cloud.google.com/static/sql/images/quickstart-sql-server-1.png)

  2. Enter **testdb** for the **Database name** and click the **OK** button.

![Enter database name of testdb in the dialog](https://docs.cloud.google.com/static/sql/images/quickstart-sql-server-2.png)

  3. Under the newly created **testdb** database, right-click the **Tables** node and select **New > Table**.

![Select New Table](https://docs.cloud.google.com/static/sql/images/quickstart-sql-server-3.png)

  4. Enter the following values in the **Create table** dialog:

     1. In the **Properties** window, for **Identity > Name**, enter **guestbook**.
     2. For the first **Column Name** , enter **entryID** , set its Data Type to **int** , and clear the **Allow Nulls** checkbox. 
        1. In the **Column Properties** window, expand the **Identity Specification** item and set **(Is Identity)** to **Yes**.
     3. For the second **Column Name** , enter **guestname** and set its Data Type to varchar(255).
     4. For the third **Column Name** , enter **content** and set its Data Type to varchar(255).

![Enter values for a table](https://docs.cloud.google.com/static/sql/images/quickstart-sql-server-4.png)

  5. Click the **File** menu and select **Save guestbook**.

![Save the guestbook table](https://docs.cloud.google.com/static/sql/images/quickstart-sql-server-5.png)

  6. Right-click the **testdb** table under **Databases** and select **New Query**.

![For testdb, select New Query](https://docs.cloud.google.com/static/sql/images/quickstart-sql-server-6.png)

  7. Enter the following two INSERT statements into the **SQL query** text window and click the **Execute** button.
         
         INSERT INTO guestbook (guestName, content) values ('first guest', 'I got here!');
         
         INSERT INTO guestbook (guestName, content) values ('second guest', 'Me too!');

As an example: ![Enter two Insert statements](https://docs.cloud.google.com/static/sql/images/quickstart-sql-server-7.png)

  8. Expand the **Tables** item under the **Databases > testdb** item in the **Object Explorer** window. Right-click the **dbo.guestbook** table and choose **Select Top 1000 Rows**.

![Select the top rows](https://docs.cloud.google.com/static/sql/images/quickstart-sql-server-8.png)




The two records you inserted are displayed as **Results** , along with the SQL `SELECT` statement used to query the records.

![View the results of your query](https://docs.cloud.google.com/static/sql/images/quickstart-sql-server-9.png)

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

  * Learn about [creating Cloud SQL instances](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance).

  * Learn about creating [SQL Server users](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users) and [databases](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-databases) for your Cloud SQL instance.

  * See the [Cloud SQL pricing information](https://cloud.google.com/sql/pricing).

  * In this quickstart you connected to the instance by using Cloud Shell. Learn about all of the [connectivity options](https://docs.cloud.google.com/sql/docs/sqlserver/connect-overview#connection_options) in Cloud SQL. How you connect depends on your networking configuration, such as if your Cloud SQL instance has a public or private IP address. See how to configure your Cloud SQL instance with a [public IP](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ip) and a [private IP](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-ip) address.

  * Learn about connecting to a Cloud SQL instance from other Google Cloud applications:

    * [From an application running on the App Engine standard environment](https://docs.cloud.google.com/sql/docs/sqlserver/connect-app-engine)
    * [From an application running on Compute Engine](https://docs.cloud.google.com/sql/docs/sqlserver/connect-compute-engine)
    * [From an application running on GKE](https://docs.cloud.google.com/sql/docs/sqlserver/connect-kubernetes-engine)
    * [From Cloud Run](https://docs.cloud.google.com/sql/docs/sqlserver/connect-run)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
