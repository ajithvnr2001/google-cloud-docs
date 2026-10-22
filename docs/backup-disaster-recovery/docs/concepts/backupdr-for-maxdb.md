---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-maxdb/
title: Backup and DR for SAP MaxDB on a backup/recovery appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:36:10.155729+00:00
---

# Backup and DR for SAP MaxDB on a backup/recovery appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-maxdb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Backup and DR for SAP MaxDB on a backup/recovery appliance Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

**Caution:** Beginning July 31, 2027, support for backing up SAP MaxDB databases using the appliance management console is deprecated. To learn more about this deprecation and alternative backup solutions, see [Migrate from legacy database backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations/migrating-legacy-databases).

SAP MaxDB is the database management system developed and supported by SAP SE. SAP MaxDB is available on Microsoft Windows, Linux, and Unix, and for the most prominent hardware platforms.

## How it works: Backup and DR volume-based backup with Linux CBT

Only changed blocks are tracked in the bitmap—no copy-on-writes or I/O-intensive operations.

Data backup and recovery with volume-based backups and CBT follows these steps:

  1. The Backup and DR agent has CBT to track changed blocks in the database data area.

  2. The agent calls the database API to freeze or pause database for data backup.

  3. Agent creates LVM snapshot of database data area and synthesizes a bitmap.

  4. Agent call to database API to unfreeze database.

  5. Agent copies changed blocks to backup/recovery appliance, which then deletes the snapshot and catalogs the backup.

  6. The appliance issues an internal snapshot and synthesizes a point-in-time virtual full backup.

  7. For data recovery, Backup and DR instantly mounts a rewritable staging disk and brings the database online.




## How it works: file-based backup

Data backup and recovery with file-based backups follows these steps:

  1. Backup and DR agent is deployed in the database server.

  2. Mount staging disk on the database server.

  3. Invoke Full+Incremental backup using the dump backup command, writing the backup to the mounted disk.

  4. Backup and DR takes an internal snapshot. Log backups are done in a similar fashion directly from the file-system at any schedule that you configure.

  5. For data recovery, Backup and DR instantly mounts the staging disk to the database server and initiates the database restore operation. Logs can be played to any point in time after the database is restored.

  6. For recovery, Backup and DR instantly mounts the staging disk to the database server and initiates the database restore operation. Logs can be played to any point in time after the database is restored.




## SAP MaxDB APIs

Backup and DR uses the following SAP MaxDB backup APIs:

  * **Linux CBT and LVM snapshot** : MaxDB `UTIL_EXECUTE SUSPEND LOGWRITER` and `UTIL_EXECUTE RESUME LOGWRITER` API with Linux CBT and LVM snapshot

  * **File-based backups** : MaxDB `dbmcli -d &lt;dbsid&gt; -u &lt;dbm_username&gt;,&lt;dbm_password&gt;backup_start` file-based backups API

This provides the full backup of the database in backup format. The prerequisite for data backup is to define the backup template first. Recovery API restore db recovers the database by physically overwriting the data area.

  * **MaxDB log backup** : MaxDB autolog backup must be enabled on the application side. Backup and DR copies the log backup files to staging disk with cp command. As Autolog Backup is enabled we use os command to purge the log backup.




## What's next

[Prepare the database for Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/otherdb-prep-database)

## Other documentation for Backup and DR for MaxDB

This page is one in a series of pages specific to protecting and recovering MaxDB databases with Backup and DR. You can find additional information at the following pages:

  * [Backup and DR for SAP MaxDB](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/maxdb-intro)
  * [Prepare the database for Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/otherdb-prep-database)
  * [Add a MaxDB database host and discover databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/otherdb-add-host)
  * [Define policy templates and resource profiles](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template)
  * [Set application details and settings](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-otherdb)
  * [Check staging disk format and backup method](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/backup-method-staging-disk-otherdb)
  * [Protect the MaxDB database and its logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/otherdb-protect)
  * [Mount a MaxDB database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/otherdb-mounts)
  * [Recover MaxDB Backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/otherdb-restore)
  * [Create a MaxDB Backup and DR Workflow](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/otherdb-workflow)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
