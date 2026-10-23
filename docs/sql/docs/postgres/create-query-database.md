---
url: https://docs.cloud.google.com/sql/docs/postgres/create-query-database/
title: Quickstart: Create and query a Cloud SQL for PostgreSQL database using the Google Cloud console \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:43.247669+00:00
---

# Quickstart: Create and query a Cloud SQL for PostgreSQL database using the Google Cloud console  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/create-query-database/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and query a Cloud SQL for PostgreSQL database using the Google Cloud console

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/create-query-database "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/create-query-database "View this page for the SQL Server database engine")

Learn how to create and query a Cloud SQL for PostgreSQL database using the Google Cloud console. This quickstart is intended for database practitioners seeking a quick introduction to Cloud SQL for PostgreSQL. The quickstart takes you through the steps required to complete the following tasks:

  * Create a Cloud SQL for PostgreSQL instance
  * Create a database
  * Create a schema
  * Create a table
  * Insert data
  * Query the data that you inserted
  * Clean up your resources



As you follow along, keep the default values for settings unless otherwise specified.

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

  5. Enable the Cloud SQL, Cloud SQL Admin, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=sql-component.googleapis.com,sqladmin.googleapis.com,compute.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Cloud SQL, Cloud SQL Admin, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=sql-component.googleapis.com,sqladmin.googleapis.com,compute.googleapis.com)




### Required roles

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the [Cloud SQL Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a Cloud SQL for PostgreSQL instance

Create an instance in the Google Cloud console using the following settings. For all other settings, keep the default.

**Note:** You might be eligible for a [free trial instance](https://docs.cloud.google.com/sql/docs/postgres/free-trial-instance).

  1. Go to the Cloud SQL Instances page in the Google Cloud console.  
[Go to the Cloud SQL Instances page](https://console.cloud.google.com/sql/instances)
  2. Click **Create Instance**.
  3. Click **Choose Cloud SQL for PostgreSQL**.
  4. For **Choose a Cloud SQL edition** , choose **Enterprise**.
  5. For **Edition preset** , select **Sandbox**.
  6. For **Instance ID** , enter `quickstart-instance`.
  7. Enter a password for the default user account and save it for future use.
  8. Choose a region near you.
  9. For **Zonal availability** , select **Single zone**.
  10. Click **Create instance** , and then wait until the instance initializes and starts. The initialization process can take more than five minutes.

**Tip:** Check the _long-running operation drawer_ at the bottom of the Google Cloud console to monitor the status of your instance-creation operation.

## Create a database

After `quickstart-instance` has been created, you can create a database in your Cloud SQL for PostgreSQL instance.

  1. In the instance navigation menu, click **Databases**.
  2. Click **Create a database**.
  3. In the **Database Name** text field, enter `quickstartdb`.
  4. Click **Create**.



## Add a user

Before you can read or write to the database, you must create a database user that is different from the root user.

  1. In the instance navigation menu, click **Users**.
  2. Click **Add user account**.
  3. In the pane that opens, select **Built-in authentication**.
  4. In the **User name** field, enter `quickstart-user`.
  5. Enter a password for the new user. Save this password for future use. 
  6. Click **Add**.



## Create a schema

After you've created your instance and database, you can navigate to **Cloud SQL Studio** and use the query editor to create a schema.

  1. In the instance navigation menu, click **Cloud SQL Studio**. A dialog is displayed.
  2. In the **Database** drop-down, choose **quickstartdb**.
  3. Select **Built-in database authentication**. 
  4. In the **User** drop-down, select **quickstart-user**.
  5. In the **Password** field, enter the password that you chose for the user in the Add a user section. 
  6. Click **Authenticate**. Cloud SQL Studio opens.
  7. Click **Untitled Query** to open the query editor.
  8. Paste the following code into the query editor:
         
         CREATE SCHEMA IF NOT EXISTS "myschema";
         

  9. Optional: to correctly format the SQL statement, click **Format**.

  10. Click **Run**. The results pane displays a success message.




## Create a table

Now create a table using the schema that you created.

  1. Click **New tab** add_box to open a new query editor tab.
  2. Paste the following statement into the query editor:
         
         CREATE TABLE IF NOT EXISTS
           "myschema"."quickstart_table" ( "UserId" SERIAL
           PRIMARY KEY
             ,
             "FirstName" VARCHAR(255),
             "LastInitial" VARCHAR(1),
             "BirthDate" DATE );
         

  3. Optional: to correctly format the SQL statement, click **Format**.

  4. Click **Run**. The results pane displays a success message.




The `quickstartdb` database now has a table with the columns to store the following data:

  * An automatically incrementing user ID column that is configured to be the table's primary key
  * First name
  * Last initial
  * Birthdate



## Insert data

To populate the `quickstart_table` table with some data, take the following steps:

  1. Click **New tab** add_box to open a new query editor tab.
  2. Paste the following statement into the query editor:
         
         INSERT INTO
           "myschema"."quickstart_table" ("FirstName",
             "LastInitial",
             "BirthDate")
         VALUES
           ('Yuri', 'Z', '1999-05-24'),
           ('Cruz', 'S', '1978-11-01'),
           ('Kai', 'D', '1965-12-09'),
           ('Luka', 'L', '2003-04-19'),
           ('Taylor', 'S', '2001-01-31');
         

  3. Optional: to format the SQL statement correctly, click **Format**.

  4. Click **Run**. The results pane displays a success message.




## Query the database

Now you can run queries against the data in the table that you created.

### Select all records

To retrieve all records in the table, do the following:

  1. Click **New tab** add_box to open a new query editor tab.

  2. Paste the following statement into the query editor:
         
         SELECT
           *
         FROM
           "myschema"."quickstart_table"
         

  3. Click **Run**.

The query results are similar to the following:

UserID | FirstName | LastInitial | BirthDate  
---|---|---|---  
1 | Yuri | Z | 1999-05-24 00:00:00  
2 | Cruz | S | 1978-11-01 00:00:00  
3 | Kai | D | 1965-12-09 00:00:00  
4 | Luka | L | 2003-04-19 00:00:00  
5 | Taylor | S | 2001-01-31 00:00:00  



### Run a filtered select statement

To retrieve the user ID and first name of users born on or after January 1, 2000, specify the columns and use a `WHERE` clause:

  1. Click **New tab** add_box to open a new query editor tab.
  2. Paste the following statement into the query editor:
         
         SELECT
           "UserId",
           "FirstName"
         FROM
           "myschema"."quickstart_table"
         WHERE
           "BirthDate" > '1999-12-31';
         

  3. Click **Run**.

The query results are similar to the following:

UserID | FirstName  
---|---  
4 | Luka  
5 | Taylor  



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

Disable deletion protection and then delete the quickstart instance:

  1. In the instance navigation menu, click **Overview**.
  2. Click **Edit**.
  3. Expand the **Data Protection** section.
  4. In **Instance deletion protection** , deselect all options.
  5. Click **Save. Delete** is now selectable.
  6. Click **Delete**. A dialog appears.
  7. In the **Instance ID** field, enter `quickstart-instance`.
  8. Click **Delete**.



## What's next

  * [Configure public IP](https://docs.cloud.google.com/sql/docs/postgres/configure-ip)
  * [Cloud SQL for PostgreSQL features](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
