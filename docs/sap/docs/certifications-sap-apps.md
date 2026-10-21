---
url: https://docs.cloud.google.com/sap/docs/certifications-sap-apps/
title: Certifications for SAP applications on Google Cloud \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:14:32.521506+00:00
---

# Certifications for SAP applications on Google Cloud  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/certifications-sap-apps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Certifications for SAP applications on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the SAP application solutions that are certified by SAP to run on Google Cloud. The page also lists the operating systems and Google Cloud infrastructure that SAP has certified for use with the SAP application solutions.

The certifications on this page don't apply to SAP HANA. For SAP HANA, see [Certified SAP HANA configurations on Google Cloud](https://docs.cloud.google.com/sap/docs/certifications-sap-hana) or [Certified and supported SAP HANA hardware directory](https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=iaas;ve:29).

The content in this document is for informational purposes only. The official source of certification information for SAP applications on Google Cloud is [ SAP Note 2456432 - SAP Applications on Google Cloud: Supported Products and Google Cloud machine types](https://launchpad.support.sap.com/#/notes/2456432). To access SAP Notes, you need to login to [SAP ONE Support Launchpad](https://launchpad.support.sap.com/) using your S-user account.

## Certified SAP applications on Google Cloud

The following table lists the SAP application solutions that are certified to run on Google Cloud, as well as the operating systems and the Compute Engine VM families that they are certified to run with.

For SAP application solutions that use SAP HANA, such as S/4HANA or BW/4HANA, the VM support requirements for SAP HANA apply if SAP HANA is installed on the same VM as the application system.

For a detailed list of the certified machine types, see the following section, Certified Compute Engine machine types.

For more information about the supported operating systems, see [Operating system support for SAP NetWeaver on Google Cloud](https://docs.cloud.google.com/sap/docs/netweaver-os-support).

SAP solution | Supported database options | Supported operating systems | Certified machine types  
---|---|---|---  
SAP NetWeaver AS, ABAP/Java  
SAP S/4HANA (3-tier configuration)  
SAP BW/4HANA (3-tier configuration)  
SAP ECC  
SAP Business Suite  
SAP NetWeaver Business Warehouse  
SAP Landscape Transformation  
Replication Server (SLT)  
SAP Solution Manager  
SAP BusinessObjects BI Suite |  SAP HANA  
SAP Adaptive Server Enterprise (ASE)  
SAP IQ  
SAP MaxDB, SAP liveCache, and SAP Content Server  
IBM Db2  
Microsoft SQL Server |  SUSE Linux Enterprise Server (11, 12, and 15)  
Red Hat Enterprise Linux (6, 7, 8, and 9 Note)  
Microsoft Windows Server (2016, 2019, 2022, and 2025)  
|  Compute-optimized  
General-purpose  
Memory-optimized  
Custom  
Bare Metal Solution servers  
Oracle Database 19c or later |  [ Oracle Linux 8 and 9 with UEK](https://docs.cloud.google.com/sap/docs/oracle-planning#supported_operating_systems)  
SAP Business One (9.3 and 10.0) | SAP HANA  | For 9.3, SLES 12 SP3  
For 10.0, SLES 15 and later  | n2-highmem-8  
n2-highmem-16  
n2-highmem-32  
n2-highmem-64  
n2-highmem-80  
n1-highmem-32  
n1-highmem-64   
Microsoft SQL Server  | Microsoft Windows Server | Any Compute Engine machine type that satisfies [Business One hardware requirements](https://help.sap.com/doc/011000358700000244612011e/9.3/en-US/B1_Hardware_Requirements_Guide.pdf)  
SAP Financial Consolidation | SAP HANA |  Linux  
Microsoft Windows |  Compute-optimized  
General-purpose  
Memory-optimized  
Custom  
Bare Metal Solution servers  
**Note:** Before you install any SAP software on RHEL for SAP 9.x, additional packages must be installed on your host machines, especially `chkconfig` and `compat-openssl11`. If you use an image provided by Compute Engine, then these packages are automatically installed for you. For more information from SAP, see the SAP note [3108316 - Red Hat Enterprise Linux 9.x: Installation and Configuration](https://me.sap.com/notes/3108316). 

## Certified machine types for SAP applications

Google Cloud offers SAP-certified machines in the following machine-type families:

  * Compute-optimized machine types: C2 or C2D
  * General-purpose machine types: N1, N2, N2D, T2D, C3, C3D, C4, or C4D
  * Memory-optimized machine types: M1, M2, M3, M4, M4N, X4, or X5
  * Bare Metal Solution servers: O2
  * Custom machine types based on the machine types: N1, N2, or N2D



For the SAPS numbers for each machine type that are formally certified by SAP, see [ SAP Note 2456432 - SAP Applications on Google Cloud: Supported Products and Google Cloud machine types](https://launchpad.support.sap.com/#/notes/2456432).

Predefined machine types have a fixed set of resources. To define your own machine type, see Custom machine types.

Before selecting a machine type for use, confirm that it is available in the region and zones that you need.

For more information about each Compute Engine machine type, including its regional and zonal availability, see [Machine types](https://docs.cloud.google.com/compute/docs/machine-types).

For the availability of Bare Metal Solution machine types, see Regional availability of SAP-certified Bare Metal Solution machines.

### Compute-optimized machine types

The Compute Engine compute-optimized machine types, C2 and C2D, that are certified for SAP applications are optimized for compute-intensive workloads.

The compute-optimized machines provide the option to run on either an Intel or AMD CPU platform. The C2 machines run on Intel and the C2D machines run on AMD.

For more information, see [Compute-optimized machine family](https://docs.cloud.google.com/compute/docs/compute-optimized-machines).

#### C2 compute-optimized machine types

The C2 machine types run on an Intel CPU platform. The SAP-certified configurations of the `c2-standard` machines have 4 GB of memory per vCPU.

Built on Intel Cascade Lake scalable processors, the c2-standard machine types offer up to 3.1 Ghz base frequency, and 3.8 Ghz all-core-turbo.

C2 compute-optimized machines | vCPUs | Memory (GB) | Minimum CPU platform  
---|---|---|---  
`c2-standard-4` | 4 | 16 | Intel Cascade Lake  
`c2-standard-8` | 8 | 32 | Intel Cascade Lake  
`c2-standard-16` | 16 | 64 | Intel Cascade Lake  
`c2-standard-30` | 30 | 120 | Intel Cascade Lake  
`c2-standard-60` | 60 | 240 | Intel Cascade Lake  
  
#### C2D compute-optimized machine types

The C2D machine types run on an AMD CPU platform. The SAP-certified configurations of the `c2d-standard` machines have 4 GB of memory per vCPU. The SAP-certified configurations of the `c2d-highmem` machines have 8 GB of memory per vCPU.

C2D compute-optimized machines | vCPUs | Memory (GB) | Minimum CPU platform  
---|---|---|---  
**`c2d-highmem` machine types**  
`c2d-highmem-2` | 2 | 16 | AMD EPYC Milan  
`c2d-highmem-4` | 4 | 32 | AMD EPYC Milan  
`c2d-highmem-8` | 8 | 64 | AMD EPYC Milan  
`c2d-highmem-16` | 16 | 128 | AMD EPYC Milan  
`c2d-highmem-32` | 32 | 256 | AMD EPYC Milan  
`c2d-highmem-56` | 56 | 448 | AMD EPYC Milan  
`c2d-highmem-112` | 112 | 896 | AMD EPYC Milan  
**`c2d-standard` machine types**  
`c2d-standard-2` | 2 | 8 | AMD EPYC Milan  
`c2d-standard-4` | 4 | 16 | AMD EPYC Milan  
`c2d-standard-8` | 8 | 32 | AMD EPYC Milan  
`c2d-standard-16` | 16 | 64 | AMD EPYC Milan  
`c2d-standard-32` | 32 | 128 | AMD EPYC Milan  
`c2d-standard-56` | 56 | 224 | AMD EPYC Milan  
`c2d-standard-112` | 112 | 448 | AMD EPYC Milan  
  
### General-purpose machine types

With a balance of vCPUs and memory, the Compute Engine general-purpose machine types N1, N2, N2D, T2D, C3, C3D, C4, and C4D offer the best price-performance ratio for a variety of workloads.

For use with SAP NetWeaver based applications, SAP has certified the standard and high-memory configurations of the N1, N2, N2D, C3, C3D, C4, and C4D general-purpose machine types.

The T2D general-purpose machine types certified by SAP include only the standard configuration.

For more information, see [General-purpose machine family](https://docs.cloud.google.com/compute/docs/general-purpose-machines).

#### C4D general-purpose machine types

The C4D machine types are the fifth generation of the general-purpose machines and run on the AMD EPYC Turin™ CPU platform. The following table shows the C4D machine types that are certified by SAP for use with SAP NetWeaver:

C4D general-purpose machines | vCPUs | Memory (GB) | Minimum CPU platform  
---|---|---|---  
**C4D high-memory machine types**  
`c4d-highmem-2` | 2 | 15 | AMD EPYC Turin  
`c4d-highmem-4` | 4 | 31 | AMD EPYC Turin  
`c4d-highmem-8` | 8 | 63 | AMD EPYC Turin  
`c4d-highmem-16` | 16 | 126 | AMD EPYC Turin  
`c4d-highmem-32` | 32 | 252 | AMD EPYC Turin  
`c4d-highmem-48` | 48 | 378 | AMD EPYC Turin  
`c4d-highmem-64` | 64 | 504 | AMD EPYC Turin  
`c4d-highmem-96` | 96 | 756 | AMD EPYC Turin  
`c4d-highmem-192` | 192 | 1,512 | AMD EPYC Turin  
`c4d-highmem-384` | 384 | 3,024 | AMD EPYC Turin  
`c4d-highmem-384-metal` | 384 | 3,072 | AMD EPYC Turin  
**C4D standard machine types**  
`c4d-standard-2` | 2 | 7 | AMD EPYC Turin  
`c4d-standard-4` | 4 | 15 | AMD EPYC Turin  
`c4d-standard-8` | 8 | 31 | AMD EPYC Turin  
`c4d-standard-16` | 16 | 62 | AMD EPYC Turin  
`c4d-standard-32` | 32 | 124 | AMD EPYC Turin  
`c4d-standard-48` | 48 | 186 | AMD EPYC Turin  
`c4d-standard-64` | 64 | 248 | AMD EPYC Turin  
`c4d-standard-96` | 96 | 372 | AMD EPYC Turin  
`c4d-standard-192` | 192 | 744 | AMD EPYC Turin  
`c4d-standard-384` | 384 | 1,488 | AMD EPYC Turin  
`c4d-standard-384-metal` | 384 | 1,536 | AMD EPYC Turin  
  
#### C4 general-purpose machine types

The C4 machine types are the fourth generation of the general-purpose machines and run on the Intel Emerald Rapids CPU platform. The SAP-certified configurations of the `c4-standard` machines have 3.75 GB of memory per vCPU. The SAP-certified configurations of the `c4-highmem` machines have 7.75 GB of memory per vCPU.

C4 general-purpose machines | vCPUs | Memory (GB) | Minimum CPU platform  
---|---|---|---  
**C4 high-memory machine types**  
`c4-highmem-2` | 2 | 15 | Intel Emerald Rapids  
`c4-highmem-4` | 4 | 31 | Intel Emerald Rapids  
`c4-highmem-8` | 8 | 62 | Intel Emerald Rapids  
`c4-highmem-16` | 16 | 124 | Intel Emerald Rapids  
`c4-highmem-32` | 32 | 248 | Intel Emerald Rapids  
`c4-highmem-48` | 48 | 372 | Intel Emerald Rapids  
`c4-highmem-96` | 96 | 744 | Intel Emerald Rapids  
`c4-highmem-144` | 144 | 1,116 | Intel Granite Rapids  
`c4-highmem-192` | 192 | 1,488 | Intel Emerald Rapids  
`c4-highmem-288` | 288 | 2,232 | Intel Granite Rapids  
`c4-highmem-288-metal` | 288 | 2,232 | Intel Granite Rapids  
**C4 standard machine types**  
`c4-standard-2` | 2 | 7 | Intel Emerald Rapids  
`c4-standard-4` | 4 | 15 | Intel Emerald Rapids  
`c4-standard-8` | 8 | 30 | Intel Emerald Rapids  
`c4-standard-16` | 16 | 60 | Intel Emerald Rapids  
`c4-standard-32` | 32 | 120 | Intel Emerald Rapids  
`c4-standard-48` | 48 | 180 | Intel Emerald Rapids  
`c4-standard-96` | 96 | 360 | Intel Emerald Rapids  
`c4-standard-144` | 144 | 540 | Intel Granite Rapids  
`c4-standard-192` | 192 | 720 | Intel Emerald Rapids  
`c4-standard-288` | 288 | 1,080 | Intel Granite Rapids  
`c4-standard-288-metal` | 288 | 1,080 | Intel Granite Rapids  
  
#### C3 general-purpose machine types

The C3 machine types are the third generation of the general-purpose machines and run on an Intel CPU platform. The SAP-certified configurations of the `c3-standard` machines have 4 GB of memory per vCPU. The SAP-certified configurations of the `c3-highmem` machines have 8 GB of memory per vCPU.

The C3 series also includes bare metal machine types.

C3 general-purpose machines | vCPUs | Memory (GB) | Minimum CPU platform  
---|---|---|---  
**`c3-standard` bare metal machine types**  
`c3-standard-192-metal` | 192 | 768 | Intel Sapphire Rapids  
**`c3-highmem` bare metal machine types**  
`c3-highmem-192-metal` | 192 | 1,536 | Intel Sapphire Rapids  
**`c3-highmem` machine types**  
`c3-highmem-4` | 4 | 32 | Intel Sapphire Rapids  
`c3-highmem-8` | 8 | 64 | Intel Sapphire Rapids  
`c3-highmem-22` | 22 | 176 | Intel Sapphire Rapids  
`c3-highmem-44` | 44 | 352 | Intel Sapphire Rapids  
`c3-highmem-88` | 88 | 704 | Intel Sapphire Rapids  
`c3-highmem-176` | 176 | 1,408 | Intel Sapphire Rapids  
**`c3-standard` machine types**  
`c3-standard-4` | 4 | 16 | Intel Sapphire Rapids  
`c3-standard-8` | 8 | 32 | Intel Sapphire Rapids  
`c3-standard-22` | 22 | 88 | Intel Sapphire Rapids  
`c3-standard-44` | 44 | 176 | Intel Sapphire Rapids  
`c3-standard-88` | 88 | 352 | Intel Sapphire Rapids  
`c3-standard-176` | 176 | 704 | Intel Sapphire Rapids  
  
#### C3D general-purpose machine types

The C3D machine types run on an AMD CPU platform. The SAP-certified configurations of the `c3d-standard` machines have 4 GB of memory per vCPU. The SAP-certified configurations of the `c3d-highmem` machines have 8 GB of memory per vCPU.

C3D general-purpose machines | vCPUs | Memory (GB) | Minimum CPU platform  
---|---|---|---  
**`c3d-highmem` machine types**  
`c3d-highmem-4` | 4 | 32 | AMD EPYC Genoa  
`c3d-highmem-8` | 8 | 64 | AMD EPYC Genoa  
`c3d-highmem-16` | 16 | 128 | AMD EPYC Genoa  
`c3d-highmem-30` | 30 | 240 | AMD EPYC Genoa  
`c3d-highmem-60` | 60 | 480 | AMD EPYC Genoa  
`c3d-highmem-90` | 90 | 720 | AMD EPYC Genoa  
`c3d-highmem-180` | 180 | 1440 | AMD EPYC Genoa  
**`c3d-standard` machine types**  
`c3d-standard-4` | 4 | 16 | AMD EPYC Genoa  
`c3d-standard-8` | 8 | 32 | AMD EPYC Genoa  
`c3d-standard-16` | 16 | 64 | AMD EPYC Genoa  
`c3d-standard-30` | 30 | 120 | AMD EPYC Genoa  
`c3d-standard-60` | 60 | 240 | AMD EPYC Genoa  
`c3d-standard-90` | 90 | 360 | AMD EPYC Genoa  
`c3d-standard-180` | 180 | 720 | AMD EPYC Genoa  
  
#### N2 general-purpose machine types

The N2 machine types are the second generation of the general-purpose machines and run on an Intel CPU platform. The SAP-certified configurations of the `n2-standard` machines have 4 GB of memory per vCPU. The SAP-certified configurations of the `n2-highmem` machines have 8 GB of memory per vCPU.

N2 general-purpose machines | vCPUs | Memory (GB) | Minimum CPU platform  
---|---|---|---  
**`n2-highmem` machine types**  
`n2-highmem-2` | 2 | 16 | Intel Ice Lake  
Intel Cascade Lake  
`n2-highmem-4` | 4 | 32 | Intel Ice Lake  
Intel Cascade Lake  
`n2-highmem-8` | 8 | 64 | Intel Ice Lake  
Intel Cascade Lake  
`n2-highmem-16` | 16 | 128 | Intel Ice Lake  
Intel Cascade Lake  
`n2-highmem-32` | 32 | 256 | Intel Ice Lake  
Intel Cascade Lake  
`n2-highmem-48` | 48 | 384 | Intel Ice Lake  
Intel Cascade Lake  
`n2-highmem-64` | 64 | 512 | Intel Ice Lake  
Intel Cascade Lake  
`n2-highmem-80` | 80 | 640 | Intel Ice Lake  
Intel Cascade Lake  
`n2-highmem-96` | 96 | 768 | Intel Ice Lake  
`n2-highmem-128` | 128 | 838 | Intel Ice Lake  
**`n2-standard` machine types**  
`n2-standard-2` | 2 | 8 | Intel Ice Lake  
Intel Cascade Lake  
`n2-standard-4` | 4 | 16 | Intel Ice Lake  
Intel Cascade Lake  
`n2-standard-8` | 8 | 32 | Intel Ice Lake  
Intel Cascade Lake  
`n2-standard-16` | 16 | 64 | Intel Ice Lake  
Intel Cascade Lake  
`n2-standard-32` | 32 | 128 | Intel Ice Lake  
Intel Cascade Lake  
`n2-standard-48` | 48 | 192 | Intel Ice Lake  
Intel Cascade Lake  
`n2-standard-64` | 64 | 256 | Intel Ice Lake  
Intel Cascade Lake  
`n2-standard-80` | 80 | 320 | Intel Ice Lake  
Intel Cascade Lake  
`n2-standard-96` | 96 | 384 | Intel Ice Lake  
`n2-standard-128` | 128 | 512 | Intel Ice Lake  
  
#### N2D general-purpose machine types

The N2D machine types are the second generation of the general-purpose machines and run on an AMD CPU platform. The SAP-certified configurations of the `n2d-standard` machines have 4 GB of memory per vCPU. The SAP-certified configurations of the `n2d-highmem` machines have 8 GB of memory per vCPU.

N2D general-purpose machines | vCPUs | Memory (GB) | Minimum CPU platform  
---|---|---|---  
**`n2d-highmem` machine types**  
`n2d-highmem-2` | 2 | 16 | AMD EPYC Milan  
`n2d-highmem-4` | 4 | 32 | AMD EPYC Milan  
`n2d-highmem-8` | 8 | 64 | AMD EPYC Milan  
`n2d-highmem-16` | 16 | 128 | AMD EPYC Milan  
`n2d-highmem-32` | 32 | 256 | AMD EPYC Milan  
`n2d-highmem-48` | 48 | 384 | AMD EPYC Milan  
`n2d-highmem-64` | 64 | 512 | AMD EPYC Milan  
`n2d-highmem-80` | 80 | 640 | AMD EPYC Milan  
`n2d-highmem-96` | 96 | 768 | AMD EPYC Milan  
**`n2d-standard` machine types**  
`n2d-standard-2` | 2 | 8 | AMD EPYC Milan  
`n2d-standard-4` | 4 | 16 | AMD EPYC Milan  
`n2d-standard-8` | 8 | 32 | AMD EPYC Milan  
`n2d-standard-16` | 16 | 64 | AMD EPYC Milan  
`n2d-standard-32` | 32 | 128 | AMD EPYC Milan  
`n2d-standard-48` | 48 | 192 | AMD EPYC Milan  
`n2d-standard-64` | 64 | 256 | AMD EPYC Milan  
`n2d-standard-80` | 80 | 320 | AMD EPYC Milan  
`n2d-standard-96` | 96 | 384 | AMD EPYC Milan  
`n2d-standard-128` | 128 | 512 | AMD EPYC Milan  
`n2d-standard-224` | 224 | 896 | AMD EPYC Milan  
  
#### T2D general-purpose machine types

The T2D machine types run on an AMD CPU platform. The SAP-certified configurations of the `t2d-standard` machines have 4 GB of memory per vCPU.

Machine types in the T2D machine series have simultaneous multithreading (SMT) disabled; therefore a vCPU is equivalent to an entire core.

The T2D machine types are only available in specific zones. For more information, see [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

T2D general-purpose machines | vCPUs | Memory (GB) | Minimum CPU platform  
---|---|---|---  
`t2d-standard-2` | 2 | 8 | AMD EPYC Milan  
`t2d-standard-4` | 4 | 16 | AMD EPYC Milan  
`t2d-standard-8` | 8 | 32 | AMD EPYC Milan  
`t2d-standard-16` | 16 | 64 | AMD EPYC Milan  
`t2d-standard-32` | 32 | 128 | AMD EPYC Milan  
`t2d-standard-48` | 48 | 192 | AMD EPYC Milan  
`t2d-standard-60` | 60 | 240 | AMD EPYC Milan  
  
#### N1 general-purpose machine types

The N1 machine types are the first generation of the general-purpose machine types. The SAP-certified configurations of the `n1-standard` machines have 3.75 GB of memory per vCPU. The SAP-certified configurations of the `n1-highmem` machines have 6.5 GB of memory per vCPU.

N1 general-purpose machines | vCPUs | Memory (GB) | Minimum CPU platform  
---|---|---|---  
**`n1-highmem` machine types**  
`n1-highmem-2` | 2 | 13 | Intel Skylake  
Intel Broadwell  
`n1-highmem-4` | 4 | 26 | Intel Skylake  
Intel Broadwell  
`n1-highmem-8` | 8 | 52 | Intel Skylake  
Intel Broadwell  
`n1-highmem-16` | 16 | 104 | Intel Skylake  
Intel Broadwell  
`n1-highmem-32` | 32 | 208 | Intel Skylake  
Intel Broadwell  
`n1-highmem-64` | 64 | 416 | Intel Skylake  
Intel Broadwell  
`n1-highmem-96` | 96 | 624 | Intel Skylake  
**`n1-standard` machine types**  
`n1-standard-8` | 8 | 30 | Intel Skylake  
Intel Broadwell  
`n1-standard-16` | 16 | 60 | Intel Skylake  
Intel Broadwell  
`n1-standard-32` | 32 | 120 | Intel Skylake  
Intel Broadwell  
`n1-standard-64` | 64 | 240 | Intel Skylake  
Intel Broadwell  
`n1-standard-96` | 96 | 360 | Intel Skylake  
  
### Memory-optimized machine types

The memory-optimized machine types that are certified for SAP applications are optimized for memory-intensive workloads, such as SAP HANA, in-memory analytics, and SQL analysis services.

### X5 memory-optimized bare metal machine types

X5 is a series of memory-optimized machine types offered by Compute Engine. These machine types primarily support SAP workloads that require up to 48 TB of memory.

**Note** : The `x5-2064-48T-metal` machine type is available for use with SAP workloads that SAP manages under the RISE with SAP program. 

The following restrictions apply:

  * Only Hyperdisk can be attached to an X5 instance. This applies to the boot volume as well.
  * The X5 machine series is available in only [select zones and regions](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * X5 instances aren't supported with all operating system images. For information about which operating system versions you can use with X5 instances, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).
  * The X5 machine series is only available as predefined machine types. Custom machine shapes are not available.



The following table lists the X5 machine types that you can use to run SAP workloads:

X5 memory-optimized bare metal machine type | vCPUs | Memory | CPU platform  
---|---|---|---  
`x5-688-12T-metal` | 688 | 12,288 GB | Intel Granite Rapids  
`x5-688-16T-metal` | 688 | 16,384 GB | Intel Granite Rapids  
`x5-1376-24T-metal` | 1,376 | 24,576 GB | Intel Granite Rapids  
`x5-1376-32T-metal` | 1,376 | 32,768 GB | Intel Granite Rapids  
`x5-2064-48T-metal` Note | 2,064 | 49,152 GB | Intel Granite Rapids  
  
#### X4 memory-optimized bare metal machine types

X4 is a series of memory-optimized machine types offered by Compute Engine. They are designed to primarily support SAP workloads that require up to 32 TB of memory.

The following restrictions apply:

  * Only Hyperdisk can be attached to an X4 instance. This applies to the boot volume as well.
  * The X4 machine series is available in only [select zones and regions](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * X4 instances aren't supported with all operating system images. For information about which operating system versions you can use with X4 instances, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).
  * The X4 machine series is only available as predefined machine types. Custom machine shapes are not available.



For more information about the X4 machine series, see [X4 machine series](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x4_series).

The following table lists the X4 machine types that you can use to run SAP workloads:

**Note** : From December 12, 2025, the naming convention for X4 machine types has changed to clarify the memory they offer. For example, `x4-megamem-960-metal` has changed to `x4-960-16t-metal` because it offers 16 TB of memory. While this naming change is backwards compatible, we recommend that you use the updated names for new deployments.

X4 memory-optimized bare metal machine type | vCPUs | Memory | CPU platform  
---|---|---|---  
`x4-960-16t-metal` | 960 | 16,384 GB | Intel Sapphire Rapids  
`x4-1440-24t-metal` | 1,440 | 24,576 GB | Intel Sapphire Rapids  
`x4-1920-32t-metal` | 1,920 | 32,768 GB | Intel Sapphire Rapids  
  
#### M4N memory-optimized machine types

The M4N series of Compute Engine VMs are the fourth generation of memory-optimized machine types.

The SAP-certified configurations of the `m4n-megamem` machines have 13.29 GB of memory per vCPU. he SAP-certified configurations of the `m4-hypermem` machines have 15.5 GB of memory per vCPU. The SAP-certified configurations of the `m4-ultramem` machines have 26.57 GB of memory per vCPU.

The following restrictions apply:

  * Memory-optimized machine types are only available as predefined machine types.
  * You cannot use [regional persistent disks](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) with memory-optimized machine types.
  * Memory-optimized machine types are only available in specific zones. For more information, see [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * M4N machine series is not available with all operating system images. For information about which operating system versions can be used with M4N machine types, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).
  * M4N machine series does not support Persistent Disk.



For more information about M4N machine types, see [M4N machine types](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m4n_machine_types).

The following table shows the M4N machine types that are certified by SAP for use with SAP NetWeaver on Google Cloud:

M4N memory-optimized machines | vCPUs | Memory (GiB) | CPU platform  
---|---|---|---  
`m4n-hypermem-16` | 16 | 248 | Intel Emerald Rapids  
`m4n-hypermem-32` | 32 | 496 | Intel Emerald Rapids  
`m4n-hypermem-64` | 64 | 992 | Intel Emerald Rapids  
`m4n-megamem-28` | 28 | 372 | Intel Emerald Rapids  
`m4n-megamem-56` | 56 | 744 | Intel Emerald Rapids  
`m4n-megamem-112` | 112 | 1,488 | Intel Emerald Rapids  
`m4n-megamem-224` | 224 | 2,976 | Intel Emerald Rapids  
`m4n-ultramem-56` | 56 | 1,488 | Intel Emerald Rapids  
`m4n-ultramem-112` | 112 | 2,976 | Intel Emerald Rapids  
`m4n-ultramem-224` | 224 | 5,952 | Intel Emerald Rapids  
  
#### M4 memory-optimized machine types

The M4 series of Compute Engine VMs are the fourth generation of memory-optimized machine types.

The SAP-certified configurations of the `m4-megamem` machines have 13.29 GB of memory per vCPU. The SAP-certified configurations of the `m4-ultramem` machines have 26.57 GB of memory per vCPU. The SAP-certified configurations of the `m4-hypermem` machines have 15.5 GB of memory per vCPU.

The following restrictions apply:

  * Memory-optimized machine types are only available as predefined machine types.
  * You cannot use [regional persistent disks](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) with memory-optimized machine types.
  * Memory-optimized machine types are only available in specific zones. For more information, see [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * M4 machine series is not available with all operating system images. For information about which operating system versions can be used with M4 machine types, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).
  * M4 machine series does not support Persistent Disk.



For more information about M4 machine types, see [M4 machine types](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m4_machine_types).

The following table shows the M4 machine types that are certified by SAP for use with SAP NetWeaver on Google Cloud:

M4 memory-optimized machines | vCPUs | Memory (GiB) | CPU platform  
---|---|---|---  
`m4-megamem-28` | 28 | 372 | Intel Emerald Rapids  
`m4-megamem-56` | 56 | 744 | Intel Emerald Rapids  
`m4-megamem-112` | 112 | 1,488 | Intel Emerald Rapids  
`m4-megamem-224` | 224 | 2,976 | Intel Emerald Rapids  
`m4-ultramem-56` | 56 | 1,488 | Intel Emerald Rapids  
`m4-ultramem-112` | 112 | 2,976 | Intel Emerald Rapids  
`m4-ultramem-224` | 224 | 5,952 | Intel Emerald Rapids  
`m4-hypermem-16` | 16 | 248 | Intel Emerald Rapids  
`m4-hypermem-32` | 32 | 496 | Intel Emerald Rapids  
`m4-hypermem-64` | 64 | 992 | Intel Emerald Rapids  
  
#### M3 memory-optimized machine types

The M3 series of Compute Engine VMs are the third generation of memory-optimized machine types.

The `m3-ultramem` machine type has 30 GB of memory per vCPU. The `m3-megamem` machine type has 15 GB of memory per vCPU.

The following restrictions apply:

  * Memory-optimized machine types are only available as predefined machine types.
  * You cannot use [regional persistent disks](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) with memory-optimized machine types.
  * Memory-optimized machine types are only available in specific zones. For more information, see [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * M3 machine series is not available with all operating system images. For information about which operating system versions can be used with M3 machine types, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).
  * M3 machine series does not support standard persistent disks (pd-standard).



For more information, see [M3 machine types](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m3_machine_types).

M3 memory-optimized machines | vCPUs | Memory (GiB) | CPU platform  
---|---|---|---  
`m3-ultramem-32` | 32 | 976 | Intel Ice Lake  
`m3-ultramem-64` | 64 | 1,952 | Intel Ice Lake  
`m3-ultramem-128` | 128 | 3,904 | Intel Ice Lake  
`m3-megamem-64` | 64 | 976 | Intel Ice Lake  
`m3-megamem-128` | 128 | 1,952 | Intel Ice Lake  
  
#### M2 memory-optimized machine types

The M2 series of Compute Engine VMs are the second generation of memory-optimized machine types.

The `m2-ultramem` machine type has 28 GB of memory per vCPU. The `m2-megamem` machine type has 14 GB of memory per vCPU. The `m2-hypermem` machine type has 21 GB of memory per vCPU.

The following restrictions apply:

  * Memory-optimized machine types are only available as predefined machine types.
  * You cannot use [regional persistent disks](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) with memory-optimized machine types.
  * Memory-optimized machine types are only available in specific zones. For more information, see [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * M2 series of machine types are available only on the Intel Cascade Lake platform.



For more information, see [M2 machine types](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m2_machine_types).

M2 memory-optimized machines | vCPUs | Memory (GiB) | CPU platform  
---|---|---|---  
`m2-ultramem-208` | 208 | 5,888 | Intel Cascade Lake  
`m2-ultramem-416` | 416 | 11,776 | Intel Cascade Lake  
`m2-megamem-416` | 416 | 5,888 | Intel Cascade Lake  
`m2-hypermem-416` | 416 | 8,832 | Intel Cascade Lake  
  
#### M1 memory-optimized machine types

The M1 series of VMs are the first generation of Compute Engine memory optimized machine types.

The `m1-ultramem` machine type has 24 GB of memory per vCPU. The `m1-megamem` machine type has approximately 15 GB of memory per vCPU.

The following restrictions apply:

  * Memory-optimized machine types are only available as predefined machine types.
  * You cannot use [regional persistent disks](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) with memory-optimized machine types.
  * Memory-optimized machine types are only available in specific zones. For more information, see [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * M1-ultramem machine types are available only on the Broadwell E7 platform. The m1-megamem machine type is available only on the Skylake platform.



For more information, see [M1 machine types](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m1_machine_types).

M1 memory-optimized machines | vCPUs | Memory (GiB) | CPU platform  
---|---|---|---  
`m1-megamem-96` | 96 | 1433 | Intel Skylake  
`m1-ultramem-40` | 40 | 961 | Intel Broadwell  
`m1-ultramem-80` | 80 | 1922 | Intel Broadwell  
`m1-ultramem-160` | 160 | 3,844 | Intel Broadwell  
  
### Bare Metal Solution servers

The Google Cloud Bare Metal Solution servers that are certified for SAP applications are bare-metal servers that are designed for specialized workloads, including extra-large, high-performance SAP HANA workloads and other workloads that need to run on a non-virtualized machine.

The following restrictions apply:

  * Bare Metal Solution servers are only available as predefined servers.
  * For most changes to Bare Metal Solution servers or their environment, you need to open a change request.
  * Bare Metal Solution servers are not available in all regions. For more information, see Regional availability.



#### SAP-certified Bare Metal Solution servers

The following table lists the Bare Metal Solution servers that you can use to run SAP NetWeaver based applications:

Bare Metal Solution server | CPU cores | vCPUs | Sockets | Memory | CPU platform  
---|---|---|---|---|---  
**General-purpose server**  
`o2-standard-16-metal` | 8 | 16 | 2 | 192 GB | Intel Cascade Lake  
`o2-standard-32-metal` | 16 | 32 | 2 | 384 GB | Intel Cascade Lake  
`o2-standard-48-metal` | 24 | 48 | 2 | 768 GB | Intel Cascade Lake  
`o2-standard-112-metal` | 56 | 112 | 2 | 1.5 TB | Intel Cascade Lake  
**High-memory general-purpose server**  
`o2-highmem-224-metal` | 112 | 224 | 4 | 3 TB | Intel Cascade Lake  
  
#### Regional availability of SAP-certified Bare Metal Solution servers

The Bare Metal Solution servers that are certified for SAP applications are available only in Bare Metal Solution region extensions, which are not available for every Google Cloud region. For the full list of regions that have a Bare Metal Solution region extension, see [Bare Metal Solution regional availability](https://docs.cloud.google.com/bare-metal/docs/bms-planning#regional_availability).

### Custom machine types

Custom machine types let you tailor the size of your Compute Engine VM to your workload.

When you configure a custom VM instance, to ensure support from SAP, you must conform to memory-to-vCPU ratios that are based on the machine type that you are customizing and SAP guidelines.

You can customize only certain types of Compute Engine machines. Each machine type has different rules for customizations. The following table summarizes the rules for each custom machine type that SAP supports.

Machine type | vCPUs | Standard-memory option | High-memory option  
---|---|---|---  
**N1** | 1, or any even number up to 96 | 3.75 GB or more per vCPU | 6.5 GB or more per vCPU  
**N2** | Any even number up to 32. After 32, the number of vCPUs must be divisible by 4, up to 80 vCPUs. For example, 32, 36, and 40 vCPUs are all valid, but 38 is invalid. | 4.0 GB or more per vCPU | 8.0 GB or more per vCPU  
**N2D** | Must conform to Compute Engine [N2D custom machine type rules](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#n2d_custom_machine_types) up to a limit of 96 vCPUs. | 4.0 GB or more per vCPU | 8.0 GB or more per vCPU  
  
Custom machine types need to be evaluated by SAP before SAP supports them. Because the capacity (SAPS) of a custom machine configuration is not predetermined, SAP cannot guarantee that a configured custom machine would be suitable to run Business Suite workloads without first reviewing the configuration.

Open an SAP support ticket against SAP component `BC-OP-LNX-GOOGLE` or `BC-OP-NT-GOOGLE` to indicate your interest in a custom VM for an SAP deployment. The SAP or Google platform team reviews your configuration to confirm that it meets the SAP supportability requirements.

For more information, see:

  * [ SAP Note 2456432 - SAP Applications on Google Cloud: Supported Products and Google Cloud machine types](https://launchpad.support.sap.com/#/notes/2456432)
  * [Creating a custom VM instance](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type)



## Persistent disk storage for SAP applications

For persistent block storage, you can attach Persistent Disk and Hyperdisk volumes to your Compute Engine VMs.

Compute Engine offers different types of Persistent Disk and Hyperdisk. Each type has different performance characteristics. Google Cloud manages the underlying hardware of these disks to ensure data redundancy, and to optimize performance.

With SAP NetWeaver, you can use any of the following Persistent Disk or Hyperdisk types:

  * **Persistent Disk types** : Standard (`pd-standard`), Balanced (`pd-balanced`), Performance or SSD (`pd-ssd`), and Extreme (`pd-extreme`) 
    * Standard Persistent Disk is backed by standard hard-disk drives (HDD). Disks of this type are efficient and economical for handling sequential read-write operations, but are not optimized to handle high rates of random input-output operations per second (IOPS).
    * Balanced, Performance or SSD (`pd-ssd`), and Extreme Persistent Disk types are backed by solid-state drives (SSD). These disk types provide cost-effective and reliable block storage.
    * Performance (SSD) Persistent Disk provides higher performance than Balanced Persistent Disk.
    * Balanced and Performance (SSD) Persistent Disk support PD Async Replication. You can use this feature for cross-region active-passive disaster recovery. For more information, see [PD Async Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about).
    * While you can use Extreme Persistent Disk (`pd-extreme`) with your SAP applications, we recommend that you instead use Hyperdisk volumes, which provide greater performance. For information about the machine types that support using Extreme Persistent Disk, see [Machine shape support](https://docs.cloud.google.com/compute/docs/disks/extreme-persistent-disk#machine_shape_support).
  * **Hyperdisk types** : Hyperdisk Balanced (`hyperdisk-balanced`) and Hyperdisk Extreme (`hyperdisk-extreme`) 
    * Hyperdisk Extreme provides higher maximum IOPS and throughput options than Persistent Disk types.
    * For Hyperdisk Extreme, you select the performance you need by provisioning IOPS, which also determines your throughput. For more information, see [Size and performance limits for Hyperdisk Extreme](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme#size_limits).
    * For Hyperdisk Balanced, you select the performance you need by provisioning IOPS and throughput. For more information, see [Size and performance limits for Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#size_limits).
    * For information about the machine types that support using Hyperdisk, see [Machine type support](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support).

For more information about persistent disk architecture and performance for SAP NetWeaver, see [Persistent disks](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#persistent_disks). 

For more information about the different types of block storage offered by Compute Engine, their performance characteristics, and how to work with them, see the Compute Engine documentation:

  * [Storage options](https://docs.cloud.google.com/compute/docs/disks)
  * [About Google Cloud Hyperdisk performance](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-performance)
  * [Persistent Disk performance](https://docs.cloud.google.com/compute/docs/disks/performance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
