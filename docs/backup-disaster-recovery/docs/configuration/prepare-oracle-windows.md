---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-oracle-windows/
title: Prepare Oracle databases in a Windows environment for Backup and DR on a backup/recovery appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:11.727091+00:00
---

# Prepare Oracle databases in a Windows environment for Backup and DR on a backup/recovery appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-oracle-windows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Prepare Oracle databases in a Windows environment for Backup and DR on a backup/recovery appliance Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

## Before you begin

Before you can discover, protect, and mount Oracle databases in a Windows environment, be sure to check the following:

  1. Check the following settings on the database server:

     1. The Oracle database and the Oracle Listener are up and running (check Windows services).

     2. Confirm that there is a tns entry with the name SID. The file tnsnames.ora is under
            
            %ORACLE_HOME%\network\admin
            

     3. Verify tns entry is valid by running:
            
            %ORACLE_HOME%\bin\tnsping <SID>
            

  2. Check if the log mode is set to Archive Log mode:
         
         sql> archive log list
         

If the database is in no-archive log mode, then return it to archive log mode:

**Note:** This will take down the database.
         
         sql> shutdown immediate;
         sql> startup mount;
         sql> alter database archivelog;
         sql> alter database open;
         

  3. Enable database change block tracking. With database BCT off, incremental backup time is impacted. Change block tracking feature is available in Oracle Enterprise Edition. Run a SQL query to check that change block tracking is enabled. Run the query:
         
         sqlplus / as sysdba
         sql> select * from v$block_change_tracking;
         




To enable change block tracking: 
    
    
        sql> alter database enable block change tracking
        using file '<Oracle home directory>\orcl.bct';
    

## Back up an Oracle database in a Windows environment

**Note:** Database authentication is not supported for Oracle in a Windows environment. OS authentication is fully supported.

To back up an Oracle database in a Windows environment, follow these steps:

  1. In the appliance management console set [Application Details & Settings for Oracle Databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-oracle).

  2. Apply a backup plan to protect the database.




**Known issue**

Oracle 19c SQL*Plus (sqlplus.exe) occasionally hangs on Windows when executing the exit command (Doc ID 2820655.1). This bug is specific to Windows. Oracle has confirmed that this issue occurs in SQL*Plus versions 19.10, 19.11 and 19.12. Oracle provided these solutions:

  * Use SQL*Plus 21.1 or later (or)
  * Apply patch:31466370. This patch is available for 19.11 and 19.13.



## Recover Oracle databases in a Windows environment manually using RMAN to a scheduled backup point if the archivelog is not protected through Backup and DR

To recover an entire Oracle database in a Windows environment:

  1. Mount the database backup snapshot from Backup and DR back to the Oracle server as detailed in [Mount an Oracle database as a standard mount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-oracle).

  2. Set the database environment and start the database in no-mount state using the parameter file from the Backup and DR mounted volume (for example for a mounted database volume to E:):
         
         sqlplus / as sysdba
         sql> startup nomount pfile='E:\<sid>___backup.ora';
         

  3. Create spfile from pfile:
         
         sql> create spfile='%ORACLE_HOME%\database\spfile<sid>.ora'
         from pfile='E:\<sid>___backup.ora';
         

  4. Start the database with spfile in the `nomount` state:
         
         sql> shutdown immediate;
         sql> startup nomount;
         

  5. Restore the control file using RMAN from the Backup and DR mounted volume:
         
         rman target /
         rman> restore controlfile from 'E:\cf-D_<sid>-id_<id>.ctl';
         

  6. Mount the database:
         
         rman> alter database mount;
         

  7. Catalog the datafile and the archive file folder from the Backup and DR mounted volume to RMAN:
         
         rman> run
         {
         catalog start with 'E:\datafile' noprompt;
         catalog start with 'E:\archivelog' noprompt;
         }
         

  8. Restore and recover the database:
         
         rman> run
         {
         restore database;
         recover database;
         }
         

  9. Open the database with reset log option:
         
         rman> alter database open resetlogs;
         




## Recover Oracle databases in a Windows environment manually using RMAN to a scheduled backup point with roll-forward of Backup and DR-protected archivelog

  1. Mount the backup from the source database server to recover. Mount the backup snapshot from Backup and DR back to the Oracle server as detailed in [Mount an Oracle database as a standard mount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-oracle).

  2. Set the database environment and start the database in no-mount state using the parameter file from the Backup and DR mounted volume. In this example, the database backup backup is mounted at: E:\ and the protected archive log is mounted at: Z:.
         
         sqlplus / as sysdba
         
         
         startup nomount pfile='E:\<sid>___backup.ora';
         

  3. Create spfile from pfile:
         
         sql> create spfile='%ORACLE_HOME%\database\spfile<sid>.ora' from
         pfile='E:\<sid>___backup.ora';
         

  4. Start the database with spfile in the nomount state:
         
         ```sql
         shutdown immediate;
         startup nomount;
         ```
         

  5. Restore the control file using RMAN from the Backup and DR mounted archive log backup:
         
         ```rman
         rman target /
         rman> restore controlfile from 'Z:\cf-D_<sid>-id_<id>.ctl';
         ```
         

  6. Mount the database:
         
         ```rman
         rman> alter database mount;
         ```
         

  7. Catalog the datafile and archivelog folder from Backup and DR mounted database backup and archive log backup to RMAN:
         
         ```rman
         rman> run
         {
         catalog start with 'E:\datafile' noprompt;
         catalog start with 'E:\archivelog' noprompt;
         catalog start with 'Z:\archivelog' noprompt;
         }
         ```
         

  8. Restore and recover the database:
         
         ```rman
         rman> run
         {
         restore database;
         recover database;
         }
         ```
         

For a specific point in time recovery run the recover command as follows:
         
         ```rman
         rman> run
          {
           restore database;
           recover database until time "to_date('<time stamp>','yyyymmddhh24mi')";
          }
          ```
         

  9. Open the database with reset log option:
         
         ```rman
         rman> alter database open resetlogs;
         ```
         

The database is available for read and write.




### Watch script to watch for database volumes being mounted

If you create an application-aware mount, then you can use a watch script to show the volumes being mounted from Backup and DR, and the Oracle processes running. Application-aware mounts are described in [Mounting an Oracle Database as a Virtual Application](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-oracle-virtualdb).

When performing an application-aware mount, you can use this watch script. The script location must be: C:\Program Files\Backup and DR\scripts. Scripts run on Windows hosts must be .bat or .vbs files.
    
    
        ```Windows
        @echo off
        :loop
        echo. > watchtemp
        echo ------------------ >> watchtemp
        echo  Oracle Processes >> watchtemp
        echo ------------------ >> watchtemp
        tasklist /svc | findstr oracle >> watchtemp
        echo. >> watchtemp
        echo ------------------ >> watchtemp
        echo   Backup and DR Mounts >> watchtemp
        echo ------------------ >> watchtemp
        wmic volume get label, name | findstr Backup and DR >> watchtemp
        echo. >> watchtemp
        cls
        type watchtemp
        timeout 2 > null
        goto loop
        ```
    

Which produces output like this:
    
    
        Oracle Processes
        ------------------
        oracle.exe                    1492 OracleServiceORCL
        oracle.exe                    3768 OracleServiceTestDB
        oracle.exe                     872 OracleServiceTestDB2
        ------------------
          Backup and DR Mounts
        ------------------
        Backup and DR-Backup-ORCL    D:\mount_1
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
