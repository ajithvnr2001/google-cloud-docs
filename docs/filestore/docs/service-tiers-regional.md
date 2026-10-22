---
url: https://docs.cloud.google.com/filestore/docs/service-tiers-regional/
title: Regional service tier \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:30.101734+00:00
---

# Regional service tier  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/service-tiers-regional/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Regional service tier Stay organized with collections  Save and categorize content based on your preferences. 

The Filestore Regional service tier is intended for mission-critical, high performance computing applications requiring continuous availability and regional resilience. It provides regional storage resilient to zone outages by replicating data across multiple zones within a region.

Regional service tier provides the following benefits:

  * Optimized for enterprise-grade network attached storage (NAS)
  * Allows for non-disruptive upgrades (NDUs)
  * Offers linear performance that changes with capacity, staying within the stated capacity range.
  * Supports [custom performance](https://docs.cloud.google.com/filestore/docs/custom-performance), letting you set performance options separately from capacity.

Regional specifications Specification | Lower capacity range  | Higher capacity range   
---|---|---  
Capacity range | 100 GiB to 10,239 GiB | 10 TiB to 100 TiB  
Client connections | 2,000 per 1 TiB, scaling in increments of 500,   
for up to 19,500 connections | 8,000 per 10 TiB, scaling in increments of 2,000,   
for up to 80,000 connections  
File size | Up to the size of instance capacity | Up to the size of instance capacity  
Number of files* | Approximately 89,000,000 files per 1 TiB of capacity | Approximately 89,000,000 files per 1 TiB of capacity  
File locks | 250 per file | 250 per file  
Performance | Configurable | Configurable  
Minimum capacity | 100 GiB | 10 TiB  
Maximum capacity | 10,239 GiB | 100 TiB  
Scaling direction | Up or down | Up or down  
Minimum scaling units | 1 GiB | 2.5 TiB  
Read throughput | 120 MiB/s per 1 TiB of provisioned capacity | 650 MiB/s per 2.5 TiBs of provisioned capacity  
Write throughput | 100 MiB/s per 1 TiB of provisioned capacity | 220 MiB/s per 2.5 TiBs of provisioned capacity  
Read IOPS | 12,000 per 1 TiB of provisioned capacity | 23,000 per 2.5 TiBs of provisioned capacity  
Write IOPS | 4,000 per 1 TiB of provisioned capacity | 6,500 per 2.5 TiBs of provisioned capacity  
Availability | Regional | Regional  
Data protection | [Backups](https://docs.cloud.google.com/filestore/docs/backups), [Snapshots](https://docs.cloud.google.com/filestore/docs/snapshots) | [Backups](https://docs.cloud.google.com/filestore/docs/backups), [Snapshots](https://docs.cloud.google.com/filestore/docs/snapshots)  
Customer-managed encryption keys | Supported | Supported  
Non-disruptive maintenance | Supported (Regional instances remain available during maintenance events.) | Supported (Regional instances remain available during maintenance events.)  
[Google Cloud VMware Engine](https://docs.cloud.google.com/filestore/docs/gcve-datastores) | Supported | Supported  
[Filestore multishares for GKE](https://docs.cloud.google.com/filestore/docs/multishares) | Not supported | Not supported  
[Protocol support](https://docs.cloud.google.com/filestore/docs/about-supported-protocols) | NFSv3, NFSv4.1 | NFSv3, NFSv4.1  
[Instance replication](https://docs.cloud.google.com/filestore/docs/instance-replication) | Supported | Supported  
[Custom performance](https://docs.cloud.google.com/filestore/docs/custom-performance) | Supported | Supported  
  
*The number of files listed is an indication of the maximum number of supported connections to small or empty files. The number of supported file connections decreases as file size increases. While no practical limit exists across service tiers, instance performance may be delayed when supporting a large number of files.

## Regional tier limitations

The following limitations apply:

  * The regional service tier can't be combined with the Filestore multishares feature.
  * The regional service tier can't be combined with the [GKE Filestore CSI driver](https://docs.cloud.google.com/filestore/docs/csi-driver).



### Capacity

  * 10 TiB regional instances must be created with the higher capacity range specification (10 TiB to 100 TiB).
  * Capacity range selection is permanent. Once the outer limits of the instance capacity are met, the service tier does not scale up or down to a new capacity range. If greater or lower capacity is needed, you must create a new instance with the service tier and capacity range you want to use.



### Backups

Backup `restore` operations are only supported when restoring to a new instance. For these operations, the new instance must match the service tier and also accommodate instance capacity greater than or equal to the size of the backup. For a detailed description of backup limitations, see [Backups](https://docs.cloud.google.com/filestore/docs/backups).

### Performance

  * While performance scales linearly with capacity, note that a 10 TiB enterprise instance will have better performance than a 10 TiB regional instance.

  * Performance scales linearly with capacity within the parameters of the specified capacity range. Performance is not linear between the two regional capacity ranges. A regional instance with 9.75 TiB of capacity will have better performance, for example, with an upper limit of 117,000 Read IOPS, than a regional instance with 10 TiB of instance capacity, with an upper limit of 92,000 Read IOPS. For more information, see [Performance](https://docs.cloud.google.com/filestore/docs/performance#expected).

  * Instances with capacity lower than 1,024 GiB have a fixed minimum IOPS value of 2,000. When creating instances smaller than 1,024 GiB, you must enable custom performance.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
