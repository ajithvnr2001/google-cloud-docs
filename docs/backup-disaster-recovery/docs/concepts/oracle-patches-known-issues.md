---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/oracle-patches-known-issues/
title: Oracle patches and known issues \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:11:42.715489+00:00
---

# Oracle patches and known issues  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/oracle-patches-known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)



Send feedback 

#  Oracle patches and known issues Stay organized with collections  Save and categorize content based on your preferences. 

These are the Oracle patches that must be applied for best results with Oracle in Backup and DR.

Oracle version | Needs patch | Due to these bugs | Notes  
---|---|---|---  
11.2.0.1 to 12.1.0.2.  |  19621704  |  ORA-00600 [723] [memory Leak] Error With Leaked Memory For "mbr node memory"  |  Backup and DR Application Aware mounts may fail   
11.x  |  Fixed in 12.x and later  |  Bug 19874632 - ORA-15196: INVALID ASM BLOCK HEADER [KFC.C:26368] [OBJ_KFBL] [8] [529] [3 != 8] (Doc ID 19874632.8)  |  This requires Oracle version 12.x and later.   
12.1+  |  Fixed in 19.1.0 and later  
See Oracle Doc ID 27424405.8 for patch details for your Oracle version from 12.1 to 19.1  |  RMAN: Restore of files greater than 32G can cause ORA-8103, ORA-600 [3020]  
RMAN might not backup all blocks from source.  |  Restore and recovery can fail with ORA-600.   
12.1.0.2  |  22709877  |  ORA-00600: INTERNAL ERROR CODE, ARGUMENTS: [KCVFDB_PDB_SET_CLEAN_SCN: CLEANCKPT]  |  Backup and DR Application Aware mount may fail   
Fixed in: 12.2.0.1+   
12.1.0.2 to 19c  |  26978857  |  CONTROLFILE BACKUP TO TRACE REFERS PDB DATAFILE OFFLINE IN CDB$ROOT CONTEXT  |  Backup and DR Application Aware mounts may fail.   
12.1.0.2  |  23019710  |  RMAN LIST BACKUP SUMMARY FAILS With any of:   
ORA-01507: database not mounted   
ORA-01219: database or pluggable database not open: queries allowed on fixed   
ORA-00972: identifier is too long   
ORA-01589: must use RESETLOGS or NORESETLOGS option for database open   
ORA-01426: numeric overflow   
ORA-01152: file 3 was not restored from a sufficiently old backup   
ORA-01110: data file 3:   
ORA-01109: database not open   
ORA-01034: ORACLE not available  |  Backup and DR Oracle backups may fail   
12.1.0.2  |  18845653  |  ORA-600 from PDB close if PDB renamed in another session  |  Backup and DR Application Aware mounts may fail. Fixed in 12.2.0.1+   
12.1.0.2  |  19075256  |  ORA-600 [kcfmis_internal: enq] from PDB RENAME  |   
12.1.0.2  |  22809813 (Win)   
19404068 (Linux)  |  ORA-1610 ON RECOVER DATABASE FOR CREATED CONTROLFILE  |  Backup and DR Application Aware mounts may fail.   
12.2 to 19c  |  30045273  |  PDB: ORA-00600 [KDSGRP1] / BLOCK INCONSISTENCIES AFTER DATABASE RECOVER FROM RMAN IMAGE COPIES USING NEW CONTROLFILE  |  Backup and DR Application Aware mounts may fail.   
12.2.0.2  |  31718134  |  ORA-00304: requested INSTANCE_NUMBER is busy  |  Restarting new database instance for the first time in no mount state may fail   
18c & 19c  |  30419450  |  ORA-65250: invalid path specified for file - /act/mnt/Staging_631487/datafile/24v0gutb_1_1  |  Backup and DR Oracle database backups may fail.   
Workaround until patch is installed: Unset parameter CREATE_FILE_DESTINATION for pluggable database.   
18.10 and later  |  Check with Oracle for interim patches for earlier versions.  |  Bug 29056767 - STANDBY: Datafiles Checkpoint not Updated at Standby Database when Media Recover is running (Doc ID 29056767.8)  |  Backup and DR Application Aware mounts may fail.  
Fixed in:   
19.4.0.0.190716 Jul 2019 DB RU   
18.8.0.0.191015 Oct 2019 DBRU   
20.10.   
19.14  |  34383066  |  Bug 34383066 - RMAN backup after upgrade to 19.14 hangs on release channel does not come back to prompt.  |  Backup and DR Oracle backups may hang.   
  
# Known Oracle issues

For best performance, be sure to review and address these Oracle known issues.

## Queries on DBA_FREE_SPACE are slow (Doc ID 271169.1)

During Backup and DR backup, the Backup and DR agent queries the **`dba_free_space`** Oracle metadata table to determine the database allocated and free space. Sometimes the sql queries to dba_free_space become costly. This is Oracle known issue Doc ID 271169.1 (Queries on `DBA_FREE_SPACE` are slow). This can be observed on a hung system by running `ps -ef | grep -i dbFreeSize.sql` from the command line.

Oracle recommends to purge the recycle bin from the database:

  1. Login to the database as sysdba:
         
         ```sh
         sqlplus / as sysdba
         SQL>purge dba_recyclebin;
         SQL>exit;
         ```
         

  2. It is a good idea to run the statistics on fixed objects. This can take a few minutes.

Log into the database as sysdba:
         
         ```sh
         sqlplus / as sysdba
         SQL>exec dbms_stats.GATHER_FIXED_OBJECTS_STATS
         SQL>exit;
         ```
         




See also ASM scalability and limits (from Oracle Doc ID 370921.1).

## Impact of `max_string_size=extended` parameter on application aware mounts, restore & switch restore

If the `max_string_size init` parameter is set to `extended` in the source database, then an app-aware mount or restore of the DB backup image taken before this parameter change along with roll-forward using log backups taken after this change fails with the error: **ORA-14694: database must be in UPGRADE mode to begin`MAX_STRING_SIZE` migration**

**Solution** If you set the `max_string_size init` parameter to `extended` in the source database, run a new on-demand level 1 (full) database backup job [1](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs#run) and use the new image for app-aware mount or restore operations.

## `SQLNET.AUTHENTICATION_SERVICES` must be set to nts in a Windows environment

On Windows, Oracle database sqlnet.ora is configured with `SQLNET.AUTHENTICATION_SERVICES` = (none). This restricts the database connection to using Windows operating system authentication. This requires a valid database username and password to connect to the database, without which restore jobs can fail.

Solution: Set `SQLNET.AUTHENTICATION_SERVICES` = (nts)

## ASM scalability and limits (from Oracle Doc ID 370921.1)

This depends on:

  * Oracle Database, Enterprise Edition

  * Oracle Database12c

  * With Oracle Exadata Storage

  * Without Exadata Storage, COMPATIBLE.ASM or COMPATIBLE.RDBMS disk group attribute < 12.1

  * Without Exadata Storage, COMPATIBLE.ASM and COMPATIBLE.RDBMS disk group attributes > 12.1




**Oracle Database, Enterprise Edition**

For Oracle Database, Enterprise Edition, Versions 10.1.0.2 to 11.1.0.7 and 11.2.0.3, ASM imposes the following limits:

  * 63 disk groups in a storage system

  * 10,000 ASM disks in a storage system

  * 2 terabyte maximum storage for each ASM disk (the Bug 6453944 allowed larger sizes, but that led to problems, see Note 736891.1 "ORA-15196 WITH ASM DISKS LARGER THAN 2TB")

  * 40 exabyte maximum storage for each storage system

  * 1 million files for each disk group

  * 2.4 terabyte maximum storage for each file




**Oracle Database12c**

For Oracle Database12c, ASM imposes the following limits:

  * 511 disk groups in a storage system for Oracle Database 12c Release 1 or later

  * 10,000 Oracle ASM disks in a storage system

  * 1 million files for each disk group




**With Oracle Exadata Storage**

With all Oracle Exadata Storage, Oracle ASM has the following storage limits:

  * 4 PB maximum storage for each Oracle ASM disk with the AU size equal to 1 MB

  * 8 PB maximum storage for each Oracle ASM disk with the AU size equal to 2 MB

  * 16 PB maximum storage for each Oracle ASM disk with the AU size equal to 4 MB

  * 32 PB maximum storage for each Oracle ASM disk with the AU size equal to 8 MB

  * 320 EB maximum for the storage system




**Without Exadata Storage, COMPATIBLE.ASM or COMPATIBLE.RDBMS disk group attribute < 12.1**

Without any Oracle Exadata Storage, Oracle ASM has the following storage limits if the COMPATIBLE.ASM or COMPATIBLE.RDBMS disk group attribute is set to less than 12.1:

  * 2 terabytes (TB) maximum storage for each Oracle ASM disk

  * 20 petabytes (PB) maximum for the storage system




**Without Exadata Storage, COMPATIBLE.ASM and COMPATIBLE.RDBMS disk group attri­butes > 12.1**

Without any Oracle Exadata Storage, Oracle ASM has the following storage limits if the COMPATIBLE.ASM and COMPATIBLE.RDBMS disk group attributes are set to 12.1 or greater:

  * 4 PB maximum storage for each Oracle ASM disk with the allocation unit (AU) size equal to 1 MB

  * 8 PB maximum storage for each Oracle ASM disk with the AU size equal to 2 MB

  * 16 PB maximum storage for each Oracle ASM disk with the AU size equal to 4 MB

  * 32 PB maximum storage for each Oracle ASM disk with the AU size equal to 8 MB

  * 320 exabytes (EB) maximum for the storage system




## The Oracle DBA Guide

  * [Backup and DR for Oracle databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/oracle-intro)
  * [Prerequisites for protecting an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prerequisites)
  * [Oracle patches and known issues](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/oracle-patches-known-issues)
  * [Prepare Oracle databases for protection](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prepare)
  * [Discover and protect an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-oracle)
  * [Details and settings for Oracle databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/oracle-advanced-settings)
  * [Use dNFS with Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-dnfs)
  * [Protect a discovered Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/oracle-db-protect)
  * [Mount an Oracle database as a standard mount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount)
  * [Create an instant virtual copy of an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount-virtualdb)
  * [Restore and recover an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-oracle)
  * [Instant recovery of an Oracle database using Mount and Migrate](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/oracle-mm)
  * [Provision an environment with a Backup and DR workflow](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/create-workflow-oracle)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
