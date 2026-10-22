---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/logging/
title: Logging \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:28.841778+00:00
---

# Logging  |  Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to AlloyDB for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/scenario-overview)



Send feedback 

#  Logging Stay organized with collections  Save and categorize content based on your preferences. 

Database Migration Service uses Cloud Logging. You can access two log categories to acquire detailed information on events that occur with relation to your migration jobs: Database Migration Service logs, and the destination AlloyDB for PostgreSQL logs.

## Database Migration Service logs

Database Migration Service for Oracle to AlloyDB for PostgreSQL provides [ structured logs](https://docs.cloud.google.com/logging/docs/structured-logging#structured_logging_special_fields) for the [ `datamigration.googleapis.com/MigrationJob`](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#resource:-migrationjob), [ `datamigration.googleapis.com/ConnectionProfile`](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles), and [ `datamigration.googleapis.com/PrivateConnection`](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections) resources. These logs represent real-world events, such as when a migration job is created, when Database Migration Service reads information from your source database, or when a connection profile is edited.

Each log entry contains a `jsonPayload.textMessage` field with a description to help you better understand the event. There are different types of messages, for example:

Sample log messages for the `datamigration.googleapis.com/MigrationJob` resource   
---  
Log text message | Description  
`FULL DUMP read is completed for table: {SCHEMA_TABLE_NAME}` | This message means that Database Migration Service finished reading specific table data in your source database for the full dump phase. This message indicates that the full dump phase for the table is in an advanced stage and is likely to complete shortly.  
`Successfully loaded {NUMBER} FULL DUMP rows into table: {SCHEMA_TABLE_NAME}` | This message means that Database Migration Service finished writing a batch of rows into a specific table in your destination cluster during the full dump phase.  
`Successfully applied {NUMBER} CDC rows into table: {SCHEMA_TABLE_NAME}` | This message means that Database Migration Service finished writing a batch of rows into a specific table in your destination cluster during the CDC phase.  
`Accessing data of table: {SCHEMA_TABLE_NAME} for data processing purpose` | When you [ use a CMEK](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/cmek-for-migration-jobs) for your migration job, this message indicates that Database Migration Service accessed the encryption key to process data for a specific table.  
  
## AlloyDB for PostgreSQL cluster logs

AlloyDB for PostgreSQL also provides log entries for your destination cluster. See the [ AlloyDB for PostgreSQL logs reference ](https://docs.cloud.google.com/logging/docs/api/platform-logs#alloydb) in the Cloud Logging documentation.

## View and query logs

To view your logs, perform the following:

  1. In the Google Cloud console, go to the **Migration jobs** page. 

[ Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

  2. In the **Jobs** tab, click the display name of the migration job for which you want to view logs. 

The migration job details page opens.

  3. On the migration job details page, click **View logs** and perform one of the following: 
     * To view migration job logs, select **Migration job logs**.
     * To view logs for your AlloyDB for PostgreSQL destination cluster, select **Destination instance logs**.

The **Logs Explorer** page opens.

  4. On the **Logs Explorer** page, you can use the drop-down menus to modify the query and filter log entries. For example, to filter migration job logs for events where Database Migration Service accessed a specific table in your source database, you can use a query similar to the following: 
         
         resource.type="datamigration.googleapis.com/MigrationJob"
         resource.labels.migration_job_id="MIGRATION_JOB_ID"
         jsonPayload.textMessage:"Accessing data of table"




## What's next

  * For more information on using Logs Explorer, see [ View logs by using Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

  * For a detailed reference of what fields are supported in Database Migration Service log entries, see [ Database Migration Service logs reference](https://docs.cloud.google.com/logging/docs/api/platform-logs#cloud_database_migration_service).

  * To get a complete, step-by-step migration walkthrough, see [ Oracle to AlloyDB for PostgreSQL migration guide](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/guide).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
