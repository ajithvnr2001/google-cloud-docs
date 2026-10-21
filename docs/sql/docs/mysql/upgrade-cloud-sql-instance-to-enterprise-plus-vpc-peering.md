---
url: https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-to-enterprise-plus-vpc-peering/
title: Upgrade an instance to Cloud SQL Enterprise Plus edition by using VPC peering \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:31.164757+00:00
---

# Upgrade an instance to Cloud SQL Enterprise Plus edition by using VPC peering  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-to-enterprise-plus-vpc-peering/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Upgrade an instance to Cloud SQL Enterprise Plus edition by using VPC peering Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-to-enterprise-plus-vpc-peering "View this page for the PostgreSQL database engine") | SQL Server

  


**Note:** This page contains features related to Cloud SQL editions. For more information about Cloud SQL editions, see [Introduction to Cloud SQL editions](https://docs.cloud.google.com/sql/docs/mysql/editions-intro). 

This page shows you how to use the private VPC peering network connectivity method of Database Migration Service to upgrade a Cloud SQL Enterprise edition instance to Cloud SQL Enterprise Plus edition. Database Migration Service creates a new Cloud SQL instance and migrates data to that instance.

## Overview

Cloud SQL Enterprise Plus edition is ideal for applications that require maximum read and write performance. For more information about these improvements, see [Performance enhancements](https://docs.cloud.google.com/sql/docs/mysql/editions-intro#performance_enhancements).

To enable these enhancements for your existing Cloud SQL Enterprise edition instances, you must upgrade them to Cloud SQL Enterprise Plus edition using Database Migration Service.

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

  6. Enable the Database Migration Service API. 

[ Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=datamigration.googleapis.com)

  7. Make sure that you have the Database Migration Admin role assigned to your user account. 

[ Go to IAM](https://console.cloud.google.com/iam-admin/iam)




## Requirements

Database Migration Service offers various source database options and network connectivity methods. Different sources work better with some connectivity methods than with others. On this page, we assume that you're using a Cloud SQL Enterprise edition instance in an environment where you can configure your network to add an inbound firewall rule. Because we can't know the specifics of your environment, we can't provide detailed steps when it comes to your networking configuration.

## Retrieve information from the source instance

To upgrade a source Cloud SQL Enterprise edition instance, you must retrieve the following information:

  * The instance's private IP address. You use this IP address when you create a connection profile in Database Migration Service.
  * The name of the VPC network that allows the Cloud SQL Enterprise Plus edition destination instance to communicate with the Cloud SQL Enterprise edition source instance directly. You use this VPC network when you create a migration job in Database Migration Service.



To retrieve information from the source Cloud SQL Enterprise edition instance, complete the following steps:

  1. In the Google Cloud console, go to the **SQL Instances** page.

[ Go to Cloud SQL Instances](https://console.cloud.google.com/sql/instances)

  2. Click your source instance.
  3. In the **Connect to this instance** section, click **Copy to clipboard** in the **Private IP address** field. 
  4. At the top of the page, click **Edit**.
  5. Expand the **Connections** section.
  6. In the **Associated networking** section, make a note of the name of the VPC network that appears in the **Network** field.



## Create a connection profile

A connection profile contains information about the source Cloud SQL Enterprise edition database. Database Migration Service uses the information in the connection profile to migrate data from your source database to the destination Cloud SQL Enterprise Plus edition instance.

To create a connection profile, complete the following steps:

  1. In the Google Cloud console, go to the **Connection profiles** page in Database Migration Service.

[Go to Connection profiles](https://console.cloud.google.com/dbmigration/connection-profiles)

  2. Click **Create profile**.

  3. From the **Database engine** drop-down list, select **Cloud SQL for MySQL**.

  4. From the **Cloud SQL instance** drop-down list, select the name of your Cloud SQL Enterprise edition instance.

**Note:** Cloud SQL generates the connection profile name and connection profile ID automatically with information about your source instance. We recommend that you don't change these values.
  5. In the **Hostname or IP address** field, replace the value with the private IP address that you copied in Retrieve information from the source Cloud SQL Enterprise edition instance.

  6. To authenticate to your source instance, enter a username and password.

**Note:** Cloud SQL populates the **Port** field automatically with information about your source instance. If this field is empty, then enter the appropriate port number.
  7. Select the region where you want to save the connection profile.

**Note:** Connection profiles, like all resources, are saved in a region. Region selection doesn't affect which migration jobs can use connection profiles, or which regions can connect to the data location. But region selection can affect availability in the case of regional downtime.
  8. If you want to encrypt your data, then enable [SSL/TLS encryption](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl) for the connection between the source and destination databases. Otherwise keep the default value of **None**.

  9. Click **Create**.




## Create a migration job

Database Migration Service uses migration jobs to migrate data from your source Cloud SQL Enterprise edition database instance to the destination Cloud SQL Enterprise Plus edition instance.

Creating a migration job includes the following steps:

  * Defining settings for the job.
  * Selecting the connection profile that you created for your source Cloud SQL Enterprise edition database. This is your _source connection profile_.
  * Defining settings for the destination Cloud SQL Enterprise Plus edition instance.
  * Setting up connectivity between the source and destination database instances.
  * Testing the migration job to ensure that the connection information that you provided for the job is valid.



### Define settings for the migration job

  1. In the Google Cloud console, go to the **Migration jobs** page in Database Migration Service.

[Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

  2. Click **Create migration job**.

  3. In the **Migration job name** field, enter a name for the migration job, such as `My Migration Job`.

  4. From the **Source database engine** drop-down list, select **Cloud SQL for MySQL**. Database Migration Service selects the **Destination database engine** automatically. 

  5. Select the destination region where the Cloud SQL Enterprise Plus edition instance is created.

  6. From the **Migration job type** drop-down list, select **Continuous** because you want ongoing changes in your source Cloud SQL Enterprise edition database to be migrated to the destination Cloud SQL Enterprise Plus edition instance.

  7. Review the required prerequisites that are generated automatically to reflect how the environment must be prepared for a migration job. These prerequisites can include how to configure the source Cloud SQL Enterprise edition database and how to connect it to the destination Cloud SQL Enterprise Plus edition instance.

It's recommended to complete these prerequisites at this step, but you can complete them at any time before you test or start your migration job.

  8. Click **Save & continue**.




### Specify information about the source connection profile

  1. From the **Select source connection profile** drop-down list, select the connection profile that you created.

  2. Click **Save & continue**.




### Define settings for the destination Cloud SQL Enterprise Plus edition instance

  1. In the **Password** field, enter an alphanumeric password for the destination Cloud SQL Enterprise Plus edition instance. This is the password for the `root` administrator account in the instance.

  2. From the **Database version** drop-down list, select the destination instance from the list of supported Cloud SQL versions for the specified database engine.

  3. Select **Enterprise Plus**.

  4. From the **Choose region and zone** section, select the desired Google Cloud zone for the new Cloud SQL Enterprise Plus edition instance (or leave as **Any**).

  5. Select the **Private IP** checkbox.

  6. From the **VPC** drop-down list, select the VPC network that you noted in Retrieve information from the source Cloud SQL Enterprise edition instance.

  7. Select the machine shape for the Cloud SQL Enterprise Plus edition instance. The disk size must be equal to or greater than the source database size.

  8. Define the storage type and storage capacity for the Cloud SQL instance.

  9. To create the new instance, click **Create & Continue**.

  10. In the dialog that appears, click **Create destination & continue**. Creating the instance may take several minutes to complete.

**Important:** This procedure creates a Cloud SQL Enterprise Plus edition instance. You're charged according to the configuration that you select.



### Set up connectivity

  1. Choose how you'd like to use to establish connectivity between the source Cloud SQL Enterprise edition and destination Cloud SQL Enterprise Plus edition databases. For this procedure, use the **Connectivity method** drop-down list to select **Source and destination are using private IP**.
  2. From the **VPC** drop-down list, select the VPC network where your source Cloud SQL Enterprise edition instance resides. This is the VPC network that you noted in Retrieve information from the source Cloud SQL Enterprise edition instance.
  3. Click **Configure & continue**.



### Test, create, and start the migration job

  1. Review the settings that you chose for the migration job.

  2. Verify that the source has been configured correctly, that the source Cloud SQL Enterprise edition and destination Cloud SQL Enterprise Plus edition instances are able to communicate with each other, and that the migration job is valid:

     1. Click **Test job**.

     2. Verify that you see the `Your migration job test was successful!` status.

If the test fails, then you can address the problem in the appropriate part of the flow, and return to re-test.

  3. To create the migration job and start it immediately, click **Create & start job**.

  4. In the dialog that appears, click **Create & start**.

  5. In the **Migration jobs** page, verify that your migration job has a status of `Starting`.

  6. After a few minutes, confirm that the status changes to `Running`.




## Verify the migration job

To confirm that Database Migration Service used the migration job to migrate data from your source Cloud SQL Enterprise edition database instance to the destination Cloud SQL Enterprise Plus edition database instance, complete the following steps:

  1. In the Google Cloud console, go to the **SQL Instances** page.

[ Go to Cloud SQL Instances](https://console.cloud.google.com/sql/instances)

  2. Click the read replica entry of your migration job.

**Note:** Make sure that the Cloud SQL edition for this entry is **Enterprise Plus** , and not **Enterprise**.

  3. Click the **Activate Cloud Shell** icon that appears next to the **Search** field.
  4. At the prompt, to connect to the destination Cloud SQL Enterprise Plus edition database instance, use the [`gcloud sql connect`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/connect) command.
         
         gcloud sql connect DESTINATION_INSTANCE_NAME --user=root

Replace DESTINATION_INSTANCE_NAME with the name of the destination Cloud SQL Enterprise Plus edition instance.

  5. **Optional:** If an **Authorize Cloud Shell** dialog appears, then click **Authorize**.
  6. At the **Enter password** prompt, enter the password that you provided in Define settings for the destination Cloud SQL Enterprise Plus edition instance.


  7. At the **mysql** prompt, to list the databases and verify that you see your source Cloud SQL Enterprise edition database instance, enter `show databases;`.
  8. At the **mysql** prompt, to see the tables that are associated with this database instance, enter `use SOURCE_DATABASE_INSTANCE_NAME;`.
  9. At the **mysql** prompt, to see the tables of this instance, enter `show tables;`.
  10. At the **mysql** prompt, to see the information that's replicated from a table in your source Cloud SQL Enterprise edition database instance, enter `select * from TABLE_NAME;`.
  11. Verify that you see the correct information in the table.



## Promote the migration job

Promoting the migration job replaces the source Cloud SQL Enterprise edition database instance with the destination Cloud SQL Enterprise Plus edition database instance as the primary database.

To promote the migration job, complete the following steps:

  1. Return to the **Migration jobs** page.

  2. Click the migration job that you want to promote. The **Migration job details** page appears.

  3. Stop all writes to the source Cloud SQL Enterprise edition database.

**Important:** Before you stop writes to the source database, wait for the replication delay to be minimal. You must stop all writes to this database because, by promoting the migration job, the destination Cloud SQL Enterprise Plus edition database becomes your primary database. You can use a script to verify that writing is stopped. For more information, see [Find write activities](https://docs.cloud.google.com/database-migration/docs/mysql/debugging-tools#write-activities). 
  4. Verify that the replication delay is minimal.

  5. Click the migration job that you want to promote. This job has a status of `Running`.

  6. To promote the migration job, click **Promote**.

  7. In the dialog that appears, click **Promote**.

  8. Verify that the migration job has a status of `Promote in progress`. After a few minutes, confirm that the status changes to `Completed`.




Your new Cloud SQL Enterprise Plus edition database instance is ready to use.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, use the Google Cloud console to delete your migration job, connection profile, source Cloud SQL Enterprise edition instance, and project if you don't need them.

## What's next

  * Read more about the key features of [Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/editions-intro#features).
  * Read more about performance enhancements for [Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/editions-intro#performance_enhancements).
  * Read more about region support for [Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/editions-intro#editions-regions).
  * Read more about pricing for [Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/editions-intro#pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
