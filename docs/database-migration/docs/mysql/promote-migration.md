---
url: https://docs.cloud.google.com/database-migration/docs/mysql/promote-migration/
title: Promote a migration job \u00a0|\u00a0 Database Migration Service for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:50.216517+00:00
---

# Promote a migration job  |  Database Migration Service for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/mysql/promote-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview)



Send feedback 

#  Promote a migration job Stay organized with collections  Save and categorize content based on your preferences. 

For continuous migrations, you can initiate the promotion process after it's time to move reads and writes to the destination databases. Promotion means that the migrated Cloud SQL databases become now accessible for all read and write operations.

You can promote a migration job or promote selected databases from a migration job.

  1. Stop all writes, running scripts, and client connections to the source database. The downtime period begins here. 
  2. Make sure that all the available data from transaction log files is replicated to the Cloud SQL destination instance. 
  3. Wait until the [ replication delay metric](https://docs.cloud.google.com/database-migration/docs/mysql/migration-job-metrics) is at or close to zero. This means that the migration job has processed all outstanding changes. 

You can promote a migration even if the replication delay isn't at zero. This can reduce the database downtime, but may affect the accuracy of the data in the destination. 

  4. Perform the promote action: 

### Console

     1. In the Google Cloud console, go to the **Migration jobs** page. 

[ Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

     2. On the **Jobs** tab, click the display name of the migration job that you want to promote.

The migration job details page opens.

     3. Perform one of the following promote actions: 
        * If you want to promote all databases included in the migration, on the migration job's toolbar, click **Promote**.

The promote migration job dialog appears.

        * If you want to promote only specific databases, select them using the checkboxes next to the database names and on the **Databases** tab, click **Promote**.

The dialog with a number of databases that you want to promote appears.

     4. In the dialog, ensure that no errors are displayed, and then click **Promote**.

### gcloud

Before using any of the command data below, make the following replacements: 

     * MIGRATION_JOB_ID with your migration job identifier. 

If you don't know the identifier, you can use the [ `gcloud database-migration migration-jobs list`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/list) command to list all migration jobs in a given region and view their identifiers. 

     * REGION with the identifier of the region where your connection profile is saved.

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

     * Use the [ `gcloud database-migration migration-jobs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/describe) command with the MIGRATION_JOB_ID to view the status of the migration job.
     * Use the [ `gcloud database-migration operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe) command with the OPERATION_ID to see the status of the operation itself.
  5. The destination instance or the databases that you selected are promoted, and your migrated databases are now accessible for all read and write operations. The migration job status changes to `Completed`.
  6. The application can now be connected to the Cloud SQL instance and the migration job can be safely deleted. 



## What's next

  * [Verify migration data](https://docs.cloud.google.com/database-migration/docs/mysql/verify-migration) for completeness.
  * Optional: [Set up cascading read replicas](https://docs.cloud.google.com/database-migration/docs/mysql/set-up-cascading-replica) for your promoted Cloud SQL instance.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
