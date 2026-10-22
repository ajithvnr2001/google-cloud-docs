---
url: https://docs.cloud.google.com/compute/docs/disks/async-pd/about/
title: About Asynchronous Replication \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:09.688371+00:00
---

# About Asynchronous Replication  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/async-pd/about/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About Asynchronous Replication Stay organized with collections  Save and categorize content based on your preferences. 

Asynchronous Replication provides low recovery point objective ([RPO](https://wikipedia.org/wiki/Recovery_point_objective)) and low recovery time objective ([RTO](https://wikipedia.org/wiki/Recovery_time_objective)) block storage replication for cross-region active-passive disaster recovery (DR).

Asynchronous Replication is a storage option that provides asynchronous replication of data between two regions. In the unlikely event of a regional outage, Asynchronous Replication lets you failover your data to a secondary region and restart your workload in that region.

You can use Asynchronous Replication to manage replication for Compute Engine workloads at the infrastructure-level, instead of the workload-level.

## Overview

Asynchronous Replication replicates data from a disk that is attached to a running workload, the _primary disk_ , to a separate disk located in another region. The disk receiving replicated data is referred to as the _secondary disk_.

The region that the primary disk is located in is referred to as the _primary region_ and the region that the secondary disk is located in is referred to as the _secondary region_. The primary and secondary regions are referred to as a _region pair_.

Any disk that meets the [disk requirements](https://docs.cloud.google.com/compute/docs/disks/async-pd/configure#disk_requirements) can be used as a primary disk. After you have a primary disk, you can [create a secondary disk](https://docs.cloud.google.com/compute/docs/disks/async-pd/configure#create_a_secondary_disk) that references the primary disk and [start replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-replication#start_replication) from the primary disk to the secondary disk.

If you stop replication from the primary disk at any point, and want to restart replication at a later point, then you must create a new secondary disk to restart replication.

### Consistency groups

Consistency groups enable you to perform DR and DR testing across multiple disks. A consistency group is a resource policy that does the following:

  * Aligns replication across primary disks and ensures that all disks contain replication data from a common point in time, which is used for DR.
  * Aligns disk clones from secondary disks and ensures that all disk clones contain data from a common point in time, which is used for DR drills.



If you want to align the replication period across multiple disks, add primary disks to a consistency group. If you want to clone multiple disks and ensure those clones have data from a common point in time, add secondary disks to a consistency group. A consistency group can be used for replication or cloning, but not both simultaneously.

If you want to add primary disks to a consistency group, you must [add disks to the consistency group](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-consistency-groups#add_a_disk_to_a_consistency_group) before you start replication. You can add secondary disks to a consistency group at any time.

### Failover and failback

In the event of an outage in the primary region, it is your responsibility to identify the outage and failover restart your workload using the secondary disks, in the secondary region. Asynchronous Replication doesn't offer outage monitoring. You can identify an outage using [RPO metrics](https://docs.cloud.google.com/compute/docs/disks/async-pd/performance#monitor_rpo), [health checks](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts), application-specific metrics, and by contacting Cloud Customer Care.

The [failover process](https://docs.cloud.google.com/compute/docs/disks/async-pd/failover-failback#failover_to_the_secondary_disk) involves the following tasks:

  1. Stop replication.
  2. Attach the secondary disks to VMs in the secondary region.



After you failover disks, it is your responsibility to validate and restart your application workload in the secondary region and reconfigure the network addresses that are used to access your application to point to the secondary region.

Following a failover from the primary region to the secondary region, the secondary region becomes the acting primary region. After the outage or disaster gets resolved, you can initiate failback to start replication from the original secondary region (the acting primary region) to the original primary region. You can optionally repeat the process to move the workload back to the original primary region.

The [failback process](https://docs.cloud.google.com/compute/docs/disks/async-pd/failover-failback#failback_to_the_original_primary_region) involves the following tasks:

  1. Configure replication between the new primary region and the original primary region.

     * The original secondary disk is now the new primary disk, and you configure it to replicate to a new secondary disk in the original primary region.
     * You can create a new consistency group resource policy in the new primary region so that the new primary disks (the original secondary disks) can replicate consistently to a new set of secondary disks in the original primary region.
  2. (Optional) After the initial replication has occurred, you can repeat the failover process to return the workload to the original primary region.




### Disk encryption

Primary and secondary disks don't support customer-supplied encryption keys (CSEK)([Deprecated](https://docs.cloud.google.com/compute/docs/deprecations)). Use [Google-owned and Google-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/default-keys) or [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption) instead. If you use CMEK on the primary disk, you must also use CMEK on the secondary disk. You can use different CMEKs on both disks.

### Customize a secondary disk

When you create a secondary disk, Compute Engine automatically copies the properties of the primary disk to the secondary disk. You can change certain properties of the secondary disk so that they differ from the primary disk. For example, the primary and secondary disk must have the same size and encryption key, but you might assign additional labels to the secondary disk.

If the primary disk is a boot disk, the secondary disk is created with the boot configuration of the primary disk. The boot configuration includes information about the OS architecture, OS licenses, and its guest OS features.

For boot disks, you can enable additional security or networking options on the secondary disk by specifying additional guest OS features. However, you can't remove any of the primary disk's guest OS features. Compute Engine merges the new features you specify with the existing guest OS features of the primary disk.

For more information on how to customize a secondary disk, see [Create a custom secondary disk](https://docs.cloud.google.com/compute/docs/disks/async-pd/configure#secondary2).

#### Example

Suppose you have a boot disk called `disk-1`, with the following guest OS features: `[GVNIC, UEFI_COMPATIBLE]`.

If you create a secondary disk from `disk-1`, you can only specify additional features. You can't remove the `UEFI_COMPATIBLE` and `GVNIC` features. So, if you specify `MULTI_IP_SUBNET` when you create the secondary disk, the new feature is merged with those of the primary disk, so the resulting guest OS features for the secondary disk are `[GVNIC,UEFI_COMPATIBLE, and MULTI_IP_SUBNET]`.

### Modify a primary disk

After you create the secondary disk, you might want to modify the properties of the primary disk. For some properties, if you make a change on the primary disk, Compute Engine automatically updates the property on the secondary disk.

Compute Engine monitors and automatically updates the following properties:

  * Access mode (Hyperdisk only)
  * Disk size
  * Provisioned IOPS and throughput (Hyperdisk only)
  * Replication status



If you modify any other properties of the primary disk, you must manually update the secondary disk.

  * To learn how to change the size of a Persistent Disk or Hyperdisk volume, see [Modify the size of a Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk) and [Modify the size and provisioned performance of a Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks), respectively.
  * To learn how to modify a Hyperdisk's access mode, see [Access mode changes](https://docs.cloud.google.com/compute/docs/disks/modify-persistent-disk#access_mode).



### Asynchronous Replication and regional disks

You can use Asynchronous Replication with [regional disks](https://docs.cloud.google.com/compute/docs/disks#repds) to achieve high availability (HA) and DR.

Regional persistent disks can be used as the primary or secondary disk in a Asynchronous Replication disk pair. A disk pair is a primary disk that replicates to a secondary disk.

When using a regional disk as the primary disk, replication remains uninterrupted even if one of its zones experiences an outage. The regional primary disk continues replicating data from the healthy zone to the secondary disk. Similarly, when a regional disk serves as a secondary disk, replication persists despite an outage in one of its zones. Using a regional disk as a secondary disk prepares your workload for high availability across zones in the event of a failover, where the secondary disk transitions to become the new primary disk.

## Limitations

  * Asynchronous Replication is supported only for the following [disk types](https://docs.cloud.google.com/compute/docs/disks): 
    * Balanced Persistent Disk
    * Performance (SSD) Persistent Disk
    * Hyperdisk Balanced
    * Hyperdisk Balanced High Availability
    * Hyperdisk Extreme
  * Read-only disks aren't supported.
  * Multi-writer disks are supported only for Hyperdisk Balanced and Hyperdisk Balanced High Availability.
  * Not all changes to Hyperdisk properties automatically apply to the secondary disk. For more information on which properties automatically apply to the secondary disk, see Secondary disk customization.
  * Each disk can have a maximum size of 64 TiB.
  * You must stop replication before you can delete a primary or secondary disk.
  * If replication is ongoing for a VM's boot disk, then you can't delete the VM until you stop replication.
  * If a primary disk is attached to a VM as a non-boot disk, and the disk is configured to be deleted with the VM, you can't delete the VM or the disk until you stop replication or detach the primary disk from the VM. Attempts to delete the VM will fail until you stop replication.
  * Each project can have at most 1000 disk pairs in each region pair.

For example, a given project, `project-1` can have up to 1000 disk pairs in the Iowa-Oregon region pair. `project-1` can also have up to 1000 disk pairs in the Belgium-Frankfurt region pair.




## Supported regions

Asynchronous Replication is available in all regions in the following continents:

  * Asia, except Indonesia
  * Europe
  * North America
  * Oceania
  * South America



You can replicate a primary disk in a given region to a secondary disk in any available region within the same continent. This means that you can create a region pair from any two regions within the same continent.

For example, suppose you have a primary disk in Frankfurt (`europe-west3`). You can replicate that disk to a secondary disk anywhere in Europe, but you can't replicate it to a region in North America.

For a full list of all regions in Compute Engine, see [Available zones and regions](https://docs.cloud.google.com/compute/docs/regions-zones#available).

## Performance

The recovery point objective (RPO), or the time delay for when data is available at the secondary site, depends on disk change rates. Asynchronous Replication typically replicates data with a target RPO of one minute, for up to 12.5 GB of compressed changed blocks per minute with disk blocks replicated with 4 KB block granularity. If a given block is changed multiple times between replication events, only the most recent change is replicated to the secondary disk. At higher disk change rates, RPO may be greater than one minute and typically increases as disk change rates grow. RPO is not configurable.

RPO might exceed one minute in the following scenarios:

  * **When disk replication starts.** During the initial replication, Asynchronous Replication replicates all the used blocks on the primary disk to the secondary disk. The initial replication is complete when the [`disk/async_replication/time_since_last_replication` metric](https://docs.cloud.google.com/compute/docs/disks/async-pd/performance#monitor_rpo) is available in Cloud Monitoring.
  * **If the disk change rate is greater than 12.5 GB of compressed changed blocks per minute.** After a spike in disk changes, the RPO for later replication cycles might exceed one minute while replication catches up.
  * **If you detach a disk from a VM or restart a VM while the disk is replicating.** Disks that are undergoing replication that are detached from a VM might see RPO increase up to five minutes for a short period of time.



To learn how to view the RPO for your disks, see [Asynchronous Replication performance metrics](https://docs.cloud.google.com/compute/docs/disks/async-pd/performance).

The recovery time objective (RTO) during [failover](https://docs.cloud.google.com/compute/docs/disks/async-pd/failover-failback#failover_to_the_secondary_disk) depends on the time it takes to complete the various tasks involved in failing over your workload to a new region. Tasks such as stopping replication and attaching disks to VMs in the secondary region should take only a few minutes to complete. You can speed up RTO by ensuring that you have VMs running in the secondary region so that if failover occurs, you don't have to wait for VMs to start up.

## What's next

  * Learn how to [configure replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/configure).
  * Learn how to [manage replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-replication).
  * Learn how to [manage consistency groups](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-consistency-groups).
  * Learn how to [failover and failback](https://docs.cloud.google.com/compute/docs/disks/async-pd/failover-failback).
  * Learn how to [manage disks that use Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-async-disks).
  * Learn how to [Monitor Asynchronous Replication performance](https://docs.cloud.google.com/compute/docs/disks/async-pd/performance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
