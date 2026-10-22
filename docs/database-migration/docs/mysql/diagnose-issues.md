---
url: https://docs.cloud.google.com/database-migration/docs/mysql/diagnose-issues/
title: Diagnose issues for MySQL \u00a0|\u00a0 Database Migration Service for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:05.338146+00:00
---

# Diagnose issues for MySQL  |  Database Migration Service for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/mysql/diagnose-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview)



Send feedback 

#  Diagnose issues for MySQL Stay organized with collections  Save and categorize content based on your preferences. 

The migration job process might incur errors during runtime.

  * Some errors, such as a bad password on the source database, are recoverable, meaning they can be fixed and the migration job resumes automatically.
  * Some are unrecoverable, such as a lost binlog position, meaning the migration job needs to be restarted from the beginning.



When an error occurs, the migration job status changes to `Failed`, and the substatus reflects the last status before failure.

To troubleshoot an error, navigate to the failed migration job to view the error and follow the steps outlined in the error message.

To view more details about the error, navigate to Cloud Monitoring using the link on the migration job. The logs are filtered to the specific migration job.

In the following table, you can find some examples of issues and how they can be solved:

For this problem... | The issue might be... | Try this...  
---|---|---  
Destination database settings are different from the Terraform configuration used to provision the database. (This issue is also sometimes referred to as _configuration drift_.) | When you migrate to an [ existing destination database](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job-existing-instance), Database Migration Service modifies certain settings of your destination database to execute the migration job. | You need to re-apply the settings you use in your Terraform configuration after you promote the migration job. See Terraform configuration drift.  
Error message: `Error processing table {table_name}: MySQL Error 1118 (42000): Row size too large (>8126).` | Tables that use `VARCHAR` columns might have rows that exceed the maximum size allowed by [InnoDB](https://dev.mysql.com/doc/refman/8.0/en/innodb-introduction.html) (the default storage engine used in MySQL). | You can unblock your migration job by converting columns to BLOB or TEXT, or by temporarily setting the [`innodb_strict_mode`](https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_strict_mode) flag to `off`. See Error 1118: row size too large.  
Migration job failed during the initial dump phase with the following error message:  
`ERROR 1064 (42000) at {line_number}: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near {reserved_word} at {line_number}.` |  This issue occurs when migrating between MySQL versions. Entities in your source MySQL version might be using words that are not allowed in the MySQL version you want to migrate to. For example, in MySQL 5.7 you can use the word `function` in column names. But in MySQL 8.0, [`function` is a reserved word](https://dev.mysql.com/doc/refman/8.0/en/keywords.html#keywords-new-8-0-F), so the destination database can't parse your sources. |  Rename your source database objects referenced in the error message or put them in backticks (````) to escape the syntax. When complete, retry the migration job.   
Error message: `ERROR 1109 (42S02): Unknown table in _< schema name here>_` | Database Migration Service doesn't migrate the `mysql`, `performance_schema`, `information_schema`, `ndbinfo`, or `sys` system schemas.  Your migration job might fail if the source database contains objects that reference tables from any of these schemas.  |  Check your source database for objects that reference tables contained in any of the system schemas that aren't migrated. See ERROR 1109 (42S02): Unknown table in _< schema name here>_.   
Error message: `Unknown table 'COLUMN_STATISTICS' in information_schema (1109)` | Relevant for manual database dump scenarios with `mysqldump` only.  
MySQL databases in versions earlier than 8 don't have the [COLUMN_STATISTICS](https://dev.mysql.com/doc/refman/8.0/en/information-schema-column-statistics-table.html) table. The `mysqldump` utility in versions 8 and later tries to export this table by default. The export fails because the column doesn't exist. | Use the `--column-statistics=0` flag when using `mysqldump`.  
Error message: `Specified key was too long; max key length is 767 bytes`. | The source database instance may have the variable `innodb_large_prefix` set. | Set the `innodb_large_prefix` flag to `ON` when creating the destination instance, or update the existing destination instance with the flag.  
Error message: `Table definition has changed`. | There were data definition language (DDL) changes during the dump process. | Avoid DDL changes during the dump process.  
Error message: `While 'Loading data': Dump timeout`. | A connectivity issue might be causing the timeout. | Verify network connection with your source database. For sample guidance, see [Debugging connectivity](https://docs.cloud.google.com/database-migration/docs/mysql/debugging-connectivity).   
If there were data definition language (DDL) changes performed during the dump process, Database Migration Service might be stuck due to a metadata lock.  | Investigate your source database to check for processes stuck in the `Waiting for table metadata lock` state. If you find processes with that status, we recommend that you restart the migration job. Don't perform DDL changes during the full dump phase after the restart. You can use a [ sample script to verify that DDL operations are stopped](https://docs.cloud.google.com/database-migration/docs/mysql/debugging-tools#alter-table).   
`MySQL Error 2013: (HY000): Lost connection to MySQL server during query` | A connectivity issue might be causing the timeout. | Verify network connection with your source database. For sample guidance, see [Debugging connectivity](https://docs.cloud.google.com/database-migration/docs/mysql/debugging-connectivity).   
If there were data definition language (DDL) changes performed during the dump process, Database Migration Service might be stuck in a metadata lock.  | Investigate your source database to check for processes stuck in the `Waiting for table metadata lock` state. If you find processes with that status, we recommend that you restart the migration job. Don't perform DDL changes during the full dump phase after the restart. You can use a [ sample script to verify that DDL operations are stopped](https://docs.cloud.google.com/database-migration/docs/mysql/debugging-tools#alter-table).   
Error message: `Timeout waiting for no write traffic on source: context deadline exceeded`. | A connectivity issue might be causing the timeout. | Verify network connection with your source database. For sample guidance, see [Debugging connectivity](https://docs.cloud.google.com/database-migration/docs/mysql/debugging-connectivity).   
If there were data definition language (DDL) changes performed during the dump process, Database Migration Service might be stuck in a metadata lock.  | Investigate your source database to check for processes stuck in the `Waiting for table metadata lock` state. If you find processes with that status, we recommend that you restart the migration job. Don't perform DDL changes during the full dump phase after the restart. You can use a [ sample script to verify that DDL operations are stopped](https://docs.cloud.google.com/database-migration/docs/mysql/debugging-tools#alter-table).   
Error message: `Access denied; you need (at least one of) the SUPER privilege(s) for this operation`. | There could be an event, a view, a function, or a procedure in the source database using super user@localhost (such as root@localhost). This is not supported by Cloud SQL. | See [more information](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer) about `DEFINER` usage in Cloud SQL.  
Error message: `Definer user 'x' does not exist. Please create the user on the replica. ` | The user doesn't exist on the replica. | See [more information](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer) about `DEFINER` usage in Cloud SQL.  
Error message: `ERROR 1045 (28000) at line {line_number}: Access denied for user 'cloudsqlimport'@'localhost`. | There is a `DEFINER` in the source database that doesn't exist in the replica. | See [more information](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer) about `DEFINER` usage in Cloud SQL.  
Error message: `Lost connection to MySQL server during query when dumping table`. | The source database may have become unreachable, or the dump contained packets too large. | Try these suggestions.  
Error message: `Got packet bigger than 'max_allowed_packet' bytes when dumping table`. | The packet was larger than allowed by settings. | Use manual dump with the `max_allowed_packet` option.  
Initial data migration was successful, but no data is being replicated. | There may be conflicting replication flags. | Check these flag settings.  
Initial data migration was successful, but data replication stopped working after a while. | There could be many causes. | Try these suggestions.  
Error message: `mysqld check failed: data disk is full`. | The data disk of the destination instance is full. | Increase the disk size of the destination instance. You can either manually increase the disk size or enable auto storage increase.  
Failure connecting to the source database instance.  | There was a connectivity issue between the source database instance and the destination instance. | Follow the steps in the [debugging connectivity](https://docs.cloud.google.com/database-migration/docs/mysql/debugging-connectivity) article.  
Migration from a managed database (Amazon RDS/Aurora) doesn't start.  | Migrating from a managed source database without SUPERUSER privileges requires a brief downtime in the beginning of the migration. | Follow the steps in [this](https://docs.cloud.google.com/database-migration/docs/mysql/configure-source-database#aws-rds-mysql) article.   
Binlog is configured incorrectly on the source database.  | The Binlog definitions are incorrect. | For continuous MySQL migration jobs, make sure you follow the [required binlog definitions](https://docs.cloud.google.com/database-migration/docs/mysql/configure-source-database-continuous).  
Failure to find the dump file.  | DMS is unable to find the dump file provided. | This can happen if the migration job can't find the dump file at the given location.  


  1. Check the dump path to ensure a proper file is there, or change the path.
  2. If you change the path, then use a `PATCH` request to ensure the job uses it.
  3. Restart the migration job.

  
Unable to resume replication as binlog position was lost.  | The binlog position was lost and the migration job couldn't be resumed. | This error can occur when the replication process is paused for a long time, which causes the binlog position to be lost. Migration jobs shouldn't be paused for periods of time that approach the binlog retention period. Restart the migration job.  
When you migrate to [ an existing destination instance](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job-existing-instance), you receive the following error message: `The destination instance contains existing data or user defined entities (for example databases, tables, or functions). You can only migrate to empty instances. Clear your destination instance and retry the migration job.` | Your destination Cloud SQL instance contains extra data. You can only migrate to existing instances that are empty. See [Known limitations](https://docs.cloud.google.com/database-migration/docs/mysql/known-limitations#existing-instance-limitations). | Promote your destination instance to make it a read/write instance, remove the extra data, and re-try the migration job. See Clear extra data from your existing destination instance.   
Failure running migration job due to incompatible source and destination database versions.  | The source database version provided is incompatible with the destination database version. | Make sure that the [destination database version](https://docs.cloud.google.com/database-migration/docs/mysql/migration-src-and-dest) is the same or one major version above the source destination version, then create a new migration job.  
Error Message: `Unable to connect to source database server.` | Database Migration Service can't establish a connection to the source database server. | Make sure that the source and destination database instances can communicate with each other, and that you've completed all of the required prerequsities that appeared when you [defined your settings for the migration job](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job#src).  
Error Message: `Timeout waiting for no write traffic on source.` | Migrating from a managed source database without `SUPERUSER` privileges results in a brief downtime during the beginning of the migration. | Follow the steps in [Migrating from RDS MySQL without SUPERUSER privileges](https://docs.cloud.google.com/database-migration/docs/mysql/configure-source-database#aws-rds-mysql).  
Error Message: `ERROR 1146 (42S02) at line {line_number}: Table '{table_name}' doesn't exist.` | There might be an inconsistency between the value of the [`lower_case_table_names`](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_lower_case_table_names) flag for the source database and the value of the flag for the destination Cloud SQL instance. | Set the value of the [flag](https://docs.cloud.google.com/sql/docs/mysql/flags) for the Cloud SQL instance to match the value of the flag for the source database.  
Error Message: `ERROR 1109 (42S02) at line {line_number}: Unknown table '{table}' in {database}.` | Some objects on the source database, such as views, functions, stored procedures, or triggers, reference a table that no longer exists on the database. | Check to see if these objects exist. If they do, then either drop the objects from the source database or add the table that the objects are referencing to the source database.  
Error Message: `ERROR 1045: Access denied for user '{user_name}'@'{replica_IP}' (using password: YES)". Check if MySQL replication user and password are correct. Not attempting further retries.` | You provided an incorrect password for the source instance. Or, the source instance forces an SSL connection; however, the migration job isn't configured to use SSL certifications. | Confirm whether the username, password, and SSL settings are correct for the source instance by [using the `mysql` client](https://dev.mysql.com/doc/refman/8.0/en/mysql.html). If the source instance is Cloud SQL, then see [Requiring SSL/TLS](https://docs.cloud.google.com/sql/docs/mysql/configure-ssl-instance#enforcing-ssl) to verify whether SSL/TLS is required for TCP connections.  
The replication lag is consistently high. |  The write load is too high for the replica to handle. Replication lag takes place when the Cloud SQL for MySQL thread on a replica can't keep up with the I/O thread. Some types of queries or workloads can cause a temporary or permanent high replication lag for a given schema. Some typical causes of replication lag are: 

  * Slow queries are performed on the replica. Find and fix them.
  * It is highly recommended that all tables have a unique, primary key. Every update on a table that doesn't have this key causes full table scans on the replica, leading to replication delays.
  * Queries such as `DELETE ... WHERE field < 50000000` cause replication lag with row-based replication because a huge number of updates are piled up on the replica.

| Some possible solutions include: 

  * [Configure parallel replication](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#configuring-parallel-replication) if the replica is MySQL version 5.7 (or above).
  * Set the [`innodb_flush_log_at_trx_commit`](https://docs.cloud.google.com/sql/docs/mysql/flags#tips-flush-log) flag on the replica to 2. See [Tips for working with flags](https://docs.cloud.google.com/sql/docs/mysql/flags#tips) for more information about this flag.
  * [Edit the Cloud SQL for MySQL instance](https://docs.cloud.google.com/sql/docs/mysql/edit-instance#editing_an_instance) to increase the size of the replica.
  * Reduce the load on the source database.
  * [Index tables](https://docs.cloud.google.com/sql/docs/mysql/replication/read-replica-indexes) on the replica for any tables that don't have primary, unique keys.
  * Index tables on the source database. This requires restarting the migration job.
  * Identify and fix slow queries on the source database.

| Error Message: `'Character set '#255' is not a compiled character set and is not specified in the '/usr/share/mysql/charsets/Index.xml' file' on query.` | The source database may use characters sets or collations that aren't supported by the selected Cloud SQL replica. One example is AWS Aurora version 2.x, which is compatible with MySQL 5.7. However, this version supports the `utf8mb4_0900_as_ci` collation, which isn't supported in Cloud SQL for MySQL 5.7. | 

  * If the migration fails during the full dump phase, then check the source table definition if unsupported characters sets or collations are used. If possible, then update to supported character sets or collations.
  * If the migration fails during the CDC phase, then check the [replica status](https://dev.mysql.com/doc/refman/8.0/en/show-replica-status.html), find the binlog that causes the migration to fail, and examine the source database and application to locate the SQL statements that use the character sets or collations. If possible, then update to supported character sets or collations.

  
  
### Error 1108: row size too large

Tables with columns that store variable-length strings can have rows that exceed the [default InnoDB maximum row size](https://dev.mysql.com/doc/refman/8.0/en/innodb-limits.html). 

#### Things to try

##### Adjust source table schema

This issue can reoccur whenever you perform any INSERT statements into the tables that exceed the maximum size row limit. To avoid future problems, it's best if you adjust your tables before you retry the migration:

  * Change your table [`ROW_FORMAT`](https://dev.mysql.com/doc/refman/8.0/en/innodb-row-format.html) to `DYNAMIC` or `COMPRESSED` by executing the following query: 
        
        ALTER TABLE TABLE_NAME ROW_FORMAT=FORMAT_NAME;
          

Where: 
    * TABLE_NAME is the name of the table whose rows exceed the maximum row size limit
    * FORMAT_NAME is `DYNAMIC` or `COMPRESSED`
For example: 
    
    ALTER TABLE mytable ROW_FORMAT=DYNAMIC;
      

  * Convert row data to BLOB or TEXT. One way you can achieve this operation is with the [`CONVERT()` function](https://dev.mysql.com/doc/refman/8.0/en/cast-functions.html#function_convert). 



##### Disable InnoDB strict mode

If it's not possible for you to adjust the source table schema, you can temporarily disable InnoDB validation to complete the migration job. Keep in mind that the issue can reoccur during future database write attempts, so it's best to adjust your table schema when feasible.

To temporarily disable InnoDB validation for the purposes of completing your migration job, follow these steps:

**If...**| **Then...**  
---|---  
If you migrate to a new destination instance | 

  1. [Re-create your migration job](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job).
  2. At the end of the **Define a destination** step, click **Show optional configurations**.
  3. In the **Flags** section, select the `innodb_strict_mode` flag and set it to `Off`.
  4. After your migration is complete, set the `innodb_strict_mode` flag to `On`. See [Configure database flags](https://docs.cloud.google.com/sql/docs/mysql/flags) in Cloud SQL for MySQL documentation.

  
If you migrate to an existing destination instance | 

  1. In Cloud SQL, navigate to your destination instance and set the `innodb_strict_mode` flag to `Off`. See [Configure database flags](https://docs.cloud.google.com/sql/docs/mysql/flags) in Cloud SQL for MySQL documentation. 
  2. [ Re-create your migration job](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job-existing-instance).
  3. After your migration is complete, set the `innodb_strict_mode` flag to `On`. See [Configure database flags](https://docs.cloud.google.com/sql/docs/mysql/flags) in Cloud SQL for MySQL documentation.

  
  
* * *

### Clear extra data from your existing destination instance

When you migrate to [ an existing destination instance](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job-existing-instance), you receive the following error message: `The destination instance contains existing data or user defined entities (for example databases, tables, or functions). You can only migrate to empty instances. Clear your destination instance and retry the migration job.`

This issue can occur if your destination instance contains extra data. You can only migrate to existing instances that are empty. See [Known limitations](https://docs.cloud.google.com/database-migration/docs/mysql/known-limitations#existing-instance-limitations).

#### Things to try

Clear extra data from your destination instance and start the migration job again by performing the following steps:

  1. [Stop the migration job](https://docs.cloud.google.com/database-migration/docs/mysql/migration-job-actions).
  2. At this point, your destination Cloud SQL instance is in `read-only` mode. [Promote the destination instance](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external#promote_the_replica) to gain write access. 
  3. [Connect to your destination Cloud SQL instance](https://docs.cloud.google.com/sql/docs/mysql/connect-overview).
  4. Remove extra data from your destination instance databases. Your destination can only contain system configuration data. Destination databases can't contain user data (such as tables). There are different SQL statements you can run on your databases to find non-system data, for example: 
         
         SELECT schema_name FROM information_schema.SCHEMATA
         WHERE schema_name NOT IN ('information_schema', 'sys', 'performance_schema', 'mysql');
           

  5. [Start the migration job](https://docs.cloud.google.com/database-migration/docs/mysql/migration-job-actions).



* * *

### Terraform configuration drift

When you migrate to an [ existing destination database](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job-existing-instance), Database Migration Service modifies certain settings of your destination database to execute the migration job. For databases provisioned with Terraform, this interaction might cause a configuration drift where the actual destination database configuration is different from the configuration set in your Terraform files. 

#### Things to try

Don't attempt to re-apply Terraform configuration when the migration job is running. You can safely adjust the necessary configuration after your destination database is promoted. Database Migration Service performs the following modifications to your destination Cloud SQL instance: 

  * [Backup configuration](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups) is set to default values.
  * [Point-in-time recovery](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restore#tips-pitr) is reset to default values.

You can expect configuration drift to occur if your Terraform configuration contains settings for any of these features. If you need to correct the destination database configuration, wait until the migration job completes and your destination database is promoted. Then, perform the following steps: 1\. Run the `terraform plan` command to see the preview of your modifications. 1\. Run the `terraform apply` command to re-adjust your destination database settings. 

* * *

### ERROR 1109 (42S02): Unknown table in _< schema name here>_

Migration jobs fail with the following message: `ERROR 1109 (42S02): Unknown table in _< schema name here>_ `, for example: `ERROR 1109 (42S02) at line X: Unknown table 'GLOBAL_STATUS' in information_schema`.

#### The issue might be

Database Migration Service doesn't migrate the `mysql`, `performance_schema`, `information_schema`, `ndbinfo`, or `sys` system schemas (see [Known limitations](https://docs.cloud.google.com/database-migration/docs/mysql/known-limitations)). Your migration job might fail if the source database contains objects that reference tables from any of these schemas.

#### Things to try

Check your source database for objects that reference tables from the system schemas. On your source database, execute the following queries: 
    
    
    # Query to check routines or functions definitions.
    SELECT ROUTINE_SCHEMA, ROUTINE_NAME FROM information_schema.routines
    WHERE ROUTINE_SCHEMA NOT IN ('information_schema', 'mysql', 'ndbinfo', 'performance_schema', 'sys')
    AND ROUTINE_DEFINITION like '%OBJECT_NAME_REPORTED_IN_THE_ERROR_MESSAGE%'
    
    # Query to check view definitions.
    SELECT TABLE_SCHEMA, TABLE_NAME FROM information_schema.views
    WHERE TABLE_SCHEMA NOT IN ('information_schema', 'mysql', 'ndbinfo', 'performance_schema', 'sys')
    AND view_definition like '%OBJECT_NAME_REPORTED_IN_THE_ERROR_MESSAGE%'
    
    # Query to check trigger definitions.
    SELECT TRIGGER_SCHEMA, TRIGGER_NAME FROM information_schema.TRIGGERS
    WHERE TRIGGER_SCHEMA NOT IN ('information_schema', 'mysql', 'ndbinfo', 'performance_schema', 'sys')
    AND event_object_table = 'OBJECT_NAME_REPORTED_IN_THE_ERROR_MESSAGE'
    
    # Query to check constraint definitions.
    SELECT TABLE_SCHEMA, TABLE_NAME
    FROM information_schema.KEY_COLUMN_USAGE
    WHERE TABLE_SCHEMA NOT IN ('information_schema', 'mysql', 'ndbinfo', 'performance_schema', 'sys')
    AND REFERENCED_TABLE_NAME = 'OBJECT_NAME_REPORTED_IN_THE_ERROR_MESSAGE'

If these queries return any results, consider deleting the relevant code objects and perform the migration again. 

* * *

### Unknown table 'COLUMN_STATISTICS' in information_schema

When running the `mysqldump` utility version 8 or later to export a MySQL database version earlier than 8, you encounter this error: `Unknown table 'COLUMN_STATISTICS' in information_schema (1109)`.

#### The issue might be

MySQL databases in versions earlier than 8 don't have the [COLUMN_STATISTICS](https://dev.mysql.com/doc/refman/8.0/en/information-schema-column-statistics-table.html) table. The `mysqldump` utility in versions 8 and later try to export this table by default. The export fails because the column doesn't exist.

#### Things to try

Add the `--column-statistics=0` flag to your `mysqldump` command to remove the `COLUMN_STATISTICS` table from the export. For more information, see [Exporting a MySQL database using mysqldump](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-dump).

* * *

### Specified key was too long; max key length is 767 bytes

You see the error `Specified key was too long; max key length is 767 bytes.`

#### The issue might be

The source database may have the variable **innodb_large_prefix** set. This allows index key prefixes longer than 767 bytes. The default value is `OFF` for MySQL 5.6.

#### Things to try

Set the `innodb_large_prefix` flag to `ON` when creating the destination database, or update the existing destination database with the flag.

* * *

### Table definition has changed

You see the error `Table definition has changed`.

#### The issue might be

There were DDL changes during the dump process.

#### Things to try

Don't modify tables or perform any other DDL changes during the dump process.You can use a [script](https://docs.cloud.google.com/database-migration/docs/mysql/debugging-tools#alter-table) to verify that DDL operations are stopped.

* * *

### Access denied; you need (at least one of) the SUPER privilege(s) for this operation

You see the error `Access denied; you need (at least one of) the SUPER privilege(s) for this operation`.

#### The issue might be

There could be an event, a view, a function, or a procedure in the source database using super user@localhost (such as root@localhost). This is not supported by Cloud SQL.

#### Things to try

Refer to [this](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer) document on migrating a database with `DEFINER` clauses.

* * *

### Error message: `Definer user 'x' does not exist. Please create the user on the replica.`

You see the error `Definer user 'x' does not exist. Please create the user on the replica.`

#### The issue might be

The root cause is that a user in the source database with the `DEFINER` clause doesn't exist on the replica database.

#### Things to try

Refer to [this](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer) document on migrating a database with `DEFINER` clauses. You may need to create the user in the replica database.

* * *

### Error message: `ERROR 1045 (28000) at line {line_number}: Access denied for user 'cloudsqlimport'@'localhost`

You see the error `ERROR 1045 (28000) at line {line_number}: Access denied for user 'cloudsqlimport'@'localhost`.

#### The issue might be

The root cause is that a user in the source database with the `DEFINER` clause doesn't exist on the replica database and that user is cross-referenced in the object definitions in the source database.

#### Things to try

Refer to [this](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer) document on migrating a database with `DEFINER` clauses. You may need to create one or more users in the replica database.

* * *

### Lost connection to MySQL server during query when dumping table

You see the error `Lost connection to MySQL server during query when dumping table`.

#### The issue might be

  * The source database instance may have become unreachable from the destination instance.
  * The source database may have tables with large blobs or long strings which require setting the `max_allowed_packet` to a larger number on the source database.



#### Things to try

  * Verify the source database instance is up and reachable.
  * [Configure the `max-allowed-packet` flag in the migration job](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job#specify-source-connection-profile-info), and then restart the migration job. Or, generate a [manual dump](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-dump) with the `max_allowed_packet` option to dump the data and migrate with the dump file. 
  * Increasing `max_allowed_packet`, will most likely require tweaking the `net_read_timeout` and `net_write_timeout` settings on the source database (generally it should be increased till the connection error stops).



* * *

### Got packet bigger than 'max_allowed_packet' bytes when dumping table

You see the error `Got packet bigger than 'max_allowed_packet' bytes when dumping table`.

#### The issue might be

The packet was larger than allowed by settings.

#### Things to try

Create a migration job using a [manual dump](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-dump) with the `max_allowed_packet` option to dump the data and migrate with the dump file.

* * *

### No data is being replicated

Initial data migration was successful, but no data is being replicated.

#### The issue might be

A possible root cause could be your source database has replication flags which result in some or all database changes not being replicated over.

#### Things to try

Make sure the replication flags such as `binlog-do-db`, `binlog-ignore-db`, `replicate-do-db` or `replicate-ignore-db` are not set in a conflicting way.  
Run the command `show master status` on the source database to see the current settings.

* * *

### Initial data migration was successful but data replication stopped working after a while

The initial data migration was successful but data replication stopped working after a while.

#### The issue might be

There can be many root causes for this issue.

#### Things to try

  * Check the [replication metrics](https://console.cloud.google.com/monitoring/dashboards/resourceList/cloudsql_database) for your destination instance in the Cloud Monitoring.
  * The errors from the MySQL IO thread or SQL thread can be found in [Cloud Logging](https://console.cloud.google.com/logs) in the mysql.err log files.
  * The error can also be found when connecting to the destination instance. Run the command `SHOW REPLICA STATUS`, and check for these fields in the output:
    * Replica_IO_Running
    * Replica_SQL_Running
    * Last_IO_Error
    * Last_SQL_Error

**Note:** The `SHOW REPLICA STATUS` is an alias introduced in MySQL 8.0.22. For previous versions (MySQL 5.7, MySQL 8.0), use the old alias of the status command. For more information, see [Status statement](https://dev.mysql.com/doc/refman/8.0/en/show-slave-status.html) in MySQL documentation.

If you got the error `fatal error 1236 from master when reading data from binary log: 'Could not find first log file name in binary log index file' in Last_IO_Error`, this could be due to insufficient binlog retention setting on source instance.

If you got the error `error connecting to master 'USER_NAME@SOURCE_HOST:SOURCE_PORT' - retry-time: RETRY_TIME retries: RETRIES`, this could be due to the destination instance failing to reconnect to the source because of a connectivity or authentication issue.




* * *

### mysqld check failed: data disk is full

You see the error `mysqld check failed: data disk is full`.

#### The issue might be

The data disk of the destination instance is probably full.

#### Things to try

Increase the disk size of the destination instance.

* * *

### Failure connecting to source database

Failure connecting to source database.

#### The issue might be

There was a connectivity issue between the source database instance and the destination instance.

#### Things to try

Follow the steps in the [debugging connectivity article](https://docs.cloud.google.com/database-migration/docs/mysql/debugging-connectivity).

* * *

### Migration from a managed database (Amazon RDS/Aurora) doesn't start

The migration job fails to start.

#### The issue might be

Migrating from a managed source database without `SUPERUSER` privileges requires a brief downtime in the beginning of the migration.

#### Things to try

  * For Amazon RDS, follow the steps in [this article](https://docs.cloud.google.com/database-migration/docs/mysql/configure-source-database#aws-rds-mysql).
  * For Amazon Aurora, follow the steps in [this article](https://docs.cloud.google.com/database-migration/docs/mysql/configure-source-database#aws-aurora-mysql).



* * *

### Binlog is configured incorrectly on the source database

You see an error indicating a problem with the binary logs.

#### The issue might be

This can happen for continuous MySQL migration jobs if the binlog configuration is incorrect on the source database.

#### Things to try

Make sure you follow the steps on the [here](https://docs.cloud.google.com/database-migration/docs/mysql/configure-source-database-continuous). 

* * *

### Failure reading the provided dump file

You see an error indicating a problem with the dump file.

#### The issue might be

DMS is unable to find the dump file provided.

#### Things to try

  1. Check the dump path to ensure a proper file is there, or change the path
  2. If you change the path, then use a `[PATCH](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/patch)` request to ensure the job uses it.
  3. Restart the migration job.



* * *

### Unable to resume replication as binlog position was lost

The binlog position is lost.

#### The issue might be

This error can occur when the replication process is paused for a long time, which causes the binlog position to be lost. Migration jobs shouldn't be paused for periods of time that approach the binlog retention period. 

#### Things to try

Restart the migration job.

* * *

### Failure running migration job due to incompatible source and destination database versions

The source and destination database versions are not a supported combination.

#### The issue might be

The source database version provided is incompatible with the destination database version.

#### Things to try

Make sure that the [destination database version](https://docs.cloud.google.com/database-migration/docs/mysql/migration-src-and-dest) is the same or one major version above the source destination version, then create a new migration job.

* * *

### Can't connect to the source database server

You see the error `Unable to connect to source database server`.

#### The issue might be

Database Migration Service can't establish a connection to the source database server.

#### Things to try

Verify that the source and destination database instances can communicate with each other. Then, make sure that you've completed all of the required prerequisites that appeared when you [defined the settings for your migration job](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job#src).

* * *

### Cloud SQL destination instance disk usage drops to zero

The disk usage suddenly drops to zero during migration.

#### The issue might be

There may be a failure when importing the initial data. When this happens, the migration process tries to perform another load of the data. This process first wipes out existing data on the destination instance (This is why you see the disk usage going down to zero.), and then tries to reload the data.

#### Things to try

Go to the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), and select your destination instance from the resource list. Look for a similar log message: `DUMP_STAGE(RETRY): Attempt .../...: import failed: error..."; Clearing database and trying again."` Find the message after the `import failed:` text and try to resolve the underlying issue.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
