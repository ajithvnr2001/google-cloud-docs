---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/storage-overview/
title: Storage for GKE clusters overview \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:24.307940+00:00
---

# Storage for GKE clusters overview  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/storage-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Storage for GKE clusters overview Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document covers the storage options that GKE supports and some key considerations for selecting the best option for your business needs. To determine which machine family is appropriate for your selection, see [Machine series comparison](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison).

GKE supports the following storage types and integrations:

  * Block storage using Persistent Disk
  * Block storage using Google Cloud Hyperdisk
  * Block storage using Hyperdisk Storage Pools
  * Ephemeral and raw block storage using Local SSD
  * Parallel file system (Google Cloud Managed Lustre)
  * Network file system (Filestore)
  * AI/ML object storage access using Run:ai Model Streamer
  * Object storage using Cloud Storage FUSE
  * Managed databases
  * Build artifacts



## Block storage (Persistent Disk)

Persistent Disk volumes are durable network storage devices managed by Compute Engine that your GKE clusters can access like physical disks in a desktop or a server. When your clusters require additional storage space, you can attach more Persistent Disk volumes to your nodes or resize your existing Persistent Disk volumes. You can let GKE [dynamically provision PersistentVolumes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes) backed by Persistent Disk, or you can manually provision disks.

This storage option is supported on GKE Autopilot and Standard clusters.

By default, Persistent Disk volumes are zonal resources (kept in a single zone within a region). You can create regional Persistent Disk volumes (kept across two zones in the same region). You can also attach a Persistent Disk volume as read-only to multiple nodes simultaneously. This is supported for both zonal and regional Persistent Disk volumes.

Persistent Disk storage on GKE is persistent, meaning that the data stored on your disks will persist even if the Pod that is using it is terminated.

### Why use Persistent Disk storage

Use Persistent Disk storage if your clusters require access to high-performance, highly available durable block storage. A Persistent Disk volume is typically attached to a single Pod. This storage option supports the [ReadWriteOnce access mode](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes). GKE provides support for configuring Persistent Disk volumes with a range of latency and performance options, including the following:

  * **Balanced Persistent Disk** : Suitable for standard enterprise applications. This option provides a balance of performance and cost. Backed by solid-state drives (SSD). This is the default option for dynamic volume provisioning on clusters and nodes running GKE 1.24 or later.
  * **Performance Persistent Disk** : Suitable for scale-out analytics, databases, and persistent caching. This option is ideal for performance-sensitive workloads. Backed by solid-state drives (SSD).
  * **Standard Persistent Disk** : Suitable for big data, big compute workloads. This option is the most cost-effective disk type. Backed by standard hard disk drives (HDD).
  * **Extreme Persistent Disk** : Suitable for enterprise applications such as SAP HANA and Oracle. This option offers the highest performance to meet the needs of the largest in-memory databases. Backed by solid-state drives (SSD). For performance-critical applications, where Persistent Disk does not provide enough performance, use Hyperdisk Extreme disks.



To start using this storage option, see these resources:

  * To learn about the available disk types, see [Storage options](https://docs.cloud.google.com/compute/docs/disks#disk-types) in the Compute Engine documentation.
  * The Compute Engine Persistent Disk CSI driver is the primary way you use Persistent Disk storage with GKE. For instructions, see [Using the Compute Engine Persistent Disk CSI Driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver#using_the_for_linux_clusters).



## Block storage (Google Cloud Hyperdisk)

Hyperdisk volumes use the next generation of Google Cloud block storage. Hyperdisk volumes let you dynamically tune the performance of your block storage to your workload. You can configure input/output operations per second (IOPS) and throughput independently for your applications and adapt to changing performance needs over time.

This storage option is supported on GKE Autopilot and Standard clusters. Hyperdisk volumes are zonal resources, subject to [regional availability](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#hyperdisk_regions). Hyperdisk storage on GKE is persistent, meaning that the data stored on your disks will persist even if the Pod that is using it is terminated.

### Why use Hyperdisk storage

Use Hyperdisk storage if you need to dynamically resize and adjust IOPS or throughput. A Hyperdisk volume is typically attached to a single Pod. Most Hyperdisk storage options support the [`ReadWriteOnce` access mode](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes). You can select from the following Hyperdisk storage options for GKE based on your price-performance needs:

  * **Hyperdisk Balanced** : The best fit for most workloads. This is a good option for deploying most enterprise and line-of-business apps, as well as databases and web servers.
  * **Hyperdisk Throughput** : Optimized for cost-efficient high-throughput. This is a good option if your use case targets scale-out analytics (for example, Hadoop or Kafka), restoring cold data from backup servers, and throughput-oriented cost-sensitive workloads.
  * **Hyperdisk Extreme** : Optimized for IOPS performance. This is a good option if you're deploying high-performance workloads, such as database management systems.
  * **Hyperdisk ML** : Optimized for AI/ML training and inference workloads that need to load model weights quickly. Unlike other Hyperdisk volumes, this option supports the `ReadOnlyMany` access mode, allowing multiple Pods to read the same model weights concurrently. Use this option to reduce idleness of GPU/TPU resources due to latency bottlenecks.



Hyperdisk storage options are supported on GKE Autopilot and Standard clusters.

To start using this storage option, refer to these resources:

  * For an overview, see [About Hyperdisk for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hyperdisk).
  * For the per disk limits, including the maximum throughput and IOPs, refer to [Hyperdisk limits per disk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#limitations) in the Compute Engine documentation.
  * To set up and consume Hyperdisk Throughput and Extreme storage in your clusters, see [Scale your storage performance with Hyperdisk](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/hyperdisk).



## Block storage (Hyperdisk Storage Pool)

A Hyperdisk Storage Pool is a pre-provisioned pool of storage resources (capacity, throughput, and IOPS) that disks in your GKE cluster can use. The storage resources are shared across all Hyperdisks that you create within the Storage Pool.

Standard clusters allow both Hyperdisk boot disks (for operating systems) and attached Hyperdisks (for data storage) to be part of a Storage Pool. GKE Autopilot clusters support only attached Hyperdisks for Storage Pools.

To start using this storage option, refer to the following resources:

  * For an overview, see [About Hyperdisk Storage Pools](https://docs.cloud.google.com/compute/docs/disks/storage-pools).
  * To set up Hyperdisk Storage Pool in your GKE clusters, see [Optimize storage performance and cost with Hyperdisk Storage Pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/hyperdisk-storage-pools).



## Ephemeral and raw block storage (Local SSD)

Local SSD disks are physical drives that are attached directly to your nodes. They can offer better performance, but are ephemeral. Each Local SSD volume is attached to a specific node. You can't move the volume to a different node.

This storage option is supported on GKE Standard clusters. Autopilot support for Local SSD is available in preview on A2 Ultra A100 machines, on clusters and node pools running GKE 1.27 and later.

Ephemeral storage backed by Local SSD storage on GKE is tied to the lifecycle of a Pod. When your Pod is terminated, the ephemeral storage associated with that Pod is also deleted.

### Why use Local SSD

Using Local SSD storage in GKE clusters is suitable if you need hot caching for databases and for real-time analytics, or flash-optimized ephemeral storage offering the lowest latencies. Local SSD storage can be particularly effective as a caching layer in front of Cloud Storage for AI/ML, batch processing, analytics, and in-memory databases use cases.

To start using this storage option, refer to these resources:

  * For an overview, see [About Local SSD storage for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd).
  * To set up and consume Local SSD storage in your clusters as [emptyDir](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir), see [Provision and use Local SSD-backed ephemeral storage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd).
  * To set up and consume Local SSD storage in your clusters as [local](https://kubernetes.io/docs/concepts/storage/volumes/#local) PersistentVolumes resources, see [Provision and use Local SSD-backed raw block storage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd-raw).



## Parallel file system (Google Cloud Managed Lustre)

Managed Lustre is a fully managed, high-performance parallel file system on Google Cloud, integrated with GKE through the Managed Lustre CSI driver. It is designed for demanding workloads that require persistent, scalable, and high-throughput storage, particularly in AI/ML and high performance computing (HPC). You can also dynamically expand your Lustre volumes to meet growing storage demands without disrupting your applications. The Managed Lustre CSI driver automates the lifecycle management of Managed Lustre instances, letting you provision and access them through standard Kubernetes objects like PersistentVolumes and PersistentVolumeClaims.

This storage option is supported on GKE Autopilot and Standard clusters that run Container-Optimized OS nodes. Managed Lustre storage on GKE is persistent, so data remains even if the Pod using it is terminated.

### Why use Managed Lustre storage

Use Managed Lustre storage for workloads that require high-throughput and low-latency file access from multiple Pods simultaneously. It is a good choice for the following use cases:

  * **AI/ML** : Training and inference workloads that need to access large datasets.
  * **HPC** : Large-scale scientific and engineering simulations.
  * **Dynamic storage needs** : Workloads where storage requirements grow over time, because you can increase the capacity of your Lustre volumes without application downtime.



To start using this storage option, refer to these resources:

  * To get an overview of the feature, see [About the Google Cloud Managed Lustre CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managed-lustre).
  * To create and use a volume backed by a new Managed Lustre instance, see [Access Managed Lustre instances with the Google Cloud Managed Lustre CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/lustre-csi-driver-new-volume).
  * To connect to an existing Managed Lustre instance, see [Access existing Managed Lustre instances with the Google Cloud Managed Lustre CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/lustre-csi-driver-existing-instance).
  * To expand an existing Managed Lustre volume, see [Scale your Managed Lustre storage on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/expand-lustre-volumes).



## Network file system (Filestore)

Filestore provides a cloud-based shared file system for unstructured data, with network file system (NFS) access. Filestore instances function as file servers on Google Cloud that provide durable storage with [`ReadWriteMany`](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes) access for your GKE clusters. Filestore instances are decoupled from the host and require minimal manual operation. Workload failovers are seamless because there are no infrastructure operations to attach or detach volumes.

This storage option is supported on GKE Autopilot and Standard clusters. Filestore storage with the [enterprise service tier](https://docs.cloud.google.com/filestore/docs/service-tiers#enterprise_tier) defaults to regional availability, while the other service tiers have zonal availability. Filestore storage on GKE is persistent, meaning that the data stored in your instances will persist even if the Pod that is using it is terminated.

### Why use Filestore storage

Use Filestore storage if your applications need network file system (NFS) access and multiple readers and writers. This storage option is suitable if your use case involves content management systems, application migration, data analytics, rendering, and media processing.

For additional cost efficiency, [Filestore multishares for GKE](https://docs.cloud.google.com/filestore/docs/multishares) lets you share a Filestore enterprise tier instance of 10 GiB or larger with up to 80 PersistentVolumes.

To start using this storage option, refer to these resources:

  * For an overview, see [About Filestore support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/filestore-for-gke).
  * The Filestore CSI driver is the primary way you use Filestore storage with GKE. For instructions, see [Access Filestore instances with the Filestore CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver).
  * For Filestore multishares instructions, see [Optimize storage with Filestore multishares for GKE](https://docs.cloud.google.com/filestore/docs/optimize-multishares).



## Object storage (Cloud Storage FUSE)

Cloud Storage is an object store for binary and object data, blobs, and unstructured data. The [Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/cloud-storage-fuse-csi-driver) manages the integration of Cloud Storage FUSE with Kubernetes APIs to consume existing Cloud Storage buckets as volumes. You can use the Cloud Storage FUSE CSI driver to mount buckets as file systems on GKE nodes.

The Cloud Storage FUSE CSI driver supports the `ReadWriteMany`, `ReadOnlyMany`, and `ReadWriteOnce` access modes on GKE Autopilot and Standard clusters. Cloud Storage objects have regional availability. Cloud Storage data on GKE is persistent, meaning that the data stored in your buckets will persist even if the Pod that is using it is terminated.

### Why use Cloud Storage FUSE

The Cloud Storage FUSE option is suitable if you need file semantics in front of Cloud Storage for portability. Cloud Storage FUSE is also a common choice for developers who want to store and access [machine learning (ML) training](https://docs.cloud.google.com/storage/docs/gcsfuse-integrations#machine-learning) and model data as objects in Cloud Storage.

To start using this storage option, refer to these resources:

  * For an overview, see [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/gcs-fuse).
  * To consume Google Cloud buckets in your clusters, see [Access Cloud Storage buckets with the Cloud Storage CSI FUSE driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/cloud-storage-fuse-csi-driver).



## AI/ML object storage access using Run:ai Model Streamer

[Run:ai Model Streamer](https://github.com/run-ai/runai-model-streamer/blob/master/docs/README.md) is a Python SDK designed to accelerate the loading of large AI models onto GPUs by streaming model weights directly from object storage, like [Cloud Storage](https://docs.cloud.google.com/storage), to GPU memory. This open-source solution uses a high-performance C++ implementation to read model tensors concurrently, which can significantly reduce cold-start times for inference engines.

The model streamer integrates with inference servers like vLLM and works with models stored in Cloud Storage. Although the streamer accelerates data access, the underlying model data stored in Cloud Storage buckets remains persistent, meaning the data will persist even if the Pod using it is terminated.

### Why use Run:ai Model Streamer

We recommend Run:ai Model Streamer if you need to accelerate model loading times for inference, particularly when accessing `safetensors` files from Cloud Storage with serving frameworks like vLLM or SGLang. By enabling parallel data transfer, the streamer is designed to load models much faster than conventional methods, which boosts overall GPU utilization and efficiency for large-scale AI workloads.

To get started on GKE, see [Accelerate model loading on GKE with Run:ai model streamer and vLLM](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/run-ai-model-streamer).

## Managed databases

A managed database, such as [Cloud SQL](https://docs.cloud.google.com/sql) or [Spanner](https://docs.cloud.google.com/spanner), provides reduced operational overhead and is optimized for Google Cloud infrastructure. Managed databases require less effort to maintain and operate than a database that you deploy directly in Kubernetes.

### Why use managed databases

Using a Google Cloud managed database lets your stateful workloads on GKE to access persistent data while automating maintenance tasks such as backups, patching, and scaling. You create a database, build your app, and let Google Cloud scale it for you. However, this also means you might not have access to the exact version of a database, extension, or the exact flavor of database that you want.

GKE provides support for connecting with Google Cloud managed database services, including the following:

  * **AlloyDB for PostgreSQL** : Fully managed, PostgreSQL-compatible database with superior performance, availability, and scale for transactional and analytical workloads. Refer to [Connect from Google Kubernetes Engine to AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/quickstart/integrate-kubernetes).

  * **Cloud SQL** : Fully managed MySQL, PostgreSQL, and SQL Server database. Refer to [Connect from Google Kubernetes Engine](https://docs.cloud.google.com/sql/docs/postgres/connect-kubernetes-engine).

  * **Spanner** : Horizontally scalable relational database with high consistency and availability. Refer to [Deploy an app using GKE Autopilot and Cloud Spanner](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/gke-spanner-integration).

  * **Memorystore for Redis** : Fully managed in-memory data store service. Refer to [Connecting to a Redis instance from a Google Kubernetes Engine cluster](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-gke).




To start using this storage option, refer to these resources:

  * [Your Google Cloud database options, explained](https://cloud.google.com/blog/topics/developers-practitioners/your-google-cloud-database-options-explained).
  * For considerations on using a managed database or a containerized database hosted on GKE, see [Plan your database deployments on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/database-options).



## Build artifacts (Artifact Registry)

Artifact Registry is a repository manager for container images, OS packages, and language packages that you build and deploy.

### Why use Artifact Registry

Artifact Registry is a suitable option for storing your private container images, Helm charts, and other build artifacts.

To pull images from Artifact Registry Docker repositories to GKE, see [Deploying to Google Kubernetes Engine](https://docs.cloud.google.com/artifact-registry/docs/integrate-gke) in the Artifact Registry documentation.

## What's next

  * Read the blog post [A map of storage options in Google Cloud](https://cloud.google.com/blog/topics/developers-practitioners/map-storage-options-google-cloud).
  * [Design an optimal storage strategy for your cloud workload](https://docs.cloud.google.com/architecture/storage-advisor).
  * Understand how to use Kubernetes storage abstractions in GKE: [PersistentVolumes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes), [StatefulSets](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/statefulset).
  * See the [Data on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/data) resource page to learn about data solutions you can integrate with GKE.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
