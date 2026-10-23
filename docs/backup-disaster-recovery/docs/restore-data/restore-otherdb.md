---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-otherdb/
title: Restore other databases and instances to the source in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:39.501724+00:00
---

# Restore other databases and instances to the source in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-otherdb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Restore other databases and instances to the source in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

The Backup and DR **Restore** operation restores a backup image to the source, overwriting whatever data exists there. 

## System limitations and workarounds

  * System databases on a root partition backed up as logical volume manager (LVM) snapshots cannot be used in a restore operation because the root partition cannot be unmounted. These require manual restore and recovery from a standard mount back to the same host.  
To recover a volume-level database image with less downtime for users, see [Mount and migrate other types of databases for instant recovery](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/otherdb-mount-and-migrate).

  * Restoring back to the source is not supported if multiple instances share the same volume or file systems. To restore such applications, mount the image to the host and use the procedure to perform single database recovery detailed in Restore a single database from a volume-based backup image to the source.

  * If there are nested mount points under the production volumes being backed up, then restore and migrate operations back to the source fails because the production volumes are busy and cannot be unmounted.

  * To restore /backup-disaster-recovery/docs/restore-data/otherdb-restore




## Restore databases from a volume-level backup image to the source

This procedure uses physical recovery of the source data area. To recover back to the source, follow these instructions:

  1. From the **App Manager Applications** list, right-click the protected database and select **Access**. Use the **Managed Backup Plan** status filter to show only protected databases.

  2. Select a snapshot image and click **Restore**.

  3. Select **Traditional** —not mount and migrate.

  4. If the source application is protected by a snapshot policy that has enabled database log backups, and logs are available with the image, you can use them to roll forward to a specific point in time by changing these options in the **Roll Forward Time** section:

     * The date field contains all possible dates that the database can be rolled forward to—through the application of database transaction logs. Select which date you need the database to be rolled forward to.
     * The time field contains a slider showing all possible times on the selected date that the database can be rolled forward to. If you select the latest possible date and then move the slider to the right most position, the restore job applies to all available logs. If you select the earliest possible date and move the slider to the left most position, the restore job applies no logs.
     * You can specify to roll forward using either **User Time** or **Host Time**. **User Time** is relative to the local time of the current user. **Host time** is relative to the system that hosts the data to be restored.
  5. Enable **Restore With Recovery** to apply recovered logs.

  6. Click **Submit**.


**Note:** SAP IQ only. After the database has been restored, SAP IQ PITR (point-in-time recovery) logging must be set to ON to take a log backup. To configure the PITR log option, you need these SAP IQ API:
    
    
      ```sh
        ALTER DBSPACE IQ_SYSTEM_LOG RENAME /pitr_log_location
        SET OPTION PUBLIC.IQ_POINT_IN_TIME_RECOVERY_LOGGING = 'ON'
      ```
    

## Restore a single database from a volume-based backup image to the source

To restore a single Db2 or SAP ASE backup image to its source, follow these steps:

  1. From the **App Manager Applications** list, right-click the protected database and select **Access**.

**Note:** You can use the **Managed Backup Plan** status filter to show only protected databases.
  2. Select the latest snapshot to recover and click **Mount**.

  3. In the **Application Options** , disable **Create New Virtual Application**.

  4. In **Mapping Options** , provide the mount-point location. 

For example, using `/mymount` mounts the database backup under this location. The log backup is mounted under `/mymount_archivelog`.

  5. Click **Submit**.

  6. Check the **Monitor** > **Jobs** page to see when the mount job is finished.

  7. When the job is finished, log into the database server as root. On the server, change directory to `/act/custom_apps/<var>database type</var>/restore`.

  8. Get the `JobID` of the mount from `/var/act/log/UDSAgent.log`. To find the `JobID`, run the following command:
         
         grep "mount -t " /var/act/log/UDSAgent.log | grep -w "<var>mountpoint from step 4</var>"|tail -1
         

For example:
         
         grep "mount -t " /var/act/log/UDSAgent.log | grep -w "/db2mnt" |tail -1
         2019-11-18 23:59:19.740 GEN-INFO \[22488\] **Job_0404207** Spawning cmd: mount -t ext4 /dev/act403764_DBDump_1574101677612/act_staging_vol /db2mnt 2>&1
         

  9. `ARCHIVELOG_MNT` is `<var>mountpoint provided in step 4</var>_archivelog`.

  10. From the target host command line as root, run the script:




### IBM Db2

Script: `act_db2_lvm_customdb_recovery.sh`

Arguments to the script:
    
    
    SOURCE_INSTANCE = <var>Db2  Instance name</var>
    DB_NAME=<var>Db2 Database name to be recovered(Single)</var>
    TARGET_MNT = <var>Db2 Database image mountpoint name</var>
    ARCHIVELOG_MNT= <var>Archive Log backup mount point name</var>
    UNTIL_TIME = <var>Recovery Time(Format: "YYYY-MM-DD-HH.MI.SS")</var>
    JOBID = <var>Database mount Job name</var>
    

Connect to the Db2 instance and confirm that the databases are recovered and online.
    
    
    db2 connect to <var>dbname</var>
    db2 select db_status FROM SYSIBMADM.SNAPDB
    

### SAP ASE

Run the script act_sybase_lvm_customdb_recovery.sh with these arguments.
    
    
    ./act_sybase_lvm_customdb_recovery.sh OSUSER=sybase
    TARGET_SYBASE_SQLD=/home/sybase/Sybase16Home/OCS-16_0 TARGET_MNT_PNT=/sngRst
    TARGET_SERVER_NAME=ASE1 TARGET_DB_USER=sa STRIPEON=4 TARGET_DBUSER_PASSWD=sybase
    SRC_DBNAME=CU1 LOG_BKP_MNTPT=/sngRst_archivelog UNTIL_TIME="2019-11-07 20:31:27"
    BEGIN_TIME="2019-11-07 19:31:27" JOBID="Job_2677627"
    

Arguments to the script
    
    
    OSUSER = SAP Ase OS owner name
    TARGET_SYBASE_SQLD = SAP ASE iSQL path on the target recovery host
    TARGET_MNT_PNT = SAP ASE Instance image mountpoint name
    TARGET_SERVER_NAME = SAP ASE data server name on the target recovery host
    TARGET_DB_USER = SAP ASE Instance username on the target recovery host
    TARGET_DBUSER_PASSWD = SAP ASE Instance user password on the target recovery host
    SRC_DBNAME = SAP ASE Database name to be recovered (Single)
    LOG_BKP_MNTPT = SAP ASE Log image mountpoint name
    BEGIN_TIME= Backup begin time (Format: "YYYY-MM-DD HH24:MI:SS")
    UNTIL_TIME = Point in time to recover the database (Format: "YYYY-MM-DD HH24:MI:SS")
    JOBID = Database mount Job name
    

Connect to the SAP ASE database and verify the data.

  1. In the appliance management console, access the image again and **Unmount+Delete** the database mount point.



## Restore a file-based Full+Incremental backup image to the source

**Note:** SAP ASE databases protected with Full+Incremental based backup must have the same character set or sort order for both the source and target databases for a successful restore. For details refer to [SAP Note: 1860413 - How to change character set or sort order of SAP ASE](https://userapps.support.sap.com/sap/support/knowledge/en/1860413).

This procedure overwrites the source data. To restore the source database from a file-based backup image, follow this procedure:

  1. From the **App Manager Applications** list, right-click the protected database and select **Access**.

**Note:** You can use the **Managed Backup Plan** status filter to show only protected databases.
  2. Select a snapshot image and click **Restore**.

  3. Select **Traditional** —not mount and migrate.

  4. Use **Select Items** to choose one or more databases to restore.

  5. Enable **Restore With Recovery** to apply all recovered logs.

  6. Click **Submit**. This starts the source database physical recovery using the database's recovery API.


**Note:** SAP IQ only. After the database has been restored, SAP IQ PITR logging must be set to ON to take a log backup. To configure the PITR log option, you need these SAP IQ API:
    
    
      ALTER DBSPACE IQ_SYSTEM_LOG RENAME '/<var>pitr_log_location</var>'
      SET OPTION PUBLIC.IQ_POINT_IN_TIME_RECOVERY_LOGGING = 'ON'
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
