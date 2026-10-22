---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/reading-from-sqlserver-multi/
title: Read from multiple Microsoft SQL Server tables \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:10.853199+00:00
---

# Read from multiple Microsoft SQL Server tables  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/reading-from-sqlserver-multi/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Read from multiple Microsoft SQL Server tables Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to read multiple tables from a Microsoft SQL Server database, using the **Multi Table** [source](https://docs.cloud.google.com/data-fusion/docs/concepts/overview#source). Use the Multi Table source when you want your pipeline to read from multiple tables. If you want your pipeline to read from a single table, see [Reading from a SQL Server table](https://docs.cloud.google.com/data-fusion/docs/how-to/reading-from-sqlserver).

The Multi Table source outputs data with multiple schemas and includes a table name field that indicates the table from which the data came. When using the Multi Table source, use one of the multi table [sinks](https://docs.cloud.google.com/data-fusion/docs/concepts/overview#sink), **BigQuery Multi Table** or **GCS Multi File**.

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

  6. Enable the Cloud Data Fusion, Cloud Storage, BigQuery, and Dataproc APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=datafusion.googleapis.com,bigquery.googleapis.com,storage.googleapis.com,dataproc.googleapis.com)

  7. [ Create a Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-instance).
  8. Ensure that your SQL Server database can accept connections from Cloud Data Fusion. To do this securely, we recommend that you [create a private Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip).



### View your Cloud Data Fusion instance

When using Cloud Data Fusion, you use both the Google Cloud console and the separate Cloud Data Fusion UI. In the Google Cloud console, you can create a Google Cloud project, and create and delete Cloud Data Fusion instances. In the Cloud Data Fusion UI, you can use the various pages, such as **Studio** or **Wrangler** , to use Cloud Data Fusion features.

  1. In the Google Cloud console, go to the Cloud Data Fusion page.

  2. To open the instance in the Cloud Data Fusion Studio, click **Instances** , and then click **View instance**.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)




## Store your SQL Server password as a secure key

Add your SQL Server password as a secure key to encrypt on your Cloud Data Fusion instance. Later in this guide, you will ensure that your password is retrieved using [Cloud KMS](https://docs.cloud.google.com/kms/docs).

  1. In the top-right corner of any Cloud Data Fusion page, click **System Admin**.

  2. Click the **Configuration** tab.

  3. Click **Make HTTP Calls**. ![Configuration.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/reading-from-sqlserver/config.png)

  4. In the dropdown menu, choose **PUT**.

  5. In the path field, enter `namespaces/NAMESPACE_ID/securekeys/PASSWORD`.

  6. In the **Body** field, enter `{"data":"SQL_SERVER_PASSWORD"}`.

  7. Click **Send**.

![Password.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/reading-from-sqlserver/password.png)



Ensure that the **Response** you get is status code `200`.

## Get the JDBC driver for SQL Server

### Using the Hub

  1. In the Cloud Data Fusion UI, click **Hub**.

  2. In the search bar, enter `Microsoft SQL Server JDBC Driver`.

  3. Click **Microsoft SQL Server JDBC Driver**.

  4. Click **Download**. Follow the download steps shown.

  5. Click **Deploy**. Upload the JAR file from the previous step.

  6. Click **Finish**.




### Using Studio

  1. Visit [Microsoft.com](https://www.microsoft.com/en-us/download/details.aspx?id=11774).

  2. Choose your download and click **Download**.

  3. In the Cloud Data Fusion UI, click menu **Menu** and navigate to the **Studio** page.

  4. Click add **Add**.

  5. Under **Driver** , click **Upload**.

  6. Upload the JAR file downloaded in step 2.

  7. Click **Next**.

  8. Configure the driver by entering a **Name**.

  9. In the **Class name** field, enter `com.microsoft.sqlserver.jdbc.SQLServerDriver`.

  10. Click **Finish**.




## Deploy the Multiple Table Plugins

  1. In the Cloud Data Fusion web UI, click **Hub**.

  2. In the search bar, enter `Multiple table plugins`.

  3. Click **Multiple Table Plugins**.

![Password.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/reading-from-sqlserver/multi-table-plugins.png)
  4. Click **Deploy**.

  5. Click **Finish**.

  6. Click **Create a Pipeline**.




## Connect to SQL Server

  1. In the Cloud Data Fusion UI, click menu **Menu** and navigate to the **Studio** page.

  2. In **Studio** , expand the **Source** menu.

  3. Click **Multiple Database Tables**.

![Multiple tables.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/reading-from-sqlserver/studio-multi-tables.png)
  4. Hold the pointer over the **Multiple Database Tables** node and click **Properties**.

![Properties.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/reading-from-sqlserver/properties-multiple-tables.png)
  5. In the **Reference name** field, specify a reference name that will be used to identify your SQL Server source.

  6. In the **JDBC Connection String** field, enter the JDBC connection string. For example, `jdbc:sqlserver://mydbhost:1433`. For more information, see [Building the connection URL](https://docs.microsoft.com/en-us/sql/connect/jdbc/building-the-connection-url).

  7. Enter the **JDBC Plugin Name** , **Database User Name** , and **Database User Password**.

  8. Click **Validate**.

  9. Click close **Close**.




## Connect to BigQuery or Cloud Storage

  1. In the Cloud Data Fusion UI, click menu **Menu** and navigate to the **Studio** page.

  2. Expand **Sink**.

  3. Click **BigQuery Multi Table** or **GCS Multi File**.

  4. Connect the **Multiple Database Tables** node with **BigQuery Multi Table** or **GCS Multi File**.

![Connect sink.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/reading-from-sqlserver/connect-sink.png)
  5. Hold the pointer over the **BigQuery Multi Table** or **GCS Multi File** node, click **Properties** , and configure the sink.

For more information, see [Google BigQuery Multi Table Sink](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/464912385/Google+BigQuery+Multi+Table+Sink) and [Google Cloud Storage Multi File Sink](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/464945223/Google+Cloud+Storage+Multi+File+Sink).

  6. Click **Validate**.

  7. Click close **Close**.




## Run preview of the pipeline

  1. In the Cloud Data Fusion UI, click menu **Menu** and navigate to the **Studio** page.

  2. Click **Preview**.

  3. Click **Run**. Wait for the preview to finish successfully.




## Deploy the pipeline

  1. In the Cloud Data Fusion UI, click menu **Menu** and navigate to the **Studio** page.

  2. Click **Deploy**.




## Run the pipeline

  1. In the Cloud Data Fusion UI, click menu **Menu**.

  2. Click **List**.

  3. Click the pipeline.

  4. On the pipeline details page, click **Run**.




## What's next

  * Learn more about [Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/overview).
  * Follow one of the [tutorials](https://docs.cloud.google.com/data-fusion/docs/tutorials).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
