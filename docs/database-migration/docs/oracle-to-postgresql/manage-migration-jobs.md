---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/manage-migration-jobs/
title: View and manage migration progress \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:02.436665+00:00
---

# View and manage migration progress  |  Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/manage-migration-jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/scenario-overview)



Send feedback 

#  View and manage migration progress Stay organized with collections  Save and categorize content based on your preferences. 

For heterogeneous Oracle to Cloud SQL for PostgreSQL migrations, you can monitor and manage your migration progress for the whole migration job, or for individual tables included in the migration job.

This page describes the actions you can take at each level. For more information, see the  Manage migration jobs and  Manage individual tables sections.

## Manage migration jobs

In the Google Cloud console, you can perform actions in bulk for migration jobs that have the same [ status](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/migration-job-statuses). You can perform actions on a single migration job both in the Google Cloud console (either from the Database Migration Service console or directly from the destination Cloud SQL instance page) and by using Google Cloud CLI.

You can perform any of the following actions on your migration job:

Action | Description  
---|---  
Start | Start migration jobs is that aren't in the **Running** or **Starting** state. See [ Migration job statuses](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/migration-job-statuses).  
Stop | Stop a running migration job. The data movement is paused. The migration job status first changes to `Stopping` and then to `Stopped`. You can resume, delete, or [ promote](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/finalize-migration) a stopped migration job. _For continuous migrations_ : In some cases, the source database must retain the data until you resume the migration job. The retention period for the source database may be limited. If the migration job is paused for longer than the retention period, and then the migration job is resumed, this can cause the migration job to fail. If this occurs, then delete or restart the migration job.   
Resume | When you resume a migration job, Database Migration Service resumes the data movement operations: 

  * For continuous migrations stopped during the CDC phase, Database Migration Service resumes the replication of change events that accumulate when the migration job is stopped. 
  * For migration jobs stopped during the full dump phase (either a one-time or a continuous migration), Database Migration Service resumes copying the data it didn't copy before you stopped the migration. 

  
Restart |  You can restart a migration job that encountered an error and can't proceed with data replication.  The result of restarting a migration job depends on why it failed:

  * If the replication has failed because of an error on one or more source or destination database tables, then restarting the migration job wipes all data from destination database tables included in the migration job. 
  * Restarting the migration job doesn't cause Database Migration Service to replicate new tables that you created in the source database. You first need to [ add the tables to the conversion workspace and convert their schema](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/work-with-conversion-workspaces#add-source-objects). 

  
Edit | See  Edit a migration job.   
Delete | A migration job can be deleted. The outcome depends on the status of the job: 

  * If the migration job is in the `Completed` status, then the record is deleted from the migration job list.
  * If the migration job is in any other status, then there's an option to choose to delete the associated destination Cloud SQL for PostgreSQL instance.

  
Promote | During the migration process, your destination database is put into a read-only state where it is fully managed by Database Migration Service. When you want to switch your application to the migrated destination database, promoting the migration job updates the destination database into a standalone replica. See [ Promote a migration](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/finalize-migration).  
  
### Review a migration job

  1. In the Google Cloud console, go to the **Migration jobs** page. 

[ Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

  2. Select a migration job to see its details page, which includes: 
     * Migration job metadata, such as the display name, ID, migration type, source connection profile, source database engine, destination, connectivity method, date and time that the migration job was created, and how long the migration job is running. 
     * Migration job status and substatus, and additional information. Different actions are available depending on the migration job's status and substatus.



### Start a migration job

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



### Stop a migration job

You can stop a [ running](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/migration-job-statuses#running) migration job at any time by performing the following steps:

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



### Resume a migration job

You can resume a [ stopped](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/migration-job-statuses#stopped) migration job by performing the following steps:

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



### Restart a migration job

When you restart a migration job, Database Migration Service wipes all data from the **destination** tables - your source data isn't affected. The migration process then begins anew, starting with the full dump stage.

To restart a migration job, perform the following steps:

### Console

You can restart a migration job from the Database Migration Service console or from the destination instance page.

**From the Database Migration Service console:**

  1. In the Google Cloud console, go to the **Migration jobs** page. 

[ Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

  2. In the **Jobs** tab, click the display name of the migration job that you want to restart. 

The migration job details page opens.

  3. Click **Restart**.
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



### Update a draft migration job

To finish creating a migration job, perform the following steps:

  1. In the Google Cloud console, go to the **Migration jobs** page. 

[ Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

  2. In the **Drafts** tab, click the display name of the migration job that you want to finish creating. 

The migration job creation wizard opens.

  3. Finish creating the migration job. See [ Create a migration job](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-migration-job).



### Edit a migration job

You can modify the configuration information for the source, such as the database tables and schemas in the source that Database Migration Service will migrate to the destination. Database Migration Service uses this configuration information to migrate the correct data from the source into the destination.

#### Add or remove objects from migration

To add or remove tables or schemas from the migration, do the following:

  1. Go to the **Migration jobs** page in the Google Cloud console.

[ Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

  2. Click the display name of the migration job that you want to modify. An overview page appears for the migration job.

  3. In the **Select objects to migrate** section, select or clear the check boxes to change the tables and schemas in the source that Database Migration Service will migrate into the destination.

Make sure that the destination has any schemas that you select.
  4. Click **Save** or **Save and Restart**.

     * If you click **Save** , then Database Migration Service will move only historical data for the schemas and tables that you select.

     * If you click **Save and Restart** , then Database Migration Service will start the migration from the beginning, after cleaning any tables that you select in the destination.



#### Adjust maximum concurrent connections to source database

You can customize how many maximum concurrent connections Database Migration Service can make to your source instance for the **full dump phase** or the **CDC phase**.

  1. Go to the **Migration jobs** page in the Google Cloud Console.

[ Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

  2. Click the display name of the migration job that you want to modify. An overview page appears for the migration job.

  3. Expand the **Customize source configuration** > **Source read settings** section.

  4. In the **Maximum concurrent full dump connections** or **Maximum concurrent CDC connections** sections, use **Custom** field to enter the maximum connections limit for either the full dump or CDC phases.

  5. Click **Save** or **Save and Restart**.




#### Adjust destination configuration settings

You can customize transaction timeout and the maximum number of concurrent connections for your destination database:

  1. Go to the **Migration jobs** page in the Google Cloud console.

[ Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

  2. Click the display name of the migration job that you want to modify. 

An overview page appears for the migration job.

  3. Expand the **Customize destination configuration** section, and modify the following settings: 

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

  4. Click **Save** or **Save and Restart**.



### Test a migration job

Before you run the migration job, you can perform a test operation to check if Database Migration Service can reach all the necessary source and destination entities. In the Google Cloud console, you can only test draft migration jobs that you create in the migration job creation wizard (see [ Create a migration job](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-migration-job)).

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



## Manage individual tables

For heterogeneous Oracle to Cloud SQL for PostgreSQL migrations, you can view status details for specific tables included in your migration job.

### View all tables in a job

To view details for all tables in a migration job, do the following:

### Console

  1. In the Google Cloud console, go to the **Migration jobs** page. 

[ Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

  2. In the **Jobs** tab, click the display name of your migration job. 

The migration job details page opens.

  3. Select the **Tables** tab and view all tables included in your job. You can also use interactive filters to narrow the list. 



### gcloud

Before using any of the command data below, make the following replacements: 

  * MIGRATION_JOB_ID with your migration job identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration migration-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/list) command to list all migration jobs in a given region and view their identifiers. 

  * REGION with the identifier of the region where your migration job is saved. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration objects list \
      --migration-job=MIGRATION_JOB_ID \
      --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration objects list `
      --migration-job=MIGRATION_JOB_ID `
      --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration objects list ^
      --migration-job=MIGRATION_JOB_ID ^
      --region=REGION

#### Result

This command returns the state, phase, and error details for all tables included in the migration job separated by empty lines. 

**Note:** The following example adds indentation for easier viewing, but keep in mind that the `ERROR` object in the response is a JSON-formatted single-line string that contains all issues for the specific object. 
    
    
    SOURCE_OBJECT: {'schema': 'Schema1', 'table': 'MyTable1', 'type': 'TABLE'}
    STATE: RUNNING
    PHASE: CDC
    ERROR: {}
    
    SOURCE_OBJECT: {'schema': 'Production', 'table': 'MyTable2', 'type': 'TABLE'}
    STATE: RUNNING
    PHASE: FULL_DUMP
    ERROR:
      { 'code': 2,
        'details': [
            { '@type': 'type.googleapis.com/google.rpc.ErrorInfo',
              'domain': 'datamigration.googleapis.com',
              'metadata': {
                'errorMessage': '[DATABASE] error trying to write processed rows.
                  Line: 2619 Position: 0 Schema: production Table: mytable2',
                'errorScope': 'NON_GLOBAL',
                'objectId': 'Production_MyTable2',
                'projectName': 'PROJECT_ID',
                'resourceName': 'MIGRATION_JOB_ID',
                'severity': 'ERROR'
              },
              'reason': 'DESTINATION_WRITE_ERROR'
            }
          ],
        'message': 'Encountered errors with your migration job table. Check the `details`
                      array for specific information on each issue.'
      }
    

### View details for a single table

To view migration details for a single table, do the following:

### Console

  1. In the Google Cloud console, go to the **Migration jobs** page. 

[ Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

  2. In the **Jobs** tab, click the display name of your migration job. 

The migration job details page opens.

  3. Select the **Tables** tab, and click the table that you want to inspect. You can also use interactive filters to narrow the list. 

The table details side panel opens.




### gcloud

Before using any of the command data below, make the following replacements: 

  * MIGRATION_JOB_ID with your migration job identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration migration-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/list) command to list all migration jobs in a given region and view their identifiers. 

  * REGION with the identifier of the region where your migration job is saved. 
  * SCHEMA_NAME with the name of the parent schema that contains your table. 
  * TABLE_NAME with the name of your table.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration objects lookup \
      --migration-job=MIGRATION_JOB_ID \
      --region=REGION \
      --schema=SCHEMA_NAME \
      --table=TABLE_NAME

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration objects lookup `
      --migration-job=MIGRATION_JOB_ID `
      --region=REGION `
      --schema=SCHEMA_NAME `
      --table=TABLE_NAME

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud database-migration objects lookup ^
      --migration-job=MIGRATION_JOB_ID ^
      --region=REGION ^
      --schema=SCHEMA_NAME ^
      --table=TABLE_NAME

#### Result

This command returns the state, phase, creation time, and error details for your table. The whole response is a multiline, yaml-formatted string. For example: 
    
    
    createTime: '2025-06-02T10:20:29.792832Z'
    error:
      code: 2
      details:
      - '@type': type.googleapis.com/google.rpc.ErrorInfo
        domain: datamigration.googleapis.com
        metadata:
          errorMessage: '[DATABASE] error trying to write processed rows.
                  Line: 2619 Position: 0 Schema: production Table: mytable2'
          errorScope: NON_GLOBAL
          objectId: Production_MyTable2
          projectName: PROJECT_ID
          resourceName: MIGRATION_JOB_ID
          severity: ERROR
        reason: DESTINATION_WRITE_ERROR
      message: Encountered errors with your migration job table. Check the `details` array
        for specific information on each issue.
    name: projects/PROJECT_ID/locations/REGION/migrationJobs/MIGRATION_JOB_ID/objects/TABLE_UUID
    phase: FULL_DUMP
    sourceObject:
      schema: Production
      table: MyTable2
      type: TABLE
    state: RUNNING
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
