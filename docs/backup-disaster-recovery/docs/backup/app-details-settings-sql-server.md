---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-sql-server/
title: Configure application details and settings for Microsoft SQL Server databases in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:36:03.280148+00:00
---

# Configure application details and settings for Microsoft SQL Server databases in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-sql-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Configure application details and settings for Microsoft SQL Server databases in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

## Configure advanced settings for policy settings overrides

Click **Policy Overrides** in the **Manage Backup Plan** window to show the **Policy Settings Override** dialog. You can override specific policy settings associated with the selected backup template. When done, click **Save Changes**.

To reset a policy override setting to its default state, click the checkbox next to the selection; click **Select options that will revert back to default** to reset all policy override settings back to their default state.

**Note:** You can override policy settings in the **Application Manager** only if the policy template **Allow Overrides on Policy Settings** parameter has been set to **Yes**.

The following list has descriptions for the policy settings overrides valid for SQL Server instances, availability groups (AG), databases, and consistency groups.

  * **Do Not Unmap.** Keep staging disks mapped between jobs: Select this if you want temporary staging disks mapped to the host and used during data movement to remain mapped to the host. LUNs are mapped during the first job and all subsequent jobs reuse the same mapped LUN. By default, this option is selected. Unmap staging disks after each job: This option both unmounts the staging disk from the operating system at the conclusion of every job (removing mount points or drive letters), and also unmaps it from the host altogether. This option requires the host to perform a scan for SCSI LUNs at the start of the next job, as the re-mapped staging disks must be rediscovered before they can be remounted.

**Note:** For applications protected using the Backup and DR agent where the application is on an OS running inside a VMware VM, this behaves differently. The staging disk is unmapped from the VM after every job, but, LUNs are not unmapped from the ESX hosts.
  * **Truncate Log After Backup.** Specify whether to truncate the logs after every backup. When enabled, application-related logs are truncated until the recent or current backup. If you truncate logs, you must also back up the transaction log to enable a roll-forward recovery.

  * **Skip Offline Applications in the Consistency Group.** For consistency group management only. Specify whether to ignore unavailable databases that are part of a consistency group. Create a consistency group to back up multiple databases together to preserve consistency of data. Consistency groups are collections of databases from the same instance or availability group.

**Note:** Backups at the instance or availability group also provide consistency across all included databases.

The options are:

    * Fail backup when offline applications are found
    * Skip offline applications during backup
  * **Map staging disks to all ESX Hosts in a Cluster.** (This option is not relevant when using NFS datastores.) Map staging disk to ESX host for VM only. Map staging disk to all ESX hosts in the cluster. Map staging disk to two ESX hosts in the cluster.

**Note:** VMs can only be moved to a different ESX host during a backup if the staging disk is mapped to both the source and destination ESX host. Choosing two hosts reduces job durations and minimizes iSCSI HBA scanning on the ESX hosts.
  * **Backup SQL Server User Logins.** Backup of the SQL Server instance login records for accounts granted access to databases being backed up. When the database is mounted as a virtual application (application aware mount) the backed up user logins can be optionally restored into the target SQL Server instance, ensuring the virtual database will be accessible by the same users with access to the original source database. The options are **Yes** or **No**.

  * **Enable Database Log Backup.** The **Enable Database Log Backup** option allows the backup plan policy to backup an Oracle or SQL Server database and all associated transaction log files. The logs are backed up when the log snapshot job runs. The options are **Yes** or **No**. When set to **Yes** , the related options are enabled.

**Note:** For details on **Log Protection** , see Database Log Protection in a backup plan policy.
  * **RPO.** When **Enable Database Log Backup** is set to **Yes** , RPO defines the frequency for database log backup. Frequency is set in minutes and must not exceed the database backup interval. The smallest value that can be set (in minutes) is 15.

  * **Log Backup Retention Period.** When **Enable Database Log Backup** is set to **Yes** , log retention is defined separately from the retention of the snapshot policy. Having a separate retention period lets you use logs in conjunction with copies of the database stored in the snapshot pool. The log retention period is a mandatory setting.

  * **Replicate Logs.** (Uses StreamSnap Technology) When **Enable Database Log Backup** is set to **Enable** , the **Replicate Logs** advanced setting allows SQL Server database transaction logs to be replicated to a remote backup/recovery appliance. For a log replication job to run, there must be a StreamSnap replication policy in the template along with a resource profile that specifies a remote backup/recovery appliance. Also there must be at least one successful replication of the database must first be completed. You can then use the logs at the remote site for any database image within the retention range of the replicated logs. This function is enabled by default.

Log replication uses StreamSnap technology to perform the replication between the local and remote backup/recovery appliances; log replication goes directly from the local snapshot pool to the snapshot pool on the remote appliance.

**Note:** Log replication does not occur until a SQL Server database has been protected and the database has been replicated to the remote appliance.
  * **Send Logs to OnVault Pool.** When **Enable Database Log Backup** is set to **Enable** , this setting allows SQL Server database transaction logs to be replicated to an OnVault pool. To run a log replication job, there must be an OnVault policy included in the template along with a resource profile that specifies an OnVault pool. Also at least one database must first be sent to the pool. Then use the logs at the remote site for any database image within the retention range. This function is enabled by default.

  * **Log Staging Disk Growth Size.** When **Enable Database Log Backup** is set to **Yes** , **Log Staging Disk Growth Size** defines the growth to use when automatically growing the staging disk on which the logs reside. This setting is from 5 to 100 percent.

  * **Estimated Change Rate.** When **Enable Database Log Backup** is set to **Yes** , this setting defines the daily change (in percent), which allows the backup/recovery appliance to better calculate the size of the staging disk needed to hold logs. This setting is from 0 to 100.

  * **Compress Database Log Backup.** When **Enable Database Log Backup** is set to **Yes** , this setting instructs the source database to compress its logs before they are backed up by appliance management console. The database server performs log compression during log backup. The options are **Yes** or **No**. When set to **Yes** , the **Compress Database Log Backup** option is enabled.

  * **Script Timeout.** The Backup and DR agent lets you create host-side scripts that run on an application's host before or after a policy is run. The four timeouts provided in a policy template map directly into the four stages of a host-side script.

    * **Script Init Timeout.** Defines how long a policy should wait before assuming host-side scripts on a managed host have been initialized. 120 seconds is the default value, allowed range is from 1 to 86400 seconds (24 hours).
    * **Script Freeze Timeout.** Defines how long a policy should wait before assuming the application is frozen and ready for data back up. 60 seconds is the default value, allowed range is from 1 to 86400 seconds.
    * **Script Unfreeze Timeout.** Defines how long a policy should wait before assuming the application is unfrozen. 60 seconds is the default value, allowed range is from 1 to 86400 seconds.
    * **Script Finish Timeout.** Defines how long a policy should wait before data back up is complete. 60 seconds is the default value, allowed range is from 1 to 86400 seconds.
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

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
