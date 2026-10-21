---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-db2/
title: Backup and DR for IBM Db2 on a backup/recovery appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:52.609683+00:00
---

# Backup and DR for IBM Db2 on a backup/recovery appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-db2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Backup and DR for IBM Db2 on a backup/recovery appliance Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Db2 is a is a family of relational database management systems within IBM's Information Management division that is centered on several relational database management system offerings. This section explains how to protect Db2 application consistent database data with Backup and DR in Linux environments.

**Note:** If you are using Pacemaker HADR, then see [Configure Pacemaker-aware snapshots for IBM Db2 HADR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/configure-db2-pacemaker).

## Protection method

Db2 uses `WRITE SUSPEND` and `WRITE RESUME` (Persistent Disk snapshot backup) for both primary and secondary Db2 databases on a Compute Engine instance to incrementally back up data and log volumes from your Persistent Disks with application consistency.

Backup and DR stores multiple copies of each snapshot across multiple locations with automatic checksums to ensure the integrity of your data.

The following are Db2 backup APIs used by Backup and DR:

  * **Standby (HADR) database** : The `Db2 database deactivate` and `Db2 database activate` API are used for freeze and thaw.

  * **Db2 log backup** : Logs are flushed using `Db2 archive log for database`. During a log backup, the payload of the log segments is copied from the log area to the location specified by the parameter logarchmeth1.




## Protect IBM Db2 databases

To get started protecting your Db2 databases, go through the Db2 procedures in [Protect and recover an IBM Db2 database running in Compute Engine](https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/db2-on-gce-backup-recovery)

Backup and DR uses Persistent Disk snapshots to incrementally back up data and log volumes from your persistent disks with application consistency. Backup and DR stores multiple copies of each snapshot across multiple locations with automatic checksums to ensure the integrity of your data.

## What's next

[Prepare the database for Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/otherdb-prep-database)

## Other documentation for Backup and DR for IBM Db2

This page is one in a series of pages specific to protecting and recovering IBM Db2 databases with Backup and DR. You can find additional information at:

  * [Backup and DR for Db2](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/db2-intro)
  * [Prepare the database for Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/otherdb-prep-database)
  * [Add a Db2 database host and discover databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/otherdb-add-host)
  * [Define policy templates and resource profiles](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template)
  * [Set application details and settings](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-otherdb)
  * [Check staging disk format and backup method](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/backup-method-staging-disk-otherdb)
  * [Protect the Db2 database and its logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/otherdb-protect)
  * [Mount a Db2 database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/otherdb-mounts)
  * [Recover a Db2 backup to another location](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/otherdb-mount-and-migrate)
  * [Restore Db2 backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/otherdb-restore)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
