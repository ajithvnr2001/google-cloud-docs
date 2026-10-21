---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-plan-to-filesystem/
title: Back up a file system in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:58.046360+00:00
---

# Back up a file system in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-plan-to-filesystem/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Back up a file system in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

You manage a mapped file system in the appliance management console by assigning a resource profile and a template to it.

To apply a backup plan to a file system:

  1. In the appliance management console click the **App Manager** tab and select the **Applications** option from the drop-down list. The **Applications** page opens.

**Note:** The appliance management console refers to local filesystems as `FileSystem` and mapped file systems as `SMB` and `NFS`.
  2. Select the file system that you want to manage, and then choose **Manage Backup Plan** from the drop-down list at the bottom right corner of the page. The **Manage Backup Plan** page opens.

  3. Choose from the **Template** and **Profile** drop-down lists:

     * **Template.** An existing backup template that includes policies to define the snapshot or replication of the application data.
     * **Profile.** An existing resource profile that defines the resources used to store the data of the application as snapshot or replicated backups.

The **Manage Backup Plan** page shows a view of the policies assigned to the selected applications in the backup plan policy map. Data capture management comes from the template policies and profiles that you designed in the backup plans.

  4. From the backup template page make the following changes prior to applying a backup plan:

     * **Application Settings.** Apply application-specific settings when managing a file system application data capture. Application settings can be useful or required in certain circumstances. See [Configure application settings to protect file system data](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/configure-app-settings-for-filesystems) for details.

     * **Policy Overrides.** Override specific policy settings previously configured in the selected backup template. Advanced settings can be useful or required in certain circumstances. See [Configure policy overrides](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview#override) for details.

**Note:** You can override policy settings only if the policy template **Allow Overrides on Policy Settings** property has been set to **Yes**.
  5. Click **Apply Backup Plan** to apply the backup template and resource profile. A success message opens.

  6. Click **Okay**.

If you back up a file system to a backup/recovery appliance that would exceed its recommended storage capacity or snapshot limit, you will see a notification with a recommendation to back up the data to a different backup/recovery appliance.

**Caution:** Exceeding the capacity of a backup/recovery appliance can lead to failed jobs and unprotected data and failed restore operations.

The application might not get backed up until the scheduled job runs according to the hours of operations defined in the backup template. For example, if at 10:00 you assign a template that has hours of operation from 02:00 to 05:00, then the first job won't start until the appliance has an available job slot at 02:00 of the following day. To run a job immediately, see [perform an on-demand capture](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/states-of-an-application).

**Note:** All policy start and end times are in UTC time zone.

To change backup plan settings for the application, see [Modify backup plan management of a managed application](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/states-of-an-application#remove). To disable a backup plan, see [Removing backup plan management of an application](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/states-of-an-application#remove).


**Note:** To reset one or more application settings back to its default state, click the **Reset to Default** checkbox to the right of the selection you want to reset, or click **Reset All to Default** to reset all application selections back to their default state.

## The File System Administrator Guide to Backup and DR

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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
