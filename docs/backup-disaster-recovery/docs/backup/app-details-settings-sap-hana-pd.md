---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-sap-hana-pd/
title: Configure application details and settings for SAP HANA databases to be backed up to Persistent Disk snapshots \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:14.751215+00:00
---

# Configure application details and settings for SAP HANA databases to be backed up to Persistent Disk snapshots  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-sap-hana-pd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Configure application details and settings for SAP HANA databases to be backed up to Persistent Disk snapshots Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).**Note:** This information is for SAP HANA instances using the Persistent Disk backup method. If you plan to use the volume level backup or the full+incremental methods, see [Configure application details and settings for SAP HANA databases to be backed up to block or volume-level backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-sap-hana-scaleout).

After [setting the staging disk format and backup method](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/backup-method-staging-disk-sap-hana), you must enter the details and settings you want to apply to your backup plans:

  1. In the appliance management console, go to **App manager** and click **Applications**.

  2. Right-click the SAP HANA database and click **Manage backup configuration**.

  3. At the top of the page, click **Details & Settings**.

  4. In the **Application details & settings** window, configure database settings based on your host type.

     * **Backup Capture Method** : Use Persistent Disk snapshots.
     * **HANA DB User Store Key** : This is the mandatory SAP HANA hdbuserstore key for the system database created earlier. 
     * **Retention of production DB logs in hours** : At the end of every log backup, the log purge will run and delete all the logs older than the number of hours specified here. For example if the number of hours specified is 4 hours then all the logs older than ((the start time of the log backup) - (4 hours)) will be purged. The default value is 2 hours.
     * **Retention of production catalog in days** : This is the retention of catalog metadata in days. The HANA catalog metadata (m_backup_catalog table) will be purged of logs older than the specified number of days. For example if the number of days specified is 14 days then data from HANA catalog will be purged older than ((the current day) - (14 days)). The default value is 7 days.

     * **Script Timeout** : This value is applied to internal backup and recovery scripts called by the Backup and DR agent. Default value is recommended.

  5. Click **Save changes**.




## The Backup and DR SAP HANA DBA guide

This page is one in a series of pages specific to protecting and recovering SAP HANA databases with Backup and DR. You can find additional information in the following pages:

  * [Backup and DR for SAP HANA](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-hana)
  * [Prepare SAP HANA databases for backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-sap-hana)
  * [Add an SAP HANA database host, and discover and protect its databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-sap-hana)
  * [Set application details and settings for SAP HANA databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-sap-hana)
  * [Back up a discovered HANA database](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/back-up-sap-hana-db)
  * [Back up HANA 1+n and HANA scale-out databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/back-up-sap-hana-scaleout)
  * [Restore and recover SAP HANA databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-sap-hana)
  * [Mount an SAP HANA backup as a standard mount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sap-hana)
  * [Mount an SAP HANA backup as a virtual database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sap-hana-virtualdb)
  * [Mount and migrate an SAP HANA backup for instant recovery to any target](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-and-migrate-sap-hana)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
