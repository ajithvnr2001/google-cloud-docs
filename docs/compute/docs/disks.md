---
url: https://docs.cloud.google.com/compute/docs/disks/
title: Choose a disk type \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:05.106827+00:00
---

# Choose a disk type  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Choose a disk type Stay organized with collections  Save and categorize content based on your preferences. 

This document discusses the block storage, commonly referred to as _disks_ or _volumes_ , offered by Compute Engine. You can use block storage for boot and data volumes for all compute instances, including virtual machines (VMs), containers, and bare metal instances. This page discusses how to choose block storage for your compute instances.

The terms _disk_ , _volume_ , and _block storage volume_ are synonymous and are used interchangeably across the documentation, the Google Cloud console, the Google Cloud CLI, and the REST API.

## About block storage

Google Cloud offers two types of disks, or block storage—temporary and durable block storage. You can combine these block storage types in a single compute instance.

### Temporary block storage

Temporary, or ephemeral, block storage offers the fastest performance among all block storage types, with the tradeoff that the _stored data is lost if the VM stops for any reason_. Data is lost if you stop, suspend, or restart the VM, or if the VM crashes or fails.

Because of its ephemeral nature, use temporary block storage for only scratch data, caches such as `tempdb` for Microsoft SQL Server, or storage for flash-optimized databases. You can't use temporary block storage as a boot volume.

Local SSD, including Titanium SSD, is the temporary block storage offering in Google Cloud. Local SSD disks are physically attached to the server that hosts your instance.

For more information about Local SSD, see the following sections:

  * Review [Local SSD performance limits](https://docs.cloud.google.com/compute/docs/disks/local-ssd)
  * To learn when Local SSD data is preserved, see [Local SSD data persistence](https://docs.cloud.google.com/compute/docs/disks/local-ssd#data_persistence)
  * [Supported machine series for Local SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd#machine-types)
  * [Add Local SSD disks you create a VM](https://docs.cloud.google.com/compute/docs/disks/add-local-ssd)



### Durable block storage

Durable, or persistent, block storage is for data that you want to preserve after you stop, suspend or delete the VM, or even if the VM crashes or fails.

[Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) and [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) are the durable block storage offerings in Google Cloud, but Persistent Disk isn't available with the latest machine series. Google recommends using Hyperdisk for the highest performance and advanced features.

Hyperdisk and Persistent Disk volumes have the following characteristics:

  * **Function as physical disks** : you can use a Hyperdisk or Persistent Disk volume with compute instance as if it was a physical disk attached to the instance. However, they are network-attached devices that transmit data over Google's networks.

  * **Portability** : Hyperdisk and Persistent Disk volumes are independent of the compute instances that you attach them to. This characteristic means you can attach a volume to a running instance without downtime. You can also detach the volume to keep your data even after you delete the instance.

  * **Security** : by default, data is encrypted at rest and in transit. You can also customize the encryption with your own keys.

  * **High availability options** : protect your data from zonal failures by replicating the volume across two zones.




### Differences between Hyperdisk and Persistent Disk

Hyperdisk and Persistent Disk both offer durable, secure, and efficient block storage, but Google recommends using Hyperdisk.

Hyperdisk offers the following key advantages over Persistent Disk:

  * Customizable performance: You can independently configure the performance and size of each Hyperdisk volume. Hyperdisk performance is independent of provisioned capacity. This feature means that you can increase or decrease a Hyperdisk volume's performance without changing its size.

Unlike Hyperdisk, Persistent Disk performance depends on provisioned capacity. Consequently, to improve a Persistent Disk volume's performance, you must increase its size.

  * Better overall performance: Hyperdisk has higher IOPS and throughput limits than Persistent Disk.




## Choose a type of block storage

To decide between Local SSD, Hyperdisk and Persistent Disk, follow these steps:

  1. Determine whether you need durable or temporary block storage. For example, the boot volume for a compute instance must use durable block storage.

  2. If you need to use temporary block storage, use Local SSD if Local SSD is available for your machine series. If you need durable storage, continue to the next step.

  3. If you need to use durable block storage, use Hyperdisk if it's [available for your machine series](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support). If your machine series doesn't support Hyperdisk, use Persistent Disk.

  4. Choose the Hyperdisk or Persistent Disk type that best suits your workload. To learn about the Hyperdisk and Persistent Disk types, see [Choose a Hyperdisk type](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#when-to-use) and [Persistent Disk types](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#disk-types), respectively.




For more information about the features, performance, and durability of Hyperdisk, see [About Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks). For Persistent Disk, see [About Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks).

## Alternatives to block storage

In addition to the disks that Google Cloud offers, you can deploy the following alternative storage solutions on your compute instances.

  * [Create a file server or distributed file system](https://docs.cloud.google.com/architecture/filers-on-compute-engine) on Compute Engine to use as a network file system with NFSv3 and SMB3 capabilities.
  * [Mount a RAM disk](https://docs.cloud.google.com/compute/docs/disks/mount-ram-disks) within the VM memory that offers high throughput and low latency.



To compare block storage with the other storage options available in Google Cloud, such as Cloud Storage and Filestore, see [Review the storage options](https://docs.cloud.google.com/architecture/storage-advisor#review_the_storage_options) in the Cloud Architecture Center.

## Cost considerations

You're billed for the storage capacity provisioned from when you create a volume until you delete the volume. This charge applies to Local SSD, Persistent Disk, and Hyperdisk.

Costs continue to apply through the following scenarios:

  * Boot volumes that are created automatically when you create a compute instance
  * Durable storage volumes that are attached to a stopped or suspended instance
  * Durable storage volumes that aren't attached to any VM



For Hyperdisk and Extreme Persistent Disk volumes, you're billed for the provisioned performance.

For example, since Hyperdisk ML volumes support customizing only throughput, you're billed for the provisioned throughput for a Hyperdisk ML volume, but not for the IOPS the volume uses.

However, you're billed for the provisioned IOPS and throughput of Hyperdisk Balanced volumes, because Hyperdisk Balanced volumes support configuring IOPS and throughput.

For more pricing information, see [Disk and image pricing](https://cloud.google.com/compute/disks-image-pricing).

## What's next

  * View machine series availability for each storage option:

    * [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support)
    * [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#pd-machine-series)
    * [Local SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd#machine-series-lssd)
  * Learn more about each storage option:

    * [About Local SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd)
    * [About Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks)
    * [About Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks)
  * Learn how to use each storage option:

    * [Create a VM with Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/add-local-ssd#create_local_ssd)
    * [Add a Hyperdisk volume to your VM](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk)
    * [Add a Persistent Disk volume to your VM](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk)



  * To learn about replication for Hyperdisk and Persistent Disk volumes, see [About synchronous disk replication](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
