---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-postgresql/
title: Backup and DR for PostgreSQL on a backup/recovery appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:27.527359+00:00
---

# Backup and DR for PostgreSQL on a backup/recovery appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-postgresql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Backup and DR for PostgreSQL on a backup/recovery appliance Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

**Caution:** Beginning July 31, 2027, support for backing up PostgreSQL databases using the appliance management console is deprecated. To learn more about this deprecation and alternative backup solutions, see [Migrate from legacy database backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations/migrating-legacy-databases).

PostgreSQL is a powerful, open source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workloads.

## PostgreSQL backup API used by Backup and DR

  * **Volume level (Linux change block tracking and LVM snapshot) backups** : Backup and DR uses the PostgreSQL `pg_start_backup(label)` and `pg_stop_backup()` commands when performing backups with Linux change block tracking and LVM snapshot.

  * **Full+Incremental (file-based traditional) backups** : Backup and DR uses the PostgreSQL `pg_dump` file-based backups commands. The `pg_dump` command doesn't have an option to capture incremental changes of a database, so each backup is a full database dump backup.

Restore of the database recovers the database by physically overwriting the data area.

  * **PostgreSQL log backup** : During a log backup, Backup and DR physically copies all the PostgreSQL WALs (`WriteAheadLog`). To purge logs, Backup and DR uses an OS-level command.




## How it works: Backup and DR volume-based backup with Linux CBT

Only changed blocks are tracked in the bitmap: no copy-on-writes, no I/O-intensive operations.

The following steps describe the process for data backup and recovery:

  1. The Backup and DR agent has CBT to track changed blocks in the database data area.

  2. The agent calls the database API to freeze or pause database for data backup.

  3. Agent creates LVM snapshot of database data area and synthesizes a bitmap.

  4. Agent call to database API to unfreeze database.

  5. Agent copies changed blocks to backup/recovery appliance, which then deletes the snapshot and catalogs the backup.

  6. The appliance issues an internal snapshot and synthesizes a point-in-time virtual full backup.

  7. For data recovery, Backup and DR instantly mounts a rewritable staging disk and brings the database online.




The quiesce or unquiesce command is run on the **primary** for a volume-level snapshot job:
    
    
    select pg_start_backup(<label>);
    select pg_stop_backup();
    

The quiesce and unquiesce commands are run on a **standby node** for a volume-level snapshot job:

If PostgreSQL version is 10.x or later:
    
    
    select pg_wal_replay_pause();
    select pg_wal_replay_resume();
    

If PostgreSQL version is 9.x:
    
    
    select pg_xlog_replay_pause();
    select pg_xlog_replay_resume();
    

## How it works: file-based backup

The following steps describe the process for how to perform data backup and recovery with file-based backups:

  1. Backup and DR agent is deployed in the database server.

  2. Mount staging disk on the database server.

  3. Invoke full backup using the dump backup command, writing the backup to the mounted disk.

  4. Backup and DR takes an internal snapshot. Log backups are done in a similar fashion directly from the file-system at any schedule that you configure.

  5. For data recovery, Backup and DR instantly mounts the staging disk to the database server and initiates the database restore operation. Logs can be played to any point in time after the database is restored.

**Note:** The `pg_dump` API doesn't have an option to capture incremental changes of a database, so each backup is a full database dump backup.



## What's next

[Prepare the database for Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/otherdb-prep-database)

## Other documentation for Backup and DR for PostgreSQL

  * [Backup and DR for PostgreSQL](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/postgresql-intro)
  * [Prepare the database for Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/otherdb-prep-database)
  * [Add a PostgreSQL database host and discover databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/otherdb-add-host)
  * [Define policy templates and resource profiles](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template)
  * [Set application details and settings](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-otherdb)
  * [Check staging disk format and backup method](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/backup-method-staging-disk-otherdb)
  * [Protect the PostgreSQL database and its logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/otherdb-protect)
  * [Mount a PostgreSQL database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/otherdb-mounts)
  * [Recover PostgreSQL Backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/otherdb-restore)
  * [Create a PostgreSQL Backup and DR Workflow](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/otherdb-workflow)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
