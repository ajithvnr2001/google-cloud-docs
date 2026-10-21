---
url: https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-actions/
title: Manage migration jobs \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:51.120392+00:00
---

# Manage migration jobs  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-actions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgres/scenario-overview)



Send feedback 

#  Manage migration jobs Stay organized with collections  Save and categorize content based on your preferences. 

You can perform actions from the migration jobs list, from the single migration job details page, or directly from the destination instance page in Cloud SQL. In the Google Cloud console, you can perform actions on multiple jobs simultaneously if they all have the same [ status](https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-statuses). You can perform actions on a single migration job both in the Google Cloud console and by using Google Cloud CLI.

You can perform some actions on migration jobs as a whole, while other actions (such as restart, promote, or viewing details) can also be performed on selected individual databases within a migration job.

You can perform the following actions on migration jobs:

Action | Description  
---|---  
Edit | To make the following changes, edit the migration job:

  * Change between migrating all databases and specific databases.
  * Add or remove databases in any migration state or phase, as many times as you need. When you remove a database, Database Migration Service stops the replication process on that database, but doesn't remove it from the destination instance. For more information, see Add or remove databases.
  * Edit the [data dump parallelism](https://docs.cloud.google.com/database-migration/docs/postgres/known-limitations#parallelism-considerations) level of a running migration job. You must save and restart the job after you make the changes.
  * Update the migration job display name with gcloud CLI. For more information, see Edit a non-draft migration job.

  
Start | Start migration jobs that were created without being started. You can start jobs that aren't in the **Running** or **Starting** state. See [ Migration job statuses](https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-statuses).  
Stop | Stop a running migration job at any time. The data migration is halted, and the migration job status changes to `Stopping` and subsequently to `Stopped`.

  * If the migration job is stopped during the initial full dump phase, you can delete or restart the job. However, **WAL logs will continue to accumulate in replication slots** on the source database, which can eventually lead to the source database running out of disk space. In addition, Database Migration Service continues to poll for replication delay metrics, continuing to consume network traffic.
  * If the migration job is stopped during the change data capture (CDC) phase, you can resume, [promote](https://docs.cloud.google.com/database-migration/docs/postgres/promote-migration), or delete the job.

Monitor the replication slots and disk space of your source database server. Deleting the migration job cleans all replication slots on the source and stops network traffic.  
Resume | If a continuous migration job was stopped during the CDC phase, then it can be resumed. Resuming the migration job restarts replication of events and data changes that accumulated during the stopped time.  
Restart | If a migration job failed and isn't recoverable, or was stopped during the initial full dump phase, you can restart it from the beginning. Restarting the migration wipes all data from any destination databases that are impacted by errors, and takes a new full dump. If new databases were created on the source PostgreSQL server since the migration started, restarting the migration also replicates those new databases into the destination instance. You can restart all databases in the migration job or only selected databases.  
**Delete** | Delete a migration job. You can delete migration jobs in any state. However, you can delete a running migration job only in the Google Cloud console. The outcome depends on the status of the job:

  * If the migration job status is `Completed`, then the record is deleted from the migration job list.
  * If the migration job is in any other status, there's an option in the Google Cloud console to choose whether to delete the destination Cloud SQL instance.

Deleting a migration job removes allocated replication slots on the source database and stops network traffic. Deleting a migration job doesn't delete the source databases.  
[Promote](https://docs.cloud.google.com/database-migration/docs/postgres/promote-migration) | Promote the destination instance from a replica to a standalone primary database instance, and disconnect the destination instance from the source. You can promote the entire migration job or promote selected individual databases. For more information, see [ Promote a migration](https://docs.cloud.google.com/database-migration/docs/postgres/promote-migration).  
View specific database | View migration details for a specific database configured for migration.  
View all databases | View migration details for all databases configured for migration.  
  
## Start a migration job

When your migration job is fully created (that is, it isn't saved in a draft state), you can start it at any time to begin migrating data.

To start a migration job, perform the following steps:

### Console

  1. In the Google Cloud console, go to the **Migration jobs** page. 

[ Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

  2. In the **Jobs** tab, click the display name of the migration job that you want to start. 

The migration job details page opens.

  3. Click **Start**.
  4. In the dialog, click **Start**.



### gcloud

Before using any of the command data below, make the following replacements: 

  * MIGRATION_JOB_ID with your migration job identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration migration-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/list) command to list all migration jobs in a given region and view their identifiers. 

  * REGION with the identifier of the region where your connection profile is saved.



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

  * Use the [ `gcloud database-migration migration-jobs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command with the MIGRATION_JOB_ID to view the status of the migration job.
  * Use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command with the OPERATION_ID to see the status of the operation itself.



## Stop a migration job

You can stop a [ running](https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-statuses#running) migration job at any time. When you stop a migration job, data migration is halted, and the migration job status changes to `Stopping` and subsequently to `Stopped`.

**Caution:** When a migration job is stopped, **WAL logs continue to accumulate in replication slots** on the source database server. This can eventually lead to your source database running out of disk space. In addition, Database Migration Service continues to poll for replication delay metrics, continuing to consume network traffic. Monitor your source database server's replication slots and disk space. If you don't plan to resume the migration, delete the migration job to clean up the replication slots and stop network traffic. 

To stop a migration job, perform the following steps:

### Console

  1. In the Google Cloud console, go to the **Migration jobs** page. 

[ Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

  2. In the **Jobs** tab, click the display name of the migration job that you want to stop. 

The migration job details page opens.

  3. Click **Stop**.
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

If a continuous migration job was stopped during the change data capture (CDC) phase, you can resume it. Resuming the migration job restarts replication of events and data changes that accumulated on the source database while the job was stopped.

To resume a [ stopped](https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-statuses#stopped) migration job, perform the following steps:

### Console

  1. In the Google Cloud console, go to the **Migration jobs** page. 

[ Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

  2. In the **Jobs** tab, click the display name of the migration job that you want to resume. 

The migration job details page opens.

  3. Click **Resume**.
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

If a migration job failed and isn't recoverable, or was stopped during the initial full dump phase, you can restart it from the beginning.

Restarting the migration wipes all data from any destination databases that are impacted by errors, and initiates a new full dump. If new databases were created on the source PostgreSQL server since the migration started, restarting the migration also replicates those new databases into the destination instance.

You can restart all databases in the migration job, or restart only specific databases.

To restart a migration job, perform the following steps:

### Console

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



### gcloud

Before using any of the command data below, make the following replacements: 

  * MIGRATION_JOB_ID with your migration job identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration migration-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/list) command to list all migration jobs in a given region and view their identifiers. 

  * REGION with the identifier of the region where your migration job is saved.
  * Optional: Database Migration Service migrates all databases in your source by default. If you want to migrate only specific databases, use the `--databases-filter` flag and specify their identifiers as a comma-separated list.

For example: `--databases-filter=my-business-database,my-other-database`

You can later edit migration jobs that you created with the `--databases-filter` flag by using the [`gcloud database-migration migration-jobs update`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update) command.




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

  3. Finish creating the migration job. See [ Create a migration job](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job).



### gcloud

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [`gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command to verify if your operation is successful.

Before using any of the command data below, make the following replacements: 

  * MIGRATION_JOB_ID with a machine-readable identifier for your migration job.
  * REGION with the region identifier where you want to save the connection profile.
  * MIGRATION_JOB_NAME with a human-readable name for your migration job. This value is displayed in Database Migration Service in the Google Cloud console.
  * SOURCE_CONNECTION_PROFILE_ID with a machine-readable identifier of the source connection profile.
  * DESTINATION_CONNECTION_PROFILE_ID with a machine-readable identifier of the destination connection profile. 
  * COMMA_SEPARATED_DATABASE_ID_LIST with a comma-separated list of database identifiers of the PostgreSQL you want to migrate.



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
      --databases-filter=COMMA_SEPARATED_DATABASE_ID_LIST \
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
      --databases-filter=COMMA_SEPARATED_DATABASE_ID_LIST `
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
      --databases-filter=COMMA_SEPARATED_DATABASE_ID_LIST ^
      --type=CONTINUOUS

You should receive a response similar to the following:
    
    
    Waiting for migration job [MIGRATION_JOB_ID]
    to be updated with [OPERATION_ID]
    
    Waiting for operation [OPERATION_ID] to complete...done.
    
    Updated migration job MIGRATION_JOB_ID [OPERATION_ID]
    

## Add or remove databases from the migration job

You can add or remove databases in any migration state or phase, as many times as you need. When you remove a database, Database Migration Service stops the replication process on that database, but doesn't remove it from the destination Cloud SQL instance.

**Note:** You must save the migration job after each change. 

To add or remove databases from your migration job, perform the following steps:

  1. In the Google Cloud console, go to the **Migration jobs** page. 

[ Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

  2. In the **Jobs** tab, click the display name of your migration job. The migration job details page opens.
  3. Click **Edit**.
  4. In the **Select databases to migrate** section, use the checkboxes to select the new database you want to add to the migration job or clear the ones that you want to remove.
  5. Click **Save**.



## Edit a non-draft migration job

To edit the data dump parallelism level of a running migration job, see [Parallelism considerations](https://docs.cloud.google.com/database-migration/docs/postgres/known-limitations#parallelism-considerations). You must save and restart the migration job after changing the parallelism settings.

For non-draft migration jobs, you can use Google Cloud CLI to change the display name of the migration job:

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [`gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command to verify if your operation is successful.

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

Before you run the migration job, you can perform a test operation to check if Database Migration Service can reach all the necessary source and destination entities. In the Google Cloud console, you can only test draft migration jobs that you create in the migration job creation wizard (see [ Create a migration job](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job)).

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

  * Use the [ `gcloud database-migration migration-jobs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command with the MIGRATION_JOB_ID to view the status of the migration job.
  * Use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command with the OPERATION_ID to see the status of the operation itself.



## View migration details for a specific database

When your migration job is fully created (that is, it isn't saved in a draft state), you can use Google Cloud CLI to view details about a specific database in that migration job.

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [`gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command to verify if your operation is successful.

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

This sample uses the optional `--no-async` flag so that all operations are performed synchronously. This means that some commands might take a while to complete. You can skip the `--no-async` flag to run commands asynchronously. If you do, you need to use the [`gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command to verify if your operation is successful.

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
