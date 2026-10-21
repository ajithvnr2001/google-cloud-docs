---
url: https://docs.cloud.google.com/tpu/docs/storage-options-compute/
title: Storage options for TPU data \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:52:50.130890+00:00
---

# Storage options for TPU data  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/storage-options-compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Storage options for TPU data

This document describes data storage options you can use when training models on TPU VMs.

Workloads running on TPU VMs require data storage for the following tasks:

  * Dataset downloading and preprocessing
  * Host input pipeline processing
  * Model training input
  * Model training output
  * Checkpoints
  * Model weights
  * Key-value cache offloading



You can use the following storage options with TPU VMs:

  * Durable block storage, including the boot disk and attached storage disks
  * Cloud Storage buckets, including the Cloud Storage Rapid product family (Rapid Bucket and regional buckets with Rapid Cache)
  * Google Cloud Managed Lustre

**Note:** For information about storage for Google Kubernetes Engine (GKE) clusters, see [Storage for GKE clusters overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/storage-overview).

## Durable block storage

Durable block storage, also known as _disks_ or _volumes_ , is for data that you want to preserve after you stop, suspend, or delete your TPU VM. Durable block storage is still available even if the TPU VM crashes or fails. You can use the TPU VM boot disk or attach additional block storage to your TPU.

You might want to attach an additional disk in the following scenarios:

  * The size of your training dataset exceeds the size of the TPU boot disk.
  * You have read-only data and want faster read access using a Hyperdisk ML volume.



### TPU generation and supported disk types

The following table shows the types of disks supported by each TPU generation:

TPU generation | Supported disk types  
---|---  
TPU7x | Hyperdisk Balanced, Hyperdisk ML  
v6e | Hyperdisk Balanced, Hyperdisk ML  
v5p | Balanced Persistent Disk, Hyperdisk ML  
v5e | Balanced Persistent Disk, Hyperdisk ML  
v4 | Balanced Persistent Disk  
v3 | Balanced Persistent Disk  
v2 | Balanced Persistent Disk  
  
### TPU VM boot disk

By default, each TPU VM has a single 10 GB boot disk. When you create your VMs, you can configure a larger boot disk. For more information, see [Create a customized boot disk](https://docs.cloud.google.com/compute/docs/disks/create-root-persistent-disks). The boot disk contains the operating system, TPU drivers, and libraries. The boot disk can also store downloaded datasets temporarily for preprocessing and model input and output data, as long as the total size of the data doesn't exceed the available space on the boot disk.

If your application requires additional storage space beyond the boot disk default, you can add durable disks to your TPU VM instance or you can resize the boot disk. For more information, see the following resources:

  * [Create a new Persistent Disk volume](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk)
  * [Create a new Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk)
  * [Modify the settings for a Google Cloud Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks)
  * [Change the size of a Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk)



For information about best practices when customizing the TPU VM boot disk, see [Customize the TPU VM boot disk](https://docs.cloud.google.com/tpu/docs/storage-best-practices#customize-boot-disk).

### Attached storage

Both Google Cloud Hyperdisk and Persistent Disk are durable network storage devices that your VM instances can access like physical disks in a desktop or a server. You create both types of disks independently from your VM instances, so you can keep your data even after you delete your VM.

Advantages of using Hyperdisk over Persistent Disk include customizable performance, higher IOPS and throughput limits. For more information about Hyperdisk and Persistent Disk, see [Choose a disk type](https://docs.cloud.google.com/compute/docs/disks).

When you attach a disk to a MIG with a multi-host TPU VM slice, the system attaches the disk to each VM in that TPU slice. To prevent two or more TPU VMs from writing to a disk at the same time, you must configure all disks that you attach to a multi-host TPU slice as read-only. Read-only disks are useful for storing a dataset for processing on a TPU slice. Because Hyperdisk Balanced doesn't support read-only mode, you can only attach a Hyperdisk Balanced volume to a single TPU VM instance.

For more information about using durable block storage, see [Add a persistent disk to your VM](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk) and [Add a Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk).

### Disk backups

If the TPU VM is in an unknown state or you accidentally delete data, recovering that data from the boot disk is difficult. Back up your data using another storage option, such as Cloud Storage buckets.

If you store data on an attached disk, you can use disk snapshots, which incrementally back up data on a disk. The TPU VM boot disk does not support disk snapshots. For more information, see [About disk snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots).

## Cloud Storage

[Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) is an object storage system designed for storing and processing massive datasets (such as images, text, and video files) that require petabyte scale and massive bandwidth. It is highly cost-efficient, scalable, and resilient. When you use Cloud Storage, you store data as objects in _containers_ called _buckets_. The performance of Cloud Storage buckets depends on the [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) that you select and the location of the bucket relative to your TPU VM instance.

When using Cloud Storage, you select a bucket type based on your throughput, scale, cost, and data availability requirements. The [ Cloud Storage Rapid product family](https://docs.cloud.google.com/storage/docs/rapid/high-performance-storage), which includes Rapid Bucket and regional buckets with Rapid Cache, provides high-performance options for AI/ML workloads:

  * [**Rapid Bucket**](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket): A Cloud Storage capability that lets you store objects in the [Rapid storage class](https://docs.cloud.google.com/storage/docs/storage-classes#rapid) by creating a zonal bucket. Zonal buckets support high throughput and sub-millisecond latency for open files. They are ideal for asynchronous checkpoints, training data, and model weights.
  * [**Regional buckets**](https://docs.cloud.google.com/storage/docs/locations): A Cloud Storage bucket located in one or more regions. Regional buckets offer standard object storage performance. To meet throughput and latency requirements of AI/ML workloads, use regional buckets with [Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache). Rapid Cache is an SSD-backed zonal read cache for regional buckets that boosts throughput and reduces latency for read-intensive and cacheable workloads, such as training data loading or model weight loading for inference.



All Cloud Storage buckets have built-in redundancy to protect your data against equipment failure and to ensure data availability through data center maintenance events. Cloud Storage calculates checksums for all operations to help ensure data integrity.

Unlike durable block storage, Cloud Storage buckets don't restrict you to the zone where your instance is located. Additionally, you can read and write data to a bucket from multiple instances simultaneously. For example, you can configure instances in multiple zones to read and write data in the same bucket rather than replicate the data to durable block storage in multiple zones.

For more information, see [Connect TPU VMs to Cloud Storage buckets](https://docs.cloud.google.com/tpu/docs/storage-buckets-compute).

### Cloud Storage FUSE

Cloud Storage FUSE is a FUSE adapter that lets you mount buckets as a local file system. When using Google Kubernetes Engine, we recommend using the [Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver) and the [Cloud Storage FUSE profiles](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gcsfuse-profiles).

For more information about Cloud Storage FUSE, see the [Cloud Storage FUSE documentation](https://docs.cloud.google.com/storage/docs/gcs-fuse).

## Managed Lustre

Google Cloud Managed Lustre is a fully managed parallel file system with full POSIX compliance. It is designed for the low-latency, high-concurrency metadata performance profiles that are required for model training or inference workloads. It is optimized for ultra-low latency (less than 1 ms) workloads such as home directories, synchronous checkpoints, reinforcement learning (high-speed weight propagation storage), key-value (KV) caching offload storage, or training datasets with many small files (less than 1 MB). Managed Lustre offers a cost-effective [Dynamic tier](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers#dynamic_tier) that automatically optimizes performance based on data access patterns.

For more information, see the [Managed Lustre documentation](https://docs.cloud.google.com/managed-lustre/docs).

## What's next

  * [Create a new Persistent Disk volume](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk)
  * [Create a new Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk)
  * [Connect TPU VMs to Cloud Storage buckets](https://docs.cloud.google.com/tpu/docs/storage-buckets-compute)
  * [Storage best practices for AI/ML on TPU VMs](https://docs.cloud.google.com/tpu/docs/storage-best-practices)
  * [Cloud Storage FUSE performance tuning best practices](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
