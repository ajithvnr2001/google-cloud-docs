---
url: https://docs.cloud.google.com/filestore/docs/service-tiers-zonal/
title: Zonal tier \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:56.477586+00:00
---

# Zonal tier  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/service-tiers-zonal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Zonal tier Stay organized with collections  Save and categorize content based on your preferences. 

The Filestore Zonal tier is optimized for high performance computing (HPC), batch compute, and localized workloads that require high throughput and low latency. It lets you process large data sets, perform batch compute jobs, and advanced AI/ML training as well as build systems and development environments requiring fast local storage.

Zonal instances allow for non-disruptive upgrades (NDUs) and support [custom performance](https://docs.cloud.google.com/filestore/docs/custom-performance) that lets you define the performance settings independently from capacity.

The Zonal tier replaces the high scale SSD.

Zonal specifications Specification | Lower capacity range  | Higher capacity range   
---|---|---  
Capacity range | 1 TiB to 9.75 TiB | 10 TiB to 100 TiB  
Usage | Suitable for performance-critical workloads with lower capacity needs | Suitable for performance-critical workloads with higher capacity needs, very high number of connected clients, high single client throughput, or overall high IOPS or throughput.  
Client connections | 2,000 per 1 TiB, scaling in increments of 500,   
for up to 19,500 connections | 8,000 per 10 TiB, scaling in increments of 2,000,   
for up to 80,000 connections  
File size | Up to the size of the instance capacity | Up to the size of the instance capacity  
Number of files* | Approximately 89,000,000 files per 1 TiB of capacity | Approximately 89,000,000 files per 1 TiB of capacity  
File locks | 250 per file | 250 per file  
Minimum capacity | 1 TiB | 10 TiB  
Maximum capacity | 9.75 TiB | 100 TiB  
Scaling direction | Up or down | Up or down  
Minimum scaling units | 256 GiB | 2.5 TiB  
Read throughput | 260 MiB/s per 1 TiB of provisioned capacity | 650 MiB/s per 2.5 TiBs of provisioned capacity  
Write throughput | 88 MiB/s per 1 TiB of provisioned capacity | 220 MiB/s per 2.5 TiBs of provisioned capacity  
Read IOPS | 9,200 per 1 TiB of provisioned capacity | 23,000 per 2.5 TiBs of provisioned capacity  
Write IOPS | 2,600 per 1 TiB of provisioned capacity | 6,500 per 2.5 TiBs of provisioned capacity  
Availability | Zonal | Zonal  
Data protection | [Backups](https://docs.cloud.google.com/filestore/docs/backups), [Snapshots](https://docs.cloud.google.com/filestore/docs/snapshots) | [Backups](https://docs.cloud.google.com/filestore/docs/backups), [Snapshots](https://docs.cloud.google.com/filestore/docs/snapshots)  
Customer-managed encryption keys | Supported | Supported  
Non-disruptive maintenance | Supported (zonal instances remain available during maintenance events.) | Supported (zonal instances remain available during maintenance events.)  
[Google Cloud VMware Engine](https://docs.cloud.google.com/filestore/docs/gcve-datastores) | Supported | Supported  
[Filestore multishares for GKE](https://docs.cloud.google.com/filestore/docs/multishares) | Not supported | Not supported  
[Protocol support](https://docs.cloud.google.com/filestore/docs/about-supported-protocols) | NFSv3, NFSv4.1 | NFSv3, NFSv4.1  
[Instance replication](https://docs.cloud.google.com/filestore/docs/instance-replication) | Supported | Supported  
[Custom performance](https://docs.cloud.google.com/filestore/docs/custom-performance) | Supported | Supported  
  
* The number of files listed is an indication of the maximum number of supported connections to small or empty files. The number of supported file connections decreases as file size increases. While no practical limit exists across service tiers, instance performance may be delayed when supporting a large number of files.

## Zonal limitations

The capacity range selection is permanent. Once the outer limits of the instance capacity are met, the service tier doesn't scale up or down to a new capacity range. If greater or lower capacity is needed, you must create a new instance with the service tier and capacity range you want to use.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
