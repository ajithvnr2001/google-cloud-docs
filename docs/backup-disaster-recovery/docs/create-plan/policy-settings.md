---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings/
title: Configure advanced policy settings in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:41.735989+00:00
---

# Configure advanced policy settings in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Configure advanced policy settings in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page lists the advanced settings for a backup configuration policy template. You can define the advanced policy settings while creating a [backup policy](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview).

You can also view and change the policy settings for specific applications by displaying the policy overrides panel from the **Manage Backup Plan** page for the application.

Use the following instructions to view the policy settings page.

  1. In the appliance management console, click the **Backup Plans** tab and select the **Templates** option from the drop-down.
  2. Select the template to manage and then click **Edit** from the drop-down at the bottom right corner of the page.
  3. On the template page, on the right side, click the white arrow beside the policy that you want to manage. At the bottom of the selections, click **Edit Policy**.
  4. At the bottom of the **Create/Edit Policy** section click **Advanced Policy Settings**. This opens the advanced policy settings detailed in the following table.
  5. When you are finished, click **Save Changes** to update the settings.

**Note:** The **Policy Overrides** settings page might not show all the settings listed in the following table. It only displays relevant settings based on your application.



The following table details the advanced policy settings.

Advanced setting | Description  
---|---  
**Application consistent**   
(applicable only for Google Cloud VMware Engine VMs and Compute Engine VMs) | Select one of the following:   

* **Crash consistent backup** : Crash consistent backup is a fast backup of application data in storage as if power were lost at that moment. It doesn't pause application data I/O. All data on disk is saved, and data in memory is lost. The recovery of a crash consistent backup might take longer and introduce exceptions. It might be required to perform some additional manual recovery steps during the recovery, depending on the guest OS, file systems, and applications. Choose crash consistent if the application consistent process causes issues for your applications or workloads due to the quiescing process. Crash consistent might result in a longer RTO due to the need for the file system or application to perform a recovery from the inconsistent snap, and could even result in an unrecoverable snap in extreme cases. 
* **Take application consistent backup** : Application consistent backup leverages quiesced snapshots, which uses VMware tools or a Google Cloud guest environment to quiesce the file system of the virtual machine. A quiesce operation leverages Windows operating built-in capabilities to quiesce file systems and applications that support VSS. It also leverages any customer supplied freeze or thaw scripts (on all platforms) to get higher level application consistency. The result is a higher confidence level in the recoverability of the backup, as well as shorter recovery times in most cases. Application consistent backups can sometimes cause a brief pause in I/O, and while uncommon, some busier applications might report I/O errors at the time of the backup. Occasionally, application consistent backups fails if VMware is unable to quiesce the VM within a predetermined timeout during the snapshot operation. Use application consistent backups when recoverability is most important, and the applications in the VM aren't sensitive to the brief I/O pause.   
Read the [Create a Linux application consistent persistent disk snapshot](https://docs.cloud.google.com/compute/docs/disks/creating-linux-application-consistent-pd-snapshots) section for more information.   
  
To mount a Windows Compute Engine snapshot as a new or an existing VM that is captured with the **Application consistent** option, you must change the disk from read-only to read-write mode. To do this, follow the instructions in [Optional: Mark your disk as available for read and write](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot#read-only). 
* **Take crash consistent backup on last try** : This option initially takes application consistent backups, but if an application consistent backup fails for any reason, it takes a crash consistent backup.  
**Snapshot location**   
(applicable only for Compute Engine and SAP HANA instances) | Select the region where the Persistent Disk snapshots are to be stored. By default, multi-region is selected (based on the source disk location). You can also change the snapshot storage location to a different region than the source disk region. When storing snapshots in a location that is different from the location of your source disk, the data travels over the network between those locations and might incur network fees. Snapshots incur the same fees as Cloud Storage data transfer. Learn more about the [persistent disk snapshot.](https://docs.cloud.google.com/compute/docs/disks/snapshots) To know the pricing details, see [disk pricing.](https://docs.cloud.google.com/compute/disks-image-pricing#disk)  
**Snapshot type**   
(applicable only for Compute Engine and SAP HANA instances) | Select the Persistent Disk snapshot type to be used for Compute Engine instance backups. Snapshots incrementally backup data from Persistent disks. During backups, a new snapshot is created to capture the current state of the Persistent disk and later can be used to create a new disk for mounts or restores. Compute Engine stores multiple copies of each snapshot across multiple locations with automatic checksums to ensure the integrity of your data. Learn more about the [persistent disk snapshot.](https://docs.cloud.google.com/compute/docs/disks/snapshots) To know the pricing details, see [disk pricing.](https://docs.cloud.google.com/compute/disks-image-pricing#disk)   

* **Standard** : By default, the Standard snapshot type is selected. It is recommended to use the standard type if you want to retain the backups for less than 90 days. 
* **Archive** : Select the Archive type if you want to retain the backups for long duration. Note that the minimum billing period for the archive snapshot is 90 days irrespective of the retention period defined in policy and that Archive type also has an additional retrieval charge if used in a mount or restore job.  
**Staging Disk Over-allocation**   
(In percentage) | Specify the extra space allocated for staging disk (on top of what's actually needed) to accommodate growth of the application. This setting is from zero to 1000 percent.  
**Global Prune Paths** | Don't back up these directories (specify full path). Also see the policy-level Global Prune Paths values.  
**Compress Streamsnap Replication** | By default, compression for streamsnap replication is enabled. Compression increases the efficiency of the streamsnap replication to the remote backup/recovery appliance when transferring data over the network, for example, when replicating backups and videos. When compression is enabled, all of the packets are compressed. The target backup/recovery appliance decompresses the packets before writing to the staging disk. If compression isn't needed for streamsnap replication to the second backup/recovery appliance, then change the compress streamsnap replication advanced setting to **Don't compress** and then click **Save Changes**.   
Note: Streamsnap replication is only supported for the backup/recovery appliances deployed in a single network.   
**Do Not Unmap** | Specifies if you want temporary staging disks mapped to the host and used during data movement for backup to remain mapped to the host. LUNs are mapped during the first job and all the subsequent jobs reuse the same mapped LUN. Select either: 
* Keep staging disks mapped between jobs. Select this option if you want the temporary staging disks mapped to the host and used during data movement to remain mapped to the host. LUNs are mapped during the first job and all the subsequent jobs reuse the same mapped LUN. By default, this option is selected.   
Note: For applications managed using the Backup and DR agent (such as SQL database) where the application is on an OS running inside a VMware VM, this option is ignored. The staging disk is always be unmapped from the VM after every job.
* Unmap staging disks after each job. This option both unmounts the staging disk from the operating system at the conclusion of every job (removing mount points or drive letters), and also unmaps it from the host altogether. This option requires the host to perform a scan for SCSI LUNs at the start of the next job, as the re-mapped staging disks must be rediscovered before they can be remounted.  
**Truncate (Purge) Log After Backup** | Specify whether to truncate (purge) the database logs after every backup. When **Truncate Log After Backup** is enabled, application-related logs are truncated until the recent or current backup. If you truncate logs, you must also back up the transaction log to enable a roll forward recovery.   
The options are: 
* Don't truncate or purge log after backup
* Truncate or purge log after backup  
**Skip Offline Applications**   
(For Consistency Group management only) | Specify whether to ignore unavailable applications that are part of a consistency group. You create a consistency group to back up the data of all member applications together to preserve consistency of data across the member applications. Consistency groups are collections of discovered applications from the same host.   
Options are: 
* Fail backup when offline applications are found
* Skip offline applications during backup  
**Map staging disks to all nodes in an application cluster** | If your nodes are in an application cluster, you can use this to ensure that the nodes of an application cluster are protected in case of failover during backup.   

* Don't map staging disk to all nodes of application cluster.
* Map staging disk to all nodes of application cluster   
In the event of an application cluster failure, this option protects failover copies.  
**Map Staging Disk to All ESX Hosts in a Cluster**   
(For VMware VMs only)  | If your ESX servers are in an appliance, you can use this setting to ensure that the VMs are managed in case of failover during backup. In the event of an ESX host failure, this option manages failover copies of VMware VMs. (Oracle, local file systems, SMB, NFS, SQL Server):   

* Map staging disk to ESX host for VM only
* Map staging disk to all ESX hosts in the cluster
* Map staging disk to two ESX hosts in the cluster  
**Backup SQL Server User Logins** | Captures the SQL Server database login credentials. When the database is mounted as a virtual application (app aware mount) the virtual database has all of the login credentials used by the source. The options are **Yes** or **No**.  
**Enable Database Log Backup** | The **Enable Database Log Backup** option allows the backup plan policy to backup a database and all associated transaction log files. The logs are backed up when the log snapshot job runs. Options are Yes or No. When set to **Yes** , the related options are enabled.   
Note: For details on **Log Protection** , see [ Database Log Protection in a backup plan policy](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan-policy-best-practices#Log-protection).  
**RPO** | When **Enable Database Log Backup** is set to **Yes** , RPO defines the frequency for database log backup. Frequency is set in minutes and must not exceed the database backup interval. The smallest value that can be set (in minutes) is 15.  
**Log Backup Retention Period**   
(In Days) | When **Enable Database Log Backup** is set to **Yes** , log retention is defined separately from the retention of the snapshot policy. Having a separate retention period lets you use logs in conjunction with copies of the database stored in the snapshot pool. The log retention period is a mandatory setting.  
**Replicate Logs**   
(Uses Streamsnap Technology) | When **Enable Database Log Backup** is set to **Enable** , the **Replicate Logs** advanced setting allows database logs to be replicated to a remote appliance. For a log replication job to run, there must be streamsnap replication policy included in the template along with a resource profile that specifies a remote appliance, and at least one successful replication of the database must first be completed. You can then use the logs at the remote site for any database backup within the retention range of the replicated logs. This function is enabled by default.   
Log replication uses streamsnap technology to perform the replication between the local and remote appliances; log replication goes directly from the local snapshot pool to the snapshot pool on the remote appliance.   
Note: Log replication doesn't occur until database has been protected and the backup replicated to the remote appliance.  
**Send logs to OnVault Pool** | Set to **Yes** , logs are replicated to one or more OnVault storage pools enabling for point-in-time recoveries from OnVault on another site.  
**Note** : If you select this, then Backup and DR sends logs to every OnVault pool defined in the profile for that application. If there are two pools in the profile, then the monitor will show OnVault (log) jobs for each log backup, one for each pool. Only OnVault pools that are in the profile for that SLA will get the logs. 

  * The retention of logs replicated to OnVault is similar to snapshot log retention.
  * Replicating database logs to an OnVault bucket is different from a database backup. If you select **Send logs to OnVault Pool** , then Backup and DR will continuously replicate the logs to OnVault buckets similar to log snapshot backups. For example, if a log backup is taken every 15 minutes, then the logs will be replicated to OnVault every 15 minutes to ensure all log snapshots are replicated to OnVault pools.
  * The policy ID shown in the appliance management console is the snapshot policy ID as this replication of logs to OnVault buckets is tied to Snapshot policy.

**Note** : Daily, Weekly, Monthly and Yearly OnVault policies are only for database backups, they don't apply to log backups.   
**Log Staging Disk Growth Size (In Percent)** | When **Enable Database Log Backup** is set to **Yes** , **Log Staging Disk Growth Size** defines the growth to use when automatically growing the staging disk on which the logs reside. This setting is from five to 100 percent.  
**Estimated Change Rate** | When **Enable Database Log Backup** is set to **Yes** , this setting defines the daily change (in percent), which allows the appliance to better calculate the size of the staging disk needed to hold logs. This setting is from zero to 100.  
**Compress Database Log Backup** | When **Enable Database Log Backup** is set to **Yes** , this setting instructs the source database to compress its logs before they are captured by the appliance management console. The database server performs log compression during log backup. The options are **Yes** or **No**. When set to **Yes** , the **Compress Database Log Backup** option is enabled.  
**Enforced Retention** | Allows the user to configure their immutability period between zero and 36525 days. By default, the value is set to zero for all existing policies.   
You can modify a policy that is already used to protect an application by setting a longer enforced retention period. However, you can't shorten the enforced retention period.   
You can't set enforced retention for a streamsnap policy whose retention is "Only keep the most recent remote image".   
Note: **Enforced Retention** can't be overridden on a per-application basis. The option doesn't appear on the **Policy Overrides** page.   
Note: The **Enforced Retention** advanced policy setting is not compatible with application protection that points to a backup vault. When a backup vault is the storage target, the backup vault determines the enforced retention period.   
**Job Behavior When Target VM Needs snapshot Consolidation** | Select an action if the VM requires consolidation:   

* Fail the job if VM needs consolidation: Point-in-time jobs fail.
* Run the job without performing consolidation: All jobs run normally even if consolidation is pending.
* Perform consolidation at the beginning of the job: Point-in-time jobs try to perform consolidation at the beginning of the job. If consolidation fails, the job fails with an error message.  
**Fail On Missing Start Path** | If one or more start paths are specified, and any of these start paths doesn't exist, the job fails with the message UDSAgent: Specified start path doesn't exist. If no start paths are specified, this option has no effect. Options are **Yes** or **No**.   
Note: The default state for this option is No (disabled), which is the same behavior of the previous versions of the Backup and DR agent; the job doesn't fail if a start path doesn't exist.  
**Enable Degraded Capture Mode** | Degraded capture mode captures incremental data when **Change Block Tracking** (CBT) service is unavailable. Data capture might take longer. The options are **Yes** or **No**.  
**Script Timeout**   
(applicable only for agent based backups) | The Backup and DR agent lets you create host-side scripts that run on an application's host before or after a policy is run. The four timeouts provided in a policy template map directly into the four stages of a host-side script.   
Note: By default, the script timeout values are per the following values. If a script timeout isn't specified, the value is blank and the default is used. 
* **Script Init Timeout** : Defines how long a job should wait for the script that is invoked on the host before any action is taken by the job. If the script doesn't complete within this timeout, the job fails. The default value is 60 seconds. Allowed range is one to 86400 seconds.
* **Script Freeze Timeout** : Defines how long a policy should wait for the script that is invoked in order to freeze an application, before a snapshot is taken. If the script doesn't complete within this timeout, the job fails. The default value is 60 seconds. Allowed range is one to 86400 seconds. 
* **Script Unfreeze Timeout** : Defines how long a policy should wait for the script that is invoked in order to freeze an application, after a snapshot is taken. If the script doesn't complete within this timeout, the job fails. The default value is 60 seconds. Allowed range is one to 86400 seconds. 
* **Script Finish Timeout** : Defines how long a policy should wait for the script that is invoked at the very end of the job. If the script doesn't complete within this timeout, the job fails. The default value is 60 seconds. Allowed range is one to 86400 seconds.  
  
## What's next

  * Get an overview of [backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan)
  * Create a [backup template](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template)
  * Create a [backup policy](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview)
  * Create a [resource profile](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/resource-profiles)
  * [Apply a backup plan to an application](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-temp-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
