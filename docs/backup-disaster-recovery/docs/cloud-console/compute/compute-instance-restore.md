---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-restore/
title: Restore a Compute Engine instance from a backup vault \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:44.024165+00:00
---

# Restore a Compute Engine instance from a backup vault  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Restore a Compute Engine instance from a backup vault Stay organized with collections  Save and categorize content based on your preferences. 

This page helps you to restore a Compute Engine instance from a backup vault in the Google Cloud console, which can target either a new Compute Engine instance or a new Persistent Disk. To selectively restore an individual disk to a new Persistent Disk, see [Perform a selective disk restore from a Compute Engine instance backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/disk-restore#restore-disk-from-compute-instance-backup).

## Required roles

To get the permissions that you need to restore a Compute Engine instance from a backup vault, ask your administrator to grant you the following IAM roles on the project, the target project, the Backup and DR service agent, and the VPC host project: 

  * Restore a Compute Engine instance: 
    * [Backup and DR Restore User ](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)
    * [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`)
  * Grant roles to the service agent: [Backup and DR Compute Engine Operator ](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.computeEngineOperator) (`roles/backupdr.computeEngineOperator`) 
  * Use a Shared VPC (optional): [Compute Network User ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`) 
  * Perform a selective disk restore operation from a Compute Engine instance backup: [Backup and DR Disk Operator ](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.diskOperator) (`roles/backupdr.diskOperator`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to restore a Compute Engine instance from a backup vault. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to restore a Compute Engine instance from a backup vault:

  * Restore a Compute Engine instance: 
    * `backupdr.bvbackups.restore`
    * `backupdr.compute.restoreFromBackupVault`
    * `backupdr.backupVaults.get`
    * `backupdr.backupVaults.list`
    * `backupdr.bvbackups.list`
    * `backupdr.bvdataSources.get`
    * `backupdr.bvdataSources.list`
    * `backupdr.bvbackups.get`
  * Restore a Compute Engine instance using the Google Cloud console (additional permissions): 
    * `compute.acceleratorTypes.list`
    * `compute.disks.list`
    * `compute.machineTypes.list`
    * `compute.projects.get`
    * `compute.regions.list`
    * `compute.zones.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Restore a Compute Engine instance

Use the following instructions to restore a Compute Engine instance.

###  Console 

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

All Compute Engine instances with vaulted backups are listed here.

  2. Click the action icon to select the **Restore** action. The **Restore page** displays where you select the following restore options:

     * Select a **Resource name**.
     * Select a **Backup creation time**.
     * Select the **Restore scope** , either the entire Compute Engine instance or an individual disk. To restore an individual disk, see [Perform a selective disk restore from a Compute Engine instance backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/disk-restore#restore-disk-from-compute-instance-backup).
     * Select the **Project name** into which you want to restore the VM.
  3. Click **Proceed**.

The **Create a new Compute Engine instance from a backup** page appears, where the Compute Engine instance properties are pre-populated based on the source Compute Engine instance properties. You can modify the properties to create a new Compute Engine instance, for example, change the selection for **Region** or **Machine Type**.

  4. Click **Create** to create a new VM from the selected backup.

**Note:** You can view and monitor the restore jobs in the **Backup and DR** > **Jobs** page.



###  gcloud 

  1. Get the backup vault service account using the `gcloud backup-dr backup-vaults describe` command:
         
         gcloud backup-dr backup-vaults describe BACKUP_VAULT_NAME /
         --location=REGION_NAME
         

Replace the following:

     * BACKUP_VAULT_NAME: the backup vault name you want to restore data from.

     * REGION_NAME: the region of the backup vault.

  2. Before you can restore a Compute Engine instance, use the following commands to get the data source ID and the ID of the required backup:

     1. Find the data source ID using the `gcloud backup-dr data-sources list` command:
            
            gcloud backup-dr data-sources list \
            --project=PROJECT_NAME \
            --location=REGION_NAME \
            --backup-vault=BACKUP_VAULT_NAME \
            "--filter=dataSourceGcpResource.computeInstanceDatasourceProperties.name:(DATA_SOURCE)" \
            "--format=get(name)"
            

     2. List existing backups for the data source to find the correct `BACKUP_ID` using the `gcloud backup-dr backups list` command:
            
            gcloud backup-dr backups list \
            --location=REGION_NAME \
            --backup-vault=BACKUP_VAULT_NAME \
            --data-source=DATA_SOURCE \
            "--format=yaml(backupType,computeInstanceBackupProperties.sourceInstance,consistencyTime,enforcedRetentionEndTime,expireTime,name)"
            

  3. To restore a Compute Engine instance, use the following commands:

     * Restore a Compute Engine instance in the same project as the workload project with the backup ID using the `gcloud backup-dr backups restore compute` command:
           
           gcloud backup-dr backups restore compute test-backup-id \
           --project=PROJECT_NAME --location=REGION_NAME \
           --backup-vault=BACKUP_VAULT_NAME --data-source=DATA_SOURCE\
           --name=NAME --target-zone=TARGET_ZONE \
           --target-project=TARGET_PROJECT
           

     * Restore a Compute Engine instance in the same project as the workload project with backup full resource URL using the `gcloud backup-dr backups restore compute projects` command:
           
           gcloud backup-dr backups restore compute projects/test-project-id/locations/us-central1/backupVaults/test-vault/dataSources/test-ds/backups/test-backup-id \
           --name=NAME --target-zone=TARGET_ZONE \
           --target-project=TARGET_PROJECT
           

     * Restore a Compute Engine instance with custom service account and network configuration using the `gcloud backup-dr backups restore compute` command:
           
           gcloud backup-dr backups restore compute test-backup-id \
           --project=PROJECT --location=REGION \
           --backup-vault=BACKUPVAULT_NAME --data-source=DATA_SOURCE\
           --name=NAME --target-zone=TARGET_ZONE \
           --target-project=TARGET_PROJECT \
           --network-interface=network=NETWORK,subnet=SUBNET \
           --service-account=SERVICE_ACCOUNT \
           --scopes=SCOPE
           

Replace the following:

       * PROJECT: the name of the backup vault project.

       * REGION: the location of the backup vault.

       * BACKUPVAULT_NAME: the backup vault name you want to restore data from.

       * DATA_SOURCE: the data source name you want to restore data from.

       * NAME: the name of the restored Compute Engine instance.

       * TARGET_ZONE: the region the Compute Engine instance is restored in.

       * TARGET_PROJECT: the project the Compute Engine instance is restored in.

       * NETWORK: the network URI of the Compute Engine instance.

       * SUBNET: the subnet URI of the Compute Engine instance.

       * SERVICE_ACCOUNT: the service account of the restored Compute Engine instance.

       * SCOPE: the authorization scope of the service account.

     * Restore a Compute Engine disk using the `gcloud backup-dr backups restore disk` command. For detailed instructions on restoring an individual disk from a Compute Engine instance backup, see [Perform a selective disk restore from a Compute Engine instance backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/disk-restore#restore-disk-from-compute-instance-backup).
           
           gcloud backup-dr backups restore disk BACKUP_NAME  \
           --name=DISK_NAME \
           --target-project=TARGET_PROJECT_NAME \
           [--source-instance-boot-disk | --source-instance-disk-device-name=DEVICE_NAME] \
           [--target-zone=TARGET_ZONE_NAME | --target-region=TARGET_REGION_NAME --replica-zones=ZONE_NAME] \
           [DISK_OVERRIDE_FLAGS...] \
           [--async]
           




To override other Compute Engine instance properties, see [Overview of Backup and DR ](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backups/restore)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) commands.

### Restore limitations for selective disk backups

When you restore a Compute Engine instance from a backup created using [selective disk backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-backup#configure_selective_disk_backup_in_a_backup_plan), only the disks that were protected at the time of backup are restored and attached to the new virtual machine (VM) instance. In the Google Cloud console, the summary section highlights the protected disks included in the backup (for example, `Protected disks: 2 out of 3`).

**Note:** If any mounted disks were excluded during backup, the restored instance might fail to boot if the excluded disk is still referenced in the source instance's boot configuration (for example, in the `/etc/fstab` file on Linux). When the restored VM boots up, the operating system attempts to mount all disks referenced in the boot configuration. If an excluded disk is missing, boot operations might fail.

To prevent boot failures when restoring VMs with excluded disks, configure the source VM's boot configuration to ignore missing disks (for example, by adding the `nofail` mount option in `/etc/fstab`). For more information about this Compute Engine limitation, see [Persistent disk restore limitations and caveats](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images#workarounds-for-boot-failures).

## Restore a backup from a CMEK-enabled backup vault

The encryption handling for restores from a CMEK-enabled backup vault depends on whether you are restoring the entire Compute Engine instance or an individual disk.

### CMEK handling for entire Compute Engine instance restores

When you restore an entire Compute Engine instance from a backup stored in a CMEK-enabled backup vault, the backup itself is protected by the vault's CMEK. The disks within the restored Compute Engine instance retain their original encryption settings by default, either Google-managed or their original CMEKs. The permissions required to access the vault's CMEK are granted to the Backup and DR service agent as described in [CMEK concepts](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/cmek).

### CMEK handling for individual disk restores

When you choose the **Individual disk** restore scope to restore a single disk from a Compute Engine instance backup, the following behavior occurs:

  * **Default behavior** : the new disk created from the backup attempts to use the **same encryption key as the source disk** from the original Compute Engine instance.

    * If the source disk used Google-managed encryption, the restored disk also uses Google-managed encryption.

    * If the source disk used a specific CMEK, the restored disk attempts to use that same CMEK.

  * **Key unavailability** : if the original CMEK used by the source disk isn't accessible in the target project or region, for example, due to key deletion, permission changes, or cross-region restore, the restore operation fails unless you override the encryption settings.

  * **Overriding encryption settings:** you can change the encryption settings for the restored disk during the restore process using the following instructions:

###  Console 

    * In the **Target Disk Properties** section of the restore wizard, you can modify the **Encryption** settings using one of the following options:

      * Select a different Customer-managed encryption key (CMEK).

      * Switch to Google-managed encryption.

###  gcloud 

    * When using the `gcloud backup-dr backups restore disk` command with either the `--source-instance-boot-disk` or `--source-instance-disk-device-name` flags:

      * To specify a different CMEK for the restored disk, use the `--kms-key` flag:
    
    --kms-key=projects/MY-KEY-PROJECT/locations/us-central1/keyRings/MY-RING/cryptoKeys/MY-NEW-KEY
    

      * To force the restored disk to use Google-managed encryption, use the `--clear-encryption-key` flag.

  * **Permissions for CMEK overrides** :

    * If you override the encryption to use a _new_ or _different_ CMEK, you must ensure that the Compute Engine service agent of the **target project** has the `Cloud KMS CryptoKey Encrypter/Decrypter` role (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) on the specified KMS key. The service agent account format is: `service-TARGET_PROJECT_NUMBER@compute-system.iam.gserviceaccount.com`.

    * This permission is required for Compute Engine to create the new disk encrypted with the chosen key.




Refer to [Restore a Persistent Disk from a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/disk-restore) for more details on disk restore operations and flag usage.

## Restore a backup from a CMEK-enabled backup vault

When you restore a backup from a CMEK-enabled backup vault, the encryption of the restored resource depends on the encryption of the source:

  * **If the source resource was protected by CMEK:** The restored resource defaults to using the same CMEK key as the source. For example: 
    * A Compute Engine persistent disk encrypted with key `K1` is restored to a disk encrypted with `K1`.
    * If a VM has multiple disks, each disk in the restored VM inherits the encryption of its corresponding source disk (CMEK-encrypted disks remain encrypted with their original keys, and Google-managed encrypted disks remain Google-managed).
  * **If the source resource used Google-managed encryption:** The restored resource defaults to using Google-managed encryption.



You can override this default behavior when restoring Compute Engine persistent disks or Compute Engine instances using the API or [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). For example, you can restore a backup of a CMEK-protected resource to a new resource that uses Google-managed encryption, or to a new resource protected by a different CMEK key. To restore to a resource protected by a new CMEK key, ensure the relevant service agent (e.g., Compute Engine Service Agent) for the destination project has `roles/cloudkms.cryptoKeyEncrypterDecrypter` permission on the new destination key.

### Perform a cross-region restore with CMEK

Because Cloud Key Management Service keys are regional, when you perform a cross-region restore (for example, restoring an instance from `asia-south1` to `asia-south2`), the restore operation fails if you use the default behavior. The restored VM's disks cannot be encrypted with the source region's KMS key.

This is a current limitation in the Google Cloud console. To perform a cross-region restore of a CMEK-protected VM, you must use the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), API or Terraform to override the encryption settings and specify a new KMS key in the target region.

To restore to a resource protected by a new CMEK key, perform the following steps:

  1. **Ensure you have a key in the target region:** Ensure you have a Cloud Key Management Service key in the region where you are restoring the VM (in either the target project or a shared KMS project), and create one if you don't.
  2. **Grant KMS permissions:** Grant the **Cloud KMS CryptoKey Encrypter/Decrypter** (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) role on this target key to the Compute Engine Service Agent of the target project where the VM is being restored.

  3. **Perform the restore:** Execute the restore using one of the following methods, overriding the KMS key for each disk:




### gcloud

  1. **Get backup details:** Retrieve the backup name and the device names of the disks from the backup using the `gcloud backup-dr backups list` command:
         
         gcloud backup-dr backups list \
           --project=PROJECT_ID \
           --location=SOURCE_REGION \
           --backup-vault=BACKUP_VAULT_NAME \
           --filter="computeInstanceBackupProperties.sourceInstance~SOURCE_INSTANCE_NAME"
         

Replace the following:

     * PROJECT_ID: the name of the project where the backup vault resides.
     * SOURCE_REGION: the location of the backup vault.
     * BACKUP_VAULT_NAME: the name of the backup vault you want to restore data from.
     * SOURCE_INSTANCE_NAME: the name of the source Compute Engine instance.
  2. **Run the restore command:** Execute the restore command and override the KMS key for each disk using the `--create-disk` parameter.

     1. **Restore a VM with a single disk:**
            
            gcloud backup-dr backups restore compute BACKUP_ID \
              --project=PROJECT_ID \
              --location=SOURCE_REGION \
              --backup-vault=BACKUP_VAULT_NAME \
              --data-source=DATA_SOURCE \
              --name=RESTORED_VM_NAME \
              --target-zone=TARGET_ZONE \
              --target-project=TARGET_PROJECT_ID \
              --create-disk=device-name=DEVICE_NAME,kms-key=projects/KMS_PROJECT_ID/locations/TARGET_REGION/keyRings/KEYRING/cryptoKeys/KEY_NAME
            

Replace the following:

        * BACKUP_ID: the ID of the backup you want to restore.
        * PROJECT_ID: the name of the project where the backup vault resides.
        * SOURCE_REGION: the location of the backup vault.
        * BACKUP_VAULT_NAME: the name of the backup vault you want to restore data from.
        * DATA_SOURCE: the ID of the data source you want to restore data from.
        * RESTORED_VM_NAME: the name of the restored VM.
        * TARGET_ZONE: the zone where the VM is restored.
        * TARGET_PROJECT_ID: the project where the VM is restored.
        * DEVICE_NAME: the device name of disk.
        * KMS_PROJECT_ID: the ID of the project where the Cloud Key Management Service key resides.
        * TARGET_REGION: the region where the Cloud Key Management Service key resides.
        * KEYRING: the name of the Cloud Key Management Service key ring.
        * KEY_NAME: the name of the Cloud Key Management Service key for disk 1.
     2. **Restore a VM with multiple disks:** Provide a separate `--create-disk` flag for each disk:
            
            gcloud backup-dr backups restore compute BACKUP_ID \
              --project=PROJECT_ID \
              --location=SOURCE_REGION \
              --backup-vault=BACKUP_VAULT_NAME \
              --data-source=DATA_SOURCE \
              --name=RESTORED_VM_NAME \
              --target-zone=TARGET_ZONE \
              --target-project=TARGET_PROJECT_ID \
              --create-disk=device-name=DEVICE_NAME_1,kms-key=projects/KMS_PROJECT_ID/locations/TARGET_REGION/keyRings/KEYRING/cryptoKeys/KEY_NAME_1 \
              --create-disk=device-name=DEVICE_NAME_2,kms-key=projects/KMS_PROJECT_ID/locations/TARGET_REGION/keyRings/KEYRING/cryptoKeys/KEY_NAME_2
            

Replace the following:

        * BACKUP_ID: the ID of the backup you want to restore.
        * PROJECT_ID: the name of the project where the backup vault resides.
        * SOURCE_REGION: the location of the backup vault.
        * BACKUP_VAULT_NAME: the name of the backup vault you want to restore data from.
        * DATA_SOURCE: the ID of the data source you want to restore data from.
        * RESTORED_VM_NAME: the name of the restored VM.
        * TARGET_ZONE: the zone where the VM is restored.
        * TARGET_PROJECT_ID: the project where the VM is restored.
        * DEVICE_NAME_1: the device name of disk 1.
        * KMS_PROJECT_ID: the ID of the project where the Cloud Key Management Service key resides.
        * TARGET_REGION: the region where the Cloud Key Management Service key resides.
        * KEYRING: the name of the Cloud Key Management Service key ring.
        * KEY_NAME_1: the name of the Cloud Key Management Service key for disk 1.
        * DEVICE_NAME_2: the device name of disk 2.
        * KEY_NAME_2: the name of the Cloud Key Management Service key for disk 2.



### API

  1. **Get backup details:** Retrieve the backup name and the device names of the disks by sending a `GET` request to list backups:
         
         GET https://backupdr.googleapis.com/v1/projects/PROJECT_ID/locations/SOURCE_REGION/backupVaults/BACKUP_VAULT_NAME/dataSources/DATA_SOURCE/backups
         

  2. **Run the restore API:** Send a `POST` request to the backup's `restore` URI.

     1. **Restore a VM with a single disk:**
            
            POST https://backupdr.googleapis.com/v1/projects/PROJECT_ID/locations/SOURCE_REGION/backupVaults/BACKUP_VAULT_NAME/dataSources/DATA_SOURCE/backups/BACKUP_ID:restore
            

Payload:
            
            {
              "computeInstanceTargetEnvironment": {
                "project": "TARGET_PROJECT_ID",
                "zone": "TARGET_ZONE"
              },
              "computeInstanceRestoreProperties": {
                "name": "RESTORED_VM_NAME",
                "machineType": "projects/TARGET_PROJECT_ID/zones/TARGET_ZONE/machineTypes/e2-medium",
                "disks": [
                  {
                    "deviceName": "DEVICE_NAME",
                    "diskEncryptionKey": {
                    "kmsKeyName": "projects/KMS_PROJECT_ID/locations/TARGET_REGION/keyRings/KEYRING/cryptoKeys/KEY_NAME"
                    }
                  }
                ]
              }
            }
            

     2. **Restore a VM with multiple disks:**
            
            POST https://backupdr.googleapis.com/v1/projects/PROJECT_ID/locations/SOURCE_REGION/backupVaults/BACKUP_VAULT_NAME/dataSources/DATA_SOURCE/backups/BACKUP_ID:restore
            

Payload:
            
            {
              "computeInstanceTargetEnvironment": {
                "project": "TARGET_PROJECT_ID",
                "zone": "TARGET_ZONE"
              },
              "computeInstanceRestoreProperties": {
                "name": "RESTORED_VM_NAME",
                "machineType": "projects/TARGET_PROJECT_ID/zones/TARGET_ZONE/machineTypes/e2-medium",
                "disks": [
                  {
                    "deviceName": "DEVICE_NAME_1",
                    "diskEncryptionKey": {
                      "kmsKeyName": "projects/KMS_PROJECT_ID/locations/TARGET_REGION/keyRings/KEYRING/cryptoKeys/KEY_NAME_1"
                    }
                  },
                  {
                    "deviceName": "DEVICE_NAME_2",
                    "diskEncryptionKey": {
                      "kmsKeyName": "projects/KMS_PROJECT_ID/locations/TARGET_REGION/keyRings/KEYRING/cryptoKeys/KEY_NAME_2"
                    }
                  }
                ]
              }
            }
            




### Terraform

Use the `google_backup_dr_restore_workload` resource

  1. **Restore a VM with a single disk:**
         
         resource "google_backup_dr_restore_workload" "restore_single" {
           location         = "SOURCE_REGION"
           backup_vault_id  = "BACKUP_VAULT_NAME"
           data_source_id   = "DATA_SOURCE"
           backup_id        = "BACKUP_ID"
         
           compute_instance_target_environment {
             project = "TARGET_PROJECT_ID"
             zone = "TARGET_ZONE"
           }
         
           compute_instance_restore_properties {
             name = "RESTORED_VM_NAME"
             machine_type = "zones/TARGET_ZONE/machineTypes/e2-medium"
             disks {
               device_name = "DEVICE_NAME"
               disk_encryption_key {
                 kms_key_name = "projects/KMS_PROJECT_ID/locations/TARGET_REGION/keyRings/KEYRING/cryptoKeys/KEY_NAME"
               }
             }
           }
         }
         

  2. **Restore a VM with multiple disks:**
         
         resource "google_backup_dr_restore_workload" "restore_multi" {
           location         = "SOURCE_REGION"
           backup_vault_id  = "BACKUP_VAULT_NAME"
           data_source_id   = "DATA_SOURCE"
           backup_id        = "BACKUP_ID"
         
           compute_instance_target_environment {
             project = "TARGET_PROJECT_ID"
             zone = "TARGET_ZONE"
           }
         
           compute_instance_restore_properties {
             name = "RESTORED_VM_NAME"
             machine_type = "zones/TARGET_ZONE/machineTypes/TARGET_MACHINETYPE"
             disks {
               device_name = "DEVICE_NAME_1"
               disk_encryption_key {
                 kms_key_name = "projects/KMS_PROJECT_ID/locations/TARGET_REGION/keyRings/KEYRING/cryptoKeys/KEY_NAME_1"
               }
             }
         
             disks {
               device_name = "DEVICE_NAME_2"
               disk_encryption_key {
                 kms_key_name = "projects/KMS_PROJECT_ID/locations/TARGET_REGION/keyRings/KEYRING/cryptoKeys/KEY_NAME_2"
               }
             }
           }
         }
         




If the Cloud Key Management Service key that protects the source workload is unavailable during a restore operation, the restore fails by default. In this case, you must use the API or [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) to override the encryption setting by specifying a new CMEK key or by changing the encryption type to Google-managed encryption for the restored resource.

If the Cloud Key Management Service key version used to encrypt data in the backup vault is disabled or destroyed, you won't be able to restore from that backup.

## The Backup and DR Compute Engine guide

  * [Create and manage a backup plan for vaulted backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create)
  * [Check for the cloud credentials](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/create-cloud-credentials)
  * [Discover and protect Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-ce-inst)
  * [Mount backup images of Compute Engine Persistent Disk](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-snapshot-images-of-cloud-instances)
  * [Restore a Compute Engine instance](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-instance)
  * [Import Persistent Disk snapshot images](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/import-pdsnapshot-images)



## What's next

  * To learn how to [restore a Persistent Disk from a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/disk-restore)
  * To learn how to [perform a selective disk restore from a Compute Engine instance backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/disk-restore#restore-disk-from-compute-instance-backup)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
