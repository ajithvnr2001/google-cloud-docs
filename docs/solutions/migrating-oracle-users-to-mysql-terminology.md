---
url: https://docs.cloud.google.com/solutions/migrating-oracle-users-to-mysql-terminology/
title: Migrating Oracle users to Cloud SQL for MySQL: Terminology and functionality \u00a0|\u00a0 Solutions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:42:56.380106+00:00
---

# Migrating Oracle users to Cloud SQL for MySQL: Terminology and functionality  |  Solutions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/solutions/migrating-oracle-users-to-mysql-terminology/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Solutions ](https://docs.cloud.google.com/solutions)



Send feedback 

#  Migrating Oracle users to Cloud SQL for MySQL: Terminology and functionality Stay organized with collections  Save and categorize content based on your preferences. 

This document is part of a series that provides key information and guidance related to planning and performing Oracle® 11g/12c database migrations to Cloud SQL for MySQL version 5.7, second-generation instances. The series includes the following parts:

  * Migrating Oracle users to Cloud SQL for MySQL: Terminology and functionality (this document)
  * [Migrating Oracle users to Cloud SQL for MySQL: Data types, users, and tables](https://docs.cloud.google.com/solutions/migrating-oracle-users-to-mysql-data-users-tables)
  * [Migrating Oracle users to Cloud SQL for MySQL: Queries, stored procedures, functions, and triggers](https://docs.cloud.google.com/solutions/migrating-oracle-users-to-mysql-queries-procedures-functions-triggers)
  * [Migrating Oracle users to Cloud SQL for MySQL: Security, operations, monitoring, and logging](https://docs.cloud.google.com/solutions/migrating-oracle-users-to-mysql-security-ops-monitoring-logging)



## Terminology

This section details the similarities and differences in database terminology between Oracle and Cloud SQL for MySQL. It reviews and compares core aspects of each of the database platforms. The comparison distinguishes between Oracle versions 11g and 12c, due to architectural differences (for example, Oracle 12c introduces the multi-tenant feature). The Cloud SQL for MySQL version referenced here is 5.7.x.

### Differences in terminology between Oracle 11g and Cloud SQL for MySQL

Oracle 11g | Description | Cloud SQL for MySQL | Key differences  
---|---|---|---  
**Instance** | A single Oracle 11g instance can hold only one database. | **Instance** | One MySQL instance can hold multiple databases.  
**Database** | A database qualifies as a single instance (the name of the database is identical to the instance name). | **Database** | Multiple or single databases serve multiple applications.  
**Schema** | Schema and users are identical because both are considered to be the owners of database objects (a user can be created without specifying or being allocated to a schema). | **Schema** | A schema is referred to as a database, while database objects are created under a certain schema/database.  
**User** | Identical to schema because both are owners of database objects—for example, instance → database → schemas/users → database objects. | **User** | A database user with specific permissions to connect or modify database objects on specific schemas/databases—for example, instance → databases/schemas → database objects.  
**Role** | Defined set of database permissions that can be chained as a group and can be assigned to database users. | **MySQL privileges** | MySQL 5.7 does not support roles management. Permissions can be configured using the `GRANT` clause for users to have privileges on database objects at different levels (READ/WRITE, etc.).  
**Admin/SYSTEM users** | Oracle administrator users with the highest level of access:  

    
    
    SYS
    SYSTEM
    

| **Super users** | Once deployed, Cloud SQL for MySQL has the `root@'%'` user (can connect from any host) and an additional user named `mysql.sys`, which can connect only from the localhost.  
**Dictionary/metadata** | Oracle uses the following metadata tables:  

    
    
    USER_TableName
    ALL_TableName
    DBA_TableName
    

| **Dictionary/metadata** | MySQL uses several databases/schemas for dictionary/metadata:  

    
    
    MYSQL
    INFORMATION_SCHEMA
    PERFORMANCE_SCHEMA
    SYS
    

Each of these databases are also system databases and are created with each Cloud SQL for MySQL deployment.  
**System dynamic views** | Oracle dynamic views:  

    
    
    V$ViewName
    

| **System dynamic views** | MySQL dynamic views can be found in several of the system databases:  

    
    
    INFORMATION_SCHEMA
    PERFORMANCE_SCHEMA
    SYS
      
  
**Tablespace** | The primary logical storage structures of Oracle databases; each tablespace can hold one or more data files. | **Tablespace** | Similar to Oracle, a MySQL tablespace is a logical unit, but represents only a single table, unlike the Oracle tablespace, which can have multiple data files (holds data for multiple tables).  
  
MySQL supports the creation of a new tablespace with an allocated data file, then creating a new table attached to the newly created tablespace. Note that tablespace configuration settings such as sizing and limits are set using database parameters and not during tablespace creation.  
**Data files** | The physical elements of an Oracle database that hold the data and are defined under a specific tablespace.  
  
A single data file is defined by the initial size and max size and can hold data for multiple tables.  
  
Oracle data files uses the `.dbf` suffix (not mandatory). | **Data files** | Cloud SQL for MySQL uses the `innodb_file_per_table` parameter with the value "`ON`" (default); this configuration generates a new data file for each table and a dedicated tablespace.  
  
MySQL data files use `.ibd` (data) and `.frm` (metadata) files.  
**System tablespace** | Contains the data dictionary tables and views objects for the entire Oracle database. | **System tablespace** | Same as Oracle, contains the dictionary/metadata tables. Stored in the `innodb_system` tablespace attached with the `ibdata1` data file.  
**Temporary tablespace** | Contains schema objects valid for the duration of a session; in addition, it supports running operations that cannot fit in server memory. | **Temporary tablespace** | Purpose is identical to Oracle, stored in MySQL `innodb_temporary` tablespace attached with the `ibtmp1` data file.  
**Undo**  
**tablespace** | A special type of system-permanent tablespace used by Oracle to manage rollback operations when running the database in automatic undo management mode (default). | **Undo tablespace** | Similar to Oracle, MySQL Undo tablespace contains undo logs for rollback purposes. By default, this option is set to `OFF` and mentioned as [deprecated](https://dev.mysql.com/doc/refman/5.7/en/innodb-undo-tablespaces.html) for future MySQL releases.  
**ASM** | Oracle Automatic Storage Management is an integrated, high-performance database file system and disk manager all run automatically by an Oracle database configured with ASM. | **Not supported** | MySQL uses the term storage engines to describe different data handling implementations, but does not support Oracle ASM. [Cloud SQL for MySQL](https://docs.cloud.google.com/sql) supports many features that provide storage automation, such as automatic storage increases, performance, and scalability.  
**Tables/views** | User-created fundamental database objects. | **Tables/views** | Identical to Oracle.  
**Materialized views** | Defined with specific SQL statements and can be manually or automatically refreshed based on specific configurations. | **Not supported by MySQL** | As a workaround, triggers/views can be used instead of Oracle materialized views.  
**Sequence** | Oracle unique value generator. | **Auto increment** | MySQL does not support Oracle sequences; use the `AUTO_INCREMENT` as an alternative solution to automatic sequence generation functionality.  
**Synonym** | Oracle database objects that serve as alternative identifiers for other database objects. | **Not supported** | MySQL does not support Oracle Synonym; as a workaround, views can be used while setting the appropriate permissions.  
**Partitioning** | Oracle provides many partitioning solutions for splitting large tables into smaller managed pieces. | **Partitioning** | MySQL has more limited partitioning support to improve performance, while retaining data management and maintenance operations, like Oracle partitions.  
**Flashback database** | Oracle proprietary feature that can be used to initialize an Oracle database to a previous defined time, allowing you to query or restore data that was modified or corrupted by mistake. | **Not supported** | For an alternative solution, you can use Cloud SQL backups and point-in-time [recovery](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restoring#restorebackups) to restore a database to a previous state (for example, restoring before a table drop).  
**sqlplus** | Oracle command-line interface that lets you query and manage the database instance. | **mysql** | MySQL-equivalent command line-interface for querying and managing. Can be connected from any client with the appropriate permissions to Cloud SQL.  
**PL/SQL** | Oracle extended procedural language to ANSI SQL. | **MySQL** | MySQL has its own extended procedural language with different syntax and implementation, and does not have additional naming for this extended language.  
**Package & package body** | Oracle-specific functionality to group stored procedures and functions under the same logical reference. | **Not supported** | MySQL supports stored procedures and functions as single objects with group allocation.  
**Stored procedures & functions** | Uses PL/SQL to implement code functionality. | **Stored procedure & functions** | The creation of stored procedures and functions is supported by MySQL with its proprietary procedural language implementation.  
**Trigger** | Oracle object used to control DML implementation over tables. | **Trigger** | Identical to Oracle.  
**PFILE/SPFILE** | Oracle instance and database level parameters are kept in a binary file known as the `SPFILE` (in previous versions, the file was called `PFILE`), which can be used as a text file for setting parameters manually. | **Cloud SQL for MySQL database flags** | You can set or modify Cloud SQL for MySQL parameters through the [database flags](https://docs.cloud.google.com/sql/docs/mysql/flags) utility. You cannot change database parameters in Cloud SQL for MySQL by using the MySQL client command-line interface (for example, `mysql> SET GLOBAL ...`). You can change these parameters only by using the database flags utility.  
**SGA/PGA/AMM** | Oracle memory parameters that control memory allocation to the database instance. | ` INNODB_BUFFER_POOL_SIZE ` | MySQL has its own memory parameters. An equivalent parameter could be `INNODB_BUFFER_POOL_SIZE`. In Cloud SQL for MySQL, this parameter is predefined by the chosen instance type, and the value changes accordingly.  
**Result Cache** | Reduces SQL I/O operations by retrieving rows from the buffer cache, which can be managed using database parameters and hints at the session level. | **Query Cache** | Has the same fundamental purpose as Oracle Result Cache and can be managed at the database level and at the session level.  
**Database hints** | Controlled impact to SQL statements that influence the optimizer's behavior in order to achieve better performance. Oracle has more than 50 different database hints. | **Database hints** | MySQL supports a limited set of database hints in comparison to Oracle (optimizer hints and index hints). Note that MySQL uses different database hints, syntax, and naming.  
**RMAN** | Oracle Recovery Manager utility. Used to take database backups with extended functionality to support multiple disaster recovery scenarios and more (cloning, etc.). | **Cloud SQL for MySQL Backup** | Cloud SQL for MySQL offers two methods for applying full [backup](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups): on-demand and automated backups.  
**Data Pump (EXPDP/IMPDP)** | Oracle dump generation utility that can be used for many features, such as export/import, database backup (at the schema or object level), schema metadata, generate schema SQL files and more. | 
    
    
    mysqldump/mysqlimport
    

| MySQL dump (export) utility that can be connected as a client (remotely) and generate a dump file (SQL). Later, you can compress the dump file and move it to Cloud Storage. The `mysqldump` utility is for the export step only.  
**SQL*Loader** | Tool that provides the ability to upload data from external files such as text files, CSV files, and more. | 
    
    
    mysqlimport/  
    LOAD FILE INFILE
    

| The `mysqlimport` utility provides the ability to load text or CSV files (Oracle supports additional file formats) into a database table with a corresponding structure.  
**Data Guard** | Oracle disaster recovery solution using a standby instance, enabling users to perform `READ` operations from the standby instance. | **Cloud SQL for MySQL high availability and replication** | To achieve disaster recovery or high availability, Cloud SQL for MySQL offers the failover replica [architecture](https://docs.cloud.google.com/sql/docs/mysql/high-availability) and for read-only operations (READ/WRITE separation) using the [Read Replica](https://docs.cloud.google.com/sql/docs/mysql/replication).  
**Active Data Guard/Golden Gate** | Oracle's main replication solutions, which can serve multiple purposes such as Standby (DR), Read-Only instance, Bi-Directional replication (multi-source), data warehousing, and more. | **Cloud SQL for MySQL Read Replica** | Cloud SQL for MySQL [Read Replica](https://docs.cloud.google.com/sql/docs/mysql/replication) to implement clustering with READ/WRITE separation. Currently, there is no support for multi-source configuration, such as Golden Gate Bi-Directional replication, or heterogeneous replication.  
**RAC** | Oracle Real Application Cluster. Oracle proprietary clustering solution for providing high availability by deploying multiple database instances with a single storage unit. | **Not supported** | Multi-source architecture is not yet supported in Google Cloud Cloud SQL. To achieve clustering architecture with READ/WRITE separation and high availability, use Cloud SQL high availability and read replica.  
**Grid/Cloud Control (OEM)** | Oracle software for managing and monitoring databases and other related services in a web app format. This tool is useful for real-time database analysis to understand high workloads. | **Cloud SQL for MySQL Console, Cloud Monitoring** | Use Cloud SQL for MySQL for monitoring, including detailed time and resources-based graphs. Also use Cloud Monitoring to hold specific MySQL monitoring metrics and logs analysis for advanced monitoring capabilities.  
**REDO logs** | Oracle transaction logs that consist of two (or more) pre-allocated defined files that store all data modifications as they occur. The purpose of the redo log is to protect the database in case of an instance failure. | **REDO logs** | MySQL also has [redo logs](https://dev.mysql.com/doc/refman/5.7/en/innodb-redo-log.html) files, which are used during crash recovery to correct data written by incomplete transactions' redo logs mechanism.  
**Archive logs** | Archive logs provide support for backup and replication operations and more. Oracle writes to archive logs (if enabled) after each redo log switch operation. | **binlogs** | MySQL implementation of transaction logs retention. Used mainly for replication purposes (enabled by default with Cloud SQL).  
**Control file** | The Oracle control file holds information about the database, such as data files, redo logs names, and locations, the current log sequence number, and information about the instance checkpoint. | **MySQL** | MySQL architecture doesn't include a control file similar to Oracle implementation. This is controlled through the MySQL parameters and by using the `SHOW MASTER STATUS` command in order to see the current binary log position.  
**SCN** | Oracle SCN (System Change Number) is the primary method of maintaining data consistency by all Oracle database components in order to satisfy the ACID model of transaction. | **Log Sequence Number** | MySQL implementation for database consistency uses the LSN (Log Sequence Number).  
**AWR** | Oracle AWR (Automatic Workload Repository) is a verbose report providing detailed information about Oracle database instance performance and is considered a DBA tool for performance diagnostics. | 
    
    
    performance_schema
    

| MySQL doesn't have a report equivalent to Oracle AWR, but MySQL gathers performance data collected by `performance_schema`. An alternative solution would be to use MySQL [Workbench](https://dev.mysql.com/doc/workbench/en/wb-performance-dashboard.html) performance dashboards.  
      
    
    DBMS_SCHEDULER
    

| Oracle utility used to set and time predefined operations. | 
    
    
    EVENT_SCHEDULER
    

| MySQL database internal scheduler functionality. By default, this feature is set to `OFF`.  
**Transparent data encryption** | Encrypts data stored on disks as data-at-rest protection. | **Cloud SQL Advanced Encryption Standard** | Cloud SQL for MySQL uses the 256-bit [Advanced Encryption Standard (AES-256)](https://docs.cloud.google.com/sql/faq#encryption-manage-rest) for data-at-rest security protection, as well as for in-transit data  
**Advanced compression** | To improve the database storage footprint, reduce storage costs, and improve database performance, Oracle provides data (tables/indexes) advanced compression capabilities. | **InnoDB table compression** | MySQL offers [table compression](https://dev.mysql.com/doc/refman/5.7/en/innodb-table-compression.html) by creating a table using the `ROW_FORMAT` parameter set to `COMPRESSED`. Read more about [index compression](https://dev.mysql.com/doc/refman/5.5/en/innodb-compression-internals.html).   
**SQL Developer** | Oracle free SQL GUI for managing and running SQL and PL/SQL statements (can be used with MySQL as well). | **MySQL Workbench** | MySQL free SQL GUI for managing and running SQL and MySQL code statements.  
**Alert Log** | Oracle main log for general database operations and errors. | **MySQL Error Log** | Uses Cloud Logging [Logs Viewer](https://docs.cloud.google.com/sql/docs/mysql/instance-info#mysqllogs) to watch MySQL error logs  
**`DUAL` table** | Oracle special table holding mostly for retrieving pseudo column values such as `SYSDATE` or `USER` | **DUAL table** | MySQL allows `DUAL` to be specified as a table in SQL statements that do not depend on data from any tables.  
**External table** | Oracle allows users to create external tables having the source data on files outside the database. | **Not supported.** | No direct equivalent.  
**Listener** | Oracle network process tasked with listening for incoming database connections | **Cloud SQL Authorized networks** | MySQL accepts connections from remote sources once allowed in the Cloud SQL [Authorized Networks](https://docs.cloud.google.com/sql/docs/mysql/connect-external-app#proxy) configuration page  
**TNSNAMES** | Oracle network configuration file that defines database addresses for establishing connections by using connection aliases. | **Does not exist** | MySQL accepts external connections using the Cloud SQL Instance connection name or [private](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip)/[public](https://docs.cloud.google.com/sql/docs/mysql/configure-ip) IP address. [Cloud SQL Proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy) is an additional secure access method to connect to Cloud SQL for MySQL (second-generation instances) without having to allow specific IP addresses or configure SSL.  
**Instance default port** | 1521 | **Instance default port** | 3306  
**Database link** | Oracle schema objects which can be used to interact with local/remote database objects. | **Not supported** | For an alternative workaround, use application code to connect and retrieve data from a remote database.  
  
### Differences in terminology between Oracle 12c and Cloud SQL for MySQL

Oracle 12c | Description | Cloud SQL for MySQL | Key differences  
---|---|---|---  
**Instance** | The multi-tenant ability introduced in Oracle 12c instance that can hold multiple databases as a pluggable database (PDB), as opposed to Oracle 11g, where an Oracle instance can only obtain one database.  | **Instance** | Cloud SQL for MySQL can hold multiple databases with different naming serving multiple services and applications.  
**CDB** | A multi-tenant container database (CDB) can support one or more PDBs, while CDB global objects (affects all PDBs) can be created, such as roles. | **MySQL Instance** | The MySQL instance is comparable to the Oracle CDB. Both provide a system layer for the PDBs.  
**PDB** | PDBs (pluggable databases) can be used to isolate services and applications from one another and can be used as a portable collection of schemas. | **MySQL databases/schemas** | A MySQL database can serve multiple services and applications as well as many database users.  
**Session sequences** | Starting with Oracle 12c, sequences can be created at the session level (return unique values only within a session) or at the global level (for example, when using temporary tables). | **Auto**  
**increment** | Sequences are not supported by MySQL, but users can use the `AUTO_INCREMENT` column property as an alternate solution.  
**Identity columns** | The Oracle 12c `IDENTITY` type generates a sequence and associates it with a table column without the need to manually create a separate sequence object. | **Auto increment** | Use the `AUTO_INCREMENT` column property to simulate the same functionality as Oracle 12c identity column (an alternative solution to automatic sequence generation functionality).  
  
**Sharding** | Oracle sharding is a solution in which one Oracle database is partitioned into multiple smaller databases (shards) to allow scalability, availability, and geo-distribution for OLTP environments. | **Not supported (as a feature)** | MySQL does not have an equivalent sharding feature. Sharding can be implemented using MySQL (as the data platform) with a supporting application layer.  
**In-memory database** | Oracle provides a suite of features which can improve database performance for OLTP as well for and mixed workloads. | **Not supported** | MySQL does not have an equivalent feature. You can use [Memorystore](https://docs.cloud.google.com/memorystore) as an alternative.  
**Redaction** | As part of Oracle's advanced security features, redaction can perform column masking to prevent sensitive data from being displayed by users and applications. | **Not supported** | MySQL does not have an equivalent feature.  
  
## Functionality

Although Oracle 11g/12c and Cloud SQL for MySQL databases work on different architectures (infrastructure and extended procedural languages), they share the same fundamental aspects of a relational database. They support database objects, multi-user concurrency workloads, and transactions (ACID compatibility). They also manage locking contentions that support multiple isolation levels (based on the business needs), and they serve ongoing application requirements as a relational data store for Online Transactional Processing (OLTP) operations and Online Analytical Processing (OLAP).

The following section provides an overview of some of the main functional differences between Oracle and Cloud SQL for MySQL. In some cases, where needed, the section includes detailed technical comparisons.

### Creating and viewing existing databases

Oracle 11g/12c | Cloud SQL for MySQL 5.7  
---|---  
You usually create databases, and view existing ones, by using the Oracle [Database Creation Assistant (DBCA)](https://docs.oracle.com/cd/B28359_01/server.111/b28310/create002.htm#ADMIN12479) utility. Manually created databases or instances require that you specify additional parameters:  

    
    
    SQL> CREATE DATABASE ORADB
         USER SYS IDENTIFIED BY password
         USER SYSTEM IDENTIFIED BY password
         EXTENT MANAGEMENT LOCAL
         DEFAULT TEMPORARY TABLESPACE temp
         UNDO TABLESPACE undotbs1
         DEFAULT TABLESPACE users;
    

| Use a statement of the form `CREATE DATABASE Name;`, as in this example: 
    
    
    mysql> CREATE DATABASE MYSQLDB;
      
  
**Oracle 12c** | **Cloud SQL for MySQL 5.7**  
In Oracle 12c, you can create PDBs from the seed, either from a container database (CDB) template or by cloning a PDB from an existing PDB. You use several parameters:  
  

    
    
    SQL> CREATE PLUGGABLE DATABASE PDB
         ADMIN USER usr IDENTIFIED BY passwd
         ROLES = (dba)
         DEFAULT TABLESPACE sales
         DATAFILE '/disk1/ora/dbs/db/db.dbf'
         SIZE 250M AUTOEXTEND ON
         FILE_NAME_CONVERT =
         ('/disk1/oracle/dbs/pdbseed/',
          '/disk1/oracle/dbs/salespdb/')
          STORAGE (MAXSIZE 2G)
          PATH_PREFIX =
          '/disk1/oracle/dbs/salespdb/';
    

| Use a statement of the form `CREATE DATABASE Name;`, as in this example:  

    
    
    mysql> CREATE DATABASE MYSQLDB;
      
  
List all PDBs:  

    
    
    SQL> SHOW is PDBS;
    

| List all existing databases:  

    
    
    mysql> SHOW DATABASES;
      
  
Connect to a different PDB:  

    
    
    SQL> ALTER SESSION SET CONTAINER=pdb;
    

| Connect to a different database:  

    
    
    mysql> use databaseName;
    

Or:  

    
    
    mysql> \u databaseName;
      
  
Open or close a specific PDB (open/read-only):  

    
    
    SQL> ALTER PLUGGABLE DATABASE pdb CLOSE;
    

| Not supported for a single database.  
  
All databases are under the same Cloud SQL for MySQL instance; thus, all databases are all up or all down.  
  
### Managing a database through the Cloud SQL console

  * In the Google Cloud console, go to **Storage > SQL > Instance > Databases > View/Create**.

![Console page for creating/viewing a MySQL database.](https://docs.cloud.google.com/static/solutions/images/migrating-oracle-users-mysql-database.png)




### System databases and schemas

Oracle database instances obtain certain system schemas—for example, `SYS/SYSTEM`—with the owners role of database metadata objects.

In contrast, MySQL holds several system databases (as opposed to Oracle schemas), which serve the metadata layer (note that the database names are case sensitive):

  * [**`Mysql`**](https://dev.mysql.com/doc/refman/5.7/en/system-schema.html)

The `mysql` system database holds tables that store information required by the MySQL server as it runs, such as the following:

    * System privileges tables
    * Objects information tables
    * Log system tables
    * Replication system tables
    * Optimizer system tables
    * Time zone system tables
  * [**`INFORMATION_SCHEMA`**](https://dev.mysql.com/doc/refman/5.7/en/information-schema.html)

`INFORMATION_SCHEMA` serves as the main database data dictionary and system catalog. It provides access to database metadata, which is internal database information about the MySQL server, such as the name of a database or table, the column data type, and the access privileges.

  * [**`performance_schema`**](https://dev.mysql.com/doc/refman/5.7/en/performance-schema.html)

A system database that collects statistical information about the MySQL instance. The `performance_schema` system database holds metrics for server execution monitoring at a very granular level. The schema provides server internal execution inspection at run time, and it can serve as the main source for analyzing database performance issues.

The `performance_schema` is not enabled by default using [Cloud SQL for MySQL](https://docs.cloud.google.com/sql/docs/mysql/flags#tips-performance-schema). To enable the schema, use the [`gcloud`](https://docs.cloud.google.com/sql/docs/mysql/flags) command-line tool:
        
        gcloud sql instances patch INSTANCE_NAME --database-flags performance_schema=on
        

To complete this configuration, you must reboot the instance. You cannot modify the `--database-flags` parameter by using the Cloud SQL for MySQL database flags page in the Google Cloud console.

  * [**`sys`**](https://dev.mysql.com/doc/refman/5.7/en/sys-schema.html)

The `sys` schema exists from MySQL version 5.5.7 and holds mainly views on the `performance_schema` system tables. This schema provides a more readable set of views that summarize `performance_schema` data into a more easily understandable form. The `sys` schema also holds several stored procedures and functions to perform operations such as configuring `performance_schema` and generating diagnostic reports.

The `sys` schema displays information only when the `performance_schema` is enabled.




### Viewing metadata and system dynamic views

This section provides an overview of some of the most common metadata tables and system dynamic views used in Oracle and their corresponding database objects in Cloud SQL for MySQL version 5.7.

Oracle provides hundreds of system metadata tables and views, while MySQL only holds several dozen. For each case, there can be more than one database object, serving a specific purpose.

Oracle provides several levels of metadata objects, each requiring different privileges:

  * `USER_TableName`: Can be viewed by the user.
  * `ALL_TableName`: Can be viewed by all users.
  * `DBA_TableName`: Can be viewed only by users with the DBA privilege, such as `SYS` and `SYSTEM`.



For dynamic performance views, Oracle uses the `V$` and `GV$` prefixes. For a MySQL user to be able to view system metadata tables or views, they must have specific permissions on system objects. For more information about security, see the [Security](https://docs.cloud.google.com/solutions/migrating-oracle-users-to-mysql-security-ops-monitoring-logging#security) section.

**Note:** In MySQL, table and view names are case sensitive.Metadata type | Oracle table/view | MySQL table/view/show (MySQL CMD)  
---|---|---  
**Open sessions** | 
    
    
    V$SESSION
    

| 
    
    
    SHOW PROCESSLIST
    INFORMATION_SCHEMA.PROCESSLIST
    performance_schema.threads
      
  
**Running transactions** | 
    
    
    V$TRANSACTION
    

| 
    
    
    INFORMATION_SCHEMA.INNODB_TRX
      
  
**Database objects** | 
    
    
    DBA_OBJECTS
    

| Not supported. Query each object by its type.  
**Tables** | 
    
    
    DBA_TABLES
    

| 
    
    
    INFORMATION_SCHEMA.TABLES
    INFORMATION_SCHEMA.INNODB_SYS_TABLES
      
  
**Table columns** | 
    
    
    DBA_TAB_COLUMNS
    

| 
    
    
    INFORMATION_SCHEMA.COLUMNS
    INFORMATION_SCHEMA.INNODB_SYS_COLUMNS
      
  
**Table and column privileges** | 
    
    
    TABLE_PRIVILEGES
    DBA_COL_PRIVS
    ROLE_TAB_PRIVS
    

| 
    
    
    INFORMATION_SCHEMA.COLUMN_PRIVILEGES
      
  
**Partitions** | 
    
    
    DBA_TAB_PARTITIONS
    DBA_TAB_SUBPARTITIONS
    

| 
    
    
    INFORMATION_SCHEMA.PARTITIONS
    SHOW CREATE TABLE TableName
    SHOW TABLE STATUS LIKE 'TableName'
      
  
**Views** | 
    
    
    DBA_VIEWS
    

| 
    
    
    INFORMATION_SCHEMA.VIEWS
      
  
**Constraints** | 
    
    
    DBA_CONSTRAINTS
    

| 
    
    
    INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS
    SHOW CREATE TABLE TableName
      
  
**Indexes** | 
    
    
    DBA_INDEXES
    DBA_PART_INDEXES
    

| 
    
    
    INFORMATION_SCHEMA.STATISTICS
    INFORMATION_SCHEMA.INNODB_SYS_INDEXES
    INFORMATION_SCHEMA.KEY_COLUMN_USAGE
      
  
**Materialized views** | 
    
    
    DBA_MVIEWS
    

| Not supported  
**Stored procedures** | 
    
    
    DBA_PROCEDURES
    

| 
    
    
    INFORMATION_SCHEMA.ROUTINES
      
  
**Stored functions** | 
    
    
    DBA_PROCEDURES
    

| 
    
    
    INFORMATION_SCHEMA.ROUTINES
      
  
**Triggers** | 
    
    
    DBA_TRIGGERS
    

| 
    
    
    INFORMATION_SCHEMA.TRIGGERS
      
  
**Users** | 
    
    
    DBA_USERS
    

| 
    
    
    mysql.user
      
  
**User privileges** | 
    
    
    DBA_SYS_PRIVS
    DBA_ROLE_PRIVS
    SESSION_PRIVS
    

| 
    
    
    INFORMATION_SCHEMA.USER_PRIVILEGES
      
  
**Jobs/**  
**Scheduler** | 
    
    
    DBA_JOBS
    DBA_JOBS_RUNNING
    DBA_SCHEDULER_JOBS
    DBA_SCHEDULER_JOB_LOG
    

| 
    
    
    INFORMATION_SCHEMA.EVENTS
      
  
**Tablespaces** | 
    
    
    DBA_TABLESPACES
    

| 
    
    
    INFORMATION_SCHEMA.INNODB_SYS_TABLESPACES
      
  
**Data files** | 
    
    
    DBA_DATA_FILES
    

| 
    
    
    INFORMATION_SCHEMA.FILES
    INFORMATION_SCHEMA.INNODB_SYS_DATAFILES
      
  
**Synonyms** | 
    
    
    DBA_SYNONYMS
    

| Not supported  
**Sequences** | 
    
    
    DBA_SEQUENCES
    

| Not supported  
**Database links** | 
    
    
    DBA_DB_LINKS
    

| Not supported  
**Statistics** | 
    
    
    DBA_TAB_STATISTICS
    DBA_TAB_COL_STATISTICS
    DBA_SQLTUNE_STATISTICS
    DBA_CPU_USAGE_STATISTICS
    

| 
    
    
    INFORMATION_SCHEMA.STATISTICS
    INFORMATION_SCHEMA.KEY_COLUMN_USAGE
    SHOW INDEXES FROM TableName
      
  
**Locks** | 
    
    
    DBA_LOCK
    DBA_DDL_LOCKS
    DBA_DML_LOCKS
    V$SESSION_BLOCKERS
    V$LOCKED_OBJECT
    

| 
    
    
    INFORMATION_SCHEMA.INNODB_LOCKS
    INFORMATION_SCHEMA.INNODB_LOCK_WAITS
    INFORMATION_SCHEMA.INNODB_TRX
    performance_schema.metadata_locks
    performance_schema.rwlock_instances
    SHOW PROCESSLIST
      
  
**Database parameters** | 
    
    
    V$PARAMETER
    V$NLS_PARAMETERS
    SHOW PARAMETER Param
    

| 
    
    
    performance_schema.global_variables
    performance_schema.session_variables
    INFORMATION_SCHEMA.CHARACTER_SETS
    SHOW VARIABLES LIKE '%variable%';
      
  
**Segments** | 
    
    
    DBA_SEGMENTS
    

| Segments table is not supported. Query each object by its type.  
**Roles** | 
    
    
    DBA_ROLES
    DBA_ROLE_PRIVS
    USER_ROLE_PRIVS
    

| 
    
    
    Roles not supported use instead:
    information_schema.COLUMN_PRIVILEGES
    information_schema.SCHEMA_PRIVILEGES
    information_schema.TABLE_PRIVILEGES
    information_schema.USER_PRIVILEGES
    mysql.columns_priv
    mysql.procs_priv
    mysql.proxies_priv
    mysql.tables_priv
      
  
**Session history** | 
    
    
    V$ACTIVE_SESSION_HISTORY
    DBA_HIST_*
    

| 
    
    
    sys.statement_analysis
    performance_schema.events_stages_history
    performance_schema.events_stages_history_long
    performance_schema.events_statements_history
    performance_schema.events_statements_history_long
    performance_schema.events_transactions_history
    performance_schema.events_transactions_history_long
    performance_schema.events_waits_history
    performance_schema.events_waits_history_long
      
  
**Version** | 
    
    
    V$VERSION
    

| 
    
    
    sys.version
    SHOW VARIABLES LIKE '%version%';
      
  
**Wait events** | 
    
    
    V$WAITCLASSMETRIC
    V$WAITCLASSMETRIC_HISTORY
    V$WAITSTAT
    V$WAIT_CHAINS
    

| 
    
    
    performance_schema.events_waits_current
    performance_schema.events_waits_history
    performance_schema.events_waits_history_long
    sys.innodb_lock_waits
    sys.io_global_by_wait_by_bytes
    sys.io_global_by_wait_by_latency
    sys.schema_table_lock_waits
    sys.wait_classes_global_by_avg_latency
    sys.wait_classes_global_by_latency
    sys.waits_by_host_by_latency
    sys.waits_by_user_by_latency
    sys.waits_global_by_latency
      
  
**SQL tuning and**  
**analyzing** | 
    
    
    V$SQL
    V$SQLAREA
    V$SESS_IO
    V$SYSSTAT
    V$STATNAME
    V$OSSTAT
    V$ACTIVE_SESSION_HISTORY
    V$SESSION_WAIT
    V$SESSION_WAIT_CLASS
    V$SYSTEM_WAIT_CLASS
    V$LATCH
    V$SYS_OPTIMIZER_ENV
    V$SQL_PLAN
    V$SQL_PLAN_STATISTICS
    

| 
    
    
    performance_schema.events_statements_current
    performance_schema.events_statements_history
    performance_schema.events_statements_history_long
    sys.statement_analysis
    sys.host_summary_by_statement_latency
    sys.host_summary_by_statement_type
    sys.statements_with_errors_or_warnings
    sys.statements_with_full_table_scans
    sys.statements_with_runtimes_in_95th_percentile
    sys.statements_with_sorting
    sys.statements_with_temp_tables
    sys.user_summary_by_statement_latency
    sys.user_summary_by_statement_type
    slow-query-log
    general-log
    SHOW STATUS LIKE '%StatusName%';
      
  
**Instance**  
**memory tuning** | 
    
    
    V$SGA
    V$SGASTAT
    V$SGAINFO
    V$SGA_CURRENT_RESIZE_OPS
    V$SGA_RESIZE_OPS
    V$SGA_DYNAMIC_COMPONENTS
    V$SGA_DYNAMIC_FREE_MEMORY
    V$PGASTAT
    

| 
    
    
    information_schema.INNODB_CMPMEM_RESET
    information_schema.INNODB_CMPMEM
    performance_schema.memory_summary_by_account_by_event_name
    performance_schema.memory_summary_by_host_by_event_name
    performance_schema.memory_summary_by_thread_by_event_name
    performance_schema.memory_summary_by_user_by_event_name
    performance_schema.memory_summary_global_by_event_name
    performance_schema.replication_group_member_stats
    performance_schema.replication_group_members
    sys.memory_by_host_by_current_bytes
    sys.memory_by_thread_by_current_bytes
    sys.memory_by_user_by_current_bytes
    sys.memory_global_by_current_bytes
    sys.memory_global_total
      
  
### MySQL storage engines

Unlike many other RDBMS (including Oracle's), MySQL can work polymorphically due to its pluggable storage system. The MySQL pluggable storage engine architecture enables a database administrator to select a specialized storage engine for a particular application need.

The MySQL pluggable storage engine component in the MySQL database server is responsible for performing the data I/O operations, including storing the data into the disks or memory buffers. The pluggable storage engine architecture provides a standard set of management and support services that are common among all underlying storage engines.

From MySQL version 5.5 and higher, the default storage engine is the InnoDB storage engine, while InnoDB is also handling the temporary tables. You can configure storage engines during table `CREATE` or `ALTER`, as in the following example:
    
    
    mysql> SHOW CREATE TABLE JOBS \G;
    

The output is the following:
    
    
    *************************** 1. row ***************************
           Table: JOBS
    Create Table: CREATE TABLE `JOBS` (
      `JOB_ID` varchar(10) NOT NULL,
      `JOB_TITLE` varchar(35) NOT NULL,
      `MIN_SALARY` decimal(6,0) DEFAULT NULL,
      `MAX_SALARY` decimal(6,0) DEFAULT NULL,
      PRIMARY KEY (`JOB_ID`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    

For more information, see MySQL [different storage engines](https://dev.mysql.com/doc/refman/5.7/en/storage-engines.html).  
You can view the storage engine configuration by using the following query:
    
    
    mysql> SHOW VARIABLES LIKE '%storage%';
    

The output is similar to the following:
    
    
    +----------------------------------+--------+
    | Variable_name                    | Value  |
    +----------------------------------+--------+
    | default_storage_engine           | InnoDB |
    | default_tmp_storage_engine       | InnoDB |
    | disabled_storage_engines         |        |
    | enforce_storage_engine           | Innodb |
    | internal_tmp_disk_storage_engine | InnoDB |
    +----------------------------------+--------+
    

You can view all built-in storage engines:
    
    
    mysql> SHOW STORAGE ENGINES;
    

The output is similar to the following:
    
    
    +--------------------+---------+----------------------------------------------------------------+--------------+------+------------+
    | Engine             | Support | Comment                                                        | Transactions | XA   | Savepoints |
    +--------------------+---------+----------------------------------------------------------------+--------------+------+------------+
    | CSV                | YES     | CSV storage engine                                             | NO           | NO   | NO         |
    | PERFORMANCE_SCHEMA | YES     | Performance Schema                                             | NO           | NO   | NO         |
    | MRG_MYISAM         | YES     | Collection of identical MyISAM tables                          | NO           | NO   | NO         |
    | BLACKHOLE          | YES     | /dev/null storage engine (anything you write to it disappears) | NO           | NO   | NO         |
    | MyISAM             | YES     | MyISAM storage engine                                          | NO           | NO   | NO         |
    | FEDERATED          | NO      | Federated MySQL storage engine                                 | NULL         | NULL | NULL       |
    | MEMORY             | YES     | Hash based, stored in memory, useful for temporary tables      | NO           | NO   | NO         |
    | InnoDB             | DEFAULT | Supports transactions, row-level locking, and foreign keys     | YES          | YES  | YES        |
    +--------------------+---------+----------------------------------------------------------------+--------------+------+------------+
    

Note that InnoDB is the default storage engine, and is the only storage engine to support transactions (ACID compliant). Because InnoDB is the only storage engine that approximates Oracle functionality, we recommend that you use InnoDB at all times. Cloud SQL for MySQL [Second Generation](https://docs.cloud.google.com/sql/docs/mysql/1st-2nd-gen-differences#differences) supports only the InnoDB storage engine.

### System parameters

Both Oracle and Cloud SQL for MySQL databases can be specifically configured to achieve certain functionality beyond the default configuration. To alter configuration parameters in Oracle, certain administration permissions are required (primarily the `SYS/SYSTEM` user permissions).

Following is an example of altering the Oracle configuration by using the `ALTER SYSTEM` statement. In this example, the user changes the "maximum attempts for failed logins" parameter at the `spfile` configuration level only (with the modification valid only after after a reboot):
    
    
    SQL> ALTER SYSTEM SET SEC_MAX_FAILED_LOGIN_ATTEMPTS=2 SCOPE=spfile;
    

In the next example, the user is requesting to simply view the Oracle parameter value:
    
    
    SQL> SHOW PARAMETER SEC_MAX_FAILED_LOGIN_ATTEMPTS;
    

The output is similar to the following:
    
    
    NAME                                 TYPE        VALUE
    ------------------------------------ ----------- ------------------------------
    sec_max_failed_login_attempts        integer     2
    

The Oracle parameter modification works in three scopes:

  * **SPFILE** : Parameter modifications are written to the Oracle `spfile`, with an instance reboot required for the parameter to take effect.
  * **MEMORY** : Parameter modifications are applied in the memory layer only while no static parameter change is allowed.
  * **BOTH** : Parameter modifications are applied in both the server parameter file and in the instance memory, where no static parameter change is allowed.



#### Cloud SQL for MySQL configuration flags

You can modify the Cloud SQL for MySQL system parameters by using the [configuration flags](https://docs.cloud.google.com/sql/docs/mysql/flags) in the Google Cloud console, the gcloud CLI, or CURL. See the [complete list of all parameters](https://docs.cloud.google.com/sql/docs/mysql/flags#list-flags) supported by Cloud SQL for MySQL that you can alter.

MySQL parameters can be divided into several scopes:

  * **Dynamic parameters:** Can be altered at run time.
  * **Static parameters:** Require an instance reboot to take effect.
  * **Global parameters:** Will have a global effect on all current and future sessions.
  * **Session parameters:** Can be altered at the session level for the current session lifetime only, isolated from other sessions.



The Cloud SQL for MySQL memory parameter [`innodb_buffer_pool_size`](https://dev.mysql.com/doc/refman/5.7/en/innodb-parameters.html#sysvar_innodb_buffer_pool_size) (one of the crucial parameters to consider when planning and sizing a MySQL environment) is determined by the instance type and cannot be altered by using the configuration flags or by any other method—for example:

  * Instance type `db-n1-standard-1` has 1.4 GB of memory allocation.
  * Instance type `db-n1-highmem-8` has 38 GB of memory allocation.



#### Examples of altering Cloud SQL for MySQL parameters

### Console

Use the Google Cloud console to enable the `event_scheduler` parameter.

  1. Go to the **Edit instance** page of Cloud Storage.

[Go to Edit instance](https://console.cloud.google.com/sql/instances/)

  2. Under **Flags** , click **Add item** and search for `event_scheduler` as in the following screenshot.

![Edit the event scheduler instance in the console.](https://docs.cloud.google.com/static/solutions/images/migrating-oracle-users-mysql-event-scheduler.png)




### gcloud

  * Use the gcloud CLI to enable the `event_scheduler` parameter.:
        
        gcloud sql instances patch INSTANCE_NAME \
            --database-flags event_scheduler=on
        

The output is the following:
        
        WARNING: This patch modifies database flag values, which may require
        your instance to be restarted. Check the list of supported flags -
        /sql/docs/mysql/flags - to see if your
        instance will be restarted when this patch is submitted.
        
        Do you want to continue (Y/n)?
        




### MySQL session

Disable `AUTOCOMMIT` mode at the session level. This alteration stays in effect for the current session and holds for the session lifetime only.

  1. Show variables like `autocommit`:
         
         mysql> SHOW VARIABLES LIKE '%autoc%';
         

You see the following output, where `autocommit` is `ON`:
         
         +---------------+-------+
         | Variable_name | Value |
         +---------------+-------+
         | autocommit    | ON    |
         +---------------+-------+
         

  2. Disable `autocommit`:
         
         mysql> SET autocommit=off;
         

  3. Show variables like `autocommit`:
         
         mysql> SHOW VARIABLES LIKE '%autoc%';
         

You see the following output, where `autocommit` is `OFF`:
         
         +---------------+-------+
         | Variable_name | Value |
         +---------------+-------+
         | autocommit    | OFF   |
         +---------------+-------+
         




### Transactions and isolation levels

This section describes the main differences between Oracle and Cloud SQL for MySQL relevant to transaction and isolation level migrations.

#### Commit mode

Oracle works by default in non-autocommit mode, where each DML transaction must be determined with `COMMIT/ROLLBACK` statements. One of the fundamental differences between Oracle and MySQL is that MySQL works by default in autocommit mode, and each DML transaction is autocommitted with explicitly specifying the `COMMIT/ROLLBACK` statements.

To force MySQL to work in a non-autocommit mode, there are several options:

  * When managing transactions within the scope of stored procedures, use the `START TRANSACTION` clause to enter the same transactional mode same as Oracle.
  * Use the following statement to set the `autocommit` system parameter to `OFF` at the session level and explicitly use `COMMIT/ROLLBACK` statements in DML transactions:
        
        mysql> SET autocommit=off;
        




#### Isolation levels

The ANSI/ISO SQL standard (SQL92) defines four levels of isolation. Each level provides a different approach for handling concurrent execution of database transactions:

  * **Read Uncommitted:** A currently processed transaction can see uncommitted data made by the other transaction. If a rollback is performed, all data is restored to its previous state.
  * **Read Committed:** A transaction only sees data changes that were committed; uncommitted changes("dirty reads") are not possible.
  * **Repeatable Read:** A transaction can view changes made by the other transaction only after both transactions issued a `COMMIT` or both are rolled back.
  * **Serializable:** The strictest/strongest isolation level. This level locks all records that are accessed, and locks the resource so that records cannot be appended to the table.



Transaction isolation levels manage the visibility of changed data as seen by other running transactions. Also, when the same data is accessed by several concurrent transactions, the selected level of transaction isolation affects the way different transactions interact.

Oracle supports the following isolation levels:

  * Read Committed (default)
  * Serializable
  * Read-Only (not a part of the ANSI/ISO SQL standard (SQL92)



Oracle MVCC (Multiversion Concurrency Control):

  * Oracle uses the MVCC mechanism to provide automatic read consistency across the entire database and all sessions.
  * Oracle relies on the System Change Number (SCN) of the current transaction to obtain a consistent view of the database; therefore, all database queries only return data committed with respect to the SCN at the time of query execution.
  * Isolation levels can be changed at the transaction and session levels.



Here's an example of setting isolation levels:
    
    
    -- Transaction Level
    SQL> SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
    SQL> SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
    SQL> SET TRANSACTION READ ONLY;
    
    -- Session Level
    SQL> ALTER SESSION SET ISOLATION_LEVEL = SERIALIZABLE;
    SQL> ALTER SESSION SET ISOLATION_LEVEL = READ COMMITTED;
    

Cloud SQL for MySQL, like Oracle, supports the following four [transaction isolation levels](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_transaction_isolation) specified in the ANSI SQL:92 standard:

  * `READ UNCOMMITTED`
  * `READ COMMITTED`
  * `REPEATABLE READ (default)`
  * `SERIALIZABLE`



The Cloud SQL for MySQL default isolation level is `REPEATABLE READ`. Any new data will be available for both only after both transactions issue a `COMMIT` command. These isolation levels can be altered at `SESSION` level and at `GLOBAL` level ([global](https://docs.cloud.google.com/sql/docs/mysql/flags#mysql-i) level modification is currently in beta stage using configuration flags).

To verify current isolation levels both at `SESSION` and `GLOBAL` levels, use the following statement:
    
    
    mysql> SELECT @@GLOBAL.tx_isolation, @@tx_isolation;
    

The output is the following:
    
    
    +-----------------------+-----------------+
    | @@GLOBAL.tx_isolation | @@tx_isolation  |
    +-----------------------+-----------------+
    | REPEATABLE-READ       | REPEATABLE-READ |
    +-----------------------+-----------------+
    

You can modify the isolation level syntax as follows:
    
    
    SET [SESSION] TRANSACTION ISOLATION LEVEL [READ WRITE | READ ONLY]
    | REPEATABLE READ | READ COMMITTED | READ UNCOMMITTED | SERIALIZABLE]
    

And you can modify the isolation level at `SESSION` level:
    
    
    mysql> SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
    
           -- Verify
    
    mysql> SELECT @@GLOBAL.tx_isolation, @@tx_isolation;
    

The output is the following:
    
    
    +-----------------------+------------------+
    | @@GLOBAL.tx_isolation | @@tx_isolation   |
    +-----------------------+------------------+
    | REPEATABLE-READ       | READ-UNCOMMITTED |
    +-----------------------+------------------+
    

#### Cloud SQL for MySQL transactions structure

[Transactions](https://dev.mysql.com/doc/refman/5.7/en/commit.html) syntax:
    
    
    START TRANSACTION
        [transaction_characteristic [, transaction_characteristic] ...]
      
    
    transaction_characteristic: {
        WITH CONSISTENT SNAPSHOT
      | READ WRITE
      | READ ONLY
    }
      
    
    BEGIN [WORK]
    COMMIT [WORK] [AND [NO] CHAIN] [[NO] RELEASE]
    ROLLBACK [WORK] [AND [NO] CHAIN] [[NO] RELEASE]
    SET autocommit = {0 | 1}
      
  
---  
  
Transactions can be implemented with `START TRANSACTION` or `BEGIN`.

The `WITH CONSISTENT SNAPSHOT` option starts a consistent `READ` transaction, which is effectively the same as issuing a `START TRANSACTION`, followed by a `SELECT` from any table. The `WITH CONSISTENT SNAPSHOT` clause that starts a consistent `READ` (a `READ` operation that uses snapshot information to present query results based on a point in time) does not change the transaction isolation level and is supported only by the `REPEATABLE READ` isolation level.

A consistent `READ` uses snapshot information to make query results available based on a point-in-time, regardless of modifications performed by concurrent transactions. If queried data has been changed by another transaction, the original data is reconstructed using the undo log. This will assist avoiding locking issues that may reduce concurrency.

With `REPEATABLE READ` isolation level, the snapshot is based on the time the first `READ` operation is performed. With the `READ COMMITTED` isolation level, the snapshot is reset to the time of each consistent `READ` operation.

Here's an example of transaction and isolation level setting:
    
    
    mysql> SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
    mysql> START TRANSACTION;
    mysql> INSERT INTO tbl1 VALUES (1, 'A');
    mysql> UPDATE tbl2 SET col1 = 'Done' WHERE KeyColumn = 1;
    mysql> COMMIT;
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
