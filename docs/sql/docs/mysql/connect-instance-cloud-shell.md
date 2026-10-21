---
url: https://docs.cloud.google.com/sql/docs/mysql/connect-instance-cloud-shell/
title: Quickstart: Connect to Cloud SQL for MySQL from Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:24.050864+00:00
---

# Quickstart: Connect to Cloud SQL for MySQL from Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/connect-instance-cloud-shell/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connect to Cloud SQL for MySQL from Cloud Shell

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/quickstart "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/quickstart "View this page for the SQL Server database engine")

This page shows you how to create and connect to a MySQL instance and perform basic SQL operations by using the Google Cloud console and a client. The resources created in this quickstart typically cost less than a dollar, assuming you complete the steps, including the cleanup, in a timely manner.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/freetrial?redirectPath=/?walkthrough_id=sql--mysql--quickstart)

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



## Connect to your instance

In this quickstart, we'll use the mysql client in Cloud Shell to connect to your instance. Cloud Shell is a remote, sandboxed environment. 

**Note:** Cloud Shell doesn't work with a private IP address. These instructions are only for an instance with a public IP address.

  1. Optional: If you're running a local instance of MySQL, stop it before connecting to your Cloud SQL instance. Otherwise, you might encounter errors such as `address already in use`.
  2. In the [Google Cloud console](https://console.cloud.google.com/), click the Cloud Shell icon (![Cloud Shell icon.](https://docs.cloud.google.com/static/sql/images/cloud-shell-icon.png)) in the upper right corner.

When Cloud Shell finishes initializing, a message, such as the following one, appears: 
         
         Welcome to Cloud Shell! Type "help" to get started.
         Your Cloud Platform project in this session is set to sample-project.
         Use "gcloud config set project [PROJECT_ID]" to change to a different project.
         username@sample-project:~ (sample-project)$
         

  3. Optional: If you haven't authorized [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) to access the Google Cloud Platform with your Google user credentials, then use the [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) command.
  4. At the Cloud Shell prompt, connect to your Cloud SQL instance. Use the [`gcloud sql connect`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/connect) command as follows. Replace the instance name if your instance name is different.
         
         gcloud sql connect myinstance --user=root

  5. In the dialog, click **Authorize** to authorize Cloud Shell to make API calls. 

The following message appears:
         
         Allowlisting your IP for incoming connection for 5 minutes...done.
         

This message indicates that the public IP address of your Cloud SQL instance is being allowed to have incoming connections. After this message, you're prompted to enter your password. 

  6. Enter your root password.

The `mysql` prompt appears.




## Create a database and upload data

  1. Create a SQL database on your Cloud SQL instance: 
         
         CREATE DATABASE guestbook;

  2. Insert sample data into the guestbook database: 
         
         USE guestbook;
         CREATE TABLE entries (guestName VARCHAR(255), content VARCHAR(255),
             entryID INT NOT NULL AUTO_INCREMENT, PRIMARY KEY(entryID));
             INSERT INTO entries (guestName, content) values ("first guest", "I got here!");
             INSERT INTO entries (guestName, content) values ("second guest", "Me too!");

  3. Retrieve the data: 
         
         SELECT * FROM entries;

The result is: 
         
         +--------------+-------------------+---------+
         | guestName    | content           | entryID |
         +--------------+-------------------+---------+
         | first guest  | I got here!       |       1 |
         | second guest | Me too!           |       2 |
         +--------------+-------------------+---------+
         2 rows in set (0.00 sec)
         mysql>
         




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

  * Learn about [creating Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/create-instance).

  * Learn about creating [MySQL users](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users) and [databases](https://docs.cloud.google.com/sql/docs/mysql/create-manage-databases) for your Cloud SQL instance.

  * See the [Cloud SQL pricing information](https://cloud.google.com/sql/pricing).

  * In this quickstart you connected to the instance by using Cloud Shell. Learn about all of the [connectivity options](https://docs.cloud.google.com/sql/docs/mysql/connect-overview#connection_options) in Cloud SQL. How you connect depends on your networking configuration, such as if your Cloud SQL instance has a public or private IP address. See how to configure your Cloud SQL instance with a [public IP](https://docs.cloud.google.com/sql/docs/mysql/configure-ip) and a [private IP](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip) address.

  * Learn about connecting to a Cloud SQL instance from other Google Cloud applications:

    * [From an application running on the App Engine standard environment](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine)
    * [From an application running on Compute Engine](https://docs.cloud.google.com/sql/docs/mysql/connect-compute-engine)
    * [From an application running on GKE](https://docs.cloud.google.com/sql/docs/mysql/connect-kubernetes-engine)
    * [From Cloud Run](https://docs.cloud.google.com/sql/docs/mysql/connect-run)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
