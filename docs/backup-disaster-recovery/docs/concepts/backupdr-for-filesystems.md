---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-filesystems/
title: Backup and DR for file systems on a backup/recovery appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:03.013983+00:00
---

# Backup and DR for file systems on a backup/recovery appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-filesystems/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Backup and DR for file systems on a backup/recovery appliance Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Backup and DR lets you capture data from production SMB and NFS file systems, manage it efficiently, and use virtual copies of the data for business requirements like backup, test and development, analytics, and AI.

When configuring a backup plan for a file system, you have the following settings to help ensure that you get exactly what you need:

  * Exclude Patterns and Include Patterns: You can exclude or include certain file types. Using either the Exclude Patterns or Include Patterns option, only the most crucial data is backed-up. Only files are excluded or included, this does not impact directories. A pattern can include wildcard characters. On Windows, files named pagefile.sys and hiberfil.sys that appear in the root directory of a drive are automatically ignored.

  * Start Paths: Specifies the point in the file share where backup starts. If the Start Path field is left blank, backup starts at the root directory of the file system to be backed-up.

    * Linux example: `/usr/local` backs up the `/usr/local` directory.

    * Windows example: `\\SERVERNAME\SHARENAME\abc` backs up the abc directory on the file share.

  * Prune Paths: A prune path specifies a point in the file system where directory traversals stop. If this field is left blank, the directory traversal descends into every subdirectory of the start paths being backed up.

    * Linux example: `/usr/local/lib` ensures that nothing within `/usr/local/lib` is copied, but all other directories and files in `/usr/local` are copied.

    * Windows example: `\\SERVERNAME\SHARENAME\abc` ensures that nothing within `\\SERVERNAME\SHARENAME\abc` is copied, but all other directories and files in `\\SERVERNAME\SHARENAME` are copied.

  * Service access point IP address: This allows the backup/recovery appliance to connect to the Backup and DR agent using the cluster resource IP and to back up the file system from the active cluster node.




## How it works example: Backup and DR volume-based backup with Linux CBT

Only changed blocks are tracked in the bitmap, there are no copy-on-writes or I/O-intensive operations.

The following steps describe the process for how to perform data backup and recovery with volume-based backups and CBT:

  1. The Backup and DR agent has CBT to track changed blocks in the file system.

  2. The agent calls the OS API to freeze or pause file changes.

  3. Agent creates a LVM snapshot of the file system and synthesizes a bitmap.

  4. Agent API call to unfreeze the file system.

  5. Agent copies changed blocks to backup/recovery appliance, which then deletes the snapshot and catalogs the backup.

  6. The appliance issues an internal snapshot and synthesizes a point-in-time virtual full backup.

  7. For data recovery, Backup and DR instantly mounts a rewritable staging disk and brings the file system online.




## What's next

[Manage hosts and their connected applications](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-hosts-and-their-connected-applications)

## Other documentation for Backup and DR for file systems

This page is one in a series of pages specific to protecting and recovering filesystems with Backup and DR. You can find additional information in the following pages:

  * [Backup and DR for file systems](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/filesystem-intro)
  * [Manage hosts and their connected applications](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-hosts-and-their-connected-applications)
  * [Configure application details and settings to protect file system data](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/configure-app-settings-for-filesystems)
  * [Apply a backup plan to protect a file system](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-plan-to-filesystem)
  * [Restore a file system to the source](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/filesystem-restore)
  * [Mount a file system or file share](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-file-system)
  * [Mount and migrate a file system for instant recovery to any target](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/filesystem-mount-and-migrate)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
