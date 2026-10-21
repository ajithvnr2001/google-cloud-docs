---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-migration-job/
title: Create a migration job \u00a0|\u00a0 Database Migration Service for heterogeneous SQL Server to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:10.203196+00:00
---

# Create a migration job  |  Database Migration Service for heterogeneous SQL Server to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-migration-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ SQL Server to Cloud SQL for AlloyDB ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/scenario-overview)



Send feedback 

#  Create a migration job Stay organized with collections  Save and categorize content based on your preferences. 

Database Migration Service uses migration jobs to migrate data from your source databases to the AlloyDB for PostgreSQL destination cluster. Migration jobs help you organize the source and destination connection profiles, define settings specific to the migration process, monitor the progress, and safely finalize the whole operation.

Creating a migration job includes performing the following tasks:

  * Selecting source and destination connection profiles.

  * Selecting the conversion workspace and specifying objects you want to migrate.

  * Performing a migration job test to ensure that Database Migration Service is able to connect to your data source and destination.

  * Starting the migration job, and monitoring the progress.

  * Promoting the migration job when you want to switch your application to the new instance.




## Before you begin

  1. Ensure you meet the following requirements: 
     * You configured your source database for migration. See [ Configure source database for continuous migrations ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/configure-source-database) or [ Configure source database for a one-time migration](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/configure-source-database-one-time). 
     * You configured [ source network connectivity](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/networking-methods-source). 
     * You have the [ source connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-source-connection-profile) for your database. 
     * You [ created and configured your destination](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/configure-destination-database) AlloyDB for PostgreSQL instance.
     * You configured [ destination network connectivity](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/networking-methods-destination). 
     * You have the [ destination connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-destination-connection-profile) for the AlloyDB for PostgreSQL instance.
     * You [ converted your source SQL Server schema](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/convert-sql) with a Database Migration Service conversion workspace. 
     * Optional: If you want to manage your own certificates for the migration job, you [ prepared the necessary encryption keys](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/cmek-for-migration-jobs). 
  2. In the Google Cloud console, on the project selector page, select or [ create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Enable the Database Migration Service and AlloyDB for PostgreSQL Admin APIs. 

[ Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=datamigration.googleapis.com,sqladmin.googleapis.com)




### Required roles

To get the permissions that you need to create a migration job for heterogeneous SQL Server migrations, ask your administrator to grant the required IAM roles on your project for the following [ accounts involved in the migration process](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/access-control):

  * User account that performs the migration: 
    * [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) 
  * Database Migration Service service account: 
    * [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) 



For more information about granting roles, see [ Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the Identity and Access Management documentation. 

These predefined roles contain the permissions required to perform heterogeneous SQL Server migrations with Database Migration Service. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to perform heterogeneous SQL Server migrations with Database Migration Service: 

  * `datamigration.* `
  * `resourcemanager.projects.get `
  * `resourcemanager.projects.list `
  * `alloydb.clusters.create`
  * `alloydb.clusters.get`
  * `alloydb.clusters.list`
  * `alloydb.clusters.update`
  * `alloydb.clusters.delete`
  * `alloydb.instances.create`
  * `alloydb.instances.get`
  * `alloydb.instances.list`
  * `alloydb.instances.update`
  * `alloydb.instances.delete`
  * `alloydb.operations.get`
  * `compute.machineTypes.list `
  * `compute.machineTypes.get `
  * `compute.projects.get `



You might also be able to get these permissions with [ custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [ predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions). 

## Define settings and create a migration job

To create a migration job, perform the following steps:

  1. In the Google Cloud console, go to the **Migration jobs** page. 

[ Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

  2. Click **Create migration job**. 

The migration job configuration wizard page opens. This wizard contains multiple panels that walk you through each configuration step.

You can pause the creation of a migration job at any point by clicking **SAVE & EXIT**. All of the data that you enter up to that point is saved in a draft migration job. You can finish your draft migration job later. See [ Update a draft migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/manage-migration-jobs#update-draft).

  3. On the **Get started** page, enter the following information: 
     * Migration job name 

This is a human-readable name for your migration job. This value is displayed in the Google Cloud console.

     * Migration job ID 

This is a machine-readable identifier for your migration job. You use this value to work with migration jobs by using Database Migration Service Google Cloud CLI commands or API.

     * From the **Source database engine** list, select your SQL Server source database.
     * From the **Destination database engine** drop-down menu, select **AlloyDB for PostgreSQL**.
     * Optional: If you want to manage your own data encryption key for the migration, expand the **Advanced encryption options** and do the following: 
       1. Select the **Cloud KMS key** option.
       2. Leave the default **Cloud KMS** option for the **Key type** setting. 

Database Migration Service doesn't support the _Cloud KMS with autokey_ feature.

       3. From the **Select a customer-managed key** drop-down menu, select your encryption key. You can also manually enter the fully qualified identifier for your key. 
  4. Click **Save and continue**.
  5. On the **Define your source** page, perform the following actions: 
     1. From the **Source connection profile** drop-down menu, select your source connection profile. 
     2. _Continuous migrations only_ : In this section, you can choose how to perform the full dump phase of your migration The default value is Automatic. For more information on available settings, expand the _Full dump settings_ section: 

#### Full dump settings

You can use the following settings for making the full dump:

        * **Automatic**

When the migration is started, Database Migration Service pulls existing data in addition to newly changed data from the included objects. This is the default option. 

        * **Customer-managed**

When the migration is started, Database Migration Service pulls only newly changed data from the included tables.

Choose this option if you want to perform the full dump on your own.

In the **CDC start position (LSN)** field, provide a SQL Server LSN (Log Sequence Number) to start the CDC from.

     3. In the **Source read settings** section, configure how many concurrent connections Database Migration Service can make to your source instance. For more information on available settings, expand the _Source read settings_ section: 

#### Source read settings

Database Migration Service adjusts the number of connections to ensure the best performance within provided connection limits. Increasing the maximum connection limit can improve the migration speed, but introduces additional load on your source databases. 

You can use the following settings:

        * **Maximum concurrent full dump connections** defines the maximum number of concurrent full dump connections. The actual number of concurrent connections might be lower at any particular time.

Default: `50` connections

Custom: minimum `1`, maximum `50` connections

        * **Maximum concurrent CDC connections**

Default: `5` connections

Custom: minimum `1`, maximum `50` connections

     4. Click **Save and continue**.
  6. On the **Define a destination** page, from the **Destination connection profile** drop-down menu, select your destination connection profile. 
  7. In the **Customize destination configuration** section, configure the following settings: 

Maximum concurrent destination connections
    

Default value: `128`

Allowed values: minimum `2`, maximum `256`

You can customize how many maximum concurrent connections Database Migration Service can make to your destination instance. 

Database Migration Service adjusts the number of connections to ensure the best performance within provided connection limit. Increasing the maximum connection limit can improve the migration speed, but introduces additional load on your destination databases.

Transaction timeout
    

Default value: `30`

Allowed values: minimum `30`, maximum `300`

During the migration process, Database Migration Service can encounter certain issues that cause the transaction to time out. You can adjust the number of seconds that Database Migration Service waits for the transaction to complete before it is canceled. 

Canceled transactions don't cause your migration job to fail. The migration job continues to copy data, but moves to the **Running with errors** status. You can view migration job details to check what issues need to be addressed. 

  8. Click **Save and continue**.
  9. On the **Configure migration objects** page, perform the following actions: 
     1. From the **Conversion workspace** drop-down menu, select your conversion workspace.
     2. In the **Select objects to migrate** section, use the checkboxes to select which objects you want to include in this migration job. This list is populated based on what objects you converted to PostgreSQL schema in the conversion workspace. 
  10. Click **Save and continue**.
  11. On the **Test and create migration job** , perform the following actions: 
     1. (Optional) Click **Test job** to verify if Database Migration Service can successfully identify all the backup files and establish the necessary network connections. 

If the test fails, you can consult the error messages to address the problem, and run the test again. For more information on possible errors, see [ Diagnose issues](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/diagnose-issues).

     2. Click **Create and start job** to begin your migration. 

If you want to perform the migration job at a different time, click **Save** and return later to run the job. See [ Start a migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/manage-migration-jobs#start).




## What's next

  * [ Start migration jobs](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/manage-migration-jobs#start)
  * [ Monitor migration jobs](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/migration-job-metrics)
  * [ Promote a migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/finalize-migration)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
