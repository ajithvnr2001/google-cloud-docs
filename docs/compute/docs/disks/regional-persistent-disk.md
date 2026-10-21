---
url: https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk/
title: Create and manage regional disks \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:29.195759+00:00
---

# Create and manage regional disks  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create and manage regional disks Stay organized with collections  Save and categorize content based on your preferences. 

[Hyperdisk Balanced High Availability and regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk) are storage options that let you implement high availability (HA) services in Compute Engine. Regional Persistent Disk and Hyperdisk Balanced High Availability synchronously replicate data between two zones in the same region and ensure HA for disk data for up to one zonal failure. The regional disk can be a boot disk or a data disk. You can attach regional disks only to instances that are in the same zones as the disk's replicas. 

To allow different instances to concurrently access a Hyperdisk Balanced High Availability volume, set the access mode for the volume. For more information, see [Share a disk between instances](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms).

This document explains how to do the following tasks for regional disks:

  * Create regional disks.
  * Attach a regional disk to your Compute Engine instance.
  * Change a zonal disk to a regional disk.
  * Create a new instance with a regional boot disk.
  * Create a new instance with additional regional disks.
  * Attach a regional boot disk to an instance.
  * List and describe your regional disks.
  * Resize a regional disk.



## Before you begin

  * Review the basics of [synchronous disk replication](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk).
  * Read about [regional disk failover](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk#repd-failover).
  * If using multi-writer mode for Hyperdisk Balanced High Availability disks, review the requirements and limitations in [Share disks between instances](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms).
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

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles and permissions

To get the permissions that you need to create a regional disk, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To connect to an instance that can run as a service account: [Service Account User (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create a regional disk. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a regional disk:

  * `compute.disks.create`
  * `compute.instances.attachDisk`
  * `compute.disks.use`
  * Create a snapshot of a disk: `compute.disks.createSnapshot`
  * Create a regional disk from an image: `compute.images.useReadOnly` on the image 
  * View the details for a disk: `compute.disks.get`
  * Get a list of disks: `compute.disks.list`
  * Change the size of a disk: `compute.disks.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Limitations

  * You can attach regional Persistent Disk only to VMs that use [E2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#e2_machine_types), [N1](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_machines), [N2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_machines), and [N2D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2d_machines) machine types.
  * You can attach Hyperdisk Balanced High Availability only to [supported machine types](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha#machine-series-support). 
  * When using read-only mode, you can attach a regional Balanced Persistent Disk to a maximum of 10 VM instances.
  * The minimum size of a regional Standard Persistent Disk is 200 GiB.
  * You can only increase the size of a regional Persistent Disk or Hyperdisk Balanced High Availability volume; you can't decrease its size.
  * Regional Persistent Disk and Hyperdisk Balanced High Availability volumes have different performance characteristics than their corresponding zonal disks. For more information, see [About Persistent Disk performance](https://docs.cloud.google.com/compute/docs/disks/performance) and [Hyperdisk Balanced High Availability performance limits](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha#perf-limits). 
  * You can't change the size of a Hyperdisk Balanced High Availability volume that's in multi-writer mode if any of the instances that the volume is attached to is in a zone that's experiencing an outage. 
  * You can't use a Hyperdisk Balanced High Availability volume that's in multi-writer mode as a boot disk.
  * If you create a replicated disk by cloning a zonal disk, then the two zonal replicas aren't fully in sync at the time of creation. After creation, you can use the regional disk clone within 3 minutes, on average. However, you might need to wait for tens of minutes before the disk reaches a fully replicated state and the [ recovery point objective (RPO)](https://wikipedia.org/wiki/Recovery_point_objective) is close to zero. Learn how to [ check if your replicated disk is fully replicated](https://docs.cloud.google.com/compute/docs/disks/monitor-regional-persistent-disk-replica-state#determine_repd_replication_state).
  * You can't create regional disks in [AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones).
  * Creating a regional disk from an image has the following limitations: 
    * When you create a regional disk from an image, you can create one disk within a project every 5 minutes. You can issue up to 5 requests at once but you can't create more than 5 disks within a 25-minute period. 
    * Creating a regional disk from an image is in [Preview](https://cloud.google.com/products#product-launch-stages), and is slower than creating a zonal disk from an image. 
  * You can't create a regional disk by cloning the source disk if the source disk is a Hyperdisk ML or Hyperdisk Throughput volume. You must [create a new Hyperdisk Balanced High Availability volume from a snapshot of the zonal disk](https://docs.cloud.google.com/compute/docs/disks/migrate-to-hyperdisk#migrate-to-hdbha). 




## About using a regional disk as a boot disk for an instance

You can attach a regional Persistent Disk or Hyperdisk Balanced High Availability disk as a boot disk for stateful workloads that are provisioned ahead of time, before you provision a production workload. Regional boot disks are not intended for hot standbys, because you can't simultaneously attach one boot disk to two instances.

In a high availability setup, if the boot device is a regional disk, Google recommends that you don't pre-create and start the standby instance. Instead, at the failover stage, attach the existing regional disk when you create the standby instance by using the `forceAttach` option.

You can create a regional boot disk from any of the following Compute Engine resources:

  * Standard and archive snapshots
  * Public and custom images ([Preview](https://cloud.google.com/products#product-launch-stages))
  * Instant snapshots
  * Zonal boot disks, by cloning the disk ([Preview](https://cloud.google.com/products#product-launch-stages)).



To use a regional disk as the boot disk for an instance, use one of the following methods.

  * Create the instance and the boot disk at the same time.
  * Create a regional boot disk, and then use the disk as the boot disk for a new or existing instance:

    1. Create a regional boot disk using one of the following methods:

       * [Clone an existing zonal boot disk](https://docs.cloud.google.com/compute/docs/disks/clone-duplicate-disks#create-regional-clone) ([Preview](https://cloud.google.com/products/#product-launch-stages))
       * Create a new disk from an image ([Preview](https://cloud.google.com/products/#product-launch-stages)) or snapshot
    2. Attach the regional boot disk to an instance.

We recommend creating regional boot disks from snapshots and not from clones of zonal boot disks.




To failover a regional boot disk to a running standby instance in the replica zone, use the steps described in Attach a regional boot disk to an instance.

## Size limits and reference names for regional disks

The size you specify for a regional disk must be within the ranges listed in following table.

When you create a regional disk with the Google Cloud CLI, REST, or the Cloud Client Libraries for Compute Engine, you can indicate the type of disk to create by providing the value in the **Reference name** column in the following table.

Disk type | Reference name | Minimum size | Maximum size | Default size  
---|---|---|---|---  
Hyperdisk Balanced High Availability | `hyperdisk-balanced-high-availability` | 4 GiB | 64 TiB | 100 GiB  
Balanced Persistent Disk | `pd-balanced` | Zonal: 10 GiB  
Regional: 10 GiB | 64 TiB | 100 GiB  
Performance (SSD) Persistent Disk | `pd-ssd` | Zonal: 10 GiB  
Regional: 10 GiB | 64 TiB | 100 GiB  
Standard Persistent Disk | `pd-standard` | Zonal: 10 GiB  
Regional: 200 GiB | 64 TiB | 500 GiB  
  
## Create a regional disk from an image or snapshot

Create a regional Persistent Disk or Hyperdisk Balanced High Availability volume that you can use as a boot or data disk for an instance. The regional disk must be in the same region as the compute instance that you plan to attach it to.

If you create a Hyperdisk Balanced High Availability volume, you can also allow different instances to concurrently access the disk by setting the disk access mode. For more information, see [Share a disk between instances](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms).

For regional Persistent Disk, if you create a disk in the Google Cloud console, the default [disk type](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#disk-types) is `pd-balanced`. If you create a disk using the gcloud CLI or REST, the default disk type is `pd-standard`. 

###  Console 

  1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. Select the required project.

  3. Click **Create disk**.

  4. Specify a **Name** for your disk.

  5. For the **Location** , choose **Regional**.

  6. Select the **Region** and **Zone**. You must select the same region when you create your instance.

  7. Select the **Replica zone** in the same region. Make a note of the zones that you select because you must attach the disk to your instance in one of those zones.

  8. Under **Disk source type** , choose the data source for the disk:

     * To create a blank disk, select **Blank disk**.
     * To create the disk from an image: 
       1. Select **Image**.
       2. Under **Source image** , choose the source image for the disk.
     * To create the disk from an existing snapshot: 
       1. Select **Snapshot** , **Instant snapshot** or **Archive snapshot** , depending on whether the source snapshot is a standard snapshot, an instant snapshot, or an archive snapshot, respectively.
       2. Under **Source snapshot** , select the source snapshot or instant snapshot from the list. Only snapshots that are in the location you selected are listed.
     * To create the disk from a specific disk that's within a machine image (Preview): 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

       1. Select **Machine Image**.
       2. In the **Source machine image** drop-down menu, select the machine image you want to use.
       3. In the **Source disk** drop-down menu, select the device name of the specific disk within the chosen machine image that you want to use as the source for the new disk.
       4. If the selected machine image is protected by a Customer-supplied encryption key (CSEK) ([Deprecated](https://docs.cloud.google.com/compute/docs/deprecations/csek-deprecation-in-compute-engine)), an **Encryption** section appears. Enter the required decryption key in the provided field.
       5. Configure other disk properties such as **Name** , **Type** , **Size** , and **Deletion** rule as needed.
  9. Under **Disk settings** , choose a **Disk type** and **Size**. For Hyperdisk Balanced High Availability volumes, you can also change the default **Provisioned IOPS** , and **Provisioned Throughput** settings.

  10. Optional: For Hyperdisk Balanced High Availability volumes, you can enable attaching the disk to multiple instances by creating the disk in multi-writer mode. In **Access mode** , select **Multiple VMs read write**.

  11. Click **Create** to finish creating your disk.




###  gcloud 

Create a regional disk by using the [`compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create).

You can create a blank disk, or you can create the disk from an image ([Preview](https://cloud.google.com/products#product-launch-stages)), an instant snapshot, or a standard snapshot.

###  Blank disk 
    
    
    gcloud compute disks create DISK_NAME \
     --size=DISK_SIZE \
     --type=DISK_TYPE \
     --region=REGION \
     --replica-zones=ZONE1,ZONE2 \
     --access-mode=DISK_ACCESS_MODE
    

Replace the following: 

  * `DISK_NAME`: the name of the new disk
  * `DISK_SIZE`: the size, in GiB, of the new disk. Must be within the size limits for the disk type. 
  * `DISK_TYPE`: For regional Persistent Disk, this is the type of the regional disk. The default value is `pd-standard`. For Hyperdisk, specify the value `hyperdisk-balanced-high-availability`.
  * `REGION`: the region for the regional disk to reside in, for example: `europe-west1`
  * `ZONE1`,`ZONE2`: the zones within the region where the two disk replicas are located, for example: `europe-west1-b,europe-west1-c`
  * `DISK_ACCESS_MODE`: optional: For Hyperdisk Balanced High Availability disks, specify how instances can access the data on the disk. The following values are supported: 
    * `READ_WRITE_SINGLE`, for read-write access from one instance. This is the default. 
    * `READ_WRITE_MANY`, for read-write access from multiple instances.



###  Snapshot 

To create the disk from a **standard or archive snapshot** , use the `--source-snapshot` flag to specify the name of the snapshot.
    
    
    gcloud compute disks create DISK_NAME \
      --size=DISK_SIZE \
      --type=DISK_TYPE \
      --region=REGION \
      --replica-zones=ZONE1,ZONE2 \
      --access-mode=DISK_ACCESS_MODE \
      **--source-snapshot= SNAPSHOT_NAME** \
      [ --source-snapshot-region=SOURCE_REGION ]
    

Replace the following: 

  * `DISK_NAME`: the name of the new disk
  * `DISK_SIZE`: the size, in GiB, of the new disk. Must be within the size limits for the disk type. 
  * `DISK_TYPE`: For regional Persistent Disk, this is the type of the regional disk. The default value is `pd-standard`. For Hyperdisk, specify the value `hyperdisk-balanced-high-availability`.
  * `REGION`: the region for the regional disk to reside in, for example: `europe-west1`
  * `ZONE1`,`ZONE2`: the zones within the region where the two disk replicas are located, for example: `europe-west1-b,europe-west1-c`
  * `DISK_ACCESS_MODE`: optional: For Hyperdisk Balanced High Availability disks, specify how instances can access the data on the disk. The following values are supported: 
    * `READ_WRITE_SINGLE`, for read-write access from one instance. This is the default. 
    * `READ_WRITE_MANY`, for read-write access from multiple instances.
  * `SNAPSHOT_NAME` with the name of the snapshot. 
  * `SOURCE_REGION`: optional. If the snapshot is a regionally scoped snapshot, specify the region that the snapshot is scoped to.



To create the disk **from an instant snapshot** , use the `--source-instant-snapshot` flag to specify the name of the instant snapshot.
    
    
     gcloud compute disks create DISK_NAME \
        **--source-instant-snapshot= INSTANT_SNAPSHOT_NAME**
    

Replace `INSTANT_SNAPSHOT_NAME` with the name of the instant snapshot.

###  Image 

**Preview — Creating a regional disk from an image**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To create the disk from a specific version of a public image or from a custom image, use the beta version of the command. Specify the name of the image with `--image` flag:
    
    
     gcloud beta compute disks create DISK_NAME \
        --size=DISK_SIZE \
        --type=DISK_TYPE \
        --region=REGION \
        --replica-zones=ZONE1,ZONE2 \
        --access-mode=DISK_ACCESS_MODE \
        **--image= IMAGE_NAME**
    

Replace the following: 

  * `DISK_NAME`: the name of the new disk
  * `DISK_SIZE`: the size, in GiB, of the new disk. Must be within the size limits for the disk type. 
  * `DISK_TYPE`: For regional Persistent Disk, this is the type of the regional disk. The default value is `pd-standard`. For Hyperdisk, specify the value `hyperdisk-balanced-high-availability`.
  * `REGION`: the region for the regional disk to reside in, for example: `europe-west1`
  * `ZONE1`,`ZONE2`: the zones within the region where the two disk replicas are located, for example: `europe-west1-b,europe-west1-c`
  * `DISK_ACCESS_MODE`: optional: For Hyperdisk Balanced High Availability disks, specify how instances can access the data on the disk. The following values are supported: 
    * `READ_WRITE_SINGLE`, for read-write access from one instance. This is the default. 
    * `READ_WRITE_MANY`, for read-write access from multiple instances.
  * `IMAGE_NAME` with the name of the image, for example: `debian-13-trixie-v20260902`. 



To create the disk using the latest version of an [image family](https://docs.cloud.google.com/compute/docs/images#image_families), use the beta version of the command. Specify the image family name with the `--image-family` flag:
    
    
     gcloud beta compute disks create DISK_NAME \
        --size=DISK_SIZE \
        --type=DISK_TYPE  --region=REGION \
        --replica-zones=ZONE1,ZONE2 \
        **--image-family= IMAGE_FAMILY_NAME**
    

Replace `IMAGE_FAMILY_NAME` with the name of the image family, for example, `debian-13`.

###  Terraform 

To create a regional Persistent Disk or Hyperdisk Balanced High Availability volume, use the [`google_compute_region_disk` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_disk).

To specify the type of the disk, set the `type` argument to the corresponding value from the following list.

  * Hyperdisk Balanced High Availability: `hyperdisk-balanced-high-availability`
  * SSD Persistent Disk: `pd-ssd`
  * Balanced Persistent Disk: `pd-balanced`
  * Standard Persistent Disk: `pd-standard`



To create a disk from an image ([Preview](https://cloud.google.com/products#product-launch-stages)), replace the `snapshot` argument in the following example with the [`image` argument](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_disk#image-1).

The following example creates a regional disk from a snapshot.
    
    
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

To create a regional Persistent Disk or Hyperdisk Balanced High Availability volume, construct a `POST` request to the [`compute.regionDisks.insert` method](https://docs.cloud.google.com/compute/docs/reference/v1/regionDisks/insert).

You can create a blank disk, or you can create the disk from an image ([Preview](https://cloud.google.com/products#product-launch-stages)) or a standard or instant snapshot.

###  Blank disk 

To create a blank disk, construct a `POST` request with the following request body:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/disks
    {
     
       "name": "DISK_NAME",
       "region": "projects/PROJECT_ID/regions/REGION",
       "replicaZones": [
       "projects/PROJECT_ID/zones/ZONE1",
       "projects/PROJECT_ID/zones/ZONE2"
       ],
       "sizeGb": "DISK_SIZE",
       "type": "projects/PROJECT_ID/regions/REGION/diskTypes/DISK_TYPE",
       "accessMode": "DISK_ACCESS_MODE"
    }
    

Replace the following: 

  * `PROJECT_ID`: your project ID
  * `REGION`: the region for the regional disk to reside in, for example: `europe-west1`
  * `DISK_NAME`: the name of the new disk
  * `ZONE1`,`ZONE2`: the zones where replicas of the new disk should be located
  * `DISK_SIZE`: the size, in GiB, of the new disk. Must be within the size limits for the disk type.
  * `DISK_TYPE`: For regional Persistent Disk, this is the type of Persistent Disk. For Hyperdisk, specify the value `hyperdisk-balanced-high-availability`
  * `DISK_ACCESS_MODE`: Optional: for Hyperdisk Balanced High Availability disks, specify how instances can access the data on the Hyperdisk Balanced High Availability disk. The following values are supported: 
    * `READ_WRITE_SINGLE`, for read-write access from one instance. This is the default.
    * `READ_WRITE_MANY`, for read-write access from multiple instances.



###  Snapshot 

To create the disk **from a standard or archive snapshot** , use the `sourceSnapshot` field to specify the URL of the snapshot.

  * If the snapshot is a global snapshot:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/ REGION/disks
        {
        
           "name": "DISK_NAME",
           "region": "projects/PROJECT_ID/regions/REGION",
           "replicaZones": [
           "projects/PROJECT_ID/zones/ZONE1",
           "projects/PROJECT_ID/zones/ZONE2"
           ],
           "sizeGb": "DISK_SIZE",
           "type": "projects/PROJECT_ID/regions/REGION/diskTypes/DISK_TYPE",
           "accessMode": "DISK_ACCESS_MODE",
        **"sourceSnapshot": " SNAPSHOT_NAME"**
        }
        

Replace the following: 

    * `PROJECT_ID`: your project ID
    * `REGION`: the region for the regional disk to reside in, for example: `europe-west1`
    * `DISK_NAME`: the name of the new disk
    * `ZONE1`,`ZONE2`: the zones where replicas of the new disk should be located
    * `DISK_SIZE`: the size, in GiB, of the new disk. Must be within the size limits for the disk type.
    * `DISK_TYPE`: For regional Persistent Disk, this is the type of Persistent Disk. For Hyperdisk, specify the value `hyperdisk-balanced-high-availability`
    * `DISK_ACCESS_MODE`: Optional: for Hyperdisk Balanced High Availability disks, specify how instances can access the data on the Hyperdisk Balanced High Availability disk. The following values are supported: 
      * `READ_WRITE_SINGLE`, for read-write access from one instance. This is the default.
      * `READ_WRITE_MANY`, for read-write access from multiple instances.
    * `SNAPSHOT_NAME`: the name of the standard or archive snapshot. 
  * If the snapshot is a **regionally scoped snapshot** ([Preview](https://cloud.google.com/products/#product-launch-stages)), then use the beta version of the endpoint:
        
        POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/regions/REGION/disks
        {
          "name": "DISK_NAME",
          **"sourceSnapshot": "projects/ PROJECT_ID/regions/SOURCE_REGION/snapshots/SNAPSHOT_NAME"**
        }
        

Replace the following:

    * `REGION`: the region for the regional disk to reside in, for example: `europe-west1`
    * `SOURCE_REGION`: the region that the source snapshot is scoped to
    * `SNAPSHOT_NAME`: the source snapshot for the disk



To create the disk from an **instant snapshot** , use the `sourceInstantSnapshot` field instead of `sourceSnapshot` to specify the URL of the instant snapshot.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/ PROJECT_ID/regions/REGION/disks
    {
     "name": "DISK_NAME",
     **"sourceInstantSnapshot": "projects/ PROJECT/regions/SOURCE_REGION/instantSnapshots/ SOURCE_INSTANT_SNAPSHOT_NAME"**
    }
    

Replace `SOURCE_INSTANT_SNAPSHOT_NAME` with the name of the instant snapshot.

###  Image 

**Preview — Creating a regional disk from an image**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To create the disk from a custom or public image, use the beta version of the endpoint and specify the URL of the image with the `sourceImage` field.

  * To use a **custom image** or the latest version of a custom image family:
        
        POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/regions/REGION/disks
        {
        
           "name": "DISK_NAME",
           "region": "projects/PROJECT_ID/regions/REGION",
           "replicaZones": [
           "projects/PROJECT_ID/zones/ZONE1",
           "projects/PROJECT_ID/zones/ZONE2"
           ],
           "sizeGb": "DISK_SIZE",
           "type": "projects/PROJECT_ID/regions/REGION/diskTypes/DISK_TYPE",
           "accessMode": "DISK_ACCESS_MODE",
        **"sourceImage": "global/images/ IMAGE_NAME_OR_PATH"**
        }
        

Replace the following: 

    * `PROJECT_ID`: your project ID
    * `REGION`: the region for the regional disk to reside in, for example: `europe-west1`
    * `DISK_NAME`: the name of the new disk
    * `ZONE1`,`ZONE2`: the zones where replicas of the new disk should be located
    * `DISK_SIZE`: the size, in GiB, of the new disk. Must be within the size limits for the disk type.
    * `DISK_TYPE`: For regional Persistent Disk, this is the type of Persistent Disk. For Hyperdisk, specify the value `hyperdisk-balanced-high-availability`
    * `DISK_ACCESS_MODE`: Optional: for Hyperdisk Balanced High Availability disks, specify how instances can access the data on the Hyperdisk Balanced High Availability disk. The following values are supported: 
      * `READ_WRITE_SINGLE`, for read-write access from one instance. This is the default.
      * `READ_WRITE_MANY`, for read-write access from multiple instances.
    * `IMAGE_NAME_OR_PATH`: To use a specific image, replace the `IMAGE_NAME_OR_PATH` with the name of the image, for example: `custom-debug-image`. To use an image from an image family, specify `family/IMAGE_FAMILY_NAME`, where `IMAGE_FAMILY_NAME` is the name of the image family. For example, `family/debug-image-family`. 
  * To use a specific public image or the latest version of a public image family:
        
        POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/regions/REGION/disks
        {
        "name": "DISK_NAME",
        **"sourceImage": "projects/ IMAGE_PROJECT/global/images/IMAGE_NAME_OR_PATH"**
        }
        

Replace the following:

    * `IMAGE_PROJECT`: the [project](https://docs.cloud.google.com/compute/docs/images#os-compute-support) that contains the public image. For example, to use a Debian image, specify `debian-cloud`.
    * `IMAGE_NAME_OR_PATH`: the name or path to the image. To use a specific version of an image, specify the image name, for example: `debian-13-trixie-v20260902`. To use the latest version of a public OS image, specify the image family name, for example: `family/debian-13`.



After you create the disk, you can use it as a boot disk for an instance or attach it as a data disk to an instance.

## Attach a regional disk to your instance

To attach a regional boot disk to an instance, see Attach a regional boot disk to an instance.

For disks that are not boot disks, after you create a regional Persistent Disk or Hyperdisk Balanced High Availability volume, you can attach it to an instance. The instance must be in the same region as the disk.

To attach a Hyperdisk Balanced High Availability disk to multiple instances, repeat the procedure in this section for each instance. You can attach Hyperdisk Balanced High Availability disks only in read-write mode.

###  Console 

  1. To attach a disk to an instance, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the **Name** column, click the name of the instance.

  3. Click **Edit** edit.

  4. Click **+Attach existing disk**.

  5. Choose the previously created regional disk to add to your instance.

  6. If you see a warning that indicates the selected disk is already attached to another instance, select the **Force-attach disk** box to force-attach the disk to the instance that you are editing.

Review the use cases for force-attaching regional disks at [Regional disk failover](https://docs.cloud.google.com/compute/docs/disks/repd-failover).

  7. Optional: If attaching a Hyperdisk Balanced High Availability disk to multiple instances, for **Disk attachment mode** , select **Read/write**.

  8. Click **Save**.

  9. On the **Edit VM** page, click **Save**.




###  gcloud 

To attach a regional disk to a running or stopped instance, use the [`compute instances attach-disk` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk) with the `--disk-scope` flag set to `regional`.

If attaching a Hyperdisk Balanced High Availability disk in multi-writer mode to multiple instances, the only supported attachment mode is `rw`, which is the default access mode. You don't need to include the `--mode` flag.
    
    
    gcloud compute instances attach-disk INSTANCE_NAME \
        --disk=DISK_NAME \
        --disk-scope=regional \
        --device-name=DEVICE_NAME
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance to which you're adding the regional disk
  * `DISK_NAME`: the name of the new disk that you're attaching to the instance
  * `DEVICE_NAME`: Optional: a name that the guest OS uses to create a [symlink](https://docs.cloud.google.com/compute/docs/disks/disk-symlinks), which helps identify the disk at the OS level.



###  Terraform 

To attach a regional Persistent Disk or Hyperdisk Balanced High Availability volume to an instance, you can use the [`google_compute_attached_disk` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_attached_disk).
    
    
    resource "google_compute_instance" "test_node" {
      name         = "test-node"
      machine_type = "f1-micro"
      zone         = "us-west1-a"
    
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-13"
        }
      }
      attached_disk {
        source      = google_compute_disk.default.id
        device_name = google_compute_disk.default.name
      }
    
      network_interface {
        network = "default"
        access_config {
          # Ephemeral IP
        }
      }
    
      # Ignore changes for persistent disk attachments
      lifecycle {
        ignore_changes = [attached_disk]
      }
    
    
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

To attach a regional disk to a running or stopped instance, construct a `POST` request to the [`compute.instances.attachDisk` method](https://docs.cloud.google.com/compute/docs/reference/v1/instances/attachDisk) and include the URL to the regional disk that you created.

If attaching a Hyperdisk Balanced High Availability disk in multi-writer mode to multiple instances, the only supported attachment mode is `READ-WRITE`, which is the default access mode. You don't need to include the `mode` property.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/attachDisk
     {
      "source": "/projects/PROJECT_ID/regions/REGION/disks/DISK_NAME",
      "deviceName": DEVICE_NAME
     }
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `ZONE`: the location of your instance
  * `INSTANCE_NAME`: the name of the instance to which you're adding the new regional disk
  * `REGION`: the region where the regional disk is located
  * `DISK_NAME`: the name of the regional disk (as shown in the Google Cloud console).
  * `DEVICE_NAME`: Optional: a name that the guest OS uses to create a [symlink](https://docs.cloud.google.com/compute/docs/disks/disk-symlinks), which helps identify the disk at the OS level.



For non-boot disks, after you create and attach a blank regional disk to an instance, you must [format and mount the disk](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux), so that the operating system can use the available storage space.

## Change a zonal disk to a regional disk

How you change a zonal disk to a regional disk depends on the type of the zonal disk:

  * To convert an existing zonal disk of the following types to a regional disk, create a clone of the source disk.

    * Hyperdisk Balanced volumes
    * Hyperdisk Extreme volumes
    * Balanced, SSD, and Standard Persistent Disk volumes

To learn how to clone a disk, see [Create a regional disk by cloning the source disk](https://docs.cloud.google.com/compute/docs/disks/clone-duplicate-disks#create-regional-clone).

  * To convert a disk of any of the following types to a regional disk, follow the steps in [Change a zonal disk to a Hyperdisk Balanced High Availability disk](https://docs.cloud.google.com/compute/docs/disks/migrate-to-hyperdisk#migrate-to-hdbha):

    * Hyperdisk Throughput
    * Hyperdisk ML



## Create an instance that uses a new regional boot disk

When setting up a highly available compute instance, you can create the primary instance with a new regional boot disk. When you create an instance at the same time as its regional boot disk, you can create the boot disk from an image ([Preview](https://cloud.google.com/products/#product-launch-stages)) or a standard snapshot.

**Important:** You can't use a disk that's in multi-writer mode as a boot disk.

To create a new regional disk from an existing zonal disk instead, you must first Change the zonal disk to a regional disk, and then create the instance with the regional disk that you created.

This section describes how to create an instance with a new, regional, boot disk using the Google Cloud console, Google Cloud CLI, or REST.

**Preview — Creating a regional disk from an image**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

If prompted, select your project and click **Continue**.

The **Create an instance** page appears and displays the **Machine configuration** pane.

  2. In the **Machine configuration** pane, do the following:

     1. In the **Name** field, specify a name for your instance. For more information, see [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).
     2. Optional: In the **Zone** field, select a zone for this instance.

The default selection is **Any**. If you don't change this default selection, then Google automatically chooses a zone for you based on machine type and availability. 

     3. Select a machine family for your instance from one of the following options:

        * **General purpose**
        * **Compute optimized**
        * **Memory optimized**
        * **Storage optimized**
        * **Network optimized**
        * **GPUs**
        * **TPUs**

The Google Cloud console then displays the machine series that are available for your selected machine family.

     4. In the **Series** column, select the machine series for your instance.

If you selected **GPUs** as the machine family in the previous step, then select the **GPU type** that you want. The machine series is then automatically selected for the selected GPU type.

     5. In the **Machine type** section, select the machine type for your instance.

  3. In the navigation menu, click **OS and storage**. In the **Operating system and storage** pane that appears, complete the following steps.

To learn more about the parameters that you can configure while adding new disks, see [About Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) and [About Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).

     1. To start configuring your boot disk, click **Change**. The **Boot disk** pane appears and displays the **Public images** tab.
     2. Configure the data source for the boot disk in one of the following ways:

**Note:** Unless you explicitly choose a different boot disk, if the name of the new instance matches the name of an existing disk, then the existing disk automatically attaches to the new instance as the boot disk.

        * To choose a public image as the data source for your boot disk, in the **Public images** tab, specify the following: 
          1. In the **Operating system** list, select the OS type.
          2. In the **Version** list, select the OS version.
          3. In the **Boot disk type** list, select the type of the boot disk.
          4. In the **Size (GB)** field, specify the size of the boot disk.
        * To choose a custom image as the data source for your boot disk, click **Custom images** and then, in the **Custom images** tab that appears, specify the following: 
          1. To select the image project, click **Change** , and then select the project that contains the image.
          2. In the **Image** list, select the image that you want to import.
          3. In the **Boot disk type** list, select the type of the boot disk.
          4. In the **Size (GB)** field, specify the size of the boot disk.
        * To choose a standard snapshot as the data source for your boot disk, click **Snapshots** and then, in the **Snapshots** tab that appears, specify the following: 
          1. In the **Snapshot** list, select the snapshot.
          2. In the **Boot disk type** list, select the type of the boot disk.
          3. In the **Size (GB)** field, specify the size of the boot disk.
        * To choose an archive snapshot as the data source for your boot disk, click **Archive snapshots** and then, in the **Archive snapshots** tab that appears, specify the following: 
          1. In the **Archive snapshot** list, select the archive snapshot.
          2. In the **Boot disk type** list, select the type of the boot disk.
          3. In the **Size (GB)** field, specify the size of the boot disk.
        * To choose an existing disk as your boot disk, click **Existing disks**. Then, in the **Existing disks** tab that appears, select an existing disk in the **Disk** list. _This option uses the existing disk as the boot disk and doesn't create a new disk._
     3. Optional: For advanced configuration options, expand the expand_more **Show advanced configurations** section.

     4. To confirm your boot disk options and return to the **Operating system and storage** pane, click **Select**.

     5. Optional: To learn how to attach non-boot disks to your instance, see [Create an instance with additional non-boot disks](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-additional-non-boot-disks).

  4. If you did not choose an existing boot disk, configure it to be a regional disk by doing the following:

     1. In the navigation menu, click **Data protection**. In the **Data protection** pane that appears, do the following:

**Caution:** The data backup and replication settings that you specify while creating an instance using the Google Cloud console are applied only when your selected instance and disk configurations support those options. You must verify that your configuration for the instance and each disk meets the requirements for each data protection option that you specify. For more information, see the requirements for regional disks and [Data protection options](https://docs.cloud.google.com/compute/docs/disks/data-protection).
        1. To configure all new disks for the instance to use [synchronous disk replication](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) (regional Persistent Disk or Hyperdisk Balanced High Availability), select the **Regional disks** checkbox.

        2. (No action required by default.) Clear the **Exclude boot disks** checkbox.

  5. Optional: Specify other configuration options. For more information, see [Configuration options during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview#new_instance_configuration_options).

  6. To create and start the instance, click **Create**.




###  gcloud 

Use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) to create an instance, and the `--create-disk` flag to specify the regional disk. When specifying the disk parameters, the characters `^:^` specify that the separation character between parameters is a colon (`:`). This lets you use a comma (`,`) when specifying the replica-zones parameter.

  * To create an instance and create its regional boot disk from a public image or a custom image ([Preview](https://cloud.google.com/products/#product-launch-stages)):
        
        gcloud compute instances create PRIMARY_INSTANCE_NAME \
        --zone=ZONE --project=PROJECT_ID \
        --create-disk=^:^name=REGIONAL_DISK_NAME:boot=true:type=DISK_TYPE:replica-zones=ZONE,REMOTE_ZONE:[IMAGE_NAME_OR_FAMILY]
        

Replace the following:

    * PRIMARY_INSTANCE_NAME: a name for the instance
    * ZONE: the name of the zone in which to create the instance
    * PROJECT_ID: the name of the project in which to create the instance
    * REGIONAL_DISK_NAME: a name for the regional disk
    * DISK_TYPE: the type of disk to create, for example, `hyperdisk-balanced-high-availability`. If using a Persistent Disk, then you must also specify `scope=regional` within the `--create-disk` flag to create a Regional Persistent Disk.
    * REMOTE_ZONE: the alternate zone for the regional disk
    * IMAGE_NAME_OR_FAMILY: the name or family of the image to use.

    * To use a specific version of a public or custom image, specify `image=<var>IMAGE_NAME</var>`, where `<var>IMAGE_NAME</var>` is the image name. For example, `image=debian-13-trixie-v20260902` or `image=my-custom-image`.

    * To use an [image family](https://docs.cloud.google.com/compute/docs/images#image_families), specify `image-family=<var>IMAGE_FAMILY</var>:image-family-scope=global`. This creates the instance that uses the most recent, non-deprecated OS image in the image family.

For example, to use the latest version of the OS image in the Debian 13 image family, specify `image-family=debian-13:image-family-scope=global`.

  * To create an instance and create a regional boot disk from a snapshot:
        
        gcloud compute instances create PRIMARY_INSTANCE_NAME \
        --zone=ZONE --project=PROJECT_ID \
        --create-disk=^:^name=REGIONAL_DISK_NAME:boot=true:type=DISK_TYPE:source-snapshot=SNAPSHOT_NAME:replica-zones=ZONE,REMOTE_ZONE
        

Use the same parameters as the previous command, and replace `<var>SNAPSHOT_NAME</var>` with the name of the snapshot for the boot disk, for example, `dev-snapshot-may2026`.




###  REST 

Create a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) and specify the properties `boot: 'true'` and `replicaZones`. To create the instance from a snapshot, specify the `sourceSnapshot` property. To create the instance from an image, specify the `sourceImage` property.

  * To create an instance and create its regional boot disk from a snapshot:


    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    {
     "name": "INSTANCE_NAME",
     "disks": [{
        "boot": true,
        "initializeParams": {
           "sourceSnapshot": "global/snapshots/BOOT_SNAPSHOT_NAME",
           "replicaZones": [
               "projects/PROJECT_ID/zones/ZONE",
               "projects/PROJECT_ID/zones/REMOTE_ZONE"
           ],
           "diskType": "projects/PROJECT_ID/zones/ZONE/diskTypes/DISK_TYPE"
        }
      }],
     "networkInterfaces": [
        {
          "network": "global/networks/default"
        }
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `ZONE`: the name of the zone where you want to create the instance
  * `INSTANCE_NAME`: a name for the instance
  * `BOOT_SNAPSHOT_NAME`: the name of the boot disk snapshot
  * `REMOTE_ZONE`: the remote zone for the regional disk
  * `DISK_TYPE`: the type of disk to create, for example, `hyperdisk-balanced-high-availability` or `pd-balanced`

  * To create an instance and create its regional boot disk from an image ([Preview](https://cloud.google.com/products/#product-launch-stages)):



    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    {
     "name": "INSTANCE_NAME",
     "disks": [{
        "boot": true,
        "initializeParams": {
           "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE_NAME",
           "replicaZones": [
               "projects/PROJECT_ID/zones/ZONE",
               "projects/PROJECT_ID/zones/REMOTE_ZONE"
           ],
           "diskType": "projects/PROJECT_ID/zones/ZONE/diskTypes/DISK_TYPE"
        }
      }],
     "networkInterfaces": [
        {
          "network": "global/networks/default"
        }
      ]
    }
    

## Create a new instance and attach regional data disks

When creating an instance, you can optionally include regional Persistent Disk or Hyperdisk Balanced High Availability volumes as additional data disks.

To create and attach a regional Persistent Disk or Hyperdisk Balanced High Availability volume to an instance during instance creation, see either of the following:

  * [Create an instance with additional non-boot disks](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-additional-non-boot-disks)
  * [Create a new instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#create_a_new_instance_template)



## Attach a regional boot disk to an instance

Follow the steps in this section to complete any of the following tasks:

  * Replace the boot disk of an existing instance with a regional boot disk.
  * Failover a regional boot disk to a hot standby instance that is running in the backup zone. You do this by attaching the regional disk to the instance as the boot disk.



These steps assume that the regional disk and instance already exist.

To attach a regional boot disk to an instance, use the gcloud CLI or REST.

###  gcloud 

  1. Stop the instance. 
         
         [gcloud compute instances stop](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/stop) INSTANCE_NAME  --zone=ZONE
         

  2. Detach the current boot disk from the instance. 
         
         [gcloud compute instances detach-disk](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/detach-disk) INSTANCE_NAME \
          --zone=ZONE --disk=CURRENT_BOOT_DEVICE_NAME
         

  3. Attach the regional boot disk to the instance. 
         
         [gcloud compute instances attach-disk](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk) INSTANCE_NAME  \
          --zone=ZONE  \
          --disk=REGIONAL_DISK_NAME  \
          --disk-scope=regional --force-attach \
          --boot
         

  4. Restart the instance. 
         
         [gcloud compute instances start](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/start) INSTANCE_NAME
         

**Note:** If the instance you want to start uses customer-supplied encryption keys, you must provide those keys when trying to start the instance. For more information, see [Start an instance that has encrypted disks](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#start_a_vm_that_has_encrypted_disks).



Replace the variables in the previous commands with the following:

  * `INSTANCE_NAME`: the name of the instance to which you want to attach the regional boot disk
  * `ZONE`: the zone in which the instance is located
  * `CURRENT_BOOT_DEVICE_NAME`: the name of the boot disk being used by the instance. This is usually the same as the name of the instance.
  * `REGIONAL_DISK_NAME`: the name of the regional disk that you want to attach to the instance as a boot disk



Optional: If you can't successfully detach the regional boot disk from the primary instance due to an outage or failure, include the flag `--force-attach`.

###  REST 

  1. Stop the instance.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/stop
         

  2. Detach the current boot disk from the instance.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/detachDisk?deviceName=CURRENT_BOOT_DEVICE_NAME
         

  3. Attach the regional boot disk to the instance.

Construct a `POST` request to the `compute.instances.attachDisk` method, and include the URL to the regional boot disk:
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/attachDisk
         {
         "source": "compute/v1/projects/PROJECT_ID/regions/REGION/disks/REGIONAL_DISK_NAME",
         "boot": true
         }

  4. Restart the instance.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/start
         

**Note:** If the instance you want to start uses customer-supplied encryption keys, you must provide those keys when trying to start the instance. For more information, see [Start an instance that has encrypted disks](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#start_a_vm_that_has_encrypted_disks).



Replace the variables in the previous commands with the following:

  * `PROJECT_ID`: your project ID
  * `INSTANCE_NAME`: the name of the instance to which you want to attach the regional disk
  * `ZONE`: the zone in which the instance is located
  * `CURRENT_BOOT_DEVICE_NAME`: the name of the boot disk being used by the instance. This is usually the same as the name of the instance.
  * `REGION`: the region in which the regional disk is located
  * `REGIONAL_DISK_NAME`: the name of the regional disk that you want to attach to the instance as a boot disk



Optional: If you can't successfully detach the regional boot disk from the instance that it was originally attached to because of an outage or failure, include `"forceAttach": true` in the request body.

## List and describe your regional disks

You can view a list of all your configured regional disks, and information about their properties, including the following:

  * Disk ID
  * Disk name
  * Size
  * Disk type
  * Region
  * Zonal replicas



To view detailed information about your regional disks, use the following:

  * To view the details of all regional disks in a specific region and project: 
    * Construct a `GET` request to the [`compute.regionDisks.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionDisks/list).
    * Use the [`gcloud compute disks list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/list) and filter the results by region.
  * To view the details of a specific regional disk: 
    * Run the [`gcloud compute disks describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/describe) with the `--region` flag, and specify the name of the disk and its region.
    * Construct a `GET` request to the [`compute.regionDisks.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionDisks/get).



## Resize a regional disk

If instances with regional disks require additional storage space, you can resize the disks. You can resize a regional disk at any time, even if the disk is attached to a running instance. If you need to separate your data into unique volumes, create multiple secondary disks for the instance. For Hyperdisk Balanced High Availability you can also increase the IOPS and throughput limits for the disk.

### Decrease the size of a regional disk

You can only increase, and not decrease, the size of a disk. To decrease the disk size, you must create a new disk with a smaller size. Until you delete the original, larger disk, you are charged for both disks.

### Considerations for resizing a Hyperdisk Balanced High Availability volume that's in multi-writer mode

You can increase the size of a Hyperdisk Balanced High Availability volume that's in multi-writer mode while it is attached to multiple instances. However, you must keep the following constraints in mind:

  * You can't increase the size of a Hyperdisk Balanced High Availability volume that's in multi-writer mode if any of the instances that the volume is attached to is in a zone that's experiencing an outage.
  * You must wait for the resize operation to complete before you attempt to access the disk from any of the attached instances.
  * After the resize operation completes, you must verify that the updated disk size is visible to all the attached instances.
  * After you verify that the updated disk size is visible to all the attached instances, you must connect to one of the attached instances to resize the file system.



### How to increase the size of a regional disk

The command for resizing a regional disk is very similar to that for resizing a zonal disk. However, you must specify a region instead of a zone for the disk location. For instructions on how to modify a regional disk, see the following: 

  * Regional Persistent Disk: [Increase the size of a Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#increase_the_size_of_a_disk)
  * Hyperdisk Balanced High Availability: [Modify a Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks#modify_hyperdisk)



## What's next

  * Learn about [disk pricing](https://cloud.google.com/compute/disks-image-pricing).
  * Learn how to [monitor the replica states of regional disks](https://docs.cloud.google.com/compute/docs/disks/monitor-regional-persistent-disk-replica-state).
  * Learn how to [determine the replication state of a regional disk](https://docs.cloud.google.com/compute/docs/disks/monitor-regional-persistent-disk-replica-state#determine-repd-replication-status-monitoring). 
  * Review [Share Persistent Disk volumes between compute instances](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms) as an alternative to Regional Persistent Disks for read-only data. 
  * [Create a snapshot of a disk](https://docs.cloud.google.com/compute/docs/disks/create-snapshots).
  * Learn about [instance groups](https://docs.cloud.google.com/compute/docs/instance-groups) for compute instances.
  * Learn how to [build scalable and resilient web applications on Google Cloud](https://docs.cloud.google.com/architecture/scalable-and-resilient-apps).
  * See the [Google Cloud disaster recovery planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
