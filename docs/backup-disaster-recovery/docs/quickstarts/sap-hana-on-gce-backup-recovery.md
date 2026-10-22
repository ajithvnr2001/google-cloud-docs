---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/sap-hana-on-gce-backup-recovery/
title: Protect and recover SAP HANA databases on Compute Engine instances in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:43.230644+00:00
---

# Protect and recover SAP HANA databases on Compute Engine instances in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/sap-hana-on-gce-backup-recovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Protect and recover SAP HANA databases on Compute Engine instances in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

## Protect the SAP production environment against data loss, errors, and corruption

SAP HANA is one of the most popular enterprise databases in the world. It's unique because it runs in-memory, so it can return query results very quickly. Many enterprises use SAP HANA for their mission critical applications. As can happen with any database, SAP HANA is susceptible to corruption, accidental deletion, or even security threats such as ransomware attacks. Backup and DR lets you efficiently and securely back up and recover your production systems.

For an introduction to how you use Backup and DR to protect your HANA databases, see [Backup and DR for SAP HANA](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-hana).

**Note:** SAP HANA Scale-Out isn't supported for backup to Persistent Disk snapshots.

## Deploy Backup and DR first

Before you begin, you must read and complete the following procedures:

  * [Plan a Backup and DR deployment](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-plan)

  * [Prepare to deploy Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-prep)

  * [Deploy Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-guide)




## See how Backup and DR works

Then see how Backup and DR works by going through [Get started with Backup and DR: protect and recover a Compute Engine instance](https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/gce-instances-backup-recovery).

## Prepare SAP HANA instances for backup

Before you can back up your SAP HANA instances, review the following preparation steps.

### Prerequisites

  * All the configured services—see SAP Note 1697613 and SAP Note 1649519— such as `nameserver` and `indexserver` must be running. You can check this in the **Overview of SAP HANA studio** > **Operational State** > Confirm all services are started.
  * To allow the Backup and DR agent to perform host-side operations, use an SAP HANA `hdbuserstore` key instead of a username and password to communicate with the HANA database using the SAP HANA secure userstore.
  * Database `log_mode` must be **normal** under the HANA Studio configuration tab.
  * All SAP HANA servers (Compute Engine) that have HANA data to be protected by Backup and DR must have been onboarded to Backup and DR
  * All SAP HANA servers (Compute Engine) that have HANA data to be protected by Backup and DR must have the Backup and DR agent installed.
  * SAP HANA log backup recommendation:

    * Make sure to set the SAP HANA log backup path as the basepath_logbackup and basepath_catalogbackup in global.ini
    * Don't use the SAP HANA log backup mount to store files other than HANA archive log backup
    * By default log purge runs with every database backup. This achieves the best recovery RTO.
  * To back up SAP HANA using the Persistent Disk snapshot capture method, the configuration must follow these criteria:

    * /hana/shared, and /usr/sap shouldn't be shared with data, log, or log backup volume groups or disks.
    * Log backups (/hana/logbackup) should have a separate disk configured, and they shouldn't be shared with data volume or active log volume or with HANA binary. /hana/data and /hana/log can reside on the same volume.

**Note:** If production log retention is set then purge will run based on the **Retention of production db logs in hour** setting under **[Application Details& Settings](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-sap-hana-pd)**. Size the HANA archive log backup disk to store archives based on the production log retention setting.**Note:** If any of these prerequisites can't be met, then use the protection methods for SAP HANA detailed in [Backup and DR for SAP HANA](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-hana).

### Configure the HANA userstore key

Use the following instructions to configure the HANA userstore key:

  1. Create the database backup user from HANA Studio.
  2. Get the instance and SQL port numbers.
  3. Create the SAP HANA hdbuserstore key for system DB backup users.



#### Step 1: Create the database backup user from HANA Studio

Choose a database username based on the company's standard. Make sure to create this user account under `SYSTEMDB`.

  1. Create the user under `SYSTEMDB`: 
     * From SAP HANA Studio SYSTEMDB, go to **System** > **Security** > **Users** > **New User**.
     * Assign a username and a password.
     * Set **Force password change on next logon** to **No**.
     * HANA 2.0 (SPS01 to SPS04): Click the **System privilege tab** and assign privileges by selecting the following: 
       * **Backup admin**
       * **Catalog read**
       * **Database admin**
       * **Database start**
       * **Database stop**
     * HANA 2.0 (SPS05 and later): Click the **System privilege tab** and assign privileges by selecting the following: 
       * **Backup admin**
       * **Catalog read**
       * **Database backup operator**
       * **Database recovery operator**
       * **Database admin**
       * **Database start**
       * **Database stop**
  2. Deploy the newly created system user by clicking the **green arrow**.



#### Step 2: Get the instance and SQL port numbers

You need the HANA instance and SQL Port numbers for system DBs.

To get the instance and SQL port numbers from HANA 2.0 studio:

  1. Go to **System**.
  2. Click the **Landscape** tab.
  3. Click the **Services** tab.
  4. Under the **Service** column, navigate to the `nameserver`.
  5. Get the value of SQL port. The instance number is the second and third digits of the SQL port number.



#### Step 3: Create the SAP HANA `hdbuserstore` key for system DB backup users

Use this naming convention for the userstore key name:

For SYSTEMDB, set the key name to (`Database backup username`). For example, for database backup username (`Actbackup`), set `SYSTEMDB-key_name- (`ACTBACKUP`)`.

**Procedure**

  1. Connect to the HANA database system using SSH and log into (sid)adm: `su - (sid)adm`
  2. Change directory: `cd exe`
  3. Create entries in hdbuserstore using command `hdbuserstore`: `./hdbuserstore SET (key_name) (host name):(port) (DB_user_name) (DB_user_password)`

In this example: ``./hdbuserstore SET ACTBACKUP s4hana:30013 ACTBACKUP (DB_user_password)`

  4. Check the keystore: `./hdbuserstore list`




### Set up the log mode and log backup in HANA Studio

Using the HANA Studio set the HANA log mode and log backup location for Backup and DR to take backups of HANA DB transaction logs:

  1. In SAP HANA HDB studio, make sure log backup is set correctly under **DATABASE (SYSTEMDB FOR HANA 2.0)** > **Backup** > **Configuration** page: 
     * Destination type is **File**.
     * Destination is set to a local file system mount path.
     * Backup interval is set to **required RPO**.
     * Automatic log backup is enabled.
     * Database `log_mode` must be set to **normal**.
  2. Check under Database configuration: DATABASE (SYSTEMDB FOR HANA 2.0) > Configuration page. In the filter, type **basepath**.
  3. Verify that `basepath_logbackup` is set correctly: 
     * Set the `basepath_catalogbackup` to the same as `basepath_logbackup`.
     * Open the `basepath_catalogbackup` edit page and set the **New value** to the same as `basepath_logbackup`. Click **Save**. This ensures the backup of the catalog with log backup for point in time recovery.
  4. On the HANA database server, run the re-config for the values to take effect: `hdbnsutil -reconfig`.



## About this quickstart exercise

This exercise guides you through the steps of discovering and protecting an SAP HANA database running in a Compute Engine instance, and finally mounting a fully-functional new HANA database from the backup image to a new location.

  1. Install the Backup and DR agent on the Compute Engine
  2. Create a backup plan for the SAP HANA database
  3. Discover and protect SAP HANA databases
  4. Mount an SAP HANA backup image as a standard mount
  5. Restore SAP HANA databases



## Install the Backup and DR agent on the host

The Backup and DR agent connects the Compute Engine instance to the backup/recovery appliance. To install the Backup and DR agent, see [Install the Backup and DR agent on a Linux host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/linux-agent).

## Create a backup plan for the SAP HANA databases

The backup plan is how Backup and DR schedules backup jobs and manages storage for the backup images.

You created a backup plan for the Compute Engine instance in [Get started with Backup and DR: protect and recover a Compute Engine instance](https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/gce-instances-backup-recovery). Now you must create a backup plan for the HANA database that is running inside the Compute Engine instance. See [Create and apply a policy template](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template).

### Advanced Policy Settings specific to HANA databases on Compute Engine Persistent Disks

The policy template needs these specific advanced settings.

  1. In the appliance management console under **Backup Plans** , select **Templates**.
  2. Select the policy template for the HANA database and click **Edit**.
  3. On the right-hand side under **Policies** , click the white arrow beside **Snapshot** , then click **Edit Policy**.
  4. At the bottom of the **Create/Edit Policy** section, click **Advanced Policy Settings**.
  5. Within the **Advanced Settings** dialog, find and set the following advanced settings:

**Snapshot location** : Select the region where the Persistent Disk snapshots are to be stored. By default, **Multi-regional** is selected (based on the source disk location). You can also change the snapshot storage location to a different region than the source disk region. When storing snapshots in a location that is different from the location of your source disk, the data travels over the network between those locations and might incur network fees. Snapshots incur the same fees as Cloud Storage egress. Learn more about the [Persistent Disk snapshot.](https://docs.cloud.google.com/compute/docs/disks/snapshots). To learn the pricing details, see [disk pricing](https://docs.cloud.google.com/compute/disks-image-pricing#disk).

**Snapshot type** : Select the Persistent Disk snapshot type to be used for SAP HANA backups. Snapshots incrementally back up data from Persistent Disks. During backups, a new snapshot is created to capture the current state of the Persistent Disk. This can later be used to create a new disk for mounts or restores. Compute Engine stores multiple copies of each snapshot across multiple locations with automatic checksums to ensure the integrity of your data. Learn more about the [Persistent Disk snapshot](https://docs.cloud.google.com/compute/docs/disks/snapshots). To know the pricing details, see [disk pricing.](https://docs.cloud.google.com/compute/disks-image-pricing#disk).

     * **Standard snapshot** : By default, the standard snapshot type is selected. Use the standard type if you want to retain the backups for less than 90 days.
     * **Archive snapshot** : Select the archive type if you want to retain backup images for a long duration. Note that the minimum billing period for the archive snapshot is 90 days irrespective of the retention period defined in the policy and that an archive type snapshot also has an additional retrieval charge if it is used in a mount or a restore job.

**Truncate (Purge) Log After Backup** : Specify whether to truncate (purge) the HANA archive logs after backup. When **Truncate Log after Backup** is enabled, HANA archive logs are truncated. By default archive purge runs with every database backup. Use the default to achieve best recovery RTO. If production log retention is set, then purge runs based on the **Retention of production db logs in hours** setting under **[Application Details& Settings](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-sap-hana-pd)**.

     * **Don't truncate/purge log after backup** : This is the default. In this mode the archive log won't be purged.
     * **Truncate/purge log after backup** : Select this option to enable archive log purge.

**Enable Database Log Backup** : Set this option to "Yes". The Enable Database Log Backup option allows the backup plan policy to backup a database and all associated transaction log files. The logs are backed up when the log snapshot job runs. When set to Yes, the related options are enabled.

**Note:** When using the Persistent Disk snapshot backup capture method, concurrent database and log backups are not supported; they will execute sequentially according to the backup plan.

**RPO** : Specify the database log backup in minutes. When Enable Database Log Backup is set to Yes, RPO defines the frequency for database log backup. Frequency is set in minutes and must not exceed the database backup interval. The smallest value that can be set (in minutes) is 15.

**Replicate Logs (Uses Streamsnap technology)** : Set this to **No**. This doesn't apply to SAP HANA Persistent Disk snapshot protection. This function is enabled (set to "Yes") by default. Not setting it to "No" will result in template creation error.

**Send logs to OnVault Pool** : Set this to **No**. This doesn't apply to SAP HANA Persistent Disk snapshot protection. This function is enabled (set to "Yes") by default. Not setting it to No will result in template creation error.

**Note:** **Replicate Logs (Uses Streamsnap technology)** and **Send logs to OnVault Pool** don't apply to SAP HANA Persistent Disk snapshot protection. These are both set to "Yes" by default. Set them to "No". If you don't set both of these to **No** , you will experience template creation errors.



## Discover and protect SAP HANA databases

**Note:** If you are protecting a HANA database that has already been added and that already has LVM backup images, then you must change the capture method from LVM to Persistent Disk. To do this, remove the existing LVM template protection and then apply a template with new Persistent Disk capture method.

To discover HANA databases on a Compute Engine instance and then protect them with Backup and DR, the Compute Engine instance hosting the SAP HANA database must be onboarded before you can onboard the SAP HANA database application. You onboarded a Compute Engine instance in [Get started with Backup and DR: protect and recover a Compute Engine instance](https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/gce-instances-backup-recovery).

  * If this is the instance that hosts the SAP HANA database, then continue to the next section.
  * If you must onboard a different Compute Engine instance to Backup and DR see [Discover and protect Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-compute-engine).

**Note:** For SAP HANA snapshot backups, only SSFS encryption keys are included for backup and imported during database restoration; LSS keys are neither backed up nor imported through this process.

### Onboard the SAP HANA databases from the App Manager

**Note:** Successful Compute Engine onboarding provides the link to **SAP HANA onboarding wizard** (step 3 below).

To discover and protect the HANA database applications:

  1. Select **Add Application** from the appliance management console's **App Manager > Applications page**.
  2. Select **SAP HANA** in the **Add Application wizard**.
  3. Follow the wizard: 
     * Select the database to manage from the **Select** section.
     * In the Manage section, apply the policy template and the resource profile that you created in Create a backup plan for the SAP HANA databases.
  4. Under **Application Settings** in the **Configure** section, set the **Configure backup options** : 
     * **HANA DB user store key** : This is the SAP HANA hdbuserstore key for the system database created earlier. This field is mandatory.
     * **Backup capture method** : choose **Use Persistent Disk Snapshot**.
     * **Retention of production DB logs in hours** : At the end of every log backup, the log purge will run and delete all the logs older than the number of hours specified here. For example if the number of hours specified is 4 hours then all the logs older than ((the start time of the log backup) - (4 hours)) will be purged. The default value is 2 hours.
     * **Retention of production catalog in days** : This is the retention of catalog metadata in days. The HANA catalog metadata (m_backup_catalog table) will be purged of logs older than the specified number of days. For example if the number of days specified is 14 days then data from HANA catalog will be purged older than ((the current day) - (14 days)). The default value is 7 days.
  5. Click **Save** > **Next** , then click **Finish**.
  6. You can see the database in the App Manager Applications list with a green shield indicating that the backup plan has been applied.



## Set application details & settings

After [setting the staging disk format and backup method](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/backup-method-staging-disk-sap-hana), you must enter the details and settings you want to apply to your backup plans:

  1. In the appliance management console, go to **App manager** and click **Applications**.

  2. Right-click the HANA database and click **Manage backup configuration**.

  3. At the top of the page, click **Details & Settings**.

  4. In the **Application details & settings** window, configure database settings based on your host type.

     * **Backup Capture Method** : persistent disk
     * **HANA DB User Store Key** : This is the SAP HANA hdbuserstore key for the system database created earlier. This field is mandatory.
     * **Retention of production DB logs in hours** : At the end of every log backup, the log purge will run and delete all the logs older than the number of hours specified here. For example if the number of hours specified is 4 hours then all the logs older than ((the start time of the log backup) - (4 hours)) will be purged. The default value is 2 hours.
**Note:** Log purge retention values less than 24 hours cause the creation of multiple temporary log backup disks during restore and mount operations (restore, unmount-delete, or forget active mount jobs). These additional disks are automatically managed and they are deleted once the operation is completed.
     * **Retention of production catalog in days** : This is the retention of catalog metadata in days. The HANA catalog metadata (m_backup_catalog table) will be purged of logs older than the specified number of days. For example if the number of days specified is 14 days then data from HANA catalog will be purged older than ((the current day) - (14 days)). The default value is 7 days.
  5. Click **Save changes**.




### Protect HANA (HA) 1+n

HANA 1+n is always discovered as a cluster application containing all node details in the metadata. After application discovery the application has the cluster host as (HANA sid name)_cluster_(site id)_(HANA hardware id). For example, if sr1 is the HANA instance, then the application name is sr1 and the hostname is sr1_cluster<_…> in the App Manager Applications list.

It is a good idea to run a force discovery after any changes to cluster node configuration—such as after adding or deleting a node from the cluster. If a node is removed or added after discovery and protection, the configuration doesn't update automatically in Backup and DR metadata, and might cause backup issues.

**Note:** With the failover of the HANA database from primary to secondary, the next database backup is a full snapshot that contains all the data on the Persistent Disk. Subsequent database backup snapshot will contain any new data or modified data since the first snapshot and starts a new chain.**Note:** If the secondary node or database is down during backup, Persistent Disk details of the secondary node won't be saved. To perform restore using this image, you must detach and delete data, log, and log backup disks from the secondary node before restoring the image.

**Prerequisites for protecting HANA HA (1+n)**

  * All SAP HANA servers (Compute Engine) of the SAP HANA cluster must have been onboarded to Backup and DR.
  * All SAP HANA servers (Compute Engine) of the SAP HANA cluster must have the Backup and DR agent installed.
  * All SAP HANA servers (Compute Engine) of he SAP HANA cluster must have a secret applied under **App Manage** > **Manage** > **Host** > **Backup and DR Backup and DR agent Settings** > **Secret**.
  * Ports need to be opened on the hosts to allow communication on port 5106. This requires an ingress firewall rule where the backup/recovery appliance is the source, the host running the Backup and DR agent is the target and the target port is 5106. Also, there is no need to add port 5106 to the default ingress rule created for the backup/recovery appliance, as this specifies the backup/recovery appliance as the target.



## Mount an SAP HANA backup image as a standard mount

A standard mount provides the backup image disk of data, active log and archive log volume to the specified target. You can mount snapshot backup images of an SAP HANA database as a standard mount for:

  * Any manual operation or
  * To Mount a backup for an integrity check



### Pre checks during mount

  * Connector connectivity status: Verify that the Backup and DR agent is installed and secret is applied for host connectivity between the backup/recovery appliance and the Backup and DR agent.
  * Mount locations specified are available for mount operation.
  * HANA binary is installed
  * Verify that the HANA sid the same as the source isn't up and running on the target.
  * The HANA instance version is greater than 2.0SP05.
  * Permission Check On Source and target Project for the Cloud Storage service



### Mount the backup

Use these instructions to mount a backup:

  1. Right-click the protected database from the **App Manager Applications** list, and select **Access**.

**Note:** You can use the **Managed Backup Plan** status filter to show only protected databases.
  2. Select a snapshot image and choose **Mount**.

  3. On the **Mount** page:

     * **Project name** , **Region** , and **Zone** : Select the project, region, and Zone of the instance to which you want to mount the HANA database image.
     * **Instance Name** : Eligible Compute Engine instances (HANA nodes) will be available to choose under the drop-down. Select the node for mount from the drop-down.
  4. Optionally, enter a unique name associated with the mount in the **Label** field.

  5. **INCLUDED TENANT DATABASES** is informational only, showing the list of tenant databases under backup image.

  6. Under **Mapping Options** :

     * **DATA Volume Mount Location** : This is prepopulated with the source device path and disk type where the HANA data volume is mounted.
     * **Log Volume Mount Location** : This is prepopulated with the source device path and disk type where the HANA active log volume is mounted.
     * **Log Backup Volume Mount Location** : This is prepopulated with the source device path and disk type where the HANA archive log backup volume is mounted.

       * **DEVICE PATH** : is pre-populated with the source DEVICE PATH. Provide a path that isn't in use at the selected target and that you want to use to mount the snapshot image of DATA VOLUME, LOG VOLUME, and LOG BACKUP VOLUME on the target server.
**Note:** The hyphen special character "-" (for example: data-1) isn't supported in the device mount location.
       * **DISK TYPE** : is pre-populated with the source DISK TYPE value. You can change the disk type by selecting the different type from the drop-down value.
  7. **SNAPSHOT DATA INTEGRITY CHECK** : By default the value is set to **true**. If you don't want to run the check, set this to false by clicking the toggle button. This tool will run the SAP HANA persistence checking tool `hdbpersdiag` API with the 'check all' option. This will verify the healthy state of data and active log volumes from the mounted snapshot image. If the precheck discovers any corruption in the image, then the mount job fails with a descriptive error message.

The result of the integrity check is available under `/var/act/log/(HANA sid)_dataintegrity_check.log` and `/usr/sap/(HANA sid)/HDB00/(host name)/trace/localclient.*.trc`.

  8. Click **Pre-Flight check**. This validates the required options on the target server for a successful mount. If the pre-flight check fails, the pre-flight will show which check failed so you can correct it and rerun the pre-flight.

  9. Click **Submit**. You can go to the **Job Monitor** to view the progress and details of the job.

**Note:** The integrity check is detailed in Mount a backup for an integrity check.



### Unmount the mounted backup snapshot image

To remove or keep the disk after a successful mount:

  * Go to **Application** > **Access** page and select the image used for mount.
  * On the Access page under the **Current active mount** drop-down, select either: 
    * **Unmount & Delete**: Choose this option to unmount the mount point, detach the disk and delete the disk from the target server.
    * **Forget Active Mount** : Choose this option to leave the disk attached and mounted, but remove the metadata from Backup and DR. You will have to use the Google Cloud console to remove this image from the target instance after this operation is finished.



### Mount a backup for an integrity check

This tool runs the SAP HANA persistence checking tool, `hdbpersdiag`, with the 'check all' option to verify the healthy state of data volumes from the mounted snapshot image. If the precheck discovers any corruption in the image, then the mount job fails with a descriptive error message.

#### Clone the source database server as a new target server for data integrity check

Clone the source database server and then mount the backup to the new target. This will have the same configuration as the source and no additional prerequisites will be needed. This is the best practice.

#### Prerequisites for data integrity check mount if clone is impossible

If the source database server cannot be cloned, then make sure that these prerequisites are set on the new target server:

  * The HANA binary must be configured on the target server. The HANA version must be equal or greater than the source HANA instance.
  * Be sure that the target HANA configuration has the same tenant DBID configured as source tenant database DBID.
  * If the source HANA database data volume and log volumes are encrypted using HANA database encryption then you must create a config file with the encryption key credentials on the target HANA server. Follow these steps on the target HANA server:

    1. Create a config file DB_DETAILS.lst under /hana/shared.
    2. Provide read permission 400 to the config file (/hana/shared/DB_DETAILS.lst).
    3. In the config file (/hana/shared/DB_DETAILS.lst) enter the password with the tenant name:
           
           HANA SID Tenant name 'password'
           

For example, for a HANA instance with SID "S82", DB_DETAILS.lst would contain these lines:

`S82 SYSTEMDB 'xxxxxxxx'`

`S82 S82 'xxxxxx'`




#### Can I mount back to the source for integrity check?

This is not recommended. Mounting back to source while the database is running may corrupt the data block due to the same VG name of the data volume.

If you must mount back to the source, make sure to shut down the HANA instance at the source before performing the mount operation.

#### Integrity check results

The result of the integrity check is available under `/var/act/log/(HANA sid)_dataintegrity_check.log` and `/usr/sap/(HANA sid)/HDB00/(host name)/trace/localclient.*.trc`.

## Restore SAP HANA databases

Before you can restore an SAP HANA database from a backup image, review these license requirements.

### License requirements and impact on restore

  * The license key for an SAP HANA database is based on the system ID and the hardware ID. After a recovery, an SAP HANA license key becomes invalid if the SID or hardware ID has changed.
  * During recovery, a temporary license key is installed automatically if the backup used for recovery has a permanent license, which is still valid. You can work with the automatically installed temporary license for up to 90 days. During this time, you need to apply to SAP to have the license from the source database transferred to a new license key. You then need to install the new license key in the recovered SAP HANA database.
  * If the backup that was used for recovery only had a temporary license, the database is in lockdown mode immediately after recovery.
  * Source database with temporary license These are backups taken with temporary licenses. 
    * Restore back to source: It is 90 days from the time of database creation and the database is in lockdown mode.
    * Restore to the new target: It fails as SAP temp license doesn't allow the restore to a new target.
  * Source database with permanent license These are backups taken with permanent licenses. 
    * Restore back to source: No issue.
    * Restore to the new target: It has a 90 days trial license. Backups succeed but you can't use the new backup to restore.



### SAP references

  * https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/2.0.02/en-US/19a0f5a85685453080f00087bb9b9c98.html
  * https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/2.0.02/en-US/bddd0b28bb571014bd9592d247dcd403.html



### Preflight check

Before submitting the restore procedure, preflight checks validate the required prerequisites for a successful database restore.

  * HANA SID: HANA is configured on the target node with the same HANA SID name.
  * Verify Database Status: HANA Database isn't up and running.
  * Config file: Config file global.ini is available on target server
  * Log backup path: Log backup path is set under global.ini
  * HANA Version: Target HANA version is the same as the source HANA version.
  * USERSTOREKEY: Provided userstore key exists on target or a valid privileged username and password is specified which exists at the time of backup.
  * For restore to a new target, verify the Mount point specified under the mapping option isn't used or mounted at the target server.
  * Verify Data & Log Volume Details: If the Data & Log Volume path in the config file (global.ini) is defined other than the chosen device path under mapping option then the config file (global.ini) will be updated with the path chosen under the mapping option.
  * Node Status:

    * Scale-up and standalone config: Target HANA server is up and available
    * HANA HA (1+n) config: Validates that replication is disabled. Replication needs to disabled before restore can be initiated. Post restore replication needs to be reconfigured. Restoring to any node of a HANA HA (1+n) cluster results in creating a standalone application on the selected target host. User has to explicitly configure the cluster back as needed and discover the application appropriately.
**Note:** To be sure SAP HANA replication cluster protection works correctly, every node in the cluster must be able to resolve the hostnames of all other nodes in the cluster.



### Restore an SAP HANA database

  1. From the **App Manager Applications** list, right-click the database and select **Access**.
  2. Select the backup image to recover and choose **Restore**.
  3. On the **Restore** page the options are:

     * **Restore back to source** : All fields are pre-populated with the source value of protected SAP HANA instance and are immutable except application options.
     * **Restore to new target** : All fields are pre-populated with the source value of protected SAP HANA instance and are mutable.

**Note:** Before restoring an SAP HANA database to a new target server, if the DATA, Active LOG and Log backup volumes are encrypted by HANA encryption, then import the encryption keys from the source database server to the target database server.**Note:** Restoring to a new target will present new disks for data, active log and log backup volumes. Existing disks will remain attached to Compute Engine instances. If not needed, the user should detach and delete those disks.  
Restoring to the source will delete the existing data, active log, and log backup volumes. It will then create new disks from the persistent disk snapshots and make them available to the server.

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

       * If the username and password are provided with the existing userstore key, then the userstore key will be recreated with this username and password. The validation will only be done after the systemdb recovers. The tenant recovery might fail if the username or password isn't valid or or doesn't contain the right privilege and or not available as part of the backup image.
       * If a new userstore key with username and password is specified, then the userstore key will be created with the specified userstore key name and username and password. The validation will only be done after the systemdb recovery. The tenant recovery might fail if the username or password is not valid or or doesn't contain the right privilege or isn't available as part of the backup image.
       * If no userstorekey, username, and password are passed, then during the precheck, validation will occur to check if the userstorekey used during backup exists on the target server. The precheck fails if the userstorekey used during backup isn't found. Tenant recovery might fail if the username or password isn't valid or or doesn't contain the right privilege or isn't available as part of the backup image.
       * If no userstorekey is passed, but username and password are provided, then the userstorekey used during backup will be recreated with the credentials passed on the target server. The tenant recovery might fail if the username or password isn't valid or or doesn't contain the right privileges or isn't available as part of the backup image.

**Mapping Options**

     * **DATA Volume Mount Location** : This is prepopulated with the source device path and disk type where the HANA data volume is mounted.
     * **Log Volume Mount Location** : This is prepopulated with the source device path and disk type where the HANA active log volume is mounted.
     * **Log backup Volume Mount Location** : This is prepopulated with the source device path and disk type where the HANA archive log backup volume is mounted.

       * **Device Path** : Immutable for restore back to source. This can be changed during restore to a new target.

**Note:** The hyphen special character "-" (ex: data-1) isn't supported in the device mount location.
       * **Disk Type:** Mutable for restore back to source. This can be changed during restore back to source or to a new target. The disk type lets you select the type of underlying block storage that is used for the recovered data from the backup images.

**Restore Custom HANA Configuration**

The backup image captures the customer-specific configuration settings (.ini files that have been changed from the default). You can choose to restore custom configuration settings captured at the time of backup.

  4. Click the pre-flight check.

     * If the pre-flight check fails, fix the issue and resubmit the Pre-Flight Check.
     * If the pre-flight check is successful, click **Submit** to submit the restore job.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
