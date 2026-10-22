---
url: https://docs.cloud.google.com/compute/docs/disks/async-pd/failover-failback/
title: Failover and failback asynchronous disks \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:14.242060+00:00
---

# Failover and failback asynchronous disks  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/async-pd/failover-failback/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Failover and failback asynchronous disks Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to failover and failback Asynchronous Replication disks.

In the event of an outage in the primary region, it is your responsibility to identify the outage and failover restart your workload using the secondary disks, in the secondary region. Asynchronous Replication doesn't offer outage monitoring. You can identify an outage using [RPO metrics](https://docs.cloud.google.com/compute/docs/disks/async-pd/performance#monitor_rpo), [health checks](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts), application-specific metrics, and by contacting Cloud Customer Care.

Following a failover from the primary region to the secondary region, the secondary region becomes the acting primary region.

After the outage or disaster gets resolved, you can initiate failback to start replication from the original secondary region (the acting primary region) to the original primary region. You can optionally repeat the process to move the workload back to the original primary region. Moving the workload back to the original primary region isn't strictly necessary, but can be done based on disaster recovery requirements, such as locality or available resources.

To learn more about failover and failback, see [About Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about#failover_and_failback).

## Failover to the secondary region

When you identify that a disaster has occurred, initiate failover to the secondary region. A failover moves the workload from the primary region to the secondary region. After the failover, the secondary disk is the acting primary disk and the secondary region is the action primary region.

You can failover a single disk, or all disks in a consistency group.

###  Single disk 

To failover a single disk, do the following:

  1. [Stop disk replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-replication#stop_replication_for_a_single_disk).
  2. If you don't already have a VM in the same region as the secondary disk, [create one](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).
  3. Attach the secondary disk to the VM:

     * For secondary boot disks, [update the boot disk for the VM](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk#update_a_boot_disk_for_an_instance).
     * For secondary data disks, [add the disk to the VM](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk#create_disk).

The secondary disk is now the workload's acting primary disk and the secondary region is the acting primary region.




###  Consistency group

To failover a consistency group, do the following:

  1. [Stop consistency group replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-replication#stop_replication_for_a_consistency_group).
  2. If you don't already have VMs in the same region as the secondary disks, [create them](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).
  3. Attach the secondary disks to the VMs:

     * For secondary boot disks, [update the boot disk for the VM](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk#update_a_boot_disk_for_an_instance).
     * For secondary data disks, [add the disk to the VM](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk#create_disk).



## Failback to the original primary region

After a disaster has resolved, initiate a failback to the original primary region. A failback configures and starts replication from the acting primary disk to a new secondary disk in the acting secondary region.

You can failback a single disk, or all disks in a consistency group.

###  Single disk 

To failback a single disk, do the following:

  1. [Create a secondary disk](https://docs.cloud.google.com/compute/docs/disks/async-pd/configure#create_a_secondary_disk) in the acting secondary region. The acting secondary region is the original primary region.
  2. [Start replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-replication#start_replication) from the acting primary disk to the new secondary disk.
  3. Optional: Move the workload from the acting primary region to the original primary region by doing the following:

     1. Wait for the initial replication to complete. The initial replication is complete when the [`disk/async_replication/time_since_last_replication` metric](https://docs.cloud.google.com/compute/docs/disks/async-pd/performance#monitor_rpo) is available in Cloud Monitoring. If you don't see the RPO metric in Cloud Explorer, that means the initial replication isn't complete.
     2. Recommended: To avoid data loss, schedule downtime for the workload and bring the workload offline.
     3. [Stop replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-replication#stop_replication_for_a_single_disk).
     4. Attach the secondary disk to a VM:

        * For secondary boot disks, [update the boot disk for the VM](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk#update_a_boot_disk_for_an_instance).
        * For secondary data disks, [add the disk to the VM](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk#create_disk).

The secondary disk is now the workload's primary disk in the original primary region.

     5. Reconfigure replication in the original primary region by doing the following:

        1. [Create a new secondary disk](https://docs.cloud.google.com/compute/docs/disks/async-pd/configure#create_a_secondary_disk) in the original secondary region.
        2. [Start replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-replication#start_replication) from the primary disk to the new secondary disk.



###  Consistency group 

To failback a consistency group, do the following:

  1. [Create a new consistency group in the acting primary region](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-consistency-groups#create_a_consistency_group). The acting primary region is the original secondary region.
  2. [Add the acting primary disks to the consistency group](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-consistency-groups#add_a_disk_to_a_consistency_group)
  3. [Create secondary disks](https://docs.cloud.google.com/compute/docs/disks/async-pd/configure#create_a_secondary_disk) in the acting secondary region that reference the acting primary disks.
  4. [Start replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-replication#start_replication).
  5. Optional: Move the workload from the acting primary region to the original primary region by doing the following:

     1. Wait for the initial replication to complete. The initial replication is complete when the [RPO metric is available.](https://docs.cloud.google.com/compute/docs/disks/review-disk-metrics#performance_metrics). If you don't see the RPO metric in Cloud Explorer, that means the initial replication isn't complete.
     2. Recommended: To avoid data loss, schedule downtime for the workload and bring the workload offline.
     3. [Stop replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-replication#stop_replication_for_a_consistency_group).
     4. Attach the secondary disk to VMs:

        * For secondary boot disks, [update the boot disk for the VM](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk#update_a_boot_disk_for_an_instance).
        * For secondary data disks, [add the disk to the VM](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk#create_disk).

The secondary disks are now the workload's primary disks in the original primary region.

     5. Reconfigure replication in the original primary region by doing the following:

        1. [Add the primary disks to the original consistency group](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-consistency-groups#add_a_disk_to_a_consistency_group).
        2. [Create new secondary disks](https://docs.cloud.google.com/compute/docs/disks/async-pd/configure#create_a_secondary_disk) in the original secondary region.
        3. [Start replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-replication#start_replication).



## What's next

  * Learn how to [monitor Asynchronous Replication performance](https://docs.cloud.google.com/compute/docs/disks/async-pd/performance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
