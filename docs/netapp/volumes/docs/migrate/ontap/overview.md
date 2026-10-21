---
url: https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/overview/
title: Volume migration overview \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:38.018701+00:00
---

# Volume migration overview  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Volume migration overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the volume migration feature.

## About volume migration

**Note:** For the Standard, Premium, and Extreme service levels, this feature is available in allow-listed General Availability (GA) and isn't open by default. To request access to this feature, contact [sales](https://cloud.google.com/contact).

The volume migration feature lets you migrate volumes from ONTAP-based sources to Google Cloud NetApp Volumes using a SnapMirror-based migration. SnapMirror works on a per-volume level and can replicate a source volume to a destination volume on a different system.

SnapMirror offers many advantages over conventional data copy methods:

  * It operates over any IP network and is resilient to network issues, supporting a wide range of network speeds and latencies.

  * It copies only used data.

  * After an initial baseline data transfer, the subsequent transfers are incremental, copying only changed data indefinitely. The calculation of changes for incremental transfers is exceptionally fast and independent of the data type stored in the volume.

  * The transfers retain storage efficiency. If the source volume contains deduplicated or compressed data, these efficiencies are carried over, reducing the amount of data to transfer.

  * All transfers are encrypted in transit.

  * You can use the source volume without any noticeable performance impact.

  * You can use the destination volume in a read-only state after the baseline transfer is completed.

  * All data, including metadata such as complex access control lists (ACL) and locked files is transferred.




SnapMirror transfers volumes between ONTAP systems, even across different geographical locations.

Google Cloud NetApp Volumes uses SnapMirror for [volume replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-volume-replication) between NetApp Volumes in different Google regions. Additionally, you can use SnapMirror to replicate between external ONTAP-based volumes and NetApp Volumes, which is called _hybrid replication_.

Hybrid replications include two types:

  * Volume migration is intended for one-time transfers from ONTAP to NetApp Volumes.

  * [External replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/replicate-ontap/overview) is intended for ongoing disaster recovery replications where the replication direction can be reversed.




## Overview of migration process

Hybrid replication ensures fast, consistent, and complete data migrations from source to destination with minimum impact on your production. This process consists of the following phases:

  1. Authentication

  2. Baseline transfer

  3. Incremental transfers

  4. Cutover

  5. Cleanup




### Authentication

During the authentication phase, the storage administrators of the source ONTAP system must grant NetApp Volumes permission to fetch a volume from the source system. This is achieved through administrative steps on the source ONTAP system, called [_cluster peering_](https://docs.netapp.com/us-en/ontap/peering/peering-basics-concept.html) and _SVM peering_. The volume migration process generates the ONTAP commands that administrators must run on the source system.

### Baseline transfer

After you set up a migration, a snapshot creates a consistency point on the source system. All data captured from this snapshot, including older snapshots, is then transferred to NetApp Volumes during an initial phase called a _baseline transfer_.

A baseline transfer can take minutes, hours, days, or weeks. This duration depends on the following:

  * The amount of data in the snapshot.

  * The network speed between your ONTAP source system and NetApp Volumes.

  * The throughput setting of your NetApp Volumes.




During the baseline transfer, your source volume continues to serve your workload and data is added, changed, or deleted. These changes don't affect the snapshot used for the baseline's consistency point. While the baseline is in progress, the destination volume isn't available to clients. After the baseline completes, the destination volume becomes online and available for client access in read-only mode. Note that the destination volume will have a different IP address.

Unlike volume replication, volume migration can't read the source volume parameters such as size, protocol choices, and export or snapshot policies. Therefore, you must configure these settings correctly for the destination volume.

You can now start mounting or mapping the destination volume to VMs to prepare for the end of the migration.

### Incremental transfers

After the baseline transfer completes, the migration triggers hourly incremental transfers.

Each incremental transfer performs the following actions:

  1. Takes a new snapshot of your source volume.

  2. Calculates the data changes between the current and the previous snapshots.

  3. Starts transferring these changes to the destination.




If a significant volume of changes occur since the baseline snapshot, and an incremental transfer is still running when the next hourly transfer is scheduled, this transfer is skipped. The next incremental transfer captures a new source snapshot, deletes the oldest SnapMirror snapshot, calculates the changes, and transfers them.

Clients that mount the destination volume see a read-only view with static content. However, once an incremental transfer is complete, the volume's contents are instantly updated from the previous replication snapshot to the latest one through a single, atomic operation.

Unless the amount of new data added to the source volume exceeds what can be transferred within an hour, the size of the incremental transfer decreases with each successful transfer. This process continues until it stabilizes at a rate defined by the source volume's hourly change rate, which might take a few iterations. Once this steady state is reached, you can schedule a cutover. To minimize the required downtime during the cutover, the objective is to reduce the changes between the source and destination volumes.

### Cutover

During a cutover, you move your workloads from the source volume to the destination volume without data loss (RPO = 0) and minimal downtime (RTO). The cutover process consists of the following substeps:

  1. Stop modifications

  2. Wait for current transfer

  3. Perform a manual incremental transfer

  4. Stop replication

  5. Reconfigure and restart applications




#### Stop modifications

Since incremental transfers are asynchronous, your source volume might contain changes that are not yet reflected on the destination volume. To synchronize, stop all modifications on the source volume by:

  * Stopping all applications that modify data.

  * Optional: change the volume permissions to read-only to prevent any client from modifying the data.




#### Wait for current transfer

Make sure that any running incremental transfers are completed.

#### Perform a manual incremental transfer

Perform a manual incremental transfer to send the latest data to the destination system. This should take only a few seconds to minutes, depending on the volume of data changed since the last transfer, network speed, and the throughput limits of the destination volumes.

After the manual incremental transfer completes, the latest data is available at the destination.

#### Stop replication

Run the stop operation on the replication to make your destination volume read-writeable. This completes your data migration.

#### Reconfigure and restart applications

Reconfigure your applications to use the destination volume and then restart them. Make sure that all data access to the source volume is stopped to prevent any application from accidentally using the source volume.

### Cleanup

If the cutover is successful, you can perform the following cleanup steps:

  1. **Delete stopped replication** : when you delete the stopped replication, the replication resource is deleted but the destination volume isn't deleted. This process also deletes the SnapMirror relationship used in the backend with your source system.

  2. **Remove cluster peering** : if this was the last SnapMirror relationship between NetApp Volumes and your source cluster, you can remove the cluster peering from the source ONTAP system. Additionally, you can remove any networking configured only for migration purposes between the source and destination.




## What's next

[Plan the migration](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/plan-the-migration).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
