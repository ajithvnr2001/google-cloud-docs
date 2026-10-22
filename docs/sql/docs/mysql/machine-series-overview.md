---
url: https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview/
title: Choose a machine series \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:38:18.547044+00:00
---

# Choose a machine series  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Choose a machine series Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/machine-series-overview "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview "View this page for the SQL Server database engine")

When you create a new instance, you need to choose a machine series. The machine series you choose affects the [edition](https://docs.cloud.google.com/sql/docs/mysql/choose-edition), [storage option](https://docs.cloud.google.com/sql/docs/mysql/storage-options-overview), and [location](https://docs.cloud.google.com/sql/docs/mysql/region-availability-overview) available for your to choose from for your instance. For more information on the requirements and decisions you need to make prior to creating a new instance, see [Plan and prepare overview](https://docs.cloud.google.com/sql/docs/mysql/plan-prepare-overview).

Cloud SQL provides machine series options for your instance, based on its Cloud SQL edition. A machine series is a curated set of processor and hardware configurations optimized for specific Cloud SQL workloads. These machine series let you tailor vCPU and memory for your instance and optimize performance for various demands. The machine series you select also determines the [storage option](https://docs.cloud.google.com/sql/docs/mysql/storage-options-overview) available for your Cloud SQL instance.

Each machine series provides multiple machine types. When you create an instance, you select a machine type from the machine series you want to use, which defines the resource and storage option available for your instance. For example, if you select the `db-perf-optimized-N-2` machine type, which belongs to the `N2` machine series, the storage option available for your instance is `SSD`.

## Machine series supported by Cloud SQL

The following table provides an overview of the machine series options that Cloud SQL supports, based on your instance's Cloud SQL edition and the storage options available for each machine series:

Cloud SQL edition | Machine series | Storage option  
---|---|---  
[Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#enterprise-plus) | [C4A](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#c4a)  
[C4](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#c4) | [Hyperdisk Balanced](https://docs.cloud.google.com/sql/docs/mysql/storage-options-overview#hyperdisk)  
[Hyperdisk Balanced](https://docs.cloud.google.com/sql/docs/mysql/storage-options-overview#hyperdisk)  
[N2](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#n2) | [SSD](https://docs.cloud.google.com/sql/docs/mysql/storage-options-overview#ssd)  
[Cloud SQL Enterprise edition](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#enterprise) | [N4 machine series](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#n4)  
[Shared or dedicated core](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#enterprise) | [Hyperdisk Balanced](https://docs.cloud.google.com/sql/docs/mysql/storage-options-overview#hyperdisk)  
[SSD](https://docs.cloud.google.com/sql/docs/mysql/storage-options-overview#ssd)  
[HDD](https://docs.cloud.google.com/sql/docs/mysql/storage-options-overview#hdd)  
  
To see machine series availability by region, see [Region availability](https://docs.cloud.google.com/sql/docs/mysql/region-availability-overview).

## Machine series availability for Cloud SQL Enterprise Plus edition instances

For Cloud SQL Enterprise Plus edition instances, you can select one of the following machine series:

  * **N2**: This x86-based machine series provides a balanced price-to-performance ratio for a variety of Cloud SQL workloads.
  * **C4A**: This ARM-based machine series provides optimized price-performance and delivers predictable high performance for high demand Cloud SQL workloads.
  * **C4**: This x86-based machine series provides optimized price-performance and delivers predictable high performance for high demand Cloud SQL workloads.



For Cloud SQL Enterprise Plus edition instances, each machine series provides predefined machine types with preset memory and vCPUs for your instances. Availability depends on your instance's Cloud SQL edition, region, and database version.

### [N2 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_series)

The N2 machine series provides a balanced price-performance for a wide variety of database workloads, with a memory-to-compute ratio of 1 vCPU:8 GB RAM. It uses the Performance Persistent Disk (PD-SSD) storage option. For more information about storage types, see [Choose a storage option](https://docs.cloud.google.com/sql/docs/mysql/storage-options-overview).

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
  
### [C4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series)

The C4A machine series provides high performance for a variety of performance-sensitive database workloads. The series is ARM-based, powered by Google Axion processor built on the Arm Neoverse V2 compute core.

It uses the Hyperdisk Balanced storage option, which is a Google Cloud Hyperdisk offering. Google Cloud Hyperdisk is the latest generation of network block storage service in Google Cloud. For more information about storage types, see [Choose a storage option](https://docs.cloud.google.com/sql/docs/mysql/storage-options-overview).

The C4A machine series provides predefined machine types that depend on your instance's region and configuration. Your Cloud SQL for MySQL Enterprise Plus edition instance must be MySQL version 8.0.31 or later to select a C4A machine series. 

For more information about supported regions, see [Regional availability](https://docs.cloud.google.com/sql/docs/mysql/region-availability-overview).

#### C4A machine types

The following table shows predefined machine types that are available for the C4A machine series with optional Data Cache:

Machine type | vCPUs | Memory (GB) | Optional Data Cache (GB)  
---|---|---|---  
`db-c4a-highmem-2` | 2 | 16 | Not available  
`db-c4a-highmem-4` | 4 | 32 | 375  
`db-c4a-highmem-8` | 8 | 64 | 750  
`db-c4a-highmem-16` | 16 | 128 | 1,500  
`db-c4a-highmem-32` | 32 | 256 | 2,250  
`db-c4a-highmem-48` | 48 | 384 | 3,750  
`db-c4a-highmem-64` | 64 | 512 | 5,250  
`db-c4a-highmem-72` | 72 | 576 | 6,000  
  
### [C4 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series)

The C4 machine series provide consistent, predictable high performance. It uses the Hyperdisk Balanced storage option, which is a Google Cloud Hyperdisk offering. Google Cloud Hyperdisk is the latest generation of network block storage service in Google Cloud. For more information about storage types, see [Choose a storage option](https://docs.cloud.google.com/sql/docs/mysql/storage-options-overview).

The C4 machine series provides predefined machine types that depend on your instance's region and configuration. For more information about supported regions, see [Regional availability](https://docs.cloud.google.com/sql/docs/mysql/region-availability-overview).

#### C4 machine types

The following table shows predefined machine types that are available for the C4 machine series.

Machine type | vCPUs | Memory (GB) | Optional Data Cache (GB)  
---|---|---|---  
`db-perf-optimized-C4-2` | 2 | 15 | Not available  
`db-perf-optimized-C4-4` | 4 | 31 | 375  
`db-perf-optimized-C4-8` | 8 | 62 | 375  
  
## Machine series availability for Cloud SQL Enterprise edition instances

For Cloud SQL Enterprise edition instances, you can select one of the following machine series:

  * **N4**: this machine series provides balanced price-to-performance using Intel Emerald Rapids processors.


  * **General purpose shared core**: this machine series is a x86 based machine series.


  * **General purpose dedicated core**: this machine series provides balanced price-to-performance using x86 based machines.



### [N4 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4_series)

The N4 machine series provides balanced price-to-performance for your Cloud SQL Enterprise edition instances, with a memory-to-compute ratio of 1 vCPU:8 GB RAM. It uses the Hyperdisk Balanced storage option. For more information about storage types, see [Choose a storage option](https://docs.cloud.google.com/sql/docs/mysql/storage-options-overview).

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
  
### General purpose shared core

The general purpose shared core machine series provides machine types with predefined CPUs (cores) and memory for your instances. It uses the SSD or HDD storage option. For more information about storage types, see [Choose a storage option](https://docs.cloud.google.com/sql/docs/mysql/storage-options-overview).

The following machine types are available for instances for the general purpose shared core machine series:

Machine type | vCPUs | Memory (GB)  
---|---|---  
`db-f1-micro` | 1 | 0.614  
`db-g1-small` | 1 | 1.7  
  
### General purpose dedicated core

The General purpose dedicated core machine series provides custom instance configurations that let you select the memory and CPUs your instance needs. This flexibility lets you select the appropriate VM shape for your workload. It uses the SSD or HDD storage option. For more information about storage types, see [Choose a storage option](https://docs.cloud.google.com/sql/docs/mysql/storage-options-overview).

Custom machine type names use the following format: `db-custom-{CPUs}-{Memory}`. When you select the number of CPUs and memory, some restrictions apply to the configurations you can select.

#### General purpose dedicated core and custom machine types

You can set custom configurations for the general purpose dedicated core machine series as follows:

  * vCPUs must be either 1 or an even number between 2 and 96.
  * Memory must be: 
    * 0.9 to 6.5 GB per vCPU
    * A multiple of 256 MB
    * At least 3.75 GB (3840 MB)



## Pricing

The machine series you select affects the cost of your instance. For more information, see [Instance pricing](https://cloud.google.com/sql/pricing#2nd-gen-instance-pricing). You can also use the [pricing calculator](https://cloud.google.com/products/calculator) to see pricing for various scenarios.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
