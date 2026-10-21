---
url: https://docs.cloud.google.com/sql/docs/mysql/import-export/
title: Best practices for importing and exporting data \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:01.570482+00:00
---

# Best practices for importing and exporting data  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/import-export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Best practices for importing and exporting data Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/import-export "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/import-export "View this page for the SQL Server database engine")

This page provides best practices for importing and exporting data with Cloud SQL. For step-by-step instructions for importing data into Cloud SQL, see [Importing Data](https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-sql).

To export data from Cloud SQL for use in a MySQL instance that you manage, see [Exporting and importing using SQL dump files](https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-sql) or [Export and import using CSV files](https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-csv).

**Note:** If you are migrating an entire database from a supported database server (on-premises, in AWS or Google Cloud) to a new Cloud SQL instance, you can use the [Database Migration Service](https://docs.cloud.google.com/database-migration/docs) instead of exporting and then importing files.

## Best practices for importing and exporting

The following are best practices to consider when importing and exporting data:

  * Use the same SQL mode for import and export
  * Don't use Cloud Storage Requester Pays buckets
  * Minimize the performance impact of exports
  * Use the correct flags when you create a SQL dump file
  * Compress data to reduce cost.
  * Reduce long-running import and export processes
  * Use InnoDB
  * MySQL import and migration jobs containing metadata with DEFINER clause
  * Verify the imported database



### Use the same SQL Mode for import and export

The SQL Mode setting affects how Cloud SQL interprets SQL queries. For example, if you export from a database without Strict SQL enabled, then try to import to Cloud SQL (which enables Strict SQL by default), the import might fail. The best practice is to use the same SQL Mode on import that you used for export. 

Review the SQL Mode on both the source and target databases for compatibility. Pay particular attention to the flags that enable Strict SQL mode. If Strict SQL is NOT set on your database, you will likely want to remove it in Cloud SQL. If you remove Strict SQL, you must set another flag.

To verify that your Cloud SQL instance has the desired mode set, run `SELECT @@GLOBAL.sql_mode;`. 

### Don't use Cloud Storage Requester Pays buckets

You cannot use a Cloud Storage bucket that has [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays) enabled for imports and exports from Cloud SQL.

### Minimize the performance impact of exports

For a standard export from Cloud SQL, the export is run while the database is online. When the data being exported is smaller, the impact is likely to be minimal. However, when there are large databases, or large objects, such as BLOBs in the database, there's the possibility that the export might degrade database performance. This might impact the time it takes to perform database queries and operations against the database. After you start an export, it's not possible to stop it if your database starts to respond slowly.

To prevent slow responses during an export, you can:

  1. Take the export from a read replica. This might be a good option if you take exports frequently (daily or more often), but the amount of data being exported is small. To perform an export from a read replica, use the Google Cloud Console, `gcloud`, or REST API export functions on your read replica instance. See [ Create read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica) for more information about how to create and manage read replicas.

  2. Use serverless export. With serverless export, Cloud SQL creates a separate, temporary instance to offload the export operation. Offloading the export operation allows databases on the primary instance to continue to serve queries and perform operations at the usual performance rate. When the data export is complete, the temporary instance is deleted automatically. This might be a good option if you're taking a one-time export of a large database. Use the Google Cloud Console, `gcloud`, or REST API [ export functions](https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-sql), with the `offload` flag, to perform a serverless export operation. 

During a serverless export operation you can run some other operations, such as instance edit, import, and failover. However, if you select `delete`, the export operation stops some time after you delete the instance, and it doesn't export any data.

See the following table to learn about the operations that can be blocked while a serverless export operation is running: Current operation | New operation | Blocked? | Any operation | Serverless export | Yes  
---|---|---  
Serverless export | Any operation except serverless export | No  
Any operation except serverless export | Any operation except serverless export | Yes  
  
A serverless export takes longer to do than a standard export, because it takes time to create the temporary instance. At a minimum, it takes longer than five minutes, but for larger databases, it might be longer. Consider the impact to time, performance, and cost before determining which type of export to use.


**Note:** Serverless export costs extra. See the [pricing page](https://cloud.google.com/sql/pricing#serverless-export-pricing).

### Use the correct flags when you create a SQL dump file

If you do not use the right flags when you export your data to a SQL dump file, your import might be unsuccessful. For information about creating a SQL dump file for import into Cloud SQL, see [Creating a SQL dump file](https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-sql). 

### Compress data to reduce cost

Cloud SQL supports importing and exporting both compressed and uncompressed files. Compression can save significant storage space on Cloud Storage and reduce your storage costs, especially when you are exporting large instances.

**Note:** Compression can degrade export performance.

When you export a SQL dump or CSV file, use a `.gz` file extension to compress the data. When you import a file with an extension of `.gz`, it is decompressed automatically.

### Reduce long-running import and export processes

Imports into Cloud SQL and exports out of Cloud SQL can take a long time to complete, depending on the size of the data being processed. This can have the following impacts: 

  * You can't stop a long-running Cloud SQL instance operation. 
  * You can perform only one import or export operation at a time for each instance, and a long-running import or export blocks other operations, such as daily automated backups. Serverless exports allow you to run other operations, including editing instances, import, failover, and unblocking daily automated backups. 



You can decrease the amount of time it takes to complete each operation by using the Cloud SQL import or export functionality with smaller batches of data.

For exports, you can perform the export from a [read replica](https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica) or use [serverless export](https://docs.cloud.google.com/sql/docs/mysql/import-export#serverless) to minimize the impact on database performance and allow other operations to run on your instance while an export is running. 

**Note:** Serverless export costs extra. See the [pricing page](https://cloud.google.com/sql/pricing#export-offload). For more tips, see [Diagnosing Issues with Cloud SQL Instances](https://docs.cloud.google.com/sql/docs/mysql/diagnose-issues#import-export). 

### Use InnoDB

InnoDB is the only supported storage engine for MySQL instances.

You can convert your tables from MyISAM to InnoDB by piping the output of mysqldump through a sed script as follows:
    
    
    mysqldump --databases [DATABASE_NAME] \
    -h [INSTANCE_IP] -u [USERNAME] -p [PASSWORD] \
    --hex-blob --default-character-set=utf8mb4 | sed 's/ENGINE=MyISAM/ENGINE=InnoDB/g' > [DATABASE_FILE].sql

**Warning:** Don't do this if your `mysqldump` file contains the `mysql` schema. Those files must remain in MyISAM.

### MySQL import and migration jobs containing metadata with DEFINER clause

Because a MySQL import or migration job doesn't migrate user data, sources and dump files which contain metadata defined by users with the `DEFINER` clause will fail to be imported or migrated as the users don't yet exist there.

To identify which `DEFINER` values exist in your metadata, use the following queries (or search in your dump file) and check if there are entries for either `root%localhost` or users that don't exist in the target instance.
    
    
    SELECT DISTINCT DEFINER FROM INFORMATION_SCHEMA.EVENTS;
    SELECT DISTINCT DEFINER FROM INFORMATION_SCHEMA.ROUTINES;
    SELECT DISTINCT DEFINER FROM INFORMATION_SCHEMA.TRIGGERS;
    SELECT DISTINCT DEFINER FROM INFORMATION_SCHEMA.VIEWS;

To run an import or migration job from a source which includes such metadata, you can do one of the following:

  * Create the users on your target Cloud SQL instance before starting your import or migration job.
  * Update the `DEFINER` clause to `INVOKER` on your source MySQL instance or dump file before starting your import or migration job.

**Important:** In both cases, if your metadata was created by `'root'@'localhost'`, the process fails. Change the definer to a different user before starting the import or migration job.

### Verify the imported database

After an import operation is complete, connect to your database and run the appropriate database commands to make sure the contents are correct. For example, [connect](https://docs.cloud.google.com/sql/docs/mysql/quickstart#connect) and list the databases, tables, and specific entries.

## Known limitations

For a list of known limitations, see [Issues with importing and exporting data](https://docs.cloud.google.com/sql/docs/mysql/known-issues#import-export).

## Automating export operations

Although Cloud SQL doesn't provide a built-in way to automate database exports, you can build your own automation tool using several Google Cloud components. To learn more, see [ this tutorial](https://docs.cloud.google.com/architecture/scheduling-cloud-sql-database-exports-using-cloud-scheduler). 

## Troubleshooting

The following sections cover troubleshooting related to both import and export operations.

### Troubleshooting import operations

Issue | Troubleshooting | `HTTP Error 409: Operation failed because another operation was already in progress`. | There is already a pending operation for your instance. Only one operation is allowed at a time. Try your request after the current operation is complete.  
---|---  
The import operation is taking too long. | Too many active connections can interfere with import operations. Close unused operations. Check the CPU and memory usage of your Cloud SQL instance to make sure there are plenty of resources available. The best way to ensure maximum resources for the import is to restart the instance before beginning the operation. A restart:

  * Closes all connections.
  * Ends any tasks that may be consuming resources.

  
An import operation can fail when one or more users referenced in the dump file don't exist. | Before importing a dump file, all the database users who own objects or were granted permissions on objects in the dumped database must exist in the target database. If they don't, the import operation fails to recreate the objects with the original ownership or permissions. [ Create the database users](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users#creating) before importing.  
An import operation fails with an error that a table doesn't exist. | Tables can have foreign key dependencies on other tables, and depending on the order of operations, one or more of those tables might not yet exist during the import operation. Things to try: Add the following line at the start of the dump file:
    
    
    SET FOREIGN_KEY_CHECKS=0;
      

Additionally, add this line at the end of the dump file:
    
    
    SET FOREIGN_KEY_CHECKS=1;
      

These settings deactivate data integrity checks while the import operation is in progress, and reactivate them after the data is loaded. This doesn't affect the integrity of the data on the database, because the data was already validated during the creation of the dump file.  
  
### Troubleshooting export operations

Issue | Troubleshooting | `HTTP Error 409: Operation failed because another operation was already in progress.` | There is already a pending operation for your instance. Only one operation is allowed at a time. Try your request after the current operation is complete.  
---|---  
`HTTP Error 403: The service account does not have the required permissions for the bucket.` | Ensure that the bucket exists and the service account for the Cloud SQL instance (which is performing the export) has the `Storage Object Creator` role (`roles/storage.objectCreator`) to allow export to the bucket. See [IAM roles for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).  
CSV export worked but SQL export failed. | CSV and SQL formats do export differently. The SQL format exports the entire database, and likely takes longer to complete. The CSV format lets you define which elements of the database to include in the export. [Use CSV exports](https://docs.cloud.google.com/sql/docs/mysql/import-export/exporting#csv) to export only what you need.  
Export is taking too long. | Cloud SQL does not support concurrent synchronous operations. Use [ export offloading](https://docs.cloud.google.com/sql/docs/mysql/import-export#best_practices_for_importing_and_exporting). At a high level, in export offloading, instead of issuing an export on the source instance, Cloud SQL spins up an offload instance to perform the export. Export offloading has several advantages, including increased performance on the source instance and the unblocking of administrative operations while the export is running. With export offloading, total latency can increase by the amount of time it takes to bring up the offload instance. Generally, for reasonably sized exports, latency is not significant. However, if your export is small enough, then you may notice the increase in latency.  
You want exports to be automated. | Cloud SQL does not provide a way to automate exports. You could build your own automated export system using Google Cloud products such as Cloud Scheduler, Pub/Sub, and Cloud Run functions, similar to this article on [ automating backups](https://betterprogramming.pub/how-to-automate-google-cloud-sql-backups-2de6d3cc7d01).  
  
## What's next

  * [Learn how to import or export data using SQL dump files](https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-sql).
  * [Learn how to import and export data using CSV files](https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-csv).
  * [Learn how to enable automatic backups](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups).
  * [Learn how to restore from backups](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restore).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
