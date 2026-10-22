---
url: https://docs.cloud.google.com/netapp/volumes/docs/discover/how-it-works/storage-pools/
title: Storage pools \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:25.749308+00:00
---

# Storage pools  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/discover/how-it-works/storage-pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)



Send feedback 

#  Storage pools Stay organized with collections  Save and categorize content based on your preferences. 

## Storage pools

Storage pools act as a container for volumes. All volumes in a storage pool share the same region, service level, VPC network, [Active Directory (AD) policy], and [customer-managed encryption key (CMEK) policy]. The capacity to the pool can be assigned to volumes within the pool. Billing is based on region, service level, and capacity allocated to a pool independent of consumption at the volume level.

### Supported regions

### Service levels

The service level is a property of the storage pool. Service levels have capacity-dependent throughput limits. NetApp Volumes offers two service levels: Premium and Extreme. For a volume to have a different service level, you need to reassign it to a storage pool with the target service level. 

Service level | Throughput per TiB of allocated volume capacity | Workload types  
---|---|---  
Premium | 64 MiB/s | Databases and applications  
Extreme | 128 MiB/s | High-performance applications  
  
### Network

A pool defines which Virtual Private Cloud (VPC) its volumes connect to. The volumes are accessible only for clients that are on the same VPC or those connected to it with a VPN.

### Active Directory settings

Some NAS protocols or protocol variations require access to an external directory service. [NetApp Volumes support Active Directory] as the only directory service. You can attach one Active Directory policy to a single pool.

### Customer-managed encryption key settings

NetApp Volumes encrypts the data of all volumes at rest using a Google-owned and Google-managed encryption key. you can choose to encrypt the volumes using a customer-managed encryption key (CMEK). You can attach a CMEK policy during storage pool creation and all volumes created in that pool will use it. You can have a mix of storage pools with and without CMEK policies in a region. 

### Capacity

NetApp Volumes allows you to add or remove capacity to your volume as needed to adjust for any application changes. Capacity is allocated to storage pools and volumes, and can be modified.

  * Storage pools: You can allocate 2 TiB - 10 PiB of capacity to a storage pool and increase or decrease capacity in 1 TiB increments.

  * Volumes: You can allocate 100-102,400 GiB of capacity to a volume and increase or decrease in 1 GiB increments.




### Volumes

You can assign volumes to storage pools, and also move a volume created within a pool to a different pool with the same settings (region, network, AD policy, and CMEK policy) as long as the target pool has enough spare capacity. 

For more information, see [Manage storage pools]. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
