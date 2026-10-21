---
url: https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances/
title: Bare metal instances \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:05.399200+00:00
---

# Bare metal instances  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Bare metal instances Stay organized with collections  Save and categorize content based on your preferences. 

In addition to virtual machine (VM) instances, Compute Engine also offers bare metal instances. Bare metal instances provide direct access to the host server's CPU and memory, without Compute Engine's hypervisor in the middle. Bare metal instances also expose all CPU performance counters and built in [CPU accelerators](https://docs.cloud.google.com/compute/docs/cpu-platforms#accelerators).

Bare metal instances on Compute Engine are consumed and managed in the same way as VM instances. Bare metal instances run on physical servers in Google data centers and are fully managed by Google.

When you select a machine type with a name that contains `-metal`, you create a bare metal instance in the same way that you create a VM instance. For example, you can:

  * Attach Google Cloud Hyperdisk storage to a bare metal instance.
  * Configure the network interface to attach to a Virtual Private Cloud (VPC) network and subnetwork.



## Workload recommendations for bare metal instances

Cloud native bare metal instances are generally not substitutes for VM instances, but they expand the types of workloads you can run on Compute Engine. Some of the use cases for bare metal instances are:

  * Workloads that require direct, non-hypervisor mediated access to the host server's CPU and memory resources, primarily to run third-party hypervisors: 
    * Networking security
    * CI/CD Pipelines
    * Third-party private clouds and VMware (through Google Cloud VMware Engine).
  * Workloads that are sensitive to CPU performance
  * Workloads that require direct access to CPU counters and process to thread pinning, such as financial exchanges or other realtime workloads
  * Workloads that use non-virtualizable, [on-CPU chip accelerators](https://docs.cloud.google.com/compute/docs/cpu-platforms#accelerators) such as QAT, DLB, and IAA
  * Workloads not licensed for virtual machine use



## Differences between VM instances and bare metal instances

Almost all of the features of VM instances are available with bare metal instances. Bare metal instances require a dedicated host server. If you create a bare metal instance, then that compute instance is the only one that can run on the host server. 

The features not available with bare metal instances include:

Feature | VM instances | Bare metal instances  
---|---|---  
Network interface | VirtIO is the default interface type for [first and second generation](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology) machine series and gVNIC is supported with some second generation machine series. GVNIC is required by third generation and later machine series.  | [Intel IDPF LAN PF device driver](https://docs.cloud.google.com/compute/docs/networking/using-idpf). Bare metal instances don't run a hypervisor and don't support gVNIC or VirtIO.  
Multiple network interfaces | Each VM can have up to 10 network interfaces. | 

  * Z4M bare metal instances come with two physical NICs and support up to 10 network interfaces per instance.
  * All other bare metal instances have a single network interface. You can use Dynamic Network Interfaces to configure additional network interfaces. For more information about using multiple network interfaces with a bare metal instance, see [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts). 

  
Disk interface | 

  * For first and second generation machine series, SCSI is the default for Persistent Disk but NVMe can be used for Local SSD disks. 
  * For third generation and later machine series, only NVMe is supported.

| Only NVMe.  
Attached disks | VM instances can use standard Persistent Disk, Hyperdisk storage, and Local SSD. | Bare metal instances don't support Persistent Disk.  
Windows OS support | VM instances support Windows images. | Bare metal instances don't provide support for Windows images.  
Virtual Trusted Platform Module (vTPM) | Features such as Secure Boot, vTPM-enabled Measured Boot, and other Shielded VM features are available. | vTPM features aren't available with bare metal instances with the exception of A4X Max and C4A bare metal.  
On host maintenance | VM instances support live migration. | The maintenance behavior must be set to `TERMINATE`. Live migration is not feasible. Bare metal instances with attached Local SSD disks can be set to `RESTART IN PLACE` to preserve the Local SSD disk data.  
CPU utilization monitoring | Available using hypervisor metrics. | CPU utilization monitoring isn't available. If you install the Ops Agent, you can instead use the metric `OS Reported CPU %`.   
  
## Machine series with bare metal machine types

You can create a bare metal instance using machine types from the following machine series.

### A4X Max machine series

[A4X Max](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms) bare metal instances are powered by NVIDIA GB300 Grace Blackwell Ultra Superchips. The A4X Max machine series offers one bare metal machine type:

  * `a4x-maxgpu-4g-metal` comes with 144 vCPUs and 960 GB of memory.



A4X Max uses NVIDIA Grace CPUs with Arm Neoverse V2 cores, which are connected to four NVIDIA B300 Blackwell GPUs. You can attach Hyperdisk Balanced, Hyperdisk Extreme, Hyperdisk ML, and Hyperdisk Throughput disks to A4X Max bare metal instances. 12,000 GB of Local SSD storage is automatically attached to A4X Max bare metal instances. A4X Max bare metal instances offer up to 3,600 Gbps of network bandwidth.

The A4X Max machine series is part of the [accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines), which is designed for AI, ML, and HPC workloads.

### C4 machine series

[C4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series) bare metal instances are powered by 6th generation Intel Xeon Scalable processors (code-named Granite Rapids). You can create C4 bare metal instances with 288 vCPUs, up to 2,232 GB of memory, and 18 TiB of local Titanium SSD storage. Bare metal instances require a dedicated host server. If you create a bare metal instance, then that compute instance is the only one that can run on the host server. 

The amount of memory available to your bare metal instance depends on which machine type you use:

  * **`standard`** : 288 vCPUs and 1,080 GB of memory.
  * **`highmem`** : 288 vCPUs and 2,232 GB of memory.



C4 is built on [Titanium](https://cloud.google.com/titanium) which offloads processing from the host CPU for network processes and Titanium SSD disk I/O. You can attach Hyperdisk Balanced and Hyperdisk Extreme disks to C4 bare metal instances. C4 bare metal instances offer up to 100 Gbps network bandwidth for standard networking and up to 200 Gbps with per VM Tier_1 networking performance.

The C4 machine series is part of the [general-purpose machine family](https://docs.cloud.google.com/compute/docs/general-purpose-machines), which has excellent price-performance with flexible vCPU to memory ratios.

### C4A machine series

[C4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series) bare metal instances are powered by Google Axion processors. You can create a `standard` C4A bare metal instance `c4a-standard-96-metal` with 96 vCPUs and 384 GB of memory or a `highmem` C4A bare metal instance `c4a-highmem-96-metal` with 96 vCPUs and 768 GB of memory.

C4A is built on [Titanium](https://cloud.google.com/titanium) which offloads processing from the host CPU for network processes and Titanium SSD disk I/O. You can attach Hyperdisk Balanced, Hyperdisk Extreme, Hyperdisk Throughput, and Hyperdisk ML disks to C4A bare metal instances. C4A bare metal instances offer up to 50 Gbps network bandwidth for standard networking and up to 100 Gbps with per VM Tier_1 networking performance.

### C4D machine series

[C4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4d_series) instances are powered by 5th generation AMD EPYC Turin processors. You can create C4D bare metal instances with 384 vCPUs and up to 3,072 GB of memory. Bare metal instances require a dedicated host server. If you create a bare metal instance, then that compute instance is the only one that can run on the host server. 

The amount of memory available to your bare metal instance depends on which machine type you use:

  * `c4d-highcpu-384-metal` comes with 384 vCPUs and 768 GB of memory.
  * `c4d-standard-384-metal` comes with 384 vCPUs and 1,488 GB of memory.
  * `c4d-highmem-384-metal` comes with 384 vCPUs and 3,072 GB of memory.



C4D is built on [Titanium](https://cloud.google.com/titanium) which uses network offloads. You can attach Hyperdisk Balanced and Hyperdisk Extreme disks to C4D bare metal instances. Local SSD disks aren't available for C4D bare metal instances, but are available with C4D VMs created with a machine type that ends in `-lssd`. C4D bare metal instances offer up to 100 Gbps network bandwidth for standard networking and up to 200 Gbps network bandwidth for per VM Tier_1 networking performance.

The C4D machine series is part of the general-purpose machine family. To learn more about the machine types and features of C4D, see [C4D machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4d_series).

### C3 machine series

[C3](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_series) is the first machine series to offer a bare metal machine type. C3 instances are powered by 4th generation Intel Xeon Scalable processors (code-named Sapphire Rapids). You can create C3 bare metal instances with 192 vCPUs and up to 1,536 GB of memory. Bare metal instances require a dedicated host server. If you create a bare metal instance, then that compute instance is the only one that can run on the host server. 

The amount of memory available to your bare metal instance depends on which machine type you use:

  * `c3-highcpu-192-metal` comes with 192 vCPUs and 512 GB of memory.
  * `c3-standard-192-metal` comes with 192 vCPUs and 768 GB of memory.
  * `c3-highmem-192-metal` comes with 192 vCPUs and 1,536 GB of memory.



C3 is built on [Titanium](https://cloud.google.com/titanium) which uses network offloads. You can attach Hyperdisk Balanced and Hyperdisk Extreme disks to C3 bare metal instances. Local SSD disks aren't available for C3 bare metal instances, but are available with C3 VMs created with a machine type that ends in `-lssd`. C3 bare metal instances offer up to 100 Gbps network bandwidth for standard networking and up to 200 Gbps with per VM Tier_1 networking performance.

The C3 machine series is part of the [general-purpose machine family](https://docs.cloud.google.com/compute/docs/general-purpose-machines), which has the best price-performance with the most flexible vCPU to memory ratios.

### X5 machine series

The [X5 machine series](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x5_series) is the direct successor to the X4 bare metal series. It significantly expands the maximum available memory to 48TB and uses next-generation Intel Granite Rapids (GNR) CPUs. The X5 machine series is purpose-built and certified for ultra-large SAP HANA scale-up workloads.

X5 offers these predefined machine types:

  * `x5-688-12T-metal` comes with 688 vCPUs and 12,288 GB of memory and 4 sockets.
  * `x5-688-16T-metal` comes with 688 vCPUs and 16,384 GB of memory and 4 sockets.
  * `x5-1376-24T-metal` comes with 1,376 vCPUs and 24,576 GB of memory and 8 sockets.
  * `x5-1376-32T-metal` comes with 1,376 vCPUs and 32,768 GB of memory and 8 sockets.
  * `x5-2064-48T-metal` comes with 2,064 vCPUs and 49,152 GB of memory and 12 sockets. 



X5 instances are powered by the 6th generation Intel Xeon Scalable processor (code-named Granite Rapids) and [Titanium](https://cloud.google.com/titanium). X5 instances can be used with all Hyperdisk storage. Local SSD disks aren't available for X5 instances. X5 supports up to 200 Gbps network bandwidth for standard networking.

The X5 machine series is part of the [memory-optimized machine family](https://docs.cloud.google.com/compute/docs/memory-optimized-machines), which provides the most compute and memory resources of any Compute Engine machine family and higher memory-to-vCPU ratios than general-purpose machine types.

### X4 machine series

The [X4 machine series](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x4_series) offers these predefined machine types:

  * `x4-480-6t-metal` comes with 480 vCPUs and 6,144 GB of memory.
  * `x4-480-8t-metal` comes with 480 vCPUs and 8,192 GB of memory.
  * `x4-960-12t-metal` comes with 960 vCPUs and 12,288 GB of memory.
  * `x4-960-16t-metal` (previously `x4-megamem-960-metal`) comes with 960 vCPUs and 16,384 GB of memory.
  * `x4-1440-24t-metal` (previously `x4-megamem-1440-metal`) comes with 1,440 vCPUs and 24,576 GB of memory.
  * `x4-1920-32t-metal` (previously `x4-megamem-1920-metal`) comes with 1,920 vCPUs and 32,768 GB of memory.



X4 instances are powered by the 4th generation Intel Xeon Scalable processor (code-named Sapphire Rapids) and [Titanium](https://cloud.google.com/titanium). X4 instances can be used with only Hyperdisk Balanced and Hyperdisk Extreme storage. Local SSD disks aren't available for X4 instances. X4 supports up to 100 Gbps network bandwidth for standard networking.

The X4 machine series is part of the [memory-optimized machine family](https://docs.cloud.google.com/compute/docs/memory-optimized-machines), which provides the most compute and memory resources of any Compute Engine machine family and higher memory-to-vCPU ratios than general-purpose machine types.

### Z4D machine series

[Z4D instances](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4d_series) are powered by AMD EPYC Turin processors, DDR5 memory, and [Titanium offload processors](https://cloud.google.com/titanium). Z4D machine types are optimized for the underlying NUMA architecture to deliver optimal, reliable, and consistent performance. Z4D also offers larger Titanium SSD disk sizes than Z3.

Z4D offers only a single bare metal machine type: `z4d-highmem-384-standardlssd-metal`. This machine type comes with 384 vCPUs, 3,072 GB of memory, two physical NICs, and 84,000 GiB of local Titanium SSD storage.

The Z4D machine series is part of the storage-optimized machine family, and provides high density, high performing Titanium SSD storage. Z4D provides high vCPU to Titanium SSD capacity ratios of any machine series offered by Google Cloud.

You can attach Hyperdisk Balanced, Hyperdisk Balanced High Availability, Hyperdisk Extreme, Hyperdisk ML, and Hyperdisk Throughput disks to Z4D bare metal instances. Z4D bare metal instances offer up to 400 Gbps network bandwidth for standard networking.

### Z4M machine series

[Z4M](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4m_series) is a multi-NIC storage-optimized machine series. Z4M supports Cloud RDMA. Z4M instances are powered by 5th generation Intel Emerald Rapids Xeon Scalable processors. Bare metal instances require a dedicated host server. If you create a bare metal instance, then that compute instance is the only one that can run on the host server. 

To create a Z4M bare metal instance, use the `z4m-highmem-192-metal` machine type. This machine type comes with 192 vCPUs, 1,536 GB of memory, 168,000 GiB of local Titanium SSD storage, and up to 400 Gbps network bandwidth.

Z4M is built on [Titanium](https://cloud.google.com/titanium), which uses network offloads. You can attach any type of Hyperdisk disk to Z4M bare metal instances.

The Z4M machine series is part of the storage-optimized machine family, and provides high density, high performing Titanium SSD storage. Z4M provides higher vCPU to Titanium SSD capacity ratios of any machine series offered by Google Cloud.

### Z3 machine series

[Z3](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_series) is the first machine series to offer Titanium SSD disks with a bare metal machine type. Z3 instances are powered by 4th generation Intel Xeon Scalable processors (code-named Sapphire Rapids).

Z3 offers only a single bare metal machine type: `z3-highmem-192-highlssd-metal`. This machine type comes with 192 vCPUs, 1,536 GB of memory, and 72,000 GiB of local Titanium SSD storage.

Z3 is built on [Titanium](https://cloud.google.com/titanium), which uses network offloads. You can attach Hyperdisk Balanced and Hyperdisk Extreme disks to Z3 bare metal instances. Z3 bare metal instances offer up to 100 Gbps network bandwidth for standard networking and up to 200 Gbps with per VM Tier_1 networking performance.

The Z3 machine series is part of the storage-optimized machine family, and provides high density, high performing Titanium SSD storage.

## Supported OS images for bare metal instances

Because bare metal instances use the IDPF network driver, you can only use [OS images that support IDPF](https://docs.cloud.google.com/compute/docs/images/os-details#networking).

**Note:** C4D bare metal instances don't support SUSE Linux Enterprise Server (SLES) version 15 SP6.

## Regional availability of bare metal instances

The following sortable table shows the regional availability of bare metal instances and which bare metal machine types are available in each zone. You can filter the table rows by geographical location or machine series. You can also sort the table by **Zones**.

Machine type names that include an asterisk (`*`) symbol represent machine types either with or without Titanium SSD disks attached. For example, `c4-standard-288-*-metal` represents both the `c4-standard-288-metal` and `c4-standard-288-lssd-metal` machine types.

For information about the regional availability of A4X Max bare metal instances, see [GPU locations](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones).

APACNorth AmericaSouth AmericaEuropeMiddle EastAfricaA4X MaxC4 C4AC4DC3X4X5Z3Z4DZ4M

Clear all

Zones | Location | Machine series | Machine types  
---|---|---|---  
`africa-south1-a`  
`africa-south1-b`  
`africa-south1-c` | Johannesburg, South Africa | N/A | N/A  
`asia-east1-a` | Changhua County, Taiwan, APAC | C3, Z3 | `c3-highmem-192-metal`  
`z3-highmem-192-highlssd-metal`  
`asia-east1-b` | Changhua County, Taiwan, APAC | Z3 | `z3-highmem-192-highlssd-metal`  
`asia-east1-c` | Changhua County, Taiwan, APAC | C3, Z3 | `c3-highmem-192-metal`  
`z3-highmem-192-highlssd-metal`  
`asia-east2-a`  
`asia-east2-b`  
`asia-east2-c` | Hong Kong, APAC | N/A | N/A  
`asia-northeast1-a` | Tokyo, Japan, APAC | C4A | `c4a-highmem-96-metal`  
`asia-northeast1-b` | Tokyo, Japan, APAC | C4A, Z3 | `c4a-highmem-96-metal`  
`z3-highmem-192-highlssd-metal`  
`asia-northeast1-c` | Tokyo, Japan, APAC | N/A | N/A  
`asia-northeast2-a`  
`asia-northeast2-b`  
`asia-northeast2-c` | Osaka, Japan, APAC | N/A | N/A  
`asia-northeast3-a`  
`asia-northeast3-b`  
`asia-northeast3-c` | Seoul, South Korea, APAC | N/A | N/A  
`asia-south1-a` | Mumbai, India, APAC | N/A | N/A  
`asia-south1-b` | Mumbai, India, APAC | C3, X4 | `c3-highmem-192-metal`  
For X4, contact sales team  
`asia-south1-c` | Mumbai, India, APAC | X4, Z3 | For X4, contact sales team  
`z3-highmem-192-highlssd-metal` | X4, Z3 | Contact sales team  
`asia-south2-a` | Delhi, India, APAC | X4, X5 | Contact sales team  
`asia-south2-b`  
`asia-south2-c` | Delhi, India, APAC | N/A | N/A  
`asia-southeast1-a` | Jurong West, Singapore, APAC | C4 , C3, Z3 | `c4-standard-288-*-metal`  
`c4-highmem-288-*-metal`  
`c3-highcpu-192-metal`  
`c3-standard-192-metal`  
`c3-highmem-192-metal`  
`z3-highmem-192-highlssd-metal`  
`asia-southeast1-b` | Jurong West, Singapore, APAC | C4 , C4D, Z3 | `c4-standard-288-*-metal`  
`c4-highmem-288-*-metal`  
`c4d-highcpu-384-metal`  
`c4d-standard-384-metal`  
`c4d-highmem-384-metal`  
`z3-highmem-192-highlssd-metal`  
`asia-southeast1-c` | Jurong West, Singapore, APAC | C4 , C3, Z3 | `c4-standard-288-*-metal`  
`c4-highmem-288-*-metal`  
`c3-highcpu-192-metal`  
`c3-standard-192-metal`  
`z3-highmem-192-highlssd-metal`  
`asia-southeast2-a`  
`asia-southeast2-b`  
`asia-southeast2-c` | Jakarta, Indonesia, APAC | N/A | N/A  
`asia-southeast2-b`  
`asia-southeast2-c` | Jakarta, Indonesia, APAC | N/A | N/A  
`australia-southeast1-a`  
`australia-southeast1-b`  
`australia-southeast1-c` | Sydney, Australia, APAC | N/A | N/A  
`australia-southeast2-a`  
`australia-southeast2-b` | Melbourne, Australia, APAC | Z3 | `z3-highmem-192-highlssd-metal`  
`australia-southeast2-c` | Melbourne, Australia, APAC | Z3 | `z3-highmem-192-highlssd-metal`  
`australia-southeast2-c` | Melbourne, Australia, APAC | N/A | N/A  
`europe-central2-a`  
`europe-central2-b`  
`europe-central2-c` | Warsaw, Poland, Europe | N/A | N/A  
`europe-north2-a` | Stockholm, Sweden, Europe | C3, Z3 | `c3-highmem-192-metal`  
`z3-highmem-192-highlssd-metal`  
`europe-north2-b` | Stockholm, Sweden, Europe | C3 | `c3-highmem-192-metal`  
`europe-north2-c` | Stockholm, Sweden, Europe | N/A | N/A  
`europe-southwest1-a`  
`europe-southwest1-b`  
`europe-southwest1-c` | Madrid, Spain, Europe | C4  | `c4-highmem-288-*-metal`  
`europe-west1-b`  
`europe-west1-c` | St. Ghislain, Belgium, Europe | C3, C4, X4, X5, Z3 | `c3-highcpu-192-metal`  
`c3-standard-192-metal`  
`c3-highmem-192-metal`  
`c4-standard-288-*-metal`  
`c4-highmem-288-*-metal`  
For X4 and X5, contact sales team  
`z3-highmem-192-highlssd-metal`  
`europe-west1-d` | St. Ghislain, Belgium, Europe | N/A | N/A  
`europe-west2-a`  
`europe-west2-b` | London, England, Europe | Z3 | `z3-highmem-192-highlssd-metal`  
`europe-west2-c` | London, England, Europe | N/A | N/A  
`europe-west3-a` | Frankfurt, Germany, Europe | C3, C4A, X4 | `c3-highmem-192-metal`  
`c4a-highmem-96-metal`  
For X4, contact sales team  
`europe-west3-b` | Frankfurt, Germany, Europe | C3, C4A, X4, Z3 | `c3-highmem-192-metal`  
`c4a-highmem-96-metal`  
For X4, contact sales team  
`z3-highmem-192-highlssd-metal`  
`europe-west3-c` | Frankfurt, Germany, Europe | C4A, Z3 |  `c4a-highmem-96-metal`  
`z3-highmem-192-highlssd-metal`  
`europe-west4-a` | Eemshaven, Netherlands, Europe | C4 , C4A, C4D, X4, Z3 | `c4-standard-288-*-metal`  
`c4-highmem-288-*-metal`  
`c4a-highmem-96-metal`  
`c4d-highcpu-384-metal`  
`c4d-standard-384-metal`  
`c4d-highmem-384-metal`  
For X4, contact sales team  
`z3-highmem-192-highlssd-metal`  
`europe-west4-b` | Eemshaven, Netherlands, Europe | C4 , C4A, C4D, C3, X4, Z3 | `c4-standard-288-*-metal`  
`c4-highmem-288-*-metal`  
`c4a-highmem-96-metal`  
`c4d-highcpu-384-metal`  
`c4d-standard-384-metal`  
`c4d-highmem-384-metal`  
`c3-highcpu-192-metal`  
`c3-highmem-192-metal`  
For X4, contact sales team  
`z3-highmem-192-highlssd-metal`  
`europe-west4-c` | Eemshaven, Netherlands, Europe | C3, C4A, X4, X5, Z3 | `c3-highcpu-192-metal`  
`c3-standard-192-metal`  
`c3-highmem-192-metal`  
`c4a-highmem-96-metal`  
For X4 and X5 contact sales team  
`z3-highmem-192-highlssd-metal`  
`europe-west6-a`  
`europe-west6-b`  
`europe-west6-c` | Zurich, Switzerland, Europe | N/A | N/A  
`europe-west8-a` | Milan, Italy, Europe | X4, X5 | For X4 and X5, contact sales team  
`europe-west8-b` | Milan, Italy, Europe | C4, Z3 | `c4-highmem-288-*-metal`  
`z3-highmem-192-highlssd-metal`  
`europe-west8-c` | Milan, Italy, Europe | X4, X5, Z3 | For X4 and X5, contact sales team  
`z3-highmem-192-highlssd-metal`  
`europe-west9-a`  
`europe-west9-b`  
`europe-west9-c` | Paris, France, Europe | N/A | N/A  
`europe-west10-a`  
`europe-west10-b`  
`europe-west10-c` | Berlin, Germany, Europe | N/A | N/A  
`europe-west12-a`  
`europe-west12-b`  
`europe-west12-c` | Turin, Italy, Europe | N/A | N/A  
`me-central1-a` | Doha, Qatar, Middle East | C3, Z3 | `c3-standard-192-metal`  
`c3-highmem-192-metal`  
`z3-highmem-192-highlssd-metal`  
`me-central1-b` | Doha, Qatar, Middle East | N/A | N/A  
`me-central1-c` | Doha, Qatar, Middle East | C3, Z3 | `c3-standard-192-metal`  
`c3-highmem-192-metal`  
`z3-highmem-192-highlssd-metal`  
`me-central2-a`  
`me-central2-b`  
`me-central2-c` | Dammam, Saudi Arabia, Middle East | N/A | N/A  
`me-west1-a`  
`me-west1-b`  
`me-west1-c` | Tel Aviv, Israel, Middle East | N/A | N/A  
`northamerica-northeast1-a`  
`northamerica-northeast1-b`  
`northamerica-northeast1-c` | Montréal, Québec, North America | N/A | N/A  
`northamerica-northeast2-a` | Toronto, Ontario, North America | N/A | N/A  
`northamerica-northeast2-b`  
`northamerica-northeast2-c` | Toronto, Ontario, North America | Z3 | `z3-highmem-192-highlssd-metal`  
`northamerica-south1-a`  
`northamerica-south1-b`  
`northamerica-south1-c` | Queretaro, Mexico, North America | N/A | N/A  
`southamerica-east1-a` | Osasco, São Paulo, Brazil, South America | Z3 | `z3-highmem-192-highlssd-metal`  
`southamerica-east1-b`  
`southamerica-east1-c` | Osasco, São Paulo, Brazil, South America | N/A | N/A  
`southamerica-west1-a` | Santiago, Chile, South America | Z3 | `z3-highmem-192-highlssd-metal`  
`southamerica-west1-b`  
`southamerica-west1-c` | Santiago, Chile, South America | N/A | N/A  
`us-central1-a` | Council Bluffs, Iowa, North America | A4X Max, C4 , C4A, C3, X5, X4, Z4D, Z4M, Z3 | `a4x-maxgpu-4g-metal`  
`c3-standard-192-metal`  
`c3-highmem-192-metal`  
`c4-standard-288-*-metal`  
`c4-highmem-288-*-metal`  
`c4a-highmem-96-*-metal`  
For X4 and X5, contact sales team  
`z4d-highmem-384-standardlssd-metal`  
`z4m-highmem-192-metal`  
`z3-highmem-192-highlssd-metal`  
`us-central1-b` | Council Bluffs, Iowa, North America | A4X Max, C4 , C4A, C4D, X4, Z4D, Z3 | `a4x-maxgpu-4g-metal`  
`c4-standard-288-*-metal`  
`c4-highmem-288-*-metal`  
`c4a-highmem-96-metal`  
`c4d-standard-384-metal`  
For X4, contact sales team  
`z4d-highmem-384-standardlssd-metal`  
`z3-highmem-192-highlssd-metal`  
`us-central1-c` | Council Bluffs, Iowa, North America | C4 , C4A, C3, X4, X5, Z4D, Z3 | `c4-standard-288-*-metal`  
`c4-highmem-288-*-metal`  
`c4a-standard-96-metal`  
`c4a-highmem-96-metal`  
`c3-highcpu-192-metal`  
For X4 and X5, contact sales team  
`z4d-highmem-384-standardlssd-metal`  
`z3-highmem-192-highlssd-metal`  
`us-central1-f` | Council Bluffs, Iowa, North America | C4, Z4D | `c4-standard-288-*-metal`  
`c4-highmem-288-*-metal`  
`z4d-highmem-384-standardlssd-metal`  
`us-east1-b` | Moncks Corner, South Carolina, North America | C4, Z3 | `c4-standard-288-*-metal`  
`c4-highmem-288-*-metal`  
`z3-highmem-192-highlssd-metal`  
`us-east1-c` | Moncks Corner, South Carolina, North America | C3, C4, Z3 | `c3-highcpu-192-metal`  
`c3-standard-192-metal`  
`c3-highmem-192-metal`  
`c4-standard-288-*-metal`  
`c4-highmem-288-*-metal`  
`z3-highmem-192-highlssd-metal`  
`us-east1-d` | Moncks Corner, South Carolina, North America | C3, C4 | `c3-highcpu-192-metal`  
`c3-standard-192-metal`  
`c3-highmem-192-metal`  
`c4-standard-288-*-metal`  
`c4-highmem-288-*-metal`  
`us-east4-a` | Ashburn, Virginia, North America | A4X Max, C4 , C3, X5, X4, Z4D | `a4x-maxgpu-4g-metal`  
`c4-standard-288-*-metal`  
`c4-highmem-288-*-metal`  
`c3-highcpu-192-metal`  
`c3-standard-192-metal`  
`c3-highmem-192-metal`  
For X4 and X5, contact sales team  
`z4d-highmem-384-standardlssd-metal`  
`us-east4-b` | Ashburn, Virginia, North America | A4X Max, C4 , C4D, X4, Z4D, Z3 | `a4x-maxgpu-4g-metal`  
`c4-highmem-288-*-metal`  
`c4-standard-288-*-metal`  
`c4d-highcpu-384-metal`  
`c4d-standard-384-metal`  
`c4d-highmem-384-metal`  
For X4, contact sales team  
`z4d-highmem-384-standardlssd-metal`  
`z3-highmem-192-highlssd-metal`  
`us-east4-c` | Ashburn, Virginia, North America | C3, C4, C4A, X4, X5, Z4D, Z3 | `c3-highcpu-192-metal`  
`c3-standard-192-metal`  
`c3-highmem-192-metal`  
`c4-highmem-288-*-metal`  
`c4-standard-288-*-metal`  
`c4a-highmem-96-metal`  
For X4 and X5, contact sales team  
`z4d-highmem-384-standardlssd-metal`  
`z3-highmem-192-highlssd-metal`  
`us-east5-a` | Columbus, Ohio, North America | C3, C4, Z3, Z4D, Z4M | `c3-highcpu-192-metal`  
`c3-standard-192-metal`  
`c3-highmem-192-metal`  
`c4-highmem-288-*-metal`  
`c4-standard-288-*-metal`  
`z3-highmem-192-highlssd-metal`  
`z4d-highmem-384-standardlssd-metal`  
`z4m-highmem-192-metal`  
`us-east5-b` | Columbus, Ohio, North America | A4X Max, C3, C4A, Z3, Z4D, Z4M | `a4x-maxgpu-4g-metal`  
`c3-highcpu-192-metal`  
`c3-standard-192-metal`  
`c3-highmem-192-metal`  
`c4a-highmem-96-metal`  
`z3-highmem-192-highlssd-metal`  
`z4d-highmem-384-standardlssd-metal`  
`z4m-highmem-192-metal`  
`us-east5-c` | Columbus, Ohio, North America | A4X Max, Z3, Z4D, Z4M | `a4x-maxgpu-4g-metal`  
`z3-highmem-192-highlssd-metal`  
`z4d-highmem-384-standardlssd-metal`  
`z4m-highmem-192-metal`  
`us-south1-a` | Dallas, Texas, North America | C4, Z3 | `c4-highmem-288-*-metal`  
`z3-highmem-192-highlssd-metal`  
`us-south1-b` | Dallas, Texas, North America | C4 | `c4-highmem-288-*-metal`  
`us-south1-c` | Dallas, Texas, North America | N/A | N/A  
`us-west1-a`  
`us-west1-b` | The Dalles, Oregon, North America | C3, C4 | `c3-highcpu-192-metal`  
`c3-standard-192-metal`  
`c3-highmem-192-metal`  
`c4-highmem-288-*-metal`  
`c4-standard-288-*-metal`  
`us-west1-c` | The Dalles, Oregon, North America | C4 | `c4-highmem-288-*-metal`  
`c4-standard-288-*-metal`  
`us-west2-a` | Los Angeles, California, North America | Z3 | `z3-highmem-192-highlssd-metal`  
`us-west2-b`  
`us-west2-c` | Los Angeles, California, North America | N/A | N/A  
`us-west3-a`  
`us-west3-b`  
`us-west3-c` | Salt Lake City, Utah, North America | N/A | N/A  
`us-west4-a` | Las Vegas, Nevada, North America | C4A, X4 | `c4a-highmem-96-metal`  
For X4, contact sales team  
`us-west4-b` | Las Vegas, Nevada, North America | C4, X4 | `c4-highmem-288-*-metal`  
`c4-standard-288-*-metal`  
For X4, contact sales team  
`us-west4-c` | Las Vegas, Nevada, North America | C4A | `c4a-highmem-96-metal`  
  
## What's next

  * [Create and start a Compute Engine bare metal instance](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-public-image#baremetal).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
