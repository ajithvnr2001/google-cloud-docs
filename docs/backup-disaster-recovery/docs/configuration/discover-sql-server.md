---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-sql-server/
title: Add Microsoft SQL Server & discover databases in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:04:30.439704+00:00
---

# Add Microsoft SQL Server & discover databases in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-sql-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Add Microsoft SQL Server & discover databases in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Before you can protect SQL Server databases, complete the following:

  * Review your network configuration, including firewall ports. Pay close attention to our notes on how to SQL database discovery considerations.

  * Install the Backup and DR agent on the database hosts.

  * Make sure the database permissions are set correctly.




## SQL database discovery considerations

  * backup/recovery appliances support Microsoft SQL Server on Microsoft Windows server.

  * Discovery relies on SQL VSS writer. For the discovery to work correctly, SQL VSS writer must be installed and running on the host.

  * Appliances can manage Microsoft SQL Servers, SQL instances, consistency groups of SQL Server databases, and SQL availability groups.

  * For a SQL failover appliance, the discovery needs to be run on either the active node—or node IP—or appliance node—or appliance IP. Otherwise, clustered databases aren't discovered.




## Add the host

Add the host to the appliance management console. If the host has already been added, then edit the host and make sure to set all the configurations correctly.

**Note:** If you have added the Windows server to Backup and DR as a Compute Engine instance or as a VMware VM, then a host for this VM already exists and you don't need to add it again using the following procedure. Instead, find and edit that host.

  1. Click **Manage** > **Hosts** , then click **\+ Add Host**.

  2. On the **Add Host** page, complete the following:

     * **Name** : Provide the database server name.

     * **IP Address** : Provide the database server IP and click the **plus sign (+)**.

     * **Appliances** : Select the checkbox for the appliance.

     * **Host Type** : Make sure this is **Generic**.

  3. Click **Add** at bottom right to add the host. The host is added.

  4. Right-click the host and select **Edit**.

  5. Leave the **Staging Disk Format** as **Block**.

  6. Enter the username and password that you set up in **Application Discovery Credentials**.

  7. Select **Save**.




## Discover SQL Server instances and databases

Use the following instructions to discover SQL Server instances and databases:

  1. Click **App Manager** > **Applications** , select **Add Application**.

  2. Select **SQL Server** on the **Add Application** page, then select the SQL Server database host. If you have many hosts, you can use the search feature or use the filter to see only hosts that are managed by a specific backup/recovery appliance.

**Note:** When adding SQL instances that participate in Microsoft Server Failover Clusters, either:  
Run the wizard once for each node in the cluster, or else  
Add all applications and multi-select all nodes at once. With this method, apply protection from the **Applications Listing** view by selecting **Manage Backup Plan** for the SQL instance.
  3. Select the host and click **Next**. This runs the discovery on the SQL Server host and discovers all SQL Server instances and databases running on it.

**Note:** Discovery on any one node adds other nodes of cluster as well.  
To discover system DBs, run discovery on each node. System DBs can be protected as part of a SQL instance.  
Availability Group databases can be protected as part of a SQL AG application.  
You can take a backup of a secondary by specifying the AG backup preference from application advanced settings.  
Log truncation on the primary is managed by SQL Server, even when backing up db or logs on a secondary.



## Find the discovered instances and databases in the App Manager

To find the newly-discovered database, go to the **App Manager Applications** list. All applications known to the appliance management console of all types are listed. Use the **Type** application filter to show only SQL Server database instances. The new SQL Server instances and databases appear in the list as unmanaged—the shield icon.

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



## What's Next

[Configure backup plans for Microsoft SQL Server instances and databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/back-up-sql-server)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
