---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/storage/
title: About storage services for AI and ML workloads \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:31:20.549022+00:00
---

# About storage services for AI and ML workloads  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  About storage services for AI and ML workloads Stay organized with collections  Save and categorize content based on your preferences. 

Storage services provide the essential data architecture that helps enable high-performance model training, inference, and fine tuning in AI Hypercomputer.

These recommendations are specifically for [ Clustered GPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus).

This document is intended to help architects, storage engineers, and developers evaluate and select the right storage service for their workloads on AI Hypercomputer.

## Introduction to storage services

Google Cloud offers multiple storage solutions that are optimized for AI and ML use cases:

  * Cloud Storage is an object storage system that's designed for processing and storing massive datasets, like those required for training or bulk inference. Cloud Storage offers several capabilities to help you optimize your data storage for AI and ML tasks.

  * Google Cloud Managed Lustre is a fully managed and POSIX-compliant parallel file system that's designed for the specialized, low-latency, and high-concurrency metadata performance required for training and inference workloads.

  * Hyperdisk pools and Hyperdisk Exapools provide an aggregated block of storage capacity, throughput, and input/output operations per second (IOPS) that you can share across compute instances. You can request Hyperdisk Balanced volumes or Hyperdisk Throughput volumes in a reservation.




The following sections provide more information about each storage service.

### Cloud Storage

[Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) is a foundational object store that's designed to offer global scalability, durability, and cost efficiency. When you use Cloud Storage, you store data as objects in containers called [buckets](https://docs.cloud.google.com/storage/docs/buckets). Cloud Storage offers multiple capabilities for your buckets that help optimize AI and ML workload performance:

  * Products in the [Cloud Storage Rapid family](https://docs.cloud.google.com/storage/docs/rapid/high-performance-storage) are designed to clear data bottlenecks for your AI and ML workloads by bringing your data closer in proximity to your compute resources. These products let you colocate your data in the same zones as your compute workloads and enable high performance and cost-efficient data storage scaling for your GPU or TPU clusters. Cloud Storage Rapid products include the following:

    * [Rapid Bucket](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket) provides the fastest read and write performance in Cloud Storage for zonal buckets. Objects in zonal buckets are stored in the [Rapid storage class](https://docs.cloud.google.com/storage/docs/storage-classes#rapid), a high-performance storage class that's optimized for I/O-intensive workloads. In addition to lower latency, Rapid Bucket delivers significantly higher throughput (up to 15 TB/s) compared to other products and bucket locations in Cloud Storage.

    * [Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache) accelerates data reads to existing buckets without requiring code changes. Rapid Cache is an SSD-backed zonal read cache for Cloud Storage buckets that's used to serve data for data read requests. The product offers higher throughput (up to 2.5 TB/s) and lower latency than buckets without a cache.

Rapid Cache is often set up for multi-region buckets, where accelerator capacity is fragmented across Google Cloud regions. Data read from the cache incurs reduced data transfer fees than data read directly from a multi-region bucket.

  * [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview) is an open source [FUSE](https://en.wikipedia.org/wiki/Filesystem_in_Userspace) adapter that lets you mount buckets as local file systems, enabling applications to interact with object storage by using standard file system semantics. This capability lets you leverage the global scalability, durability, and cost efficiency of Cloud Storage with local file access. Cloud Storage FUSE is actively maintained and supported by Google.

Cloud Storage FUSE offers multiple client-side caching and tuning parameters, such as parallel downloads. These capabilities can abstract development complexities and help achieve peak performance by sharding or parallelizing streams.

  * [Hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) enables a true file system structure in buckets and provides efficient data management capabilities, including atomic folder renames and faster file lookups when the bucket is mounted with Cloud Storage FUSE. Hierarchical namespace offers 8 times higher queries per second (QPS) for object reads and writes than buckets without hierarchical namespace. For more information about the benefits of using hierarchical namespace, see [performance and management benefits](https://docs.cloud.google.com/storage/docs/hns-overview#features).

Enabling hierarchical namespace is highly recommended when you have workloads that require high-throughput data loading and frequent model checkpointing. Having hierarchical namespace enabled is required when creating zonal buckets with Rapid Bucket.




### Managed Lustre

[Google Cloud Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/overview) is a high performance, POSIX-compliant, fully managed parallel file system that's optimized for AI and ML applications. The Managed Lustre architecture is ideally suited for high-throughput, low-latency, and high-metadata-concurrency AI/ML workloads, such as checkpointing, high-speed weight propagation in reinforcement learning, and Key-Value (KV) caching.

For more information about common use cases for Managed Lustre, see [Business cases](https://cloud.google.com/products/managed-lustre#business-case).

### Hyperdisk pools

[Hyperdisk pools](https://docs.cloud.google.com/compute/docs/disks/pools) let you manage and share storage capacity, throughput, and IOPS in a dedicated pool across compute instances. This approach helps ensure that you have the storage resources that you need to run your workloads.

When you reserve capacity for clustered GPUs, you can request a Hyperdisk pool as well. This action delivers compute and storage resources together all at once.

## Comparison of storage services

The following table provides a high-level comparison of Cloud Storage, Managed Lustre, and Hyperdisk pools across key characteristics:

Characteristics | Cloud Storage | Managed Lustre | Hyperdisk pools  
---|---|---|---  
Architecture | Object store

  * Data is stored in flat [buckets](https://docs.cloud.google.com/storage/docs/buckets) by default. All bucket types (zonal, region, dual-region, and multi-region) offer geo-redundancy options that can be accelerated with Cloud Storage Rapid capabilities.
  * You can optionally enable [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) to create buckets that support storing data in a file system structure.
  * You can optionally enable [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview) to mount buckets as local file systems.

| Parallel file system

  * Data is stored as files in [Managed Lustre instances](https://docs.cloud.google.com/managed-lustre/docs/create-instance) and mounted as local file systems across your accelerator clusters without any additional tuning needs.

| Hyperdisk pools

  * If you use Hyperdisk Balanced volumes, then storage pools and Exapools support both boot and non-boot disks. If you use Hyperdisk Throughput volumes, then storage pools and Exapools support non-boot disks only.

  
Storage capacity | Scales up to EBs of capacity. | Scales up to 80 PB of capacity, depending on the instance's [performance tier](https://docs.cloud.google.com/managed-lustre/docs/create-instance#performance-tiers). | Scales from 10 TiB up to 5 PiB per pool (up to 5 EiB with Exapools).  
Performance | Supports the following:

  * Sub-millisecond latency for open files with Rapid Bucket
  * Tens of millions of IOPS/TiB with Rapid Bucket
  * Up to 2.5 TiB/s of bandwidth with Rapid Cache
  * Up to 15 TiB/s of bandwidth with Rapid Bucket
  * [Bandwidth increase requests](https://docs.cloud.google.com/storage/docs/bandwidth-usage#increase)

| Supports the following:

  * Sub-millisecond latency
  * Tens of millions of IOPs/TiB
  * Up to 10 TiB/s of bandwidth

| Supports the following:

  * Sub-millisecond latency
  * Up to 4,194,304 provisioned IOPS for Hyperdisk Balanced storage pools
  * Up to 1 TiB/s provisioned throughput for storage pools
  * For Exapools, performance scales with capacity units (read-optimized, write-optimized, or capacity-optimized) into millions of IOPS and multiple TiB/s of throughput
  * Standard or advanced provisioning for capacity and performance

  
Pricing |  For details, see [Cloud Storage pricing](https://cloud.google.com/storage/pricing).  |  For details, see [Managed Lustre pricing](https://cloud.google.com/products/managed-lustre/pricing). |  For details, see [Persistent Disk and Hyperdisk pricing](https://docs.cloud.google.com/compute/disks-image-pricing#storage_pools).  
Recommendations by requirements | Recommended for applications that need a scalable object store and general cost efficiency for training datasets, asynchronous multi-tier checkpointing, and model weight storage. In particular, Cloud Storage Rapid is recommended for high-performance and cost-efficient data scaling. | Recommended for applications that need a fully POSIX-compliant parallel file system or home directories. Also recommended for latency-sensitive or high-metadata-concurrency workloads, such as KV caching offloads, synchronous checkpointing, and high-speed weight propagation for reinforcement learning. | Recommended for node boot disks, local high-performance file systems, and dedicated scratch disks that require consistent performance and high-level of capacity assurance.  
  
## Storage service recommendations by use case

Use case | Storage service recommendation | Reason for recommendation  
---|---|---  
Training and preparing datasets | **Object storage recommendation** : Cloud Storage Rapid Bucket | Cloud Storage buckets provide the capacity, throughput scale, cost efficiency, and durability that are often needed for massive volumes of training and inference datasets. When you use Rapid Bucket to create a zonal bucket, the zonal bucket benefits from very high throughput (up to 15 TB/s) and sub-millisecond latency for open files at optimal cost.  
**File storage recommendation** : Managed Lustre | Managed Lustre provides sub-millisecond latency. It's helpful as a dedicated, ultra-fast workspace for your most intensive training and dataset preparation tasks where low latency and metadata concurrency performance are a high priority.  
Moving or saving model weights for checkpointing or weight transfers | **Object storage recommendation** : Cloud Storage Rapid Bucket | Rapid Bucket is well suited for asynchronous multi-tiered or distributed checkpointing when it's used with [GCSFS](https://github.com/fsspec/gcsfs) through `fsspec` or [Cloud Storage FUSE with client-side performance tuning](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance).   
**File storage recommendation** : Managed Lustre | Managed Lustre provides sub-millisecond latency and parallel data access, enabling thousands of rollout workers to pull the same weight file simultaneously.  
Storing and downloading models for inference | **Object storage recommendation** : Cloud Storage Rapid Cache or Rapid Bucket | Rapid Cache acts as a booster that helps reduce the inference cold start. With Rapid Cache, the model weights can be pre-warmed in the same zone as your inference nodes, allowing a new inference instance to quickly download the model weights and process its first request. Rapid Bucket serves as a high-performance, accelerated zonal storage engine, letting you locate model weights in the same zone as your inference fleet. For model serving, we recommend using the [Run:ai Model Streamer for vLLM](https://docs.vllm.ai/en/stable/models/extensions/runai_model_streamer/) for peak download performance. For other inference stacks, optimizing [Cloud Storage FUSE parallel download parameters](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/file-caching#parallel-downloads) can significantly reduce cold-start latency during model weight downloads.  
**File storage recommendation** : Managed Lustre | Managed Lustre provides sub-millisecond latency and parallel data access, benefitting performance-sensitive models and the scaling of concurrent GPUs downloading the same model simultaneously.  
KV cache offloading | **File storage recommendation** : Managed Lustre | Managed Lustre provides sub-millisecond latency and parallel data access, allowing different nodes to "pull" the KV cache and resume chats without re-processing the whole history of the chat.  
Node boot disks and local high-performance storage | **Primary recommendation** : Hyperdisk pools | Hyperdisk pools aggregate storage capacity, IOPS, and throughput across compute instances, providing predictable performance for boot and non-boot disks.  
  
## What's next

  * Learn more about [Cloud Storage Rapid](https://docs.cloud.google.com/storage/docs/rapid/high-performance-storage), a family of products in Cloud Storage that are designed for AI, ML, and data-intensive analytics.

  * Learn how to optimize performance when using [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance) or the [Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf) to download datasets.

  * Learn how to [accelerate model loading on Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/run-ai-model-streamer).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
