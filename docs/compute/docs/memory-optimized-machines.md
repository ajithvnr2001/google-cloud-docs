---
url: https://docs.cloud.google.com/compute/docs/memory-optimized-machines/
title: Memory-optimized machine family for Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T23:38:59.989830+00:00
---

# Memory-optimized machine family for Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/memory-optimized-machines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Memory-optimized machine family for Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

The memory-optimized machine family provides the most compute and memory resources of any Compute Engine machine family offering. They are ideal for workloads that require higher memory-to-vCPU ratios than the high-memory machine types in the general-purpose machine series.

  * The X5 machine series offers bare metal instances with 12 to 48 TB of memory.
  * The X4 machine series offers bare metal instances with 6 to 32 TB of memory.
  * The M4N machine series offers VM instances with up to 6 TB of memory.
  * The M4 machine series offers VM instances with up to 6 TB of memory.
  * The M3 machine series offers VM instances with 1 to 4 TB of memory.
  * The M2 machine series offers VM instances with up to 12 TB of memory.
  * The M1 machine series offers VM instances with up to 4 TB of memory.



These machine series are well-suited for large in-memory databases such as SAP HANA, as well as online analytical processing (OLAP) and in-memory data analytics workloads.

The X5, X4, M4N, M4, M3, M2, and M1 machine series offer the lowest cost per GB of memory on Compute Engine, making them a great choice for workloads that utilize higher memory configurations with low compute resources requirements. Additionally, the following discounts are available:

  * **Sustained use discounts (SUDs):** M2 and M1 offer savings of up to 30% with sustained use discounts.
  * **Committed use discounts (CUDs):** X4, M4N, M4, M3, M2, and M1 are eligible for [resource-based committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts), that can bring savings of greater than 60% in exchange for 3-year commitments.
  * **Compute flexible CUDs:** M4N, M4, M3, M2, and M1 are eligible for [compute flexible committed use discounts](https://docs.cloud.google.com/compute/docs/instances/flexible-committed-use-discounts) that can bring savings of 54% or 63% in exchange for 3-year commitments. M4N also offers 1-year compute flexible CUDs.

**Machine series** | **Workloads**  
---|---  
[X5 machine series](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x5_machine_types) | 

  * Purpose-built for ultra-large SAP HANA scale-up workloads and high performance computing
  * Powered by Intel Granite Rapids (6th generation Intel Xeon Scalable)
  * Supports 688 to 2,064 vCPUs
  * Offers significantly higher memory capacities, ranging from 12 TB to 48 TB
  * Exclusively supports NVMe interfaces and Google Cloud Hyperdisk (Balanced, Extreme, Throughput, and ML). Standard Persistent Disks and local SSD disks are not supported.
  * Uses the Intel IDPF driver, supporting up to 200 Gbps standard bandwidth.
  * Includes access to Intel hardware accelerators: QAT, DLB, DSA, and IAA.

  
[X4 machine series](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x4_machine_types) | 

  * Extra large SAP HANA systems
  * On-demand, enterprise grade, ultra memory-equipped IaaS
  * High performance computing

  
[M4N machine series](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m4n_machine_types) | 

  * High-performance vector databases
  * Retrieval-augmented generation (RAG) data layers
  * Massive in-memory context caching
  * Real-time semantic search

  
[M4 machine series](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m4_machine_types) | 

  * OLAP and OLTP SAP workloads
  * Memory intensive applications, such as genomic modeling and electronic design automation
  * Small to medium in-memory databases such as SAP HANA
  * High performance computing

  
[M3 machine series](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m3_machine_types) | 

  * OLAP and OLTP SAP workloads
  * Memory intensive applications, such as genomic modeling and electronic design automation
  * High performance computing

  
[M2 machine series](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m2_machine_types) | 

  * Large in-memory databases such as SAP HANA
  * In-memory databases and in-memory analytics, business warehousing (BW) workloads, genomics analysis, SQL analysis services

  
[M1 machine series](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m1_machine_types) | 

  * Medium in-memory databases such as SAP HANA
  * Tasks that require intensive use of memory with higher memory-to-vCPU ratios than the general-purpose high-memory machine types.
  * In-memory databases and in-memory analytics, business warehousing (BW) workloads, genomics analysis, SQL analysis services.
  * Microsoft SQL Server and similar databases.

  
  
## X5 machine series

The X5 machine series offers more storage and networking options to support your most demanding workloads. The X5 machine series offers six predefined machine types. These machine types provide you with the capability to provision bare metal instances with up to 2,064 vCPUs and up to 48 TB of RAM.

X5 instances are powered by the 6th generation Intel Xeon Scalable processors (code-named Granite Rapids) and [Titanium](https://cloud.google.com/titanium). X5 instances use only the NVMe disk interface for storage, and only use [Google Cloud Hyperdisk storage](https://docs.cloud.google.com/compute/docs/disks/hyperdisks). X5 instances use a version of the Intel [Infrastructure Data Plane Function (IDPF) driver](https://docs.cloud.google.com/compute/docs/networking/using-idpf) that has been optimized for use with Google Cloud. VirtIO-net, gVNIC, and SCSI interfaces are not supported.

X5 bare metal instances give you access to the raw compute resources of the host server. Bare metal instances also provide access to several on-board, function-specific [accelerators and offloads](https://docs.cloud.google.com/compute/docs/cpu-platforms#accelerator):

  * Intel QuickAssist Technology (QAT): 1 accelerator
  * Intel Dynamic Load Balancer (DLB): 1 accelerator
  * Intel Data Streaming Accelerator (DSA): up to 4 accelerators
  * Intel In-Memory Analytics Accelerator (IAA): up to 4 accelerators



To move your workload from a VM instance to an X5 bare metal instance, see [Move your workload to a new compute instance](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm).

Contact your [Google Cloud account manager](https://cloud.google.com/tam) for pricing and ordering information for X5, or to discuss on-demand pricing for testing X5 instances.

When purchasing [resource-based commitments](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments) for X5 machine types, note that the commitment type is separate for each X5 machine type.

### X5 Limitations

The X5 machine series is only available as predefined machine types. Custom machine shapes are not available. The following additional restrictions apply:

  * You can't attach Persistent Disk volumes to an X5 instance, only Hyperdisk volumes.
  * The X5 machine series is available in only [select zones and regions](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * X5 instances aren't supported with all operating system images. The [operating system details](https://docs.cloud.google.com/compute/docs/images/os-details) page shows which operating system versions can be used with X5 instances.
  * If using a custom image, when you create the image, you must enable the [UEFI-compatible](https://docs.cloud.google.com/compute/docs/images/create-custom#guest-os-features) OS feature.
  * [Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm) isn't supported with bare metal instances.
  * Live migration isn't supported with X5 instances.
  * There's no hypervisor provided with X5 bare metal instances and [nested virtualization](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview) isn't enabled.
  * X5 machine series instances can take up to 30 mins to boot due to large hardware and the Power-On Self-Test (POST).



### X5 machine types

The following table lists the hardware characteristics of each machine type for the X5 machine series:

Machine types | vCPUs1 | Memory (GB) | Local SSD | Default egress  
bandwidth (Gbps)2 | NUMA domains3  
  
---|---|---|---|---|---  
`x5-688-12t-metal` | 688 | 12,288 | Not available | Up to 200 | 8  
`x5-688-16t-metal` | 688 | 16,384 | Not available | Up to 200 | 8  
`x5-1376-24t-metal` | 1,376 | 24,576 | Not available | Up to 200 | 16  
`x5-1376-32t-metal` | 1,376 | 32,768 | Not available | Up to 200 | 16  
`x5-2064-48t-metal` | 2,064 | 49,152 | Not available | Up to 200 | 24  
  
1 A vCPU represents a single hardware thread, or logical core. The number of available hardware threads is equivalent to the number of hardware threads on the host server.  
2 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3 The "NUMA domains" column in the tables shows the number of NUMA nodes exposed to the guest OS.

### Supported disk types for X5

X5 machine types support the following block storage options:

  * Hyperdisk Balanced (`hyperdisk-balanced`)
  * Hyperdisk Balanced High Availability (`hyperdisk-balanced-ha`)
  * Hyperdisk Throughput (`hyperdisk-throughput`)
  * Hyperdisk Extreme (`hyperdisk-extreme`)
  * Hyperdisk ML (`hyperdisk-ml`)



For disks attached to an X5 instance:

  * The number of Google Cloud Hyperdisk volumes can't exceed 8 Hyperdisk Extreme or 32 Hyperdisk Balanced per instance. The total number of Google Cloud Hyperdisk volumes can't exceed 32 per instance.
  * The maximum total disk capacity (in TiB) across all disk types can't exceed 512 TiB.



For details about the capacity limits, see [Google Cloud Hyperdisk capacity limits per VM](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance).

X5 storage limits are described in the following table:

Maximum number of disks  
---  
Machine types | Google Cloud Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme | Hyperdisk ML  
`x5-688-12t-metal` | 32 | 32 | 32 | 32 | 8 | 32  
`x5-688-16t-metal` | 32 | 32 | 32 | 32 | 8 | 32  
`x5-1376-24t-metal` | 32 | 32 | 32 | 32 | 8 | 32  
`x5-1376-32t-metal` | 32 | 32 | 32 | 32 | 8 | 32  
`x5-2064-48t-metal` | 32 | 32 | 32 | 32 | 8 | 32  
  
### Network support for X5 instances

X5 bare metal instances require the [Intel IDPF LAN PF device driver](https://docs.cloud.google.com/compute/docs/networking/using-idpf). X5 supports up to 200 Gbps network bandwidth for standard networking. The gVNIC network interface isn't supported with bare metal.

Before migrating to X5 or creating X5 instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the IDPF network driver. If you create an X5 instance with an operating system that doesn't support the IDPF driver, then you might not be able to connect to the instance.

### Maintenance experience for X5 instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple _host events_. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The X5 machine series offers the following features related to host maintenance:

Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | On-demand maintenance | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance)  
---|---|---|---|---|---  
All machine types | Minimum of 90 days | Restart in place | 60 days | Yes | Yes  
  
The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

X5 also lets you perform maintenance for unplanned emergent maintenance events within a short window of time. Emergent maintenance events are typically needed to address security, hardware, or software issues of medium to high severity that have a high potential for causing outages. These maintenance events are deemed important and time-sensitive, but not critical enough to require an immediate outage to perform the maintenance. Emergent maintenance events have the following features for X5 machine types: 

  * [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event): 14 days
  * [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors): Restart in place



During emergent maintenance maintenance, X5 instances are moved to a different, healthy host.

For emergent maintenance events, you can trigger the maintenance at any time within the 14 day advance notification period. If you don't begin the maintenance operation within the 14-day period, then the maintenance starts automatically at the end of the advanced notification period.

For information about how to manually start host maintenance events for X5 instances, see [Manually starting host maintenance doesn't work for X5 instances](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#x4-ctm).

## X4 machine series

The X4 machine series offers more storage and networking options to support your most demanding workloads. The X4 machine series offers six predefined machine types. These machine types provide you with the capability to provision bare metal instances with up to 1,920 vCPUs and up to 32 TB of RAM.

X4 instances are powered by the 4th generation Intel Xeon Scalable processors (code-named Sapphire Rapids) and [Titanium](https://cloud.google.com/titanium). X4 instances use only the NVMe disk interface for storage, and only use [Google Cloud Hyperdisk storage](https://docs.cloud.google.com/compute/docs/disks/hyperdisks). X4 instances use a version of the Intel [Infrastructure Data Plane Function (IDPF) driver](https://docs.cloud.google.com/compute/docs/networking/using-idpf) that has been optimized for use with Google Cloud. VirtIO-net, gVNIC, and SCSI interfaces are not supported.

X4 instances give you access to the raw compute resources of the server. Bare metal instances also provide access to several on-board, function-specific [accelerators and offloads](https://docs.cloud.google.com/compute/docs/cpu-platforms#accelerator):

  * Intel QuickAssist Technology (QAT): 1 accelerator
  * Intel Dynamic Load Balancer (DLB): 1 accelerator
  * Intel Data Streaming Accelerator (DSA): up to 4 accelerators
  * Intel In-Memory Analytics Accelerator (IAA): up to 4 accelerators



To move your workload from a VM instance to an X4 bare metal instance, see [Move your workload to a new compute instance](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm).

Contact your [Google Cloud account manager](https://cloud.google.com/tam) for pricing and ordering information for X4, or to discuss on-demand pricing for testing X4 instances.

When purchasing [resource-based commitments](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments) for X4 machine types, note that the commitment type is separate for each X4 machine type.

### X4 Limitations

The X4 machine series is only available as predefined machine types. Custom machine shapes are not available. The following additional restrictions apply:

  * You can't attach Persistent Disk volumes to an X4 instance, only Hyperdisk volumes.
  * The X4 machine series is available in only [select zones and regions](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * X4 instances aren't supported with all operating system images. The [operating system details](https://docs.cloud.google.com/compute/docs/images/os-details) page shows which operating system versions can be used with X4 instances.
  * If using a custom image, when you create the image, you must enable the [UEFI-compatible](https://docs.cloud.google.com/compute/docs/images/create-custom#guest-os-features) OS feature.
  * [Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm) isn't supported with bare metal instances.
  * Live migration is not supported with X4 instances.
  * There's no hypervisor provided with X4 bare metal instances and [nested virtualization](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview) isn't enabled.
  * X4 machine series instances can take up to 30 mins to boot due to large hardware and the Power-On Self-Test (POST).



### X4 machine types

The following table lists the hardware characteristics of each machine type for the X4 machine series:

Machine types | vCPUs1 | Memory (GB) | Local SSD | Default egress  
bandwidth (Gbps)2 | Tier_1 egress  
bandwidth (Gbps)  
---|---|---|---|---|---  
`x4-480-6t-metal` | 480 | 6,144 | Not available | Up to 100 | Not available  
`x4-480-8t-metal` | 480 | 8,192 | Not available | Up to 100 | Not available  
`x4-960-12t-metal` | 960 | 12,288 | Not available | Up to 100 | Not available  
`x4-960-16t-metal` | 960 | 16,384 | Not available | Up to 100 | Not available  
`x4-1440-24t-metal` | 1,440 | 24,576 | Not available | Up to 100 | Not available  
`x4-1920-32t-metal` | 1,920 | 32,768 | Not available | Up to 100 | Not available  
  
1 A vCPU represents a single hardware thread, or logical core. The number of available hardware threads is equivalent to the number of hardware threads on the host server.  
2 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  


### Supported disk types for X4

X4 machine types support the following block storage options:

  * Hyperdisk Balanced (`hyperdisk-balanced`)
  * Hyperdisk Extreme (`hyperdisk-extreme`)



For disks attached to an X4 instance:

  * The number of Google Cloud Hyperdisk volumes can't exceed 8 Hyperdisk Extreme or 32 Hyperdisk Balanced per instance. The total number of Google Cloud Hyperdisk volumes can't exceed 32 per instance.
  * The maximum total disk capacity (in TiB) across all disk types can't exceed 512 TiB.



For details about the capacity limits, see [Hyperdisk capacity limits per VM](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance).

X4 storage limits are described in the following table:

Maximum number of disks  
---  
Machine types | Google Cloud Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk Extreme  
`x4-480-6t-metal` | 32 | 32 | Not available | 8  
`x4-480-8t-metal` | 32 | 32 | Not available | 8  
`x4-960-12t-metal` | 32 | 32 | Not available | 8  
`x4-960-16t-metal` | 32 | 32 | Not available | 8  
`x4-1440-24t-metal` | 32 | 32 | Not available | 8  
`x4-1920-32t-metal` | 32 | 32 | Not available | 8  
  
### Network support for X4 instances

X4 bare metal instances require the [Intel IDPF LAN PF device driver](https://docs.cloud.google.com/compute/docs/networking/using-idpf). X4 supports up to 100 Gbps network bandwidth for standard networking. The gVNIC network interface isn't supported with bare metal.

Before migrating to X4 or creating X4 instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the IDPF network driver. If you create an X4 instance with an operating system that doesn't support the IDPF driver, then you might not be able to connect to the instance.

### Maintenance experience for X4 instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple _host events_. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The X4 machine series offers the following features related to host maintenance:

Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | On-demand maintenance | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance)  
---|---|---|---|---|---  
All machine types | Minimum of 90 days | Restart in place | 60 days | Yes | Yes  
  
The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

X4 also lets you perform maintenance for unplanned emergent maintenance events within a short window of time. Emergent maintenance events are typically needed to address security, hardware, or software issues of medium to high severity that have a high potential for causing outages. These maintenance events are deemed important and time-sensitive, but not critical enough to require an immediate outage to perform the maintenance. Emergent maintenance events have the following features for X4 machine types: 

  * [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event): 14 days
  * [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors): Restart in place



During emergent maintenance maintenance, X4 instances are moved to a different, healthy host.

For emergent maintenance events, you can trigger the maintenance at any time within the 14 day advance notification period. If you don't begin the maintenance operation within the 14-day period, then the maintenance starts automatically at the end of the advanced notification period.

For information about how to manually start host maintenance events for X4 instances, see [Manually starting host maintenance doesn't work for X4 instances](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#x4-ctm).

## M4N machine series

M4N is engineered to deliver leading block storage performance with Hyperdisk Extreme, scaling up to 25 GiB/s of Hyperdisk bandwidth and up to 1,000,000 IOPS on the largest machine types. M4N also provides up to 400 Gbps network bandwidth on the largest machine types. This new level of performance opens up new possibilities for I/O-intensive workloads that require extreme bandwidth for data access and processing.

M4N instances are powered by the Intel Emerald Rapids processors and [Titanium](https://cloud.google.com/titanium) offload processors. The largest M4N machine types provide twice as much disk I/O performance as M4 instances due to having two Titanium Smart NICs for each instance.

This machine series is well-suited for large in-memory databases such as SAP HANA, as well as online analytical processing (OLAP) and in-memory data analytics workloads. The M4N machine series with Hyperdisk Extreme offers a lower cost per transaction for Oracle Database workloads and the best TCO when compared to any other Google Cloud memory-optimized instance for databases that require licensing per core.

M4N instances are eligible for the following discounts with long term purchase commitments:

  * **Resource-based committed use discounts (CUDs)** : savings of 60% in exchange for 3-year commitments and savings of 37% in exchange for 1-year commitments. For the commitment type values to use, see the [resource-based CUDs documentation](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments).
  * **Compute flexible CUDs** : savings of 54% in exchange for 3-year commitments, and savings of 28% in exchange for 1-year commitments. For more information about compute flexible CUDs, see the [compute flexible CUDs documentation](https://docs.cloud.google.com/compute/docs/instances/flexible-committed-use-discounts).



M4N machine types allow you to provision up to 224 vCPUs and up to 6 TB of RAM. M4N instances use only NVMe for storage, and support [Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced) and [Hyperdisk Extreme](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme). M4N instances use only [gVNIC for networking](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). VirtIO-net and SCSI interfaces are not supported.

### M4N Limitations

The M4N machine series has the following restrictions:

  * M4N machine types are only available as predefined machine types. Custom machine types aren't available.
  * You can't use GPUs with M4N instances.
  * M4N instances are available in only [select zones and regions](https://docs.cloud.google.com/compute/docs/regions-zones#available).



### M4N machine types

Machine types | vCPUs1 | Memory (GB) | Titanium SSD | Physical NIC count | NUMA domains | Maximum internal network bandwidth  
(Gbps)2 | Maximum external network bandwidth  
(Gbps)2  
---|---|---|---|---|---|---|---  
`m4n-hypermem-16` | 16 | 248 | Not available | 1 | 1 shared | Up to 50 | Up to 7  
`m4n-hypermem-32` | 32 | 496 | Not available | 1 | 1 shared | 57 | 7  
`m4n-hypermem-64` | 64 | 992 | Not available | 1 | 2 shared | 114 | 7  
`m4n-megamem-28` | 28 | 372 | Not available | 1 | 1 shared | 50 | 7  
`m4n-megamem-56` | 56 | 744 | Not available | 1 | 1 isolated | 100 | 7  
`m4n-megamem-112` | 112 | 1,488 | Not available | 1 | 2 isolated | 200 | 7  
`m4n-megamem-224` | 224 | 2,976 | Not available | 2 | 4 (full server) | 100 | 7  
`m4n-ultramem-56` | 56 | 1,488 | Not available | 1 | 2 shared | 100 | 7  
`m4n-ultramem-112` | 112 | 2,976 | Not available | 1 | 4 shared | 200 | 7  
`m4n-ultramem-224` | 224 | 5,952 | Not available | 2 | 4 (full server) | 100 | 7  
  
1 Each virtual CPU (vCPU) is implemented as a single hardware multithread, and two vCPUs share each physical CPU core by default.  
2 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  


### Supported disk types for M4N

M4N instances can use the following block storage types:

  * Hyperdisk Balanced (`hyperdisk-balanced`)
  * Hyperdisk Balanced High Availability (`hyperdisk-balanced-high-availability`)
  * Hyperdisk Extreme (`hyperdisk-extreme`)
  * Hyperdisk Throughput (`hyperdisk-throughput`)
  * Hyperdisk ML (`hyperdisk-ml`)



#### Disk and capacity limits

The following restrictions apply:

  * The number of Hyperdisk volumes can't exceed 64 per VM.
  * The maximum total disk capacity across all disks can't exceed 512 TiB.



For details about the capacity limits, see [Hyperdisk capacity limits per VM](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#limits-instance).

M4N storage limits are described in the following table:

| Maximum number of disks |   
---|---|---  
Machine types | Hyperdisk  
per VM | Hyperdisk Balanced1 | Hyperdisk Throughput | Hyperdisk Extreme | Hyperdisk ML  
`m4n-hypermem-16` | 16 | 16 | 16 | 8 | 16  
`m4n-hypermem-32` | 32 | 32 | 32 | 8 | 32  
`m4n-hypermem-64` | 32 | 32 | 32 | 8 | 32  
`m4n-megamem-28` | 32 | 32 | 32 | 8 | 32  
`m4n-megamem-56` | 32 | 32 | 32 | 8 | 32  
`m4n-megamem-112` | 64 | 64 | 64 | 8 | 64  
`m4n-megamem-224` | 128 | 128 | 128 | 8 | 128  
`m4n-ultramem-56` | 32 | 32 | 32 | 8 | 32  
`m4n-ultramem-112` | 64 | 64 | 64 | 8 | 64  
`m4n-ultramem-224` | 128 | 128 | 128 | 8 | 128  
  
1 Includes Hyperdisk Balanced High Availability disks.

### Network support for M4N instances

M4N instances deliver up to 400 Gbps standard network bandwidth for VM-to-VM networking, a 4x increase in network bandwidth per vCPU when compared to standard M4 instances. M4N instances don't use per VM Tier_1 networking performance.

For the largest M4N machine types (224 vCPUs), during instance creation you must configure at least 2 network interfaces (vNICs) that use [Jumbo frames (8896B)](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu) to achieve the full network throughput. Compute Engine maps the vNICs automatically to physical NICs (pNICs) in a round-robin way. The guest OS or your application can then divide the network load across at least two vNICs (mapped to separate pNICs) to achieve the full network throughput and ensure optimal performance.

M4N instances require [gVNIC network interfaces](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). The maximum number of network interfaces that you can attach to an instance scales with the number of vCPUs, up to a maximum of 10 network interfaces. For more information about using multiple network interfaces with Compute Engine, see [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts). 

Before migrating to M4N or creating M4N instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use fully supports M4N and higher network bandwidths. Google recommends using the latest gVNIC driver version to benefit from additional features and bug fixes.

### Maintenance experience for M4N instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple _host events_. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The M4N machine series offers the following features related to host maintenance:

Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance)  
---|---|---|---|---|---  
All machine types | Monthly | Live migrate | 7 days | Yes | Yes  
  
The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## M4 machine series

The M4 machine series offers machine types that are suitable for OLTP and OLAP workloads running on SAP HANA. These machine types allow you to provision up to 224 vCPUs and up to 6 TB of RAM. M4 instances use only NVMe for storage, and support [Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced) and [Hyperdisk Extreme](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme). M4 instances use only [gVNIC for networking](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). VirtIO-net and SCSI interfaces are not supported.

M4 instances support resource-based CUDs, Spot VMs, and reservations, as well as performance monitoring unit (PMU), and compact placement policies.

Resource-based CUDs for M4 instances are available under two separate commitment types, each applying to specific machine types. When you purchase a commitment, ensure that you select the correct commitment type, as follows:

  * For `m4-ultramem-224` (6 TB), select **Memory-optimized M4 6TB** as the commitment type in the Google Cloud console.
  * For any other M4 machine type, select **Memory-optimized M4** as the commitment type in the Google Cloud console.
  * If you use gcloud CLI or REST to purchase commitments, see the [resource-based CUDs documentation](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments) for the commitment type values to use.



### M4 machine types

The following table lists the hardware characteristics of each machine type for the M4 machine series:

Machine types | vCPUs | Memory (GB) | Local SSD | NUMA domains2 | Default egress  
bandwidth (Gbps)1 | Tier_1 egress  
bandwidth (Gbps)  
---|---|---|---|---|---|---  
`m4-hypermem-16` | 16 | 248 | Not available | 1 shared | Up to 16 | Not available  
`m4-hypermem-32` | 32 | 496 | Not available | 1 shared | Up to 32 | Not available  
`m4-hypermem-64` | 64 | 992 | Not available | 2 shared | Up to 32 | Not available  
`m4-megamem-28` | 28 | 372 | Not available | 1 shared | Up to 32 | Not available  
`m4-megamem-56` | 56 | 744 | Not available | 1 isolated | Up to 32 | Not available  
`m4-megamem-112` | 112 | 1,488 | Not available | 2 isolated | Up to 50 | Not available  
`m4-megamem-224` | 224 | 2,976 | Not available | 4 (full machine) | Up to 100 | Not available  
`m4-ultramem-56` | 56 | 1,488 | Not available | 2 shared | Up to 32 | Not available  
`m4-ultramem-112` | 112 | 2,976 | Not available | 4 shared | Up to 50 | Not available  
`m4-ultramem-224` | 224 | 5,952 | Not available | 4 (full machine) | Up to 100 | Not available  
  
1 Maximum egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
2 The "NUMA domains" column in the tables shows the number of vNUMA nodes exposed to the guest OS.

### Supported disk types for M4

M4 machine types support the following block storage options:

  * Hyperdisk Balanced (`hyperdisk-balanced`)
  * Hyperdisk Extreme (`hyperdisk-extreme`)



M4 machine types support only the NVMe disk interface.

M4 instances don't support Persistent Disk or Local SSD. Read [Move your workload from an existing VM to a new VM](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm) to migrate your Persistent Disk resources to a newer machine series.

#### Disk and capacity limits

You can attach a mixture of different Hyperdisk types to an instance, but the maximum total disk capacity (in TiB) across all disk types can't exceed: 

  * For machine types with less than 32 vCPUs: 257 TiB for all Hyperdisk

  * For machine types with 32 or more vCPUs: 512 TiB for all Hyperdisk




For details about the capacity limits, see [ Hyperdisk size and attachment limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance).

M4 instance storage limits are described in the following table:

| Maximum number of disks  
---|---  
Machine types | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk Extreme  
`m4-hypermem-16` | 16 | 16 | 0 | 0  
`m4-hypermem-32` | 32 | 32 | 0 | 0  
`m4-hypermem-64` | 32 | 32 | 0 | 8  
`m4-megamem-28` | 32 | 32 | 0 | 0  
`m4-megamem-56` | 32 | 32 | 0 | 0  
`m4-megamem-112` | 64 | 64 | 0 | 8  
`m4-ultramem-56` | 32 | 32 | 0 | 0  
`m4-ultramem-112` | 64 | 64 | 0 | 8  
`m4-ultramem-224` | 128 | 128 | 0 | 8  
  
### Network support for M4 instances

M4 instances require [gVNIC network interfaces](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). M4 instances support up to 100 Gbps network bandwidth for standard networking and don't support per VM Tier_1 networking performance.

M4 instances require [gVNIC network interfaces](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). The maximum number of network interfaces that you can attach to an instance scales with the number of vCPUs, up to a maximum of 10 network interfaces. For more information about using multiple network interfaces with Compute Engine, see [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts). 

Before migrating to M4 or creating M4 VM instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the gVNIC driver for VM instances. These images include an updated gVNIC driver, even if the guest OS shows the `gve` driver version as 1.0.0. If your M4 VM is using an operating system with an older version of gVNIC driver, this is still supported but the VM might experience suboptimal performance such as less network bandwidth or higher latency.

If you use a custom OS image to create a M4 VM, you can [manually install the most recent gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup). The gVNIC driver version v1.4.2 or later is recommended for use with M4 VMs. Google recommends using the latest gVNIC driver version to benefit from additional features and bug fixes.

### M4 Limitations

The M4 machine series is only available as predefined machine types. Custom machine shapes are not available. The M4 instances are available in only [select zones and regions](https://docs.cloud.google.com/compute/docs/regions-zones#available).

### Maintenance experience for M4 instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple _host events_. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The M4 machine series offers the following features related to host maintenance:

Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance)  
---|---|---|---|---|---  
All machine types | Monthly | Live migrate | 7 days | Yes | Yes  
  
The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## M3 machine series

The M3 machine series introduces two new OLAP shapes for 2 TiB and 1 TiB SAP HANA systems. These machine types allow you to provision up to 128 vCPUs and up to 4 TB of RAM. M3 instances use only NVMe for storage, and support [Hyperdisk Balanced storage](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced). M3 machines use only [gVNIC for networking](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). VirtIO-net and SCSI interfaces are not supported.

[Pricing](https://docs.cloud.google.com/compute/all-pricing#memory-optimized) for these instances per vCPU hour and per GB of memory is similar to the pricing for M1 instances. Disk usage and network usage is charged separately from machine type pricing. For details, see [Disk and image pricing](https://cloud.google.com/compute/disks-image-pricing) and [Network pricing](https://cloud.google.com/vpc/network-pricing).

M3 instances support resource-based CUDs, Spot VMs, and reservations, as well as compact placement policies. The commitment type that you must use to purchase M3 instances is separate from the one for M1 or M2 instances. You can purchase a single commitment to cover both M1 and M2 instances, but you can't group M3 instances in that commitment. For more information, see the [Commitment types](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#commitment_types) section for resource-based commitments.

To update a current instance to use the M3 machine series, see [Move your workload to a new compute instance](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm).

### M3 machine types

The following table lists the hardware characteristics of each machine type for the M3 machine series:

Machine types | vCPUs | Memory (GB) | Local SSD1 | Default egress bandwidth (Gbps)2 | Tier_1 egress bandwidth (Gbps)3  
---|---|---|---|---|---  
`m3-ultramem-32` | 32 | 976 | 4 or 8 | Up to 32 | Not available  
`m3-ultramem-64` | 64 | 1,952 | 4 or 8 | Up to 32 | Up to 50  
`m3-ultramem-128` | 128 | 3,904 | 8 | Up to 32 | Up to 100  
`m3-megamem-64` | 64 | 976 | 4 or 8 | Up to 32 | Up to 50  
`m3-megamem-128` | 128 | 1,952 | 8 | Up to 32 | Up to 100  
  
1 Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
2 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3 Available with [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) on larger machine shapes. 

### Supported disk types for M3

M3 machine types support the following block storage options:

  * Zonal balanced Persistent Disk (`pd-balanced`)
  * Zonal SSD (performance) Persistent Disk (`pd-ssd`)
  * [Extreme Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/extreme-persistent-disk) (`pd-extreme`)
  * Hyperdisk Balanced (`hyperdisk-balanced`)
  * Hyperdisk Balanced High Availability (`hyperdisk-balanced-high-availability`)
  * Hyperdisk Extreme (`hyperdisk-extreme`)
  * Hyperdisk Throughput (`hyperdisk-throughput`)
  * Local SSD



M3 machine types support only the NVMe disk interface.

#### Disk and capacity limits

If supported by the machine type, you can attach a mixture of Hyperdisk and Persistent Disk volumes to an instance, but the following restrictions apply: 

  * The combined number of both Hyperdisk and Persistent Disk volumes can't exceed 128 per instance.
  * The maximum total disk capacity (in TiB) across all disk types can't exceed:

    * For machine types with less than 32 vCPUs:

      * 257 TiB for all Hyperdisk or all Persistent Disk
      * 257 TiB for a mixture of Hyperdisk and Persistent Disk
    * For machine types with 32 or more vCPUs:

      * 512 TiB for all Hyperdisk
      * 512 TiB for a mixture of Hyperdisk and Persistent Disk
      * 257 TiB for all Persistent Disk



For details about the capacity limits, see [ Hyperdisk size and attachment limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance) and [Persistent Disk maximum capacity](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#capacity_257tb).

The maximum number of disks that you can attach to M3 instances are described in the following table:

Machine types | Per VM1 | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk Extreme  
---|---|---|---|---|---  
`m3-ultramem-32` | 128 | 64 | 32 | 64 | 0  
`m3-ultramem-64` | 128 | 64 | 32 | 64 | 8  
`m3-ultramem-128` | 128 | 64 | 32 | 64 | 8  
`m3-megamem-64` | 128 | 64 | 32 | 64 | 8  
`m3-megamem-128` | 128 | 64 | 32 | 64 | 8  
  
1 This limit applies to Persistent Disk and Hyperdisk, but doesn't include Local SSD disks. 

### Network support for M3 instances

M3 instances require [gVNIC network interfaces](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). M3 instances support up to 32 Gbps network bandwidth for standard networking and up to 100 Gbps network bandwidth per VM Tier_1 networking performance.

Before migrating to M3 or creating M3 VM instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the gVNIC driver for VM instances. These images include an updated gVNIC driver, even if the guest OS shows the `gve` driver version as 1.0.0. If your M3 VM is using an operating system with an older version of gVNIC driver, this is still supported but the VM might experience suboptimal performance such as less network bandwidth or higher latency.

If you use a custom OS image to create a M3 VM, you can [manually install the most recent gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup). The gVNIC driver version v1.4.2 or later is recommended for use with M3 VMs. Google recommends using the latest gVNIC driver version to benefit from additional features and bug fixes.

### M3 Limitations

The M3 machine series is only available as predefined machine types. Custom machine shapes are not available. The following additional restrictions apply:

  * You can't use [regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) with the M3 machine series.
  * The M3 machine series is available in only [select zones and regions](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * M3 instances aren't available with all operating system images. The [operating system details](https://docs.cloud.google.com/compute/docs/images/os-details) page shows which operating system versions can be used with M3 instances.
  * The M3 machine series doesn't support standard Persistent Disk (`pd-standard`).
  * The ability to add or resize a Persistent Disk for a running M3 instance doesn't work as expected on Windows Server 2016 or Windows Server 2012 R2 operating systems. For more information, see [Generic disk error on Windows Server 2016 and 2012 R2 for M3 VMs](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#windows_nvme_disks).



### Maintenance experience for M3 instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple _host events_. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The M3 machine series offers the following features related to host maintenance:

Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance)  
---|---|---|---|---|---  
All machine types | Minimum of 30 days | Live migrate | 7 days | Yes | Yes  
  
The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## M2 machine series

With 6 TiB, 9 TiB, and 12 TiB machine types in the M2 machine series, SAP customers can run their largest SAP HANA databases on Google Cloud.

The M2 series is available with on-demand and spot pricing for an evaluation period only. Long running usage requires purchasing a resource-based commitment. For more information, see the [VM pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#larger_ultramem). Disk usage and network usage is charged separately from machine type pricing. For details, see [Disk and image pricing](https://cloud.google.com/compute/disks-image-pricing) and [Network pricing](https://cloud.google.com/vpc/network-pricing).

M2 instances support resource-based CUDs, Spot VMs, reservations, and compact placement policies.

### M2 machine types

The following table lists the hardware characteristics of each machine type for the M2 machine series:

Machine types | vCPUs1 | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)2  
---|---|---|---|---  
`m2-ultramem-208` | 208 | 5,888 | Not available | Up to 323  
`m2-ultramem-416` | 416 | 11,776 | Not available | Up to 323  
`m2-megamem-416` | 416 | 5,888 | Not available | Up to 323  
`m2-hypermem-416` | 416 | 8,832 | Not available | Up to 323  
  
1 A vCPU is implemented as a single hardware Hyper-thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3 32 Gbps for Cascade Lake or later [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms). 16 Gbps for all other platforms.

### Supported disk types for M2

M2 machine types can use the following block storage options:

  * Zonal balanced Persistent Disk (`pd-balanced`)
  * Zonal SSD (Performance) Persistent Disk (`pd-ssd`)
  * Extreme Persistent Disk (`pd-extreme`)
  * Hyperdisk Balanced (`hyperdisk-balanced`)
  * Hyperdisk Extreme (`hyperdisk-extreme`)



If supported by the machine type, you can attach a mixture of Hyperdisk and Persistent Disk volumes to an instance, but the following restrictions apply: 

  * The combined number of both Hyperdisk and Persistent Disk volumes can't exceed 128 per instance.
  * The maximum total disk capacity (in TiB) across all disk types can't exceed:

    * For machine types with less than 32 vCPUs:

      * 257 TiB for all Hyperdisk or all Persistent Disk
      * 257 TiB for a mixture of Hyperdisk and Persistent Disk
    * For machine types with 32 or more vCPUs:

      * 512 TiB for all Hyperdisk
      * 512 TiB for a mixture of Hyperdisk and Persistent Disk
      * 257 TiB for all Persistent Disk



For details about the capacity limits, see [ Hyperdisk size and attachment limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance) and [Persistent Disk maximum capacity](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#capacity_257tb).

The maximum number of disks that you can attach to M2 instances are described in the following table:

Machine types | Per VM | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk Extreme  
---|---|---|---|---|---  
`m2-ultramem-208` | 128 | 64 | 32 | 0 | 8  
`m2-ultramem-416` | 128 | 64 | 32 | 0 | 8  
`m2-megamem-416` | 128 | 64 | 32 | 0 | 8  
`m2-hypermem-416` | 128 | 64 | 32 | 0 | 8  
  
### M2 Limitations

The M2 machine series is available only as predefined machine types. This series offers from 14 GB to 28 GB memory per vCPU. The following restrictions apply:

  * The M2 machine series is available in only [select zones and regions](https://docs.cloud.google.com/compute/docs/regions-zones#available) on specific [CPU processors](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison).
  * You can't use [regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) with the M2 machine series.
  * The M2 machine series uses only the SCSI interface for attached disks.
  * [Sole tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes) are available for only the `m2-ultramem-416` shape.
  * You can't use Windows Server 2016 OS images with machine types that have more than 255 vCPUs.



### Maintenance experience for M2 instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple _host events_. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The M2 machine series offers the following features related to host maintenance:

Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance)  
---|---|---|---|---|---  
All machine types | Minimum of 30 days | Live migrate | 7 days | Yes | Yes  
  
The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## M1 machine series

The M1 machine series is the older generation memory-optimized machine series that offers 14.9 to 24 GB of memory per vCPU. This series offers the `m1-ultramem` and `m1-megamem` machine types and are only available in specific [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

**Note:** The prefix in the following machine names changed from "`n1`" to "`m1`" to more clearly identify the machines as members of the memory-optimized machine family: 

  * `n1-megamem-96` is now `**m1** -megamem-96`
  * `n1-ultramem-40` is now `**m1** -ultramem-40`
  * `n1-ultramem-80` is now `**m1** -ultramem-80`
  * `n1-ultramem-160` is now `**m1** -ultramem-160`

The machines themselves did not change and the former names are still supported as aliases for these machines. 

For details on pricing, see the [VM pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#m1_machine_types). Disk usage and network usage is charged separately from machine type pricing. For more information, see [Disk and image pricing](https://cloud.google.com/compute/disks-image-pricing) and [Network pricing](https://cloud.google.com/vpc/network-pricing).

M1 instances support resource-based CUDs, Spot VMs, reservations, and compact placement policies.

### M1 machine types

The following table lists the hardware characteristics of each machine type for the M1 machine series:

Machine types | vCPUs1 | Memory (GB) | Local SSD2 | Default egress bandwidth (Gbps)3  
---|---|---|---|---  
`m1-ultramem-40` | 40 | 961 | 5 | Up to 32  
`m1-ultramem-80` | 80 | 1922 | 8 | Up to 32  
`m1-ultramem-160` | 160 | 3844 | Not available | Up to 32  
`m1-megamem-96` | 96 | 1433.6 | Not available | Up to 32  
  
1 A vCPU is implemented as a single hardware thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
3 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).

### Supported disk types for M1

M1 machine types can use the following block storage options:

  * Zonal balanced Persistent Disk (`pd-balanced`)
  * Zonal SSD (Performance) Persistent Disk (`pd-ssd`)
  * Extreme Persistent Disk (`pd-extreme`)
  * Hyperdisk Balanced (`hyperdisk-balanced`)
  * Hyperdisk Extreme (`hyperdisk-extreme`)
  * Local SSD



If supported by the machine type, you can attach a mixture of Hyperdisk and Persistent Disk volumes to an instance, but the following restrictions apply: 

  * The combined number of both Hyperdisk and Persistent Disk volumes can't exceed 128 per instance.
  * The maximum total disk capacity (in TiB) across all disk types can't exceed:

    * For machine types with less than 32 vCPUs:

      * 257 TiB for all Hyperdisk or all Persistent Disk
      * 257 TiB for a mixture of Hyperdisk and Persistent Disk
    * For machine types with 32 or more vCPUs:

      * 512 TiB for all Hyperdisk
      * 512 TiB for a mixture of Hyperdisk and Persistent Disk
      * 257 TiB for all Persistent Disk



For details about the capacity limits, see [ Hyperdisk size and attachment limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance) and [Persistent Disk maximum capacity](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#capacity_257tb).

The maximum number of disks that you can attach to M1 instances are described in the following table:

Machine types | Per VM1 | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk Extreme  
---|---|---|---|---|---  
`m1-ultramem-40` | 128 | 64 | 32 | 0 | 0  
`m1-ultramem-80` | 128 | 64 | 32 | 0 | 8  
`m1-ultramem-160` | 128 | 64 | 32 | 0 | 8  
`m1-megamem-96` | 128 | 64 | 32 | 0 | 8  
  
### M1 Limitations

The M1 machine series is only available as predefined machine types. This series offers 14 GB to 28 GB of memory per vCPU. The following restrictions apply:

  * You can't use [regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) with the M1 series.
  * M1 instances are only available in [select zones and regions](https://docs.cloud.google.com/compute/docs/regions-zones#available) on specific [CPU processors](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison).



### Maintenance experience for M1 instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple _host events_. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The M1 machine series offers the following features related to host maintenance:

Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance)  
---|---|---|---|---|---  
All machine types | Minimum of 30 days | Live migrate | 7 days | Yes | Yes  
  
The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## What's next

  * [Creating and starting a virtual machine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance)
  * Learn about the different [Storage options](https://docs.cloud.google.com/compute/docs/disks) for your instance.
  * [Move your workload to a new compute instance](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm)
  * [Using Google Virtual NIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic)
  * [VM instance pricing](https://cloud.google.com/compute/vm-instance-pricing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
