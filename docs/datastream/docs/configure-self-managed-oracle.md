---
url: https://docs.cloud.google.com/datastream/docs/configure-self-managed-oracle/
title: Configure a self-managed Oracle database for CDC \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:36.889169+00:00
---

# Configure a self-managed Oracle database for CDC  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/configure-self-managed-oracle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Configure a self-managed Oracle database for CDC Stay organized with collections  Save and categorize content based on your preferences. 

To stream change data capture (CDC) updates from a self-managed Oracle database to a [supported destination](https://docs.cloud.google.com/datastream/docs/destinations) such as BigQuery or Cloud Storage, you can configure Datastream to read your redo log files using the binary log reader ([Preview](https://cloud.google.com/products#product-launch-stages)) or the LogMiner API. You prepare your database by enabling `ARCHIVELOG` mode, setting a data retention policy, enabling supplemental logging, and granting user privileges. For more information about these CDC methods, see [Work with Oracle database redo log files](https://docs.cloud.google.com/datastream/docs/work-with-oracle-database-redo-log-files).

## Configure your self managed Oracle database for binary log reader

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To configure your self-managed Oracle database for use with the binary log reader CDC method, perform the following steps:

  1. Create a database user account to be used by Datastream to connect to your database:
         
         CREATE USER USER_NAME IDENTIFIED BY USER_PASSWORD;

Replace the following:

     * USER_NAME: the name of the database user account that you want to use to connect to your database.
     * USER_PASSWORD: the password for the database user account.
  2. Select one of the following methods to access your log files:

     * **Automatic Storage Management (ASM)** : if you select this option, you need to create a dedicated ASM connection, and provide its details when you create your connection profile. The user account used for the ASM connection must have the `SYSASM` privilege.

To create a new ASM user with the `SYSASM` privilege, run the following commands:
           
           CREATE USER ASM_USER_NAME IDENTIFIED BY ASM_PASSWORD;
           GRANT SYSASM TO ASM_USER_NAME;

Replace the following:

       * ASM_USER_NAME: the name of the ASM user.
       * ASM_PASSWORD: the password for the ASM user.
     * **Database directories** : if you select this option, you need to create database directory objects that point to the redo log files and the archived log files, and grant `READ` access to the directories to your database user:
    
    CREATE DIRECTORY DIRECTORY_NAME_1 as 'ONLINE_REDO_LOGS_PATH';
    CREATE DIRECTORY DIRECTORY_NAME_2 as 'ARCHIVED_REDO_LOGS_PATH';
    GRANT READ ON DIRECTORY DIRECTORY_NAME_1 to USER_NAME;
    GRANT READ ON DIRECTORY DIRECTORY_NAME_2 to USER_NAME;

Replace the following:

     * DIRECTORY_NAME_1: the name of the directory for the online redo log files.
     * DIRECTORY_NAME_2: the name of the directory for the archived redo log files.
     * ONLINE_REDO_LOGS_PATH: the path to the directory where online redo log files are to be stored.
     * ARCHIVED_REDO_LOGS_PATH: the path to the directory where archived log files are to be stored.
     * USER_NAME: the name of the database user account created earlier.

If you select the binary log reader method and use database directories, you need to provide the redo log and archived log directory names when you create your stream.

  3. Verify that your database is running in `ARCHIVELOG` mode.

To do so, sign in to your Oracle database and run the following command at the SQL prompt:

`SELECT LOG_MODE FROM V$DATABASE;`

     1. If the result is `ARCHIVELOG`, then move on to the next step.
     2. If the result is `NOARCHIVELOG`, then you'll need to enable `ARCHIVELOG` mode for your database.
     3. Run the following commands when logged in as `SYSDBA`:
            
            SHUTDOWN IMMEDIATE;
            STARTUP MOUNT;
            ALTER DATABASE ARCHIVELOG;
            ALTER DATABASE OPEN;

     4. Archived log files consume disk space, so you'll want to configure the [DB_RECOVERY_FILE_DEST_SIZE](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DB_RECOVERY_FILE_DEST_SIZE.html#GUID-FA2F9735-DD0E-4026-96F0-80AF0E5E6E64) parameter for your database. Use this parameter to specify (in bytes) the hard limit on the total space to be used by target database recovery files. By setting this parameter, you can manage the tradeoff between protecting the database from running out of disk space and the stream failing because of log position loss.

  4. Define a data retention policy for your database by running these Oracle Recovery Manager (RMAN) commands: 
         
         TARGET /
         CONFIGURE RETENTION POLICY TO RECOVERY WINDOW OF 4 DAYS;

You use the `TARGET /` command to start an RMAN client and connect to the source database. See [Making Database Connections with RMAN](https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/starting-interacting-with-rman-client.html#GUID-E07231B2-F213-4F8F-8D02-E410A6DAE94C).

We recommend that you retain backups and archive logs for a minimum of 4 days, and 7 days is recommended.

Running this command will restart your database instance so that the changes you made to the database can take effect.
  5. Return to the SQL prompt of the database tool that you're using to configure the Oracle log file rotation policy. We recommend setting a maximum log file size of no more than 512MB.

  6. Enable [supplemental log data](https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/oracle-logminer-utility.html#GUID-D857AF96-AC24-4CA1-B620-8EA3DF30D72E). To do so, first enable minimal database-level supplemental logging by running the following command:
         
         ALTER DATABASE ADD SUPPLEMENTAL LOG DATA;

Next, choose whether to turn on logging for specific tables or the entire database.

To log changes only for specific tables, run the following command for each table that you want to replicate:
         
         ALTER TABLE SCHEMA.TABLE ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS;

Replace the following:

     * SCHEMA: the name of the schema that contains the table.
     * TABLE: the name of the table for which you want to log changes.

To replicate most or all tables in your database, consider turning logging on for the entire database. Run the following command to enable supplemental log data for the entire database:
    
    ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS;

The supplemental logging mode must be set to `ALL`. You can't set this mode to `PK_ONLY`.
  7. Grant the appropriate privileges directly to the user account that's used to connect to your database. Note that these grants don't work when assigned to a role, for example. To do so, run the following commands:
         
         GRANT SELECT ON GV_$LOG TO USER_NAME;
         GRANT SELECT ON GV_$LOGFILE TO USER_NAME;
         GRANT SELECT ON GV_$ARCHIVED_LOG TO USER_NAME;
         GRANT SELECT ON GV_$INSTANCE TO USER_NAME;
         GRANT SELECT ON GV_$STANDBY_LOG TO USER_NAME;
         GRANT SELECT ON V_$INSTANCE TO USER_NAME;
         GRANT SELECT ON V_$PDBS TO USER_NAME;
         GRANT SELECT ON V_$TRANSPORTABLE_PLATFORM TO USER_NAME;
         GRANT SELECT ON V_$DATABASE TO USER_NAME;
         GRANT SELECT ON V_$PARAMETER TO USER_NAME;
         GRANT SELECT ON COL$ TO USER_NAME;
         GRANT SELECT ON DBA_OBJECTS TO USER_NAME;
         GRANT SELECT ON DBA_TABLESPACES TO USER_NAME;
         GRANT SELECT ON DBA_ENCRYPTED_COLUMNS TO USER_NAME;
         GRANT SELECT ON DBA_EXTENTS TO USER_NAME;
         
         GRANT CONNECT TO USER_NAME;
         GRANT CREATE SESSION TO USER_NAME;
         GRANT SELECT ANY TABLE TO USER_NAME;

Replace USER_NAME with the name of the database user account created earlier.




## Configure your self managed Oracle database for LogMiner

  1. Create a database user account to be used by Datastream to connect to your database:
         
         CREATE USER USER_NAME IDENTIFIED BY USER_PASSWORD;

Replace the following:

     * USER_NAME: the name of the database user account that you want to use to connect to your database.
     * USER_PASSWORD: the password for the database user account.
  2. Verify that your database is running in `ARCHIVELOG` mode.

To do so, sign in to your Oracle database and run the following command at the SQL prompt:

`SELECT LOG_MODE FROM V$DATABASE;`

     1. If the result is `ARCHIVELOG`, then move on to the next step.
     2. If the result is `NOARCHIVELOG`, then you need to enable `ARCHIVELOG` mode for your database.
     3. Run the following commands when logged in as `SYSDBA`:
            
            SHUTDOWN IMMEDIATE;
            STARTUP MOUNT;
            ALTER DATABASE ARCHIVELOG;
            ALTER DATABASE OPEN;

     4. Archived log files consume disk space, so you'll want to configure the [DB_RECOVERY_FILE_DEST_SIZE](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DB_RECOVERY_FILE_DEST_SIZE.html#GUID-FA2F9735-DD0E-4026-96F0-80AF0E5E6E64) parameter for your database. Use this parameter to specify (in bytes) the hard limit on the total space to be used by target database recovery files. By setting this parameter, you can manage the tradeoff between protecting the database from running out of disk space and the stream failing because of log position loss.

  3. Define a data retention policy for your database by running these Oracle Recovery Manager (RMAN) commands: 
         
         TARGET /
         CONFIGURE RETENTION POLICY TO RECOVERY WINDOW OF 4 DAYS;

You use the `TARGET /` command to start an RMAN client and connect to the source database. See [Making Database Connections with RMAN](https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/starting-interacting-with-rman-client.html#GUID-E07231B2-F213-4F8F-8D02-E410A6DAE94C).

We recommend that you retain backups and archive logs for a minimum of 4 days, and 7 days is recommended.

Running this command will restart your database instance so that the changes you made to the database can take effect.
  4. Return to the SQL prompt of the database tool that you're using to configure the Oracle log file rotation policy. We recommend setting a maximum log file size of no more than 512MB.

  5. Enable [supplemental log data](https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/oracle-logminer-utility.html#GUID-D857AF96-AC24-4CA1-B620-8EA3DF30D72E). To do so, first enable minimal database-level supplemental logging by running the following command:
         
         ALTER DATABASE ADD SUPPLEMENTAL LOG DATA;

Next, choose whether to turn on logging for specific tables or the entire database.

To log changes only for specific tables, run the following command for each table that you want to replicate:
         
         ALTER TABLE SCHEMA.TABLE ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS;

Replace the following:

     * SCHEMA: the name of the schema that contains the table.
     * TABLE: the name of the table for which you want to log changes.

To replicate most or all tables in your database, consider turning logging on for the entire database. Run the following command to enable supplemental log data for the entire database:
    
    ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (ALL) COLUMNS;

The supplemental logging mode must be set to `ALL`. You can't set this mode to `PK_ONLY`.
  6. Grant the appropriate privileges directly to the user account that's used to connect to your database. Note that these grants don't work when assigned to a role, for example. To do so, run the following commands:
         
         GRANT EXECUTE_CATALOG_ROLE TO USER_NAME;
         GRANT CONNECT TO USER_NAME;
         GRANT CREATE SESSION TO USER_NAME;
         GRANT SELECT ON SYS.V_$DATABASE TO USER_NAME;
         GRANT SELECT ON SYS.V_$LOG TO USER_NAME; -- for primary databases
         GRANT SELECT ON SYS.V_$STANDBY_LOG TO USER_NAME; -- for standby databases
         GRANT SELECT ON SYS.V_$LOGFILE TO USER_NAME;
         GRANT SELECT ON SYS.V_$ARCHIVED_LOG TO USER_NAME;
         GRANT SELECT ON SYS.V_$LOGMNR_CONTENTS TO USER_NAME;
         GRANT SELECT ON SYS.V_$PARAMETER TO USER_NAME;
         GRANT EXECUTE ON DBMS_LOGMNR TO USER_NAME;
         GRANT EXECUTE ON DBMS_LOGMNR_D TO USER_NAME;
         GRANT SELECT ANY TRANSACTION TO USER_NAME;
         GRANT SELECT ANY TABLE TO USER_NAME;

If your database uses Transparent Data Encryption (TDE), grant the following permissions:
         
         GRANT SELECT ON DBA_TABLESPACES TO USER_NAME;
         GRANT SELECT ON DBA_ENCRYPTED_COLUMNS TO USER_NAME;

If your organization doesn't permit granting the `GRANT SELECT ANY TABLE` permission, use the solution described in the [Oracle change data capture (CDC)](https://docs.cloud.google.com/datastream/docs/faq#grant-select) section of the Datastream FAQ page.

If your source database is Oracle 12c or newer, then grant the following additional privilege:
         
         GRANT LOGMINING TO USER_NAME;

For each command, replace `USER_NAME` with the name of the database user account. Also, running these commands will grant privileges to the user to read from `V$DATABASE` (which is required for validation), start the log miner, and grant privileges to select from `V$LOGMNR_CONTENT`. 
  7. Grant the user account `SELECT` access to the `DBA_EXTENTS` view in your database. This privilege lets you use the [`ROWID` based backfill](https://docs.cloud.google.com/datastream/docs/sources-oracle#rowid-backfill) for your Oracle source:
         
         GRANT SELECT ON DBA_EXTENTS TO USER_NAME;




## What's next

  * Learn more about how Datastream works with [Oracle sources](https://docs.cloud.google.com/datastream/docs/sources-oracle).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
