---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-source-database/
title: Configure your source Oracle database for continuous migrations \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:05.856105+00:00
---

# Configure your source Oracle database for continuous migrations  |  Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-source-database/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/scenario-overview)



Send feedback 

#  Configure your source Oracle database for continuous migrations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure your Oracle source database for a continuous migration with Database Migration Service.

Database Migration Service leverages the Oracle LogMiner API, which is part of Oracle Database, to query archived redo log files. Redo log files contain information about the history of activity on a database. For more information about how Database Migration Service works with these log files, see [ About data flow for Oracle migrations](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/about-data-flow#cdc).

Database Migration Service can pull changes to data from an on-premises Oracle database or any cloud-hosted Oracle database, including Oracle relational database service (RDS). 

## Configure your source Oracle database

Before you can use Database Migration Service to pull data from your source Oracle database, you must configure your database by:

  * Setting up [ archive logging](https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/managing-archived-redo-log-files.html#GUID-36F3335E-A28B-47BA-82C2-E17B4C8A453A) to track changes in your database, such as the `INSERT`, `UPDATE`, `DELETE`, and `RENAME` operations.

  * Granting the appropriate privileges to the user account that will be used to connect to your database and access schema and code objects.

By default, Database Migration Service attempts to access all your object definitions through [ `DBA_VIEWS`](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_VIEWS.html). Access to `DBA_VIEWS` is granted with the `SELECT ANY DICTIONARY` privilege. If DBA views aren't accessible to the migration user account, Database Migration Service falls back to [ `ALL_VIEWS`](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_VIEWS.html). This approach provides you with the greatest degree of flexibility with respect to defining a security model that best matches your requirements.

If you want Database Migration Service to only access a certain subset of your object definitions, then grant the migration user a role with more fine-grained privilege configuration instead of `SELECT ANY DICTIONARY`.

  * Defining a data retention policy for your database to determine which data will be archived, how long it will be kept, should the data at the end of the retention period be archived or destroyed.




Database Migration Service works with the following types of Oracle databases:

  * Amazon RDS for Oracle
  * Self-hosted Oracle
  * Self-hosted Oracle pluggable database



### Configure an Amazon RDS for Oracle database

  1. Verify that your database is running in `ARCHIVELOG` mode. To do so, run the following command:

`SELECT LOG_MODE FROM V$DATABASE;`

     1. If the result is `ARCHIVELOG`, then move on to step c.

     2. If the result is `NOARCHIVELOG`, then you'll need to enable `ARCHIVELOG` mode for your database.

For your database to be placed in `ARCHIVELOG` mode, you must enable backups for the database.
     3. Archived log files consume disk space, we recommend that you configure the [ `DB_RECOVERY_FILE_DEST_SIZE`](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DB_RECOVERY_FILE_DEST_SIZE.html#GUID-FA2F9735-DD0E-4026-96F0-80AF0E5E6E64) parameter for your database. Use this parameter to specify (in bytes) the hard limit on the total space to be used by target database recovery files. By setting this parameter, you can manage the tradeoff between information availability and disk space.

     4. Define a data retention policy for your database by running this command:
            
            exec rdsadmin.rdsadmin_util.set_configuration('archivelog retention hours',96);

We recommend that you retain backups and archive logs for a minimum of 4 days, and 7 days is recommended.

Running these commands will restart your database instance so that the changes you made to the database can take effect. 
     5. Configure the Oracle log file rotation policy. We recommend setting a maximum log file size of no more than 512MB. For more information about managing the log rotation, see [ Work with Oracle database log files](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/work-with-oracle-database-redo-log-files).

  2. Enable [ supplemental log data](https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/oracle-logminer-utility.html#GUID-D857AF96-AC24-4CA1-B620-8EA3DF30D72E). To do so, first enable supplemental logging on the database by running the following command:
         
         exec rdsadmin.rdsadmin_util.alter_supplemental_logging('ADD');

Next, choose whether to turn on logging for specific tables or the entire database.

To log changes only for specific tables, run the following command for each table that you want to replicate:
         
         ALTER TABLE SCHEMA.TABLE ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS

Replace the following:

     * SCHEMA: the name of the schema that contains the table.
     * TABLE: the name of the table for which you want to log changes.

To replicate most or all tables in your database, consider turning logging on for the entire database.

At the SQL prompt, run the following command to enable supplemental log data for the entire database:
    
    exec rdsadmin.rdsadmin_util.alter_supplemental_logging('ADD','ALL');

The supplemental logging mode must be set to `ALL`. You can't set this mode to `PK_ONLY`. 
  3. Grant the appropriate privileges to the user account that will be used to connect to your database. To do so, run the following commands:
         
         GRANT CONNECT TO USER_NAME;
         GRANT CREATE SESSION TO USER_NAME;
         exec rdsadmin.rdsadmin_util.grant_sys_object('V_$DATABASE','USER_NAME','SELECT');
         exec rdsadmin.rdsadmin_util.grant_sys_object('V_$ARCHIVED_LOG','USER_NAME','SELECT');
         exec rdsadmin.rdsadmin_util.grant_sys_object('V_$LOGMNR_LOGS','USER_NAME','SELECT');
         exec rdsadmin.rdsadmin_util.grant_sys_object('V_$LOGMNR_CONTENTS','USER_NAME','SELECT');
         exec rdsadmin.rdsadmin_util.grant_sys_object('DBMS_LOGMNR','USER_NAME','EXECUTE');
         exec rdsadmin.rdsadmin_util.grant_sys_object('DBMS_LOGMNR_D','USER_NAME','EXECUTE');
         GRANT SELECT ANY TRANSACTION TO USER_NAME;
         GRANT SELECT ANY TABLE TO USER_NAME;
         GRANT SELECT ANY DICTIONARY TO USER_NAME;
         GRANT SELECT ON DBA_EXTENTS TO USER_NAME;

If your source database is Oracle 12c or newer, then grant the following additional privilege:
         
         GRANT LOGMINING TO USER_NAME;

For each command, replace `USER_NAME` with the name of the user account. Also, running these commands will grant privileges to the user to read from `V$DATABASE` (which is required for validation), start the log miner, and grant privileges to select from `V$LOGMNR_CONTENT`. 




### Configure a self-hosted Oracle database

  1. Verify that your database is running in `ARCHIVELOG` mode. To do so, run the following command:

`SELECT LOG_MODE FROM V$DATABASE;`

     1. If the result is `ARCHIVELOG`, then move on to step 2.

     2. If the result is `NOARCHIVELOG`, then you'll need to enable `ARCHIVELOG` mode for your database.

     3. Run the following commands when logged in as `SYSDBA`:
            
            SHUTDOWN IMMEDIATE;
            STARTUP MOUNT;
            ALTER DATABASE ARCHIVELOG;
            ALTER DATABASE OPEN;

Running these commands will restart your database instance so that the changes you made to the database can take effect. 
     4. Archived log files consume disk space, we recommend that you configure the [ `DB_RECOVERY_FILE_DEST_SIZE`](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DB_RECOVERY_FILE_DEST_SIZE.html#GUID-FA2F9735-DD0E-4026-96F0-80AF0E5E6E64) parameter for your database. Use this parameter to specify (in bytes) the hard limit on the total space to be used by target database recovery files. By setting this parameter, you can manage the tradeoff between information availability and disk space.

  2. Define a data retention policy for your database by running the following Oracle Recovery Manager (RMAN) command:
         
         CONFIGURE RETENTION POLICY TO RECOVERY WINDOW OF 4 DAYS;

You can use the `TARGET /` command to start an RMAN client and connect to the source database. See [ Connecting to the Target Database Using RMAN](https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/starting-interacting-with-rman-client.html#GUID-E07231B2-F213-4F8F-8D02-E410A6DAE94C). 

We recommend that you retain backups and archive logs for a minimum of 4 days, and 7 days is recommended.

  3. Return to the SQL prompt of the database tool that you're using to configure the Oracle log file rotation policy. We recommend setting a maximum log file size of no more than 512MB.

  4. Enable [ supplemental log data](https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/oracle-logminer-utility.html#GUID-D857AF96-AC24-4CA1-B620-8EA3DF30D72E). To do so, first enable supplemental logging on the database by running the following command:
         
         ALTER DATABASE ADD SUPPLEMENTAL LOG DATA;

Next, choose whether to turn on logging for specific tables or the entire database.

To log changes only for specific tables, run the following command for each table that you want to replicate:
         
         ALTER TABLE SCHEMA.TABLE ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS

Replace the following:

     * SCHEMA: the name of the schema that contains the table.
     * TABLE: the name of the table for which you want to log changes.

To replicate most or all tables in your database, consider turning logging on for the entire database.

Run the following command to enable supplemental log data for the entire database:
    
    ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (all) COLUMNS;

The supplemental logging mode must be set to `ALL`. You can't set this mode to `PK_ONLY`. 
  5. Grant the appropriate privileges to the user account that will be used to connect to your database. To do so, run the following commands:
         
         GRANT CONNECT TO USER_NAME;
         GRANT CREATE SESSION TO USER_NAME;
         GRANT SELECT ON SYS.V_$DATABASE TO USER_NAME;
         GRANT SELECT ON SYS.V_$ARCHIVED_LOG TO USER_NAME;
         GRANT SELECT ON SYS.V_$LOGMNR_CONTENTS TO USER_NAME;
         GRANT SELECT ON SYS.V_$LOGMNR_LOGS TO USER_NAME;
         GRANT EXECUTE ON DBMS_LOGMNR TO USER_NAME;
         GRANT EXECUTE ON DBMS_LOGMNR_D TO USER_NAME;
         GRANT SELECT ANY TRANSACTION TO USER_NAME;
         GRANT SELECT ANY TABLE TO USER_NAME;
         GRANT SELECT ANY DICTIONARY TO USER_NAME;
         GRANT EXECUTE_CATALOG_ROLE TO USER_NAME;
         GRANT SELECT ON DBA_EXTENTS TO USER_NAME;

If your source database is Oracle 12c or newer, then grant the following additional privilege:
         
         GRANT LOGMINING TO USER_NAME;

For each command, replace `USER_NAME` with the name of the user account. Also, running these commands will grant privileges to the user to read from `V$DATABASE` (which is required for validation), start the log miner, and grant privileges to select from `V$LOGMNR_CONTENT`. 




### Configure a self-hosted Oracle pluggable database

Database Migration Service supports Oracle multi-tenant architecture, where a single [ container database (CDB)](https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/introduction-to-oracle-database.html#GUID-AB84D6C9-4BBE-4D36-992F-2BB85739329F) contains one or more pluggable databases (PDBs). Each pluggable database is a self-contained database with a unique ID and name, and can be managed independently.

To connect to a container in a multi-tenant architecture setup, or to switch between container sessions, use the following command:

`ALTER SESSION SET CONTAINER = CONTAINER_NAME;`

Replace CONTAINER_NAME with the name of your container, for example your pluggable database or the `CDB$ROOT` container.

To configure a self-hosted Oracle pluggable database so that you can use it with Database Migration Service, perform the following steps:

  1. Verify that your database is running in `ARCHIVELOG` mode. To do so, run the following command from the `CDB$ROOT` container:

`SELECT LOG_MODE FROM V$DATABASE;`

     1. If the result is `ARCHIVELOG`, then move on to step 2.

     2. If the result is `NOARCHIVELOG`, then you'll need to enable `ARCHIVELOG` mode for your database.

     3. Run the following commands when logged in as `SYSDBA`:
            
            SHUTDOWN IMMEDIATE;
            STARTUP MOUNT;
            ALTER DATABASE ARCHIVELOG;
            ALTER DATABASE OPEN;

Running these commands will restart your database instance so that the changes you made to the database can take effect. 
     4. Archived log files consume disk space, we recommend that you configure the [ `DB_RECOVERY_FILE_DEST_SIZE`](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DB_RECOVERY_FILE_DEST_SIZE.html#GUID-FA2F9735-DD0E-4026-96F0-80AF0E5E6E64) parameter for your database. Use this parameter to specify (in bytes) the hard limit on the total space to be used by target database recovery files. By setting this parameter, you can manage the tradeoff between information availability and disk space.

  2. Define a data retention policy for your database by running the following Oracle Recovery Manager (RMAN) command from the `CDB$ROOT` container:
         
         CONFIGURE RETENTION POLICY TO RECOVERY WINDOW OF 4 DAYS;

You can use the `TARGET /` command to start an RMAN client and connect to the source database. See [ Connecting to the Target Database Using RMAN](https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/starting-interacting-with-rman-client.html#GUID-E07231B2-F213-4F8F-8D02-E410A6DAE94C). 

We recommend that you retain backups and archive logs for a minimum of 4 days, and 7 days is recommended.

  3. Return to the SQL prompt of the database tool that you're using to configure the Oracle log file rotation policy. We recommend setting a maximum log file size of no more than 512MB.

  4. Enable [ supplemental log data](https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/oracle-logminer-utility.html#GUID-D857AF96-AC24-4CA1-B620-8EA3DF30D72E). To do so, first enable supplemental logging on the database at the `CDB$ROOT` level by running the following command:
         
         ALTER DATABASE ADD SUPPLEMENTAL LOG DATA;

Next, choose whether to turn on logging for specific tables or the entire pluggable database.

To log changes only for specific tables, connect to the pluggable database container and run the following command for each table that you want to replicate:
         
         ALTER TABLE SCHEMA.TABLE ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS

Replace the following:

     * SCHEMA: the name of the schema that contains the table.
     * TABLE: the name of the table for which you want to log changes.

To replicate most or all tables in your database, consider turning logging on for the entire database.

Run the following command to enable supplemental log data for the entire database:
    
    ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (all) COLUMNS;

The supplemental logging mode must be set to `ALL`. You can't set this mode to `PK_ONLY`. 
  5. Create a [ common user](https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/tables-and-table-clusters.html#GUID-19337B94-645B-45E8-842C-762BBC544B13). A common user has the same identity in the `CDB$ROOT` container and in the pluggable databases. A common user can connect to and perform operations within the root, and within any pluggable database in which it has privileges. The common username must start with `C##` or `c##`.

  6. Grant the appropriate privileges to the common user that will be used to connect to your database. Different permissions are required at the `CDB$ROOT` container and pluggable database levels.

     * Connect to the `CDB$ROOT` container and run the following commands:
           
           GRANT CREATE SESSION TO USER_NAME;
           GRANT SET CONTAINER TO USER_NAME;
           GRANT SELECT ON SYS.V_$DATABASE TO USER_NAME;
           GRANT SELECT ON SYS.V_$LOGMNR_CONTENTS TO USER_NAME;
           GRANT EXECUTE ON DBMS_LOGMNR TO USER_NAME;
           GRANT EXECUTE ON DBMS_LOGMNR_D TO USER_NAME;
           GRANT LOGMINING TO USER_NAME;
           GRANT EXECUTE_CATALOG_ROLE TO USER_NAME;

     * Connect to the pluggable database and run the following commands:
           
           GRANT CREATE SESSION TO USER_NAME;
           GRANT SET CONTAINER TO USER_NAME;
           GRANT SELECT ANY TABLE TO USER_NAME;
           GRANT SELECT ANY DICTIONARY TO USER_NAME;
           GRANT SELECT ON SYS.V_$DATABASE TO USER_NAME;
           GRANT SELECT ON SYS.V_$ARCHIVED_LOG TO USER_NAME;
           GRANT SELECT ON DBA_SUPPLEMENTAL_LOGGING TO USER_NAME;
           GRANT SELECT ON DBA_EXTENTS TO USER_NAME;

For each command, replace `USER_NAME` with the name of the common user account. Running these commands will grant privileges to the user to read from `V$DATABASE` (which is required for validation), start the log miner, and grant privileges to select from `V$LOGMNR_CONTENT`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
