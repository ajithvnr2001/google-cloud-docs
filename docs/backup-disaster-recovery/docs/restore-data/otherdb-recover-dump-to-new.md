---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/otherdb-recover-dump-to-new/
title: Recover a Full+Incremental backup of other SAP databases to a new target in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:17.030527+00:00
---

# Recover a Full+Incremental backup of other SAP databases to a new target in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/otherdb-recover-dump-to-new/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Recover a Full+Incremental backup of other SAP databases to a new target in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

The following sections include information on recovering SAP ASE, SAP IQ, and SAP MaxDB databases from a Full+Incremental backup to a new target.

## Procedure

To restore a file-based backup to a new target, follow these instructions:

  1. From the **App Manager Applications** list, right-click the protected database and select **Access**.

**Note:** You can use the **Managed Backup Plan** status filter to show only protected databases.
  2. Select the latest snapshot to recover and click **Mount**.

  3. Provide a mount point under mount location, for example: `/mymountpoint`.

The database backup is mounted under `/mymountpoint` and the log backup is mounted under `/mymountpoint_archivelog`.

  4. Retrieve the `JobID` of the mount from `/var/act/log/UDSAgent.log` by running the following command:
         
         grep "mount -t " /var/act/log/UDSAgent.log | grep -w "(mountPoint provided in step 3)"|tail -1
         

For example:
         
         # grep "mount -t " /var/act/log/UDSAgent.log| grep -w "/db2mnp" |tail -1
         2019-11-18 23:59:19.740 GEN-INFO 22488 Job_0404207 Spawning cmd: mount -t ext4 /dev/act403764_DBDump_1574101677612/act_staging_vol /db2mnp 2>&1
         

  5. `ARCHIVELOG_MNT` is equal to _archivelog. Refer to step three.

  6. Login to the database server as root. On the server, change the directory to the following:
         
         cd /act/custom_apps/(database type)/dump
         

  7. Run the script from command line as root.

  8. Unmount the mounted dump backup.




## Required script

Before you can mount a database to a new target, you must prepare a script.

### SAP ASE
    
    
      /act/custom_apps/sybase/dump/ACT_SYBASE_dumprestore_newTarget.sh
      SYBOSUSER
      SRC_SYBASE_SQLD
      TARGET_DB_USER
      TARGET_DBUSER_PASSWD
      ACT_NAME
      TARGET_MNT_PNT
      SRC_DBNAME
      UNTIL_TIME
      BEGIN_TIME
      LOG_BKP_MNTPT
      SRC_PAGE_SIZE
    

Connect to the SAP ASE instance and confirm that the databases are recovered and online.
    
    
        isql -U<username> -P<password> -S<SAP ASE server name>
        sp_helpdb
        go
    

### SAP IQ
    
    
      /act/custom_apps/sybase/dump/ACT_SYBASE_dumprestore_newTarget.sh
      OSUSER
      TARGET_MNT
      SRC_DB_DBA_USER
      SRC_DB_DBA_PWD
      SYBIQ_HOME
      VERSION
      ACT_NAME
      CATALOG_DB_FILE
      LOG_BKP_MNTPT
    

Connect to the IQ database and confirm databases are recovered and online.
    
    
        dbisql -c "uid=<username>;pwd=<password>;eng=<engine name>;dbn=<database name>;" -nogui
    

### SAP MaxDB
    
    
      /act/custom_apps/maxdb/dump/ACT_Maxdb_dumpRestore_newTarget.conf
      OSUSER
      SRC_DBSID
      TARGET_DB_USER
      TARGET_DBUSER_PASSWD
      TARGET_SERVER_NAME
      DUMPBKPLOC
      DBADMIN_PWD
      UNTIL_TIME
      LOG_MNT_PNT
      DATA_MNT_PNT
      JobID
      MANIFEST_FILE_LOC
      LOG_BKP_MNTPT
      BEGIN_TIME
      SRC_DB_VERSION
    

**Note:** Target MAXDB Instance DBM username and password must be the same as the source DBM username and password or recovery fails. You can change the password after the restore is finished.

You can get these values by running the following commands:

  * DUMPBKPLOC:
        
        df -h | grep <DUMPBKPLOC> | awk '{print $NF}'
        cat /var/act/log/UDSAgent.log | grep -w <DUMPBKPLOC> | tail -1 | cut -d']' -f2 | cut -d' ' -f2
        

  * JobID:
        
        cat /var/act/log/UDSAgent.log | grep <JOBID> | awk -F"disk at " '{print $2}'
        

  * MANIFEST_FILE_LOC:
        
        cat /var/act/log/UDSAgent.log | grep -i "Manifest_File_" | awk -F"disk at " '{print $2}'
        

  * LOG_BKP_MNTPT:
        
        df -h | grep "_archivelog" | awk '{print $NF}'
        

  * BEGIN_TIME:
        
        cat /var/act/log/UDSAgent.log | grep "BEGIN_TIME" | awk -F"BEGIN_TIME=" '{ print $2 }' | cut -d' ' -f1-2 | cut -d'"' -f2
        

  * SRC_DB_VERSION:
        
        dbmcli -d <SRC_DBSID> dbm_version | grep "VERSION" | awk -F"= " '{print $2}'
        




Connect to the MaxDB instance and confirm that the databases are recovered and online:
    
    
        dbmcli -d <TARGET_SERVER_NAME> -u
        <TARGET_DB_USER>,<TARGET_DBUSER_PASSWD>
        db_state
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
