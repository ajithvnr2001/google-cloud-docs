---
url: https://docs.cloud.google.com/netapp/volumes/docs/quotas/
title: Quotas and limits \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:21:19.901109+00:00
---

# Quotas and limits  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Resources ](https://docs.cloud.google.com/netapp/volumes/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Google Cloud NetApp Volumes.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

There are also _system limits_ on NetApp Volumes resources. System limits can't be changed. 

Google Cloud NetApp Volumes use is subject to limits and default quotas. Limits can't be changed, however, you can request a quota increase. To learn more, see [Request a quota increase](https://docs.cloud.google.com/netapp/volumes/docs/quotas#request_a_quota_increase).

## View your API quotas

View your API quotas and usage for NetApp Volumes in the Google Cloud console.

[Go to NetApp API quotas](https://console.cloud.google.com/apis/api/netapp.googleapis.com/quotas)

## NetApp Volumes default quotas

The following table shows the default quotas for each resource. To increase or decrease most quotas, use the Google Cloud console. For more information, see [Request a higher quota limit](https://docs.cloud.google.com/docs/quotas/help/request_increase).

Resource | Default quota  
---|---  
Flex File and Flex Unified storage pool capacity (GiB) per region | 25 TiB  
Flex File and Flex Unified cross region replicated volumes per region | 5  
Flex File and Flex Unified volumes per region | 100  
Flex File and Flex Unified volumes with backup configuration per region | 10  
Flex File and Flex Unified storage pool throughput (MiBps) per region | 5120  
Flex File and Flex Unified storage pool IOPS per region | 160,000  
Standard storage pool capacity (GiB) per region | 25 TiB  
Standard cross region replicated volumes per region | 5  
Standard hybrid replicated volumes per region | 1  
Standard volumes per region | 100  
Standard volumes with backup configuration per region | 10  
Premium and Extreme storage pool capacity (GiB) per region | 25 TiB  
Premium and Extreme cross region replicated volumes per region | 5  
Premium and Extreme hybrid replicated volumes per region | 1  
Premium and Extreme volumes per region | 100  
Premium and Extreme volumes with backup configuration per region | 10  
Backup vaults per region for all service levels | 10  
  
## NetApp Volumes limits

NetApp Volumes feature limits vary by location and region. The following tables show the current limits per resource. You can't change these limits.

### Backup limits

Resource | Limit  
---|---  
Number of backups per volume | 1,000  
Total number of scheduled backups (daily, weekly, and monthly) | 1,000  
Maximum number of concurrent backups per Flex storage pool | 10  
  
### Storage pool limits

Resource | Limit  
---|---  
Minimum pool capacity | 

  * **Flex Unified and Flex File service level** : 1 TiB. For more information, see [NetApp Volumes service levels table](https://docs.cloud.google.com/netapp/volumes/docs/discover/service-levels)
  * **Flex Unified large capacity pool** : 6 TiB
  * **Standard, Premium, and Extreme service levels** : 2 TiB

  
Maximum pool capacity | 

  * **Flex Unified regular pool** : 425 TiB
  * **Flex Unified large capacity pool** : 
    * **Without auto-tiering** : 2.48 PiB
    * **With auto-tiering** : 20 PiB
  * **Standard service level** : 200 TiB
  * **Premium and Extreme service levels** : 10 PiB
  * **Flex File service level** : 
    * 200 TiB (regular pool)
    * 300 TiB (if custom performance is enabled)

  
Maximum number of volumes per storage pool | 

  * **Flex service level** : 
    * **File** type: 50
    * **Unified** type: 1000
  * **Standard, Premium, and Extreme service levels** : not applicable

  
Maximum number of storage pools | 

  * **Flex File and Flex Unified service levels** : 100 zonal pools per zone and 100 regional pools
  * **Standard, Premium, and Extreme service levels** : not applicable

  
Maximum number of replications per storage pool | 

  * **Flex Unified service level** : 100 replications per pool
  * **Flex File service level** : 10 replications per pool
  * **Standard, Premium, and Extreme service levels** : not applicable

  
  
### Networking limits

Resource | Limit  
---|---  
Number of VPC networks per project | 5  
  
### Volume limits

Resource | Limit  
---|---  
Volumes per region | **Flex Unified service level** : 5,000 zonal volumes per zone and 5,000 regional volumes  
  
**Standard, Premium, and Extreme service levels** : not applicable  
  
**Flex File service level** : 5,000 zonal volumes per zone and 5,000 regional volumes  
Minimum capacity of a single volume | **Flex Unified and Flex File service level** : 1 GiB. For more information, see [NetApp Volumes service levels table](https://docs.cloud.google.com/netapp/volumes/docs/discover/service-levels)  
  
**Standard, Premium, and Extreme service levels** : 100 GiB  
Maximum capacity of a single volume | **Flex File service level** :  
100 TiB (regular volume)  
300 TiB (if custom performance is enabled)  
  
**Flex Unified service level** :  
300 TiB for NFS and SMB  
128 TiB for iSCSI  
  
**Standard, Premium, and Extreme service levels** : 100 TiB  
Minimum capacity of a large capacity volume (in Flex Unified large capacity pool) | 4.8 TiB (default large volumes (48 member volumes))  
  
2,400 GiB (with custom number of member volumes (minimum 2))  
Maximum capacity of a large capacity volume (in Flex Unified large capacity pool) | 2.48 PiB without auto-tiering  
  
20 PiB with auto-tiering  
Minimum capacity of a large capacity volume (Premium and Extreme service levels only) | 15 TiB  
Maximum capacity of a large capacity volume (Premium and Extreme service levels only) | 3 PiB  
Number of snapshots per volume | 255  
Number of backups per volume | 1,000  
Maximum capacity of a single LUN | 128 TiB  
Maximum capacity of a single file | 128 TiB for all service levels, except 16 TiB for Flex File  
Maximum size of a single directory | Approximately 4 million files 1  
Maximum filename length | 255 characters  
Maximum number of NFS export rules per volume | 20  
Maximum length of an NFS export rule | 4,096 characters  
Maximum number of user and group quota rules | 100  
  
1 The limit might be less when you use long file names or Flex Unified pools with lower performance settings.

### Network File System (NFS) limits

Resource | Limit  
---|---  
Maximum number of UNIX groups supported for LDAP-enabled volumes | 1,024  
  
### Active Directory policy limits

Resource | Limit  
---|---  
Maximum number of Active Directory policies per region | 5  
  
### Inode limits

Every directory, file, or link uses an inode, but each volume has a limit on how many inodes it can store. If that limit is reached, you can't create new files or directories, even if there is free space. To resolve this, you must delete existing files or directories to free up inodes. Alternatively, you can also increase the volume capacity to add more inodes.

Google Cloud NetApp Volumes allocates one inode for every 32 KB of volume capacity, based on an average file size of 32 KB. If your average file size is smaller, you might run out of inodes before using up all the available storage capacity.

Volumes in Standard, Premium, and Extreme service levels provide a minimum of 21.2 million inodes for each volume. Beyond 683 GiB of capacity, the inode count increases linearly with volume capacity, adding one inode for every 32 KB. Flex volumes start with approximately 31,000 inodes for a 1 GiB volume and grow linearly with volume capacity at one inode for every 32 KB.

Auto-tiering reduces the amount of hot data in a volume, but doesn't impact the number of used inodes.

The maximum hard limit for each volume is 2,040 million inodes. For large capacity volumes, each constituent counts as a separate volume for inode limits. Premium and Extreme large capacity volumes have 24 constituents, and Flex Unified Default-mode large capacity volumes have 48 constituents. Each constituent has an inode density of one inode per 32 KB, with a hard limit of 2,040 million inodes per constituent. Because the total volume capacity is distributed across the constituents, each constituent represents a smaller portion of the overall volume capacity.

The following table provides a few examples of volume capacity versus maximum inodes for volumes:

Volume capacity in GiB | Inode limit for Standard, Premium, and Extreme service levels | Inode limit for Flex service level  
---|---|---  
100 | 21.2 million | 3.1 million  
512 | 21.2 million | 15.9 million  
1024 | 31.8 million | 31.8 million  
2048 | 63.7 million | 63.7 million  
4096 | 127.5 million | 127.5 million  
5200 | 161.8 million | 161.8 million  
  
For more information about monitoring inode usage, see [Methods for monitoring volume usage](https://docs.cloud.google.com/netapp/volumes/docs/monitor/monitor-volume-usage#methods_for_monitoring_volume_usage).

## Request a quota increase

**Important:** If your project doesn't have any NetApp Volumes resources, create a storage pool or volume of the minimum capacity before you request a quota increase. This action helps ensure that Google has the necessary account information to resolve your quota increase request.

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
