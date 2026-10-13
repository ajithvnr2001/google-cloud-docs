---
url: https://docs.cloud.google.com/sap/docs/backup-recovery-for-hana-on-bare-metal-instances/
title: Backup and recovery for SAP HANA on bare metal instances \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:18.912664+00:00
---

# Backup and recovery for SAP HANA on bare metal instances  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/backup-recovery-for-hana-on-bare-metal-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Backup and recovery for SAP HANA on bare metal instances Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the backup and recovery strategy recommended by Google Cloud, including best practices, for your SAP HANA systems running on Compute Engine bare metal instances, available with C3 and X4. 

Compute Engine bare metal instances let you run multi-terabyte SAP HANA workloads. Consequently, for such large workloads, specific settings and approaches are required to optimize their backup and recovery operations.

This document is meant for SAP Basis administrators who want to optimize SAP HANA systems running on bare metal instances. For information about SAP HANA backup and recovery that is not specific deployments on bare metal instances, see [Backup and recovery](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide#backup_and_recovery).

For information about the Compute Engine bare metal instances that are certified by SAP for use with SAP HANA, see [Bare metal machine types for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#bare-metal-machines-for-hana).

## Recommended backup strategy

The following table describes the backup strategy that Google Cloud recommends for SAP HANA systems running on C3 and X4 bare metal instances. To avoid resource contention, create backups during periods of lower processing activity.

Frequency | Activity  
---|---  
Weekly, at least once | Create a full system backup. You can do this by using the [ Backint](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery) feature of Google Cloud's Agent for SAP.   
Daily, at least once | Create a snapshot based backup of the SAP HANA data volume. You can do this by using the [ disk snapshot](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/disk-snapshot-backup-recovery) feature of Google Cloud's Agent for SAP.   
Every alternate day, at least once | Create a delta backup of the SAP HANA data volume.  
Every 15 minutes or less, depending on your database's configuration for log backup interval, or when the SAP HANA log segment becomes full | Create an SAP HANA log backup. You can do this by using the [ Backint](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery) feature of Google Cloud's Agent for SAP.  
At least once during a backup retention cycle | Do the following: 

  * Test the consistency of your backups.
  * Test your backups by performing test recovery operations. This helps verify that the backups are usable for recovering your database.

  
  
This backup strategy is based on the following considerations:

  * A [standard disk snapshot](https://docs.cloud.google.com/compute/docs/disks/snapshots) provides an incremental block device point-in-time data copy. This mechanism enables a significantly faster and more resource-efficient method to transfer large amounts of data from SAP HANA's primary block storage to a secondary, durable location such as Cloud Storage. This is required for a robust disaster recovery strategy.
  * Because disk snapshot based backups don't perform a logical integrity check on the page or block level, any inconsistency or corruption in your SAP HANA data volume gets copied to its disk snapshot. This is where a full system backup becomes necessary. A [Backint](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery) based, weekly, full-system backup provides an implicit consistency check and a verified way to recover your SAP HANA database in case there is a logical corruption in the snapshot of your SAP HANA data volume.
  * To recover your database to a specific point in time, which lets you meet your RPO objectives, you can combine [Backint](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery) based SAP HANA log volume backups with either disk snapshot backups or Backint based full database backups.



## Limitations

There are some limitations that apply to disk snapshot based backup and recovery when using Google Cloud's Agent for SAP. For information about these limitations, see [Limitations](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/disk-snapshot-backup-recovery#limitations).

## Customizations

To suit the RTO or RPO objectives of your organization, you can customize the recommended backup strategy given in this document by creating additional Backint or disk snapshot based backups.

For information about how to use Google Cloud's Agent for SAP to create these backups, see the following:

  * [Backup and recovery for SAP HANA by using Backint](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery)
  * [Backup and recovery for SAP HANA by using disk snapshots](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/disk-snapshot-backup-recovery)



## Best practices

The following are the backup and recovery best practices that Google Cloud recommends for SAP HANA systems running on bare metal instances:

  * **Backint configuration** : To achieve maximum performance during [Backint](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery) based backup and recovery operations, you must perform the following configurations:

    * For log backups, we recommend that you create a separate Backint configuration file and specify its path to the `log_backup_parameter_file` parameter in your SAP HANA `global.ini` file. And then in the Backint configuration file, set the following parameter values:

Parameter | Value  
---|---  
`parallel_streams` | 32  
`xml_multipart_upload` | `true`  
`rate_limit_mb` | 2500  
  
    * For data backups, we recommend that you set the following parameter values in your SAP HANA `global.ini` file:

Parameter | Value  
---|---  
`parallel_data_backup_backint_channels` | 32  
  
  * **Consistency and integrity checks** : To make sure that your backups are usable for recovering your database from any future disaster, you need to perform periodic consistency and integrity checks on your backups. The method you use to perform these checks depends on the method you use to create your backups.

    * For [Backint](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery) based backups, consistency check is performed during backup creation.

To check the integrity Backint based backups, you can use the [`hdbbackupcheck` tool](https://help.sap.com/docs/SAP_HANA_ONE/1c837b3899834ddcbae140cc3e7c7bdd/77522ef1e3cb4d799bab33e0aeb9c93b.html). This tool automatically performs integrity checks while your data and log backups are being created. If the integrity check is successful, then the backup file is written to the backup destination, such as Cloud Storage.

    * To check the consistency of [disk snapshot](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/disk-snapshot-backup-recovery) based backups, you can use the `hdbpersdiag` tool. For information about best practices related to disk snapshot based backup and recovery, see [Best practices](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/disk-snapshot-backup-recovery#best_practices).

For information about how to validate snapshot consistency by using Google Cloud's Agent for SAP, see [Validate snapshot consistency](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/perform-disk-snapshot-backup-recovery#validate_snapshot_consistency).

While this method of performing consistency checks involves considerable time and manual effort, it's required because snapshot based backups are not automatically checked for their consistency during backup creation, unlike Backint based backups.

  * **Backup recoverability checks** : To make sure that you can meet your RPO objectives, you need to make sure that your backups are available and usable. For this, you can use SAP's [`hdbbackupdiak` tool](https://help.sap.com/docs/SAP_HANA_ONE/1c837b3899834ddcbae140cc3e7c7bdd/f60cd67cd71846a9ae3da198a78f7851.html).

  * **Backup catalog housekeeping** : To avoid issues that you might experience because of a large number of entries and data in the SAP HANA backup catalog, you must maintain your backup catalog and backup storage. For more information, see the SAP document [Housekeeping for Backup Catalog and Backup Storage](https://help.sap.com/docs/SAP_HANA_ONE/1c837b3899834ddcbae140cc3e7c7bdd/cac903c28b0e4301b39814ef41dbf568.html).

Deleting the entry of a storage snapshot from the SAP HANA backup catalog does not delete the disk snapshot stored in Google Cloud. For information about how to delete a disk snapshot, see [Delete a snapshot](https://docs.cloud.google.com/compute/docs/disks/manage-snapshots#delete_a_snapshot).

  * **Database encryption** : SAP HANA lets you encrypt the data volume, log volume, and database backups. Enabling encryption on the data volume and database backups can have a negative impact on the performance of both backup and recovery operations. Make sure to take this impact into consideration when you're defining your RTO requirements, or your backup strategy.

While Google Cloud also provides options to encrypt the disks and disk snapshots related to your SAP HANA system, their impact on the performance of backup and recovery operations is minimal.

  * **Backup encryption** : Backint and disk snapshot based backups are encrypted at rest by default. However, to make them more secure, you can explore additional options. For information about these options, including their impact on database performance, see the following:

    * For Backint based backups, see [Encryption options for backups](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#encryption_options_for_backups).
    * For disk snapshot based backups, see [Encrypt disk snapshots](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/disk-snapshot-backup-recovery#encrypt_disk_snapshots).
  * **Long term retention** : To retain backups for longer periods, see the following:

    * For Backint based backups that are stored in Cloud Storage, you can define long-term retention by setting a retention policy on the Cloud Storage bucket. The retention policy defines how long the objects in the bucket are to be retained. For information about how to configure a bucket's retention policy, see [Bucket lock](https://docs.cloud.google.com/storage/docs/bucket-lock).

    * Disk snapshot based backups are retained by default. You need to create your own retention policy and delete them manually once you don't require them. Deleting an older snapshot doesn't invalidate a more recent snapshot. For more information, see [Snapshot deletion](https://docs.cloud.google.com/compute/docs/disks/snapshots#snapshot_deletion). For information about how to delete a snapshot, or how to delete multiple snapshots based on a filter, see [Manage disk snapshots](https://docs.cloud.google.com/compute/docs/disks/manage-snapshots).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
