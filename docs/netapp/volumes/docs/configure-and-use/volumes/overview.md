---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/overview/
title: Volumes overview \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:29.678528+00:00
---

# Volumes overview  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Volumes overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the volumes feature of Google Cloud NetApp Volumes. The volume instructions provided on this page don't apply to Flex Unified ONTAP-mode. You can't create, view, update, or delete ONTAP-mode volumes using the Google Cloud console or Google Cloud CLI. For more information about ONTAP-mode instructions, see [ONTAP-mode](https://docs.cloud.google.com/netapp/volumes/docs/discover/features#ontap-mode).

## About volumes

A volume is a file system container in a storage pool that stores application, database, and user data.

You create a volume's capacity using the available capacity in the storage pool and you can define and resize the capacity without disruption to your processes.

Storage pool settings apply to the volumes contained within them automatically. These settings include the service level, location, network (Virtual Private Cloud (VPC)), Active Directory policy, LDAP, and the customer-managed encryption key (CMEK) policy. Also, to use auto-tiering on a volume, you must enable it on the pool.

For ONTAP-mode, you must configure Active Directory policy and LDAP settings directly in ONTAP, not at the storage pool level.

## Volume performance

**Flex Unified and Flex File with custom performance storage pools** : the performance of a volume depends on the performance configured on its storage pool. The pool performance is shared between all volumes in the pool.

**Flex File storage pools with default performance** : the performance of a volume depends on the size and capabilities of its storage pool. The pool performance is shared between all volumes in the pool.

**Standard storage pools** : the volume's performance is defined by the volume size and the service level it inherits from the pool. Every GiB of volume capacity adds 16 KiBps of throughput. The volume size can be increased or decreased to optimize performance.

**Premium and Extreme storage pools** : the volume's performance is defined by the volume size and the service level it inherits from the pool. Every GiB of volume capacity adds 64 KiBps or 128 KiBps of throughput. The volume size can be increased or decreased to optimize performance. Additionally, you can move a volume non-disruptively between Premium and Extreme pools to optimize performance.

## Space provisioning

Volumes must have enough capacity to store your data, including future growth. Depending on how much data you add each day and how quickly your organizational processes let you increase a volume's size, plan for enough headroom.

If a volume becomes full, clients receive an `out of space` error when they try to modify or add data, which can lead to problems for your applications or users. You should monitor usage of your volumes and maintain a provisioned space buffer of 20% above your expected volume utilization. For more information about monitoring usage, see [Monitor NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/monitor/monitor-volume-usage).

Snapshots consume the volume's capacity. When snapshots exist, you might delete data, but the volume's space utilization doesn't decrease. This happens because the data in your active file system counts toward a snapshot, which also contributes to the volume's used capacity. Space becomes available only after you delete the last snapshot that contains that data. For more information, see [Snapshot space use](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/overview#snapshot_space_use_example).

For Standard, Premium, and Extreme service levels, the size of the volume also determines the allocated throughput capability. For more information, see [Standard, Premium, and Extreme performance](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/volume-performance-sizing#standard_premium_and_extreme_performance).

### Billing: logical versus physical capacity

NetApp Volumes bills you for [logical capacity](https://docs.cloud.google.com/netapp/volumes/docs/discover/features#billing), not physical capacity. This billing model applies to your storage pools and volumes as follows:

  * You're billed for the capacity that you provision for the storage pool that hosts the volume.

  * The used space in your volume includes the data blocks that store user data, file system metadata, and snapshot data.




## Volume user and group quotas

For the Standard, Premium, Extreme, and Flex Unified default-mode service levels, you can limit volume space used by specific users or groups. Note that these are different from Google Cloud Quotas and system limits. You set user and group quotas directly on a NetApp Volumes volume. For more information about quota rules, see [Manage quota rules](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-quota-rules).

For ONTAP-mode, quotas must be defined at the ONTAP level. Google supports quota management for ONTAP-mode storage pools, but not for ONTAP-mode volumes.

Quotas can be set for individual Windows or Unix users, or Unix groups, but not for Windows groups. Quotas target the specific user IDs (UID), security identifier (SID), or group IDs (GID) for the user or group, not the name.

Quotas are intended to limit usage, not to allocate storage for a user's usage. Quota limits are checked in sequential order, starting with user quotas and then group quotas. When quota limits are reached, writes are blocked. Group quotas are shared by all users in the group. For more information about how to manage quota rules, see [Manage quota rules](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-quota-rules).

**Warning:** If you decide to use both user and group quotas together, writes will be blocked if any limit is reached.

For example, three groups HR, Finance, and Management share a 10 TiB volume. The default group quota is 500 GiB which limits HR and Management group users, and Finance has a 10 TiB group quota. The default user quota is 1 TiB. Users Sasha in Finance and Alex in Management are assigned an individual user quota of 5 TiB. The following are some examples of the effective quota for specific users:

  * Users Kim in HR, Taylor, and Alex in Management are limited to a 500 GiB group quota. Alex's 5 TiB user quota is effectively overridden by the group quota.

  * User Sasha in Finance is limited by the user quota to 5 TiB.

  * User Lee in Finance is limited by the user quota to 1 TiB.

  * No one in Finance has a user quota greater than 5 TiB, thus none can individually store up to the 10 TiB group quota.




When users try to write beyond the quota limit, they will receive an error. User quota consumption and limits are visible to the user in Windows Explorer or Linux quota command. The group quota consumption and limits are only visible when using an rquota v2 compatible client.

There are four types of quota rules:

  * **Individual user quota** : applies to explicit user using Linux UID or Windows SID

  * **Individual group quota** : applies to explicit group using Linux GID without Windows support

  * **Default user quota** : applies to every user without an individual quota rule

  * **Default group quota** : applies to every group without an individual quota rule




## Volume reversion

NetApp Volumes lets you revert volumes to a previously created snapshot. When you revert a volume, it restores all volume contents back to the point in time the snapshot was taken. Any snapshot created after the snapshot used for the reversion is lost. If you don't want to lose data, we recommend that you clone a volume or restore data with snapshots instead.

You can use volume reversion to test and upgrade applications or fend off ransomware attacks. The process is similar to overwriting the volume with a backup, but only takes a few seconds. You can revert a volume to a snapshot independent of the capacity of the volume.

Reversions happen when the volume is online and in use by clients. We recommend stopping all critical applications before you revert to avoid potential data corruption because the reversion changes open files without any notification to the application.

## Block volume from deletion when clients are connected

NetApp Volumes lets you block the deletion of volumes when they are mounted by a client. If you use volumes for Google Cloud VMware Engine (GCVE) datastores, you must enable the setting to block the deletion of volumes when clients have mounted volumes. If you enable **Block volume from deletion when clients are connected** setting, an error message displays when you try to delete a mounted volume.

Volumes support blocking the deletion of volumes when you create a volume, create a new volume from a snapshot, and create a new volume from a backup.

The following protocols support blocking the deletion of volumes:

  * NFSV3

  * NFSV4.1

  * NFSV3 and NFSV4.1

  * iSCSI




To delete an NFS volume when this option is enabled, unmount the datastore from all clients. After that, you must wait for more than 52 hours to delete the volume. To delete an iSCSI volume, unmount the virtual machine file system (VMFS) datastore from all clients and disconnect the volume from the host group. You can then delete the iSCSI volume.

## Large capacity volumes

**Note:** The large capacity volumes feature is generally available (GA) for Flex Unified service level for NFS and SMB volumes. The Flex Unified service level with limited performance doesn't support large capacity pools.  
  
For Premium and Extreme service levels, this feature is available in allow-listed General Availability (GA) and isn't open by default. To request access to this feature, contact [sales](https://cloud.google.com/contact).

Normal volumes in Premium and Extreme service levels allow volume sizes between 100 GiB and 102,400 GiB and maximum throughput of up to 4.5 GiBps. The Flex Unified service level supports volume sizes between 1 GiB and 300 TiB and maximum throughput of up to 5 GiBps. Some workloads require larger volumes and higher throughput, which can be achieved by using the large capacity volume option for these service levels.

Large capacity volumes let you scale storage capacity and performance to much higher levels. They use multiple IP addresses to distribute clients across endpoints and balance the workload. These volumes are ideal for workloads that require high performance and highly concurrent access to the same data. For recommendations on how to connect your clients, see [Connect large capacity volumes with multiple storage endpoints](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-large-capacity-volumes).

The default quota for storage pool is 25 TiB per location. Most large volumes need more capacity, so you must request an increase to your Storage pool capacity (GiB) per location quota. For more information, see [NetApp Volumes quotas](https://docs.cloud.google.com/netapp/volumes/docs/quotas).

Volumes can't be converted into large capacity volumes and the other way around after creation.

The following service levels support large volumes:

  * Flex Unified Default-mode

  * Flex Unified ONTAP-mode

  * Premium and Extreme




### Flex Unified Default-mode

Large capacity volumes are available only in large capacity storage pools. Limited performance pools don't support them.

A large capacity volume consists of smaller member volumes called constituents. These constituents share the volume's storage capacity and performance. Each constituent has its own storage endpoint to let clients distribute traffic across multiple IP addresses.

A large capacity volume includes 48 constituents by default. Each constituent must be at least 100 GiB, so the minimum default volume capacity is 4,800 GiB. The maximum capacity is 2.48 PiB, or 20 PiB when auto-tiering is enabled.

When using a custom number of constituents, you can select a minimum of two. In this configuration, the minimum volume size is 2,400 GiB, with each individual constituent requiring at least 100 GiB. Additionally no constituent can exceed the size of the aggregate in which it is stored.

A large capacity pool distributes data across six aggregates, so the maximum capacity of a constituent is about one-sixth of the pool capacity. For example, in a 6 TiB pool, each aggregate stores about 1,024 GiB, so each constituent is limited to about that capacity.

You set the number of constituents when you create the volume, and this setting can't be changed later.

You can increase or decrease the capacity of a large volume in 1 GiB increments. After you change the capacity, the system redistributes capacity across the existing constituents.

### Flex Unified ONTAP-mode

You can create large capacity volumes in Flex Unified ONTAP-mode using regular or large capacity pools. ONTAP FlexGroup [creation rules](https://docs.netapp.com/us-en/ontap/flexgroup/create-task.html) are applicable.

### Premium and Extreme

Large capacity volumes in Premium or Extreme pools must be allow-listed before use. You can then create large capacity volumes in any Premium or Extreme pool.

Large capacity volumes must be between 15 TiB and 3 PiB. You can increase or decrease the capacity in 1 GiB increments. Large capacity volumes support throughput of up to 30 GiBps.

## Auto-tiering

Google Cloud NetApp Volumes lets you enable auto-tiering on a per-volume basis if auto-tiering is enabled on the storage pool. Auto-tiering reduces the overall cost of volume usage by moving unused data to a cold data tier. For more information about auto-tiering, see [Manage auto-tiering](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-auto-tiering).

## What's next

[Create a volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/create-volume).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
