---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-sap-hana-scaleout/
title: Add an SAP HANA database host and discover and protect its databases in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:44.184189+00:00
---

# Add an SAP HANA database host and discover and protect its databases in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-sap-hana-scaleout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)



Send feedback 

#  Add an SAP HANA database host and discover and protect its databases in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Before you can protect an SAP HANA database, you must [onboard the Compute Engine instance](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-compute-engine).

**Note:** This information is for SAP HANA scale-out instances. For scale-up and HA 1+1 configurations, see [Backup and DR for SAP HANA](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-hana).

## Discover and protect the SAP HANA database application

**Note:** Use of a third-party backup in between Backup and DR backups is not recommended, because of the following:

  * LVM backups fail for any third party backup backint setup
  * Recovery is compromised due to break in the recovery chain
  * A Full+Incremental backup can get orphan incrementals causing recovery issues.

**Note:** The SAP HANA `basepath_logbackup` path should be set only in the SYSTEM DB global.ini file. Don't specify it in each tenant level global.ini file.

Use the following instructions to discover and protect SAP HANA scale-out instances:

  1. Select **Add Application** from the appliance management console's **App Manager** > **Applications** page.

  2. Select **SAP HANA** in the **Add Application** wizard.

  3. Follow the wizard:

     * Select the database to manage from the **Select** section.

     * Apply the policy template and the resource profile in the **Manage** section, you created these in [Define policy templates and resource profiles](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/configure-sap-backupmethod).

  4. Click **Application Settings** in the **Configure** section.

  5. Select the **Backup Capture Method** from the **Application Settings** window. The method is based on your needs and the information in [Protect the SAP production environment against data loss, errors, and corruption](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-hana-scaleout).




In the **Application Settings** tab, you can change application-specific settings. Be sure to address the following:

  * **HANA DB user store key** : This is the SAP HANA hdbuserstore key for the system database created earlier. This field is mandatory.

  * **Percentage of reserve space in volume group** : This is needed for volume level backup to determine the required amount of temporary free space in LVM volume group for snapshots. The recommended value is 20%.

  * **Backup capture method** :

    * **Use Persistent Disk Snapshot** : This is the standard Persistent Disk snapshot used by Compute Engine. Select this for HANA databases running in a Compute Engine instance. If you can use this method, see [](https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/sap-hana-on-gce-backup-recovery).

    * **Use volume level backup** : Use volume level LVM snapshots with CBT on Linux to a block-based staging disk. This option uses the SAP HANA savepoint API to enable you to create incremental-forever backups. This requires the HANA database data and log volume to be LVM-managed. If you are using NFS protocol staging disks, then you cannot use volume-level backups.

    * **Use Full+Incremental backup** : This is the older file-based backup and recovery. This "file dump" method does not support creation of virtual databases. You can select this for block and for NFS staging disks. This method only supports older Backint backup and physical recovery.

**Note:** There are two protocols for presenting the backup staging disk to the host—block-based and NFS. For scale-out backint or file-based backup, always use the NFS option for staging disk.
  * **Retention of production DB logs in hours** : At the end of every log backup, the log purge will run and delete all the logs older than the number of hours specified here. For example if the number of hours specified is 4 hours then all the logs older than ((the start time of the log backup) - (4 hours)) will be purged. The default value is 2 hours.

  * **Retention of production catalog in days** : This is the retention of catalog metadata in days. The HANA catalog metadata (m_backup_catalog table) will be purged of logs older than the specified number of days. For example if the number of days specified is 14 days then data from HANA catalog will be purged older than ((the current day) - (14 days)). The default value is 7 days.


**Note:** All required properties are marked with a red asterisk. The **Apply Backup Plan** option at the bottom of the dialog is disabled until all required property values are added, then click **Save Changes**.

  1. Click **Save** > **Next** , then click **Finish**.

  2. You can see the database in the **App Manager Applications** list with a green shield indicating that the backup plan has been applied.


**Note:** The application cannot be captured until the scheduled job runs according to the hours of operation defined in the backup template. For example, if at 10:00 (UTC) you assign a template that has hours of operation from 02:00 (UTC) to 05:00 (UTC), then the first job cannot start until the appliance has an available job slot at 02:00 (UTC) of the following day. To run a job immediately, perform an [on-demand capture](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs#run).

## Back up HANA 1+n and HANA scale-out databases

This section includes information about protecting HANA 1+n and HANA scale-out.

### Protect HANA 1+n

To protect a HANA 1+n replication cluster as a single application, after application discovery the application has the cluster host as sid `name_cluster`. For example, if sr1 is the HANA instance, then the application name is sr1 and the hostname is sr1_cluster in the **App Manager Applications** list.

The HANA log backup destination must be shared between two nodes. When failover occurs, the database and log backup automatically fails over to the current primary, and log backups are performed from the current primary, capturing the last logs from the old primary as well as new logs from the new primary. Follow the preparation steps in [Prepare your SAP HANA databases for protection](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-hana).

HANA 1+n is always discovered as cluster application containing all node details in the metadata. After application discovery, the application has the cluster host as (HANA sid name)_cluster_(site id)_(HANA hardware id). For example, if sr1 is the HANA instance, then the application name is sr1 and the hostname is sr1 _cluster <_…> in the App Manager Applications list.

It is a good idea to run a force discovery after any changes to cluster node configuration—such as after adding or deleting a node from the cluster. If a node is removed or added after discovery and protection, the configuration is not updated automatically in Backup and DR metadata, and may cause backup issues.

**Note:** With the failover of the HANA database from primary to secondary, the next database backup is a full snapshot that contains all the data on the Persistent Disk. Subsequent database backup snapshots will contain any new data or modified data since the first snapshot and starts a new chain.

#### Prerequisites for protecting SAP HANA 1+n instances and databases

Before protecting SAP HANA instances, ensure the following:

  * All SAP HANA servers or Compute Engine instances of the SAP HANA cluster must have been onboarded to Backup and DR.
  * All SAP HANA servers or Compute Engine instances of the SAP HANA cluster must have the Backup and DR agent installed.
  * All SAP HANA servers or Compute Engine instances of the SAP HANA cluster must have a secret applied under **App Manage** > **Manage** > **Host** > **Backup and DR Agent Settings** > **Secret**.

  * If hosts have virtual IPs configured, add only the virtual IP and hostname of the host during discovery.

  * The Backup and DR agent must be installed on all nodes.

  * Ports need to be opened on the hosts to allow communication on port 5106. This requires an ingress firewall rule where the backup/recovery appliance is the source, the host running the agent is the target and the target port is 5106. There is no need to add port 5106 to the default ingress rule created for the appliance, as this specifies the appliance as the target.

  * HANA log backup location must be set on shared—NFS.


**Note:** Activate logical volume manager change block tracking on all the nodes of SAP HANA scale-out cluster by running `/opt/act/cbt/bin/cbt_activate.sh` on the command line as a root user. Verify that logical volume manager change block tracking is activated by running `pgrep cbt`—this should return two processes running for change block tracking.

### Protect HANA scale-out

![SAP HANA scale-out](https://docs.cloud.google.com/static/backup-disaster-recovery/docs/images/backup/sap-hana-scaleout-concept.png)

#### Prerequisites for protecting SAP HANA scale-out

Before protecting SAP HANA scale-out, be sure that the following is complete:

  * If hosts have virtual IPs configured, add only the virtual IP and the associated hostname of the host during discovery.
  * The Backup and DR agent must be installed on all nodes.
  * Ports need to be opened on the hosts to allow communication on port 5106. This requires an ingress firewall rule where the backup/recovery appliance is the source, the host running the agent is the target and the target port is 5106. Also, there is no need to add port 5106 to the default ingress rule created for the appliance, as this specifies the appliance as the target.
  * For backint file based—Full+Incremental—backup, the HANA log backup location must be set to shared—NFS. See [Add the host to the appliance management console](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/otherdb-add-host).
  * For storage snapshot protection

    * Data and log volume are non-shared across all nodes
    * Data and log volumes are logical volume manager managed
    * Ensure mnt000* directories exist on the local mount points to identify the primary and secondary nodes
**Note:** The discovered HANA instance shows up after the application list with: Application (HANA sid name): Hostname and Friendly path (HANA sid name)_cluster(site id)_(HANA hardware id).

Follow the setup procedures in [Prepare your SAP HANA databases for protection](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-hana).


**Note:** Activate logical volume manager change block tracking on all the nodes of SAP HANA scale-out cluster by running `/opt/act/cbt/bin/cbt_activate.sh` on the command line as a root user. Verify that logical volume manager change block tracking is activated by running `pgrep cbt`—this should return two processes running for change block tracking.

## Backup and DR documentation for SAP HANA scale-out

This page is one in a series of pages specific to protecting and recovering SAP HANA scale-out instances with Backup and DR. You can find additional information in the following pages:

  * [Backup and DR for SAP HANA scale-out](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-hana-scaleout)
  * [Prepare SAP HANA scale-out instances for backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-sap-hana)
  * [Add an SAP HANA scale-out host, and discover and protect its databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-sap-hana-scaleout)
  * [Configure staging disk format and backup method for SAP HANA scale-out](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/backup-method-staging-disk-sap-hana-scaleout)
  * [Set application details and settings for SAP HANA scale-out instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-sap-hana-scaleout)
  * [Back up HANA 1+n and HANA scale-out databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/back-up-sap-hana-scaleout)
  * [Restore and recover SAP HANA scale-out instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-sap-hana-scaleout)
  * [Mount an SAP HANA scale-out backup as a standard mount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sap-hana)
  * [Mount an SAP HANA scale-out backup as a virtual database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sap-hana-virtualdb)
  * [Mount and migrate an SAP HANA scale-out backup for instant recovery to any target](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-and-migrate-sap-hana)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
