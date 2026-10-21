---
url: https://docs.cloud.google.com/datastream/docs/configure-amazon-rds-oracle/
title: Configure an Amazon RDS Oracle database for CDC \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:47.944547+00:00
---

# Configure an Amazon RDS Oracle database for CDC  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/configure-amazon-rds-oracle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Configure an Amazon RDS Oracle database for CDC Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure change data capture (CDC) to stream data from an Amazon RDS Oracle database to a [supported destination](https://docs.cloud.google.com/datastream/docs/destinations), such as BigQuery or Cloud Storage.

You can configure your source Oracle database for use with the following CDC methods:

  * Binary log reader ([Preview](https://cloud.google.com/products/#product-launch-stages))
  * LogMiner API



For more information about the binary log reader and the LogMiner API, see [Work with Oracle database redo log files](https://docs.cloud.google.com/datastream/docs/work-with-oracle-database-redo-log-files).

For detailed instructions about how to configure your source Oracle database for each of these methods, see the sections that follow.

## Configure your Amazon RDS Oracle database for binary log reader

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For Amazon RDS sources, Datastream supports only database directory objects as the log access method for the binary log reader. You need to create the database directories that point to the online redo log files and the archived log files. The names of these directories are static and can't be changed later. You need to provide these names to Datastream when you create your stream.

  1. Connect to your source Amazon RDS instance.

  2. In the terminal, or using the Amazon RDS dashboard, run the following commands:
         
         BEGIN
         rdsadmin.rdsadmin_master_util.create_archivelog_dir;
         END;
         BEGIN
         rdsadmin.rdsadmin_master_util.create_onlinelog_dir;
         END;
         COMMIT;
         GRANT READ ON DIRECTORY ONLINELOG_DIR TO USER_NAME;
         GRANT READ ON DIRECTORY ARCHIVELOG_DIR TO USER_NAME;

  3. Verify that your database is running in `ARCHIVELOG` mode. To do so, sign in to your Oracle database and run the following command at the SQL prompt:

`SELECT LOG_MODE FROM V$DATABASE;`

     1. If the result is `ARCHIVELOG`, then move on to step c.
     2. If the result is `NOARCHIVELOG`, then you'll need to enable `ARCHIVELOG` mode for your database. For your database to run in `ARCHIVELOG` mode, you must enable backups for the database.
     3. Archived log files consume disk space, so you'll want to configure the [DB_RECOVERY_FILE_DEST_SIZE](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DB_RECOVERY_FILE_DEST_SIZE.html#GUID-FA2F9735-DD0E-4026-96F0-80AF0E5E6E64) parameter for your database. Use this parameter to specify (in bytes) the hard limit on the total space to be used by target database recovery files. By setting this parameter, you can manage the tradeoff between protecting the database from running out of disk space and the stream failing because of log position loss.
     4. Define a data retention policy for your database by running this command: 
            
            exec rdsadmin.rdsadmin_util.set_configuration('archivelog retention hours',96);

We recommend that you retain backups and archive logs for a minimum of 4 days, and 7 days is recommended. Running this command will restart your database instance so that the changes you made to the database can take effect.
     5. Configure the Oracle log file rotation policy. We recommend setting a maximum log file size to a value lower than 1GB.
  4. Enable [supplemental log data](https://docs.oracle.com/cd/B19306_01/server.102/b14215/logminer.htm#i1021068). To do so, first enable minimal database-level supplemental logging by running the following command: 
         
         exec rdsadmin.rdsadmin_util.alter_supplemental_logging('ADD');

Next, choose whether to turn on logging for specific tables or the entire database.

To log changes only for specific tables, run the following command for each table that you want to replicate: 
         
         ALTER TABLE SCHEMA.TABLE ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS;

Replace the following:

     * SCHEMA: the name of the schema that contains the table.
     * TABLE: the name of the table for which you want to log changes.

To replicate most or all tables in your database, consider turning logging on for the entire database. At the SQL prompt, run the following command to enable supplemental log data for the entire database:
    
    exec rdsadmin.rdsadmin_util.alter_supplemental_logging('ADD','ALL');

The supplemental logging mode must be set to `ALL`. You can't set this mode to `PK_ONLY`.
  5. Grant the following privileges to the database user:
         
         exec rdsadmin.rdsadmin_util.grant_sys_object('GV_$LOG','USER_NAME','SELECT');
         exec rdsadmin.rdsadmin_util.grant_sys_object('GV_$LOGFILE','USER_NAME','SELECT');
         exec rdsadmin.rdsadmin_util.grant_sys_object('GV_$ARCHIVED_LOG','USER_NAME','SELECT');
         exec rdsadmin.rdsadmin_util.grant_sys_object('GV_$INSTANCE','USER_NAME','SELECT');
         exec rdsadmin.rdsadmin_util.grant_sys_object('GV_$STANDBY_LOG','USER_NAME','SELECT');
         exec rdsadmin.rdsadmin_util.grant_sys_object('V_$INSTANCE','USER_NAME','SELECT');
         exec rdsadmin.rdsadmin_util.grant_sys_object('V_$PDBS','USER_NAME','SELECT');
         exec rdsadmin.rdsadmin_util.grant_sys_object('V_$TRANSPORTABLE_PLATFORM','USER_NAME','SELECT');
         exec rdsadmin.rdsadmin_util.grant_sys_object('V_$DATABASE','USER_NAME','SELECT');
         exec rdsadmin.rdsadmin_util.grant_sys_object('V_$PARAMETER','USER_NAME','SELECT');
         exec rdsadmin.rdsadmin_util.grant_sys_object('COL$','USER_NAME','SELECT');
         exec rdsadmin.rdsadmin_util.grant_sys_object('DBA_OBJECTS','USER_NAME','SELECT');
         exec rdsadmin.rdsadmin_util.grant_sys_object('DBA_TABLESPACES','USER_NAME','SELECT');
         exec rdsadmin.rdsadmin_util.grant_sys_object('DBA_ENCRYPTED_COLUMNS','USER_NAME','SELECT');
         exec rdsadmin.rdsadmin_util.grant_sys_object('DBA_EXTENTS','USER_NAME','SELECT');
         GRANT CONNECT TO USER_NAME;
         GRANT CREATE SESSION TO USER_NAME;
         GRANT SELECT ANY TABLE TO USER_NAME;

Replace USER_NAME with the name of the user account that you intend to use to connect to your database.




## Configure your Amazon RDS Oracle database for LogMiner

  1. Verify that your database is running in `ARCHIVELOG` mode. To do so, sign in to your Oracle database and run the following command at the SQL prompt:
         
         SELECT LOG_MODE FROM V$DATABASE;
         

     1. If the result is `ARCHIVELOG`, then move on to step c.
     2. If the result is `NOARCHIVELOG`, then you'll need to enable `ARCHIVELOG` mode for your database.

Key point: For your database to run in `ARCHIVELOG` mode, you must enable backups for the database.

     3. Archived log files consume disk space, so you'll want to configure the [DB_RECOVERY_FILE_DEST_SIZE](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DB_RECOVERY_FILE_DEST_SIZE.html#GUID-FA2F9735-DD0E-4026-96F0-80AF0E5E6E64) parameter for your database. Use this parameter to specify (in bytes) the hard limit on the total space to be used by target database recovery files. By setting this parameter, you can manage the tradeoff between protecting the database from running out of disk space and the stream failing because of log position loss.

     4. Define a data retention policy for your database by running this command:
            
            exec rdsadmin.rdsadmin_util.set_configuration('archivelog retention hours',96);
            

We recommend that you retain backups and archive logs for a minimum of 4 days, and 7 days is recommended.

**Note:** Running this command will restart your database instance so that the changes you made to the database can take effect. 5\. Configure the Oracle log file rotation policy. We recommend setting a maximum log file size to a value lower than 1GB.
  2. Enable [supplemental log data](https://docs.oracle.com/cd/B19306_01/server.102/b14215/logminer.htm#i1021068). To do so, first enable minimal database-level supplemental logging by running the following command:
         
         exec rdsadmin.rdsadmin_util.alter_supplemental_logging('ADD');
         

Next, choose whether to turn on logging for specific tables or the entire database.

To log changes only for specific tables, run the following command for each table that you want to replicate:
         
         ALTER TABLE SCHEMA.TABLE ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS;
         

Replace the following:

     * SCHEMA: the name of the schema that contains the table.
     * TABLE: the name of the table for which you want to log changes.

To replicate most or all tables in your database, consider turning logging on for the entire database.

At the SQL prompt, run the following command to enable supplemental log data for the entire database:
    
    exec rdsadmin.rdsadmin_util.alter_supplemental_logging('ADD','ALL');
    

**Important:** The supplemental logging mode must be set to `ALL`. You can't set this mode to `PK_ONLY`.
  3. Grant the appropriate privileges to the user account that will be used to connect to your database. To do so, run the following commands:
         
         GRANT EXECUTE_CATALOG_ROLE TO USER_NAME;
         GRANT CONNECT TO USER_NAME;
         GRANT CREATE SESSION TO USER_NAME;
         exec rdsadmin.rdsadmin_util.grant_sys_object('V_$DATABASE','USER_NAME','SELECT');
         exec rdsadmin.rdsadmin_util.grant_sys_object('V_$ARCHIVED_LOG','USER_NAME','SELECT');
         exec rdsadmin.rdsadmin_util.grant_sys_object('V_$LOG','USER_NAME','SELECT'); -- for primary databases
         exec rdsadmin.rdsadmin_util.grant_sys_object('V_$STANDBY_LOG','USER_NAME','SELECT'); -- for standby databases
         exec rdsadmin.rdsadmin_util.grant_sys_object('V_$LOGFILE','USER_NAME','SELECT');
         exec rdsadmin.rdsadmin_util.grant_sys_object('V_$LOGMNR_LOGS','USER_NAME','SELECT');
         exec rdsadmin.rdsadmin_util.grant_sys_object('V_$LOGMNR_CONTENTS','USER_NAME','SELECT');
         exec rdsadmin.rdsadmin_util.grant_sys_object('V_$PARAMETER','USER_NAME','SELECT');
         exec rdsadmin.rdsadmin_util.grant_sys_object('DBMS_LOGMNR','USER_NAME','EXECUTE');
         exec rdsadmin.rdsadmin_util.grant_sys_object('DBMS_LOGMNR_D','USER_NAME','EXECUTE');
         GRANT SELECT ANY TRANSACTION TO USER_NAME;
         GRANT SELECT ANY TABLE TO USER_NAME;

If your database uses Transparent Data Encryption (TDE), grant the following permissions:
         
         exec rdsadmin.rdsadmin_util.grant_sys_object('DBA_TABLESPACES','USER_NAME','SELECT');
         exec rdsadmin.rdsadmin_util.grant_sys_object('DBA_ENCRYPTED_COLUMNS','USER_NAME','SELECT');

If your organization doesn't permit granting the `GRANT SELECT ANY TABLE` permission, use the solution described in the [Oracle change data capture (CDC)](https://docs.cloud.google.com/datastream/docs/faq#grant-select) section of the Datastream FAQ page.

If your source database is Oracle 12c or newer, then grant the following additional privilege:
         
         GRANT LOGMINING TO USER_NAME;

For each command, replace `USER_NAME` with the name of the user account. Also, running these commands will grant privileges to the user to read from `V$DATABASE` (which is required for validation), start the log miner, and grant privileges to select from `V$LOGMNR_CONTENT`.
  4. Grant the user account `SELECT` access to the `DBA_EXTENTS` view in your database. This privilege lets you use the [`ROWID` based backfill](https://docs.cloud.google.com/datastream/docs/sources-oracle#rowid-backfill) for your Oracle source:
         
         GRANT SELECT ON DBA_EXTENTS TO USER_NAME;




## What's next

  * Learn more about how Datastream works with [Oracle sources](https://docs.cloud.google.com/datastream/docs/sources-oracle).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
