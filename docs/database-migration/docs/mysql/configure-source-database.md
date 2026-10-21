---
url: https://docs.cloud.google.com/database-migration/docs/mysql/configure-source-database/
title: Configure your source MySQL database for one-time migrations \u00a0|\u00a0 Database Migration Service for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:19:14.967022+00:00
---

# Configure your source MySQL database for one-time migrations  |  Database Migration Service for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/mysql/configure-source-database/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview)



Send feedback 

#  Configure your source MySQL database for one-time migrations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure the following source database instances for one-time homogeneous MySQL migrations:

  * Cloud SQL for MySQL
  * Self-hosted MySQL
  * Amazon RDS for MySQL
  * Amazon Aurora for MySQL
  * Microsoft Azure Database for MySQL



## Configure a Cloud SQL for MySQL source

To configure a Cloud SQL for MySQL source instance for your migration process, do the following:

  1. Check if your source database contains metadata defined by users with the `DEFINER` clause. See [ Verify metadata with a `DEFINER` clause](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer). 

Database Migration Service for homogeneous MySQL migrations doesn't migrate user accounts and logins. Sources that contain metadata defined by user accounts with the `DEFINER` clause might block your migration. 

  2. If your source database contains objects that reference tables in the `mysql`, `performance_schema`, `information_schema`, `ndbinfo`, or `sys` system schemas, ensure that the replica databases also contain these system schema tables. 

If the replica databases don't have these tables, your migration job might fail with the [ `Unknown table in system schema `](https://docs.cloud.google.com/database-migration/docs/mysql/diagnose-issues#unknown-table-in-system-schema). 

  3. Create a dedicated migration user account in your instance. See [ Create a user](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users) in the Cloud SQL documentation. Make sure that: 

     * You allow the dedicated user account to connect from any host (`host=%`). 
     * The password for the account doesn't exceed 32 characters in length. For more information about the MySQL user password length limitations, see [MySQL Bug #43439](https://bugs.mysql.com/bug.php?id=43439). 
  4. Assign the necessary privileges to the dedicated migration user account. For one-time migrations, the full list of required privileges depends on whether you provide your own dump files or use Database Migration Service managed dump feature: 

### Managed dump

If you want Database Migration Service to automatically take the full dump of your source database, assign the following privileges to the user account: 

     * `[SELECT](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_select)`
     * `[SHOW VIEW](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_show-view)`
     * `[TRIGGER](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_trigger)`
     * `[RELOAD](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_reload)`
     * _For source MySQL versions 8.0 or later:_ Make sure the migration account doesn't have the `BACKUP_ADMIN` privilege. 

### Manual dump

If you provide your own [ dump files created with `mysqldump`](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-dump), you don't need to assign any extra privileges to the user account.




## Configure a self-hosted MySQL source

To configure a self-hosted MySQL source instance for your migration process, do the following:

  1. Ensure that all your tables (except tables in system databases) use the [ InnoDB storage engine](https://dev.mysql.com/doc/refman/5.7/en/innodb-storage-engine.html). If you use a different storage engine, you might need to convert your tables. For more information, see [ Converting Tables from MyISAM to InnoDB](https://dev.mysql.com/doc/refman/5.7/en/converting-tables-to-innodb.html). 
  2. Check if your source database contains metadata defined by users with the `DEFINER` clause. See [ Verify metadata with a `DEFINER` clause](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer). 

Database Migration Service for homogeneous MySQL migrations doesn't migrate user accounts and logins. Sources that contain metadata defined by user accounts with the `DEFINER` clause might block your migration. 

  3. If your source database contains objects that reference tables in the `mysql`, `performance_schema`, `information_schema`, `ndbinfo`, or `sys` system schemas, ensure that the replica databases also contain these system schema tables. 

If the replica databases don't have these tables, your migration job might fail with the [ `Unknown table in system schema `](https://docs.cloud.google.com/database-migration/docs/mysql/diagnose-issues#unknown-table-in-system-schema). 

  4. Make sure that `GTID_MODE` is set to `ON` or `OFF`, no other value is supported. 

Database Migration Service requires `GTID_MODE` set to `ON` in the following scenarios: 

     * When you [ migrate to an existing destination instance](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job-existing-instance) that has [read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication#read-replicas) enabled. 
     * If you plan to manually create the dump files and provide them in the migration job. 

For more information about `GTID_MODE`, see [ Global Transaction ID System Variable](https://dev.mysql.com/doc/refman/5.7/en/replication-options-gtids.html#sysvar_gtid_mode). 

  5. Create a dedicated migration user account in your instance. See [ Account management statements](https://dev.mysql.com/doc/refman/5.7/en/account-management-statements.html). Make sure that: 

     * You allow the dedicated user account to connect from any host (`host=%`). 
     * The password for the account doesn't exceed 32 characters in length. For more information about the MySQL user password length limitations, see [MySQL Bug #43439](https://bugs.mysql.com/bug.php?id=43439). 
  6. Assign the necessary privileges to the dedicated migration user account. For one-time migrations, the full list of required privileges depends on whether you provide your own dump files or use Database Migration Service managed dump feature: 

### Managed dump

If you want Database Migration Service to automatically take the full dump of your source database, assign the following privileges to the user account: 

     * `[SELECT](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_select)`
     * `[SHOW VIEW](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_show-view)`
     * `[TRIGGER](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_trigger)`
     * _For sources with`GTID_MODE = ON` setting_: `[RELOAD](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_reload)`

With the managed dump flow, Database Migration Service requires the `GTID_MODE = ON` setting only when you [ migrate to an existing destination instance](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job-existing-instance) that has [read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication#read-replicas) enabled. 

     * _For source MySQL versions 8.0 or later:_ Make sure the migration account doesn't have the `BACKUP_ADMIN` privilege. 

### Manual dump

If you provide your own [ dump files created with `mysqldump`](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-dump), you don't need to assign any extra privileges to the user account.




## Configure an Amazon RDS for MySQL source

To configure an Amazon RDS for MySQL source instance for your migration process, do the following:

  1. Amazon RDS for MySQL uses [ InnoDB storage engine](https://dev.mysql.com/doc/refman/5.7/en/innodb-storage-engine.html) by default, but allows using other storage engines. Ensure that all your tables (except tables in system databases) use the InnoDB storage engine. If you use a different storage engine, you might need to convert your tables. For more information, see [ Converting Tables from MyISAM to InnoDB](https://dev.mysql.com/doc/refman/5.7/en/converting-tables-to-innodb.html). 
  2. Check if your source database contains metadata defined by users with the `DEFINER` clause. See [ Verify metadata with a `DEFINER` clause](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer). 

Database Migration Service for homogeneous MySQL migrations doesn't migrate user accounts and logins. Sources that contain metadata defined by user accounts with the `DEFINER` clause might block your migration. 

  3. If your source database contains objects that reference tables in the `mysql`, `performance_schema`, `information_schema`, `ndbinfo`, or `sys` system schemas, ensure that the replica databases also contain these system schema tables. 

If the replica databases don't have these tables, your migration job might fail with the [ `Unknown table in system schema `](https://docs.cloud.google.com/database-migration/docs/mysql/diagnose-issues#unknown-table-in-system-schema). 

  4. Make sure that `GTID_MODE` is set to `ON` or `OFF`, no other value is supported. Amazon RDS for MySQL uses `GTID_MODE = OFF` by default. 

Database Migration Service requires `GTID_MODE` set to `ON` in the following scenarios: 

     * When you [ migrate to an existing destination instance](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job-existing-instance) that has [read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication#read-replicas) enabled. 
     * If you plan to manually create the dump files and provide them in the migration job. 

For more information about `GTID_MODE`, see [ Global Transaction ID System Variable](https://dev.mysql.com/doc/refman/5.7/en/replication-options-gtids.html#sysvar_gtid_mode). 

  5. Create a dedicated migration user account in your instance. See [ Account management statements](https://dev.mysql.com/doc/refman/5.7/en/account-management-statements.html). Make sure that: 

     * You allow the dedicated user account to connect from any host (`host=%`). 
     * The password for the account doesn't exceed 32 characters in length. For more information about the MySQL user password length limitations, see [MySQL Bug #43439](https://bugs.mysql.com/bug.php?id=43439). 
  6. Assign the necessary privileges to the dedicated migration user account. For one-time migrations, the full list of required privileges depends on whether you provide your own dump files or use Database Migration Service managed dump feature: 

### Managed dump

If you want Database Migration Service to automatically take the full dump of your source database, assign the following privileges to the user account: 

     * `[SELECT](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_select)`
     * `[SHOW VIEW](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_show-view)`
     * `[TRIGGER](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_trigger)`
     * `[LOCK TABLES](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_lock-tables)`
     * _For sources with`GTID_MODE = ON` setting_: `[RELOAD](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_reload)`

With the managed dump flow, Database Migration Service requires the `GTID_MODE = ON` setting only when you [ migrate to an existing destination instance](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job-existing-instance) that has [read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication#read-replicas) enabled. 

     * _For source MySQL versions 8.0 or later:_ Make sure the migration account doesn't have the `BACKUP_ADMIN` privilege. 

### Manual dump

If you provide your own [ dump files created with `mysqldump`](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-dump), you don't need to assign any extra privileges to the user account.




## Configure an Amazon Aurora for MySQL source

To configure an Amazon Aurora for MySQL source instance for your migration process, do the following:

  1. Check if your source database contains metadata defined by users with the `DEFINER` clause. See [ Verify metadata with a `DEFINER` clause](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer). 

Database Migration Service for homogeneous MySQL migrations doesn't migrate user accounts and logins. Sources that contain metadata defined by user accounts with the `DEFINER` clause might block your migration. 

  2. If your source database contains objects that reference tables in the `mysql`, `performance_schema`, `information_schema`, `ndbinfo`, or `sys` system schemas, ensure that the replica databases also contain these system schema tables. 

If the replica databases don't have these tables, your migration job might fail with the [ `Unknown table in system schema `](https://docs.cloud.google.com/database-migration/docs/mysql/diagnose-issues#unknown-table-in-system-schema). 

  3. Make sure that `GTID_MODE` is set to `ON` or `OFF`, no other value is supported. Amazon Aurora for MySQL uses `GTID_MODE = OFF` by default. 

Database Migration Service requires `GTID_MODE` set to `ON` in the following scenarios: 

     * When you [ migrate to an existing destination instance](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job-existing-instance) that has [read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication#read-replicas) enabled. 
     * If you plan to manually create the dump files and provide them in the migration job. 

For more information about `GTID_MODE`, see [ Global Transaction ID System Variable](https://dev.mysql.com/doc/refman/5.7/en/replication-options-gtids.html#sysvar_gtid_mode). 

  4. Create a dedicated migration user account in your instance. See [ Account management statements](https://dev.mysql.com/doc/refman/5.7/en/account-management-statements.html). Make sure that: 

     * You allow the dedicated user account to connect from any host (`host=%`). 
     * The password for the account doesn't exceed 32 characters in length. For more information about the MySQL user password length limitations, see [MySQL Bug #43439](https://bugs.mysql.com/bug.php?id=43439). 
  5. Assign the necessary privileges to the dedicated migration user account. For one-time migrations, the full list of required privileges depends on whether you provide your own dump files or use Database Migration Service managed dump feature: 

### Managed dump

If you want Database Migration Service to automatically take the full dump of your source database, assign the following privileges to the user account: 

     * `[SELECT](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_select)`
     * `[SHOW VIEW](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_show-view)`
     * `[TRIGGER](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_trigger)`
     * `[LOCK TABLES](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_lock-tables)`
     * _For sources with`GTID_MODE = ON` setting_: `[RELOAD](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_reload)`

With the managed dump flow, Database Migration Service requires the `GTID_MODE = ON` setting only when you [ migrate to an existing destination instance](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job-existing-instance) that has [read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication#read-replicas) enabled. 

     * _For source MySQL versions 8.0 or later:_ Make sure the migration account doesn't have the `BACKUP_ADMIN` privilege. 

### Manual dump

If you provide your own [ dump files created with `mysqldump`](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-dump), you don't need to assign any extra privileges to the user account.




## Configure a Microsoft Azure Database for MySQL source

To configure a Microsoft Azure Database for MySQL source instance for your migration process, do the following:

  1. Check if your source database contains metadata defined by users with the `DEFINER` clause. See [ Verify metadata with a `DEFINER` clause](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer). 

Database Migration Service for homogeneous MySQL migrations doesn't migrate user accounts and logins. Sources that contain metadata defined by user accounts with the `DEFINER` clause might block your migration. 

  2. If your source database contains objects that reference tables in the `mysql`, `performance_schema`, `information_schema`, `ndbinfo`, or `sys` system schemas, ensure that the replica databases also contain these system schema tables. 

If the replica databases don't have these tables, your migration job might fail with the [ `Unknown table in system schema `](https://docs.cloud.google.com/database-migration/docs/mysql/diagnose-issues#unknown-table-in-system-schema). 

  3. Make sure that `GTID_MODE` is set to `ON` or `OFF`, no other value is supported. Microsoft Azure Database for MySQL uses `GTID_MODE = OFF` by default. 

Database Migration Service requires `GTID_MODE` set to `ON` in the following scenarios: 

     * When you [ migrate to an existing destination instance](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job-existing-instance) that has [read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication#read-replicas) enabled. 
     * If you plan to manually create the dump files and provide them in the migration job. 

For more information about `GTID_MODE`, see [ Global Transaction ID System Variable](https://dev.mysql.com/doc/refman/5.7/en/replication-options-gtids.html#sysvar_gtid_mode). 

  4. Check the value of your **`require_secure_transport`** setting.

By default, Microsoft Azure databases require [SSL/TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) encryption for all incoming connections. Depending on the `require_secure_transport` value, use one of the following encryption settings when you [create the source connection profile](https://docs.cloud.google.com/database-migration/docs/mysql/create-connection-profiles):

     * If `require_secure_transport` is set to `on`, select **Basic** , **TLS** , or **mTLS**.
     * If `require_secure_transport` is set to `off`, select **None**.
  5. Create a dedicated migration user account in your instance. See [ Account management statements](https://dev.mysql.com/doc/refman/5.7/en/account-management-statements.html). Make sure that: 

     * You allow the dedicated user account to connect from any host (`host=%`). 
     * The password for the account doesn't exceed 32 characters in length. For more information about the MySQL user password length limitations, see [MySQL Bug #43439](https://bugs.mysql.com/bug.php?id=43439). 
  6. Assign the necessary privileges to the dedicated migration user account. For one-time migrations, the full list of required privileges depends on whether you provide your own dump files or use Database Migration Service managed dump feature: 

### Managed dump

If you want Database Migration Service to automatically take the full dump of your source database, assign the following privileges to the user account: 

     * `[SELECT](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_select)`
     * `[SHOW VIEW](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_show-view)`
     * `[TRIGGER](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_trigger)`
     * _For sources with`GTID_MODE = ON` setting_: `[RELOAD](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_reload)`

With the managed dump flow, Database Migration Service requires the `GTID_MODE = ON` setting only when you [ migrate to an existing destination instance](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job-existing-instance) that has [read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication#read-replicas) enabled. 

     * _For source MySQL versions 8.0 or later:_ Make sure the migration account doesn't have the `BACKUP_ADMIN` privilege. 

### Manual dump

If you provide your own [ dump files created with `mysqldump`](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-dump), you don't need to assign any extra privileges to the user account.




## What's next

To get a complete, step-by-step migration walkthrough for homogeneous Cloud SQL for MySQL migrations, see [ Get started with Cloud SQL for MySQL migrations](https://docs.cloud.google.com/database-migration/docs/mysql/get-started-with-mysql-migrations).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
