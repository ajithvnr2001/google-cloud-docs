---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-filesystem/
title: Restore a file system to the source in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:26.522485+00:00
---

# Restore a file system to the source in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-filesystem/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Restore a file system to the source in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

The restore function reverts production data to a specified point in time. You can restore a local file system, mapped NFS file system, or mapped SMB file system to its original host, overwriting the existing file system.

## File system restoration

When you restore a file system, the backup/recovery appliance:

  * Replaces any files on the production disk with the version from the backup.
  * Adds to the production disk any files that are in the backup, even if they are no longer on the production disk.
  * Leaves in place any files on the production disk that are not in the backup.



In rare cases in which the production data resides on a disk or on an external storage pool presented by the backup/recovery appliance, restores replace the entire volume or block device, so the file system reverts to exactly what it was at the time of backup: Any files on the production disk that are not in the backup will no longer be on the production disk after restore.

The amount of time required to complete a restore operation depends on the amount of data involved.

## Restore a file system

Use these instructions to restore a file system from a backup.

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Select the backup that you want to restore, and then choose **Access** from the drop-down list at the bottom of the **Applications** page.

The **Access** page opens listing captured backups in the timeline ramp view. For more information on the view, see [Access the timeline ramp view of a backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/access-image-copy-data-list#access-time).

**Note:** If you are restoring an NFS backup, the **Advanced NFS Settings** must only be changed after consulting with your support representative.

A warning dialog opens.

  3. Read it and then enter `DATA LOSS` to confirm.

  4. Depending on your configuration, a second warning may appear. If so, you need to enter `OVERWRITE OTHER APPS` to confirm the restore operation.

The restore job starts. You can verify that the restore operation is successful by viewing the job status in **Monitor**.




## Restore a mapped SMB file system

Use these instructions to restore a point-in-time mapped SMB file system backup.

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Select the mapped backup that you want to restore.

  3. Choose **Access** from the drop-down list.

The **Access** page opens listing captured backups appear in the timeline ramp view. For more information on the view, see [Access the timeline ramp view of a backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-vm#restore-apps).

  4. Select a backup, then select **Restore** from the list of access operations.

The **Restore** page opens.

  5. Select a single volume or multiple volumes to restore. By default all volumes are selected.

  6. Click **Submit**.

A warning dialog appears.

  7. Read the dialog and enter `DATA LOSS` to confirm.

  8. Depending on your configuration, a second warning may appear. If so, you need to enter `OVERWRITE OTHER APPS` to confirm the restore operation.

The restore job starts. You can verify that the restore operation is successful by viewing the job status in **Monitor**.

**Note:** If you need a different username or password to access the SMB share during restore than was used during data capture—perhaps you had to change the password between the captured and restore process—you can click **Details & Settings** and modify the application-specific settings to add a new username or password—see [Configure application settings for file systems](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/configure-app-settings-for-filesystems).



## Restore a mapped NFS file system

Use these instructions to restore a mapped NFS file system backup.

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Select the mapped NFS backup that you want to restore, and then choose **Access** from the drop-down list at the bottom of the **Applications** page.

The **Access** page opens listing captured backups appear in the timeline ramp view. For more information on the view, see [Access the timeline ramp view of a backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/access-image-copy-data-list#access-time).

  3. Select a backup and then select **Restore** from the list of access operations.

The **Restore** page opens.

  4. Select a single volume or multiple volumes to restore. By default all volumes are selected.

  5. Click **Submit**. A warning dialog appears.

  6. Read the dialog and enter `DATA LOSS` to confirm.

  7. Depending on your configuration, a second warning may appear. If so, you must enter `OVERWRITE OTHER APPS` to confirm the restore operation.

The restore job starts. You can verify that the restore operation is successful by viewing the job status in **Monitor**.




## The file system administrator guide to Backup and DR

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
