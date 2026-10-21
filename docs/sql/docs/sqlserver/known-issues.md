---
url: https://docs.cloud.google.com/sql/docs/sqlserver/known-issues/
title: Known issues \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:17.510374+00:00
---

# Known issues  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Known issues Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/known-issues "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/known-issues "View this page for the PostgreSQL database engine") | SQL Server

This page lists known issues with Cloud SQL for SQL Server, along with ways you can avoid or recover from these issues.

### Instance connection issues

  * Expired SSL/TLS certificates

If your instance is configured to use SSL, go to the [Cloud SQL Instances page](https://console.cloud.google.com/sql/instances) in the Google Cloud console and open the instance. Open its **Connections** page, select the **Security** tab and make sure that your server certificate is valid. If it has expired, you must add a new certificate and rotate to it. 

  * Cloud SQL Auth Proxy version

If you are connecting using the Cloud SQL Auth Proxy, make sure you are using the most recent version. For more information, see [Keeping the Cloud SQL Auth Proxy up to date](https://docs.cloud.google.com/sql/docs/sqlserver/sql-proxy#keep-current).

  * Not authorized to connect

If you try to connect to an instance that does not exist in that project, the error message only says that you are not authorized to access that instance. 

  * Can't create a Cloud SQL instance

If you see the `Failed to create subnetwork. Router status is temporarily unavailable. Please try again later. Help Token: [token-ID]` error message, try to create the Cloud SQL instance again.




### Administrative issues

  * A large export operation can adversely affect instance availability

Before starting a large export, ensure that at least 25 percent of the database size is free (on the instance). Doing so helps prevent issues with aggressive autogrowth, which can affect the availability of the instance.

    * If your SQL Server instance uses a SQL Server Express edition:

      * If you specify a flag when you create a new instance, then creating the instance fails.

      * You can't set database flags on an existing instance.

    * Long-running Cloud SQL import and export instance operations can't be cancelled or stopped

Only one operation can run at a time on a Cloud SQL instance. Make sure you don't need to perform other operations on an instance when you start a long-running operation.

When you start a long-running Cloud SQL instance operation, such as an import or export operation, there's no way to cancel the operation without [restarting](https://docs.cloud.google.com/sql/docs/sqlserver/start-stop-restart-instance#restart) the instance.

    * If you cancel an import from a BAK file, then the database that you're importing is left in a partial state. You must drop the database. If you cancel an import from a SQL file, then you must clean up partial data manually.




### Issues with importing and exporting data

  * Do not create a BAK file (for import) from a read-only database or from a database that is in single-user mode. If you create a BAK file from a read-only database or from a database that is in single-user mode, and import that file, an error may occur.

  * If you're trying to import and export data from a large database (for example, a database that has 500 GB of data or greater), then the import and export operations might take a long time to complete. In addition, other operations (for example, the backup operation) aren't available for you to perform while the import or export is occurring. A potential option to improve the performance of the import and export process is to [restore a previous backup](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/restoring#projectid) using `gcloud` or the API.

  * Cloud SQL supports bulk insert only on SQL Server 2022.

  * Cloud SQL only supports the `RAW` [codepage](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver16).

  * Cloud SQL doesn't support bulk insert on read replicas.

  * Cloud SQL supports bulk insert only for importing data to tables.



  * Cloud Storage supports a [ maximum single-object size of up to five tebibytes (5 TiB)](https://docs.cloud.google.com/storage-transfer/docs/known-limitations-transfer#object-limit). Because Cloud SQL compresses data before uploading it to Cloud Storage, an export operation fails only if the _compressed_ size of an export file exceeds 5 TiB.

The compression ratio depends on the data types in the database; for example, text compresses better than binary data like [BLOBs](https://cloud.google.com/discover/what-is-binary-large-object-storage). Therefore, a database or table size greater than 5 TiB might not cause an export to fail if the data is highly compressible, while uncompressed data approaching 5 TiB might fail.

If you perform a standard export operation, then Cloud SQL typically creates a single export file. If you use striped export, then Cloud SQL creates multiple export files. With this type of export, the export operation fails if any table is large enough that its compressed export file exceeds 5 TiB.

If your export fails due to the 5 TiB limit, then you need to break your export into smaller segments. If you're using a standard export and you encounter this limit, then consider switching to striped export.




### Transaction logs and disk growth

Logs are purged once daily, not continuously. When the number of days of log retention is configured to be the same as the number of backups, a day of logging might be lost, depending on when the backup occurs. For example, setting log retention to seven days and backup retention to seven backups means that between six and seven days of logs will be retained.

We recommend setting the number of backups to at least one more than the days of log retention to guarantee a minimum of specified days of log retention.

### Issues related to Cloud Monitoring or Cloud Logging

Instances with the following region names are displayed incorrectly in certain contexts, as follows:

  * `us-central1` is displayed as `us-central`
  * `europe-west1` is displayed as `europe`
  * `asia-east1` is displayed as `asia`



This issue occurs in the following contexts:

  * Alerting in Cloud Monitoring
  * Metrics Explorer
  * Cloud Logging



You can mitigate the issue for Alerting in Cloud Monitoring, and for Metrics Explorer, by using [Resource metadata labels](https://cloud.google.com/monitoring/api/v3/metric-model#meta-labels). Use the system metadata label `region` instead of the [cloudsql_database](https://cloud.google.com/monitoring/api/resources#tag_cloudsql_database) monitored resource label `region`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
