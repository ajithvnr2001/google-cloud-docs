---
url: https://docs.cloud.google.com/sql/docs/mysql/orphan-tables/
title: Orphan tables \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:09.637924+00:00
---

# Orphan tables  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/orphan-tables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Orphan tables Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This page discusses known issues with [orphan tables](https://dev.mysql.com/doc/refman/5.7/en/innodb-troubleshooting-datadict.html) in MySQL.

## What are orphan tables?

Orphan tables are tables with disconnected definitions across MySQL data dictionaries and can occur in MySQL 5.6 or MySQL 5.7. Either of the following scenarios can block a major version upgrade (MVU) from MySQL 5.7 to MySQL 8.0:

  * The presence of `InnoDB` data files (`.ibd`) without corresponding definition files (`.frm`), or the other way around.
  * The presence of intermediate tables left over from `ALTER TABLE` statements that are no longer referenced or used by any active application logic.



## Orphan temporary tables

Orphan temporary table names start with the `#sql-` prefix, such as `#sql-123`.

Use the following query to help identify orphan temporary (temp) tables:
    
    
    SELECT * FROM INFORMATION_SCHEMA.INNODB_SYS_TABLES WHERE NAME RLIKE '#sql-[0-9].*';
    

You can use the `DROP TABLE` command to drop orphan temporary tables without any other additional steps. This addresses most cases:

**Note:** To run the command, make sure you have `DROP` privileges.
    
    
    DROP TABLE `DB`.`#mysql50#TEMPORARY_ORPHAN_TABLE`;
    

Replace `DB` with the database name you want to use.

An example might look like the following:
    
    
    DROP TABLE `testdb`.`#mysql50##sql-1234`;
    

**Note:** Use `#mysql50#` to ignore filename-safe encoding in MySQL.

If the previous `DROP` table command doesn't work, then the definition file (`.frm`) might be reused by another `ALTER TABLE` operation. In such cases, a placeholder `.frm` file needs to be created on disk to remove the table. Contact [Cloud SQL support](https://docs.cloud.google.com/sql/docs/mysql/getting-support) for assistance. If you don't have a support contract, see Self-serve methods for troubleshooting steps.

## Orphan intermediate tables

Orphan intermediate table names start with the `#sql-ib` prefix, for example, `#sql-ib23-343224`.

Use the following query to identify orphan intermediate tables:
    
    
    SELECT * FROM INFORMATION_SCHEMA.INNODB_SYS_TABLES WHERE NAME LIKE '%#sql-ib%';
    

To remove intermediate orphan tables, first change the orphan definition filename (`.frm`) to match the table name, and then drop the table from the command line.

To remove intermediate orphan tables, contact the Cloud SQL support team for assistance. If you don't have a support contract, then see Self-serve methods for troubleshooting steps.

## Orphan normal tables

An orphan `InnoDB` table occurs when its corresponding data file (`.ibd`) file remains in the file system, but the data dictionary no longer references the data file correctly. This scenario requires manual intervention.

To resolve this issue, contact Cloud SQL support. The support team can create a placeholder `.frm` file, and then use a `DROP TABLE` command to try to remove the table. If unsuccessful, the `InnoDB` (`.ibd`) file likely requires manual removal from the data directory.

After the file is manually removed, you can back up all tables and database structures.

Drop a database using `DROP DATABASE` and create a database using `CREATE DATABASE`. This last step might require downtime for applications connected to the affected database.

If you don't have a support contract, see Self-serve methods for troubleshooting steps.

## Self-service troubleshooting

The following self-service troubleshooting methods involve dropping or migrating the entire database to remove the orphan tables when dropping an individual table doesn't work. This method is disruptive. If your organization is under a support contract, then we highly recommend contacting Cloud SQL support team for assistance.

To remove orphan temporary tables, make sure to follow the steps in Orphan temporary tables first. If the `DROP TABLE` command is unsuccessful, then try the following suggestions.

### Before you begin

  * We strongly recommend you [take a full instance backup](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups) to help reduce the risk of data loss.

  * To help reduce the length of possible application downtime, we strongly recommend cloning the instance and verifying the following migration steps before completing them in a production environment.

For more information, see [Clone instances](https://docs.cloud.google.com/sql/docs/mysql/clone-instance).




### Drop schema using object migration

Database object migration is a multi-step process to move database objects, such as tables, to a temporary schema:

  1. Back up other database objects, including procedures, functions, and views.
  2. Drop and recreate the impacted schema.
  3. Import the backed-up objects back into the original schema.



This migration method typically causes application downtime. To minimize interruption, prepare all necessary scripts in advance. For example, make sure that your scripts are ready to handle:

  * Renaming tables and moving them to a temporary schema.
  * Backing up other database objects, such as procedures, functions, views, and any others.
  * Restoring all database objects to the original schema.



After these scripts are ready, complete the following steps:

  1. Create a temp schema (example: `fix_orphan_tables`) on the same instance.
  2. Stop the application traffic on the affected schema.
  3. Move all the tables to temp schema using `RENAME TABLE`:
         
         RENAME TABLE DB.TABLE_NAME TO fix_orphan_tables.TABLE_NAME;
         

Make the following replacements:

     * `DB`: the database name you want to use.
     * `TABLE_NAME`: the table name.
  4. Backup database objects, such as views, routines, stored procedures, triggers, and events. One way of doing so is using `mysqldump`:
         
         mysqldump -u USER --password=PASSWORD \
           -h HOST_IP --set-gtid-purged=OFF --no-data --no-create-db  \
           --no-create-info --routines --triggers --skip-opt --events \
           DB > DB_export.sql
         

Make the following replacements:

     * `USER`: the username.
     * `PASSWORD`: the database password.
     * `HOST_IP`: the IP address of the host.
     * `DB`: the database name you want to use.

You are strongly encouraged to manually backup views using the [`SHOW CREATE VIEW`](https://dev.mysql.com/doc/refman/8.0/en/show-create-view.html) command snippet.

  5. Drop the schema containing orphaned tables.

  6. Create the schema with the original name.

  7. Verify if the orphan table is removed:
         
         SELECT * FROM INFORMATION_SCHEMA.INNODB_SYS_TABLES WHERE NAME LIKE '%ORPHAN_TABLE_NAME</var>';
         

Replace `ORPHAN_TABLE_NAME` with the orphan table name.

  8. Copy the tables back to original schema:
         
         RENAME TABLE fix_orphan_tables.TABLE_NAME TO DB.TABLE_NAME;
         

Make the following replacements:

     * `TABLE_NAME`: the table name.
     * `DB`: the database name you want to use.
  9. Copy all the database objects from the backup taken in step 4.
         
         mysql -u USER \
           --password=PASSWORD \
           -h <var>HOST_IP \
           -D<var>DB < >varDB_export.sql
         

Make the following replacements:

     * `USER`: the username.
     * `PASSWORD`: the database password.
     * `HOST_IP`: the IP address of the host.
     * `DB`: the database name you want to use.

You are strongly encouraged to manually restore views by creating them again using the [`CREATE VIEW`](https://dev.mysql.com/doc/refman/8.0/en/create-view.html) statement.

  10. Resume any application traffic that you stopped previously.




### Drop schema using dump and load to the same instance

Another way to remove an orphan table is to perform a full dump of the impacted schema, dropping and recreating the schema, and then restoring the dump. In some scenarios, this method might be faster and less complex. To minimize interruption, make sure to prepare all backup and restore scripts in advance.

After these scripts are ready, complete the following steps:

  1. Stop the application traffic on the impacted schema.
  2. Backup the schema where the orphan table is located, including all stored procedures, triggers, views and events using `mysqldump`.
  3. Drop the schema.
  4. Create the schema again and restore the backup file.
  5. Resume any application traffic stopped in the first step.



### Dump and load to a new or recreated instance

In certain conditions, the schema containing the orphan table can't be dropped. In these cases, you must either migrate out to a new instance or recreate the existing instance using a logical dump and load. Either approach can cause application interruptions and might require reconfiguring your applications to point to the newly created or recreated database instance. The following sections cover both methods.

#### Migrate data to a new instance using Database Migration Service (DMS)

  1. Use [Database Migration Service](https://docs.cloud.google.com/database-migration/docs/mysql/quickstart) to create a new Cloud SQL for MySQL instance.
  2. After the replica instance has finished replicating data associated with the new instance, stop any applications that connect to the source instance.
  3. Promote the replica Cloud SQL for MySQL instance.
  4. Change all application connections to point to the newly promoted Cloud SQL for MySQL instance and restart the applications.



#### Manual dump and restore

  1. If you're creating a new database instance, create an instance with the same configuration as the current instance.
  2. Stop all application traffic on the current database instance.
  3. Backup all schemas using `mysqldump` or a similar utility.
  4. If using the same instance, delete and recreate the instance.
  5. Using the backup you created in the third step, restore the backup to the new instance or to the same recreated instance.
  6. Point your applications to the new instance or to the same recreated instance and resume application operations.



## What's next

  1. [Troubleshooting](https://docs.cloud.google.com/sql/docs/mysql/troubleshooting)
  2. [Upgrade the database major version in-place](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
