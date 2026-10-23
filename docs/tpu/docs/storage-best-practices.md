---
url: https://docs.cloud.google.com/tpu/docs/storage-best-practices/
title: Storage best practices for AI/ML workloads on TPU VMs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:15.467995+00:00
---

# Storage best practices for AI/ML workloads on TPU VMs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/storage-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Storage best practices for AI/ML workloads on TPU VMs

To maximize the performance and cost-efficiency of your AI/ML workloads on TPU VMs, select and configure the right storage solution for your workload. By removing I/O bottlenecks, you can reduce the amount of time that your TPU accelerators are idle, which reduces training time and costs.

This document provides workload-specific storage recommendations and optimization best practices for training, checkpointing, serving, and caching on TPU VMs. Before applying these practices, review the available [Storage options for TPU data](https://docs.cloud.google.com/tpu/docs/storage-options). This document assumes that you are familiar with TPU VMs and have basic experience provisioning Cloud Storage resources.

## Workload-specific guidance

The following table provides storage recommendations, listed in order of preference, for different workloads:

Workload | Recommendation | Optimization and tooling (if applicable)  
---|---|---  
**Training datasets, including data preparation** | 

  1. Use [Cloud Storage regional buckets](https://docs.cloud.google.com/storage/docs/buckets) with [Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache) and client-side tuning (such as read-ahead reads) for the lowest cost. 
  2. Use [Cloud Storage Rapid Bucket](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket) for the best performance and scale. 
  3. Use [Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/overview) if you're standardizing on Lustre (file system storage) due to high metadata concurrency or small files (less than 1 MB). 

| 

  * For regional Cloud Storage buckets, enable hierarchical namespace. 
  * For regional Cloud Storage buckets or Rapid Bucket, use Cloud Storage FUSE and [gRPC](https://grpc.io/). For GKE, use the [`gcsfusecsi-training` profile](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gcsfuse-profiles#select-performance-profile). 
  * For Managed Lustre, consider using the Dynamic tier to reduce costs and automatically optimize performance. 

  
**Checkpointing and reinforcement learning weights** | 

  1. Use [Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/overview) for high performance without extensive tuning for low latency (less than 1 ms) requirements, such as synchronous checkpoints and high-speed weight propagation for reinforcement learning. 
  2. Use [Cloud Storage Rapid Bucket](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket) for the highest throughput for asynchronous and multi-tiered checkpointing and parallelizing checkpoint operations to storage. Rapid Bucket provides the high throughput needed for these workloads. 

|  For Rapid Bucket, use the [`gcsfusecsi-checkpointing` profile](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gcsfuse-profiles#select-performance-profile).   
**Model storage and download** | 

  1. Use [Hyperdisk ML](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-ml) for small model caching and up to 2,500 instances. 
  2. Use the same storage solution that you use for training datasets (Managed Lustre, Rapid Bucket, or regional buckets) if you want to standardize on a single storage solution. 

|  For downloading models, use [GKE Run:ai Model Streamer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/run-ai-model-streamer) or Cloud Storage FUSE with a separate mount point using the [`gcsfusecsi-serving` profile](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gcsfuse-profiles#select-performance-profile).   
**Key-value (KV) cache offload** | 

  1. Always use host CPU memory (RAM) as the primary tier to free up VRAM without adding significant latency. 
  2. If CPU memory is insufficient, use [Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/overview) as a parallel, low-latency second tier in the cache hierarchy to meet the ultra low latency (less than 1 ms) needs of KV cache offloading at high throughput (up to 10 TB/s). 

|   
  
## Cloud Storage optimizations

The following sections describe best practices to optimize performance when using Cloud Storage with TPU VMs.

### Enable hierarchical namespace for metadata optimization

To improve metadata performance, enable hierarchical namespace when you create regional buckets for AI/ML workloads. Metadata performance refers to how quickly Cloud Storage can process operations that involve looking up, listing, or modifying object paths and folders, rather than reading or writing the file contents themselves.

In buckets without hierarchical namespace enabled, folders don't exist as actual resources, but are instead [simulated folders](https://docs.cloud.google.com/storage/docs/folder-types) represented by object name prefixes delimited by forward slashes (`/`). This makes operations like listing directory contents or renaming directories slow because the system must scan all objects with that prefix. Hierarchical namespace provides a true file system structure, which is important for AI/ML workloads for several reasons:

  * **Atomic directory renames** : ML frameworks use directory renames to finalize checkpoints. Hierarchical namespace supports atomic renames, ensuring that checkpoints are finalized quickly.
  * **Higher initial QPS** : Hierarchical namespace supports up to eight times higher initial queries per second (QPS) for reads and writes compared to buckets without hierarchical namespace enabled. This prevents bottlenecks when many TPUs access storage simultaneously.
  * **Efficient folder-level operations** : Finding and listing files within specific directories is much faster, reducing response times during training and data loading.



Zonal buckets, offered through Rapid Bucket, use hierarchical namespace by default. For more information, see [Hierarchical namespace overview](https://docs.cloud.google.com/storage/docs/hns-overview).

### Use Cloud Storage FUSE with appropriate profiles

[Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview) is a FUSE adapter that lets you mount buckets as a local file system. When using Google Kubernetes Engine, we recommend using the [Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver) and the [Cloud Storage FUSE profiles](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gcsfuse-profiles) to automate performance tuning.

For more information about best practices for using Cloud Storage FUSE, see [Performance tuning best practices](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance).

## Customize the TPU VM boot disk

You can customize the guest OS environment on a TPU VM by using startup scripts or by creating custom images. Customizing the boot disk is useful for the following scenarios:

  * **Pre-loading software and libraries** : Install specific ML frameworks, dependencies, or custom software to reduce VM startup time and ensure consistent environments.
  * **Using non-standard OS distributions** : Use an OS distribution or version not included in the [Google-managed list](https://docs.cloud.google.com/tpu/docs/tpu-os-images#google-managed_os_images).
  * **Applying security and monitoring configurations** : Apply custom security settings, install monitoring agents, or set environment variables.



However, boot disk recovery for TPU VMs is limited. You can't detach or snapshot the boot disk for offline repair, so use caution when making changes that affect the boot process. By following these best practices, you can reduce the risk of boot failures when customizing your TPU VM environments.

Keep the following key principles in mind when customizing your boot disk:

  * **Minimize boot disk modifications** : Whenever possible, install applications and store data on Persistent Disk or Hyperdisk volumes rather than heavily modifying the boot disk.

  * **Use UUIDs for mounting** : When adding entries to the `/etc/fstab` file, always use UUIDs to identify disks and partitions (`UUID=...`) rather than device names like `/dev/sdb1`. Auto-generated device names are not guaranteed to be stable across reboots.




Follow these recommendations to reduce the risk of boot failures when making system changes:

  * **Error handling** : Implement robust error checking and graceful failure modes in your scripts. Log detailed messages to the serial console and Cloud Logging to aid in debugging.

  * **Critical dependencies** : Be extremely careful when modifying files essential for booting, such as the `/etc/fstab` file, network configurations, or bootloader settings. A syntax error or incorrect entry can render the VM unbootable.

  * **Secondary disks** : If your script relies on secondary disks, ensure it handles cases where the disk might not be present or takes longer to attach than expected. Avoid making the boot process critically dependent on secondary disk mounts unless absolutely necessary.

The following are examples of recommended and not recommended `/etc/fstab` entries for mounting a secondary disk:

    * **Recommended** : `UUID=a1b2c3d4-e5f6-7890-1234-567890abcdef /mnt/mydata ext4 defaults,nofail 0 2`
    * **Not recommended** : `/dev/sdb1 /mnt/mydata ext4 defaults 0 2`

Using the `nofail` option can prevent the system from halting if the disk isn't found, but ensure your application can handle the mount point being unavailable.

  * **Package management** : Be cautious when adding third-party repositories. Ensure they are trusted and compatible with the base OS image. Understand the dependencies of any packages you install and their potential impact on system libraries.

  * **Disk space** : Monitor boot disk usage. Extensive logging or large software installations can fill the boot disk, preventing the VM from starting.

  * **Logging** : Configure your applications and scripts to log verbosely to the serial console, as this is the primary tool for diagnosing boot issues on TPU VMs.




## Plan your storage capacity

It's important to plan the amount of storage capacity that your workload will need to fully utilize your accelerators. This includes the storage capacity and checkpoint bandwidth.

### Estimate storage

You can use the following estimates as a starting point for your storage requirements:

Workload type | Dataset storage | Checkpoint storage  
---|---|---  
LLM pre-training | 2 TB per TPU | 200 GB per TPU  
Multimodal training | 12 TB per TPU | 1 TB per TPU  
Inference | 1 TB per TPU | 1 GB per TPU  
  
### Estimate checkpoint bandwidth

You can estimate the minimum checkpointing bandwidth required for training workloads using the following formula. For data reads, multiple training runs, or training and inference, increase your estimated bandwidth requirements proportionally.

  1. **Checkpoint size** : _Number of parameters_ ×  _bytes per parameter_ (approximately 12-16 bytes per parameter for FP16 + optimizer state). Add a buffer (approximately 3×) for optimizer states and different precisions.
  2. **Checkpoint interval** : How often you save a checkpoint (for example, every 15 minutes).
  3. **Required bandwidth** : _Checkpoint size_ ÷  _checkpoint interval_.



The following example shows how to estimate the minimum checkpointing bandwidth for Qwen3-72B:

  1. **Checkpoint size** : 72B parameters × 12 bytes ≈ 864 GB per checkpoint. With buffer, 3 × 864 GB ≈ 2.5 TB.
  2. **Checkpoint interval** : 2 minutes = 120 seconds.
  3. **Required bandwidth** : 2.5 TB ÷ 120 seconds ≈ 20 GBps.



## Reference recipes

For examples of storage configurations for specific hardware and workloads, see the following recipes:

  * **TPU7x inference** : 
    * [Cloud Storage recipe](https://github.com/AI-Hypercomputer/tpu-recipes/blob/main/inference/ironwood/vLLM/GPT-OSS/README-gcs.md)
    * [Managed Lustre recipe](https://github.com/AI-Hypercomputer/tpu-recipes/blob/main/inference/ironwood/vLLM/GPT-OSS/README-lustre.md)
  * **TPU7x training** : 
    * [Cloud Storage recipe](https://github.com/AI-Hypercomputer/tpu-recipes/tree/main/training/ironwood/deepseek3-671b/4k-bf16-tpu7x-4x8x8-gcs)
    * [Managed Lustre recipe](https://github.com/AI-Hypercomputer/tpu-recipes/tree/main/training/ironwood/deepseek3-671b/4k-bf16-tpu7x-4x8x8-lustre)
    * [Provision Managed Lustre on GKE using Cluster Toolkit](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ct-lustre-tpu)



## Quotas and bandwidth limits

The bandwidth for Cloud Storage and Compute Engine offerings is limited by default quotas. If you exceed a quota, your input and output requests might be throttled.

For information about Cloud Storage quotas and how to request increases, see [Quotas & limits](https://docs.cloud.google.com/storage/quotas) in the Cloud Storage documentation. For information about Compute Engine quotas for Hyperdisk and Persistent Disk, see [Disk quotas](https://docs.cloud.google.com/compute/resource-usage#disk_quota).

## What's next

  * [Storage options for TPU data](https://docs.cloud.google.com/tpu/docs/storage-options)
  * [Connect TPU VMs to Cloud Storage buckets](https://docs.cloud.google.com/tpu/docs/storage-buckets-compute)
  * [Attach durable block storage to a TPU VM](https://docs.cloud.google.com/tpu/docs/attach-durable-block-storage-compute)
  * [Cloud Storage FUSE performance tuning best practices](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
