---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-overview/
title: Overview of restore operations \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:15.685297+00:00
---

# Overview of restore operations  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Overview of restore operations Stay organized with collections  Save and categorize content based on your preferences. 

The restore function reverts production data to a specified point in time. Restoring replaces the original production application data with the specified point-in-time backup. This restoration results in the loss of all current application data as the application will be restored to its status at the point-in-time when the backup was created. This operation cannot be undone.

**Note:** If you are restoring an NFS backup, the advanced NFS Settings should only be changed after consulting with your Support representative.

Typically restore operations are performed to restore a database to a valid state after events like unexpected data corruption. The amount of time required to complete a restore operation depends on the amount of data involved.

## Restore operations

Restore operations let you revert production workloads or recover data from a point-in-time backup stored in your backup vault. You can initiate restores directly from the **Vaulted backups** page in the Google Cloud console.

### Types of restore operations

Depending on your recovery requirements, you can perform different kinds of restore operations:

  * **Full workload restore** : recreates an entire VM instance, database cluster, or file share from a point-in-time backup. For Compute Engine instances, this creates a new VM instance with pre-populated properties matching the source instance.

  * **Selective disk restore** : when restoring from a Compute Engine instance backup, you can choose the **Individual disk** restore scope. This selectively restores an individual protected disk from an instance backup to create a new Persistent Disk volume without restoring the entire VM instance. See [Perform a selective disk restore from a Compute Engine instance backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/disk-restore#restore-disk-from-compute-instance-backup).

  * **Independent disk restore** : restores a captured independent persistent disk backup directly to a new Persistent Disk volume. See [Restore a disk from a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/disk-restore).

  * **Database and file share restore** : recovers automated enhanced backups to create a new Cloud SQL instance or AlloyDB for PostgreSQL cluster, or reverts a Filestore instance.




### Supported workloads and restore targets

Depending on the workload type, you can restore backups to new resources or perform selective data recovery:

  * **Compute Engine instances** : restore a Compute Engine instance backup to create a completely new Compute Engine instance with matching configurations, or perform a selective disk restore to create a new Persistent Disk from an instance backup. See [Restore a Compute Engine instance from a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-restore).

  * **Persistent Disk** : restore a captured persistent disk backup to a new persistent disk. See [Restore a disk from a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/disk-restore).

  * **Cloud SQL instances** : restore point-in-time enhanced backups to create a new Cloud SQL instance. See [Restore a Cloud SQL instance from a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/sql/csql-restore).

  * **AlloyDB clusters** : restore a vaulted backup to create a new AlloyDB for PostgreSQL cluster. See [Restore an AlloyDB cluster from a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/alloydb/alloydb-restore).

  * **Filestore instances** : restore Filestore backups to revert data or recover file shares. See [Restore a Filestore instance from a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/filestore/filestore-instance-restore).




## Restore application backups using the appliance management console

Only users with the Restore Manage right can perform a Restore operation. User roles are detailed in [Managing Roles](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/manage-roles).

The appliance management console restores applications in different ways. In all cases, the backup replaces the identical original production data. In some cases, new data created after the backup was taken may be protected from being overwritten.

Use this procedure to restore captured application backups from a specific point-in-time. If you are selecting applications from a VM, ensure that the Backup and DR agent is installed on the Virtual Machine and applications on the VM have been discovered.

Each type of application has prerequisites, constraints, or requirement. See Restoring VMs and Specific Types of Applications for details.

When you restore a point-in-time backup, backup plan management of the application is disabled in **App Manager**.

## Restore an application backup

To restore a point-in-time backup from a managed application:

  1. Click the **App Manager** tab and select **Applications** from the drop-down menu. The Applications page opens.
  2. Select the application with the backup you want to restore and then choose **Access** from the drop-down list at the bottom of the Applications page. The Access page opens listing captured backups appears in the Timeline ramp view. For more information on the view, see [Accessing the Timeline Ramp View of a backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/filesystem-restore).
  3. Select the backup and select **Restore** from the list of access operations. The Restore page opens.

**Note:** If you are restoring an NFS backup, the Advanced NFS Settings should only be changed after consulting with your support representative.
  4. Select a single volume or multiple volumes to restore. By default all the volumes are selected.

  5. Click **Submit**. A warning dialog opens. Read it and then enter **DATA LOSS** to confirm.

  6. Depending on your configuration, a second warning may appear. If so, you need to enter **OVERWRITE OTHER APPS** to confirm the restore operation.

The restore job starts. You can verify that the restore operation is successful by viewing the job status in the **Monitor** tab.

When the database backup is restored, the appliance management console creates a new database backup populated with data copied from the specified point-in-time backup.




## Restore specific types of applications

The backup/recovery appliance restores applications in different ways. In all cases, the point-in-time backup replaces the identical original production data. In some cases, new data created after the backup was taken may be protected from being overwritten.

Restoring always involves risk of data loss. The appliance management console offers other options for recovering data from your backup/recovery appliances. When restoring applications from managed databases, be sure to take into account the following information.

For system restore, see the following:

  * [Restore a Compute Engine instance](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-instance)

  * [Restore a VMware VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-vm)




For database restore:

  * [Restore a Microsoft SQL Server database](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/sql-restore)
  * [Restore an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-oracle)
  * [Restore an SAP HANA backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/recover-sap-hana)
  * [Restore an IBM Db2 instance](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/otherdb-restore)
  * [Restore a PostgreSQL instance](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/otherdb-restore)
  * [Restore an SAP ASE instance](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/otherdb-restore)
  * [Restore an SAP IQ database](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/otherdb-restore)
  * [Restore an SAP MaxDB database](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/otherdb-restore)



For file system and other application types, see the following:

  * [Restore a file system](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/filesystem-restore)
  * [Restore a consistency group](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-instance)
  * [Restore a generic application (LVM)](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/generic-application-restore)

**Note:** If you are restoring an NFS backup, the advanced NFS settings should only be changed after consulting with your support representative.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
