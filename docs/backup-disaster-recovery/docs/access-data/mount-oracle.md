---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-oracle/
title: Mount an Oracle backup as a standard mount in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:38.657458+00:00
---

# Mount an Oracle backup as a standard mount in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-oracle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Mount an Oracle backup as a standard mount in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

You can mount a backup of an Oracle database as a standard mount or as a virtual database—application aware mount.

This is the procedure for a standard mount. To make a virtual database—application aware mount—see the procedure in [Mount an Oracle database as a virtual database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount-virtualdb).

**Note:** OnVault pools pointing to backup vaults don't support mount operations.

## Mount an Oracle database image protected under an ASM disk group for data access

Use these instructions to mount an Oracle database image for data access:

  1. Open the appliance management console to the **App Manager** > **Applications** and enter the database application name or use the filters to make it easier to get to the database image that you need.

  2. Right-click the application and select **Access**.

  3. On the **Access** page, select the image and click **Mount** under the **Mount** menu.

  4. On the **Mount** page, fill in the required information.

     * Under **Target** , select a host to mount the new database on, and provide a **Label** as needed. This is optional.

     * Under **Application Options** , clear **Create New Virtual Application**.

If you want to create an application aware mount, see [Mount an Oracle database as a virtual database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount-virtualdb).

     * Open the **Mapping Options** by clicking on the arrow icon to the left of the title.

     * If required, change the default **Storage pool** to be used for the mount from the drop-down list. This only applies to mounts where there is no existing staging disk, such as direct to OnVault and imported OnVault images, otherwise the pool where the source image disks are located is always used regardless of what is set here.

     * **MOUNT LOCATION** : Enter the mount path where to mount the log backup image.

       * If logs are Backup and DR protected, then the logs image is mounted to `<mountpath>_archivelog_Log`, and subsequent logs images to `<mountpath>_archivelog_Log1`, or `<mountpath>_archivelog_Log2`.
       * If no mount path is specified, the Oracle database backup image and the log backup image are mounted to a default generated path `/act/mnt/(jobid)_mountpoint_<random generated number>`
     * **DISK GROUP NAME**

       * Enter a diskgroup name where to mount the database backup image under ASM. The Oracle database image is mounted to ASM with a disk group name specified under **Disk Group Name**.
     * **RAC NODE LIST** :

       * If empty, the backup image is mounted to the selected host's IP address.
       * To provision a RAC database on the target RAC cluster, specify the IP address of all nodes for the target RAC cluster separated by a colon (:).
**Note:** To create a virtual application (application-aware mount) as a RAC database, specify the IP address of all nodes for the target RAC cluster separated by a colon (:) in the order of RAC nodes. The first IP address in the RAC Node list must be the selected host's IP address in the ASM details.**Note:** The 'Maximum performance' option is only supported for OnVault backup images.
  5. Click **Submit**. You can go to the **Job Monitor** to view the progress and details of the job. The mounted image is available in the Active Mounts.




## Mount an Oracle database image protected under a file system for data access

Use these instructions to mount an Oracle database image for data access:

  1. From the Backup and DR appliance management console, click **App Manager** > **Applications** to open the **Applications** page, then enter the database application name or use the filters to find the database image that you need.

  2. Right-click the application and select **Access**.

  3. On the **Access** page, select the image and click **Mount** under the **Mount** menu.

  4. On the **Mount** page, fill in the required information.

     * Under **Target** , select the host for the newly mounted database. The requested information changes depending on what type of host was selected.

     * Optionally, provide a label as needed.

     * Deselect **Create New Virtual Application**. If you want to make an application aware mount, then follow the procedure in [Mount an Oracle database as a virtual application](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount-virtualdb).

     * Open the **Mapping Options** by clicking on the arrow icon to the left of the title.

     * If required, change the default **Storage pool** to be used for the mount from the drop-down list. This only applies to mounts where there is no existing staging disk, such as Direct to OnVault and imported OnVault images, otherwise the pool where the source image disks are located are always used regardless of what is set here.

     * **MOUNT LOCATION** : Enter the mount path where to mount the database and log backup image:

       * The Oracle database backup image is mounted to the specified mount path `/<mountpath>`.
**Note:**   
If the path exists as an empty folder, the Backup and DR agent uses it.  
If it does not exist, the Backup and DR agent creates it.  
If it exists as a file or as a folder that is not empty, then the job fails.
     * If logs are Backup and DR protected, then the logs image are mounted to `<mountpath>_archivelog_Log`, and subsequent logs images to the same archivelog name with a increasing number at the end, for example, `<mountpath>_archivelog_Log1`.

     * If no mount path is specified the Oracle database backup image and log backup image is mounted to a default generated path `/act/mnt/(jobid)_mountpoint_<random generated number>`.

**Note:** The 'Maximum performance' option is only supported for OnVault backup images.
  5. Click **Submit** to submit the job. You can go to **Monitor** > **Jobs** to view the progress and details of the job The mounted image is available in the Active Mounts.




## Management of the active mounts

Once you have created a mount, you can track the image from the **App Manager** > **Active Mounts**. Ideally, don't leave any image mounted indefinitely. This is because the backup image that the mount was created from, cannot expire until all its mounts have been deleted. When you have finished using the mounted image then either:

  * [Unmount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount) the image. You can [remount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#remount) it if needed. You can then [delete](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#delete) the image later when you are certain it is no longer needed.
  * [Unmount and delete](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount-delete) the image. This deletes the mounted image, not the backup that the mount is based on.



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
