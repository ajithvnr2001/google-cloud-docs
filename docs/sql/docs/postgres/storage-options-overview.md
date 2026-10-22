---
url: https://docs.cloud.google.com/sql/docs/postgres/storage-options-overview/
title: Choose a storage option \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:32:19.019543+00:00
---

# Choose a storage option  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/storage-options-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Choose a storage option Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/storage-options-overview "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/storage-options-overview "View this page for the SQL Server database engine")

Cloud SQL storage options let you match your instance's IOPS, throughput, and cost to your database workload. You can configure Hyperdisk Balanced for customizable performance, solid-state drives (SSD) for low-latency active data, or hard-disk drives (HDD) for archival and batch workloads. Because storage availability depends on your instance's machine type, see the [Machine series overview](https://docs.cloud.google.com/sql/docs/postgres/machine-series-overview#availability) to confirm which options your configuration supports.

## Google Cloud Hyperdisk Balanced

Cloud SQL uses the Hyperdisk Balanced storage option for the [N4](https://docs.cloud.google.com/sql/docs/postgres/machine-series-overview#n4), [C4A](https://docs.cloud.google.com/sql/docs/postgres/machine-series-overview#c4a), and [C4](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#c4) machine series. This storage type is an Google Cloud Hyperdisk offering. Hyperdisk is the latest generation of network block storage. It offers scalable, high-performance storage with comprehensive data persistence and management capabilities. You can also enable [automatic storage increase](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#automatic-storage-increase-2ndgen) with this storage option to have Cloud SQL automatically increase the storage for your instance when it falls below the threshold size.

Hyperdisk Balanced provides customizable throughput and IOPS. For more information, see [About Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced).

Hyperdisk Balanced sets default IOPS and throughput values and limits based on your instance's configuration, which include the machine type and storage capacity. Storage capacity limits the default value, and the machine type sets the maximum value for both IOPS and throughput. You can modify these values for your instance.

### C4A machine series IOPS and throughput limits

The following table shows the minimum and maximum limits for IOPS and throughput (in MiB/s) for each machine type in the [C4A machine series](https://docs.cloud.google.com/sql/docs/postgres/machine-series-overview) based on its vCPUs:

|  |  | Hyperdisk Balanced | Hyperdisk Balanced HA  
---|---|---|---|---  
vCPUs | Minimum IOPS | Minimum throughput | Maximum IOPs | Maximum throughput | Maximum IOPs | Maximum throughput  
2 | 3,000 | 140 | 50,000 | 800 | 50,000 | 800  
4 | 3,000 | 140 | 50,000 | 800 | 50,000 | 800  
8 | 3,000 | 140 | 50,000 | 1,000 | 50,000 | 1,000  
16 | 3,000 | 140 | 80,000 | 2,400 | 80,000 | 1,200  
32 | 3,000 | 140 | 120,000 | 2,400 | 100,000 | 1,200  
48 | 3,000 | 140 | 160,000 | 2,400 | 100,000 | 1,200  
64 | 3,000 | 140 | 160,000 | 2,400 | 100,000 | 1,200  
72 | 3,000 | 140 | 160,000 | 2,400 | 100,000 | 1,200  
  
The following table shows the default Google Cloud Hyperdisk Balanced IOPS and throughput values based on the selected disk size:

Disk size | Default IOPS | Default throughput (MiB/s)  
---|---|---  
20 - 256 GB | 4,000 | 170  
> 256 - 512 GB | 7,000 | 240  
> 512 GB - 1 TB | 10,000 | 500  
> 1 TB - 4 TB | 16,000 | 750  
> 4 TB - 32 TB | Minimum of 70,000 or maximum IOPS for machine type | Minimum of 1,200 or maximum throughput for machine type  
> 32 TB - 64 TB | Minimum of 100,000 or maximum IOPS for machine type | Minimum of 1,200 or maximum throughput for machine type  
  
You can also set custom IOPS and throughput when using Hyperdisk Balanced.

### C4 machine series IOPS and throughput limits

The following table shows the minimum and maximum limits for IOPS and throughput (in MiB/s) for each machine type in the [C4 machine series](https://docs.cloud.google.com/sql/docs/postgres/machine-series-overview#c4) based on its vCPUs:

|  |  | Hyperdisk Balanced | Hyperdisk Balanced HA  
---|---|---|---|---  
vCPUs | Minimum IOPS | Minimum throughput | Maximum IOPs | Maximum throughput | Maximum IOPs | Maximum throughput  
2 | 3,000 | 140 MiB/s | 50,000 | 400 MiB/s | 50,000 | 400 MiB/s  
4 | 3,000 | 140 MiB/s | 50,000 | 400 MiB/s | 50,000 | 400 MiB/s  
8 | 3,000 | 140 MiB/s | 50,000 | 800 MiB/s | 50,000 | 800 MiB/s  
  
The following table shows the default Google Cloud Hyperdisk Balanced IOPS and throughput values based on the selected disk size:

Disk Size Range (GB) | Default IOPS | Default Throughput  
---|---|---  
10 to 256 | 4,000 | 170 MiB/s  
257 to 512 | 7,000 | 240 MiB/s  
513 to 1,024 | 10,000 | 500 MiB/s  
1,025 to 4,096 | 16,000 | 750 MiB/s  
4,097 to 32,768 | 70,000 | 1,200 MiB/s  
32,769 to 65,536 | 100,000 | 1,200 MiB/s  
  
You can also set custom IOPS and throughput when using Hyperdisk Balanced.

### N4 machine series IOPS and throughput limits

The following table shows the minimum and maximum limits for IOPS and throughput for each machine type in the [N4 machine series](https://docs.cloud.google.com/sql/docs/postgres/machine-series-overview#n4) based on its vCPUs:

**Note:** Read and write IOPs and throughput values are combined for Hyperdisk Balanced. |  |  | Hyperdisk Balanced | Hyperdisk Balanced HA  
---|---|---|---|---  
vCPUs | Minimum IOPS | Minimum throughput | Maximum IOPs | Maximum throughput | Maximum IOPs | Maximum throughput  
0-7 | 3,000 | 140 | 15,000 | 240 | 15,000 | 240  
8-15 | 3,000 | 140 | 15,000 | 480 | 15,000 | 480  
16-31 | 3,000 | 140 | 80,000 | 1,200 | 80,000 | 1,200  
32-47 | 3,000 | 140 | 100,000 | 1,600 | 100,000 | 1,200  
48+ | 3,000 | 140 | 160,000 | 2,400 | 100,000 | 1,200  
  
The following table shows the default Google Cloud Hyperdisk Balanced IOPS and throughput values based on the selected disk size:

Disk size | Default IOPS | Default throughput  
---|---|---  
20 - 256 GB | 4,000 | 170  
> 256 - 512 GB | 7,000 | 240  
> 512 GB - 1 TB | 10,000 | Minimum of 500 or maximum throughput of machine type  
> 1 TB - 4 TB | Minimum of 16,000 or maximum IOPS for machine type | Minimum of 750 or maximum throughput of machine type  
> 4 TB - 32 TB | Minimum of 70,000 or maximum IOPS for machine type | Minimum of 1,200 or maximum throughput for machine type  
> 32 TB - 64 TB | Minimum of 100,000 or maximum IOPS for machine type | Minimum of 1,200 or maximum throughput for machine type  
  
You can also set custom IOPS and throughput when using Hyperdisk Balanced.

### Hyperdisk Balanced custom IOPS and throughput

You can set custom IOPS and throughput levels for your Google Cloud Hyperdisk Balanced and Google Cloud Hyperdisk Balanced High Availability volumes. The modified values must meet the following requirements:

  * **IOPS**

    * Minimum: 3,000 IOPS
    * Maximum: 500 IOPS per GB disk capacity, for a maximum of 160,000 for Google Cloud Hyperdisk Balanced and a maximum of 100,000 for Google Cloud Hyperdisk Balanced High Availability.
  * **Throughput**

    * Minimum: 140 MiB/s
    * Maximum: For Google Cloud Hyperdisk Balanced, the greater of 2,400 MiB/s or the provisioned IOPS divided by 4. For Google Cloud Hyperdisk Balanced High Availability, the greater of 1,200 MiB/s, or the provisioned IOPS divided by 4.



### Hyperdisk Balanced limitations

Consider the following limitations when using Hyperdisk Balanced with your Cloud SQL instances:

  * Hyperdisk Balanced only allows changes to capacity and disk size, twice every four hours. Data workloads needing more frequent increases might result in extended periods of full storage and might impact performance.
  * Hyperdisk Balanced only allows changes to IOPS and throughput once every four hours. Data workloads needing more frequent increases might result in extended periods of full storage and might impact performance.



## Solid-state drive (SSD)

The solid-state drive (SSD) option is available for the general purpose shared core, general purpose dedicated core, and N2 machine series.

The SSD storage option provides an efficient, cost-effective option for your Cloud SQL Cloud SQL Enterprise edition instances. Compared to a hard disk drive, SSD is faster and provides more predictable performance. SSD offers high write and read throughput, and maintains low latency for data access. This makes it an excellent option for storing active data that requires frequent, low-latency access.

SSD is a Persistent Disk volumes offering that provides durable network storage devices. It is suitable for enterprise applications and high-performance databases that require lower latency and more IOPS. For more information, see [About Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks).

Cloud SQL sets IOPS and throughput for SSD storage based on the machine type and storage capacity you configure. You can't configure the values for IOPS and throughput.

### N2 machine series IOPS and throughput limits

The following table shows the maximum values for IOPS and throughput (in MiB/s) for the SSD storage option based on the number of vCPUs for Cloud SQL Enterprise Plus edition instances using the [N2 machine series](https://docs.cloud.google.com/sql/docs/postgres/machine-series-overview#n2) :

| Zonal | Regional  
---|---|---  
vCPUs | Maximum IOPs (read/write) | Maximum throughput (read/write) | Maximum IOPs (read/write) | Maximum throughput (read/write)  
2 | 15,000 / 15,000 | 240 / 240 | 15,000 / 15,000 | 240 / 120  
4 | 15,000 / 15,000 | 240 / 240 | 15,000 / 15,000 | 240 / 120  
8 | 15,000 / 15,000 | 800 / 800 | 15,000 / 15,000 | 800 / 400  
16 | 25,000 / 25,000 | 1,200 / 1,200 | 25,000 / 25,000 | 1,200 / 600  
32 | 60,000 / 60,000 | 1,200 / 1,200 | 60,000 / 60,000 | 1,200 / 600  
48 | 60,000 / 60,000 | 1,200 / 1,200 | 60,000 / 60,000 | 1,200 / 600  
64 | 100,000 / 100,000 | 1,200 / 1,200 | 100,000 / 80,000 | 1,200 / 1,000  
80 | 100,000 / 100,000 | 1,200 / 1,200 | 100,000 / 80,000 | 1,200 / 1,000  
96 | 100,000 / 100,000 | 1,200 / 1,200 | 100,000 / 80,000 | 1,200 / 1,000  
128 | 100,000 / 100,000 | 1,200 / 1,200 | 100,000 / 80,000 | 1,200 / 1,000  
**Note:** To increase the IOPS and throughput values for the N2 machine series, increase the storage capacity of your instance.

### General purpose machine series IOPS and throughput limits

The following table shows the maximum values for IOPS and throughput for the SSD storage option based on the number of vCPUs for the general purpose shared or dedicated core machine series, and custom machine types:

| Zonal | Regional  
---|---|---  
vCPUs | Maximum IOPs (read/write) | Maximum throughput (read/write) | Maximum IOPs (read/write) | Maximum throughput (read/write)  
1 | 15,000 / 15,000 | 200 / 200 | 15,000 / 15,000 | 200 / 100  
2-7 | 15,000 / 15,000 | 240 / 240 | 15,000 / 15,000 | 240 / 120  
8-15 | 15,000 / 15,000 | 800 / 800 | 15,000 / 15,000 | 800 / 400  
16-31 | 25,000 / 25,000 | 1,200 / 1,200 | 25,000 / 25,000 | 1,200 / 600  
32-63 | 60,000 / 60,000 | 1,200 / 1,200 | 60,000 / 60,000 | 1,200 / 600  
64+ | 100,000 / 100,000 | 1,200 / 1,200 | 100,000 / 80,000 | 1,200 / 1,000  
  
## Hard disk drive (HDD)

The hard disk drive (HDD) storage option is available for general purpose shared or dedicated core machine series only, and might be appropriate in certain use cases. For example, consider HDD for instances with large datasets (>10 TB) that are not latency-sensitive, are accessed infrequently, or where storage cost is a primary concern. HDD might also be suitable for the following workload categories:

  * Batch workloads with scans and writes, and only occasional random reads of a few rows.
  * Data archival, where you write large amounts of data and rarely read it.



For example, if you plan to store extensive historical data for a large number of remote-sensing devices and use the data to generate daily reports, then the cost savings for HDD storage might justify the performance trade-off. However, if you plan to use the data to display a real-time dashboard, HDD might not be the optimal choice because reads are much more frequent and slower with HDD storage.

### General purpose machine series IOPS and throughput limits

The following table shows the maximum values for IOPS and throughput for the HDD storage option based on the number of vCPUs for Cloud SQL instances:

| Zonal | Regional  
---|---|---  
vCPUs | Maximum IOPs (read/write) | Maximum throughput (read/write) | Maximum IOPs (read/write) | Maximum throughput (read/write)  
1 | 1,000 / 10,000 | 200 / 200 | 1,000 / 10,000 | 200 / 100  
2-7 | 3,000 / 15,000 | 240 / 240 | 3,000 / 15,000 | 240 / 120  
8-15 | 5,000 / 15,000 | 800 / 400 | 5,000 / 15,000 | 800 / 200  
16+ | 7,500 / 15,000 | 1,200 / 400 | 7,500 / 15,000 | 1,200 / 200  
  
## Options to manually reduce storage capacity

If it's later determined that the storage capacity of a Cloud SQL instance is larger than your application needs, then you can manually reduce, or shrink, your storage capacity to a smaller size.

For more information, see [About storage shrink](https://docs.cloud.google.com/sql/docs/postgres/about-storage-shrink).

## What's next

  * [Create an instance](https://docs.cloud.google.com/sql/docs/postgres/create-instance)
  * Learn more about the [machine series](https://docs.cloud.google.com/sql/docs/postgres/machine-series-overview) available in Cloud SQL.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
