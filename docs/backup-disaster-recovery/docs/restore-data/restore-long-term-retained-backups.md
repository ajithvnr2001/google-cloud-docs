---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-long-term-retained-backups/
title: Restore long-term retained backups \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:43.437502+00:00
---

# Restore long-term retained backups  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-long-term-retained-backups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Restore long-term retained backups Stay organized with collections  Save and categorize content based on your preferences. 

You can recover long-term retained backups directly from your [Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/buckets) using a standalone utility, ensuring data access even without active Backup and DR appliances.

This document describes how to use this standalone recovery utility to discover, verify, mount, and restore Backup and DR [OnVault](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/storage-pools#onvault) and Compute Engine backup images.

## Overview

Long-term retained backups are stored in Cloud Storage buckets using OnVault policies for compliance and archiving. To ensure data accessibility independently of the backup infrastructure, you can use a standalone recovery utility to discover, verify, and restore this data directly from the storage bucket. This is critical for disaster recovery or decommissioning scenarios where the originating backup/recovery appliance might not be available.

## Before you begin

Before you begin restoring long-term retained backups, complete the following sections.

### Get required roles

To get the permissions that you need to restore long-term retained backups, ask your administrator to grant you the [Backup and DR Cloud Storage Operator ](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.cloudStorageOperator) (`roles/backupdr.cloudStorageOperator`) IAM role on the target Cloud Storage bucket. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Other prerequisites

Before you restore long-term retained backups, ensure that you meet the following prerequisites:

  1. Before you initiate a recovery, confirm that your data is available in OnVault storage. Verify existing backups in the backup/recovery appliance pool, and migrate them to OnVault by assigning the relevant OnVault protection policy.
  2. For recovery scenarios that involve Persistent Disk (Persistent Disk) snapshots, verify that all backup metadata is replicated to the target Cloud Storage bucket. The recovery utility depends on this metadata to catalog and process snapshot images. To facilitate data transfer and confirm that metadata is present in the Cloud Storage bucket, contact Cloud Customer Care.

**Note:** This migration is the final step before appliance deletion. Any changes or new backups generated after this step aren't restorable.
  3. Ensure that the host system where you run this tool meets the following requirements:

     * **[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud)** : Installed and accessible in your `PATH` environment variable (specifically `gcloud storage`).
     * **Authentication** : Configured with active credentials by running `gcloud auth login`, or using Application Default Credentials (ADC) or service account keys.
  4. Identify and keep a list of Cloud Storage bucket names and their corresponding Google Cloud project IDs to use with the recovery utility.




## Deploy the recovery utility

Configure a VM instance to serve as a recovery proxy or as the destination application host, and then deploy the standalone recovery tool.

## Discover appliances, hosts, and images

The standalone recovery utility accepts a pair of bucket and project values (`--bucket` and `--project`) for commands. The utility supports the following operations:

  * List applications
  * List backups
  * Expire backups
  * Mount a backup image
  * Unmount a backup image



## Mount the backup image

To perform a recovery mount, you first need to identify the backup image name.

List the available backups to identify the backup image name:
    
    
    python3 ~/gcbdr-onvault-cli/python/gcbdr_onvault.py \
      --bucket BUCKET_NAME \
      --project PROJECT_ID \
      --cluster APPLIANCE_NAME \
      --host HOST_NAME \
      --app APPLICATION_NAME \
      --list-images
    

Then, to perform a non-interactive recovery mount, use a command similar to the following sample to mount the selected backup image directly onto either your designated recovery proxy or the target database server:
    
    
    python3 ~/gcbdr-onvault-cli/python/gcbdr_onvault.py \
      --bucket BUCKET_NAME \
      --project PROJECT_ID \
      --cluster APPLIANCE_NAME \
      --host HOST_NAME \
      --app APPLICATION_NAME \
      --image IMAGE_NAME \
      --mountpoint MOUNT_POINT \
      --auto-mount
    

Replace the following:

  * `BUCKET_NAME`: the name of the Cloud Storage bucket.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `APPLIANCE_NAME`: the name or ID of the backup/recovery appliance.
  * `HOST_NAME`: the hostname or ID of the source host.
  * `APPLICATION_NAME`: the name or ID of the protected application.
  * `IMAGE_NAME`: the name of the active backup image to mount.
  * `MOUNT_POINT`: (Optional) the local directory path where the backup is mounted. The default is `/tmp/recovery_folder`.



After extraction completes, you can view the backed-up data in the mount point directory.

## Restore applications

To access raw database files, go to `MOUNT_POINT/restored_data/`. Select the recovery path for your workload type and mounting configuration:

### Microsoft SQL

  1. **Locate files** : identify the primary `.mdf` and `.ldf` database files in the `db_volume/` directory.
  2. **Direct attach (same host)** : stop the target database instance. Open SQL Server Management Studio, select **Attach Database** , and specify the file paths pointing to the data and log files in the recovery mount point directory.
  3. **Copy and attach (different host)** : stop the target database instance. Transfer the `.mdf` and `.ldf` files to the target server local storage drives, and then attach them using SQL Server Management Studio.



### Oracle

  1. **Locate files** : the utility automatically detects `init.ora` or `spfile` files and `.dbf` data files while bringing the RMAN database backup and `Archive log` volume groups online.
  2. **Recover database** : shut down the target Oracle instance or start it in `NOMOUNT` mode. Either update initialization parameters (such as control files) to point to the mounted `.dbf` files for direct validation, or copy the `.dbf` files to local storage or Automatic Storage Management (ASM) storage for permanent recovery.
  3. **Open database** : bring the instance to `MOUNT` status, apply required recovery logs from the mounted `TransactionLog` volume group, and then open the database.



###  VMware Engine VM 

Beyond database application recovery, Google Cloud VMware Engine (VMware Engine) virtual machine protection encompasses the entire hardware configuration alongside virtual disk extents.

  1. **Mount and locate files** : mount the backup image as described in Mount the backup image. The utility generates the sparse virtual disk (`vol00.raw`) within the primary mount path. It then attaches the disk to expose the guest operating system file system under the `db_volume/` directory, while VMware configuration metadata (including `.ovf`, `.vmx`, and `Catalog.xml`) is organized within the `log_files/` folder.
  2. **Restore the VM directly** : deactivate the target VM to secure its base disk for manifest parsing. A worker process reads data blocks from local storage, writes them to the VMDK by using VMware Virtual Disk Development Kit (VDDK) libraries, and then automatically restarts the VM.



###  Compute Engine PD snapshots 

In contrast to OnVault backups mounted as local file systems, Compute Engine Persistent Disk snapshots are restored by initializing new persistent disks and attaching them directly to a target Compute Engine instance.

  1. **Identify target backup and metadata** : confirm that the Persistent Disk snapshot metadata catalog file (`pdsnapshot_catalog.json`) is present in your Cloud Storage bucket. Use the persistent disk manager utility to review the available backups listed in the catalog and select the specific `IMAGE ID` intended for recovery.
  2. **Restore and attach volumes** : use the `attach` command to automate the generation of persistent disks from backup snapshots. This single action handles the creation and connection of all relevant volumes to your destination virtual machine.
  3. **Mount devices at the operating system level** : after the attachment completes, connect to the target Compute Engine instance to identify the newly mapped block devices using tools such as `lsblk`. Manually mount the file systems to access the recovered data or initiate the application recovery process.



### SAP HANA PD

Unlike OnVault backups, which are mounted directly as local file systems, restoring SAP HANA Persistent Disk snapshots involves provisioning new persistent disks and attaching them to the target Compute Engine instance.

  1. **Verify metadata and locate backup image** : ensure that the Persistent Disk snapshot metadata catalog file is available in the Cloud Storage bucket. Use the persistent disk manager tool to inspect cataloged backups and choose the required `IMAGE ID` for recovery.
  2. **Provision disks and attach volumes** : run the `attach` command to automate generating persistent disks from the chosen backup snapshot. This step creates all required volumes and attaches them to the target virtual machine in a single operation.
  3. **Mount devices at the operating system level** : after the disks are attached, connect to the destination SAP HANA VM and check for newly assigned block devices using tools such as `lsblk`. Mount the file systems manually to access recovered data or begin application-level restoration.
  4. **Recover SAP HANA** : after mounting the SAP HANA data, log, and archive log volumes, start the system database (including point-in-time recovery if required), followed by the recovery and initialization of the tenant databases.



### IBM Db2 PD

In contrast to OnVault backups, which mount directly as local file systems, restoring IBM Db2 Persistent Disk snapshots requires provisioning new persistent disks and attaching them to the destination Compute Engine instance.

  1. **Locate backup image and validate metadata** : verify that the Persistent Disk snapshot metadata catalog file is present in the designated Cloud Storage bucket. Use the persistent disk manager tool to inspect the cataloged backups to identify and select the target `IMAGE ID` required for recovery.
  2. **Attach volumes and provision disks** : run the `attach` command to automatically create persistent disks from the specified backup snapshot. This single step provisions all necessary volumes and attaches them directly to the target virtual machine.
  3. **Mount operating system file systems** : after attaching the disks, connect to the target IBM Db2 VM to identify newly mapped block devices using tools such as `lsblk`. Manually mount the file systems to access restored data or proceed with application recovery.
  4. **Recover application database** : after you mount the Db2 data, transaction log, and archive log volumes, catalog each Db2 database instance, perform database recovery as needed, and bring the database online.



### MySQL/MariaDB

  1. **Locate files** : locate the main data directory in `db_volume/`, containing user databases, system schema, and InnoDB tablespaces.
  2. **Restore database** : stop the active MySQL or MariaDB service. To test directly, adjust the `datadir` entry in `my.cnf` to target the recovery mount folder. For a permanent restoration, copy the database files to local storage (such as `/var/lib/mysql/`) and ensure correct file system ownership and permissions.

**Note:** If you use dump backups (full and incremental), you don't need to shut down the database. Run the standard dump restoration commands.
  3. **Bring online and recover** : restart the database service. If binary transaction logs exist, perform point-in-time recovery by using the `mysqlbinlog` utility.




### PostgreSQL

  1. **Locate files** : in the `db_volume/` directory, identify the `PGDATA` assets, including core databases (`base/`, `global/`, and `pg_wal/`) and the `postgresql.conf` configuration file.
  2. **Restore database** : shut down the destination PostgreSQL instance. For validation directly from the mount, point the `data_directory` or `PGDATA` environment variable to the recovery path. To restore permanently, transfer the complete directory structure to the target host local storage.

**Note:** If you use dump backups (full and incremental), you don't need to shut down the database. Run the standard dump restoration commands.
  3. **Open database** : restart the service to bring the instance online. If point-in-time recovery is required, apply archived WAL logs from the `log_files/` folder by defining a `recovery.conf` file or configuring the `restore_command` within `postgresql.conf` (for PostgreSQL 12 and later), and then bring the database online.




### SAP ASE

  1. **Locate files** : identify the primary master device, alongside specific user database and log devices, situated within the mounted `db_volume/` folder.
  2. **Restore database** : shut down the destination SAP ASE instance. For direct mounting, update the `RUN_server` configuration to redirect the master device parameter (such as `-d`) to the recovery path. Alternatively, transfer all device assets to their permanent storage locations.

**Note:** If you use dump backups (full and incremental), you don't need to shut down the database. Run the standard dump restoration commands.
  3. **Open database** : start the SAP ASE dataserver process. If transaction logs are present, execute the `LOAD TRAN` operation to perform point-in-time recovery before bringing the database online.




### SAP MaxDB

  1. **Locate volumes** : go to the `db_volume/` mount path to find the primary SAP MaxDB data and log files.
  2. **Restore or redirect configuration** : stop the destination SAP MaxDB process. Use the Database Manager (`dbmcli`) to update parameters such as `DataVolumeName` to point to the recovery mount, or copy the files directly to local storage for a full restore.

**Note:** If you use dump backups (full and incremental), you don't need to shut down the database. Run the standard dump restoration commands.
  3. **Start and bring online** : start the database instance and set its operational status to `ONLINE` using Database Manager.




### SAP IQ

  1. **Locate files** : go to the `db_volume/` directory to identify the primary SAP IQ main store, the catalog store (`.db`), and all associated temporary store assets.
  2. **Restore database** : shut down the destination SAP IQ instance. To perform direct validation from the recovery mount, modify the startup parameters to reference the mounted catalog file. For permanent restoration, transfer all store volumes to local storage while verifying that appropriate file system ownership and permissions are maintained.

**Note:** If you use dump backups (full and incremental), you don't need to shut down the database. Run the standard dump restoration commands.
  3. **Open database** : run the `start_iq` utility to bring the instance online and verify data integrity.




### IBM Db2 LVM/dump

  1. **Locate files** : go to the `db_volume/` and `log_files/` mount paths. Based on the protection method, identify either the LVM data and log volumes or the specific backup image assets for dump-based recovery.
  2. **Recover database (LVM)** : shut down the destination Db2 instance. Transfer the database data and active transaction log volumes from the recovery mount to the target local storage, ensuring correct file system ownership for the Db2 user and group.
  3. **Restore database (dump-based full and incremental)** : stop active connections and drop the target database if it exists. Use the `db2ckrst` tool with the specific backup timestamp to catalog the necessary incremental sequence. Run the `RESTORE` operation for each image in the prescribed order.
  4. **Open database** : start the Db2 instance. If the database remains in a pending state or requires point-in-time recovery, apply the transaction logs using the `db2 rollforward` utility to complete the recovery and bring the instance online.



## Clean up resources

After copying or detaching all necessary database files from the database engine, safely unmount the active volumes, detach any associated loop devices, and remove local staging directories to avoid residual locks or orphaned references.

To unmount volumes and clean up the recovery directory, run the following commands:
    
    
    python3 ~/gcbdr-onvault-cli/python/gcbdr_onvault.py \
      --mountpoint MOUNT_POINT \
      --unmount
    rm -rf MOUNT_POINT
    

Replace the following:

  * `MOUNT_POINT`: the local directory path where the backup was mounted, such as `/tmp/recovery_folder`.



## What's next

  * [Overview of restore operations](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-overview)
  * [Monitor jobs in the Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs-console)
  * [Manage backups in the Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/bv-backup-manage)
  * [Audit logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/audit-logging)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
