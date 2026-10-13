---
url: https://docs.cloud.google.com/compute/docs/storage-optimized-machines/
title: Storage-optimized machine family for Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:51:41.771544+00:00
---

# Storage-optimized machine family for Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/storage-optimized-machines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Storage-optimized machine family for Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

The storage-optimized machine family is suitable for workloads that are low in core usage and high in storage density. This machine family is ideal for high performance workloads that need fast access to data stored in local storage, such as data streaming, SQL and NoSQL databases, data search, data analytics, and data warehousing.

  * The Z4D machine series offers compute instances with up to 3 TB of memory and 84,000 GiB of Titanium SSD capacity. The Z4D machine series includes machine types that provision 2 physical NICs per instance.
  * The Z3 machine series offers compute instances with up to 1.5 TB of memory and up to 72,000 GiB of Titanium SSD capacity. The Z3 machine series includes a bare metal machine type.



Z4D and Z3 offer machine types with different ratios of vCPU to Titanium SSD capacity: `standardlssd` and `highlssd`.

**Machine series** | **Workloads**  
---|---  
Z4D | 

  * I/O intensive workloads such as SQL, NoSQL, and vector databases
  * Data analytics and data warehouses
  * Search
  * Parallel file systems for AI/ML

  
Z3 | 

  * SQL, NoSQL, and vector databases
  * Data analytics and data warehouses
  * Search
  * Media streaming
  * Large distributed parallel file systems

  
  
## Z4D machine series

Z4D instances are powered by AMD EPYC Turin processors, DDR5 memory, and [Titanium offload processors](https://cloud.google.com/titanium). Z4D machine types are optimized for the underlying NUMA architecture to deliver optimal, reliable, and consistent performance. Z4D also offers larger Titanium SSD disk sizes than Z3.

The Z4D machine series offers up to 84,000 GiB local storage using [Titanium SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd#local_ssd_types).

Z4D offers the following features:

  * Uses Titanium to offload networking and storage processing from the host CPU onto silicon devices deployed throughout the data center
  * Delivers high performance block storage with [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks)
  * Offers a large amount of Titanium SSD storage capacity
  * Supports [Advanced Vector Extensions (AVX512)](https://docs.cloud.google.com/compute/docs/cpu-platforms#avx512), which is a built-in accelerator that offers built-in acceleration for vector-based processing, supporting 32 double-precision and 64 single-precision floating-point numbers, along with 8 64-bit and 16 32-bit integers.



Z4D instances use Titanium to enable higher levels of networking performance, isolation, and security.

  * Z4D instances with 1 physical NIC support network bandwidths of up to 200 Gbps, depending on the number of vCPUs.
  * Z4D instances with 2 physical NICs support network bandwidths of up to 400 Gbps.



For details on pricing, see the [VM pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#z4d_machine_types). Disk usage and network usage is charged separately from machine type pricing. For more information, see [Disk and image pricing](https://cloud.google.com/compute/disks-image-pricing) and [Network pricing](https://cloud.google.com/vpc/network-pricing). For Titanium SSD pricing, see [Storage-optimized machine type family pricing](https://docs.cloud.google.com/compute/vm-instance-pricing?e=48754805#section-4).

### Z4D Limitations

The following restrictions apply:

  * You can't use [regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) with Z4D instances.
  * Z4D instances are available in [select zones and regions](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * You can't use [GPUs](https://docs.cloud.google.com/compute/docs/gpus) with Z4D instances.
  * Z4D doesn't support sole tenancy.
  * You can't suspend a Z4D instance.
  * You can't create custom machine types for Z4D instances.
  * Live migration is only supported for Z4D instances with 42,000 GiB or less of attached Titanium SSD. During host maintenance events, Z4D instances with more than 42,000 GiB of attached Titanium SSD terminate with data persistence.
  * Z4D isn't supported on Windows images.



### Z4D machine types

The Z4D machine series supports the following predefined `lssd` machine subtypes:

  * `standardlssd`: offers high performance search and data analysis for medium-sized data sets. This machine type has a vCPU to Titanium SSD capacity ratio of 1:219 and offers the highest Titanium SSD performance per vCPU.
  * `highlssd`: offers high performance and storage intensive streaming and data analysis for large-sized data sets. This machine type has a vCPU to Titanium SSD capacity ratio of 1:438 and offers a larger Titanium SSD disk partition size than `standardlssd`.



### Z4D standardlssd

Machine types | vCPUs1 | Memory  
(GB) | Titanium SSD | Number of NICs | Default egress  
bandwidth (Gbps)2 | Egress bandwidth (Gbps)  
outside a VPC network2  
---|---|---|---|---|---|---  
`z4d-highmem-16-standardlssd` | 16 | 126 | (1 x 3,500 GiB)  
3,500 GiB | 1 | Up to 20 | Up to 7  
`z4d-highmem-32-standardlssd` | 32 | 252 | (2 x 3,500 GiB)  
7,000 GiB | 1 | Up to 32 | Up to 7  
`z4d-highmem-48-standardlssd` | 48 | 378 | (3 x 3,500 GiB)  
10,500 GiB | 1 | Up to 50 | Up to 25  
`z4d-highmem-64-standardlssd` | 64 | 504 | (4 x 3,500 GiB)  
14,000 GiB | 1 | Up to 65 | Up to 25  
`z4d-highmem-96-standardlssd` | 96 | 756 | (6 x 3,500 GiB)  
21,000 GiB | 1 | Up to 100 | Up to 25  
`z4d-highmem-192-standardlssd` | 192 | 1,512 | (12 x 3,500 GiB)  
42,000 GiB | 1 | Up to 200 | Up to 25  
`z4d-highmem-384-standardlssd` | 384 | 3,024 | (24 x 3,500 GiB)  
84,000 GiB | 2 | Up to 400 | Up to 50  
  
### Z4D highlssd

Machine types | vCPUs1 | Memory  
(GB) | Titanium SSD | Number of NICs | Default egress  
bandwidth (Gbps)2 | Egress bandwidth (Gbps)  
outside a VPC network2  
---|---|---|---|---|---|---  
`z4d-highmem-8-highlssd` | 8 | 63 | (1 x 3,500 GiB)  
3,500 GiB | 1 | Up to 20 | Up to 7  
`z4d-highmem-16-highlssd` | 16 | 126 | (2 x 3,500 GiB)  
7,000 GiB | 1 | Up to 20 | Up to 7  
`z4d-highmem-32-highlssd` | 32 | 252 | (4 x 3,500 GiB)  
14,000 GiB | 1 | Up to 32 | Up to 7  
`z4d-highmem-48-highlssd` | 48 | 378 | (6 x 3,500 GiB)  
21,000 GiB | 1 | Up to 50 | Up to 25  
`z4d-highmem-64-highlssd` | 64 | 504 | (8 x 3,500 GiB)  
28,000 GiB | 1 | Up to 65 | Up to 25  
`z4d-highmem-96-highlssd` | 96 | 756 | (12 x 3,500 GiB)  
42,000 GiB | 1 | Up to 100 | Up to 25  
`z4d-highmem-192-highlssd` | 192 | 1,512 | (24 x 3,500 GiB)  
84,000 GiB | 1 | Up to 200 | Up to 25  
  
1A vCPU is implemented as a single hardware thread on the available [CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth). 

### Supported disk types for Z4D

Z4D instances support only the NVMe disk interface and can use the following block storage types:

  * Hyperdisk Balanced (`hyperdisk-balanced`)
  * Hyperdisk Balanced High Availability (`hyperdisk-balanced-high-availability`)
  * Hyperdisk Extreme (`hyperdisk-extreme`)
  * Hyperdisk Throughput (`hyperdisk-throughput`)
  * Hyperdisk ML (`hyperdisk-ml`)
  * Titanium SSD



Every machine type in the Z4D machine series comes with locally attached Titanium SSD disks. The disks are added automatically when you create an instance. The capacity and performance for Titanium SSD disks for Z4D are listed in the following table:

### Z4D standardlssd

| IOPS |  | Throughput   
(MiBps)  
---|---|---|---  
Machine type | # of attached  
Titanium disks | Disk size (GiB) | Total size (GiB) | Read | Write | Read | Write  
`z4d-highmem-16-standardlssd` | 1 | 3,500 | 3,500 | 650,000 | 512,000 | 3,150 | 2,400  
`z4d-highmem-32-standardlssd` | 2 | 3,500 | 7,000 | 1,300,000 | 1,024,000 | 6,300 | 4,800  
`z4d-highmem-48-standardlssd` | 3 | 3,500 | 10,500 | 1,950,000 | 1,536,000 | 9,450 | 7,200  
`z4d-highmem-64-standardlssd` | 4 | 3,500 | 14,000 | 2,600,000 | 2,048,000 | 12,600 | 9,600  
`z4d-highmem-96-standardlssd` | 6 | 3,500 | 21,000 | 3,900,000 | 3,072,000 | 18,900 | 14,400  
`z4d-highmem-192-standardlssd` | 12 | 3,500 | 42,000 | 7,800,000 | 6,144,000 | 37,800 | 28,800  
`z4d-highmem-384-standardlssd` | 24 | 3,500 | 84,000 | 15,600,000 | 12,288,000 | 75,600 | 57,600  
  
### Z4D highlssd

| IOPS |  | Throughput   
(MiBps)  
---|---|---|---  
Machine type | # of attached  
Titanium disks | Disk size (GiB) | Total size (GiB) | Read | Write | Read | Write  
`z4d-highmem-8-highlssd` | 1 | 3,500 | 3,500 | 650,000 | 512,000 | 3,150 | 2,400  
`z4d-highmem-16-highlssd` | 2 | 3,500 | 7,000 | 1,300,000 | 1,024,000 | 6,300 | 4,800  
`z4d-highmem-32-highlssd` | 4 | 3,500 | 14,000 | 2,600,000 | 2,048,000 | 12,600 | 9,600  
`z4d-highmem-48-highlssd` | 6 | 3,500 | 21,000 | 3,900,000 | 3,072,000 | 18,900 | 14,400  
`z4d-highmem-64-highlssd` | 8 | 3,500 | 28,000 | 5,200,000 | 4,096,000 | 25,200 | 19,200  
`z4d-highmem-96-highlssd` | 12 | 3,500 | 42,000 | 7,800,000 | 6,144,000 | 37,800 | 28,800  
`z4d-highmem-192-highlssd` | 24 | 3,500 | 84,000 | 15,600,000 | 12,288,000 | 75,600 | 57,600  
  
For the performance limits of Hyperdisk and Persistent Disk, see the following:

  * [Hyperdisk performance limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits)
  * [Persistent Disk performance limits for Z4D VMs](https://docs.cloud.google.com/compute/docs/disks/performance#z4d_vms)



#### Disk and capacity limits

For details about the capacity limits, see [ Hyperdisk size and attachment limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance) and [Persistent Disk maximum capacity](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#capacity_257tb).

The maximum number of disks that you can attach to Z4D instances are listed in the following tables:

### Z4D standardlssd

Machine type | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk Extreme | Hyperdisk ML  
---|---|---|---|---|---  
`z4d-highmem-16-standardlssd` | 32 | 32 | 32 | 0 | 32  
`z4d-highmem-32-standardlssd` | 32 | 32 | 32 | 0 | 32  
`z4d-highmem-48-standardlssd` | 32 | 32 | 32 | 0 | 32  
`z4d-highmem-64-standardlssd` | 64 | 64 | 64 | 8 | 64  
`z4d-highmem-96-standardlssd` | 64 | 64 | 64 | 8 | 64  
`z4d-highmem-192-standardlssd` | 64 | 64 | 64 | 8 | 64  
`z4d-highmem-384-standardlssd` | 128 | 128 | 128 | 8 | 128  
  
### Z4D highlssd

Machine type | Hyperdisk per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk Extreme | Hyperdisk ML  
---|---|---|---|---|---  
`z4d-highmem-8-highlssd` | 16 | 16 | 16 | 0 | 16  
`z4d-highmem-16-highlssd` | 32 | 32 | 32 | 0 | 32  
`z4d-highmem-32-highlssd` | 32 | 32 | 32 | 0 | 32  
`z4d-highmem-48-highlssd` | 32 | 32 | 32 | 0 | 32  
`z4d-highmem-64-highlssd` | 64 | 64 | 64 | 8 | 64  
`z4d-highmem-96-highlssd` | 64 | 64 | 64 | 8 | 64  
`z4d-highmem-192-highlssd` | 64 | 64 | 64 | 8 | 64  
  
**Note:** The column for Hyperdisk Balanced also applies to Hyperdisk Balanced High Availability disks. 

### Network support for Z4D VMs

Z4D VM instances require [gVNIC network interfaces](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). 

Z4D supports up to 200 Gbps network bandwidth for standard networking. Z4D instances with two NICs support up to 400 Gbps network bandwidth for standard networking. Z4D instances don't use the per VM Tier_1 networking performance feature.

Before migrating to Z4D or creating Z4D instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the IDPF network driver. If you create an Z4D instance with an operating system that doesn't support the IDPF driver, then you might not be able to connect to the instance.

Machine type | Maximum internal bandwidth (Gbps) | Maximum external bandwidth (Gbps)  
---|---|---  
`z4d-highmem-8-*` | Up to 20 | Up to 7  
`z4d-highmem-16-*` | Up to 20 | Up to 7  
`z4d-highmem-32-*` | Up to 32 | Up to 7  
`z4d-highmem-48-*` | Up to 50 | Up to 25  
`z4d-highmem-64-*` | Up to 65 | Up to 25  
`z4d-highmem-96-*` | Up to 100 | Up to 25  
`z4d-highmem-192-*` | Up to 200 | Up to 25  
`z4d-highmem-384-*` | Up to 400 | Up to 25  
  
### Maintenance experience for Z4D instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple _host events_. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background. 

The Z4D machine series supports on-demand maintenance and offers the following features related to host maintenance:

Attached Titanium SSD (GiB) | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance)  
---|---|---|---|---|---  
42,000 or less | Minimum of 30 days | Live migrate | 7 days | Yes | Yes  
More than 42,000 | Minimum of 30 days | Terminates with Local SSD data persistence | 7 days | Yes | Yes  
  
The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently. 

Compute Engine preserves data on the local Titanium SSD disks for Z4D instances during maintenance events.

If a host event occurs, Compute Engine tries to recover any Titanium SSD disks attached to the instance. By default, Compute Engine spends up to 1 hour recovering the data. For Z4D instances, Compute Engine spends up to 6 hours trying to recover the Titanium SSD data before reaching the timeout limit. This timeout limit is customizable. For more information about Local SSD and Titanium SSD recovery options, see [Disk persistence following instance termination](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#disk-persistence).

## Z3 machine series

Z3 instances are powered by the fourth generation Intel Xeon Scalable processor (code-named Sapphire Rapids), DDR5 memory, and [Titanium offload processors](https://cloud.google.com/titanium). Z3 machine types are optimized for the underlying NUMA architecture to deliver optimal, reliable, and consistent performance.

The Z3 machine series offers the following Local SSD storage capacities using [Titanium SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd#local_ssd_types):

  * Up to 36,000 GiB with VM instances
  * 72,000 GiB with bare metal instances



Titanium SSD is custom-designed Local SSD based on Titanium I/O offload processing. It offers enhanced security, performance, and management compared to Local SSD.

Z3 offers the following features:

  * Uses Titanium to offload networking and storage processing from the host CPU onto silicon devices deployed throughout the data center
  * Delivers high performance block storage with [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks)
  * Offers a larger amount of Titanium SSD storage capacity than other Compute Engine machine series in different machine families
  * Supports [Intel Advanced Matrix Extensions (AMX)](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel-amx), which is a built-in accelerator that significantly improves the performance of deep-learning training and inference on the CPU.
  * Offers bare metal instances that provide access to several onboard, function-specific [accelerators and offloads](https://docs.cloud.google.com/compute/docs/cpu-platforms#accelerator) like Intel QAT, Intel DLB, Intel DSA, Intel TDX, and Intel IAA.
  * Supports the following discount and consumption options: 
    * Resource-based committed use discounts (CUDs)
    * Flexible CUDs
    * Spot VMs (excluding bare metal machine types)
    * Reservations



Z3 instances use Titanium to enable higher levels of networking performance, isolation, and security. The Z3 machine series supports a default network bandwidth of up to 100 Gbps and up to 200 Gbps with [per VM Tier_1 networking performance](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration).

For details on pricing, see the [VM pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#z3_machine_types). Disk usage and network usage is charged separately from machine type pricing. For more information, see [Disk and image pricing](https://cloud.google.com/compute/disks-image-pricing) and [Network pricing](https://cloud.google.com/vpc/network-pricing). For Titanium SSD pricing, see [Storage-optimized machine type family pricing](https://docs.cloud.google.com/compute/vm-instance-pricing?e=48754805#section-4).

### Z3 Limitations

The following restrictions apply:

  * You can't use [regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) with Z3 instances.
  * Z3 instances are only available in [select zones and regions](https://docs.cloud.google.com/compute/docs/regions-zones#available). For regional availability of bare metal instances, see [Bare metal instances](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances#regions_zones).
  * You can't use [GPUs](https://docs.cloud.google.com/compute/docs/gpus) with Z3 instances.
  * Z3 doesn't support sole tenancy.
  * You can't suspend a Z3 instance.
  * You can't create custom machine types for Z3 instances.
  * Live migration is only supported for Z3 instances with 18,000 GiB or less of attached Titanium SSD.
  * Z3 isn't supported on Windows images.



### Z3 machine types

The Z3 machine series supports the following predefined `lssd` machine subtypes:

  * `standardlssd`: offers high performance search and data analysis for medium-sized data sets. This machine type has a vCPU to Titanium SSD capacity ratio of less than 1:350 and offers the highest Titanium SSD performance per vCPU.
  * `highlssd`: offers high performance and storage intensive streaming and data analysis for large-sized data sets. This machine type has a vCPU to Titanium SSD capacity ratio between 1:350 and 1:600 and offers a higher total Titanium SSD capacity than `standardlssd`.



To create a bare metal instance with Z3, use the `z3-highmem-192-highlssd-metal` machine type.

### Z3 standardlssd

Machine types | vCPUs1 | Memory (GB) | Titanium SSD | Default egress bandwidth (Gbps)2 | Tier_1 egress bandwidth (Gbps)2  
---|---|---|---|---|---  
`z3-highmem-14-standardlssd` | 14 | 112 | (1 x 3000 GiB) 3,000 GiB | Up to 23 | N/A  
`z3-highmem-22-standardlssd` | 22 | 176 | (2 x 3000 GiB) 6,000 GiB | Up to 23 | N/A  
`z3-highmem-44-standardlssd` | 44 | 352 | (3 x 3000 GiB) 9,000 GiB | Up to 32 | Up to 50  
`z3-highmem-88-standardlssd` | 88 | 704 | (6 x 3000 GiB) 18,000 GiB | Up to 62 | Up to 100  
`z3-highmem-176-standardlssd` | 176 | 1,406 | (12 x 3000 GiB) 36,000 GiB | Up to 100 | Up to 200  
  
1A vCPU is implemented as a single hardware thread on the available [CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth). 

### Z3 highlssd

Machine types | vCPUs1 | Memory (GB) | Titanium SSD | Default egress bandwidth (Gbps)2 | Tier_1 egress bandwidth (Gbps)2  
---|---|---|---|---|---  
`z3-highmem-8-highlssd` | 8 | 64 | (1 x 3000 GiB) 3,000 GiB | Up to 23 | N/A  
`z3-highmem-16-highlssd` | 16 | 128 | (2 x 3000 GiB) 6,000 GiB | Up to 23 | N/A  
`z3-highmem-22-highlssd` | 22 | 176 | (3 x 3000 GiB) 9,000 GiB | Up to 23 | N/A  
`z3-highmem-32-highlssd` | 32 | 256 | (4 x 3000 GiB) 12,000 GiB | Up to 32 | N/A  
`z3-highmem-44-highlssd` | 44 | 352 | (6 x 3000 GiB) 18,000 GiB | Up to 32 | Up to 50  
`z3-highmem-88-highlssd` | 88 | 704 | (12 x 3000 GiB) 36,000 GiB | Up to 62 | Up to 100  
`z3-highmem-192-highlssd-metal` | 1923 | 1,536 | (12 x 6000 GiB) 72,000 GiB | Up to 100 | Up to 200  
  
1A vCPU is implemented as a single hardware thread on the available [CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2 Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. See [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3 For bare metal instances, the number of vCPUs is equivalent to the number of hardware threads on the host server. 

### Supported disk types for Z3

Z3 VMs support only the NVMe disk interface and can use the following block storage types:

  * Hyperdisk Balanced (`hyperdisk-balanced`)
  * Hyperdisk Balanced High Availability (`hyperdisk-balanced-high-availability`)
  * Hyperdisk Extreme (`hyperdisk-extreme`)
  * Hyperdisk Throughput (`hyperdisk-throughput`)
  * Balanced Persistent Disk (`pd-balanced`)
  * SSD (performance) Persistent Disk (`pd-ssd`)
  * Titanium SSD



Z3 bare metal instances can use the following block storage types:

  * Hyperdisk Balanced (`hyperdisk-balanced`)
  * Hyperdisk Extreme (`hyperdisk-extreme`)
  * Titanium SSD



Every machine type in the Z3 machine series comes with locally attached Titanium SSD disks. The disks are added automatically when you create an instance. The capacity and performance for Titanium SSD disks for Z3 are listed in the following table:

### Z3 standardlssd

| IOPS |  | Throughput   
(MiBps)  
---|---|---|---  
Machine type | # of attached  
Titanium disks | Disk size (GiB) | Total size (GiB) | Read | Write | Read | Write  
`z3-highmem-14-standardlssd` | 1 | 3,000 | 3,000 | 750,000 | 500,000 | 3,000 | 2,500  
`z3-highmem-22-standardlssd` | 2 | 3,000 | 6,000 | 1,500,000 | 1,000,000 | 6,000 | 5,000  
`z3-highmem-44-standardlssd` | 3 | 3,000 | 9,000 | 2,250,000 | 1,500,000 | 9,000 | 7,500  
`z3-highmem-88-standardlssd` | 6 | 3,000 | 18,000 | 4,500,000 | 3,000,000 | 18,000 | 15,000  
`z3-highmem-176-standardlssd` | 12 | 3,000 | 36,000 | 9,000,000 | 6,000,000 | 36,000 | 30,000  
  
### Z3 highlssd

| IOPS |  | Throughput   
(MiBps)  
---|---|---|---  
Machine type | # of attached  
Titanium disks | Disk size (GiB) | Total size (GiB) | Read | Write | Read | Write  
`z3-highmem-8-highlssd` | 1 | 3,000 | 3,000 | 750,000 | 500,000 | 3,000 | 2,500  
`z3-highmem-16-highlssd` | 2 | 3,000 | 6,000 | 1,500,000 | 1,000,000 | 6,000 | 5,000  
`z3-highmem-22-highlssd` | 3 | 3,000 | 9,000 | 2,250,000 | 1,500,000 | 9,000 | 7,500  
`z3-highmem-32-highlssd` | 4 | 3,000 | 12,000 | 3,000,000 | 2,000,000 | 12,000 | 10,000  
`z3-highmem-44-highlssd` | 6 | 3,000 | 18,000 | 4,500,000 | 3,000,000 | 18,000 | 15,000  
`z3-highmem-88-highlssd` | 12 | 3,000 | 36,000 | 9,000,000 | 6,000,000 | 36,000 | 30,000  
`z3-highmem-192-highlssd-metal` | 12 | 6,000 | 72,000 | 9,000,000 | 6,000,000 | 36,000 | 30,000  
  
For the performance limits of Hyperdisk and Persistent Disk, see the following:

  * [Hyperdisk performance limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits)
  * [Persistent Disk performance limits for Z3 VMs](https://docs.cloud.google.com/compute/docs/disks/performance#z3_vms)



#### Disk and capacity limits

For details about the capacity limits, see [ Hyperdisk size and attachment limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance) and [Persistent Disk maximum capacity](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#capacity_257tb).

Z3 storage limits are described in the following table:

### Z3 standardlssd

| Maximum number of disks |  |   
---|---|---|---  
Machine type | Per VM1 | Hyperdisk volumes  
per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk Extreme  
`z3-highmem-14-standardlssd` | 128 | 16 | 16 | 16 | 0  
`z3-highmem-22-standardlssd` | 128 | 32 | 32 | 32 | 0  
`z3-highmem-44-standardlssd` | 128 | 32 | 32 | 32 | 0  
`z3-highmem-88-standardlssd` | 128 | 32 | 32 | 32 | 8  
`z3-highmem-176-standardlssd` | 128 | 32 | 32 | 32 | 8  
  
1 The maximum size per Hyperdisk volume is 64 TiB.

### Z3 highlssd

| Maximum number of disks |  |   
---|---|---|---  
Machine type | Per VM1 | Hyperdisk volumes  
per VM | Hyperdisk Balanced | Hyperdisk Throughput | Hyperdisk Extreme  
`z3-highmem-8-highlssd` | 128 | 16 | 16 | 16 | 0  
`z3-highmem-16-highlssd` | 128 | 16 | 16 | 16 | 0  
`z3-highmem-22-highlssd` | 128 | 32 | 32 | 32 | 0  
`z3-highmem-32-highlssd` | 128 | 32 | 32 | 32 | 0  
`z3-highmem-44-highlssd` | 128 | 32 | 32 | 32 | 0  
`z3-highmem-88-highlssd` | 128 | 32 | 32 | 32 | 8  
`z3-highmem-192-highlssd-metal` | 32 | 32 | 16 | 0 | 16  
  
1 The maximum size per Hyperdisk volume is 64 TiB.

### Network support for Z3 VMs

The following network interface drivers are required:

  * Z3 VM instances require [gVNIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). 
  * Z3 bare metal instances require the [Intel IDPF LAN PF device driver](https://docs.cloud.google.com/compute/docs/networking/using-idpf). 



Z3 supports up to 100 Gbps network bandwidth for standard networking and up to 200 Gbps with per VM Tier_1 networking performance for VM and bare metal instances.

Before migrating to Z3 or creating Z3 instances, make sure that the [operating system image](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that you use supports the IDPF network driver. If you create an Z3 instance with an operating system that doesn't support the IDPF driver, then you might not be able to connect to the instance.

### Maintenance experience for Z3 instances

During the [lifecycle of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), the host machine that your instance runs on undergoes multiple _host events_. A host event can include the regular maintenance of Compute Engine infrastructure, or in rare cases, a host error. Compute Engine also applies some non-disruptive lightweight upgrades for the hypervisor and network in the background. 

The Z3 machine series supports on-demand maintenance and offers the following features related to host maintenance:

Attached Titanium SSD (GiB) | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | [Simulate maintenance](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance)  
---|---|---|---|---|---  
18,000 or less | Minimum of 30 days | Live migrate | 7 days | Yes | Yes  
36,000 | Minimum of 30 days | Terminates with Local SSD data persistence | 7 days | Yes | Yes  
72,000 (bare metal) | Minimum of 180 days | Terminates with Local SSD data persistence | 90 days | Yes | Yes  
  
The maintenance frequencies shown in the previous table are approximations, not guarantees. Compute Engine might occasionally perform maintenance more frequently. 

Compute Engine preserves data on the local Titanium SSD disks for Z3 instances during maintenance events.

If a host event occurs, Compute Engine tries to recover any Titanium SSD disks attached to the instance. By default, Compute Engine spends up to 1 hour recovering the data. For Z3 instances, Compute Engine spends up to 6 hours trying to recover the Titanium SSD data before reaching the timeout limit. This timeout limit is customizable. For more information about Local SSD and Titanium SSD recovery options, see [Disk persistence following instance termination](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#disk-persistence).

## What's next

  * [Creating and starting a virtual machine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance)
  * Learn about the different [Storage options](https://docs.cloud.google.com/compute/docs/disks) for your VM
  * [Move your workload to a new compute instance](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm)
  * [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#storage-optimized)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
