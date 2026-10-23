---
url: https://docs.cloud.google.com/filestore/docs/restore-data/
title: Restore data \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:41.563484+00:00
---

# Restore data  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/restore-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Restore data Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to restore a backup to an instance.

## Before you start

Before you start restoring data, enable APIs and ensure the necessary roles and permissions are granted. For more information, see [Before you start](https://docs.cloud.google.com/filestore/docs/backups-before-you-start).

## Restore standard backup to the source or an existing instance

You can restore a basic tier backup to the source instance or to a file share of an existing Filestore instance.

Before initiating a restore operation, we recommend pausing applications and unmounting from the file system to reduce the risk of application errors. You must then remount the file share after it is restored from a backup. All outstanding file locks are revoked upon successful restoration. During restoration, client `READ` and `WRITE` operations are paused.

When restoring a backup to an existing Filestore instance, the capacity of the target instance must be greater than or equal to that of the original instance the backup was created from. If the original instance has a greater capacity, you must first increase the target instance's capacity before attempting the restore operation.

If a backup restore to a Basic HDD or Basic SSD instance fails, the file share state remains unchanged.

###  Console 

  1. In the Google Cloud console, go to the **Instances** page.



[Go to Instances](https://console.cloud.google.com/filestore/instances)

  1. In the instance list, click the instance that you want to restore the backup from to see the instance details.
  2. Click the **Backups** tab.
  3. Locate the backup that you want to restore from and click more_horiz **More actions**.
  4. Click **Restore backup**.
  5. Choose a target instance to restore: 
     * If restoring the source instance, click **Source instance**.
     * If restoring to another existing instance: 
       1. Click **Other existing instance**.
       2. Click **Select instance**.
       3. Select the target instance where you want the restored backup to reside and click **Select**.
  6. Click **Restore**.
  7. Click the acknowledgement checkbox.
  8. Enter the name of the backup in the input field and click **Restore**.



###  gcloud 

To restore a Filestore file share to an existing instance, run the [`instances restore`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/restore) command:
    
    
      gcloud filestore instances restore INSTANCE_ID \
      --source-backup=BACKUP_ID \
      --source-backup-region=BACKUP_LOCATION \
      --file-share=FILE_SHARE_NAME \
      --zone=INSTANCE_LOCATION
    

Where:

  * INSTANCE_ID is the name of the existing Filestore instance to restore the file share to.
  * BACKUP_ID is the name of the backup to restore data from.
  * BACKUP_LOCATION is the region where the backup is located.
  * FILE_SHARE_NAME is the name of the file share to restore the backup to.
  * INSTANCE_LOCATION is the zone that the Filestore instance is located.



### Example

The following command restores `mybackup`, which is located in region `asia-east2`, to file share `vol1` on Filestore instance `myinstance`, which is located in zone `us-central1-c`:
    
    
      gcloud filestore instances restore myinstance \
      --source-backup=mybackup \
      --source-backup-region=asia-east2  \
      --file-share=vol1 \
      --zone=us-central1-c
    

## Restore standard backup to a new instance

When a Zonal, Regional, and Enterprise backup is restored to a new Filestore instance, the capacity of the new file share must be greater than or equal to the capacity of the backup. To restore a standard backup follow these steps:

###  Console 

  1. In the Google Cloud console, go to the Filestore **Backups** page.

[Go to Backups](https://console.cloud.google.com/filestore/backups)

  2. Click the **Standard** tab.

  3. Select the backup from the list.

  4. Click **Restore**.

  5. Configure the new instance by following the instructions in [Create an instance](https://docs.cloud.google.com/filestore/docs/creating-instances).

  6. Click **Restore**.




###  gcloud 

To restore a Filestore file share to a new instance, run the [`instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/create) command:
    
    
      gcloud filestore instances create INSTANCE_ID \
      --zone=ZONE \
      --tier=TIER \
      --file-share=name=FILE_SHARE_NAME,capacity=FILE_SHARE_CAPACITY,source-backup=SOURCE_BACKUP_NAME,source-backup-region=SOURCE_BACKUP_LOCATION \
      --network=name=VPC_NETWORK,reserved-ip-range=RESERVED_IP_ADDRESS
    

Where:

  * INSTANCE_ID is the name you want to give to the new Filestore instance.
  * ZONE is the zone where the Filestore instance resides.
  * TIER is the service tier that you want to use.
  * FILE_SHARE_NAME is the name you specify for the NFS file share that is served from the instance.
  * FILE_SHARE_CAPACITY is the capacity you want for the file share in GiB or TiB, depending on the instance type and your needs. 
  * SOURCE_BACKUP_NAME is the name of the backup to restore data from.
  * SOURCE_BACKUP_LOCATION is the region where the backup is located.
  * VPC_NETWORK is the name of the VPC network you want the instance to use.
  * RESERVED_IP_ADDRESS is the IP address range for the Filestore instance.



For `gcloud` flag details, see [Create an instance](https://docs.cloud.google.com/filestore/docs/creating-instances).

### Example

The following command creates a new Filestore instance `myinstance-restored` located in zone `us-central1-c` on network default. Backup `mybackup` located in region `asia-east2` is restored on file share `vol1` of `myinstance-restored` with a `2TiB` capacity:
    
    
      gcloud filestore instances create myinstance-restored \
      --zone=us-central1-c \
      --tier=zonal \
      --network=name=default \
      --file-share=name=vol1,capacity=2TiB,source-backup=mybackup,source-backup-region=asia-east2
    

## Restore an enhanced backup

You can only restore an enhanced backup to a new instance. To restore an enhanced backup, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the Filestore **Backups** page.

[Go to Backups](https://console.cloud.google.com/filestore/backups)

  2. Click the **Enhanced** tab.

  3. Select an instance and a backup vault from the list to display the available backups and click the backup name.

  4. Click **Restore**.

  5. Configure the new instance by following the instructions in [Create an instance](https://docs.cloud.google.com/filestore/docs/creating-instances).




###  gcloud 

To restore a Filestore file share to a new instance, run the [`instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/create) command:
    
    
      gcloud filestore instances create INSTANCE_ID \
      --zone=ZONE \
      --tier=TIER \
      --network=name=VPC_NETWORK \
      --file-share=name=FILE_SHARE_NAME,capacity=FILE_SHARE_CAPACITY,source-backupdr-backup=SOURCE_BACKUP_PATH
    

Where:

  * INSTANCE_ID is the name you want to give to the new Filestore instance.
  * ZONE is the zone where the Filestore instance resides.
  * TIER is the service tier you want to use.
  * FILE_SHARE_NAME is the name you specify for the NFS file share that is served from the instance.
  * FILE_SHARE_CAPACITY is the capacity you want for the file share in GiB or TiB, depending on the instance type and your needs. The provisioned capacity of the new instance must be equal to or exceed the provisioned capacity of the source instance. 
  * SOURCE_BACKUP_PATH is the full path to the backup that the instance is restored from. The path is in the following format:
        
        projects/PROJECT_ID/locations/LOCATION/backupVaults/BACKUP_VAULT_ID/dataSources/DATASOURCE/backups/BACKUP_ID
        

Where:

    * PROJECT_ID is the name of the project where the backup resides.
    * LOCATION is the location of the backup.
    * BACKUP_VAULT_ID is the name of the backup vault.
    * DATASOURCE is ID of the data source.
    * BACKUP_ID is the ID of the backup.
  * VPC_NETWORK is the name of the VPC network you want the instance to use.




### Example

The following command creates a new Filestore instance `backupdr-instance-restored` located in zone `us-central1-a` on the network `default`. The backup is restored on file share `vol1` of `backupdr-instance-restored` with a `1TiB` capacity:
    
    
      gcloud --project=gcbdr-project filestore instances create backupdr-instance-restored \
      --zone=us-central1-a \
      --tier=zonal \
      --file-share=name="vol1",capacity=1024,source-backupdr-backup="projects/gcbdr-project/locations/us-central1/backupVaults/vault-1/dataSources/a11111bb222ccc333ddd4444eee555555f6666/backups/00aaab11-2222-3333-c444-d5ddd555555d" \
      --network=name="default"
    

## Restore a Filestore instance from a backup vault

To restore a Filestore instance from a backup vault in the Google Cloud follow the instructions in [Restore a Filestore instance from a backup vault in the Google Cloud](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/filestore/filestore-instance-restore).

## What's next

  * Learn how to [schedule backups using Cloud Scheduler](https://docs.cloud.google.com/filestore/docs/scheduling-backups).
  * Learn more about [backups, common use cases, and best practices](https://docs.cloud.google.com/filestore/docs/backups).
  * Learn about backups [pricing](https://cloud.google.com/filestore/pricing#backups_pricing).
  * Learn how to set up alerts for [low disk space](https://docs.cloud.google.com/filestore/docs/monitoring-instances#low-disk-space) and [low backups quota](https://docs.cloud.google.com/filestore/docs/monitoring-instances#low-backups-quota).
  * Learn about backups-related [known issues](https://docs.cloud.google.com/filestore/docs/known-issues#unable_to_use_backups_with_instances_created_using_private_services_access).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
