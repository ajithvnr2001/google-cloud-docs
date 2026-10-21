---
url: https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption/
title: Protect resources with Cloud KMS keys \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:53.267663+00:00
---

# Protect resources with Cloud KMS keys  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Protect resources with Cloud KMS keys Stay organized with collections  Save and categorize content based on your preferences. 

You can protect your Compute Engine disks, snapshots, andmachine images by using Cloud Key Management Service keys instead of Google-owned and Google-managed encryption keys. Using Cloud KMS keys lets you control and manage your encryption keys and meet specific compliance or regulatory requirements. For more information, see [Customer-managed encryption keys](https://docs.cloud.google.com/kms/docs/cmek).

Keys managed in Cloud KMS are called _customer-managed encryption keys (CMEKs)_. This document describes how to use manually-created CMEKs to create and protect Compute Engine [disks](https://docs.cloud.google.com/compute/docs/disks), [machine images](https://docs.cloud.google.com/compute/docs/images), [instant snapshots](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots), and [standard snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots).

To use CMEKs created by Cloud KMS Autokey, see [Create protected resources using Cloud KMS Autokey](https://docs.cloud.google.com/kms/docs/create-resource-with-autokey).

## Before you begin

  * Understand [disks](https://docs.cloud.google.com/compute/docs/disks), [images](https://docs.cloud.google.com/compute/docs/images), [standard snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots), and [virtual machine (VM) instances](https://docs.cloud.google.com/compute/docs/instances).

  * Decide whether you are going to run Compute Engine and Cloud KMS in the same Google Cloud project, or in different projects. For information about Google Cloud project IDs and project numbers, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

  * For the Google Cloud project that runs Cloud KMS, do the following: 
    1. Enable the Cloud KMS API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com)

  * To create a new Hyperdisk Balanced volume in Confidential mode, ensure your use case is supported by reviewing the relevant [Limitations](https://docs.cloud.google.com/compute/docs/disks/disk-encryption#conf_hdb_limitations) and [supported regions](https://docs.cloud.google.com/compute/docs/disks/disk-encryption#conf_hdb_regions). 
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles and permissions

The Compute Engine Service Agent has the following form:
    
    
    service-PROJECT_NUMBER@compute-system.iam.gserviceaccount.com
    

You can use the Google Cloud CLI to assign the role:
    
    
    gcloud projects add-iam-policy-binding KMS_PROJECT_ID \
        --member serviceAccount:service-PROJECT_NUMBER@compute-system.iam.gserviceaccount.com \
        --role roles/cloudkms.cryptoKeyEncrypterDecrypter
    

Replace the following:

  * `KMS_PROJECT_ID`: the ID of your Google Cloud project that runs Cloud KMS (even if this is the same project running Compute Engine)
  * `PROJECT_NUMBER`: the project number (not Google Cloud project ID) of your Google Cloud project that runs the Compute Engine resources



To ensure that the Compute Engine Service Agent has the necessary permissions to protect resources by using Cloud KMS keys, ask your administrator to grant the [Cloud KMS CryptoKey Encrypter/Decrypter ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypterDecrypter) (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) IAM role to the Compute Engine Service Agent on your project. **Important:** You must grant this role to the Compute Engine Service Agent, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors.  For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to protect resources by using Cloud KMS keys. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to protect resources by using Cloud KMS keys:

  * To rotate an encryption key protecting a disk: `compute.disks.updateKmsKey`
  * To rotate an encryption key protecting a snapshot: `compute.snapshots.updateKmsKey`



Your administrator might also be able to give the Compute Engine Service Agent these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Encryption specifications

The Cloud KMS keys used to help protect your data in Compute Engine are AES-256 keys. These keys are key encryption keys, and they encrypt the data encryption keys that encrypt your data, not the data itself.

The data on the disks is encrypted using Google-owned and Google-managed encryption keys. For specifications related to the default encryption in Google Cloud, see [Default encryption at rest](https://cloud.google.com/security/encryption/default-encryption#googles_default_encryption) in the Security documentation.

With Confidential mode for Hyperdisk Balanced and Cloud HSM, the data encryption key (DEK) has additional security properties with hardware-backed enclaves.

## Limitations

  * You can't encrypt existing resources with CMEKs. You can only encrypt disks, images, and snapshots with CMEKs when you create them.

  * When you create a disk from a CMEK-encrypted instant snapshot, you must specify the key used to encrypt the source disk. You don't have to specify the key when working with other CMEK-encrypted resources such as disk clones and standard snapshots.

  * When you create a regionally scoped snapshot ([Preview](https://cloud.google.com/products/#product-launch-stages)) from a disk encrypted with a CMEK, you must create the snapshot with a regional CMEK that's in the same location as the snapshot. This ensures regional isolation of your snapshot and increases your snapshot's reliability.

  * You can't use your own keys with Local SSD disks because the keys are managed by Google Cloud infrastructure and deleted when the VM is terminated.

  * Regional resources (disks) can only be encrypted by a key in one of the following Cloud KMS locations:

    * A key in the same region as the disk.
    * A multi-regional key in the same geographical location as the disk.
    * A key in the global location.

For example, a disk in zone `us-west1-a` can be encrypted by a key in the global location, the `us-west1` region, or the `us` multi-region.

Global resources (such as images and snapshots) can be encrypted by keys in any location. For more information, see [Types of locations for Cloud KMS](https://docs.cloud.google.com/kms/docs/locations#location_types).

**Note:** We recommended using keys in the same location as the resources you want to protect. This approach helps to decrease latency and prevents cases where resources depend on services spread across multiple failure domains.
  * You can't change or remove the encryption key for an image or instant snapshot.

  * You can't remove a disk or snapshot's encryption key, or change the key from a CMEK to a Google-owned and managed key. Instead, create a copy of the disk or snapshot and specify a new encryption type for the copy.

For more information, see Remove the CMEK from a disk and Remove the CMEK from a snapshot.

  * You can't rotate or change the CMEK of online Confidential Hyperdisk volumes or online Hyperdisk volumes that are attached to unsupported machine types.

  * You can rotate or change the CMEK on only the following disk types:

    * All Persistent Disk volumes
    * Disks and snapshots that were not created with the Terraform provider for Google Cloud
    * Hyperdisk volumes that were created from an instant snapshot
    * Offline Hyperdisk volumes
    * Offline Confidential Hyperdisk volumes
    * Online Hyperdisk volumes that are attached to first- or second-generation machine types
    * Online Hyperdisk volumes that are attached to the following third- or fourth-generation machine types:

      * A3
      * A4
      * Z3
      * H4D
      * all TPU versions
      * Bare metal A4X, C4, C4A, C4D, C3, and X4 machine types
  * To change or rotate the CMEK for a disk or snapshot, you must use either the gcloud CLI or REST; you can't use the Google Cloud console.

  * To create a snapshot using a CMEK that is different from the CMEK used to encrypt the source disk, you must use either the gcloud CLI or REST; you can't use the Google Cloud console.

  * If you use the Terraform provider for Google Cloud to create or manage CMEK-encrypted disks and snapshots, then you can't change or rotate the CMEK. You shouldn't attempt to change or rotate the CMEK using the gcloud CLI or REST. 

  * You can't change the key for Hyperdisk volumes that you created by cloning a disk, unless you have deleted the source disk and all other clones of the source disk.




## Manual or automated key creation

You can either create Cloud KMS keys manually or use Cloud KMS Autokey. Autokey simplifies creating and managing Cloud KMS keys by automating provisioning and assignment. With Autokey, you don't need to provision key rings, keys, and service accounts ahead of time. Instead, they are generated on demand as part of Compute Engine resource creation. For more information, see the [Autokey overview](https://docs.cloud.google.com/kms/docs/autokey-overview).

### Manually create key ring and key

For the Google Cloud project that runs Cloud KMS, create a key ring and a key as described in [Creating key rings and keys](https://docs.cloud.google.com/kms/docs/creating-keys).

## Encrypt a new Persistent Disk with CMEK

You can encrypt a new Persistent Disk by supplying a key during VM or disk creation.

### Console

  1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. Click **Create disk** and enter the properties for the new disk.
  3. Under **Encryption** , select **Customer-managed key**.
  4. In the drop-down menu, select the Cloud KMS key that you want to use to encrypt this disk.
  5. To create the disk, click **Create**.



###  gcloud 

Create an encrypted disk by using the [`gcloud compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create), and specify the key using the `--kms-key` flag.
    
    
    gcloud compute disks create DISK_NAME \
      --kms-key projects/KMS_PROJECT_ID/locations/REGION/keyRings/KEY_RING/cryptoKeys/KEY
    

Replace the following:

  * `DISK_NAME`: the name of the new disk
  * `KMS_PROJECT_ID`: the project that owns the Cloud KMS key
  * `REGION`: the region where the key is located
  * `KEY_RING`: the name of the key ring that includes the key
  * `KEY`: the name of the key used to encrypt the disk

**Note:** If you're creating a regional Persistent Disk, you must assign the disk replicas to two different zones by specifying the `--replica-zones` flag.

###  REST 

Construct a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). To encrypt a disk, use the `diskEncryptionKey` property with the `kmsKeyName` property. For example, you can encrypt a new disk during VM creation with your Cloud KMS key by using the following:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
    "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
    "disks": [
     {
      "type": "PERSISTENT",
      "diskEncryptionKey": {
        "kmsKeyName": "projects/KMS_PROJECT_ID/locations/REGION/keyRings/KEY_RING/cryptoKeys/KEY"
      },
      "initializeParams": {
       "sourceImage": "SOURCE_IMAGE"
      },
      "boot": true
     }
    ],
    ...
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project running Compute Engine
  * `ZONE`: the zone to create the VM in
  * `MACHINE_TYPE`: the machine type, for example `c3-standard-4`
  * `KMS_PROJECT_ID`: the project that owns the Cloud KMS key
  * `REGION`: the region where the disk is located
  * `KEY_RING`: the name of the key ring that includes the key
  * `KEY`: the name of the key used to encrypt the disk
  * `SOURCE_IMAGE`: the image to use when creating the VM, for example, `projects/debian-cloud/global/images/debian-13-trixie-v20260902`



Similarly, you can use the [`disks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert) to create a new standalone Persistent Disk and encrypt it with your Cloud KMS key:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks?sourceImage=SOURCE_IMAGE
    {
     "name": "DISK_NAME",
     "diskEncryptionKey": {
       "kmsKeyName": "projects/KMS_PROJECT_ID/locations/REGION/keyRings/KEY_RING/cryptoKeys/KEY"
      },
     "type": "projects/PROJECT_ID/zones/ZONE/diskTypes/DISK_TYPE"
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project running Compute Engine
  * `ZONE`: the zone to create the disk in
  * `SOURCE_IMAGE`: the image to use when creating the disk, for example, `projects/debian-cloud/global/images/debian-13-trixie-v20260902`
  * `DISK_NAME`: a name for the new disk
  * `KMS_PROJECT_ID`: the project that owns the Cloud KMS key
  * `REGION`: the region where the disk is located
  * `KEY_RING`: the name of the key ring that includes the key
  * `KEY`: the name of the key used to encrypt the disk
  * `DISK_TYPE`: the [type of disk](https://docs.cloud.google.com/compute/docs/disks#disk-types) to create



## Create a Hyperdisk Balanced disk in Confidential mode

You can create a new Hyperdisk Balanced disk in Confidential mode with the Google Cloud console, Google Cloud CLI, or REST. To create a disk that isn't in confidential mode, follow the steps in [Create a Persistent Disk from a snapshot encrypted with CMEK](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#create-disk-from-encrypted-snapshot).

### Console

  1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. Click **Create disk** and enter the properties for the new disk.
  3. In the **Disk settings** section, choose **Hyperdisk Balanced** for the disk type.
  4. Optional. Change the default disk **Size** , **Provisioned IOPS** , and **Provisioned Throughput** settings for the disk.
  5. In the **Encryption** section, select **Cloud KMS key**.
  6. In the list of keys, select the Cloud HSM key that you want to use to encrypt this disk.
  7. In the **Confidential Computing** section, select **Enable Confidential Computing services**.
  8. To create the disk, click **Create**.



###  gcloud 

Encrypt a new disk with Confidential mode for Hyperdisk Balanced by using the [`gcloud compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create). Enable Confidential mode with the `--confidential-compute` flag and specify the key using the `--kms-key` flag.
    
    
    gcloud compute disks create DISK_NAME \
      --type=hyperdisk-balanced \
      --kms-key projects/KMS_PROJECT_ID/locations/REGION/keyRings/KEY_RING/cryptoKeys/KEY \
      --confidential-compute
    

Replace the following:

  * `DISK_NAME`: the name of the new disk
  * `KMS_PROJECT_ID`: the project that owns the Cloud HSM key
  * `REGION`: the region where the key is located
  * `KEY_RING`: the name of the key ring that includes the key
  * `KEY`: the name of the key used to encrypt the disk



###  REST 

Construct a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). To encrypt a disk with Confidential mode for Hyperdisk Balanced, use the `diskEncryptionKey` property with the `kmsKeyName` property and set the `enableConfidentialCompute` flag. For example, you can encrypt a new disk during VM creation with your Cloud HSM key by using the following:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
    "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
    "disks": [
     {
      "type": "DISK_TYPE",
      "diskEncryptionKey": {
        "kmsKeyName": "projects/KMS_PROJECT_ID/locations/REGION/keyRings/KEY_RING/cryptoKeys/KEY"
      },
      "initializeParams": {
       "sourceImage": "SOURCE_IMAGE",
       "enableConfidentialCompute": true
      },
      "boot": true
     }
    ],
    "networkInterfaces": [
      {
       "network": "global/networks/default"
      }
    ]
    }
    

Replace the following:

  * `DISK_TYPE`: the type of disk to create, for example, `hyperdisk-balanced`
  * `PROJECT_ID`: the ID of the Google Cloud project running Compute Engine
  * `ZONE`: the zone to create the VM in
  * `MACHINE_TYPE`: the machine type, for example `n2d-standard-4`
  * `KMS_PROJECT_ID`: the project that owns the Cloud HSM key
  * `REGION`: the region where the disk is located
  * `KEY_RING`: the name of the key ring that includes the key
  * `KEY`: the name of the key used to encrypt the disk
  * `SOURCE_IMAGE`: the image that supports Confidential VM to use when creating the VM, for example, `projects/debian-cloud/global/images/debian-13-trixie-v20260902`



Similarly, you can use the [`disks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert) to create a new Confidential mode for Hyperdisk Balanced:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks?sourceImage=SOURCE_IMAGE
    {
     "name": "DISK_NAME",
     "diskEncryptionKey": {
       "kmsKeyName": "projects/KMS_PROJECT_ID/locations/REGION/keyRings/KEY_RING/cryptoKeys/KEY"
      },
     "type": "projects/PROJECT_ID/zones/ZONE/diskTypes/DISK_TYPE",
     "enableConfidentialCompute": true
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project running Compute Engine
  * `ZONE`: the zone to create the disk in
  * `SOURCE_IMAGE`: the image that supports Confidential VM when creating the disk, for example, `projects/debian-cloud/global/images/debian-13-trixie-v20260902`
  * `DISK_NAME`: a name for the new disk
  * `KMS_PROJECT_ID`: the project that owns the Cloud HSM key
  * `REGION`: the region where the disk is located
  * `KEY_RING`: the name of the key ring that includes the key
  * `KEY`: the name of the key used to encrypt the disk
  * `DISK_TYPE`: the type of disk to create, for example, `hyperdisk-balanced`.



## Create a CMEK-encrypted snapshot

You can create a CMEK-protected snapshot of any disk, unless the source disk is protected with a customer-supplied encryption key. If the source disk is CMEK encrypted, then you can encrypt the snapshot with the same CMEK or with a different CMEK.

You can't convert a CMEK-encrypted snapshot to use a Google-owned and managed key unless you create a new disk and then create snapshot of that disk.

Snapshots of CMEK-encrypted disks are [incremental](https://docs.cloud.google.com/compute/docs/disks/create-snapshots).

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.snapshots.create` on the project
  * `compute.disks.createSnapshot`



**Caution:** If you try to create a snapshot from a disk and the snapshot creation process fails, you won't be able to delete the original disk until you capture a clean snapshot. This failsafe helps to prevent the accidental deletion of source data in the event of an unsuccessful backup. 

### Console

  1. In the Google Cloud console, go to the **Snapshots** page.

[Go to Snapshots](https://console.cloud.google.com/compute/snapshots)

  2. Click **Create snapshot**.
  3. Under **Source disk** , choose the source disk for the snapshot. The snapshot is automatically encrypted with the same key used by the source disk.



###  gcloud 

To create a snapshot encrypted with a CMEK, specify the Cloud KMS key by using the `--kms-key` flag. If the source disk is already encrypted with a CMEK, then you can use the same key or specify a different key.

If the source disk is encrypted with a CMEK and you don't specify the `--kms-key` flag, the snapshot is automatically encrypted with the key used by the source disk.

You can create your snapshot in the storage location policy defined by your [snapshot settings](https://docs.cloud.google.com/compute/docs/disks/snapshot-settings) or using an alternative storage location of your choice. For more information, see [Choose your snapshot storage location](https://docs.cloud.google.com/compute/docs/disks/snapshots#selecting_a_storage_location). 

  * To create a snapshot in the predefined or customized default location configured in your snapshot settings, use the [`gcloud compute snapshots create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/create).
        
        gcloud compute snapshots create SNAPSHOT_NAME \
            --source-disk-zone=SOURCE_ZONE \
            --source-disk=SOURCE_DISK_NAME \
            --snapshot-type=SNAPSHOT_TYPE \
            --kms-key=projects/KMS_PROJECT_ID/locations/KEY_REGION/keyRings/KEY_RING/cryptoKeys/SNAPSHOT_KEY
        

  * Alternatively, to override the snapshot settings and create a snapshot in a custom storage location, include the `--storage-location` flag to indicate where to store your snapshot.
        
        gcloud compute snapshots create SNAPSHOT_NAME \
            --source-disk-zone=SOURCE_ZONE \
            --source-disk=SOURCE_DISK_NAME \
            --snapshot-type=SNAPSHOT_TYPE \
            --storage-location=STORAGE_LOCATION \
            --kms-key=projects/KMS_PROJECT_ID/locations/KEY_REGION/keyRings/KEY_RING/cryptoKeys/SNAPSHOT_KEY
        

  * ([Preview](https://cloud.google.com/products/#product-launch-stages)) To create a regionally scoped snapshot in an allowed region, include the `--region` flag to indicate where to create your snapshot.
        
        gcloud beta compute snapshots create SNAPSHOT_NAME \
              --region=SNAPSHOT_SCOPE_REGION \
              --source-disk=SOURCE_DISK_NAME \
              --source-disk-zone=SOURCE_ZONE \
              --snapshot-type=SNAPSHOT_TYPE \
              --kms-key=projects/KMS_PROJECT_ID/locations/KEY_REGION/keyRings/KEY_RING/cryptoKeys/SNAPSHOT_KEY
        




Replace the following:

  * SNAPSHOT_NAME: A name for the snapshot.
  * SOURCE_ZONE: The zone of the source disk. 
  * SOURCE_DISK_NAME: The name of the disk volume from which you want to create a snapshot. 
  * KMS_PROJECT_ID: The project that contains the encryption key that is stored in Cloud Key Management Service. 
  * KEY_REGION: The region where the Cloud KMS key is located. 
  * KEY_RING: The name of the key ring that contains the Cloud KMS key. 
  * SNAPSHOT_KEY: The name of the Cloud KMS key to use to encrypt the snapshot. 
  * SNAPSHOT_TYPE: The snapshot type, either **STANDARD** or **ARCHIVE**. If a snapshot type is not specified, a `STANDARD` snapshot is created.
  * STORAGE_LOCATION: Optional: For globally scoped snapshots, the [Cloud Storage multi-region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) or the [Cloud Storage region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) where you want to store your snapshot. You can specify only one storage location.

Use the `--storage-location` parameter only when you want to override the predefined or customized default storage location configured in your snapshot settings.

  * SNAPSHOT_SCOPE_REGION: Optional: For regionally scoped snapshots, the region that the snapshot is scoped to. If you include this parameter, you can't use the `--storage-location` parameter. The STORAGE_LOCATION is automatically set to the SNAPSHOT_SCOPE_REGION.


**Note:** Google recommends using the `gcloud compute snapshots create` command instead of the [`gcloud compute disks snapshot` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot) because it supports more features, such as creating snapshots in a project different from the source disk project. 

###  REST 

To create a snapshot encrypted with a CMEK, specify the `snapshotEncryptionKey` property in the request body. If the source disk is already encrypted with a CMEK, then you can use the same key or specify a different key.

You can create your snapshot in the storage location policy defined by your [snapshot settings](https://docs.cloud.google.com/compute/docs/disks/snapshot-settings) or using an alternative storage location of your choice. For more information, see [Choose your snapshot storage location](https://docs.cloud.google.com/compute/docs/disks/snapshots#selecting_a_storage_location). 

  * To create a snapshot in the predefined or customized default location configured in your snapshot settings, make a `POST` request to the [`snapshots.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/insert):
        
        POST https://compute.googleapis.com/compute/v1/projects/DESTINATION_PROJECT_ID/global/snapshots
        {
            "name": "SNAPSHOT_NAME",
            "sourceDisk": "projects/SOURCE_PROJECT_ID/zones/SOURCE_ZONE/disks/SOURCE_DISK_NAME",
            "snapshotEncryptionKey":  {
             "kmsKeyName": "projects/KMS_PROJECT_ID/locations/KEY_REGION/keyRings/KEY_RING/cryptoKeys/SNAPSHOT_KEY"
            },
            "snapshotType": "SNAPSHOT_TYPE"
        }
        

  * Alternatively, to override the snapshot settings and create a snapshot in a custom storage location, make a `POST` request to the `snapshots.insert` method and include the `storageLocations` property in your request:
        
        POST https://compute.googleapis.com/compute/v1/projects/DESTINATION_PROJECT_ID/global/snapshots
        {
            "name": "SNAPSHOT_NAME",
            "sourceDisk": "projects/SOURCE_PROJECT_ID/zones/SOURCE_ZONE/disks/SOURCE_DISK_NAME",
            "snapshotEncryptionKey":  {
             "kmsKeyName": "projects/KMS_PROJECT_ID/locations/KEY_REGION/keyRings/KEY_RING/cryptoKeys/SNAPSHOT_KEY"
            },
            "snapshotType": "SNAPSHOT_TYPE",
            "storageLocations": [
                "STORAGE_LOCATION"
            ],
        }
        

  * ([Preview](https://cloud.google.com/products/#product-launch-stages)) To create a regionally scoped snapshot in an allowed region, make a `POST` request to the `snapshots.insert` method and define the creation region:
        
        POST https://compute.googleapis.com/compute/beta/projects/DESTINATION_PROJECT_ID/regions/SNAPSHOT_SCOPE_REGION/snapshots
        {
          "name": "SNAPSHOT_NAME",
          "sourceDisk": "projects/SOURCE_PROJECT_ID/regions/SOURCE_REGION/disks/SOURCE_DISK_NAME",
          "snapshotType": "SNAPSHOT_TYPE",
          "snapshotEncryptionKey": {
            "kmsKeyName":"projects/KMS_PROJECT_ID/locations/KEY_REGION/keyRings/KEY_RING/cryptoKeys/SNAPSHOT_KEY",
          },
        }
        




Replace the following:

  * DESTINATION_PROJECT_ID: The ID of project in which you want to create the snapshot.
  * SNAPSHOT_NAME: A name for the snapshot.
  * SOURCE_PROJECT_ID: The ID of the source disk project.
  * SOURCE_ZONE: The zone of the source disk. 
  * SOURCE_DISK_NAME: The name of the disk from which you want to create a snapshot. 
  * KMS_PROJECT_ID: The project that contains the encryption key that is stored in Cloud Key Management Service. 
  * KEY_REGION: The region where the Cloud KMS key is located. 
  * KEY_RING: The name of the key ring that contains the Cloud KMS key. 
  * SNAPSHOT_KEY: The name of the Cloud KMS key to use to encrypt the snapshot. 
  * SNAPSHOT_TYPE: The snapshot type, either **STANDARD** or **ARCHIVE**. If a snapshot type is not specified, a `STANDARD` snapshot is created.
  * STORAGE_LOCATION: Optional: For globally scoped snapshots, the [Cloud Storage multi-region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) or the [Cloud Storage region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) where you want to store your snapshot. You can specify only one storage location.

Use the `storageLocations` parameter only when you want to override the predefined or customized default storage location configured in your snapshot settings.

  * SNAPSHOT_SCOPE_REGION: Optional: For regionally scoped snapshots, the region that the snapshot is scoped to. If you include this parameter, you can't use the `storageLocations` parameter. The STORAGE_LOCATION is automatically set to the SNAPSHOT_SCOPE_REGION.


**Note:** Google recommends using the `snapshots.insert` method instead of the [`disks.createSnapshot` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/createSnapshot) because it supports more features, such as creating snapshots in a project different from the source disk project. 

## Encrypt an imported image with CMEK

You can encrypt a new image when you [import a custom image](https://docs.cloud.google.com/compute/docs/import/import-existing-image) to Compute Engine. Before you can import an image, you must [create and compress a disk image file](https://docs.cloud.google.com/compute/docs/import/import-existing-image#create_image_file) and [upload that compressed file to Cloud Storage](https://docs.cloud.google.com/storage/docs/cloud-console#_uploadingdata).

### Console

  1. In the Google Cloud console, go to the **Images** page.

[Go to Images](https://console.cloud.google.com/compute/images)

  2. Click **Create image**.
  3. For **Source disk** , select the disk you want to create an image of.
  4. For **Encryption** , select **Customer-managed key**.
  5. In the drop-down menu, select the Cloud KMS key that you want to use to encrypt this image.
  6. Continue with the image creation process.



###  gcloud 

To import and encrypt an image, use the [`gcloud compute images create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/create). For customer-managed encryption, specify the Cloud KMS key for the image.
    
    
    gcloud compute images create IMAGE_NAME \
        --source-disk=SOURCE_DISK  \
        --kms-key projects/KMS_PROJECT_ID/locations/REGION/keyRings/KEY_RING/cryptoKeys/KEY
    

Replace the following:

  * `IMAGE_NAME`: the name of the image you're creating
  * `SOURCE_DISK`: the name of the disk to create a snapshot of
  * `KMS_PROJECT_ID`: the project that contains the Cloud KMS key
  * `REGION`: the region the Cloud KMS key is located in
  * `KEY_RING`: the key ring that contains the Cloud KMS key
  * `KEY`: the name of the key to use to encrypt the new disk



###  REST 

To encrypt an imported image, construct a `POST` request to the [`images.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/insert). Specify the URI to the compressed file, add the `imageEncryptionKey` property to the image creation request, and specify the key to encrypt the image in the `kmsKeyName` property.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/images
    
    {
     "rawDisk": {
      "source": "http://storage.googleapis.com/example-image/example-image.tar.gz"
      },
     "name": "IMAGE_NAME",
     "sourceType": "RAW",
     "imageEncryptionKey": {
       "kmsKeyName": "projects/KMS_PROJECT_ID/locations/REGION/keyRings/KEY_RING/cryptoKeys/KEY"
       }
    }
    

Replace the following:

  * `PROJECT_ID`: the project to create the encrypted image in
  * `IMAGE_NAME`: the name of the image you're creating
  * `KMS_PROJECT_ID`: the project that contains the Cloud KMS key
  * `REGION`: the region the Cloud KMS key is located in
  * `KEY_RING`: the key ring that contains the Cloud KMS key
  * `KEY`: the name of the key that you used to encrypt the source disk



## Create a disk from a snapshot encrypted with CMEK

To create a new disk from an encrypted snapshot, do the following:

### Console

  1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. Click **Create disk** and enter the properties for the new disk.
  3. For **Source type** , select the snapshot or image you want to use.
  4. Optional: If you want to specify a new encryption key, for **Encryption** , specify the type of encryption key to use, and then provide the encryption key information.

If you want to remove the customer managed or customer supplied encryption key, for **Encryption** , use the default value **Google-managed encryption key**.

  5. Continue with the disk creation process.




###  gcloud 

  * To create a new disk from a globally scoped encrypted snapshot, use the [`gcloud compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create).
        
        gcloud compute disks create DISK_NAME \
          --zone=ZONE \
          --source-snapshot=SNAPSHOT_NAME \
          --kms-key=projects/KMS_PROJECT_ID/locations/REGION/keyRings/KEY_RING/cryptoKeys/KEY
        

  * ([Preview](https://cloud.google.com/products/#product-launch-stages)) To create a new disk from a regionally scoped encrypted snapshot, use the [`gcloud compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create) and specify the source snapshot region.
        
        gcloud compute disks create DISK_NAME \
          --zone=ZONE \
          --source-snapshot=SNAPSHOT_NAME \
          --source-snapshot-region=SOURCE_REGION \
          --kms-key=projects/KMS_PROJECT_ID/locations/REGION/keyRings/KEY_RING/cryptoKeys/KEY
        




Replace the following:

  * `DISK_NAME`: the name of the new disk
  * `SNAPSHOT_NAME`: the name of the encrypted snapshot

To use an image instead of a snapshot, replace `--source-snapshot SNAPSHOT_NAME` with `--image IMAGE_NAME`.

  * `KMS_PROJECT_ID`: Optional: the project that contains the Cloud KMS key

  * `REGION`: Optional: the region the Cloud KMS key is located in

  * `SOURCE_REGION`: The region that the source snapshot is scoped to

  * `ZONE`: The zone where the new disk will reside

  * `KEY_RING`: Optional: the key ring that contains the Cloud KMS key

  * `KEY`: Optional: the name of the Cloud KMS key to use to encrypt the new disk

To encrypt the new disk, you can do one of the following:

    * To specify a new customer managed encryption key, use the `--kms-key` flag.
    * To use the default Google-owned and Google-managed encryption key, don't include the `--kms-key` flag.



###  REST 

  * To create a new disk from a globally scoped encrypted snapshot, construct a `POST` request to the [`compute.disks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert). Use the `sourceSnapshot` property to specify the snapshot.
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks
        
        {
          "name": "DISK_NAME",
          "sourceSnapshot": "projects/SNAPSHOT_PROJECT_ID/global/snapshots/SNAPSHOT_NAME",
          "diskEncryptionKey": {
            "kmsKeyName": "projects/KMS_PROJECT_ID/locations/REGION/keyRings/KEY_RING/cryptoKeys/KEY"
          }
        }
        

  * ([Preview](https://cloud.google.com/products/#product-launch-stages)) To create a new disk from a regionally scoped encrypted snapshot, construct a `POST` request to the [`compute.disks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert). Use the `sourceSnapshot` property to specify the snapshot.
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks
        
        {
          "name": "DISK_NAME",
          "sourceSnapshot": "projects/SNAPSHOT_PROJECT_ID/regions/SOURCE_REGION/snapshots/SNAPSHOT_NAME",
          "type": "projects/PROJECT_ID/zones/ZONE/diskTypes/DISK_TYPE",
          "zone": "projects/PROJECT_ID/zones/ZONE"
          "diskEncryptionKey": {
            "kmsKeyName": "projects/KMS_PROJECT_ID/locations/REGION/keyRings/KEY_RING/cryptoKeys/KEY"
          }
        }
        




Replace the following:

  * `PROJECT_ID`: The project to create the new disk in
  * `ZONE`: The zone to create the new disk in
  * `SOURCE_REGION`: The region that the source snapshot is scoped to
  * `DISK_NAME`: The name of the new disk
  * `DISK_TYPE`: The full or partial URL for the [type](https://docs.cloud.google.com/compute/docs/disks#disk-types) of the disk, for example, `PROJECT_ID/zones/ZONE/diskTypes/pd-ssd`
  * `SNAPSHOT_PROJECT_ID`: The project that contains the snapshot
  * `SNAPSHOT_NAME`: The name of the encrypted snapshot

To use an image instead of a snapshot, replace `sourceSnapshot` with `sourceImage`.

  * `KMS_PROJECT_ID`: Optional: the project that contains the Cloud KMS key

  * `REGION`: Optional: the region the Cloud KMS key is located in

  * `KEY_RING`: Optional: the key ring that contains the Cloud KMS key

  * `KEY`: Optional: the name of the Cloud KMS key to use to encrypt the new disk

If you include `diskEncryptionKey`, then the disk is encrypted with the specified Cloud KMS key. If you don't include `diskEncryptionKey`, then the disk is encrypted using a Google-owned and Google-managed encryption key.




## Attaching a boot disk encrypted with CMEK to a new VM

### Console

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. Specify the VM details, and in the **Boot disk** section, click **Change**. Then, do the following:

     1. Click **Existing disks**.
     2. In the **Disk** list, select an existing disk to attach to the VM.
     3. Click **Select**.
  3. Continue with the VM creation process.




###  gcloud 

To attach an encrypted disk when you create a new VM, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create). Use the `--disk` flag to specify the encrypted boot disk, as shown in the following example:
    
    
    gcloud compute instances create VM_NAME \
      ...
      --disk name=DISK_NAME,boot=yes
    

Replace the following:

  * `VM_NAME`: the name of the VM you are creating
  * `DISK_NAME`: the name of the encrypted disk



###  REST 

Construct a `POST` request to the [`compute.instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). Use the `disks` property to specify the encrypted boot disk, as shown in the following example:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    {
      ...
      "disks": [
        {
          "deviceName": "DISK_ALIAS",
          "source": "projects/PROJECT_ID/zones/ZONE/disks/DISK_NAME"
        }
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: the project to create the new VM in
  * `ZONE`: the zone to create the new VM in
  * `DISK_ALIAS`: a unique device name to use as the disk alias in the `/dev/disk/by-id/google-*` directory of VM that runs a Linux operating system. This name can be used to reference the disk for operations such as mounting or resizing from within the instance. If you don't specify a device name, the VM chooses a default device name to apply to this disk, in the form `persistent-disk-x`, where `x` is a number assigned by Compute Engine. This field is only applicable for Persistent Disk volumes.
  * `DISK_NAME`: the name of the encrypted disk



## Rotate the CMEK for a disk or snapshot

To reduce the potential consequences of your key being compromised, we recommend that you rotate your CMEKs on a regular basis. To learn more about CMEK rotation, see [Key rotation](https://docs.cloud.google.com/kms/docs/key-rotation).

To rotate the CMEK that's protecting a disk or snapshot, you can use either the gcloud CLI or REST; you can't use the Google Cloud console or the Terraform provider for Google Cloud.

**Warning:** If you use the Terraform provider for Google Cloud to create or manage CMEK-encrypted disks and snapshots, then you can't change or rotate the CMEK. You shouldn't attempt to change or rotate the CMEK using the gcloud CLI or REST. 

###  gcloud 

To rotate the Cloud KMS key that's used to encrypt a disk, an archive snapshot, or a standard snapshot to a new key version, use the [`gcloud compute disks update-kms-key` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/update-kms-key) or [`gcloud compute snapshots update-kms-key` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/update-kms-key).

  * To rotate the key version encrypting a disk:
        
        gcloud compute disks update-kms-key DISK_NAME \
        --zone ZONE
        

  * To rotate the key version encrypting a standard snapshot:
        
        gcloud compute snapshots update-kms-key SNAPSHOT_NAME
        




Replace the following:

  * `DISK_NAME`: the name of the encrypted disk
  * `ZONE`: the zone where the encrypted disk is located
  * `SNAPSHOT_NAME`: the name of the encrypted snapshot



###  REST 

To rotate the Cloud KMS key that's used to encrypt a disk, archive snapshot, or standard snapshot to a new key version, construct a `PATCH` request to the [`compute.disks.updateKmsKey` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/updateKmsKey) or [`compute.snapshots.updateKmsKey` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/updateKmsKey).

  * To rotate the key version encrypting a zonal disk:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks/DISK_NAME/updateKmsKey
        

  * To rotate the key version encrypting a regional disk:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/disks/DISK_NAME/updateKmsKey
        

  * To rotate the key version encrypting a globally scoped standard snapshot:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/snapshots/SNAPSHOT_NAME/updateKmsKey
        

  * ([Preview](https://cloud.google.com/products/#product-launch-stages)) To rotate the key version encrypting a regionally scoped standard snapshot:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/snapshots/SNAPSHOT_NAME/updateKmsKey
        




Replace the following:

  * `PROJECT_ID`: the project where the encrypted disk or snapshot is located
  * `ZONE`: the zone where the encrypted disk is located
  * `REGION`: the region where the regional disk or regionally scoped snapshot is located
  * `DISK_NAME`: the name of the encrypted disk
  * `SNAPSHOT_NAME`: the name of the encrypted snapshot
  * `REGION`: the region where the regional disk or regionally scoped snapshot is located



The response will include a `name` item with an operation value that represents the key rotation:
    
    
      "name": "operation-YYYYYYYYYYYYY-YYYYYYYYYYYYY-YYYYYYYY-YYYYYYYY"
      

You can then poll the status for the operation to determine if your API call was successful by making a `GET` request:
    
    
      GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/operations/OPERATION_NAME
      

Replace the following:

  * `PROJECT_ID`: the project where the encrypted disk or snapshot is located
  * `ZONE`: the zone where the encrypted disk is located
  * `OPERATION_NAME`: the name of the CMEK rotation operation, in the format `operation-YYYYYYYYYYYYY-YYYYYYYYYYYYY-YYYYYYYY-YYYYYYYY`



The response will include a `progress` value that represents the status of the key rotation. When `progress` is `100`, the operation succeeded.

Rotating keys doesn't disable or delete previous key versions. For more information, see [After you rotate keys](https://docs.cloud.google.com/kms/docs/key-rotation#after).

## Change the CMEK for a disk or snapshot

You can change the encryption of a disk, an archive snapshot, or a standard snapshot to a different CMEK (for example, during a project migration or to meet new compliance requirements) without downtime.

Changing the CMEK re-encrypts the resource's data encryption key (DEK) with the new key. This process doesn't change the DEK and doesn't impact performance on running workloads.

To change the CMEK that's protecting a disk or snapshot, you can use either the gcloud CLI or REST; you can't use the Google Cloud console or Terraform.

**Warning:** If you use the Terraform provider for Google Cloud to create or manage CMEK-encrypted disks and snapshots, then you can't change or rotate the CMEK. You shouldn't attempt to change or rotate the CMEK using the gcloud CLI or REST. 

###  gcloud 

To change the Cloud KMS key for a disk or standard snapshot, use the `--kms-key` flag with the [`gcloud compute disks update-kms-key` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/update-kms-key) or [`gcloud compute snapshots update-kms-key` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/update-kms-key).

  * To change the key for a zonal disk:
        
        gcloud compute disks update-kms-key DISK_NAME \
        --kms-key=projects/KEY_PROJECT_ID/locations/global/keyRings/KEY_RING/cryptoKeys/NEW_KEY_NAME \
        --zone=ZONE
        

  * To change the key for a regional disk:
        
        gcloud compute disks update-kms-key DISK_NAME \
        --kms-key=projects/KEY_PROJECT_ID/locations/global/keyRings/KEY_RING/cryptoKeys/NEW_KEY_NAME \
        --region=REGION
        

  * To change the key for a global snapshot:
        
        gcloud compute snapshots update-kms-key SNAPSHOT_NAME \
        --kms-key=projects/KEY_PROJECT_ID/locations/global/keyRings/KEY_RING/cryptoKeys/NEW_KEY_NAME
        

  * To change the key for a regionally scoped snapshot:
        
        gcloud beta compute snapshots update-kms-key SNAPSHOT_NAME \
        --kms-key=projects/KEY_PROJECT_ID/locations/global/keyRings/KEY_RING/cryptoKeys/NEW_KEY_NAME \
        --regions=REGION
        




Replace the following:

  * `DISK_NAME`: the name of the encrypted disk.
  * `NEW_KMS_KEY`: the full resource ID of the new CMEK.
  * `ZONE`: the zone where the disk is located.
  * `REGION`: the region where the disk or snapshot is located.
  * `SNAPSHOT_NAME`: the name of the encrypted snapshot.



###  REST 

To change the key, send a `POST` request to the [`compute.disks.updateKmsKey` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/updateKmsKey) or [`compute.snapshots.updateKmsKey` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/updateKmsKey) and include the `kmsKeyName` in the request body.

  * To change the key for a zonal disk:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks/DISK_NAME/updateKmsKey
        
        {
        "kmsKeyName": "projects/KEY_PROJECT_ID/locations/global/keyRings/KEY_RING/cryptoKeys/NEW_KEY_NAME"
        }
        

  * To change the key for a regional disk:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/disks/DISK_NAME/updateKmsKey
        
        {
        "kmsKeyName": "projects/KEY_PROJECT_ID/locations/global/keyRings/KEY_RING/cryptoKeys/NEW_KEY_NAME"
        }
        

  * To change the key for a global snapshot:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/snapshots/SNAPSHOT_NAME/updateKmsKey
        
        {
        "kmsKeyName": "projects/KEY_PROJECT_ID/locations/global/keyRings/KEY_RING/cryptoKeys/NEW_KEY_NAME"
        }
        

  * To change the key for a regionally scoped snapshot:
        
        POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/regions/REGION/snapshots/SNAPSHOT_NAME/updateKmsKey
        
        {
        "kmsKeyName": "projects/KEY_PROJECT_ID/locations/global/keyRings/KEY_RING/cryptoKeys/NEW_KEY_NAME"
        }
        




Replace the following:

  * `PROJECT_ID`: the project containing the disk or snapshot.
  * `ZONE`: the zone where the disk is located.
  * `REGION`: the region where the disk or snapshot is located.
  * `DISK_NAME`: the name of the disk.
  * `NEW_KEY_NAME`: the name of the new CMEK.
  * `SNAPSHOT_NAME`: the name of the encrypted snapshot.



**Note:** If you provide the same CMEK that's already protecting the resource, then the operation will perform a version rotation to the key's primary version.

## Remove the CMEK from a disk

You can't remove a CMEK from a disk or change the encryption key's type. You can do one of the following:

  * Change the disk to use a different CMEK.

  * Decrypt the contents of a CMEK-encrypted disk and create a new disk that uses Google Cloud default encryption instead. By default, Google Cloud [encrypts all data at rest](https://cloud.google.com/security/encryption-at-rest/default-encryption).




To create a disk that uses Google-owned and managed key from a CMEK-encrypted disk, follow these steps:

  1. Create a snapshot of the encrypted disk.
  2. Use the new encrypted snapshot to create a new disk.



After you create the new disk, it uses Google Cloud default encryption to help protect the disk contents. You can encrypt subsequent snapshots created from that disk with a CMEK or use default encryption.

## Remove the CMEK from a snapshot

You can't remove a CMEK from a snapshot or change the encryption key's type. You can change the snapshot to use a different CMEK, or create a copy of the snapshot and encrypt the copy with a Google-owned and managed key.

To create a snapshot that uses Google-owned and managed key from a CMEK-encrypted snapshot, follow these steps:

  1. [Create a new disk from the snapshot](https://docs.cloud.google.com/compute/docs/disks/restore-snapshot). When you create the new disk, select the encryption type that you want.

  2. Create a snapshot of the new disk:

     * If the new disk is encrypted with a CMEK, see Create a disk from a snapshot encrypted with CMEK.

     * If the new disk is encrypted with a Google-owned and managed key, see [Create disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots).




## Disable or destroy a CMEK

If you no longer need a CMEK or want to prevent its use, [disable](https://docs.cloud.google.com/kms/docs/enable-disable#disable_an_enabled_key_version) or [destroy](https://docs.cloud.google.com/kms/docs/destroy-restore#schedule_a_key_version_for_destruction_destroy_a_key_version) the key. Deleting, disabling, or removing IAM permissions on a key is also referred to as _revoking_ the key.

**Note:** There is a delay of up to an hour between when you disable or destroy the key, during which it is still usable for encrypting and decrypting data. You may disable the Compute Engine Service Agent used to encrypt and decrypt keys in order to apply the effects of disabling or destroying a key more quickly.**Note:** If a disk was attached to a VM when you revoked the disk's encryption key, the disk is still accessible from the VM until the VM shuts down. To trigger the automatic shutdown of VMs that are attached to such disks, enable VM shutdown on key revocation.

### Impact of key revocation on encrypted resources

When you revoke an encryption key, resources that the key protects are affected as follows:

  * You can't boot a VM if any of its attached disks have revoked keys.
  * If a disk that uses the key is attached to a running VM, and you enabled VM shutdown on key revocation for the VM, then Compute Engine shuts down the VM within 7 hours.
  * You can't attach a disk with a revoked key to a VM or create a snapshot from the disk.
  * You can't use images or snapshots that are encrypted with revoked keys to create disks.



If you disable the key, you can reverse the preceding effects by enabling the key. If you destroy the key, you cannot reverse the preceding effects.

### Configure VM shutdown on Cloud KMS key revocation

You can configure your VM to shutdown automatically when you revoke the Cloud KMS key that is helping to protect a disk attached to the VM. You can revoke a key by [disabling](https://docs.cloud.google.com/kms/docs/enable-disable#disable_an_enabled_key_version) or [deleting](https://docs.cloud.google.com/kms/docs/destroy-restore#schedule_a_key_version_for_destruction_destroy_a_key_version) it. With this setting enabled, the VM shuts down within 7 hours of key revocation.

If you enable the key again, you can restart the VM with the attached disk that the key helps to protect. **The VM does not automatically restart after you enable the key.**

### Console

To configure a VM to shutdown when a Cloud KMS key is revoked, do the following:

  1. Begin creating a VM that includes a disk that is protected by a Cloud KMS key.
  2. Open the **Networking, disks, security, management, sole-tenancy** menu.
  3. Expand the **Management** section.
  4. Under **Customer Managed Encryption Key (CMEK) revocation policy** , select **Shut down**.



###  gcloud 

Use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) to create a VM, and include `--key-revocation-action-type=stop`.
    
    
    gcloud compute instances create VM_NAME \
      --image IMAGE \
      --key-revocation-action-type=stop
    

###  REST 

Use the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) to create a VM, and set the property `"keyRevocationActionType"` to `"STOP"`. The following example creates the VM from a public image.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
      "machineType": "zones/MACHINE_TYPE_ZONE/machineTypes/MACHINE_TYPE",
      "name": "VM_NAME",
      "disks": [
        {
          "initializeParams": {
            "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
          },
          "boot": true
        }
      ],
      "keyRevocationActionType": "STOP"
    }
    

Alternatively, you can configure an [instance template](https://docs.cloud.google.com/compute/docs/instance-templates) to create VMs that shut down on key revocation by using the Google Cloud CLI or REST.

### Console

You can use an instance template to create VMs that shutdown when a Cloud KMS key is revoked.

  1. Begin creating a new instance template that includes a disk that is protected by a Cloud KMS key.
  2. Open the **Networking, disks, security, management, sole-tenancy** menu.
  3. Expand the **Management** section.
  4. Under **Customer Managed Encryption Key (CMEK) revocation policy** , select **Shutdown**.



###  gcloud 

Create an instance template by using the [`gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create), and include `--key-revocation-action-type=stop`.
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
      --key-revocation-action-type=stop
    

###  REST 

Construct a POST request to the [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/v1/instanceTemplates/insert). In the request body, you must explicitly define all of the required configuration fields. If you want VMs created from this template to shut down on key revocation, specify `"keyRevocationActionType":"STOP"`. For example, an instance template with the minimal required fields that will create VMs that shut down on key revocation looks like the following:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceTemplates
    
    {
      "name": "example-template",
      "properties": {
      "machineType": "e2-standard-4",
      "networkInterfaces": [
        {
          "network": "global/networks/default",
          "accessConfigs": [
            {
              "name": "external-IP",
              "type": "ONE_TO_ONE_NAT"
            }
          ]
        }
      ],
      "disks":
      [
        {
          "type": "PERSISTENT",
          "boot": true,
          "mode": "READ_WRITE",
          "initializeParams":
          {
            "sourceImage": "projects/debian-cloud/global/images/family/debian-13"
          }
        }
      ],
      "keyRevocationActionType": "STOP"
      }
    }
    

After you create a VM that is configured to shut down on Cloud KMS revocation, create and [attach](https://docs.cloud.google.com/compute/docs/disks/attach-disks) a Persistent Disk encrypted with a Cloud KMS key.

## What's next

  * Learn more [about disk encryption](https://docs.cloud.google.com/compute/docs/disks/disk-encryption).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
