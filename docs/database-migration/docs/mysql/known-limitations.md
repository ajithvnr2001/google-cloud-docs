---
url: https://docs.cloud.google.com/database-migration/docs/mysql/known-limitations/
title: Known limitations \u00a0|\u00a0 Database Migration Service for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:03:02.664536+00:00
---

# Known limitations  |  Database Migration Service for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/mysql/known-limitations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview)



Send feedback 

#  Known limitations Stay organized with collections  Save and categorize content based on your preferences. 

Before you choose to migrate your databases to Cloud SQL, consider known limitations for this migration scenario.

**Note:** You can also use Google Cloud Migration Center to discover gaps in feature support. See [ Discover and import databases](https://docs.cloud.google.com/migration-center/docs/discover-and-import-databases) in the Migration Center documentation. 

Known limitations for using a MySQL database as a source include:

  * To migrate encrypted databases you need to provide the encryption keys to Database Migration Service. Database Migration Service supports migrating data from encrypted Amazon Aurora or Amazon RDS databases because these databases handle decryption transparently in their services. For more information, see [ Encrypting Amazon Aurora resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html), [ Encrypting Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html), and [ Configure customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/sql/docs/mysql/configure-cmek).

  * Migrating to MySQL 5.6, MySQL 8.4, or MySQL 9.7 with a Percona XtraBackup physical backup file is not supported.

  * _For MySQL 8.0 to MySQL 8.4 and MySQL 8.4 to MySQL 9.7 migrations_ :

    * Your destination database must have the `local_infile` flag set to `ON`.
    * The dedicated migration account on the source instance can't have the [ `BACKUP_ADMIN`](https://dev.mysql.com/doc/refman/9.1/en/privileges-provided.html#priv_backup-admin) privilege.

These considerations are also covered in the relevant sections, such as the [Configure source database](https://docs.cloud.google.com/database-migration/docs/mysql/configure-source-database) page.

  * When you migrate across major MySQL versions (for example, from MySQL 8.0 to MySQL 8.4) you need to address possible incompatibilities to ensure a smooth migration without data consistency issues.

When you prepare for a cross-version migration, review the [features supported by Cloud SQL for MySQL](https://docs.cloud.google.com/sql/docs/mysql/db-versions) as well as the release notes for your target major version to determine what incompatibilities you need to address.

    * [MySQL 9.7](https://dev.mysql.com/doc/refman/9.7/en/upgrading-from-previous-series.html)
    * [MySQL 8.4](https://dev.mysql.com/doc/refman/8.4/en/upgrading-from-previous-series.html)
    * [MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/upgrading-from-previous-series.html)
    * [MySQL 5.7](https://dev.mysql.com/doc/refman/5.7/en/upgrading-from-previous-series.html)
  * During the full data dump phase, you can't perform any data definition language (DDL) operations (such as `ALTER TABLE`, `DROP TABLE`, `TRUNCATE TABLE`) on your source database. Running these operations during the full dump phase might lead to a metadata deadlock, causing the migration process to fail (with the `Table definition has changed` error) or stop responding (and report timeout errors such as `ERROR: While 'Loading data': Dump timeout` or `MySQL Error 2013 (HY000): Lost connection to MySQL server during query`). You can perform DDL changes on your source database during the CDC phase. For more information, see the following entries in the troubleshooting section:

    * [ `Table definition has changed`](https://docs.cloud.google.com/database-migration/docs/mysql/diagnose-issues#table-definition-changed)
    * [ `While 'Loading data': dump timeout`](https://docs.cloud.google.com/database-migration/docs/mysql/diagnose-issues#dump-timeout)
    * [ `MySQL Error 2013: Lost connection to MySQL server during query`](https://docs.cloud.google.com/database-migration/docs/mysql/diagnose-issues#mysql-error-2013)
    * [ `Timeout waiting for no write traffic on the source: context deadline exceeded`](https://docs.cloud.google.com/database-migration/docs/mysql/diagnose-issues#context-deadline-exceeded)
  * If the source is Amazon RDS MySQL, Amazon Aurora MySQL, or a source that doesn't grant SUPERUSER privileges, then additional steps are required for successful migration, including a brief write downtime on the source. For more information, see the [Configure source database for Amazon RDS](https://docs.cloud.google.com/database-migration/docs/mysql/configure-source-database#aws-rds-mysql) and [Amazon Aurora-specific](https://docs.cloud.google.com/database-migration/docs/mysql/configure-source-database#aws-aurora-mysql) sections.

  * Database Migration Service can't migrate data from an [Amazon Aurora read replica instance](https://repost.aws/questions/QUQuQ2eje6TnatP_lAtdydhg/can-we-configure-separate-binary-logging-binlog-on-aurora-my-sq-ls-read-replica-instance) or an Oracle Cloud Infrastructure (OCI) MySQL read replica instance because binary log files can't be retrieved from the instance. For more information about Amazon Aurora, see the [Amazon Aurora-specific section](https://docs.cloud.google.com/database-migration/docs/mysql/configure-source-database#aws-aurora-mysql).

  * When migrating from a self-managed MySQL read replica, GTID isn't supported. You must use binary log file and position-based replication. For more information, see [ Migration types and phases](https://docs.cloud.google.com/database-migration/docs/mysql/migration-types).

  * The MySQL system database isn't migrated as part of the server migration, so information about user accounts, logins, and roles isn't included.

  * While you can select specific databases to migrate, you can't filter or select individual database objects within a database (such as specific tables, views, or stored procedures) when you migrate by using Database Migration Service. All InnoDB tables and objects from each selected database are migrated, excluding the following system schemas: `mysql`, `performance_schema`, `information_schema`, and `sys`. Before you begin the migration, make sure that your source database doesn't contain objects that reference tables in these schemas. Otherwise, your migration can fail with the `ERROR 1109 (42S02): Unknown table in _< schema name here>_` message. See [Configure your source database](https://docs.cloud.google.com/database-migration/docs/mysql/configure-source-database) and [Diagnose issues](https://docs.cloud.google.com/database-migration/docs/mysql/diagnose-issues#unknown-table-in-system-schema).

  * During migration, the destination Cloud SQL database is in read-only mode, to prevent modification of the database which might break the migration process or data integrity. After the destination is promoted, it becomes writable.

  * Database Migration Service isn't compatible with MariaDB.

  * You must [set the binary log format](https://dev.mysql.com/doc/refman/8.0/en/binary-log-setting.html) to `ROW`. Configuring the binary log to any other format, such as `STATEMENT` or `MIXED`, might cause the replication to fail. For example, using the `LOAD DATA IN FILE` statement.

Learn more about this limitation for the [`STATEMENT`](https://dev.mysql.com/doc/refman/8.0/en/replication-sbr-rbr.html#replication-sbr-rbr-sbr-disadvantages) or [`MIXED`](https://dev.mysql.com/doc/refman/8.0/en/binary-log-mixed.html) formats.

  * If you create a continuous migration job using your own dump file, then don't use the `mysqldump` utility from MySQL version 5.7.36. For more information, see [bug #105761](https://bugs.mysql.com/bug.php?id=105761) in the MySQL documentation.

  * InnoDB is the only supported storage engine for Cloud SQL. Migrating with MyISAM might cause data inconsistency and requires data validation. For help with converting tables from MyISAM to InnoDB, see the [MySQL documentation](https://dev.mysql.com/doc/refman/5.7/en/converting-tables-to-innodb.html).

  * [ Private Service Connect interfaces connectivity method](https://docs.cloud.google.com/database-migration/docs/mysql/networking-methods#psc-interfaces) is only supported for migrating to existing destination instances. If you want to use private IP connectivity and migrate to a new destination instance, use VPC peering.




### Data dump parallelism considerations

Data dump parallelism lets you migrate from MySQL databases using a high-performance dump mechanism, significantly improving the migration speed. When using data dump parallelism, consider the following:

  * Data dump parallelism is available only when migrating to MySQL versions 5.7, 8.0, 8.4, or 9.7.

  * At the beginning of the data dump, Database Migration Service briefly locks your source database making it temporarily unavailable for writes. The lock duration depends on the number of tables in the source database:

Number of tables | Approximate lock time  
---|---  
100 | 1 second  
10K | 9 seconds  
50K | 49 seconds  

**Note:** For scenarios where it isn't possible to lock your source database, use a read replica as the source database instead. For information on migrating from read replicas in Amazon RDS, see [Migrating from RDS MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/configure-source-database#aws-rds-mysql).

### Limitations for migrations to existing destination instances

  * Your existing destination instance can only contain default system databases that are set up automatically when you create the destination instance. Migrating to existing destination instances that contain user data (such as tables in system schemas, or databases) isn't supported. 

If you encounter issues due to extra data in your existing destination instance, clear the databases in your destination instance and re-try the migration job. See [ Clear extra data from your existing destination instance](https://docs.cloud.google.com/database-migration/docs/mysql/diagnose-issues#clear-ext-instance-data-steps).

  * You can configure only one migration job per destination instance.
  * You can only migrate to standalone Cloud SQL instances. Migrating to [external server replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-external-replica) isn't supported.
  * Migrating to a Cloud SQL instance that has a [read replica](https://docs.cloud.google.com/sql/docs/mysql/replication#read-replicas) requires that your source instance has global transaction ID (GTID) logging enabled.
  * You can't use Cloud SQL for MySQL read replicas as the migration destination instance. 
  * **For Terraform users** : Database Migration Service modifies the backup and recovery settings of your destination instance. This might cause the destination instance settings to be different from the Terraform configuration you used for provisioning. If you experience this issue, follow the guidance in [Diagnose issues](https://docs.cloud.google.com/database-migration/docs/mysql/diagnose-issues#existing-instance-terraform-config-drift). 



### Quotas

  * Up to 2,000 connection profiles and 1,000 migration jobs can exist at any given time. To create space for more, migration jobs (including completed ones) and connection profiles can be deleted.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
