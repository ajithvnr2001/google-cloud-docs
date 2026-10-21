---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-and-recover-sap-hana-single-tenant/
title: Mount and recover an SAP HANA single-tenant database from a Persistent Disk backup in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:45:01.228065+00:00
---

# Mount and recover an SAP HANA single-tenant database from a Persistent Disk backup in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-and-recover-sap-hana-single-tenant/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Mount and recover an SAP HANA single-tenant database from a Persistent Disk backup in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

To restore and recover a single tenant from a persistent disk-based SAP HANA database backup, follow these steps.

## Mount the backup

Use the appliance management console to mount the backup to the target server:

  1. Stop the running HANA instance (required only for recovery to the source).
  2. Log into the appliance management console to the **Applications** page.
  3. Select the database and select **Access**.
  4. Select the backup to recover and click **Mount**.
  5. On the Mount page, select the target **Project name** , **Region** , **Zone** , and target **GCE instance name**.
  6. Update the **Data volume** , **Log volume** , and **Log backup volume** mount location. (To ensure preflight succeeds, specify all mount locations that are unused.)
  7. Disable the **Snapshot integrity check** option.
  8. Run the **Pre-Flight Check**. If it fails, address the errors and run it again, then submit the job.
  9. Once the Mount job is completed successfully, you can see the mount points on the target host.
  10. If you recovered to the source, then restart the instance.



## Recover a mounted single tenant database

Example variables used:

  * Source DBSID: DM2
  * Target DBSID: NVM (Must be pre configured on the target host.)
  * Data Volume: /hana/data_2
  * Log Volume: /hana/log_2
  * Log Backup Volume: /hanabackup_2, /hana/backup_2_533788010
  * Source Tenant: DM2 (data file locations: mnt00001/hdb00002.00003, mnt00001/hdb00003.00003)
  * Target Tenant: NVM



**Procedure**

  1. Log into the target host as root user and change the ownership of the files:
         
         chown -R nvmadm:sapsys /hanabackup_2 /hana/backup_2_533788010
         

  2. Confirm that the manifest file was created as part of the mount operation:
         
         cd /act/touch
         cat dm2_HANA.manifest
         

Example output looks like this: `SYSTEMDB=mnt00001/hdb00001` `DM2=mnt00001/hdb00002.00003:mnt00001/hdb00003.00003`

  3. Confirm that the necessary directory exists on the target server related to the tenant database displayed in the manifest file:
         
         ls -ltr /hana/data/NVM/mnt00001/hdb00002.00003/
         total 103252
         -rw-r--r-- 1 nvmadm sapsys         0 Jun 13 20:11 __DO_NOT_TOUCH_FILES_IN_THIS_DIRECTORY__
         -rw-r--r-- 1 nvmadm sapsys 269811712 Jun 14 19:26 datavolume_0000.dat
         
         ls -ltr /hana/data/NVM/mnt00001/hdb00003.00003/
         total 3801248
         -rw-r--r-- 1 nvmadm sapsys          0 Jun 13 20:11 __DO_NOT_TOUCH_FILES_IN_THIS_DIRECTORY__
         -rw-r--r-- 1 nvmadm sapsys 3892314112 Jun 14 19:29 datavolume_0000.dat
         

  4. Stop the tenant database on the target server:
         
         hdbsql -U ACTBACKUP
         hdbsql SYSTEMDB=> alter system stop database NVM;
         

  5. Copy the files from the mounted mount points to the target server mount point:
         
         cp /hana/data_2/DM2/mnt00001/hdb00002.00003/* /hana/data/NVM/mnt00001/hdb00002.00003/
         cp /hana/data_2/DM2/mnt00001/hdb00003.00003/* /hana/data/NVM/mnt00001/hdb00003.00003/
         

  6. Ensure the permissions are changed for the copied files:
         
         chown -R nvmadm:sapsys /hana/data/NVM/mnt00001/hdb00002.00003
         chown -R nvmadm:sapsys /hana/data/NVM/mnt00001/hdb00003.00003
         

  7. Check to ensure SYSTEMDB is started.

  8. Recover the tenant database using point-in-time recovery.

**Note:** The recovery range must be in UTC.
     * If the mounted database contains multiple log mount points, then pass the comma-separated mount points log path:
    
    hdbsql -jAU ACTBACKUP
    
    RECOVER DATABASE FOR NVM UNTIL TIMESTAMP '2024-06-14 17:16:00'  CLEAR LOG USING CATALOG PATH  ('/hana/backup_2_533788010/log/DB_DM2') USING DATA PATH ('/hana/data/NVM')  USING LOG PATH ('/hanabackup_2/log/DB_DM2','/hana/backup_2_533788010/log/DB_DM2') USING SNAPSHOT CHECK ACCESS USING FILE;
    

     * If you are recovering from database image only then use this command:
    
    hdbsql -jAU ACTBACKUP
    RECOVER DATA FOR $TSID USING SNAPSHOT CLEAR LOG
    

  9. Once the tenant database is recovered, check the status of the database:
         
         hdbsql -jAU ACTBACKUP
         
         hdbsql SYSTEMDB=> select * from m_databases;
         | DATABASE | DESCRIPTION     | ACT | ACTIVE | OS_USER  | OS_GROUP | RESTART | F |
         | -------- | --------------- | --- | ------ | -------- | -------- | ------- | - |
         | SYSTEMDB | SystemDB-NVM-00 | YES | ACTIVE |          |          | DEFAULT | ? |
         | NVM      | NVM-00          | YES | ACTIVE |          |          | DEFAULT | ? |
         

  10. Perform [unmount & delete](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount-delete) (to remove backup disks /hana/data_2, etc).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
