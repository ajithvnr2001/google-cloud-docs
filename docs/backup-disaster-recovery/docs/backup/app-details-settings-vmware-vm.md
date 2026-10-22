---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-vmware-vm/
title: Configure application details and settings for VM data in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:57.723090+00:00
---

# Configure application details and settings for VM data in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-vmware-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Configure application details and settings for VM data in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page includes information on configuring application settings for VMware VMs.

## Protecting a VM and its applications

In some cases you may be required to capture an entire VM, then capture one or more applications on that VM. In such situations, create two policy templates; one to capture the VM's boot volume and another to capture the applications on the VM. Note that the two capture operations cannot run at the same time.

## Application details and settings for VMware VM

From the **Application Details & Settings** page, modify application-specific settings for configuring backup options for VMware VM. Application settings may be useful or required in certain circumstances. After you configure your application settings, click **Save Changes**.

To reset one or more application settings back to its default state, click the checkbox next to the selection you want to reset, or click **Select options that will revert back to default** to reset all application selections back to their default state.

Application setting | Description  
---|---  
Application consistent   
(Not applicable to database management) | Select one of the following:   

* Take crash consistent backup: Crash consistent backup is a fast backup of application data in storage as if power were lost at that moment. It does not pause application data I/O. All data on disk are saved, and data in memory is lost. Incomplete transactions may be saved. The recovery of a crash consistent backup may take longer time and introduce exceptions. Typically recovery from crash has to be made manually. Crash consistent backups are fast for virtual machines.
* Take application consistent backup: Application consistent backup notifies the application to prepare for a backup. This option loses no data. It pauses application data I/O, completes in flight transactions, and flushes memory to disk. On recovery, data is quickly accessed. For virtual clients, usually an agent is needed to get notification of a backup at host, and then notify applications, and may need to wait for an approval from applications. Not all applications support application consistent backups.
* Take crash consistent backup on last try: This option initially takes application consistent backups, but if an application consistent backup fails for any reason, it then takes a crash consistent backup.  
Staging Disk Over-allocation (in percentage) | Specify the extra space allocated for staging disk—on top of what's actually needed—to accommodate growth of the application. This setting is from 0 to 1000 percent.  
Truncate/Purge Log After Backup | Specify whether to truncate/purge the logs after every backup. When Truncate Log After Backup is enabled, application-related logs are truncated until the recent or current backup. If you truncate logs, you must also back up the transaction log to enable a roll forward recovery. (Oracle, SQL Server).   
Options are: 
* Don't truncate or purge log after backup
* Truncate or purge log after backup  
Log Backup Retention Period (In Days)* | When Enable Database Log Backup is set to Yes, log retention is defined separately from the retention of the snapshot policy. Having a separate retention period lets you use logs in conjunction with copies of the database stored in the snapshot pool. The log retention period is a mandatory setting.  
Replicate Logs (Uses StreamSnap Technology)** | When Enable Database Log Backup is set to Enable, the Replicate Logs advanced setting allows. Oracle archive logs or SQL server database transaction logs to be replicated to a remote backup/recovery appliance. For a log replication job to run, there must be a replication policy (StreamSnap) included in the template along with a resource profile that specifies a remote backup/recovery appliance, and at least one successful replication of the database must first be completed. You can then use the logs at the remote site for any database image within the retention range of the replicated logs. This function is enabled by default. Log replication uses StreamSnap technology to perform the replication between the local and remote backup/recovery appliances; log replication goes directly from the local snapshot pool to the snapshot pool on the remote appliance.   
Note: Log replication does not occur until a database has been protected and the database has been replicated to the remote backup/recovery appliance.  
Send logs to OnVault Pool | Set to Yes, logs get replicated to one or more OnVault storage pool enabling for point-in-time recoveries from OnVault on another site.  
Log Staging Disk Growth Size (In Percent)* | When Enable Database Log Backup is set to Yes, Log Staging Disk Growth Size defines the growth to use when automatically growing the staging disk on which the logs reside. This setting is from five to 100 percent.  
Job Behavior When Target VM Needs Snapshot Consolidation | Select an action if the VM requires consolidation: 
* Fail the job if VM needs consolidation: Point-in-time jobs fail.
* Run the job without performing consolidation: All jobs run normally even if consolidation is pending.
* Perform consolidation at the beginning of the job: Point-in-time jobs try to perform consolidation at the beginning of the job. If consolidation fails, the job fails with an error message.  
Script Timeout | The Backup and DR agent lets you create host-side scripts that run on an application's host before or after a policy is run. The four timeouts provided in a policy template map directly into the four stages of a host-side script.   
Note: By default, the script timeout values are per the values stated. If a script timeout is not specified, the value is blank and the default is used.   

* Script Init Timeout: Defines how long a job should wait for the script that is invoked on the host before any action is taken by the job. If the script does not complete within this timeout, the job fails. The default value is 60 seconds. Allowed range is 1 to 86400 seconds.
* Script Freeze Timeout: Defines how long a policy should wait for the script that is invoked in order to freeze an application, before a snapshot is taken. If the script does not complete within this timeout, the job fails. The default value is 60 seconds. Allowed range is one to 86400 seconds.
* Script Unfreeze Timeout: Defines how long a policy should wait for the script that is invoked in order to freeze an application, after a snapshot is taken. If the script does not complete within this timeout, the job fails. The default value is 60 seconds. Allowed range is one to 86400 seconds.
* Script Finish Timeout: Defines how long a policy should wait for the script that is invoked at the very end of the job. If the script does not complete within this timeout, the job fails. The default value is 60 seconds. Allowed range is one to 86400 seconds.  
  
## The VMware administrator's guide

This page is one in a series of pages specific to protecting and recovering VMware VMs with Backup and DR. You can find additional information at:

  * [Backup and DR for VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/vmware-intro)
  * [Configure Google Cloud VMware Engine for Backup and DR protection](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-vmware)
  * [Add vCenter and ESX server hosts to the appliance management console](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-vcenter-host)
  * [Discover and protect VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-vms)
  * [Apply a backup template to protect a VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-template-to-manage-a-VM)
  * [Configure Application settings for VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/configure-application-settings-for-vmware-vm)
  * [Restore a VMware VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-vm)
  * [Mount a VMware image](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-vmware-image)
  * [Clone an image of a VMware VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/clone-image-of-a-vm)
  * [Create LiveClone workflows](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/create-liveclone-workflows)
  * [Move VM management between two backup/recovery appliances](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/supported-vmware)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
