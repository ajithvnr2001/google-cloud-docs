---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-and-migrate-otherdb/
title: Mount and migrate other types of database backups for recovery to any target in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:44.481303+00:00
---

# Mount and migrate other types of database backups for recovery to any target in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-and-migrate-otherdb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Mount and migrate other types of database backups for recovery to any target in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

The Backup and DR mount and migrate feature allows near instant recovery of a volume-level database backup image. Full+Incremental backup images cannot use mount and migrate.

**Note:** Mount and migrate recovers entire instances. It cannot recover a single database in a database instance. For this you need [Recover other database types back to a new location](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/otherdb-recover-to-new).

Microsoft SQL server, Oracle, and SAP HANA databases have specific procedures for mount and migrate.

**Note:** Mount and migrate is a quick mount. The database is immediately available from the staging disk, then the data moves from the staging disk to the target storage. If users are active in the database, this takes time and impacts performance. [SAP IQ and SAP MaxDB databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/otherdb-recover-iq-max-volume-to-new) can also use a restore procedure with scripts to recover a volume image to a new target. This method keeps the database down for the entire time of the restore procedure, often some hours, but at the end the database is available on the target storage at full performance, with no impact of background migration or reading from a staging disk.

This page provides instructions for these other supported database types:

  * [IBM Db2](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/db2-intro)

  * [PostgreSQL](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/postgresql-intro)

  * [SAP ASE](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/sap-ase-intro)

  * [SAP IQ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/sap-iq-intro)

  * [SAP MaxDB](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/maxdb-intro)




You can access backup images for these databases in several ways:

  * [Restore to the source](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/otherdb-restore)
  * [Recover to a new target (SAP MaxDB and SAP IQ only)](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/otherdb-recover-to-new)
  * [Clone](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/clone)
  * [LiveClone](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/liveclone)
  * [Backup and DR Workflow](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/otherdb-workflow)
  * [Mount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/otherdb-mounts)



A mount and migrate operation lets you restore a database by first mounting it, and then migrating it to production storage or to a new location. Users have normal access to the database while it is mounted and during the migration step.

Once you have protected a database or instance with a volume-level backup image, you can mount it and migrate it:

  * Mount and migrate back to the source
  * Mount and migrate to a new instance



This page describes how to make standard and virtual database (application aware) mounts of the other types of databases.

## Mount and migrate back to the source

Use these instructions to mount a database from a backup image and migrate the mounted image back to the source.

  1. From the Backup and DR appliance management console, click **App Manager** > **Applications** , right-click the protected database and select **Access**. You can use the **Managed Backup Plan** status filter to show only protected databases.
  2. Disable the backup plan to be sure no new jobs interfere with this job.

### IBM Db2 only

[Mount the image as a standard mount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/otherdb-mounts#standard).

If under mount location, you use the mount point `/mydatabase`, then the following is true:

     * The database backup is mounted under `/mydatabase`
     * The log backup is mounted under `/mydatabase_archivelog`

Once the mount job is completed, run the mountrecover script with the parameters in **Arguments to the script**.

Location of the script: /act/custom_apps/db2/clone/ACT_DB2_mountrecover.sh
    
    /act/custom_apps/db2/clone/ACT_DB2_mountrecover.sh \
      TARGET_MNT \
      TARGET_INSTANCE \
      TARGET_DBNAME_LIST \
      UNTIL_TIME \
      JOBID
    

**Example**
    
    /act/custom_apps/db2/clone/ACT_DB2_mountrecover.sh TARGET_MNT=/db2gj \
      TARGET_INSTANCE=db2prod TARGET_DBNAME_LIST=ENG,TEST1,IND \
      UNTIL_TIME="2020-02-12 04.14.41" JOBID=Job_12332
    

### All other database types

[Mount the image as a virtual mount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/otherdb-mounts#block-based).

  3. When the mount operation completes successfully, the recovered database is operational from the backup/recovery appliance. The next step is to migrate the database to your production storage.




### Migrate the data from the backup/recovery appliance to the source

The following prerequisites must be met in order to migrate the data:

  * The local target host device shouldn't be in use by another process such as a running database since it needs to be taken offline or online at the start of the pvmove process.
  * The size of the target host LVM device must be equal to or more than the `BackupDR_mount_point` size.
  * Make sure /etc/fstab has the /dev/mapper entries for production data and log volumes.
  * Use the **df** command to learn the Backup and DR mount point.
  * To view the available target logical volume manager devices, use the **lvdisplay** command. You must specify the full logical volume path.
  * To view the job name use **Monitor** > **Jobs**.
  * All other values should be the same as those used during the mount.


  1. Once the mountrecover script is completed, run the migration script:

### IBM Db2
         
         /act/custom_apps/db2/restore/ACT_DB2_lvm_migrate_newtarget.sh \
           SOURCE_INSTANCE \
           TARGET_DBNAME_LIST \
           JOBID \
           ARCHIVELOG_LOC \
           DATAVOL_DISK_MAPPING
         

**Example**
         
         /act/custom_apps/db2/restore/ACT_DB2_lvm_migrate_newtarget.sh \
           SOURCE_INSTANCE=db2prod TARGET_DBNAME_LIST=TEST1,TEST2 JOBID=Job_4488748 \
           ARCHIVELOG_LOC=/db2gj_archivelog \
           DATAVOL_DISK_MAPPING=/db2gj/db2/data:/dev/mapper/vg00/vol_data,/db2gj/db2/log:/dev/mapper/vg01/vol_log
         

### PostgreSQL

Script: /act/custom_apps/postgresql/restore/ACT_POSTGRESQL_lvm_migrate_newTarget
         
         /act/custom_apps/postgresql/restore/ACT_POSTGRESQL_lvm_migrate_newTarget.sh \
           DATAVOL_DISK_MAPPING \
           BASEDIR \
           OSUSER \
           PORT \
           DBUSER \
           DBPASSWORD \
           JOBID
         

**Example**
         
         /act/custom_apps/postgresql/restore/ACT_POSTGRESQL_lvm_migrate_newTarget.sh \
           DATAVOL_DISK_MAPPING=/chtst/pgData10.3:/dev/mapper/actdevdatapg103_1594980385483/act_staging_vol \
           BASEDIR=/home/postgres/postgresql_home_10.3 OSUSER=postgres PORT=6010 \
           DBUSER=postgres JOBID=Job_0957580
         

### SAP ASE

Script: /act/custom_apps/sybase/lvm_migrate/ACT_SYBASE_lvm_migrate_newTarget.sh
         
         /act/custom_apps/sybase/lvm_migrate/ACT_SYBASE_lvm_migrate_newTarget.sh \
           DATAVOL_DISK_MAPPING \
           TARGET_SERVER_NAME \
           TARGET_DB_USER \
           TARGET_DBUSER_PASSWD \
           TARGET_DBNAME_LIST \
           JOBID
         

**Note:** Target logical volume manager devices should be empty.

**Example**
         
         /act/custom_apps/sybase/lvm_migrate/ACT_SYBASE_lvm_migrate_newTarget.sh \
            DATAVOL_DISK_MAPPING=/mntNT/log/CU1:/dev/mapper/vg2-lv2,/mntNT/data/CU1:/dev/mapper/vg2-lv1 \
            TARGET_SERVER_NAME=ASE1 TARGET_DB_USER=sa TARGET_DBUSER_PASSWD=sybase \
            TARGET_DBNAME_LIST=CU1:SU2 JOBID=Job_12345
          ```
         

### SAP IQ

Script: /act/custom_apps/sybaseiq/lvm_migrate/ACT_SYBASEIQ_lvm_migrate_newTarget.sh
         
         /act/custom_apps/sybaseiq/lvm_migrate/ACT_SYBASEIQ_lvm_migrate_newTarget.sh \
           DATAVOL_DISK_MAPPING \
           newDBNAME \
           DBA_USER \
           DBA_PASSWD \
           JOBID \
           NSTMNT_CHECK \
           PORTNO \
           DBFILE_LOC
         

**Example**
         
         /act/custom_apps/sybaseiq/lvm_migrate/ACT_SYBASEIQ_lvm_migrate_newTarget.sh \
          DATAVOL_DISK_MAPPING=/mr/iqlog:/dev/mapper/vg3-log,/mr/iqdata:/dev/mapper/vg3-data \
          newDBNAME=MR DBA_USER=act DBA_PASSWD=passwd JOBID=Job_123456 \
          NSTMNT_CHECK=TRUE PORTNO=2700 DBFILE_LOC=/home/sybaseiq/chdb
         

### SAP MaxDB

Script: /act/custom_apps/maxdb/lvm_migrate/ACT_MAXDB_lvm_migrate_newTarget.sh
         
         /act/custom_apps/maxdb/lvm_migrate/ACT_MAXDB_lvm_migrate_newTarget.sh \
           OSUSER \
           DBSID \
           DBUSER \
           DBPASSWORD \
           JOBID \
           LOCAL_PRG_PATH \
           DATAVOL_DISK_MAPPING
         

**Example**
         
         /act/custom_apps/maxdb/lvm_migrate/ACT_MAXDB_lvm_migrate_newTarget.sh \
          OSUSER=sdb DBSID=DEMODB DBUSER=dbm DBPASSWORD=password JOBID=Job_0377678 \
          LOCAL_PRG_PATH=/opt/sdb/MaxDB DATAVOL_DISK_MAPPING=/mmTST/maxdbdata:/dev/mapper/vg1-m7
         




The output is similar to this:
    
    
    INFOMSG: pvmove starting ......................
    + pvmove
      /dev/sdi: Moved: 47.07%
      /dev/sdi: Moved: 70.43%
      /dev/sdi: Moved: 93.83%
    

When the job is successful, the data moves to the local production storage from backup/recovery appliance-provisioned disks while the database is running. You can validate that the file system for the database created by the mount should now be on a local logical volume rather than the logical volume presented by the mount by running the **df** command.

  1. Once the job is successful, the data is moved to the local production storage from disks provisioned from the backup/recovery appliance while the database is running.
  2. Go to the appliance management console and perform **Unmount+Delete**.
  3. Re-enable the backup plan to trigger the scheduled jobs.



## Mount and migrate to a new instance

To mount a database image as a virtual database and then migrate it to a new target, perform an application aware mount as detailed in [Mount a virtual database from a volume-level backup image](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/otherdb-mounts#block-based).

**Note:** Enable both **Create New Virtual Application** and **Manage New Application**.

### Migrate the data

The prerequisites for migrating data are listed here:

  * The local target host device mustn't be in use by another process such as a running database since it needs to be taken offline or online at the start of the `pvmove` process.
  * Check that the size of target host logical volume manager device is equal to or more than **BackupDR_mount_point** size.
  * Check that /etc/fstab has the /dev/mapper entries for production data and log volumes.
  * Use the **df** command to learn the Backup DR mount point.
  * View available target logical volume manager devices using the **lvdisplay** command. You need to specify the full logical volume path.
  * Use **Monitor** > **Jobs** to view the job name.
  * All other values should be the same as those used during the mount.


  1. Once the mount is completed, run the `ACT_<database type>_lvm_migrate_newtarget` script with the parameters in the arguments to the script sections.

### IBM Db2

Script: /act/custom_apps/db2/restore/ACT_DB2_lvm_migrate_newtarget.sh
         
         /act/custom_apps/db2/restore/ACT_DB2_lvm_migrate_newtarget.sh \
           SOURCE_INSTANCE \
           TARGET_DBNAME_LIST \
           JOBID \
           ARCHIVELOG_LOC \
           DATAVOL_DISK_MAPPING
         

**Example**
         
         /act/custom_apps/db2/restore/ACT_DB2_lvm_migrate_newtarget.sh \
           SOURCE_INSTANCE=db2prod TARGET_DBNAME_LIST=TEST1,TEST2 \
           JOBID=Job_4488748 ARCHIVELOG_LOC=/db2gj_archivelog \
           DATAVOL_DISK_MAPPING=/db2gj/db2/data:/dev/mapper/vg00/vol_data,/db2gj/db2/log:/dev/mapper/vg01/vol_log
         

### PostgreSQL

Script: /act/custom_apps/postgresql/restore/ACT_POSTGRESQL_lvm_migrate_newTarget.sh
         
         /act/custom_apps/postgresql/restore/ACT_POSTGRESQL_lvm_migrate_newTarget.sh \
            DATAVOL_DISK_MAPPING \
            BASEDIR \
            OSUSER \
            PORT \
            DBUSER \
            DBPASSWORD \
            JOBID
          ```
         
         **Example**
         
         ```sh
          /act/custom_apps/postgresql/restore/ACT_POSTGRESQL_lvm_migrate_newTarget.sh \
            DATAVOL_DISK_MAPPING=/chtst/pgData10.3:/dev/mapper/actdevdatapg103_1594980385483/act_staging_vol \
            BASEDIR=/home/postgres/postgresql_home_10.3 OSUSER=postgres PORT=6010 \
            DBUSER=postgres JOBID=Job_0957580
          ```
         

### SAP ASE

Script: /act/custom_apps/sybase/lvm_migrate/ACT_SYBASE_lvm_migrate_newTarget.sh
         
         /act/custom_apps/sybase/lvm_migrate/ACT_SYBASE_lvm_migrate_newTarget.sh \
           DATAVOL_DISK_MAPPING \
           TARGET_SERVER_NAME \
           TARGET_DB_USER \
           TARGET_DBUSER_PASSWD \
           TARGET_DBNAME_LIST \
           JOBID
         

**Note:** Target logical volume manager devices should be empty.

**Example**
         
         /act/custom_apps/sybase/lvm_migrate/ACT_SYBASE_lvm_migrate_newTarget.sh \
          DATAVOL_DISK_MAPPING=/mntNT/log/CU1:/dev/mapper/vg2-lv2,/mntNT/data/CU1:/dev/mapper/vg2-lv1 \
          TARGET_SERVER_NAME=ASE1 TARGET_DB_USER=sa TARGET_DBUSER_PASSWD=sybase \
          TARGET_DBNAME_LIST=CU1:SU2 JOBID=Job_12345
         

### SAP IQ

Script: /act/custom_apps/sybaseiq/lvm_migrate/ACT_SYBASEIQ_lvm_migrate_newTarget.sh
         
         /act/custom_apps/sybaseiq/lvm_migrate/ACT_SYBASEIQ_lvm_migrate_newTarget.sh \
           DATAVOL_DISK_MAPPING \
           TARGET_DBNAME \
           DBA_USER \
           DBA_PASSWD \
           JOBID \
           NSTMNT_CHECK \
           PORTNO \
           DBFILE_LOC
         

**Example**
         
         /act/custom_apps/sybaseiq/lvm_migrate/ACT_SYBASEIQ_lvm_migrate_newTarget.sh \
           DATAVOL_DISK_MAPPING=/mr/iqlog:/dev/mapper/vg3-log,/mr/iqdata:/dev/mapper/vg3-data \
           newDBNAME=MR DBA_USER=act DBA_PASSWD=passwd JOBID=Job_123456 \
           NSTMNT_CHECK=TRUE PORTNO=2700 DBFILE_LOC=/home/sybaseiq/chdb
         

### SAP MaxDB

Script: /act/custom_apps/maxdb/lvm_migrate/ACT_MAXDB_lvm_migrate_newTarget.sh
         
         /act/custom_apps/maxdb/lvm_migrate/ACT_MAXDB_lvm_migrate_newTarget.sh \
         OSUSER \
         DBSID \
         DBUSER \
         DBPASSWORD \
         JOBID \
         LOCAL_PRG_PATH \
         DATAVOL_DISK_MAPPING \
         

Example:

/act/custom_apps/maxdb/lvm_migrate/ACT_MAXDB_lvm_migrate_newTarget.sh OSUSER=sdb DBSID=DEMODB DBUSER=dbm DBPASSWORD=password JOBID=Job_0377678 LOCAL_PRG_PATH=/opt/sdb/MaxDB DATAVOL_DISK_MAPPING=/mmTST/maxdbdata:/dev/mapper/vg1-m7



  1. When the job is successful, the data is moved to the local production storage from disks provisioned from the backup/recovery appliance while the database is running. Go to the appliance management console and perform an **Unmount+Delete**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
