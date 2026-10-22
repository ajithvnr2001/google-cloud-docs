---
url: https://docs.cloud.google.com/database-migration/docs/mysql/mysql-dump/
title: Exporting a MySQL database using mysqldump \u00a0|\u00a0 Database Migration Service for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:03.347281+00:00
---

# Exporting a MySQL database using mysqldump  |  Database Migration Service for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/mysql/mysql-dump/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview)



Send feedback 

#  Exporting a MySQL database using mysqldump Stay organized with collections  Save and categorize content based on your preferences. 

You can run the mysqldump utility directly against your MySQL database, using whatever options you require. However, if you're exporting to import the data into a Cloud SQL database, then use the mysqldump utility with the following flags:

  * `--databases` Specify an explicit list of databases to export. This list must _not_ contain the system databases (`sys`, `mysql`, `performance_schema`, and `information_schema`).
  * `--hex-blob` If your database contains any binary fields, then you must use this flag to ensure that your binary fields are imported correctly.
  * `--single-transaction` Starts a transaction before running. Rather than lock the entire database, this lets mysqldump read the database in the current state, making for a consistent data dump.
  * `--routines` To include stored procedures and functions. 
  * **When using`mysqldump` version 8 or later to export MySQL databases versions earlier than 8**:  
`--column-statistics=0`

This flag removes the [COLUMN_STATISTICS](https://dev.mysql.com/doc/refman/8.0/en/information-schema-column-statistics-table.html) table from the database export to avoid the `Unknown table 'COLUMN_STATISTICS' in information_schema (1109)` error. For more information, see [Diagnose issues](https://docs.cloud.google.com/database-migration/docs/mysql/diagnose-issues#unknown-table-column-statistics).




It's also recommended to use the following flags:

  * `--no-autocommit`
  * `--default-character-set=utf8mb4`
  * `--master-data`

**Important:** While [mysqldump](https://dev.mysql.com/doc/refman/5.7/en/mysqldump.html) is running, do not perform any [DDL operations](https://dev.mysql.com/doc/refman/5.7/en/glossary.html#glos_ddl) on the database. Doing so could cause inconsistencies in the export file.

From a machine with network connectivity to your MySQL server, run the following command:
    
    
        mysqldump \
            -h [SOURCE_ADDR] -P [SOURCE_PORT] -u [USERNAME] -p \
            --databases [DBS]  \
            --hex-blob \
            --no-autocommit \
            --default-character-set=utf8mb4 \
            --master-data=1  \
            --single-transaction \
            --routines \
            | gzip \
            | gcloud storage cp - gs://[BUCKET_NAME]/[DUMP_FILENAME].gz
    

**Note:** If your source database server doesn't support GTID, then use the `--master-data=1` property; otherwise, don't use this property. Also, if your source database server supports GTID, then use the `--set-gtid-purged=on` property; otherwise, don't use this property.

If the source of the migration is a Relational Database Service (RDS) for MySQL:

  * The `master-data` property isn't supported.
  * If your source database server supports GTID, then use the `--set-gtid-purged=on` property; otherwise, don't use this property.
  * If you're using a manual dump to migrate your data, then perform the migration with GTID enabled.



This command might look like the following example:
    
    
        mysqldump \
            -h [SOURCE_ADDR] -P [SOURCE_PORT] -u [USERNAME] -p \
            --databases [DBS]  \
            --hex-blob  \
            --no-autocommit \
            --default-character-set=utf8mb4 \
            --set-gtid-purged=on \
            --single-transaction \
            --routines \ 
            | gzip \
            | gcloud storage cp - gs://[BUCKET_NAME]/[DUMP_FILENAME].gz
    

Also, you should configure RDS instances to retain binlogs longer. This command might look like the following example:
    
    
        # Sets the retention period to one week.
        call mysql.rds_set_configuration('binlog retention hours', 168);
    

Replace [PROPERTIES_IN_BRACKETS] with the following values:

Property | Value  
---|---  
[SOURCE_ADDR] | The IPv4 address or hostname for the source database server.  
[SOURCE_PORT] | The port for the source database server.  
[USERNAME] | The MySQL user account.  
[DBS] | A space-separated list of the databases on the source database server to include in the dump. Use the `SHOW DATABASES` MySQL command to list your databases.  
[BUCKET_NAME] | The bucket in Cloud Storage that's created by the user and that's used for storing the dump file (for example, `replica-bucket`).  
[DUMP_FILENAME] | The dump's filename, ending with a `.gz` file extension (for example, `source-database.sql.gz`).  
**Note:** The `gzip` command causes the dump file to be compressed. If your database contains data that does not compress well, such as binary incompressible data or JPG images, then remove `| gzip` from the command.

## What's next

To get a complete, step-by-step migration walkthrough, see [ Get started with Cloud SQL for MySQL migrations](https://docs.cloud.google.com/database-migration/docs/mysql/get-started-with-mysql-migrations).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
