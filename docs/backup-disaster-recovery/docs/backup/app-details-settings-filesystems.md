---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-filesystems/
title: Configure application details and settings for file systems in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:36.559817+00:00
---

# Configure application details and settings for file systems in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-filesystems/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Configure application details and settings for file systems in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

From the appliance management console **Application Details & Settings** page—accessed from the **Details & Settings** link at the top of each application's backup plan—you can modify application-specific settings for backing up a file system. Application settings may be useful or required in certain circumstances. After you configure your application settings, click **Save Changes**.

**Note:** To reset one or more application settings back to its default state, click the checkbox to the left of the selection you want to reset, or click **Select options that will revert back to default** to reset all application selections back to their default state.

The following is a list of the application settings and a description of what they do.

  * **Username/Password** : If alternate credentials were specified when the network drive was mapped to the host, in the spaces provided, enter the file share username and password.
  * **Staging Disk Size (GB)** : Enter a value in gigabytes. Valid entries are one to 256000. By default, the Backup and DR agent uses the size of the managed file system as the size of the staging disk. This setting allows the administrator to override this value to allow for growth of the file system.

  * **Use Staging Disk Granularity as Minimum Staging Disk Size** : The default value is zero when you select **No**. If you select **Yes** , then you must enter a value in GB in the **Staging disk granularity** field. This setting is for applications that are less than the size of the granularity setting and tend to grow periodically. This setting helps avoid frequent and costly full backups. There is no initial cost to using a staging disk that is larger than required for immediate use because the staging disk is thin-provisioned.

  * **Staging Disk Granularity (GB)** : Defines the granularity of the staging disk created for an out-of-band application. It specifies the size of each staging disk when multiple staging disks are used for an application. Valid entries are one to 128000. For example, the following:

    * If an application is 4.3TB, and the **Stage Disk Granularity** value is 2TB and **Last Staging Disk Minimum Size** value is 1TB, the backup/recovery appliance creates three staging disks of 2T, 2T, and 1T.
    * If an application is 4.3TB, and the **Stage Disk Granularity** value is 2TB and **Last Staging Disk Minimum Size** value is 0.1TB, the backup/recovery appliance three staging disks of 2T, 2T, and 0.3T.
    * If an application is 4.3TB, and the **Stage Disk Granularity** value is 5TB and **Last Staging Disk Minimum Size** value is 1TB, the backup/recovery appliance creates one staging disk of 4.3T. **Stage Disk Granularity** and **Last Staging Disk Minimum Size** are specified at the application level and override the system-wide default values.
  * **Staging Disk Mount Point** : Enter a **Staging Disk Mount Point** if you need the staging disk mounted to a particular location.

  * **Exclude Patterns, Include Patterns** : Enter the filename pattern to be excluded from or included in backup. The backup/recovery appliance offers the ability to exclude or include certain file types. Using either the **Exclude Patterns** or **Include Patterns** option, only the most crucial data is backed-up leaving a side the non-critical files. The guidelines include the following:

    * Only files are excluded or included, this does not impact directories.
    * A pattern can include wildcard characters, for example, an asterisk (*) or a question mark (?). To exclude all the files that contains `.sys` as extension, enter `*.sys` in the **Exclude Pattern** or **Include Pattern** field.
    * On Windows, files named `pagefile.sys` and `hiberfil.sys` that appear in the root directory of a drive are automatically ignored.
  * **Start Paths** : Specifies the point in the file share where backup starts. If the **Start Path** field is left blank, backup starts at the root directory of the file system to be backed-up. 

Linux example: `/usr/local` backs up the `/usr/local` directory.

Windows example: `\\SERVERNAME\SHARENAME\abc` backs up the abc directory on the file share.

  * **Prune Paths** : Provide the prune paths in the **Prune Paths** field. Prune path specifies a point in the file system where directory traversals stop.

Linux example: `/usr/local/lib` ensures that nothing following `/usr/local/lib` is copied, but all other directories and files in `/usr/local` are copied. 

Windows example: `\\SERVERNAME\SHARENAME\abc` ensures that nothing following `\\SERVERNAME\SHARENAME\abc` is copied, but all other directories and files in `\\SERVERNAME\SHARENAME` are copied. 

If this field is left blank, the directory traversal descends into every subdirectory of the start paths being backed up.

  * **Service Access Point IP Address** : If a file system is a cluster resource and if you want it to be backed up irrespective of which cluster node is hosting the file system, then specify the cluster resource IP as a service access point IP. This allows the backup/recovery appliance to connect to the Backup and DR agent using the cluster resource IP and to back up the file system from the active cluster node. For backup to work correctly across all cluster nodes, the Backup and DR agent must be installed on all cluster nodes. Enter a virtual IP address for a clustered application. For failover clusters, this is used to find the active node for a backup. For active/active clusters, this is a comma separated list of eligible servers that can be used for the backup.

  * **Use Service IP for Restore** : Honor the service access point IP address during restore for a clustered application. Select **Yes** if you want to use the service IP address for restoring a cluster application. Select **No** if you do not want to use the service IP address to restore.

  * **Backup and DR Agent Options** : Leave Backup and DR agent options blank unless you are working with support.

  * **Prefer LVM for Single Staging Disk** : Create an LVM even when a single staging disk is enough for backup. Select **Yes** if you want to use an LVM-based staging disk that can be expanded without requiring a new full backup, regardless of the size of the Linux source disk. Select **No** if you do not want to use an expanded LVM-based staging disk.




## Backup and DR for Filestore and file systems

This page is one in a series of pages specific to protecting and recovering filesystems with Backup and DR. You can find additional information in the following pages:

  * [Backup and DR for file systems](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-filesystems)
  * [Manage hosts and their connected applications](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-hosts-and-their-connected-applications)
  * [Configure application details and settings to protect file system data](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/configure-app-settings-for-filesystems)
  * [Apply a backup plan to protect a file system](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-plan-to-filesystem)
  * [Restore a file system to the source](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/filesystem-restore)
  * [Mount a file system or file share](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-file-system)
  * [Mount and migrate a file system for instant recovery to any target](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/filesystem-mount-and-migrate)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
