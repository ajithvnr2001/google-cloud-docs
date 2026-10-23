---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-sap-hana-new/
title: Restore and recover SAP HANA databases in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:32.003319+00:00
---

# Restore and recover SAP HANA databases in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-sap-hana-new/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Restore and recover SAP HANA databases in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

There are two ways to recover an SAP HANA database from a backup:

  * Mount an SAP HANA backup as a standard mount
  * Restore SAP HANA databases



## Mount an SAP HANA backup as a standard mount

A standard mount provides the backup image disk of data, active log and archive log volume to the specified target. You can mount snapshot backups of an SAP HANA database as a standard mount:

### Pre checks during mount

Before a mount job runs, these pre checks are performed:

  * Connector connectivity status: Verify that the Backup and DR agent is installed and secret is applied for host connectivity between the backup/recovery appliance and the Backup and DR agent.
  * Mount locations specified are available for mount operation.
  * HANA binary is installed
  * Verify that the HANA SID the same as the source is not up and running on the target.
  * The HANA instance version is greater than 2.0 SP05.
  * Permission Check On Source and target Project for the Cloud Storage service.



### Mount the backup

Use these instructions to mount a backup:

  1. Right-click the protected database from the **App Manager Applications** list, and select **Access**.

**Note:** You can use the **Managed Backup Plan** status filter to show only protected databases.
  2. Select a snapshot image and choose **Mount**.

  3. On the **Mount** page:

     * **Project name** , **Region** , and **Zone** : Select the project, region, and Zone of the instance to which you want to mount the HANA database image.
     * **Instance Name** : Eligible Compute Engine instances (HANA nodes) will be available to choose under the drop-down. Select the node for mount from the drop-down. .
  4. Optionally, enter a unique name associated with the mount in the **Label** field.

  5. **INCLUDED TENANT DATABASES** is informational only, showing the list of tenant databases under backup image.

  6. Under **Mapping Options** :

     * **DATA Volume Mount Location** : This is prepopulated with the source device path and disk type where the HANA data volume is mounted.
     * **Log Volume Mount Location** : This is prepopulated with the source device path and disk type where the HANA active log volume is mounted.
     * **Log Backup Volume Mount Location** : This is prepopulated with the source device path and disk type where the HANA archive log backup volume is mounted.

       * **DEVICE PATH** : is pre-populated with the source DEVICE PATH. Provide a path that is not in use at the selected target and that you want to use to mount the snapshot image of DATA VOLUME, LOG VOLUME, and LOG BACKUP VOLUME on the target server.
**Note:** The hyphen special character "-" (for example: data-1) is not supported in the device mount location.
       * **DISK TYPE** : is pre-populated with the source DISK TYPE value. You can change the disk type by selecting the different type from the drop-down value.
  7. Click **Pre-Flight check**. This validates the required options on the target server for a successful mount. If the pre-flight check fails, the pre-flight will show which check failed so you can correct it and rerun the pre-flight.

  8. Click **Submit**. You can go to the **Job Monitor** to view the progress and details of the job.




### Unmount the mounted backup snapshot image

To remove or keep the disk after a successful mount:

  * Go to **Application** > **Access** page and select the image used for mount. 
  * On the Access page under the **Current active mount** drop-down, select either: 
    * **Unmount & Delete**: Choose this option to unmount the mount point, detach the disk and delete the disk from the target server.
    * **Forget Active Mount** : Choose this option to leave the disk attached and mounted, but remove the metadata from Backup and DR. You will have to use the Google Cloud console to remove this image from the target instance after this operation is finished.



## Restore SAP HANA databases

Before you can restore an SAP HANA database from a backup image, review these license requirements.

### License requirements and impact on restore

  * The license key for an SAP HANA database is based on the system ID and the hardware ID. After a recovery, an SAP HANA license key becomes invalid if the SID or hardware ID has changed.
  * During recovery, a temporary license key is installed automatically if the backup used for recovery has a permanent license, which is still valid. You can work with the automatically installed temporary license for up to 90 days. During this time, you need to apply to SAP to have the license from the source database transferred to a new license key. You then need to install the new license key in the recovered SAP HANA database.
  * If the backup that was used for recovery only had a temporary license, the database is in lockdown mode immediately after recovery.
  * Source database with temporary license These are backups taken with temporary licenses. 
    * Restore back to source: It is 90 days from the time of database creation and the database is in lockdown mode.
    * Restore to the new target: It fails as SAP temp license does not allow the restore to a new target.
  * Source database with permanent license These are backups taken with permanent licenses. 
    * Restore back to source: No issue.
    * Restore to the new target: It has a 90 days trial license. Backups succeed but you cannot use the new backup to restore.



### SAP references

  * https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/2.0.02/en-US/19a0f5a85685453080f00087bb9b9c98.html
  * https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/2.0.02/en-US/bddd0b28bb571014bd9592d247dcd403.html



### Preflight check

Before submitting the restore procedure, preflight checks validate the required prerequisites for a successful database restore.

  * HANA SID: HANA is configured on the target node with the same HANA SID name.
  * Verify Database Status: HANA Database is not up and running.
  * Config file: Config file global.ini is available on target server
  * Log backup path: Log backup path is set under global.ini
  * HANA Version: Target HANA version is the same as the source HANA version.
  * USERSTOREKEY: Provided userstore key exists on target or a valid privileged username and password is specified which exists at the time of backup.
  * For restore to a new target, verify the Mount point specified under the mapping option is not used or mounted at the target server.
  * Verify Data & Log Volume Details: If the Data & Log Volume path in the config file (global.ini) is defined other than the chosen device path under mapping option then the config file (global.ini) will be updated with the path chosen under the mapping option.
  * Node Status: 
    * Scale-up and standalone config: Target HANA server is up and available
    * HANA HA (1+n) config: Validates that replication is disabled. Replication needs to disabled before restore can be initiated. Post restore replication needs to be reconfigured. Restoring to any node of a HANA HA (1+n) cluster results in creating a standalone application on the selected target host. User has to explicitly configure the cluster back as needed and discover the application appropriately.



### Restore an SAP HANA database

  1. From the **App Manager Applications** list, right-click the database and select **Access**.
  2. Select the backup image to recover and choose **Restore**.
  3. On the **Restore** page the options are:

     * **Restore back to source** : All fields are pre-populated with the source value of protected SAP HANA instance and are immutable except **Application options**.
     * **Restore to new target** : All fields are pre-populated with the source value of protected SAP HANA instance and are mutable.
**Note:** Before restoring an SAP HANA database to a new target server, if the DATA, Active LOG and Log backup volumes are encrypted by HANA encryption, then import the encryption keys from the source database server to the target database server.**Note:** Restoring to a new target will present new disks for data, active log and log backup volumes. Existing disks will remain attached to Compute Engine instances. If not needed, the user should detach and delete those disks.

**Options**

     * **Project name** , **Region** , and **Zone** : 
       * If you are restoring back to the source: All fields are pre-populated with the source value of protected SAP HANA instance and are immutable.
       * If you are restoring to a new target: To recover to a new target, select the project, region and zone of the instance that you want to recover the HANA database to.
     * **Instance Name** : 
       * If you are restoring back to the source: The source Compute Engine instance is selected and immutable.
       * If you are restoring to a new target: Eligible Compute Engine instances (HANA nodes) will be available to choose under the drop-down. Select the node for restore from the drop-down.
     * **Label** : Optionally, enter a unique name to be associated with this mount.
     * **Included Tenant Databases** is informational only, showing the list of tenant databases under backup image.
     * **Replace Original Application identity** : This option is only available when restore is performed to a new host on the same backup/recovery appliance where the backup was originally generated. 
       * **Yes** : This replaces the original application with the restored one, which will carry the same application ID, jobhistory, backup images, and backup plan as the original application.
       * **No** : This won't replace the original application. It will be discovered as a new application as part of the restore job.

**Application Options**

     * **Rollforward time** : Choose a date and time for a database protected with logs to recover to the required point in time.

**Note:** When recovering the most current backup, the rollforward control is set to the latest point in time. For a point-in-time recovery for older images, you must select the roll-forward time.
     * **TARGET DATABASE SID** : This is pre-populated with the protected database SID name and is immutable.

     * **SAP DB USER STORE-KEY** : This is pre-populated with the user store key during the backup. A new userstore key can be specified with a privileged username and password that was available during backup. This new userstore key will be created and will be used for recovery.

       * If the username and password are provided with the existing userstore key, then the userstore key will be recreated with this username and password. The validation will only be done after the systemdb recovers. The tenant recovery may fail if the username or password is not valid or or does not contain the right privilege and or not available as part of the backup image.
       * If a new userstore key with username and password is specified, then the userstore key will be created with the specified userstore key name and username and password. The validation will only be done after the systemdb recovery. The tenant recovery may fail if the username or password is not valid or or does not contain the right privilege or is not available as part of the backup image.
       * If no userstorekey, username, and password are passed, then during the precheck, validation will occur to check if the userstorekey used during backup exists on the target server. The precheck fails if the userstorekey used during backup is not found. Tenant recovery may fail if the username or password is not valid or or does not contain the right privilege or is not available as part of the backup image.
       * If no userstorekey is passed, but username and password are provided, then the userstorekey used during backup will be recreated with the credentials passed on the target server. The tenant recovery may fail if the username or password is not valid or or does not contain the right privileges or is not available as part of the backup image.

**Mapping Options**

     * **DATA Volume Mount Location** : This is prepopulated with the source device path and disk type where the HANA data volume is mounted.
     * **Log Volume Mount Location** : This is prepopulated with the source device path and disk type where the HANA active log volume is mounted.
     * **Log backup Volume Mount Location** : This is prepopulated with the source device path and disk type where the HANA archive log backup volume is mounted.

       * **Device Path** : Immutable for restore back to source. This can be changed during restore to a new target.

**Note:** The hyphen special character "-" (ex: data-1) is not supported in the device mount location.
       * **Disk Type:** Mutable for restore back to source. This can be changed during restore back to source or to a new target. The disk type lets you select the type of underlying block storage that is used for the recovered data from the backup images.

**Restore Custom HANA Configuration**

The backup image captures customer-specific configuration settings (.ini files that have been changed from the default). You can choose to restore custom configuration settings captured at the time of backup.

Restore Custom HANA Configuration requires the database user configured in the user store key to have DATABASE ADMIN and INIFILE ADMIN privileges.

**Restore an encrypted backup on Persistent Disk**

Restore back to the source: Restoring to the source system succeeds if the encryption keys used for the latest backup match the current keys on the source. If the encryption keys have been modified, then before initiating the restore job you must create a configuration file as follows.

Restore to a new target: The simplest way is to clone the source Compute Engine instance to a new target. This will have the same configuration as the source instance and no additional prerequisites are required.

If the source database server cloning is not feasible, then create a configuration file as follows and confirm all prerequisites listed in the restore section are met.

**_Create a configuration file_**

If the encryption keys used for the latest backup no longer match the current keys on the source server, you must import the encryption keys during the recovery process. This requires a configuration file.

Create the config file `DB_DETAILS.lst` with read permission 400 on the SAP HANA server under `/hana/shared`. Enter the encryption password with the tenant name as follows:

`<HANA SID> <TENANT NAME> '<PASSWORD>'`

Example: For "S82" HANA instance
    
    S82    SYSTEMDB     'aaaaaaaa'
    S82        S82      'aaaaaaaa'
    

Make sure to provide the config file (/hana/shared/DB_DETAILS.lst)

  4. Click the pre-flight check.

     * If the pre-flight check fails, fix the issue and resubmit the Pre-Flight Check.
     * If the pre-flight check is successful, click **Submit** to submit the restore job.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
