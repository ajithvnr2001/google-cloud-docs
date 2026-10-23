---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-cmek/
title: About Backup for GKE CMEK encryption \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:28.688769+00:00
---

# About Backup for GKE CMEK encryption  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  About Backup for GKE CMEK encryption Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

By default, Backup for GKE encrypts customer content at rest. Backup for GKE handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Backup for GKE. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Backup for GKE resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

## Overview

There are two types of user data artifacts that are produced and stored by Backup for GKE:

  * **Config backup** : a set of Kubernetes resource descriptions extracted from the API server of the cluster undergoing backup, capturing the cluster state.
  * **Volume backups** : a set of volume backups that correspond to `PersistentVolumeClaim` resources found in the config backup.



By default, all backup artifacts produced by Backup for GKE are encrypted at rest using a Google-supplied key.

However, you may choose to have these artifacts encrypted using a customer-managed encryption key (CMEK) managed with the [Cloud Key Management Service](https://docs.cloud.google.com/kms).

## Enable CMEK encryption

Enabling CMEK encryption involves two steps:

  * Designate a key for encrypting backups produced for a [`BackupPlan`](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-plan).

  * Grant access by the appropriate service accounts to the appropriate keys.




For any particular backup scenario, there are potentially three CMEK keys involved:

  * `bplan_key`: This is the key that you reference when creating or updating the `BackupPlan`. When possible, this key that will be used when encrypting all backup artifacts. This key must live in the same region as the `BackupPlan` itself (see [About resource locations](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-locations)).

  * `orig_disk_key`: If you have encrypted your persistent disk volumes using a CMEK key, then the volume backups that Backup for GKE produces for those volumes will be encrypted with this key, even if a different key is registered with the `BackupPlan`.

  * `new_disk_key`: This is the CMEK key you want to use for encrypting volumes you have restored from backup. This is referenced by the `StorageClass` in the restore's target cluster.




There are three different service accounts that might require access to CMEK keys:

  * `agent_robot`: This service account must be granted access to the `bplan_key`. This service account will have the form: `service-PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com`, where `PROJECT_NUMBER` is the number of your Google Cloud project.

  * `gkebackup_service_agent`: When backing up non-CMEK-encrypted volumes, this service account must be granted access to the `bplan_key`. When backing up CMEK-encrypted volumes, this service account must be granted access to the `orig_disk_key`. This service account will have the form: `service-PROJECT_NUMBER@gcp-sa-gkebackup.iam.gserviceaccount.com`, where `PROJECT_NUMBER` is the number of your Google Cloud project.

  * `compute_service_agent`: This service account is used when creating new encrypted volumes for a cluster and must be granted access to the `new_disk_key`. This service account will have the form: `service-PROJECT_NUMBER@compute-system.iam.gserviceaccount.com`, where `PROJECT_NUMBER` is the number of your Google Cloud project.




If [diskEncryptionKey.kmsKeyServiceAccount](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionDisks) is set for the disks, you will need to perform the following steps before creating a backup:

  * Disable the organization policy `iam.disableCrossProjectServiceAccountUsage` to [enable service account impersonation across projects](https://docs.cloud.google.com/iam/docs/attach-service-accounts#enabling-cross-project):
        
        gcloud resource-manager org-policies disable-enforce \
              iam.disableCrossProjectServiceAccountUsage
              --project=PROJECT_ID
        

  * Grant `gkebackup_service_agent` the `roles/iam.serviceAccountTokenCreator` role to [create short-lived credentials](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role):
        
        gcloud iam service-accounts add-iam-policy-binding \
            # Replace the email with the value from
            # `diskEncryptionKey.kmsKeyServiceAccount`
            your-kms-key-service-acount@PROJECT_ID.iam.gserviceaccount.com \
            --member=service-PROJECT_NUMBER@gcp-sa-gkebackup.iam.gserviceaccount.com \
            --role=roles/iam.serviceAccountTokenCreator
        




If you're performing a cross-project backup or cross-project restore operation, there are three project names that must be listed:

  * `cluster_project`: the project that contains the cluster that you want to back up.

  * `backup_project`: the project where you want your backups to be stored.

  * `restore_project`: the project that contains the restore's target cluster.




The following table summarizes which service accounts must be granted access to which keys in various scenarios:

Artifact | Service account | Project number | Key  
---|---|---|---  
config backup cluster | _agent_robot_ | 

  * _cluster_project_ (during backup)
  * _restore_project_ (during restore)

| _bplan_key_  
backup of CMEK-encrypted volume | _gkebackup_service_agent_ | _backup_project_ | _orig_disk_key_  
backup of google-encrypted volume | _gkebackup_service_agent_ | _backup_project_ | _bplan_key_  
new CMEK-encrypted volume created during restore | _compute_service_agent_ | _restore_project_ | _new_disk_key_  
  
You can choose to grant access to keys at a project level, which grants access to all keys in that project, or to the individual key.

## Grant project level access

You can grant access to keys at a project level, which grants access to all keys in that project.

Use the following instructions to grant access at a project level.

### Console

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Click **Grant access**.

  3. In the **New principals** field, enter the email address of the service account.

  4. From the **Select a role** list, select the **Cloud KMS CryptoKey Encrypter/Decrypter** role.

  5. Click **Save**.




### gcloud

  1. Grant access at a project level.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member serviceAccount:service-PROJECT_NUMBER@gcp-sa-gkebackup.iam.gserviceaccount.com \
         --role roles/cloudkms.cryptoKeyEncrypterDecrypter
         

Replace the following:

     * `PROJECT_ID`: the ID of the project you want to grant access to.
     * `PROJECT_NUMBER`: the number of the project you want to grant access to.



### Terraform

  1. Grant access at a project level.
         
         resource "google_project_iam_member" "example_iam_member" {
         project = "PROJECT_ID"
         role    = "roles/cloudkms.cryptoKeyEncrypterDecrypter"
         member  = "serviceAccount:service-PROJECT_NUMBER@gcp-sa-gkebackup.iam.gserviceaccount.com"
         }
         

Replace the following:

     * `PROJECT_ID`: the ID of the project you want to grant access to.
     * `PROJECT_NUMBER`: the number of the project you want to grant access to.



## Grant access at key level

Use the following instructions to grant access at the individual key level.

### Console

  1. In the Google Cloud console, go to the **Key management** page.

[Go to Key management](https://console.cloud.google.com/security/kms/keyrings)

  2. Click the name of the key ring.

  3. Click the name of the key.

  4. Click the **Permissions** tab.

  5. Click **Grant access**.

  6. In the **New principals** field, enter the email address of the service account.

  7. From the **Select a role** list, select the **Cloud KMS CryptoKey Encrypter/Decrypter** role.

  8. Click **Save**.




### gcloud

  1. Grant access at the individual key level.
         
         gcloud kms keys add-iam-policy-binding KEY_NAME \
         --keyring KEY_RING \
         --location LOCATION \
         --member "serviceAccount:service-PROJECT_NUMBER@gcp-sa-gkebackup.iam.gserviceaccount.com" \
         --role roles/cloudkms.cryptoKeyEncrypterDecrypter
         

Replace the following:

     * `KEY_NAME`: the name of the key.
     * `KEY_RING`: the name of the key ring that contains the key.
     * `LOCATION`: the Cloud KMS location of the key ring.
     * `PROJECT_NUMBER`: the number of the project you want to grant access to.



### Terraform

  1. Grant access at the individual key level.
         
         resource "google_kms_crypto_key_iam_member" "crypto_key_iam_member" {
         crypto_key_id = "projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME"
         role          = "roles/cloudkms.cryptoKeyEncrypterDecrypter"
         member        = "serviceAccount:service-PROJECT_NUMBER@gcp-sa-gkebackup.iam.gserviceaccount.com" 
         }
         

Replace the following:

     * `PROJECT_ID`: the ID of the project you want to grant access to.
     * `LOCATION`: the Cloud KMS location of the key ring.
     * `KEY_RING`: the name of the key ring that contains the key.
     * `KEY_NAME`: the name of the key.
     * `PROJECT_NUMBER`: the number of the project you want to grant access to.



## Usage considerations and limitations

  * If you want to back up a CMEK-encrypted volume, you must grant access to that disk's key, even if you don't enable CMEK encryption in your `BackupPlan`.

  * CMEK keys must be in the same region as the `BackupPlan` to ensure that a regional outage won't remove access to the key while backups are still accessible. However, this constraint cannot be enforced for keys shared with encrypted volumes. When encrypted volumes are involved, it is possible that a restoration may fail even when a backup is available, because the disk encryption key may not be stored in the same region as the backup.




## Use and manage external keys

You can use Cloud External Key Manager (Cloud EKM) to create and manage external keys. External keys are pointers to keys that reside outside of Google Cloud. These keys reside with a [supported external key management partner](https://docs.cloud.google.com/kms/docs/ekm#supported_partners). For more information, see [Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm).

After you create an external key with Cloud EKM, you can apply it to a new backup plan by providing the ID of that key when [creating a new backup plan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-plan#create). This procedure is the same as applying a Cloud KMS key to a new backup plan.

You can use Key Access Justifications as part of Cloud EKM. Key Access Justifications lets you view the reason for each Cloud EKM request. Additionally, based on the justification provided, you can automatically approve or deny a request. For more information, see [Overview](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview).

**Note:** To use Key Access Justifications with Cloud EKM, you can [create a new backup plan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-plan#create). If you need to apply Key Access Justifications to an existing backup plan, [update the backup plan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-plan#update_a_backup_plan).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
