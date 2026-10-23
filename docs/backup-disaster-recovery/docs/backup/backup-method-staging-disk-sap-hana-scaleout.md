---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/backup-method-staging-disk-sap-hana-scaleout/
title: Set the staging disk format and backup method for SAP HANA scale-out databases \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:59.946022+00:00
---

# Set the staging disk format and backup method for SAP HANA scale-out databases  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/backup-method-staging-disk-sap-hana-scaleout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Set the staging disk format and backup method for SAP HANA scale-out databases Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

In the appliance management console the policy template and the resource profile that make up the backup plan define the type of data capture to perform and where to store the captured image.

Based on the required RPOs and backup storage location you must create **Templates** and **Profiles**. The policy part of the template provides additional backup configuration such as enabling logs backups.

A resource profile defines the backup/recovery appliances that are identified as the primary (local) appliance hosting the disk pool to use for snapshots, and a remote appliance for remote backup to be used for disaster recovery operations. The profile also defines the OnVault pools to be used to send backup data to Cloud Storage.

Use the existing template and profile to protect the application or refer to [Create a policy template](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template) and [Create a resource profile](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/resource-profiles#create-profile) to create a new template and profile.

**Note:** Staging disks are necessary when backing up to a backup/recovery appliance. Staging disks are not needed when your backup capture method is set to **Use Persistent Disk snapshot** in the [application details and settings](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-sap-hana-pd).

## Apply policy templates and resource profiles to discovered databases

Once you have discovered one or more applications, apply a policy template and resource profile to the application to capture data operations.

You can choose between two very different backup methods in the **Application Details & Settings**:

  * **Use volume level backup (SAP HANA Savepoint API).** Use volume level LVM snapshots with CBT on Linux to a block-based staging disk. This option lets you create incremental-forever backups.

  * **Use full+incremental backup (SAP Backint API).** This file-dump method does not support the creation of virtual databases. You can select this for both block and NFS staging disks, and this method only supports full backup and physical recovery.

**Note:** If there is third party backup outside the scheduled backups, then database restore will fail. Manual recovery can be done by rebuilding the catalog. Force a full backup whenever the third party backup is run.



When creating a snapshot policy as part of creating a template, you have the option of also capturing its log files at a specified frequency. Details are in [Create a policy template](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template)

Replicate database logs to a remote backup/recovery appliance or to an OnVault. Use the logs at the remote site for any database image within the retention range of the replicated logs. Log replication uses StreamSnap technology to perform the replication between the local and remote backup/recovery appliances; log replication goes directly from the local snapshot pool to the snapshot pool on the remote appliance. For a log replication job to run, there must be a replication policy included in the template, and at least one successful replication of the database must first be completed.

## What's Next?

[Set application details and settings for SAP HANA databases.](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-sap-hana)

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
