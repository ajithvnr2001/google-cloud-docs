---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-and-migrate-oracle/
title: Mount and migrate an Oracle backup for instant recovery to any target in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:54.684624+00:00
---

# Mount and migrate an Oracle backup for instant recovery to any target in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-and-migrate-oracle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Mount and migrate an Oracle backup for instant recovery to any target in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Instant recovery of an Oracle database to any target using Backup and DR _Mount and Migrate_ is a two-phase operation: The _Restore Mount_ phase provides instant access to the database by starting it from a backup/recovery appliance presented backup image. The _Migration_ phase migrates the database data files to the production storage while the database is online.

## How it works

**Restore Mount Phase** : provides instant access to the database from a selected image presented by the backup/recovery appliance.

  * A copy of the selected backup image is mapped to the target database server and presented to the ASM or file system layer (based on the source database backup image format).
  * RMAN API is used to perform the following processes: 
    * Restore the Control file and Redo Log file to the specified control file and redo file location (ASM diskgroup or file system).
    * Switch the database to the copy of the image presented by the backup/recovery appliance.
    * Roll-forward all available archive logs to the specified recovery point.
    * Open the database in read and write mode.
  * The database is running from the mapped copy of the backup image presented by the backup/recovery appliance.
  * The Control File and the Redo Log file of the database is on the selected local production storage (ASM diskgroup or file system) on the target.
  * After a successful restore mount operation, the database is available for production operation; a migration option is available to move the data back to the production storage (ASM disk group or file system) using the Oracle online datafile `move` API. The migration can take place while the database and application is up and running.



**Migration Phase** : moves the database datafile online to the production storage.

  * Data migration runs in the background. The Oracle online datafile move API is used to migrate the data.
  * Datafiles are moved from the Backup and DR presented copy of backup image to the selected target database storage (ASM diskgroup or file system).
  * The Backup and DR presented copy of the backup image (ASM diskgroup or file system) is removed and unmapped from target upon completion of migration.



You can track the progress of the Restore Migrate job in the appliance management console monitor.

## Phases of the mount-and-migrate process

A mount-and-migrate process goes through two distinct phases, a restore-mount followed by the data migration.

### Restore Mount phase

  1. From the Backup and DR appliance management console, open the **App Manager** > **Applications** list.
  2. Right-click the database and select **Access**.
  3. Select the latest snapshot to recover and choose **Restore**.
  4. On the Restore page, choose **MOUNT AND MIGRATE**.

     * Target: For all configurations, eligible Oracle database servers will be available to choose under the drop-down. Select the target server for restore from the drop-down.
     * Replace Original Application identity: This option is only available when a restore is performed to a new server on the same appliance where the backup was originally generated. 
       * Yes: This replaces the original application and will carry the same application ID, jobhistory, backup images and backup plan as the original Oracle application.
       * No: This won't replace the original application. It will be discovered as a new application as part of restore job.
     * Rollforward time: Choose a date and time for a database protected with logs to recover to the required point in time.
     * Application Options:

       * DATABASESID: This is pre-populated with the protected database SID name and is immutable.
       * USERNAME: This is pre-populated with source database Oracle software owner. Update the USERNAME if the Oracle software owner on the selected target server is different.
       * ORAHOME: This is pre-populated with source database Oracle Home path. Update the Oracle Home directory if the Oracle Home path is different on the selected target server.
       * Advanced Options: This is pre-populated and displays all the database parameter settings (from pfile) at the source at backup time. Make sure the parameter value is correct for the target database server (source or new target) for restore.
     * Mapping Options:

       * CONTROL FILE TARGET TYPE: Select the database control file target type (ASM diskgroup or file system) for the database from the drop-down list. FS target type is not supported for backup images in ASM format.

Backup image format | Supported storage type  
---|---  
ASM | ASM (FS not supported)  
FS | FS, ASM  
       * CONTROL FILE TARGET: A drop-down list shows the available target (ASM diskgroup or file system) based on selected CONTROL FILE TARGET TYPE. Select the target for the control file location from the list of eligible disk groups or file systems in the drop-down list. Multiple selections can be made to multiplex the control file. This location is also used as the destination for the temporary files for the temp tablespace.

       * REDO TARGET: If none is selected then the Control File Target will be used for the Redo target. A drop-down list shows the available target (ASM diskgroup or file system) based on the selected Control File Target Type. Select the target for the redo file location from the list of eligible disk groups or file systems in the drop-down list. Multiple selections can be made to multiplex the redo file.

       * RAC NODES: This is only available when the selected restore target is set up with a RAC cluster. Click **+** to add the RAC node list for restore to RAC cluster.

  5. Click the **Pre-Flight Check**. If the pre-flight check fails, fix the issue and resubmit the pre-flight check.

  6. Click **Submit** to submit the restore job.


**Note:** When the job is complete, the database will be available for production operation. The database will be running out of the backup image copy presented by backup/recovery appliance where Control File, and the Redo Log file of the database will be on the selected local server.**Note:** Adding a new data file in the database after the restore mount operation and before starting the migration job: Post restore mount operation, the database is running from the Backup and DR presented backup image. To add a new datafile, make sure to use the `default db_create_file_dest` location which will create the data file on backup/recovery appliances presented disk. Adding the data file with location before migration to the local disk is started will lead to database backup failure.**Note:** Migration is blocked until the post-restore mount database backup is complete. The baseline backup for restore mounted database from a snapshot image is instant, because it uses the backup/recovery appliance internal snapshot of the data disk. The baseline backup of a restore mounted database from an OnVault pool may take a long time depending on the size of database, because the backup uses conventional RMAN.**Note:** Migration of a large database can take a long time. If you plan to upgrade the backup/recovery appliance, and if you have a restore mounted database (an active mount), make sure that you either complete the migration, or cancel the restore mount to remove the restore mounted database.

### Migration phase

  1. From the appliance management console App Manager **Applications** list, right-click the database and select **Access**.
  2. Select the mounted image. From the active mount select **Migrate**.

  3. On the **Migrate** page, for **Copy Thread Count** , enter a thread count value to configure parallelism for the online datafile move operation.

  4. For Migrate Mapping, map the source volume to Target volume (ASM diskgroup or file system) in these scenarios:

     * Source volume displays source database data file distinct locations (ASM diskgroup or file system) name.
     * Required Size displays the space required on the target location (ASM diskgroup or file system).
     * Target volume displays all the eligible target locations (ASM diskgroup or file system) for datafiles. Select the appropriate target for source datafile to target datafile location mapping.
  5. Click the pre-flight check. If the pre-flight check fails, fix the issue and resubmit the pre-flight check.

  6. Click **Submit** to submit the restore job. When the migration job is complete, the Backup and DR presented backup image copy (ASM diskgroup or file system) will be removed and unmapped from the target, and the database will be running from your production storage.


**Note:** After a successful database migration, Oracle may occasionally hold locks on staging disks for an extended duration. If this occurs, analyze the process types holding the locks. If it is safe to do so, manually release the locks by killing the process, or by restarting the database. When the locks are released, re-run the job to remove the staging disks. This should remove the disks and mark the job as successful.

## The Oracle DBA Guide

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
