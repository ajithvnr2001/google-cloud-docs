---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/back-up-sql-server/
title: Back up Microsoft SQL Server instances and databases to appliance-managed backup \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:58.849836+00:00
---

# Back up Microsoft SQL Server instances and databases to appliance-managed backup  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/back-up-sql-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Back up Microsoft SQL Server instances and databases to appliance-managed backup Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Backup and DR lets you back up Microsoft SQL Server:

  * Instances

  * Primary database of an Always On availability group

  * Databases in VMs

  * System databases

  * User databases

  * Databases and support files in a consistency group

  * Individual members of a consistency group




## Before you begin

Before you protect Microsoft SQL Server databases:

  * Add the hosts and discover their databases using the appliance management console SQL Server wizard as detailed in [Add a SQL Server database host and discover databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-sql-server)

  * Create [Backup plan policy templates](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template) and [Resource profiles](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/resource-profiles#create-profile) that define how to protect the databases.




## Best practices for protecting Microsoft SQL Server databases

For Microsoft SQL Server databases that use the full recovery model, take advantage of the backup/recovery appliance's ability to back up both the database and its logs with a single policy. When both the database and its logs are backed up, the appliance can recover the database to a point in time by rolling its logs forward using the appliance's user interface. Backing up both the database and its logs is enabled using the policy template's advanced settings.

### Back up databases in an instance versus a consistency group

When a database is quiesced to create a backup, a snapshot of its disks is created and then released. For consistency groups and database instances, members are quiesced and released together for a consistent point-in-time of data.

When backing up a **SQL Instance** , as databases are added to the instance, they are automatically included in the Backup and DR backup operation. Backing up databases in a SQL instance lends itself to environments where databases are regularly added and removed. Databases mounted to a SQL instance as virtual applications are not protected with the other members of the instance. Virtually mounted databases must be protected separately.

Membership to a **consistency group** is done manually. Backing up databases in a consistency group lends itself to environments where databases are not often added or removed.

### Database versus VM management

Microsoft SQL Servers are protected differently whether they are protected as an application (database, instance, or availability group) or as part of an entire VM.

Protected as an Application, Not ESP  | Protected as Part of a VM  
---|---  
Backup/recovery appliances protects only the database files.  |  Entire VMware VMs are backed up using VMware APIs. If you are managing SQL databases that are part of an entire protected VM, see [Protect and recover Compute Engine instances](/backup-disaster-recovery/docs/quickstarts/gce-instances-backup-recovery).   
Backup and DR agent coordinates the VSS snapshot and performs log truncation.  |  The VMware API coordinates the VSS snapshot. The Backup and DR agent must be installed on the VM for log truncation.   
The Backup and DR agent uses change block tracking on named files—very efficient for large database files.  |  The VMware API provides change block tracking.   
Transaction logs are backed up when a backup job runs if you select **Truncate Log After Backup** in **Details & Settings** (see [Configure advanced settings for policy settings overrides](: #SetOverrides)  |  Transaction logs are not backed up.   
Client can roll forward with logs.  |  Roll forward not supported during restore.   
  
Use the following instructions to apply a backup plan to protect a Microsoft SQL server database.

  1. From the Backup and DR appliance management console, go to **App Manager** > **Applications**. The **Applications** page opens.

  2. Select the Microsoft SQL server database, instance, AG, or consistency group that you want to back up and in the lower right corner of the page select **Manage Backup Plan**.

  3. From the **Manage Backup Plan** window, choose a **Template** and **Profile** from the drop-down lists:

     * **Template.** An existing backup template that includes policies to define the snapshot and replication of the application data.

     * **Profile.** An existing resource profile that defines the resources used to store the data of the application as snapshot and replicated images.

  4. From the **Manage Backup Plan Template** window make the following changes prior to applying a backup plan:

     * **Application Settings.** Settings specific to Microsoft SQL such as application type, hostname, host IP address, path, operating system, backup/recovery appliance, and appliance IP address.

     * **Policy Overrides.** Override specific policy settings previously configured in the selected backup template. Policy overrides can be useful or required in certain circumstances. You can only override policy settings if the policy's template has been configured to allow policy settings overrides.

  5. To select databases, under **Database Inclusion Rule** , click **Edit**. The **Manage Membership** dialog opens.

     * From the **Manage Membership** dialog, select the databases to back up by assigning an inclusion rule (**All** , **System Databases** , **User Databases**), and then select whether the rule should **Include Selected** or **Exclude Selected**.

     * Click **Save** and the **Manage Membership** dialog closes.

  6. Click **Apply** to apply the backup template and resource profile and the success message box appears.

The first time the selected database is discovered, an on-demand job runs as soon as possible to protect the data. Afterward, new data is backed up when the scheduled job runs according to the hours of operations defined in the backup template. For example, if at 10:00 (UTC) you assign a template that has hours of operation from 02:00 to 05:00 (UTC), then the first job won't start until the appliance has an available job slot after 02:00 (UTC).

If you back up a workload to a backup/recovery appliance that would exceed its recommended storage capacity or snapshot limit, you will see a notification with a recommendation to back up the data to a different backup/recovery appliance.

**Caution:** Exceeding the capacity of a backup/recovery appliance can lead to failed jobs and unprotected data and failed restore operations.



### Database log protection in a Backup plan policy

When creating a snapshot policy for a database you can also back up its log files. The frequency at which database logs are backed up is defined separately from that of the database. For example, a database can be backed up every day and its logs backed up every hour. The frequency of database log backup is set in minutes, and the frequency at which logs are backed up must not exceed the frequency at which its associated database is backed up. For example, if a database is backed up every 24 hours, the log file back up frequency must be less than every 24 hours.

Frequency and retention are defined in the **Details & Settings** of the database snapshot policy. Log back up is done without regard to when its associated database is backed up.

You enable the **Log Protection** through the **Enable Database Log Backup** advanced settings in a backup plan snapshot policy. Frequency and retention are defined in the **Details & Settings** for a backup plan policy.

The space required to accommodate a database's logs is automatically managed by the appliance management console. The appliance management console evaluates typical log sizes and their retention period and adds space as needed. To manage the storage requirements for a database's logs, Snapshot policies provide the following advanced settings:

  * **Log Backup Retention Period.** Log retention is defined separately from the retention of the snapshot policy. Having a separate retention period lets you use logs in conjunction with copies of the database stored in the Snapshot pool and optionally in an OnVault pool. The log retention period is mandatory when log backups are enabled.

  * **Replicate Logs.** You can replicate database logs to a remote backup/recovery appliance or to an OnVault pool, and use the remote logs for any database image within the retention range of the replicated logs. Log replication uses StreamSnap technology between the local and remote appliances, going directly from the local snapshot pool to the snapshot pool on the remote appliance. This requires a StreamSnap replication policy in the template, and at least one successful replication of the database must first be completed.

  * **Log Staging Disk Size Growth Size.** Defines the percent at which to automatically grow the staging disk on which the logs reside. This setting is a percentage and valid values are from 5 to 100.

  * **Estimated Change Rate.** Defines the daily change (in percent), which allows the backup/recovery appliance to better calculate the size of the staging disk needed to hold logs. This setting is a percentage and valid values are 0 to 100.

  * **Compress Database Log Backup.** Instructs the source database to compress its logs before back up. The database server performs log compression during log backup.




## Configure advanced settings for policy settings overrides

Click **Policy Overrides** in the **Manage Backup Plan** window to show the **Policy Settings Override** dialog. From here you can override specific policy settings associated with the selected backup template. After you are done, click **Save Changes**.

To reset a policy override setting to its default state, click the checkbox to the left of the selection; click **Select options that will revert back to default** to reset all policy override settings back to their default state.

**Note:** You can override policy settings in the **Application Manager** only if the policy template **Allow Overrides on Policy Settings** parameter has been set to **Yes**.

The following list has descriptions for the policy settings overrides valid for SQL Server instances, availability groups (AG), databases, and consistency groups.

  * **Do Not Unmap.** Keep staging disks mapped between jobs: Select this if you want temporary staging disks mapped to the host, and used during data movement to remain mapped to the host. LUNs are mapped during the first job and all subsequent jobs reuse the same mapped LUN. By default, this option is selected. Unmap staging disks after each job: This option both unmounts the staging disk from the operating system at the conclusion of every job (removing mount points or drive letters), and also unmaps it from the host altogether. This option requires the host to perform a scan for SCSI LUNs at the start of the next job, as the re-mapped staging disks must be rediscovered before they can be remounted.

**Note:** For applications protected using the Backup and DR agent where the application is on an OS running inside a VMware VM, this behaves differently. The staging disk is unmapped from the VM after every job, but, LUNs are not unmapped from the ESX hosts.
  * **Truncate Log After Backup.** Specify whether to truncate the logs after every backup. When enabled, application-related logs are truncated until the recent or current backup. If you truncate logs, you must also back up the transaction log to enable a roll forward recovery.

  * **Skip Offline Applications in the Consistency Group.** (For consistency group management only) Specify whether to ignore unavailable databases that are part of a consistency group. You create a consistency group to back up multiple databases together to preserve consistency of data across the databases. Consistency groups are collections of databases from the same instance or availability group.

**Note:** Backups at the instance or Availability Group also provide consistency across all included databases.

The options are:

    * Fail backup when offline applications are found
    * Skip offline applications during backup
  * **Map staging disks to all ESX Hosts in a Cluster.** (This option is not relevant when using NFS datastores.) Map staging disk to ESX host for VM only. Map staging disk to all ESX hosts in the cluster. Map staging disk to two ESX hosts in the cluster.

**Note:** VMs can only be moved to a different ESX host during a backup if the staging disk is mapped to both the source and destination ESX host. Choosing two hosts reduces job durations and minimizes iSCSI HBA scanning on the ESX hosts.
  * **Backup SQL Server User Logins.** Backs up the SQL Server instance login records for accounts granted access to databases being backed up. When the database is mounted as a virtual application (application aware mount) the backed up user logins can be optionally restored into the target SQL Server instance, ensuring the virtual database will be accessible by the same users with access to the original source database. The options are **Yes** or **No**.

  * **Enable Database Log Backup.** The **Enable Database Log Backup** option allows the backup plan policy to backup an Oracle or Microsoft SQL Server database and all associated transaction log files. The logs are backed up when the log snapshot job runs. The options are **Yes** or **No**. When set to **Yes** , the related options are enabled.

**Note:** For details on **Log Protection** , see **Database Log Protection** in a backup plan policy.
  * **RPO.** When **Enable Database Log Backup** is set to **Yes** , RPO defines the frequency for database log backup. Frequency is set in minutes and must not exceed the database backup interval. The smallest value that can be set (in minutes) is 15.

  * **Log Backup Retention Period.** When **Enable Database Log Backup** is set to **Yes** , log retention is defined separately from the retention of the snapshot policy. Having a separate retention period lets you to use logs in conjunction with copies of the database stored in the snapshot pool. The log retention period is a mandatory setting.

  * **Replicate Logs.** (Uses StreamSnap Technology) When **Enable Database Log Backup** is set to **Enable** , the **Replicate Logs** advanced setting allows Microsoft SQL Server database transaction logs to be replicated to a remote backup/recovery appliance. For a log replication job to run, there must be a StreamSnap replication policy in the template along with a resource profile that specifies a remote backup/recovery appliance, and at least one successful replication of the database must first be completed. You can then use the logs at the remote site for any database image within the retention range of the replicated logs. This function is enabled by default.

Log replication uses StreamSnap technology to perform the replication between the local and remote backup/recovery appliances; log replication goes directly from the local snapshot pool to the snapshot pool on the remote appliance.

**Note:** Log replication does not occur until a SQL Server database has been protected and the database has been replicated to the remote appliance.
  * **Send Logs to OnVault Pool.** When **Enable Database Log Backup** is set to **Enable** , this setting allows Microsoft SQL Server database transaction logs to be replicated to an OnVault pool. For a log replication job to run, there must be an OnVault policy included in the template along with a resource profile that specifies an OnVault pool, and at least one database must first be sent to the pool. You can then use the logs at the remote site for any database image within the retention range. This function is enabled by default.

  * **Log Staging Disk Growth Size.** When **Enable Database Log Backup** is set to **Yes** , **Log Staging Disk Growth Size** defines the growth to use when automatically growing the staging disk on which the logs reside. This setting is from 5 to 100 percent.

  * **Estimated Change Rate.** When **Enable Database Log Backup** is set to **Yes** , this setting defines the daily change (in percent), which allows the backup/recovery appliance to better calculate the size of the staging disk needed to hold logs. This setting is from 0 to 100.

  * **Compress Database Log Backup.** When **Enable Database Log Backup** is set to **Yes** , this setting instructs the source database to compress its logs before they are backed up by the appliance management console. The database server performs log compression during log backup. The options are **Yes** or **No**. When set to **Yes** , the **Compress Database Log Backup** option is enabled.

  * **Script Timeout.** The Backup and DR agent lets you create host-side scripts that run on an application's host before or after a policy is run. The four timeouts provided in a policy template map directly into the four stages of a host-side script.

    * **Script Init Timeout.** Defines how long a policy should wait before assuming host-side scripts on a managed host have been initialized. 120 seconds is the default value, allowed range is from 1 to 86400 seconds (24 hours).
    * **Script Freeze Timeout.** Defines how long a policy should wait before assuming the application is frozen and ready for data back up. 60 seconds is the default value, allowed range is from 1 to 86400 seconds.
    * **Script Unfreeze Timeout.** Defines how long a policy should wait before assuming the application is unfrozen. 60 seconds is the default value, allowed range is from 1 to 86400 seconds.
    * **Script Finish Timeout.** Defines how long a policy should wait before data backup is complete. 60 seconds is the default value, allowed range is from 1 to 86400 seconds.
    * **Script Post Replication Timeout.** Defines how long a policy should wait before replication is complete. 60 seconds is the default value, allowed range is from 1 to 86400 seconds.



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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
