---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-otherdb/
title: Mount other types of databases and instances in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:45:04.797401+00:00
---

# Mount other types of databases and instances in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-otherdb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Mount other types of databases and instances in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page describes how to make standard and virtual database—application aware mounts of the other types of databases in the appliance management console.

You can access databases in several ways as well:

  * [Restore to the source](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/otherdb-restore)
  * [Recover to a new target (SAP MaxDB and SAP IQ only)](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/otherdb-recover-iq-max-volume-to-new)
  * [LiveClone](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/liveclone)
  * [Backup and DR Workflow](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/otherdb-workflow)
  * [Mount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/otherdb-mounts)



## Making a standard mount for other database types

This is the procedure for a standard mount. To make a virtual database—application aware mount—see the procedure in Mount a virtual database from a volume-level backup image.

Use these instructions to mount the database image as a standard mount:

  1. From the Backup and DR appliance management console, open the **App Manager** > **Applications** list.
  2. Right-click the protected database and select **Access**.

**Note:** You can use the **Managed Backup Plan** status filter to show only protected databases.
  3. Select a snapshot image and choose **Mount**.

  4. On the **Mount** page, from **Target** , choose the target database server from the drop-down.

  5. In **Label** , optionally enter a unique name associated with the mount.

  6. Under **Application Options** , disable **Create New Virtual Application**.

**Note:** If you don't see the **Create New Virtual Application** option, then the image is from a file-based Full+Incremental snapshot, so a virtual database is not possible.
  7. Under **Mapping Options** , do the following:

     * If required, change the default **Storage pool** to be used for the mount from the drop-down list. This only applies to mounts where there is no existing staging disk, such as direct to OnVault and imported OnVault images, otherwise the pool where the source image disks are located can always be used regardless of what is set here.
     * Enter the **Mount Location**.
  8. In the **Pre-Script** and **Post-Script** fields, enter the path and relative file names. Enter the timeout values to prevent hanging. 300 seconds is a good default timeout value.

  9. Click **Submit**. You can go to the **Job Monitor** to view the progress and details of the job. The mounted image is available in the Active Mounts.




## Mount a virtual database from a volume-level backup image

Only volume-based snapshots can be mounted as virtual databases. Snapshots taken using Full+Incremental are file based; these cannot be mounted as virtual databases.

**Note:** For PostgreSQL database applications, the target host's SELinux mode should set to Permissive or disabled. Otherwise, the mount job may fail. The command to set the SELinux mode to permissive is `setenforce 0`.

To mount the database image as a virtual application—an application aware mount—to a new target:

  1. From the Backup and DR appliance management console, open the **App Manager** > **Applications** list.
  2. Right-click the protected database and select **Access**. You can use the **Managed Backup Plan** status filter to show only protected databases.
  3. Select a backup image and choose **Mount**.
  4. Keep **Host or VM** selected; containers are not supported for databases.
  5. On the **Mount** page, from **Target** , choose the target database server from the drop-down.

**Note:** (Db2 only) Be sure that the target instance doesn't have any databases with the same name as any of the source databases or the new target database name selected for the source databases during mount.
  6. In **Label** , optionally enter a unique name associated with the mount.

  7. Under **Application Options** , enable **Create New Virtual Application**.

  8. At **Included Databases** , **Select Items** , choose one or more databases to virtualize, and click **Database Options** for each selected database to specify a target database name for the new virtual copy.

     * A single database are managed as standalone virtual copy.
     * Multiple databases are managed as a consistency group.
**Note:** Not applicable for SAP IQ and MaxDB databases.
  9. If the source application is protected by a backup policy that has enabled database log backups, and logs are available with the image, you can use them to roll forward to a specific point in time by changing these options in the **Roll Forward Time** section:

     * The date field contains all possible dates that the database can be rolled forward to (through the application of database transaction logs). Select which date you want the database to be rolled forward to.
     * The time field contains a slider showing all possible times on the selected date that the database can be rolled forward to. If you select the latest possible date and then move the slider to the right most position, the job will apply to all available logs. If you select the earliest possible date and move the slider to the left most position, the job will apply no logs.
     * You can specify to roll forward using either **User Time** or **Host Time**. User Time is relative to the local time of the current user. Host time is relative to the system that hosts the data to be mounted.
  10. **NAME OF CONSISTENCY GROUP.** This option will appear if more than one database is selected. Provide a unique name to manage the selected databases as a virtual copy.

  11. Each database type has application settings:

### IBM Db2

     * TARGET INSTANCE NAME. From the drop-down, select a target Db2 instance to attach the selected database as a virtual copy.

### PostgreSQL

     * PostgreSQL Target Server Port. Enter an unused port number on the target server where the new PostgreSQL instance will be created for the new child databases.
     * PostgreSQL Target OS User Name. Enter the name of the operating system user on the target server where the new PostgreSQL instance will be created.
     * PostgreSQL Target Server Home Directory. Enter the path to the base directory where the configuration files for PostgreSQL instance on the target server are stored.

### SAP ASE

     * TARGET SAP ASE USER
     * TARGET SAP ASE PASSWORD
     * TARGET SAP ASE INSTANCE NAME. From the drop-down, select a target SAP ASE instance to attach the selected database as a virtual copy.

### SAP IQ

     * TARGET DATABASE NAME. The name of the target SAP IQ database
     * SAP IQ TARGET OS USER NAME. OS user for target SAP IQ database
     * SAP IQ TARGET DB USER NAME. dbm user for target SAP IQ
     * SAP IQ TARGET DB PASSWORD. dbm user password for target SAP IQ
     * SAP IQ HOME DIRECTORY. Specify the directory path of SAP IQ binaries

### SAP MaxDB

     * TARGET DATABASE NAME. The name of the target MaxDB database
     * MAXDB TARGET OS USER NAME. OS user for target MaxDB instance
     * MAXDB TARGET DB USER NAME. dbm user for target MaxDB
     * MAXDB TARGET DB PASSWORD. dbm user password for target MaxDB

  12. If you want to apply a backup plan to the new virtual database, then enable **Manage New Application** and select a template and a profile.

  13. In Advanced Options, you can enter the Home Directory of the database, and for Overwrite Existing Database, 

These database instances have additional advanced options:

### IBM Db2

     * TARGET NODE NUMBER
     * OVERWRITE EXISTING DATABASE. indicate when to overwrite a database on the target server that has the same name as the new database(s) being mounted: Yes, No, or Only if it's Stale.

### PostgreSQL

     * POSTGRESQL TARGET DB USER NAME and POSTGRESQL TARGET DB PASSWORD. (Optional) Enter new credentials for the target PostgreSQL instance that will be created. If you don't specify anything, empty database credentials will be used. By default, a password is not required to sign in from the local system. For the Directory Path, enter the path to the messages directory for the PostgreSQL instance on the target server.
     * TAKE OVER IN-USE PORT

### SAP ASE

     * OVERWRITE EXISTING DATABASE. indicate when to overwrite a database on the target server that has the same name as the new database(s) being mounted: Yes, No, or Only if it's Stale.

### SAP IQ

     * OVERWRITE EXISTING DATABASE. indicate when to overwrite a database on the target server that has the same name as the new database(s) being mounted: Yes, No, or Only if it's Stale.

### SAP MaxDB

     * MAXDB HOME DIRECTORY
     * OVERWRITE EXISTING DATABASE. indicate when to overwrite a database on the target server that has the same name as the new database(s) being mounted: Yes, No, or Only if it's Stale.

  14. Complete the following under **Mapping Options** :

     * If required, change the default **Storage pool** to be used for the mount from the drop-down list. This only applies to mounts where there is no existing staging disk, such as Direct to OnVault and imported OnVault images, otherwise the pool where the source image disks are located will always be used regardless of what is set here.
     * **Mount Location.** specify a target mount point to mount the new virtual database to.
  15. In the **Pre-Script** and **Post-Script** fields, enter the path and relative filenames. Enter the timeout values to prevent hanging. 300 seconds is a good default timeout value.

  16. Click **Submit**. You can go to the **Monitor** to view the progress and details of the job. The mounted image is available in the Active Mounts.




## Management of the active mounts

Once you have created a mount, you can track the image from the **App Manager** > **Active Mounts**. Ideally, don't leave any image mounted indefinitely because the backup image that the mount was created from cannot expire until all its mounts have been deleted. When you have finished using the mounted image then either:

  * [Unmount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount) the image. You can [remount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#remount) it if needed. You can then [delete](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#delete) the image later when you are certain it is no longer needed.
  * [Unmount and delete](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount-delete) the image. This deletes the mounted image, not the backup that the mount is based on.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
