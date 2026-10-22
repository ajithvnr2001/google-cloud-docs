---
url: https://docs.cloud.google.com/alloydb/docs/import-export-best-practices/
title: Best practices for importing and exporting data \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:55.244854+00:00
---

# Best practices for importing and exporting data  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/import-export-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Best practices for importing and exporting data Stay organized with collections  Save and categorize content based on your preferences. 

To optimize performance, reduce storage costs, and prevent operational disruptions when you move data into or out of AlloyDB for PostgreSQL, follow these best practices:

  * Don't use Cloud Storage [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays) buckets for imports or exports.
  * Use the correct flags when you create a SQL dump file.
  * Compress data to reduce cost.
  * Reduce long-running import and export processes by processing data in batches.
  * Verify the imported database after import.



### Don't use Cloud Storage Requester Pays buckets

You can't use a Cloud Storage bucket that has Requester Pays enabled for imports to or exports from AlloyDB. AlloyDB uses a Google-managed service account, Service Agent, to perform imports and exports. This agent generally doesn't have the context or configuration to charge the requester's project for data access, which causes operations that involve Requester Pays buckets to fail.

### Use the correct flags when you create a SQL dump file

If you don't use the correct flags and options when you export data to a SQL dump file, your import might be unsuccessful. For information about exporting data for import into AlloyDB, see [Export a DMP file](https://docs.cloud.google.com/alloydb/docs/export-dmp-file) and [Export a SQL file](https://docs.cloud.google.com/alloydb/docs/export-sql-file).

### Compress data to reduce cost

AlloyDB supports importing and exporting compressed `.gz` files from Cloud Storage. Compression can save significant storage space on Cloud Storage and reduce your storage costs, especially when you export large amounts of data. When you export a SQL dump or CSV file using the AlloyDB API, use a `.gz` file extension in the destination URI to compress the data. When you import a file with a `.gz` extension, the file decompresses automatically.

### Reduce long-running import and export processes

Depending on the size of your data, imports into and exports from AlloyDB can take a long time to complete. If an operation takes too long, it might block other operations.

Reduce the time to complete each operation by using smaller data batches. You can also use the `pg_dump` tool to perform a manual export from a client connected to a read pool instance.

### Verify the imported database

After an import operation completes, connect to your database using `psql` or another client, and run appropriate commands to make sure that the contents are correct, such as listing tables or querying row counts.

## Automate export operations

Although AlloyDB doesn't provide a built-in method for automating exports, you can build an automation tool using other Google Cloud components such as Cloud Scheduler, Pub/Sub, and Cloud Run functions.

## Troubleshooting

This section provides suggested fixes for issues that you might encounter with import and export operations.

### Import operations

Issue | Description | Recommended fix  
---|---|---  
`ERROR: permission denied for schema public` | For PostgreSQL 15 and later, importing data might fail due to schema permissions if you create the target database from `template0`. |  To resolve this, use the following command to grant privileges on the `public` schema to the user importing data:
    
    
            GRANT ALL ON SCHEMA public TO IMPORT_USER;
              
  
The import operation is taking too long. | Too many active connections can interfere with import operations. |  Try the following:

  * Close unused connections.
  * To ensure sufficient resources are available, check the CPU and memory usage of your instance.
  * To ensure maximum resources for the import, restart the instance before you begin the operation. This closes all connections and ends tasks that might consume resources.

  
An import operation fails because one or more users referenced in the dump file don't exist. | Before you import a dump file, all database users who own objects or received permissions on objects in the dumped database must exist in the target database. If they don't exist, the import operation fails to recreate the objects with the original ownership or permissions. | Create the required database users before importing.  
`GRANT stderr: ERROR: must be member of role ROLE_NAME` | This error can occur if you import a SQL dump file that contains objects owned by `ROLE_NAME`, or permissions granted to `ROLE_NAME`, but the database user performing the import isn't a member of `ROLE_NAME`. | To resolve this, ensure that the `ROLE_NAME` role exists in the destination database, and grant membership in `ROLE_NAME` to the user performing the import _before_ running the import.  
  
### Export operations

Issue | Description | Recommended fix  
---|---|---  
`HTTP Error 403: The service account does not have the required permissions for the bucket.` | The AlloyDB service account doesn't have the required permissions for the destination bucket. | Ensure that the destination Cloud Storage bucket exists and that the AlloyDB service account has the `roles/storage.objectAdmin` or `roles/storage.objectCreator` roles granted. These roles allow it to write to the bucket. See [Identity and Access Management (IAM) roles for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).   
CSV export worked, but SQL export failed. | CSV and SQL formats export differently. The SQL format exports database schema and data, and typically takes longer. The CSV format exports only the data resulting from a `SELECT` query that you provide. | If a SQL export fails or is too slow, consider exporting individual tables using CSV.  
Export is taking too long. | If an export takes too long on your primary instance, the export might be too large. | Consider exporting data in smaller batches. For example, export tables individually rather than exporting an entire database in one operation. You can also use the `pg_dump` tool to perform a manual export from a client connected to a read pool instance.   
`Create Extension` error in `pg_restore` log or import fails. | The dump file contains references to a PostgreSQL extension that AlloyDB doesn't support, or that isn't installed on your cluster. | To remove the references, edit the dump file or [install the extension](https://docs.cloud.google.com/alloydb/docs/instance-configure-extensions) on your cluster if AlloyDB supports it.   
Error using `pg_dumpall`. | The `pg_dumpall` utility with flags such as `--globals-only` might require privileges unavailable in AlloyDB. |  To export global objects such as users and roles without passwords, use the following command to include the `--no-role-passwords` flag:
    
    
            pg_dumpall --globals-only --no-role-passwords
              
  
The export operation times out or you see `Connection reset by peer`. | If Cloud Storage doesn't receive data within a certain timeframe, the connection can reset. This might happen if the initial database queries required for the export take too long to run. | If this occurs, try performing a manual export using the `pg_dump` tool from a client connected to a read pool instance.  
  
### Common issues

Issue | Description | Recommended fix  
---|---|---  
`HTTP Error 409: Operation failed because another operation was already in progress.` | The system allows only one API-based import or export operation at a time. | Try your request after the current operation completes.  
  
## What's next

  * [Import data using dump files](https://docs.cloud.google.com/alloydb/docs/import-dmp-file).
  * [Export data using dump files](https://docs.cloud.google.com/alloydb/docs/export-dmp-file).
  * [Import data using CSV files](https://docs.cloud.google.com/alloydb/docs/import-csv-file).
  * [Export data using CSV files](https://docs.cloud.google.com/alloydb/docs/export-csv-file).
  * [Import data using SQL files](https://docs.cloud.google.com/alloydb/docs/import-sql-file).
  * [Export data using SQL files](https://docs.cloud.google.com/alloydb/docs/export-sql-file).
  * [Enable automated backups](https://docs.cloud.google.com/alloydb/docs/backup/configure).
  * [Restore from a backup](https://docs.cloud.google.com/alloydb/docs/backup/restore).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
