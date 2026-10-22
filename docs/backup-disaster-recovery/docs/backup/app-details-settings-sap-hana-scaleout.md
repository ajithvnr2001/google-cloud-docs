---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-sap-hana-scaleout/
title: Configure application details and settings for SAP HANA databases to be backed up to block or volume-level backups \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:39.595529+00:00
---

# Configure application details and settings for SAP HANA databases to be backed up to block or volume-level backups  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-sap-hana-scaleout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Configure application details and settings for SAP HANA databases to be backed up to block or volume-level backups Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).**Note:** This information is for SAP HANA instances using the volume level backup or the full+incremental backup methods. If you plan to back up to Persistent Disk snapshots, see [Configure application details and settings for SAP HANA databases to be backed up to Persistent Disk snapshots](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-sap-hana-pd).

After [setting the staging disk format and backup method](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/backup-method-staging-disk-sap-hana-scaleout), you must enter the details and settings you want to apply to your backup plans:

  1. In the appliance management console, go to **App manager** and click **Applications**.

  2. Right-click the HANA database and click **Manage backup configuration**.

  3. At the top of the page, click **Details & Settings**.

  4. In the **Application details & settings** window, configure database settings based on your host type.

Setting | Backup Capture Method: Volume-Level Backup | Backup Capture Method: Full+Incremental Backup  
---|---|---  
HANA DB User Store Key | This is the SAP HANA hdbuserstore key for the system database created earlier. This field is mandatory. | This is the SAP HANA hdbuserstore key for the system database created earlier. This field is mandatory.  
Use Staging Disk Granularity as Minimum Staging Disk Size | Not applicable. | For applications that are under the size of granularity setting that tend to periodically grow this new option is useful to avoid frequent costly FULL backups. Because the staging disk is thin provisioned, there is no initial cost to use a staging disk that is larger than required for immediate use. The values are 0 for No and the Staging Disk Granularity setting for Yes.  
Staging Disk Granularity | Not applicable. | Maximum size of each staging disk when multiple staging disks are used for an application. The default value is 1000GB.  
Last Staging Disk Minimum Size | Not applicable. | Minimum size of the last staging disk created for an application with multiple staging disks. This value is also used for additional disks allocated to accommodate growth. The default value is 250GB.  
Use BACKINT for HANA Full+Incremental File system Backup | Not applicable | When set to Yes, database backup uses the BACKINT configuration and BACKINT parameters are updated in the HANA database configuration files.  
Force Full File system Backup | Not applicable | Use for an on-demand full backup  
Ignore Partial Database Backup Failures | Not applicable | Enable this option to continue the backup job even if a tenant backup fails in a multitenant SAP HANA instance.  
Database File system Staging Disk Size in GB | Not applicable | Use the default calculation: (database size * 1.5)+ 10%. The disks will grow dynamically.  
Retention of Production DB Logs in Hours | At the end of every log backup, the log purge will run and delete all the logs older than the number of hours specified here. For example if the number of hours specified is 4 hours then all the logs older than ((the start time of the log backup) - (4 hours)) will be purged. The default value is 2 hours. | At the end of every log backup, the log purge will run and delete all the logs older than the number of hours specified here. For example if the number of hours specified is 4 hours then all the logs older than ((the start time of the log backup) - (4 hours)) will be purged. The default value is 2 hours.  
Retention of Production Catalog in Days | This is the retention of catalog metadata in days. The HANA catalog metadata (m_backup_catalog table) will be purged of logs older than the specified number of days. For example if the number of days specified is 14 days then data from HANA catalog will be purged older than ((the current day) - (14 days)). The default value is 7 days. | This is the retention of catalog metadata in days. The HANA catalog metadata (m_backup_catalog table) will be purged of logs older than the specified number of days. For example if the number of days specified is 14 days then data from HANA catalog will be purged older than ((the current day) - (14 days)). The default value is 7 days.  
Tenant DB User Store Key Prefix | Not applicable. | HANA user store key prefix to backup tenant database. During the backup Tenant database name is appended to the string provided. For example, if Prefix is provided as ACTBACKUP and tenant name is CL5, then userstore key for tenant will be ACTBACKUPCL5.  
Use SystemDB User Store Key to Backup Tenant | Not applicable. | SYSTEMDB user store key will be used to backup all the tenant databases.  
Run Tenant Backups in Parallel | Not applicable. | If set to Yes, all tenant databases will be backed up in parallel for backups using file system, non-backint.  
Script Timeout | This value is applied to internal backup and recovery scripts called by Backup and DR agent. Default value is recommended. | This value is applied to internal backup and recovery scripts called by the Backup and DR agent. Default value is recommended.  
     * **Retention of production DB logs in hours** : At the end of every log backup, the log purge will run and delete all the logs older than the number of hours specified here. For example if the number of hours specified is 4 hours then all the logs older than ((the start time of the log backup) - (4 hours)) will be purged. The default value is 2 hours.
     * **Retention of production catalog in days** : This is the retention of catalog metadata in days. The HANA catalog metadata (m_backup_catalog table) will be purged of logs older than the specified number of days. For example if the number of days specified is 14 days then data from HANA catalog will be purged older than ((the current day) - (14 days)). The default value is 7 days.
  5. Click **Save changes**.




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

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
