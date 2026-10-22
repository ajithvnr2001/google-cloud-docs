---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/backup-method-staging-disk-otherdb/
title: Set staging disk format and backup method for other database types in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:36:16.275207+00:00
---

# Set staging disk format and backup method for other database types in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/backup-method-staging-disk-otherdb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Set staging disk format and backup method for other database types in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

These two settings determine the type of backup that you get. It is important to make sure they are set properly.

## Ensure that the staging disk format is set correctly

You set the staging disk format when you added the host. Before continuing, check the staging disk format to be sure that you can get the backup type that you need.

To check the staging disk format, follow these steps:

  1. From **Manage** , **Hosts** list, right-click the host and select **Edit**.

  2. Halfway down the **Edit Host** page, the **Staging Disk Format** is either **NFS** or **Block** :

     * **Block** : Block-based staging disks are the most useful for both Backup and DR and TDM usage. Backup and DR changed-block tracking is only available on block-based staging disks, and virtual databases can only be mounted to block-based staging disks.

     * **NFS** : NFS based staging disks permit only file-based backup with Full+Incremental file system backup. Select **NFS** only if **Block** is not an option in your network.

  3. If the staging disk format is set incorrectly, change it now and click **Save** before continuing.

**Note:** System databases on a root partition can be backed up as logical volume manager snapshots and later mounted as virtual databases, but they cannot be used in a **Restore** operation as the root partition cannot be unmounted. This needs manual restore and recovery from a standard mount back to the same host.



## Check the backup method to be used for this database or instance

The backup method determines the type of backup you get, either volume-level or file-based.

You set the backup method when you filled in the details and settings for this database. Before continuing, check the backup method to ensure that you get the backup type you need.

To configure the database backup plan settings, follow these instructions:

  1. Click **App manager** > **Applications**.

  2. Right-click the database and select **Manage backup plan**.

  3. Select **Details & settings**.

  4. Go to **Backup capture method**. Choose between two backup methods:

     * **Volume level backup** : Use volume level logical volume manager snapshots with change block tracking on Linux to a block-based staging disk. This option lets you create application aware virtual databases from the snapshots. The production instance or database must be present on the logical volume manager volume.

     * **Full+Incremental backup** : This is file-based backup and recovery. This file dump method does not support the creation of virtual databases. You can use this for both block and NFS staging disks. If you need to use NFS staging disks, then use this backup method. For most purposes, volume-level backups are a better choice.

A virtual database can be protected individually and the protection applies on the entire instance. You can include or exclude specific databases during the process using a database inclusion rule from the **Manage backup plan** pages.

  5. Click **Save** at the bottom of the page if changes were made to your settings.


**Note:** With one exception, protection is set for the entire Db2 instance. You can include or exclude specific databases during the process using a **Database Inclusion Rule** from the **Manage Backup Plan** pages. The exception is that a virtual database can be protected individually.

## What's next

[Protect the database or instance and its logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/otherdb-protect)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
