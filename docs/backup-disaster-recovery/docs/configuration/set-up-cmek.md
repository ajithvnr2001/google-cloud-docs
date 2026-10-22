---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/set-up-cmek/
title: Use customer-managed encryption keys to protect your backups \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:38:50.515509+00:00
---

# Use customer-managed encryption keys to protect your backups  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/set-up-cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Use customer-managed encryption keys to protect your backups Stay organized with collections  Save and categorize content based on your preferences. 

This guide explains how to enhance backup security by using Customer-Managed Encryption Keys (CMEK) with Backup and DR. You'll learn to grant necessary permissions, create CMEK-enabled backup vaults, and apply these to your resources, ensuring your backup data is protected with keys you control in Cloud Key Management Service. This is essential for meeting compliance requirements and gaining greater control over your data encryption.

For more information about CMEK concepts and supported workload types in Backup and DR, see [Overview of customer-managed encryption keys (CMEK) with Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/cmek).

## Before you begin

Before you begin using CMEK, complete the following steps:

  1. **Enable the Cloud Key Management Service API**.

[Enable the API](https://console.cloud.google.com/apis/library/cloudkms.googleapis.com?project=PROJECT_ID)

Replace `PROJECT_ID` with the ID of the project where you will manage your keys.

  2. **[Create a Cloud Key Management Service key ring and key](https://docs.cloud.google.com/kms/docs/creating-keys)** : when creating your key, ensure that you select a location that matches the location of your backup vault. A backup vault in a region must use a key from the same region.

  3. **Create the Backup and DR service agent if needed** : the service agent is typically created automatically when the first Backup and DR resource (like a management console or backup vault) is created in a project. If you need to grant permissions to the service agent _before_ creating any Backup and DR resources, trigger its creation manually:
         
         gcloud beta services identity create --service=backupdr.googleapis.com --project=PROJECT_ID
         

Replace `PROJECT_ID` with the ID of your project.




### Permissions required for a CMEK-enabled backup vault

The Backup and DR service agent requires permissions to use the designated Cloud KMS key to encrypt and decrypt data within the backup vault.

**Important:** The Backup and DR service agent (`service-PROJECT_NUMBER@gcp-sa-backupdr...`) is distinct from the _backup vault service account_ (`bvault-SA-VAULT_ID@PROJECT_ID.iam.gserviceaccount.com`). The `gcp-sa-backupdr` service agent needs access to the CMEK key for encrypting and decrypting vault data. The per-vault service account is granted permissions on source projects to access and backup workloads (like Compute Engine instances) and is _not_ used for the vault's CMEK operations.

To get the permissions that you need to encrypt and decrypt data within the backup vault using CMEK, ask your administrator to grant you the following IAM roles on the Cloud KMS key designated for the backup vault: 

  * To the Backup and DR service agent (`service-VAULT_PROJECT_NUMBER@gcp-sa-backupdr.iam.gserviceaccount.com`): Cloud KMS CryptoKey Encrypter/Decrypter (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) 

Replace `VAULT_PROJECT_NUMBER` with the project number of the project containing your backup vault.




For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to encrypt and decrypt data within the backup vault using CMEK. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to encrypt and decrypt data within the backup vault using CMEK:

  * To encrypt data with the key version: `cloudkms.cryptoKeyVersions.useToEncrypt`
  * To decrypt data with the key version: `cloudkms.cryptoKeyVersions.useToDecrypt`
  * To get metadata about key locations: `cloudkms.locations.get`
  * To list key locations: `cloudkms.locations.list`
  * To get metadata about the key's project: `resourcemanager.projects.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To grant the required role to the `gcp-sa-backupdr` service agent, use the following instructions:

### Console

  1. In the Google Cloud console, navigate to the **Backup Vaults** page.

[Go to Backup Vaults](https://console.cloud.google.com/backupdr/backup-vaults)

  2. Click **Create Backup Vault**.

  3. Enter the necessary details for your backup vault, such as name and location.

  4. In the **Encryption** section, select **Customer-managed encryption key (CMEK)** to use your own key.

  5. Click **Select a customer-managed key** and choose the Cloud KMS key you want to use from the picker.

  6. **Service Agent Permission Grant** :

     * After selecting a key, the console checks if the Backup and DR service agent has permission to use it. The service agent is named service-VAULT_PROJECT_NUMBER@gcp-sa-backupdr.iam.gserviceaccount.com.

     * If you have sufficient permissions on the key such as `roles/cloudkms.admin`, and the service agent doesn't already have access, the console may offer to automatically grant the `roles/cloudkms.cryptoKeyEncrypterDecrypter` role to the Backup and DR service agent for the selected key.

     * If prompted, confirm the grant to allow Backup and DR to encrypt and decrypt data in the vault using your CMEK.

     * If the automatic grant option is not available, or if you lack permission to grant roles, you must manually grant the `roles/cloudkms.cryptoKeyEncrypterDecrypter` role to the service agent. See the `gcloud` tab for instructions.

  7. Configure any other backup vault settings as needed.

  8. Click **Create**.




### gcloud
    
    
    gcloud kms keys add-iam-policy-binding KEY_NAME \
        --location=KMS_LOCATION \
        --keyring=KEY_RING \
        --member=serviceAccount:service-VAULT_PROJECT_NUMBER@gcp-sa-backupdr.iam.gserviceaccount.com \
        --role=roles/cloudkms.cryptoKeyEncrypterDecrypter \
        --project=KMS_PROJECT_ID
    

Replace the variables:

  * `KEY_NAME`: the name of your CMEK key.

  * `KMS_LOCATION`: the region of your key ring.

  * `KEY_RING`: the name of your key ring.

  * `VAULT_PROJECT_NUMBER`: the project number where the backup vault resides.

  * `KMS_PROJECT_ID`: the project ID where the CMEK key is managed.




Granting the role on the specific key is recommended, following the principle of least privilege.

### Permissions required for backing up existing CMEK-protected resources

If the source resource you are backing up is already encrypted with a _different_ CMEK key, such as a Compute Engine instance with CMEK-encrypted disks, the service agent of the _source resource's service_ such as Compute Engine Service Agent needs permission to access the key protecting that source resource.

**Note:** Usually, the source service agent such as the Compute Engine Service Agent already has the necessary permissions on the resource's CMEK key for its normal operations. You typically don't need to grant this permission separately for Backup and DR to back up the resource.

To get the permissions that you need to allow the source service to access its CMEK key during backup operations, ask your administrator to grant you the following IAM roles on the CMEK key(s) protecting the source resource such as Compute Engine disks: 

  * To the service agent of the service hosting the source resource: Typically Cloud Key Management Service CryptoKey Encrypter/Decrypter (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) 

For example, for a CMEK-encrypted Compute Engine instance, the principal is the Compute Engine Service Agent of the source instance's project 




For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to allow the source service to access its CMEK key during backup operations. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to allow the source service to access its CMEK key during backup operations:

  * To encrypt data with the key version: `cloudkms.cryptoKeyVersions.useToEncrypt`
  * To decrypt data with the key version: `cloudkms.cryptoKeyVersions.useToDecrypt`
  * To get metadata about key locations: `cloudkms.locations.get`
  * To list key locations: `cloudkms.locations.list`
  * To get metadata about the key's project: `resourcemanager.projects.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Use CMEK with Backup and DR

  1. **Create a CMEK-enabled backup vault.** When [creating a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create), select the **Customer-managed encryption key (CMEK)** option in the **Encryption type** section and choose the Cloud Key Management Service key you created. CMEK can only be enabled during vault creation. It cannot be added, removed, or changed on an existing vault.

  2. **Create a backup plan.** When [creating a backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create), select the CMEK-enabled backup vault you created as the target.

  3. **Apply the backup plan to resources.** Compatibility depends on the resource type and its encryption:

     * **Compute Engine instances:**

Instance disk encryption | Backup vault encryption | Supported | Notes  
---|---|---|---  
All Google-managed | Google-managed | Yes |   
All Google-managed | CMEK | Yes | Backups will be encrypted with the Backup Vault's CMEK.  
Any disk CMEK-encrypted | Google-managed | No | Backups of instances with CMEK-encrypted disks require a CMEK-enabled backup vault.  
Any disk CMEK-encrypted | CMEK | Yes | The backup vault CMEK can be different from the disk CMEK.  
     * **Persistent Disk volumes:**

       * Backups of Persistent Disk volumes always retain the encryption method of the source disk.

       * If the source Persistent Disk uses Google-managed encryption, the backup will also use Google-managed encryption.

       * If the source Persistent Disk uses CMEK, the backup will be protected by the _same_ CMEK key version as the source disk.

       * The backup vault's encryption setting, CMEK or Google-managed, does not alter the encryption of the Persistent Disk backup data itself. However, organization policies might still apply, see CMEK organization policies.




## Restoring CMEK-encrypted backups

When restoring a workload from a CMEK-encrypted backup, the restored resource defaults to using the same Cloud Key Management Service key that protected the source resource at the time of backup. You have the option to specify a different Cloud Key Management Service key for the target resource during the restore process.

**Note:** During cross-region restores to a new instance, it's required to re-encrypt the restored Cloud SQL instance with a different Cloud Key Management Service key that resides in the restored target's region (not applicable when overwriting an existing instance).

## How Cloud Key Management Service key rotation affects backup restorability

When you rotate a key, Cloud Key Management Service creates a new key version, which becomes the primary version. Backup and DR uses this primary key version to encrypt all _new_ backups for backup vaults configured with that key.

Existing backups remain encrypted with the key version they were originally created with. To restore any backup, the specific key version used to encrypt it must be available and enabled in Cloud Key Management Service.

### Consequences of key version inaccessibility

  * Disabling or destroying a key version renders any backups encrypted with that version inaccessible.

  * If Backup and DR cannot access your CMEK key due to it being disabled, destroyed, or having its permissions revoked, the following outcomes may occur:

    * New backups to the CMEK-enabled backup vault will fail.

    * Restores from backups will fail if the specific key version for that backup is inaccessible.

    * Creation of new backup vaults using an inaccessible key will fail.




Re-enabling a disabled key version restores access. Destroying a key version is permanent and results in irreversible data loss for backups encrypted with that version.

## How CMEK organization policies apply

You can use [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) to enforce CMEK requirements for Backup and DR resources. See [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy) for more information.

### backup vault creation constraints

  * **`constraints/gcp.restrictNonCmekServices`:** if enforced for `backupdr.googleapis.com`, all new backup vaults must be created with CMEK.

  * **`constraints/gcp.restrictCmekCryptoKeyProjects`:** if enforced, CMEK-enabled backup vaults must use keys from an allowed project or folder.




### Backup operations constraints

  * **`constraints/gcp.restrictNonCmekServices`** : if enforced for `backupdr.googleapis.com`:

    * **Compute Engine instance backups** : fail if the target backup vault uses Google-managed encryption.

    * **Persistent Disk backups** : fail if the source Persistent Disk uses Google-managed encryption.

  * **`constraints/gcp.restrictCmekCryptoKeyProjects`** : if enforced:

    * **Compute Engine instance backups** : if the target backup vault is CMEK-encrypted, its key must be from an allowed project or folder.

    * **Persistent Disk backups** : if the source Persistent Disk is CMEK-encrypted, its key must be from an allowed project or folder.




## What's next

  * Learn how to [Create and manage backup vaults](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/backup-vault).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
