---
url: https://docs.cloud.google.com/sql/docs/mysql/known-issues/
title: Known issues \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:36.295497+00:00
---

# Known issues  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Known issues Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/known-issues "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/known-issues "View this page for the SQL Server database engine")

This page lists known issues with Cloud SQL for MySQL, along with ways you can avoid or recover from these issues.

If you are experiencing issues with your instance, make sure you also review the [Operational Guidelines](https://docs.cloud.google.com/sql/docs/mysql/operational-guidelines), as well as the information in [Diagnosing Issues](https://docs.cloud.google.com/sql/docs/mysql/diagnose-issues). 

### Data durability and availability issues

  * Generated columns (MySQL 5.7 instances only)

Due to an issue in MySQL, using generated columns might result in data corruption. For more information, see [MySQL bug #82736](https://bugs.mysql.com/bug.php?id=82736).




### Instance connection issues

  * Expired SSL/TLS certificates

If your instance is configured to use SSL, go to the [Cloud SQL Instances page](https://console.cloud.google.com/sql/instances) in the Google Cloud console and open the instance. Open its **Connections** page, select the **Security** tab and make sure that your server certificate is valid. If it has expired, you must add a new certificate and rotate to it. 

  * Cloud SQL Auth Proxy version

If you are connecting using the Cloud SQL Auth Proxy, make sure you are using the most recent version. For more information, see [Keeping the Cloud SQL Auth Proxy up to date](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy#keep-current).

  * Not authorized to connect

If you try to connect to an instance that does not exist in that project, the error message only says that you are not authorized to access that instance. 

  * Can't create a Cloud SQL instance

If you see the `Failed to create subnetwork. Router status is temporarily unavailable. Please try again later. Help Token: [token-ID]` error message, try to create the Cloud SQL instance again.




### Administrative issues

  * Only one long-running Cloud SQL import or export operation can run at a time on an instance. When you start an operation, make sure you don't need to perform other operations on the instance. Also, when you start the operation, you can [cancel it](https://docs.cloud.google.com/sql/docs/mysql/import-export/cancel-import-export).

  * MySQL auto-commits on each DDL statement. Cloud SQL persists all steps of the import up to cancelling the instance. Therefore, you might have to clean up the data on the instance manually.




### Issues with importing and exporting data

  * CSV export does not format NULLs and newlines correctly.

When you export data as CSV using the Cloud SQL export feature, NULLs are exported as `"N`, which can cause the CSV file to contain unbalanced quotation marks. Additionally, if your text data contains a newline character, a trailing quote mark is added at the end of the line.

When you import a file that you exported using the default escape character, the file treats the value as `"NULL"` instead of `NULL`. To override the default when you export the file, use `--escape="5C"`.

  * The SQL Mode setting affects how Cloud SQL interprets SQL queries.

For example, if you export from a database without Strict SQL enabled, then try to import to Cloud SQL (which enables Strict SQL by default), the import might fail. The best practice is to use the same SQL Mode on import that you used for export.

  * The DEFINER clause may cause import to fail

A DEFINER clause may cause an import operation to fail if the DEFINER user is a SUPER or system user and is different from the user doing the import into Cloud SQL. Learn more about [DEFINER usage](https://docs.cloud.google.com/sql/docs/mysql/import-export#definer-clause) and potential workarounds in Cloud SQL.

  * If you're trying to import and export data from a large database (for example, a database that has 500 GB of data or greater), then the import and export operations might take a long time to complete. In addition, other operations (for example, the backup operation) aren't available for you to perform while the import or export is occurring. A potential option to improve the performance of the import and export process is to [restore a previous backup](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restoring#projectid) using `gcloud` or the API.



  * Cloud Storage supports a [ maximum single-object size of up to five tebibytes (5 TiB)](https://docs.cloud.google.com/storage-transfer/docs/known-limitations-transfer#object-limit). Because Cloud SQL compresses data before uploading it to Cloud Storage, an export operation fails only if the _compressed_ size of an export file exceeds 5 TiB.

The compression ratio depends on the data types in the database; for example, text compresses better than binary data like [BLOBs](https://cloud.google.com/discover/what-is-binary-large-object-storage). Therefore, a database or table size greater than 5 TiB might not cause an export to fail if the data is highly compressible, while uncompressed data approaching 5 TiB might fail.

If you perform a standard export operation, then Cloud SQL typically creates a single export file. If you use parallel export, then Cloud SQL creates multiple export files. With this type of export, the export operation fails if any table is large enough that its compressed export file exceeds 5 TiB.

If your export fails due to the 5 TiB limit, then you need to break your export into smaller segments. If you're using a standard export and you encounter this limit, then consider switching to parallel export.




### Transaction logs and disk growth

Logs are purged once daily, not continuously. When the number of days of log retention is configured to be the same as the number of backups, a day of logging might be lost, depending on when the backup occurs. For example, setting log retention to seven days and backup retention to seven backups means that between six and seven days of logs will be retained.

We recommend setting the number of backups to at least one more than the days of log retention to guarantee a minimum of specified days of log retention.

### Issues with upgrading your MySQL instance

If you use Database Migration Service to [upgrade your MySQL instance](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-migrate) from version 5.7 to version 8.0, and you have stored procedures created in the database named `mysql` in your version 5.7 instance, then your stored procedures may not get copied to the `mysql` database in the upgraded version 8.0 instance. Also, you may not be able to create stored procedures in the `mysql` database in the upgraded instance.

### Issues with InnoDB page compression

[InnoDB page compression](https://dev.mysql.com/doc/refman/8.0/en/innodb-page-compression.html) can improve the performance of update queries by reducing the amount of data that needs to be read and written to disk. However, page compression can impact performance on the update queries on frequently updated tables. To evaluate the impact of page compression on your update queries, you can run a performance test with and without page compression. This helps you to observe how page compression affects the performance of your workload.

You can optimize page compression performance as follows:

  * Use a compression algorithm suitable for your data type. For example, use LZ4 for text data and ZLIB for binary data.

  * Avoid using compression for data that is frequently updated. Compressing and decompressing data can slow down your update queries.




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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
