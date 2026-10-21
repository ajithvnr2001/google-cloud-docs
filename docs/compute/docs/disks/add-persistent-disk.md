---
url: https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk/
title: Create a new Persistent Disk volume \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:30.424224+00:00
---

# Create a new Persistent Disk volume  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a new Persistent Disk volume Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

You can either create a blank Persistent Disk volume, or [create a disk from a data source](https://docs.cloud.google.com/compute/docs/disks/create-disk-from-source). You can use Persistent Disk as a boot disk for a compute instance, or as a data disk that you attach to an instance.

This document explains how to create a blank, non-boot zonal Persistent Disk volume and attach it to your VM.

For other types of disk creation and addition, see the following:

  * To create a boot disk that you can later use to create an instance, see [Create a customized boot disk](https://docs.cloud.google.com/compute/docs/disks/create-root-persistent-disks).

  * To add a Google Cloud Hyperdisk disk to an instance, see [Add Google Cloud Hyperdisk storage to an instance](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk).

  * To add a disk to an instance that is part of a managed instance group (MIG), see [Apply new VM configurations in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs).




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




## Restrictions

  * During VM creation, you can attach up to 127 secondary non-boot zonal Persistent Disk volumes.
  * You can have a total attached capacity of 257 TB per VM. For information about how to ensure maximum performance with large volumes, see [Logical volume size](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance#logical_volume_size).



## Persistent Disk size limits and reference names

When you create a Persistent Disk volume with the Google Cloud CLI, REST, or the Cloud Client Libraries for Compute Engine, indicate the Persistent Disk type to create by providing the value in the **Reference name** column in the following table.

The size you specify for a Persistent Disk volume must be within the ranges listed in following table.

Disk type | Reference name | Minimum size | Maximum size | Default size  
---|---|---|---|---  
Balanced Persistent Disk | `pd-balanced` | Zonal: 10 GiB  
Regional: 10 GiB | 64 TiB | 100 GiB  
Performance (SSD) Persistent Disk | `pd-ssd` | Zonal: 10 GiB  
Regional: 10 GiB | 64 TiB | 100 GiB  
Standard Persistent Disk | `pd-standard` | Zonal: 10 GiB  
Regional: 200 GiB | 64 TiB | 500 GiB  
Extreme Persistent Disk | `pd-extreme` | 500 GiB | 64 TiB | 1 TiB  
  
## Add a non-boot Persistent Disk to your instance

Create and attach a non-boot zonal Persistent Disk by using the [Google Cloud console](https://console.cloud.google.com/), the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute), or [REST](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances).

You should specify a custom device name when attaching the disk to a VM. The name you specify is used to generate a [symlink](https://docs.cloud.google.com/compute/docs/disks/disk-symlinks) for the disk in the guest OS, making identification easier.

**Caution:** If you add a custom device name to a disk after you attach the disk to a VM, Compute Engine temporarily detaches the disk from the VM, which might disrupt your workloads.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.disks.create` on the project before you can create a new disk
  * `compute.instances.attachDisk` on the VM
  * `compute.disks.use` permission on the disk to attach

**Note:** If you create a disk in the Google Cloud console and don't specify a disk type, the default [disk type](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#disk-types) is `pd-balanced`. If you create a disk using the gcloud CLI or REST, the default disk type is `pd-standard`.

###  Console 

  1. Go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Click the name of the VM where you want to add a disk.

  3. On the details page, click **edit Edit**.

  4. In the **Storage** section, under **Additional disks** , click **Add new disk**.

  5. Specify a name for the disk and configure the disk's properties.

  6. Under **Disk source type** , choose the data source for the disk: 

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
  7. Optional: For advanced configuration options, expand the expand_more **Show advanced configurations** section. 

     * Select the disk attachment mode in the **Mode** field.
     * Choose to keep or delete the disk when the instance is deleted by selecting the option in the **Deletion rule** field.
     * To make identifying the disk easier from within the guest OS, specify a custom device name. Under the heading **Device name** , select the option **Use a custom device name**. In the **Device name** field, enter a string to use as a symlink for the disk. 
  8. Click **Done** to complete the disk's configuration.

  9. Click **Save** to apply your changes to the VM and add the new disk.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Use the [`gcloud compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create) to create the zonal Persistent Disk volume.
         
         gcloud compute disks create DISK_NAME \
           --size DISK_SIZE --zone=ZONE \
           --type DISK_TYPE
         

Replace the following:

     * `DISK_NAME`: the name of the new disk.
     * `DISK_SIZE`: the size, in gigabytes, of the new disk. Acceptable sizes range, in 1 GB increments, from 10 GB to 65,536 GB, inclusive.
     * `ZONE`: the zone where Compute Engine create the disk, for example, `us-central1-f`.
     * `DISK_TYPE`: the type of the new disk. For example, for SSD Persistent Disk, specify `pd-ssd`.
  3. After you create the disk, attach it to any running or stopped VM. Use the [`gcloud compute instances attach-disk` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk):
         
         gcloud compute instances attach-disk VM_NAME \
           --disk DISK_NAME --device-name=DEVICE_NAME \
           --zone=ZONE
         

Replace the following:

     * `VM_NAME`: the name of the VM where you are adding the new zonal Persistent Disk volume
     * `DISK_NAME`: the name of the new disk that you are attaching to the VM.
     * `DEVICE_NAME`: Optional: a name that the guest OS uses to identify the disk.
     * `ZONE`: the zone where Compute Engine creates the instance and disk, for example, `us-central1-f`.
  4. Use the [`gcloud compute disks describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/describe) to see a description of your disk.




###  Terraform 

To create a disk, use the [`google_compute_disk` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_disk).
    
    
    # Using pd-standard because it's the default for Compute Engine
    
    resource "google_compute_disk" "default" {
      name = "disk-data"
      type = "pd-standard"
      zone = "us-west1-a"
      size = "5"
    }

To attach the disk to a VM, use the [`google_compute_instance` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance).
    
    
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

  1. Construct a `POST` request to create a zonal Persistent Disk by using the [`disks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert). Include the `name`, `sizeGb`, and `type` properties. To create this disk as an empty and unformatted non-boot disk, don't specify a source image or a source snapshot.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks
         
         {
          "name": "DISK_NAME",
          "sizeGb": "DISK_SIZE",
          "type": "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/diskTypes/DISK_TYPE"
         }
         

Replace the following:

     * `PROJECT_ID`: your project ID.
     * `ZONE`: the zone where your VM and new disk are located.
     * `DISK_NAME`: the name of the new disk.
     * `DISK_SIZE`: the size, in gigabytes, of the new disk. Acceptable sizes range, in 1 GB increments, from 10 GB to 65,536 GB, inclusive.
     * `DISK_TYPE`: the type of the new disk. For example, for SSD Persistent Disk, specify `pd-ssd`.
  2. Construct a POST request to the [`compute.instances.attachDisk`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/attachDisk) method, and include the URL to the zonal Persistent Disk volume that you just created:
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/attachDisk
         
         {
          "source": "/compute/v1/projects/PROJECT_ID/zones/ZONE/disks/DISK_NAME",
          "deviceName": DEVICE_NAME
         }
         

Replace the following:

     * `PROJECT_ID`: your project ID
     * `ZONE`: the zone where your VM and new disk are located
     * `VM_NAME`: the name of the VM where you are adding the new Persistent Disk volume
     * `DISK_NAME`: the name of the new disk
     * `DEVICE_NAME`: Optional: a name that the guest OS uses to identify the disk.



After you create the new disk and attach it to a VM, you must format and mount the disk, so that the operating system can use the available storage space.

## What's next

  * Learn how to [format and mount your new disks on a Linux VM](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux).
  * Learn how to [format and mount your new disks on a Windows VM](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-windows).
  * Learn how to [resize your Persistent Disk volumes](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk).
  * Learn how to regularly [back up your disks using snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots) to prevent unintended data loss.
  * To enable high availability for your disks, learn about [regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk), which synchronously replicates a disk between two zones.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
