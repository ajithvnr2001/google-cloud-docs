---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-oracle-virtualdb/
title: Mount an Oracle backup as a virtual database in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:19.136824+00:00
---

# Mount an Oracle backup as a virtual database in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-oracle-virtualdb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Mount an Oracle backup as a virtual database in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

## Before you begin

For Oracle databases with Transparent Data Encryption (TDE), the wallet for TDE can be captured by setting the Oracle [configuration file location](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-oracle) advanced setting for the Oracle application. Application aware mounts for TDE enabled databases require the wallet to be copied to the appropriate location on the mount host and the wallet must be configured and open. To set autologin, use this code:

`orapki wallet create -wallet <wallet_path> -auto_login -pwd <wallet_password>`

## Mount an Oracle database as a virtual application

To mount an Oracle database as a virtual application, follow these steps:

  1. From the Backup and DR appliance management console, click **App Manager** > **Applications** and enter the database application name or use the filters to make it easier to get to the database image that you need.

  2. Right-click the application and select **Access**.

  3. On the **Access** page, select the required image and click **Mount** under the **Mount** menu.

  4. Under **Application Options** enable **Create New Virtual Application**.

  5. Fill in the form as needed for this virtual application. Fields marked with an asterisk (`*`) are required. You can click each entry for additional helpful information.

**Application Options**

     * If the source application is protected by a snapshot policy that has enabled database log backups, and logs are available with the image, you can use them to roll forward to a specific point in time by changing these options in the **Roll Forward Time** section:

       * The date field contains all possible dates that the database can be rolled forward to—through the application of database transaction logs. Select which date you want the database to roll forward to.
       * The time field contains a slider showing all possible times on the selected date that the database can roll forward to. If you select the latest possible date and then move the slider to the right most position, the job applies to all available logs. If you select the earliest possible date and move the slider to the left most position, the job applies no logs.
       * You can specify to roll forward using either **User Time** or **Host Time**. **User Time** is relative to the local time of the current user. Host time is relative to the system that hosts the data to be mounted.
     * **Target Database SID** : Specify the SID for the new Oracle database to be provisioned on the target. Follow standard Oracle naming conventions for this value. Make sure that the target host database version matches the version of the source host, and that there are enough resources on the target database server. Follow standard Oracle naming conventions for this value.

**Note:** You cannot mount an Oracle virtual database with logs back to the source. This prevents overwriting the data file in the source database when a newly added datafile is captured in the log backup.
     * **User Name** : Specify **Oracle Operating System** user credentials on the target.

     * **Oracle Home Directory** : Specify the **Oracle Home Directory** ($ORACLE_HOME) on the target database server.

**Note:** (Windows only) A user who runs an application aware mount must be the administrator user who owns the ORACLE_HOME, or else has READ/WRITE privileges on mount locations used during the application aware mount. Otherwise a call to oradim will prompt for password and become stuck.
     * The application aware mount is a new database. If you want to protect the new database, then enable **Manage New Application** to apply a backup plan to the new database. New **Template** and **Profile** fields appears where you can select any of your existing backup templates and resource profiles. The snapshots of the database are incremental.
**Note:** There is one exception: if the target server is a VMware VM, you must select **pRDM** for the mount if you want the child database to have the efficient incremental snapshots. If you forget and leave the default of **vRDM** , then the first snapshot job is a full backup.

**Advanced Options**

     * **TNS Admin Directory path** : Specify TNS_ADMIN Directory path—path of tnsnames.ora file—on the target database server.

     * **Database Memory Size in MB** : Database total memory size, in MB, for the database being provisioned on the target. See the following table for the expected behavior depending on how this and SGA%—next—are set.

     * **SGA%** : Parameter to configure SGA/PGA memory, as a percentage of total memory, for the database being provisioned. See the following table for the expected behavior depending on how this and **Database Memory Size in MB** are set.

Database Memory Size in MB | SGA% | Behavior  
---|---|---  
not specified | N/A | Total database memory size and memory parameter on target is the same as source database.  
specified | not specified | MEMORY_TARGET parameter is set for the database being provisioned on the target.  
specified | specified | Set SGA and PGA for the database provisioned on the target to:  
SGA_TARGET = **Database Memory Size in MB** x (**SGA%** /100) PGA_TARGET = **Database Memory Size in MB** x (100-(**SGA%** /100))  
Note: Don't set SGA to 100. To avoid database slowness, reserve some memory for PGA.  
     * **REDO Size** : Parameter to configure REDO size, in MB, for the database being provisioned. If not specified, REDO size is set to 1000 MB.

     * **Shared_Pool_Size in MB** : Parameter to configure shared pool size, in MB, for the database being provisioned. If not specified, shared_pool_size is not used.

     * **DB_Cache_Size in MB** : Parameter to configure database cache size, in MB, for the database being provisioned. If not specified, db_cache_size is not used.

     * **DB_Recovery_File_Dest_Size in MB** : Parameter to configure database recovery file destination size, in MB, for the database being provisioned. If not specified, db_recovery_file_dest_size is set to 50000 MB.

     * **inmemory_size** : Parameter to configure database inmemory_size, in MB, for the database being provisioned. The minimum size can be set is 100MB. If not specified, inmemory_size parameter is skipped regardless of Oracle version.

     * **Diagnostic_Dest** : Parameter to configure diagnostic destination on the host. If not specified, diagnostic_dest is set to ORACLE_HOME.

**Note:** Diagnostic_Dest is not supported for Oracle 10g. Simply leave it blank.
     * **Max number of processes** : Parameter to configure max number of system user processes that can simultaneously connect to Oracle, for the database being provisioned. If not specified, processes is set to 500.

     * **Max number of open cursors** : Parameter to configure maximum number of open cursors that a session can have at once, for the database being provisioned. If not specified, number of open cursors is using source database settings.

     * **TNS Listener IP** : Specify IP address for the TNS Listener. It can be one of SCAN IP, VIP, or Host IP. If not specified, Host IP is used.

     * **TNS Listener port** : TNS Listener port to be used to create service name under tnsnames.ora for provisioned database on target. If not specified, port 1521 is used.

     * **TNS Domain Name** : Specify domain name to be used with service name under tnsnames.ora for provisioned database on target. This is needed when database service is using **Domain Name**.

     * **PDB Prefix** : Specify a prefix for renaming PDB during child database creation.

     * **User to be removed** : This is a comma-separated list of users that to be removed as part of the mount operation.

     * **Do not change database DBID** : If selected, the new database's DBID is not be changed.

     * **No Archive Mode** : If selected, new database is running in no-archivelog mode. Reprotection of the new instance is not available.

     * **Clear Archivelog** : If selected, clear archivelogs after masking is performed.

     * **Do not update tnsnames.ora** : If selected, an entry for the new database is not be added to tnsnames.ora. This may require manual intervention for connections to the new database, and in some cases snapshot jobs for the new database fails without this manual intervention.

     * **Do not update oratab:** If selected, an entry for the new database is not be added to oratab if one exists.

     * **Add TNS Listener Entry** : the default is false. If this option is enabled, a listener entry is added to the tnsnames.ora file.

     * **Number of Channels** : The number of RMAN channels.

     * **Clear OS_Authent_Prefix** : OS_Authent_Prefix is a prefix that Oracle uses to authenticate users connecting to the server. Oracle concatenates the value of this parameter to the beginning of the user's operating system account name and password.

     * **Restore with Recovery** : If selected, brings the newly created database online: the provisioned database on target is open for read and write. This is the default selection.

     * **Stand Alone Non-RAC** : This is only applicable for databases where the source database is in a non-RAC configuration and Backup and DR stores the copy in ASM format. If selected, this performs an application aware mount to a standalone ASM non-RAC instance. Don't select this option if a RAC node list has been provided.

**Note:** To create a virtual application (application-aware mount) as a RAC database, specify the IP address of all nodes for the target RAC cluster separated by a colon (:) in the order of RAC nodes 1... n. The first IP address in the RAC Node list must be the selected host's IP addressin the ASM details.
     * **Use existing Oracle password file** : If this option is selected, a virtual database mount uses the existing Oracle password file and does not delete it during cleanup on unmount

     * **Environment variable** : If you have any user-defined environment variables to be passed to pre- and post-scripts, you can enter one here.

  6. Click **Submit** to submit the job. You can go to the **Job Monitor** to view the progress and details of the job. The mounted image is available in the Active Mounts.




## Management of the active mounts

Once you have created a mount, you can track the image from the **App Manager** > **Active Mounts**. Ideally, don't leave any image mounted indefinitely. This is because the backup image that the mount was created from cannot expire until all its mounts have been deleted. When you have finished using the mounted image then either:

  * [Unmount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount) the image. You can [remount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#remount) it if needed. You can then [delete](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#delete) the image later when you are certain it is no longer needed.
  * [Unmount and delete](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount-delete) the image. This deletes the mounted image, not the backup that the mount is based on.



## Bringing Backup and DR protected ASM diskgroups back online after reboot of a target DB server

After any database server reboot where Backup and DR copy is mounted, or Backup and DR backups are in progress for the database at the time of reboot/crash, follow these steps to get the Backup and DR disk group mount back:

  1. Check that the target database server is back up, and that ASM and RAC system are also up.

  2. Restart the Backup and DR agent (from root).

  3. Set ASM environment.

  4. Log into ASM sqlplus and check the disk group status:
         
         `select name, state from v$asm_diskgroup where (name = '<dg name>';)`
         

  5. If unmounted, mount the disk group: `alter diskgroup <dg name> mount;`

  6. Login to the Oracle OS and set the database environment, then start the database.




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

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
