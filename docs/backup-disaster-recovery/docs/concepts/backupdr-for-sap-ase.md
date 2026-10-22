---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-ase/
title: Backup and DR for SAP ASE on a backup/recovery appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:59.141125+00:00
---

# Backup and DR for SAP ASE on a backup/recovery appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-ase/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Backup and DR for SAP ASE on a backup/recovery appliance Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

**Caution:** Beginning July 31, 2027, support for backing up SAP ASE databases using the appliance management console is deprecated. To learn more about this deprecation and alternative backup solutions, see [Migrate from legacy database backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations/migrating-legacy-databases).

This page introduces Backup and DR concepts and the procedures used to capture and access databases.

## Backup and DR data virtualization

A backup/recovery appliance is a highly scalable copy data management platform that virtualizes application data to improve the resiliency, agility, and cloud mobility of your business. It works by virtualizing data in much the same way other technologies have virtualized servers and networks. This lets you capture data from production systems, manage it in the most efficient way possible, and use virtual copies of the data however they are needed.

SAP ASE (formerly Sybase ASE) is a is a family of relational database management systems within SAP Information Management division that is centered on several relational database management system offerings. This DBA guide explains how to protect SAP ASE application consistent database data with Backup and DR in a Linux environment.

Backup and DR uses these SAP ASE backup APIs:

  * **Linux change block tracking and LVM snapshot** : SAP ASE quiesce database hold and quiesce database release API with Linux change block tracking and LVM snapshot.

  * **File-based backups** : SAP ASE dump database file-based backups API. This provides the Full+Incremental backups of the database in backup format. On recovery, the restore DB API recovers the database by physically overwriting the data area.

  * **Log backup** : During a log backup the dump transaction API called to dump logs to a Backup and DR log staging disk.




## How it works: Backup and DR volume-based backup with Linux CBT

Data backup and recovery follows these steps:

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

  3. Invoke Full + Incremental backup using the dump backup command, writing the backup to the mounted disk.

  4. Backup and DR takes an internal snapshot. Log backups are done in a similar fashion directly from the file-system at any schedule that you configure.

  5. For data recovery, Backup and DR instantly mounts the staging disk to the database server and initiates the database restore operation. Logs can be played to any point in time after the database is restored.

  6. For recovery, Backup and DR instantly mounts the staging disk to the database server and initiates the database restore operation. Logs can be played to any point in time after the database is restored.




## Capture data

Capturing data consists of four steps:

  1. Add servers that host databases.

  2. Discover the databases.

  3. Define Backup and DR policy templates and resource profiles according to your RPOs and RTOs.

  4. Assign Backup and DR policy templates and resource profiles to discovered databases. The jobs runs on schedule defined in the policy template.




## SAP ASE configurations support

SAP ASE primary and standby protection can be set from primary or the standby. Protection is at the instance level residing on protected LVM. Transaction log protection is from the primary instance only.

## What's next

[Prepare the database for Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/otherdb-prep-database)

## Other documentation for Backup and DR for SAP ASE

This page is one in a series of pages specific to protecting and recovering SAP ASE databases with Backup and DR. You can find additional information at:

  * [Backup and DR for SAP ASE](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/sap-ase-intro)
  * [Prepare the database for Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/otherdb-prep-database)
  * [Add a SAP ASE database host and discover databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/otherdb-add-host)
  * [Define policy templates and resource profiles](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template)
  * [Set application details and settings](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-otherdb)
  * [Check staging disk format and backup method](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/backup-method-staging-disk-otherdb)
  * [Protect the SAP ASE database and its logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/otherdb-protect)
  * [Mount a SAP ASE database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/otherdb-mounts)
  * [Recover SAP ASE Backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/otherdb-restore)
  * [Create a SAP ASE Backup and DR Workflow](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/otherdb-workflow)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
