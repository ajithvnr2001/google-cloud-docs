---
url: https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-to-enterprise-plus-ip-allowlists/
title: Upgrade an instance to Cloud SQL Enterprise Plus edition by using IP allowlists \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:59.718623+00:00
---

# Upgrade an instance to Cloud SQL Enterprise Plus edition by using IP allowlists  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-to-enterprise-plus-ip-allowlists/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Upgrade an instance to Cloud SQL Enterprise Plus edition by using IP allowlists Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-to-enterprise-plus-ip-allowlists "View this page for the MySQL database engine") | PostgreSQL | SQL Server

  


**Note:** This page contains features related to Cloud SQL editions. For more information about Cloud SQL editions, see [Introduction to Cloud SQL editions](https://docs.cloud.google.com/sql/docs/mysql/editions-intro). 

This page shows you how to use the public IP allowlist network connectivity method of Database Migration Service to upgrade a Cloud SQL Enterprise edition instance to Cloud SQL Enterprise Plus edition. Database Migration Service creates a new Cloud SQL instance and migrates data to that instance.

## Overview

Cloud SQL Enterprise Plus edition is ideal for applications that require maximum write performance. For more information about these improvements, see [Performance enhancements](https://docs.cloud.google.com/sql/docs/postgres/editions-intro#performance_enhancements).

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

## Configure your source instance

To configure your source Cloud SQL Enterprise edition instance, complete the following steps:

  1. If you don't have the `postgres` database for your source instance, then create one. For more information, see [Create a database on the Cloud SQL instance](https://docs.cloud.google.com/sql/docs/postgres/create-manage-databases#create).
  2. Install the `pglogical` package on the databases of your source instance. Make sure that the package is included in the [`shared_preload_libraries`](https://www.postgresql.org/docs/current/runtime-config-client.html) variable. For more information, see Configure your source databases.
  3. Enable logical replication and decoding for the databases of your source instance. For more information, see Enable logical replication and decoding for your source databases.



## Configure your source databases

**Note:** For PostgreSQL 9.4, install the `pglogical_origin` extension. Then, install the extension on every database by running the following commands:

  * `CREATE EXTENSION IF NOT EXISTS pglogical_origin;`
  * `CREATE EXTENSION IF NOT EXISTS pglogical;`



Aside from the `template0` and `template1` databases, Database Migration Service migrates every other database under your source Cloud SQL Enterprise edition instance.

On each database in your source instance that isn't mentioned above, complete the following steps:

  1. To install the `pglogical` extension into the database, run the `CREATE EXTENSION IF NOT EXISTS pglogical` command.

  2. For any tables that don't have primary keys, migrate the `UPDATE` and `DELETE` statements manually.

**Note:** For tables that don't have primary keys, Database Migration Service supports migration of the initial snapshot and `INSERT` statements during the change data capture (CDC) phase. 

To learn how to generate a query to list tables in a PostgreSQL database without primary keys, see [Debugging and other tools](https://docs.cloud.google.com/database-migration/docs/postgres/debugging-tools). For each database table that you find that doesn't have a primary key and the table isn't part of the databases that aren't migrated, [ alter the table so that it has a primary key](https://www.postgresql.org/docs/current/static/sql-altertable.html) or [migrate the `UPDATE` and `DELETE` operations for the table](https://docs.cloud.google.com/database-migration/docs/postgres/debugging-tools#find_tables_without_primary_keys_pks). For tables that don't have primary keys, only the initial snapshot and `INSERT` statements are migrated.

  3. To set these privileges on each of the migrated databases, create a user or set the privileges of an existing user. You use this user to connect to the source instance, and you configure this user as the user in the [**Connection profiles**](https://console.cloud.google.com/dbmigration/connection-profiles) page. This user must have certain privileges on each of the migrated databases, as well as the default `postgres` database.

To set these privileges, connect to the instance and run the following commands:

     1. `GRANT USAGE on SCHEMA SCHEMA to USER` on all schemas (aside from the information schema and schemas starting with `pg_`) on each database that you want to migrate.
     2. `GRANT USAGE on SCHEMA pglogical to PUBLIC;` on each database that you want to migrate.
     3. `GRANT SELECT on ALL TABLES in SCHEMA pglogical to USER` on all databases to get replication information from source databases.
     4. `GRANT SELECT on ALL TABLES in SCHEMA SCHEMA to USER` on all schemas (aside from the information schema and schemas starting with `pg_`) on each database that you want to migrate.
     5. `GRANT SELECT on ALL SEQUENCES in SCHEMA SCHEMA to USER` on all schemas (aside from the information schema and schemas starting with `pg_`) on each database that you want to migrate.
     6. `ALTER USER USER with REPLICATION role`



## Enable logical replication and decoding for your source databases

Enable logical replication and decoding for the databases of your source Cloud SQL Enterprise edition instance by setting the `[cloudsql.logical_decoding](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication)` and `[cloudsql.enable_pglogical](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication)` flags to `On`. For more information about these flags, see [Configure database flags](https://docs.cloud.google.com/sql/docs/postgres/flags).

To enable both of these flags, complete the following steps:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click your source instance.
  3. Click **Edit**.
  4. In the **Customize your instance** section, if the **Show configuration options** menu appears, then click it.
  5. Expand the **Flags** section.

  6. To set the `cloudsql.logical_decoding` and `cloudsql.enable_pglogical` flags, complete the following steps: 

     1. Click **Add a database flag**.
     2. From the drop-down menu, choose the `cloudsql.logical_decoding` flag.
     3. Set the value for this flag to `On`.
     4. Click **Done**.
     5. Repeat these steps for the `cloudsql.enable_pglogical` flag.
  7. Click **Save**.

  8. In the **Changes require restart** dialog, click **Save and restart**. Cloud SQL restarts your source instance so that the configuration changes that you made to the flags can take effect.

  9. In the **Configuration** pane, confirm your changes in the **Database flags** section.



## Create a connection profile

A connection profile contains information about the source Cloud SQL Enterprise edition database. Database Migration Service uses the information in the connection profile to migrate data from your source database to the destination Cloud SQL Enterprise Plus edition instance.

To create a connection profile, complete the following steps:

  1. In the Google Cloud console, go to the **Connection profiles** page in Database Migration Service.

[Go to Connection profiles](https://console.cloud.google.com/dbmigration/connection-profiles)

  2. Click **Create profile**.

  3. From the **Database engine** drop-down list, select **Cloud SQL for PostgreSQL**.

  4. In the **Connection profile name** field, enter a name for the connection profile for your source database, such as `My Connection Profile`.

**Note:** Cloud SQL generates the connection profile ID automatically with information about your source instance. We recommend that you don't change this value.
  5. Select the region where you want to save the connection profile.

**Note:** Connection profiles, like all resources, are saved in a region. Region selection doesn't affect which migration jobs can use connection profiles, or which regions can connect to the data location. But region selection can affect availability in the case of regional downtime.
  6. From the **Cloud SQL instance** drop-down list, select the name of your Cloud SQL Enterprise edition instance.

  7. To authenticate to your source instance, enter a username and password. Then, click **Continue**.

**Note:** Cloud SQL populates the **Hostname or IP address** and **Port** fields automatically with information about your source instance. If these fields are empty, then enter the appropriate values.
  8. If you want to encrypt your data, then enable [SSL/TLS encryption](https://docs.cloud.google.com/sql/docs/postgres/authorize-ssl) for the connection between the source and destination databases. Otherwise keep the default value of **None**.

  9. Click **Continue**.

  10. From the **Connectivity test** drop-down menu, select **Public IP**.

  11. Verify that the source has been configured correctly and that Database Migration Service can communicate with the source:

     1. Click **Run test**.

     2. Verify that you see the `Your connection profile test was successful!` status.

If the test fails, then you can address the problem in the appropriate part of the flow, and return to re-test.

  12. Click **Create**.




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

  4. From the **Source database engine** drop-down list, select **Cloud SQL for PostgreSQL**.

  5. From the **Destination database engine** drop-down list, select **Cloud SQL for PostgreSQL**. 

  6. Select the destination region where the Cloud SQL Enterprise Plus edition instance is created.

  7. From the **Migration job type** drop-down list, select **Continuous** because you want ongoing changes in your source Cloud SQL Enterprise edition database to be migrated to the destination Cloud SQL Enterprise Plus edition instance.

  8. Review the required prerequisites that are generated automatically to reflect how the environment must be prepared for a migration job. These prerequisites can include how to configure the source Cloud SQL Enterprise edition database and how to connect it to the destination Cloud SQL Enterprise Plus edition instance.

It's recommended to complete these prerequisites at this step, but you can complete them at any time before you test or start your migration job.

  9. Click **Save & continue**.




### Specify information about the source connection profile

  1. From the **Select source connection profile** drop-down list, select the connection profile that you created.

  2. Click **Save & continue**.




### Define settings for the destination Cloud SQL Enterprise Plus edition instance

  1. In the **Password** field, enter an alphanumeric password for the destination Cloud SQL Enterprise Plus edition instance. This is the password for the `postgres` administrator account in the instance.

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
         
         gcloud sql connect DESTINATION_INSTANCE_NAME --user=postgres

Replace DESTINATION_INSTANCE_NAME with the name of the destination Cloud SQL Enterprise Plus edition instance.

  5. **Optional:** If an **Authorize Cloud Shell** dialog appears, then click **Authorize**.
  6. At the **Enter password** prompt, enter the password that you provided in Define settings for the destination Cloud SQL Enterprise Plus edition instance.


  7. At the **postgres** prompt, to list the databases and verify that you see your source Cloud SQL Enterprise edition database instance, enter `\list`.
  8. At the **postgres** prompt, to see the tables that are associated with this database instance, enter `\connect SOURCE_DB_NAME`. The name of the prompt changes from `postgres` to SOURCE_DB_NAME.
  9. At the SOURCE_DB_NAME prompt, to see the tables of this instance, enter `\dt`.
  10. At the SOURCE_DB_NAME prompt, to give this user permission to access the data in the tables of this instance, enter `GRANT cloudsqlexternalsync to USER;`. 

Replace USER with the name of the user that you used to connect to the destination Cloud SQL Enterprise Plus edition database instance.

  11. At the SOURCE_DB_NAME prompt, to see the information that's replicated from a table in your source Cloud SQL Enterprise edition database instance, enter `SELECT * from TABLE_NAME;`.
  12. Verify that you see the correct information in the table.



## Promote the migration job

Promoting the migration job replaces the source Cloud SQL Enterprise edition database instance with the destination Cloud SQL Enterprise Plus edition database instance as the primary database.

To promote the migration job, complete the following steps:

  1. Return to the **Migration jobs** page.

  2. Click the migration job that you want to promote. The **Migration job details** page appears.

  3. Stop all writes to the source Cloud SQL Enterprise edition database.

**Important:** Before you stop writes to the source database, wait for the replication delay to be minimal. You must stop all writes to this database because, by promoting the migration job, the destination Cloud SQL Enterprise Plus edition database becomes your primary database. 
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
