---
url: https://docs.cloud.google.com/netapp/volumes/docs/discover/how-it-works/snapshots-and-snapshot-based-data-management/
title: Snapshots and snapshot-based data management \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:12:26.785688+00:00
---

# Snapshots and snapshot-based data management  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/discover/how-it-works/snapshots-and-snapshot-based-data-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)



Send feedback 

#  Snapshots and snapshot-based data management Stay organized with collections  Save and categorize content based on your preferences. 

NetApp Volumes helps you manage your data usage by using snapshot capabilities. 

Unlike Google persistent disk snapshots, NetApp Volumes snapshots aren't a separate physical copy of your data. NetApp Volumes use just-in-time copy-on-write so that any unmodified files in snapshots do not consume any of the volume's capacity. Note that overwriting all data causes the snapshot to consume significant volume capacity which needs to be factored into provisioning volume capacity.

### Snapshot attributes

Snapshots have many attributes, such as the following:

  * **Instant capture.** Snapshots instantly capture data within a volume at an exact point in time.

  * **Unchanged performance.** Using snapshots doesn't affect the performance of the volume.

  * **Space efficient.** A fresh snapshot only consumes a small amount of metadata. When existing data is overwritten, old data blocks are retained as long as any snapshot pointing to these data blocks exists. In other words, deleted or modified data still referenced by a snapshot consumes extra space in the volume. When the last snapshot referencing a data block is deleted, the block becomes available.

  * **Readable as a file system.** You can easily access snapshots, which are read-only, through standard file system interfaces. You can access all snapshots of different point-in-time versions of the volume and read their content. 

  * **Can be used for fast clones.** You can create new volumes from any snapshot stored in the same region. Creating a new volume from a snapshot takes the same amount of time as creating a new empty volume independent of the volume or snapshot size. For example, a 100 TiB volume can be cloned within a few seconds. The clone is a new volume and is charged for its capacity.

  * **Quick reversions back to a snapshot.** Within minutes, you can restore a volume to a snapshot version regardless of the volume size. Changes made to volumes after snapshot creation are undone. This includes newer snapshots.

  * **Cost efficient.** Snapshots offer a complete view of multiple point-in-time versions of the volume while only requiring extra capacity for the changed data. Snapshot capacity is counted towards the used space of a volume.




### Use cases

The following section describes scenarios where you can use snapshots to address data management challenges.

  * **Application cloning:** Utilize the snapshot and application cloning feature to allow more test iterations at faster speeds independent of clone size and data structure. 

  * **Volume backup and recovery:** NetApp Volumes uses snapshots to instantaneously recover individual files or directories if data is corrupted or deleted while only consuming space for modified data. To learn more about snapshots, see Snapshots.

  * **Data versioning:** Snapshots help you keep multiple versions of the same dataset accessible, and only changed data consumes extra capacity.

  * **Application and data upgrades:** NetApp Volumes takes an instant snapshot of your data to ensure that a current version of your data is captured before you implement an upgrade in case the upgrade causes an application to break. If the upgrade succeeds and causes no issues, you can delete the snapshot. If the upgrade fails, you can use the snapshot to quickly recover individual files, or simply revert the entire volume to its previous state before the upgrade.

  * **Ransomware protection:** NetApp Volumes helps defend against data loss from ransomware attacks. Because snapshots are read-only and can't be encrypted, they help defend against unwanted data encryption or deletion from a compromised VM which might have the volume mounted. In the event of a large data loss or compromise, you can use a snapshot to revert an entire volume back to an older state in seconds. 

You can create a usable volume clone from an older snapshot in order to resume operations until your data is investigated for changes or corruptions following a ransomware attack. Both options make all your data usable within minutes.

  * **Application-consistent recovery points:** You can use NetApp Volumes to take crash-consistent snapshots, which are snapshots of your data which may not contain the latest changes due to client caching. You can also opt to take application-consistent snapshots, which are snapshots taken after the operating system and application write the current state of the data to storage. Application-consistent snapshots provide a clear recovery point for the application and can be used to create a consistent clone of the application. 

Crash-consistent snapshots can also be used to recover data, which works well for a majority of applications, however, some data in storage might not be current at the time of recovery because it's kept in operating system and application caches for some time before it's written to storage.

  * **Logical space use:** NetApp Volumes space usage reflects data in the active file system and deleted blocks that are retained by snapshots. Retained snapshot blocks are freed as soon as the last snapshot that references the blocks is deleted. The logical space used, including any deleted data retained by snapshots, consumes provisioned space of your volume. For more information, see Manage volume snapshots. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
