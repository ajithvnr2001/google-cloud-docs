---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/oracle-advanced-settings/
title: Configure application details and settings for Oracle databases in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:09:00.299947+00:00
---

# Configure application details and settings for Oracle databases in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/oracle-advanced-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Configure application details and settings for Oracle databases in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Use the following tabs to find the backup type you want to configure settings for.

### Database backup

Configure a database backup using the application settings shown in this table:

Setting | Input  
---|---  
**Username and Password**   
in the **Authentication** section | **1\. Backup from Primary Node**   
  
**Database Authentication** (Linux only): Oracle database authentication uses Oracle database credentials. With Oracle database authentication, you must provide database credentials to connect to the database with `sysdba` privilege, or `sysbackup` for Oracle 12c and later. Make sure the database user account has the proper role selected based on the **User role in the database** section.   
  
**OS authentication** : Not applicable - No database user account and no service name are needed. Backup and DR uses `/ as sysdba` for `SQLPLUS` and `target /` for `RMAN` to connect to the database for backup.   
  
**2\. Backup from data guard (standby) node:**   
  
**Database authentication** (Linux only): Oracle database authentication uses Oracle database credentials for backup. With Oracle database authentication, you must provide database credentials to connect to the database with `sysdba` privilege, or `sysbackup` for Oracle 12c and later. Make sure the database user account has the proper role selected based on the **User role in the database**.   
  
**OS authentication:** Database user account is required to switch the archive log on primary to capture a consistent copy of backup on data guard node. Under OS authentication, `sysdba` or `sysbackup` privilege is not required. If the user does not have the `sysdba` role, then the user needs **grant connect, alter system, select on`dba_tablespaces`**. Make sure the database user account has the **None** role selected under **User role in the database** section.   
**User role in the database** | `RMAN` backup requires the role `sysdba`, or `sysbackup` role for Oracle 12c and later. The default value is `sysdba`. Ensure that you select the right role based on the role assigned to the user account in the database. This is applicable for DB authentication only.   
  
**Data guard backup with OS authentication** : Select the role **None** for non-`sysdba` or non-`sysoper` database user account. The required privileges for non-`sysdba` or non-`sysoper` are `connect, alter system, select on dba_tablespaces` role.   
**Number of channels** | Enter the number of `RMAN` channels to configure parallelism for backup. The number of channels should be configured based on the number of cores available on the server, taking into account other database backups configured to run in parallel. The default number of channels is 2.  
**`RMAN` log location** | By default, the `RMAN` log location is `/var/act/log/rman.log`.   
  
This entry lets you change the `RMAN` log file location. Enter the full path, with `RMAN` filename.  
**Restore validate** | `RMAN RESTORE VALIDATE` will check and verify the integrity of the backups. It is used to detect any corrupted block in the database. When this box is selected, the Backup and DR agent will invoke `RMAN` restore validation for each backup. This validation is costly and will add time to the backup.  
**RMAN catalog DB name**(Optional) | This is the catalog database service name. This is for the user environment where `RMAN CATALOG DATABASE` is set up for `RMAN` backup. The catalog database service name must have an entry in the `tnsnames.ora` file for Backup and DR to connect.  
**`RMAN` catalog user and   
`RMAN` catalog password** | This is the catalog database username and password for `RMAN` to connect during the backup. This is required if `RMAN` catalog DB name is provided to run the backup connected to catalog DB.  
**Oracle service name** | Provides the ability to specify a new service name in `tnsnames.ora` file to be used by Backup and DR backup, as described in [**Create and verify the Oracle service name in a non-RAC environment**](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prepare#non-rac) and in [**Create and verify the Oracle service name in a RAC environment**](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prepare#rac).   
  
If not specified, then by default Backup and DR will use the Oracle SID name (instance name) as the service name. Either the new service name or the default SID name must have an entry in the `tnsnames.ora` file for Backup and DR to connect. The Oracle service Name is used only with database authentication.  
**Oracle data guard primary node service name** | This is the service name in the tnsnames.ora file configured on the data guard node to connect to the primary database node from the standby database node.   
  
This is required only when you are protecting data from Oracle data guard. For more information, see [**Protect from an Oracle data guard node**](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prepare#data-guard).  
**Cluster nodes** | Specify a failover node choice in format:   
`Failover choice:Node IP:servicename:role`   
This is used for RAC only, see [**Configure RAC transparent failover of Backup and DR`RMAN` backup to other nodes**](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prepare#rac-failover).   
  
Example:`1:172.16.16.21:svc_orarac2_act:F`   
  
Role should be `F` for failover. role can also be `M` for maintenance. When a node role is `M`, then the backup/recovery appliance uses this as the backup node instead of using the original protected node.  
**Maxcorrupt parameter setting** | Setting `maxcorrupt` allows a specified number of previously undetected block corruptions in datafiles during the execution of an `RMAN BACKUP` command. If `RMAN` detects more than this number of new corrupt blocks while taking the backup, then the backup job aborts.  
**Section size override** | Section size is in MB. The section size `RMAN` parameter allows the backup of large files to be parallelized across multiple `RMAN` channels.   
  
Default section size is 16000, or 16GB. Enter a new size between 1 and 200000 if you want to override the default value.  
**Do not uncatalog** | Check this box to keep `RMAN` datafile backup metadata cataloged after each backup job. By default, Backup and DR data file backup will be cataloged at the start of backup and then be uncataloged at the end of the backup.  
**Force new level zero backup** | Backup and DR `RMAN` backup is incremental forever using updated image copy where each incremental backup creates a logical full copy. If a full level zero backup is required, overwriting the Backup and DR incremental backup, then check this box for a single backup job. Be sure to clear it after the full level zero backup is complete, otherwise this will force each backup to be a new level zero Oracle `RMAN`RMAN backup. This has an impact on snapshot pool storage.  
**Oracle configuration file location** | Use this when backing up Oracle configuration files with an Oracle `RMAN` backup such as wallet for encryption support. Requires a full path.   
  
If a folder name is specified, all files under that folder are backed up. If a filename is specified then only the specified file is backed up.   
  
**Note:** For Oracle databases with TDE, the wallet for TDE can be captured by setting the Oracle configuration file location advanced setting for the Oracle application. Application aware mounts for TDE enabled databases require the wallet to be copied to the appropriate location on the mount host and the wallet must be configured and open.  
**`AU_SIZE`** | Parameter to configure ASM Diskgroup AU size, in MB, default is 1MB. This only takes effect during diskgroup creation, which is during level zero backup job. Set this before the first backup, or select Force new level 0 to recreate the disk group with new `AU_SIZE`.   
  
Be sure to have enough free space in the snapshot pool when using the new level 0 backup.  
**Auto-discover RAC members** |  Check this to autodiscover all members of the RAC databases. It enables mapping of the staging disk to all RAC nodes. Auto-discovery won't work if the hostname does not have a FQDN. In that case add the nodes manually.  
**RAC member nodes** | If you choose not to autodiscover RAC members, then provide a RAC node list for mapping the staging disk to the selected RAC member. List the protected nodes first. Use this only for protecting Oracle databases in an ASM disk group.  
  
### Archive log backup

Configure an archive log backup using these application settings:

Setting | Input  
---|---  
**Number of channels for archive log backup** | Specify the number of `RMAN` channels, or parallel log backup, to use during archivelog backup. Default `RMAN` channel is 2.  
**Oracle`TNS_Admin` path** | If `tnsnames.ora` is in a non-standard location, then provide the full path of the directory where it is located. The Oracle `TNS_Admin` path is used only with database authentication.  
**Log purging retention period** | In the space provided, enter the number of hours to retain production archive logs in the archive log destination. For example, if this is set to four, then archive logs older than four hours will be purged from the database archive destination. The default value is 24 hours.   
  
**Note** : If you set **Log purging retention period** to zero, then the log will be purged immediately after the backup job is finished. If you do this, set **Successful log backups before purge** to at least one.  
**Successful log backups before purge** | By default, archive purging does not check for the number of successful log backups. Enter a number of successful log backups after which to run the archive purge.  
**Cross-check archive log** |  Select this to run crosscheck and delete expired production archive logs on archive log backup.  
**Cross-check backup of archive log once a day** | Select this to cross check the backup of archivelog on Backup and DR Staging disk once a day during log backup after database backup. This option will override cross check during each archivelog backup if **Crosscheck backup of archivelog** is selected.  
**Cross-check backup of archive log** | Select this to cross check the backup of archivelog on Backup and DR Staging disk with each archivelog backup.  
**Number of files per backup set** | Specify the number of archive logs to include in a backupset during archivelog backup. The default value is 4.  
**Archive log backup service name** | Provide a dedicated Oracle database service name for the archive log backup in a RAC environment when Oracle service name is configured to run from more than one node. The archive log backup service name is used only with database authentication.  
  
### Backup staging disk

Configure a backup staging disk using these application settings:

Setting | Input  
---|---  
**Convert ASM format to file system format** |  By default, the database is captured in its default format, either ASM or file system. The backup destination is ASM for production Oracle database with data file on ASM disk group, and file system for Oracle database with data file on file system. Set this to **Yes** if the source database data file is on ASM disk group and the backup destination must be set to the file system staging disk.  
This must be set to **Yes** for all ASM databases in a Windows environment.  
**Convert file system format to Oracle ASM format** | By default, the database is captured in its default format, either ASM or file system. The backup destination is ASM for production Oracle database with data file on ASM disk group, and file system for Oracle database with data file on file system. Set this to **Yes** if the source database with data file on file system and the backup destination must be set to Oracle ASM disk group. This requires ASM to be installed on the Oracle server.  
**ASM disk group compatibility** | The minimum version of the ASM software that can access the disk group. Refer to **ASM disk group compatibility attribute** to specify and override the backup ASM disk group ASM compatibility. This will require a new force level 0 backup. This has an impact on snapshot pool storage.  
**Database compatibility** | The minimum compatible database initialization parameter setting for any database instance that uses the disk group. Refer **ASM Disk Group Compatibility Attribute** to specify and override the backup ASM disk group RDBMS compatibility. This will require a new force level 0 backup. This has an impact on snapshot pool storage.  
**Staging disk size** | By default, the Backup and DR agent calculates the staging disk size for database backup as 1.5 times the maximum size of the database. To specify a value manually, allocate a staging disk to allow for two years future growth of the database. Setting it manually will restrict the dynamic growth of staging disk with growth of database size.  
**Staging disk granularity** | Maximum size of each disk when multiple disks are used in a backup staging disk for an application. The default value is 1000GB.  
**Use staging disk granularity as minimum staging disk size** | Use this for applications that are under the size of the granularity setting (default value is 1000GB) and that tend to periodically grow. This option is useful to avoid frequent costly full backups. Because the staging disk is thin provisioned, there is no initial cost to use a staging disk that is larger than required for immediate use.  
**Last staging disk minimum size** | Minimum size of the last disk when multiple disks are used in a backup staging disk for an application.This value is also used for additional disks allocated for backup staging disk to accommodate growth. The default value is 250GB.  
**Staging disk mount point** | Allows you mount the staging disk to a specific location.  
**Log staging disk size** | Used if log backup policy is set. By default, Backup and DR uses the 30-day high-water mark to determine the staging disk size for archive backup staging disk.   
Note: You can create a log backup staging disk with a size greater than the system granularity default of 1TB, but if you do then the automatic log staging size updating will be disabled. To re-enable it, wait for a successful log backup, and then reset the log staging disk size value to the default value. When automatic log staging size updating is enabled, the staging disk won't resize automatically when the calculated size is less than 1TB; when the calculated size is greater than 1TB, new disk will be added to the log backup volume to grow it.   
  
## Policy template overrides for Oracle databases

  1. Go to **App manager** and click **Applications**.

  2. Right-click a database and select **Manage backup plan**.

  3. At the top of the page, click **Policy overrides**.

  4. In the policy overrides fields, enter the required input. For details on log protection, refer to [Database log protection in a backup plan policy](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan-policy-best-practices#Log-protection)




## The Oracle DBA guide

  * [Backup and DR for Oracle databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/oracle-intro)
  * [Prerequisites for protecting an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prerequisites)
  * [Oracle patches and known issues](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/oracle-patches-known-issues)
  * [Prepare Oracle databases for protection](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prepare)
  * [Discover and protect an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-oracle)
  * [Details and settings for Oracle databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/oracle-advanced-settings)
  * [Use dNFS with Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-dnfs)
  * [Protect a discovered Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/oracle-db-protect)
  * [Mount an Oracle database as a standard mount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount)
  * [Create an instant virtual copy of an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount-virtualdb)
  * [Restore and recover an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-oracle)
  * [Instant recovery of an Oracle database using Mount and Migrate](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/oracle-mm)
  * [Provision an environment with a Backup and DR workflow](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/create-workflow-oracle)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
