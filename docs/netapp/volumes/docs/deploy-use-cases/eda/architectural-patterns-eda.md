---
url: https://docs.cloud.google.com/netapp/volumes/docs/deploy-use-cases/eda/architectural-patterns-eda/
title: Architectural patterns for electronic design automation workloads on NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:08.333890+00:00
---

# Architectural patterns for electronic design automation workloads on NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/deploy-use-cases/eda/architectural-patterns-eda/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Architectural patterns for electronic design automation workloads on NetApp Volumes Stay organized with collections  Save and categorize content based on your preferences. 

This page describes architectural patterns for electronic design automation (EDA) workloads on Google Cloud NetApp Volumes.

NetApp Volumes provides highly scalable NFS shared storage to support EDA workloads. These workloads process petabyte-scale datasets comprising millions of small files, execute metadata-heavy directory operations, and drive bursty parallel I/O across thousands of compute cores. NetApp Volumes keeps design libraries, toolchains, and scratch data accessible by scaling from project-sized volumes to [large capacity volumes](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/overview#large-capacity-volumes), with optional [FlexCache](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/overview) for hybrid and fan-out designs. The following patterns map common EDA deployment models to these capabilities.

For GitHub reference implementations, such as `eda-all-on-cloud` and `eda-hybrid-cloud`, see [Cluster Toolkit EDA examples](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/community/examples/eda).

## Architectural patterns

The following table summarizes common patterns for EDA workloads. The best pattern for your use case depends on where your primary data resides and how you want to scale read performance and compute.

Pattern | Use case | Primary NetApp Volumes capabilities  
---|---|---  
Large capacity volumes for compute clusters | Design data and toolchains reside in Google Cloud and require a single shared namespace at scale | Large capacity pools and volumes, multi-volume layout, and deployment-group lifecycle  
Burst to the cloud | Primary datasets reside on-premises or in another region, and you require cloud compute for peak demand | FlexCache from on-premises ONTAP origin, prepopulation, and pre-existing volumes  
Performance scaling through fan-out caches | Read-heavy phases require more aggregate throughput or locality than a single export can provide | Multiple FlexCache volumes or multiple storage endpoints per large volume  
  
### Use large capacity volumes as file storage for compute clusters

Use this pattern when compute and persistent data both run in Google Cloud, for example, greenfield EDA farms, migrated design centers, or dedicated cloud burst partitions that own their datasets.

#### Challenges resolved by large capacity volumes

Large capacity volumes address the high capacity, performance, and concurrency requirements of large-scale EDA workloads. This configuration resolves the following challenges:

  * **Capacity constraints** : Accommodates large working sets, such as libraries, IP blocks, and regression scratch data.

  * **High metadata and I/O load** : Handles intensive metadata paths (including `readdir` and `stat` operations), small random I/O, and high sequential bandwidth.




#### Recommended layout

Instead of placing all of your data into a single, large volume, partition your data across multiple volumes based on its lifecycle and access patterns.

The following table describes the recommended layout for partitioning your data:

Volume role | Common data types | Access patterns and lifecycle  
---|---|---  
Tools | Vendor binaries and licensed EDA installations | Read-mostly, long retention, and stable exports  
Libraries | PDKs, standard cells, and reference designs | Read-mostly, large file count, and benefits from attribute-cache tuning on clients  
Home | User dotfiles and small project state | Mixed read/write and moderate metadata rates  
Scratch | Run directories and intermediate results | High churn, largest capacity, and highest IOPS demand  
  
The Cluster Toolkit blueprint [eda-all-on-cloud](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/community/examples/eda/eda-all-on-cloud.yaml) provisions this layout with Slurm-managed Compute Engine partitions mounting the NetApp Volumes over NFS.

#### When to use large capacity volumes

For volumes larger than 4.8 TiB (Flex Unified) or 15 TiB (Premium and Extreme), create [large capacity volumes](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/overview#large-capacity-volumes). These volumes scale to very large capacity and provide higher throughput and IOPS ceilings. Scratch and library volumes that exceed single-endpoint limits are suitable for this configuration.

#### Client distribution on large volumes

A large capacity volume exposes [multiple storage endpoints](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-large-capacity-volumes) (IP addresses) to the same export. Distribute NFS clients across multiple endpoints to scale aggregate throughput and prevent a single IP address from becoming a bottleneck. You can use one of the following options:

  * **Round-robin DNS (recommended at scale)** : Create a Cloud DNS A record listing multiple IP addresses. Mount by using the FQDN so each client resolves to one address at mount time. Remount if you change DNS records.

  * **Static sharding** : Divide clients into multiple groups and mount each group to a chosen endpoint for deterministic load placement.


**Caution:** Some automation paths mount only the first storage endpoint. The Cluster Toolkit Slurm integration uses the first IP address of a large capacity volume when you attach it using the `netapp-volume` module and the `use` directive. For full multiple-endpoint fan-out with Slurm, mount by using DNS or [pre-existing-network-storage](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/file-system/pre-existing-network-storage) with a DNS name, as described in the [hybrid blueprint README](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/community/examples/eda/README.md). If you use `pre-existing-network-storage` with a DNS name for multiple IP addresses, make sure that the mount units resolve DNS during boot and remount after DNS changes.

In an all-on-cloud architecture, you provision separate NetApp Volumes exports in one Google Cloud region for tools, libraries, and scratch. Tools and libraries hold read-mostly reference data; scratch holds run directories and checkpoints and is often a large capacity volume. Slurm-managed Compute Engine nodes in the same VPC mount each export using NFS. Storage is deployed in a `base` deployment group and compute in a `cluster` group to let you scale or delete the cluster without deleting the volumes.

### Burst to the cloud

Use this pattern when authoritative design data remains on-premises or in a remote ONTAP system and you want to run regression, characterization, or peak-capacity jobs on Google Cloud compute without copying entire libraries first.

#### Resolve hybrid cloud storage challenges with FlexCache

[FlexCache volumes](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/overview) resolve common hybrid cloud storage challenges for EDA environments by providing the following benefits:

  * **LAN-like access performance** : WAN latency and bandwidth limit how fast cloud compute cores can read on-premises datasets. FlexCache serves read-heavy phases and metadata operations locally after working sets are cached to counter this issue.

  * **On-demand block-level caching** : Copying full libraries into the cloud before every job introduces startup delays and duplicates storage. FlexCache caches only the accessed data blocks, which minimizes startup times and reduces overall cloud storage usage.

  * **Cohesive origin source** : Instead of managing disconnected copies of your data, you can use a local NFS export in the cloud and still maintain a single, coherent copy at the on-premises origin volume.




#### FlexCache behavior and characteristics

You [create a FlexCache volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/create-flexcache-volume) in NetApp Volumes that points to an existing ONTAP origin volume. Reads of cached data are served by Google Cloud. Cold reads retrieve blocks from the ONTAP origin volume once and then serve them locally. By default, write operations use a [write-around](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/overview#write-around): the cache forwards write operations to the origin and invalidates the affected cached data, which preserves coherence across caches.

The following are the key FlexCache characteristics for EDA environments:

  * **Block-level, pull-only caching** : Only accessed data consumes cache capacity. Sparse volumes are efficient for large libraries that are accessed partially per run.

  * **Coherent, current reads** : Data read from the cache or origin is consistent. This approach is suitable for shared reference libraries when write patterns match FlexCache guidance.

  * **LAN-like read latency after warm-up** : Metadata-heavy and throughput-heavy read phases, such as library traversal and repeated reference files, benefit once working sets are cached.

  * **Prepopulation** : To avoid a cold-read penalty on first access, [prepopulate](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/prepopulate-flexcache-volume) directories for known run lists before starting a job.




#### Hybrid reference blueprint

[eda-hybrid-cloud](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/community/examples/eda/README.md) mounts pre-existing volumes, such as tools, libraries, home, and scratch, using `pre-existing-network-storage`. Volumes can be standard NetApp Volumes exports, large capacity volumes, or FlexCache volumes. Provisioning storage outside the cluster blueprint avoids accidental deletion when you tear down compute and supports FlexCache origins that you manage in ONTAP.

Consider the following operational guidelines:

  * Size the cache volumes for the working set, not the full origin volume capacity.

  * Disable or limit the access-time updates on the origin volume (`-atime-update` in ONTAP) to avoid unnecessary cache invalidation. For more information, see [FlexCache overview](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/overview).

  * Enable [global file locking](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/overview#global_file_locking) only if your flow requires strict cross-cache deny-read semantics. This approach adds latency and couples availability to the origin link.

  * Plan the network connectivity and bandwidth between the origin and Google Cloud. Write-heavy phases remain bound by the origin or the network link when you use [write-around](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/overview#write-around).




In the hybrid read-burst architecture, authoritative tools and library data reside on an on-premises ONTAP system. NetApp Volumes hosts FlexCache volumes in Google Cloud that reference those origins using a WAN or private link. Slurm nodes in Google Cloud mount the FlexCache exports. Reads are served from the cache when data is warm; cold reads retrieve blocks from the on-premises origin. For scratch and checkpoints that receive heavy write traffic from cloud compute, create a separate cloud-native scratch volume in the same region as the cluster to keep writes local, instead of routing sustained write traffic through a FlexCache with an on-premises origin.

### Performance scaling through fan-out caches

Use this pattern when a single export, even a large capacity volume, doesn't provide enough aggregate read throughput or client fan-out for a phase of the flow.

You can implement fan-out in two ways:

  * Multiple FlexCache volumes for the same origin

  * Multiple storage endpoints on one large volume




#### Fan-out FlexCache volumes

Create multiple FlexCache volumes backed by the same origin volume, and mount different compute pools (or job types) on different caches. Each cache warms independently, scales read I/O across separate NetApp Volumes endpoints, and isolates thrash between workloads, for example, library preprocessing versus long regression.

The following table compares single and multiple FlexCache deployment approaches.

Approach | Scales | Trade-off  
---|---|---  
Single FlexCache | Simplicity, one mount path | One cache capacity and throughput ceiling  
Multiple FlexCaches (fan-out) | Aggregate cached read throughput; isolation per pool | More volumes to manage; working set split across caches  
Origin only (no cache) | Strongest write coherency to single site | WAN latency for cloud compute  
  
If you know your job inputs in advance, use prepopulation on each fan-out cache.

#### Fan-out on large capacity volumes with multiple endpoints

Large capacity volumes and FlexCache volumes at scale expose multiple IP addresses per volume. Treat each IP as a [storage endpoint](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-large-capacity-volumes) with its own connection slot budget.

If you have hundreds or thousands of NFS clients, consider the following:

  * **Lower per-client RPC slot table entries** : For example, 8 slots per client on NFSv3, so that total outstanding operations per endpoint stay within recommended limits (approximately 10,000 slots per endpoint across the farm). For more information, see [Linux NFS concurrency](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-concurrency).

  * **Spread mounts across endpoints** : Use Cloud DNS round-robin or static sharding.




To implement FlexCache fan-out, use one origin volume (on-premises ONTAP or a cloud ONTAP-mode volume) to back multiple FlexCache volumes in NetApp Volumes. Mount each cache using different consumers, such as a Slurm partition or job class, to isolate working sets and read loads across exports.

To implement multiple-endpoint fan-out, use one large capacity volume that exposes the same NFS export on multiple IP addresses. Spread clients across those endpoints by assigning fixed client groups to each IP address, or by mounting a DNS name that resolves to one address per mount. Each endpoint has its own connection budget; distributing clients helps avoid concentrating farm-wide I/O on a single IP address.

## Combine patterns

For production EDA environments, you can combine these architectural patterns to optimize performance:

  * **All-on-cloud** : Use large capacity scratch volumes plus smaller standard volumes for tools and home.

  * **Hybrid** : Use FlexCache for libraries and tools, with a cloud-provisioned scratch volume for job output.

  * **Fan-out** : Use FlexCache per site or per scheduler queue, plus multiple-endpoint DNS for a cloud-native large scratch volume.




Match the volume service level and pool type (Flex Unified regular versus large capacity) to the capacity and performance needs of each tier. For more information, see [service levels](https://docs.cloud.google.com/netapp/volumes/docs/discover/service-levels).

## What's next

  * [Optimize Linux NFS client access for electronic design automation workloads](https://docs.cloud.google.com/netapp/volumes/docs/deploy-use-cases/eda/optimize-client-access-for-eda).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
