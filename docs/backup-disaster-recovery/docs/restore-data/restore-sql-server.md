---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-sql-server/
title: Restore and recover Microsoft SQL Server databases in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:51.838922+00:00
---

# Restore and recover Microsoft SQL Server databases in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-sql-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Restore and recover Microsoft SQL Server databases in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

If a database was deleted or corrupted and you can restore it in either ways:

  * Perform a full restore operation
  * Create a clone, or mount the database almost instantly as a virtual application and then migrate it back to the original location or to a new location. To mount and migrate the database, see [SQL Server mount and Migrate](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/sql-server-mount-and-migrate).

**Note:** Don't use the procedures in this section if you are restoring only a subset of databases on a single volume, when the databases are running from a Backup and DR mount. This may result in unintentional data loss as the contents of the entire volume get overwritten during restore of the volume.

The restore process is wizard driven and varies slightly depending on whether you are restoring a single database backup such as a member of an Always on Availability Group (AG) or multiple backups in a SQL instance.

## Before you begin

Before running the procedures in this section, ensure that:

  * The database is not in Emergency mode.

  * Wait for running jobs to finish.




## Microsoft SQL Server database restore overview

The Restore function replaces the original production database data with the selected point-in-time backup, or from a backup from a backup vault. This restoration results in the loss of all current database data as the database will be overwritten while being restored to its status at the point-in-time when the backup was created. This operation cannot be undone.

**Note:** Backup and DR provides the flexibility to restore Microsoft SQL Server databases to the original Microsoft SQL Server or to an alternate server. To restore to an alternate server, the Backup and DR agent must be installed on the alternate server, and the clone operation should be performed instead of restore. See [Clone SQL Server databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/sql-cloning).

Restore operations are typically performed to restore a database to a valid state after a data corruption event. The amount of time required to complete a restore operation depends on the amount of data involved.

Databases that use the Microsoft SQL Server Full Recovery Model use a single policy to capture both the database and its logs. Such a database can be recovered to any point in time by rolling its logs forward. If you restore the database through the appliance management console by specifying Restore With Recovery, the SQL Server database will be restored and brought online after applying logs.

Backup and DR supports the following common use cases when restoring Microsoft SQL Server databases and instances:

  * Perform an in-place database restore: If a production database or instance has become corrupted but it is still online, then perform a restore operation.

  * Use a virtual application (Virtual Application Mount): You can use a Virtual Application Mount of the last known good version of a corrupted SQL Server instance or database as a means to allow users and applications to resume work as soon as possible. The database can then be migrated in the background using Mount and Migrate, see [SQL Server mount and Migrate](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/sql-server-mount-and-migrate).


**Warning:** Don't use the Restore procedure to restore databases that are members of an Always On Availability Group. Use the Clone capability to perform parallel clones on all nodes in the SQL AG. See [Clone SQL Server databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/sql-cloning).

## Restore Microsoft SQL instances and databases

**Warning:** If you have copies of multiple SQL Server databases on a single volume, are restoring only a subset of databases on the volume, and the databases are already running from a Backup and DR mount, do _not_ perform this procedure. It may result in an unintentional data loss as the contents of the entire volume get overwritten during restore of the volume. Instead, Clone the database to another host as detailed in [Clone SQL Server databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/sql-cloning).

This is the simplest and most common restore scenario. In this case, you restore selected SQL databases from a previous backup to the original database server. The database must be online for this type of restore. If the database is not online, the restore operation will fail during database validation; in this case Clone the database instead.

To run this procedure:

  * The Microsoft SQL Server database must be online. If the database is not online, the restore operation will fail during database validation.

  * Wait for running jobs to finish.




To restore the SQL Server database(s):

  1. Open the App Manager to the **Applications** page.

  2. Right-click the Microsoft SQL Server database to restore and choose **Access** from the drop-down list. The Access page opens listing captured backups in the Timeline ramp view. Backup types that support a Restore operation include Snapshot and OnVault, but only when using the same appliance that captured the backup.

If restoring with a different appliance is required, use the Clone operation instead.

The background differentiates snapshot backups containing a SQL server database with transaction log files, and also illustrates the restore range time period for the logs

  3. Select the backup, then select **Restore** from the list of operations. The Restore page opens.

  4. Select **Traditional** for this restore operation.

**Note:** In most cases, Mount and Migrate is a better option, as it results in near-zero downtime. Mount and Migrate restores are detailed in [SQL Server mount and Migrate](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/sql-server-mount-and-migrate).
  5. If the selected database does not have logs, the Restore page does not show roll forward options. If the SQL Server database was managed with a log protection backup template, and logs are available with the backup, you can:

     * Specify to roll forward using either User Time or Host Time. You can base the dates and times on User Time or Host time. User Time is relative to the viewer of the current screen. Host time is relative to the system that hosts the data to be restored.

     * Use the Calendar tool to select a date for the roll-forward operation.

     * Use the Restore Range slider to select a specific time on the selected date to restore the database. Slide the slider tool all the way to the left with the earliest date selected to restore just the SQL Server database without rolling forward any logs.

  6. Deselect the Restore With Recovery checkbox if you want to leave the database in restoring mode. Restore with recovery brings the restored database online. Once online, no more logs can be applied.

  7. Click **Submit**.

A warning dialog opens. Read it and then enter **DATA LOSS** to confirm. The restore job starts. You can verify that the restore operation is successful by viewing the job status in System Monitor.




## Restore SQL system databases

Backup and DR can discover and backup Microsoft SQL system databases just like SQL Server user databases.

To restore a SQL system database, you must first mount the last known good version of that database, then use a file copy operation to copy the good SQL Server system database .mdf and .ldf files to the source SQL server that hosts the corrupt SQL system system database.

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Select and mount the last known good backup of the consistency group. Be sure to _deselect_ **Create new virtual application**.

**Note:** OnVault pools pointing to backup vaults don't support the preceding mount operations.
  3. If possible, use the following sample query to show file locations for databases:
         
         SELECT name, physical_name AS current_file_location FROM sys.master_files
         

  4. From the SQL instance, use either the SQL Server Configuration Manager or the Services MMC to stop the source SQL instance:

  5. Using Windows Explorer or some other means, navigate to the mounted backup of the SQL system databases.

  6. Copy the mounted .mdf and .ldf files for the database being restored.

  7. Using Windows Explorer or some other means, navigate to the source SQL Server database:

  8. Paste the .mdf and .ldf files into the source SQL Server database.

  9. From the SQL instance, use either the SQL Server Configuration Manager or the Services MMC to Restart the source SQL Server database.




## Restore to a SQL Server cluster

For a SQL Server Failover instance, the database is always restored to the active node. For SQL Server Availability Groups, the restore is performed on all nodes.

## Restore SQL Server databases in a consistency group

Use caution when restoring Microsoft SQL Server databases in a consistency group (see [Restoring a Consistency Group](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/consistency-group-restore-overview)). When you restore SQL Server databases that are in a consistency group, **all** databases in the consistency group are overwritten.

**Note:** For a SQL Server Failover instance, the database is always restored to the active node. The backup/recovery appliance mounts the backup to the active node and performs the restore operation on the node. For SQL Server Availability Groups, the restore is also performed on the active node.

## The Backup and DR Microsoft SQL Server DBA Guide

This page is one in a series of pages specific to protecting and recovering Microsoft SQL Server databases with Backup and DR. You can find additional information at:

  * [Backup and DR for Microsoft SQL Server Databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sql-server)
  * [Prepare SQL Server databases for Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-sql-server)
  * [Add a SQL Server database host and discover databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-sql-server)
  * [Configure backup plans for Microsoft SQL Server instances and databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/back-up-sql-server)
  * [Application details and settings for Microsoft SQL Server instances and databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-sql-server)
  * [Mount a SQL Server database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sql-server)
  * [Mount databases into SQL Always On Availability Groups](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sql-server-aag)
  * [Manage an active mount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts)
  * [Migrate a SQL Server database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-and-migrate-sql-server-2)
  * [Clone SQL Server databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/clone-sql-server)
  * [Recover SQL Server backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-sql-server)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
