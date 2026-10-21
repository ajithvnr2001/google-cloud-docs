---
url: https://docs.cloud.google.com/data-fusion/docs/tutorials/replicating-data/mysql-to-bigquery/
title: Replicating data from MySQL to BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:31.714845+00:00
---

# Replicating data from MySQL to BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/tutorials/replicating-data/mysql-to-bigquery/




#  Replicating data from MySQL to BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to create and deploy a job that continuously replicates changed data from a MySQL database to a BigQuery table. 

## Objectives

In this tutorial, you:

  1. Deploy your MySQL database on Compute Engine.
  2. Set up your MySQL database to enable replication.
  3. Create and run a Cloud Data Fusion replication job.
  4. View the results in BigQuery. 



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/pricing)
  * [BigQuery](https://cloud.google.com/bigquery/pricing)
  * [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/pricing)
  * [Cloud Storage](https://docs.cloud.google.com/storage/pricing)
  * [Compute Engine](https://docs.cloud.google.com/compute/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When Replication runs, you're charged for the Managed Service for Apache Spark cluster and you incur processing costs for BigQuery. To optimize these costs, we strongly recommend that you use [BigQuery flat rate pricing](https://cloud.google.com/bigquery/pricing#flat_rate_pricing).

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

### Required roles

To get the permissions that you need for this tutorial, see [Access control with IAM](https://docs.cloud.google.com/data-fusion/docs/access-control) and [Grant service account user permission](https://docs.cloud.google.com/data-fusion/docs/how-to/granting-service-account-permission).

## Install MySQL in Compute Engine

  1. [Download](https://hub.docker.com/r/mysql/mysql-server/) a MySQL Server Docker image.

  2. [Upload](https://docs.cloud.google.com/artifact-registry/docs/docker/pushing-and-pulling) your Docker image to the Artifact Registry.

  3. [Deploy](https://docs.cloud.google.com/compute/docs/containers/deploying-containers) your Docker image on a new VM instance.

**Note:** To deploy the image in the new VM instance, the Compute Engine service must have the [Artifact Registry Reader role](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`).
  4. On the Compute Engine **Disks** page, change the disk size to `500 GB` and restart the VM.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  5. [Create a firewall](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules) for the VM instance.

  6. Install the [Sakila sample database](https://dev.mysql.com/doc/sakila/en/sakila-installation.html).




## Enable replication in your MySQL database

To enable replication, [set up Change Data Capture (CDC) in MySQL](https://github.com/data-integrations/database-delta-plugins/blob/develop/mysql-delta-plugins/docs/mysql-cdcSource.md#setting-up-mysql).

You may need to contact your database administrator to obtain permissions to run the commands.

## Create and run a Cloud Data Fusion replication job

### Upload the JDBC driver

**Note:** Use JDBC driver version 8 or later.

  1. [Download the MySQL JDBC driver](https://dev.mysql.com/downloads/connector/j/) (version 8 or higher) to your local machine.

  2. In the Cloud Data Fusion web interface, [upload the JDBC driver](https://docs.cloud.google.com/data-fusion/docs/how-to/using-jdbc-drivers#upload-driver).

Use these values to configure the JDBC driver:

     * In the **Name** field, enter `mysql`.
     * In the **Version** field, keep the default.
     * In the **Class Name** field, enter `com.mysql.jdbc.Driver`.



### Create the job

  1. In the Cloud Data Fusion web interface, click **Replication**.

  2. Click add_circle **Create a replication job**.

  3. On the **Create new replication job** page, specify a replication job **Name** and click **Next**.

  4. Configure the source:

     1. Select **MySQL** as the source.
     2. For **Host** , enter the hostname of the MySQL server to read from.
     3. For **Port** , enter the port to use to connect to the MySQL server: `3306`.
     4. For **JDBC Plugin Name** , select `mysql` or the name you specified when you configured the JDBC driver.
     5. For **Database Name** , enter `sakila`.
     6. In the **Credentials section** , enter your username and password to access the MySQL server.
  5. Click **Next**.

  6. Configure the target:

     1. Select the BigQuery target.
     2. The **Project ID** and **Service Account Key** are automatically detected. Keep the default values.
     3. Optional: In the **Advanced** section, configure the staging bucket's name, location, load interval, staging table prefix, and behavior when tables or databases are dropped.
  7. Click **Next**.

  8. If the connection is successful, a list of Sakila sample database tables is displayed. For this tutorial, select a few tables and events to replicate, such as Insert, Update, and Delete events.

  9. Optional: Configure the advanced properties. For this tutorial, you can use the default settings.

  10. Click **Next**.

  11. On the **Review assessment** page, click **View mappings** by any of the tables for an assessment of schema issues, missing features, or connectivity issues that might occur during replication. If issues occur, they must be resolved before you can proceed. For this tutorial, if any of the tables have issues, go back to the step where you selected tables and choose tables or events (Inserts, Updates, or Deletes) without issues.

For more information about data type conversions from the source database to the BigQuery destination, see [Replication data types](https://docs.cloud.google.com/data-fusion/docs/reference/replication-data-types#mysql).

  12. Click **Next**.

  13. Review the summary replication job details, and then click **Deploy replication job**.




### Start the job

  * On the **Replication job details** page, click **Start**.



The replication job transitions from **Provisioning** to **Starting** to **Running** state. In the running state, the replication job loads an initial snapshot of the table data that you selected into BigQuery. In this state, the state of the table is listed as **Snapshotting**. After the initial snapshot is loaded into BigQuery, any changes made to the table are replicated to BigQuery, and the state of the table is listed as **Replicating**.

### Monitor the job

You can start and stop the replication job, review its configuration and logs, and monitor your replication job.

You can monitor replication job activities from the **Replication job details** page.

  1. From the **Replication** page, click the replication job **Name**.

  2. Click **Monitoring**.




## View the results in BigQuery

The replication job creates a replicated dataset and table in BigQuery, with names inherited from the corresponding MySQL database and table names.

**Note:** If your source database name doesn't follow the [BigQuery dataset naming conventions](https://docs.cloud.google.com/bigquery/docs/datasets), or if you have naming conflicts when you replicate multiple datasets into a single BigQuery dataset, specify aliases in the BigQuery target properties.

  1. In the Google Cloud console, go to the BigQuery page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the left panel, select your project name to expand a list of datasets.

  3. To view the results, select the `sakila` dataset and select a table.




For more information, see the [BigQuery documentation](https://docs.cloud.google.com/bigquery/docs).

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

After you've finished the tutorial, clean up the resources you created on Google Cloud so they won't take up quota and you won't be billed for them in the future. The following sections describe how to delete or turn off these resources.

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
  * Work through the tutorial for [Replicating data from SQL Server to BigQuery](https://docs.cloud.google.com/data-fusion/docs/tutorials/replicating-data/sqlserver-to-bigquery).
  * Work through the tutorial [Replicating data from Oracle to BigQuery](https://docs.cloud.google.com/data-fusion/docs/tutorials/replicating-data/oracle-to-bigquery).



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
