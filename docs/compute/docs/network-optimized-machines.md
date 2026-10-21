---
url: https://docs.cloud.google.com/compute/docs/network-optimized-machines/
title: Network-optimized machine family for Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T23:39:01.104324+00:00
---

# Network-optimized machine family for Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/network-optimized-machines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Network-optimized machine family for Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

The network-optimized machine family delivers the highest network and block storage performance within Compute Engine. They offer best-in-class price-performance optimized for demanding I/O bound applications such as network and security appliances, high-performance databases, Telco 5G UPF, high-scale data analytics, and distributed file systems. Compared to the general-purpose machine family, the machine series in the network-optimized machine family offer significantly higher:

  * Network bandwidth
  * Packet processing performance (PPS)
  * Storage throughput and IOPS per vCPU



By eliminating the need to over-provision compute resources just to scale I/O capabilities, the network-optimized family delivers significant Total Cost of Ownership (TCO) benefits.

**Machine series** | **Workloads**  
---|---  
C4N | 

  * Network and Security appliances
    * Firewall
    * Load balancers
    * Virtual routers
    * DDOS mitigation appliances
    * NatProxy
    * CDN
  * Telco (5G UPF)
  * High density containers
  * Filesystems
  * High performance databases
  * Large-scale data analytics
  * CPU-based AI/ML workloads

  
M4N | 

  * High performance databases
  * Retrieval-augmented generation (RAG) data layers
  * Massive in-memory context caching
  * Real-time semantic search

  
  
## C4N machine series

C4N instances are powered by 5th Generation Intel Xeon Scalable processors (code named Emerald Rapids) running high-frequency DDR5 memory and dual-NIC [Titanium](https://cloud.google.com/titanium) offloaded architecture. The C4N machine series is engineered to maximize both networking throughput and extreme block storage performance without requiring premium infrastructure add-ons (such as per VM Tier_1 networking performance).

  * **For databases** : When compared to similarly sized C4 instances, C4N delivers 45% better queries per second for MySQL when the data resides primarily on disk.
  * **For web-serving workloads** : C4N significantly boosts performance for network-bound web applications. C4N delivers up to 55% additional Nginx requests per second for typical web request sizes (100-300kb) when compared to C4.



C4N instances are available in 8 predefined machine types across standard, high CPU, and high memory configurations, scaling from 2 to 192 vCPUs and up to 1.5 TB of memory.

C4N offers the following features:

  * **Superior VM-to-VM network bandwidth** : Achieves up to 400 Gbps of VM-to-VM network bandwidth and supports up to 50 Gbps single-flow bandwidth between C4N instances routed within the same VPC network.
  * **Enhanced VM to Internet performance** : Internet egress network bandwidth can reach up to 200 Gbps. Internet egress packet processing performance can scale up to 48 million packets per second (MPPS).
  * **Industry-leading packet processing** : Up to 95 MPPS of sustained packet processing performance (measured using DPDK Pktgen).
  * **Optimized I/O for smaller shapes** : Up to 25 to 50 Gbps of network bandwidth specifically for machine types with 2 to 16 vCPUs. Additionally, these smaller machine types introduce predictable, steady-state baseline bandwidth limits to provide consistent performance at a lower cost.
  * **Enhanced out-of-the-box networking** : gVNIC-type network interfaces on C4N now start with more Tx/Rx queues by default, and scale with the number of vCPUs up to a maximum of 64 per vNIC.
  * **Titanium-powered efficiency with Dual-NIC Titanium architecture** : Features two 200G Titanium network adapters (2 x 200G) to fully offload network and storage management, ensuring your applications run with maximum performance and predictability.
  * **Leading Block Storage performance and options** : Supports the complete Hyperdisk portfolio, including Hyperdisk Balanced, Hyperdisk Balanced High Availability, Hyperdisk Extreme, Hyperdisk Throughput, and Hyperdisk ML block storage options. C4N with Hyperdisk Extreme provides the low-latency, high-speed data access that modern databases and enterprise AI applications need, with up to 25 GiB/s of block storage throughput and nearly 1M IOPS. C4N offers a 2.5x increase in storage performance over C4.



C4N supports the following discount and consumption options:

  * Resource-based committed use discounts (CUDs)
  * Flexible CUDs
  * Spot VMs 
  * Reservations
  * Sole-tenancy
  * Spread and compact placement policies



### C4N Limitations

The C4N machine series has the following restrictions:

  * C4N machine types are only available as predefined machine types. Custom machine types aren't available.
  * You can't use GPUs with C4N instances.



### C4N machine types

### C4N highcpu

Machine types | vCPUs1 | Memory (GB) | Titanium SSD | Physical NIC count | NUMA domains | Maximum internal bandwidth (Gbps) | Maximum external bandwidth (Gbps)  
---|---|---|---|---|---|---|---  
`c4n-highcpu-2` | 2 | 4 | Not supported | 1 | 1 shared | Up to 25 | Up to 7  
`c4n-highcpu-4` | 4 | 8 | Not supported | 1 | 1 shared | Up to 30 | Up to 7  
`c4n-highcpu-8` | 8 | 16 | Not supported | 1 | 1 shared | Up to 40 | Up to 15  
`c4n-highcpu-16` | 16 | 32 | Not supported | 1 | 1 shared | Up to 50 | Up to 25  
`c4n-highcpu-24` | 24 | 48 | Not supported | 1 | 1 shared | 50 | Up to 25  
`c4n-highcpu-48` | 48 | 96 | Not supported | 1 | 1 isolated | 100 | Up to 50  
`c4n-highcpu-96` | 96 | 192 | Not supported | 1 | 2 | 200 | Up to 100  
`c4n-highcpu-192` | 192 | 384 | Not supported | 2 | 4 (full machine) | 4002 | Up to 200  
  
### C4N standard

Machine types | vCPUs1 | Memory (GB) | Titanium SSD | Physical NIC count | NUMA domains | Maximum internal bandwidth (Gbps) | Maximum external bandwidth (Gbps)  
---|---|---|---|---|---|---|---  
`c4n-standard-2` | 2 | 7 | Not supported | 1 | 1 shared | Up to 25 | Up to 7  
`c4n-standard-4` | 4 | 15 | Not supported | 1 | 1 shared | Up to 30 | Up to 7  
`c4n-standard-8` | 8 | 30 | Not supported | 1 | 1 shared | Up to 40 | Up to 15  
`c4n-standard-16` | 16 | 60 | Not supported | 1 | 1 shared | Up to 50 | Up to 25  
`c4n-standard-24` | 24 | 90 | Not supported | 1 | 1 shared | 50 | Up to 25  
`c4n-standard-48` | 48 | 180 | Not supported | 1 | 1 isolated | 100 | Up to 50  
`c4n-standard-96` | 96 | 360 | Not supported | 1 | 2 | 200 | Up to 100  
`c4n-standard-192` | 192 | 720 | Not supported | 2 | 4 (full machine) | 4002 | Up to 200  
  
### C4N highmem

Machine types | vCPUs1 | Memory (GB) | Titanium SSD | Physical NIC count | NUMA domains | Maximum internal bandwidth (Gbps) | Maximum external bandwidth (Gbps)  
---|---|---|---|---|---|---|---  
`c4n-highmem-2` | 2 | 15 | Not supported | 1 | 1 shared | Up to 25 | Up to 7  
`c4n-highmem-4` | 4 | 31 | Not supported | 1 | 1 shared | Up to 30 | Up to 7  
`c4n-highmem-8` | 8 | 62 | Not supported | 1 | 1 shared | Up to 40 | Up to 15  
`c4n-highmem-16` | 16 | 124 | Not supported | 1 | 1 shared | Up to 50 | Up to 25  
`c4n-highmem-24` | 24 | 186 | Not supported | 1 | 1 shared | 50 | Up to 25  
`c4n-highmem-48` | 48 | 372 | Not supported | 1 | 1 isolated | 100 | Up to 50  
`c4n-highmem-96` | 96 | 744 | Not supported | 1 | 2 | 200 | Up to 100  
`c4n-highmem-192` | 192 | 1488 | Not supported | 2 | 4 (full machine) | 4002 | Up to 200  
  
### C4N standard

Machine types | vCPUs1 | Memory (GB) | Titanium SSD | Physical NIC count | NUMA domains | Maximum internal bandwidth (Gbps) | Maximum external bandwidth (Gbps)  
---|---|---|---|---|---|---|---  
`c4n-standard-4-lssd` | 4 | 15 | (1 x 375 GiB) 375 GiB | 1 | 1 shared | Up to 30 | Up to 7  
`c4n-standard-8-lssd` | 8 | 30 | (1 x 375 GiB) 375 GiB | 1 | 1 shared | Up to 40 | Up to 15  
`c4n-standard-16-lssd` | 16 | 60 | (2 x 375 GiB) 750 GiB | 1 | 1 shared | Up to 50 | Up to 25  
`c4n-standard-24-lssd` | 24 | 90 | (4 x 375 GiB) 1,500 GiB | 1 | 1 shared | 50 | Up to 25  
`c4n-standard-48-lssd` | 48 | 180 | (8 x 375 GiB) 3,000 GiB | 1 | 1 isolated | 100 | Up to 50  
`c4n-standard-96-lssd` | 96 | 360 | (16 x 375 GiB) 6,000 GiB | 1 | 2 | 200 | Up to 100  
`c4n-standard-192-lssd` | 192 | 720 | (32 x 375 GiB) 12,000 GiB | 2 | 4 (full machine) | 4002 | Up to 200  
  
### C4N highmem

Machine types | vCPUs1 | Memory (GB) | Titanium SSD | Physical NIC count | NUMA domains | Maximum internal bandwidth (Gbps) | Maximum external bandwidth (Gbps)  
---|---|---|---|---|---|---|---  
`c4n-highmem-4-lssd` | 4 | 31 | (1 x 375 GiB) 375 GiB | 1 | 1 shared | Up to 30 | Up to 7  
`c4n-highmem-8-lssd` | 8 | 62 | (1 x 375 GiB) 375 GiB | 1 | 1 shared | Up to 40 | Up to 15  
`c4n-highmem-16-lssd` | 16 | 124 | (2 x 375 GiB) 750 GiB | 1 | 1 shared | Up to 50 | Up to 25  
`c4n-highmem-24-lssd` | 24 | 186 | (4 x 375 GiB) 1,500 GiB | 1 | 1 shared | 50 | Up to 25  
`c4n-highmem-48-lssd` | 48 | 372 | (8 x 375 GiB) 3,000 GiB | 1 | 1 isolated | 100 | Up to 50  
`c4n-highmem-96-lssd` | 96 | 744 | (16 x 375 GiB) 6,000 GiB | 1 | 2 | 200 | Up to 100  
`c4n-highmem-192-lssd` | 192 | 1,488 | (32 x 375 GiB) 12,000 GiB | 2 | 4 (full machine) | 4002 | Up to 200  
  
1 Each virtual CPU (vCPU) is implemented as a single hardware multithread. By default, two vCPUs share each physical CPU core.  
2 For instances with 192 vCPUs, you must configure at least 2 network interfaces (vNIC), with each network interface attached to a different physical NIC, to achieve the full network throughput. Compute Engine automatically maps the vNIC to a physical NIC in a round-robin fashion. 

### Supported disk types for C4N

C4N instances support only the NVMe disk interface and can use the following block storage types:

  * Hyperdisk Balanced (`hyperdisk-balanced`)
  * Hyperdisk Balanced High Availability (`hyperdisk-balanced-high-availability`)
  * Hyperdisk Throughput (`hyperdisk-throughput`)
  * Hyperdisk Extreme (`hyperdisk-extreme`)
  * Hyperdisk ML (`hyperdisk-ml`)
  * Titanium SSD



For the performance limits of each Hyperdisk type, see [Hyperdisk performance limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits).

#### Disk and capacity limits

The following restrictions apply:

  * The number of Hyperdisk volumes can't exceed 64 per VM.
  * The maximum total disk capacity across all disks can't exceed 512 TiB.



For details about the capacity limits, see [Hyperdisk capacity limits per VM](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#limits-instance).

C4N storage limits are described in the following table:

### C4N highcpu

Maximum number of disks per instance  
---  
Machine types | All Hyperdisk  
types | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme | Hyperdisk ML  
`c4n-highcpu-2` | 8 | 8 | 8 | 8 | 8 | 8  
`c4n-highcpu-4` | 16 | 16 | 16 | 16 | 8 | 16  
`c4n-highcpu-8` | 32 | 32 | 32 | 32 | 8 | 32  
`c4n-highcpu-16` | 32 | 32 | 32 | 32 | 8 | 32  
`c4n-highcpu-24` | 32 | 32 | 32 | 32 | 8 | 32  
`c4n-highcpu-48` | 64 | 64 | 64 | 64 | 8 | 64  
`c4n-highcpu-96` | 128 | 128 | 128 | 128 | 8 | 128  
`c4n-highcpu-192` | 128 | 128 | 128 | 128 | 8 | 128  
  
### C4N standard

Maximum number of disks per instance  
---  
Machine types | All Hyperdisk  
types | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme | Hyperdisk ML  
`c4n-standard-2` | 8 | 8 | 8 | 8 | 8 | 8  
`c4n-standard-4` | 16 | 16 | 16 | 16 | 8 | 16  
`c4n-standard-8` | 32 | 32 | 32 | 32 | 8 | 32  
`c4n-standard-16` | 32 | 32 | 32 | 32 | 8 | 32  
`c4n-standard-24` | 32 | 32 | 32 | 32 | 8 | 32  
`c4n-standard-48` | 64 | 64 | 64 | 64 | 8 | 64  
`c4n-standard-96` | 128 | 128 | 128 | 128 | 8 | 128  
`c4n-standard-192` | 128 | 128 | 128 | 128 | 8 | 128  
  
### C4N highmem

Maximum number of disks per instance  
---  
Machine types | All Hyperdisk  
types | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme | Hyperdisk ML  
`c4n-highmem-2` | 8 | 8 | 8 | 8 | 8 | 8  
`c4n-highmem-4` | 16 | 16 | 16 | 16 | 8 | 16  
`c4n-highmem-8` | 32 | 32 | 32 | 32 | 8 | 32  
`c4n-highmem-16` | 32 | 32 | 32 | 32 | 8 | 32  
`c4n-highmem-24` | 32 | 32 | 32 | 32 | 8 | 32  
`c4n-highmem-48` | 64 | 64 | 64 | 64 | 8 | 64  
`c4n-highmem-96` | 128 | 128 | 128 | 128 | 8 | 128  
`c4n-highmem-192` | 128 | 128 | 128 | 128 | 8 | 128  
  
### C4N standard

Maximum number of disks per instance  
---  
Machine types | All Hyperdisk  
types | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme | Hyperdisk ML  
`c4n-standard-4-lssd` | 16 | 16 | 16 | 16 | 8 | 16  
`c4n-standard-8-lssd` | 32 | 32 | 32 | 32 | 8 | 32  
`c4n-standard-16-lssd` | 32 | 32 | 32 | 32 | 8 | 32  
`c4n-standard-24-lssd` | 32 | 32 | 32 | 32 | 8 | 32  
`c4n-standard-48-lssd` | 64 | 64 | 64 | 64 | 8 | 64  
`c4n-standard-96-lssd` | 128 | 128 | 128 | 128 | 8 | 128  
`c4n-standard-192-lssd` | 128 | 128 | 128 | 128 | 8 | 128  
  
### C4N highmem

Maximum number of disks per instance  
---  
Machine types | All Hyperdisk  
types | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme | Hyperdisk ML  
`c4n-highmem-4-lssd` | 16 | 16 | 16 | 16 | 8 | 16  
`c4n-highmem-8-lssd` | 32 | 32 | 32 | 32 | 8 | 32  
`c4n-highmem-16-lssd` | 32 | 32 | 32 | 32 | 8 | 32  
`c4n-highmem-24-lssd` | 32 | 32 | 32 | 32 | 8 | 32  
`c4n-highmem-48-lssd` | 64 | 64 | 64 | 64 | 8 | 64  
`c4n-highmem-96-lssd` | 128 | 128 | 128 | 128 | 8 | 128  
`c4n-highmem-192-lssd` | 128 | 128 | 128 | 128 | 8 | 128  
  
### Network support for C4N instances

C4N instances deliver up to 400 Gbps standard network bandwidth for VM-to-VM networking, a 4x increase in network bandwidth per vCPU when compared to standard C4 instances. C4N instances don't use per VM Tier_1 networking performance.

For the largest C4N machine types (192 vCPUs) , during instance creation you must configure at least 2 network interfaces (vNICs) that use [Jumbo frames (8896B)](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu) to achieve the full network throughput. Compute Engine maps the vNICs automatically to physical NICs (pNICs) in a round-robin way. The guest OS or your application can then divide the network load across at least two vNICs (mapped to separate pNICs) to achieve the full network throughput and ensure optimal performance.

C4N instances require [gVNIC network interfaces](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). The maximum number of network interfaces that you can attach to an instance scales with the number of vCPUs, up to a maximum of 10 network interfaces. For more information about using multiple network interfaces with Compute Engine, see [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts). 

Before migrating to C4N or creating C4N instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use fully supports C4N and higher network bandwidths. Google recommends using the latest gVNIC driver version to benefit from additional features and bug fixes.

### Maintenance experience for C4N instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple _host events_. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The C4N machine series offers the following features related to host maintenance:

Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance)  
---|---|---|---|---|---  
`c4n-*-192` | Minimum of 30 days | Live migrate | Up to 7 days | Yes | Yes  
`c4n-*-lssd` | Minimum of 30 days | Live migrate | Up to 7 days | Yes | Yes  
All others | Minimum of 30 days | Live migrate | Up to 7 days | No | Yes  
  
The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

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

## What's next

  * [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance)
  * Learn about the different [block storage options](https://docs.cloud.google.com/compute/docs/disks) for your compute instance
  * Learn how to [move your workload to a new compute instance](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm)
  * Review [Virtual machine pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#network-optimized)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
