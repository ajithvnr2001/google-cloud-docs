---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/storage-pools/overview/
title: Storage pools overview \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:29.147654+00:00
---

# Storage pools overview  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/storage-pools/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Storage pools overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the Google Cloud NetApp Volumes storage pools. Storage pools let you centrally manage the shared infrastructure and configuration for your [volumes](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/overview#about-volumes).

## About storage pools

Storage pools act as a container for volumes. All volumes in a storage pool share the same location, service level, Virtual Private Cloud network, [Active Directory policy](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/about-ad), LDAP settings, and [customer-managed encryption key (CMEK) policy](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/cmek-overview). You can assign the capacity of the pool to volumes within the pool. Billing is based on the location, service level, and capacity allocated to a pool independent of consumption at the volume level.

When you create a Flex Unified storage pool in ONTAP-mode, you must configure Active Directory and LDAP settings in ONTAP instead of using Google APIs and Google Cloud console.

## Supported locations

All volumes in a storage pool live in the same location as the pool. All service levels aren't available in every region. For more information about supported locations, see [NetApp Volumes supported locations](https://docs.cloud.google.com/netapp/volumes/docs/locations).

## Service levels

The service level is a property of the storage pool. Service levels have capacity-dependent throughput limits.

NetApp Volumes offers the following service levels:

  * Flex Unified

  * Flex File

  * Standard

  * Premium

  * Extreme


**Important:** Effective September 15, 2026, you can't create new Flex File storage pools, but existing pools remain supported. For more information, see [Migration to Flex Unified service level](https://docs.cloud.google.com/netapp/volumes/docs/get-started/migration-to-flex-unified).

For more information, see [NetApp Volumes service levels table](https://docs.cloud.google.com/netapp/volumes/docs/discover/service-levels).

The following table provides the throughput of allocated capacity for each service level and what each service level is best used for:

Service level | Throughput | Workload types  
---|---|---  
Flex Unified | Independent scaling of capacity and performance up to 5 GiBps | General purpose storage  
  
Databases and applications  
  
High-performance applications  
Flex File | Default performance: 16 KiBps per GiB of allocated pool capacity  
  
Custom performance: independent scaling of capacity and performance up to  
5 GiBps | General purpose storage  
Standard | 16 KiBps per GiB of allocated volume capacity | General purpose storage  
Premium | 64 KiBps per GiB of allocated volume capacity | Databases and applications  
Extreme | 128 KiBps per GiB of allocated volume capacity | High-performance applications  
**Note:** In regions with limited performance, you can provision throughput up to a maximum of 1.6 GiBps. For more information about limited performance regions, see [Supported regions for Flex Unified limited performance](https://docs.cloud.google.com/netapp/volumes/docs/discover/service-levels#supported_regions_for_flex_unified_limited_performance).

You can reassign the Premium service level volume to an Extreme service level storage pool and the other way around. This allows instant adjustments to changing performance requirements.

## Availability

Pools in different service levels have different availability. For more information, see [NetApp Volumes service level agreement (SLA)](https://cloud.google.com/netapp/volumes/sla). Pools of the Flex Unified and Flex File non-custom performance service level let you choose between zonal and regional availability.

A regional pool maintains two synchronous replicas of your data in two different zones. When creating a regional pool, you can choose the active zone and a replica zone. All volumes of your pool are available from the active zone, while the replica zone acts as a standby. In case the active zone fails or you are triggering a manual zone switch, all volume access moves to the replica zone, which then becomes the new active zone. The previous active zone becomes the new replica zone. This zone switch can cause a pause of file service activity. After the zone switch is completed, the file services starts again.

If the regional Flex active zone and the workload VMs are in the same Google Cloud zone, it optimizes I/O latency and helps you achieve better performance.

## Network

A pool defines which Virtual Private Cloud (VPC) its volumes connect to. The volumes are accessible only for clients that are on the same VPC or those connected to it with a VPN.

## Active Directory settings

Some network-attached storage (NAS) protocols or protocol variations require access to an external directory service. [NetApp Volumes supports Active Directory](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/about-ad) as the only directory service. An [Active Directory policy](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/about-ad) provides the service with all necessary information to join a Windows domain. Since connecting to Active Directory might fail for reasons such as incorrect routing, firewall settings, or credentials, NetApp Volumes provides you with a [connectivity test](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/test-ad-policy-connection) when you configure the Active Directory policy. The connectivity test checks whether an Active Directory policy is correctly connected to the Active Directory service.

While you can create multiple Active Directory policies per region, a single storage pool can only have one Active Directory policy attached to it. All volumes in the pool use the same policy. Different pools can use different policies.

## Customer-managed encryption key settings

NetApp Volumes encrypts the data of all volumes at rest using a Google-owned and Google-managed encryption key, however, you can choose to encrypt the volumes using a customer-managed encryption key (CMEK). You can attach a CMEK policy during storage pool creation; all of the volumes created in that pool use the policy.

Like all other pools, Flex Unified ONTAP-mode pools also use CMEK policies. Configuring different key managers isn't supported in ONTAP-mode.

## Capacity

NetApp Volumes lets you add or remove capacity to your volume as needed to adjust for any application changes. Capacity is allocated to storage pools and volumes, and can be modified.

Depending on the service level, storage pools and volumes have different size and resizing rules, specified in the [feature overview](https://docs.cloud.google.com/netapp/volumes/docs/discover/service-levels).

For Flex Unified, you can create regular and large capacity storage pools. You can't switch between both pool types. Use a large capacity pool if you need more than 5 GiBps throughput or over 300 TiB of capacity in a single volume without auto-tiering. Otherwise, use a regular pool.

## Auto-tiering

Auto-tiering lets you reduce cost by automatically and transparently moving unused data to cold storage. For more information about how auto-tiering works, see [Manage auto-tiering](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-auto-tiering).

You must enable auto-tiering on a storage pool before you can enable it for any volumes in the pool. For Flex Unified and Flex File custom performance, you must enable auto-tiering when you create the pool. For Premium and Extreme, you can also enable it on existing pools. When you enable auto-tiering for the pool, the selection is permanent.

## Volumes

Storage pools provide space, performance, and a configuration environment for volumes that host your data. Before you create volumes in a pool, make sure that the pool meets the following volume requirements:

  * The pool has enough storage capacity to host your volume and can grow to accommodate future data growth.

  * The pool has enough performance capacity to host your volume and can grow to accommodate future data growth.

  * The pool is connected to the correct VPC.

  * The pool has the correct CMEK settings.

  * The pool is connected to the correct Active Directory and can reach domain controllers.

  * To use NFS extended groups or multi-protocol volumes, check whether LDAP is enabled for the pool.

  * The pool has the appropriate service level.

  * The pool has the correct auto-tiering setting configured.




If the pools share the same location, network, Active Directory, LDAP, and CMEK settings, NetApp Volumes lets you move volumes between the Premium and Extreme service levels without any data copy. For all other service levels, moving volumes between pools involves data copy and assigns new access paths.

You can assign volumes to storage pools, and also move a volume within a pool to a different pool with the same settings (location, network, Active Directory policy, and CMEK policy) as long as the service level allows and the target pool has enough spare capacity.

Before you can start to create volumes, you need to provision a storage pool to host the volumes.

## Storage pool states

Each storage pool has a `state` attribute:

  * `CREATING`: the state while the pool is being created.

  * `READY`: the state after pool creation completes.




The following list shows the pool creation times for each service level:

  * Standard, Premium, and Extreme pools: a few seconds

  * Flex File pools: 15 to 20 minutes

  * Flex Unified regular pools: approximately 20 minutes

  * Large capacity pools: approximately 45 minutes




In some cases, pool creation can take longer.

When you update a pool, its state changes to `UPDATING` and returns to `READY` when the update completes. Updates take a few seconds for Standard, Premium, and Extreme pools, but take several minutes for Flex File and Flex Unified pools. While a pool is `UPDATING`, you can't edit its parameters.

During planned service upgrades or unplanned backend infrastructure failures, a Flex Unified pool enters the `DEGRADED` state.

The following are the planned events, which aren't subject to the SLA:

  * **Planned maintenance events** : For more information about how to subscribe to email notifications for planned maintenance events, see [View planned maintenance events](https://docs.cloud.google.com/netapp/volumes/docs/monitor/maintenance-events#view_planned_maintenance_events).

  * **Internal updates** : Increasing the throughput or IOPS of Flex Unified pools triggers internal pool infrastructure updates.




The following are the unplanned events:

  * **Infrastructure failures** : Failures in the service backend.



When a Flex Unified pool is in a `DEGRADED` state, you can't perform the following operations:

  * Pool updates

  * Cross-region replication (CRR)

  * CMEK-backed volume creation

  * CMEK migration workflows

  * CMEK pool creation




While the pool is in the `DEGRADED` state, write latency increases and maximum write throughput decreases by up to 60%. Recovery is automatic and requires no manual intervention. During the recovery process, you experience a few [I/O pauses](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/application-resilience#io_pauses). Recovery typically takes a few minutes, but in exceptional cases such as when a redundant copy of the pool is lost, it takes several hours.

## What's next

[Create a storage pool](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/storage-pools/create-storage-pool).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
