---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/plan-installation/
title: Plan your AlloyDB Omni installation on a VM \u00a0|\u00a0 AlloyDB Omni for containers: 15.7.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:06:53.221565+00:00
---

# Plan your AlloyDB Omni installation on a VM  |  AlloyDB Omni for containers: 15.7.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/plan-installation/

This page documents AlloyDB Omni version **15.7.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/overview)



Send feedback 

#  Plan your AlloyDB Omni installation on a VM Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.7.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/plan-installation)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/plan-installation)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/plan-installation)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/plan-installation)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/plan-installation)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/plan-installation)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/plan-installation)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/plan-installation)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/plan-installation)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/plan-installation)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/plan-installation)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/plan-installation)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/plan-installation)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/plan-installation)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/plan-installation)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/plan-installation)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/plan-installation)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/plan-installation)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/plan-installation)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/plan-installation)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/plan-installation)

**Note:** Your use of AlloyDB Omni is subject to the agreement between you and Google that governs Google Cloud offerings. If you do not have a Google Cloud account, or have not otherwise entered into an agreement with Google that governs Google Cloud offerings, please do not proceed or download this software until you have done so. To create a Google Cloud account, see [ the Google Cloud homepage](https://docs.cloud.google.com/docs/get-started). 

This document describes how to prepare for running AlloyDB Omni in any Linux environment that supports container runtimes.

For an overview of AlloyDB Omni, see [AlloyDB Omni overview](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/overview).

## Size and capacity

Size and capacity directly affects the performance, reliability, and cost-effectiveness of your AlloyDB Omni instance. When you migrate an existing database, the CPU and memory resources required are similar to the requirements of the source database system.

Plan to start with a deployment using matching CPU, RAM and disk resources, and use the source system configuration as the AlloyDB Omni baseline configuration. You might be able to reduce your resource consumption after you perform sufficient testing of your AlloyDB Omni instance.

Sizing a AlloyDB Omni environment includes the following steps:

  1. Define your workload.

     * Data volume: Estimate the total amount of data you'll store in AlloyDB Omni. Consider both current data and projected growth over time.

     * Transaction rate: Determine the expected number of transactions per second (TPS), including reads, writes, updates, and deletes.

     * Concurrency: Estimate the number of concurrent users or connections accessing the database.

     * Performance requirements: Define your acceptable response times for different types of queries and operations.

  2. Ensure that your hardware supports sizing requirements.

     * CPU: AlloyDB Omni benefits from systems with multiple CPU cores, and AlloyDB Omni scales linearly, depending on the workload. However, open source PostgreSQL generally doesn't benefit from greater than 16 vCPUs. Take the following into consideration:

       * The number of cores based on workload concurrency and computation needs.
       * Any gains that might be present due to a change in CPU generation or platform.
     * Memory: Allocate sufficient RAM for AlloyDB Omni's shared buffers for caching data and working memory for query processing. The exact requirement depends on the workload. Start with 8 GB of RAM per vCPU.

     * Storage

       * Type: Based on your needs, choose between local NVMe storage for performance or SAN storage for scalability and data sharing.

       * Capacity: Ensure enough storage for your data volume, indexes, Write-Ahead Log (WAL), backups, and future growth.

       * IOPS: Estimate the required input/output operations per second (IOPS) based on your workload's read and write patterns. When running AlloyDB Omni in a public cloud, consider the performance characteristics of your storage type to understand if you need to increase storage capacity to meet a specific IOPS target.




## Prerequisites for running AlloyDB Omni

Before you run AlloyDB Omni, make sure that you meet the following hardware and software requirements.

### Hardware requirements

OS/Platform | Minimum hardware | Recommended hardware | Linux | 

  * CPU: x86-64 or ARM CPU with AVX2 support
  * RAM: 2GB
  * Disk space1: 10GB

| 

  * CPU: x86-64 or ARM CPU with AVX2 support
  * RAM: 8GB per vCPU allocated to AlloyDB Omni
  * Disk space1: 20GB+

  
---|---|---  
macOS | 

  * CPU: Intel CPU with AVX2 support or M-chip
  * RAM: 2GB
  * Disk space1: 10GB

| 

  * CPU: Intel CPU with AVX2 support or M-chip
  * RAM: 8GB per vCPU allocated to AlloyDB Omni
  * Disk space1: 20GB+

  
  
  1. We recommend that you use a dedicated solid-state drive (SSD) storage device for storing your data. If you use a physical device for this purpose, we recommend that you attach it directly to the host machine. 

**Tip:** To install AlloyDB Omni on a cloud platform, we recommend that you use instances that maintain the ratio of 8GB of RAM per vCPU.**Note:** AlloyDB Omni is compiled to run directly on Linux systems. Running AlloyDB Omni in a Docker container on macOS utilizes Docker's compatibility layer, which results in reduced performance compared to running directly on Linux.

### Software requirements

OS/Platform | Minimum software | Recommended software | Linux1 | 

  * One of the following OS: 
    * Ubuntu 22.04+
    * Debian 11
    * RHEL 8.10
  * Linux kernel version 4.18+
  * Cgroups v1 or v2 enabled
  * Docker Engine 20.10+ or Podman 4.2.0+

| 

  * One of the following OS: 
    * Ubuntu 22.04+
    * Debian 11 or 12
    * RHEL 9
  * Linux kernel version 6.1+, or any Linux kernel version older than 5.3 that has support for the `MADV_COLLAPSE` and `MADV_POPULATE_WRITE` directives 
  * Cgroupsv2 enabled
  * Docker Engine 25.0.0+ or Podman 5.0.0+

  
---|---|---  
macOS | 

  * Docker Desktop 4.20+

| 

  * Docker Desktop 4.30+

  
  
  1. AlloyDB Omni assumes that SELinux, when present, is configured on the host to permit the container to run, including access to the file system (or SELinux is set to permissive). 



## Supported storage types

AlloyDB Omni supports file systems on block storage volumes in database instances. For smaller development or trial systems, use the local file system of the host where the container is running. For enterprise workloads, use storage that is reserved for AlloyDB Omni instances. Depending on the demands set by your database workload, configure your storage devices either in a singleton configuration with one disk device for each container, or in a consolidated configuration where multiple containers read and write from the same disk device.

### Local NVMe or SAN storage

Both local Non-Volatile Memory Express (NVMe) storage and Storage Area Network (SAN) storage offer distinct advantages. Choosing the right solution depends on your specific workload requirements, budget, and future scalability needs.

To determine the best storage option, consider the following:

  * To prioritize absolute performance, choose local NVMe.
  * If you need large-scale, shared storage, choose SAN.
  * If you need to balance performance and sharing, consider SAN with NVMe over Fabrics for faster access.



### Local NVMe storage

NVMe is a high-performance protocol designed for solid-state drives (SSDs). For applications that need fast data access, local NVMe storage offers the following benefits:

  * NVMe SSDs connect directly to the Peripheral Component Interconnect express (PCIe) bus to deliver fast read and write speeds.
  * Local NVMe storage provides the lowest latency.
  * Local NVMe storage provides the highest throughput.



Scaling local NVMe storage requires adding more drives to individual servers. However, adding more drives to individual servers leads to fragmented storage pools and potential management complexities. Local NVMe storage isn't designed for data sharing between multiple servers. Since local NVMe storage is local, server administrators must protect against disk failures using hardware or software [Redundant Array of Inexpensive Disks (RAID)](https://en.wikipedia.org/wiki/Standard_RAID_levels). Otherwise, the failure of a single NVMe device will result in data loss.

### SAN storage

SAN is a dedicated storage network that connects multiple servers to a shared pool of storage devices, often SSDs or centralized NVMe storage. While SAN isn't as fast as local NVMe, modern SANs, especially those using NVMe over Fabrics, still deliver excellent performance for most enterprise workloads.

  * SANs are highly scalable. To add more storage capacity or performance, add new storage arrays or upgrading existing ones. SANs provide redundancy at the storage layer, providing protection against storage media failures.

  * SANs excel at data sharing. For enterprise environments that require high availability, multiple servers can access and share data stored on the SAN. In the event of a server failure, you can present SAN storage to another server in the data center, allowing for faster recovery.




## What's next

  * [Install AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/quickstart)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
