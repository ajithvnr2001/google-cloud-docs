---
url: https://docs.cloud.google.com/sql/docs/postgres/known-issues/
title: Known issues \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:38.957957+00:00
---

# Known issues  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Known issues Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/known-issues "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/known-issues "View this page for the SQL Server database engine")

This page lists known issues with Cloud SQL for PostgreSQL, along with ways you can avoid or recover from these issues.

If you are experiencing issues with your instance, make sure you also review the information in [Diagnosing Issues](https://docs.cloud.google.com/sql/docs/postgres/diagnose-issues). 

### Instance connection issues

  * Expired SSL/TLS certificates

If your instance is configured to use SSL, go to the [Cloud SQL Instances page](https://console.cloud.google.com/sql/instances) in the Google Cloud console and open the instance. Open its **Connections** page, select the **Security** tab and make sure that your server certificate is valid. If it has expired, you must add a new certificate and rotate to it. 

  * Cloud SQL Auth Proxy version

If you are connecting using the Cloud SQL Auth Proxy, make sure you are using the most recent version. For more information, see [Keeping the Cloud SQL Auth Proxy up to date](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy#keep-current).

  * Not authorized to connect

If you try to connect to an instance that does not exist in that project, the error message only says that you are not authorized to access that instance. 

  * Can't create a Cloud SQL instance

If you see the `Failed to create subnetwork. Router status is temporarily unavailable. Please try again later. Help Token: [token-ID]` error message, try to create the Cloud SQL instance again.



  * The following only works with the default user ('postgres'): `gcloud sql connect --user`

If you try to connect using this command with any other user, the error message says FATAL: database 'user' does not exist. The workaround is to connect using the default user ('postgres'), then use the `"\c"` psql command to reconnect as the different user. 



  * PostgreSQL connections hang when IAM db proxy authentication is enabled.

When the [ Cloud SQL Auth Proxy is started using TCP sockets](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy#start-proxy) and with the `-enable_iam_login` flag, then a PostgreSQL client hangs during TCP connection. One workaround is to use `sslmode=disable` in the PostgreSQL connection string. For example:
        
        psql "host=127.0.0.1 dbname=postgres user=me@google.com sslmode=disable"

Another workaround is to [ start the Cloud SQL Auth Proxy using Unix sockets](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy#start-proxy). This turns off PostgreSQL SSL encryption and lets the Cloud SQL Auth Proxy do the SSL encryption instead. 




### Administrative issues

  * Only one long-running Cloud SQL import or export operation can run at a time on an instance. When you start an operation, make sure you don't need to perform other operations on the instance. Also, when you start the operation, you can [cancel it](https://docs.cloud.google.com/sql/docs/postgres/import-export/cancel-import-export).

PostgreSQL imports data in a single transaction. Therefore, if you cancel the import operation, then Cloud SQL doesn't persist data from the import. 




### Issues with importing and exporting data

  * If your Cloud SQL instance uses PostgreSQL 17, but your databases use PostgreSQL 16 and earlier, then you can't use Cloud SQL to import these databases into your instance. To do this, use [Database Migration Service](https://docs.cloud.google.com/database-migration/docs).

  * If you use Database Migration Service to import a PostgreSQL 17 database into Cloud SQL, then it's imported as a PostgreSQL 16 database.

  * For PostgreSQL versions 15 and later, if the target database is created from `template0`, then importing data might fail and you might see a `permission denied for schema public` error message. To resolve this issue, provide public schema privileges to the `cloudsqlsuperuser` user by running the `GRANT ALL ON SCHEMA public TO cloudsqlsuperuser` SQL command.

  * Exporting many large objects cause instance to become unresponsive

If your database contains many large objects (blobs), exporting the database can consume so much memory that the instance becomes unresponsive. This can happen even if the blobs are empty.

  * Cloud SQL doesn't support customized tablespaces but it does support data migration from customized tablespaces to the default tablespace, `pg_default`, in destination instance. For example, if you own a tablespace named `dbspace` is located at `/home/data`, after migration, all the data inside `dbspace` is migrated to the `pg_default`. But Cloud SQL will not create a tablespace named "dbspace" on its disk.

  * If you're trying to import and export data from a large database (for example, a database that has 500 GB of data or greater), then the import and export operations might take a long time to complete. In addition, other operations (for example, the backup operation) aren't available for you to perform while the import or export is occurring. A potential option to improve the performance of the import and export process is to [restore a previous backup](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restoring#projectid) using `gcloud` or the API.



  * Cloud Storage supports a [ maximum single-object size of up to five tebibytes (5 TiB)](https://docs.cloud.google.com/storage-transfer/docs/known-limitations-transfer#object-limit). Because Cloud SQL compresses data before uploading it to Cloud Storage, an export operation fails only if the _compressed_ size of an export file exceeds 5 TiB.

The compression ratio depends on the data types in the database; for example, text compresses better than binary data like [BLOBs](https://cloud.google.com/discover/what-is-binary-large-object-storage). Therefore, a database or table size greater than 5 TiB might not cause an export to fail if the data is highly compressible, while uncompressed data approaching 5 TiB might fail.

If you perform a standard export operation, then Cloud SQL typically creates a single export file. If you use parallel export, then Cloud SQL creates multiple export files, usually one for each table. With this type of export, the export operation fails if any table is large enough that its compressed export file exceeds 5 TiB.

If your export fails due to the 5 TiB limit, then you need to break your export into smaller segments. If you're using a standard export and you encounter this limit, then consider switching to parallel export.

If you're already using parallel export and you hit the 5 TiB limit, then one of your tables is too large to export, even by itself. In this case, as an alternative, you can connect from a Compute Engine instance and use the `pg_dump` utility to export the table.




### Transaction logs and disk growth

Logs are purged once daily, not continuously. When the number of days of log retention is configured to be the same as the number of backups, a day of logging might be lost, depending on when the backup occurs. For example, setting log retention to seven days and backup retention to seven backups means that between six and seven days of logs will be retained.

We recommend setting the number of backups to at least one more than the days of log retention to guarantee a minimum of specified days of log retention.

**Note:** Replica instances see a storage increase when replication is suspended and then resumed later. The increase is caused when the primary instance sends the replica the transaction logs for the period of time when replication was suspended. The transaction logs updates the replica to the current state of the primary instance.

### Issues related to Cloud Monitoring or Cloud Logging

Instances with the following region names are displayed incorrectly in certain contexts, as follows:

  * `us-central1` is displayed as `us-central`
  * `europe-west1` is displayed as `europe`
  * `asia-east1` is displayed as `asia`



This issue occurs in the following contexts:

  * Alerting in Cloud Monitoring
  * Metrics Explorer
  * Cloud Logging



You can mitigate the issue for Alerting in Cloud Monitoring, and for Metrics Explorer, by using [Resource metadata labels](https://docs.cloud.google.com/monitoring/api/v3/metric-model#meta-labels). Use the system metadata label `region` instead of the [cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database) monitored resource label `region`.

### Issue related to deleting a PostgreSQL database

When you delete a database created in Google Cloud console using your `psql` client, you may encounter the following error:
    
    
    ERROR: must be owner of database [DATABASE_NAME]
    

This is a permission error since the owner of a database created using a `psql` client doesn't have Cloud SQL `superuser` attributes. Databases created using the Google Cloud console are owned by `cloudsqlsuperuser` and databases created using a `psql` client are owned by users connected to that database. Since Cloud SQL is a managed service, customers cannot create or have access to users with `superuser` attributes. For more information, see [Superuser restrictions and privileges](https://docs.cloud.google.com/sql/docs/postgres/users#superuser-restrictions-and-privileges).

Due to this limitation, databases created using the Google Cloud console can only be deleted using the Google Cloud console, and databases created using a `psql` client can only be deleted by connecting as the owner of the database.

To find the owner of a database, use the following command:
    
    
    SELECT d.datname as Name,
    pg_catalog.pg_get_userbyid(d.datdba) as Owner
    FROM pg_catalog.pg_database d
    WHERE d.datname = 'DATABASE_NAME';
    

Replace the following:

  * DATABASE_NAME: the name of the database that you want to find owner information for.



If the owner of your database is `cloudsqlsuperuser`, then use Google Cloud console to delete your database. If the owner of the database is a `psql` client database user, then connect as the database owner and run the `DROP DATABASE` command.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
