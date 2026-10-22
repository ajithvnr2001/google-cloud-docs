---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sql-server/
title: Backup and DR for Microsoft SQL Server on a backup/recovery appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:17.465998+00:00
---

# Backup and DR for Microsoft SQL Server on a backup/recovery appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sql-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Backup and DR for Microsoft SQL Server on a backup/recovery appliance Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

## Capture SQL Server data

Backup and DR lets you capture the following types of Microsoft SQL Server applications:

  * Instances

  * Databases in Always On Availability Groups

  * Consistency groups of databases

  * Individual databases

  * System databases

  * User databases

  * Databases in VMs




Backup and DR moves and manages the Microsoft SQL Server data separately from where Microsoft SQL Server writes its primary storage.

A backup/recovery appliance stores application data on a staging disk. Snapshots on the staging disk allow the backup/recovery appliance to maintain historical data.

## Prepare to backup Microsoft SQL Server data

Preparing to backup Microsoft SQL Server data consists of four steps:

  1. Add servers that host Microsoft SQL Server databases.

  2. Discover VMs and Microsoft SQL Server databases.

  3. Define Backup and DR policy templates and resource profiles according to your RPOs and RTOs.

Databases that use the Microsoft SQL Server full recovery model can capture both the database and its logs. Therefore, a captured database can be recovered to a point in time by rolling its logs forward.

  4. Assign Backup and DR policy templates and resource profiles to Microsoft SQL Server databases.


**Note:** For SQL Server Always On Availability Groups, all the cluster nodes or hosts of the AAG must be discovered and backed up on same backup/recovery appliance.

## Data capture

When capturing data, consider the following:

  * A staging disk is automatically created and mounted on a server.

  * An initial full copy is made to the staging disk. Subsequent copies consist only of changed blocks.

  * The staging disk is unmounted from the server.

  * A snapshot of the staging disk is made on the backup/recovery appliance.




## Capture SQL Server database logs

Database log capture is set in a snapshot policy's **Details & Settings**. It enables a single snapshot policy to capture logs for Microsoft SQL Server databases and consistency groups that contain Microsoft SQL Server databases.

The frequency with which database logs are captured is defined separately from that of the database. For example, a database can be captured every day and its logs captured every hour.

The frequency of database log backup is set in minutes, and the frequency at which logs are captured must not exceed the frequency at which its associated database is captured. For example, if a database capture frequency is every 24 hours, the log file capture frequency must be equal to or less than every 24 hours.

Log retention is also defined separately from its associated database. Having separate retention periods lets you maintain enough log information to cover all snapshot and OnVault versions of a database. For example, if a database's snapshot data is kept for three days and its OnVault data is kept for seven days, you can define log retention to span all seven days. In this example, a single captured database can be selected and its logs can be rolled forwards over the entire period.

Database logs are staged to a single staging disk in the Backup and DR snapshot pool. To conserve space in the snapshot pool, you can use an advanced setting to instruct the database to compress its logs.

You can specify to replicate Microsoft SQL Server database transaction logs to a remote backup/recovery appliance. You can use the logs at the remote site for any database within the retention range of the replicated logs.

## Resize database log's staging disk

The physical space required to accommodate backups of a database's logs is automatically managed by Backup and DR. This is called a log staging disk and is separate to the storage managed by the source server. At a minimum, Backup and DR evaluates typical log sizes and their retention period and uses a larger disk if needed.

To more efficiently and effectively manage the storage requirements for a database's logs, snapshot policies provide the following advanced settings:

  * **Log Backup Retention Period** : Log retention is defined separately from its associated database. Having separate retention rates lets you maintain enough log information to cover all snapshot versions of a database. The log retention period is a mandatory setting.

  * **Log Staging Disk Size Growth** : Defines the percent at which to automatically grow the staging disk on which the logs reside.

  * **Estimated Change Rate** : Defines the daily change (percent), which allows the backup/recovery appliance to better calculate the size of the staging disk needed to hold logs.

  * **Compress Database Log Backup** : Instructs the source database to compress its logs before capture on the backup/recovery appliance. The database server performs log compression during log backup (default is **Enabled**).




## SQL Server data capture options

The following sections go over the SQL Server data capture options.

### Capture instances, individual databases, and groups of databases

The Backup and DR agent is used to capture instances, user databases, system databases, and groups of databases on physical and virtual servers.

When capturing a SQL Server instance, you have the option of capturing the entire instance or selected databases within the instance. When you protect the entire instance, as databases are added to the instance, they are automatically included in the next Backup and DR capture job. Databases in an instance are quiesced and captured together with a single backup plan.

If Backup and DR database and log capture are enabled on the backup plan policy, then all databases in that instance can be recovered to the same point-in-time. Recovery and rolling forward of the logs for all or individual databases in an instance is performed from the Backup and DR user interface with a single action.

Individual members of an instance can be accessed by mount, clone, LiveClone, and restore operations as needed.

### Capture consistency groups

A consistency group is a group of databases that are quiesced and captured together with a single backup plan policy template and resource profile. Membership to a consistency group is assigned manually and is suitable to groups of databases whose members don't change very often. To automatically protect new members of a group of databases, create and protect those databases in a SQL Server instance instead.

As the name implies, consistency groups ensure consistent point-in-time capture and recovery across multiple databases. If Backup and DR's database and log capture technology is enabled on the backup plan policy, then all databases in that group can be recovered to the same point-in-time. Recovery and rolling forward of the logs for all or individual databases in a consistency group is performed from the Backup and DR user interface with a single action. Members of a consistency group must reside in the same instance.

A consistency group can be made up of the following:

  * One or more system databases

  * One or more user databases

  * System or user databases together

  * Zero or more file systems (drive letters or mount points)




Individual members of a consistency group can be accessed by mount, clone, LiveClone, and restore operations.

Databases in a clustered failover instance must be discovered from the active node. Once protected, GO follows the active SQL node in a cluster. Protection jobs continue to run even in a failover condition. In addition to making capture and access operations fast, consistency groups consume fewer system resources (VDisks) than protecting databases individually.

You can validate the integrity of database backup periodically by mounting a backup to a server and running database consistency check. You can use the workflow feature to automate the validation process.

### Capture a VM's databases and boot volume

When capturing databases on VMs you have the option of also capturing the VM's boot volume. When a VM's boot volume is captured along with its databases, a backup can be presented that is a fully functional database and VM. The backup can then be migrated to a new, permanent location.

## Replicate SQL Server data

Data can be replicated to a second backup/recovery appliance or to the cloud for recovery, disaster recovery, or test or dev purposes. Data replication has long been an inhibitor to efficient data management in a geographically distributed environment. Backup and DR replication addresses these issues with compression that:

  * Drives down overall network usage.

  * Eliminates the need for a dedicated WAN accelerator or optimizer.

  * Encrypts data using the AES-256 encryption standard. Authentication between backup/recovery appliances is performed using 1024-bit certificates.




Replication is controlled by Backup and DR policy template policies:

  * **Production to Mirror** policies have several options to replicate data to a second backup/recovery appliance.

  * **Production to OnVault** policies use a Backup and DR proprietary engine to transfer data to object storage.




## Replicate logs

When a policy's **Enable Database Log Backup** is set to **Enable** , the **Replicate Logs advanced setting allows** Microsoft SQL Server database transaction logs to be replicated to a remote backup/recovery appliance. For a log replication job to run, there must be a StreamSnap replication policy included in the template along with a resource profile that specifies a remote backup/recovery appliance, and at least one successful replication of the database must first be completed. You can then use the logs at the remote site for any database backup within the retention range of the replicated logs. This function is enabled by default.

Log replication uses StreamSnap technology to perform the replication between the local and remote backup/recovery appliances; log replication goes directly from the local snapshot pool to the snapshot pool on the remote appliance.

Logs may also be replicated to an OnVault pool. When enabled (not default), logs are sent to each OnVault pool specified by a valid OnVault policy or resource profile combination (e.g., OnVault pool one selected in the policy, and OnVault pool one specified in the resource profile). Log retention in the OnVault pool always matches the log retention in the snapshot pool.

## Access SQL Server data

For Microsoft SQL Server databases that use the full recovery model, Backup and DR can instantly present a copy of the database rolled forward to a specific point of time. The roll forward operation is specified in the appliance management console.

For Microsoft SQL Server databases that use the basic recovery model, Backup and DR can instantly present any backup of the database that has not passed its retention period.

Regardless of the Microsoft SQL Server recovery model used, Microsoft SQL Server data can be accessed using iSCSI interface. If you are using VMware (GCVE), data may also be accessed using an NFS Datastore presented to the ESXi host.

### Role-based access control

You can control which users have access to data, Backup and DR features, and resources. Captured data can be marked sensitive, and Backup and DR users can be granted access permission to sensitive data.

### Mounts

The Backup and DR mount function provides instant access to data without moving data. Captured copies of databases can be rolled forward using the Backup and DR user interface and mounted on any database server. Backup and DR provides two ways to mount an Microsoft SQL Server database:

  * **The Virtual Application mount** presents and makes the captured **Microsoft SQL Server** data available to a target server as an **Microsoft SQL Server** database. This lets you create and manage copies of production databases for non-production use. Virtual application mounts are created from the backup/recovery appliance and don't require manual intervention by database, server, or storage administrators. Virtual application mounts can be used for database reporting, analytics, integrity testing, and test and development. Virtual databases are detailed in [Mount a SQL Server database as a new virtual database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/sql-access#VirData) and [Mount databases into SQL Always On Availability groups](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/sql-create-AAG-mount).

  * **The standard mount** , also called a direct mount, presents and makes the captured **Microsoft SQL Server** data available to a target server as a file system, not as a database. This is useful if a database is corrupt, lost, or if a database server is being replaced. In such cases you cannot use a restore operation to recover the database. Instead, you can mount a backup and copy the database files from the mounted backup to their original location on the database server. Direct Mounts are detailed in [Mount captured Microsoft SQL data](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/sql-access#MicroSQL).


**Note:** OnVault pools pointing to backup vaults don't support mount operations.

### LiveClones

A LiveClone is an independent copy of Microsoft SQL Server data that can be refreshed and masked before being made available to users. This enables development and test teams to work on the latest set of data without having to manually manage the data or interfere with the production environment.

### Clones

The clone function moves a copy of the production data to a different location from the source. The amount of time required to complete a clone operation depends on the amount of data involved. Clones are detailed in [Clone SQL Server databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/sql-cloning).

### Restores

A restore reverts the production data to a specified point in time. Restore operations actually move data. Restore operations are typically performed after a massive data corruption. The amount of time required to complete a restore operation depends on the amount of data involved.

To restore a database and then apply logs, the restored database must be in **Restoring Mode**. You can restore the database in **Restoring Mode** and then roll the logs forward to a specific point in time. If you restore the database without specifying **Restore with no Recovery** , the database will be restored and brought online without applying logs. Restores are detailed in [Restore SQL Server databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/sql-restore). For a near-zero-downtime restore, mount the data first as detailed in [Mount and migrate SQL data](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/sql-server-mount-and-migrate).

## Workflows to automate access to SQL Server data

Workflows automate access to the captured Microsoft SQL Server data. Workflows can present data as a direct mount or as a LiveClone:

  * Direct mounts (standard or application aware) work well for Microsoft SQL Server data that does not need to be masked prior to being presented. A mounted copy of data can be refreshed manually or automatically on a schedule. Direct mounts allow you to instantly access captured Microsoft SQL Server data without actually moving the data.

  * A LiveClone is a copy of your production Microsoft SQL Server data that can be updated manually or on a scheduled basis. You can mask sensitive data in a LiveClone prior to making it available to users.




Combining Backup and DR's automated Microsoft SQL Server data capture and access control with workflows and their optional data masking capabilities lets you create self-provisioning environments. Users can provision their own environments almost instantly.

For example, a Backup and DR administrator can create a backup template policy that captures Microsoft SQL Server data according to a specified schedule. The administrator can mark the captured production Microsoft SQL Server data as sensitive and only accessible by users with the proper access rights.

After access rights have been defined and data has been captured, the administrator can create a workflow that:

  * Makes the captured Microsoft SQL Server data available as a LiveClone or as a direct mount.

  * Updates the LiveClone or mountable Microsoft SQL Server data on a scheduled or on-demand basis

  * Optionally automatically applies scripts to the LiveClone's Microsoft SQL Server data after each update. This is useful for masking sensitive Microsoft SQL Server data.




Once the Workflow completes, users with proper access can provision their environments with the LiveClone or mountable Microsoft SQL Server data.

## Backup and DR working with existing backup products

As more and more enterprises look to speed up the application development using production databases, Backup and DR is often required to coexist with legacy backup products working off the same production database environments. Backup and DR can perfectly co-exist with other products capturing data from production databases, if these best practices are followed.

Backup and DR has a proprietary method of change block tracking so backup solutions using SQL or other methods of obtaining the backups are not impacted by a scheduled Backup and DR data capture jobs.

Backup jobs can be very I/O intensive. They may have long durations, and may impact performance of the database during the backup windows. Backup and DR minimizes the impact during jobs, but even a block-level incremental-forever update must generate some I/O, and must take a little time.

**Requirement** |  Don't schedule legacy backup software and Backup and DR to run jobs in a way that allows any overlap in time.   
---|---  
**Best Practice** |  Schedule Backup and DR database jobs to begin at a time when the legacy backup software should be finished. Don't schedule the legacy backup software to run immediately after an Backup and DR job would normally complete.   
**Reason** |  If legacy backup jobs and Backup and DR jobs run concurrently, it may result a serious performance impact on the database server leading to instability and possibly an outage.   
  
Database logs are used to capture individual transactions in a database, enabling point-in-time recoveries. Most agility use cases center around getting database snapshots on a periodic basis from production. Common frequency ranges from daily to weekly or once in two weeks, depending on the use case. As a result, application developers don't commonly have the need to position their non-prod instance to a specific point-in-time from the source (production). This usually eliminates the need to capture and manage logs as a part of a Backup and DR agility solution.

**Requirement** |  Only one system can manage (capture or truncate (purge)) logs, either the legacy backup software or Backup and DR.   
---|---  
**Best Practice** |  Continue to allow all log management be performed by the legacy backup software, don't use Backup and DR to protect logs in this environment.   
**Reason** |  If your system is configured to manage (capture or truncate(purge)) logs, and the legacy backup software is also capturing and/or truncating/purging logs, then one or both systems may end up with an incomplete log chain, making it difficult or impossible to recover the database to a specific point in time.   
  
## Other documentation for Backup and DR for Microsoft SQL Server

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

[Prepare SQL server databases for Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-sql-server).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
