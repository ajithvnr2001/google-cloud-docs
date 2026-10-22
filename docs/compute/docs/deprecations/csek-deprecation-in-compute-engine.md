---
url: https://docs.cloud.google.com/compute/docs/deprecations/csek-deprecation-in-compute-engine/
title: Deprecation of customer-supplied encryption keys (CSEK) in Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:45.890310+00:00
---

# Deprecation of customer-supplied encryption keys (CSEK) in Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/deprecations/csek-deprecation-in-compute-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Resources ](https://docs.cloud.google.com/compute/docs/resources)



Send feedback 

#  Deprecation of customer-supplied encryption keys (CSEK) in Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

Using [customer-supplied encryption keys (CSEK)](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) to encrypt the following Compute Engine resources is deprecated. As of **July 20, 2026** , you can no longer use a CSEK to encrypt any of the following Compute Engine resources:

  * Persistent Disks
  * Images
  * Machine images
  * Standard snapshots and archive snapshots
  * Instant snapshots



CSEK will be completely removed from Compute Engine on **July 20, 2027**.

## Alternatives to CSEK

Use customer-managed encryption keys (CMEK) managed by the [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs/cmek). Cloud KMS offers enhanced security controls, auditability, and rotation support for your keys, and support for Hyperdisk volumes.

This document describes how to migrate your CSEK-encrypted Compute Engine resources to use CMEKs instead.

For more information about using CMEKs for Compute Engine disks, snapshots, and images, see [Protect resources with Cloud KMS keys](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption).

## Migrate CSEK-encrypted resources to use customer-managed encryption keys (CMEK)

You can't remove the CSEK used to encrypt a resource and replace it with a CMEK. You must create a copy of the existing resource and encrypt the copy with the CMEK.

This section describes how to migrate the following Compute Engine resources to use CMEKs instead of CSEK:

  * Persistent Disk volumes
  * Images
  * Machine Images
  * Standard and archive snapshots
  * Instant snapshots

**Caution:** Always test these migration steps in a non-production environment before applying them to a production workloads.

### Prepare to migrate CSEK-encrypted resources

Before you can encrypt a resource with a CMEK, you must have at least one Cloud KMS key ring and key. To create a key ring and key, follow the steps in [Creating key rings and keys](https://docs.cloud.google.com/kms/docs/creating-keys).

### Migrate CSEK-encrypted Persistent Disk volumes to use CMEKs

You can't remove the CSEK from a disk. Instead, you must create a new CMEK-encrypted disk from a snapshot of the CSEK-encrypted disk.

**Caution:** Replacing a CSEK-encrypted disk with a new disk often requires stopping the compute instance that the original disk is attached to, so you should plan accordingly for the downtime.

  1. Optional: if the existing CSEK-encrypted disk is the boot disk of a running compute instance, [stop the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance).

  2. [Create a standard snapshot of the CSEK-encrypted disk](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#create_snapshot).

  3. Create a new disk from the standard snapshot and encrypt it with a Cloud KMS key. You can use the Google Cloud CLI or REST.

###  gcloud CLI 

Use the [`gcloud compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create).

If the CSEK for the snapshot is RSA-wrapped, use the [`gcloud beta compute disks create command`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/disks/create). instead.

Specify the CMEK for the new disk with the `--kms-key` flag.

To create a regional disk, specify the disk's replica zones using the `replica-zones` flag: `--replica-zones=^:^ZONE:REPLICA_ZONE.
         
         gcloud compute disks create NEW_CMEK_DISK_NAME \
             --source-snapshot=CSEK_SNAPSHOT_NAME \
             --csek-key-file=PATH_TO_CSEK_KEY_FILE \
             --kms-key=projects/KMS_PROJECT_ID/locations/KEY_REGION/keyRings/KEY_RING/cryptoKeysKMS_KEY_NAME \
             --no-require-csek-key-create \
             --LOCATION_FLAG=ZONE_OR_REGION \
             --type=DISK_TYPE
         

Replace the following:

     * NEW_CMEK_DISK_NAME: the name of the new disk, for example, `migrated-cmek-disk`.
     * CSEK_SNAPSHOT_NAME: the name of the snapshot created from the CSEK-encrypted disk, for example, `my-csek-snapshot`.
     * PATH_TO_CSEK_KEY_FILE: the path to the file containing the CSEK used to encrypt the snapshot, for example, `/tmp/csek_key.json`. The format of the file is described in [Key file format](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#key_file_format). 
     * KMS_PROJECT_ID: the project ID where the Cloud KMS key is located.
     * KEY_REGION: the region where the key is located.
     * KEY_RING: the name of the key ring that includes the key.
     * KMS_KEY_NAME: the name of the key used to encrypt the disk
     * LOCATION_FLAG: the flag to specify the location, either `zone` or `region`.
     * ZONE_OR_REGION: the zone or region for the new disk, for example, `us-central1-a` or `us-central1`.
     * DISK_TYPE: the type for the new disk, for example, to create a new Balanced Persistent Disk volume, specify `pd-balanced`. For valid values, see [Supported types for Hyperdisk volumes](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk#hd_disk_types) and [Persistent Disk type variables](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk#hd_disk_types).

###  REST 

Make a `POST` request to the [`disks.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert) method.
    
    POST https://compute.googleapis.com/compute/API_VERSION_TO_USE/projects/PROJECT_ID/LOCATION_TYPE/ZONE_OR_REGION/disks
    
    {
     "name": "NEW_CMEK_DISK_NAME",
     "type": "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/LOCATION_TYPE/ZONE_OR_REGION/diskTypes/DISK_TYPE",
     "sourceSnapshot": "projects/SNAPSHOT_PROJECT_ID/global/snapshots/CSEK_SNAPSHOT_NAME",
     "diskEncryptionKey": {
        "kmsKeyName": "projects/KMS_PROJECT_ID/locations/KEY_REGION/keyRings/KEY_RING/cryptoKeys/KMS_KEY_NAME"
     },
     "sourceSnapshotEncryptionKey": {
        "CSEK_KEY_TYPE": "RAW_OR_RSA_KEY"
     }
    }
    

Replace the following:

     * API_VERSION_TO_USE: the API version to use. If the CSEK key is an RSA-wrapped key, specify `beta`. Otherwise, specify `v1`.
     * PROJECT_ID: the ID of your project, for example, `myproject-171`.
     * LOCATION_TYPE: the type of location, `zones` to create a zonal disk, or `regions` to create a regional disk.
     * ZONE_OR_REGION: the zone or region for the new disk, for example, `us-central1-a` or `us-central1`.
     * DISK_TYPE: the type for the new disk, for example, to create a new Balanced Persistent Disk volume, specify `pd-balanced`. For valid values, see [Supported types for Hyperdisk volumes](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk#hd_disk_types) and [Persistent Disk type variables](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk#hd_disk_types).
     * NEW_CMEK_DISK_NAME: the name of the new disk, for example, `migrated-cmek-disk`.
     * SNAPSHOT_PROJECT_ID: the project ID of the snapshot.
     * CSEK_SNAPSHOT_NAME: the name of the snapshot created from the CSEK-encrypted disk, for example, `my-csek-snapshot`.
     * KMS_PROJECT_ID: the project ID where the Cloud KMS key is located.
     * KEY_REGION: the region where the key is located.
     * KEY_RING: The name of the key ring that includes the key.
     * KMS_KEY_NAME: the name of the key used to encrypt the disk
     * CSEK_KEY_TYPE: The type of the customer-supplied encryption key, `rawKey` for a raw key or `rsaEncryptedKey` if the key is RSA-wrapped.
     * RAW_OR_RSA_KEY: The value of the raw or RSA-encrypted key.

  4. Use the new disk with your compute instance:

     1. If the existing CSEK-encrypted disk is the boot disk of a running compute instance, [stop the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance).

     2. To start using the new disk, detach the CSEK-encrypted source disk from the instance and attach the new disk that you just created.

        * If the source disk is a boot disk:

          1. [Detach the source disk from the instance](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk#detach_disk).
          2. [Use the new disk as the instance's boot disk](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk#attach_disk).
        * If the source disk is a non-boot disk:

          1. [Detach the source disk from the instance](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk#detach_non_boot_disk).
          2. [Attach the new disk to the instance](https://docs.cloud.google.com/compute/docs/disks/attach-disks).
     3. [Start the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#restart-vm).

     4. Verify that the new disk works as expected.

     5. After you test the new disk, [delete the snapshot](https://docs.cloud.google.com/compute/docs/disks/manage-snapshots#delete-standard-snapshots) and the original CSEK-encrypted disk.

You continue to incur charges for the disk and snapshot until you delete them.




### Migrate CSEK-encrypted instant snapshots

You can't directly remove the CSEK from an instant snapshot. Instead, you must convert the snapshot to a CMEK-encrypted instant snapshot by completing the following tasks:

  1. Create a temporary [CSEK-encrypted standard snapshot from the instant snapshot](https://docs.cloud.google.com/compute/docs/disks/convert-instant-snapshot#convert-from-isp).

  2. Create a [temporary CMEK-encrypted disk from the CSEK-encrypted snapshot](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#create_a_disk_from_a_csek-encrypted_snapshot).

  3. [Create a CMEK-encrypted instant snapshot of the new disk](https://docs.cloud.google.com/compute/docs/disks/create-instant-snapshots).

  4. After you create the CMEK-encrypted instant snapshot, delete the CSEK-encrypted standard snapshot and the temporary disk.




### Migrate CSEK-encrypted images and snapshots

You can't remove the CSEK from an image, an archive snapshot, instant snapshot, or standard snapshot. Instead, you must create a new CMEK-encrypted disk from the image or snapshot, and then create an image or snapshot of the new disk.

  1. Create a new Google Cloud Hyperdisk or Persistent Disk volume from the image or snapshot:

     * [Create a new disk from a CSEK-encrypted snapshot](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#create_a_disk_from_a_csek-encrypted_snapshot).
     * [Create a disk from a CSEK-encrypted image](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#create_a_disk_from_an_image_encrypted_with_csek).
  2. Create an image or standard snapshot of the new disk. Encrypt the new image or snapshot with a CMEK.

     * [Create a CMEK-encrypted image of a disk](https://docs.cloud.google.com/compute/docs/images/create-custom#create_image)
     * [Create a CMEK-encrypted standard or archive snapshot of a disk](https://docs.cloud.google.com/compute/docs/disks/create-snapshots)
  3. Delete the disk that you created earlier.




### Migrate CSEK-encrypted machine images

To create a CMEK-encrypted machine image from a CSEK-encrypted machine image, you must create a temporary instance from the machine image and then create a CMEK-encrypted machine image from the temporary instance. Follow these steps.

  1. Create a new instance from the CSEK-encrypted machine image, specifying a Cloud KMS key for each disk that's in the machine the image. You must use the REST or Google Cloud CLI. For more information about overriding properties when creating a machine image, see [Create an instance from a machine image with property overrides](https://docs.cloud.google.com/compute/docs/machine-images/create-instance-from-machine-image#create-instance-from-image-override).

###  Google Cloud CLI 

Use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create)
         
         gcloud compute instances create NEW_INSTANCE_NAME \
          --project=PROJECT_ID \
          --zone=ZONE \
          --machine-type=INSTANCE_MACHINE_TYPE \
          --source-machine-image=CSEK_MACHINE_IMAGE_NAME \
          --source-machine-image-csek-key-file=PATH_TO_CSEK_KEY_FILE \
          --create-disk=device-name=BOOT_DISK_DEVICE_NAME,boot=yes,auto-delete=yes,kms-key=projects/KMS_PROJECT_ID/locations/REGION/keyRings/KEY_RING/cryptoKeys/BOOT_DISK_KMS_KEY \
          --create-disk=device-name=DEVICE_NAME_FOR_DATA_DISK_1,boot=no,kms-key=projects/KMS_PROJECT_ID/locations/REGION/keyRings/KEY_RING/cryptoKeys/KMS_KEY_FOR_DATA_DISK_1 \
          --create-disk=device-name=DEVICE_NAME_FOR_DATA_DISK_2,boot=no,kms-key=projects/KMS_PROJECT_ID/locations/REGION/keyRings/KEY_RING/cryptoKeys/KMS_KEY_FOR_DATA_DISK_2
         
         

Replace the following:

     * NEW_INSTANCE_NAME: the name of the new instance, for example, `migrated-instance`.
     * PROJECT_ID: the ID for the project that you want to create the instance in, for example,`myproject-123`.
     * ZONE: the zone for the new instance, for example, `us-central1-a`.
     * INSTANCE_MACHINE_TYPE: the machine type for the new instance, for example, `c3-standard-4`.
     * CSEK_MACHINE_IMAGE_NAME: the name of the source CSEK-encrypted machine image.
     * PATH_TO_CSEK_KEY_FILE: the path to the file containing the CSEK used to encrypt the source machine image, for example, `/tmp/csek_key.json`. For the required file format, see [Key file format](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#key_file_format).
     * BOOT_DISK_DEVICE_NAME: th new device name for the boot disk as defined within the machine image.
     * KMS_PROJECT_ID: the project ID where your Cloud KMS key is located.
     * REGION: the region where your Cloud KMS key is located, for example, `us-central1`.
     * KEY_RING: the name of the key ring that includes the keys.
     * BOOT_DISK_KMS_KEY: the name of the Cloud KMS key used to encrypt the boot disk for the new instance.
     * DEVICE_NAME_FOR_DATA_DISK_1: a new device name for the first data disk as defined inside the source machine image.
     * KMS_KEY_FOR_DATA_DISK_1: the name of the Cloud KMS key used to encrypt the first data disk.
     * KMS_KEY_FOR_DATA_DISK_2: the name of the Cloud KMS key used to encrypt the second data disk.

###  REST 

Make a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert)
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
     {
        "name": "NEW_INSTANCE_NAME",
        "sourceMachineImage": "projects/PROJECT_ID/global/machineImages/CSEK_MACHINE_IMAGE_NAME",
           "disks": [
           {
              "deviceName": "BOOT_DISK_DEVICE_NAME",
              "boot": true,
              "diskEncryptionKey": {
                 "kmsKeyName": "projects/KMS_PROJECT_ID/locations/REGION/keyRings/KEY_RING/cryptoKeys/BOOT_DISK_KMS_KEY"
              }
           },
           {
              "deviceName": "DEVICE_NAME_FOR_DATA_DISK_1",
              "boot": false,
              "diskEncryptionKey": {
                 "kmsKeyName": "projects/KMS_PROJECT_ID/locations/REGION/keyRings/KEY_RING/cryptoKeys/KMS_KEY_FOR_DATA_DISK_1"
              }
           },
           {
              "deviceName": "DEVICE_NAME_FOR_DATA_DISK_2",
              "boot": false,
              "diskEncryptionKey": {
                 "kmsKeyName": "projects/KMS_PROJECT_ID/locations/REGION/keyRings/KEY_RING/cryptoKeys//KMS_KEY_FOR_DATA_DISK_2"
              }
           }
        ]
     }
    

Replace the following:

     * `PROJECT_ID`: the project ID of the project in which you want to create the temporary instance, for example, `myproject-123`.
     * `ZONE`: the zone for the new instance, for example, `us-central1-a`.
     * `NEW_INSTANCE_NAME`: the name of the temporary instance to create, for example, `migrated-instance`.
     * `CSEK_MACHINE_IMAGE_NAME`: the name of the source CSEK-encrypted machine image, for example, `csek-encrypted-image`.
     * `BOOT_DISK_DEVICE_NAME`: the device name of the boot disk as defined within the source machine image, for example, `boot-disk-0`.
     * `KMS_PROJECT_ID`: the project ID where your Cloud KMS key is located.
     * `REGION`: the region where your Cloud KMS key is located, for example, `us-central1`.
     * `KEY_RING`: the name of the key ring that includes the encryption keys.
     * `BOOT_DISK_KMS_KEY`: the name of the Cloud KMS key used to encrypt the new boot disk.
     * `DEVICE_NAME_FOR_DATA_DISK_1`: the device name of the first data disk as defined in the source machine image.
     * `KMS_KEY_FOR_DATA_DISK_1`: the name of the Cloud KMS key used to encrypt the first data disk.
     * `DEVICE_NAME_FOR_DATA_DISK_2`: the device name of the second data disk as defined in the source machine image.
     * `KMS_KEY_FOR_DATA_DISK_2`: the name of the Cloud KMS key used to encrypt the second data disk.

  2. Verify that the instance works as expected.

  3. After you test the instance, [create a CMEK-encrypted machine image](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images#create-image-from-instance) from the new instance.

  4. [Delete the temporary instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance).




### Remove unused resources

To avoid incurring costs for unused resources, delete any disks, machine images, snapshots, instances, and images that you no longer need.

## What's next

  * [Learn best practices for working with CMEKs](https://docs.cloud.google.com/kms/docs/cmek-best-practices)
  * Manage the CMEKs used for your Compute Engine disks and snapshots: 
    * [Rotate the CMEK for a disk or snapshot](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#rotate_encryption)
    * [Change the CMEK for a disk or snapshot](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#change-key)
    * [Understand how deleting or disabling a disk's CMEK works](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#impact-of-key-revocation-on-encrypted-resources)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
