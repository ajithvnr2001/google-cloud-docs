---
url: https://docs.cloud.google.com/compute/docs/general-purpose-machines/
title: General-purpose machine family for Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:22.507498+00:00
---

# General-purpose machine family for Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/general-purpose-machines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  General-purpose machine family for Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the features of the Compute Engine general-purpose machine family, which has the best price-performance with the most flexible vCPU to memory ratios, and provides features that target most standard and cloud-native workloads.

The general-purpose machine family has predefined and custom machine types to align with your workload, depending on your requirements.

C4D is powered by the fifth generation AMD EPYC Turin processor and [Titanium](https://cloud.google.com/titanium). These machine types have up to 384 vCPUs and 3,024 GB of DDR5 memory, a max-boost frequency of 4.1 GHz, and up to 200 Gbps per VM Tier_1 networking performance. C4D also offers Local SSD (`-lssd`) machine types and bare metal (`-metal`) machine types.

C4A is powered by Google's Axion processor built on the Arm Neoverse V2 compute core. C4A provides `standard`, `highcpu`, and `highmem` machine types with up to 72 vCPUs, 576 GB DDR5 memory, 6 TiB of local Titanium SSD, and up to 100 Gbps with per VM Tier_1 networking performance. C4A also offers Local SSD (`-lssd`) machine types and a `highmem` bare metal (`-metal`) machine type with 96 vCPUs and 768 GB DDR5 memory.

C4 is powered by the sixth generation (code-named Granite Rapids) and fifth generation (code-named Emerald Rapids) Intel Xeon Scalable processors. C4 instances running on Granite Rapids offer a sustained, all-core turbo frequency of 3.9 GHz and a max turbo frequency of 4.2 GHz, 2.2 TB of DDR5 memory, 18 TiB of Titanium SSD for C4. supports up to 200 Gbps of per VM Tier_1 networking performance. C4 also offers Local SSD (`-lssd`) machine types and bare metal (`-metal`) machine types.

N4D is powered by the fifth generation AMD EPYC Turin processor and [Titanium](https://cloud.google.com/titanium). These machine types have up to 96 vCPUs and 768 GB of DDR5 memory, and a max-boost frequency of 4.1 GHz. N4D offers 50 Gbps of standard network bandwidth.

N4A is powered by Google's Axion processor built on the Arm Neoverse N3 compute core. N4A provides machine types of up to 64 vCPUs and 512 GB of DDR5 memory. N4A is available in standard, high-mem, high-cpu, and custom machine types with extended memory, and up to 50 Gbps of standard networking.

N4 is powered by the fifth generation Intel Xeon Scalable processor (code-named Emerald Rapids). N4 offers a sustained, all-core turbo frequency of 2.9 GHz, 640 GB of DDR5 memory, and up to 50 Gbps of standard network bandwidth.

C3 is powered by fourth generation Intel Xeon Scalable processors and offers a sustained, all-core turbo frequency of 3.0 GHz, 8 channels of DDR5 memory, and up to 200 Gbps per VM Tier_1 networking performance.

C3D is powered by fourth generation AMD EPYC Genoa processors and offers a sustained, all-core turbo frequency of 3.3 GHz, 2,880 GB of DDR5 memory, and up to 200 Gbps per VM Tier_1 networking performance.

For bare metal machine types, choose the C4, C4D, or C3 machine series.

All [third and fourth generation](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology) general-purpose VMs support [Titanium](https://cloud.google.com/titanium).

E2, E2 shared-core, N2, N2D, Tau T2A, and Tau T2D are second generation machine series in this family; N1 and its related shared-core machine types are the first generation machine series.

**Machine series** | **Workloads**  
---|---  
N4, N4A, N4D, N2, N2D, N1 | 

  * Medium traffic web and application servers
  * Containerized microservices
  * Business intelligence applications
  * Virtual desktops
  * CRM applications
  * Development and test environments
  * Batch processing
  * Storage and archive

  
C4A, C4, C4D, C3, C3D | 

  * High traffic web, app and ad servers
  * Databases and caches
  * Game servers
  * Data analytics
  * Media streaming and transcoding
  * Network appliances
  * CPU-based ML training and inference

  
E2 | 

  * Low-traffic web servers
  * Back office apps
  * Containerized microservices
  * Small databases
  * Virtual desktops
  * Development and test environments

  
Tau T2A, Tau T2D | 

  * Scale-out workloads
  * Web servers
  * Containerized microservices
  * Media transcoding
  * Large-scale Java applications

  
  
## C4D machine series

C4D VMs are powered by the fifth generation AMD EPYC Turin processor and [Titanium](https://cloud.google.com/titanium). C4D delivers a 30% performance boost over C3D on the estimated [SPECrate®2017_int_base benchmark](https://www.spec.org/cpu2017/), which lets you scale performance with fewer resources, thereby optimizing your costs.

C4D is designed to run workloads including web, app and game servers, AI inference, video streaming, and data centric applications like analytics, as well as relational and in-memory databases.

For databases, C4D delivers 55% more queries per second for MySQL and 35% higher operations per second for Memorystore for Redis workloads compared to C3D due to its higher core frequency (up to 4.1 GHz) and improved Instructions Per Clock (IPC).

**Note:** C4D doesn't support All Core Turbo Mode setting. C4D instances always run without frequency restrictions.

For web-serving workloads, AMD EPYC Turin's advancements in L3-cache efficiency and branch prediction enable up to 80% higher throughput per vCPU with C4D.

In summary, the C4D machine series has the following features:

  * Powered by the AMD EPYC Turin CPU and Titanium.
  * Supports up to 384 vCPUs and 3,024 GB of DDR5 memory.
  * Supports up to 12 TiB of local Titanium SSD disks.
  * Offers predefined machine types that range in size from 2 to 384 vCPUs.
  * Supports up to 3,024 GB of DDR5 memory for VM instances and up to 3,072 GB of memory for bare metal instances.
  * Supports consumption options like on-demand, Spot VMs, and future reservations.
  * Supports standard network configuration with up to 100 Gbps bandwidth.
  * Supports per VM Tier_1 networking performance with up to 200 Gbps bandwidth.
  * Supports only Hyperdisk volumes.
  * Supports [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) with AMD SEV, excluding bare metal instances and configurations with more than 255 vCPUs.
  * Supports [resource-based and flexible committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview).
  * Supports [compact and spread placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview).



### C4D machine types

C4D VMs are available as predefined configurations in `standard`, `highcpu`, and `highmem` sizes ranging from 2 vCPU to 384 vCPUs and up to 3,024 GB of memory.

To use Titanium SSD with C4D, create your instance using the `-lssd` variant of the C4D machine types. Selecting this machine type creates an instance of the specified size with Titanium SSD partitions attached. You can't attach Titanium SSD volumes separately.

To create a bare metal instance with C4D, use one of the following machine types:

  * `c4d-standard-384-metal`
  * `c4d-highcpu-384-metal`
  * `c4d-highmem-384-metal`



### C4D standard

Machine types | vCPUs1 | Memory (GB) | Titanium SSD | NUMA domains5 | Default egress bandwidth (Gbps)3 | Tier_1 egress bandwidth (Gbps)4  
---|---|---|---|---|---|---  
`c4d-standard-2` | 2 | 7 | No | 1 shared | Up to 10 | N/A  
`c4d-standard-4` | 4 | 15 | No | 1 shared | Up to 20 | N/A  
`c4d-standard-8` | 8 | 31 | No | 1 shared | Up to 20 | N/A  
`c4d-standard-16` | 16 | 62 | No | 1 shared | Up to 20 | N/A  
`c4d-standard-32` | 32 | 124 | No | 1 shared | Up to 23 | N/A  
`c4d-standard-48` | 48 | 186 | No | 1 shared | Up to 34 | Up to 50  
`c4d-standard-64` | 64 | 248 | No | 1 shared | Up to 45 | Up to 75  
`c4d-standard-96` | 96 | 372 | No | 1 shared | Up to 67 | Up to 100  
`c4d-standard-192` | 192 | 744 | No | 1 isolated | Up to 100 | Up to 150  
`c4d-standard-384` | 384 | 1,488 | No | 2 (full machine) | Up to 100 | Up to 200  
`c4d-standard-384-metal`2 | 384 | 1,536 | No | 2 (full machine) | Up to 100 | Up to 200  
  
1 A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).   
2 For bare metal instances, the number of vCPUs is equivalent to the number of hardware threads on the host server.  
3 Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
4 Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.  
5 The number of vNUMA nodes exposed to the guest OS.

### C4D highcpu

Machine types | vCPUs1 | Memory (GB) | Titanium SSD | NUMA domains5 | Default egress bandwidth (Gbps)3 | Tier_1 egress bandwidth (Gbps)4  
---|---|---|---|---|---|---  
`c4d-highcpu-2` | 2 | 3 | No | 1 shared | Up to 10 | N/A  
`c4d-highcpu-4` | 4 | 7 | No | 1 shared | Up to 20 | N/A  
`c4d-highcpu-8` | 8 | 15 | No | 1 shared | Up to 20 | N/A  
`c4d-highcpu-16` | 16 | 30 | No | 1 shared | Up to 20 | N/A  
`c4d-highcpu-32` | 32 | 60 | No | 1 shared | Up to 23 | N/A  
`c4d-highcpu-48` | 48 | 90 | No | 1 shared | Up to 34 | Up to 50  
`c4d-highcpu-64` | 64 | 120 | No | 1 shared | Up to 45 | Up to 75  
`c4d-highcpu-96` | 96 | 180 | No | 1 shared | Up to 67 | Up to 100  
`c4d-highcpu-192` | 192 | 360 | No | 1 isolated | Up to 100 | Up to 150  
`c4d-highcpu-384` | 384 | 720 | No | 2 (full machine) | Up to 100 | Up to 200  
`c4d-highcpu-384-metal`2 | 384 | 768 | No | 2 (full machine) | Up to 100 | Up to 200  
  
1 A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).   
2 For bare metal instances, the number of vCPUs is equivalent to the number of hardware threads on the host server.  
3 Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
4 Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.  
5 The number of vNUMA nodes exposed to the guest OS.

### C4D highmem

Machine types | vCPUs1 | Memory (GB) | Titanium SSD | NUMA domains5 | Default egress bandwidth (Gbps)3 | Tier_1 egress bandwidth (Gbps)4  
---|---|---|---|---|---|---  
`c4d-highmem-2` | 2 | 15 | No | 1 shared | Up to 10 | N/A  
`c4d-highmem-4` | 4 | 31 | No | 1 shared | Up to 20 | N/A  
`c4d-highmem-8` | 8 | 63 | No | 1 shared | Up to 20 | N/A  
`c4d-highmem-16` | 16 | 126 | No | 1 shared | Up to 20 | N/A  
`c4d-highmem-32` | 32 | 252 | No | 1 shared | Up to 23 | N/A  
`c4d-highmem-48` | 48 | 378 | No | 1 shared | Up to 34 | Up to 50  
`c4d-highmem-64` | 64 | 504 | No | 1 shared | Up to 45 | Up to 75  
`c4d-highmem-96` | 96 | 756 | No | 1 shared | Up to 67 | Up to 100  
`c4d-highmem-192` | 192 | 1,512 | No | 1 isolated | Up to 100 | Up to 150  
`c4d-highmem-384` | 384 | 3,024 | No | 2 (full machine) | Up to 100 | Up to 200  
`c4d-highmem-384-metal`2 | 384 | 3,072 | No | 2 (full machine) | Up to 100 | Up to 200  
  
1 A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).   
2 For bare metal instances, the number of vCPUs is equivalent to the number of hardware threads on the host server.  
3 Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
4 Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.  
5 The number of vNUMA nodes exposed to the guest OS.

### C4D standard

Machine types | vCPUs1 | Memory (GB) | Titanium SSD | NUMA domains5 | Default egress bandwidth (Gbps)3 | Tier_1 egress bandwidth (Gbps)4  
---|---|---|---|---|---|---  
`c4d-standard-8-lssd` | 8 | 31 | (1 x 375 GiB) 375 GiB | 1 shared | Up to 20 | N/A  
`c4d-standard-16-lssd` | 16 | 62 | (1 x 375 GiB) 375 GiB | 1 shared | Up to 20 | N/A  
`c4d-standard-32-lssd` | 32 | 124 | (2 x 375 GiB) 750 GiB | 1 shared | Up to 23 | N/A  
`c4d-standard-48-lssd` | 48 | 186 | (4 x 375 GiB) 1,500 GiB | 1 shared | Up to 34 | Up to 50  
`c4d-standard-64-lssd` | 64 | 248 | (6 x 375 GiB) 2,250 GiB | 1 shared | Up to 45 | Up to 75  
`c4d-standard-96-lssd` | 96 | 372 | (8 x 375 GiB) 3,000 GiB | 1 shared | Up to 67 | Up to 100  
`c4d-standard-192-lssd` | 192 | 744 | (16 x 375 GiB) 6,000 GiB | 1 isolated | Up to 100 | Up to 150  
`c4d-standard-384-lssd` | 384 | 1,488 | (32 x 375 GiB) 12,000 GiB | 2 (full machine) | Up to 100 | Up to 200  
  
1 A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).   
2 For bare metal instances, the number of vCPUs is equivalent to the number of hardware threads on the host server.  
3 Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
4 Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.  
5 The number of vNUMA nodes exposed to the guest OS.

### C4D highmem

Machine types | vCPUs1 | Memory (GB) | Titanium SSD | NUMA domains5 | Default egress bandwidth (Gbps)3 | Tier_1 egress bandwidth (Gbps)4  
---|---|---|---|---|---|---  
`c4d-highmem-8-lssd` | 8 | 63 | (1 x 375 GiB) 375 GiB | 1 shared | Up to 20 | N/A  
`c4d-highmem-16-lssd` | 16 | 126 | (1 x 375 GiB) 375 GiB | 1 shared | Up to 20 | N/A  
`c4d-highmem-32-lssd` | 32 | 252 | (2 x 375 GiB) 750 GiB | 1 shared | Up to 23 | N/A  
`c4d-highmem-48-lssd` | 48 | 378 | (4 x 375 GiB) 1,500 GiB | 1 shared | Up to 34 | Up to 50  
`c4d-highmem-64-lssd` | 64 | 504 | (6 x 375 GiB) 2,250 GiB | 1 shared | Up to 45 | Up to 75  
`c4d-highmem-96-lssd` | 96 | 756 | (8 x 375 GiB) 3,000 GiB | 1 shared | Up to 67 | Up to 100  
`c4d-highmem-192-lssd` | 192 | 1,512 | (16 x 375 GiB) 6,000 GiB | 1 isolated | Up to 100 | Up to 150  
`c4d-highmem-384-lssd` | 384 | 3,024 | (32 x 375 GiB) 12,000 GiB | 2 (full machine) | Up to 100 | Up to 200  
  
1 A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).   
2 For bare metal instances, the number of vCPUs is equivalent to the number of hardware threads on the host server.  
3 Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
4 Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.  
5 The number of vNUMA nodes exposed to the guest OS.

C4D doesn't support custom machine types.

### Regional availability for C4D instances

For C4D VMs, you can view the available regions and zones in the [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available) table, as follows:

  * To view all the zones where you can create a C4D VM, in the **Select a machine series** menu, select `C4D`.
  * You can also use the **Select a location** menu to limit the results to a geographical area.



For regional availability of C4D bare metal instances, see [Bare metal instances on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances#c4d-metal).

### Supported disk types for C4D

C4D VMs support only the NVMe disk interface and can use the following [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) block storage:

  * Hyperdisk Balanced (`hyperdisk-balanced`)
  * Hyperdisk Extreme (`hyperdisk-extreme`)
  * Hyperdisk Throughput (`hyperdisk-throughput`)
  * [Local Titanium SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd#local_ssd_types) (added automatically with `-lssd` machine types)



C4D doesn't support Persistent Disk.

#### Disk and capacity limits

You can attach a mixture of different Hyperdisk types to an instance, but the maximum total disk capacity (in TiB) across all disk types can't exceed: 

  * For machine types with less than 32 vCPUs: 257 TiB for all Hyperdisk

  * For machine types with 32 or more vCPUs: 512 TiB for all Hyperdisk




For details about the capacity limits, see [ Hyperdisk size and attachment limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance).

C4D storage limits are described in the following table:

### C4D standard

| Maximum number of disks |   
---|---|---  
Machine types | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme  
`c4d-standard-2` | 4 | 4 | 4 | 0 | 0  
`c4d-standard-4` | 8 | 8 | 8 | 0 | 0  
`c4d-standard-8` | 16 | 16 | 16 | 0 | 0  
`c4d-standard-16` | 32 | 32 | 32 | 0 | 0  
`c4d-standard-32` | 32 | 32 | 32 | 0 | 0  
`c4d-standard-48` | 32 | 32 | 32 | 0 | 0  
`c4d-standard-64` | 32 | 32 | 64 | 0 | 8  
`c4d-standard-96` | 32 | 32 | 64 | 0 | 8  
`c4d-standard-192` | 64 | 64 | 64 | 0 | 8  
`c4d-standard-384` | 128 | 128 | 128 | 0 | 8  
`c4d-standard-384-metal` | 128 | 128 | 8 | 0 | 8  
  
### C4D highcpu

| Maximum number of disks |   
---|---|---  
Machine types | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme  
`c4d-highcpu-2` | 4 | 4 | 4 | 0 | 0  
`c4d-highcpu-4` | 8 | 8 | 8 | 0 | 0  
`c4d-highcpu-8` | 16 | 16 | 16 | 0 | 0  
`c4d-highcpu-16` | 32 | 32 | 32 | 0 | 0  
`c4d-highcpu-32` | 32 | 32 | 32 | 0 | 0  
`c4d-highcpu-48` | 32 | 32 | 32 | 0 | 0  
`c4d-highcpu-64` | 32 | 32 | 64 | 0 | 8  
`c4d-highcpu-96` | 32 | 32 | 64 | 0 | 8  
`c4d-highcpu-192` | 64 | 64 | 64 | 0 | 8  
`c4d-highcpu-384` | 128 | 128 | 128 | 0 | 8  
`c4d-highcpu-384-metal` | 128 | 128 | 8 | 0 | 8  
  
### C4D highmem

| Maximum number of disks |   
---|---|---  
Machine types | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme  
`c4d-highmem-2` | 4 | 4 | 4 | 0 | 0  
`c4d-highmem-4` | 8 | 8 | 8 | 0 | 0  
`c4d-highmem-8` | 16 | 16 | 16 | 0 | 0  
`c4d-highmem-16` | 32 | 32 | 32 | 0 | 0  
`c4d-highmem-32` | 32 | 32 | 32 | 0 | 0  
`c4d-highmem-48` | 32 | 32 | 64 | 0 | 0  
`c4d-highmem-64` | 32 | 32 | 64 | 0 | 8  
`c4d-highmem-96` | 32 | 32 | 64 | 0 | 8  
`c4d-highmem-192` | 64 | 64 | 64 | 0 | 8  
`c4d-highmem-384` | 128 | 128 | 128 | 0 | 8  
`c4d-highmem-384-metal` | 128 | 128 | 8 | 0 | 8  
  
### C4D standard

| Maximum number of disks |   
---|---|---  
Machine types | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme  
`c4d-standard-8-lssd` | 16 | 16 | 16 | 0 | 0  
`c4d-standard-16-lssd` | 32 | 32 | 32 | 0 | 0  
`c4d-standard-32-lssd` | 32 | 32 | 32 | 0 | 0  
`c4d-standard-48-lssd` | 32 | 32 | 32 | 0 | 0  
`c4d-standard-64-lssd` | 32 | 32 | 64 | 0 | 8  
`c4d-standard-96-lssd` | 32 | 32 | 64 | 0 | 8  
`c4d-standard-192-lssd` | 64 | 64 | 64 | 0 | 8  
`c4d-standard-384-lssd` | 128 | 128 | 128 | 0 | 8  
  
### C4D highmem

| Maximum number of disks |   
---|---|---  
Machine types | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme  
`c4d-highmem-8-lssd` | 16 | 16 | 16 | 0 | 0  
`c4d-highmem-16-lssd` | 32 | 32 | 32 | 0 | 0  
`c4d-highmem-32-lssd` | 32 | 32 | 32 | 0 | 0  
`c4d-highmem-48-lssd` | 32 | 32 | 32 | 0 | 0  
`c4d-highmem-64-lssd` | 32 | 32 | 64 | 0 | 8  
`c4d-highmem-96-lssd` | 32 | 32 | 64 | 0 | 8  
`c4d-highmem-192-lssd` | 64 | 64 | 64 | 0 | 8  
`c4d-highmem-384-lssd` | 128 | 128 | 128 | 0 | 8  
  
### Network support for C4D instances

The following network interface drivers are required:

  * C4D VM instances require [gVNIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). 
  * C4D bare metal instances require the [Intel IDPF LAN PF device driver](https://docs.cloud.google.com/compute/docs/networking/using-idpf). 



C4D supports up to 100 Gbps network bandwidth for standard networking and up to 200 Gbps with per VM Tier_1 networking performance for VM and bare metal instances.

Before migrating to C4D or creating C4D VMs or bare metal instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the IDPF network driver for bare metal instances or the gVNIC driver for VM instances. To get the best possible performance on C4D VMs, choose an OS image that supports both "Tier_1 Networking" and "200 Gbps network bandwidth". These images include an updated gVNIC driver, even if the guest OS shows the `gve` driver version as 1.0.0. If your C4D VM is using an operating system with an older version of gVNIC driver, this is still supported but the VM might experience suboptimal performance such as less network bandwidth or higher latency.

If you use a custom OS image to create a C4D VM, you can [manually install the most recent gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup). The gVNIC driver version v1.4.2 or later is recommended for use with C4D VMs. Google recommends using the latest gVNIC driver version to benefit from additional features and bug fixes.

### Maintenance experience for C4D instances

During the lifespan of a virtual machine (VM) instance, the host machine that your instance runs undergoes multiple host events. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The C4D machine series offers the following features related to host maintenance:

Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance)  
---|---|---|---|---|---  
`c4d-*-lssd` | Minimum of 30 days | Live migrate | 7 days | Yes | Yes  
`c4d-*-384` | Minimum of 30 days | Live migrate | 7 days | Yes | Yes  
All others | Minimum of 30 days | Live migrate | 7 days | No | Yes  
  
The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## C4A machine series

C4A VMs are powered by Google's first Arm Axion™ processor. C4A provides machine types with up to 72 vCPUs and 576 GB of DDR5 memory, and 6 TiB of local [Titanium SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd#local_ssd_types). C4A is available in `standard`, `highmem`, and `highcpu` machine types. It also offers `-lssd` variants for Titanium SSD and a `highmem` bare metal machine type with 96 vCPUs and 768 GB of DDR5 memory. C4A uses Google Cloud's latest generation of Google Cloud Hyperdisk storage options and Titanium SSD. C4A offers up to 50 Gbps of standard network performance, and up to 100 Gbps per VM Tier_1 networking performance for your instances.

C4A VMs are placed within a single node with [Uniform Memory Access (UMA)](https://wikipedia.org/wiki/Uniform_memory_access) and also support sole tenant nodes to deliver consistent performance.

In summary, the C4A machine series has the following features:

  * Is powered by the Google Axion CPU and Titanium.
  * Supports multiple predefined machine types with up to 72 vCPUs and 576 GB of DDR5 memory.
  * Supports up to 6 TiB of local Titanium SSD disks.
  * Supports `highmem` bare metal instances with 96 vCPUs and 768 GB of DDR5 memory.
  * Supports standard network configuration with up to 50 Gbps bandwidth.
  * Supports per VM Tier_1 networking performance with up to 100 Gbps bandwidth.
  * Supports Hyperdisk only.
  * Supports the following discount and consumption options: 
    * [Resource-based and flexible committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)
    * [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
    * [Reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type)
  * Supports the [performance monitoring unit (PMU)](https://docs.cloud.google.com/compute/docs/pmu-overview).
  * Doesn't support [compact placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview).
  * Doesn't support [suspend](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance#suspend-instance-local-ssd) with C4A instances that have attached Titanium SSD disks.



For information about migrating to Arm VMs, read the [Arm on Compute](https://docs.cloud.google.com/compute/docs/instances/arm-on-compute) document.

### C4A machine types

**Note:** Community supported Arm OSes might be supported. If the OS isn't listed on the [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#networking) page, test the OS to learn if it is supported.

C4A VMs are available as predefined configurations in sizes ranging from 1 vCPU to 72 vCPUs and up to 576 GB of memory.

  * `standard`: 4 GB memory per vCPU
  * `highcpu`: 2 GB memory per vCPU
  * `highmem`: 8 GB memory per vCPU



To use Titanium SSD with C4A, create your VM using the `-lssd` variant of the C4A machine types. Selecting this machine type creates a VM of the specified size with Titanium SSD partitions attached. You can't attach Titanium SSD volumes separately.

You can create a bare metal instance with a `c4a-highmem-96-metal` machine type.

### C4A standard

Machine types | vCPUs1 | Memory (GB) | Titanium SSD | Default egress bandwidth (Gbps)2 | Tier_1 egress bandwidth (Gbps)3  
---|---|---|---|---|---  
`c4a-standard-1` | 1 | 4 | No | Up to 10 | N/A  
`c4a-standard-2` | 2 | 8 | No | Up to 10 | N/A  
`c4a-standard-4` | 4 | 16 | No | Up to 23 | N/A  
`c4a-standard-8` | 8 | 32 | No | Up to 23 | N/A  
`c4a-standard-16` | 16 | 64 | No | Up to 23 | N/A  
`c4a-standard-32` | 32 | 128 | No | Up to 23 | Up to 50  
`c4a-standard-48` | 48 | 192 | No | Up to 34 | Up to 50  
`c4a-standard-64` | 64 | 256 | No | Up to 45 | Up to 75  
`c4a-standard-72` | 72 | 288 | No | Up to 50 | Up to 100  
  
1 SMT is not supported. Each vCPU is equivalent to an entire core. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3 Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. 

### C4A highcpu

Machine types | vCPUs1 | Memory (GB) | Titanium SSD | Default egress bandwidth (Gbps)2 | Tier_1 egress bandwidth (Gbps)3  
---|---|---|---|---|---  
`c4a-highcpu-1` | 1 | 2 | No | Up to 10 | N/A  
`c4a-highcpu-2` | 2 | 4 | No | Up to 10 | N/A  
`c4a-highcpu-4` | 4 | 8 | No | Up to 23 | N/A  
`c4a-highcpu-8` | 8 | 16 | No | Up to 23 | N/A  
`c4a-highcpu-16` | 16 | 32 | No | Up to 23 | N/A  
`c4a-highcpu-32` | 32 | 64 | No | Up to 23 | Up to 50  
`c4a-highcpu-48` | 48 | 96 | No | Up to 34 | Up to 50  
`c4a-highcpu-64` | 64 | 128 | No | Up to 45 | Up to 75  
`c4a-highcpu-72` | 72 | 144 | No | Up to 50 | Up to 100  
  
1 SMT is not supported. Each vCPU is equivalent to an entire core. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3 Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. 

### C4A highmem

Machine types | vCPUs1 | Memory (GB) | Titanium SSD | Default egress bandwidth (Gbps)2 | Tier_1 egress bandwidth (Gbps)3  
---|---|---|---|---|---  
`c4a-highmem-1` | 1 | 8 | No | Up to 10 | N/A  
`c4a-highmem-2` | 2 | 16 | No | Up to 10 | N/A  
`c4a-highmem-4` | 4 | 32 | No | Up to 23 | N/A  
`c4a-highmem-8` | 8 | 64 | No | Up to 23 | N/A  
`c4a-highmem-16` | 16 | 128 | No | Up to 23 | N/A  
`c4a-highmem-32` | 32 | 256 | No | Up to 23 | Up to 50  
`c4a-highmem-48` | 48 | 384 | No | Up to 34 | Up to 50  
`c4a-highmem-64` | 64 | 512 | No | Up to 45 | Up to 75  
`c4a-highmem-72` | 72 | 576 | No | Up to 50 | Up to 100  
`c4a-highmem-96-metal` | 96 | 768 | No | Up to 50 | Up to 100  
  
1 SMT is not supported. Each vCPU is equivalent to an entire core. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3 Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. 

### C4A standard

Machine types | vCPUs1 | Memory (GB) | Titanium SSD | Default egress bandwidth (Gbps)2 | Tier_1 egress bandwidth (Gbps)3  
---|---|---|---|---|---  
`c4a-standard-4-lssd` | 4 | 16 | (1 x 375 GiB) 375 GiB | Up to 23 | N/A  
`c4a-standard-8-lssd` | 8 | 32 | (2 x 375 GiB) 750 GiB | Up to 23 | N/A  
`c4a-standard-16-lssd` | 16 | 64 | (4 x 375 GiB) 1,500 GiB | Up to 23 | N/A  
`c4a-standard-32-lssd` | 32 | 128 | (6 x 375 GiB) 2,250 GiB | Up to 23 | Up to 50  
`c4a-standard-48-lssd` | 48 | 192 | (10 x 375 GiB) 3,750 GiB | Up to 34 | Up to 50  
`c4a-standard-64-lssd` | 64 | 256 | (14 x 375 GiB) 5,250 GiB | Up to 45 | Up to 75  
`c4a-standard-72-lssd` | 72 | 288 | (16 x 375 GiB) 6,000 GiB | Up to 50 | Up to 100  
  
1 SMT is not supported. Each vCPU is equivalent to an entire core. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3 Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. 

### C4A highmem

Machine types | vCPUs* | Memory (GB) | Titanium SSD | Default egress bandwidth (Gbps)‡ | Tier_1 egress bandwidth (Gbps)#  
---|---|---|---|---|---  
`c4a-highmem-4-lssd` | 4 | 32 | (1 x 375 GiB) 375 GiB | Up to 23 | N/A  
`c4a-highmem-8-lssd` | 8 | 64 | (2 x 375 GiB) 750 GiB | Up to 23 | N/A  
`c4a-highmem-16-lssd` | 16 | 128 | (4 x 375 GiB) 1,500 GiB | Up to 23 | N/A  
`c4a-highmem-32-lssd` | 32 | 256 | (6 x 375 GiB) 2,250 GiB | Up to 23 | Up to 50  
`c4a-highmem-48-lssd` | 48 | 384 | (10 x 375 GiB) 3,750 GiB | Up to 34 | Up to 50  
`c4a-highmem-64-lssd` | 64 | 512 | (14 x 375 GiB) 5,250 GiB | Up to 45 | Up to 75  
`c4a-highmem-72-lssd` | 72 | 576 | (16 x 375 GiB) 6,000 GiB | Up to 50 | Up to 100  
  
1 SMT is not supported. Each vCPU is equivalent to an entire core. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3 Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. 

C4A doesn't support custom machine types.

### Supported disk types for C4A

C4A VMs support only the NVMe disk interface and can use the following [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) block storage:

###  VM instances 

  * Hyperdisk Balanced (`hyperdisk-balanced`)
  * Hyperdisk Balanced High Availability (`hyperdisk-balanced-high-availability`)
  * Hyperdisk Throughput (`hyperdisk-throughput`)
  * Hyperdisk Extreme (`hyperdisk-extreme`)
  * Hyperdisk ML (`hyperdisk-ML`)
  * [Local Titanium SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd#local_ssd_types) (only available with `-lssd` machine types)



###  Bare metal instances 

  * Hyperdisk Balanced (`hyperdisk-balanced`)
  * Hyperdisk Extreme (`hyperdisk-extreme`)
  * Hyperdisk ML (`hyperdisk-ML`)



C4A doesn't support Persistent Disk.

#### Disk and capacity limits

You can attach a mixture of different Hyperdisk types to an instance, but the maximum total disk capacity (in TiB) across all disk types can't exceed: 

  * For machine types with less than 32 vCPUs: 257 TiB for all Hyperdisk

  * For machine types with 32 or more vCPUs: 512 TiB for all Hyperdisk




For details about the capacity limits, see [ Hyperdisk size and attachment limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance).

### C4A standard

Maximum number of disks  
---  
Machine types | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme | Hyperdisk ML  
`c4a-standard-1` | 16 | 16 | 16 | 16 | 0 | 16  
`c4a-standard-2` | 16 | 16 | 16 | 16 | 0 | 16  
`c4a-standard-4` | 16 | 16 | 16 | 16 | 0 | 16  
`c4a-standard-8` | 16 | 16 | 16 | 16 | 0 | 16  
`c4a-standard-16` | 32 | 32 | 32 | 32 | 0 | 32  
`c4a-standard-32` | 32 | 32 | 32 | 32 | 0 | 32  
`c4a-standard-48` | 32 | 32 | 32 | 32 | 0 | 32  
`c4a-standard-64` | 64 | 64 | 64 | 64 | 8 | 64  
`c4a-standard-72` | 64 | 64 | 64 | 64 | 8 | 64  
  
### C4A highcpu

Maximum number of disks  
---  
Machine types | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme | Hyperdisk ML  
`c4a-highcpu-1` | 16 | 16 | 16 | 16 | 0 | 16  
`c4a-highcpu-2` | 16 | 16 | 16 | 16 | 0 | 16  
`c4a-highcpu-4` | 16 | 16 | 16 | 16 | 0 | 16  
`c4a-highcpu-8` | 16 | 16 | 16 | 16 | 0 | 16  
`c4a-highcpu-16` | 32 | 32 | 32 | 32 | 0 | 32  
`c4a-highcpu-32` | 32 | 32 | 32 | 32 | 0 | 32  
`c4a-highcpu-48` | 32 | 32 | 32 | 32 | 0 | 32  
`c4a-highcpu-64` | 64 | 64 | 64 | 64 | 8 | 64  
`c4a-highcpu-72` | 64 | 64 | 64 | 64 | 8 | 64  
  
### C4A highmem

Maximum number of disks  
---  
Machine types | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme | Hyperdisk ML  
`c4a-highmem-1` | 16 | 8 | 16 | 16 | 0 | 16  
`c4a-highmem-2` | 16 | 8 | 16 | 16 | 0 | 16  
`c4a-highmem-4` | 16 | 16 | 16 | 16 | 0 | 16  
`c4a-highmem-8` | 16 | 16 | 16 | 16 | 0 | 16  
`c4a-highmem-16` | 32 | 32 | 32 | 32 | 0 | 32  
`c4a-highmem-32` | 32 | 32 | 32 | 32 | 0 | 32  
`c4a-highmem-48` | 32 | 32 | 32 | 32 | 0 | 32  
`c4a-highmem-64` | 64 | 64 | 64 | 64 | 8 | 64  
`c4a-highmem-72` | 64 | 64 | 64 | 64 | 8 | 64  
`c4a-highmem-96-metal` | 128 | 128 | Not supported | Not supported | 8 | 32  
  
### C4A standard

Maximum number of disks  
---  
Machine types | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme | Hyperdisk ML  
`c4a-standard-4-lssd` | 16 | 16 | 16 | 16 | 0 | 16  
`c4a-standard-8-lssd` | 16 | 16 | 16 | 16 | 0 | 16  
`c4a-standard-16-lssd` | 32 | 32 | 32 | 32 | 0 | 32  
`c4a-standard-32-lssd` | 32 | 32 | 32 | 32 | 0 | 32  
`c4a-standard-48-lssd` | 32 | 32 | 32 | 32 | 0 | 32  
`c4a-standard-64-lssd` | 64 | 64 | 64 | 64 | 8 | 64  
`c4a-standard-72-lssd` | 64 | 64 | 64 | 64 | 8 | 64  
  
### C4A highmem

Maximum number of disks  
---  
Machine types | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme | Hyperdisk ML  
`c4a-highmem-4-lssd` | 16 | 16 | 16 | 16 | 0 | 16  
`c4a-highmem-8-lssd` | 16 | 16 | 16 | 16 | 0 | 16  
`c4a-highmem-16-lssd` | 32 | 32 | 32 | 32 | 0 | 32  
`c4a-highmem-32-lssd` | 32 | 32 | 32 | 32 | 0 | 32  
`c4a-highmem-48-lssd` | 32 | 32 | 32 | 32 | 0 | 32  
`c4a-highmem-64-lssd` | 64 | 64 | 64 | 64 | 8 | 64  
`c4a-highmem-72-lssd` | 64 | 64 | 64 | 64 | 8 | 64  
  
### Network support for C4A instances

The following network interface drivers are required:

  * C4A VM instances require [gVNIC network interfaces](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). 
  * C4A bare metal instances require the [Intel IDPF LAN PF device driver](https://docs.cloud.google.com/compute/docs/networking/using-idpf). 



C4A supports up to 100 Gbps network bandwidth for standard networking and bare metal instances.

Before migrating to C4A or creating C4A VMs or bare metal instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the IDPF network driver for bare metal instances or the gVNIC driver for VM instances. To get the best possible performance on C4A VMs, choose an OS image that supports both "Tier_1 Networking" and "100 Gbps network bandwidth". These images include an updated gVNIC driver, even if the guest OS shows the `gve` driver version as 1.0.0. If your C4A VM is using an operating system with an older version of gVNIC driver, this is still supported but the VM might experience suboptimal performance such as less network bandwidth or higher latency.

If you use a custom OS image to create a C4A VM, you can [manually install the most recent gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup). The gVNIC driver version v1.4.2 or later is recommended for use with C4A VMs. Google recommends using the latest gVNIC driver version to benefit from additional features and bug fixes.

### Maintenance experience for C4A instances

During the lifespan of a virtual machine (VM) instance, the host machine that your instance runs undergoes multiple host events. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The C4A machine series offers the following features related to host maintenance:

Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event)  
---|---|---|---|---  
`c4a-*-lssd` | Minimum of 30 days | Live migrate | 7 days | Yes  
`c4a-*-metal` | Minimum of 30 days | Terminate | 7 days | Yes  
All others | Minimum of 30 days | Live migrate | 7 days | No  
  
The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## C4 machine series

C4 VMs are powered by 6th generation (code-named Granite Rapids) or 5th generation (code-named Emerald Rapids) Intel Xeon Scalable processors and [Titanium](https://cloud.google.com/titanium). C4 Local SSD (`-lssd`) and bare metal (`-metal`) instances, as well as instances with 144 or 288 vCPUs, use the 6th generation Intel Granite Rapids processor. All other instances use the 5th generation Intel Emerald Rapids processor.

The C4 machine series is designed to deliver price-performance and enterprise-grade reliability along with a maintenance experience for your most demanding workloads. C4 instances are ideal for web and app serving, game servers, databases and caches, video streaming, data analytics, network appliances, and CPU-based ML inference.

C4 VMs are designed to achieve maximum performance from single-core turbo boosting. For more consistent vCPU performance, disable vCPU boosting and limit the vCPUs to the sustainable all-core turbo frequency. You can do this by setting `turboMode=ALL_CORE_MAX` in the [AdvancedMachineFeatures](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) settings.

In summary, the C4 machine series:

  * Is powered by the 6th generation Intel Granite Rapids or 5th generation Intel Emerald Rapids processor and Titanium IPU.
  * Lets you switch between core-boosting performance and steady all-core turbo performance for your vCPUs.
  * Supports up to 288 vCPUs and 2.2 TB of DDR5 memory.
  * Supports up to 18 TiB of local Titanium SSD disks.
  * Supports compact and spread placement policies.
  * Offers multiple predefined machine types.
  * Supports standard network configuration with up to 100 Gbps bandwidth.
  * Supports per VM Tier_1 networking performance with up to 200 Gbps bandwidth.
  * Supports [Intel Advanced Matrix Extensions (AMX)](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel-amx), a built-in accelerator that significantly improves the performance of deep-learning training and inference on the CPU.
  * Supports the following discount and consumption options: 
    * [Resource-based and flexible committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)
    * [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
    * [Reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type)
  * Supports the [performance monitoring unit (PMU)](https://docs.cloud.google.com/compute/docs/pmu-overview).
  * Supports up to 192 vCPUs for [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) with Intel TDX using Granite Rapids processors. Intel TDX support isn't available on Emerald Rapids processors.



### C4 Limitations

  * You can't dynamically add or remove a disk when using Windows Server 25.
  * You can't dynamically add or remove multiple disks when using Windows Server 25 or Windows 11.
  * C4 VM shapes powered by Granite Rapids might experience lower networking performance on Windows 11 and Debian 11 [OS images](https://docs.cloud.google.com/compute/docs/images).



### C4 machine types

C4 VMs are available as predefined configurations in sizes ranging from 2 vCPUs to 288 vCPUs and up to 2,232 GB of memory.

  * `standard`: 3.75 GB memory per vCPU
  * `highcpu`: 2 GB memory per vCPU
  * `highmem`: 7.75 GB memory per vCPU



To use Titanium SSD with C4, create your instance using the `-lssd` variant of the C4 machine types. Selecting this machine type creates an instance of the specified size with Titanium SSD partitions attached. You can't attach Titanium SSD volumes separately.

To create a bare metal instance with C4, use one of the following machine types:

  * `c4-standard-288-metal`
  * `c4-standard-288-lssd-metal`
  * `c4-highmem-288-metal`
  * `c4-highmem-288-lssd-metal`



The maximum number of NUMA nodes for C4 running on the Emerald Rapids CPU platform is 4. For the Granite Rapids CPU platform, the maximum number of NUMA nodes is 6."

### C4 standard

Machine types | vCPUs1 | Memory (GB) | Titanium SSD | NUMA domains4 | Default egress bandwidth (Gbps)2 | Tier_1 egress bandwidth (Gbps)3  
---|---|---|---|---|---|---  
`c4-standard-2` | 2 | 7 | No | 1 shared | Up to 10 | N/A  
`c4-standard-4` | 4 | 15 | No | 1 shared | Up to 23 | N/A  
`c4-standard-8` | 8 | 30 | No | 1 shared | Up to 23 | N/A  
`c4-standard-16` | 16 | 60 | No | 1 shared | Up to 23 | N/A  
`c4-standard-24` | 24 | 90 | No | 1 shared | Up to 23 | N/A  
`c4-standard-32` | 32 | 120 | No | 1 shared | Up to 23 | N/A  
`c4-standard-48` | 48 | 180 | No | 1 isolated | Up to 34 | Up to 50  
`c4-standard-96` | 96 | 360 | No | 2 isolated | Up to 67 | Up to 100  
`c4-standard-144` | 144 | 540 | No | 3 isolated | Up to 100 | Up to 150  
`c4-standard-192` | 192 | 720 | No | 4 (full machine on EMR, not on GNR5) | Up to 100 | Up to 200  
`c4-standard-288` | 288 | 1,080 | No | 6 (full machine) | Up to 100 | Up to 200  
`c4-standard-288-metal` | 288 | 1,080 | No | 6 (full machine on GNR5) | Up to 100 | Up to 200  
  
1 A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3 Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.  
4 The "NUMA domains" column in the tables shows the number of vNUMA nodes exposed to the guest OS.  
5 GNR stands for Granite Rapids, Intel's 6th generation Xeon Scalable processor. EMR stands for Emerald Rapids, Intel's 5th generation Xeon Scalable processor.

### C4 highcpu

Machine types | vCPUs1 | Memory (GB) | Titanium SSD | NUMA domains4 | Default egress bandwidth (Gbps)2 | Tier_1 egress bandwidth (Gbps)3  
---|---|---|---|---|---|---  
`c4-highcpu-2` | 2 | 4 | No | 1 shared | Up to 10 | N/A  
`c4-highcpu-4` | 4 | 8 | No | 1 shared | Up to 23 | N/A  
`c4-highcpu-8` | 8 | 16 | No | 1 shared | Up to 23 | N/A  
`c4-highcpu-16` | 16 | 32 | No | 1 shared | Up to 23 | N/A  
`c4-highcpu-24` | 24 | 48 | No | 1 shared | Up to 23 | N/A  
`c4-highcpu-32` | 32 | 64 | No | 1 shared | Up to 23 | N/A  
`c4-highcpu-48` | 48 | 96 | No | 1 isolated | Up to 34 | Up to 50  
`c4-highcpu-96` | 96 | 192 | No | 2 isolated | Up to 67 | Up to 100  
`c4-highcpu-144` | 144 | 288 | No | 3 isolated | Up to 100 | Up to 150  
`c4-highcpu-192` | 192 | 384 | No | 4 (full machine on EMR, not on GMR5) | Up to 100 | Up to 200  
`c4-highcpu-288` | 288 | 576 | No | 6 (full machine) | Up to 100 | Up to 200  
  
1 A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3 Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.  
4 The "NUMA domains" column in the tables shows the number of vNUMA nodes exposed to the guest OS.  
5 GNR stands for Granite Rapids, Intel's 6th generation Xeon Scalable processor. EMR stands for Emerald Rapids, Intel's 5th generation Xeon Scalable processor.

### C4 highmem

Machine types | vCPUs1 | Memory (GB) | Titanium SSD | NUMA domains4 | Default egress bandwidth (Gbps)2 | Tier_1 egress bandwidth (Gbps)3  
---|---|---|---|---|---|---  
`c4-highmem-2` | 2 | 15 | No | 1 shared | Up to 10 | N/A  
`c4-highmem-4` | 4 | 31 | No | 1 shared | Up to 23 | N/A  
`c4-highmem-8` | 8 | 62 | No | 1 shared | Up to 23 | N/A  
`c4-highmem-16` | 16 | 124 | No | 1 shared | Up to 23 | N/A  
`c4-highmem-24` | 24 | 186 | No | 1 shared | Up to 23 | N/A  
`c4-highmem-32` | 32 | 248 | No | 1 shared | Up to 23 | N/A  
`c4-highmem-48` | 48 | 372 | No | 1 isolated | Up to 34 | Up to 50  
`c4-highmem-96` | 96 | 744 | No | 2 isolated | Up to 67 | Up to 100  
`c4-highmem-144` | 144 | 1,116 | No | 3 isolated | Up to 100 | Up to 150  
`c4-highmem-192` | 192 | 1,488 | No | 4 (full machine on EMR, not on GNR5) | Up to 100 | Up to 200  
`c4-highmem-288` | 288 | 2,232 | No | 6 (full machine) | Up to 100 | Up to 200  
`c4-highmem-288-metal` | 288 | 2,232 | No | 6 (full machine) | Up to 100 | Up to 200  
  
1 A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3 Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.  
4 The "NUMA domains" column in the tables shows the number of vNUMA nodes exposed to the guest OS.  
5 GNR stands for Granite Rapids, Intel's 6th generation Xeon Scalable processor. EMR stands for Emerald Rapids, Intel's 5th generation Xeon Scalable processor.

### C4 standard

Machine types | vCPUs1 | Memory (GB) | Titanium SSD | NUMA domains4 | Default egress bandwidth (Gbps)2 | Tier_1 egress bandwidth (Gbps)3  
---|---|---|---|---|---|---  
`c4-standard-4-lssd` | 4 | 15 | (1 x 375 GiB) 375 GiB | 1 shared | Up to 23 | N/A  
`c4-standard-8-lssd` | 8 | 30 | (1 x 375 GiB) 375 GiB | 1 shared | Up to 23 | N/A  
`c4-standard-16-lssd` | 16 | 60 | (2 x 375 GiB) 750 GiB | 1 shared | Up to 23 | N/A  
`c4-standard-24-lssd` | 24 | 90 | (4 x 375 GiB) 1,500 GiB | 1 shared | Up to 23 | N/A  
`c4-standard-32-lssd` | 32 | 120 | (5 x 375 GiB) 1,875 GiB | 1 shared | Up to 23 | N/A  
`c4-standard-48-lssd` | 48 | 180 | (8 x 375 GiB) 3,000 GiB | 1 isolated | Up to 34 | N/A  
`c4-standard-96-lssd` | 96 | 360 | (16 x 375 GiB) 6,000 GiB | 2 isolated | Up to 67 | N/A  
`c4-standard-144-lssd` | 144 | 540 | (24 x 375 GiB) 9,000 GiB | 3 isolated | Up to 100 | N/A  
`c4-standard-192-lssd` | 192 | 720 | (32 x 375 GiB) 12,000 GiB | 4 isolated | Up to 100 | N/A  
`c4-standard-288-lssd` | 288 | 1,080 | (48 x 375 GiB) 18,000 GiB | 6 (full machine) | Up to 100 | Up to 200  
`c4-standard-288-lssd-metal` | 288 | 1,080 | (6 x 3,000 GiB) 18,000 GiB | 6 (full machine) | Up to 100 | Up to 200  
  
1 A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3 Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.  
4 The "NUMA domains" column in the tables shows the number of vNUMA nodes exposed to the guest OS.  
5 GNR stands for Granite Rapids, Intel's 6th generation Xeon Scalable processor. EMR stands for Emerald Rapids, Intel's 5th generation Xeon Scalable processor.

### C4 highmem

Machine types | vCPUs1 | Memory (GB) | Titanium SSD | NUMA domains4 | Default egress bandwidth (Gbps)2 | Tier_1 egress bandwidth (Gbps)3  
---|---|---|---|---|---|---  
`c4-highmem-4-lssd` | 4 | 31 | (1 x 375 GiB) 375 GiB | 1 shared | Up to 23 | N/A  
`c4-highmem-8-lssd` | 8 | 62 | (1 x 375 GiB) 375 GiB | 1 shared | Up to 23 | N/A  
`c4-highmem-16-lssd` | 16 | 124 | (2 x 375 GiB) 750 GiB | 1 shared | Up to 23 | N/A  
`c4-highmem-24-lssd` | 24 | 186 | (4 x 375 GiB) 1,500 GiB | 1 shared | Up to 23 | N/A  
`c4-highmem-32-lssd` | 32 | 248 | (5 x 375 GiB) 1,875 GiB | 1 shared | Up to 23 | N/A  
`c4-highmem-48-lssd` | 48 | 372 | (8 x 375 GiB) 3,000 GiB | 1 isolated | Up to 34 | N/A  
`c4-highmem-96-lssd` | 96 | 744 | (16 x 375 GiB) 6,000 GiB | 2 isolated | Up to 67 | N/A  
`c4-highmem-144-lssd` | 144 | 1,116 | (24 x 375 GiB) 9,000 GiB | 3 isolated | Up to 100 | N/A  
`c4-highmem-192-lssd` | 192 | 1,488 | (32 x 375 GiB) 12,000 GiB | 4 isolated | Up to 100 | N/A  
`c4-highmem-288-lssd` | 288 | 2,232 | (48 x 375 GiB) 18,000 GiB | 6 (full machine) | Up to 100 | Up to 200  
`c4-highmem-288-lssd-metal` | 288 | 2,232 | (6 x 3,000 GiB) 18,000 GiB | 6 (full machine) | Up to 100 | Up to 200  
  
1 A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3 Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.  
4 The "NUMA domains" column in the tables shows the number of vNUMA nodes exposed to the guest OS.  
5 GNR stands for Granite Rapids, Intel's 6th generation Xeon Scalable processor. EMR stands for Emerald Rapids, Intel's 5th generation Xeon Scalable processor.

C4 doesn't support custom machine types.

### Supported disk types for C4

C4 VMs support only the NVMe disk interface and can use the following [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) block storage:

###  VM instances 

  * Hyperdisk Balanced (`hyperdisk-balanced`)
  * Hyperdisk Balanced High Availability (`hyperdisk-balanced-high-availability`)
  * Hyperdisk Throughput (`hyperdisk-throughput`)
  * Hyperdisk Extreme (`hyperdisk-extreme`)
  * Local SSD (only available with `-lssd` machine types)



###  Bare metal instances 

  * Hyperdisk Balanced (`hyperdisk-balanced`)
  * Hyperdisk Extreme (`hyperdisk-extreme`)
  * Local SSD (only available with `-lssd-metal` machine types)



C4 doesn't support Persistent Disk. When upgrading to a newer machine series, to migrate your Persistent Disk resources to Hyperdisk, see [Move your workload from an existing VM to a new VM](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm).

#### Disk and capacity limits

You can attach a mixture of different Hyperdisk types to an instance, but the maximum total disk capacity (in TiB) across all disk types can't exceed: 

  * For machine types with less than 32 vCPUs: 257 TiB for all Hyperdisk

  * For machine types with 32 or more vCPUs: 512 TiB for all Hyperdisk




For details about the capacity limits, see [ Hyperdisk size and attachment limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance).

### C4 standard

| Maximum number of disks |   
---|---|---  
Machine types | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme  
`c4-standard-2` | 8 | 8 | 8 | 8 | 0  
`c4-standard-4` | 16 | 16 | 16 | 16 | 0  
`c4-standard-8` | 32 | 32 | 32 | 32 | 0  
`c4-standard-16` | 32 | 32 | 32 | 32 | 0  
`c4-standard-24` | 32 | 32 | 32 | 32 | 0  
`c4-standard-32` | 64 | 64 | 32 | 64 | 0  
`c4-standard-48` | 64 | 64 | 32 | 64 | 0  
`c4-standard-96` | 128 | 128 | 64 | 128 | 8  
`c4-standard-144` | 128 | 128 | 64 | 128 | 8  
`c4-standard-192` | 128 | 128 | 128 | 128 | 8  
`c4-standard-288` | 128 | 128 | 128 | 128 | 8  
`c4-standard-288-metal` | 128 | 128 | Not supported | Not supported | 8  
  
### C4 highcpu

| Maximum number of disks |   
---|---|---  
Machine types | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme  
`c4-highcpu-2` | 8 | 8 | 8 | 8 | 0  
`c4-highcpu-4` | 16 | 16 | 16 | 16 | 0  
`c4-highcpu-8` | 32 | 32 | 32 | 32 | 0  
`c4-highcpu-16` | 32 | 32 | 32 | 32 | 0  
`c4-highcpu-24` | 32 | 32 | 32 | 32 | 0  
`c4-highcpu-32` | 64 | 64 | 32 | 64 | 0  
`c4-highcpu-48` | 64 | 64 | 32 | 64 | 0  
`c4-highcpu-96` | 128 | 128 | 64 | 128 | 8  
`c4-highcpu-144` | 128 | 128 | 64 | 128 | 8  
`c4-highcpu-192` | 128 | 128 | 128 | 128 | 8  
`c4-highcpu-288` | 128 | 128 | 128 | 128 | 8  
  
### C4 highmem

| Maximum number of disks |   
---|---|---  
Machine types | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme  
`c4-highmem-2` | 8 | 8 | 8 | 8 | 0  
`c4-highmem-4` | 16 | 16 | 16 | 16 | 0  
`c4-highmem-8` | 32 | 32 | 32 | 32 | 0  
`c4-highmem-16` | 32 | 32 | 32 | 32 | 0  
`c4-highmem-24` | 32 | 32 | 32 | 32 | 0  
`c4-highmem-32` | 64 | 64 | 32 | 64 | 0  
`c4-highmem-48` | 64 | 64 | 32 | 64 | 0  
`c4-highmem-96` | 128 | 128 | 64 | 128 | 8  
`c4-highmem-144` | 128 | 128 | 64 | 128 | 8  
`c4-highmem-192` | 128 | 128 | 128 | 128 | 8  
`c4-highmem-288` | 128 | 128 | 128 | 128 | 8  
`c4-highmem-288-metal` | 128 | 128 | Not supported | Not supported | 8  
  
### C4 standard

| Maximum number of disks |   
---|---|---  
Machine types | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme  
`c4-standard-4-lssd` | 16 | 16 | 16 | 16 | 0  
`c4-standard-8-lssd` | 32 | 32 | 32 | 32 | 0  
`c4-standard-16-lssd` | 32 | 32 | 32 | 32 | 0  
`c4-standard-24-lssd` | 32 | 32 | 32 | 32 | 0  
`c4-standard-32-lssd` | 32 | 32 | 32 | 32 | 0  
`c4-standard-48-lssd` | 32 | 32 | 32 | 32 | 0  
`c4-standard-96-lssd` | 64 | 64 | 64 | 64 | 8  
`c4-standard-144-lssd` | 64 | 64 | 64 | 64 | 8  
`c4-standard-192-lssd` | 128 | 128 | 128 | 128 | 8  
`c4-standard-288-lssd` | 128 | 128 | 128 | 128 | 8  
`c4-standard-288-lssd-metal` | 128 | 128 | Not supported | Not supported | 8  
  
### C4 highmem

| Maximum number of disks |   
---|---|---  
Machine types | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput | Hyperdisk Extreme  
`c4-highmem-4-lssd` | 16 | 16 | 16 | 16 | 0  
`c4-highmem-8-lssd` | 32 | 32 | 32 | 32 | 0  
`c4-highmem-16-lssd` | 32 | 32 | 32 | 32 | 0  
`c4-highmem-24-lssd` | 32 | 32 | 32 | 32 | 0  
`c4-highmem-32-lssd` | 32 | 32 | 32 | 32 | 0  
`c4-highmem-48-lssd` | 32 | 32 | 32 | 32 | 0  
`c4-highmem-96-lssd` | 64 | 64 | 64 | 64 | 8  
`c4-highmem-144-lssd` | 64 | 64 | 64 | 64 | 8  
`c4-highmem-192-lssd` | 128 | 128 | 128 | 128 | 8  
`c4-highmem-288-lssd` | 128 | 128 | 128 | 128 | 8  
`c4-highmem-288-lssd-metal` | 128 | 128 | Not supported | Not supported | 8  
  
### Network support for C4 VMs

The following network interface drivers are required:

  * C4 VM instances require [gVNIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). 
  * C4 bare metal instances require the [Intel IDPF LAN PF device driver](https://docs.cloud.google.com/compute/docs/networking/using-idpf). 



C4 supports up to 100 Gbps network bandwidth for standard networking and up to 200 Gbps with per VM Tier_1 networking performance for VM and bare metal instances.

Before migrating to C4 or creating C4 VMs or bare metal instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the IDPF network driver for bare metal instances or the gVNIC driver for VM instances. To get the best possible performance on C4 VMs, choose an OS image that supports both "Tier_1 Networking" and "200 Gbps network bandwidth". These images include an updated gVNIC driver, even if the guest OS shows the `gve` driver version as 1.0.0. If your C4 VM is using an operating system with an older version of gVNIC driver, this is still supported but the VM might experience suboptimal performance such as less network bandwidth or higher latency.

If you use a custom OS image to create a C4 VM, you can [manually install the most recent gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup). The gVNIC driver version v1.4.2 or later is recommended for use with C4 VMs. Google recommends using the latest gVNIC driver version to benefit from additional features and bug fixes.

### Maintenance experience for C4 instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple _host events_. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The C4 machine series offers the following features related to host maintenance:

Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event)  
---|---|---|---|---  
`c4-*-192` and `c4-*-288` | Minimum of 30 days | Live migrate | 7 days | Yes  
`c4-*-lssd` | Minimum of 30 days | Live migrate | 7 days | Yes  
`c4-*-288-metal` | Minimum of 30 days | Terminate | 7 days | Yes  
`c4-*-288-lssd-metal` | Minimum of 30 days | Terminate | 7 days | Yes  
All others | Minimum of 30 days | Live migrate | 7 days | No  
  
The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## N4D machine series

N4D VMs are powered by the fifth generation AMD EPYC processors (code-name Turin) and [Titanium](https://docs.cloud.google.com/titanium). N4D VMs are engineered for flexibility, cost optimization, and enhanced price-performance through their efficient architecture. N4D supports next generation dynamic resource management, making better use of resources on host machines.

In summary, the N4D machine series:

  * Powered by the AMD EPYC Turin CPU and Titanium.
  * Supports up to 96 vCPUs and 768 GB of DDR5 memory.
  * Offers predefined machine types that range in size from 2 to 96 vCPUs.
  * Supports custom machine types and extended memory.
  * Supports consumption options like on-demand, Spot VMs, and future reservations.
  * Supports standard network configuration with up to 50 Gbps bandwidth.
  * Supports only Hyperdisk volumes.
  * Supports resource-based and flexible committed use discounts [(CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview).
  * Supports [spread placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-spread-policies).
  * Doesn't support Local SSD or per per VM Tier_1 networking performance.



### N4D machine types

N4D VMs are available as predefined configurations in sizes ranging from 2 vCPUs to 96 vCPUs and up to 768 GB of memory.

  * `standard`: 4 GB memory per vCPU
  * `highcpu`: 2 GB memory per vCPU
  * `highmem`: 8 GB memory per vCPU



### N4D standard

Machine types | vCPUs1 | Memory (GB) | Local SSD | Default egress bandwidth (Gbps) | Tier_1 egress bandwidth (Gbps)  
---|---|---|---|---|---  
`n4d-standard-2` | 2 | 8 | Not supported | Up to 10 | N/A  
`n4d-standard-4` | 4 | 16 | Not supported | Up to 10 | N/A  
`n4d-standard-8` | 8 | 32 | Not supported | Up to 16 | N/A  
`n4d-standard-16` | 16 | 64 | Not supported | Up to 32 | N/A  
`n4d-standard-32` | 32 | 128 | Not supported | Up to 32 | N/A  
`n4d-standard-48` | 48 | 192 | Not supported | Up to 32 | N/A  
`n4d-standard-64` | 64 | 256 | Not supported | Up to 45 | N/A  
`n4d-standard-80` | 80 | 320 | Not supported | Up to 50 | N/A  
`n4d-standard-96` | 96 | 384 | Not supported | Up to 50 | N/A  
  
1 A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms)

. 

### N4D highcpu

Machine types | vCPUs1 | Memory (GB) | Local SSD | Default egress bandwidth (Gbps) | Tier_1 egress bandwidth (Gbps)  
---|---|---|---|---|---  
`n4d-highcpu-2` | 2 | 4 | Not supported | Up to 10 | N/A  
`n4d-highcpu-4` | 4 | 8 | Not supported | Up to 10 | N/A  
`n4d-highcpu-8` | 8 | 16 | Not supported | Up to 16 | N/A  
`n4d-highcpu-16` | 16 | 32 | Not supported | Up to 32 | N/A  
`n4d-highcpu-32` | 32 | 64 | Not supported | Up to 32 | N/A  
`n4d-highcpu-48` | 48 | 96 | Not supported | Up to 32 | N/A  
`n4d-highcpu-64` | 64 | 128 | Not supported | Up to 45 | N/A  
`n4d-highcpu-80` | 80 | 160 | Not supported | Up to 50 | N/A  
`n4d-highcpu-96` | 96 | 192 | Not supported | Up to 50 | N/A  
  
1 A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms)

. 

### N4D highmem

Machine types | vCPUs1 | Memory (GB) | Local SSD | Default egress bandwidth (Gbps) | Tier_1 egress bandwidth (Gbps)  
---|---|---|---|---|---  
`n4d-highmem-2` | 2 | 16 | Not supported | Up to 10 | N/A  
`n4d-highmem-4` | 4 | 32 | Not supported | Up to 10 | N/A  
`n4d-highmem-8` | 8 | 64 | Not supported | Up to 16 | N/A  
`n4d-highmem-16` | 16 | 128 | Not supported | Up to 32 | N/A  
`n4d-highmem-32` | 32 | 256 | Not supported | Up to 32 | N/A  
`n4d-highmem-48` | 48 | 384 | Not supported | Up to 32 | N/A  
`n4d-highmem-64` | 64 | 512 | Not supported | Up to 45 | N/A  
`n4d-highmem-80` | 80 | 640 | Not supported | Up to 50 | N/A  
`n4d-highmem-96` | 96 | 768 | Not supported | Up to 50 | N/A  
  
1 A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms)

. 

### Supported disk types for N4D

N4D VMs support only the NVMe disk interface and can use the following [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) block storage:

  * Hyperdisk Balanced (`hyperdisk-balanced`)
  * Hyperdisk Balanced High Availability (`hyperdisk-balanced-high-availability`)
  * Hyperdisk Throughput (`hyperdisk-throughput`)



N4D doesn't support Persistent Disk or Local SSD. Read [Move your workload from an existing VM to a new VM](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm) to migrate your Persistent Disk resources to a newer machine series.

#### Disk and capacity limits

The number of Hyperdisk volumes of all types that you can attach to a VM can't exceed the limits stated in the _Max number of Hyperdisk volumes._ For details about these limits, see [Hyperdisk capacity](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#hyperdisk-capacity).

For instances running Microsoft Windows and using the NVMe disk interface, the combined number of both Hyperdisk and Persistent Disk attached volumes can't exceed a total of 16 disks. See [Known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#windows-disk-attachment). Local SSD volumes are excluded from this issue. 

N4D storage limits are described in the following table:

### N4D standard

| Maximum number of disks |   
---|---|---  
Machine types | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput  
`n4d-standard-2` | 4 | 16 | 16 | 16  
`n4d-standard-4` | 8 | 16 | 16 | 16  
`n4d-standard-8` | 16 | 16 | 16 | 16  
`n4d-standard-16` | 32 | 32 | 32 | 32  
`n4d-standard-32` | 64 | 32 | 32 | 32  
`n4d-standard-48` | 64 | 32 | 32 | 32  
`n4d-standard-64` | 64 | 32 | 32 | 32  
`n4d-standard-80` | 64 | 32 | 32 | 32  
`n4d-standard-96` | 64 | 32 | 32 | 32  
  
### N4D highcpu

| Maximum number of disks |   
---|---|---  
Machine types | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput  
`n4d-highcpu-2` | 4 | 16 | 16 | 16  
`n4d-highcpu-4` | 8 | 16 | 16 | 16  
`n4d-highcpu-8` | 16 | 16 | 16 | 16  
`n4d-highcpu-16` | 32 | 32 | 32 | 32  
`n4d-highcpu-32` | 64 | 32 | 32 | 32  
`n4d-highcpu-48` | 64 | 32 | 32 | 32  
`n4d-highcpu-64` | 64 | 32 | 32 | 32  
`n4d-highcpu-80` | 64 | 32 | 32 | 32  
`n4d-highcpu-96` | 64 | 32 | 32 | 32  
  
### N4D highmem

| Maximum number of disks |   
---|---|---  
Machine types | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput  
`n4d-highmem-2` | 4 | 16 | 16 | 16  
`n4d-highmem-4` | 8 | 16 | 16 | 16  
`n4d-highmem-8` | 16 | 16 | 16 | 16  
`n4d-highmem-16` | 32 | 32 | 32 | 32  
`n4d-highmem-32` | 64 | 32 | 32 | 32  
`n4d-highmem-48` | 64 | 32 | 32 | 32  
`n4d-highmem-64` | 64 | 32 | 32 | 32  
`n4d-highmem-80` | 64 | 32 | 32 | 32  
`n4d-highmem-96` | 64 | 32 | 32 | 32  
  
### Network support for N4D VMs

N4D instances require [gVNIC network interfaces](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). N4D instances support up to 50 Gbps network bandwidth for standard networking and don't support per VM Tier_1 networking performance.

Before migrating to N4D or creating N4D VM instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the gVNIC driver for VM instances. These images include an updated gVNIC driver, even if the guest OS shows the `gve` driver version as 1.0.0. If your N4D VM is using an operating system with an older version of gVNIC driver, this is still supported but the VM might experience suboptimal performance such as less network bandwidth or higher latency.

If you use a custom OS image to create a N4D VM, you can [manually install the most recent gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup). The gVNIC driver version v1.4.2 or later is recommended for use with N4D VMs. Google recommends using the latest gVNIC driver version to benefit from additional features and bug fixes.

### Maintenance experience for N4D instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple _host events_. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The N4D machine series offers the following features related to host maintenance:

Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event)  
---|---|---|---|---  
All N4D machine types | Variable | Live migrate | 60 seconds | No  
  
The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## N4A machine series

N4A VMs are the second family of VMs powered by Google's latest custom-designed Axion processor, built on Arm Neoverse N3 compute core and powered by [Titanium](https://cloud.google.com/titanium) IPU. N4A VMs are placed within a single node with [Uniform Memory Access (UMA)](https://wikipedia.org/wiki/Uniform_memory_access). They are engineered to be our most efficient and flexible Arm VMs, delivering exceptional price-performance for a wide range of general-purpose and scale-out workloads. N4A uses next generation [dynamic resource management](https://docs.cloud.google.com/compute/docs/dynamic-resource-management), which makes better use of resources on host machines.

Ideal use cases include web and application servers, microservices, containerized applications using Google Kubernetes Engine (GKE), open-source databases, and development and testing environments.

In summary, the N4A machine series:

  * Is powered by the Google Axion Arm processor and Titanium IPU.
  * Supports up to 64 vCPUs and 512 GB of DDR5 memory.
  * Offers multiple predefined machine types and custom machine types with extended custom memory up to 512 GB.
  * Supports standard network configuration with up to 50 Gbps of bandwidth.
  * Supports Hyperdisk only.
  * Supports the following discount and consumption options: 
    * [Resource-based and flexible committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)
    * [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
    * [Reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type)
  * Doesn't support Local SSD or per VM Tier_1 networking performance.
  * Confidential VM is not supported by this CPU.
  * 32-bit mode EL0 (guest userspace) is not supported due to a hardware limitation.



### N4A machine types

N4A VMs are available as predefined configurations in sizes ranging from 1 vCPUs to 64 vCPUs and up to 512 GB of memory.

  * `standard`: 4 GB memory per vCPU
  * `highcpu`: 2 GB memory per vCPU
  * `highmem`: 8 GB memory per vCPU



For information about custom machine types, see Custom machine types.

### N4A standard

Machine types | vCPUs1 | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)2 | Tier_1 egress bandwidth (Gbps)  
---|---|---|---|---|---  
`n4a-standard-1` | 1 | 4 | Not supported | Up to 10 | N/A  
`n4a-standard-2` | 2 | 8 | Not supported | Up to 10 | N/A  
`n4a-standard-4` | 4 | 16 | Not supported | Up to 10 | N/A  
`n4a-standard-8` | 8 | 32 | Not supported | Up to 16 | N/A  
`n4a-standard-16` | 16 | 64 | Not supported | Up to 32 | N/A  
`n4a-standard-32` | 32 | 128 | Not supported | Up to 32 | N/A  
`n4a-standard-48` | 48 | 192 | Not supported | Up to 32 | N/A  
`n4a-standard-64` | 64 | 256 | Not supported | Up to 50 | N/A  
  
1 SMT is not supported. Each vCPU is equivalent to an entire core. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  


### N4A highcpu

Machine types | vCPUs1 | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)2 | Tier_1 egress bandwidth (Gbps)  
---|---|---|---|---|---  
`n4a-highcpu-1` | 1 | 2 | Not supported | Up to 10 | N/A  
`n4a-highcpu-2` | 2 | 4 | Not supported | Up to 10 | N/A  
`n4a-highcpu-4` | 4 | 8 | Not supported | Up to 10 | N/A  
`n4a-highcpu-8` | 8 | 16 | Not supported | Up to 16 | N/A  
`n4a-highcpu-16` | 16 | 32 | Not supported | Up to 32 | N/A  
`n4a-highcpu-32` | 32 | 64 | Not supported | Up to 32 | N/A  
`n4a-highcpu-48` | 48 | 96 | Not supported | Up to 32 | N/A  
`n4a-highcpu-64` | 64 | 128 | Not supported | Up to 50 | N/A  
  
1 SMT is not supported. Each vCPU is equivalent to an entire core. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  


### N4A highmem

Machine types | vCPUs1 | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)2 | Tier_1 egress bandwidth (Gbps)  
---|---|---|---|---|---  
`n4a-highmem-1` | 1 | 8 | Not supported | Up to 10 | N/A  
`n4a-highmem-2` | 2 | 16 | Not supported | Up to 10 | N/A  
`n4a-highmem-4` | 4 | 32 | Not supported | Up to 10 | N/A  
`n4a-highmem-8` | 8 | 64 | Not supported | Up to 16 | N/A  
`n4a-highmem-16` | 16 | 128 | Not supported | Up to 32 | N/A  
`n4a-highmem-32` | 32 | 256 | Not supported | Up to 32 | N/A  
`n4a-highmem-48` | 48 | 384 | Not supported | Up to 32 | N/A  
`n4a-highmem-64` | 64 | 512 | Not supported | Up to 50 | N/A  
  
1 SMT is not supported. Each vCPU is equivalent to an entire core. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  


### Supported disk types for N4A

N4A VMs support only the NVMe disk interface and can use the following [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) block storage:

  * Hyperdisk Balanced (`hyperdisk-balanced`)
  * Hyperdisk Balanced High Availability (`hyperdisk-balanced-high-availability`)
  * Hyperdisk Throughput (`hyperdisk-throughput`)



N4A doesn't support Persistent Disk or Local SSD. Read [Move your workload from an existing VM to a new VM](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm) to migrate your Persistent Disk resources to a newer machine series.

#### Disk and capacity limits

The number of Hyperdisk volumes of all types that you can attach to a VM can't exceed the limits stated in the _Max number of Hyperdisk volumes_. For details about these limits, see [Hyperdisk capacity](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#hyperdisk-capacity).

The combined total number of Hyperdisk Balanced volumes attached to a single VM depends on the number of vCPUs the VM has, and can't exceed these limits:

N4A storage limits are described in the following table:

### N4A standard

| Maximum number of disks |   
---|---|---  
Machine types | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput  
`n4a-standard-1` | 4 | 16 | 16 | 16  
`n4a-standard-2` | 4 | 16 | 16 | 16  
`n4a-standard-4` | 8 | 16 | 16 | 16  
`n4a-standard-8` | 16 | 16 | 16 | 16  
`n4a-standard-16` | 32 | 32 | 32 | 32  
`n4a-standard-32` | 64 | 32 | 32 | 32  
`n4a-standard-48` | 64 | 32 | 32 | 32  
`n4a-standard-64` | 64 | 32 | 32 | 32  
  
### N4A highcpu

| Maximum number of disks |   
---|---|---  
Machine types | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput  
`n4a-highcpu-1` | 4 | 16 | 16 | 16  
`n4a-highcpu-2` | 4 | 16 | 16 | 16  
`n4a-highcpu-4` | 8 | 16 | 16 | 16  
`n4a-highcpu-8` | 16 | 16 | 16 | 16  
`n4a-highcpu-16` | 32 | 32 | 32 | 32  
`n4a-highcpu-32` | 32 | 32 | 32 | 32  
`n4a-highcpu-48` | 64 | 32 | 32 | 32  
`n4a-highcpu-64` | 64 | 32 | 32 | 32  
  
### N4A highmem

| Maximum number of disks |   
---|---|---  
Machine types | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput  
`n4a-highmem-1` | 4 | 16 | 16 | 16  
`n4a-highmem-2` | 4 | 16 | 16 | 16  
`n4a-highmem-4` | 8 | 16 | 16 | 16  
`n4a-highmem-8` | 16 | 16 | 16 | 16  
`n4a-highmem-16` | 32 | 32 | 32 | 32  
`n4a-highmem-32` | 32 | 32 | 32 | 32  
`n4a-highmem-48` | 64 | 32 | 32 | 32  
`n4a-highmem-64` | 64 | 32 | 32 | 32  
  
### Network support for N4A VMs

N4A instances require [gVNIC network interfaces](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). N4A instances support up to 50 Gbps network bandwidth for standard networking and don't support per VM Tier_1 networking performance.

Before migrating to N4A or creating N4A VM instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the gVNIC driver for VM instances. These images include an updated gVNIC driver, even if the guest OS shows the `gve` driver version as 1.0.0. If your N4A VM is using an operating system with an older version of gVNIC driver, this is still supported but the VM might experience suboptimal performance such as less network bandwidth or higher latency.

If you use a custom OS image to create a N4A VM, you can [manually install the most recent gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup). The gVNIC driver version v1.4.2 or later is recommended for use with N4A VMs. Google recommends using the latest gVNIC driver version to benefit from additional features and bug fixes.

### Maintenance experience for N4A instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple _host events_. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The N4A machine series offers the following features related to host maintenance:

Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event)  
---|---|---|---|---  
All N4A machine types | Variable | Live migrate | 60 seconds | No  
  
## N4 machine series

N4 VMs are powered by the 5th generation Intel Xeon Scalable processors (code-named Emerald Rapids) and [Titanium](https://cloud.google.com/titanium). N4 machine types are built from the ground up for flexibility and cost optimization through an efficient architecture of streamlined features, shapes, and next generation [dynamic resource management](https://docs.cloud.google.com/compute/docs/dynamic-resource-management), which makes better use of resources on host machines. N4 offers flexible options like custom machine types that lets you use choose varied combinations of compute and memory to optimize costs and reduce resource waste. N4 is suited for a variety of general-purpose workloads that don't require peak processing power at all times.

In summary, the N4 machine series:

  * Is powered by 5th generation Intel Emerald Rapids processor and titanium processors.
  * Supports up to 80 vCPUs and 640 GB of DDR5 memory.
  * Offers multiple predefined machine types and custom machine types and extended custom memory up to 640 GB.
  * Supports standard network configuration with up to 50 Gbps bandwidth
  * Supports Intel Advanced Matrix Extensions (AMX), a built-in accelerator that significantly improves the performance of deep-learning training and inference on the CPU.
  * Supports the following discount and consumption options: 
    * [Resource-based and flexible committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)
    * [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
    * [Reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type)
  * Doesn't support Local SSD or per VM Tier_1 networking performance.



### N4 machine types

N4 VMs are available as predefined configurations in sizes ranging from 2 vCPUs to 80 vCPUs and up to 640 GB of memory.

  * `standard`: 4 GB memory per vCPU
  * `highcpu`: 2 GB memory per vCPU
  * `highmem`: 8 GB memory per vCPU



### N4 standard

Machine types | vCPUs1 | Memory (GB) | Local SSD | Default egress bandwidth (Gbps) | Tier_1 egress bandwidth (Gbps)  
---|---|---|---|---|---  
`n4-standard-2` | 2 | 8 | Not supported | Up to 10 | N/A  
`n4-standard-4` | 4 | 16 | Not supported | Up to 10 | N/A  
`n4-standard-8` | 8 | 32 | Not supported | Up to 16 | N/A  
`n4-standard-16` | 16 | 64 | Not supported | Up to 32 | N/A  
`n4-standard-32` | 32 | 128 | Not supported | Up to 32 | N/A  
`n4-standard-48` | 48 | 192 | Not supported | Up to 32 | N/A  
`n4-standard-64` | 64 | 256 | Not supported | Up to 45 | N/A  
`n4-standard-80` | 80 | 320 | Not supported | Up to 50 | N/A  
  
1 A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms)

. 

### N4 highcpu

Machine types | vCPUs1 | Memory (GB) | Local SSD | Default egress bandwidth (Gbps) | Tier_1 egress bandwidth (Gbps)  
---|---|---|---|---|---  
`n4-highcpu-2` | 2 | 4 | Not supported | Up to 10 | N/A  
`n4-highcpu-4` | 4 | 8 | Not supported | Up to 10 | N/A  
`n4-highcpu-8` | 8 | 16 | Not supported | Up to 16 | N/A  
`n4-highcpu-16` | 16 | 32 | Not supported | Up to 32 | N/A  
`n4-highcpu-32` | 32 | 64 | Not supported | Up to 32 | N/A  
`n4-highcpu-48` | 48 | 96 | Not supported | Up to 32 | N/A  
`n4-highcpu-64` | 64 | 128 | Not supported | Up to 45 | N/A  
`n4-highcpu-80` | 80 | 160 | Not supported | Up to 50 | N/A  
  
1 A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms)

. 

### N4 highmem

Machine types | vCPUs1 | Memory (GB) | Local SSD | Default egress bandwidth (Gbps) | Tier_1 egress bandwidth (Gbps)  
---|---|---|---|---|---  
`n4-highmem-2` | 2 | 16 | Not supported | Up to 10 | N/A  
`n4-highmem-4` | 4 | 32 | Not supported | Up to 10 | N/A  
`n4-highmem-8` | 8 | 64 | Not supported | Up to 16 | N/A  
`n4-highmem-16` | 16 | 128 | Not supported | Up to 32 | N/A  
`n4-highmem-32` | 32 | 256 | Not supported | Up to 32 | N/A  
`n4-highmem-48` | 48 | 384 | Not supported | Up to 32 | N/A  
`n4-highmem-64` | 64 | 512 | Not supported | Up to 45 | N/A  
`n4-highmem-80` | 80 | 640 | Not supported | Up to 50 | N/A  
  
1 A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms)

. 

### Supported disk types for N4

N4 VMs supports only the NVMe disk interface and can use the following [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) block storage:

  * Hyperdisk Balanced (`hyperdisk-balanced`)
  * Hyperdisk Balanced High Availability (`hyperdisk-balanced-high-availability`)
  * Hyperdisk Throughput (`hyperdisk-throughput`)



N4 doesn't support Persistent Disk or Local SSD. Read [Move your workload from an existing VM to a new VM](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm) to migrate your Persistent Disk resources to a newer machine series.

#### Disk and capacity limits

The number of Hyperdisk volumes of all types that you can attach to a VM can't exceed the limits stated in the _Max number of Hyperdisk volumes_. For details about these limits, see [Hyperdisk capacity](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#hyperdisk-capacity).

N4 storage limits are described in the following table:

### N4 standard

| Maximum number of disks |   
---|---|---  
Machine types | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput  
`n4-standard-2` | 16 | 16 | 16 | 16  
`n4-standard-4` | 16 | 16 | 16 | 16  
`n4-standard-8` | 16 | 16 | 16 | 16  
`n4-standard-16` | 32 | 32 | 32 | 32  
`n4-standard-32` | 32 | 32 | 32 | 32  
`n4-standard-48` | 32 | 32 | 32 | 32  
`n4-standard-64` | 32 | 32 | 32 | 32  
`n4-standard-80` | 32 | 32 | 32 | 32  
  
### N4 highcpu

| Maximum number of disks |   
---|---|---  
Machine types | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput  
`n4-highcpu-2` | 16 | 16 | 16 | 16  
`n4-highcpu-4` | 16 | 16 | 16 | 16  
`n4-highcpu-8` | 16 | 16 | 16 | 16  
`n4-highcpu-16` | 32 | 32 | 32 | 32  
`n4-highcpu-32` | 32 | 32 | 32 | 32  
`n4-highcpu-48` | 32 | 32 | 32 | 32  
`n4-highcpu-64` | 32 | 32 | 32 | 32  
`n4-highcpu-80` | 32 | 32 | 32 | 32  
  
### N4 highmem

| Maximum number of disks |   
---|---|---  
Machine types | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Balanced High Availability | Hyperdisk Throughput  
`n4-highmem-2` | 16 | 16 | 16 | 16  
`n4-highmem-4` | 16 | 16 | 16 | 16  
`n4-highmem-8` | 16 | 16 | 16 | 16  
`n4-highmem-16` | 32 | 32 | 32 | 32  
`n4-highmem-32` | 32 | 32 | 32 | 32  
`n4-highmem-48` | 32 | 32 | 32 | 32  
`n4-highmem-64` | 32 | 32 | 32 | 32  
`n4-highmem-80` | 32 | 32 | 32 | 32  
  
### Network support for N4 VMs

N4 instances require [gVNIC network interfaces](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). N4 instances support up to 50 Gbps network bandwidth for standard networking and don't support per VM Tier_1 networking performance.

Before migrating to N4 or creating N4 VM instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the gVNIC driver for VM instances. These images include an updated gVNIC driver, even if the guest OS shows the `gve` driver version as 1.0.0. If your N4 VM is using an operating system with an older version of gVNIC driver, this is still supported but the VM might experience suboptimal performance such as less network bandwidth or higher latency.

If you use a custom OS image to create a N4 VM, you can [manually install the most recent gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup). The gVNIC driver version v1.4.2 or later is recommended for use with N4 VMs. Google recommends using the latest gVNIC driver version to benefit from additional features and bug fixes.

### Maintenance experience for N4 instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple _host events_. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The N4 machine series offers the following features related to host maintenance:

Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event)  
---|---|---|---|---  
All N4 machine types | Variable | Live migrate | 60 seconds | No  
  
The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## C3D machine series

C3D VMs are powered by the 4th generation AMD EPYC™ (Genoa) processor with a maximum frequency of 3.7 Ghz. C3D machine types are optimized for the underlying hardware architecture to deliver optimal, reliable, and consistent performance.

C3D uses [Titanium](https://cloud.google.com/titanium), which enables higher levels of networking performance, isolation and security. The C3D machine series supports Tier_1 networking bandwidth of up to 100 Gbps and up to 200 Gbps.

In summary, the C3D machine series:

  * Is powered by 4th generation AMD EPYC™ processor and Titanium.
  * Supports up to 360 vCPUs and 2,880 GB of DDR5 memory.
  * Supports standard network configuration with up to 100 Gbps bandwidth and Tier_1 networking with up to 200 Gbps bandwidth.
  * Supports the following discount and consumption options: 
    * [Resource-based and flexible committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)
    * [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
    * [Reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type)
  * Supports [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) with AMD SEV, excluding bare metal instances and configurations with more than 255 vCPUs.

**Caution** : When you purchase resource-based commitments for C3 and C3D resources, the machine family that is specified by the commitment type changes depending on the interface: 

  * In the gcloud CLI and REST, the commitment type values use _Compute-optimized_ as the machine family, even though C3 and C3D are part of the general-purpose machine family.
  * In the Google Cloud console, the commitment type values use the correct machine series: _General-Purpose_.

Make sure to select the correct commitment type value that corresponds to the interface that you're using. For more information, see the [resource-based CUDs documentation](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts). 

### C3D machine types

C3D VMs are available in `standard`, `highcpu`, `highmem`, and `lssd` configurations in sizes ranging from 4 to 360 vCPUs and up to 2,880 GB of memory. The `highcpu` configuration offers the lowest price per performance for compute-bound workloads that don't require large amounts of memory.

### C3D standard

Machine types | vCPUs1 | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)2 | Tier_1 egress bandwidth (Gbps)3  
---|---|---|---|---|---  
`c3d-standard-4` | 4 | 16 | Not supported | Up to 20 | N/A  
`c3d-standard-8` | 8 | 32 | Not supported | Up to 20 | N/A  
`c3d-standard-16` | 16 | 64 | Not supported | Up to 20 | N/A  
`c3d-standard-30` | 30 | 120 | Not supported | Up to 20 | Up to 50  
`c3d-standard-60` | 60 | 240 | Not supported | Up to 40 | Up to 75  
`c3d-standard-90` | 90 | 360 | Not supported | Up to 60 | Up to 100  
`c3d-standard-180` | 180 | 720 | Not supported | Up to 100 | Up to 150  
`c3d-standard-360` | 360 | 1,440 | Not supported | Up to 100 | Up to 200  
  
1 A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).   
2 Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3 Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

### C3D highcpu

Machine types | vCPUs1 | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)2 | Tier_1 egress bandwidth (Gbps)3  
---|---|---|---|---|---  
`c3d-highcpu-4` | 4 | 8 | Not supported | Up to 20 | N/A  
`c3d-highcpu-8` | 8 | 16 | Not supported | Up to 20 | N/A  
`c3d-highcpu-16` | 16 | 32 | Not supported | Up to 20 | N/A  
`c3d-highcpu-30` | 30 | 59 | Not supported | Up to 20 | Up to 50  
`c3d-highcpu-60` | 60 | 118 | Not supported | Up to 40 | Up to 75  
`c3d-highcpu-90` | 90 | 177 | Not supported | Up to 60 | Up to 100  
`c3d-highcpu-180` | 180 | 354 | Not supported | Up to 100 | Up to 150  
`c3d-highcpu-360` | 360 | 708 | Not supported | Up to 100 | Up to 200  
  
1 A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).   
2 Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3 Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

### C3D highmem

Machine types | vCPUs1 | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)2 | Tier_1 egress bandwidth (Gbps)3  
---|---|---|---|---|---  
`c3d-highmem-4` | 4 | 32 | Not supported | Up to 20 | N/A  
`c3d-highmem-8` | 8 | 64 | Not supported | Up to 20 | N/A  
`c3d-highmem-16` | 16 | 128 | Not supported | Up to 20 | N/A  
`c3d-highmem-30` | 30 | 240 | Not supported | Up to 20 | Up to 50  
`c3d-highmem-60` | 60 | 480 | Not supported | Up to 40 | Up to 75  
`c3d-highmem-90` | 90 | 720 | Not supported | Up to 60 | Up to 100  
`c3d-highmem-180` | 180 | 1,440 | Not supported | Up to 100 | Up to 150  
`c3d-highmem-360` | 360 | 2,880 | Not supported | Up to 100 | Up to 200  
  
1 A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).   
2 Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3 Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

### C3D standard

Machine types | vCPUs1 | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)2 | Tier_1 egress bandwidth (Gbps)3  
---|---|---|---|---|---  
`c3d-standard-8-lssd` | 8 | 32 | (1 x 375 GiB)  
375 GiB | Up to 20 | N/A  
`c3d-standard-16-lssd` | 16 | 64 | (1 x 375 GiB)  
375 GiB | Up to 20 | N/A  
`c3d-standard-30-lssd` | 30 | 120 | (2 x 375 GiB)  
750 GiB | Up to 20 | Up to 50  
`c3d-standard-60-lssd` | 60 | 240 | (4 x 375 GiB)  
1.5 TiB | Up to 40 | Up to 75  
`c3d-standard-90-lssd` | 90 | 360 | (8 x 375 GiB)  
3 TiB | Up to 60 | Up to 100  
`c3d-standard-180-lssd` | 180 | 720 | (16 x 375 GiB)  
6 TiB | Up to 100 | Up to 150  
`c3d-standard-360-lssd` | 360 | 1440 | (32 x 375 GiB)  
12 TiB | Up to 100 | Up to 200  
  
1 A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).   
2 Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3 Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

### C3D highmem

Machine types | vCPUs1 | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)2 | Tier_1 egress bandwidth (Gbps)3  
---|---|---|---|---|---  
`c3d-highmem-8-lssd` | 8 | 64 | (1 x 375 GiB)  
375 GiB | Up to 20 | N/A  
`c3d-highmem-16-lssd` | 16 | 128 | (1 x 375 GiB)  
375 GiB | Up to 20 | N/A  
`c3d-highmem-30-lssd` | 30 | 240 | (2 x 375 GiB)  
750 GiB | Up to 20 | Up to 50  
`c3d-highmem-60-lssd` | 60 | 480 | (4 x 375 GiB)  
1.5 TiB | Up to 40 | Up to 75  
`c3d-highmem-90-lssd` | 90 | 720 | (8 x 375 GiB)  
3 TiB | Up to 60 | Up to 100  
`c3d-highmem-180-lssd` | 180 | 1440 | (16 x 375 GiB)  
6 TiB | Up to 100 | Up to 150  
`c3d-highmem-360-lssd` | 360 | 2880 | (32 x 375 GiB)  
12 TiB | Up to 100 | Up to 200  
  
1 A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).   
2 Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3 Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

C3D doesn't support custom machine types.

### Supported disk types for C3D

C3D VMs support only the NVMe disk interface and can use the following block storage types:

  * Balanced Persistent Disk (`pd-balanced`)
  * SSD (performance) Persistent Disk (`pd-ssd`)
  * Hyperdisk Balanced (`hyperdisk-balanced`)
  * Hyperdisk Balanced High Availability (`hyperdisk-balanced-high-availability`)
  * Hyperdisk ML (`hyperdisk-ml`)
  * Hyperdisk Extreme (`hyperdisk-extreme`)
  * Hyperdisk Throughput (`hyperdisk-throughput`)
  * Local SSD (only available with `-lssd` machine types)



To use Local SSD with C3D, create your VM using the `-lssd` variant of the C3D machine types. Selecting this machine type creates a VM of the specified size with Local SSD partitions attached. You must use a machine type that ends in `-lssd` to use Local SSD with your C3D VM; you can't attach Local SSD volumes separately.

#### Disk and capacity limits

For instances running Microsoft Windows and using the NVMe disk interface, the combined number of both Hyperdisk and Persistent Disk attached volumes can't exceed a total of 16 disks. See [Known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#windows-disk-attachment). Local SSD volumes are excluded from this issue. 

C3D storage limits are described in the following table:

### C3D standard

| Maximum number of disks |   
---|---|---  
Machine types | Per VM | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme  
`c3d-standard-4` | 128 | 24 | 16 | 24 | 24 | 0  
`c3d-standard-8` | 128 | 32 | 16 | 32 | 32 | 0  
`c3d-standard-16` | 128 | 48 | 16 | 48 | 48 | 0  
`c3d-standard-30` | 128 | 64 | 16 | 64 | 64 | 0  
`c3d-standard-60` | 128 | 64 | 32 | 64 | 64 | 8  
`c3d-standard-90` | 128 | 64 | 32 | 64 | 64 | 8  
`c3d-standard-180` | 128 | 64 | 32 | 64 | 64 | 8  
`c3d-standard-360` | 128 | 64 | 32 | 64 | 64 | 8  
  
### C3D highcpu

| Maximum number of disks |   
---|---|---  
Machine types | Per VM | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme  
`c3d-highcpu-4` | 128 | 24 | 16 | 24 | 24 | 0  
`c3d-highcpu-8` | 128 | 32 | 16 | 32 | 32 | 0  
`c3d-highcpu-16` | 128 | 48 | 16 | 48 | 48 | 0  
`c3d-highcpu-30` | 128 | 64 | 16 | 64 | 64 | 0  
`c3d-highcpu-60` | 128 | 64 | 32 | 64 | 64 | 8  
`c3d-highcpu-90` | 128 | 64 | 32 | 64 | 64 | 8  
`c3d-highcpu-180` | 128 | 64 | 32 | 64 | 64 | 8  
`c3d-highcpu-360` | 128 | 64 | 32 | 64 | 64 | 8  
  
### C3D highmem

| Maximum number of disks |   
---|---|---  
Machine types | Per VM | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme  
`c3d-highmem-4` | 128 | 24 | 16 | 24 | 24 | 0  
`c3d-highmem-8` | 128 | 32 | 16 | 32 | 32 | 0  
`c3d-highmem-16` | 128 | 48 | 16 | 48 | 48 | 0  
`c3d-highmem-30` | 128 | 64 | 16 | 64 | 64 | 0  
`c3d-highmem-60` | 128 | 64 | 32 | 64 | 64 | 8  
`c3d-highmem-90` | 128 | 64 | 32 | 64 | 64 | 8  
`c3d-highmem-180` | 128 | 64 | 32 | 64 | 64 | 8  
`c3d-highmem-360` | 128 | 64 | 32 | 64 | 64 | 8  
  
### C3D standard

| Maximum number of disks |   
---|---|---  
Machine types | Per VM | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme  
`c3d-standard-8-lssd` | 128 | 24 | 16 | 24 | 24 | 0  
`c3d-standard-16-lssd` | 128 | 48 | 16 | 48 | 48 | 0  
`c3d-standard-30-lssd` | 128 | 64 | 16 | 64 | 64 | 0  
`c3d-standard-60-lssd` | 128 | 64 | 32 | 64 | 64 | 8  
`c3d-standard-90-lssd` | 128 | 64 | 32 | 64 | 64 | 8  
`c3d-standard-180-lssd` | 128 | 64 | 32 | 64 | 64 | 8  
`c3d-standard-360-lssd` | 128 | 64 | 32 | 64 | 64 | 8  
  
### C3D highmem

| Maximum number of disks |   
---|---|---  
Machine types | Per VM | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme  
`c3d-highmem-8-lssd` | 128 | 24 | 16 | 24 | 24 | 0  
`c3d-highmem-16-lssd` | 128 | 48 | 16 | 48 | 48 | 0  
`c3d-highmem-30-lssd` | 128 | 64 | 16 | 64 | 64 | 0  
`c3d-highmem-60-lssd` | 128 | 64 | 32 | 64 | 64 | 8  
`c3d-highmem-90-lssd` | 128 | 64 | 32 | 64 | 64 | 8  
`c3d-highmem-180-lssd` | 128 | 64 | 32 | 64 | 64 | 8  
`c3d-highmem-360-lssd` | 128 | 64 | 32 | 64 | 64 | 8  
  
### Network support for C3D VMs

C3D instances require [gVNIC network interfaces](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). C3D supports up to 100 Gbps network bandwidth for standard networking and up to 200 Gbps with per VM Tier_1 networking performance.

Before migrating to C3D or creating C3D instances, make sure that the operating system image that you use supports the gVNIC driver. To get the best possible performance on C3D instances, on the [**Networking features**](https://docs.cloud.google.com/compute/docs/images/os-details#networking-features) tab of the OS details table, choose an OS image that supports both "Tier_1 Networking" and "200 Gbps network bandwidth". These images include an updated gVNIC driver, even if the guest OS shows the `gve` driver version as 1.0.0. If your C3D instance is using an operating system with an older version of the gVNIC driver, this is still supported but the instance might experience suboptimal performance such as less network bandwidth or higher latency.

If you use a custom OS image with the C3D machine series, you can [manually install the most recent gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup). The gVNIC driver version v1.4.2 or later is recommended for use with C3D instances. Google recommends using the latest gVNIC driver version to benefit from additional features and bug fixes.

### Maintenance experience for C3D instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple _host events_. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The C3D machine series offers the following features related to host maintenance:

Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event)  
---|---|---|---|---  
C3D with Confidential VM | Minimum of 30 days | Terminate | 7 days | No  
`c3d-*-lssd` | Minimum of 30 days | Live migrate | 7 days | Yes  
`c3d-*-360` | Minimum of 30 days | Live migrate | 7 days | Yes  
All others | Minimum of 30 days | Live migrate | 7 days | No  
  
The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## C3 machine series

C3 VMs are powered by the 4th generation Intel Xeon Scalable processors (code-named Sapphire Rapids), DDR5 memory, and [Titanium](https://cloud.google.com/titanium). C3 machine types are optimized for the underlying NUMA architecture to deliver optimal, reliable, and consistent performance.

The new C3 machine series is a major leap in our purpose-built infrastructure offerings:

  * Leveraging Titanium processors to offload networking from the CPUs
  * Delivering high performance block-storage with [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks)
  * Speeding up ML training and inference with [Intel AMX](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel-amx)



C3 uses Titanium to enable higher levels of networking performance, isolation and security. The C3 machine series supports a default network bandwidth of up to 100 Gbps and up to 200 Gbps with [per VM Tier_1 networking performance](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration). Titanium has been designed from the ground up to enable updates that don't impact running workloads.

The C3 machine series provides some of the largest general-purpose machine types, letting you create VM instances with up to 176 vCPUs and 1.4 TB of memory.

C3 has bare metal machine types, which allow you to access all the raw compute resources of the server. You can create bare metal instances with 192 vCPUs and up to 1,536 GB of memory. Bare metal instances also provide access to several onboard, function-specific [accelerators and offloads](https://docs.cloud.google.com/compute/docs/cpu-platforms#accelerator):

  * Intel-QAT
  * Intel-DLB
  * Intel DSA
  * Intel IAA



If your organization uses a Shielded VM policy, then you must create a custom org policy that excludes bare metal shapes before you can create a bare metal instance.

In summary, the C3 machine series:

  * Is powered by Intel 4th Generation Xeon processors and Titanium.
  * Supports up to 176 vCPUs and 1.4 TB of DDR5 memory for VMs.
  * Supports up to 192 vCPUs and 1,536 GB of memory for bare metal instances.
  * Supports standard network configuration with up to 100 Gbps bandwidth and Tier_1 networking with up to 200 Gbps bandwidth.
  * Supports Intel Advanced Matrix Extensions (AMX), a built-in accelerator that significantly improves the performance of deep-learning training and inference on the CPU.
  * Supports the following discount and consumption options: 
    * [Resource-based and flexible committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)
    * [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
    * [Reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type)
  * Supports [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) with Intel TDX.
  * Doesn't offer [sustained use discounts (SUDs)](https://docs.cloud.google.com/compute/docs/sustained-use-discounts).
  * C3 bare metal instances don't support the following: 
    * [Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm)
    * [Nested virtualization](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview)



**Caution** : When you purchase resource-based commitments for C3 and C3D resources, the machine family that is specified by the commitment type changes depending on the interface: 

  * In the gcloud CLI and REST, the commitment type values use _Compute-optimized_ as the machine family, even though C3 and C3D are part of the general-purpose machine family.
  * In the Google Cloud console, the commitment type values use the correct machine series: _General-Purpose_.

Make sure to select the correct commitment type value that corresponds to the interface that you're using. For more information, see the [resource-based CUDs documentation](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts). 

### C3 machine types

C3 VMs are available in predefined machine types with sizes ranging from 4 to 176 vCPUs and up to 1,408 GB of memory.

To use Local SSD with C3, create your VM using the `-lssd` variant of the C3 machine types. Selecting this machine type creates a VM of the specified size with Local SSD partitions attached. You must use a `c3-standard-*-lssd` machine type to use Local SSD with your VM; you can't attach Local SSD volumes separately.

To create a bare metal instance with C3, use one of the following machine types:

  * `c3-standard-192-metal`
  * `c3-highcpu-192-metal`
  * `c3-highmem-192-metal`



### C3 standard

Machine types | vCPUs1 | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)2 | Tier_1 egress bandwidth (Gbps)  
---|---|---|---|---|---  
`c3-standard-4` | 4 | 16 | Not supported | Up to 23 | N/A  
`c3-standard-8` | 8 | 32 | Not supported | Up to 23 | N/A  
`c3-standard-22` | 22 | 88 | Not supported | Up to 23 | N/A  
`c3-standard-44` | 44 | 176 | Not supported | Up to 32 | Up to 50  
`c3-standard-88` | 88 | 352 | Not supported | Up to 62 | Up to 100  
`c3-standard-176` | 176 | 704 | Not supported | Up to 100 | Up to 200  
`c3-standard-192-metal` | 192† | 768 | Not supported | Up to 100 | Up to 200  
  
1 Each CPU uses two threads per core. A vCPU is implemented as a single hardware thread.

2 For bare metal instances, the number of vCPUs is equivalent to the number of hardware threads on the host server. 

3 Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth). 

### C3 highcpu

Machine types | vCPUs1 | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)2 | Tier_1 egress bandwidth (Gbps)  
---|---|---|---|---|---  
`c3-highcpu-4` | 4 | 8 | Not supported | Up to 23 | N/A  
`c3-highcpu-8` | 8 | 16 | Not supported | Up to 23 | N/A  
`c3-highcpu-22` | 22 | 44 | Not supported | Up to 23 | N/A  
`c3-highcpu-44` | 44 | 88 | Not supported | Up to 32 | Up to 50  
`c3-highcpu-88` | 88 | 176 | Not supported | Up to 62 | Up to 100  
`c3-highcpu-176` | 176 | 352 | Not supported | Up to 100 | Up to 200  
`c3-highcpu-192-metal` | 192† | 512 | Not supported | Up to 100 | Up to 200  
  
1 Each CPU uses two threads per core. A vCPU is implemented as a single hardware thread.

2 For bare metal instances, the number of vCPUs is equivalent to the number of hardware threads on the host server. 

3 Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth). 

### C3 highmem

Machine types | vCPUs1 | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)2 | Tier_1 egress bandwidth (Gbps)  
---|---|---|---|---|---  
`c3-highmem-4` | 4 | 32 | Not supported | Up to 23 | N/A  
`c3-highmem-8` | 8 | 64 | Not supported | Up to 23 | N/A  
`c3-highmem-22` | 22 | 176 | Not supported | Up to 23 | N/A  
`c3-highmem-44` | 44 | 352 | Not supported | Up to 32 | Up to 50  
`c3-highmem-88` | 88 | 704 | Not supported | Up to 62 | Up to 100  
`c3-highmem-176` | 176 | 1408 | Not supported | Up to 100 | Up to 200  
`c3-highmem-192-metal` | 192† | 1536 | Not supported | Up to 100 | Up to 200  
  
1 Each CPU uses two threads per core. A vCPU is implemented as a single hardware thread.

2 For bare metal instances, the number of vCPUs is equivalent to the number of hardware threads on the host server. 

3 Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth). 

### C3 standard

Machine types | vCPUs1 | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)2 | Tier_1 egress bandwidth (Gbps)  
---|---|---|---|---|---  
`c3-standard-4-lssd` | 4 | 16 | (1 x 375 GiB)  
375 GiB | Up to 23 | N/A  
`c3-standard-8-lssd` | 8 | 32 | (2 x 375 GiB)  
750 GiB | Up to 23 | N/A  
`c3-standard-22-lssd` | 22 | 88 | (4 x 375 GiB)  
1.5 TiB | Up to 23 | N/A  
`c3-standard-44-lssd` | 44 | 176 | (8 x 375 GiB)  
3 TiB | Up to 32 | Up to 50  
`c3-standard-88-lssd` | 88 | 352 | (16 x 375 GiB)  
6 TiB | Up to 62 | Up to 100  
`c3-standard-176-lssd` | 176 | 704 | (32 x 375 GiB)  
12 TiB | Up to 100 | Up to 200  
  
1 Each CPU uses two threads per core. A vCPU is implemented as a single hardware thread.

2 For bare metal instances, the number of vCPUs is equivalent to the number of hardware threads on the host server. 

3 Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth). 

C3 doesn't support custom machine types.

### C3 regional availability for bare metal instances

For C3 VMs, you can view the available regions and zones in the [Regional availability of bare metal instances](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances#regions-zones) table.

### Supported disk types for C3

C3 VMs support only the NVMe disk interface and can use the following block storage types:

###  VM instances 

  * Zonal balanced Persistent Disk (`pd-balanced`)
  * Zonal SSD (performance) Persistent Disk (`pd-ssd`)
  * Hyperdisk Extreme (`hyperdisk-extreme`)—Requires at least 64 vCPUs
  * Hyperdisk ML (`hyperdisk-ml`)
  * Hyperdisk Throughput (`hyperdisk-throughput`)
  * Hyperdisk Balanced (`hyperdisk-balanced`)
  * Hyperdisk Balanced High Availability (`hyperdisk-balanced-high-availability`)
  * Local SSD (only available with `-lssd` machine types)



###  Bare metal instances 

  * Hyperdisk Balanced (`hyperdisk-balanced`)
  * Hyperdisk Extreme (`hyperdisk-extreme`)



A set amount of Local SSD disks are added to the C3 VM when you use the `-lssd` machine type. This is the only way to include Local SSD storage with a C3 VM. You can't use Local SSD disks with bare metal instances.

#### Disk and capacity limits

For instances running Microsoft Windows and using the NVMe disk interface, the combined number of both Hyperdisk and Persistent Disk attached volumes can't exceed a total of 16 disks. See [Known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#windows-disk-attachment). Local SSD volumes are excluded from this issue. 

C3 storage limits are described in the following table:

### C3 standard

| Maximum number of disks |   
---|---|---  
Machine types | Per instance | Hyperdisk  
per instance | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme  
`c3-standard-4` | 128 | 24 | 16 | 24 | 24 | 0  
`c3-standard-8` | 128 | 32 | 16 | 32 | 32 | 0  
`c3-standard-22` | 128 | 48 | 32 | 48 | 48 | 0  
`c3-standard-44` | 128 | 64 | 32 | 64 | 64 | 0  
`c3-standard-88` | 128 | 64 | 32 | 64 | 64 | 8  
`c3-standard-176` | 128 | 64 | 32 | 64 | 64 | 8  
`c3-standard-192-metal` | 128 | 128 | 16 | Not supported | Not supported | 16  
  
### C3 highcpu

| Maximum number of disks |   
---|---|---  
Machine types | Per instance | Hyperdisk  
per instance | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme  
`c3-highcpu-4` | 128 | 24 | 16 | 24 | 24 | 0  
`c3-highcpu-8` | 128 | 32 | 16 | 32 | 32 | 0  
`c3-highcpu-22` | 128 | 48 | 32 | 48 | 48 | 0  
`c3-highcpu-44` | 128 | 64 | 32 | 64 | 64 | 0  
`c3-highcpu-88` | 128 | 64 | 32 | 64 | 64 | 8  
`c3-highcpu-176` | 128 | 64 | 32 | 64 | 64 | 8  
`c3-highcpu-192-metal` | 128 | 128 | 16 | Not supported | Not supported | 16  
  
### C3 highmem

| Maximum number of disks |   
---|---|---  
Machine types | Per instance | Hyperdisk  
per instance | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme  
`c3-highmem-4` | 128 | 24 | 16 | 24 | 24 | 0  
`c3-highmem-8` | 128 | 32 | 16 | 32 | 32 | 0  
`c3-highmem-22` | 128 | 48 | 32 | 48 | 48 | 0  
`c3-highmem-44` | 128 | 64 | 32 | 64 | 64 | 0  
`c3-highmem-88` | 128 | 64 | 32 | 64 | 64 | 8  
`c3-highmem-176` | 128 | 64 | 32 | 64 | 64 | 8  
`c3-highmem-192-metal` | 128 | 128 | 16 | Not supported | Not supported | 16  
  
### C3 standard

| Maximum number of disks |   
---|---|---  
Machine types | Per VM1 | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme  
`c3-standard-4-lssd` | 128 | 24 | 16 | 24 | 24 | 0  
`c3-standard-8-lssd` | 128 | 32 | 16 | 32 | 32 | 0  
`c3-standard-22-lssd` | 128 | 48 | 32 | 48 | 48 | 0  
`c3-standard-44-lssd` | 128 | 64 | 32 | 64 | 64 | 0  
`c3-standard-88-lssd` | 128 | 64 | 32 | 64 | 64 | 8  
`c3-standard-176-lssd` | 128 | 64 | 32 | 64 | 64 | 8  
  
### Network support for C3 VMs

The following network interface drivers are required:

  * C3 VM instances require [gVNIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). 
  * C3 bare metal instances require the [Intel IDPF LAN PF device driver](https://docs.cloud.google.com/compute/docs/networking/using-idpf). 



C3 supports up to 100 Gbps network bandwidth for standard networking and up to 200 Gbps with per VM Tier_1 networking performance for VM and bare metal instances.

Before migrating to C3 or creating C3 VMs or bare metal instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the IDPF network driver for bare metal instances or the gVNIC driver for VM instances. To get the best possible performance on C3 VMs, choose an OS image that supports both "Tier_1 Networking" and "200 Gbps network bandwidth". These images include an updated gVNIC driver, even if the guest OS shows the `gve` driver version as 1.0.0. If your C3 VM is using an operating system with an older version of gVNIC driver, this is still supported but the VM might experience suboptimal performance such as less network bandwidth or higher latency.

If you use a custom OS image to create a C3 VM, you can [manually install the most recent gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup). The gVNIC driver version v1.4.2 or later is recommended for use with C3 VMs. Google recommends using the latest gVNIC driver version to benefit from additional features and bug fixes.

### Maintenance experience for C3 instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple _host events_. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background.

The C3 machine series offers the following features related to host maintenance:

Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event)  
---|---|---|---|---  
C3 with Confidential VM | Minimum of 30 days | Terminate | 7 days | No  
`c3-*-lssd` | Minimum of 30 days | Live migrate | 7 days | Yes  
`c3-*-176` | Minimum of 30 days | Live migrate | 7 days | Yes  
`c3-*-192-metal` | Minimum of 30 days | Terminate | 7 days | Yes  
All others | Minimum of 30 days | Live migrate | 7 days | No  
  
The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently.

## N2D machine series

The N2D machine series runs on the third generation [AMD EPYC Milan processor](https://www.amd.com/en/products/processors/server/epyc/7003-series.html) is available only in specific [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones).

The N2D series provides some of the largest general-purpose machine types with up to 224 vCPUs and 896 GB of memory and vCPU to memory ratios of 1:1, 1:4, and 1:8.

In summary, the N2D series:

  * Support up to 224 vCPUs and 896 GB of memory.
  * Support 50 Gbps and 100 Gbps [high-bandwidth network configurations](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration).
  * Available in predefined and custom VMs.
  * Offer higher memory-to-core ratios for VMs created with the extended memory feature. Using the extended memory feature helps you avoid per-CPU software licensing costs while providing access to more than 8 GB of memory per vCPU.
  * Powered by the third generation AMD EPYC Milan processor.
  * Supports the following discount and consumption options: 
    * [Resource-based and flexible committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)
    * [Sustained use discounts (SUDs)](https://docs.cloud.google.com/compute/docs/sustained-use-discounts)
    * [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
    * [Reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type)
  * Doesn't support GPUs or nested virtualization.
  * Supports [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) with AMD SEV and AMD SEV-SNP.



N2D VMs don't support GPUs or nested virtualization.

### N2D machine types

The following table lists the features of the N2D machine series. For some machine types, certain features are not applicable (N/A).

The amount of memory configured per vCPU differs depending on the machine type:

  * `standard`: 4 GB of system memory per vCPU
  * `highmem`: 8 GB of system memory per vCPU
  * `highcpu`: 1 GB of system memory per vCPU



### N2D standard

Machine types | vCPUs1 | Memory (GB) | Local SSD2 | Default egress bandwidth (Gbps)3 | Tier_1 egress bandwidth (Gbps)4  
---|---|---|---|---|---  
`n2d-standard-2` | 2 | 8 | 1, 2, 4, 8, 16, or 24 | Up to 10 | N/A  
`n2d-standard-4` | 4 | 16 | 1, 2, 4, 8, 16, or 24 | Up to 10 | N/A  
`n2d-standard-8` | 8 | 32 | 1, 2, 4, 8, 16, or 24 | Up to 16 | N/A  
`n2d-standard-16` | 16 | 64 | 1, 2, 4, 8, 16, or 24 | Up to 32 | N/A  
`n2d-standard-32` | 32 | 128 | 2, 4, 8, 16, or 24 | Up to 32 | N/A  
`n2d-standard-48` | 48 | 192 | 2, 4, 8, 16, or 24 | Up to 32 | Up to 50  
`n2d-standard-64` | 64 | 256 | 4, 8, 16, or 24 | Up to 32 | Up to 50  
`n2d-standard-80` | 80 | 320 | 4, 8, 16, or 24 | Up to 32 | Up to 50  
`n2d-standard-96` | 96 | 384 | 8, 16, or 24 | Up to 32 | Up to 100  
`n2d-standard-128` | 128 | 512 | 8, 16, or 24 | Up to 32 | Up to 100  
`n2d-standard-224` | 224 | 896 | 8, 16, or 24 | Up to 32 | Up to 100  
  
1 Each CPU uses two threads per core. A vCPU is implemented as a single hardware thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).   
2 Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
3 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
4 Supports [ high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. For Windows OS images, the maximum network bandwidth is limited to 50 Gbps. 

### N2D high-mem

Machine types | vCPUs1 | Memory (GB) | Local SSD2 | Default egress bandwidth (Gbps)3 | Tier_1 egress bandwidth (Gbps)4  
---|---|---|---|---|---  
`n2d-highmem-2` | 2 | 16 | 1, 2, 4, 8, 16, or 24 | Up to 10 | N/A  
`n2d-highmem-4` | 4 | 32 | 1, 2, 4, 8, 16, or 24 | Up to 10 | N/A  
`n2d-highmem-8` | 8 | 64 | 1, 2, 4, 8, 16, or 24 | Up to 16 | N/A  
`n2d-highmem-16` | 16 | 128 | 1, 2, 4, 8, 16, or 24 | Up to 32 | N/A  
`n2d-highmem-32` | 32 | 256 | 2, 4, 8, 16, or 24 | Up to 32 | N/A  
`n2d-highmem-48` | 48 | 384 | 2, 4, 8, 16, or 24 | Up to 32 | Up to 50  
`n2d-highmem-64` | 64 | 512 | 4, 8, 16, or 24 | Up to 32 | Up to 50  
`n2d-highmem-80` | 80 | 640 | 4, 8, 16, or 24 | Up to 32 | Up to 50  
`n2d-highmem-96` | 96 | 768 | 8, 16, or 24 | Up to 32 | Up to 100  
  
1 Each CPU uses two threads per core. A vCPU is implemented as a single hardware thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).   
2 Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
3 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
4 Supports [ high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. For Windows OS images, the maximum network bandwidth is limited to 50 Gbps. 

### N2D high-cpu

Machine types | vCPUs1 | Memory (GB) | Local SSD2 | Default egress bandwidth (Gbps)3 | Tier_1 egress bandwidth (Gbps)4  
---|---|---|---|---|---  
`n2d-highcpu-2` | 2 | 2 | 1, 2, 4, 8, 16, or 24 | Up to 10 | N/A  
`n2d-highcpu-4` | 4 | 4 | 1, 2, 4, 8, 16, or 24 | Up to 10 | N/A  
`n2d-highcpu-8` | 8 | 8 | 1, 2, 4, 8, 16, or 24 | Up to 16 | N/A  
`n2d-highcpu-16` | 16 | 16 | 1, 2, 4, 8, 16, or 24 | Up to 32 | N/A  
`n2d-highcpu-32` | 32 | 32 | 2, 4, 8, 16, or 24 | Up to 32 | N/A  
`n2d-highcpu-48` | 48 | 48 | 2, 4, 8, 16, or 24 | Up to 32 | Up to 50  
`n2d-highcpu-64` | 64 | 64 | 4, 8, 16, or 24 | Up to 32 | Up to 50  
`n2d-highcpu-80` | 80 | 80 | 4, 8, 16, or 24 | Up to 32 | Up to 50  
`n2d-highcpu-96` | 96 | 96 | 8, 16, or 24 | Up to 32 | Up to 100  
`n2d-highcpu-128` | 128 | 128 | 8, 16, or 24 | Up to 32 | Up to 100  
`n2d-highcpu-224` | 224 | 224 | 8, 16, or 24 | Up to 32 | Up to 100  
  
1 Each CPU uses two threads per core. A vCPU is implemented as a single hardware thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).   
2 Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
3 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
4 Supports [ high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. For Windows OS images, the maximum network bandwidth is limited to 50 Gbps. 

For details on the pricing information, see the following:

  * For machine type pricing, see [VM pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#n2d_machine_types).
  * Disk usage and network usage is charged separately from machine type pricing. For details, see [Disk and image pricing](https://docs.cloud.google.com/compute/disks-image-pricing#disks) and [Network pricing](https://cloud.google.com/vpc/network-pricing).
  * For per VM Tier_1 network performance billing rates, see [Tier_1 higher bandwidth network pricing](https://cloud.google.com/products/compute/pricing/general-purpose#tier-1-higher-bandwidth-network-pricing).



### Supported disk types for N2D

N2D VMs can use the following block storage types:

  * Zonal and regional standard Persistent Disk (`pd-standard`)
  * Zonal and regional balanced Persistent Disk (`pd-balanced`)
  * Zonal and regional SSD Persistent Disk (`pd-ssd`)
  * Hyperdisk Balanced (`hyperdisk-balanced`)1
  * Hyperdisk Balanced High Availability (`hyperdisk-balanced-high-availability`)1
  * Hyperdisk Throughput (`hyperdisk-throughput`)
  * Local SSD



1 To use Hyperdisk Balanced or Hyperdisk Balanced High Availability with this machine series, you must [contact your account team](https://docs.cloud.google.com/tam). For more information, see [Design for flexibility on older machine series](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#gen2-hyperdisk_name_short). 

### N2D standard

Machine types | Max number of disks per VM,   
across all disks1 | Max number of Hyperdisk  
volumes per VM2 | Max total disk size (TiB)  
across all disks3  
---|---|---|---  
`n2d-standard-2` | 128 | 20 | 257  
`n2d-standard-4` | 128 | 24 | 257  
`n2d-standard-8` | 128 | 32 | 257  
`n2d-standard-16` | 128 | 48 | 257  
`n2d-standard-32` | 128 | 64 | 512  
`n2d-standard-48` | 128 | 64 | 512  
`n2d-standard-64` | 128 | 64 | 512  
`n2d-standard-80` | 128 | 64 | 512  
`n2d-standard-96` | 128 | 64 | 512  
`n2d-standard-128` | 128 | 64 | 512  
`n2d-standard-224` | 128 | 64 | 512  
  
1 The maximum size per Persistent Disk volume is 64 TiB.

2 The maximum size per Hyperdisk Throughput volume is 32 TiB.

3 The maximum total disk size applies to all Persistent Disk and Hyperdisk disk types attached to the VM. 

### N2D high-mem

Machine types | Max number of disks per VM,   
across all disks1 | Max number of Hyperdisk  
volumes per VM2 | Max total disk size (TiB)  
across all disks3  
---|---|---|---  
`n2d-highmem-2` | 128 | 20 | 257  
`n2d-highmem-4` | 128 | 24 | 257  
`n2d-highmem-8` | 128 | 32 | 257  
`n2d-highmem-16` | 128 | 48 | 257  
`n2d-highmem-32` | 128 | 64 | 512  
`n2d-highmem-48` | 128 | 64 | 512  
`n2d-highmem-64` | 128 | 64 | 512  
`n2d-highmem-80` | 128 | 64 | 512  
`n2d-highmem-96` | 128 | 64 | 512  
  
1 The maximum size per Persistent Disk volume is 64 TiB.

2 The maximum size per Hyperdisk Throughput volume is 32 TiB.

3 The maximum total disk size applies to all Persistent Disk and Hyperdisk disk types attached to the VM. 

### N2D high-cpu

Machine types | Max number of disks per VM,   
across all disks1 | Max number of Hyperdisk  
volumes per VM2 | Max total disk size (TiB)  
across all disks3  
---|---|---|---  
`n2d-highcpu-2` | 128 | 20 | 257  
`n2d-highcpu-4` | 128 | 24 | 257  
`n2d-highcpu-8` | 128 | 32 | 257  
`n2d-highcpu-16` | 128 | 48 | 257  
`n2d-highcpu-32` | 128 | 64 | 512  
`n2d-highcpu-48` | 128 | 64 | 512  
`n2d-highcpu-64` | 128 | 64 | 512  
`n2d-highcpu-80` | 128 | 64 | 512  
`n2d-highcpu-96` | 128 | 64 | 512  
`n2d-highcpu-128` | 128 | 64 | 512  
`n2d-highcpu-224` | 128 | 64 | 512  
  
1 The maximum size per Persistent Disk volume is 64 TiB.

2 The maximum size per Hyperdisk Throughput volume is 32 TiB.

3 The maximum total disk size applies to all Persistent Disk and Hyperdisk disk types attached to the VM. 

## N2 machine series

The N2 machine series has flexible sizing between 2 to 128 vCPUs and 0.5 to 8 GB of memory per vCPU. Machine types in this series run on the following processors:

  * Ice Lake—offered in specific [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones). It is the default processor for larger machine types.

  * Cascade Lake—the default for machine types up to 80 vCPUs. If you want to create VMs with `Ice Lake`, you must set it as the [minimum CPU platform](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform#startinginstancewithmincpuplatform).




You can find more details about these two processors on the [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel_cpu_processors) page.

N2 VMs with vNUMA enabled are split into vNUMA nodes based on the number of vCPUs in the VM. This applies for both custom and predefined machine types.

Family | vCPUS | vNUMA Nodes  
---|---|---  
n2 (Cascade Lake) | < 32 | 1  
n2 (Cascade Lake) | >= 32 | 2  
n2 (Ice Lake) | <= 48 | 1  
n2 (Ice Lake) | > 48 | 2  
  
Workloads that can take advantage of the higher clock frequency are a good choice for this series. These workloads can get higher per-thread performance while benefiting from all the flexibility that the general-purpose machine family offers.

In summary, the N2 machine series:

  * Supports up to 128 vCPUs and 864 GB of memory.
  * Supports 50 Gbps, 75 Gbps, and 100 Gbps [high-bandwidth network configurations](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration).
  * Is available in predefined and custom VMs.
  * Has higher memory-to-core ratios for VMs created with the extended memory feature. Using the extended memory feature helps control per-CPU software licensing costs while providing access to more than 8 GB of memory per vCPU.
  * Supports the following discount and consumption options: 
    * [Resource-based and flexible committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)
    * [Sustained use discounts (SUDs)](https://docs.cloud.google.com/compute/docs/sustained-use-discounts)
    * [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
    * [Reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type)



### N2 machine types

The amount of memory configured per vCPU differs depending on the machine type:

  * `standard`: 4 GB of system memory per vCPU
  * `highmem`: 8 GB of system memory per vCPU
  * `highcpu`: 1 GB of system memory per vCPU



### N2 standard

Machine types | vCPUs1 | Memory (GB) | Local SSD2 | Default egress bandwidth (Gbps)3 | Tier_1 egress bandwidth (Gbps)4  
---|---|---|---|---|---  
`n2-standard-2` | 2 | 8 | 1, 2, 4, 8, 16, or 24 | Up to 10 | N/A  
`n2-standard-4` | 4 | 16 | 1, 2, 4, 8, 16, or 24 | Up to 10 | N/A  
`n2-standard-8` | 8 | 32 | 1, 2, 4, 8, 16, or 24 | Up to 16 | N/A  
`n2-standard-16` | 16 | 64 | 2, 4, 8, 16, or 24 | Up to 32 | N/A  
`n2-standard-32` | 32 | 128 | 4, 8, 16, or 24 | Up to 32 | Up to 50  
`n2-standard-48` | 48 | 192 | 8, 16, or 24 | Up to 32 | Up to 50  
`n2-standard-64` | 64 | 256 | 8, 16, or 24 | Up to 32 | Up to 75  
`n2-standard-80` | 80 | 320 | 8, 16, or 24 | Up to 32 | Up to 100  
`n2-standard-96` | 96 | 384 | 16 or 24 | Up to 32 | Up to 100  
`n2-standard-128` | 128 | 512 | 16 or 24 | Up to 32 | Up to 100  
  
1 Each CPU uses two threads per core. A vCPU is implemented as a single hardware thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
3 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
4 Supports [ high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. For Windows OS images, the maximum network bandwidth is limited to 50 Gbps. 

### N2 high-mem

Machine types | vCPUs1 | Memory (GB) | Local SSD2 | Default egress bandwidth (Gbps)3 | Tier_1 egress bandwidth (Gbps)4  
---|---|---|---|---|---  
`n2-highmem-2` | 2 | 16 | 1, 2, 4, 8, 16, or 24 | Up to 10 | N/A  
`n2-highmem-4` | 4 | 32 | 1, 2, 4, 8, 16, or 24 | Up to 10 | N/A  
`n2-highmem-8` | 8 | 64 | 1, 2, 4, 8, 16, or 24 | Up to 16 | N/A  
`n2-highmem-16` | 16 | 128 | 1, 2, 4, 8, 16, or 24 | Up to 32 | N/A  
`n2-highmem-32` | 32 | 256 | 4, 8, 16, or 24 | Up to 32 | Up to 50  
`n2-highmem-48` | 48 | 384 | 8, 16, or 24 | Up to 32 | Up to 50  
`n2-highmem-64` | 64 | 512 | 8, 16, or 24 | Up to 32 | Up to 75  
`n2-highmem-80` | 80 | 640 | 8, 16, or 24 | Up to 32 | Up to 100  
`n2-highmem-96` | 96 | 768 | 16 or 24 | Up to 32 | Up to 100  
`n2-highmem-128` | 128 | 864 | 16 or 24 | Up to 32 | Up to 100  
  
1 Each CPU uses two threads per core. A vCPU is implemented as a single hardware thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
3 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
4 Supports [ high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. For Windows OS images, the maximum network bandwidth is limited to 50 Gbps. 

### N2 high-cpu

Machine types | vCPUs1 | Memory (GB) | Local SSD2 | Default egress bandwidth (Gbps)3 | Tier_1 egress bandwidth (Gbps)4  
---|---|---|---|---|---  
`n2-highcpu-2` | 2 | 2 | 1, 2, 4, 8, 16, or 24 | Up to 10 | N/A  
`n2-highcpu-4` | 4 | 4 | 1, 2, 4, 8, 16, or 24 | Up to 10 | N/A  
`n2-highcpu-8` | 8 | 8 | 1, 2, 4, 8, 16, or 24 | Up to 16 | N/A  
`n2-highcpu-16` | 16 | 16 | 2, 4, 8, 16, or 24 | Up to 32 | N/A  
`n2-highcpu-32` | 32 | 32 | 4, 8, 16, or 24 | Up to 32 | Up to 50  
`n2-highcpu-48` | 48 | 48 | 8, 16, or 24 | Up to 32 | Up to 50  
`n2-highcpu-64` | 64 | 64 | 8, 16, or 24 | Up to 32 | Up to 75  
`n2-highcpu-80` | 80 | 80 | 8, 16, or 24 | Up to 32 | Up to 100  
`n2-highcpu-96` | 96 | 96 | 16 or 24 | Up to 32 | Up to 100  
  
1 Each CPU uses two threads per core. A vCPU is implemented as a single hardware thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
3 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
4 Supports [ high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. For Windows OS images, the maximum network bandwidth is limited to 50 Gbps. 

For details on the pricing information, see the following:

  * For machine type pricing, see [VM pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#n2_predefined).
  * Disk usage and network usage is charged separately from machine type pricing. For details, see [Disk and image pricing](https://docs.cloud.google.com/compute/disks-image-pricing#disks) and [Network pricing](https://cloud.google.com/vpc/network-pricing).
  * For per VM Tier_1 network performance billing rates, see [Tier_1 higher bandwidth network pricing](https://cloud.google.com/products/compute/pricing/general-purpose#tier-1-higher-bandwidth-network-pricing).



### Supported disk types for N2

N2 VMs can use the following block storage types:

  * Zonal and regional standard Persistent Disk (`pd-standard`)
  * Zonal and regional balanced Persistent Disk (`pd-balanced`)
  * Zonal and regional SSD Persistent Disk (`pd-ssd`)
  * Extreme Persistent Disk (`pd-extreme`)
  * Hyperdisk Balanced (`hyperdisk-balanced`)1
  * Hyperdisk Balanced High Availability (`hyperdisk-balanced-high-availability`)1
  * Hyperdisk Extreme (`hyperdisk-extreme`). Not supported with custom N2 machine types.
  * Hyperdisk Throughput (`hyperdisk-throughput`)
  * Local SSD



1 To use Hyperdisk Balanced or Hyperdisk Balanced High Availability with this machine series, you must [contact your account team](https://docs.cloud.google.com/tam). For more information, see [ Design for flexibility on older machine series](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#gen2-hyperdisk_name_short). 

### N2 standard

Machine types | Max number of disks per VM,   
across all disks1 | Max number of Hyperdisk Extreme  
volumes per VM2 | Max number of Hyperdisk Throughput  
volumes per VM2 | Max total disk size (TiB)  
across all disks3  
---|---|---|---|---  
`n2-standard-2` | 128 | 0 | 20 | 257  
`n2-standard-4` | 128 | 0 | 24 | 257  
`n2-standard-8` | 128 | 0 | 32 | 257  
`n2-standard-16` | 128 | 0 | 48 | 257  
`n2-standard-32` | 128 | 0 | 64 | 512  
`n2-standard-48` | 128 | 0 | 64 | 512  
`n2-standard-64` | 128 | 0 | 64 | 512  
`n2-standard-80` | 128 | 8 | 64 | 512  
`n2-standard-96` | 128 | 8 | 64 | 512  
`n2-standard-128` | 128 | 8 | 64 | 512  
  
1 The maximum size per Persistent Disk volume is 64 TiB.

2 The maximum size per Hyperdisk Extreme volume is 64 TiB. The maximum size per Hyperdisk Throughput volume is 32 TiB.

3 You can attach a mixture of Hyperdisk and Persistent Disk volumes to a VM, but the total Persistent Disk capacity can't exceed 257 TiB. 

### N2 high-mem

Machine types | Max number of disks per VM,   
across all disks* | Max number of Hyperdisk Extreme  
volumes per VM† | Max number of Hyperdisk Throughput  
volumes per VM† | Max total disk size (TiB)  
across all disks‡  
---|---|---|---|---  
`n2-highmem-2` | 128 | 0 | 20 | 257  
`n2-highmem-4` | 128 | 0 | 24 | 257  
`n2-highmem-8` | 128 | 0 | 32 | 257  
`n2-highmem-16` | 128 | 0 | 48 | 257  
`n2-highmem-32` | 128 | 0 | 64 | 512  
`n2-highmem-48` | 128 | 0 | 64 | 512  
`n2-highmem-64` | 128 | 0 | 64 | 512  
`n2-highmem-80` | 128 | 8 | 64 | 512  
`n2-highmem-96` | 128 | 8 | 64 | 512  
`n2-highmem-128` | 128 | 8 | 64 | 512  
  
1 The maximum size per Persistent Disk volume is 64 TiB.

2 The maximum size per Hyperdisk Extreme volume is 64 TiB. The maximum size per Hyperdisk Throughput volume is 32 TiB.

3 You can attach a mixture of Hyperdisk and Persistent Disk volumes to a VM, but the total Persistent Disk capacity can't exceed 257 TiB. 

### N2 high-cpu

Machine types | Max number of disks per VM,   
across all disks* | Max number of Hyperdisk Extreme  
volumes per VM† | Max number of Hyperdisk Throughput  
volumes per VM† | Max total disk size (TiB)  
across all disks‡  
---|---|---|---|---  
`n2-highcpu-2` | 128 | 0 | 20 | 257  
`n2-highcpu-4` | 128 | 0 | 24 | 257  
`n2-highcpu-8` | 128 | 0 | 32 | 257  
`n2-highcpu-16` | 128 | 0 | 48 | 257  
`n2-highcpu-32` | 128 | 0 | 64 | 512  
`n2-highcpu-48` | 128 | 0 | 64 | 512  
`n2-highcpu-64` | 128 | 0 | 64 | 512  
`n2-highcpu-80` | 128 | 8 | 64 | 512  
`n2-highcpu-96` | 128 | 8 | 64 | 512  
  
1 The maximum size per Persistent Disk volume is 64 TiB.

2 The maximum size per Hyperdisk Extreme volume is 64 TiB. The maximum size per Hyperdisk Throughput volume is 32 TiB.

3 You can attach a mixture of Hyperdisk and Persistent Disk volumes to a VM, but the total Persistent Disk capacity can't exceed 257 TiB. 

## E2 machine series

The cost-optimized E2 machine series have between 2 to 32 vCPUs with a ratio of 0.5 GB to 8 GB of memory per vCPU for standard VMs, and 0.25 to 1 vCPUs with 0.5 GB to 8 GB of memory for shared-core E2 machine types. The E2 machine series offers both Intel and AMD EPYC processors. The processor is selected for you at the time of VM creation. Machine types in this series are available in all regions and zones and support a [virtio memory balloon device](https://docs.cloud.google.com/compute/docs/dynamic-resource-management#virtio-memory-device).

In summary, the E2 machine series:

  * Supports up to 32 vCPUs and up to 128 GB of memory for predefined machine types, or up to 256 GB of memory for custom machine types.
  * Supports Intel and AMD EPYC Milan processors.
  * Is available in predefined and custom VMs.
  * Offers the lowest on demand pricing across the general-purpose machine types.
  * Supports the following discount and consumption options: 
    * [Resource-based and flexible committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)
    * [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
    * [Reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type)
  * Doesn't offer [sustained use discounts (SUDs)](https://docs.cloud.google.com/compute/docs/sustained-use-discounts); however, it provides consistently low on-demand and committed-use pricing.
  * Doesn't support GPUs, Local SSDs, sole-tenant nodes, or nested virtualization.



### Shared-core VMs

E2 shared-core machine types are cost-effective, have a virtio memory balloon device, and are ideal for small workloads. The E2 machine series shared-core machine types use context-switching for multi-tasking, and time-share a single physical core for a specific fraction of time. Different shared-core machine types sustain different amounts of time on a physical core.

  * `e2-micro` sustains 2 vCPUs, each for 12.5% of [CPU time](https://wikipedia.org/wiki/CPU_time) totaling 25% CPU time.
  * `e2-small` sustains 2 vCPUs, each at 25% of CPU time, totaling 50% CPU time.
  * `e2-medium` sustains 2 vCPUs, each at 50% of CPU time, totaling 100% CPU time.



Unlike predefined machine types and custom machine types, shared-core machine types have a predefined price that includes both vCPUs and memory. For more information, see [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#e2_sharedcore_machine_types).

#### CPU bursting

Shared-core machine types offer bursting capabilities that allow instances to use additional physical CPU for short periods of time. Bursting happens automatically when your VM requires more physical CPU than originally allocated. During these spikes, each vCPU can burst up to 100% of CPU time, for short periods, before returning to their normal CPU time sharing limitations. Note that bursts are not permanent and are only possible periodically.

`e2-micro`, `e2-small`, and `e2-medium` shared-core VMs can burst for dozens of seconds. If the CPU is utilized at 100%, then the burst lasts as follows:

  * `e2-micro`: 30 seconds
  * `e2-small`: 60 seconds
  * `e2-medium` 120 seconds



The exact burst time is determined by a [Token bucket](https://wikipedia.org/wiki/Token_bucket) meaning utilizing the CPU less than 100% will result in longer bursts.

Bursting doesn't incur any additional charges. You are charged the listed on-demand price for E2 shared-core and N1 `f1-micro`, and `g1-small` shared-core VMs. 

### E2 Limitations

  * The E2 machine series doesn't offer sustained use discounts (SUDs); however, it provides consistently low on-demand and committed-use pricing.
  * The E2 machine series doesn't support GPUs, Local SSDs, sole-tenant nodes, or nested virtualization.



### E2 machine types

E2 is available in `standard`, `highmem`, and `highcpu` configurations, as well as shared-core machine type. In general, E2 shared-core machine types can be more cost-effective for running small, non-resource intensive applications than standard, high-memory, or high-CPU machine types.

The amount of memory configured per vCPU differs depending on the machine type:

  * `standard`: 4 GB of system memory per vCPU
  * `highmem`: 8 GB of system memory per vCPU
  * `highcpu`: 1 GB of system memory per vCPU
  * Shared core: 
    * `micro`: 0.5 GB of system memory per vCPU
    * `small`: 1 GB of system memory per vCPU
    * `medium`: 2 GB of system memory per vCPU



### E2 standard

Machine types | vCPUs | Memory (GB) | Local SSD | Max number of Persistent Disk (PDs)1 | Max total PD size (TiB) | Maximum egress bandwidth (Gbps)2  
---|---|---|---|---|---|---  
`e2-standard-2` | 2 | 8 | No | 128 | 257 | Up to 4  
`e2-standard-4` | 4 | 16 | No | 128 | 257 | Up to 8  
`e2-standard-8` | 8 | 32 | No | 128 | 257 | Up to 16  
`e2-standard-16` | 16 | 64 | No | 128 | 257 | Up to 16  
`e2-standard-32` | 32 | 128 | No | 128 | 257 | Up to 16  
  
1 Persistent Disk and Hyperdisk usage is charged separately from [machine pricing](https://cloud.google.com/compute/vm-instance-pricing).  
2 Maximum egress bandwidth cannot exceed the number given. Actual See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth). 

### E2 high-mem

Machine types | vCPUs | Memory (GB) | Local SSD | Max number of Persistent Disk (PDs)1 | Max total Persistent Disk size (TiB) | Maximum egress bandwidth (Gbps)2  
---|---|---|---|---|---|---  
`e2-highmem-2` | 2 | 16 | No | 128 | 257 | Up to 4  
`e2-highmem-4` | 4 | 32 | No | 128 | 257 | Up to 8  
`e2-highmem-8` | 8 | 64 | No | 128 | 257 | Up to 16  
`e2-highmem-16` | 16 | 128 | No | 128 | 257 | Up to 16  
  
1 Persistent Disk and Hyperdisk usage is charged separately from [machine pricing](https://cloud.google.com/compute/vm-instance-pricing).  
2Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth). 

### E2 high-cpu

Machine types | vCPUs | Memory (GB) | Local SSD | Max number of Persistent Disk (PDs)1 | Max total PD size (TiB) | Maximum egress bandwidth (Gbps)2  
---|---|---|---|---|---|---  
`e2-highcpu-2` | 2 | 2 | No | 128 | 257 | Up to 4  
`e2-highcpu-4` | 4 | 4 | No | 128 | 257 | Up to 8  
`e2-highcpu-8` | 8 | 8 | No | 128 | 257 | Up to 16  
`e2-highcpu-16` | 16 | 16 | No | 128 | 257 | Up to 16  
`e2-highcpu-32` | 32 | 32 | No | 128 | 257 | Up to 16  
  
1 Persistent Disk and Hyperdisk usage is charged separately from [machine pricing](https://cloud.google.com/compute/vm-instance-pricing).   
2 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth). 

### E2 shared-core

Machine types | vCPUs | Fractional vCPUs1 | Memory (GB) | Local SSD | Max number of Persistent Disk (PDs)2 | Max total PD size (TiB) | Maximum egress bandwidth (Gbps)3  
---|---|---|---|---|---|---|---  
`e2-micro` | 2 | 0.251 | 1 | No | 16 | 3 | Up to 1  
`e2-small` | 2 | 0.51 | 2 | No | 16 | 3 | Up to 1  
`e2-medium` | 2 | 11 | 4 | No | 16 | 3 | Up to 2  
  
1 Fractional vCPU of 0.25, 0.5, or 1.0 with 2 vCPUs exposed to the guest operating system.  
2 Persistent Disk and Hyperdisk usage is charged separately from [machine pricing](https://cloud.google.com/compute/vm-instance-pricing).   
3 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth). 

### Supported disk types for E2 VMs

E2 VMs can use the following block storage types:

  * Zonal and regional balanced Persistent Disk (`pd-balanced`)
  * Zonal and regional SSD Persistent Disk (`pd-ssd`)
  * Zonal and regional standard Persistent Disk (`pd-standard`)
  * Hyperdisk Balanced (`hyperdisk-balanced`)1
  * Hyperdisk Balanced High Availability (`hyperdisk-balanced-high-availability`)1



1 To use Hyperdisk Balanced or Hyperdisk Balanced High Availability with this machine series, you must [contact your account team](https://docs.cloud.google.com/tam). For more information, see [Design for flexibility on older machine series](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#gen2-hyperdisk_name_short). 

## N1 machine series

The N1 machine series is Compute Engine's first generation general-purpose machine series available on Intel Skylake, Broadwell, Haswell, Sandy Bridge, and Ivy Bridge CPU platforms.

In summary, the N1 machine series offers the following features:

  * Supports up to 96 vCPUs and 624 GB of memory.
  * Has both predefined machine types and custom machine types. Custom machine types can be created within a wide range of memory-to-core ratio, ranging from 1 GB per vCPU to 6.5 GB per vCPU.
  * Offers higher memory-to-core ratios for VMs created with the extended memory feature.
  * Supports the following discount and consumption options: 
    * [Resource-based and flexible committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)
    * [Sustained use discounts (SUDs)](https://docs.cloud.google.com/compute/docs/sustained-use-discounts); N1 machine series offers a higher SUD percentage than the N2 machine series.
    * [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
    * [Reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type)
  * Supports [Tensor Processing Units (TPUs)](https://docs.cloud.google.com/tpu/docs/tpus) in select [zones](https://docs.cloud.google.com/tpu/docs/types-zones).
  * Can support up to [ten virtual interfaces per instance](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#max-interfaces).



### N1 machine types

N1 is available in `standard`, `highmem`, and `highcpu` configurations, as well as shared-core machine types. Different shared-core machine types sustain different amounts of time on a physical core.

  * An `f1-micro` VM instance sustains a single vCPU for up to 20% of [CPU time](https://wikipedia.org/wiki/CPU_time).
  * A `g1-small` VM instance sustains a single vCPU for up to 50% of CPU time.



The amount of memory configured per vCPU differs depending on the machine type:

  * `standard`: 3.75 GB of system memory per vCPU
  * `highmem`: 6.5 GB of system memory per vCPU
  * `highcpu`: 0.9 GB of system memory per vCPU
  * Shared core: 
    * `f1-micro`: 0.6 GB of system memory per vCPU
    * `g1-small`: 1.7 GB of system memory per vCPU



### N1 standard

Machine types | vCPUs1 | Memory (GB) | Local SSD2 | Max number of Persistent Disk3 | Max total disk size (TiB) | Default egress bandwidth (Gbps)4 | Tier_1 egress bandwidth (Gbps)  
---|---|---|---|---|---|---|---  
`n1-standard-1` | 1 | 3.75 | 1 to 8, 16, or 24 | 128 | 257 | Up to 2 | N/A  
`n1-standard-2` | 2 | 7.50 | 1 to 8, 16, or 24 | 128 | 257 | Up to 10 | N/A  
`n1-standard-4` | 4 | 15 | 1 to 8, 16, or 24 | 128 | 257 | Up to 10 | N/A  
`n1-standard-8` | 8 | 30 | 1 to 8, 16, or 24 | 128 | 257 | Up to 16 | N/A  
`n1-standard-16` | 16 | 60 | 1 to 8, 16, or 24 | 128 | 257 | Up to 325 | N/A  
`n1-standard-32` | 32 | 120 | 1 to 8, 16, or 24 | 128 | 257 | Up to 325 | N/A  
`n1-standard-64` | 64 | 240 | 1 to 8, 16, or 24 | 128 | 257 | Up to 325 | N/A  
`n1-standard-96` | 96 | 360 | 1 to 8, 16, or 24 | 128 | 257 | Up to 325 | N/A  
  
1 Each CPU uses two threads per core. A vCPU is implemented as a single hardware thread.  
2 Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
3 Persistent Disk and Hyperdisk usage is charged separately from [machine type pricing](https://cloud.google.com/compute/vm-instance-pricing).   
4 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
5 32 Gbps for Skylake or later [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms). 16 Gbps for all other platforms.

### N1 high-memory

Machine types | vCPUs1 | Memory (GB) | Local SSD2 | Max number of Persistent Disk3 | Max total disk size (TiB) | Default egress bandwidth (Gbps)4 | Tier_1 egress bandwidth (Gbps)  
---|---|---|---|---|---|---|---  
`n1-highmem-2` | 2 | 13 | 1 to 8, 16, or 24 | 128 | 257 | Up to 10 | N/A  
`n1-highmem-4` | 4 | 26 | 1 to 8, 16, or 24 | 128 | 257 | Up to 10 | N/A  
`n1-highmem-8` | 8 | 52 | 1 to 8, 16, or 24 | 128 | 257 | Up to 16 | N/A  
`n1-highmem-16` | 16 | 104 | 1 to 8, 16, or 24 | 128 | 257 | Up to 325 | N/A  
`n1-highmem-32` | 32 | 208 | 1 to 8, 16, or 24 | 128 | 257 | Up to 325 | N/A  
`n1-highmem-64` | 64 | 416 | 1 to 8, 16, or 24 | 128 | 257 | Up to 325 | N/A  
`n1-highmem-96` | 96 | 624 | 1 to 8, 16, or 24 | 128 | 257 | Up to 325 | N/A  
  
1 Each CPU uses two threads per core. A vCPU is implemented as a single hardware thread.  
2 Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
3 Persistent Disk and Hyperdisk usage is charged separately from [machine type pricing](https://cloud.google.com/compute/vm-instance-pricing).   
4 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
5 32 Gbps for Skylake or later [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms). 16 Gbps for all other platforms.

### N1 high-cpu

Machine types | vCPUs1 | Memory (GB) | Local SSD2 | Max number of Persistent Disk3 | Max total disk size (TiB) | Default egress bandwidth (Gbps)4 | Tier_1 egress bandwidth (Gbps)  
---|---|---|---|---|---|---|---  
`n1-highcpu-2` | 2 | 1.80 | 1 to 8, 16, or 24 | 128 | 257 | Up to 10 | N/A  
`n1-highcpu-4` | 4 | 3.60 | 1 to 8, 16, or 24 | 128 | 257 | Up to 10 | N/A  
`n1-highcpu-8` | 8 | 7.20 | 1 to 8, 16, or 24 | 128 | 257 | Up to 16 | N/A  
`n1-highcpu-16` | 16 | 14.4 | 1 to 8, 16, or 24 | 128 | 257 | Up to 325 | N/A  
`n1-highcpu-32` | 32 | 28.8 | 1 to 8, 16, or 24 | 128 | 257 | Up to 325 | N/A  
`n1-highcpu-64` | 64 | 57.6 | 1 to 8, 16, or 24 | 128 | 257 | Up to 325 | N/A  
`n1-highcpu-96` | 96 | 86.4 | 1 to 8, 16, or 24 | 128 | 257 | Up to 325 | N/A  
  
1 Each CPU uses two threads per core. A vCPU is implemented as a single hardware thread.  
2 Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
3 Persistent Disk and Hyperdisk usage is charged separately from [machine type pricing](https://cloud.google.com/compute/vm-instance-pricing).   
4 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
5 32 Gbps for Skylake or later [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms). 16 Gbps for all other platforms.

### N1 shared-core 

Machine types | vCPUs | Fractional vCPUs1 | Memory (GB) | Local SSD | Max number of Persistent Disk2 | Max total disk size (TiB) | Maximum egress bandwidth (Gbps)3  
---|---|---|---|---|---|---|---  
`f1-micro` | 1 | 0.21 | 0.60 | No | 16 | 3 | Up to 1  
`g1-small` | 1 | 0.51 | 1.70 | No | 16 | 3 | Up to 1  
  
1 Fractional vCPU of 0.2 or 0.5, with 1 vCPU exposed to the guest operating system.  
2 Persistent Disk and Hyperdisk usage is charged separately from [VM pricing](https://cloud.google.com/compute/vm-instance-pricing).  
3 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth). 

### Supported disk types for N1 VMs

N1 VMs can use the following block storage types:

  * Zonal and regional balanced Persistent Disk (`pd-balanced`)
  * Zonal and regional SSD Persistent Disk (`pd-ssd`)
  * Zonal and regional standard Persistent Disk (`pd-standard`)
  * Hyperdisk Balanced (`hyperdisk-balanced`)1
  * Hyperdisk Balanced High Availability (`hyperdisk-balanced-high-availability`)1
  * Local SSD disks



1 To use Hyperdisk Balanced or Hyperdisk Balanced High Availability with this machine series, you must [contact your account team](https://docs.cloud.google.com/tam). For more information, see [Design for flexibility on older machine series](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#gen2-hyperdisk_name_short). 

## Tau T2A machine series

The Tau T2A machine series runs on the Ampere Altra Arm processor with a base frequency of 3.0 GHz. Tau T2A offers predefined machine types with 1 to 48 vCPUs, supports 4 GB of memory per vCPU, and offers a maximum of 32 Gbps of outbound data transfer.

This series is available only in select [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

The Tau T2A machine series doesn't support simultaneous multithreading (SMT); each vCPU is equivalent to an entire core.

### Tau T2A machine types

Tau T2A standard machine types have 4 GB of system memory per vCPU.

Machine types | vCPUs* | Memory (GB) | Local SSD | Max number of Persistent Disk (PDs)† | Max total PD size (TiB) | Default egress bandwidth (Gbps)‡ | Tier_1 egress bandwidth (Gbps)  
---|---|---|---|---|---|---|---  
`t2a-standard-1` | 1 | 4 | No | 128 | 257 | Up to 10 | N/A  
`t2a-standard-2` | 2 | 8 | No | 128 | 257 | Up to 10 | N/A  
`t2a-standard-4` | 4 | 16 | No | 128 | 257 | Up to 10 | N/A  
`t2a-standard-8` | 8 | 32 | No | 128 | 257 | Up to 16 | N/A  
`t2a-standard-16` | 16 | 64 | No | 128 | 257 | Up to 32 | N/A  
`t2a-standard-32` | 32 | 128 | No | 128 | 257 | Up to 32 | N/A  
`t2a-standard-48` | 48 | 192 | No | 128 | 257 | Up to 32 | N/A  
  
1 SMT is not supported. Each vCPU is equivalent to an entire core. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth). 

### Tau T2A Limitations

The Tau T2A machine series doesn't support:

  * [Custom machine types](https://docs.cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types)
  * [Sole tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes)
  * [Nested virtualization](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview)
  * [Extreme Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/extreme-persistent-disk)
  * [Local SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd)
  * [Regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/high-availability-regional-persistent-disk)
  * Virtio-SCSI Storage Controller and Virtio-Net Ethernet Adapter
  * Windows Server or Windows Client OS
  * 32-bit mode EL0 (guest userspace support)
  * [Committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview) or [sustained use discounts (SUDs)](https://docs.cloud.google.com/compute/docs/sustained-use-discounts); however, it offers [Spot VM discounts](https://docs.cloud.google.com/compute/docs/instances/spot).
  * [Virtual display devices](https://docs.cloud.google.com/compute/docs/instances/enable-instance-virtual-display#restrictions)



T2A supports the [Secure boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot) feature, but not all public OS images for T2A support secure boot.

### Supported disk types for T2A

T2A VMs support only the NVMe disk interface and can use the following block storage types:

  * Zonal standard Persistent Disk (`pd-standard`)
  * Zonal balanced Persistent Disk (`pd-balanced`)
  * Zonal SSD (performance) Persistent Disk (`pd-ssd`)



For instances running Microsoft Windows and using the NVMe disk interface, the combined number of both Hyperdisk and Persistent Disk attached volumes can't exceed a total of 16 disks. See [Known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#windows-disk-attachment). Local SSD volumes are excluded from this issue. 

## Tau T2D machine series

The Tau T2D machine series run on the third generation [AMD EPYC Milan processor](https://www.amd.com/en/products/processors/server/epyc/7003-series.html) with a base frequency of 2.45 GHz, an effective frequency of 2.8 GHz, and a max boost frequency of 3.5 GHz. This series has predefined machine types of up to 60 vCPUs, support 4 GB of memory per vCPU, and a maximum of 32 Gbps outbound data transfer. It also supports the following discount and consumption options:

  * [Resource-based committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#resource_based)
  * [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
  * [Reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type)



This series is available only in select [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

Machine types in the Tau T2D machine series have simultaneous multithreading (SMT) disabled; therefore a vCPU is equivalent to an entire core.

### Tau T2D Limitations

Tau T2D VMs don't support:

  * Local SSD
  * Regional Persistent Disk
  * Custom VMs
  * Sole-tenant nodes
  * Extreme Persistent Disk
  * GPUs
  * Nested virtualization
  * Flexible CUDs
  * Sustained use discounts (SUDs)
  * Confidential VMs



### Tau T2D machine types

Tau T2D standard machine types have 4 GB of system memory per vCPU.

Machine types | vCPUs* | Memory (GB) | Local SSD | Default egress bandwidth (Gbps)‡ | Tier_1 egress bandwidth (Gbps)  
---|---|---|---|---|---  
`t2d-standard-1` | 1 | 4 | No | Up to 10 | N/A  
`t2d-standard-2` | 2 | 8 | No | Up to 10 | N/A  
`t2d-standard-4` | 4 | 16 | No | Up to 10 | N/A  
`t2d-standard-8` | 8 | 32 | No | Up to 16 | N/A  
`t2d-standard-16` | 16 | 64 | No | Up to 32 | N/A  
`t2d-standard-32` | 32 | 128 | No | Up to 32 | N/A  
`t2d-standard-48` | 48 | 192 | No | Up to 32 | N/A  
`t2d-standard-60` | 60 | 240 | No | Up to 32 | N/A  
  
1 SMT is not supported. Each vCPU is equivalent to an entire core. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth). 

For details on the pricing information, see the following:

  * For machine type pricing, see [VM pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#t2d_machine_types).
  * Disk usage and network usage is charged separately from machine type pricing. For details, see [Disk and image pricing](https://docs.cloud.google.com/compute/disks-image-pricing#disks) and [Network pricing](https://cloud.google.com/vpc/network-pricing).



### Supported disk types for T2D

T2D VMs can use the following block storage types:

  * Zonal standard Persistent Disk (`pd-standard`)
  * Zonal balanced Persistent Disk (`pd-balanced`)
  * Zonal SSD (performance) Persistent Disk (`pd-ssd`)
  * Hyperdisk Throughput (`hyperdisk-throughput`)

Machine types | Max number of disks per VM* | Max number of Hyperdisk  
volumes per VM† | Max total disk size (TiB)  
across all disks‡  
---|---|---|---  
`t2d-standard-1` | 128 | 20 | 257  
`t2d-standard-2` | 128 | 20 | 257  
`t2d-standard-4` | 128 | 24 | 257  
`t2d-standard-8` | 128 | 32 | 257  
`t2d-standard-16` | 128 | 48 | 257  
`t2d-standard-32` | 128 | 64 | 512  
`t2d-standard-48` | 128 | 64 | 512  
`t2d-standard-60` | 128 | 64 | 512  
  
* The maximum size per Persistent Disk volume is 64 TiB.

†The maximum size per Hyperdisk Throughput volume is 32 TiB.

‡You can attach a mixture of Hyperdisk and Persistent Disk volumes to a VM, but the total Persistent Disk capacity can't exceed 257 TiB. 

## Custom machine types

If none of the predefined machine types in the general-purpose machine family match your workload needs, you can create a VM with a custom machine type.

Creating a VM with a custom machine type is ideal for workloads that require more processing power or more memory, but don't need all of the upgrades that are provided by the next larger predefined machine type.

It costs slightly more to use a custom machine type than an equivalent predefined machine type, and there are limitations in the amount of memory and vCPUs that you can select. The on-demand prices for custom machine types include a 5% premium over the on-demand and commitment prices for predefined machine types.

You can create a VM with a custom machine type for only the N and E machine series in the general-purpose machine family. Custom machine types are not available for the C and Tau machine series. Custom machine types are subject to the same Persistent Disk limits as E2, N2, and N1 predefined machine types. The maximum total Persistent Disk size for each VM is 257 TiB and the max number of Persistent Disk is 128. N4, N4A, and N4D custom machines types are subject to the limitations of [Hyperdisk capacity](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#hyperdisk-capacity)

If a custom machine type doesn't meet your requirements, it's possible to [customize the number of visible CPU cores](https://docs.cloud.google.com/compute/docs/instances/customize-visible-cores) on many machine types. It's also possible to [set the number of threads per core](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core) for certain machine types. You can make these changes during VM instance creation, or by editing an existing VM instance. Reducing the number of visible cores might impact the cost of your VMs. Be sure to review [pricing](https://docs.cloud.google.com/compute/docs/instances/customize-visible-cores#pricing) prior to making any changes.

Review the following table for the custom machine type limits for each machine series.

### N4A custom machine types

  * For N4A custom machine types, you can create a machine type with 1 to 64 vCPUs and memory between 2 and 512 GB. vCPU can be adjusted in increments of 1 vCPU, and memory can be adjusted in increments of 256 MB. 
  * By default, the memory per vCPU that you can select for a custom machine type is determined by the machine series you use. For the N4A machine series, select between 2 GB and 8 GB per vCPU. You can access more memory beyond the default option by enabling [extended memory.](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#extendedmemory)
  * N4A custom machine types are available only in select [regions and zones.](https://docs.cloud.google.com/compute/docs/regions-zones#available)



**Examples of invalid machine types:**

  * **2 vCPUs, 1.5 GB of total memory**. Invalid because the total memory is less than the minimum 2 GB for an N4A VM. 
  * **100 vCPUs, 200 GB of memory**. Invalid because the vCPU count is too large. N4A custom machine types can use a maximum of 64 vCPUs.



**Examples of valid machine types:**

  * **36 vCPUs, 72 GB of total memory**. Valid because the amount of memory per vCPU is within the acceptable range of 2 GB to 8 GB per vCPU. 
  * **5 vCPUs, 14 GB of total memory**. Valid because it has 5 vCPUs, which is in the acceptable range of 1 to 64 vCPUs, and the total memory is a multiple of 256 MB and is within the acceptable range of 2 GB to 8 GB per vCPU.



### N4D custom machine types

  * The maximum number of vCPUs allowed for a custom machine type is determined by the machine series you choose. For the N4D machine series, which supports the AMD EPYC Turin platform, you can deploy custom machine types with 2 to 96 vCPUs and 1 to 768 GB of memory. 
  * You can create N4D custom machine types with 2, 4, 8, or 16 vCPUs. After 16, you can increment the number of vCPUs by 16, up to 96 vCPUs. The minimum acceptable number of vCPUs is 2. 
  * By default, the memory per vCPU that you can select for a custom machine type is determined by the machine series you choose. For N4D machine types, select between 0.5 GB and 8 GB per vCPU in 256 MB increments. Higher amounts of memory are possible by enabling [extended memory.](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#extendedmemory)
  * N4D custom machine types are available only in select [regions and zones.](https://docs.cloud.google.com/compute/docs/regions-zones#available)
  * N4D custom machine types are available only with standard networking with a maximum egress limits of 50 Gbps.



**Examples of invalid machine types:**

  * **2 vCPUs, 0.4 GB of total memory**. Invalid because the total memory is less than the minimum 1 GB for an N4D VM and not in increments of 256 MB.
  * **34 vCPUs, 34 GB of total memory**. Invalid because the total number of vCPUs is not divisible by 16.
  * **1 vCPU, 1024 MB of memory**. Invalid because the vCPU count is too small. N4D custom machine types require a minimum of 2 vCPUs.



**Examples of valid machine types:**

  * **32 vCPUs, 16 GB of total memory**. Valid because the total number of vCPUs is a multiple of 16 and the total memory is a multiple of 256 MB. The amount of memory per vCPU is 0.5 GB, which satisfies the minimum requirement. Because the number of vCPUs is larger than 8 vCPUs, the number of vCPUs must be divisible by 16.
  * **2 vCPUs, 7 GB of total memory**. Valid because it has 2 vCPUs, which is the minimum value, and the total memory is a multiple of 256 MB. The amount of memory per vCPU is also within the acceptable range of 0.5 GB to 8 GB per vCPU.



### N4 custom machine types

  * For N4 custom machine types, you can create a machine type with 2 to 80 vCPUs with the vCPUs in multiples of 2, and memory between 4 and 640 GB. 
  * By default, the memory per vCPU that you can select for a custom machine type is determined by the machine series you use. For the N4 machine series, select between 2 GB and 8 GB per vCPU in 256 MB increments. When creating a standard N4 machine type, the minimum memory you can select is 4 GB. Higher amounts of memory are possible by enabling [extended memory.](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#extendedmemory)



**Examples of invalid machine types:**

  * **2 vCPUs, 0.5 GB of total memory**. Invalid because the total memory is less than the minimum 4 GB for an N4 VM.
  * **1 vCPU, 8 GB of memory**. Invalid because the vCPU count is too small. N4 custom machine types require a minimum of 2 vCPUs.



**Examples of valid machine types:**

  * **36 vCPUs, 72 GB of total memory**. Valid because the total number of vCPUs is even and the total memory is a multiple of 256 MB. The amount of memory per vCPU is also within the acceptable range of 2 GB to 8 GB per vCPU. 
  * **2 vCPUs, 14 GB of total memory**. Valid because it has 2 vCPUs, which is the minimum value, and the total memory is a multiple of 256 MB. The amount of memory per vCPU is also within the acceptable range of 2 GB to 8 GB per vCPU.



### N2D custom machine types

  * The maximum number of vCPUs allowed for a custom machine type is determined by the machine series you choose. For the N2D machine series, which supports the AMD EPYC Milan platform, you can deploy custom machine types with 2 to 96 vCPUs. 
  * You can create N2D custom machine types with 2, 4, 8, or 16 vCPUs. After 16, you can increment the number of vCPUs by 16, up to 96 vCPUs. The minimum acceptable number of vCPUs is 2. 
  * By default, the memory per vCPU that you can select for a custom machine type is determined by the machine series you choose. For N2D machine types, select between 0.5 GB and 8.0 GB per vCPU in 256 MB increments. Higher amounts of memory are possible by enabling [extended memory.](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#extendedmemory)
  * N2D custom machine types are available only in select [regions and zones.](https://docs.cloud.google.com/compute/docs/regions-zones#available)
  * N2D custom machine types support per VM Tier_1 networking performance maximum egress limits of 50 Gbps to 100 Gbps. When enabled: 
    * VMs with 48 to 94 vCPUs have a total egress limit of 50 Gbps.
    * VMs with 96 vCPUs have a total egress limit of 100 Gbps.



**Examples of invalid machine types:**

  * **2 vCPUs, 0.4 GB of total memory**. Invalid because the total memory is less than the minimum 1 GB for an N2D VM.
  * **34 vCPUs, 34 GB of total memory**. Invalid because the total number of vCPUs is not divisible by 16.
  * **1 vCPU, 1024 MB of memory**. Invalid because the vCPU count is too small. N2D custom machine types require a minimum of 2 vCPUs.



**Examples of valid machine types:**

  * **32 vCPUs, 16 GB of total memory**. Valid because the total number of vCPUs is even and the total memory is a multiple of 256 MB. The amount of memory per vCPU is 1 GB, which satisfies the minimum requirement. Because the number of vCPUs is larger than 8 vCPUs, the number of vCPUs must be divisible by 16.
  * **2 vCPUs, 7 GB of total memory**. Valid because it has 2 vCPUs, which is the minimum value, and the total memory is a multiple of 256 MB. The amount of memory per vCPU is also within the acceptable range of 1 GB to 8 GB per vCPU.



### N2 custom machine types

  * For N2 custom machine types, you can create a machine type with 2 to 80 vCPUs and memory between 1 and 864 GB. For machine types with up to 32 vCPUs, you can select a vCPU count that is a multiple of 2. For machine types with greater than 32 vCPUs, you must select a vCPU count that is a multiple of 4 (for example, 36, 40, 56, or 80).
  * You can create N2 custom machine types on different processors: 
    * **Cascade Lake** , the 2nd generation of the Intel Xeon processor. This is the default processor for N2 custom machine types with less than 80 vCPUs. 
    * **Ice Lake** , the 3rd generation of the Intel Xeon processor. Ice Lake processors are available in specific [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones). 
  * By default, the memory per vCPU that you can select for a custom machine type is determined by the machine series you use. For the N2 machine series, select between 0.5 GB and 8.0 GB per vCPU in 256 MB increments. Higher amounts of memory are possible by enabling [extended memory.](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#extendedmemory)
  * N2 custom machine types have an option for a per VM Tier_1 networking performance maximum egress of 50 Gbps to 100 Gbps with a minimum of 30 vCPUs. 
    * 32 to 62 vCPUs have a total egress of 50 Gbps
    * 64 to 78 vCPUs have a total egress of 75 Gbps
    * 80 vCPUs have a total egress of 100 Gbps



**Examples of invalid machine types:**

  * **2 vCPUs, 0.5 GB of total memory**. Invalid because the total memory is less than the minimum 1 GB for an N2 VM.
  * **34 vCPUs, 34 GB of total memory**. Invalid because the total number of vCPUs is not divisible by 4.
  * **1 vCPU, 1024 MB of memory**. Invalid because the vCPU count is too small. N2 custom machine types require a minimum of 2 vCPUs.



**Examples of valid machine types:**

  * **36 vCPUs, 18 GB of total memory**. Valid because the total number of vCPUs is even and the total memory is a multiple of 256 MB. The amount of memory per vCPU is also within the acceptable range of 0.5 GB to 8 GB per vCPU. Because the number of vCPUs is larger than 32 vCPUs, the number of vCPUs must be divisible by 4.
  * **2 vCPUs, 7 GB of total memory**. Valid because it has 2 vCPUs, which is the minimum value, and the total memory is a multiple of 256 MB. The amount of memory per vCPU is also within the acceptable range of 0.5 GB to 8 GB per vCPU.



### E2 custom machine types

  * E2 custom machine types support predefined platforms with Intel or AMD EPYC processors. You can create E2 custom machine types with vCPUs in multiples of 2, up to 32 vCPUs. The minimum acceptable number of vCPUs for a VM is 2. 
  * By default, the general-purpose machine series you choose determines the memory per vCPU that you can select for a custom machine type. For E2, the ratio of memory per vCPU is 0.5 GB to 8 GB inclusive. When creating a standard E2 machine type, the minimum memory you can select is 1 GB. 
  * An exception to the minimum vCPU limitation is to create an e2-standard-2 VM, then customize the visible core to 1 vCPU. The resulting VM is an e2-custom VM. For example, you create an E2 VM using the `e2-standard-2` machine type, stop the VM, and edit it by changing the visible core to 1 vCPU with 1.25 GB of memory. As a result, the machine type changes to `e2-custom-2-1280`. Pricing is described in the [Customize the number of visible CPU cores](https://docs.cloud.google.com/compute/docs/instances/customize-visible-cores#pricing\)) document. 



**Examples of invalid machine types:**

  * **1 vCPU, 1024 MB of memory**. Invalid because the vCPU count is too small. E2 custom machine types require a minimum of 2 vCPUs.
  * **32 vCPUs, 1 GB of total memory**. Invalid because the ratio of vCPUs to memory is incorrect. The acceptable ratio is 0.5 GB of memory to 1 vCPU.



**Examples of valid machine types:**

  * **32 vCPUs, 16 GB of total memory**. Valid because the total number of vCPUs is even and the total memory is an acceptable ratio of memory to vCPU. 
  * **2 vCPUs, 8 GB of total memory**. Valid because it has 2 vCPUs, which is the minimum value, and the total memory is a multiple of 256 MB. The amount of memory per vCPU is also within the acceptable range of 0.5 GB to 8 GB per vCPU.



### E2 shared-core custom machine types

E2 shared-core machine types support predefined Intel or AMD EPYC processors, which are preselected for you at the time of VM creation. You can create shared-core machine types with a vCPU range of 0.25 to 1 vCPU. The memory range is 1 to 8 GB, with a maximum ratio of 8 GB per vCPU.

You can't customize the number of visible cores on a shared-core E2 VM.

  * `e2-micro`: 0.25 vCPU, 1 to 2 GB of memory
  * `e2-small`: 0.50 vCPU, 1 to 4 GB of memory
  * `e2-medium`: 1 vCPU, 1 to 8 GB of memory



### N1 custom machine types

  * You can create N1 custom machine types with 1 or more vCPUs. For VMs with more than 1 vCPU, you must increment the number of vCPUs by 2, up to 96 vCPUs for Intel Skylake platform,or up to 64 vCPUs for Intel Broadwell, Haswell, or Ivy Bridge CPU platforms.
  * By default, the memory per vCPU that you can select for a custom machine type is determined by the machine series you choose. For N1 machine types, select between 0.9 GB and 6.5 GB per vCPU, inclusive. N1 custom machine types with 1 or 2 vCPUs require a minimum of 1 GB per vCPU. Higher amounts of memory are possible by enabling extended memory.



**Examples of invalid machine types:**

  * **1 vCPU, 0.2 GB of total memory**. Invalid because the total memory is less than the minimum 1 GB for an N1 VM. 
  * **3 vCPU, 1 GB of total memory**. Invalid because the number of vCPU cores must be 1 or an even number up to 96. 



**Examples of valid machine types:**

  * **32 vCPUs, 29 GB of total memory**. Valid because the total number of vCPUs is even and the total memory is a multiple of 256 MB. The total memory is an acceptable ratio of memory to vCPU.
  * **1 vCPU, 1 GB of total memory**. Valid because it has one vCPU, which is the minimum value, and the total memory is a multiple of 256 MB. The amount of memory per vCPU is also within the acceptable range of 1 GB to 6.5 GB per vCPU.



## What's next

  * [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth)
  * [Configuring a VM with a high-bandwidth network ](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)
  * [Virtual machine instances](https://docs.cloud.google.com/compute/docs/instances)
  * [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#general-purpose_machine_type_family)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
