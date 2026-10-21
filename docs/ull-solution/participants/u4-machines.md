---
url: https://docs.cloud.google.com/ull-solution/participants/u4-machines/
title: U4 Ultra Low Latency (ULL) machine family \u00a0|\u00a0 Ultra Low Latency Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:29.355930+00:00
---

# U4 Ultra Low Latency (ULL) machine family  |  Ultra Low Latency Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ull-solution/participants/u4-machines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ ULL Solution ](https://docs.cloud.google.com/ull-solution)
  * [ Exchange participants ](https://docs.cloud.google.com/ull-solution/participants)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# U4 Ultra Low Latency (ULL) machine family

**GA with allowlist** : ULL Solution is available only to approved exchange operators and their exchange participants. If you are an approved exchange participant, contact [exchanges@google.com](mailto:exchanges@google.com) to request access.

This document describes the U4 network-optimized machine family. U4 is Google Cloud's Ultra Low Latency (ULL) network-optimized machine family. U4 is designed to support the core workloads for financial exchange ecosystems by offering industry specific instance networking capabilities in the public cloud. The U4P and U4C machine series are based on Intel's 5th generation (code-named Emerald Rapids) Xeon scalable processor, while the U4S machine series is based on Intel's 6th generation (code-named Granite Rapids) Xeon scalable processor.

The U4 network-optimized machine family offers three machine series:

  * **U4P** : [Bare metal](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances) machine types with or without attached [Titanium SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#local_ssd_types)
  * **U4C** : Bare metal machine types with or without attached Titanium SSD disks
  * **U4S** : Available in several different virtual machine (VM) type sizes, either with or without attached Titanium SSD disks



Each machine type within a machine series has a specific number of CPUs, memory, number of NUMA domains, and network bandwidth.

## Recommended machine series by workload type

The following table provides the recommended machine series based on your workloads.

**Note:** U4P machines are available only to exchange operators.Machine series | Used by | Workload type  
---|---|---  
U4P | Exchange operators (providers) | Trading systems  
U4C | Exchange participants | Execute trading strategies  
U4S | 

  * Exchange operators
  * Exchange participants
  * Service providers

| 

  * Auxiliary workloads
  * Exchange ecosystem services

  
  
While U4P and U4C instances support ULL unicast and multicast traffic, U4S instances provide support for non-ULL workloads with close physical proximity to U4P and U4C instances for reduced latency.

## U4C machine series

The U4C machine series runs on Intel's 5th generation Xeon Scalable processor (code named Emerald Rapids) and is optimized for ultra low latency, financial exchange services. Only bare metal machine types are available, either with or without attached local Titanium SSD disks. Bare metal instances provide direct access to the underlying server CPU and memory with no virtualization or Compute Engine hypervisor in the middle. Each instance uses two sockets of the host machine, with 60 cores per socket. Each instance has 3 physical NICs.

Any [advanced features](https://docs.cloud.google.com/compute/docs/cpu-platforms#cpu_features) available and enabled in the host CPU are available to the U4C bare metal instances, even if the Compute Engine instances don't expose those features.

### Supported features

The U4C machine series has the following features:

  * Powered by Intel's Emerald Rapids processor and [Titanium](https://cloud.google.com/titanium).
  * Offers 120 CPUs and 512 GB or 768 GB of memory.
  * Supports up to 12 TiB of [local Titanium SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#local_ssd_types).
  * Offers only predefined machine types. 
  * Supports [standard network configuration](https://docs.cloud.google.com/compute/docs/networking/network-overview#bandwidth) with up to 100 Gbps bandwidth on `nic0`, for communication within Google Cloud.
  * Uses ULL VPC networks for communication with U4P instances.
  * Can be used with [Hyperdisk Balanced and Hyperdisk Extreme block storage](https://docs.cloud.google.com/compute/docs/disks). 
  * Supports [compact and spread placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview).
  * Can be used with stateful or stateless [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups).



### U4C machine types

U4C machine types are available as predefined configurations:

  * `standard` configurations have 120 CPUs and 768 GB of memory
  * `highcpu` configurations have 120 CPUs and 512 GB of memory



To use Titanium SSD with U4C, create your instance using the `lssd` variant of the U4C machine types. Selecting this machine type creates an instance of the specified size with Titanium SSD partitions attached. You can't attach Titanium SSD volumes separately.

Machine type | vCPU count1 | Memory (GB) | Attached Titanium SSD(GiB) | Physical NIC count | Egress bandwidth (Gbps)2  
---|---|---|---|---|---  
`u4c-standard-120-metal` | 120 | 768 | No | 3 | Up to 100 Gbps  
Up to 1 Gbps (ULL)  
`u4c-highcpu-120-metal` | 120 | 512 | No | 3 | Up to 100 Gbps  
Up to 1 Gbps (ULL)  
`u4c-standard-120-lssd-metal` | 120 | 768 | (4 x 3,000 GiB)  
12,000 GiB | 3 | Up to 100 Gbps  
Up to 1 Gbps (ULL)  
`u4c-highcpu-120-lssd-metal` | 120 | 512 | (4 x 3,000 GiB)  
12,000 GiB | 3 | Up to 100 Gbps  
Up to 1 Gbps (ULL)  
  
1Bare metal instances don't use vCPUs. For bare metal instances, the number of vCPUs is equivalent to the number of hardware threads on the host server.  
2Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth). 

### Supported disk types for U4C instances

U4C instances can use the following block storage types:

  * [Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced) (`hyperdisk-balanced`)
  * [Hyperdisk Extreme](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme) (`hyperdisk-extreme`)
  * Local Titanium SSD



#### Disk capacity limits for U4C instances

The limits for Google Cloud Hyperdisk with U4C instances are:

  * Maximum number of Hyperdisk disks attached to an instance: 32
  * Maximum disk capacity across all Hyperdisk disks for an instance: 512 TiB



For more information about disk capacity limits, see [Hyperdisk capacity limits per VM](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#limits-instance).

#### Disk performance limits for U4C instances

The performance limits for Titanium SSD and Hyperdisk per instance are listed in the following tables:

### Titanium SSD

Machine type | Number of Titanium SSD disks | Total storage space (GiB) | Read IOPS | Write IOPS | Read throughput (MiB/s) | Write throughput (MiB/s)  
---|---|---|---|---|---|---  
`u4c-highcpu-120-lssd-metal` | 4 | 12,000 | 7,200,000 | 3,600,000 | 30,000 | 15,840  
  
### Hyperdisk

Disk type | Maximum disks per instance | Maximum IOPS | Maximum throughput (MiB/s)  
---|---|---|---  
Hyperdisk Balanced | 32 | 275,000 | 8,750  
Hyperdisk Extreme | 8 | 380,000 | 8,750  
  
For more information about performance limits, see the following:

  * [Hyperdisk limits per instance](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#determine_which_limits_apply)
  * [Performance limits by Hyperdisk type](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-by-hd-type)



### Network support for U4C instances

U4C instances come with 3 physical NICs per instance.

Network interface | Driver | Usage | Internal egress  
bandwidth | External egress  
bandwidth  
---|---|---|---|---  
`nic0` |  AF_XDP supported Google Virtual NIC (gVNIC)  | General instance communication, including connections to non-ULL exchange applications and services (for example, drop copy). Uses [Premium Tier](https://docs.cloud.google.com/network-tiers/docs/overview) by default. | Up to 100 Gbps | Up to 25 Gbps  
`nic1` (ULL A) |  AF_XDP supported Google Virtual NIC (gVNIC)  | ULL unicast and multicast communication | Up to 1 Gbps | N/A  
`nic2` (ULL B) |  AF_XDP supported Google Virtual NIC (gVNIC)  | ULL unicast and multicast communication | Up to 1 Gbps | N/A  
  
The NUMA alignment for the ULL NICs is as follows: `nic1` (ULL A) uses NUMA node 0, while `nic2` (ULL B) uses NUMA node 2.

## U4S machine series

The U4S machine series is a general-purpose machine series intended to run auxiliary workloads for U4C and U4P instances that don't require a direct connection to a ULL VPC network. U4S instances are powered by 6th generation (code-named Granite Rapids) Intel Xeon Scalable processors and [Titanium](https://cloud.google.com/titanium).

### Supported features

The U4S machine series has the following features:

  * Powered by Intel's Granite Rapids processor and [Titanium](https://cloud.google.com/titanium).
  * Supports up to 18 TiB of local Titanium SSD disks.
  * Offers only predefined machine types. 
  * Supports standard network configuration with up to 100 Gbps bandwidth.
  * Can be used with Hyperdisk Balanced, Hyperdisk Extreme, and Hyperdisk Throughput block storage. 
  * Supports [compact and spread placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview). 



### U4S machine types

U4S VMs are available as predefined configurations in sizes ranging from 2 vCPUs to 288 vCPUs and up to 2,232 GB of memory. The following preconfigured machine type names correspond to the amount of memory configured for the instance:

  * `highcpu`: 2 GB memory per vCPU
  * `standard`: 3.75 GB memory per vCPU
  * `highmem`: 7.75 GB memory per vCPU



To use Titanium SSD with U4S, create your instance using the `-lssd` variant of the U4S machine types. Selecting this machine type creates an instance of the specified size with Titanium SSD partitions attached. You can't attach Titanium SSD volumes separately.

### U4S standard

Machine type | vCPU count1 | Memory (GB) | Attached Titanium SSD(GiB) | Physical NIC count | Egress bandwidth (Gbps)2,3 | Tier_1 egress bandwidth3  
---|---|---|---|---|---|---  
`u4s-standard-2` | 2 | 7 | No | 1 | Up to 10 | N/A  
`u4s-standard-4` | 4 | 15 | No | 1 | Up to 23 | N/A  
`u4s-standard-8` | 8 | 30 | No | 1 | Up to 23 | N/A  
`u4s-standard-16` | 16 | 60 | No | 1 | Up to 23 | N/A  
`u4s-standard-24` | 24 | 90 | No | 1 | Up to 23 | N/A  
`u4s-standard-32` | 32 | 120 | No | 1 | Up to 23 | N/A  
`u4s-standard-48` | 48 | 180 | No | 1 | Up to 34 | Up to 50  
`u4s-standard-96` | 96 | 360 | No | 1 | Up to 67 | Up to 100  
`u4s-standard-144` | 144 | 540 | No | 1 | Up to 100 | Up to 150  
`u4s-standard-192` | 192 | 720 | No | 1 | Up to 100 | Up to 200  
`u4s-standard-288` | 288 | 1,080 | No | 1 | Up to 100 | Up to 200  
  
1 A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3 Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

### U4S highcpu

Machine type | vCPU count1 | Memory (GB) | Attached Titanium SSD(GiB) | Physical NIC count | Egress bandwidth (Gbps)2,3 | Tier_1 egress bandwidth3  
---|---|---|---|---|---|---  
`u4s-highcpu-2` | 2 | 4 | No | 1 | Up to 10 | N/A  
`u4s-highcpu-4` | 4 | 8 | No | 1 | Up to 23 | N/A  
`u4s-highcpu-8` | 8 | 16 | No | 1 | Up to 23 | N/A  
`u4s-highcpu-16` | 16 | 32 | No | 1 | Up to 23 | N/A  
`u4s-highcpu-24` | 24 | 48 | No | 1 | Up to 23 | N/A  
`u4s-highcpu-32` | 32 | 64 | No | 1 | Up to 23 | N/A  
`u4s-highcpu-48` | 48 | 96 | No | 1 | Up to 34 | Up to 50  
`u4s-highcpu-96` | 96 | 192 | No | 1 | Up to 67 | Up to 100  
`u4s-highcpu-144` | 144 | 288 | No | 1 | Up to 100 | Up to 150  
`u4s-highcpu-192` | 192 | 384 | No | 1 | Up to 100 | Up to 200  
`u4s-highcpu-288` | 288 | 576 | No | 1 | Up to 100 | Up to 200  
  
1 A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3 Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

### U4S highmem

Machine type | vCPU count1 | Memory (GB) | Attached Titanium SSD(GiB) | Physical NIC count | Egress bandwidth (Gbps)2,3 | Tier_1 egress bandwidth3  
---|---|---|---|---|---|---  
`u4s-highmem-2` | 2 | 15 | No | 1 | Up to 10 | N/A  
`u4s-highmem-4` | 4 | 31 | No | 1 | Up to 23 | N/A  
`u4s-highmem-8` | 8 | 62 | No | 1 | Up to 23 | N/A  
`u4s-highmem-16` | 16 | 124 | No | 1 | Up to 23 | N/A  
`u4s-highmem-24` | 24 | 186 | No | 1 | Up to 23 | N/A  
`u4s-highmem-32` | 32 | 248 | No | 1 | Up to 23 | N/A  
`u4s-highmem-48` | 48 | 372 | No | 1 | Up to 34 | Up to 50  
`u4s-highmem-96` | 96 | 744 | No | 1 | Up to 67 | Up to 100  
`u4s-highmem-144` | 144 | 1,116 | No | 1 | Up to 100 | Up to 150  
`u4s-highmem-192` | 192 | 1,488 | No | 1 | Up to 100 | Up to 200  
`u4s-highmem-288` | 288 | 2,232 | No | 1 | Up to 100 | Up to 200  
  
1 A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3 Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

### U4S standard with Local SSD

Machine type | vCPU count1 | Memory (GB) | Attached Titanium SSD(GiB) | Physical NIC count | Egress bandwidth (Gbps)2,3 | Tier_1 egress bandwidth3  
---|---|---|---|---|---|---  
`u4s-standard-4-lssd` | 4 | 15 | (1 x 375 GiB)  
375 GiB | 1 | Up to 23 | N/A  
`u4s-standard-8-lssd` | 8 | 30 | (1 x 375 GiB)  
375 GiB | 1 | Up to 23 | N/A  
`u4s-standard-16-lssd` | 16 | 60 | (2 x 375 GiB)  
750 GiB | 1 | Up to 23 | N/A  
`u4s-standard-24-lssd` | 24 | 90 | (4 x 375 GiB)  
1,500 GiB | 1 | Up to 23 | N/A  
`u4s-standard-32-lssd` | 32 | 120 | (5 x 375 GiB)  
1,875 GiB | 1 | Up to 23 | N/A  
`u4s-standard-48-lssd` | 48 | 180 | (8 x 375 GiB)  
3,000 GiB | 1 | Up to 34 | N/A  
`u4s-standard-96-lssd` | 96 | 360 | (16 x 375 GiB)  
6,000 GiB | 1 | Up to 67 | N/A  
`u4s-standard-144-lssd` | 144 | 540 | (24 x 375 GiB)  
9,000 GiB | 1 | Up to 100 | N/A  
`u4s-standard-192-lssd` | 192 | 720 | (32 x 375 GiB)  
12,000 GiB | 1 | Up to 100 | N/A  
`u4s-standard-288-lssd` | 288 | 1,080 | (48 x 375 GiB)  
18,000 GiB | 1 | Up to 100 | Up to 200  
  
1 A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3 Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

### U4S highmem with Local SSD

Machine type | vCPU count1 | Memory (GB) | Attached Titanium SSD(GiB) | Physical NIC count | Egress bandwidth (Gbps)2,3 | Tier_1 egress bandwidth3  
---|---|---|---|---|---|---  
`u4s-highmem-4-lssd` | 4 | 31 | (1 x 375 GiB)  
375 GiB | 1 | Up to 23 | N/A  
`u4s-highmem-8-lssd` | 8 | 62 | (1 x 375 GiB)  
375 GiB | 1 | Up to 23 | N/A  
`u4s-highmem-16-lssd` | 16 | 124 | (2 x 375 GiB)  
750 GiB | 1 | Up to 23 | N/A  
`u4s-highmem-24-lssd` | 24 | 186 | (4 x 375 GiB)  
1,500 GiB | 1 | Up to 23 | N/A  
`u4s-highmem-32-lssd` | 32 | 248 | (5 x 375 GiB)  
1,875 GiB | 1 | Up to 23 | N/A  
`u4s-highmem-48-lssd` | 48 | 372 | (8 x 375 GiB)  
3,000 GiB | 1 | Up to 34 | N/A  
`u4s-highmem-96-lssd` | 96 | 744 | (16 x 375 GiB)  
6,000 GiB | 1 | Up to 67 | N/A  
`u4s-highmem-144-lssd` | 144 | 1,116 | (24 x 375 GiB)  
9,000 GiB | 1 | Up to 100 | N/A  
`u4s-highmem-192-lssd` | 192 | 1,488 | (32 x 375 GiB)  
12,000 GiB | 1 | Up to 100 | N/A  
`u4s-highmem-288-lssd` | 288 | 2,232 | (48 x 375 GiB)  
18,000 GiB | 1 | Up to 100 | Up to 200  
  
1 A CPU uses two threads per core, and a vCPU represents a single thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Default egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3 Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types.

1A vCPU is implemented as a single hardware hyperthread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms). For bare metal instances (U4P and U4C machines), the number of vCPUs is equivalent to the number of hardware threads on the host server.  
2Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth). 

### Supported disk types for U4S instances

U4S instances can use the following block storage types:

  * Hyperdisk Balanced (`hyperdisk-balanced`)
  * Hyperdisk Extreme (`hyperdisk-extreme`)
  * Hyperdisk Throughput (`hyperdisk-throughput`)
  * Local Titanium SSD



#### Disk capacity limits for U4S instances

The maximum total disk capacity across all disks attached to an instance can't exceed 512 TiB.

For more information about the capacity limits, see [Hyperdisk capacity limits per VM](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#limits-instance).

| Maximum number of disks |   
---|---|---  
Machine types | Hyperdisk  
per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk ML | Hyperdisk Extreme  
`u4s-*-2`  
| 8 | 8 | 8 | 0 | 0  
`u4s-*-4`  
`u4s-(standard,highmem)-4-lssd` | 16 | 16 | 16 | 0 | 0  
`u4s-*-8`  
`u4s-(standard,highmem)-8-lssd` | 32 | 32 | 32 | 0 | 0  
`u4s-*-16`  
`u4s-(standard,highmem)-16-lssd` | 32 | 32 | 32 | 0 | 0  
`u4s-*-24`  
`u4s-(standard,highmem)-24-lssd` | 32 | 32 | 32 | 0 | 0  
`u4s-*-32`  
`u4s-(standard,highmem)-32-lssd` | 64 | 64 | 64 | 0 | 0  
`u4s-*-48`  
`u4s-(standard,highmem)-48-lssd` | 64 | 64 | 64 | 0 | 0  
`u4s-*-96`  
`u4s-(standard,highmem)-96-lssd` | 128 | 128 | 128 | 0 | 8  
`u4s-*-144`  
`u4s-(standard,highmem)-144-lssd` | 128 | 128 | 128 | 0 | 8  
`u4s-*-192`  
`u4s-(standard,highmem)-192-lssd` | 128 | 128 | 128 | 0 | 8  
`u4s-*-288`  
`u4s-(standard,highmem)-288-lssd` | 128 | 128 | 128 | 0 | 8  
  
#### Disk performance limits for U4S instances

The performance limits for Titanium SSD and Hyperdisk attached disks are listed in the following table:

### Titanium SSD

Instance machine type | Number of Titanium SSD disks | Total storage space (GiB) | Read IOPS | Write IOPS | Read throughput (MiB/s) | Write throughput (MiB/s)  
---|---|---|---|---|---|---  
`u4s-*-4-lssd` | 1 | 375 | 150,000 | 75,000 | 625 | 330  
`u4s-*-8-lssd` | 1 | 375 | 150,000 | 75,000 | 625 | 330  
`u4s-*-16-lssd` | 2 | 750 | 300,000 | 150,000 | 1,250 | 660  
`u4s-*-24-lssd` | 4 | 1,500 | 600,000 | 300,000 | 2,500 | 1,320  
`u4s-*-32-lssd` | 5 | 1,875 | 750,000 | 375,000 | 3,125 | 1,650  
`u4s-*-48-lssd` | 8 | 3,000 | 1,200,000 | 600,000 | 5,000 | 2,640  
`u4s-*-96-lssd` | 16 | 6,000 | 2,400,000 | 1,200,000 | 10,000 | 5,280  
`u4s-*-144-lssd` | 16 | 6,000 | 2,400,000 | 1,200,000 | 10,000 | 5,280  
`u4s-*-192-lssd` | 32 | 12,000 | 4,800,000 | 2,400,000 | 20,000 | 10,560  
`u4s-*-288-lssd` | 48 | 18,000 | 7,200,000 | 3,600,000 | 30,000 | 15,840  
  
### Hyperdisk Balanced

Instance machine type | Maximum IOPS | Maximum throughput (MiB/s)  
---|---|---  
`u4s-*-2`  
| 50,000 | 400  
`u4s-*-4`  
`u4s-*-4-lssd` | 50,000 | 400  
`u4s-*-8`  
`u4s-*-8-lssd` | 50,000 | 800  
`u4s-*-16`  
`u4s-*-16-lssd` | 100,000 | 1,600  
`u4s-*-24`  
`u4s-*-24-lssd` | 100,000 | 1,600  
`u4s-*-32`  
`u4s-*-32-lssd` | 100,000 | 1,600  
`u4s-*-48`  
`u4s-*-48-lssd` | 160,000 | 2,400  
`u4s-*-96`  
`u4s-*-96-lssd` | 240,000 | 4,800  
`u4s-*-144`  
`u4s-*-144-lssd` | 240,000 | 4,800  
`u4s-*-192`  
`u4s-*-192-lssd` | 320,000 | 10,000  
`u4s-*-288`  
`u4s-*-288-lssd` | 320,000 | 10,000  
  
### Hyperdisk Extreme

Instance machine type | Maximum IOPS | Maximum throughput (MiB/s)  
---|---|---  
`u4s-*-96`  
`u4s-*-96-lssd` | 350,000 | 5,000  
`u4s-*-144`  
`u4s-*-144-lssd` | 350,000 | 5,000  
`u4s-*-192`  
`u4s-*-192-lssd` | 440,000 | 10,000  
`u4s-*-288`  
`u4s-*-288-lssd` | 440,000 | 10,000  
  
### Hyperdisk Throughput

Instance machine type | Maximum IOPS | Maximum throughput (MiB/s)  
---|---|---  
`u4s-*-2`  
| 1,600 | 400  
`u4s-*-4`  
`u4s-*-4-lssd` | 1,600 | 400  
`u4s-*-8`  
`u4s-*-8-lssd` | 3,200 | 800  
`u4s-*-16`  
`u4s-*-16-lssd` | 6,400 | 1,600  
`u4s-*-24`  
`u4s-*-24-lssd` | 6,400 | 1,600  
`u4s-*-32`  
`u4s-*-32-lssd` | 6,400 | 1,600  
`u4s-*-48`  
`u4s-*-48-lssd` | 9,600 | 2,400  
`u4s-*-96`  
`u4s-*-96-lssd` | 19,200 | 4,800  
`u4s-*-144`  
`u4s-*-144-lssd` | 19,200 | 4,800  
`u4s-*-192`  
`u4s-*-192-lssd` | 40,000 | 10,000  
`u4s-*-288`  
`u4s-*-288-lssd` | 40,000 | 10,000  
  
For more information about performance limits, see the following:

  * [Hyperdisk limits per instance](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#determine_which_limits_apply)
  * [Performance limits by Hyperdisk type](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-by-hd-type)



### Network support for U4S instances

U4S instances come with one physical NIC per instance, but you can configure multiple vNICs.

vCPUs | Driver | Internal IP  
egress bandwidth | External IP  
egress bandwidth  
---|---|---|---  
2 | gVNIC | Up to 10 Gbps | Up to 7 Gbps  
4 | gVNIC | Up to 23 Gbps | Up to 7 Gbps  
8 | gVNIC | Up to 23 Gbps | Up to 7 Gbps  
16 | gVNIC | Up to 23 Gbps | Up to 7 Gbps  
24 | gVNIC | Up to 23 Gbps | Up to 7 Gbps  
32 | gVNIC | Up to 23 Gbps | Up to 7 Gbps  
48 | gVNIC | Up to 50 Gbps | Up to 25 Gbps  
96 | gVNIC | Up to 100 Gbps | Up to 25 Gbps  
144 | gVNIC | Up to 150 Gbps | Up to 25 Gbps  
192 | gVNIC | Up to 200 Gbps | Up to 25 Gbps  
288 | gVNIC | Up to 200 Gbps | Up to 25 Gbps  
  
## Regional availability of U4 machine types

Machine types for the U4 machine family are available in the following Google Cloud regions and zones:

  * `us-south1`
    * `us-south1-d`
    * `us-south1-e`



## U4 limitations

The U4 machine family doesn't support the following Compute Engine features:

  * For Shielded VM features, see the following:

    * [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure_boot) isn't supported for U4 instances.

      * U4 instances require an operating system image with an out-of-tree (OOT) gVNIC driver as described in Operating system support for U4 machine types. When Secure Boot is enabled, the operating system enforces strict kernel module signature verification. Because OOT drivers aren't signed with a recognized distribution key, Secure Boot prevents the network driver from loading, which causes network initialization to fail.

      * Additionally, Secure Boot prevents using Onload built from source as described in [Work with Onload](https://docs.cloud.google.com/ull-solution/participants/use-onload). Building Onload from source installs a custom kernel module. Because custom kernel modules built from source aren't signed with a recognized distribution key, Secure Boot prevents the Onload kernel module from loading.

    * Shielded VM isn't supported for bare metal instances as described in the [limitations](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#limitations) section of the Shielded VM overview.

If your Google Cloud org uses a [Shielded VM policy](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#organization-policy-constraint), then you must create a custom org policy that excludes U4 instances from the Shielded VM requirement.

  * [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview)

  * [Sole-tenancy](https://docs.cloud.google.com/compute/docs/sole-tenant-nodes): Each U4P or U4C instance runs on a dedicated host server.

  * [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)

  * [Simulating host maintenance events](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance)




Additional limitations of U4 instances:

  * For U4S, you can create only VM instances; bare metal instances aren't supported.
  * U4P and U4C bare metal instances with the C6 CPU sleep state enabled have low single-stream NIC performance. You can disable the C6 CPU sleep state in the guest OS to achieve full network bandwidth performance. For more information, refer to the [troubleshooting network performance](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-performance#bare_metal_instances) documentation.



## Quota limits for U4

CPU quota is the total number of virtual CPUs across all of your compute instances in a region or zone. CPU quotas apply to running instances and reservations. If your CPU quota is set to 16, then you can create a single compute instance with 16 vCPUs, or you can create 4 compute instances with 4 vCPUs each.

To understand Compute Engine quotas and resource allocation limits, and to learn how to view your U4 quotas, see [Compute Engine quota and limits overview](https://docs.cloud.google.com/compute/quotas-limits).

Quota Type | Machine Series | Quota Name | Limit/Description  
---|---|---|---  
CPU | U4C | `CPUS_PER_VM_FAMILY: U4C` | 240 vCPUs per zone  
CPU | U4S | `CPUS_PER_VM_FAMILY: U4S` | 576 vCPUs per zone  
Local SSD | All | N/A | No quota request needed; disks are added automatically to instances created by using U4 machine types that end in `-lssd`.  
Google Cloud Hyperdisk | All | `Hyperdisk Balanced Capacity (GB)`  
`Hyperdisk Balanced IOPS`  
`Hyperdisk Balanced Throughput (MB/s)`  
`Hyperdisk Extreme Capacity (GB)`  
`Hyperdisk Throughput Capacity (GB)` (U4S only)  | Capacity and performance quotas apply. For more information, see [Disk quotas](https://docs.cloud.google.com/compute/resource-usage#disk_quota).  
Commitments | U4C | `Committed_U4C_CPUS` | Used with a resource-based, committed use contract  
Commitments | U4S | `Committed_U4S_CPUS` | Used with a resource-based, committed use contract  
  
If you require a quota increase you can reach out to your account teams or follow the instructions in [Allocation quotas](https://docs.cloud.google.com/compute/resource-usage#vm_instance_quota).

## Operating system support for U4 machine types

This section describes the supported operating system (OS) images for U4 machine types.

The supported public image families contain an out-of-tree (OOT) Google Virtual NIC (gVNIC) driver, which lets you create U4P and U4C bare metal instances with the `GVNIC` network interface type, as well as U4S VM instances. Additionally, the driver supports PTP, which lets you configure accurate time for U4 instances.

**Note:** The [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details) page in the Compute Engine documentation provides general OS support information across Google Cloud for non-U4 machine types. To understand OS support for U4 machine types, use the following sections.

Windows images aren't supported.

### Red Hat Enterprise Linux (RHEL) images

Google Cloud supports the following [Red Hat Enterprise Linux (RHEL)](https://docs.cloud.google.com/compute/docs/images/os-details#red_hat_enterprise_linux_rhel) OS images for U4 machine types:

  * RHEL 10.2 EUS with out-of-tree gVNIC driver 
    * Image project: `rhel-cloud`
    * Image family: `rhel-10-2-eus-oot-gve` or `rhel-10-2-eus-lvm-oot-gve`



These image families were originally available under a different name that used the format `rhel-10-2-eus-gvnic-baremetal`. While we recommend using images with the new naming format, the images that use the original format remain available and supported for the duration of the OS lifecycle.

#### RHEL BYOS images

You can also create a U4 instance by using images from your [Red Hat Cloud Access subscription](https://www.redhat.com/en/technologies/cloud-computing/cloud-access). The general procedure is described in [Create an instance using a RHEL BYOS image](https://docs.cloud.google.com/compute/docs/instances/create-rhel-byos-vm).

For bring your own subscription (BYOS) images, the image project and family are as follows:

  * Image project: `rhel-byos-cloud`
  * Image family: `rhel-10-2-eus-oot-gve-byos` or `rhel-10-2-eus-lvm-oot-gve-byos`



To use the BYOS image, you must complete an additional prerequisite as follows:

  1. You must first [give your Google Group access to your RHEL subscription](https://docs.cloud.google.com/compute/docs/instances/create-rhel-byos-vm#enable-access) as described in _Create an instance using a RHEL BYOS image_.

  2. You can then follow the procedure to [create a ULL instance](https://docs.cloud.google.com/ull-solution/participants/create-ull-instances) or [create a non-ULL instance](https://docs.cloud.google.com/ull-solution/participants/create-non-ull-instances) by specifying the BYOS image project and family.




For additional information about BYOS, see [About Licenses](https://docs.cloud.google.com/compute/docs/licenses/about).

### Rocky Linux images

Google Cloud supports the following [Rocky Linux](https://docs.cloud.google.com/compute/docs/images/os-details#rocky_linux) OS images for U4 machine types:

  * Rocky Linux 10 optimized for Google Cloud with out-of-tree gVNIC driver 
    * Image project: `rocky-linux-cloud`
    * Image family: `rocky-linux-10-optimized-gcp-oot-gve`



#### Kernel update and automatic update differences

Rocky Linux images for Google Cloud are configured to install updates by using the `dnf-automatic` tool as described in [Automatic updates](https://docs.cloud.google.com/compute/docs/images/os-details#auto-update-rocky-linux).

However, the `rocky-linux-10-optimized-gcp-oot-gve` image family is configured to exclude kernel packages from DNF updates. This configuration prevents a scenario in which the system installs a new kernel without the kernel header packages required by DKMS to compile the out-of-tree GVE module, which could lead to a loss of network connectivity upon reboot.

This difference in behavior applies to image versions `v20260911` and later. If you haven't already, we recommend that you update to the latest version.

### Custom images

While Google Cloud builds and supports the public images in the preceding sections, you can alternatively use a custom image based on another Linux distribution.

To use a custom image, the image must be configured with the required OOT gVNIC driver. Custom images can be functionally configured to work with U4 machines; however, they haven't been validated for performance or stability.

#### Red Hat-based distributions

The following procedure is adapted from the general procedure for [creating custom images](https://docs.cloud.google.com/compute/docs/images/create-custom), and includes the additional steps that are necessary to install the required driver on Red Hat-based distributions. This example uses [AlmaLinux](https://docs.cloud.google.com/compute/docs/images/os-details#almalinux).

  1. Create a temporary VM instance by using a base image, such as an AlmaLinux 10 image. You can use any machine type _except_ for U4P and U4C machines. The following example uses `n4-highcpu-2`.
         
         gcloud compute instances create INSTANCE_NAME \
             --image-project=almalinux-cloud \
             --image-family=almalinux-10 \
             --machine-type=n4-highcpu-2 \
             --project=PROJECT_ID \
             --zone=ZONE
         

Replace the following values:

     * `INSTANCE_NAME`: a name for the instance
     * `PROJECT_ID`: the ID of your project
     * `ZONE`: the zone in which to create the instance
  2. Connect to the instance by using SSH:
         
         gcloud compute ssh INSTANCE_NAME --project=PROJECT_ID --zone=ZONE
         

  3. Install the required kernel packages, Artifact Registry plugin, and Extra Packages for Enterprise Linux (EPEL) release package. Running this as a single transaction helps avoid repository mirror synchronization issues:
         
         sudo dnf makecache && sudo dnf install -y dnf-plugin-artifact-registry kernel kernel-devel kernel-headers https://dl.fedoraproject.org/pub/epel/epel-release-latest-10.noarch.rpm
         

  4. Reboot the instance to ensure that any kernel updates take effect before installing the driver:
         
         sudo reboot
         

  5. Reconnect to the instance by using SSH:
         
         gcloud compute ssh INSTANCE_NAME --project=PROJECT_ID --zone=ZONE
         

  6. Install the OOT driver by using the Google-provided RPM. The following commands compile the GVE kernel module and stage it to load on the next boot, but don't load the new driver immediately:
         
         cat << 'EOF' | sudo tee /etc/yum.repos.d/gve-rpm.repo
         [gve-el10-stable]
         name=GVE Public Stable Repo
         baseurl=https://packages.cloud.google.com/yum/repos/gve-el10-stable
         enabled=1
         repo_gpgcheck=0
         gpgcheck=1
         gpgkey=https://packages.cloud.google.com/yum/doc/rpm-package-key-v10.gpg
         EOF
         
         sudo dnf -y --refresh --enablerepo=gve-el10-stable install gve
         

  7. Reboot the instance to load the OOT driver:
         
         sudo reboot
         

  8. Stop the instance:
         
         gcloud compute instances stop INSTANCE_NAME \
             --project=PROJECT_ID \
             --zone=ZONE
         

  9. Create an image from the disk of the instance:
         
         gcloud compute images create IMAGE_NAME \
             --source-disk=INSTANCE_NAME \
             --source-disk-zone=ZONE \
             --source-disk-project=PROJECT_ID \
             --guest-os-features=UEFI_COMPATIBLE,VIRTIO_SCSI_MULTIQUEUE,GVNIC,SEV_CAPABLE,SEV_SNP_CAPABLE,SEV_LIVE_MIGRATABLE,SEV_LIVE_MIGRATABLE_V2,IDPF,TDX_CAPABLE \
             --family=IMAGE_FAMILY \
             --project=IMAGE_PROJECT
         

Replace the following values:

     * `IMAGE_NAME`: a name for your custom image
     * `INSTANCE_NAME`: the name of the instance
     * `ZONE`: the zone of the instance
     * `PROJECT_ID`: the ID of your project
     * `IMAGE_FAMILY`: an image family for your custom image
     * `IMAGE_PROJECT`: the project ID where you want to store the custom image



## What's next

  * [Create ULL Compute Engine instances](https://docs.cloud.google.com/ull-solution/participants/create-ull-instances)
  * [Create non-ULL Compute Engine instances](https://docs.cloud.google.com/ull-solution/participants/create-non-ull-instances)
  * Learn about [ULL infrastructure configuration](https://docs.cloud.google.com/ull-solution/participants/configuration-overview)
  * Learn about [ULL Multicast](https://docs.cloud.google.com/ull-solution/participants/multicast-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
