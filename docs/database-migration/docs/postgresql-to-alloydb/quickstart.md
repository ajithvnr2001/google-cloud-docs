---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/quickstart/
title: Migrate a database to AlloyDB for PostgreSQL by using Database Migration Service \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:23.076215+00:00
---

# Migrate a database to AlloyDB for PostgreSQL by using Database Migration Service  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest)



Send feedback 

#  Migrate a database to AlloyDB for PostgreSQL by using Database Migration Service Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/quickstart "View this page for the MySQL version of Database Migration Service.") | [PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/quickstart "View this page for the PostgreSQL version of Database Migration Service.") | PostgreSQL to AlloyDB

  
  
Migrate a database to AlloyDB for PostgreSQL

# Migrate a database to AlloyDB for PostgreSQL

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

  6. Enable the Database Migration Service API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=datamigration.googleapis.com)

  7. Make sure that you have the Database Migration Admin role assigned to your user account. 

[ Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)




## Requirements

Database Migration Service offers a variety of source database options and connectivity methods. Different sources work better with some connectivity methods than with others. In this quickstart, we assume that you're using a standalone PostgreSQL database in an environment where you can configure your network to add an inbound firewall rule. The source database can be on-premises or in a cloud provider. Because we can't know the specifics of your environment, we can't provide detailed steps when it comes to your networking configuration.

In this quickstart, you'll select **PostgreSQL** for the **Source database engine** , **AlloyDB for PostgreSQL** for the **Destination database engine** and **VPC peering** as the networking method.

## Create a source connection profile

By creating a connection profile, you're creating a record that contains information about the source database. Database Migration Service uses the information in the connection profile to migrate data from your source database to the destination AlloyDB database instance. 

  1. Go to the Database Migration Service Connection profiles page in the Google Cloud console.

[Go to the Database Migration Service Connection Profiles Page](https://console.cloud.google.com/dbmigration/connection-profiles)

  2. Click **CREATE PROFILE**.

  3. On the **Create a connection profile** page, from the **Profile role** list, select **Source**.

  4. From the **Database engine** list, select one of the following classification types of your source database:

     * A standalone PostgreSQL instance (PostgreSQL)
     * An existing Cloud SQL for PostgreSQL instance (Cloud SQL for PostgreSQL)
     * An Amazon RDS instance for PostgreSQL (Amazon RDS for PostgreSQL)

For this quickstart, select **PostgreSQL**.



  4. Supply the following information: 
     * In the **Connection profile name** field, enter a name for the connection profile for your source database, such as `My Connection Profile`.
     * Keep the auto-generated **Connection profile ID**.
     * Enter **Connectivity information** : 
       * If you're replicating from a self-hosted database, then enter the **Hostname or IP address** (domain or IP) and **Port** to access the host. (The default PostgreSQL port is 5432.)
       * If you're replicating from a Cloud SQL database, then select the Cloud SQL instance from the drop-down list.
     * Enter a **Username** and **Password** to authenticate to your source instance.
  5. In the **Connection profile region** section of the page, select the region where you want to save the connection profile.

Connection profiles, like all resources, are saved in a region. Region selection doesn't impact which migration jobs can use them, or which regions can connect to the data location itself, but can impact availability in the case of regional downtime.

  6. Click **CREATE**.



## Create a migration job

Database Migration Service uses migration jobs to migrate data from your source database instance to the destination AlloyDB database instance. 

Creating a migration job includes:

  * Defining settings for the job 
  * Selecting the connection profile that you created for your source database (source connection profile) 
  * Defining settings for the destination AlloyDB database instance 
  * Setting up connectivity between the source and destination database instances 
  * Testing the migration job to ensure that the connection information you provided for the job is valid



### Define settings for the migration job

  1. Go to the Database Migration Service Migration jobs page in the Google Cloud console.

[Go to the Database Migration Service Migration Jobs Page](https://console.cloud.google.com/dbmigration/migrations)

  2. Click **CREATE MIGRATION JOB**.

  3. In the **Migration job name** field, enter a name for the migration job, such as `My Migration Job`.

  4. Keep the auto-generated **Migration job ID**.

  5. Open the **Source database engine** drop-down list and select the classification type of your source database. In this quickstart, select **AlloyDB for PostgreSQL**.

  6. Select the **Destination region** where the destination instance is to be created.

  7. Set the **Migration job type** to "Continuous" because you want ongoing changes in your source database to be migrated to the destination AlloyDB database instance.

  8. Review the required prerequisites that are generated automatically to reflect how the environment must be prepared for a migration job. These prerequisites can include how to configure the source database and how to connect it to the destination AlloyDB database instance. It's best to complete these prerequisites at this step, but you can complete them at any time before you test the migration job or start it. For more information about these prerequisites, see [Configure your source.](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-source-database)

  9. Click **SAVE & CONTINUE**.




### Specify information about the source connection profile

  1. Open the **Select source connection profile** drop-down list and select the connection profile that you created.

  2. Click **SAVE & CONTINUE**.




### Create a destination AlloyDB cluster

Clusters are the top-level resource in AlloyDB. To create a destination cluster:

  1. Choose a cluster type. Database Migration Service currently supports **Highly available** AlloyDB clusters. They can serve data from more than one zone in a region, with no read pools.
  2. Click **CONTINUE**.
  3. Configure your cluster: 
     1. In the **Cluster ID** field, enter an ID for your cluster.
     2. In the **Password** field, enter a password for the default `postgres` user. You will need the password to log in to your database.
     3. In the **Network** field, select a network path to define which resources are available when setting the migration connectivity. Clusters can only be configured with a private IP network path. If you plan to connect to the source database via VPC peering, select the VPC where it resides.
     4. Optionally, select an allocated IP range name to specify IP addresses your instance can connect with.
     5. Click **CONTINUE**.
  4. Configure your primary instance. A primary instance determines a cluster's compute capacity and supports read and write operations:
     1. In the **Instance ID** field, enter an ID for your primary instance.
     2. Select a machine type.
     3. Optional: Set flags for your instance. You can use flags to customize your instance. For information on supported flags, see [AlloyDB documentation](https://docs.cloud.google.com/alloydb/docs/reference/database-flags). For each flag: 
        1. Click **ADD FLAG**.
        2. Select a flag from the **New database flag** list.
        3. Provide a value for the flag.
        4. Click **DONE**.

  5. Click **SAVE & CONTINUE**.
  6. Confirm your choice by clicking **CREATE DESTINATION & CONTINUE**.
  7. Wait for the creation of the destination instance to finish.

Your AlloyDB cluster will be in a "Bootstrapping" state while it's being managed by Database Migration Service. While in "Bootstrapping", you will not be able to perform any operations on your cluster. If you still wish to delete the cluster, you can do so using gcloud with the `--force` option.

### Set up connectivity

  1. Choose the networking method that you'd like to use to establish connectivity between the source and destination databases. For this quickstart, use the **Connectivity method** list to select **VPC peering** as the networking method. 
  2. Review the VPC network of your source database. Click **CONFIGURE & CONTINUE** to complete the connection profile configuration.



### Configure migration databases

You can select the databases that you want to migrate.

  1. From the **Databases to migrate** list, select **All databases**. 

All databases that exist on the source are selected for migration.

  2. Click **Save and continue**.



### Test and create the migration job

  1. Review the settings you chose for the migration job.

  2. Click **TEST JOB** to verify that the source has been configured correctly, that the source and destination instances are able to communicate with each other, and that the migration job is valid.

  3. Verify that you see the "Tests passed successfully!" status.

If the test fails, then you can address the problem in the appropriate part of the flow, and return to re-test.

  4. Click **CREATE & START JOB** to create the migration job and start it immediately.

  5. Click **START** in the subsequent dialog box.

  6. In the **Migration jobs** page, verify that your migration job has a status of "Starting". After a few minutes, confirm that the status changes to "Running".




## Verify the migration job

In this section, you confirm that Database Migration Service used the migration job to migrate data from your source database instance to the destination AlloyDB database instance.

  1. Go to the AlloyDB **Clusters** page in the Google Cloud console. 

[ Go to the AlloyDB Clusters page](https://console.cloud.google.com/alloydb/clusters)

  2. Click the read replica entry of your migration job.
  3. Click the **Activate Cloud Shell** icon that appears in the upper-right region of the page.
  4. At the Cloud Shell prompt, press **Enter**.
  5. Optional: If an **Authorize Cloud Shell** dialog box appears, then click **Authorize**.
  6. At the **Enter password** prompt, enter the password that you either provided or that Database Migration Service generated for you in [Define and create the destination AlloyDB instance](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job#dest).



  7. At the **postgres** prompt, enter `\list` to list the databases and verify that you see your source database instance.

  8. At the **postgres** prompt, enter `\connect SOURCE_DB_NAME` because you want to see the tables associated with this database instance. The name of the prompt changes from `postgres` to SOURCE_DB_NAME.

  9. At the SOURCE_DB_NAME prompt, enter `\dt` to see the tables of this instance.

  10. At the SOURCE_DB_NAME prompt, enter `GRANT alloydbexternalsync to USER;` because you want to give this user permission to access the data in the tables of this instance. 

Replace USER with the name of the user you used to connect to the destination database instance.

  11. At the SOURCE_DB_NAME prompt, enter `SELECT * from TABLE_NAME;` to see the information that's replicated from a table in your source database instance.

  12. Verify that you see the correct information in the table.




This confirms that Database Migration Service migrated the data.

## Promote the migration job

You're ready to promote the migration job. As a result, the destination AlloyDB database instance replaces the source database instance as the primary database.

  1. Return to the **Migration jobs** page.

  2. Click the migration job that you want to promote. The **Migration job details** page appears.

  3. Wait for the replication delay to trend toward zero.

  4. **Stop all writes to the source database**.

You must stop all writes to the source database because, by promoting the migration job, the destination AlloyDB database will become your primary database. 
  5. Wait until the replication delay is at zero.

  6. Click the migration job that you want to promote. This job should have a status of "Running".

  7. Click **PROMOTE** to promote the migration job.

  8. Click **PROMOTE** again in the subsequent dialog box.

  9. Verify that the migration job has a status of "Promote in progress". After a few minutes, confirm that the status changes to "Completed".




Your new AlloyDB database instance is ready to use.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. Use the Google Cloud console to delete your migration job, connection profile, AlloyDB cluster, and project if you don't need them.



## What's next

  * Read more about [how to manage connection profiles](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/manage_connection-profiles).
  * Read more about [migration job statuses](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/review-migration-job#migration_job_statuses).
  * Read more about [migration job metrics](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/review-migration-job#migration_job_metrics).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
    * [ Builders Hub ](https://me.developers.google.com/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


