---
url: https://docs.cloud.google.com/bare-metal/docs/solutions/oracle/data-guard-setup/db-setup-primary/
title: Prepare Data Guard's primary database \u00a0|\u00a0 Bare Metal Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:15.250965+00:00
---

# Prepare Data Guard's primary database  |  Bare Metal Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/solutions/oracle/data-guard-setup/db-setup-primary/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Prepare Data Guard's primary database

Data Guard requires a primary database and at least one standby database to function. Before setting up Data Guard on Bare Metal Solution, [create the primary database](https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/creating-and-configuring-an-oracle-database.html).

The following examples are used throughout this guide:

Database unique name | Server hostnames | RAC instance names | Role  
---|---|---|---  
DBDG_SITE1 | site1db1, site1db2 | DBDG_SITE11, DBDG_SITE12 | Primary  
DBDG_SITE2 | site2db1, site2db2 | DBDG_SITE21, DBDG_SITE22 | Standby  
  
The Bare Metal Solution servers running Oracle in this guide are configured with the following environment variables:

Environment variable name | Value  
---|---  
ORACLE_BASE | /apps/oracle/oracle_base  
ORACLE_HOME | /apps/oracle/19.0.0/db_home1  
  
You might need to modify the environment variable paths depending on your setup.

## Set up the primary database

  1. Log in to the first Bare Metal Solution server that hosts the primary database.

  2. In the `/etc/oratab` file, add an entry so the `oraenv` command can set environment variables for the primary database. Modify the instance name to match the running instance on each node, and specify the full path to the Oracle database home:
         
         DBDG_SITE11:ORACLE_HOME:N
         

  3. Set the `ORACLE_SID` environment variable so you can connect to the primary database:
         
         source oraenv <<< "DBDG_SITE11"
         

You should receive the response `The Oracle base has been set to /apps/oracle/oracle_base`.




### Configure database logging and enable flashback database

  1. Start SQL*Plus, then enable `force logging` so that `nologging` tablespaces added to the database are logged:
         
         sqlplus / as sysdba
         
         
         ALTER DATABASE FORCE LOGGING;
         

  2. Verify that `archivelog mode` and `flashback database` are on:
         
         ARCHIVE LOG LIST;
         SELECT LOG_MODE, FLASHBACK_ON FROM V$DATABASE;
         

If `archivelog mode` and `flashback database` are off, turn them on with the following SQL commands:

     1. Stop the clustered database so you can make the required changes:
            
            srvctl stop database -d 

     2. Run the required SQL commands to turn on `archivelog mode` and `flashback database`:
            
            STARTUP MOUNT;
             ALTER DATABASE ARCHIVELOG;
             ALTER DATABASE FLASHBACK ON;
             ALTER SYSTEM SET DB_FLASHBACK_RETENTION_TARGET=1440 SID='*' SCOPE=BOTH;
             ALTER DATABASE OPEN;
             SHUTDOWN IMMEDIATE;
             EXIT;
            

     3. Start the clustered database again:
            
            srvctl start database -d DBDG_SITE1
            




### Prepare the database for Data Guard

**Note:** This guide configures the Data Guard broker to manage the configuration. The broker simplifies Data Guard setup by reducing the number of database initialization parameters that must be manually set. This guide shows the minimum set of parameters that you must configure to enable Data Guard.

  1. Log in to the first Bare Metal Solution server that hosts the primary database and set the `ORACLE_SID` environment variable so you can connect to the primary database:
         
         source oraenv <<< "DBDG_SITE11"
         

You should receive the response `The Oracle base has been set to /apps/oracle/oracle_base`.

  2. Start SQL*Plus, then modify the database initialization parameters required for the Data Guard configuration and services:
         
         sqlplus / as sysdba
         
         
         ALTER SYSTEM SET LOG_ARCHIVE_FORMAT='%t_%s_%r.arc' SID='*' SCOPE=SPFILE;
         ALTER SYSTEM SET LOG_ARCHIVE_MAX_PROCESSES=8 SID='*' SCOPE=BOTH;
         ALTER SYSTEM SET REMOTE_LOGIN_PASSWORDFILE=EXCLUSIVE SID='*' SCOPE=SPFILE;
         ALTER SYSTEM SET STANDBY_FILE_MANAGEMENT=AUTO SID='*' SCOPE=BOTH;
         

  3. Check for the existence of standby redo logs in the database. Each thread must have one more standby redo log group than the number of online redo log groups.
         
         SELECT 'Logfile groups in thread ' || THREAD# || ': ' || COUNT(*) FROM V$LOG GROUP BY THREAD#
         UNION
         SELECT 'Standby logfile groups in thread ' || THREAD# || ': ' || COUNT(*) FROM V$STANDBY_LOG GROUP BY THREAD#;
         

The following example has four online redo logs per thread, and does not have any standby redo log groups created. Since there are four online redo log groups, five standby redo log groups must be created for each thread:
         
         Logfile groups in thread 1: 4
         Logfile groups in thread 2: 4
         

  4. If enough standby redo log groups exist, skip this step. Standby redo log groups must be the same size as each online redo log group. Create the necessary number of standby redo log groups with the following PL/SQL code:
         
         SET FEEDBACK OFF
         SET SERVEROUTPUT ON
         DECLARE
           CURSOR cur_thread IS
             SELECT THREAD# THREAD, COUNT(*) COUNT FROM V$LOG GROUP BY THREAD#;
           standbylog_count NUMBER := 0;
           standbylog_group NUMBER := 0;
           standbylog_size NUMBER := 0;
           last_group_number NUMBER;
           sqlstmt VARCHAR2(200);
         BEGIN
           SELECT MAX(GROUP#), MAX(BYTES)
         INTO last_group_number, standbylog_size
         FROM V$LOG;
           standbylog_group := last_group_number + 1;
           FOR rec_thread IN cur_thread LOOP
         standbylog_count := rec_thread.count + 1;
         FOR i IN 1..standbylog_count LOOP
           sqlstmt := 'ALTER DATABASE ADD STANDBY LOGFILE THREAD ' || rec_thread.thread || ' GROUP ' || TO_CHAR(standbylog_group) || ' SIZE ' || standbylog_size || ';';
           DBMS_OUTPUT.PUT_LINE( sqlstmt);
           standbylog_group := standbylog_group + 1;
         END LOOP;
           END LOOP;
         END;
         /
         SET FEEDBACK ON
         

The following example output instructs you to create five standby redo log groups for each of the two threads:
         
         ALTER DATABASE ADD STANDBY LOGFILE THREAD 1 GROUP  9 SIZE 2147483648;
         ALTER DATABASE ADD STANDBY LOGFILE THREAD 1 GROUP 10 SIZE 2147483648;
         ALTER DATABASE ADD STANDBY LOGFILE THREAD 1 GROUP 11 SIZE 2147483648;
         ALTER DATABASE ADD STANDBY LOGFILE THREAD 1 GROUP 12 SIZE 2147483648;
         ALTER DATABASE ADD STANDBY LOGFILE THREAD 1 GROUP 13 SIZE 2147483648;
         ALTER DATABASE ADD STANDBY LOGFILE THREAD 2 GROUP 14 SIZE 2147483648;
         ALTER DATABASE ADD STANDBY LOGFILE THREAD 2 GROUP 15 SIZE 2147483648;
         ALTER DATABASE ADD STANDBY LOGFILE THREAD 2 GROUP 16 SIZE 2147483648;
         ALTER DATABASE ADD STANDBY LOGFILE THREAD 2 GROUP 17 SIZE 2147483648;
         ALTER DATABASE ADD STANDBY LOGFILE THREAD 2 GROUP 18 SIZE 2147483648;
         

  5. Verify the standby redo logs are set up correctly for your configuration:
         
         SELECT 'Logfile groups in thread ' || THREAD# || ': ' || COUNT(*) FROM V$LOG GROUP BY THREAD#
         UNION
         SELECT 'Standby logfile groups in thread ' || THREAD# || ': ' || COUNT(*) FROM V$STANDBY_LOG GROUP BY THREAD#;
         

The following output has four online redo log groups per thread and five standby redo log groups per thread:
         
         Logfile groups in thread 1: 4
         Logfile groups in thread 2: 4
         Standby logfile groups in thread 1: 5
         Standby logfile groups in thread 2: 5
         

  6. Exit SQL*Plus:
         
         EXIT;
         




### Copy the database parameter and password files to the standby servers

  1. Create a database parameter file and copy it to the standby server:

     1. Create a folder for the standby database parameter file (`pfile`):
            
            mkdir /home/oracle/backup
            

     2. Start SQL*Plus, then create the standby database `pfile`:
            
            sqlplus / as sysdba
            
            
            CREATE PFILE='/home/oracle/backup/initDBDG_SITE21.ora' FROM SPFILE;
            

     3. Exit SQL*Plus, then copy the `pfile` to the first Bare Metal Solution server in the standby location:
            
            EXIT;
            
            
            scp /home/oracle/backup/initDBDG_SITE21.ora ORACLE_USERNAME@site2db1:/apps/oracle/19.0.0/db_home1/dbs/initDBDG_SITE21.ora
            

  2. Make sure the SYS remote login password is saved securely. If you don't know the password, [reset it](https://docs.oracle.com/en/database/oracle/oracle-database/19/dbseg/managing-security-for-oracle-database-users.html#GUID-E2DEFD1B-E310-432B-8DE8-01FFFAFB4F1A).

  3. Copy the password file to the standby cluster:

     1. Get the location of the password file by using the `srvctl` command:
            
            srvctl config database -db DBDG_SITE1 | grep -i password
            

The following output shows the location of a password file store in ASM:
            
            Password file: +DATA/DBDG_SITE1/PASSWORD/pwdDBDG_SITE1.287.1086459663
            

     2. Make a temporary copy of the password file on the local filesystem by using the `asmcmd` command:
            
            asmcmd cp +DATA/DBDG_SITE1/PASSWORD/pwdDBDG_SITE1.287.1086459663 /tmp/orapwDBDG_SITE21
            

     3. Copy the password file to the first Bare Metal Solution server in the standby location, and then delete the temporary copy from the Bare Metal Solution server in the primary location:
            
            scp /tmp/orapwDBDG_SITE21 ORACLE_USERNAME@site2db1:/apps/oracle/19.0.0/db_home1/dbs/orapwDBDG_SITE21
            rm /tmp/orapwDBDG_SITE21
            




### Configure the database connectivity

Edit the `$ORACLE_HOME/network/admin/tsnames.ora` file on each Bare Metal Solution server in the primary database location to update the net service configuration. There are three entries in the file; one for each database, and a temporary entry used during database duplication that you will delete later:
    
    
    DBDG_SITE1 =
      (DESCRIPTION =
          (ADDRESS = (PROTOCOL = TCP)(HOST = DBDG_SITE1_SCAN_HOSTNAME)(PORT = 1521))
          (CONNECT_DATA =
              (SERVER = DEDICATED)
              (SERVICE_NAME = DBDG_SITE1) (UR=A)
          )
      )
    
    DBDG_SITE2 =
     (DESCRIPTION =
          (ADDRESS = (PROTOCOL = TCP)(HOST = DBDG_SITE2_SCAN_HOSTNAME)(PORT = 1521))
          (CONNECT_DATA =
              (SERVER = DEDICATED)
              (SERVICE_NAME = DBDG_SITE2) (UR=A)
          )
      )
    
    DBDG_SITE2_FOR_DUPLICATION =
      (DESCRIPTION =
          (ADDRESS = (PROTOCOL = TCP)(HOST = site2db1)(PORT = 1523))
          (CONNECT_DATA =
              (SERVER = DEDICATED)
              (INSTANCE_NAME = DBDG_SITE21) (UR=A)
          )
      )
    

The primary database is now ready to be used in a Data Guard configuration.

## Next steps

Next, [create Data Guard's standby database](https://docs.cloud.google.com/bare-metal/docs/solutions/oracle/data-guard-setup/db-setup-standby).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
