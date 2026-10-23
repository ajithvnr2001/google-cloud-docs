---
url: https://docs.cloud.google.com/oracle/compute/gcnv-finalize-standby/
title: Finalize the standby database for Oracle Data Guard on NetApp Volumes \u00a0|\u00a0 Oracle on Google Cloud Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:53.345187+00:00
---

# Finalize the standby database for Oracle Data Guard on NetApp Volumes  |  Oracle on Google Cloud Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/compute/gcnv-finalize-standby/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Oracle on Google Cloud Compute ](https://docs.cloud.google.com/oracle/compute)
  * [ Guides ](https://docs.cloud.google.com/oracle/compute/overview)



Send feedback 

#  Finalize the standby database for Oracle Data Guard on NetApp Volumes Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to finalize the standby database for Oracle Data Guard.

To finalize the standby database, complete the following steps:

  1. Create standby redo log files.
  2. Enable flashback and start recovery.
  3. Enable redo shipping.
  4. Verify Data Guard state.



## Create standby redo log files

Create standby redo log files on both database hosts to support Fast-Start Failover. Size must be greater than or equal to the largest primary online redo log, and count should equal (online groups per thread) + 1. After NetApp Volumes seeding, drop and recreate standby redo logs on the standby to fix replicated paths.

  1. Create standby redo log files on the primary database (`orcl)`.
         
         ALTER SYSTEM SET db_create_file_dest='+DATA' SCOPE=BOTH;
         ALTER DATABASE ADD STANDBY LOGFILE THREAD 1 ('+DATA') SIZE 1024M;
         -- repeat (online log groups + 1) times
         

  2. Drop and recreate standby redo log files on the standby database (`orcls`) after NetApp Volumes seeding. Replicated paths under `+DATA/ORCL/…` cause `ORA-19527` and `ORA-16086` until rebuilt.
         
         ALTER DATABASE RECOVER MANAGED STANDBY DATABASE CANCEL;
         ALTER SYSTEM SET standby_file_management=MANUAL SCOPE=BOTH;
         -- DROP STANDBY LOGFILE GROUP for each group# in v$standby_log;
         ALTER SYSTEM SET db_create_file_dest='+DATA' SCOPE=BOTH;
         ALTER SYSTEM SET standby_file_management=AUTO SCOPE=BOTH;
         ALTER DATABASE ADD STANDBY LOGFILE THREAD 1 ('+DATA') SIZE 1024M;
         -- repeat (online groups + 1) times; one member per group
         ALTER DATABASE RECOVER MANAGED STANDBY DATABASE USING CURRENT LOGFILE DISCONNECT FROM SESSION;
         




## Enable flashback and start recovery

Enable flashback database on the standby to support automatic reinstatement after failover, then start managed recovery with real-time apply. Flashback must be enabled before starting managed recovery because it cannot be enabled while MRP is active.

  1. On `oracdb2`, shutdown the standby database, restart in `MOUNT` mode, and enable flashback database.
         
         # On oracdb2
         sudo -u oracle bash -c '
         . ~/.bash_profile
         export ORACLE_SID=orcls
         sqlplus / as sysdba <<SQL
         SHUTDOWN IMMEDIATE;
         STARTUP MOUNT;
         ALTER SYSTEM SET db_flashback_retention_target=1440 SCOPE=BOTH;
         ALTER DATABASE FLASHBACK ON;
         EXIT
         SQL'

  2. Start managed recovery with real-time apply:
         
         sudo -u oracle bash -c '
         . ~/.bash_profile
         export ORACLE_SID=orcls
         sqlplus / as sysdba <<SQL
         ALTER DATABASE RECOVER MANAGED STANDBY DATABASE USING CURRENT LOGFILE DISCONNECT FROM SESSION;
         EXIT
         SQL'




`USING CURRENT LOGFILE` enables real-time apply (redo applied as it lands in SRLs).

## Enable redo shipping

Enable redo transport from the primary to the standby by activating `LOG_ARCHIVE_DEST_STATE_2`, which was deliberately set to `DEFER` in [Step: Prepare the standby database password file and NOMOUNT](https://docs.cloud.google.com/oracle/compute/gcnv-create-standby-database#prepare-standby-pfile-nomount) of the standby provisioning procedure to suppress `ORA-12154` errors during standby creation.

  1. Switch `LOG_ARCHIVE_DEST_STATE_2` to `ENABLE` and force a log switch to initiate redo shipping:
         
         sudo -u oracle bash -c '
         . ~/.bash_profile
         sqlplus / as sysdba <<SQL
         ALTER SYSTEM SET LOG_ARCHIVE_DEST_STATE_2=ENABLE SCOPE=BOTH;
         ALTER SYSTEM SWITCH LOGFILE;
         ALTER SYSTEM ARCHIVE LOG CURRENT;
         EXIT
         SQL'

  2. Verify redo shipping is working correctly:
         
         sudo -u oracle bash -c '
         . ~/.bash_profile
         sqlplus / as sysdba <<SQL
         SELECT dest_id, status, error FROM v\$archive_dest_status WHERE dest_id IN (1,2);
         EXIT
         SQL'
         # Expected: dest_id=2, STATUS=VALID, ERROR null.




If `dest_2` shows `ORA-12154`, bounce the primary. After [Step: Enable the broker](https://docs.cloud.google.com/oracle/compute/gcnv-configure-broker-fsfo-observer#enable-broker) on both databases, manage transport through `DGMGRL`.

## Verify Data Guard state

Verify that the primary database is in `READ WRITE` mode and the standby database is mounted with managed recovery applying redo logs.

  1. Verify the primary database role and open mode on `oracdb1`.
         
         sudo -u oracle sqlplus -s / as sysdba \
           <<<"SELECT database_role || ' | ' || open_mode FROM v\$database;"
         # Expected: PRIMARY | READ WRITE

  2. Verify the standby database role, open mode, and managed recovery status on `oracdb2`.
         
         gcloud compute ssh oracdb2 --tunnel-through-iap --zone=us-west1-b
         
         
         sudo -u oracle bash <<'BASH'
         . ~/.bash_profile
         export ORACLE_SID=orcls
         
         sqlplus -s / as sysdba <<'SQL'
         SELECT database_role || ' | ' || open_mode
         FROM v$database;
         
         SELECT process, status, sequence#
         FROM v$managed_standby
         WHERE process IN ('MRP0','RFS');
         
         EXIT
         SQL
         BASH
         

Expected on the standby: `PHYSICAL STANDBY | MOUNTED; MRP0` with `APPLYING_LOG`.

  3. If the standby reports `MOUNTED` but apply is not running, restart managed recovery on `oracdb2`:
         
         sudo -u oracle bash -c '
         . ~/.bash_profile
         export ORACLE_SID=orcls
         sqlplus / as sysdba <<SQL
         ALTER DATABASE RECOVER MANAGED STANDBY DATABASE CANCEL;
         ALTER DATABASE RECOVER MANAGED STANDBY DATABASE USING CURRENT LOGFILE DISCONNECT FROM SESSION;
         EXIT
         SQL'
         




## What's next

  * [Configure Data Guard Broker, FSFO, and Observer](https://docs.cloud.google.com/oracle/compute/gcnv-configure-broker-fsfo-observer).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
