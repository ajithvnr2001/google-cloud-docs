---
url: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/disk-snapshot-backup-recovery/
title: Backup and recovery for SAP HANA by using disk snapshots \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:41.900114+00:00
---

# Backup and recovery for SAP HANA by using disk snapshots  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/disk-snapshot-backup-recovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Backup and recovery for SAP HANA by using disk snapshots Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To back up SAP HANA deployments that use striped data disks (where the `/hana/data` volume is hosted on more than one disk), contact Customer Care.

This planning guide describes the _disk snapshot_ feature of Google Cloud's Agent for SAP. For information about the other features, see [Google Cloud's Agent for SAP planning guide](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning).

The disk snapshot feature lets you perform backup and recovery operations for SAP HANA systems running on Compute Engine instances.

This feature is integrated with the [Data snapshots](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/ac114d4b34d542b99bc390b34f8ef375.html) feature of SAP HANA, which lets you use standard or archive snapshots of the disks hosting your `/hana/data` volume to back up and recover your SAP HANA database.

For information about how to back up and recover your SAP HANA by using this feature of the agent, see [Back up and recover SAP HANA by using disk snapshots](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/perform-disk-snapshot-backup-recovery).

## Monthly cost estimate

You incur charges for the standard snapshots that you create. For pricing information, see [Disk snapshots](https://cloud.google.com/compute/disks-image-pricing#persistent_disk_snapshots).

To estimate the monthly costs for using disk snapshots as backups for your SAP HANA data volume, you can use the [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator). Use the following information to help you better estimate the cost:

  * Estimated full sizes for the initial disk snapshots.
  * Estimated delta sizes for each subsequent disk snapshots.
  * Snapshot frequency. For example, if you create one set of snapshots every day, then the snapshot frequency is 24 hours.
  * Snapshot retention time.
  * Snapshot storage redundancy: single-region or multi-region.
  * Estimated intra-region and inter-region data transfer over your network. For example, you may incur network fees if you create or restore a standard snapshot group that is stored in a different location than the source disks.



## Limitations

The following limitations apply to backing up and recovering SAP HANA while using the disk snapshot feature of Google Cloud's Agent for SAP:

  * You cannot use the agent's disk snapshot feature for SAP HANA scale-out host auto-failover deployments. For more information, see Using snapshots with scale-out deployments.
  * Your must ensure the following for your `/hana/data` volume: 
    * It is hosted on one or more SSD-based Persistent Disk or Hyperdisk volumes. These disks must host no other SAP HANA volume. As described in the SAP Note [2039883 - FAQ: SAP HANA database and data snapshots (storage snapshots)](https://me.sap.com/notes/2039883), to be able to recover your SAP HANA database, the storage snapshot must not include the log area of the database.
    * It is mapped to a logical volume. This enables the agent to correctly handle the mount point during disk snapshot based backup or recovery operations.
    * If you're using more than one disk to host your `/hana/data` volume, then you can use this feature of the agent only if the underlying disks are Hyperdisk volumes.
  * If you have deployed your SAP HANA system by using Infrastructure as Code (IaC) tools such as Terraform, then the agent can create snapshot based backups but cannot perform recovery operations. For more information, see Using snapshots with IaC tool based deployments.
  * You must perform backup and recovery operations by using the agent instance running on the same Compute Engine instance that hosts your SAP HANA database. You cannot use agent instances running on other Compute Engine instances.
  * To back up and recover your SAP HANA database, you must grant `sudo` access to certain operating system commands either by providing root access or by using an appropriate `sudo` group. For more information, see [Set permissions](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/perform-disk-snapshot-backup-recovery#set_permissions).
  * Instant snapshots and consistency group backups are not supported if the disks are part of a storage pool. For more information, see [Storage pools limitations](https://docs.cloud.google.com/compute/docs/disks/storage-pools#sp_limitations).



For information about limitations of Compute Engine disk snapshots in general, see [Limitations](https://docs.cloud.google.com/compute/docs/disks/snapshots#limitations).

## Required permissions

To allow Google Cloud's Agent for SAP to back up and recover your SAP HANA database by using disk snapshots, you must set permissions for the following:

  * The Google Cloud project where your SAP HANA system is running.
  * The user that runs the agent commands in the operating system, which could be the SAP HANA operating system user, or your own user.
  * The SAP HANA database user used by the agent.



For information about the permissions that you must grant, see [Set permissions](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/perform-disk-snapshot-backup-recovery#set_permissions).

## Create disk snapshot based backups

To create disk snapshot based backups for SAP HANA by using Google Cloud's Agent for SAP, you run the agent's `hanadiskbackup` command. For information about how to do this, see [Back up and recover SAP HANA by using disk snapshots](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/perform-disk-snapshot-backup-recovery).

### Scale-up with `/hana/data` on one disk

The following flowchart shows the steps that the agent performs to create a disk snapshot based backup for your SAP HANA scale-up system when the `/hana/data` volume is hosted on a single disk: 

![Flowchart for disk snapshot based backup for SAP HANA scale-up, by using Google Cloud's Agent for SAP, when the SAP HANA data volume is hosted on a single disk.](https://docs.cloud.google.com/static/sap/docs/images/agent4sap_snapshot_based_backup.svg)

####  How the agent's disk snapshot feature creates a backup for your SAP HANA scale-up system that uses a single disk to host the `/hana/data` volume: 

After you run the `hanadiskbackup` command, the agent does the following: 

  1. Validates all input arguments provided to the `hanadiskbackup` command.
  2. Connects to your SAP HANA database by using the inputs provided to the `hanadiskbackup` command.
  3. Verifies that there are no existing snapshots. 

If there is any existing snapshot of the disk hosting your `/hana/data` volume, and if you've not specified `abandon-prepared=TRUE` with the `hanadiskbackup` command, then the agent exits this procedure and no backup is created. You then need to manually review and re-run the `hanadiskbackup` command.

  4. Informs SAP HANA that snapshot creation has started.
  5. Creates a snapshot of the Persistent Disk or Hyperdisk volume that hosts your `/hana/data` directory.
  6. Informs SAP HANA that snapshot creation is successful.



### Scale-up with `/hana/data` on multiple disks

The following flowchart shows the steps that the agent performs to create a disk snapshot based backup for your SAP HANA scale-up system when the `/hana/data` volume is hosted on more than one disk: 

![Flowchart for disk snapshot based backup for SAP HANA scale-up, by using
           Google Cloud's Agent for SAP, when the SAP HANA data volume is hosted on
           more than one disk.](https://docs.cloud.google.com/static/sap/docs/images/agent4sap_snapshot_based_backup_striped_disk.svg)

####  How the agent's disk snapshot feature creates a backup for your SAP HANA scale-up system that uses striped disks to host the `/hana/data` volume: 

After you run the `hanadiskbackup` command, the agent does the following: 

  1. Validates all input arguments provided to the `hanadiskbackup` command.
  2. Connects to your SAP HANA database by using the inputs provided to the `hanadiskbackup` command.
  3. Finds the disks that host your `/hana/data` volume. From version 3.7 of the agent, if you specify the `-source-disks` argument, then the agent skips this check.
  4. Verifies that all the disks hosting the `/hana/data` volume belong to the same consistency group (CG).
  5. Verifies that there is no existing snapshot based backup available for your SAP HANA database. 

If there exists a snapshot based backup for your database, and if you've not specified `abandon-prepared=TRUE` with the `hanadiskbackup` command, then the agent exits this procedure and no backup is created. You then need to manually review and re-run the `hanadiskbackup` command.

  6. Informs SAP HANA that snapshot creation has started.
  7. Creates a snapshot of your SAP HANA database by using SAP HANA HDBSQL.
  8. Creates an instant snapshot group for the disks that host your `/hana/data` volume.
  9. Converts all instant snapshots to standard or archive snapshots. 

By default, the agent creates standard snapshots. You can choose to create archive snapshots by specifying `snapshot-type=ARCHIVE` with the `hanadiskbackup` command.

  10. Deletes the instant snapshot group.
  11. Informs SAP HANA that snapshot based backup creation is successful.



### Scale-out except host auto-failover

The following flowchart shows the steps that Google Cloud's Agent for SAP performs to create a disk snapshot based backup for your SAP HANA scale-out system that doesn't use the host auto-failover solution: 

![Flowchart for disk snapshot based backup for an SAP HANA scale-out
          system, by using Google Cloud's Agent for SAP.](https://docs.cloud.google.com/static/sap/docs/images/agent4sap_snapshot_based_backup_scale_out.svg)

####  How the agent's disk snapshot feature creates a backup for your SAP HANA scale-out system that doesn't use the host auto-failover solution: 

After you run the `hanadiskbackup` command, the agent does the following: 

  1. Validates all input arguments provided to the `hanadiskbackup` command.
  2. Connects to your SAP HANA database by using the inputs provided to the `hanadiskbackup` command.
  3. Verifies that all the disks hosting the `/hana/data` volume belong to the same consistency group (CG).
  4. Verifies that there is no existing snapshot based backup available for your SAP HANA database. 

If there exists a snapshot based backup for your database, and if you've not specified `abandon-prepared=TRUE` with the `hanadiskbackup` command, then the agent exits this procedure and no backup is created. You then need to manually review and re-run the `hanadiskbackup` command.

  5. Informs SAP HANA that snapshot creation has started.
  6. Creates a snapshot of your SAP HANA database by using SAP HANA HDBSQL.
  7. Creates an instant snapshot group for the disks that host your `/hana/data` volume.
  8. Converts all instant snapshots to standard or archive snapshots. 

By default, the agent creates standard snapshots. You can choose to create archive snapshots by specifying `snapshot-type=ARCHIVE` with the `hanadiskbackup` command.

  9. Deletes the instant snapshot group.
  10. Informs SAP HANA that snapshot based backup creation is successful.



If the agent fails to complete any step in this backup procedure, then it marks the snapshot creation as `UNSUCCESSFUL` in SAP HANA and exits the procedure. You then need to manually review and re-run the `hanadiskbackup` command. To find out why the agent exited the backup procedure, you can view the entries in the `/var/log/google-cloud-sap-agent/hanadiskbackup.log` file.

### Create delta backups

When you run the `hanadiskbackup` command, the agent creates [snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots) for the disks hosting your `/hana/data` volume.

An advantage of disk snapshots is that they are incremental, where each subsequent backup only stores incremental block changes instead of creating an entirely new backup. This means that after you create the first snapshot based backup for your SAP HANA database by using Google Cloud's Agent for SAP, all the succeeding snapshot based backups that you create are delta backups by default. You need not take any additional action to create delta backups.

For more information, see [How incremental standard snapshots work](https://docs.cloud.google.com/compute/docs/disks/snapshots#incremental-snapshots).

### Encrypt disk snapshots

By default, data in Google Cloud is encrypted at rest using AES-256. This applies to the data stored in disks and disk snapshots. Alternatively, you can encrypt your snapshots by using either a [customer-managed encryption key (CMEK)](https://docs.cloud.google.com/kms/docs/cmek) or a [customer-supplied encryption key (CSEK)](https://docs.cloud.google.com/docs/security/encryption/customer-supplied-encryption-keys).

You can also implement an additional layer of security by enabling the encryption provided by SAP HANA for the `/hana/data` volume. For information about this option, see [Enabling Encryption of Data and Log Volumes](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/2ca763d3bd7d4cc187a6737ecc3cb396.html?version=latest).

## Recover SAP HANA data by using disk snapshots

To recover your SAP HANA database by using a disk snapshot based backup, you run the agent's `hanadiskrestore` command. For information about how to do this, see [Back up and recover SAP HANA by using disk snapshots](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/perform-disk-snapshot-backup-recovery).

### Scale-up with one data disk

If your `/hana/data` volume is hosted on one disk, then the following flowchart shows how you use the agent's disk snapshot feature to recover an SAP HANA database: 

![Flowchart for disk snapshot based recovery for SAP HANA by using Google Cloud's Agent for SAP](https://docs.cloud.google.com/static/sap/docs/images/agent4sap_snapshot_based_recovery.svg)

#### How you recover an SAP HANA database by using agent's disk snapshot feature

To recover your SAP HANA database by using a disk snapshot, do the following:

  1. Recover the disk hosting your `/hana/data` volume by running the agent's `hanadiskrestore` command. For instructions, see [Back up and recover for SAP HANA by using a disk snapshot](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/perform-disk-snapshot-backup-recovery). 

The following is the high-level procedure that the agent undertakes to recover your SAP HANA data volume by using a disk snapshot. The preceding flowchart shows these steps.

     1. Validate all input arguments provided to the `hanadiskrestore` command.
     2. Stop SAP HANA.
     3. Unmount the `/hana/data` volume.
     4. Detach the disk hosting the `/hana/data` volume from your host compute instance.
     5. Create a new disk for the `/hana/data` volume from a disk snapshot.
     6. Attach the new disk to your host compute instance.
     7. Rescan the volume groups for SAP HANA.
  2. Manually recover your SAP HANA database either to the snapshot time or a specific point in time, as described in the following subsections.



### Scale-up with striped data disks

If your `/hana/data` volume is hosted on more than one disk, then the following flowchart shows how you use the agent's disk snapshot feature to recover an SAP HANA database: 

![Flowchart for disk snapshot based recovery for SAP HANA by using Google Cloud's Agent for SAP](https://docs.cloud.google.com/static/sap/docs/images/agent4sap_snapshot_based_recovery_striped_disk.svg)

#### How you recover an SAP HANA database by using agent's disk snapshot feature

To recover your SAP HANA database by using a disk snapshot, do the following:

  1. Recover the disk hosting your `/hana/data` volume by running the agent's `hanadiskrestore` command. For information about how to do this, see [Back up and recover SAP HANA by using disk snapshots](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/perform-disk-snapshot-backup-recovery). 

The following is the high-level procedure that the agent undertakes to recover your SAP HANA data volume by using a disk snapshot. The preceding flowchart shows these steps.

     1. Validate all input arguments provided to the `hanadiskrestore` command.
     2. Stop SAP HANA.
     3. Unmount the `/hana/data` volume.
     4. Detach the disks hosting the `/hana/data` volume from your host Compute Engine instance.
     5. Remove the disks hosting the `/hana/data` volume from the corresponding disk consistency group.
     6. Filter the snapshots that correspond to the input consistency group.
     7. Create new disks for the `/hana/data` volume by using the source disk snapshots.
     8. Attach the new disks to your host Compute Engine instance.
     9. Add the new disks to the disk consistency group.
     10. Rescan the volume groups for SAP HANA.
  2. Manually recover your SAP HANA database either to the snapshot time or a specific point in time, as described in the following subsections.



### Scale-out except host auto-failover

The following flowchart shows how you use the agent's disk snapshot feature to recover the SAP HANA database in a scale-out deployment: 

![Flowchart for disk snapshot based recovery for SAP HANA by using Google Cloud's Agent for SAP](https://docs.cloud.google.com/static/sap/docs/images/agent4sap_snapshot_based_recovery_scale_out.svg)

#### How you recover an SAP HANA scale-out database that doesn't use the host auto-failover solution, by using agent's disk snapshot feature

To recover your SAP HANA database by using a disk snapshot, do the following:

  1. On all the nodes in your scale-out deployment, stop SAP HANA.
  2. On all the nodes in your scale-out deployment, unmount the `/hana/data` volume.
  3. Recover the disks hosting the `/hana/data` volume by running the agent's `hanadiskrestore` command. For information about how to do this, see [Back up and recover SAP HANA by using disk snapshots](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/perform-disk-snapshot-backup-recovery). 

The following is the high-level procedure that the agent undertakes to recover your SAP HANA data volume by using a disk snapshot. The preceding flowchart shows these steps.

     1. Validate all input arguments provided to the `hanadiskrestore` command.
     2. Detach the disks hosting the `/hana/data` volume from your host Compute Engine instance.
     3. Remove the disks hosting the `/hana/data` volume from the corresponding disk consistency group.
     4. Filter the snapshots that correspond to the input consistency group.
     5. Create new disks for the `/hana/data` volume by using the source disk snapshots.
     6. Attach the new disks to your host Compute Engine instance.
     7. Add the new disks to the disk consistency group.
  4. Rescan the volume groups for SAP HANA.
  5. Recover your SAP HANA database either to the snapshot time or a specific point in time, as described in the following subsections.



If the agent fails to complete any step in this procedure, then it exits the procedure. You then need to manually review, troubleshoot if required, and then re-run the `hanadiskrestore` command. To find out why the agent exited the database recovery procedure, you can view the entries in the `/var/log/google-cloud-sap-agent/hanadiskrestore.log` file.

### Recover SAP HANA to a specific point-in-time

To recover your SAP HANA database to a specific point in time, in addition to snapshots of the disks hosting your `/hana/data` volume, you need the necessary SAP HANA delta and log backups that you previously created for your database.

You can create the SAP HANA log backup either by using the [Backint](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery) feature of the agent, or a file system backup of your SAP HANA database.

While performing recovery, if you specify a timestamp in the future, then your SAP HANA database is recovered to the most recent state.

### Recover SAP HANA from an external source

You can use the disk snapshot based backups that you created for one SAP HANA system to recover another SAP HANA system. You can also use this capability to move systems across environments, for example, from a testing environment to a quality assurance environment.

For information about how to do this, see [Perform system copy or system refresh](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/perform-disk-snapshot-backup-recovery#perform_system_copy_or_refresh).

### Encrypt disks during recovery

When you recover your SAP HANA database by using the agent's `hanadiskrestore` command, you can specify a target CMEK key to encrypt the newly restored disks. The agent supports the following encryption pathways regardless of whether your SAP HANA system uses a single disk or striped multiple disks to host the `/hana/data` volume:

  * **Google Default Encryption (GMEK) to CMEK** : You can restore disks from a GMEK-encrypted snapshot to a specific target CMEK key.
  * **CMEK to Same CMEK** : You can restore a snapshot of a disk that uses CMEK, automatically inheriting the exact same CMEK for the restored disk.
  * **CMEK to Different CMEK** : You can restore a snapshot of a disk that uses CMEK but encrypt the restored disk with a different, specified target CMEK key.
  * **Cross-project CMEK** : You can specify a target CMEK key that resides in a different Google Cloud project than the restored disks.
  * **Cross-organization CMEK** : You can utilize Cloud KMS keys from projects within completely different Google Cloud organizations. This is subject to the source service account being granted IAM permissions on the key and the destination organization's policies (such as Domain Restricted Sharing and VPC Service Controls) permitting access from the source organization.

**Note:** Customer-Supplied Encryption Keys (CSEK) are supported only for single-disk restorations (`-source-snapshot`). CSEK is not supported for multi-disk restorations (`-group-snapshot-name`). CSEK and CMEK are mutually exclusive for the target disk.

## Using disk snapshots with SAP HANA deployments

The following sections provide scenario-specific planning information for the backup and recovery of SAP HANA scale-up systems by using the disk snapshot feature of Google Cloud's Agent for SAP:

  * Using snapshots with HA deployments
  * Using snapshots with DR deployments
  * Using snapshots with scale-out deployments
  * Using snapshots with IaC tool based deployments



### Using snapshots with HA deployments

In an SAP HANA scale-up system running in a high-availability (HA) cluster on Google Cloud, you need to install Google Cloud's Agent for SAP on both the primary node and the standby node in the cluster.

To create disk snapshot based backups for an SAP HANA HA system, you need to run the `hanadiskbackup` command only for the `/hana/data` volume in your primary node. If a failover event occurs, then you need to run the `hanadiskbackup` command on the new primary node. Also, while running the command, you must specify the SAP HANA hostname or IP address of your primary node's host. Don't specify the SAP HANA virtual IP (VIP) used in the cluster.

While performing recovery operations, you can use the snapshot based backup to recover the disks hosting the `/hana/data` volume in either the primary or the standby node. You can recover your SAP HANA database to the time the disk snapshots were created, or any specific point in time.

### Using snapshots with DR deployments

For an SAP HANA scale-up system in a disaster recovery (DR) deployment on Google Cloud, you need to install Google Cloud's Agent for SAP on both the primary and standby hosts.

To create disk snapshot based backups for an SAP HANA HA system, you need to run the `hanadiskbackup` command only for the `/hana/data` volume in your primary database instance. If you break the SAP HANA system replication and promote the standby database instance, then you need to run the `hanadiskbackup` command on the new primary instance.

For DR deployments, you perform recovery operations on the primary database instance. You can recover your SAP HANA database to the time the disk snapshots were created, or any specific point in time.

### Using snapshots with scale-out deployments

Up to version 3.6 of the Google Cloud's Agent for SAP, the disk snapshot feature of Google Cloud's Agent for SAP is not compatible with SAP HANA scale-out deployments.

From version 3.7 of the agent, you can use the disk snapshot feature with SAP HANA scale-out deployments that don't use the host auto-failover solution.

For backup and recovery in such scenarios, you can use the following options:

  * Use the Google Cloud Backup and DR service. For more information, see [Back up HANA 1+n and HANA scale-out databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/back-up-sap-hana-scaleout).
  * Use the Backint feature of Google Cloud's Agent for SAP. For more information, see [Backint based backup and recovery for SAP HANA](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery).



### Using snapshots with IaC tool based deployments

The disk snapshot feature of Google Cloud's Agent for SAP is partially compatible with SAP HANA systems that have been deployed by using Infrastructure as Code (IaC) tools such as Terraform.

While the agent can create snapshot based backups for these systems, the agent cannot be used to perform recovery operations. This is because snapshot based recovery by using the agent includes recreating the disks hosting the `/hana/data` volume, which can cause conflicts or issues with how the IaC performs state management.

For example, after you perform recovery by using the agent, whenever your IaC tool checks the status of the disks hosting the `/hana/data` volume, the tool would try to revert to your system's defined configuration by either reattaching the previous disks, or by deleting the new disks and recreating the previous disks. Any of these actions can **severely affect** your SAP HANA database, to the extent of making it unusable.

However, most IaC tools provide workflows that let you modify your system's state to keep up with changes to the managed infrastructure. The following is a high-level procedure that you can use to recover SAP HANA systems that you deployed by using IaC tools:

  1. Stop your SAP HANA database. For instructions, see the SAP document [Starting and Stopping SAP HANA Systems](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/19d7e465008045afb996c61a804e76f0.html?q=stop%20hana&locale=en-US).

  2. Stop the Compute Engine instance that hosts your SAP HANA system. In an HA or DR deployment, stop all compute instances. For information about how to stop a compute instance, see [Stop a VM](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm).

  3. In the IaC configuration file that contains the definition of your SAP HANA system, modify the definition of the disks corresponding to the `/hana/data` volume so that they can be recreated by using existing disk snapshots. For an HA or DR deployment, perform this action for the primary SAP HANA node.

For example, if you deployed your SAP HANA system by using one of the [Terraform configurations provided by Google Cloud](https://docs.cloud.google.com/sap/docs/tf-for-sap), then in the `./terraform/modules/sap_hana/main.tf` file, include the `snapshot` argument as follows:

**Note:** The following example applies to scenarios where the `/hana/data` volume is hosted on one disk. If you need assistance for making this change in scenarios where the `/hana/data` volume is hosted on more than one disk, then contact Customer Care.
         
         # Split data/log/sap disks
         resource "google_compute_disk" "sap_hana_data_disks" {
          count   = var.use_single_shared_data_log_disk ? 0 : var.sap_hana_scaleout_nodes + 1
          name    = format("${var.instance_name}-data%05d", count.index + 1)
          type    = local.final_data_disk_type
          zone    = var.zone
          size    = local.data_pd_size
          **snapshot = "hana- SID-snapshot-YYYYMMDD-HHMMSS"**
          project = var.project_id
          provisioned_iops = local.final_data_iops
         }
         

  4. Apply the modified configuration. For example, if you're using Terraform, then run the following commands:
         
         terraform validate
         terraform apply
         

  5. Recover your SAP HANA database. For instructions, see [Recover the database by using a disk snapshot](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/perform-disk-snapshot-backup-recovery#perform_recovery_using_disk_snapshot).




## Enable logging

While performing disk snapshot based backup and recovery operations, Google Cloud's Agent for SAP writes to the following log files: `hanadiskbackup.log` and `hanadiskrestore.log`, respectively.

These log files are located in the `/var/log/google-cloud-sap-agent/` directory on your host Compute Engine instance.

By default, logging is enabled during backup and recovery operations. The default log level is `info`. You can increase or decrease the log level by specifying the `-loglevel` argument when you run the `hanadiskbackup` and `hanadiskrestore` commands.

## Enable monitoring

By default, Google Cloud's Agent for SAP emits the following metrics to [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) each time you run the `hanadiskbackup` command. This is controlled by the `-send-metrics-to-monitoring` argument, which has the default value `TRUE`.

You can set up monitoring for your SAP HANA database by configuring alerts based on these metrics. You can also view the metrics on a dashboard.

The following table describes the metrics that the agent emits during snapshot based backup and recovery operations:

Metric | Description  
---|---  
`workload.googleapis.com/sap/agent/hanadiskbackup/status` |  `Boolean` Informs if the disk snapshot based backup operation is successful or not. The value `true` means success and `false` means failure.  
`workload.googleapis.com/sap/agent/hanadiskbackup/totaltime` |  `Int` Informs the time, in seconds, that the backup operation takes to create the disk snapshots, including the time to upload them to the specified Cloud Storage bucket.  
`workload.googleapis.com/sap/agent/hanadiskbackup/dbfreezetime` |  `Int` Informs the time, in seconds, that your SAP HANA file system was freezed during the disk snapshot based backup operation.  
  
## Best practices

While using disk snapshots to back up and recover your SAP HANA database, we recommend the following best practices:

  * **Prepare alternative recovery options for your database.** We strongly recommend that you design your backup and recovery strategy such that it combines different methods. For example, you can use the agent's disk snapshot feature in combination with a full backup of your SAP HANA database created by using the agent's [Backint](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery) feature or by using a file system backup.
  * **Perform consistency checks for your`/hana/data` volume and disk snapshots.** Because block-level integrity checks are not performed during snapshot based backup operations, we recommend that you regularly perform the following consistency checks by using the `hdbpersdiag` tool:

    * Perform page consistency checks for your `/hana/data` volume. This activity requires downtime as the tool won't be able to check the data pages of a specific data volume if there is a process using the data volume, such as the SAP HANA index server.
    * On a Compute Engine instance other than your SAP HANA host, deploy temporary disks sourced from snapshots that you created by using the agent's `hanadiskbackup` command, and then perform a consistency check on those disks. For information about how to do this, see [Validate snapshot consistency](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/perform-disk-snapshot-backup-recovery#validate_snapshot_consistency).

For information about the `hdbpersdiag` tool, see the SAP document [Perform Consistency Checks](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/60e110ea8f9e457095210115487e11a6.html).

  * **Perform maintenance activities for your disk snapshots.** Because Google Cloud's Agent for SAP doesn't perform any maintenance activities for your disk snapshots, we recommend that you periodically review them and perform activities such as deleting old snapshots.

For more information about disk snapshot related best practices, see [Best practices for Compute Engine disk snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
