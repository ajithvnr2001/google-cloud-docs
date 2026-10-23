---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-oracle/
title: Backup and DR for Oracle on a backup/recovery appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:13.909459+00:00
---

# Backup and DR for Oracle on a backup/recovery appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-oracle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Backup and DR for Oracle on a backup/recovery appliance Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Oracle database is a popular enterprise class database that supports mission-critical applications. This page introduces Backup and DR for Oracle database environments. The associated architecture provides application-consistent, incremental-forever backup to Google Cloud, as well as instant recovery and cloning for multi-TB Oracle databases.

## How it works

The following sections describe the process of data capture and data recovery.

### Data capture

  1. The Backup and DR agent is deployed in the Oracle server.

  2. Mount staging disk on database server.

  3. Invoke RMAN incremental API to copy changed blocks.

  4. Invoke RMAN incremental merge to create new virtual full.

  5. Unmount staging disk from database server.

  6. Backup and DR takes an internal snapshot. The point-in-time synthetic full backup is ready.




### Data recovery

Backup and DR instantly mounts a rewritable staging disk over ISCSI or NFS and brings the database online.

### Oracle backup APIs

Backup and DR uses the following Oracle APIs:

  * RMAN Image Copy: An image copy of a data file is much faster to restore because the physical structure of the data file already exists. RMAN directive BACKUP AS COPY creates image copies for all data files of the entire database and retains the data file format.

  * ASM and CRS API: ASM backup disk group is managed using ASM and CRS API.

  * RMAN archive log backup API: Generated archive logs are backed up to staging disk and purged from the production archive location.


**Note:** For better performance, see [Oracle patches and known issues](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/oracle-patches-known-issues).

## Minimize conflicts when you use Backup and DR with other backup products

Backup and DR can coexist with legacy products capturing data from production databases. The following best practices can help improve your experience:

### Oracle database backup schedule

Best practice |  Schedule Backup and DR database backup jobs to begin at a time when the legacy backup software should be finished. Don't schedule the legacy backup software to run immediately after a Backup and DR database backup job normally completes.  
---|---  
Reason | If legacy backup jobs and Backup and DR database backup jobs run concurrently, it may result in a serious performance impact on the database server leading to instability and possibly an outage. Additionally, for Oracle, this may result in invalid backups for one or both solutions.  
  
### Oracle archive log management

Oracle uses archive logs generated during a database backup to ensure the consistency and recoverability of that backup. As a result, if archive logs are purged during a database backup job, that backup copy is unrecoverable.

Requirement | Only one system can manage (capture and/or truncate/purge) logs, either the legacy backup software or Backup and DR.  
---|---  
Best practice | Don't allow Oracle archive logs to be purged during a Backup and DR job, and don't allow Backup and DR to purge archive logs during a legacy backup RMAN job.  
If the legacy software is managing the archive log, then disable archive log purge jobs in the legacy backup software at the start of the Backup and DR backup job, and resume purge jobs at the end or retain archive log for a minimum of 24 hours before purging.  
Reason | If archive logs are purged during a database backup job, then that database backup may be unrecoverable.  
  
### RMAN metadata conflict with legacy backups that make Backup and DR backups obsolete

By default, the parameter `DO NOT UNCATALOG` in Backup and DR application details & settings is set to **No**. A Backup and DR data file backup is cataloged at the start of backup and uncataloged at the end of the job. Setting this to **Yes** optimizes the backup time for databases with a large number of data files by keeping the RMAN data file backup cataloged after each backup job. However, it interferes with other backup products.

Requirement | Set Backup and DR application details & settings parameter `Do not uncatalog` to **No**.  
---|---  
Best practice | Backup and DR database backups are incremental-forever. This is achieved by using RMAN image copy with the RMAN incremental merge API. The first RMAN backup is a full image copy of the database data file on Backup and DR backup disk with internal snapshot of backup disk. Subsequent RMAN incremental backup runs with RMAN incremental merge on Backup and DR backup disk, updating the last full with incremental changes before snapshot. However, if a third party database backup or a crosscheck of backup runs after the Backup and DR database backup, then all backup datafiles under Backup and DR backup are marked obsolete under RMAN metadata. Backup and DR application details & settings parameter `Do not uncatalog` set to **Yes** results in the following error: **Failed to catalog image copies from staging device** and backup failure. Keep `Do not uncatalog` set to **No** to co-exist with other legacy backup products.  
Reason | By default the parameter `Do not uncatalog> in Backup and DR application details & settings is set to **No**. Setting this to **Yes** interferes with other backup products. `  
  
## Oracle database block change tracking (BCT)

Oracle block change tracking enables fast database backups by identifying which blocks have changed. Only changed blocks are included in the backup operation.

  * Backup and DR incremental-forever supports databases running with BCT enabled or disabled. With BCT not enabled the incremental backup time increases.

  * Change block tracking is enabled at database level.

  * Oracle records the changed blocks in each data file in a tracking file which is a small binary file stored in the database area.

  * With BCT enabled, RMAN uses the BCT file to get the changed blocks for incremental backup.

  * RMAN scans each block in a data file for all data files in the database during incremental backup when Change Block Tracking on the database is not enabled.




## Protect Oracle databases in a Backup and DR consistency group

In most configurations, a consistency group can contain a single Oracle database application and any number of file system applications from the Oracle server. A consistency group is the recommended choice for Oracle databases in test-dev and other business agility use cases.

## Oracle databases with TDE

Backup and DR supports a variety of capture and presentation methods for Oracle databases under various configurations. This includes backup, recovery, and Application Aware mount operations of Oracle database with Transparent Data Encryption (TDE) configured.

For Oracle databases with TDE, wallet files from the source backup host must be available to the target host of any Application Aware mounts. This can be accomplished in several ways.

  * The wallet files can be copied from the backup source server to the target mount server and Oracle configured to access them.
  * If the Oracle wallet files are stored on a central, shared device on the network, the Appaware mount target Oracle instance should be configured to access them.
  * If the Oracle wallet files were captured during Backup and DR backup by setting the Oracle Configuration File Location advanced setting, the wallet files can be retrieved with the following steps:

    1. Do a [standard mount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-oracle) of the database to the target host.
    2. Copy the wallet files from the standard database mount to the target host and configure Oracle to use them.
    3. [Unmount the database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount) from the target host.
    4. Perform an [Application Aware mount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-oracle-virtualdb) of the database to the target host. 

**Note:** Application Aware mounts for TDE enabled databases require the wallet to be copied to the appropriate location on the target host and the wallet must be configured and open.

## Backup and DR with Oracle Exadata database or Oracle ExaCC

Backup/recovery appliances support capture and presentation of Exadata data over iSCSI or Oracle dNFS protocols.

  * The backup/recovery appliance is connected over iSCSI or Oracle dNFS in the network (not in the data path).

  * RMAN backup uses RMAN to directly write to a copy datastore presented by Backup and DR as a file system or as an ASM Disk Group.

  * Data Capture Formats: under **ASM disk group** (iSCSI only) or under **File system** (dNFS or iSCSI).

  * Backup and DR incremental-forever backup uses **RMAN incrementally updated backups** , rolling forward image copy backups.




### Backup and DR capture of Exadata data and ExaCC

The Backup and DR agent must be installed on the Exadata server to facilitate communication with the backup/recovery appliance and to invoke the RMAN API for database backup.

The Backup and DR agent exposes and maps Backup and DR disks to the Exadata server as an iSCSI target. Data capture format can be under **ASM disk group** or under the **File system**.

Install the Backup and DR agent on each Exadata host under the user space to facilitate the communication with backup/recovery appliance and to invoke the RMAN API for database backup.

### Capture format under ASM diskgroup

During a backup, the Backup and DR agent does the following:

  1. Map and expose the logical disk to the Exadata server as an iSCSI target.

  2. Add the Backup and DR disk path to the ASM disk string.

  3. Make sure the ASM disk string is added to the parameter file and does not exist in the CRS profile.

  4. Create an ASM disk group as an external redundancy using Backup and DR disk.

     * RMAN backup using RMAN to directly write to a copy datastore presented by backup/recovery appliance as ASM Disk Group or as File system.

     * Incremental-forever backup using **RMAN incrementally updated backups** , rolling forward image copy backups.




### Capture format under file system using dNFS

Oracle direct NFS (dNFS) is an optimized NFS (network file system) client that provides faster and more scalable access to NFS storage located on NAS storage devices (accessible over TCP/IP). Direct NFS is built directly into the database kernel, just like ASM.

The dNFS protocol can be used for file system-based backup as an NFS share.

The Backup and DR agent exposes and map Backup and DR disks to Exadata server as NFS share.

Prerequisites for dNFS on Exadata server:

  * Enable dNFS on Exadata server:

`cd $ORACLE_HOME/rdbms/lib` `make -f ins_rdbms.mk nfs on`

  * Restart the database.

Use the RMAN API to back up the database to file system on dNFS share presented by backup/recovery appliance.

**Note:** dNFS supports backups under file system only; it does not support **ASM Switch & Rebalance**.



## Bring Backup and DR protected ASM diskgroups back online after reboot of a target DB server

After any database server reboot where Backup and DR copy is mounted, or Backup and DR backups are in progress for the database at the time of reboot/crash, follow these steps to get the Backup and DR disk group mount back:

  1. Check that the target database server is back up, and that ASM and RAC system are also up.

  2. Restart the Backup and DR agent (from root).

  3. Set ASM environment.

  4. Login to ASM `sqlplus` and check the disk group status:
         
         select name, state from v$asm_diskgroup where name = '<dg name>';)
         

  5. If unmounted, mount the disk group: `alter diskgroup <dg name> mount;`

  6. Login to the Oracle OS and set the database environment, then start the database.




## What's next

Read about the [prerequisites for backing up an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prerequisites).

## Other documentation for Backup and DR for Oracle

  * [Backup and DR for Oracle databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/oracle-intro)
  * [Prerequisites for protecting an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prerequisites)
  * [Oracle patches and known issues](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/oracle-patches-known-issues)
  * [Prepare Oracle databases for protection](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prepare)
  * [Discover and protect an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-oracle)
  * [Set application details and settings](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-oracle)
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
