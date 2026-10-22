---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sql-server-aag/
title: Mount to Microsoft SQL Always On availability group in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:05.329060+00:00
---

# Mount to Microsoft SQL Always On availability group in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sql-server-aag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Mount to Microsoft SQL Always On availability group in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Disable comment: 

## Mount to a SQL Server AAG using a snapshot pool

This approach is the fastest way to create a new SQL Server AlwaysOn Availability group for short-term use. The mounted application runs in the snapshot pool, and achieves the same performance as data captured in the snapshot pool.

**Note:** Be sure there is enough space in the snapshot pool for the availability group and regular snapshots.

  1. Mount the databases being added to the SQL availability group to each node in the AG, one node at a time. See [Mount a SQL Server database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/sql-access).

  2. Select the required host.

  3. Select the SQL instance.

  4. Specify the roll-forward time, being sure to specify the same time during mounts to each node.

  5. Under **Advanced Options** , deselect **Recover Database After Restore**.

  6. Enter a name, or a prefix or suffix. Use the same name, prefix, or suffix on all nodes.

  7. Repeat the process for each availability group member.

  8. Once all databases are mounted as virtual databases on each availability group node, using SQL, select the SQL instance that is the primary and for each database recover it:
         
         `recover database (name) with recovery`
         

  9. Keep the secondary database copies in restoring state.

  10. When the master database has been restored, using SQL, create the new availability group and join the primary and secondary databases as described in Add virtual databases to a new SQL Server AlwaysOn Availability group.




## Clone to a SQL Server availability group independently from the snapshot pool

To clone to a SQL AlwaysOn Availability group that resides independently from the snapshot pool, perform a clone operation for the databases on each node in the SQL AlwaysOn Availability group as described in [Clone SQL Server databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/sql-cloning). Be sure to deselect **Recover** database after restore and to specify the same roll-forward time for each clone operation.

## Add virtual databases to a new SQL Server AlwaysOn Availability group

After all databases for the new AG have been recovered, use SQL Studio or T-SQL to add the databases to the SQL AlwaysOn Availability group:

  1. From SQL Studio, select the SQL availability group.

  2. Add the databases to the availability group.

  3. Click **Next**. You are prompted to select a synchronization method. Select **Join only** ; the **Join only** operation forms the primary and secondary databases into an availability group.

  4. Monitor the progress of the operation. When the operation is complete, both the primary and secondary databases are in sync.

  5. If autodiscover applications is not enabled, manually discover applications on the availability group host.

  6. After discovery is complete, the databases appear in the **App Manager** as members of the SQL availability group.

  7. Capture members of an availability group just like any other database.




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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
