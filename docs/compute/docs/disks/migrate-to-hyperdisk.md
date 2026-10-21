---
url: https://docs.cloud.google.com/compute/docs/disks/migrate-to-hyperdisk/
title: Change the disk type \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:39:49.990186+00:00
---

# Change the disk type  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/migrate-to-hyperdisk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Change the disk type Stay organized with collections  Save and categorize content based on your preferences. 

This document discusses how to perform certain tasks on a disk. To perform any of the following tasks, you must create a new disk. You can't make the following changes to a disk.

  * Change a disk's type, for example, change a Hyperdisk Throughput volume to a Hyperdisk Balanced volume.
  * Change the disk's encryption type, for example, modify a disk's encryption from using Google-generated keys to customer-managed encryption keys (CMEK).
  * Move a disk into or out of a [Hyperdisk pool](https://docs.cloud.google.com/compute/docs/disks/storage-pools).
  * Move a disk to a different region or zone.
  * Move a disk to another project.



Follow these steps to perform any of the previously mentioned tasks:

  1. Create a snapshot of the existing disk.
  2. Create a new disk of the correct type or within a storage pool (referred to as its _placement_), using the snapshot as the data source for the disk.
  3. After verifying the new disk, you can delete the original disk.



## Before you begin

  * To place the new Hyperdisk volumes in a Hyperdisk Storage Pool or Hyperdisk Exapool, review the [Limitations for creating disks in a Hyperdisk pool](https://docs.cloud.google.com/compute/docs/disks/use-storage-pool-capacity#limitations). 

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

To get the permissions that you need to change the disk type, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To connect to a VM that can run as a service account: [Service Account User (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to change the disk type. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to change the disk type:

  * To create a snapshot of the disk: 
    * `compute.snapshots.create` on the project
    * `compute.disks.createSnapshot` on the disk
  * To create a new disk: `compute.disks.create` on the project 
  * To create a new disk from a standard or archive snapshot: 
    * `compute.disks.create` on the project where you want to create the disk
    * `compute.snapshots.useReadOnly` on the snapshot
  * To create a disk in a pool: 
    * `compute.storagePools.use` on the project
    * `compute.disks.create` on the project
  * To attach a disk to a VM: 
    * `compute.instances.attachDisk` on the VM
    * `compute.disks.use` on the volume that you want to attach to the VM
  * To delete a disk: `compute.disks.delete` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Change the type, placement, project, or location of a disk

To perform any of the following tasks on a disk, create a snapshot of the disk and then create a new disk from the snapshot:

  * Move a Persistent Disk volume to Hyperdisk
  * Recreate a disk in or out of a pool
  * Move a disk to a different project
  * Move a disk to a different region or zone



To move a disk to another project, you must use the Google Cloud CLI or REST; you can't use Google Cloud console.

###  Console 

  1. Prepare for creating a disk snapshot:

     * Review [Best practices for Compute Engine disk snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices) to prepare your disk for snapshotting.
     * Read [Create schedules for disk snapshots](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots) to learn about creating a snapshot schedule and attaching it to your disks. Backing up your disks regularly with scheduled snapshots can reduce the risk of unexpected data loss.

**Important:** If you pause your applications before creating a snapshot, resume your workloads only after the snapshot resource reaches the `UPLOADING` status.

For more information, see the table in [Manually creating application consistent snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices#manual).

  2. [Create a snapshot](https://docs.cloud.google.com/compute/docs/disks/create-snapshots) of your existing disk.

**Note:** When creating a snapshot, Google recommends using the [`snapshots.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/insert) instead of the [`disks.createSnapshot` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/createSnapshot) because it supports more features, such as creating snapshots in a project different from the source disk project.
  3. Optional: To create a new Hyperdisks in a pool, you must [create a storage pool](https://docs.cloud.google.com/compute/docs/disks/create-storage-pools), if one doesn't exist.
  4. Go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)
  5. Click **\+ Create Disk**.
  6. Under **Disk Type** , select **Hyperdisk Extreme** , **Hyperdisk Throughput** , or **Hyperdisk Balanced**.

Optional: To use a pool, you must select either Hyperdisk Balanced or Hyperdisk Throughput.

  7. For **Disk source type** , select **Snapshot** , then select the name of the snapshot to restore. 
  8. Specify the **Size** of the new disk, in GiB. This number must be equal to or larger than the original source disk for the snapshot. 
  9. Optional: Change the defaults, if you are changing the disk type: 

     * Hyperdisk Balanced: Change the **Provisioned IOPS** value and **Provisioned throughput** value.
     * Hyperdisk Extreme: Change the **Provisioned IOPS** value.
     * Hyperdisk Throughput: Change the **Provisioned throughput** value.
  10. Optional: To create the new disk in a pool:

     1. In the **Storage pool** section, select **Enable storage pool**.
     2. Choose the name of the pool to create the disk in. 

Only pools that exist in the selected zone appear in the list.

  11. Click **Create** to create the new disk. 
  12. After you create the disk, you can attach the disk to any running or stopped compute instance. 



###  gcloud 

  1. Prepare for creating a disk snapshot:

     * Review [Best practices for Compute Engine disk snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices) to prepare your disk for snapshotting.
     * Read [Create schedules for disk snapshots](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots) to learn about creating a snapshot schedule and attaching it to your disks. Backing up your disks regularly with scheduled snapshots can reduce the risk of unexpected data loss.

**Important:** If you pause your applications before creating a snapshot, resume your workloads only after the snapshot resource reaches the `UPLOADING` status.

For more information, see the table in [Manually creating application consistent snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices#manual).

  2. [Create a snapshot](https://docs.cloud.google.com/compute/docs/disks/create-snapshots) of your existing disk.

**Note:** When creating a snapshot, Google recommends using the [`snapshots.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/insert) instead of the [`disks.createSnapshot` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/createSnapshot) because it supports more features, such as creating snapshots in a project different from the source disk project.
  3. Use the [`disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create) to create a Hyperdisk volume from your snapshot.
         
         gcloud compute disks create DISK_NAME \
          --project=DISK_PROJECT \
          --zone=ZONE \
          --storage-pool=STORAGE_POOL_NAME \
          --size=SIZE \
          --source-snapshot=projects/SNAPSHOT_PROJECT/global/snapshots/SNAPSHOT_NAME \
          --type=DISK_TYPE \
          --provisioned-iops=PROVISIONED_IOPS \
          --provisioned-throughput=PROVISIONED_THROUGHPUT
         

Replace the following:

     * DISK_PROJECT: the project to create the disk in.
     * DISK_NAME: a unique name for the disk. You can provide a list of disk names specified by spaces to create multiple disks with the same attributes.
     * ZONE: the zone where you want to create the disk. If you want to create the disk in a pool, you must specify the zone where the pool is located. Specify this value in region-zone format, for example `us-central1-a`.
     * STORAGE_POOL_NAME: Optional: the name of the pool to create the disk in. If you don't include this parameter, then a standalone Hyperdisk is created.
     * SIZE: Optional: the provisioned capacity of the new disk. The size must be greater or equal to the size of the source Persistent Disk. The value must be a whole number followed by a size unit of GB for [gibibyte](https://simple.wikipedia.org/wiki/Gibibyte), or TB for tebibyte. If no size is specified, 100 GB is used as the default value.
     * SNAPSHOT_PROJECT: The name of the project that contains the source snapshot that you created from the original disk.
     * SNAPSHOT_NAME: The name of the snapshot that you created from the original disk.
     * DISK_TYPE: the type of disk to create. If creating a disk in a pool, then this value must match the type of the pool, either `hyperdisk-balanced` or `hyperdisk-throughput`.
     * PROVISIONED_IOPS: Optional: the IOPS to provision for the disk. You can use this parameter only when you create a Hyperdisk Balanced or Hyperdisk Extreme disk.
     * PROVISIONED_THROUGHPUT: Optional: for Hyperdisk Balanced and Hyperdisk Throughput disks, the throughput in megabyte (MB) per second to provision for the disk. The value must be a positive integer.
  4. After you create the disk, you can attach the disk to any running or stopped compute instance.




###  REST 

  1. Prepare for creating a disk snapshot:

     * Review [Best practices for Compute Engine disk snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices) to prepare your disk for snapshotting.
     * Read [Create schedules for disk snapshots](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots) to learn about creating a snapshot schedule and attaching it to your disks. Backing up your disks regularly with scheduled snapshots can reduce the risk of unexpected data loss.

**Important:** If you pause your applications before creating a snapshot, resume your workloads only after the snapshot resource reaches the `UPLOADING` status.

For more information, see the table in [Manually creating application consistent snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices#manual).

  2. [Create a snapshot](https://docs.cloud.google.com/compute/docs/disks/create-snapshots) of your existing disk.

**Note:** When creating a snapshot, Google recommends using the [`snapshots.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/insert) instead of the [`disks.createSnapshot` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/createSnapshot) because it supports more features, such as creating snapshots in a project different from the source disk project. .
  3. Construct a `POST` request to the [`disks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert). Include the `name`, `sizeGb`, `type`, and `sourceSnapshot` properties.
         
         POST https://compute.googleapis.com/compute/v1/projects/DISK_PROJECT/zones/ZONE/disks
         {
            "name": "DISK_NAME",
            "sizeGb": "DISK_SIZE",
            "type": "https://compute.googleapis.com/compute/v1/projects/DISK_PROJECT/zones/ZONE/diskTypes/DISK_TYPE",
            "sourceSnapshot": "projects/SNAPSHOT_PROJECT/global/snapshots/SNAPSHOT_NAME",
            "provisionedIops": "IOPS_LIMIT",
            "provisionedThroughput": "THROUGHPUT_LIMIT",
            "accessMode": "DISK_ACCESS_MODE"
         }
         

Replace the following:

     * `DISK_PROJECT`: the project to create the disk in
     * `ZONE`: the zone where your compute instance and new disk are located
     * `DISK_NAME`: the name of the new disk
     * `DISK_SIZE`: Optional: The size of the new disk. The value must be a whole number followed by a size unit of GB for gibibytes or TB for tebibytes.
     * `DISK_TYPE`: the type of disk. To create a Hyperdisk volume, use one of the following values: `hyperdisk-balanced`, `hyperdisk-extreme`, `hyperdisk-ml`, or `hyperdisk-throughput`.
     * `SNAPSHOT_PROJECT`: The name of the project that contains the snapshot that you created from the original disk.
     * `SNAPSHOT_NAME`: The name of the snapshot that you created from the original disk.
     * `IOPS_LIMIT`: Optional: For Hyperdisk Balanced and Hyperdisk Extreme, this is the number of I/O operations per second that the disk can handle.
     * `THROUGHPUT_LIMIT`: Optional: For Hyperdisk Balanced, Hyperdisk ML, or Hyperdisk Throughput volumes, this is an integer that represents the throughput, measured in MiB per second, that the disk can handle.
     * `DISK_ACCESS_MODE`: how compute instances can access the data on the disk. Supported values are:

       * `READ_WRITE_SINGLE`, for read-write access from one instance. This is the default value.
       * `READ_WRITE_MANY`, for read-write access from multiple instances.
       * `READ_ONLY_MANY`, for read-only access from multiple instances.

You can set the access mode for the following disk types:

       * Hyperdisk Balanced
       * Hyperdisk ML
       * Hyperdisk Balanced High Availability ([Preview](https://cloud.google.com/products#product-launch-stages))
  4. Optional: Use the [ `compute.disks.get` method](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/describe) to see a description of your disk.

  5. After you create the disk, you can attach the disk to any running or stopped compute instance.




## Change a zonal disk to a regional Hyperdisk Balanced High Availability disk

How you change a zonal Hyperdisk to a Hyperdisk Balanced High Availability disk depends on the zonal disk's type:

  * If the zonal disk is a boot disk or a Hyperdisk ML or Hyperdisk Throughput disk, create a Hyperdisk Balanced High Availability volume from the snapshot of the zonal disk, as described in this section.

  * If the zonal disk is a Hyperdisk Balanced or Hyperdisk Extreme disk and is not a boot disk, create a Hyperdisk Balanced High Availability volume by [cloning the source disk](https://docs.cloud.google.com/compute/docs/disks/clone-duplicate-disks#create-regional-clone).




###  Console 

  1. Prepare for creating a disk snapshot:

     * Review [Best practices for Compute Engine disk snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices) to prepare your disk for snapshotting.
     * Read [Create schedules for disk snapshots](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots) to learn about creating a snapshot schedule and attaching it to your disks. Backing up your disks regularly with scheduled snapshots can reduce the risk of unexpected data loss.

**Important:** If you pause your applications before creating a snapshot, resume your workloads only after the snapshot resource reaches the `UPLOADING` status.

For more information, see the table in [Manually creating application consistent snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices#manual).

  2. [Create a snapshot](https://docs.cloud.google.com/compute/docs/disks/create-snapshots) of your existing disk.

**Note:** When creating a snapshot, Google recommends using the [`snapshots.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/insert) instead of the [`disks.createSnapshot` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/createSnapshot) because it supports more features, such as creating snapshots in a project different from the source disk project.
  3. Go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)
  4. Click **\+ Create Disk**.
  5. Specify a name for the disk.
  6. In the **Location** field, choose **Regional**.
  7. Specify the primary zone for the disk in the **Region** and **Zone** fields.

The disk must be in the same region as the compute instance that you plan to attach it to.

  8. Specify the secondary zone in the **Replica zone** field.
  9. For **Disk source type** , select **Snapshot** , then select the name of the snapshot to restore.
  10. Under **Disk Type** , select **Hyperdisk Balanced High Availability**.

If you don't see the Hyperdisk Balanced High Availability disk type in the list, you might have to choose a [region that offers Hyperdisk Balanced High Availability disks](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha#supported-regions). 

  11. Specify the **Size** of the new disk, in GiB. This number must be equal to or larger than the original source disk for the snapshot. 
  12. Optional: Change the default **Provisioned IOPS** and **Provisioned throughput** values for the new disk:

  13. Click **Create** to create the new disk. 
  14. After you create the disk, you can attach the disk to any running or stopped compute instance. 



###  gcloud 

  1. Prepare for creating a disk snapshot:

     * Review [Best practices for Compute Engine disk snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices) to prepare your disk for snapshotting.
     * Read [Create schedules for disk snapshots](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots) to learn about creating a snapshot schedule and attaching it to your disks. Backing up your disks regularly with scheduled snapshots can reduce the risk of unexpected data loss.

**Important:** If you pause your applications before creating a snapshot, resume your workloads only after the snapshot resource reaches the `UPLOADING` status.

For more information, see the table in [Manually creating application consistent snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices#manual).

  2. [Create a snapshot](https://docs.cloud.google.com/compute/docs/disks/create-snapshots) of your existing disk.

**Note:** When creating a snapshot, Google recommends using the [`snapshots.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/insert) instead of the [`disks.createSnapshot` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/createSnapshot) because it supports more features, such as creating snapshots in a project different from the source disk project.
  3. Use the [`disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create) to create a Hyperdisk Balanced High Availability disk from your snapshot.
         
         gcloud compute disks create DISK_NAME \
          --size=SIZE \
          --type=hyperdisk-balanced-high-availability \
          --source-snapshot=SNAPSHOT_NAME \
          --provisioned-iops=PROVISIONED_IOPS \
          --provisioned-throughput=PROVISIONED_THROUGHPUT \
          --region=REGION \
          --replica-zones=ZONE1,ZONE2
         

Replace the following:

     * `DISK_NAME`: a unique name for the disk.
     * `SIZE`: Optional: the provisioned capacity of the new disk. The size must be greater or equal to the size of the source disk. The value must be a whole number followed by a size unit of GB for [gibibyte](https://simple.wikipedia.org/wiki/Gibibyte), or TB for tebibyte.
     * `SNAPSHOT_NAME`: The name of the snapshot that you created from the original disk.
     * `PROVISIONED_IOPS`: Optional: the IOPS to provision for the disk.
     * `PROVISIONED_THROUGHPUT`: Optional: the throughput in megabyte (MB) per second to provision for the disk.
     * `REGION`: the region for the regional disk to reside in, for example: `europe-west1`
     * `ZONE1`,`ZONE2`: the zones within the region where the two disk replicas are located, for example: `europe-west1-b,europe-west1-c`



###  Terraform 

To create a Hyperdisk Balanced High Availability volume, you can use the [`google_compute_region_disk` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_disk), as shown in the following example, but change the disk type from `pd-ssd` to `hyperdisk-balanced-high-availability`.
    
    
    resource "google_compute_region_disk" "regiondisk" {
      name                      = "region-disk-name"
      snapshot                  = google_compute_snapshot.snapdisk.id
      type                      = "pd-ssd"
      region                    = "us-central1"
      physical_block_size_bytes = 4096
      size                      = 11
    
      replica_zones = ["us-central1-a", "us-central1-f"]
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

To create a Hyperdisk Balanced High Availability volume, construct a `POST` request to the [`compute.regionDisks.insert` method](https://docs.cloud.google.com/compute/docs/reference/v1/regionDisks/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/disks
    {
      "name": "DISK_NAME",
      "sourceSnapshot": "SNAPSHOT_NAME",
      "region": "projects/PROJECT_ID/regions/REGION",
      "replicaZones": [
        "projects/PROJECT_ID/zones/ZONE1",
        "projects/PROJECT_ID/zones/ZONE2"
      ],
      "sizeGb": "DISK_SIZE",
      "type": "projects/PROJECT_ID/regions/REGION/diskTypes/hyperdisk-balanced-high-availability"
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `REGION`: the region for the regional disk to reside in, for example: `europe-west1`
  * `DISK_NAME`: the name of the new disk
  * `SNAPSHOT_NAME`: The name of the snapshot that you created from the original disk.
  * `ZONE1`,`ZONE2`: the zones where replicas of the new disk should be located, for example: `europe-west1-b,europe-west1-c`
  * `DISK_SIZE`: the size, in GiB, of the new disk



## Make the new disk accessible to your VM instance

After you create the disk, you must [attach the disk](https://docs.cloud.google.com/compute/docs/disks/attach-disks) or [attach the regional disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk#repd_add_disk) to your compute instance before you can use it.

Because the new disk you created isn't a blank disk, after attaching the disk to an instance, you only need to mount the disk to make it available the operating system.

**Caution:** Don't format the disk before mounting it, because this will remove all the copied data from the disk.

For information on how to mount the disk, refer to the following:

  * [Mount the disk](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux#mounting) (Linux)
  * [Format and mount a non-boot disk on a Windows VM](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-windows)



## Remove the original disk

After verifying the new disk, you can:

  * [Delete the original disk](https://docs.cloud.google.com/compute/docs/samples/compute-disk-delete)
  * [Delete the snapshot](https://docs.cloud.google.com/compute/docs/disks/manage-snapshots#delete_a_snapshot)



## What's next

  * Learn more about [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).
  * Learn more about [Hyperdisk pools](https://docs.cloud.google.com/compute/docs/disks/pools)
  * Learn how to [modify the size and provisioned performance of a Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks).
  * [Benchmark the performance of your new Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/benchmark-hyperdisk-performance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
