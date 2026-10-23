---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sap-hana/
title: Mount an SAP HANA backup as a standard mount in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:59.740100+00:00
---

# Mount an SAP HANA backup as a standard mount in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sap-hana/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Mount an SAP HANA backup as a standard mount in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

From the appliance management console, you can mount backups of an SAP HANA database as a standard mount or as a virtual database—application aware mount. This is the procedure for a standard mount. To make a virtual database—application aware mount—see the procedure in [SAP HANA database virtual copy](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/recover-sap-hana-virtualdb).

**Note:** This information is for SAP HANA scale-out instances. For scale-up and HA 1+1 configurations, see [Backup and DR for SAP HANA](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-hana).

## About standard mounts

A standard mount provides the backup disk of data, active log and archive log volume to the specified target. You can mount snapshot backup of an SAP HANA database as a standard mount for the following:

  * Any manual operation.
  * To run the SNAPSHOT DATA INTEGRITY CHECK: This tool runs the SAP HANA persistence checking tool, `hdbpersdiag` with the 'check all' option to verify the healthy state of data volumes from the mounted snapshot. Mount jobs fail if there is any corruption during these checks.



## Pre checks during mount

  * Connector connectivity status: The Backup and DR agent is installed and a secret is applied for host connectivity between the backup/recovery appliance and the Backup and DR agent.
  * Mount locations specified are available for mount operation.
  * HANA binary is installed.
  * Verify that the HANA sid same as source is not up and running on the target.
  * The HANA instance version is greater than 2.0SP05.
  * Permission check on source and target project for the cloud service.



## Mount the database backup as a standard mount

Use these instructions to mount the database backup as a standard mount:

  1. In the appliance management console **App Manager** , right-click the protected database from the **App Manager Applications** list, and select **Access**. 

**Note:** You can use the **Managed Backup Plan** status filter to show only protected databases.
  2. Select a backup and choose **Mount**.

  3. On the Mount page, select the **Project Name** , **Region** , **Zone** , and **GCE Instance Name**.

  4. Optionally, enter a unique name associated with the mount in the **Label** field.

  5. Under **Application Options** , disable **Create New Virtual Application**.

**Note:** If you don't see the **Create New Virtual Application** option, then the backup is from a file-based Full+Incremental snapshot, so a virtual database is not possible.

**Included Tenant Databases** is informational only, showing the list of tenant databases under the backup backup.

  6. At **Mapping Options** , enter mount locations and select disk types for both the data volume and the logs.

  7. The **Snapshot Data Integrity Check** is by default set to true. This tool will run the SAP HANA persistence checking tool, hdbpersdiag API with 'check all' option. This will verify the healthy state of data and active log volumes from the mounted snapshot. Mount jobs will fail with error for any corruption during these checks otherwise it will show success. 

The result of the Integrity check will be available under `/var/act/log/(HANA sid)_dataintegrity_check.log` and `/usr/sap/GC1/HDB00/hana-scaleup-3/trace/localclient.*.trc./`.

If you don't want to run the check, set it to false by clicking the toggle button.

  8. Click **Pre-Flight check**. The Pre-Flight check validates the required options on the target server for a successful mount. Upon a successful pre-flight the **Submit** button is enabled. If the pre-flight check fails, you see what failed so you can correct it and rerun the pre-flight check.

  9. Click **Submit**. You can go to the **Job Monitor** to view the progress and details of the job. The mounted backup is available in the Active Mounts.




## Management of the active mounts

Once you have created a mount, you can track the backup from the Backup and DR appliance management console **App Manager** > **Active Mounts**. Ideally, don't leave any backup mounted indefinitely. This is because the backup that the mount was created from, cannot expire until all its mounts have been deleted. When you have finished using the mounted backup then either:

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
