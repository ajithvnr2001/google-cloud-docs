---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/back-up-otherdb/
title: Back up other databases and their logs to an appliance-managed backup \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:34.308551+00:00
---

# Back up other databases and their logs to an appliance-managed backup  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/back-up-otherdb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Back up other databases and their logs to an appliance-managed backup Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

After the backup plan is configured as detailed in [Manage backup templates](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template), you can configure a backup method for the database or instance.

[Microsoft SQL Server](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/sql-protect), [Oracle](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/oracle-db-protect), and [SAP HANA](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/protect-sap-db) databases each have their own documentation. These other supported database types share many procedures.

The following are the other supported database types:

  * [IBM Db2](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/db2-intro)

  * [PostgreSQL](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/postgresql-intro)

  * [SAP ASE](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/sap-ase-intro)

  * [SAP IQ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/sap-iq-intro)

  * [SAP MaxDB](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/maxdb-intro)


**Note:** With one exception, protection is set for the entire instance. You can include or exclude specific databases during the process using a database inclusion rule from the **Manage Backup Plan** page. The exception is that virtual databases can be protected separately from the instance when created.

## Protect a database or a database instance

Db2 database instance protection can be done from either the primary node or from HADR nodes. To protect from a Db2 HADR node, the node must be read-enabled. Ensure that the parameter `DB2_HADR_ROS=ON` is set.

When an SAP ASE database is protected with Full+Incremental based backup, the source and target databases must use the same character set or sort order for a successful restore. For details refer to [SAP Note: 1860413 - How to change character set or sort order of SAP ASE](https://userapps.support.sap.com/sap/support/knowledge/en/1860413).

To protect the database or database instance, complete the following:

  1. Click **App Manager** > **Applications** , right-click the instance and select **Manage Backup Plan**.

  2. On the **Manage Backup Plan** page, select a template and a resource profile, then click **Apply Backup Plan**.

If you back up a workload to a backup/recovery appliance that would exceed its recommended storage capacity or snapshot limit, you will see a notification with a recommendation to back up the data to a different backup/recovery appliance.

**Caution:** Exceeding the capacity of a backup/recovery appliance can lead to failed jobs and unprotected data and failed restore operations.**Caution:** Running on-demand dump-based backups while backups are scheduled can exceed the capacity of the appliance. To avoid this, you must set the staging disk size explicitly in the [application details and settings](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-otherdb).
  3. Click **Details & Settings** and ensure that the backup capture method matches the type of backup set in [Manage backup templates](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template). Click **Apply backup plan** or **Save Changes**. The instance appears in the **App Manager** with a shield icon.

The instance is protected when the snapshot job succeeds according to the schedule in the template.

  4. If you are protecting an instance, then you can include or exclude specific databases during backup. From the **App Manager** , select the instance. Use the checkboxes to filter the list. Select **Manage backup plan**.

  5. Under **Database Inclusion Rule** , click **Edit**. If you do not see the **Database Inclusion** settings, you have selected a database, not an instance.

  6. Select an **Inclusion Rule** —**Include All** , **Include Selected** , or **Exclude Selected** —and then select the databases to include or exclude, then click **Save**.




## Protect database logs

To enable and set up database log backup, follow these steps:

  1. From the **Backup Plans Templates** page, right-click the template that will be used for protecting the instance and click **Edit**.

  2. Click the arrow beside the snapshot policy to open up the details, then click **Edit Policy**.

  3. Near the bottom, select **Advanced Policy Settings**.

  4. Set the log policy options—you have to scroll to see them all:

     * Enable **Truncate/Purge log after backup**.

     * Set **Enable Database Log Backup** to **Yes**.

     * For **RPO (Minutes)** , when **Enable Database Log Backup** is set to **Yes** , RPO defines the frequency for database log backup. Frequency is set in minutes and must not exceed the database backup interval. The smallest value that can be set is 15 minutes.

     * Set **Log Backup Retention Period (in Days)** for point in time recovery.

     * Set **Replicate Logs (Uses StreamSnap Technology)** to **Yes** if you want to enable StreamSnap replication of log backup to a DR site.

     * Set **Send Logs to OnVault Pool** to **Yes** if you want the database logs to be sent to an OnVault pool, enabling for point-in-time recoveries from OnVault on another site.

  5. Click **Save Changes**.

  6. From the **App Manager Applications** list, select the instance. You can use checkboxes on the left to filter the list. Right-click it and select **Manage Backup Plans**.

  7. At the top of the screen, select **Details & Settings**.

  8. Set the **Retention of Production DB Logs** in hours. This value is used to purge the logs from the production destination. Based on this setting, the logs are purged if they are older then the number of hours specified. If the default value is not specified, then the default value is 24 hours.

  9. Click **Save**.


**Note:** (SAP ASE only) Only user database transaction logs are backed up; System database transaction logs (including master database transaction logs) are not backed up and so they are not truncated. This means that the system database archive log can get full and cause production user database backup jobs to fail. To prevent this, manually clear the system database logs by running the command `dump tran master with no_log`.

## What's next

Your databases and instances back up on the schedules set in their backup plans. To review and report on Backup and DR activity, you can view the [appliance management console dashboard](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/dashboard) and examine the reports in the report manager. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
