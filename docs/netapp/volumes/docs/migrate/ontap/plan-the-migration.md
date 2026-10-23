---
url: https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/plan-the-migration/
title: Plan the migration \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:29.777283+00:00
---

# Plan the migration  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/plan-the-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Plan the migration Stay organized with collections  Save and categorize content based on your preferences. 

This page provides details about how to plan your migration.

## Estimate migration duration for a single volume

The volume migration duration is affected by several factors:

  * **Speed of your source volume** : SnapMirror traffic has a lower priority than NFS and SMB traffic. High workloads on your source volume can reduce the performance of the outgoing SnapMirror traffic.

  * **NetApp Volumes throughput** : defined by the service level and specific volume throughput capability. NFS or SMB traffic on the volume might also reduce SnapMirror performance.

  * **Network connection throughput** : SnapMirror tries for maximum speed and might consume bandwidth shared with other users on the network connection between the source ONTAP system and NetApp Volumes.

  * **Amount of data used in the source volume** : the larger data volumes require more time to transfer.

  * **Source volume data change rate** : a higher rate of data changes during the migration process increases the time needed for incremental transfers to synchronize.




A rough estimate of the migration duration can be calculated with a rule-of-thumb.

**Example**

Consider the following scenario for migration duration calculation:

  * **Source volume** : 15 TiB capacity with 12 TiB of data used.

    * Data to transfer: 12 TiB.

    * ONTAP storage efficiency can reduce the transfer size, but you can ignore that for this exercise.

    * Assume performance capabilities aren't a limiting factor.

  * **Change rate** : 10% per day.

    * Daily data change rate: 1.2 TiB.

    * 10% is an assumption for this example; typical change rates are usually much lower.

  * **Network connection** : On-premises infrastructure is connected to Google using a 10 Gbps interconnect.

    * Effective TCP bandwidth: approximately 1000 MiBps, which can be exclusively used.
  * **Destination volume** : 12 TiB volume with a Premium service level.

    * Throughput cap: 12 × 64 MiBps = 768 MiBps.



**Calculation**

In this example, the limiting factor is the destination volume's throughput cap of 768 MiBps. The source volume's performance is considered _unlimited_ , and network bandwidth is 1000 MiBps.

**Note:** This calculation represents a best-case scenario. Actual times might vary due to network conditions and other factors.

**Baseline transfer**

  * Data to transfer: 12 TiB

  * Throughput cap: 768 MiBps

  * Time calculation: (12 TiB x 1024^2 MiB/TiB) / 768 MiBps = 16384 seconds

  * Total time for baseline transfer: 4.6 hours




**First incremental transfer**

  * Time elapsed since baseline transfer: 5 hours

  * Data change: (12 TiB x 1024 GiB/TiB) * 10% * (5h/24h) = 256 GiB

  * Time calculation:(256 GiB x 1024 MiB/GiB) / 768 MiBps = 341 seconds

  * Total time for first incremental transfer: ~6 minutes




**Second incremental transfer**

  * Time elapsed since first incremental transfer: 1 hour

  * Data change: (12 TiB x 1024 GiB/TiB) * 10% * (1h/24h) = 51.2 GiB

  * Time calculation: (51.2 GiB x 1024 MiB/GiB) / 768 MiBps = 68 seconds

  * Total time for second incremental transfer: ~70 seconds




**Subsequent incremental transfers**

After the first incremental transfer, all subsequent transfers typically take less than one hour. Following the second incremental transfer, all subsequent transfers will take approximately the same amount of time.

**Cutover process**

Start the cutover process shortly after an incremental transfer completes to minimize the accumulation of changed data.

Total migration time: approximately 4.7 hours.

## Run multiple migrations or external replications in parallel

Volume migrations and external replications are managed in the API as two variations of a _hybrid replication_ and consume the same Google project quota.

The number of configured hybrid replications is limited by a region-specific project quota, which is set to `1` by default. You can request a higher quota using [Google Cloud console](https://console.cloud.google.com/iam-admin/quotas) for the NetApp Volumes API. The following are the relevant quotas:

  * `netapp.googleapis.com/standard_hybrid_replicated_volumes_per_region`

  * `netapp.googleapis.com/hybrid_replicated_volumes_per_region`




If you need to migrate more volumes than your current quota allows, you must perform these operations sequentially. It is recommended to group volumes that belong to the same workload into batches for simultaneous migration, which also helps in cutting them over together.

For external replication, your project quota must be sufficient to accommodate all configured external replications, in addition to any potential volume migrations.

**Note:** Running multiple migrations or replications in parallel might over-utilize shared resources, such as a Google interconnect used for migration or replication. This can result in increased migration durations or make replications skip their scheduled replication intervals.

## What's next

[Prerequisites for ONTAP and NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/prerequisites-ontap-netapp-volumes).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
