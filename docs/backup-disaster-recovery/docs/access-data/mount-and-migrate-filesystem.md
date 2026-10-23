---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-and-migrate-filesystem/
title: Mount and migrate file systems in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:12.926647+00:00
---

# Mount and migrate file systems in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-and-migrate-filesystem/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Mount and migrate file systems in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

The file system mount and migrate feature in the appliance management console is available for recovery of Linux file systems that are backed up into a logical volume manager (LVM) based staging disk—as LVM is used for the online migration during recovery.

If the source file system is less than 1 TiB or is not on a logical volume manager, a flag **Prefer LVM on Staging Disk** needs to be set to force logical volume manager onto the Backup and DR staging disk. Backups of file systems that are larger than 1 TiB are automatically backed up in logical volume manager format, regardless of whether the **Prefer LVM for Single Staging Disk** option is set or not.

## Known limitations

The target volume group extent size must be identical to the production volume group at the time of backup. If the production system does not have LVM, the staging disk uses a default extent size of 4 MB.

## Use mount and migrate to restore data back to the same server location

The following must be true for images from any file system application to be restored using the mount and migrate option:

  * The **Application** and **Details** setting `Prefer LVM on Staging disk` is set to **Yes**.
  * The production application data is resident on an logical volume manager logical volume.

**Note:** You can also restore an application to an alternative server location.

Complete the following to restore an application back to its original location.

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Select the application with the image that you want to restore using mount and migrate capability. Then select **Access** from the drop-down list at the bottom of the **Applications** page.

  3. Select the image you need, and select **Restore** from the drop-down menu on the right-hand side of the page.

The **Restore** page opens.

  4. Select the **Mount and Migrate** option to restore with near-zero downtime.

  5. Optionally, in **Label** , enter a label for the cloned application. By default, the label is filled with the **Clone - M &M** label.

  6. Click **Pre-Flight Check**. You see a status message about the progress of the pre-flight check. If the pre-flight check fails, you see an error message explaining why the pre-flight check failed. Fix the issues in the error message and run the pre-flight check again. Once the pre-flight check passes, the **Submit** button is enabled.

  7. Click **Submit**. The mount and migrate process is initiated, which results in a couple of jobs running in the background: the mount job and the migrate job.

The mount job mounts the selected point-in-time image of the file system application back to the same host and location from where the data was captured. Once the image is mounted, the data becomes available almost instantaneously to the business application, thus providing near-zero RTO.




After the successful completion of the mount job, the system auto-initiates the migrate job, which starts migrating the application data from Backup and DR disks onto the product storage in real-time— including the data changes.

## Use mount and migrate to restore (migrate) data to an alternative server location

Images from any file system application can be restored using the mount and migrate option if the following is true:

  * The **Application and Details** setting **Prefer LVM** on staging disk is set to **Yes**.
  * The production application data is resident on an logical volume manager logical volume.

**Note:** You can also restore an application to the same server location.



Use these instructions to restore an application back to a different server location.

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Select the application with the image that you want to restore using mount and migrate capability. Then select **Access** from the drop-down list at the bottom of the **Applications** page.

  3. Select a point-in-time that you want the application to restore.

  4. Select **Clone** from the list of access operations.

The **Clone** page opens.

  5. Select a host where the file system application is to be restored.

  6. Optionally, in **Label** , enter a label for the cloned application. By default, the label is filled with the **Clone - M &M** label

  7. From the **Target VG Name drop-down** list, select the **Volume Group** that you want to migrate. The selected **Volume Group** must have enough unallocated space in it to hold the volume.

  8. Click **Pre-Flight Check**. You see a status message about the progress of the pre-flight check. If the pre-flight check fails, you see an error message explaining why the pre-flight check failed. Fix the issues in the error message and re-run the pre-flight check. Once pre-flight check passes, the **Submit** button is enabled.

  9. Click **Submit**.

The mount and migrate process is initiated. This results in two jobs; the mount job and the migrate job.

The mount job mounts the selected point-in-time image of the file system application back to the same host and location from where the data was captured. Once the image is mounted, the data becomes available almost instantaneously to the business application, thus providing near-zero RTO.

After the mount job has succeeded, the system auto-initiates the migrate job, which starts migrating the application data from Backup and DR disks onto the product storage in real-time—including the data changes.




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
