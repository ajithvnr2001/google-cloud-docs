---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-hana-scaleout/
title: Backup and DR for SAP HANA Scale-Out on a backup/recovery appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:17.537901+00:00
---

# Backup and DR for SAP HANA Scale-Out on a backup/recovery appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-hana-scaleout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Backup and DR for SAP HANA Scale-Out on a backup/recovery appliance Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).**Note:** This information is for SAP HANA Scale-Out instances. For Scale-Up and HA 1+1 configurations, see [Backup and DR for SAP HANA](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-hana).

## Protection methods

The most common protection method for SAP HANA databases and logs in Backup and DR is the SAP HANA `savepoint` API (Persistent Disk snapshot) for SAP HANA on a Compute Engine instance.

You can also protect HANA databases using either of the two following alternative protection methods:

  * SAP HANA `savepoint` API (LVM backup)
  * SAP `backint` API (Full+Incremental backup)



These methods are preferable only if you require HANA Scale-Out or if you have need for application-aware mounts or mount-and-migrate ability for HANA databases.

If you can use the Persistent Disk snapshot backup method, then go to [Backup and DR for SAP HANA](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-hana).

### SAP HANA `savepoint` API (Persistent Disk snapshot) for SAP HANA on a Compute Engine instance

Backup and DR uses Persistent Disk snapshots to incrementally back up data and log volume from your persistent disks with application consistency. Backup and DR stores multiple copies of each snapshot across multiple locations with automatic checksums to ensure the integrity of your data. Backup and DR supports SAP HANA 2.0 Scale-up and SAP HANA 2.0 HA (1+1) replication system.

### SAP HANA `savepoint` API (volume-level backup)

This method leverages an SAP HANA database internal snapshot based on savepoint stored in the data volumes area and in Linux change block tracking to take an efficient, space saving, incremental forever backup.

SAP HANA data is captured in application first format, according to a specified backup plan. A golden copy of that data is created and stored once, and is then updated incrementally with only the changed blocks of data in an incremental forever model. This provides the advantage of instantaneous mount and recovery of SAP HANA databases. Virtual copies of the data can be made available instantly for use, without proliferating physical copies and taking up additional storage infrastructure.

### SAP `Backint` API (Full+Incremental backup)

The older way of backing up SAP HANA is using the Backint API using hdbsql. The Backint API sends backups to a staging disk mapped to the SAP HANA host over iSCSI or NFS. In both approaches, there is a periodic full backup and the data captured is in a proprietary backup format and not in block format.

### Backup and DR supportability of different SAP HANA configurations

**Note:** See the important information at [SAP HANA studio, metadata, and backup images](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/recover-sap-hana#SAP-HANA-studio,-metadata,-and-backup-images).

Backup and DR can virtualize and protect the following:

  * **Single container system (HANA 1.0 or 2.0) dedicated** : In a single-container system the system database and tenant database are seen as a single unit and are administered as one.

  * **Multiple-container systems (HANA 2.0)** : Multiple isolated databases in a single SAP HANA system. These are referred to as multi-tenant database containers. A multiple-container system always has exactly one system database used for central system administration, and any number of multi-tenant databases (including zero), also called tenant databases.




This table lists all the supported HANA configurations and the backup methods that apply with each one.

  * HANA `SavePoint` API method is the preferred method when available, for all HANA configurations except for scale-out with shared storage.

  * The `backint` method is available for all HANA configurations.

  * HANA log backups are always handled automatically for all configurations and options.


Configuration | SAP HANA `savepoint` API | SAP HANA `backint`  
---|---|---  
SAP HANA 2.0 standalone or HA (1+1)  | Yes  | Yes   
Scale-out HANA 2.0, non-shared storage  | Yes, requires SPS 04 or higher  | Yes   
Scale-out HANA 2.0, shared storage  | No  | Yes   
Single container system (HANA 1.0)  | Yes, requires SPS 04 or higher  | Yes   
  
## What's next

[Prepare the database for Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-sap-hana-scaleout)

## Backup and DR documentation for SAP HANA Scale-Out

This page is one in a series of pages specific to protecting and recovering SAP HANA Scale-Out instances with Backup and DR. You can find additional information in the following pages:

  * [Backup and DR for SAP HANA Scale-Out](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-hana-scaleout)
  * [Prepare SAP HANA Scale-Out instances for backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-sap-hana)
  * [Add an SAP HANA Scale-Out host, and discover and protect its databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-sap-hana-scaleout)
  * [Configure staging disk format and backup method for SAP HANA Scale-Out](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/backup-method-staging-disk-sap-hana-scaleout)
  * [Set application details and settings for SAP HANA Scale-Out instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-sap-hana-scaleout)
  * [Back up HANA 1+n and HANA scale-out databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/back-up-sap-hana-scaleout)
  * [Restore and recover SAP HANA Scale-Out instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-sap-hana-scaleout)
  * [Mount an SAP HANA Scale-Out backup as a standard mount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sap-hana)
  * [Mount an SAP HANA Scale-Out backup as a virtual database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sap-hana-virtualdb)
  * [Mount and migrate an SAP HANA Scale-Out backup for instant recovery to any target](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-and-migrate-sap-hana)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
