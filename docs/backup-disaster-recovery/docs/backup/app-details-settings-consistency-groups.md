---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-consistency-groups/
title: Configure application details and settings for consistency groups in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:40.350589+00:00
---

# Configure application details and settings for consistency groups in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-consistency-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Configure application details and settings for consistency groups in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

From the **Application Details & Settings** page—accessed through **Details & Settings**—you can modify application-specific settings when managing a consistency group data capture. Application settings may be useful or required in certain circumstances. After you configure your application settings, click **Save Changes**.

**Note:** To reset one or more application settings back to its default state, click the checkbox to the left of the selection you want to reset, or click **Select options that will revert back to default** to reset all application selections back to their default state.

The following is a list of the application settings with descriptions of what they do.

  * **Username/Password (SQL Service, SMB)** : For a SQL Server. User credentials for backing up the database transaction log. This account must have backup privileges. Credentials are required only if you select **Backup Transaction Log** or **Truncate Log** and if **Local System** does not have permissions to the SQL database. SMB: User credentials for authenticating to the SMB share.
  * **User Role in the Database (Oracle Only)** : Database user account for Backup and DR RMAN backup. This setting is required. By default, the **User Role** in the **Database** setting uses the sysdba role. For the 12c—or later—sysbackup role, select the sysbackup role. The following are roles options:

    * Role sysdba
    * Role sysbackup, applicable to 12c
  * **Number of Channels (Oracle Only)** : Allows user to configure RMAN channels based on specifics of the host computing power. Number of channels should be configured based on # of cores available on the server taking into account of other database backup configured to run in parallel. Valid entries are one to 255.

  * **Staging Disk Size (GB) (Oracle, local file systems, SMB, NFS, SQL Server)** : Enter the staging disk size in the **Staging Disk Size** (GB) field. The Backup and DR agent calculates the maximum size of the application as configured. The **Staging Disk Size** option lets you allocate a staging disk to hold backup and to allow future growth of the database.

  * **Staging Disk Granularity (GB) (local file systems, SMB, NFS, SQL Server)** : Defines the granularity of the staging disk created for an application. It specifies the size of each staging disk when multiple staging disks are used for an application. Valid entries are one to 128000, for example:

    * If an application is 4.3TB, and the **Stage Disk Granularity** value is 2TB and **Last Staging Disk Minimum Size** value is 1TB, the backup/recovery appliance creates three staging disks of the 2T, 2T, and 1T.
    * If an application is 4.3TB, and the **Stage Disk Granularity** value is 2TB and **Last Staging Disk Minimum Size** value is 0.1TB, the backup/recovery appliance creates three staging disks of 2T, 2T, and 0.3T.
    * If an application is 4.3TB, and the **Stage Disk Granularity** value is 5TB and **Last Staging Disk Minimum Size** value is 1TB, the backup/recovery appliance creates one staging disk of 4.3T. **Stage Disk Granularity** and **Last Staging Disk Minimum Size** are specified at the application-level.
  * **Last Staging Disk Minimum Size (GB) (local file systems, SMB, NFS)** :




The size of the last fragment when there is more than one staging disks created for an application. Valid entries are one to 128000. This application setting is used in conjunction with **Stage Disk Granularity** , and both application settings are specified at the application level.

  * **Staging Disk Mount Point (Oracle, local file systems, SMB, NFS)** : Enter a **Staging Disk Mount Point** if you need the staging disk mounted to a particular location.
  * **Oracle Named Listener (Oracle only)** : For more than one listener running on the database server specify the listener name here.
  * **RMAN Log Location (Oracle only)** : By default the rman log location is `/act/log/rman<db name>.log`. This provides user the flexibility to change the rman log file location.(full path, with rman file name). Enter the RMAN log path in the RMAN Log Location field. This is the custom location—full path along with RMAN file name—where RMAN writes the logs while taking the backup. (Oracle only)

    * For Linux, the default log location is `/act/log/<sid>_rman.log.` If you change the path, the value must be in the form `/act/log/test/custom_rman.log`.
    * For Windows, the default log location is `c:\act_tmp\log\<sid>_rman.log`. If you change the path, be sure there are no spaces in the path.
  * **Restore Validate (Oracle only)** : Choose to validate each backup before restoring it. RMAN provides **Restore Validate** for the backups. When this option is checked the Backup and DR agent invokes RMAN restore validate command for each backup.


**Note:** This is a resource-intensive operation.

  * **RMAN Catalog DB Name (Oracle only)** : Optionally, this is the **Catalog** database SID name. This is for the user environment where RMAN CATALOG DATABASE is set up for RMAN backup.
  * **RMAN Catalog User (Oracle only)** : Catalog database username for RMAN backup.
  * **RAN Catalog Password (Oracle only).** Catalog database user login password.
  * **Oracle Servicename (Oracle only)** : Provides the ability to specify a new service name in `tnsnames.ora` file to be used by Backup and DR backup. If not specified then by default Backup and DR uses Oracle sid name—instance name—as the service name. Either new service name or default sid name must have an entry in `tnsnames.ora` file for Backup and DR to connect. In case of Oracle RAC a dedicated service on each node are required to be set up.
  * **Cluster Nodes (Oracle only)** : Specifies the failover node choice in the format failover `choice:Node IP:servicename:role` as detailed in. This is for RAC only.
  * **SQL Database Backup Path (SQL Server only)** : Defines a location for a temporary SQL backup. If the Backup and DR agent takes a full backup of the SQL Server database, the backup is saved in this directory. Ensure that there is enough free space n the volume hosting this directory to hold a full database backup.
  * **Service Access Point IP Address (SQL Server only)** : The **Service Access Point** is relevant only for SQL Server availability groups. Enter a value here to back up from a SQL availability appliance. Specify the IP address of the appliance node you want the database to be backed up from. This option is not required if you want the database to be backed up from the active node and it is not required for a failover appliance.
  * **Backup and DR agent options** : Leave Backup and DR agent options blank unless you are working with support.
  * **Log Purging Retention Period** : Enter the number of hours to retain archive logs in the primary log destination. For example, if this is set to four, then archive logs older than four hours are purged from the database primary archive destination. Valid entries are one to 720. The default value is 24 hours.
  * **Successful Log Backups Before Purge (Oracle Only)** : Enter the required number of successful log backups needed before logs are pruned.
  * **MAXCORRUPT Parameter Setting (Oracle Only)** : Enter the maximum number of allowable corruptions before failing the capture operation.
  * **AU Size (Oracle Only)** : Allocation Unit (AU) size of ASM disk group. Default is 4 MB. This is used for the first backup under ASM disk group only. Options include 1, 2, 3, 4, 8, 16, 32, and 64 MB.
  * **Log Staging Disk Size (GB) (Oracle only)** : Applies when the log backup policy is set. Valid entries are one to 4000. By default, the appliance management console performs a 30-day average to determine the staging disk size for archive backup staging disk. Specify the **Log Staging Disk Size** to hold 24 hours of log backup—+20% overhead.
  * **Do Not Uncatalog (Oracle only)** : To keep RMAN backup cataloged after each backup. By default Backup and DR backup is uncataloged at the end of the backup and is cataloged at the start of backup. Options are **Yes** or **No**.
  * **Force New Level0 Backup (Oracle only)** : Forces start a new level0 Oracle RMAN backup. If for any reason a full level0 backup is required, to overwrite the Backup and DR incremental backup, then select this option for a single backup job. Be sure to clear it after the full level0 backup is complete, or else this forces each backup to be a new level0 Oracle RMAN backup. This has impact on snapshot pool storage.
  * **Crosscheck Archivelog** : By default crosscheck does not run with archive backup. Select this option to run crosscheck and delete expired archivelogs with each archive backup.
  * **Crosscheck backup of Archivelog** : Select this option to run crosscheck on the current backed up archivelog before the new logs are backed up, and delete expired archivelogs.
  * **Oracle Configuration File Location (Oracle only)** : To backup any Oracle configuration files such as a wallet for encryption support, this needs a full path. If the folder name is specified, then all files under that folder are backed up. If a filename is specified, then only the specified file are backed up.
  * **Oracle TND_Admin Path (Oracle only)** : Specifies the Oracle TNS administrator path as part of the Oracle environment—for example, `TNS_ADMIN=$GRID_HOME/network/admin`. The `tns_admin` parameter determines the location of the TND administration files—for example, `tnsnames.ora` and `listener.ora`.
  * **Convert FileSystem Format to Oracle ASM Format (Oracle Only)** : By default, the database is captured in its default format, either ASM or file system. The backup destination is ASM to ASM and non-ASM to file system. Select **Yes** if the source database is under file system and backup destination must be set to Oracle ASM. This requires ASM to be installed on the Oracle server. You also have the option to use **Convert ASM Format** to **Filesystem Format**. Select **Yes** if the source database is ASM and backup destination must be set to file system.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
