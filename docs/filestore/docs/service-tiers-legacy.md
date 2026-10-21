---
url: https://docs.cloud.google.com/filestore/docs/service-tiers-legacy/
title: Legacy Filestore service tiers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:06:38.664634+00:00
---

# Legacy Filestore service tiers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/service-tiers-legacy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Legacy Filestore service tiers Stay organized with collections  Save and categorize content based on your preferences. 

Filestore legacy service tiers include the following:

  * Standard / Basic HDD
  * Premium / Basic SSD



When creating new instances, use Zonal or Regional service tiers. You can still use the already existing High scale SSD instances.

## Basic HDD and Basic SSD

Basic tier Filestore instances are suitable for file sharing, software development, and use with GKE workloads. You can choose either HDD or SSD for storing data, with SSD offering greater performance at a higher cost.

Basic HDD instances have a performance increase when the provisioned capacity exceeds 10 TiB. The performance of basic SSD instances is fixed regardless of the provisioned capacity.

Basic tier specifications Specification | Basic HDD | Basic SSD  
---|---|---  
Client connections | Recommended limit of 500 | Recommended limit of 500  
File size | Up to 16 TiB | Up to 16 TiB  
Number of files* | 67,108,864 files per 1 TiB of capacity | 67,108,864 files per 1 TiB of capacity  
File locks | 128 per Filestore instance | 128 per Filestore instance  
Performance | Standard fixed | Premium fixed  
Minimum capacity | 

  * 1 TiB
  * On GKE†: 100 GiB

| 2.5 TiB  
Maximum capacity | 63.9 TiB | 63.9 TiB  
Scaling direction | Up only | Up only  
Minimum scaling units | 1 GiB | 1 GiB  
Read throughput | 

  * 1 TiB to 10 TiB capacity: 100 MiB/s
  * 10 TiB to 63.9 TiB capacity: 180 MiB/s
  * On GKE†: 100 GiB to 10 TiB capacity: 100 MiB/s

| 1,200 MiB/s  
Write throughput | 

  * 1 TiB to 10 TiB capacity: 100 MiB/s
  * 10 TiB to 63.9 TiB capacity: 120 MiB/s
  * On GKE†: 100 GiB to 10 TiB capacity: 100 MiB/s

| 350 MiB/s  
Read IOPS | 

  * 1 TiB to 10 TiB capacity: 600
  * 10 TiB to 63.9 TiB capacity: 1,000
  * On GKE†: 100 GiB to 10 TiB capacity: 600

| 60,000  
Write IOPS | 

  * 1 TiB to 10 TiB capacity: 1,000
  * 10 TiB to 63.9 TiB capacity: 5,000
  * On GKE†: 100 GiB to 10 TiB capacity: 1,000

| 25,000  
Availability | Zonal | Zonal  
Data protection | [Backups](https://docs.cloud.google.com/filestore/docs/backups) | [Backups](https://docs.cloud.google.com/filestore/docs/backups)  
Customer-managed encryption keys | Not supported | Not supported  
Non-disruptive maintenance | Not supported | Not supported  
[Google Cloud VMware Engine](https://docs.cloud.google.com/filestore/docs/gcve-datastores) | Not supported | Not supported  
[Filestore multishares for GKE](https://docs.cloud.google.com/filestore/docs/multishares) | Not supported | Not supported  
[Protocol support](https://docs.cloud.google.com/filestore/docs/about-supported-protocols) | NFSv3 | NFSv3  
  
* The number of files listed is an indication of the maximum number of supported connections to small or empty files. The number of supported file connections decreases as file size increases. While no practical limit exists across service tiers, instance performance may be delayed when supporting a large number of files.

† Basic HDD (on GKE) refers to Basic HDD instances with a minimum capacity of 100 GiB provisioned with the [Filestore CSI driver](https://docs.cloud.google.com/filestore/docs/csi-driver). Basic HDD instances with capacity lower than 1 TiB consume 1 TiB of quota.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
