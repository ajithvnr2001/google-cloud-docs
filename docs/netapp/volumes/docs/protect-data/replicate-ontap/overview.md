---
url: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/replicate-ontap/overview/
title: External replication overview \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:58.644864+00:00
---

# External replication overview  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/replicate-ontap/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  External replication overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the external replication feature.

## About external replication

**Note:** For Standard, Premium, and Extreme service levels, this feature is available in allow-listed General Availability (GA) and isn't open by default. To request access to this feature, contact [sales](https://cloud.google.com/contact).

You can manage replication between ONTAP and Flex Unified ONTAP-mode volumes, which is similar to ONTAP to ONTAP replication. However, the instructions in this document don't apply to this type of replication. For more information, see [ONTAP-mode](https://docs.cloud.google.com/netapp/volumes/docs/ontap/overview) and [Learn about ONTAP SnapMirror asynchronous disaster recovery](https://docs.netapp.com/us-en/ontap/data-protection/snapmirror-disaster-recovery-concept.html#data-protection-relationships).

Flex Unified ONTAP-mode storage pools can act as ONTAP source systems to establish a replication between ONTAP-mode pools and service level pools.

External replication uses SnapMirror to replicate data from ONTAP-based systems to Google Cloud NetApp Volumes. This feature supports the same operations such as create, stop, resume, reverse, and delete as [volume replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-volume-replication), which offers replication between volumes within NetApp Volumes.

External replication uses the same SnapMirror technology as [volume migration](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/overview#about_volume_migration) and shares common features such as baseline and incremental transfers, and cluster peering for authentication.

The following table describes the key differences between volume migration and external replication:

Volume migration | External replication  
---|---  
Designed for a time-limited, unidirectional migration from ONTAP to NetApp Volumes. | Designed as an ongoing replication solution for disaster recovery, where the replication direction can be reversed.  
  
## Overview of external replication workflow

External replication functions similarly to [volume replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-volume-replication), but the initial source system is a volume on an external ONTAP system, not a NetApp Volumes volume.

Like volume replication, external replication goes through various phases like baseline and incremental replications. It supports operations such as creating, stopping, resuming, deleting, and reversing the replication direction.

While all actions can be initiated from NetApp Volumes, some of the actions require the user to run ONTAP CLI commands on the external ONTAP system. External replication also uses the same authentication mechanism with the external ONTAP system as [volume migration](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/overview#about_volume_migration), a process that is required to establish a cluster peering.

The external replication workflow consists of the following phases:

  1. Authentication

  2. Baseline transfer

  3. Incremental transfers




### Authentication

During the authentication phase, the storage administrators of the source ONTAP system must grant NetApp Volumes permission to fetch a volume from the source system. This is achieved through administrative steps on the source ONTAP system, called [_cluster peering_](https://docs.netapp.com/us-en/ontap/peering/peering-basics-concept.html) and _SVM peering_. The external replication process generates the ONTAP commands that administrators must run on the source system.

### Baseline transfer

After you set up a replication, a snapshot creates a consistency point on the source system. All data captured from this snapshot, including older snapshots, is then transferred to NetApp Volumes during an initial phase called a _baseline transfer_.

A baseline transfer can take minutes, hours, days, or weeks. This duration depends on the following:

  * The amount of data in the snapshot.

  * The network speed between your ONTAP source system and NetApp Volumes.

  * The throughput setting of your NetApp Volumes.




During the baseline transfer, your source volume continues to serve your workload and data is added, changed, or deleted by clients. These changes don't affect the snapshot used for the baseline's consistency point. While the baseline is in progress, the destination volume isn't available to clients. After the baseline completes, the destination volume becomes online and available for client access in read-only mode. Note that the destination volume will have a different IP address.

Unlike volume replication, external replication can't read the source volume parameters such as size, protocol choices, and export or snapshot policies. Therefore, you must configure these settings correctly for the destination volume.

Clients can then map or mount the destination volume but just for read-only operation.

### Incremental transfers

After the baseline transfer completes, the replication triggers incremental transfers based on your scheduled intervals.

Each incremental transfer performs the following actions:

  1. Takes a new snapshot of your source volume.

  2. Calculates the data changes between the current and the previous snapshots.

  3. Starts transferring these changes to the destination.




Each incremental transfer creates a new source snapshot, deletes the oldest SnapMirror snapshot, calculates the changes, and transfers them. If a transfer is still running when the next scheduled transfer is due, the new transfer is skipped. This can occur if the volume of data changes exceeds what can be transferred within the specified interval, due to the following factors:

  * The specified replication interval is too short.

  * Limited network bandwidth between the ONTAP system and the NetApp Volumes.

  * A high change rate on the source system.




Skipped transfers negatively impact recovery point objectives (RPO). We recommend monitoring the lag time of the replication. If the lag frequently reaches twice the replication interval, you might have to take countermeasures such as increasing network bandwidth or extending the replication interval.

Clients that mount the destination volume see a read-only view with static content. However, once an incremental transfer is complete, the volume's contents are instantly updated from the previous replication snapshot to the latest one in a single, atomic operation.

## Running multiple external replications in parallel

External replications and volume migrations share a common project quota. To [run multiple external replications and volume migrations in parallel](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/plan-the-migration#run_multiple_migrations_or_external_replications_in_parallel), you must request a sufficient high quota.

## What's next

[Create an external replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/replicate-ontap/create-external-replication).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
