---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/reading-from-sqlserver/
title: Read from a SQL Server table \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:10.547480+00:00
---

# Read from a SQL Server table  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/reading-from-sqlserver/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Read from a SQL Server table Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up your data pipeline to read data from a Microsoft SQL Server table.

## Before you begin

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

  6. Enable the Cloud Data Fusion, BigQuery, Cloud Storage, and Dataproc APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=datafusion.googleapis.com,bigquery.googleapis.com,storage.googleapis.com,dataproc.googleapis.com)

  7. [ Create a Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-instance).
  8. Your SQL Server database must accept connections from Cloud Data Fusion. For security reasons, use a [private Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip).



### Open your Cloud Data Fusion instance

  1. In the Google Cloud console, go to the Cloud Data Fusion **Instances** page.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. In the **Actions** column for the instance, click **View instance** to open the instance in Cloud Data Fusion.




## Store your SQL Server password as a secure key

Add your SQL Server password as a secure key in your Cloud Data Fusion instance.

  1. From Cloud Data Fusion, click **System Admin**.

  2. Click the **Configuration** tab.

  3. Click **Make HTTP Calls**. ![Configuration.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/reading-from-sqlserver/config.png)

  4. Select **PUT**.

  5. In the path field, enter `namespaces/NAMESPACE_ID/securekeys/password `.

  6. In the **Body** field, enter `{"data":"password"}`. Replace password with your SQL Server password.

  7. Click **Send**.

![Password.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/reading-from-sqlserver/password.png)



The **Response** must have status code `200` to continue.

## Get the JDBC driver for SQL Server

You can get the driver from the Hub or in the Pipeline Studio in Cloud Data Fusion.

### Hub

  1. In the Cloud Data Fusion UI, click **Hub**.

  2. In the search bar, enter `SQL Server JDBC Driver` and select the driver.

  3. Click **Download**. Follow the download steps shown.

  4. Click **Deploy**. Upload the JAR file from the previous step.

  5. Click **Finish**.




### Pipeline Studio

  1. Go to [Microsoft.com](https://www.microsoft.com/en-us/download/details.aspx?id=11774).

  2. Choose your download and click **Download**.

  3. In Cloud Data Fusion, click _menu_ **Menu** and go to the **Pipeline Studio** page.

  4. Click  add  **Add**.

  5. For the driver, click **Upload**.

  6. Select the JAR file, located in the `jre7` folder.

  7. Click **Next**.

  8. To configure the driver, enter a **Name** and **Class name**.

  9. Click **Finish**.




## Deploy the SQL Server Plugin

  1. In Cloud Data Fusion, click **Hub**.

  2. In the search bar, enter `SQL Server Plugins`.

  3. Click **SQL server plugins**.

  4. Click **Deploy**.

  5. Click **Finish**.

  6. Click **Create a pipeline**.




## Connect to SQL Server

You can connect to SQL Server from Cloud Data Fusion in Wrangler or the Pipeline Studio.

### Wrangler

  1. In Cloud Data Fusion, click _menu_ **Menu** and go to the **Wrangler** page.

  2. Click **Add connection**.

An **Add connection** window opens.

  3. Click **SQL Server** to verify that the driver is installed. ![JAR uploaded.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/reading-from-sqlserver/jar-uploaded.png)

  4. Enter details in the required connection fields. In the **Password** field, select the secure key you stored previously. It ensures that your password is retrieved using [Cloud KMS](https://docs.cloud.google.com/kms/docs). ![Choose password.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/reading-from-sqlserver/choose-pw.png)

  5. To check that a connection can be established with the database, click **Test connection**.

  6. Click **Add connection**.




After your SQL Server database is connected and you've created a pipeline that reads from your SQL Server table, you can apply transformations and write your output to a sink.

### Pipeline Studio

  1. Open your Cloud Data Fusion instance and go to the **Pipeline Studio** page.

  2. Expand the **Source** menu and click **SQL Server**. ![SQL Server.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/reading-from-sqlserver/studio-sql-server.png)

  3. On the **SQL Server** node, click **Properties**.

![Properties.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/reading-from-sqlserver/properties.png)
  4. In the **Reference name** field, enter a name that identifies your SQL Server source.

  5. In the **Database** field, enter the name of the database to connect to.

  6. In the **Import query** field, enter the query to run. For example, `SELECT * FROM table WHERE $CONDITIONS`.

  7. Click **Validate**.

  8. Click close close.




After your SQL Server database is connected and you've created a pipeline that reads from your SQL Server table, add any desired transformations and write your output to a sink.

## What's next

  * Learn how to [read data from multiple SQL Server tables](https://docs.cloud.google.com/data-fusion/docs/how-to/reading-from-sqlserver-multi).
  * Learn more about [Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/overview).
  * Follow one of the [tutorials](https://docs.cloud.google.com/data-fusion/docs/tutorials).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
