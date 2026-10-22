---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver/finalize-migration/
title: Promote a migration job \u00a0|\u00a0 Database Migration Service for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:40.334474+00:00
---

# Promote a migration job  |  Database Migration Service for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver/finalize-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Homogeneous migration to SQL Server ](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview)



Send feedback 

#  Promote a migration job Stay organized with collections  Save and categorize content based on your preferences. 

For continuous migrations, you can initiate the promotion process after it's time to move reads and writes to the destination databases. Promotion means that the migrated Cloud SQL databases become now accessible for all read and write operations.

You can promote a migration job or promote selected databases from a migration job.

  1. Initiate the promotion. To avoid data loss, make sure to stop all writes, running scripts, and client connections to the source database. The downtime period begins here.
  2. Make sure that all the available data from transaction log files is replicated to the Cloud SQL for SQL Server destination instance. 

### Cloud SQL for SQL Server sources

For Cloud SQL for SQL Server sources, Database Migration Service automatically handles monitoring the transaction log exports. You don't need to perform any additional actions after you stop writes on the source instance. You can proceed with promoting the migration job. 

### Self-managed or Amazon RDS sources

For self-managed or Amazon RDS sources, you can achieve this result by performing one of the following actions: 

     * Stop your [ automated backup file uploads](https://docs.cloud.google.com/database-migration/docs/sqlserver/automate-backup-exports), or upload the last transaction log file. Monitor the [ unprocessed transaction log backups size](https://docs.cloud.google.com/database-migration/docs/sqlserver/migration-job-metrics) to determine when Database Migration Service finishes processing that file. 
     * Optionally, you can upload a transaction log file whose name ends in `.trn.final` suffix. Database Migration Service stops continuous loads when it detects a backup file whose name matches the [ `.trn.final` suffix convention](https://docs.cloud.google.com/database-migration/docs/sqlserver/export-backup-files). 

When Database Migration Service finishes processing that file, migration job status changes to [ **Ready to promote**](https://docs.cloud.google.com/database-migration/docs/sqlserver/migration-job-statuses#ready-to-promote). 

  3. Perform the promote action: 

### Console

You can promote a migration job from in Database Migration Service or from the destination instance page.

**In Database Migration Service:**

     1. In the Google Cloud console, go to the **Migration jobs** page. 

[Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

     2. On the **Jobs** tab, click the display name of the migration job that you want to promote. 

The migration job details page opens.

     3. Perform one of the following promote actions: 
        * If you want to promote all databases, on the toolbar, click **Promote**.
        * If you want to promote only specific databases, select them on the **Databases** tab and click **Promote**.
     4. In the dialog, ensure no errors are displayed, and then click **Promote**.

**From the destination instance:**

     1. In the Google Cloud console, go to the **Cloud SQL Instances** page. 

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql/instances)

     2. Click the display name of the destination instance for your migration. 

The instance details page opens.

     3. In the **Migration** section, click **Promote**.
     4. In the dialog, ensure no errors are displayed, and then click **Promote**.

### gcloud

Before using any of the command data below, make the following replacements: 

     * MIGRATION_JOB_ID with your migration job identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration migration-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/list) command to list all migration jobs in a given region and view their identifiers. 

     * REGION with the identifier of the region where your connection profile is saved.
     * Optional: Database Migration Service migrates all databases in your source by default. If you want to migrate only specific databases, use the `--databases-filter` flag and specify their identifiers as a comma-separated list.

For example: `--databases-filter=my-business-database,my-other-database`

You can later edit migration jobs that you created with the `--database-filter flag` by using the [`gcloud database-migration migration-jobs update`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/update) command.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs \
    promote MIGRATION_JOB_ID \
      --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs `
    promote MIGRATION_JOB_ID `
      --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud database-migration migration-jobs ^
    promote MIGRATION_JOB_ID ^
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
  4. The destination instance or the databases that you selected are promoted, and your migrated databases are now accessible for all read and write operations. The migration job status changes to `Completed`.
  5. The application can now be connected to the Cloud SQL instance and the migration job can be safely deleted. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
