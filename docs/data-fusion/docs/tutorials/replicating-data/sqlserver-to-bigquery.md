---
url: https://docs.cloud.google.com/data-fusion/docs/tutorials/replicating-data/sqlserver-to-bigquery/
title: Replicating data from SQL Server to BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:42.796271+00:00
---

# Replicating data from SQL Server to BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/tutorials/replicating-data/sqlserver-to-bigquery/




#  Replicating data from SQL Server to BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to create and deploy a job that continuously replicates changed data from a Microsoft SQL Server database to a BigQuery table. 

## Objectives

In this tutorial, you:

  1. Enable Change Data Capture (CDC) in your SQL Server database.
  2. Create and run a Cloud Data Fusion replication job.
  3. View the results in BigQuery.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/pricing)
  * [BigQuery](https://cloud.google.com/bigquery/pricing)
  * [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/pricing)
  * [Cloud Storage](https://docs.cloud.google.com/storage/pricing)
  * [Compute Engine](https://docs.cloud.google.com/compute/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When Replication runs, you're charged for the Managed Service for Apache Spark cluster and you incur processing costs for BigQuery. To optimize these costs, we strongly recommend using [BigQuery flat rate pricing](https://cloud.google.com/bigquery/pricing#flat_rate_pricing).

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Enable the Cloud Data Fusion, BigQuery, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=datafusion.googleapis.com,bigquery.googleapis.com,storage.googleapis.com&redirect=https%3A//console.cloud.google.com)

  4. [Create a public Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-instance) in version 6.3.0 or later. If you [create a private instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip), set up VPC network peering. 
     * When you create the instance, enable Replication by clicking **Add Accelerators** and selecting the **Replication** checkbox.
     * To enable it in an existing instance, see [Enable Replication](https://docs.cloud.google.com/data-fusion/docs/how-to/enable-replication#enable).

**Important:** You must enable Replication in your instance for it to appear in the Cloud Data Fusion web interface _menu_ **Menu** (see [Enable Replication](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading#replication)).

For more information about networking, see [Using HAProxy with Cloud Data Fusion to Navigate Complex Network Topologies](https://medium.com/@ammppp/using-haproxy-with-cloud-data-fusion-to-navigate-complex-network-topologies-fb3765bdbb2f).

### Required roles

To get the permissions that you need for this tutorial, see [Access control with IAM](https://docs.cloud.google.com/data-fusion/docs/access-control) and [Grant service account user permission](https://docs.cloud.google.com/data-fusion/docs/how-to/granting-service-account-permission).

## Optional: Set up a SQL Server VM instance

  1. [Create a SQL Server instance](https://docs.cloud.google.com/compute/docs/instances/sql-server/creating-sql-server-instances#start_sql_instance).

  2. Download the [AdventureWorks2017 (OLTP) database](https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver15&tabs=ssms) and [load the data](https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver15&tabs=ssms#restore-to-sql-server) into your SQL Server instance.


**Note:** If your SQL Server is [always on](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/overview-of-always-on-availability-groups-sql-server), see [Troubleshooting](https://docs.cloud.google.com/data-fusion/docs/support/troubleshooting#replication-sql-server) for additional steps.

## Enable CDC in your SQL Server database

For replication, enable Change Data Capture (CDC) on the [database](https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/enable-and-disable-change-data-capture-sql-server?view=sql-server-ver16#enable-for-a-database) and the [table](https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/enable-and-disable-change-data-capture-sql-server?view=sql-server-ver16#enable-for-a-table) you want to replicate.

**Note:** Contact your database administrator to grant permission to run the commands.If you defined custom data types in the table columns being replicated, the owner of the table must grant `EXECUTE` permissions for the custom data types to the database user who is specified in the replication job.

## Create and run a Cloud Data Fusion replication job

### Upload the JDBC driver

  1. [Download the SQL Server JDBC driver](https://learn.microsoft.com/en-us/sql/connect/jdbc/release-notes-for-the-jdbc-driver?view=sql-server-ver15#92) to your local machine.

  2. In the Cloud Data Fusion web interface, [upload the JDBC driver](https://docs.cloud.google.com/data-fusion/docs/how-to/using-jdbc-drivers#upload-driver). Use these values to configure the JDBC driver:

     * In the **Name** field, enter `sqlserver`.
     * In the **Class Name** field, enter `com.microsoft.sqlserver.jdbc.SQLServerDriver`.
     * In the **Version** field, keep the default.



### Create the job

  1. In the Cloud Data Fusion web interface, click **Replication**.

  2. Click add_circle **Create a replication job**.

  3. On the **Create new replication job** page, specify a replication job **Name** and click **Next**.

  4. Configure the source:

     1. Select **Microsoft SQL Server** as the source.
     2. For **Host** , enter the hostname of the SQL Server to read from.
     3. For **Port** , enter the port to use to connect to the SQL Server: `1433`.
     4. For **JDBC Plugin Name** , select `sqlserver`or the name you specified when you configured the JDBC driver.
     5. For **Database name** , enter `AdventureWorks2017`.
     6. In the **Credentials** section, enter your username and password to access the SQL Server.
  5. Click **Next**.

  6. Configure the target:

     1. Select the BigQuery target.
     2. The **Project ID** and **Service Account Key** are automatically detected. Keep the default values.
     3. Optional: In the **Advanced** section, you can configure the name and location of the Cloud Storage bucket, the load interval, the staging table prefix, and the behavior when tables or databases are dropped.
  7. Click **Next**.

  8. If the connection is successful, a list of `AdventureWorks2017` tables is displayed. For this tutorial, select a few tables and events, such as `Insert`, `Update`, and `Delete` events.

**Note:** To proceed, you must [enable CDC](https://docs.cloud.google.com/data-fusion/docs/tutorials/replicating-data/sqlserver-to-bigquery#enable_cdc_in_your_sql_server_database) on the selected tables.
  9. Optional: Configure the advanced properties. For this tutorial, you can accept the default settings.

  10. Click **Next**.

  11. On the **Review assessment** page, click **View mappings** by any of the tables for an assessment of schema issues, missing features, or connectivity issues that might occur during replication. Issues must be resolved before you can proceed. For this tutorial, if any of the tables have issues, go back to the step where you selected tables and select a table or event without issues.

For more information about data type conversions from the source database to the BigQuery destination, see [Replication data types](https://docs.cloud.google.com/data-fusion/docs/reference/replication-data-types#sql-server).

  12. Click **Back**.

  13. Click **Next**.

  14. Review the summary replication job details, and then click **Deploy replication job**.


**Note:** This tutorial uses the OLTP database [`AdventureWorks2017`](https://docs.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver15&tabs=ssms), which has [primary keys](https://en.wikipedia.org/wiki/Primary_key) on all tables. To replicate a different database, such as the Data Warehouse DB `AdventureWorksDW2017`, either exclude the tables that don't have primary keys or add primary keys to those tables.

### Start the job

  * From the **replication job details** page, click **Start**.



The replication job transitions from **Provisioning** to **Starting** to **Running** state. In the running state, the replication job loads an initial snapshot of the table data that you selected (for example, the People table) into BigQuery. In this state, the state of the People table is listed as **Snapshotting**. After the initial snapshot is loaded into BigQuery, any changes made to the People table are replicated to BigQuery. The state of the table is listed as **Replicating**.

### Monitor the job

You can start and stop the replication job, review its configuration and logs, and monitor your replication job.

You can monitor replication job activities from the **Replication job details** page.

  1. From the **Replication** page, click the replication job **Name**.

  2. Click **Monitoring**.




## View the results in BigQuery

The replication job creates a replicated dataset and table in BigQuery, with names inherited from the corresponding SQL Server database and table names.

**Note:** If your source database name doesn't follow the [BigQuery dataset naming conventions](https://docs.cloud.google.com/bigquery/docs/datasets), or if you have naming conflicts when you replicate multiple datasets into a single BigQuery dataset, specify aliases in the BigQuery target properties.

  1. Open [BigQuery](https://console.cloud.google.com/bigquery) in the Google Cloud console.

  2. In the left panel, click the project name to expand a list of datasets.

  3. Select the `adventureworks2017` dataset, and then select a table to view.




For more information, see the [BigQuery documentation](https://docs.cloud.google.com/bigquery/docs).

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

After you've finished the tutorial, delete the resources you created on Google Cloud.

### Delete the VM instance

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the checkbox for the instance that you want to delete. 
  3. To delete the instance, click more_vert **More actions** , click **Delete** , and then follow the instructions. 



### Delete the Cloud Data Fusion instance

Follow the [ instructions to delete your Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/delete-instance).

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Learn more about [Replication](https://docs.cloud.google.com/data-fusion/docs/concepts/replication) in Cloud Data Fusion.
  * Refer to the [Replication API reference](https://docs.cloud.google.com/data-fusion/docs/reference/replication-ref).
  * Work through the tutorial for [Replicating data from MySQL to BigQuery](https://docs.cloud.google.com/data-fusion/docs/tutorials/replicating-data/mysql-to-bigquery).
  * Work through the tutorial [Replicating data from Oracle to BigQuery](https://docs.cloud.google.com/data-fusion/docs/tutorials/replicating-data/oracle-to-bigquery).



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
