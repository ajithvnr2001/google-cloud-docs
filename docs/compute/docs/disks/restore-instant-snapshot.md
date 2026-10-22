---
url: https://docs.cloud.google.com/compute/docs/disks/restore-instant-snapshot/
title: Restore disks from instant snapshots \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:09.156057+00:00
---

# Restore disks from instant snapshots  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/restore-instant-snapshot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Restore disks from instant snapshots Stay organized with collections  Save and categorize content based on your preferences. 

To access data captured in an [instant snapshot](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots), you must restore, or create a new disk from the instant snapshot.

This page explains how to create a disk from an instant snapshot. After you create the disk, you can use it by attaching it to a virtual machine (VM).

## Before you begin

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

To get the permissions that you need to create a disk from an instant snapshot, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To connect to a VM that can run as a service account: [Service Account User (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create a disk from an instant snapshot. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a disk from an instant snapshot:

  * `compute.disks.create` on the destination project for the new disk
  * `compute.instantSnapshots.useReadOnly` on the source instant snapshot
  * To create disks from a consistency group of instant snapshots: 
    * `compute.disks.create` on the destination project
    * `compute.instantSnapshots.useReadOnly` on the source instant snapshots
    * `compute.resourcePolicies.useReadOnly` on the source instant snapshots
    * `compute.instantSnapshotGroups.useReadOnly` on the source consistency group of instant snapshots



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Limitations

The following limitations apply to instant snapshots and consistency groups of instant snapshots:

  * When you create a disk from an instant snapshot, the new disk always has the same type, location, and encryption as the source disk of the snapshot.

  * You can't create a VM directly from an instant snapshot. You must create a disk from the instant snapshot and then use the new disk to create a VM.

  * If the source disk of the instant snapshot [uses customer-managed or customer-supplied encryption keys](https://docs.cloud.google.com/compute/docs/disks/view-disk-details#view-encryption), you must provide the same encryption key when you create a new disk from the instant snapshot.

Consider this example. Imagine you have a disk, `DISK-1` encrypted with a customer-supplied encryption key (CSEK)([Deprecated](https://docs.cloud.google.com/compute/docs/deprecations)), `KEY-1`. You also have an instant snapshot, `IS-1`, created from `DISK-1`. To create a new disk from `IS-1`, you must provide the same key, `KEY-1`, when you create the new disk.

If the disk is encrypted with customer-managed encryption keys (CMEK), you only have to provide the key if you use the REST or the gcloud CLI to create the disk. If you use the Google Cloud console, you don't need to specify the encryption key.

  * When you create new disks from a consistency group of instant snapshots, the location of the new disks is the same as the source consistency group of instant snapshots.




## Create a disk from an instant snapshot

An instant snapshot is encrypted with the same encryption as its source disk. The steps to create a disk from an instant snapshot depend on how the instant snapshot's source disk is encrypted.

Each source disk is encrypted with one of the following methods:

  * Google-owned and Google-managed encryption keys. This is the default.
  * Customer-managed encryption keys (CMEK)
  * Customer-supplied encryption keys (CSEK).



To find out how a particular disk is encrypted, see [View information about a disk's encryption](https://docs.cloud.google.com/compute/docs/disks/view-disk-details#view-encryption).

### Create a disk from an instant snapshot encrypted with default encryption

You can create a disk from an instant snapshot with the gcloud CLI, the Google Cloud console, or the REST.

###  Console 

  1. Find the instant snapshot that you want to restore:

     1. In the Google Cloud console, go to the **Snapshots** page.

[Go to Snapshots](https://console.cloud.google.com/compute/snapshots)

     2. Click the **Instant snapshots** tab.

     3. In the **Name** column, click the name of the instant snapshot you want to restore.

  2. Click **Create disk**.

  3. In the **Name** field, enter a new name for the disk.

  4. Optional: In the **Description** field, enter additional details.

  5. Verify that the **Disk source type** is **Instant snapshot**.

  6. In the **Source instant snapshot** list, choose the instant snapshot.

  7. Optional: Configure additional customizations for the disk.

     * Enter a size: In the **Size** field, specify a size for the disk in GB. The size must be equal to or larger than the size of the source disk for the snapshot.
     * Schedule backups: If you want Compute Engine to [create standard snapshots of this new disk on a schedule](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots), select the **Enable snapshot schedule** checkbox and choose a snapshot schedule. Otherwise, clear the checkbox.
  8. Optional: To organize your project, add one or more [labels](https://docs.cloud.google.com/compute/docs/labeling-resources#what-are-labels).

  9. To create the disk, click **Create**.




###  gcloud 

Use the [`gcloud compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create). The arguments you specify depend on whether you're creating a zonal or regional disk.

###  Create a zonal disk 

Specify the zone with the `--zone` flag:
    
    
    gcloud compute disks create DISK_NAME --zone=ZONE \
      --source-instant-snapshot=SOURCE_INSTANT_SNAPSHOT_NAME
    

Replace the following:

  * `DISK_NAME`: the name of the new disk.
  * `ZONE`: the zone for the new disk, for example, `europe-west1-a`.
  * `SOURCE_INSTANT_SNAPSHOT_NAME`: the name of the source instant snapshot.



###  Create a regional disk 

Specify the region with `--region` and the new disk's target replication zones with `--replica-zones`.
    
    
    gcloud compute disks create DISK_NAME \
     --region=REGION \
     --source-instant-snapshot=SOURCE_INSTANT_SNAPSHOT_NAME \
     --replica-zones=ZONE1,ZONE2
    

Replace the following:

  * `DISK_NAME`: the name of the new disk.
  * `REGION`: the region for the regional disk to reside in, for example: `europe-west1`.
  * `SOURCE_INSTANT_SNAPSHOT_NAME`: the name of the source instant snapshot.
  * `ZONE1,ZONE2`: the zones within the region where the two disk replicas are located, for example: `europe-west1-b,europe-west1-c`.



###  REST 

To create a zonal or regional disk from an instant snapshot, use the [`disks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert). The new disk must be the same type as that of the source disk of the instant snapshot. For example, you can't create a regional disk from a snapshot of a zonal disk.

###  Create a zonal disk 

Make a `POST` request, specifying the source instant snapshot.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/SOURCE_ZONE/disks/insert
    {
    "name": "NEW_DISK_NAME",
    "sourceInstantSnapshot": "projects/PROJECT/zones/SOURCE_ZONE/instantSnapshots/SOURCE_INSTANT_SNAPSHOT_NAME"
    }
    

Replace the following:

  * `PROJECT`: the project in which to create the new disk.
  * `SOURCE_ZONE`: the zone where the instant snapshot is located, for example, `us-central1-a`. The disk is created in this zone.
  * `NEW_DISK_NAME`: a unique name for the new disk.
  * `SOURCE_INSTANT_SNAPSHOT_NAME`: the name of the source instant snapshot.



###  Create a regional disk 

Make a `POST` request, specifying the source instant snapshot and the zones where the disk should be replicated to.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT/region/SOURCE_REGION/disks/insert
    
    {
    "name": "NEW_DISK_NAME",
    "sourceInstantSnapshot": "projects/PROJECT/regions/SOURCE_REGION/instantSnapshots/SOURCE_INSTANT_SNAPSHOT_NAME",
    "replicaZones": [
      "projects/PROJECT/zones/ZONE1",
      "projects/PROJECT/zones/ZONE2"
    ]
    }
    

Replace the following:

  * `PROJECT`: the project in which to create the new disk.
  * `SOURCE_REGION`: the region where the instant snapshot is located. The disk is created in this region.
  * `NEW_DISK_NAME`: a unique name for the new disk.
  * `SOURCE_INSTANT_SNAPSHOT_NAME`: the name of the source instant snapshot.
  * `ZONE1,ZONE2`: the zones within the region for the two disk replicas, for example, `europe-west1-b`,`europe-west1-c`.



#### API request response

If the `POST` request is successful, the response body will be an object that you can poll to get the status of the disk's creation. See [Handling API responses](https://docs.cloud.google.com/compute/docs/api/how-tos/api-requests-responses#handling_api_responses) for more information.

### Create a disk from a CMEK- or CSEK-encrypted instant snapshot

###  Console 

If the instant snapshot uses Google default or CMEK encryption, Google Cloud console automatically provides the encryption key when you create a disk from the instant snapshot. Otherwise, if the instant snapshot is CSEK-encrypted, you must provide the encryption key to create a disk.

Follow the steps in the Google-managed encryption section, specifying the encryption key using these instructions:

  1. In the **Decryption** section, enter the encryption key in the **Encryption key** field.
  2. If the key is wrapped with the public RSA key, select **Wrapped key**.



###  gcloud 

Use the [`gcloud compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create).

If the source disk is CMEK-encrypted, use the `--kms-key` parameter to provide the name of the key.

If the source disk is CSEK-encrypted, use the `--csek-key-file` parameter to specify the source disk's encryption key.

###  CMEK 

To create a zonal disk from a CMEK encrypted instant snapshot, use the following command:
    
    
         gcloud compute disks create NEW_DISK_NAME \
           --zone=SOURCE_ZONE \
           --source-instant-snapshot=SOURCE_INSTANT_SNAPSHOT_NAME \
           --kms-key=projects/KMS_PROJECT_NAME/locations/KEYRING_LOCATION/keyRings/KEY_RING_NAME/cryptoKeys/KEY_NAME
    

Replace the following:

  * `NEW_DISK_NAME`: the name of the new disk.
  * `SOURCE_ZONE`: the zone where the instant snapshot is stored, for example, `europe-west1-a`.
  * `SOURCE_INSTANT_SNAPSHOT_NAME`: the name of the source instant snapshot.
  * `KMS_PROJECT_NAME`: the project containing the key. 
  * `KEYRING_LOCATION`: the location of the key ring that the key belongs to. If the key ring is global, specify `global`. Otherwise, specify the name of the region where the key ring is located, for example, `us-west1`. 
  * `KEY_RING_NAME`: the name of the key ring that includes the key, for example, `key-ring-1`. 
  * `KEY_NAME`: the name of the key used to encrypt the disk. 



###  CSEK 

To create a zonal disk from a CSEK-encrypted instant snapshot, use the following command:
    
    
         gcloud compute disks create NEW_DISK_NAME \
           --zone=SOURCE_ZONE \
           --source-instant-snapshot=SOURCE_INSTANT_SNAPSHOT_NAME \
           --csek-key-file=PATH_TO_CSEK_JSON_FILE
     

Replace the following:

  * `NEW_DISK_NAME`: the name of the new disk.
  * `SOURCE_ZONE`: the zone where the instant snapshot is stored, for example, `europe-west1-a`.
  * `SOURCE_INSTANT_SNAPSHOT_NAME`: the name of the source instant snapshot.
  * `CSEK_JSON_FILE`: Path to a JSON file containing the key. See an [ example of the CSEK file format](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#api).



To create a regional disk, replace the `--zone` flag in the preceding example with the following flags:

  * `--region`: the region for the new disk
  * `--replica-zones`: the zones within the region for the two disk replicas.



###  REST 

To create a zonal or regional disk from a CMEK- or CSEK-encrypted instant snapshot, make a `POST` request to the [`disks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert) using the properties listed in the Google-managed encryption section.

Additionally, provide the source disk's encryption key with the `diskEncryptionKey` field. The properties of the `diskEncryptionKey` field depend on whether or not the disk is CMEK- or CSEK-encrypted.

The following examples show how to create a new zonal disk for each encryption type.

###  CMEK 

In the request body, specify the name of the key with the `diskEncryptionKey.kmsKeyName` property:
    
    
    {
    "name": "NEW_DISK_NAME",
    "sourceInstantSnapshot": "projects/PROJECT/zones/SOURCE_ZONE/instantSnapshots/SOURCE_INSTANT_SNAPSHOT_NAME",
    "diskEncryptionKey": {
          "kmsKeyName": "projects/KMS_PROJECT/locations/LOCATION/keyRings/KEYRING_LOCATION/cryptoKeys/KEY_NAME"
      }
    }
    

Replace the following:

  * `NEW_DISK_NAME`: a unique name for the new disk.
  * `PROJECT`: the project in which to create the new disk.
  * `SOURCE_ZONE`: the zone where the instant snapshot is located, for example, `us-central1-a`. The disk is created in this zone.
  * `SOURCE_INSTANT_SNAPSHOT_NAME`: the name of the source instant snapshot.
  * `KMS_PROJECT`: the project containing the key.
  * `LOCATION`: the location of the key ring that the key belongs to. If the key ring is global, specify `global`. Otherwise, specify the name of the region where the key ring is located, for example, `us-west1`.
  * `KEY_RING`: the name of the key ring that includes the key, for example, `key-ring-1`.
  * `KEY`: the name of the key used to encrypt the disk.



###  CSEK 

The request body depends on whether the CSEK used to encrypt the instant snapshot is RSA-encrypted or not.

**To use a raw (non-RSA encrypted) key** , specify the key in the `diskEncryptionKey.rawKey` property of the request body:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/SOURCE_ZONE/disks/insert
    {
      "name": "NEW_DISK_NAME",
      "sourceInstantSnapshot": "projects/PROJECT/zones/SOURCE_ZONE/instantSnapshots/INSTANT_SNAPSHOT_NAME,
      "diskEncryptionKey": {
          "rawKey": "RAW_ENCRYPTION_KEY"
      }
    }
    

Replace the following with the corresponding values:

  * `PROJECT`: the project in which to create the new disk.
  * `SOURCE_ZONE`: the zone where the instant snapshot is located, for example, `us-central1-a`. The disk is created in this zone.
  * `NEW_DISK_NAME`: a unique name for the new disk.
  * `SOURCE_INSTANT_SNAPSHOT_NAME`: the name of the source instant snapshot.
  * `RAW_ENCRYPTION_KEY`: The key used to encrypt the instant snapshot and its source disk, for example, `SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0=`.



**To use an RSA-encrypted key** , modify the preceding example as follows:

  * Make a `POST` request to the [`disks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert): 
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks/insert
        

  * Specify the key in the `diskEncryptionKey.rsaEncryptedKey` property of the request body: 
        
        "diskEncryptionKey": {
         "rsaEncryptedKey": "RSA_ENCRYPTED_KEY"
        }
        




Replace `RSA_ENCRYPTED_KEY` with your encrypted key.

#### API request response

If the `POST` request is successful, the response body will be an object that you can poll to get the status of the disk's creation. See [Handling API responses](https://docs.cloud.google.com/compute/docs/api/how-tos/api-requests-responses#handling_api_responses) for more information.

## Create disks from a consistency group of instant snapshots

If you backed up a consistency group of disks with a consistency group of instant snapshots, you can create new disks from the group of snapshots. After you create the new disks, you can optionally add them to a consistency group.

###  gcloud 

How you create disks from a group of instant snapshots depends on whether all the disks in the consistency group are in the same zone, for zonal disks, or region, for regional disks.

  * If the consistency group of instant snapshots contains a mix of regional and zonal disks, or if the instant snapshots are in different zones, you must restore each instant snapshot to a new disk individually using the `gcloud compute disks create` command. For instructions on creating a disk from an instant snapshot, see Create a disk from an instant snapshot.

  * If all the disks in the consistency group are regional disks in the same region or zonal disks in the same zone, use the [`gcloud compute disks bulk create command`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/bulk/create).

    * To create zonal disks from a consistency group of instant snapshots:
          
          gcloud compute disks bulk create \
          --zone=ZONE \
          --source-instant-snapshot-group=SOURCE_INSTANT_SNAPSHOT_GROUP \
          --source-instant-snapshot-group-zone=SOURCE_ZONE
          

Replace the following:

      * `ZONE`: the zone where your new disks are located.
      * `SOURCE_INSTANT_SNAPSHOT_GROUP`: The name of the consistency group of snapshots that you are restoring.
      * `SOURCE_ZONE`: the zone where the source consistency group of snapshots is located.
    * To create regional disks from a consistency group of instant snapshots:
          
          gcloud compute disks bulk create \
          --region=REGION \
          --source-instant-snapshot-group=SOURCE_INSTANT_SNAPSHOT_GROUP \
          --source-instant-snapshot-group-region=SOURCE_REGION
          

Replace the following:

      * `REGION`: the region where your new disks are located.
      * `SOURCE_INSTANT_SNAPSHOT_GROUP`: The name of the consistency group of snapshots that you are restoring.
      * `SOURCE_REGION`: the region where the source consistency group of snapshots is located.



###  REST 

How you create disks from a group of instant snapshots depends on whether all the disks in the consistency group are in the same zone, for zonal disks, or region, for regional disks.

  * If the consistency group of instant snapshots contains a mix of regional and zonal disks, or if the instant snapshots are in different zones, you must restore each instant snapshot to a new disk individually using the `disks.insert` method. For instructions on creating a disk from an instant snapshot, see Create a disk from an instant snapshot.

  * If all the disks in the consistency group are zonal disks in the same zone or regional disks in the same region, make a `POST` request to the [`disks.bulkInsert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/bulkInsert). In the body, specify the `sourceInstantSnapshotGroup`.

    * To create zonal disks from a consistency group of instant snapshots:
          
          POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks/bulkInsert --data-ascii
          {
             "instantSnapshotGroupParameters":
               {
                 "sourceInstantSnapshotGroup": "zones/ZONE/instantSnapshotGroups/INSTANT_SNAPSHOT_GROUP_NAME"
               }
          }
          

Replace the following:

      * `PROJECT_ID`: your project ID.
      * `ZONE`: the zone where your new disks are located.
      * `INSTANT_SNAPSHOT_GROUP_NAME`: The name of the consistency group of snapshots that you are restoring.
    * To create regional disks from a consistency group of instant snapshots:
          
          POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/disks/bulkInsert --data-ascii
          {
            "instantSnapshotGroupParameters":
             {
               "sourceInstantSnapshotGroup": "regions/REGION/instantSnapshotGroups/INSTANT_SNAPSHOT_GROUP_NAME"
             }
          }
          

Replace the following:

      * `PROJECT_ID`: your project ID.
      * `REGION`: the region where your new disks are located.
      * `INSTANT_SNAPSHOT_GROUP_NAME`: The name of the consistency group of snapshots that you are restoring.



Optional: To add your newly-created disks to a consistency group, follow the steps in [Add a disk to a consistency group](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-consistency-groups#add_a_disk_to_a_consistency_group).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
