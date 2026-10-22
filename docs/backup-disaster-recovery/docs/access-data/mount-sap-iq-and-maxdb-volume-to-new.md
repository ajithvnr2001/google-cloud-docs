---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sap-iq-and-maxdb-volume-to-new/
title: Recover SAP IQ and SAP MaxDB databases to a new target in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:52.042446+00:00
---

# Recover SAP IQ and SAP MaxDB databases to a new target in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sap-iq-and-maxdb-volume-to-new/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Recover SAP IQ and SAP MaxDB databases to a new target in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Both of these procedures require you to customize and run a config file.

The following sections detail how to recover a volume-based backup of an SAP IQ or SAP MaxDB database to a new location.

  * To recover a volume-level backup of an IBM Db2, PostgreSQL, SAP ASE, SAP IQ, or SAP MaxDB database to a new target, you can also use the [instant mount and migrate of a database to a new target](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/otherdb-mount-and-migrate) procedure.

**Note:** Mount and migrate is a quick mount; the database is immediately available from the staging disk, then the data moves in the background from the staging disk to the target storage. If users are active in the database, this takes time and impacts performance.   
The restore procedures on this page keep the database down for the entire time of the restore procedure, often some hours, but at the end the database is available on the target storage at full performance, with no impact of background migration or reading from a staging disk.
  * To recover a Full+Incremental backup of an IBM Db2, PostgreSQL, SAP ASE, SAP IQ, and SAP MaxDB databases to a new target, see [Recover a Full+Incremental backup of other databases to a new target](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/otherdb-recover-dump-to-new).




## Recovery procedure

To recover a volume-level backup to a new target, follow these steps:

  1. From the Backup and DR appliance management console, open the **App Manager**. 
  2. Right-click the protected database and select **Access**. You can use the **Managed Backup Plan** status filter to show only protected databases.

  3. Select the latest snapshot to recover, and choose **Mount**.

  4. Provide a target mount point under mount location, for example, `/dmpRstNew`. This is used as the variable TARGET_MNT_PNT.

The database backup is mounted under /dmpRstNew (TARGET_MNT_PNT) and the log backup is mounted under /dmpRstNew_archivelog (LOG_BKP_MNTPT).

  5. Log into the database server as root. Change the directory to `/act/custom_apps/<database type>/restore`.

  6. Run the script.

### SAP IQ
         
         /act/custom_apps/sybaseiq/restore/act_sybaseiq_lvm_customdb_recovery.sh TARGET_MNT OSUSER CATALOG_DB_FILE SRC_DB_DBA_USER SRC_DB_DBA_PWD LOG_BKP_MNTPT RECOVERY_TIME JOBID INCR_BKP_LOC
         

**Note:** You can get ACT_JOBNAME from the appliance management console Monitor > Jobs tab.

After the script has run, connect to the IQ database and confirm that the databases are recovered and online.
         
         dbisql -c "uid=username;pwd=password;eng=engine name;dbn=database name;" -nogui
         

### SAP MaxDB
         
         /act/custom_apps/maxdb/restore/ACT_MAXDB_lvmRestore_newTarget.sh \
           OSUSER \
           TARGET_SERVER_NAME \
           TARGET_DB_USER \
           TARGET_DBUSER_PASSWD \
           SOURCE_DBSID \
           MANIFEST_FILE_LOC \
           SRC_DB_VERSION \
           ACT_JOBNAME \
           TARGET_MNT_PNT \
           LOG_BKP_MNTPT \
           UNTIL_TIME \
           BEGIN_TIME
         

**Note:** TARGET_DB_USER and TARGET_DBUSER_PASSWD must be the same as the source DBM username and password. You can change the password after the restore operation is finished.**Note:** You can get ACT_JOBNAME and TARGET_MNT_PNT from the appliance management console Monitor > Jobs tab.

Connect to the MaxDB database and confirm that the databases are recovered and online:
         
         dbmcli -d TARGET_SERVER_NAME -u TARGET_DB_USER,TARGET_DBUSER_PASSWD db_state
         

After the database is restored, take a dump database backup to generate a backup history point in backup_history_list, which is required to take log backups. For example, the following:
         
         dbmcli -d DB -u DBM_USER,DBM_PASSWORD -c backup_start TEMPLATE_NAME DATA AUTOIGNORE
         

Without this, future volume level backups fail with the error _fail to trigger autolog backup template_.

  7. Unmount the mounted snapshot.




## Change the password

In some cases, you may need to change the database password.

### SAP IQ

  1. Log into the target database. For a database named `TARGET_SERVER_NAME`, with db user `SRC_DB_DBA_USER` and password `SRC_DB_DBA_PWD`, the command to sign in is as follows.
         
         dbisql -nogui -onerror exit -c 'uid=SRC_DB_DBA_USER;pwd=SRC_DB_DBA_PWD;dbn=TARGET_DB_NAME;eng=TARGET_SERVER_NAME;
         

  2. Run the following command to change password.
         
         ALTER USER SRC_DB_DBA_USER IDENTIFIED BY NEW_PASSWORD
         

  3. Sign in again with new password to verify:
         
         dbisql -nogui -onerror exit -c 'uid=SRC_DB_DBA_USER;pwd=NEW_PASSWORD;dbn=TARGET_DB_NAME;eng=TARGET_SERVER_NAME;
         




### SAP MaxDB

  1. To change the password, sign in to the target database as DBM user:
         
         dbmcli -d TARGET_SERVER_NAME -u TARGET_DB_USER,TARGET_DBUSER_PASSWD
         user_changepwd dbm new_password
         

For example, for a DBM user changing the password from abcdef to fedcba, sign in:

`dbmcli -d glxn -u dbm,abcdef`

  2. Run the following command:

`user_changepwd dbm abcdef`

  3. Sign in again with the new password:

`dbmcli -d glxn -u dbm,fedcba`




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
