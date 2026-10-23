---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/back-up-sap-hana-db/
title: Back up a discovered SAP HANA database and its logs to an appliance-managed backup \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:18.844638+00:00
---

# Back up a discovered SAP HANA database and its logs to an appliance-managed backup  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/back-up-sap-hana-db/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Back up a discovered SAP HANA database and its logs to an appliance-managed backup Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).**Note:** This information is for SAP HANA scale-out instances. For scale-up and HA 1+1 configurations, see [Backup and DR for SAP HANA](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-hana).

Use the following instructions to back up an SAP HANA database and its logs:

  1. Click **App Manager** > **Applications** and enter the database application name or use the filters to find the database that you need.

  2. Right-click the application and select **Manage Backup Plan**.

  3. On the **Manage Backup Plan** page, select a template and a profile and click **Apply Backup Plan**.

  4. The **Apply Backup Plan** dialog opens. Assign policy overrides and change application settings as needed.

  5. You can wait for the job to run during the period scheduled in the backup plan, or you can run the job at the next opportunity by clicking on the job and selecting **Run Now**.

If you back up a workload to a backup/recovery appliance that would exceed its recommended storage capacity or snapshot limit, you will see a notification with a recommendation to back up the data to a different backup/recovery appliance.

**Caution:** Exceeding the capacity of a backup/recovery appliance can lead to failed jobs, unprotected data and failed restore operations.
  6. The job runs as soon as the scheduler has an opening, often immediately. You can go to the **Jobs Monitor** to view the progress and details of the job.




## The Backup and DR SAP HANA DBA guide

This page is one in a series of pages specific to protecting and recovering SAP HANA databases with Backup and DR. You can find additional information in the following pages:

  * [Backup and DR for SAP HANA](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-hana)
  * [Prepare SAP HANA databases for backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-sap-hana)
  * [Add an SAP HANA database host, and discover and protect its databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-sap-hana)
  * [Configure staging disk format and backup method for SAP HANA databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/backup-method-staging-disk-sap-hana)
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
