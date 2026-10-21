---
url: https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk/
title: About synchronous disk replication \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:17.285427+00:00
---

# About synchronous disk replication  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About synchronous disk replication Stay organized with collections  Save and categorize content based on your preferences. 

Regional Persistent Disk and Hyperdisk Balanced High Availability are storage options that let you implement high availability (HA) services in Compute Engine. Regional Persistent Disk and Hyperdisk Balanced High Availability synchronously replicate data between two zones in the same region and ensure HA for disk data for up to one zonal failure. 

Regional Persistent Disk and Hyperdisk Balanced High Availability volumes are designed for workloads that require a lower Recovery Point Objective (RPO) and Recovery Time Objective (RTO). To learn more about RPO and RTO, see [Basics of disaster recovery planning](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide#basics_of_dr_planning).

Regional Persistent Disk and Hyperdisk Balanced High Availability volumes are designed to work with regional [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances). 

This document provides an overview of how to build HA services with Regional Persistent Disk and Hyperdisk Balanced High Availability volumes.

When you decide to use Regional Persistent Disk or Hyperdisk Balanced High Availability, make sure that you compare the different options for increasing service availability and the [cost, performance, and resiliency](https://docs.cloud.google.com/compute/docs/disks/high-availability-regional-persistent-disk#compare_cost_performance_and_resiliency) for different service architectures.

## About synchronous disk replication

A Regional Persistent Disk or Hyperdisk Balanced High Availability volume, also referred to as a regional disk, or synchronously replicated disk, has a primary and a secondary zone within its region where it stores disk data:

  * **Primary zone** is the same zone where the compute instance that you attach the disk to is located.
  * **Secondary zone** is an alternate zone of your choice within the same region.



Compute Engine maintains replicas of your disk in both these zones. When you write data to your disk, Compute Engine synchronously replicates that data to the disk replicas in both zones to ensure HA. The data of each zonal replica is spread across multiple physical machines within the zone to ensure durability. Zonal replicas ensure that the data of the disk remains available and provide protection against temporary outages in one of the disk zones.

### Replica state for zonal replicas

Disk replica state for Regional Persistent Disk or Hyperdisk Balanced High Availability shows you the state of a zonal replica in comparison to the content of the disk. Zonal replicas for your disks are in one of the following disk replica states at all times:

  * **Synced** : The replica is available, synchronously receives all the writes performed to the disk, and is up to date with all the data on the disk.
  * **Catching up** : The replica is available but is still catching up with the data on the disk from the other replica.
  * **Out of sync** : The replica is temporarily unavailable and out of sync with the data on the disk.



To learn how to check and track the replica states of your zonal replicas, see [Monitor the disk replica states](https://docs.cloud.google.com/compute/docs/disks/monitor-regional-persistent-disk-replica-state).

### Replication states for regional disks

Depending on the state of the individual zonal replicas, your Regional Persistent Disk or Hyperdisk Balanced High Availability volume can be in one of the following replication states:

  * **Fully replicated:** Replicas in both zones are available and are synced with the latest disk data.
  * **Catching up:** Your zonal replicas are available, but one of the zonal replicas is catching up with the latest disk data.
  * **Degraded:** One of the zonal replicas has a status of `out of sync` due to a failure or an outage.



If the disk replication status is `catching up` or `degraded`, then one of the zonal replicas is not updated with all the data. Any outage during this time in the zone of the healthy replica results in an unavailability of the disk until the healthy replica zone is restored.

When your Regional Persistent Disk or Hyperdisk Balanced High Availability volume is catching up, Google Cloud starts healing the zonal replica that is catching up. Google recommends that you wait for the affected zonal replica to catch up with the data on the disk, at which point its status changes to `Synced`. After the zonal replica then moves to the synced state, the regional disk status changes back to the `Fully replicated` state.

If the regional disk has a status of `catching up` or `degraded` for a prolonged period of time and does not meet your organization's RPO requirements, we recommend that you take snapshots of the primary replica in either of following ways:

  * Enable scheduled snapshots.
  * Create a manual snapshot of your Regional Persistent Disk or Hyperdisk Balanced High Availability disk.



After you create a snapshot, you can create a new Regional Persistent Disk or Hyperdisk Balanced High Availability disk by using that snapshot as the source. This restores the snapshot to the new disk. Your new disk also starts in a fully replicated state with healthy data replication.

To learn how to check the replication state of your Regional Persistent Disk or Hyperdisk Balanced High Availability disk, see [Determine the replication state of disks](https://docs.cloud.google.com/compute/docs/disks/monitor-regional-persistent-disk-replica-state#determine_repd_replication_state).

### Replica recovery checkpoint

A _replica recovery checkpoint_ is a disk attribute that represents the most recent [crash-consistent](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices#prepare_for_consistency) point in time of a fully replicated disk. Compute Engine automatically creates and maintains a single replica recovery checkpoint for each regional disk. When a disk is fully replicated, Compute Engine keeps refreshing its checkpoint approximately every 15 minutes to ensure that the checkpoint remains updated. When the disk replication status is `degraded`, Compute Engine lets you create a standard snapshot from the replica recovery checkpoint of that disk. The resulting standard snapshot captures the data from the most recent crash-consistent version of the fully replicated disk.

In rare scenarios, when your disk is degraded, the zonal replica that is synced with the latest disk data can also fail before the out-of-sync replica catches up. You won't be able to force-attach your disk to compute instances in either zone. Your replicated disk becomes unavailable and you must migrate the data to a new disk. In such scenarios, if you don't have any existing standard snapshots available for your disk, you might still be able to recover your disk data from the incomplete replica by using a standard snapshot created from the replica recovery checkpoint. 

**Important:** In case of an unavailable disk, Google recommends that you always use any existing standard snapshots to create a new Regional Persistent Disk or Hyperdisk Balanced High Availability volume and recover disk data. Create standard snapshots from a checkpoint only if you don't have any existing standard snapshots available. 

Compute Engine automatically creates replica recovery checkpoints for each mounted Regional Persistent Disk or Hyperdisk Balanced High Availability disk. You don't incur any additional charges for the creation of these checkpoints. However, you do incur any applicable storage charges for the creation of snapshots and compute instances when you use these checkpoints to migrate your regional disk to functioning zones.

Learn more about how to [recover your regional disk data using a replica recovery checkpoint](https://docs.cloud.google.com/compute/docs/disks/repd-failover#recover-repd-using-checkpoint).

## Regional disk failover

In the event of an outage in a zone, the zone becomes inaccessible and the compute instance in that zone can't perform read or write operations on its disk. To allow the instance to keep performing read and write operations for the regional disk, Compute Engine allows migration of disk data to the other zone where the disk has a replica. This process is called _failover_.

The failover process involves detaching the zonal replica from the instance in the affected zone and then attaching the zonal replica to a new instance in the secondary zone. Compute Engine synchronously replicates the data on your disk to the secondary zone to ensure a quick failover in case of a single replica failure.

### Failover by application-specific regional control plane

The application-specific regional control plane is not a Google Cloud service. When you design HA service architectures, you must build your own application-specific regional control plane. This application control plane decides which instance must have the regional disk attached and which instance is the current primary instance.

When a failure is detected in the primary instance or database of the regional disk, the application-specific regional control plane of your HA service architecture can automatically initiate failover to the standby instance in the secondary zone. During the failover, the application-specific regional control plane reattaches the regional disk to the standby instance in the secondary zone. Compute Engine then directs all traffic to that instance based on health check signals.

The overall failover latency, excluding failure-detection time, is the sum of the following latencies:

  * Less than 1 minute to attach a regional disk to a standby instance
  * Time required for application initialization and crash recovery



For more information, see [Understanding the application-specific regional control plane](https://docs.cloud.google.com/compute/docs/disks/design-considerations-for-resilient-workloads-with-regional-persistent-disks#understanding_the_application-specific_regional_control_plane).

The [Disaster Recovery Building Blocks](https://docs.cloud.google.com/architecture/dr-scenarios-building-blocks) page covers the building blocks available on Compute Engine.

### Failover by force-attach

One of the benefits of Regional Persistent Disk and Hyperdisk Balanced High Availability is that in the unlikely event of a zonal outage, you can manually failover your workload to another zone. When the original zone has an outage, you can't complete the disk detach operation until that zonal replica is restored. In this scenario, you might need to attach the secondary zonal replica to a new compute instance without detaching the primary zonal replica from your primary instance. This process is called _force-attach_.

When your compute instance in the primary zone becomes unavailable, you can force attach your disk to an instance in the secondary zone. To perform this task, you must do one of the following:

  * Start another compute instance in the same zone as the regional disk replica that you are force attaching.
  * Maintain a hot standby compute instance in that zone. A _hot standby_ is a running instance that is identical to the one in the primary zone. The two instances have the same data.



Compute Engine executes the force-attach operation in less than one minute. The total [recovery time objective (RTO)](https://wikipedia.org/wiki/Recovery_time_objective) depends not only on the storage failover (the force attachment of the regional disk), but also on other factors, including the following:

  * Whether you must first create a secondary instance
  * The length of time that it takes the underlying file system to detect a hot-attached disk
  * The recovery time of the corresponding applications



For more information about how to failover your compute instance using force-attach, see [Failover your regional disk using `force-attach`](https://docs.cloud.google.com/compute/docs/disks/repd-failover#force-attach).

Regional Persistent Disk and Hyperdisk Balanced High Availability favor workload availability, which means there are tradeoffs for data protection in the unlikely event that both disk replicas are unavailable at the same time. For more information, see [Manage failures for regional disks](https://docs.cloud.google.com/compute/docs/disks/repd-failover). 

## Limitations

The following sections list the limitations that apply for Regional Persistent Disk and Hyperdisk Balanced High Availability.

### General limitations for regional disks

  * You can attach regional Persistent Disk only to VMs that use [E2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#e2_machine_types), [N1](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_machines), [N2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_machines), and [N2D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2d_machines) machine types.
  * You can attach Hyperdisk Balanced High Availability only to [supported machine types](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha#machine-series-support). 
  * You can't create a regional disk by cloning a Hyperdisk ML or Hyperdisk Throughput disk. You must create a snapshot of the source disk and then create a Hyperdisk Balanced High Availability disk from the snapshot. For more information, see [Change a zonal disk to a Hyperdisk Balanced High Availability disk.](https://docs.cloud.google.com/compute/docs/disks/migrate-to-hyperdisk#migrate-to-hdbha)
  * When using read-only mode, you can attach a regional Balanced Persistent Disk to a maximum of 10 VM instances.
  * The minimum size of a regional Standard Persistent Disk is 200 GiB.
  * You can only increase the size of a regional Persistent Disk or Hyperdisk Balanced High Availability volume; you can't decrease its size.
  * Regional Persistent Disk and Hyperdisk Balanced High Availability volumes have different performance characteristics than their corresponding zonal disks. For more information, see [About Persistent Disk performance](https://docs.cloud.google.com/compute/docs/disks/performance) and [Hyperdisk Balanced High Availability performance limits](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha#perf-limits). 
  * You can't use a Hyperdisk Balanced High Availability volume that's in multi-writer mode as a boot disk.
  * If you create a replicated disk by cloning a zonal disk, then the two zonal replicas aren't fully in sync at the time of creation. After creation, you can use the regional disk clone within 3 minutes, on average. However, you might need to wait for tens of minutes before the disk reaches a fully replicated state and the [ recovery point objective (RPO)](https://wikipedia.org/wiki/Recovery_point_objective) is close to zero. Learn how to [ check if your replicated disk is fully replicated](https://docs.cloud.google.com/compute/docs/disks/monitor-regional-persistent-disk-replica-state#determine_repd_replication_state).
  * You can't create regional disks in [AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones).
  * Creating a regional disk from an image has the following limitations: 
    * When you create a regional disk from an image, you can create one disk within a project every 5 minutes. You can issue up to 5 requests at once but you can't create more than 5 disks within a 25-minute period. 
    * Creating a regional disk from an image is in [Preview](https://cloud.google.com/products#product-launch-stages), and is slower than creating a zonal disk from an image. 



### Limitations for replica recovery checkpoints

  * A replica recovery checkpoint is part of the device metadata and doesn't show you any disk data by itself. You can only use the checkpoint as a mechanism to create a snapshot of your degraded disk. After you create the snapshot by using the checkpoint, you can use the snapshot to restore your data. 
  * You can create snapshots from a replica recovery checkpoint only when your disk is degraded. 
  * Compute Engine refreshes the replica recovery checkpoint of your disk only when the disk is fully replicated. 
  * Compute Engine maintains only one replica recovery checkpoint for a disk and only maintains the latest version of that checkpoint. 
  * You can't view the exact creation and refresh timestamps of a replica recovery checkpoint. 
  * You can create a snapshot from your replica recovery checkpoint only by using the Compute Engine API. 



## What's next

  * Learn how to [build high availability services using regional disks](https://docs.cloud.google.com/compute/docs/disks/high-availability-regional-persistent-disk).
  * Review the [disaster recovery planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide).
  * Learn about [disk pricing](https://cloud.google.com/compute/disks-image-pricing).
  * Learn how to [create and manage regional disks](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk).
  * Learn how to [monitor the replica states of disks](https://docs.cloud.google.com/compute/docs/disks/monitor-regional-persistent-disk-replica-state).
  * Learn how to [determine the replication state of a disk](https://docs.cloud.google.com/compute/docs/disks/monitor-regional-persistent-disk-replica-state#determine_repd_replication_state).
  * Learn how to [manage failures for regional disks](https://docs.cloud.google.com/compute/docs/disks/repd-failover).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
