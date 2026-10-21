---
url: https://docs.cloud.google.com/compute/docs/compute-optimized-machines/
title: Compute-optimized machine family for Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:17:35.562904+00:00
---

# Compute-optimized machine family for Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/compute-optimized-machines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Compute-optimized machine family for Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

Compute-optimized instances are ideal for compute-intensive and high performance computing (HPC) workloads. Compute-optimized instances offer the highest performance per core and are built on architecture that utilizes features like non-uniform memory access (NUMA) for optimal, reliable, and uniform performance.

**Note:** For the C3, C3D, C4, C4D, or C4A machine series, see [General-purpose machine family](https://docs.cloud.google.com/compute/docs/general-purpose-machines).**Machine** | **Workloads**  
---|---  
H4D machine series | 

  * HPC workloads and multi-node workloads
  * Manufacturing
  * Weather forecasting
  * Electronic design automation (EDA)
  * Healthcare and life sciences
  * Scientific computing

  
H3 machine series | 

  * HPC workloads
  * Computational fluid dynamics
  * Crash safety
  * Genomics
  * Financial modeling
  * General scientific and engineering computing

  
C2D machine series | 

  * Memory-bound workloads
  * Gaming (AAA game servers)
  * High performance computing (HPC)
  * High performance databases
  * Electronic Design Automation (EDA)
  * Media transcoding

  
C2 machine series | 

  * Compute-bound workloads
  * High-performance web serving
  * Gaming (AAA game servers)
  * Ad serving
  * High performance computing (HPC)
  * Media transcoding
  * AI/ML

  
  
The following machine series are available in this machine family:

  * H4D instances are powered by [Titanium](https://cloud.google.com/titanium) and fifth generation AMD EPYC Turin processors which have a base frequency of 2.7 GHz and a maximum frequency of 4.1 GHz. H4D instances have 192 cores (vCPUs) and up to 3,024 GB of memory. H4D instances can be used with Local SSD storage and Cloud RDMA networking.
  * H3 instances are powered by [Titanium](https://cloud.google.com/titanium) and two fourth generation Intel Xeon Scalable processors (code-named Sapphire Rapids) which have an all-core frequency of 3.0 GHz. H3 instances have 88 vCPUs and 352 GB of DDR5 memory.
  * C2D instances run on the third generation AMD EPYC Milan processor and offer up to 3.5 GHz max boost frequency. C2D instances have flexible sizing between 2 to 112 vCPUs and 2 to 8 GB of memory per vCPU.
  * C2 instances run on the second generation Intel Xeon Scalable processor (Cascade Lake) which offers up to 3.9 GHz sustained single-core max turbo frequency. C2 offers instances with 4 to 60 vCPUs and 4 GB of memory per vCPU.



## H4D machine series

H4D instances are powered by the AMD EPYC Turin 5th Generation processors and [Titanium](https://cloud.google.com/titanium) offload processors.

H4D instances deliver high performance, low cost, and scalability for multi-node workloads. H4D instances are single-threaded and are optimized for tightly-coupled applications that scale across multiple nodes. Leveraging technologies like Titanium SSD, RDMA-enabled 200 Gbps networking and cluster management capabilities, these instances prioritize performance and workload-specific optimizations. Additionally, you can use [Dynamic Workload Scheduler](https://cloud.google.com/blog/products/compute/introducing-dynamic-workload-scheduler) for scheduled or immediate cluster deployment, making H4D ideal for HPC bursty workload needs.

An H4D instance uses all the vCPUs on an entire host server. H4D instances can use the entire host network bandwidth and come with a default network bandwidth rate of up to 200 Gbps. However, the bandwidth from the instance to the internet is limited to 1 Gbps.

Simultaneous multithreading (SMT) is disabled for H4D instances and can't be enabled. There is also no overcommitting to ensure optimal performance consistency.

H4D instances are available on-demand, or with one- and three-year committed use discounts (CUDs). To compare these methods, see [Compute Engine instances provisioning models](https://docs.cloud.google.com/compute/docs/instances/provisioning-models).

### H4D Limitations

The H4D machine series has the following restrictions:

  * The H4D machine types are only available in a predefined machine type. Custom machine types aren't available.
  * You can't use GPUs with H4D instances.
  * Outbound data transfer is limited to 1 Gbps.
  * You can't create machine images from H4D instances.
  * H4D machine images can't be used to [create disks](https://docs.cloud.google.com/compute/docs/disks/create-disk-from-source).
  * You can't share disks between instances, either in [multi-writer mode](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms#multi_writer_mode) or [read-only mode](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms#use-multi-instance). 
  * Hyperdisk Balanced performance is capped at 15,000 IOPS and 240 MBps throughput.
  * Live migration isn't supported for H4D instances.



### H4D machine types

Machine types | vCPUs1 | Memory (GB) | Titanium SSD | Default egress bandwidth (Gbps)2  
---|---|---|---|---  
`h4d-standard-192` | 192 | 720 | Not supported | Up to 200 Gbps  
`h4d-highmem-192` | 192 | 1,488 | Not supported | Up to 200 Gbps  
`h4d-highmem-192-lssd` | 192 | 1,488 | (10 x 375 GiB)  
3,750 GiB | Up to 200 Gbps  
`h4d-megamem-192` | 192 | 3,024 | Not supported | Up to 200 Gbps  
`h4d-megamem-192-lssd` | 192 | 3,024 | (32 x 375 GiB)  
12,000 GiB | Up to 200 Gbps  
  
1 A vCPU represents an entire core—no simultaneous multithreading (SMT).  
2 Default egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth). 

### Supported disk types for H4D

H4D instances can use the following block storage types:

  * Hyperdisk Balanced (`hyperdisk-balanced`)
  * Local Titanium SSD



#### Disk and capacity limits

The following restrictions apply:

  * The number of Hyperdisk volumes can't exceed 128 per VM.
  * The maximum total disk capacity across all disks can't exceed 512 TiB.



For details about the capacity limits, see [Hyperdisk capacity limits per VM](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#limits-instance).

H4D storage limits are described in the following table:

Maximum number of disks per instance  
---  
Machine types | All Hyperdisk  
types | Hyperdisk Balanced  
`h4d-standard-192` | 128 | 128  
`h4d-highmem-192` | 128 | 128  
`h4d-highmem-192-lssd` | 128 | 128  
`h4d-megamem-192` | 128 | 128  
`h4d-megamem-192-lssd` | 128 | 128  
  
### Network support for H4D instances

H4D instances require [gVNIC network interfaces](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). H4D supports up to 200 Gbps network bandwidth for standard networking. Instance to Internet egress bandwidth is limited to 1 Gbps.

If using Cloud RDMA, you must configure at least two network interfaces (vNICs) when you create each instance:

  * GVNIC: This vNIC uses the gVNIC driver and is used for normal networking communication. It is fully connected to the Google network and can connect to the Internet.
  * IRDMA: The other vNIC uses an Intel iDPF/iRDMA driver and is used only for Cloud RDMA communication. This network interface doesn't connect to the Internet.



Before migrating to H4D or creating H4D instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the IDPF network driver. If you create an H4D instance with an operating system that doesn't support the IDPF driver, then you might not be able to connect to the instance.

### Maintenance experience for H4D instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple _host events_. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background. 

The H4D machine series offers the following features related to host maintenance:

Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance)  
---|---|---|---|---|---  
`h4d-standard-192` | Minimum of 30 days | Terminate | 7 days | Yes | No  
`h4d-highmem-192` | Minimum of 30 days | Terminate | 7 days | Yes | No  
`h4d-highmem-192-lssd` | Minimum of 30 days | Terminates with Local SSD data persistence | 7 days | Yes | No  
`h4d-megamem-192` | Minimum of 30 days | Terminate | 7 days | Yes | No  
`h4d-megamem-192-lssd` | Minimum of 30 days | Terminates with Local SSD data persistence | 7 days | Yes | No  
  
The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently. 

## H3 machine series

H3 instances are powered by the fourth generation Intel Xeon Scalable processors (code-named Sapphire Rapids), DDR5 memory, and [Titanium](https://cloud.google.com/titanium) offload processors.

H3 instances offer the best price performance for compute-intensive high performance computing (HPC) workloads in Compute Engine. H3 instances are [single-threaded](https://docs.cloud.google.com/compute/docs/cpu-platforms) and are ideal for a variety of modeling and simulation workloads including computational fluid dynamics, crash safety, genomics, financial modeling, and general scientific and engineering computing. H3 instances support compact placement, which is optimized for tightly-coupled applications that scale across multiple nodes.

The H3 series is available in one size, comprising an entire host server. To save on licensing costs, you can customize the number of visible cores, but you are charged the same price for the instance. H3 instances can use the entire host network bandwidth and come with a default network bandwidth rate of up to 200 Gbps. However, the bandwidth from the instance to the internet is limited to 1 Gbps.

Simultaneous multithreading (SMT) is disabled for H3 instances and can't be enabled. There is also no overcommitting to ensure optimal performance consistency.

H3 instances are available on-demand, or with one- and three-year committed use discounts (CUDs). H3 instances can be used with Google Kubernetes Engine.

### H3 Limitations

The H3 machine series has the following restrictions:

  * The H3 machine series is only available in a predefined machine type. Custom machine shapes aren't available.
  * You can't use GPUs with H3 instances.
  * Outbound data transfer is limited to 1 Gbps.
  * Persistent Disk and Google Cloud Hyperdisk performance is capped at 15,000 IOPS and 240 MBps throughput.
  * H3 instances don't support [machine images](https://docs.cloud.google.com/compute/docs/machine-images).
  * H3 instances support only the NVMe [storage interface](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#choose_an_interface).
  * H3 instance images can't be used to [create disks](https://docs.cloud.google.com/compute/docs/disks/create-disk-from-source).
  * H3 instances don't support sharing disks between instances, either in [multi-writer mode](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms#multi_writer_mode) or [read-only mode](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms#use-multi-instances).



### H3 machine types

H3 instances are available as a predefined configuration with 88 vCPUs and 352 GB of memory.

Machine types | vCPUs1 | Memory (GB) | Local SSD | Default egress  
bandwidth (Gbps)2  
---|---|---|---|---  
`h3-standard-88` | 88 | 352 | Not supported | Up to 200 Gbps  
  
1 A vCPU represents an entire core—no simultaneous multithreading (SMT).  
2 Default egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth). 

### Supported disk types for H3

H3 instances can use the following block storage types:

  * Balanced Persistent Disk (`pd-balanced`)
  * Hyperdisk Balanced (`hyperdisk-balanced`)
  * Hyperdisk Throughput (`hyperdisk-throughput`)



#### Disk and capacity limits

If supported by the machine type, you can attach a mixture of Hyperdisk and Persistent Disk volumes to an instance, but the following restrictions apply: 

  * The combined number of both Hyperdisk and Persistent Disk volumes can't exceed 128 per instance.
  * The maximum total disk capacity (in TiB) across all disk types can't exceed:

    * 512 TiB for all Hyperdisk
    * 512 TiB for a mixture of Hyperdisk and Persistent Disk
    * 257 TiB for all Persistent Disk



For details about the capacity limits, see [ Hyperdisk size and attachment limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance) and [Persistent Disk maximum capacity](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#capacity_257tb).

H3 storage limits are described in the following table:

| Maximum number of disks per instance  |   
---|---|---  
Machine types | All disk types 1 | All Hyperdisk  
types | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk Extreme  
`h3-standard-88` | 128 | 64 | 8 | 64 | 0  
  
1 This limit applies to Persistent Disk and Hyperdisk, but doesn't include Local SSD disks. 

### Network support for H3 instances

H3 instances require [gVNIC network interfaces](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). H3 supports up to 200 Gbps network bandwidth for standard networking and doesn't support per VM Tier_1 networking performance.

Before migrating to H3 or creating H3 instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the IDPF network driver. If you create an H3 instance with an operating system that doesn't support the IDPF driver, then you might not be able to connect to the instance.

### Maintenance experience for H3 instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple _host events_. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background. 

The H3 machine series offers the following features related to host maintenance:

Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance)  
---|---|---|---|---|---  
`h3-standard-88` | Minimum of 30 days | Live migrate | 7 days | Yes | Yes  
  
The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently. 

## C2D machine series

The C2D machine series provides the largest instance sizes and are best-suited for high performance computing (HPC). The C2D series also has the largest available last-level cache (LLC) cache per core.

The C2D machine series comes in different machine types ranging from 2 to 112 vCPUs, and offer up to 896 GB of memory. You can attach up to 3 TiB of Local SSD storage to these machine types for applications that require higher storage performance.

  * C2D standard and C2D high-cpu machines serve existing compute-bound workloads including high-performance web servers, media transcoding, and gaming.
  * C2D high-memory machines serve specialized workloads such as HPC and EDA, which need more memory.



The C2D series supports these compute-bound workloads by using the third generation AMD EPYC Milan platform.

The C2D series supports [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview).

### C2D Limitations

The C2D machine series has the following restrictions:

  * You can't attach [regional persistent disks](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) to a C2D instance.
  * The C2D machine series is subject to different [disk performance limits](https://docs.cloud.google.com/compute/docs/disks/performance#c2d_vms) than the general-purpose and memory-optimized machine families.
  * The C2D machine series is available only in [select zones and regions](https://docs.cloud.google.com/compute/docs/regions-zones#available) on specific [CPU processors](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison).
  * The C2D machine series doesn't support GPUs.
  * The C2D machine series doesn't support sole-tenant nodes.



### C2D machine types

C2D instances are available as predefined configurations in sizes ranging from 2 vCPUs to 112 vCPUs and up to 896 GB of memory.

  * standard: 4 GB memory per vCPU
  * highcpu: 2 GB memory per vCPU
  * highmem: 8 GB memory per vCPU




###  C2D standard 

Machine types | vCPUs1 | Memory (GB) | Local SSD2 | Default egress  
bandwidth (Gbps)3 | Tier_1 egress  
bandwidth (Gbps)4  
---|---|---|---|---|---  
`c2d-standard-2` | 2 | 8 | 1, 2, 4, or 8 | Up to 10 | N/A  
`c2d-standard-4` | 4 | 16 | 1, 2, 4, or 8 | Up to 10 | N/A  
`c2d-standard-8` | 8 | 32 | 1, 2, 4, or 8 | Up to 16 | N/A  
`c2d-standard-16` | 16 | 64 | 1, 2, 4, or 8 | Up to 32 | N/A  
`c2d-standard-32` | 32 | 128 | 2, 4, or 8 | Up to 32 | Up to 50  
`c2d-standard-56` | 56 | 224 | 4 or 8 | Up to 32 | Up to 50  
`c2d-standard-112` | 112 | 448 | 8 | Up to 32 | Up to 100  
  
1 A vCPU represents a single logical CPU thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
3 Default egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
4 Supports [ high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. For Windows OS images, the maximum network bandwidth is limited to 50 Gbps. 

###  C2D high-cpu 

Machine types | vCPUs1 | Memory (GB) | Local SSD2 | Default egress  
bandwidth (Gbps)3 | Tier_1 egress  
bandwidth (Gbps)4  
---|---|---|---|---|---  
`c2d-highcpu-2` | 2 | 4 | 1, 2, 4, or 8 | Up to 10 | N/A  
`c2d-highcpu-4` | 4 | 8 | 1, 2, 4, or 8 | Up to 10 | N/A  
`c2d-highcpu-8` | 8 | 16 | 1, 2, 4, or 8 | Up to 16 | N/A  
`c2d-highcpu-16` | 16 | 32 | 1, 2, 4, or 8 | Up to 32 | N/A  
`c2d-highcpu-32` | 32 | 64 | 2, 4, or 8 | Up to 32 | Up to 50  
`c2d-highcpu-56` | 56 | 112 | 4 or 8 | Up to 32 | Up to 50  
`c2d-highcpu-112` | 112 | 224 | 8 | Up to 32 | Up to 100  
  
1 A vCPU represents a single logical CPU thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
3 Default egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
4 Supports [ high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. For Windows OS images, the maximum network bandwidth is limited to 50 Gbps. 

###  C2D high-mem 

Machine types | vCPUs1 | Memory (GB) | Local SSD2 | Default egress  
bandwidth (Gbps)3 | Tier_1 egress  
bandwidth (Gbps)4  
---|---|---|---|---|---  
`c2d-highmem-2` | 2 | 16 | 1, 2, 4, or 8 | Up to 10 | N/A  
`c2d-highmem-4` | 4 | 32 | 1, 2, 4, or 8 | Up to 10 | N/A  
`c2d-highmem-8` | 8 | 64 | 1, 2, 4, or 8 | Up to 16 | N/A  
`c2d-highmem-16` | 16 | 128 | 1, 2, 4, or 8 | Up to 32 | N/A  
`c2d-highmem-32` | 32 | 256 | 2, 4, or 8 | Up to 32 | Up to 50  
`c2d-highmem-56` | 56 | 448 | 4 or 8 | Up to 32 | Up to 50  
`c2d-highmem-112` | 112 | 896 | 8 | Up to 32 | Up to 100  
  
1 A vCPU represents a single logical CPU thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
3 Default egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
4 Supports [ high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. For Windows OS images, the maximum network bandwidth is limited to 50 Gbps. 

### Supported disk types for C2D

C2D instances can use the following block storage types:

  * Standard Persistent Disk (`pd-standard`)
  * Balanced Persistent Disk (`pd-balanced`)
  * SSD (performance) Persistent Disk (`pd-ssd`)
  * Hyperdisk Balanced (`hyperdisk-balanced`)1
  * Hyperdisk Balanced High Availability (`hyperdisk-balanced-high-availability`)1



1 To use Hyperdisk Balanced or Hyperdisk Balanced High Availability with this machine series, you must [contact your account team](https://docs.cloud.google.com/tam). For more information, see [Design for flexibility on older machine series](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#gen2-hyperdisk_name_short). 

Each C2D instance can have a maximum of 128 Persistent Disk volumes (including the boot disk) attached to the instance, and a total of 257 TiB disk capacity.

C2D instances with Confidential Computing running Microsoft Windows with the NVMe disk interface have a disk attachment limitation of 16 disks. See [Known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#windows-disk-attachment) for details.

**Note:** Persistent Disk usage is charged separately from [machine type pricing](https://cloud.google.com/compute/vm-instance-pricing).

### Network support for C2D instances

The C2D machine types support either the VirtIO or gVNIC network driver. C2D instances with 32 or more vCPUS support higher network bandwidths of 50 Gbps and 100 Gbps with gVNIC and [per VM Tier_1 networking performance](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration).

### Maintenance experience for C2D instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple _host events_. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background. 

The C2D machine series offers the following features related to host maintenance:

Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance)  
---|---|---|---|---|---  
All machine types | Minimum of 30 days | Live migrate | 60 seconds | No | Yes  
Confidential VM | Minimum of 30 days | Restart in place | 60 seconds | No | Yes  
  
The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently. 

## C2 machine series

The C2 machine series provides full transparency into the architecture of the underlying server platforms, letting you fine-tune the performance. Machine types in this series offer much more computing power, and are generally more robust for compute-intensive workloads compared to N1 high-CPU machine types.

The C2 series comes in different machine types ranging from 4 to 60 vCPUs, and offers up to 240 GB of memory. You can attach up to 3 TiB of Local SSD storage to these instances for applications that require higher storage performance.

This series also produces a greater than 40% performance improvement compared to the previous generation N1 machines and offer higher performance per thread and isolation for latency-sensitive workloads.

The C2 series enables the highest performance per core and the highest frequency for compute-bound workloads using Intel 3.9 GHz Cascade Lake processors. If you are looking to optimize workloads for [single thread performance](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core), particularly with respect to floating point, choose a machine type in this series to take advantage of AVX-512 capabilities only available on Intel.

### C2 Limitations

The C2 machine series has the following restrictions:

  * You cannot use [regional persistent disks](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk).
  * The C2 machine series is subject to different [disk limits](https://docs.cloud.google.com/compute/docs/disks/performance#c2_vms) than the general-purpose and memory-optimized machine families.
  * The C2 machine series is available only in [select zones and regions](https://docs.cloud.google.com/compute/docs/regions-zones#available) on specific [CPU processors](https://docs.cloud.google.com/compute/docs/machine-types#machine_type_comparison).
  * The C2 machine series doesn't support GPUs.



### C2 machine types

C2 instances are available as predefined configurations with 4 to 60 vCPUs and 4 GB memory per vCPU.

Machine types | vCPUs1 | Memory (GB) | Local SSD2 | Default egress  
bandwidth (Gbps)3 | Tier_1 egress  
bandwidth (Gbps)4  
---|---|---|---|---|---  
`c2-standard-4` | 4 | 16 | 1, 2, 4, or 8 | Up to 10 | N/A  
`c2-standard-8` | 8 | 32 | 1, 2, 4, or 8 | Up to 16 | N/A  
`c2-standard-16` | 16 | 64 | 2, 4, or 8 | Up to 32 | N/A  
`c2-standard-30` | 30 | 120 | 4 or 8 | Up to 32 | Up to 50  
`c2-standard-60` | 60 | 240 | 8 | Up to 32 | Up to 100  
  
1 A vCPU represents a single logical CPU thread. See [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Number of 375 GiB Local SSD disks that you can choose to add when creating the instance.  
3 Default egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
4 Supports [ high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. For Windows OS images, the maximum network bandwidth is limited to 50 Gbps. 

### Supported disk types for C2

C2 instances can use the following block storage types:

  * Standard Persistent Disk (`pd-standard`)
  * Balanced Persistent Disk (`pd-balanced`)
  * SSD (performance) Persistent Disk (`pd-ssd`)



Each C2 instance can have a maximum of 128 Persistent Disk volumes (including the boot disk) attached to the instance, and a total of 257 TiB disk capacity.

**Note:** Persistent Disk usage is charged separately from [machine type pricing](https://cloud.google.com/compute/vm-instance-pricing).

### Network support for C2 instances

The C2 machine types support either the VirtIO or gVNIC network driver. C2 instances with 30 or more vCPUS support higher network bandwidths of 50 Gbps and 100 Gbps with gVNIC and [per VM Tier_1 networking performance](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration).

### Maintenance experience for C2 instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple _host events_. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background. 

The C2 machine series offers the following features related to host maintenance:

Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance)  
---|---|---|---|---|---  
All machine types | Minimum of 30 days | Live migrate | 60 seconds | No | Yes  
Confidential VM | Minimum of 30 days | Restart in place | 60 seconds | No | Yes  
Sole tenant node VMs | 4 to 6 weeks | Live migrate, restart in place, or migrate with a node group | none | No | Yes  
  
The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently. 

## What's next

  * [Learn about the HPC VM image](https://docs.cloud.google.com/compute/docs/instances/create-hpc-vm)
  * [Create an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).
  * [Create an instance that uses Cloud RDMA](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-rdma)
  * Review [Compute Engine instance pricing](https://cloud.google.com/compute/vm-instance-pricing).
  * [Configure an instance with a high-bandwidth network](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
