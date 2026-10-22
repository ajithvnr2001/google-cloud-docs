---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/clone-sql-server/
title: Clone Microsoft SQL Server databases in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:35.856145+00:00
---

# Clone Microsoft SQL Server databases in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/clone-sql-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Clone Microsoft SQL Server databases in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

You can clone (copy) a backup of a SQL Server database, instance or AG image to any SQL Server host known by your backup/recovery appliance.

The cloning process varies slightly depending on whether you are cloning a single database image such as a member of an Always on Availability Group (AG) or multiple images in a SQL instance.

Use a clone operation:

  * If you have copies of multiple SQL Server databases on a single volume, to avoid unintentional data loss as the contents of the entire volume get overwritten during restore of the volume.

  * If the original database has been removed because of corruption, or if the old database server is being replaced with a new server.

  * You can use a clone to effective restore SQL Server databases onto any host, unlike a restore which can only be run to the source host.

  * You can use a clone to create an independent copy of SQL Server databases for test and development where all changes will remain on the users copy and not get written back to the snapshot pool.

  * Clones can be used to recover databases to a new location, a new filename, or both. Clones are created when a source database has become corrupt, or requires root cause analysis. The clone performs a full restore with optional point in time recovery to the same host (new database name or filename), or alternative hosts running the same version or higher. The use cases for clones include performance testing, long term development and testing, reporting, and even cloning databases from staging environments into existing production instances.




To clone a SQL database to a host:

  1. From the Backup and DR appliance management console, open the **App Manager** to the **Applications** list.

  2. Right-click the application with the image that you want to clone, then choose **Access**. The **Access** page opens listing backup images in the Timeline ramp view.

  3. Select an image and then select **Clone** from the list of access operations. The Clone page opens.

  4. Select a target from the **Target** drop-down list.

  5. Optionally, enter a label for the clone job in the **Label** field.

  6. Under **Application Options** , select one or more databases to clone. Unlike the Mount operation, no new Consistency Group is created when multiple databases are cloned.

  7. If the source application is protected by a snapshot policy that has enabled database log backups, and logs are available with the image, you can use them to roll forward to a specific point in time by changing these options in the **Roll Forward Time** section:

     * The date field contains all possible dates that the database can be rolled forward to, with the application of database transaction logs. Select the date the database needs to be rolled forward to.
     * The time field contains a slider showing all possible times on the selected date that the database can be rolled forward to. If you select the latest possible date and then move the slider to the right most position, the job will apply to all available logs. If you select the earliest possible date and move the slider to the left most position, the job will apply no logs.
     * You can specify to roll forward using either **User Time** or **Host Time**. User Time is relative to the local time of the current user. Host time is relative to the system that hosts the data to be cloned.
**Note:** When performing a clone from OnVault, a roll-forward range is displayed only when logs are available on the local appliance. This includes the scenario where an OnVault import was performed on the same appliance used as a target for StreamSnap replication with log replication enabled.
  8. In SQL Server Instance Name, select a target SQL Server instance to manage the new database.

  9. If you are cloning a single database, enter the name for the new database, avoiding names of existing databases in the selected target server and instance.

If you are cloning multiple SQL databases you can supply a name for each database. Under **Advanced Options** you can also append a suffix or a prefix, or both to every cloned database's name.

  10. Enable the **Rename Files to Match New Database** option if you want to rename the database files to match the new database names.

  11. In the **Advanced Options** section, enter information for the additional fields required. 

Property  | Description  
---|---  
Recover Database After Restore  |  If **Recover Database After Restore** is not enabled, the SQL Server database is left in a state where logs can be rolled forward. When it is enabled, the SQL Server database is brought online and logs cannot be rolled forward beyond the time specified in the mount.   
Recover User Logins  |  This applies only if **Backup SQL Server User Logins** in the Policy Settings or Policy Settings Overrides is set to Yes (this is not the default). If that is set to Yes, all user logins backed up from the source instance are restored into the target instance. Domain accounts only restore if the target SQL Server is in the same domain or forest as the source and if any required trust relationships are in place.   
User Name/Password  |  User credentials for database provisioning.   
The User Name is only required when the account running the Backup and DR agent (typically "Local System") does not have privileges to apply transaction logs, or to detach a database (which is typically required during a subsequent unmount).   
Overwrite Existing Database  |  Overwrites the original database.   
  12. In the File Locations section, specify whether you want to copy the database files to the same path as the source server, or to a new location. There are three options:

     * Copy files to the same drive or path as they were on the source server (default option).

     * Choose new file locations at the volume level.

     * Choose new file locations at the file level.

If you select the second option (new file option at the volume level), you will see a table with the source volume and target volume drop-down.

In Target Volume, select a target volumes from the drop-down list of all discovered file system applications. If needed, you can also type the volume, for example: M:\, or L:\Logs\Log1.

If you select the third option (new file locations at the file level), a table with three columns appears: File, Source Location, and Target Location. In Target Location, enter the new file location as needed.

  13. Click **Submit**. A job is submitted to clone the image to the selected host. You can verify that the clone operation is successful by viewing the job status in the Monitor.




## The Backup and DR Microsoft SQL Server DBA guide

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
