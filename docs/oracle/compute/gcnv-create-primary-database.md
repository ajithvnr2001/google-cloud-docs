---
url: https://docs.cloud.google.com/oracle/compute/gcnv-create-primary-database/
title: Create the primary database on NetApp Volumes \u00a0|\u00a0 Oracle on Google Cloud Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:53.793324+00:00
---

# Create the primary database on NetApp Volumes  |  Oracle on Google Cloud Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/compute/gcnv-create-primary-database/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Oracle on Google Cloud Compute ](https://docs.cloud.google.com/oracle/compute)
  * [ Guides ](https://docs.cloud.google.com/oracle/compute/overview)



Send feedback 

#  Create the primary database on NetApp Volumes Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create the primary database (in this case, `oracdb1`) using the Oracle Database Configuration Assistant (DBCA).

To create the primary database `oracdb1`, complete the following steps:

  1. Create a container database and a pluggable database on `oracdb1` by using the Oracle DBCA in silent mode against the ASM disk groups.
         
         sudo -u oracle bash -c '
         export ORACLE_HOME=/u01/app/oracle/product/26ai/db_1
         export PATH=$ORACLE_HOME/bin:$PATH
         
         dbca -silent -createDatabase \
           -templateName General_Purpose.dbc \
           -gdbname orcl -sid orcl \
           -characterSet AL32UTF8 -nationalCharacterSet AL16UTF16 \
           -sysPassword "ChangeMe!1" -systemPassword "ChangeMe!1" \
           -emConfiguration NONE \
           -datafileDestination +DATA -storageType ASM \
           -recoveryAreaDestination +FRA -recoveryAreaSize 25000 \
           -enableArchive true -archiveLogMode AUTO \
           -memoryMgmtType AUTO_SGA -totalMemory 4096 \
           -databaseType MULTIPURPOSE \
           -createAsContainerDatabase true -numberOfPDBs 1 \
           -pdbName orclpdb -pdbAdminPassword "ChangeMe!1" \
           -ignorePreReqs
         '

  2. Specify the destination where the redo log files are archived as `+RECO`. Open the pluggable database and save its state.
         
         sudo -u oracle bash -c '
         export ORACLE_HOME=/u01/app/oracle/product/26ai/db_1
         export ORACLE_SID=orcl
         
         $ORACLE_HOME/bin/sqlplus -s / as sysdba <<SQL
         ALTER SYSTEM SET log_archive_dest_1='\''LOCATION=+RECO VALID_FOR=(ALL_LOGFILES,ALL_ROLES) DB_UNIQUE_NAME=orcl'\'' SCOPE=BOTH;
         ALTER PLUGGABLE DATABASE ALL OPEN;
         ALTER PLUGGABLE DATABASE ALL SAVE STATE;
         EXIT
         SQL'
         

  3. Verify that the database is up and running.
         
         sudo /u01/app/26ai/grid/bin/srvctl status database -d orcl
         # Expected: Database is running
         
         sudo -u oracle sqlplus -s / as sysdba <<<"SELECT name, open_mode, log_mode FROM v\$database;"
         # Expected: ORCL, READ WRITE, ARCHIVELOG

  4. Create a role-based application service so that applications connect through `orclapp`, and the failover is transparent.
         
         sudo -u oracle bash -c '
         export GRID_HOME=/u01/app/26ai/grid
         export ORACLE_HOME=/u01/app/oracle/product/26ai/db_1
         export PATH=$ORACLE_HOME/bin:$GRID_HOME/bin:$PATH
         
         srvctl add service \
           -db orcl \
           -service orclapp \
           -pdb orclpdb \
           -role PRIMARY \
           -policy AUTOMATIC
         
         srvctl start service -db orcl -service orclapp
         srvctl status service -db orcl -service orclapp
         '




After the Oracle Data Guard Broker is enabled, `orclapp` runs only on the Primary database. For Multiplex control files across ASM disk groups, size memory to the workload.

## What's next

  * [Create the standby database](https://docs.cloud.google.com/oracle/compute/gcnv-create-standby-database).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
