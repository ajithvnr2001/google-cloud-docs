---
url: https://docs.cloud.google.com/filestore/docs/cmek/
title: Encrypt data with customer-managed encryption keys (CMEK) \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:14.759888+00:00
---

# Encrypt data with customer-managed encryption keys (CMEK)  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Encrypt data with customer-managed encryption keys (CMEK) Stay organized with collections  Save and categorize content based on your preferences. 

By default, Filestore encrypts customer content at rest. Filestore handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Filestore. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Filestore resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

CMEKs are supported for use with Filestore [instances](https://docs.cloud.google.com/filestore/docs/creating-instances) and [backups](https://docs.cloud.google.com/filestore/docs/backups#backup-creation).

## CMEK options

Filestore supports CMEKs stored as software keys, as hardware keys in an [HSM cluster](https://docs.cloud.google.com/kms/docs/hsm), and as keys stored externally in [Cloud External Key Manager (Cloud EKM)](https://docs.cloud.google.com/kms/docs/ekm).

For more information, see [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs/key-management-service#cmek).

### Disruptions to EKM service

By design, external keys are managed by a third-party; in these circumstances, Google Cloud is not responsible for key availability.

If the [Cloud Key Management Service (Cloud KMS)](https://docs.cloud.google.com/kms/docs/key-management-service) is notified by the [External Key Manager (EKM)](https://docs.cloud.google.com/kms/docs/ekm#terminology) that an external key is unreachable, users receive an `ekm_key_unreachable_detected` notification. For up to one hour, users have limited access to operations on the instance. After one hour, if the key status is unchanged, the following actions apply:

  * The key is disabled.
  * All encrypt and decrypt operations fail.
  * The Filestore instance is suspended.



In some cases, such as an unplanned event like a VM restart, access to the instance may be disrupted prior to one hour.

Unreachable key notifications can be viewed from the Filestore instance details page:

[Go to the Filestore instances page](https://console.cloud.google.com/filestore/instances)

Users also receive `ekm_key_unreachable_detected` notifications on any of the following operations if performed within one hour of the first reported notification:

  * [Revert a snapshot](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances/revert)
  * [Create an instance backup](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.backups/create)
  * [Delete a backup](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.backups/delete)
  * [Restore an instance from a backup](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances/restore)
  * [Update or patch an instance](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances/patch)



## Supported tiers

The following table shows the Filestore [service tiers](https://docs.cloud.google.com/filestore/docs/service-tiers) that support CMEKs:

Tier | CMEK support  
---|---  
Basic HDD | No  
Basic SSD | No  
Zonal | Yes  
Regional | Yes  
Enterprise | Yes  
  
## Create a key ring and key to use with your instance

The key ring and key can be in a different project from the Filestore instance but they must be in the same location. If you already have a Cloud KMS key ring and key that you want to use with Filestore, skip to the next section. Otherwise, follow the instructions on [Creating symmetric encryption keys](https://docs.cloud.google.com/kms/docs/creating-keys) to create a key ring and key.

## Grant key access permission to the Filestore service account

Before you can create a Filestore instance that uses a CMEK, the Filestore [service account](https://docs.cloud.google.com/iam/docs/service-accounts) must have the Cloud KMS CryptoKey Encrypter/Decrypter role (`roles/cloudkms.cryptoKeyEncrypterDecrypter`).

  1. A Filestore service account is created the first time you create a Filestore instance in the project. If you don't already have a Filestore service account, run the following [`services identity create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/identity/create) command:
         
         gcloud beta services identity create --service=file.googleapis.com --project=INSTANCE_PROJECT_NUMBER_OR_ID
         

Replace INSTANCE_PROJECT_NUMBER_OR_ID with the project number or ID of the project where you want to create the Filestore instance.

  2. Assign the Filestore service account the Cloud KMS CryptoKey Encrypter/Decrypter role by running the [`projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command:
         
         gcloud projects add-iam-policy-binding KMS_PROJECT_NUMBER_OR_ID \
             --member serviceAccount:service-INSTANCE_PROJECT_NUMBER@cloud-filer.iam.gserviceaccount.com \
             --role roles/cloudkms.cryptoKeyEncrypterDecrypter
         

Replace the following:

     * KMS_PROJECT_NUMBER_OR_ID with the project number or ID of the project that contains the Cloud KMS key that you want to use.
     * INSTANCE_PROJECT_NUMBER with the project number (not the project ID) of the project where you want to create the Filestore instance.



## Create an instance that uses your Cloud KMS key

###  Google Cloud console 

To create an instance that uses your Cloud KMS key for data encryption:

  1. In the Google Cloud console, go to the Filestore instances page.

[Go to the Filestore instances page](https://console.cloud.google.com/filestore/instances)

  2. Click **Create Instance**

  3. Select an instance tier that supports CMEKs and fill out all other required and optional fields as you normally would.

  4. Click **Show advanced options**.

  5. Select the **Use a customer-managed encryption key (CMEK)** checkbox.

  6. Select the Cloud KMS key that you want to use for the instance.

  7. Click **Create**.




###  gcloud CLI 

To create a Filestore instance that uses your Cloud KMS key for data encryption, specify the `--kms-key` flag in the [`filestore instances create`](https://docs.cloud.google.com/filestore/docs/creating-instances#gcloud) command:
    
    
    gcloud filestore instances create nfs-server \
        --tier=<var>TIER</var> \
        --location=us-central1 \
        --file-share=name="vol1",capacity=1TiB \
        --network=name="default" \
        **--kms-key =KMS_KEY**
    

Replace the following:

  * TIER with a Filestore tier that supports CMEKs.
  * KMS_KEY with the fully qualified name of the Cloud KMS key that you want to use. Alternatively, you can specify each argument separately in the format:


    
    
    --kms-key=KMS_KEY : --kms-keyring=KEY_RING --kms-location=KMS_REGION --kms-project=KMS_PROJECT_NUMBER_OR_ID
    

Replace the following:

  * KMS_KEY with the name of the Cloud KMS key.
  * KMS_PROJECT_NUMBER_OR_ID with the project number or ID of the project where the key is created.
  * KMS_KEY_RING with the name of the key ring.
  * KMS_REGION with the region of the key ring. The key ring and instance must be located in the same region.



### Get a list of keys

You can get a list of keys by running the [`kms keys list`](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/list) command:
    
    
      gcloud kms keys list \
      --project=KMS_PROJECT_NUMBER_OR_ID \
      --keyring=KEY_RING \
      --location=KMS_REGION
    

Replace the following:

  * KMS_PROJECT_NUMBER_OR_ID with the project number or ID of the project where the key is created.
  * KEY_RING with the name of the key ring.
  * KMS_REGION with the region of the key ring.



The **Name** column of the output gives the fully qualified name of existing keys. For example:
    
    
    projects/example-project/locations/us-central1/keyRings/example-ring/cryptoKeys/example-key
    

## Get instance key information

The following sections cover how to get instance key information.

### List instances that use a particular Cloud KMS key

You can list Filestore instances that use a particular key by running the [`instances list`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/list) command:
    
    
    gcloud filestore instances list --filter="kmsKeyName=KMS_KEY"
    

Replace KMS_KEY with the fully qualified name of the key that you want to use.

**Example:**
    
    
    gcloud filestore instances list \
        --filter="kmsKeyName=projects/example-project/locations/us-central1/keyRings/example-ring/cryptoKeys/example-key"
    

The output looks like:
    
    
    INSTANCE_NAME LOCATION    TIER       CAPACITY_GB FILE_SHARE_NAME IP_ADDRESS   STATE CREATE_TIME
    nfs-server    us-central1 ENTERPRISE 1024        vol1            10.166.108.2 READY 2021-08-12T11:38:56
    

### Get Cloud KMS key information for an instance

Use one of the following methods to get Cloud KMS key information for a Filestore instance:

###  Google Cloud console 

  1. Go to the Filestore instances page.

[Go to the Filestore instances page](https://console.cloud.google.com/filestore/instances)

  2. Click the instance ID to open the instance details page.

  3. Click the **Overview** tab.




If the instance encrypts data using a Cloud KMS key instead of a Google-owned and Google-managed encryption key, the key name is displayed in the **Encryption key** field.

###  gcloud CLI 

Run the following [`instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/describe) command:
    
    
    gcloud filestore instances describe INSTANCE_ID \
       --location=INSTANCE_LOCATION
    

Replace the following:

  * INSTANCE_ID with the instance ID of the Filestore instance that you want to get information about.
  * INSTANCE_LOCATION with the region or zone where the instance is located.



The output looks like:
    
    
    createTime: '2021-08-12T11:38:56.851157387Z'
    fileShares:
    - capacityGb: '1024'
      name: vol1
    **kmsKeyName: projects/example-project/locations/us-central1/keyRings/example-ring/cryptoKeys/example-key**
    labels:
      key: val
    name: projects/consumer-project/locations/us-central1/instances/nfs-server
    networks:
    - ipAddresses:
      - 10.0.100.2
      modes:
      - MODE_IPV4
      network: network
      reservedIpRange: 10.166.108.0/23
    state: READY
    tier: ENTERPRISE
    

## Disable or destroy a Cloud KMS key that's used by an instance

If a change in Cloud KMS key state is detected, the instance automatically stops serving data. Some examples include the following:

  * [Disabling](https://docs.cloud.google.com/kms/docs/enable-disable#disable) a key or key version.
  * [Destroying](https://docs.cloud.google.com/kms/docs/destroy-restore#destroy) a key or key version.
  * Modifying a key's permissions.



This detection typically happens within a few minutes of the change in key state, but in some cases can take up to one hour.

Once an instance is stopped, all access to file share data and any snapshots is blocked. Stopped instances continue to be billed until they're [deleted](https://docs.cloud.google.com/filestore/docs/deleting-instances).

## Starting a stopped instance

**Important:** If an instance is stopped for more than four weeks, starting it again is done on a best effort basis and might not be possible.

If a stopped Filestore instance uses a Cloud KMS key for data encryption, all key versions of the key must be [enabled](https://docs.cloud.google.com/kms/docs/enable-disable#enable) or [restored](https://docs.cloud.google.com/kms/docs/destroy-restore#restore) before restarting the instance.

Once the Cloud KMS key status is enabled, the instance will automatically detect key changes and restart without any additional action, typically within 20 minutes.

## CMEK support for backup chains

You can use CMEKs to encrypt not only your Filestore instances but also your [backup chains](https://docs.cloud.google.com/filestore/docs/backup-restore#encryption).

CMEK support is not available for basic -tier backups.

Backup chains reside in a single bucket and region. To store and encrypt backup data in a region outside of the source instance, users must apply two separate CMEKs: one for the instance and one for the backup chain. Some requirements apply:

  * A CMEK must reside in the same region as the backup chain it encrypts.
  * A single CMEK is applied to the bucket where the backup chain is stored and cannot be combined or replaced.



### Key rotation limitations

During key rotation, new encryption keys are created to replace the existing keys. The following actions related to key rotation might prevent you from restoring a backup chain:

  * Deactivating a key or key version.
  * Destroying a key or key version.
  * Modifying key permissions.



These actions don't prevent backups from being created in the chain.

If you can't restore your backup chain, perform the following steps:

  1. Delete all backups.
  2. Start a new chain. You can use either of the following options: 
     * Create your backup in a different location with the same CMEK.
     * Create your backup in the same location with a new CMEK.



For more information, see [Backups overview](https://docs.cloud.google.com/filestore/docs/backups).

## What's next

  * Learn how to [apply a CMEK organization policy](https://docs.cloud.google.com/filestore/docs/cmek-organization-policy).
  * Learn more about [CMEK](https://docs.cloud.google.com/kms/docs/cmek).
  * Learn about [encryption in transit in Google Cloud](https://docs.cloud.google.com/security/encryption-in-transit).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
