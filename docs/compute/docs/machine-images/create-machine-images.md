---
url: https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images/
title: Create machine images \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:23.870554+00:00
---

# Create machine images  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create machine images Stay organized with collections  Save and categorize content based on your preferences. 

Use a machine image to store all the configuration, metadata, permissions, and data from multiple disks for a Compute Engine instance. The instance that you use to create a machine image is referred to as a _source instance_.

For information about when and how to use machine images, see [Machine images](https://docs.cloud.google.com/compute/docs/machine-images).

This document describes the steps for creating a machine image from a source instance.

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




## Limitations and restrictions

  * You can create a machine image of a specific instance at most 6 times every 60 minutes.
  * You can protect a machine image by using either [Cloud Key Management Service (Cloud KMS)](https://docs.cloud.google.com/kms/docs) or a customer-supplied encryption key (CSEK) ([Deprecated](https://docs.cloud.google.com/compute/docs/deprecations)). The encryption key protects the content of the disks. However, metadata isn't protected.
  * If you use a CSEK to protect your machine image, a full copy of all disk data is stored during the generation of the machine image. In all other scenarios disk data is stored in [differential copies](https://docs.cloud.google.com/compute/docs/machine-images#disk-backup).
  * You can't create machine images from source Compute Engine instances that:

    * Have attached disks with a combined capacity exceeding 200 TiB.
    * Don't have any attached disks.
    * Have any attached Hyperdisk volumes.
    * Use any Z4D, Z4M, or Z3 machine type except for `z3-highmem-192-highlssd-metal`.
    * Use a C3D, H3, or A3 machine type. 

For instances that don't support the creation of machine images, you can instead create an OS image from the boot disk of the instance, as described in [Create custom images](https://docs.cloud.google.com/compute/docs/images/create-custom).

  * You can't specify disks to include and specify disks to exclude at the same time.




### Instance and disk properties not supported by machine image

When you create machine images from instances or create instances from machine images, the following instance and disk properties are not preserved or restored:

  * `disks.architecture`
  * `disks.description`
  * `disks.labels`
  * `disks.locked`
  * `disks.multiWriter`
  * `disks.onUpdateAction`
  * `disks.provisionedIops`
  * `disks.shieldedInstanceInitialState`
  * `disks.sourceImage`
  * `disks.sourceImageEncryptionKey`
  * `disks.sourceInstantSnapshot`
  * `disks.sourceSnapshot`
  * `disks.sourceSnapshotEncryptionKey`
  * `privateIpv6GoogleAccess`
  * `resourceManagerTags`
  * `resourcePolicies`
  * `secure_tag`
  * `shieldedInstanceConfig`



## Create a machine image from an instance

By default, a machine image includes the boot disk and all other disks attached to the source Compute Engine instance. You can optionally specify which non-boot disks to include or exclude, but you can't exclude the boot disk.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.machineImages.create` on the project
  * `compute.instances.useReadOnly` on the source instance
  * `compute.disks.createSnapshot` on the disk



### Create a machine image from an instance and include all the attached disks

You can create machine images using either the [Google Cloud console](https://console.cloud.google.com/), the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute), or [REST](https://docs.cloud.google.com/compute/docs/reference/rest/v1).

To create a machine image, you need the following information:

  * A name for the machine image that you want to create.
  * The name of the source instance.
  * The zone that the source instance is located in.
  * An optional description.
  * An optional [`storageLocation`](https://docs.cloud.google.com/compute/docs/machine-images#storage-location). If you don't specify a location, then the default storage location is the [multiregional Cloud Storage location](https://docs.cloud.google.com/storage/docs/locations#location-mr) of the source instance.
  * An optional encryption key. You can choose between a Google-owned and Google-managed encryption key, a [Cloud Key Management Service (Cloud KMS)](https://docs.cloud.google.com/kms/docs) key or a customer-supplied encryption (CSEK)([Deprecated](https://docs.cloud.google.com/compute/docs/deprecations)). key. If no encryption key is specified, machine images are encrypted using a Google-owned and Google-managed encryption key.
  * If you want to use a machine image for [instance cloning and snapshotting](https://docs.cloud.google.com/compute/docs/machine-images#cloning), remove the OS and app information that is unique to the instance before generating the machine image from an instance. For example, for Windows VM instances, use `GCESysprep` to prepare the system for replication.




###  Console 

  1. In the Google Cloud console, go to the **Machine images** page.

[Go to Machine images](https://console.cloud.google.com/compute/machineImages)

  2. Click **Create Machine image**.

  3. Specify a **Name** for your machine image.

  4. Optional: Provide a **Description**.

  5. Select the **Source VM instance**.

  6. Optional: Specify where to store the machine image. Choose between **Multi-regional** or **Regional** storage. For more information about location, see [Machine image storage location](https://docs.cloud.google.com/compute/docs/machine-images#storage-location).

  7. Optional: Select an **Encryption** method.

  8. Click **Create**.




###  gcloud 

Use the [`gcloud compute machine-images create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/machine-images/create) command to create a machine image from an instance.
    
    
    gcloud compute machine-images create MACHINE_IMAGE_NAME \
        --source-instance=SOURCE_INSTANCE_NAME
    

Replace the following:

  * `MACHINE_IMAGE_NAME`: name of the machine image that you want to create.
  * `SOURCE_INSTANCE_NAME`: name of the source instance that you want to create the image from.



**Example**

For example, you can use the following `gcloud` command to create a machine image called `my-machine-image` from a source instance called `my-instance`:
    
    
    gcloud compute machine-images create my-machine-image  \
        --source-instance=my-instance
    

The process takes a few minutes. When the machine image is created, you get an output that resembles the following:
    
    
    Created [https://www.googleapis.com/compute/v1/projects/project-12345/global/machineImages/my-machine-image].
    NAME               STATUS
    my-machine-image   READY
    

###  REST 

In the API, construct a `POST` request to the [`machineimages.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/machineImages/insert) method. In the request body, include the following `POST` request:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/machineImages
    
    {
      "name": "MACHINE_IMAGE_NAME",
      "sourceInstance": "SOURCE_INSTANCE_URL"
    }
    

Replace the following:

  * `PROJECT_ID`: [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `MACHINE_IMAGE_NAME`: name of the machine image that you want to create.
  * `SOURCE_INSTANCE_URL`: full or partial URL of the source instance that you want to use to create the machine image. For example, if you have a source instance called `my-instance` in a project called `myProject`. The following URLs are valid:

    * `https://www.googleapis.com/compute/v1/projects/myProject/global/instances/my-instance`
    * `projects/myProject/global/instances/my-instance`
    * `global/instances/my-instance`



### Create a machine image and include specific disks (Preview)

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can use selective disk backup to create a machine image that includes or excludes specific non-boot disks.

Selective disk backups let you perform the following tasks when creating a machine image:

  * **Include specific non-boot disks** : you can create a machine image that backs up only the boot disk and a specific list of non-boot disks that you provide.

  * **Exclude specific non-boot disks** : you can create a machine image that backs up the boot disk and all attached non-boot disks _except_ for those you specify in an exclusion list.




#### Best practices for Linux instances

For Linux instances, we recommend the following best practices:

  * When you create a machine image that excludes specific non-boot disks or omits them using an inclusion list, ensure that the `/etc/fstab` file on Linux source Compute Engine instances uses the `nofail` option for those disks. This prevents the restored Compute Engine instance from failing to boot if an expected disk is missing.

  * During the boot process of a Compute Engine instance restored from a machine image, the operating system attempts to mount all disks listed in `/etc/fstab`. If an expected disk is missing and the `nofail` option is not specified, the boot process halts, and the instance is unbootable. As a workaround to handling boot failures, see Workarounds for boot failures caused by excluding specific disks.




#### Include only specific disks

Use the following instructions to create a machine image from only specific disks. You must always include the boot disk. You can't create a machine image from only specific disks by using the Google Cloud console. You must use the Google Cloud CLI or REST.

###  Google Cloud CLI 

Use the [`gcloud beta compute machine-images create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/machine-images/create) command to create a machine image from only specific disks.
    
    
    gcloud beta compute machine-images create MACHINE_IMAGE_NAME \
        --source-instance=SOURCE_INSTANCE_NAME \
        --source-instance-zone=ZONE \
        --include-disks=BOOT_DISK,DISK_NAME_1,DISK_NAME_2
    

Replace the following:

  * `MACHINE_IMAGE_NAME`: the name of the machine image that you want to create.
  * `SOURCE_INSTANCE_NAME`: the name of the source instance that you want to create the image from.
  * `ZONE`: the zone where the source instance is located.
  * `BOOT_DISK, DISK_NAME_1,DISK_NAME_2`: a comma-separated list of the boot disk and the non-boot disks attached to the source instance that you want to include in the machine image.



For example, you can use the following `gcloud` command to create a machine image called `my-gmi-include` from a source instance called `my-instance` located in `us-central1-a`, including only `data-disk-1` and `data-disk-2`:
    
    
    gcloud beta compute machine-images create my-gmi-include \
        --source-instance=my-instance \
        --source-instance-zone=us-central1-a \
        --include-disks=boot-disk,data-disk-1,data-disk-2
    

###  REST 

In the API, construct a `POST` request to the [`machineimages.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/beta/machineImages/insert) method. In the request body, include the following `POST` request:
    
    
    POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/global/machineImages
    
    {
      "name": "MACHINE_IMAGE_NAME",
      "sourceInstance": "SOURCE_INSTANCE_URL",
      "params": {
        "includedDisks": ["BOOT_DISK", "DISK_NAME_1", "DISK_NAME_2"]
      }
    }
    

Replace the following:

  * `PROJECT_ID`: ID of the project containing the machine image, for example, `my-project`.
  * `MACHINE_IMAGE_NAME`: name of the machine image that you want to create.
  * `SOURCE_INSTANCE_URL`: full or partial URL of the source instance that you want to use to create the machine image.
  * `BOOT_DISK, DISK_NAME_1, DISK_NAME_2`: list of the boot disk and non-boot disks attached to the source instance that you want to include in the machine image.



### Create a machine image and exclude specific disks (Preview)

Use the following instructions to create a machine image and exclude specific disks from the backup. You can't exclude the boot disk. You can't create a machine image and exclude specific disks by using the Google Cloud console. You can use the Google Cloud CLI or REST.

###  gcloud 

Use the [`gcloud beta compute machine-images create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/machine-images/create) command to create a machine image and exclude specific disks.
    
    
    gcloud beta compute machine-images create MACHINE_IMAGE_NAME \
        --source-instance=SOURCE_INSTANCE_NAME \
        --source-instance-zone=ZONE \
        --exclude-disks=DISK_NAME_1,DISK_NAME_2
    

Replace the following:

  * `MACHINE_IMAGE_NAME`: name of the machine image that you want to create.
  * `SOURCE_INSTANCE_NAME`: name of the source instance that you want to create the image from.
  * `ZONE`: zone where the source instance is located.
  * `DISK_NAME_1,DISK_NAME_2`: comma-separated list of the non-boot disks attached to the source instance that you want to exclude from the machine image.



**Example**

For example, you can use the following `gcloud` command to create a machine image called `my-gmi-exclude` from a source instance called `my-instance` located in `us-central1-a`, excluding `temp-disk-1` and `scratch-disk`:
    
    
     gcloud beta compute machine-images create my-gmi-exclude \
        --source-instance=my-instance \
        --source-instance-zone=us-central1-a \
        --exclude-disks=temp-disk-1,scratch-disk
    

###  REST 

In the API, construct a `POST` request to the [`machineimages.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/beta/machineImages/insert) method. In the request body, include the following `POST` request:
    
    
    POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/global/machineImages
    
    {
      "name": "MACHINE_IMAGE_NAME",
      "sourceInstance": "SOURCE_INSTANCE_URL",
      "params": {
        "excludedDisks": ["DISK_NAME_1", "DISK_NAME_2"]
      }
    }
    

Replace the following:

  * `PROJECT_ID`: ID of the project containing the machine image.
  * `MACHINE_IMAGE_NAME`: name of the machine image that you want to create.
  * `SOURCE_INSTANCE_URL`: full or partial URL of the source instance that you want to use to create the machine image.
  * `DISK_NAME_1, DISK_NAME_2`: list of the non-boot disks attached to the source instance that you want to exclude from the machine image.



#### Workarounds for boot failures caused by excluding specific disks

If you create an instance from a machine image where an excluded disk causes a boot failure, you can recover the instance using either of the following workarounds:

  * **Connect to the serial console** : [enable and connect to the interactive serial console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console) of the unbootable Compute Engine instance. Sign in to troubleshoot and edit the `/etc/fstab` file directly to remove the missing disk entry or add the `nofail` option.

  * **Disk swapping** : if a Compute Engine instance fails to boot because a disk was excluded from the machine image but is still listed in `/etc/fstab` without the `nofail` option, use the following instructions to repair the configuration using Google Cloud CLI.

    1. Stop the unbootable Compute Engine instance using the [`gcloud compute instances stop`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/stop) command:
           
           gcloud compute instances stop UNBOOTABLE_INSTANCE_NAME \
            --zone=ZONE
           

Replace the following:

       * `UNBOOTABLE_INSTANCE_NAME`: name of the unbootable Compute Engine instance.
       * `ZONE`: zone where the Compute Engine instances are located.
    2. Detach the boot disk using the [`gcloud compute instances detach-disk`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/detach-disk) command:
           
           gcloud compute instances detach-disk UNBOOTABLE_INSTANCE_NAME \
            --disk=BOOT_DISK_NAME \
            --zone=ZONE
           

Replace the following:

       * `UNBOOTABLE_INSTANCE_NAME`: name of the unbootable Compute Engine instance.
       * `BOOT_DISK_NAME`: name of the boot disk attached to the unbootable Compute Engine instance.
       * `ZONE`: zone where the Compute Engine instances are located.
    3. Attach the disk as a secondary disk to another working Compute Engine instance using the [`gcloud compute instances attach-disk`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk) command:
           
           gcloud compute instances attach-disk SECONDARY_INSTANCE_NAME \
            --disk=BOOT_DISK_NAME \
            --zone=ZONE
           

Replace the following:

       * `SECONDARY_INSTANCE_NAME`: name of the working secondary Compute Engine instance used for repairing the disk.
       * `BOOT_DISK_NAME`: name of the boot disk attached to the unbootable Compute Engine instance.
       * `ZONE`: zone where the Compute Engine instances are located.
    4. Mount the disk and edit its `/etc/fstab` file to correct the problematic entry using the following sequence of instructions:

       1. Connect to the secondary Compute Engine instance using SSH:
              
              gcloud compute ssh SECONDARY_INSTANCE_NAME \
              --zone=ZONE
              

Replace the following:

          * `SECONDARY_INSTANCE_NAME`: name of the working secondary Compute Engine instance used for repairing the disk.
          * `ZONE`: zone where the Compute Engine instances are located.
       2. Identify the attached disk, usually `/dev/sdb` or similar, using `lsblk`:
              
              lsblk
              

       3. Create a temporary mount point:
              
              sudo mkdir /mnt/repair
              

       4. Mount the root partition:
              
              sudo mount /dev/DEVICE_PARTITION /mnt/repair
              

Replace `DEVICE_PARTITION` with the device name and partition number of the attached secondary disk on the secondary Compute Engine instance (for example, `sdb1`).

       5. Open the `fstab` file:
              
              sudo nano /mnt/repair/etc/fstab
              

       6. Either add the `nofail` option to the missing disk's entry or comment out the line entirely by adding a `#` at the beginning.

       7. Save and exit.

       8. Unmount the disk:
              
              sudo umount /mnt/repair
              

    5. Detach the disk from the secondary Compute Engine instance using the [`gcloud compute instances detach-disk`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/detach-disk) command:
           
           gcloud compute instances detach-disk SECONDARY_INSTANCE_NAME \
            --disk=BOOT_DISK_NAME \
            --zone=ZONE
           

Replace the following:

       * `SECONDARY_INSTANCE_NAME`: name of the working secondary Compute Engine instance used for repairing the disk.
       * `BOOT_DISK_NAME`: name of the boot disk attached to the unbootable Compute Engine instance.
       * `ZONE`: zone where the Compute Engine instances are located.
    6. Reattach the disk as the boot disk to the original Compute Engine instance using the [`gcloud compute instances attach-disk`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk) command:
           
           gcloud compute instances attach-disk UNBOOTABLE_INSTANCE_NAME \
            --disk=BOOT_DISK_NAME \
            --boot \
            --zone=ZONE
           

Replace the following:

       * `UNBOOTABLE_INSTANCE_NAME`: name of the unbootable Compute Engine instance.
       * `BOOT_DISK_NAME`: name of the boot disk attached to the unbootable Compute Engine instance.
       * `ZONE`: zone where the Compute Engine instances are located.
    7. Start the repaired Compute Engine instance:
           
           gcloud compute instances start UNBOOTABLE_INSTANCE_NAME \
            --zone=ZONE
           

Replace the following:

       * `UNBOOTABLE_INSTANCE_NAME`: name of the unbootable Compute Engine instance.
       * `ZONE`: zone where the Compute Engine instances are located.



## What's next?

  * Learn more about [machine images](https://docs.cloud.google.com/compute/docs/machine-images)
  * [Create instances from machine images](https://docs.cloud.google.com/compute/docs/machine-images/create-instance-from-machine-image)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
