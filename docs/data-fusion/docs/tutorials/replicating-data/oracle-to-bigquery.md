---
url: https://docs.cloud.google.com/data-fusion/docs/tutorials/replicating-data/oracle-to-bigquery/
title: Replicating data from Oracle database to BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:43.109138+00:00
---

# Replicating data from Oracle database to BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/tutorials/replicating-data/oracle-to-bigquery/




#  Replicating data from Oracle database to BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to deploy a job that continuously replicates changed data from an Oracle database to a BigQuery dataset, using Cloud Data Fusion Replication. This feature is powered by [Datastream](https://cloud.google.com/datastream).

## Objectives

In this tutorial, you:

  1. Configure your Oracle database to enable supplemental logging.
  2. Create and run a Cloud Data Fusion replication job.
  3. View the results in BigQuery. 



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/pricing)
  * [Datastream](https://docs.cloud.google.com/datastream/pricing)
  * [BigQuery](https://cloud.google.com/bigquery/pricing)
  * [Cloud Storage](https://docs.cloud.google.com/storage/pricing)
  * [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/pricing)
  * [Compute Engine](https://docs.cloud.google.com/compute/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When Replication runs, you're charged for the Managed Service for Apache Spark cluster and Cloud Storage, and you incur processing costs for Datastream and BigQuery. To optimize these costs, we strongly recommend using [BigQuery flat rate pricing](https://cloud.google.com/bigquery/pricing#flat_rate_pricing).

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Enable the Cloud Data Fusion, Dataproc, Datastream, BigQuery, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=datafusion.googleapis.com,dataproc.googleapis.com,datastream.googleapis.com,bigquery.googleapis.com,storage.googleapis.com&redirect=https%3A//console.cloud.google.com)

  4. [Create a public Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-instance) in version 6.3.0 or later. If you [create a private instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip), set up VPC network peering. 
     * When you create the instance, enable Replication by clicking **Add Accelerators** and selecting the **Replication** checkbox.
     * To enable it in an existing instance, see [Enable Replication](https://docs.cloud.google.com/data-fusion/docs/how-to/enable-replication#enable).

**Important:** You must enable Replication in your instance for it to appear in the Cloud Data Fusion web interface _menu_ **Menu** (see [Enable Replication](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading#replication)).

### Required roles

To get the permissions that you need to connect to an Oracle database, ask your administrator to grant you the following IAM roles:

  * [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`) on the Managed Service for Apache Spark service account in the project that contains the cluster
  * [Cloud Data Fusion Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.runner) on the Managed Service for Apache Spark service account in the project that contains the cluster
  * [DataStream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`) on the Cloud Data Fusion service account and Managed Service for Apache Spark service account



For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

## Optional: Install Oracle in Compute Engine

This section shows how to set up an example database. If you already have an Oracle database installed, you can skip this section.

**Note:** Datastream supports only [specific versions of Oracle database](https://docs.cloud.google.com/datastream/docs/sources#versionsfororaclesourcedb).

  1. [Download](https://hub.docker.com/r/wnameless/oracle-xe-11g-r2) an Oracle Server Docker image.

For limitations of this Oracle Express Edition 11g image, see [Oracle Database Editions](https://docs.oracle.com/cd/E11882_01/license.112/e47877/editions.htm#DBLIC109).

  2. [Deploy](https://docs.cloud.google.com/compute/docs/containers/deploying-containers) your Docker image on a new VM instance.

**Note:** To deploy the image in the new VM instance, the Compute Engine service must have the [Artifact Registry Reader role](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`).
  3. On the Compute Engine **Disks** page, change the disk size to `500 GB` and restart the VM.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  4. Install the [HR sample schema](https://docs.oracle.com/database/121/COMSC/installation.htm#COMSC00004).




## Create VPC network peering or firewall rule for your Oracle server

If your Oracle Database doesn't allow ingress traffic from public IP addresses, set up VPC network peering between the Datastream VPC and the VPC where your Oracle database can be accessed. For more information, see [Create a private connectivity configuration](https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration).

If your Oracle database allows ingress traffic from public IP addresses, [create a firewall rule](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules) for the VM instance to allow ingress traffic from [Datastream public IPs](https://docs.cloud.google.com/datastream/docs/ip-allowlists-and-regions).

## Configure your Oracle Server to enable supplemental logging

Follow the [steps to configure your source Oracle database](https://docs.cloud.google.com/datastream/docs/configure-your-source-oracle-database#selfhostedoracle).

## Create and run a Cloud Data Fusion replication job

### Create the job

  1. In the Cloud Data Fusion web interface, click **Replication**.

  2. Click add_circle **Create a replication job**.

  3. On the **Create new replication job** page, specify a replication job **Name** and click **Next**.

  4. Configure the source:

     1. Select **Oracle (by Datastream)** as the source.

     2. For **Connectivity Method** , if your Oracle server allows ingress traffic from Datastream public IPs, choose **IP allowlisting**. Otherwise, for **Private Connection Name** , choose **Private connectivity (VPC peering)** and enter the VPC peering name that you created in the [Create VPC network peering or firewall rule for your Oracle Server](https://docs.cloud.google.com/data-fusion/docs/tutorials/replicating-data/oracle-to-bigquery#allow-traffic) section.

     3. For **Host** , enter the hostname of the Oracle Server to read.

     4. For **Port** , enter the port to use to connect to the Oracle Server: 1521.

     5. For **System Identity** , enter `xe` (the sample database name of the Oracle server).

     6. In the credentials section, enter your username and password for accessing the Oracle Server.

     7. Leave all other properties as is.

  5. Click **Next**.

  6. Configure the target:

     1. Select the BigQuery target.

     2. The **Project ID** and **Service Account Key** are automatically detected. Keep the default values as is.

     3. Optional: In the **Advanced** section, you can configure the following:

        * Name and location of the staging bucket
        * Load interval
        * Staging table prefix
        * Behavior when tables or databases are dropped
  7. Click **Next**.

  8. If the connection is successful, a list of tables is displayed. For this tutorial, select a few tables.

**Note:** To proceed, [supplemental logging must be enabled](https://docs.cloud.google.com/data-fusion/docs/tutorials/replicating-data/oracle-to-bigquery#configure_supplemental_logging) on the selected tables.
  9. Click **Next**.

  10. On the **Review assessment page** , click **View mappings** by any of the tables to get an assessment of schema issues, missing features, or connectivity issues that might occur during Replication.

If any issues occur, you must resolve them before proceeding. For this tutorial, if any of the tables have issues, do the following:

     1. Go back to the step where you selected tables.
     2. Select a table or event (Inserts, Updates, or Deletes) without issues.

For more information about data type conversions from the source database to the BigQuery destination, see [Replication data types](https://docs.cloud.google.com/data-fusion/docs/reference/replication-data-types#oracle).

  11. Click **Back**.

  12. Click **Next**.

  13. Review the summary replication job details, and then click **Deploy replication job**.




### Start the job

  1. In the Cloud Data Fusion web interface, go to the **replication job details** page.

  2. Click **Start**.




The replication job transitions from **Provisioning** to **Starting** to **Running** state. In the running state, the replication job loads an initial snapshot of the table data that you selected into BigQuery. In this state, the state of the table is listed as **Snapshotting**. After the initial snapshot is loaded into BigQuery, any changes made to the table are replicated to BigQuery, and the state of the table is listed as **Replicating**.

### Monitor the job

You can start and stop the replication job, review its configuration and logs, and monitor your replication job.

You can monitor replication job activities from the **replication job details** page.

  1. From the **Replication** page, click the chosen replication job **Name**.

  2. Click **Monitoring**.




## View the results in BigQuery

The replication job creates a replicated dataset and table in BigQuery, with names inherited from the corresponding Oracle database and table names.

**Note:** If your source database name doesn't follow the [BigQuery dataset naming conventions](https://docs.cloud.google.com/bigquery/docs/datasets), or if you have naming conflicts when you replicate multiple datasets into a single BigQuery dataset, specify aliases in the BigQuery target properties.

  1. In the Google Cloud console, go to the [BigQuery](https://console.cloud.google.com/bigquery) page.

  2. In the left panel, click your project name to expand a list of datasets.

  3. Select the `xe` dataset, and then select a table to view.




For more information, see the [BigQuery documentation](https://docs.cloud.google.com/bigquery/docs).

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

After you've finished the tutorial, clean up the resources you created on Google Cloud so they won't take up quota and you won't be billed for them in the future. The following sections describe how to delete or turn off these resources.

### Delete the VM instance

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the checkbox for the instance that you want to delete.

  3. To delete the instance, click **Delete**.




### Delete the Cloud Data Fusion instance

Follow the [instructions to delete your Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/delete-instance).

### Delete the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Learn more about [Datastream](https://docs.cloud.google.com/datastream/docs).
  * Learn more about [Replication](https://docs.cloud.google.com/data-fusion/docs/concepts/replication) in Cloud Data Fusion.
  * Refer to the [Replication API reference](https://docs.cloud.google.com/data-fusion/docs/reference/replication-ref).
  * Refer to the [Oracle replication reference](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1749778437/Oracle+Replication+Source)
  * Work through the tutorial for [Replicating data from MySQL to BigQuery](https://docs.cloud.google.com/data-fusion/docs/tutorials/replicating-data/mysql-to-bigquery).
  * Work through the tutorial for [Replicating data from SQL Server to BigQuery](https://docs.cloud.google.com/data-fusion/docs/tutorials/replicating-data/sqlserver-to-bigquery).



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
