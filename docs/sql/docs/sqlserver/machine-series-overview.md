---
url: https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview/
title: Choose a machine series \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:37.670562+00:00
---

# Choose a machine series  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Choose a machine series Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/machine-series-overview "View this page for the PostgreSQL database engine") | SQL Server

When you create a new instance, you need to choose a machine series. The machine series you choose affects the [edition](https://docs.cloud.google.com/sql/docs/sqlserver/choose-edition), [storage option](https://docs.cloud.google.com/sql/docs/sqlserver/storage-options-overview), and [location](https://docs.cloud.google.com/sql/docs/sqlserver/region-availability-overview) available for your to choose from for your instance. For more information on the requirements and decisions you need to make prior to creating a new instance, see [Plan and prepare overview](https://docs.cloud.google.com/sql/docs/sqlserver/plan-prepare-overview).

Cloud SQL provides machine series options for your instance, based on its Cloud SQL edition. A machine series is a curated set of processor and hardware configurations optimized for specific Cloud SQL workloads. These machine series let you tailor vCPU and memory for your instance and optimize performance for various demands. The machine series you select also determines the [storage option](https://docs.cloud.google.com/sql/docs/sqlserver/storage-options-overview) available for your Cloud SQL instance.

Each machine series provides multiple machine types. When you create an instance, you select a machine type from the machine series you want to use, which defines the resource and storage option available for your instance. For example, if you select the `db-perf-optimized-N-2` machine type, which belongs to the `N2` machine series, the storage option available for your instance is `SSD`.

## Machine series supported by Cloud SQL

The following table provides an overview of the machine series options that Cloud SQL supports, based on your instance's Cloud SQL edition and the storage options available for each machine series:

Cloud SQL edition | Machine series | Storage option  
---|---|---  
[Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview#enterprise-plus) | [C4](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview#c4) | [Hyperdisk Balanced](https://docs.cloud.google.com/sql/docs/sqlserver/storage-options-overview#hyperdisk)  
[N2](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview#n2) | [SSD](https://docs.cloud.google.com/sql/docs/sqlserver/storage-options-overview#ssd)  
[Memory-optimized-N2](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview#memory-optimized-N2) | [SSD](https://docs.cloud.google.com/sql/docs/sqlserver/storage-options-overview#ssd)  
[Cloud SQL Enterprise edition](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview#enterprise) | [N4 machine series](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview#n4)  
[Dedicated core](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview#enterprise) | [Hyperdisk Balanced](https://docs.cloud.google.com/sql/docs/sqlserver/storage-options-overview#hyperdisk)  
[SSD](https://docs.cloud.google.com/sql/docs/sqlserver/storage-options-overview#ssd)  
  
  
To see machine series availability by region, see [Region availability](https://docs.cloud.google.com/sql/docs/sqlserver/region-availability-overview).

## Machine series availability for Cloud SQL Enterprise Plus edition instances

For Cloud SQL Enterprise Plus edition instances, you can select one of the following machine series:

  * **N2**: This x86-based machine series provides a balanced price-to-performance ratio for a variety of Cloud SQL workloads.
  * **Memory-optimized-N2**: This machine series provides high memory-to-compute ratios for memory-intensive Cloud SQL workloads.
  * **C4**: This x86-based machine series provides optimized price-performance and delivers predictable high performance for high demand Cloud SQL workloads.



For Cloud SQL Enterprise Plus edition instances, each machine series provides predefined machine types with preset memory and vCPUs for your instances. Availability depends on your instance's Cloud SQL edition, region, and database version.

### [N2 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_series)

The N2 machine series provides a balanced price-performance for a wide variety of database workloads, with a memory-to-compute ratio of 1 vCPU:8 GB RAM. It uses the Performance Persistent Disk (PD-SSD) storage option. For more information about storage types, see [Choose a storage option](https://docs.cloud.google.com/sql/docs/sqlserver/storage-options-overview).

#### N2 machine types

The following machine types are available for instances for the N2 machine series:

Machine type | vCPUs | Memory (GB) | Optional Data Cache (GB)  
---|---|---|---  
`db-perf-optimized-N-2` | 2 | 16 | 375  
`db-perf-optimized-N-4` | 4 | 32 | 375  
`db-perf-optimized-N-8` | 8 | 64 | 375  
`db-perf-optimized-N-16` | 16 | 128 | 750  
`db-perf-optimized-N-32` | 32 | 256 | 1,500  
`db-perf-optimized-N-48` | 48 | 384 | 3,000  
`db-perf-optimized-N-64` | 64 | 512 | 6,000  
`db-perf-optimized-N-80` | 80 | 640 | 6,000  
`db-perf-optimized-N-96` | 96 | 768 | 6,000  
`db-perf-optimized-N-128` | 128 | 864 | 6,000  
  
### Memory-optimized-N2

The `memory-optimized-N2` machine series provides high memory-to-compute ratios for memory-intensive workloads.

The `memory-optimized-N2` machine series uses the Performance Persistent Disk (PD-SSD) storage option. PD-SSD is a Persistent Disk volumes offering that provides Cloud SQL instances with lower latency and increased IOPS. It is backed by solid-state drives (SSD). For more information, see [About Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks).

#### Memory-optimized-N2 machine types

The following machine types are available for instances for the `memory-optimized-N2` machine series:

Machine type | vCPUs | Memory (GB) | Optional Data Cache (GB)  
---|---|---|---  
`db-memory-optimized-N-4` | 4 | 128 | 750  
`db-memory-optimized-N-8` | 8 | 256 | 1,500  
`db-memory-optimized-N-16` | 16 | 512 | 3,000  
  
### [C4 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series)

The C4 machine series provide consistent, predictable high performance. It uses the Hyperdisk Balanced storage option, which is a Google Cloud Hyperdisk offering. Google Cloud Hyperdisk is the latest generation of network block storage service in Google Cloud. For more information about storage types, see [Choose a storage option](https://docs.cloud.google.com/sql/docs/sqlserver/storage-options-overview).

The C4 machine series provides predefined machine types that depend on your instance's region and configuration. For more information about supported regions, see [Regional availability](https://docs.cloud.google.com/sql/docs/sqlserver/region-availability-overview).

#### C4 machine types

The following table shows predefined machine types that are available for the C4 machine series.

Machine type | vCPUs | Memory (GB)  
---|---|---  
`db-perf-optimized-C4-2` | 2 | 15  
`db-perf-optimized-C4-4` | 4 | 31  
`db-perf-optimized-C4-8` | 8 | 62  
  
## Machine series availability for Cloud SQL Enterprise edition instances

For Cloud SQL Enterprise edition instances, you can select one of the following machine series:

  * **N4**: this machine series provides balanced price-to-performance using Intel Emerald Rapids processors.


  * **General purpose dedicated core**: this machine series provides balanced price-to-performance using x86 based machines.



### [N4 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4_series)

The N4 machine series provides balanced price-to-performance for your Cloud SQL Enterprise edition instances, with a memory-to-compute ratio of 1 vCPU:8 GB RAM. It uses the Hyperdisk Balanced storage option. For more information about storage types, see [Choose a storage option](https://docs.cloud.google.com/sql/docs/sqlserver/storage-options-overview).

#### N4 machine types

The N4 machine series provides custom machine series options. These machine type names use the following format: `db-custom-N4-{CPUs}-{Memory}`.

You can set custom configurations for the N4 machine series based on the following requirements:

  * vCPUs can range from 2 to 80, in increments of 2.
  * Memory can range from 2 GB to 640 GB and must have: 
    * Minimum memory of 2 GB per vCPU
    * Maximum memory of 8 GB per vCPU



The following table shows examples of N4 custom machine types:

Machine type | vCPUs | Minimum memory (GB) | Maximum memory (GB)  
---|---|---|---  
`db-custom-N4-2-*` | 2 | 4 | 16  
`db-custom-N4-4-*` | 4 | 8 | 32  
`db-custom-N4-6-*` | 6 | 12 | 48  
`db-custom-N4-8-*` | 8 | 16 | 64  
  
### General purpose dedicated core

The General purpose dedicated core machine series provides custom instance configurations that let you select the memory and CPUs your instance needs. This flexibility lets you select the appropriate VM shape for your workload. It uses the SSD storage option. For more information about storage types, see [Choose a storage option](https://docs.cloud.google.com/sql/docs/sqlserver/storage-options-overview).

Custom machine type names use the following format: `db-custom-{CPUs}-{Memory}`. When you select the number of CPUs and memory, some restrictions apply to the configurations you can select.

#### General purpose dedicated core and custom machine types

Custom configurations available for the general purpose dedicated core machine series depend on the Cloud SQL for SQL Server edition your instance is using:

Cloud SQL for SQL Server edition | vCPUs | Memory (GB)  
---|---|---  
2017 Express   
2019 Express   
2022 Express   
2025 Express | 1 to 8 | 3.75 to 32  
2017 Web   
2019 Web   
2022 Web | 1 to 32 | 3.75 to 32  
2017 Standard   
2019 Standard   
2022 Standard   
2025 Standard | 1 to 48 | 3.75 to 32  
2017 Enterprise   
2019 Enterprise   
2022 Enterprise   
2025 Enterprise | 2 to 96 | 8 to 32  
  
## Pricing

The machine series you select affects the cost of your instance. For more information, see [Instance pricing](https://cloud.google.com/sql/pricing#2nd-gen-instance-pricing). You can also use the [pricing calculator](https://cloud.google.com/products/calculator) to see pricing for various scenarios.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
