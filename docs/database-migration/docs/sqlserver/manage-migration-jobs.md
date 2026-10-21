---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver/manage-migration-jobs/
title: Manage migration jobs \u00a0|\u00a0 Database Migration Service for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:39.903915+00:00
---

# Manage migration jobs  |  Database Migration Service for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver/manage-migration-jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Homogeneous migration to SQL Server ](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview)



Send feedback 

#  Manage migration jobs Stay organized with collections  Save and categorize content based on your preferences. 

In the Google Cloud console, you can perform actions in bulk for migration jobs that have the same [ status](https://docs.cloud.google.com/database-migration/docs/sqlserver/migration-job-statuses). You can perform actions on a single migration job both in the Google Cloud console (either from the Database Migration Service console or directly from the destination Cloud SQL instance page) and by using Google Cloud CLI.

You can perform the following actions on migration jobs:

Action | Description  
---|---  
Edit | You can edit non-draft migration jobs to make the following changes:

  * Update the migration job display name with gcloud CLI. For more information, see Edit a non-draft migration job.
  * Add or remove databases from your migration job. For more information, see Add or remove databases.

  
Start | Start migration jobs is that aren't in the **Running** or **Starting** state. See [ Migration job statuses](https://docs.cloud.google.com/database-migration/docs/sqlserver/migration-job-statuses).  
Stop | Stop a running migration job. The data movement is paused. The migration job status first changes to `Stopping` and then to `Stopped`. You can resume, delete, or [ promote](https://docs.cloud.google.com/database-migration/docs/sqlserver/finalize-migration) a stopped migration job.  
Resume | If you stop a migration job during the incremental load, you can resume it later. When you resume a migration job, Database Migration Service picks up all transaction log files that accumulate when the migration job is stopped.  
Restart |  You can restart a migration job that encountered an error and can't proceed with data replication. The result of restarting a migration job depends on one of the following reasons why it failed:

  * Failed migration jobs that can't recover from the error re-try the whole migration process, including the initial load of the full backup file.
  * If the replication has failed because of an error on one or more source or destination databases, then restarting the migration wipes all data from the destination databases.
  * If you create a new folder for another database after starting the migration and [ add it to databases selected for migration](https://docs.cloud.google.com/database-migration/docs/sqlserver/manage-migration-jobs#add-databases), then restarting the migration also replicates the new databases into the destination instance.

  
Delete | A migration job can be deleted. The outcome depends on the status of the job: 

  * If the migration job is in the `Completed` status, then the record is deleted from the migration job list.
  * If the migration job is in any other status, then there's an option to choose to delete the destination Cloud SQL instance/primary pair.

  
Promote | During the migration process, your destination Cloud SQL for SQL Server databases are put into recovery mode where they are fully managed by Database Migration Service. You can't perform any read or write operations on the destination databases until you promote the migration job or the selected databases. For more information, see [ Promote a migration](https://docs.cloud.google.com/database-migration/docs/sqlserver/finalize-migration).   
View | You can view the details of a specific database in a migration job or all databases that you selected for migration.  
  
## Start a migration job

When your migration job is fully created (that is, it isn't saved in a draft state), you can start it at any time to begin migrating data.

To start a migration job, perform the following steps:

### Console

You can start a migration job from the Database Migration Service console or from the destination instance page.

**From the Database Migration Service console:**

  1. In the Google Cloud console, go to the **Migration jobs** page. 

[ Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

  2. In the **Jobs** tab, click the display name of the migration job that you want to start. 

The migration job details page opens.

  3. Click **Start**.
  4. In the dialog, click **Start**.



**From the destination instance:**

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page. 

[ Go to Cloud SQL Instances](https://console.cloud.google.com/sql/instances)

  2. Click the display name of the destination instance for your migration. 

The instance details page opens.

  3. In the **Migration** section, click **Start**.
  4. In the dialog, click **Start**.



### gcloud

Before using any of the command data below, make the following replacements: 

  * MIGRATION_JOB_ID with your migration job identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration migration-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/list) command to list all migration jobs in a given region and view their identifiers. 

  * REGION with the identifier of the region where your migration job is saved.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs \
    start MIGRATION_JOB_ID \
      --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs `
    start MIGRATION_JOB_ID `
      --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs ^
    start MIGRATION_JOB_ID ^
      --region=REGION

#### Result

The action is performed in an asynchronous manner. As such, this command returns an [ Operation entity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.operations) that represents a long-running operation: 
    
    
    done: false
    metadata:
      '@type': type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata
      apiVersion: v1
      createTime: '2024-02-20T12:20:24.493106418Z'
      requestedCancellation: false
      target: MIGRATION_JOB_ID
      verb: start
    name: OPERATION_ID
    

To see if your operation is successful, you can query the returned operation object, or check the status of the migration job: 

  * Use the [ `gcloud database-migration migration-jobs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to view the status of the migration job.
  * Use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) with the OPERATION_ID to see the status of the operation itself.



## Stop a migration job

You can stop a [ running](https://docs.cloud.google.com/database-migration/docs/sqlserver/migration-job-statuses#running) migration job at any time by performing the following steps:

### Console

You can stop a migration job from the Database Migration Service console or from the destination instance page.

**From the Database Migration Service console:**

  1. In the Google Cloud console, go to the **Migration jobs** page. 

[ Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

  2. In the **Jobs** tab, click the display name of the migration job that you want to stop. 

The migration job details page opens.

  3. Click **Stop**.
  4. In the dialog, click **Stop**.



**From the destination instance:**

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page. 

[ Go to Cloud SQL Instances](https://console.cloud.google.com/sql/instances)

  2. Click the display name of the destination instance for your migration. 

The instance details page opens.

  3. In the **Migration** section, click **Stop**.
  4. In the dialog, click **Stop**.



### gcloud

Before using any of the command data below, make the following replacements: 

  * MIGRATION_JOB_ID with your migration job identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration migration-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/list) command to list all migration jobs in a given region and view their identifiers. 

  * REGION with the identifier of the region where your connection profile is saved.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs \
    stop MIGRATION_JOB_ID \
      --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs `
    stop MIGRATION_JOB_ID `
      --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs ^
    stop MIGRATION_JOB_ID ^
      --region=REGION

#### Result

The action is performed in an asynchronous manner. As such, this command returns an [ Operation entity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.operations) that represents a long-running operation: 
    
    
    done: false
    metadata:
      '@type': type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata
      apiVersion: v1
      createTime: '2024-02-20T12:20:24.493106418Z'
      requestedCancellation: false
      target: MIGRATION_JOB_ID
      verb: stop
    name: OPERATION_ID
    

To see if your operation is successful, you can query the returned operation object, or check the status of the migration job: 

  * Use the [ `gcloud database-migration migration-jobs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to view the status of the migration job.
  * Use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) with the OPERATION_ID to see the status of the operation itself.



## Resume a migration job

You can resume a [ stopped](https://docs.cloud.google.com/database-migration/docs/sqlserver/migration-job-statuses#stopped) migration job by performing the following steps:

### Console

You can resume a migration job from the Database Migration Service console or from the destination instance page.

**From the Database Migration Service console:**

  1. In the Google Cloud console, go to the **Migration jobs** page. 

[ Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

  2. In the **Jobs** tab, click the display name of the migration job that you want to resume. 

The migration job details page opens.

  3. Click **Resume**.
  4. In the dialog, click **Resume**.



**From the destination instance:**

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page. 

[ Go to Cloud SQL Instances](https://console.cloud.google.com/sql/instances)

  2. Click the display name of the destination instance for your migration. 

The instance details page opens.

  3. In the **Migration** section, click **Resume**.
  4. In the dialog, click **Resume**.



### gcloud

Before using any of the command data below, make the following replacements: 

  * MIGRATION_JOB_ID with your migration job identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration migration-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/list) command to list all migration jobs in a given region and view their identifiers. 

  * REGION with the identifier of the region where your connection profile is saved.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs \
    resume MIGRATION_JOB_ID \
      --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs `
    resume MIGRATION_JOB_ID `
      --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs ^
    resume MIGRATION_JOB_ID ^
      --region=REGION

#### Result

The action is performed in an asynchronous manner. As such, this command returns an [ Operation entity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.operations) that represents a long-running operation: 
    
    
    done: false
    metadata:
      '@type': type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata
      apiVersion: v1
      createTime: '2024-02-20T12:20:24.493106418Z'
      requestedCancellation: false
      target: MIGRATION_JOB_ID
      verb: resume
    name: OPERATION_ID
    

To see if your operation is successful, you can query the returned operation object, or check the status of the migration job: 

  * Use the [ `gcloud database-migration migration-jobs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to view the status of the migration job.
  * Use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) with the OPERATION_ID to see the status of the operation itself.



## Restart a migration job

To restart a migration job, perform the following steps:

### Console

You can restart a migration job from the Database Migration Service console or from the destination instance page.

**From the Database Migration Service console:**

  1. In the Google Cloud console, go to the **Migration jobs** page. 

[ Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

  2. On the **Jobs** tab, click the display name of the migration job that you want to restart. 

The migration job details page opens.

  3. Perform one of the following restart actions: 
     * If you want to restart all databases included in the migration, on the migration job's toolbar, click **Restart**.

The restart migration job dialog appears.

     * If you want to restart only specific databases, select them using the checkboxes next to the database names and on the **Databases** tab, click **Restart**.

The dialog with a number of databases that you want to restart appears.

  4. In the dialog, click **Restart**.



**From the destination instance:**

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page. 

[ Go to Cloud SQL Instances](https://console.cloud.google.com/sql/instances)

  2. Click the display name of the destination instance for your migration. 

The instance details page opens.

  3. In the **Migration** section, click **Restart**.
  4. In the dialog, click **Restart**.



### gcloud

Before using any of the command data below, make the following replacements: 

  * MIGRATION_JOB_ID with your migration job identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration migration-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/list) command to list all migration jobs in a given region and view their identifiers. 

  * REGION with the identifier of the region where your migration job is saved.
  * Optional: Database Migration Service migrates all databases in your source by default. If you want to migrate only specific databases, use the `--databases-filter` flag and specify their identifiers as a comma-separated list.

For example: `--databases-filter=my-business-database,my-other-database`

You can later edit migration jobs that you created with the `--database-filter flag` by using the [`gcloud database-migration migration-jobs update`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update) command.




Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs \
    restart MIGRATION_JOB_ID \
      --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs `
    restart MIGRATION_JOB_ID `
      --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs ^
    restart MIGRATION_JOB_ID ^
      --region=REGION

#### Result

The action is performed in an asynchronous manner. As such, this command returns an [ Operation entity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.operations) that represents a long-running operation: 
    
    
    done: false
    metadata:
      '@type': type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata
      apiVersion: v1
      createTime: '2024-02-20T12:20:24.493106418Z'
      requestedCancellation: false
      target: MIGRATION_JOB_ID
      verb: restart
    name: OPERATION_ID
    

To see if your operation is successful, you can query the returned operation object, or check the status of the migration job: 

  * Use the [ `gcloud database-migration migration-jobs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to view the status of the migration job.
  * Use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) with the OPERATION_ID to see the status of the operation itself.



## Update a draft migration job

To finish creating a migration job, perform the following steps:

### Console

  1. In the Google Cloud console, go to the **Migration jobs** page. 

[ Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

  2. In the **Drafts** tab, click the display name of the migration job that you want to finish creating. 

The migration job creation wizard opens.

  3. Finish creating the migration job. See [ Create a migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver/create-migration-job).



### gcloud

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

  * MIGRATION_JOB_ID with a machine-readable identifier for your migration job.
  * REGION with the region identifier where you want to save the connection profile.
  * MIGRATION_JOB_NAME with a human-readable name for your migration job. This value is displayed in Database Migration Service in the Google Cloud console.
  * SOURCE_CONNECTION_PROFILE_ID with a machine-readable identifier of the source connection profile.
  * DESTINATION_CONNECTION_PROFILE_ID with a machine-readable identifier of the destination connection profile. 
  * **Differential backup configuration** : You can configure whether the migration job can use differential backup files from the Cloud Storage bucket. Add one of the following flags to your command: 
    * `--sqlserver-diff-backup` to enable differential backup files for your migration
    * `--no-sqlserver-diff-backup` to disable differential backup files for your migration

For more information on supported backup files, see [ Supported backup file types](https://docs.cloud.google.com/database-migration/docs/sqlserver/supported-backup-files). 

  * COMMA_SEPARATED_DATABASE_ID_LIST with a comma-separated list of database identifiers of the SQL Server you want to migrate from your backup files.



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
      --type=CONTINUOUS

You should receive a response similar to the following:
    
    
    Waiting for migration job [MIGRATION_JOB_ID]
    to be updated with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Updated migration job MIGRATION_JOB_ID [OPERATION_ID]
    

## Add or remove databases from the migration job

To add a new database to the migration job, you first need to create a new dedicated folder in your Cloud Storage bucket and upload the backup files there. See [ Configure Cloud Storage buckets](https://docs.cloud.google.com/database-migration/docs/sqlserver/storage-buckets).

When you have the necessary backup files in the Cloud Storage bucket, perform the following steps:

### Console

  1. In the Google Cloud console, go to the **Migration jobs** page. 

[ Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

  2. In the **Jobs** tab, click the display name of your migration job. 

The migration job details page opens.

  3. Click **Edit**.
  4. In the **Select databases to migrate** section, use the checkboxes to select the new database you want to add to the migration job or clear the ones that you want to remove. 
  5. (Optional) If you use encrypted backups, provide the encryption keys for your backups. For more details on using encrypted backups, see [ Use encrypted backups](https://docs.cloud.google.com/database-migration/docs/sqlserver/backup-file-encryption). 

Perform the following actions:

     * Click **Edit details** next to the database you selected for migration. 

The **Encryption** side panel opens.

     * Use the **Encryption key** menus to select your keys.
     * In the **Password** field, enter the encryption key password.
     * Click **Save and exit**.



### gcloud

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

  * MIGRATION_JOB_ID with your migration job identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration migration-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/list) command to list all migration jobs in a given region and view their identifiers. 

  * REGION with the identifier of the region where your connection profile is saved.
  * COMMA_SEPARATED_DATABASE_ID_LIST with a comma-separated list of database identifiers of the SQL Server you want to migrate from your backup files. These identifiers need to be the same as the [ database folder names in your Cloud Storage](https://docs.cloud.google.com/database-migration/docs/sqlserver/storage-buckets). 

For example: `--sqlserver-databases=my-business-database,my-other-database`




Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs \
    update MIGRATION_JOB_ID \
      --region=REGION \
      --sqlserver-databases=COMMA_SEPARATED_DATABASE_ID_LIST

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs `
    update MIGRATION_JOB_ID `
      --region=REGION `
      --sqlserver-databases=COMMA_SEPARATED_DATABASE_ID_LIST

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs ^
    update MIGRATION_JOB_ID ^
      --region=REGION ^
      --sqlserver-databases=COMMA_SEPARATED_DATABASE_ID_LIST

You should receive a response similar to the following:
    
    
    Waiting for migration job [MIGRATION_JOB_ID]
    to be updated with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Updated migration job MIGRATION_JOB_ID [OPERATION_ID]
    

## Edit a non-draft migration job

For non-draft migration jobs, you can use Google Cloud CLI to change the display name of the migration job:

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

  * MIGRATION_JOB_ID with your migration job identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration migration-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/list) command to list all migration jobs in a given region and view their identifiers. 

  * REGION with the identifier of the region where your connection profile is saved.
  * MIGRATION_JOB_NAME with a human-readable name for your migration job. This value is displayed in Database Migration Service in the Google Cloud console.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs \
    update MIGRATION_JOB_ID \
      --region=REGION \
      --display-name=MIGRATION_JOB_NAME

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs `
    update MIGRATION_JOB_ID `
      --region=REGION `
      --display-name=MIGRATION_JOB_NAME

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs ^
    update MIGRATION_JOB_ID ^
      --region=REGION ^
      --display-name=MIGRATION_JOB_NAME

You should receive a response similar to the following:
    
    
    Waiting for migration job [MIGRATION_JOB_ID]
    to be updated with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Updated migration job MIGRATION_JOB_ID [OPERATION_ID]
    

## Test a migration job

Before you run the migration job, you can perform a test operation to check if Database Migration Service can reach all the necessary source and destination entities. In the Google Cloud console, you can only test draft migration jobs that you create in the migration job creation wizard (see [ Create a migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver/create-migration-job)).

With gcloud CLI, you can test migration jobs that are created, but not yet started.

Before using any of the command data below, make the following replacements: 

  * MIGRATION_JOB_ID with your migration job identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration migration-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/list) command to list all migration jobs in a given region and view their identifiers. 

  * REGION with the identifier of the region where your connection profile is saved.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs \
    verify MIGRATION_JOB_ID \
      --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs `
    verify MIGRATION_JOB_ID `
      --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration migration-jobs ^
    verify MIGRATION_JOB_ID ^
      --region=REGION

#### Result

The action is performed in an asynchronous manner. As such, this command returns an [ Operation entity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.operations) that represents a long-running operation: 
    
    
    done: false
    metadata:
      '@type': type.googleapis.com/google.cloud.clouddms.v1.OperationMetadata
      apiVersion: v1
      createTime: '2024-02-20T12:20:24.493106418Z'
      requestedCancellation: false
      target: MIGRATION_JOB_ID
      verb: verify
    name: OPERATION_ID
    

To see if your operation is successful, you can query the returned operation object, or check the status of the migration job: 

  * Use the [ `gcloud database-migration migration-jobs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to view the status of the migration job.
  * Use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) with the OPERATION_ID to see the status of the operation itself.



## View migration details for a specific database

When your migration job is fully created (that is, it isn't saved in a draft state), you can use Google Cloud CLI to view details about a specific database in that migration job.

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

  * MIGRATION_JOB_ID with your migration job identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration migration-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/list) command to list all migration jobs in a given region and view their identifiers. 

  * REGION with the identifier of the region where your connection profile is saved.
  * DATABASE_NAME with the name of the database.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration objects lookup --migration-job=MIGRATION_JOB_ID \
      --region=REGION --database=DATABASE_NAME

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration objects lookup --migration-job=MIGRATION_JOB_ID `
      --region=REGION --database=DATABASE_NAME

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration objects lookup --migration-job=MIGRATION_JOB_ID ^
      --region=REGION --database=DATABASE_NAME

#### Result

The output is similar to the following: 
    
    
    createTime: '2025-03-21T17:05:19.211441641Z'
    name: PROJECT_ID
    phase: FULL_DUMP
    sourceObject:
      database: DATABASE_NAME
      type: DATABASE
    state: RUNNING
    

To see if your operation is successful, you can query the returned operation object, or check the status of the migration job: 

  * Use the [ `gcloud database-migration migration-jobs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to view the status of the migration job.
  * Use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) with the OPERATION_ID to see the status of the operation itself.



## View migration details for specific databases

When your migration job is fully created (that is, it isn't saved in a draft state), you can use Google Cloud CLI to list all databases that you selected for that migration job and view details about them.

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

  * MIGRATION_JOB_ID with your migration job identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration migration-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/list) command to list all migration jobs in a given region and view their identifiers. 

  * REGION with the identifier of the region where your connection profile is saved.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration objects list --migration-job=MIGRATION_JOB_ID \
      --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration objects list --migration-job=MIGRATION_JOB_ID `
      --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration objects list --migration-job=MIGRATION_JOB_ID ^
      --region=REGION

#### Result

The output is similar to the following: 
    
    
    Waiting for migration job MIGRATION_JOB_ID
    to fetch source objects with OPERATION_ID
    
    Waiting for operation OPERATION_ID to complete...done.
    
    SOURCE_OBJECT                            STATE    PHASE      ERROR
    {'database': 'db1', 'type': 'DATABASE'}  RUNNING  FULL_DUMP
    {'database': 'db2', 'type': 'DATABASE'}  STOPPED  CDC        {'code': 1, 'message': 'Internal error'}
    

To see if your operation is successful, you can query the returned operation object, or check the status of the migration job: 

  * Use the [ `gcloud database-migration migration-jobs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command to view the status of the migration job.
  * Use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) with the OPERATION_ID to see the status of the operation itself.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
