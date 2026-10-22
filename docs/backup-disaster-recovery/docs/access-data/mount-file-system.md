---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-file-system/
title: Mount an NFS or SMB file system in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:36:00.582961+00:00
---

# Mount an NFS or SMB file system in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-file-system/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Mount an NFS or SMB file system in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

To mount any supported file system file share, follow these steps:

  1. From the Backup and DR appliance management console, open the **App Manager** > **Applications** list, right-click the relevant application and select **Access**.

**Note:** You can use the **Managed Backup Plan** status filter to show only protected applications.
  2. Select a backup image and choose **Mount**.

**Note:** For NFS, if you are mounting to a regular host, leave the **Host or VM** option as default. If you want to mount to a **Container** use the instructions in the [Mount an image to a container](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/consume-captured-app-data-in-a-container-environment).
  3. On the **Mount** page, from **Host** , choose the target host server from the drop-down.

  4. In **Label** , optionally enter a unique name associated with the mount.

  5. In **Mount Drive** or **Mount Point** enter the entire mount drive or point you want to use. If the image consists of multiple volumes, you can select a different mount drive or point for each volume. Mount drive is for Windows only.

  6. In the **Pre-Script** and **Post-Script** fields, enter the path and relative filenames. Enter the timeout values to prevent hanging. 300 seconds is a good recommended timeout value.

  7. Click **Submit**. Go to the **Job Monitor** to view the progress and details of the job. The mounted image is available in the Active Mounts.




## Management of the active mounts

Once you have created a mount, track the image from the **App Manager** > **Active Mounts**. Don't leave any image mounted indefinitely. This is because the backup image that the mount was created from cannot expire until all its mounts have been deleted. When you have finished using the mounted image, perform one of the following actions:

  * [Unmount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount) the image. You can [remount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#remount) it if needed. You can then [delete](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#delete) the image later when you are certain it is no longer needed.
  * [Unmount and delete](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount-delete) the image. This deletes the mounted image, not the backup that the mount is based on.



## What's next

  * To define backup settings, see [Configure application details and settings to protect file system data](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/configure-app-settings-for-filesystems)

  * To restore backed up file systems, see [File system restore](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/filesystem-restore)




## Backup and DR for file systems

This page is one in a series of pages specific to protecting and recovering filesystems with Backup and DR.

You can find additional information in the following pages:

  * [Backup and DR for file systems](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-filesystems)
  * [Manage hosts and their connected applications](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-hosts-and-their-connected-applications)
  * [Configure application details and settings to protect file system data](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/configure-app-settings-for-filesystems)
  * [Apply a backup plan to protect a file system](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-plan-to-filesystem)
  * [Restore a file system to the source](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/filesystem-restore)
  * [Mount a file system or file share](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-file-system)
  * [Mount and migrate a file system for instant recovery to any target](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/filesystem-mount-and-migrate)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
