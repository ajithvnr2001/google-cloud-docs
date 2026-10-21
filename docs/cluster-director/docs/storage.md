---
url: https://docs.cloud.google.com/cluster-director/docs/storage/
title: Supported storage services for Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:42:52.656619+00:00
---

# Supported storage services for Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Supported storage services for Cluster Director Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of the Google Cloud storage services that you can use in Cluster Director. By learning the different storage solutions that you can use in your cluster, you can select the best storage options for your workload requirements and budget.

High-performance storage is a critical component for large-scale artificial intelligence (AI) and high performance computing (HPC) workloads. Cluster Director supports two distinct storage categories:

  * **Shared network storage** : cluster-wide file systems and object stores that all nodes share to load training datasets, process data, save model checkpoints, and host user home directories (`/home`).

  * **Node boot disk storage** : compute instance-level block storage that powers the Linux operating system (OS), GPU drivers, and Slurm daemons on individual compute and login nodes.




## Shared network storage

Shared storage services connect across the cluster network to provide a unified file system or object store for all cluster nodes.

### Shared file system requirement for Slurm

When you deploy a cluster with Slurm as the orchestrator, you must provide a shared file system for the `/home` directory on all compute and login nodes. To meet this requirement, you can configure Cluster Director to create a new Filestore or Google Cloud Managed Lustre instance, or you can use an existing instance.

**Note:** You can use both new and existing storage resources in the same cluster. If you use an existing Filestore or Managed Lustre instance, then the instance must be on the same VPC network as your cluster. Each storage resource that you define must specify either a new resource configuration or an existing resource configuration, not both. 

### Supported shared storage services

In addition to a mandatory `/home` file system, you can attach other shared storage solutions to your cluster. Cluster Director supports the following shared network storage services:

Storage service | Features | Recommended for  
---|---|---  
[Filestore](https://docs.cloud.google.com/filestore/docs/overview) | **Overview** : Filestore is a managed, high-performance NFS file storage service. This service provides a file system interface and serves as the default option for home directories for clusters in Cluster Director. | 

  * Home directories
  * General-purpose file storage
  * Workloads that require an NFS interface

  
[Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/overview) | **Overview** : Managed Lustre is a high-performance, managed parallel file system that is optimized for AI and HPC applications. With ultra-low latency and full POSIX support, this service provides an ideal solution to migrate on-premises AI workloads to Google Cloud.   
  
**Dynamic tier support** : you can create new or use existing Managed Lustre instances that use the [Dynamic tier](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers#dynamic_tier) when you create or modify a cluster. If you use this tier, then your cluster must use an existing VPC network that has the `dynamic_tier_capacity` quota allocated.  | 

  * Home directories
  * Migration of AI or machine learning (ML) workloads to Google Cloud
  * Model simulations
  * Workloads with frequent small reads and writes
  * High-throughput burst workloads

  
[Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) | **Overview** : Cloud Storage is a scalable, durable, and cost-effective object store. When you create a cluster, you can select from the following storage classes.

  * **[Rapid storage class](https://docs.cloud.google.com/storage/docs/storage-classes#rapid)** : provides low latency and high throughput for AI and ML workloads.
  * **[Standard storage class](https://docs.cloud.google.com/storage/docs/storage-classes#standard)** : balances cost and performance for general-purpose use cases.
  * **[Autoclass](https://docs.cloud.google.com/storage/docs/autoclass)** : automatically adjusts object storage classes based on workload access patterns to reduce costs.

Through integration with Cloud Storage FUSE, you can mount Cloud Storage buckets as local file systems for model checkpoints and training data. | 

  * High-performance data access with the Rapid storage class
  * Cost-effective data storage with Standard and other storage classes
  * Data processing and preparation
  * Model training data and checkpoints

  
  
## Node boot disk storage

Each controller, login, and compute node in a cluster requires a boot disk for the operating system (OS), GPU drivers, and system daemons. Boot disks attach to individual nodes and don't share files across the cluster.

Cluster Director supports the following boot disk options:

Boot disk option | Features | Recommended for  
---|---|---  
[Standalone boot disks](https://docs.cloud.google.com/compute/docs/disks) | **Overview** : Cluster Director provisions a dedicated Persistent Disk or Hyperdisk volume for each node. This configuration is the default choice when you create a cluster. | 

  * Standard cluster deployments
  * Static clusters with fixed node counts
  * Workloads with predictable, constant node usage

  
[Hyperdisk storage pools](https://docs.cloud.google.com/compute/docs/disks/pools)1 | **Overview** : Hyperdisk storage pools let you share capacity and performance across boot disks in a specific zone to optimize costs. In Cluster Director, you can use existing Hyperdisk pools or Hyperdisk Exapools for boot disks only. Because boot disks require Hyperdisk Balanced volumes, you can't use storage pools that use Hyperdisk Throughput volumes. | 

  * Boot disks for compute and login nodes
  * Clusters that scale compute nodes on demand
  * Workloads with shared capacity and IOPS requirements

  
  
1 Only machine series that support Hyperdisk Balanced volumes can use storage pools in Cluster Director. If you use storage pools with an unsupported machine series, then the cluster creation or modification operation fails. For more information, see [ Machine series support for Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support). 

## What's next

  * [Slurm orchestration in Cluster Director](https://docs.cloud.google.com/cluster-director/docs/orchestration)

  * [Try out Cluster Director](https://docs.cloud.google.com/cluster-director/docs/create/quickstart)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
