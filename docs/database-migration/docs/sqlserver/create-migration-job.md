---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver/create-migration-job/
title: Create a migration job \u00a0|\u00a0 Database Migration Service for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:33:22.637599+00:00
---

# Create a migration job  |  Database Migration Service for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver/create-migration-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Homogeneous migration to SQL Server ](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview)



Send feedback 

#  Create a migration job Stay organized with collections  Save and categorize content based on your preferences. 

Database Migration Service uses migration jobs to migrate data from your source databases to the Cloud SQL destination instance. Migration jobs help you organize the source and destination connection profiles, define settings specific to the migration process, monitor the progress, and safely finalize the whole operation.

Creating a migration job includes performing the following tasks:

  * Selecting source and destination connection profiles.

  * Choosing which databases detected in your source instance you want to migrate.

  * Performing a migration job test to ensure that Database Migration Service is able to connect to your data source and destination.

  * Starting the migration job, and monitoring the progress.

  * Promoting the migration job when you want to switch your application to the new instance.




Database Migration Service comes equipped with a wizard to help you create a migration job. This wizard consists of four panels: Get started, Define a source to a destination, Configure migration objects, and Test and create migration job. Information on how to populate each panel is provided in the various sections of this page.

## Before you begin

  1. Ensure you meet the following requirements: 
     * You have a Cloud Storage bucket for SQL Server backup files.
     * Your full backup and transaction log files are uploaded to the Cloud Storage bucket.
     * You have a source connection profile for the Cloud Storage bucket.
     * You created and configured your destination Cloud SQL for SQL Server instance, and you have a destination connection profile for the instance.
  2. In the Google Cloud console, on the project selector page, select or [ create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Enable the Database Migration Service, Compute Engine, Cloud Storage, and Cloud SQL Admin APIs. 

[ Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,datamigration.googleapis.com,sqladmin.googleapis.com,storage.googleapis.com)




### Required roles

To get the permissions that you need to create migration jobs in Database Migration Service, ask your administrator to grant you the following IAM roles on your project: 

  * [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) 
  * [ Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) 
  * [ Cloud SQL Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.editor) (`roles/cloudsql.editor`) 



For more information about granting roles, see [ Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to perform homogeneous SQL Server migrations with Database Migration Service. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to perform homogeneous SQL Server migrations with Database Migration Service: 

  * `datamigration.* `
  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`
  * `cloudsql.instances.create`
  * `cloudsql.instances.get`
  * `cloudsql.instances.list`
  * `cloudsql.databases.get`
  * `cloudsql.databases.delete`
  * `cloudsql.operations.get`
  * `compute.machineTypes.list`
  * `compute.machineTypes.get`
  * `compute.projects.get`
  * `storage.buckets.create`
  * `storage.buckets.list`
  * `storage.objects.list`



You might also be able to get these permissions with [ custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [ predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions). 

## Define settings and create a migration job

To create a migration job, perform the following steps:

### Console

  1. In the Google Cloud console, go to the **Migration jobs** page. 

[ Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

  2. Click **Create migration job**. 

The migration job configuration wizard page opens. This wizard contains multiple panels that walk you through each configuration step.

You can pause the creation of a migration job at any point by clicking **SAVE & EXIT**. All of the data that you enter up to that point is saved in a draft migration job. You can finish your draft migration job later. See [ Update a draft migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver/manage-migration-jobs#update-draft).

  3. On the **Get started** page, enter the following information: 
     * Migration job name 

This is a human-readable name for your migration job. This value is displayed in the Google Cloud console.

     * Migration job ID 

This is a machine-readable identifier for your migration job. You use this value to work with migration jobs by using Database Migration Service Google Cloud CLI commands or API.

     * From the **Source database engine** list, select **SQL Server** or **Amazon RDS for SQL Server**.

The **Destination database engine** and **Migration job type** fields are populated automatically and can't be changed.

  4. Click **Save and continue**.
  5. On the **Define your source** page, do the following: 
     1. Use the drop-down menu to select your source connection profile. 

If you don't yet have a source connection profile, you can click **Create connection profile** directly in the drop-down menu. For more information on creating connection profiles, see [ Create a source connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver/create-source-connection-profile).

     2. If you want to use a differential backup file in your migration, in the **Customize source configurations** section check the **Use differential backups** check-box. 

Differential backups are useful if you need to replicate a lot of data that appeared in your database since the full backup and you want to handle it in bulk rather than upload multiple transaction log files. For more information on supported backup types, see [ Supported backup file types](https://docs.cloud.google.com/database-migration/docs/sqlserver/supported-backup-files). 

If you use differential backups, make sure you create the `diff` folder in your Cloud Storage bucket. See [ Store backup files in a Cloud Storage bucket](https://docs.cloud.google.com/database-migration/docs/sqlserver/storage-buckets). 

     3. Click **Save and continue**.
  6. On the **Define a destination** page, use the drop-down menu to select your destination connection profile. 

If you don't yet have a destination connection profile, you can click **Create connection profile** directly in the drop-down menu. For more information on creating connection profiles, see [ Create a destination connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver/create-destination-connection-profile).

  7. Click **Save and continue**.
  8. On the **Configure migration databases** page, perform the following actions: 
     1. In the **Select databases to migrate** section, use the checkboxes to select which databases you want to include in this migration job. This list is populated based on the folders you created in the Cloud Storage bucket for your backup backup files. 

You can add and remove databases from the migration job later. See [ Add or remove databases from a migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver/manage-migration-jobs#add-databases).

     2. (Optional) If you use encrypted backups, provide the encryption keys for your backups. For more details on using encrypted backups, see [ Use encrypted backups](https://docs.cloud.google.com/database-migration/docs/sqlserver/backup-file-encryption). 

Perform the following actions:

        * Click **Edit details** next to the database you selected for migration. 

The **Encryption** side panel opens.

        * Use the **Encryption key** drop-down menus to select your keys.
        * In the **Password** field, enter the encryption key password.
        * Click **Save and exit**.
  9. Click **Save and continue**.
  10. On the **Test and create migration job** , perform the following actions: 
     1. (Optional) Click **Test job** to verify if Database Migration Service can successfully identify all the backup files and establish the necessary network connections. 

If the test fails, you can consult the error messages to address the problem, and run the test again. For more information on possible errors, see [ Diagnose issues](https://docs.cloud.google.com/database-migration/docs/sqlserver/diagnose-issues).

     2. Click **Create and start job** to begin your migration. 

If you want to perform the migration job at a different time, click **Save** and return later to run the job. See [ Start a migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver/manage-migration-jobs#start).




### gcloud

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

  * MIGRATION_JOB_ID with a machine-readable identifier for your migration job. You use this value to work with migration jobs by using Database Migration Service Google Cloud CLI commands or API.
  * REGION with the region identifier where you want to save the migration job.
  * MIGRATION_JOB_NAME with a human-readable name for your migration job. This value is displayed in Database Migration Service in the Google Cloud console.
  * SOURCE_CONNECTION_PROFILE_ID with a machine-readable identifier of the source connection profile.
  * DESTINATION_CONNECTION_PROFILE_ID with a machine-readable identifier of the destination connection profile. 
  * COMMA_SEPARATED_DATABASE_ID_LIST with a comma-separated list of database identifiers of the SQL Server you want to migrate from your backup files. These identifiers need to be the same as the [ database folder names in your Cloud Storage](https://docs.cloud.google.com/database-migration/docs/sqlserver/storage-buckets). 

For example: `--sqlserver-databases=my-business-database,my-other-database`

  * **Differential backup configuration** : If you use differential backup files for the migration, add the `--sqlserver-diff-backup` flag to your command. By default, migration jobs don't use differential backup files and ignore the `diff` folder in your Cloud Storage bucket. 

For more information on supported backup files, see [ Supported backup file types](https://docs.cloud.google.com/database-migration/docs/sqlserver/supported-backup-files). 

  * (Optional) MAPPING_FILE_FOR_PATHS_TO_ENCRYPTION_KEYS with your local disk path to a configuration file that maps paths to encryption keys in Cloud Storage with their relevant database identifiers. For more information on how to create this mapping file, see [Use encrypted backups](https://docs.cloud.google.com/database-migration/docs/sqlserver/backup-file-encryption). 

For example: `--sqlserver-encrypted-databases=~/encryption-keys-mapping-file.json`




Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs \
    create MIGRATION_JOB_ID \
      --no-async \
      --region=REGION \
      --display-name=MIGRATION_JOB_NAME \
      --source=SOURCE_CONNECTION_PROFILE_ID \
      --destination=DESTINATION_CONNECTION_PROFILE_ID \
      --sqlserver-databases=COMMA_SEPARATED_DATABASE_ID_LIST \
      --sqlserver-encrypted-databases=MAPPING_FILE_FOR_PATHS_TO_ENCRYPTION_KEYS \
      --type=CONTINUOUS

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs `
    create MIGRATION_JOB_ID `
      --no-async `
      --region=REGION `
      --display-name=MIGRATION_JOB_NAME `
      --source=SOURCE_CONNECTION_PROFILE_ID `
      --destination=DESTINATION_CONNECTION_PROFILE_ID `
      --sqlserver-databases=COMMA_SEPARATED_DATABASE_ID_LIST `
      --sqlserver-encrypted-databases=MAPPING_FILE_FOR_PATHS_TO_ENCRYPTION_KEYS `
      --type=CONTINUOUS

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs ^
    create MIGRATION_JOB_ID ^
      --no-async ^
      --region=REGION ^
      --display-name=MIGRATION_JOB_NAME ^
      --source=SOURCE_CONNECTION_PROFILE_ID ^
      --destination=DESTINATION_CONNECTION_PROFILE_ID ^
      --sqlserver-databases=COMMA_SEPARATED_DATABASE_ID_LIST ^
      --sqlserver-encrypted-databases=MAPPING_FILE_FOR_PATHS_TO_ENCRYPTION_KEYS ^
      --type=CONTINUOUS

You should receive a response similar to the following:
    
    
    Waiting for migration job [MIGRATION_JOB_ID]
    to be created with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Created migration job MIGRATION_JOB_ID [OPERATION_ID]
    

**Result**

The migration job is now created. You can proceed with the migration process: 

  * (Optional) [ Perform a migration job test](https://docs.cloud.google.com/database-migration/docs/sqlserver/manage-migration-jobs#test) to check if Database Migration Service can reach all the necessary source and destination entities.
  * [ Start the migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver/manage-migration-jobs#start) to begin moving your data to the destination instance.



## What's next

  * [ Start migration jobs](https://docs.cloud.google.com/database-migration/docs/sqlserver/manage-migration-jobs#start)
  * [ Monitor migration jobs](https://docs.cloud.google.com/database-migration/docs/sqlserver/migration-job-metrics)
  * [ Promote a migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver/finalize-migration)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
