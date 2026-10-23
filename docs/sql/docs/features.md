---
url: https://docs.cloud.google.com/sql/docs/features/
title: Cloud SQL features \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:53.985420+00:00
---

# Cloud SQL features  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/features/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/introduction)



Send feedback 

#  Cloud SQL features Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the major features and capabilities of Cloud SQL. **Note:** For information about the supported versions of database engines, see [Database versions and version policies](https://docs.cloud.google.com/sql/docs/mysql/db-versions).

## MySQL features by Cloud SQL editions

For more information about the features for the Cloud SQL Enterprise Plus edition and Cloud SQL Enterprise edition of Cloud SQL for MySQL, see [Introduction to Cloud SQL editions](https://docs.cloud.google.com/sql/docs/mysql/editions-intro).

## General MySQL features supported for Cloud SQL

  * Fully managed MySQL Community Edition databases in the cloud.
  * Instances available in the Americas, EU, Asia, and Australia. See [all locations where you can create Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/locations).
  * Supports migration from source databases to Cloud SQL destination databases using [Database Migration Service (DMS)](https://docs.cloud.google.com/database-migration/docs/mysql/configure-source-database).
  * Customer data encrypted on Google's internal networks and in database tables, temporary files, and backups.
  * Support for secure external connections with the Cloud SQL Auth Proxy or with the SSL/TLS protocol.
  * Support for private IP (private services access).
  * Data replication between multiple zones with automatic failover.
  * Import and export databases using `mysqldump`, or import and export CSV files.
  * Support for MySQL wire protocol and standard MySQL connectors.
  * Automated backups, on-demand backups, and point-in-time recovery.
  * Instance cloning.
  * Integration with Google Cloud Observability logging and monitoring.
  * [ISO/IEC 27001](http://www.iso.org/iso/home/store/catalogue_ics/catalogue_detail_ics.htm?csnumber=54534) compliant.
  * Support for read pools and read pool autoscaling.
  * Storage shrink. For more information, see [About storage shrink](https://docs.cloud.google.com/sql/docs/mysql/about-storage-shrink).
  * [Resource groups](https://docs.cloud.google.com/sql/docs/mysql/resource-groups).
  * Vector embedding data storage.



## Application languages supported for Cloud SQL for MySQL

You can use Cloud SQL with App Engine applications running in the flexible environment that are written in:

  * C#
  * Go
  * Java
  * Node.js
  * PHP
  * Python
  * Ruby



You can also use Cloud SQL with external applications that use the standard MySQL protocol.

## How you can connect to Cloud SQL for MySQL instances

You can connect to a Cloud SQL instance from the following:

  * [A `mysql` client](https://docs.cloud.google.com/sql/docs/mysql/connect-admin-ip)
  * [Third-party tools like SQL Workbench or Toad for MySQL](https://docs.cloud.google.com/sql/docs/mysql/admin-tools)
  * [External applications](https://docs.cloud.google.com/sql/docs/mysql/connect-external-app)
  * [App Engine applications](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine)
  * [Applications running on Compute Engine](https://docs.cloud.google.com/sql/docs/mysql/connect-compute-engine)
  * [Applications running on Google Kubernetes Engine](https://docs.cloud.google.com/sql/docs/mysql/connect-kubernetes-engine)
  * [Cloud Run functions](https://docs.cloud.google.com/sql/docs/mysql/connect-functions)
  * [Cloud Run](https://docs.cloud.google.com/sql/docs/mysql/connect-run)
  * [Google Apps Script scripts](https://developers.google.com/apps-script/jdbc)



Connecting to Cloud SQL with Private Google Access isn't supported. Private services access is supported. For more information, see [Private Access Options for Services](https://docs.cloud.google.com/vpc/docs/private-access-options).

### User management in Cloud SQL for MySQL 8.0

Due to changes in MySQL 8.0, you can't use `CREATE` or `DELETE` statements for MySQL user management. You also can't modify user privileges using `INSERT`, `UPDATE`, or `DELETE` statements. Instead, use `CREATE USER`, `DROP USER`, `GRANT`, and `REVOKE` statements to modify user privileges. For more information, see [Account management notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-0.html#mysqld-8-0-0-account-management).

**Note:** Disregard information under Account management notes about running `mysql_upgrade` to upgrade to version 8.0. Instead, upgrade using the procedure in [Upgrading MySQL on an instance](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-migrate).

## Differences between standard MySQL and Cloud SQL for MySQL

In general, the MySQL functionality provided by a Cloud SQL instance is the same as the functionality provided by a locally-hosted MySQL instance. However, there are a few differences between a standard MySQL instance and a Cloud SQL instance.

### MySQL features unsupported for Cloud SQL

  * [Federated Engine](https://dev.mysql.com/doc/refman/8.4/en/federated-storage-engine.html)
  * [Memory Storage Engine](https://dev.mysql.com/doc/refman/8.4/en/memory-storage-engine.html)



The following feature is unsupported for Cloud SQL for MySQL 5.6 and 5.7:

  * [The SUPER privilege](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_super) **Note:** Because Cloud SQL is a managed service, it restricts access to certain system procedures and tables that require advanced privileges.



The following features are unsupported for Cloud SQL for MySQL 8.0:

  * [FIPS mode](https://dev.mysql.com/doc/refman/8.0/en/fips-mode.html)



The following feature is unsupported for Cloud SQL for MySQL 8.4:

  * **Tagged GTIDs**. For more information about tagged GTIDs, see "MySQL Replication: tagged GTIDs" in the [Features Added or Changed in MySQL 8.4](https://dev.mysql.com/doc/refman/8.4/en/mysql-nutshell.html) section of the MySQL 8.4 release notes.



In addition, Cloud SQL for MySQL doesn't grant the following privileges introduced in MySQL 8.4:

  * [`TRANSACTION_GTID_TAG`](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_transaction-gtid-tag)
  * [`TELEMETRY_LOG_ADMIN`](https://dev.mysql.com/doc/refman/8.4/en/en/privileges-provided.html#priv_telemetry-log-admin)



The following MySQL 9.7 features are unsupported in Cloud SQL for MySQL 9.7:

  * [MySQL Telemetry](https://dev.mysql.com/doc/refman/9.7/en/mysql-enterprise-telemetry.html)
  * [Profile-Guided Optimization (PGO)](https://dev.mysql.com/doc/relnotes/mysql/9.7/en/news-9-7-0.html#mysqld-9-7-0-packaging)
  * [Replication Applier Metrics Component](https://dev.mysql.com/doc/refman/9.7/en/replication-applier-metrics-component.html)



#### MySQL plugins unsupported for Cloud SQL

  * [InnoDB memcached plugin](https://dev.mysql.com/doc/refman/8.4/en/innodb-memcached.html)
  * [X plugin](https://dev.mysql.com/doc/refman/8.0/en/x-plugin.html)
  * [Clone plugin](https://dev.mysql.com/doc/refman/8.0/en/clone-plugin.html)
  * [InnoDB data-at-rest encryption](https://dev.mysql.com/doc/refman/8.0/en/innodb-data-encryption.html)
  * [validate_password component](https://dev.mysql.com/doc/refman/8.0/en/validate-password.html)



#### MySQL statements unsupported for Cloud SQL

The following SQL statements generate an error with the `Error 1290: The MySQL server is running with the Google option so it cannot execute this statement` message:

  * `LOAD DATA INFILE`

**Note:** `LOAD DATA LOCAL INFILE` _is_ supported.
  * `SELECT ... INTO OUTFILE`

  * `SELECT ... INTO DUMPFILE`

  * `INSTALL PLUGIN ...`

  * `UNINSTALL PLUGIN`

  * `CREATE FUNCTION ... SONAME ...`




The following statements aren't supported because MySQL instances use GTID replication:

  * `CREATE TABLE ... SELECT` statements
  * Transactions or statements that update both transactional and nontransactional tables



The following MySQL statement is unsupported for Cloud SQL for MySQL 5.6 and 5.7, but is supported for Cloud SQL for MySQL 8.0:

  * `CREATE TEMPORARY TABLE` statements inside transactions



For more information, see the [MySQL documentation](https://dev.mysql.com/doc/refman/8.4/en/replication-gtids-restrictions.html).

### MySQL functions unsupported for Cloud SQL

  * `LOAD_FILE()`



### MySQL client program features unsupported for Cloud SQL

  * [`mysqldump`](https://dev.mysql.com/doc/refman/8.4/en/mysqldump.html) using the `--tab` option or options that are used with `--tab`. This is because the [FILE](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_file) privilege isn't granted for users. All other `mysqldump` options are supported. For information on using `mysqldump` options that optimize your file for importing into Cloud SQL, see [Export from your local MySQL server using mysqldump](https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-sql#export-mysqldump).

  * [`mysqlimport`](https://dev.mysql.com/doc/refman/8.4/en/mysqlimport.html) without using the `--local` option. This is because of the `LOAD DATA INFILE` restriction. To import data into your Cloud SQL instance, see [importing using a dump file](https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-sql#import) or [importing using a CSV file](https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-sql#import).

  * If you want to import databases with binary data into your Cloud SQL instance, you must use the `--hex-blob` option with `mysqldump`.

Although `hex-blob` isn't a required flag when you're using a local MySQL server instance and the `mysql` client, it's required if you want to import any databases with binary data into your Cloud SQL instance. To import data into your Cloud SQL instance, see [importing using a dump file](https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-sql#import) or [importing using a CSV file](https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-sql#import).

  * Not all MySQL options and parameters are enabled for editing as [ Cloud SQL flags](https://docs.cloud.google.com/sql/docs/mysql/flags).

To request the addition of a configurable Cloud SQL flag, use the [ Cloud SQL Discussion group](https://groups.google.com/forum/#!forum/google-cloud-sql-discuss).

  * InnoDB is the only supported storage engine. For help with converting tables from MyISAM to InnoDB, see [Converting table to InnoDB](https://dev.mysql.com/doc/refman/8.4/en/converting-tables-to-innodb.html) in the MySQL documentation.




### MySQL options preset for Cloud SQL

Cloud SQL runs MySQL with a specific set of options. If an option might impact how your applications work, we note it here for your information.

**`skip-name-resolve`**

This flag impacts how hostnames are resolved for client connections. See [`skip-name-resolve`](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_skip_name_resolve) in the MySQL documentation.

**`log_bin`**

This flag reports whether binary logging is enabled. If the `--log-bin` option is used, then the value of this variable is `ON`; otherwise it's `OFF`. See [`log_bin`](https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#option_mysqld_log-bin) in the MySQL documentation.

### MySQL authentication

This section describes the changes made to [MySQL built-in authentication](https://docs.cloud.google.com/sql/docs/mysql/built-in-authentication).

#### MySQL 8.0 authentication plugin default

Cloud SQL for MySQL 8.0 uses `mysql_native_password` as the default authentication plugin for new users instead of `caching_sha2_password`. The `mysql_native_password` plugin is the default for MySQL 5.6 and 5.7 users.

If you want new users to use the [`caching_sha2_password`](https://dev.mysql.com/doc/refman/8.0/en/caching-sha2-pluggable-authentication.html) plugin as the default authentication, you can configure your instance flag for `default_authentication_plugin` to use `caching_sha2_password`.

To configure existing users to use `caching_sha2_password`, use the `ALTER USER` command to change the authentication plugin.

Users that have `caching_sha2_password` authentication might need to use the [`get-server-public-key`](https://dev.mysql.com/doc/refman/8.0/en/connection-options.html#option_general_get-server-public-key) flag when connecting. For details, see [Caching SHA-2 Pluggable Authentication](https://dev.mysql.com/doc/refman/8.0/en/caching-sha2-pluggable-authentication.html) in the MySQL documentation.

#### MySQL 8.4 authentication plugin default

Starting in Cloud SQL for MySQL 8.4, the `caching_sha2_password` plugin is the default authentication plugin. All internal users and new user accounts that you create use the `caching_sha2_password` plugin for authentication. Cloud SQL for MySQL 8.4 continues to support existing Cloud SQL user accounts that use the `mysql_native_password` plugin. These existing accounts can continue to connect to Cloud SQL for MySQL instances after those instances have been upgraded MySQL 8.4.

**Important:** BigQuery federated queries don't support the `caching_sha2_password` authentication plugin. If you want to use BigQuery to query your MySQL 8.4 database, don't update the authentication plugin from `caching_sha2_password` to `mysql_native_password`. For more details, see [Troubleshooting](https://docs.cloud.google.com/bigquery/docs/cloud-sql-federated-queries#troubleshooting).

In Cloud SQL for MySQL 8.4, the `mysql_native_password` authentication plugin is deprecated. Any attempt to create a new user account with the deprecated `mysql_native_password` authentication plugin results in an error. You can't set the `authentication_policy` of an account in Cloud SQL for MySQL 8.4 to use `mysql_native_password`.

To change your existing database user accounts to use the `caching_sha2_password` authentication plugin, use the following command:
    
    
    ALTER USER 'username'@'%'
    IDENTIFIED WITH caching_sha2_password BY 'user_password';

Replace username and user_password with the values for the user account that you are updating.

For more information about the implications of this change on the compatibility between servers, clients, and connectors, see [`caching_sha2_password as the Preferred Authentication Plugin`](https://dev.mysql.com/doc/refman/8.0/en/upgrading-from-previous-series.html#upgrade-caching-sha2-password).

#### MySQL 9.7 authentication plugin default

In Cloud SQL for MySQL 9.7, the `mysql_native_password` authentication plugin is removed completely. All Cloud SQL for MySQL database user accounts that use built-in authentication and connect to a MySQL 9.7 instance must use the `caching_sha2_password` authentication plugin.

### Changes to MySQL system flags in Cloud SQL

For some MySQL system flags, Cloud SQL uses values that differ from the default values. You can't change the values for these flags. For a list of flags, see [System flags changed in Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/flags#mysql-flag-changes).

## Cloud SQL features unsupported in Cloud SQL for MySQL 8.0 and later versions

Cloud SQL for MySQL 8.0 and later versions don't support the legacy Cloud SQL for MySQL high availability (HA) configuration that uses failover replicas. Cloud SQL for MySQL 8.0 and later versions only support the regional [HA configuration](https://docs.cloud.google.com/sql/docs/mysql/high-availability).

## PostgreSQL features by Cloud SQL editions

For more information about the features for each edition of Cloud SQL for PostgreSQL, see [Introduction to Cloud SQL editions](https://docs.cloud.google.com/sql/docs/mysql/editions-intro).

## PostgreSQL feature support for Cloud SQL

  * Fully managed PostgreSQL databases in the cloud.
  * Instances available in the Americas, EU, Asia, and Australia. See [all locations where you can create Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/locations).
  * Supports migration from source databases to Cloud SQL destination databases using [Database Migration Service (DMS)](https://docs.cloud.google.com/database-migration/docs/postgres/configure-source-database).
  * Customer data encrypted on Google's internal networks and in database tables, temporary files, and backups.
  * Support for secure external connections with the Cloud SQL Auth Proxy or with the SSL/TLS protocol.
  * Data replication between multiple zones with automatic failover.
  * Import and export databases using SQL dump files.
  * Support for PostgreSQL client-server protocol and standard PostgreSQL connectors.
  * Automated backups, on-demand backups, and point-in-time recovery.
  * Instance cloning.
  * Integration with Google Cloud Observability logging and monitoring.
  * Support for multiple [PostgreSQL versions](https://docs.cloud.google.com/sql/docs/postgres/db-versions).
  * Logical replication
  * Support for read pools and read pool autoscaling
  * Storage shrink. For more information, see [About storage shrink](https://docs.cloud.google.com/sql/docs/mysql/about-storage-shrink).



## Supported PostgreSQL extensions for Cloud SQL

Cloud SQL supports many PostgreSQL extensions. For a complete list of these extensions, see [Configure PostgreSQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions).

## Supported PostgreSQL procedural languages for Cloud SQL

Cloud SQL supports the [`PL/pgSQL` SQL procedural language](https://www.postgresql.org/docs/current/static/plpgsql.html).

## Supported languages for Cloud SQL for PostgreSQL

You can use Cloud SQL with App Engine applications running in the flexible environment that are written in:

  * C#
  * Go
  * Java
  * Node.js
  * PHP
  * Python
  * Ruby



You can also use Cloud SQL with external applications using the standard PostgreSQL client-server protocol.

## How you can connect to Cloud SQL for PostgreSQL instances

You can connect to a Cloud SQL instance from:

  * A `psql` client. [Learn more](https://docs.cloud.google.com/sql/docs/postgres/connect-admin-ip).
  * Third-party tools that use the standard PostgreSQL client-server protocol.
  * External applications. [Learn more](https://docs.cloud.google.com/sql/docs/postgres/connect-external-app).
  * App Engine applications. [Learn more](https://docs.cloud.google.com/sql/docs/postgres/connect-app-engine).
  * Applications running on Compute Engine. [Learn more](https://docs.cloud.google.com/sql/docs/postgres/connect-compute-engine).
  * Applications running on Google Kubernetes Engine. [Learn more](https://docs.cloud.google.com/sql/docs/postgres/connect-kubernetes-engine).
  * Cloud Run functions. [Learn more](https://docs.cloud.google.com/sql/docs/postgres/connect-functions). 
    * Cloud Run. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/connect-run).



Connecting to Cloud SQL with Private Google access isn't supported.

## Differences between standard PostgreSQL and Cloud SQL for PostgreSQL

In general, the PostgreSQL functionality provided by a Cloud SQL instance is the same as the functionality provided by a locally-hosted PostgreSQL instance. However, there are a few differences between a standard PostgreSQL instance and a Cloud SQL instance.

### Unsupported features for Cloud SQL for PostgreSQL

  * Any feature that requires `SUPERUSER` privileges with the following exceptions:

    * You can use the `CREATE EXTENSION` statement only for supported extensions.

    * If you are assigned to the `cloudsqlsuperuser` role, then you can perform `CREATE CAST` and `DROP CAST` statements. For more information, see [Superuser restrictions and privileges](https://docs.cloud.google.com/sql/docs/mysql/users#superuser-restrictions-and-privileges).

  * The `WITHOUT FUNCTION` cast method.

  * Custom background workers.

  * The `psql` client in Cloud Shell doesn't support operations that require a reconnection, such as connecting to a different database using the `\c` command. 

  * Low-Level Virtual Machine (LLVM) Just-in-Time (JIT) compilation.




### Notable differences between PostgreSQL and Cloud SQL for PostgreSQL

  * Some PostgreSQL options and parameters aren't enabled for editing as [ Cloud SQL flags](https://docs.cloud.google.com/sql/docs/postgres/flags).



## SQL Server feature support for Cloud SQL

  * Fully managed SQL Server databases in the cloud.
  * Custom machine types with up to 624 GB of RAM and 96 CPUs.
  * Up to 64 TB of storage available, with the ability to automatically increase storage size as needed.
  * Create and manage instances in the [Google Cloud console](https://console.cloud.google.com/).
  * Instances available in the Americas, Europe, Asia or Australia. See [all locations where you can create Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/locations).
  * [Database Migration Service for SQL Server](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview).
  * Customer data encrypted on Google's internal networks and in database tables, temporary files, and backups.
  * Column- and cell-level encryption for user databases.
  * Support for secure external connections with the Cloud SQL Auth Proxy or with the SSL/TLS protocol.
  * Import databases using BAK and SQL files.
  * Export databases using BAK files.
  * Automated backups, on-demand backups, and point-in-time recovery.
  * Instance cloning.
  * Integration with Stackdriver logging and monitoring.
  * SQL Server Agent enabled to facilitate replication and other jobs.
  * Data replication between multiple regions.
  * Set a default collation for databases, when creating an instance.
  * High availability through a regional persistent disk.
  * Integration with customer-managed Active Directory (CMAD), including Windows Authentication.
  * Integration with Managed Service for Microsoft Active Directory, including Windows Authentication.
  * Integration with Microsoft Entra ID.
  * Change Data Capture (CDC).
  * Intelligent query processing.
  * Accelerated database recovery.
  * Enhanced data classification.
  * UTF-8 character encoding support.
  * Enhanced monitoring.
  * Dynamic Data Masking (DDM).
  * Processor affinity masking using [`affinity mask`](https://docs.cloud.google.com/sql/docs/mysql/flags#list-flags-sqlserver) and [`affinity I/O mask`](https://docs.cloud.google.com/sql/docs/mysql/flags#list-flags-sqlserver).
  * Linked Servers.
  * SQL Server Audit.
  * SQL Server Publisher.
  * SQL Server Subscriber.
  * SQL Server Integration Services (SSIS) that runs on a separate host and connects to Cloud SQL. You can't host SSIS packages on or execute them from Cloud SQL.
  * SQL Server Reporting Services (SSRS) that runs on a separate host and connects to Cloud SQL. You can't host SSRS packages on or execute them from Cloud SQL.
  * The bulk copy program (bcp) utility. To learn more about downloading and installing the bcp utility, see the [Microsoft documentation](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver16#download-the-latest-version-of-bcp-utility).
  * BACPAC file imports and exports by using SqlPackage. To learn more about downloading and installing SqlPackage, see the [Microsoft documentation](https://learn.microsoft.com/en-us/sql/tools/sqlpackage/sqlpackage-download?view=sql-server-ver16).
  * Bulk insert for importing data. This feature is supported only on SQL Server 2022. You can use a stored procedure for performing bulk insert. For more information, see [Use bulk insert for importing data](https://docs.cloud.google.com/sql/docs/sqlserver/import-export#bulk-insert).
  * Transparent Data Encryption (TDE). For information, see [About TDE](https://docs.cloud.google.com/sql/docs/sqlserver/about-tde).
  * Always Encrypted without secure enclaves.
  * Extended Events (XEvents).
  * Custom time zone support at instance creation and post instance creation.
  * Temporal tables. For more information, see [Temporal tables](https://learn.microsoft.com/en-us/sql/relational-databases/tables/temporal-tables?view=sql-server-ver16).
  * Support for read pools
  * Storage shrink. For more information, see [About storage shrink](https://docs.cloud.google.com/sql/docs/mysql/about-storage-shrink).



## SQL Server features unavailable for Cloud SQL

The following features are unavailable in Cloud SQL and Google Cloud doesn't support them:

### General SQL Server features unavailable for Cloud SQL

  * SQL Server Analysis Services (SSAS)
  * SP_Configure settings. For more information about this feature, see [Configure database flags](https://docs.cloud.google.com/sql/docs/sqlserver/flags).
  * Stretch database
  * Backing up to Microsoft Azure Blob Storage
  * Buffer pool extension
  * The OPENROWSET feature
  * Data Quality Services
  * Database Log Shipping
  * Database Mail
  * Dedicated Administrator Connection (DAC)
  * Distribution Transaction Coordinator (MSDTC)
  * File tables
  * FILESTREAM support
  * Installing a server that requires a full server installation with specific authentication mechanisms such as Azure DevOps Server.
  * Maintenance Plans
  * Performance Data Collector
  * Policy-Based Management
  * Machine Learning and R Services
  * Resource Governor
  * Server-level triggers
  * Service Broker endpoints
  * T-SQL endpoints (all operations using `CREATE ENDPOINT` are unavailable)
  * WCF Data Services
  * The `sysadmin` role and system stored procedures that require it
  * Hybrid buffer pool
  * Memory-optimized tempdb metadata
  * In-memory OLTP support for database snapshots
  * Registering external languages
  * Row-level security
  * Object storage backup and restore
  * [Persistent Memory (PMEM)](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-configure-pmem?view=sql-server-ver16)
  * Real-time operational analytics
  * Integrated acceleration and offloading
  * Hybrid buffer pool with direct write
  * Multi-write replication
  * Link to Azure SQL Managed instance
  * Contained availability group
  * Always Encrypted with secure enclaves
  * Support for PFX certificates and other cryptographic improvements
  * MS-TDS 8.0 protocol and TLS 1.3

**Note:** Cloud SQL is a managed service so it restricts access to certain system procedures and tables that require advanced privileges; you can't create or have access to users with superuser permissions.

### Other SQL Server operations unavailable for Cloud SQL

  * ADMINISTER BULK OPERATIONS
  * ALTER ANY CREDENTIAL
  * ALTER ANY EVENT NOTIFICATION
  * ALTER ANY EVENT SESSION
  * ALTER RESOURCES
  * ALTER SETTINGS
  * AUTHENTICATE SERVER
  * CONTROL_SERVER
  * CREATE DDL EVENT NOTIFICATION
  * CREATE ENDPOINT
  * CREATE TRACE EVENT NOTIFICATION
  * EXTERNAL ACCESS ASSEMBLY
  * RESTORE
  * SHUTDOWN
  * CLR ASSEMBLIES



## Supported syntax for 

Cloud SQL supports the [Transact-SQL syntax](https://docs.microsoft.com/en-us/sql/t-sql/language-elements/transact-sql-syntax-conventions-transact-sql?view=sql-server-2017).

## Supported languages for 

You can use Cloud SQL with App Engine applications running in the flexible environment that are written in:

  * C#
  * Go
  * Java
  * Node.js
  * PHP
  * Python
  * Ruby



## How you can connect to instances

You can connect to a Cloud SQL instance from:

  * [SQL Server Management Studio (SSMS)](https://docs.microsoft.com/en-us/sql/ssms/sql-server-management-studio-ssms?view=sql-server-2017). 
    * A client. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/connect-admin-ip).
  * [The sqlcmd utility](https://docs.microsoft.com/en-us/sql/ssms/scripting/sqlcmd-use-the-utility?view=sql-server-2017).



Connecting to Cloud SQL with Private Google access isn't supported.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
