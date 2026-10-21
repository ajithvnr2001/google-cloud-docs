---
url: https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-to-enterprise-plus-ip-allowlists/
title: Upgrade an instance to Cloud SQL Enterprise Plus edition by using IP allowlists \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:50:11.248633+00:00
---

# Upgrade an instance to Cloud SQL Enterprise Plus edition by using IP allowlists  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-to-enterprise-plus-ip-allowlists/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Upgrade an instance to Cloud SQL Enterprise Plus edition by using IP allowlists Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-to-enterprise-plus-ip-allowlists "View this page for the PostgreSQL database engine") | SQL Server

  


**Note:** This page contains features related to Cloud SQL editions. For more information about Cloud SQL editions, see [Introduction to Cloud SQL editions](https://docs.cloud.google.com/sql/docs/mysql/editions-intro). 

This page shows you how to use the public IP allowlist network connectivity method of Database Migration Service to upgrade a Cloud SQL Enterprise edition instance to Cloud SQL Enterprise Plus edition. Database Migration Service creates a new Cloud SQL instance and migrates data to that instance.

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

## Create a connection profile

A connection profile contains information about the source Cloud SQL Enterprise edition database. Database Migration Service uses the information in the connection profile to migrate data from your source database to the destination Cloud SQL Enterprise Plus edition instance.

To create a connection profile, complete the following steps:

  1. In the Google Cloud console, go to the **Connection profiles** page in Database Migration Service.

[Go to Connection profiles](https://console.cloud.google.com/dbmigration/connection-profiles)

  2. Click **Create profile**.

  3. From the **Database engine** drop-down list, select **Cloud SQL for MySQL**.

  4. From the **Cloud SQL instance** drop-down list, select the name of your Cloud SQL Enterprise edition instance.

**Note:** Cloud SQL generates the connection profile name and connection profile ID automatically with information about your source instance. We recommend that you don't change these values.
  5. To authenticate to your source instance, enter a username and password.

**Note:** Cloud SQL populates the **Hostname or IP address** and **Port** fields automatically with information about your source instance. If these fields are empty, then enter the appropriate values.
  6. Select the region where you want to save the connection profile.

**Note:** Connection profiles, like all resources, are saved in a region. Region selection doesn't affect which migration jobs can use connection profiles, or which regions can connect to the data location. But region selection can affect availability in the case of regional downtime.
  7. If you want to encrypt your data, then enable [SSL/TLS encryption](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl) for the connection between the source and destination databases. Otherwise keep the default value of **None**.

  8. Click **Create**.




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

  5. Select the **Public IP** checkbox.

  6. Select the machine shape for the Cloud SQL Enterprise Plus edition instance. The disk size must be equal to or greater than the source database size.

  7. Define the storage type and storage capacity for the Cloud SQL instance.

  8. To create the new instance, click **Create & Continue**.

  9. In the dialog that appears, click **Create destination & continue**. Creating the instance may take several minutes to complete.

**Important:** This procedure creates a Cloud SQL Enterprise Plus edition instance. You're charged according to the configuration that you select.



### Set up connectivity

  1. From the **Connectivity method** drop-down list, select **IP allowlist**. 

**Note:** An IP allowlist is a security feature that's often used for limiting and controlling access to the data in your source and destination databases only to trusted users. You can use IP allowlists to create lists of trusted IP addresses or IP ranges from which your users can access this data. Also, to use IP allowlists, you must open the source database or firewall to incoming connections from the destination Cloud SQL Enterprise Plus edition instance.

It may take a few minutes for IP addresses to appear in the **Destination outgoing IP addresses** region. 

  2. To use your destination Cloud SQL Enterprise Plus edition instance's outgoing IP addresses to establish a connection to the source Cloud SQL Enterprise edition instance, complete the following steps:

     1. In the **Destination outgoing IP addresses** region, click **Copy all**.
     2. Open a separate tab in your browser.
     3. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

     4. Click your source instance.
     5. Click **Edit**.
     6. In the **Customize your instance** section, if the **Show configuration options** menu appears, then click it.
     7. Click the **Connections** section.
     8. Click **Add a network**.
     9. In the **Name** field, provide a name for the network that represents the first IP address that you copied, such as `My First Network`. This network is used to establish a connection between the source Cloud SQL Enterprise edition and destination Cloud SQL Enterprise Plus edition database instances.
     10. In the **Network** field, enter the first IP address that you copied, followed by `/32`. This limits the network to accept connections only from this IP address.
     11. Click **Done**.
     12. Repeat these steps for each IP address that you copied.
     13. Click **Save**. Cloud SQL restarts your source Cloud SQL Enterprise edition instance so that the configuration changes that you made can take effect.

  3. On the tab that contains the migration job, click **Save & continue**.



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
