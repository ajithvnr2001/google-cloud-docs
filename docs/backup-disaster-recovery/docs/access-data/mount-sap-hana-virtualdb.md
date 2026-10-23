---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sap-hana-virtualdb/
title: Mount an SAP HANA backup as a virtual database in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:45.103392+00:00
---

# Mount an SAP HANA backup as a virtual database in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sap-hana-virtualdb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Mount an SAP HANA backup as a virtual database in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).**Note:** This information is for SAP HANA scale-out instances. For scale-up and HA 1+1 configurations, see [Backup and DR for SAP HANA](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-hana).

## Create an instant virtual copy of an SAP HANA scale-out instance to any target from a volume-level backup for data validation

Use this procedure to create an instant virtual clone of a HANA database. The HANA database is recovered to the chosen point in time and the database is up and running and available. This new virtual clone can be used for data validation and logical recovery or object-level recovery.

A new virtual database, also called an application-aware mount, is a fully functional copy of the source database in another location. It consumes no storage until you start writing to the database, when incremental storage is consumed by the changed blocks. The new virtual database can be created with a new HANA SID name.

  1. Click **App Manager** > **Protected Application** > **Access** , from the latest snapshot, choose **Mount** —not clone or LiveClone, which do different things.
  2. On the **Mount** page, from **Target** , choose the target HANA server from the drop-down.
  3. Under **Application Options** , complete the following:

     * Select **Create New Virtual Application**.
     * If the source application is protected by a snapshot policy that has enabled database log backups, and logs are available with the backup, you can use them to roll forward to a specific point in time by changing these options in the **Roll Forward Time** section:

       * The date field contains all possible dates that the database can be rolled forward to—through the application of database transaction logs. Select which date you need the database to be rolled forward to.
       * The time field contains a slider showing all possible times on the selected date that the database can be rolled forward to. If you select the latest possible date and then move the slider to the right most position, the restore job applies to all available logs. If you select the earliest possible date and move the slider to the left most position, the restore job applies no logs.
       * You can specify to roll forward using either **User Time** or **Host Time**. **User Time** is relative to the local time of the current user. Host time is relative to the system that hosts the data to be restored.
     * For **Target Database SID** , provide the target HANA database name. In order to create the virtual copy, the target HANA database must be configured.

     * For SAP DB User Store-Key, provide the hdbuserstore key for the target database—for HANA 2.0: SYSTEMDB.

     * For **Mount Location** , specify a **Mount Point** to mount to new target.

     * At **Manage New Application** , if you want to reprotect the database copy, click and enable **Manage New Application**.

     * Choose a template and a profile to protect the database.

  4. Click **Submit**. At this point, the HANA database is recovered to the chosen point in time and the database is up and running and available for data validation. You can go to the **Job Monitor** to view the progress and details of the job. The mounted backup is available in the Active Mounts.




## Management of the active mounts

Once you have created a mount, you can track the backup from the **App Manager** > **Active Mounts**. Ideally, don't leave any backup mounted indefinitely. This is because the backup that the mount was created from cannot expire until all its mounts have been deleted. When you have finished using the mounted backup then perform one of the following actions:

  * [Unmount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount) the backup. You can [remount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#remount) it if needed. You can then [delete](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#delete) the backup later when you are certain it is no longer needed.
  * [Unmount and delete](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount-delete) the backup. This deletes the mounted backup, not the backup that the mount is based on.



## Backup and DR documentation for SAP HANA scale-out

This page is one in a series of pages specific to protecting and recovering SAP HANA scale-out instances with Backup and DR. You can find additional information in the following pages:

  * [Backup and DR for SAP HANA scale-out](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-hana-scaleout)
  * [Prepare SAP HANA scale-out instances for backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-sap-hana)
  * [Add an SAP HANA scale-out host, and discover and protect its databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-sap-hana-scaleout)
  * [Configure staging disk format and backup method for SAP HANA scale-out](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/backup-method-staging-disk-sap-hana-scaleout)
  * [Set application details and settings for SAP HANA scale-out instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-sap-hana-scaleout)
  * [Back up HANA 1+n and HANA scale-out databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/back-up-sap-hana-scaleout)
  * [Restore and recover SAP HANA scale-out instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-sap-hana-scaleout)
  * [Mount an SAP HANA scale-out backup as a standard mount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sap-hana)
  * [Mount an SAP HANA scale-out backup as a virtual database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sap-hana-virtualdb)
  * [Mount and migrate an SAP HANA scale-out backup for instant recovery to any target](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-and-migrate-sap-hana)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
