---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/db2-on-gce-backup-recovery/
title: Protect and recover IBM Db2 databases on Compute Engine instances in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:23.999614+00:00
---

# Protect and recover IBM Db2 databases on Compute Engine instances in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/db2-on-gce-backup-recovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Protect and recover IBM Db2 databases on Compute Engine instances in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

This page details how to use Backup and DR for Db2 on a Compute Engine instance using Persistent Disk snapshot.

## Protect the Db2 production environment against data loss, errors, and corruption

Db2 is a family of relational database management systems within IBM's Information Management division that is centered on several relational database management system offerings. Many enterprises use Db2 for their mission critical applications. 

As can happen with any database, Db2 is susceptible to corruption, accidental deletion, or even security threats such as ransomware attacks. Backup and DR lets you efficiently and securely back up and recover your production systems.

For an introduction to how you use Backup and DR to protect your Db2 databases, see [Backup and DR for IBM Db2](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-db2).

## Deploy Backup and DR first

Before you begin, you must read and complete the following procedures:

  * [Plan a Backup and DR deployment](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-plan)

  * [Prepare to deploy Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-prep)

  * [Deploy Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-guide)




## See how Backup and DR works

Then see how Backup and DR works by going through [Get started with Backup and DR: protect and recover a Compute Engine instance](https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/gce-instances-backup-recovery).

## Prepare Db2 instances for backup

**Prerequisites**

  * The Db2 services and databases must be running.
  * Database `logarchmeth1` and `logarchmeth2` parameters for the archive log backup should be set to valid paths for log backups.
  * All Db2 servers in (Compute Engine) that have Db2 data to be protected by Backup and DR must have been onboarded to Backup and DR.
  * All Db2 servers in (Compute Engine) that have Db2 data to be protected by Backup and DR must have the Backup and DR agent installed.
  * All the Db2 database db, log, log backup mount points should have the Persistent Disk VG and LVM. Direct file system on Persistent Disks for the Db2 application is not supported.
  * The same mount point shouldn't be used for the Db2 databases for database, active log with log backups locations.



## Discover and protect Compute Engine instances that host Db2 databases

You must onboard the Db2 Compute Engine VM before you can onboard the Db2 database application. To onboard the Compute Engine instance to Backup and DR, see [Discover and protect Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-compute-engine).

## About this quickstart exercise

This exercise guides you through the steps of discovering and protecting a Db2 database running in a Compute Engine instance, and finally mounting a fully-functional new Db2 database from the backup image to a new location.

  1. Install the Backup and DR agent on the Compute Engine instance
  2. Create a backup plan for the Db2 database
  3. Discover and protect Db2 databases
  4. Recover a Db2 database from a backup: mounts and restores



## Install the Backup and DR agent on the Compute Engine instance

The Backup and DR agent connects the Compute Engine instance to the backup/recovery appliance. To install the agent, see [Install the Backup and DR agent on a Linux host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/linux-agent).

## Create a backup plan for the Db2 database

See [Create a policy template](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template).

### Set advanced policy settings for Db2 databases

When you create the policy template, you configure advanced policy settings specific to Db2 protection using Persistent Disk snapshot.

**Note:** For advanced policy settings details, see [Configure advanced policy settings](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings).

**Snapshot location** : Select the region where the Persistent Disk snapshots are to be stored. By default, multi-region is selected (based on the source disk location). You can also change the snapshot storage location to a different region than the source disk region. When storing snapshots in a location that is different from the location of your source disk, the data travels over the network between those locations and may incur network fees. Snapshots incur the same fees as Cloud Storage egress. Learn more about the [Persistent Disk snapshot](https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/db2-on-gce-backup-recovery/). To know the pricing details, see [disk pricing](https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/db2-on-gce-backup-recovery/).

**Snapshot type** : Select the Persistent Disk snapshot type to be used for Db2 backups. Snapshots incrementally backup data from Persistent disks. During backups, a new snapshot is created to capture the current state of the Persistent disk and later can be used to create a new disk for mounts or restores. Compute Engine stores multiple copies of each snapshot across multiple locations with automatic checksums to ensure the integrity of your data. Learn more about the [Persistent Disk snapshot](https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/db2-on-gce-backup-recovery/). To know the pricing details, see [disk pricing](https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/db2-on-gce-backup-recovery/).

  * Standard: By default, the Standard snapshot type is selected. Use the standard type if you want to retain the backups for less than 90 days.
  * Archive: Select the Archive type if you want to retain the backups for a long duration. Note that the minimum billing period for the archive snapshot is 90 days irrespective of the retention period defined in policy and that Archive type also has an additional retrieval charge if used in a mount or restore job.



### Enable and Protect Db2 archive log backup

When creating a snapshot policy for a database you have the option of also capturing its log files at a specified frequency. The frequency at which database logs are captured is defined separately from that of the database. For example, a database can be captured every day and its logs captured every hour.

**Truncate (Purge) Log After Backup** : Specify whether to truncate (purge) the Db2 archive logs after backup. When Truncate Log after Backup is enabled, Db2 archive logs are truncated. By default archive purge will run with every database backup. Recommend to use default to achieve best recovery RTO. If production log retention is set then purge will run based on **Retention of production db logs in hour** setting under **Application Details & Settings**.

The options are:

  * **Don't truncate/purge log after backup** : This is the default. In this mode the archive log won't be purged.
  * **Truncate/purge** log after backup: Choose this option if you want to enable archive log purge
  * **Enable Database Log Backup** : Set the option to **Yes**. The **Enable Database Log Backup** option allows the backup plan policy to back up a database and all associated transaction log files. The logs are backed up when the log snapshot job runs. When set to Yes, the related options are enabled.
  * **RPO** : Specify the database log backup in minutes. When **Enable Database Log Backup** is set to Yes, RPO defines the frequency for database log backup. Frequency is set in minutes and must not exceed the database backup interval. The smallest value that can be set (in minutes) is 15.
  * **Log Backup Retention Period (In Days)** : When Enable Database Log Backup is set to Yes, log retention is defined separately from the retention of the snapshot policy. Having a separate retention period lets you use logs in conjunction with copies of the database stored in the snapshot pool. 
  * **Replicate Logs (Uses streamsnap Technology)** : Set this option to No. This does not apply to Db2 Persistent Disk snapshot protection.

**Note:** This function is enabled (set to Yes) by default. Not setting it to **No** will result in a template creation error.

  * **Send logs to OnVault Pool** : Set this option to **No**. This does not apply to Db2 Persistent Disk snapshot protection.

**Note:** This function is enabled (set to Yes) by default. Not setting it to **No** will result in a template creation error.

### Db2 Archive log backup recommendations

For best results with log backups, pay attention to the following:

  * Don't use the Db2 database archive log mount to store files other than Db2 archive log backups.
  * By default archive purge runs every 24 hours. This achieves the best recovery RTO. If production log retention is set, then purge runs based on the **Retention of production db logs in hour** setting under **Application Details & Settings**. Size the Db2 archive log backup disk to store archives based on the production log retention setting.



## Discover and protect Db2 databases from the App Manager

**Note:** Successful Compute Engine VM onboarding provides the link to Db2 onboarding wizard (step 3 below)

To discover and protect the Db2 database applications, follow these steps:

  1. From the appliance management console's **App Manager** > **Applications** page, select **Add Application** .
  2. Select **Db2** in the wizard.
  3. Follow the wizard: 
     1. In the **Select** section, select the Db2 instance to manage.
     2. In the **Manage** section, apply the policy template and the resource profile (you created these in Create a backup plan).
     3. Under **Application Settings** in the **Configure** section, set the **Configure backup options** :
     4. **Backup capture method** : choose **Use Persistent Disk Snapshot**.
     5. **Retention of production DB logs in hours** : This is used to purge the Db2 archive log backup from the `logarchmeth1` destination. Based on this setting the log is purged older than the specified hours. With default values, all logs prior to the last data backup are purged (24 hours default).
  4. Click **Save** > **Next** , then click **Finish**.



You can see the database in the **App Manager** **Applications** list with a green shield indicating that the backup plan has been applied.

## Recover a Db2 database from a backup: mounts and restores

Restoring a database overwrites the original data from the backup. This procedure is for restoring a backed up database. To restore a database from a backup, see Restore a Db2 database from a backup

Mounting a database puts a new copy of the database at a mount point where it can be used just like the original database. To mount a new database from a backup, see Mount a Db2 backup as a standard mount.

### Mount a Db2 backup as a standard mount

A standard mount provides the backup image disk of data, active log and archive log volume to the specified target. You can mount a backup of a Db2 databases as a standard mount for any manual operation.

#### Pre-checks during mount

  * Connector connectivity status: Verify that the {backupdr_name_short} agent is installed and the secret is applied for host connectivity between the appliance and agent.
  * Mount locations specified are available for mount operation.
  * If the same VG exists at target and is in use by any database, then fail the pre-check with a message that VG is in use by the database. To proceed, shut down the database before proceeding with the mount operation.
  * Permission check on the source and target projects for the Google Cloud service.



#### Mount the database from a backup

Use these instructions to mount a backup:

  1. Right-click the protected database from the **App Manager** > **Applications** list, and select **Access**.

**Note:** You can use the **Managed Backup Plan** status filter to show only protected databases.
  2. Select a snapshot image and choose **Mount**.

  3. On the Mount page select the target Db2 server under **GCE INSTANCE NAME**. You can use the filters **Project Name** , **Region** , and **Zone**.

  4. Optionally, enter a unique name associated with the mount in the Label field. **INCLUDED DATABASES** is informational only showing the list of databases under backup image.

  5. Under **Mapping Options** :

     * **MOUNT POINT** : is pre-populated with the source MOUNT POINT. Provide the path that is not in use at the selected target and that you want to use to mount the snapshot image of all `data`, `active log`, `dbpath` and `Logbackup` volumes on the target server.
**Note:** The hyphen special character **-** (ex: data-1) is not supported in the device mount location
     * **DISK TYPE** : is pre-populated with the source DISK TYPE value. You can change the disk type from the drop-down.
  6. Click **Pre-Flight check**. This will validate the required options on the target server for a successful mount. Upon a successful Pre-Flight the **Submit** button will be enabled. Upon failure, pre-flight will show the failed check to correct and rerun the Pre-Flight.

  7. Click **Submit**. You can go to the **Job Monitor** to view the progress and details of the job.




#### Unmount the mounted database backup when it's no longer needed

To unmount the mounted database backup:

  * To remove or keep the disk after a successful mount, go to **Application** > **Access** page and select the mounted image.
  * On the access page under the **Current active mount** drop-down, there are two options: 
    * **Unmount & Delete**: Choose this option to unmount the mount point, detach the disk and delete the disk from the target server.
    * **Forget Active Mount** : Choose this option to leave the disk attached and mounted and remove the metadata from Backup and DR. Users will need to use the Google Cloud console to remove this image from the target instance.



### Restore a Db2 database from a backup

This procedure is for restoring a backed up database.

**Note:** You can also mount the database. Mounting a database puts a new copy of the database at a mount point where it can be used just like the original database. To mount a new database from a backup, see Mount a Db2 backup as a standard mount.

#### Preflight check

Before submitting the restore procedure, preflight checks validate the required prerequisites for a successful database restore:

  * Db2 SID: Db2 is configured on the target node with the same Db2 SID name.
  * Db2 VERSION: Target Db2 version is the same as the source Db2 version.
  * For restore to a new target 
    * Verify that the mount point specified under the mapping option is not used or mounted at the target server.
    * Verify that the specified mount locations are available for the mount operation.
  * Check if the Db2 instance is running. It must be shut down during the restore operation.
  * If the same VG exists at target and is in use by any database, then fail the pre-check with a message that VG is in use by the database. To proceed, shut down the database before proceeding with restore.
  * Permission check on the source and target projects for the Google Cloud service.



#### Restore a Db2 database back to the source

  1. From the **App Manager** > **Applications** list, right-click the database and select **Access**.
  2. Select the latest snapshot to recover and choose **Restore**.
  3. On the Restore page, select **Restore back to source**. All fields are pre-populated with the source value of protected Db2 instance and all are immutable except **Application options**.
  4. **Label** : Optionally, enter a unique name associated with the mount in this field.
  5. **INCLUDED DATABASES** is informational only, showing the list of databases under the backup image.
  6. Set the application options: 
     * **Rollforward time** : For a database protected with logs, choose a date and time to recover to.
     * **TARGET INSTANCE** : This is pre-populated with the protected database instance name and is immutable.
     * **Mapping Options** :
     * **Volume Mount Point Locations** : This is prepopulated with the source volume groups, logical volumes, device paths and disk types where the Db2 `data`, `dbpath`, `log`, `log backup volumes` are mounted.
     * **Disk Type** : The disk type lets you select the type of underlying block storage that is used for the recovered data from the backup images.
  7. Click the **Pre-flight check**. If the pre-flight check fails, fix the issue and resubmit the pre-flight check. If the pre-flight check is successful, click **Submit** to submit the restore job.



#### Restore a Db2 database to a new target

  1. From the **App Manager** > **Applications** list, right-click the database and select **Access**.
  2. Select the latest snapshot to recover and choose **Restore**. On the Restore page, select **Restore to new target** : All fields are pre-populated with the source value of protected Db2 instance but you can edit them.
  3. To recover to a new target, Select the **Project** , **Region** , and **Zone** of the instance that you want to recover the Db2 database to.
  4. For **Instance name** , select the node to restore from the drop-down list of eligible Compute Engine instances.
  5. **Label** : Optionally, enter a unique name associated with the mount in this field.
  6. **INCLUDED DATABASES** is informational only, showing the list of databases under the backup image.
  7. **Replace original application identity**. This option is only available when restore is performed to a new host on the same appliance where the backup was originally generated. 
     * **Yes** : replaces the original application and carries the same application ID, jobhistory, backup images and backup plan as the original application.
     * **No** : doesn't replace the original application. It will be discovered as a new application as part of the restore job.
  8. Set the application options: 
     * **Rollforward time** : For a database protected with logs, choose a date and time to recover to.
     * **TARGET INSTANCE** : This is pre-populated with the protected database instance name and is immutable.
     * **Mapping Options** :
     * **Volume Mount Point Locations** : This is prepopulated with the source volume groups, logical volumes, device paths and disk types where the Db2 `data`, `dbpath`, `log`, `log backup volumes` are mounted.
     * **Disk Type** : The disk type lets you select the type of underlying block storage that is used for the recovered data from the backup images.
  9. Click the **Pre-flight check**. If the pre-flight check fails, fix the issue and resubmit the pre-flight check. If the pre-flight check is successful, click **Submit** to submit the restore job.

**Note:** Restoring to a new target will present new disks for all VG and volumes. Existing disks will remain attached to Compute Engine instances. If not needed, detach and delete those disks.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
