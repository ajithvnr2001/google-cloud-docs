---
url: https://docs.cloud.google.com/filestore/docs/service-tiers-enterprise/
title: Filestore Multishares for GKE (Enterprise) service tier \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:15:14.807958+00:00
---

# Filestore Multishares for GKE (Enterprise) service tier  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/service-tiers-enterprise/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Filestore Multishares for GKE (Enterprise) service tier Stay organized with collections  Save and categorize content based on your preferences. 

Filestore Multishares for GKE is a Enterprise instance that allows a single high-performance Filestore instance tier to host multiple distinct NFS shares. 

A Filestore Enterprise instance combined with the [Filestore multishares for GKE](https://docs.cloud.google.com/filestore/docs/multishares) feature supports up to 80 [shares](https://docs.cloud.google.com/filestore/docs/creating-instances#instances_and_shares) in the [instance](https://docs.cloud.google.com/filestore/docs/creating-instances#instances_and_shares).

Use the Enterprise service tier for multishare instances and creating instances with the Filestore CSI driver. For any other use cases, use regional service tier. 

Enterprise specifications  Specification | Enterprise  
---|---  
Client connections | 2,000 per 1 TiB, scaling in increments of 500, for up to 20,000 connections  
File size | Up to the size of instance capacity  
Number of files* | Approximately 89,000,000 files per 1 TiB of capacity  
File locks | 250 per file  
Minimum capacity | 1 TiB  
Maximum capacity | 10 TiB  
Scaling direction | Up or down  
Minimum scaling units | 256 GiB  
Read throughput | 120 MiB/s per 1 TiB of provisioned capacity  
Write throughput | 100 MiB/s per 1 TiB of provisioned capacity  
Read IOPS | 12,000 per 1 TiB of provisioned capacity  
Write IOPS | 4,000 per 1 TiB of provisioned capacity  
Availability | Regional  
Data protection | [Backups](https://docs.cloud.google.com/filestore/docs/backups), [Snapshots](https://docs.cloud.google.com/filestore/docs/snapshots)  
Customer-managed encryption keys | Supported  
Non-disruptive maintenance | Supported (Enterprise instances remain available during maintenance events.)  
[Google Cloud VMware Engine](https://docs.cloud.google.com/filestore/docs/gcve-datastores) | Supported  
[Filestore multishares for GKE](https://docs.cloud.google.com/filestore/docs/multishares) | Supported  
[Protocol support](https://docs.cloud.google.com/filestore/docs/about-supported-protocols) | NFSv3, NFSv4.1  
[Instance replication](https://docs.cloud.google.com/filestore/docs/instance-replication) | Supported  
  
* The number of files listed is an indication of the maximum number of supported connections to small or empty files. The number of supported file connections decreases as file size increases. While no practical limit exists across service tiers, instance performance may be delayed when supporting a large number of files.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
