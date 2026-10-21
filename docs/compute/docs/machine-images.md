---
url: https://docs.cloud.google.com/compute/docs/machine-images/
title: Machine images \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:05:20.661458+00:00
---

# Machine images  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/machine-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Machine images Stay organized with collections  Save and categorize content based on your preferences. 

This page describes what a machine image is, when to use it, and how it compares to other resources that store data such as snapshots or custom images. For information about creating a machine image, see [Creating machine images](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images).

A machine image is a Compute Engine resource that stores all the configuration, metadata, permissions, and data from multiple disks of a Compute Engine instance. You can use a machine image in many system maintenance, backup and recovery, and instance cloning scenarios.

## When to use a machine image

The following table compares the use of machine images, [standard disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots), [instance templates](https://docs.cloud.google.com/compute/docs/instance-templates), and [custom images](https://docs.cloud.google.com/compute/docs/images#custom_images).

Scenarios | Machine image | Standard disk snapshot | Custom image | Instance template  
---|---|---|---|---  
Single disk backup | Yes | Yes | Yes | No  
Multiple disk backup | Yes | No | No | No  
Differential backup | Yes | Yes | No | No  
Instance cloning | Yes | No | Yes | Yes  
Base image for replication | No | No | Yes | No  
  
From the preceding table, you can see that machine images are the most ideal resources for the following use cases:

  * Multiple disk backups
  * Instance cloning



### Multiple disk backups

Machine images support backups at the instance level. Disks are backed up as differential snapshots.

When a machine image is used to copy disks, Compute Engine guarantees that the data across disks is captured in a crash-consistent manner at a given time. Compute Engine uses globally consistent timestamps to ensure this guarantee. This consistency is critical if your instance is running and you want to ensure that the backup point across disks is maintained. When the backup point across disks is maintained, you can return to the same point in time across disks when you restore a machine image.

**Note:** This consistency guarantee only applies at the I/O operation level or crash level. This guarantee isn't applied at the application level. Consistency guarantees at the application level would require OS and application participation.

#### Multiple disk backup

Machine images are suitable for creating backups of all disks that are attached to a VM instance. A machine image can be used to backup multiple disks at a time. A standard disk snapshot can only backup a single disk at a time.

#### Differential disk backup

Machine images store differential snapshots of your previously created machine images or snapshots. When you generate a machine image from a Compute Engine instance, the first machine image contains a full copy of all disk data. Subsequent machine images are stored as differential copies for better performance and space efficiency. This mechanism is similar to that used by [standard disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots).

### Instance cloning

Machine images can be used to clone instances. You can use machine image to make copies of an instance that contains most of the VM configurations of the source instance. These copies can then be used for troubleshooting, scaling VM instances, debugging, or system maintenance.

## Information stored in a machine image

A machine image collects the following information from the source instance:

  * Compute Engine instance configuration. Each Compute Engine instance configuration includes the following properties:

    * Description
    * [Machine type](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology)
    * [Instance metadata](https://docs.cloud.google.com/compute/docs/metadata/overview)
    * [Labels](https://docs.cloud.google.com/compute/docs/labeling-resources)
    * [Network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags)
    * [Maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options)
    * If applicable, [Unified Extensible Firmware Interface](https://wikipedia.org/wiki/UEFI) (UEFI) variables
  * The volume mapping used to create [disks](https://docs.cloud.google.com/compute/docs/disks) for the source instance.

  * Data stored on disks at consistent points in time across the disks.




The following information from the source instance is not collected by a machine image:

  * Data in memory.
  * Data stored in attached [Local SSD disks](https://docs.cloud.google.com/compute/docs/disks#localssds). However, a machine image captures the device mapping of the Local SSD disks.
  * Attributes that are specific to the source instance, such as the name or IP address.



## Machine image storage location

To meet compliance needs, you might need to control where your data is stored. You can control where your machine image is stored geographically by specifying a `storageLocation` during the creation of your machine image. Machine images can be stored in a [Cloud Storage multi-region](https://docs.cloud.google.com/storage/docs/locations#location-mr), such as `asia` or a [Cloud Storage region](https://docs.cloud.google.com/storage/docs/locations#location-r), such as `asia-south1`.

By default, when creating a machine image from an instance, the machine image is stored in either the Cloud Storage multi-region bucket that contains the source instance, or the geographically closest Cloud Storage multi-region bucket to the source instance.

For example, if your source instance is stored in `us-central1` your machine image is stored in the `us` multi-region by default. However, a default location like `australia-southeast1` is outside of a multi-region. The closest multi-region is `asia`.

Regardless of where the machine image is stored, you can still access the machine image globally by setting the proper permissions.

## Pricing

The cost of using a machine image depends on the size of the machine image, and the location where it is stored.

To determine the cost of your machine image, complete the following steps:

  1. Use the [`gcloud compute machine-images describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/machine-images/describe) to find the storage size in bytes. When an image is created, its storage size in bytes is based on the set of blocks that have been written on the source disks that are used for the image, regardless of the contents of the blocks.
         
         gcloud compute machine-images describe MACHINE_IMAGE_NAME
         

Replace `MACHINE_IMAGE_NAME` with the name of the machine image.

  2. Scroll to the end of the output, review the value stored in the `totalStorageBytes` field. This value is in bytes, convert this value to JEDEC binary gigabytes (GB), or IEC gibibytes (GiB), where 1 GiB is 230 bytes.
         
         .......
         storageLocations:
         - us
         totalStorageBytes: '58688064'

  3. Use the pricing tables on the [Disk pricing](https://docs.cloud.google.com/compute/disks-image-pricing#section-2) page to find the cost per GB for your disk type and region.

Alternatively, you can use the [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator) to estimate the monthly cost.




## What's next

  * Learn how to [create machine images](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images)
  * Learn how to [create archive and standard disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots)
  * Learn how to [create machine images from specific disks](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images#specific-disk-backup)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
