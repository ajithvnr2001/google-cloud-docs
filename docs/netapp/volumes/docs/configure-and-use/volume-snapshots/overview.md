---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/overview/
title: About volume snapshots \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:00.058337+00:00
---

# About volume snapshots  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  About volume snapshots Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the Google Cloud NetApp Volumes volume snapshots feature.

## About snapshots

NetApp Volumes helps you manage your data usage with snapshots that can quickly restore lost data. Snapshots are point-in-time versions of your volume's content. They are resources of volumes and are instant captures of your data that consume space only for modified data. Because data changes over time, snapshots usually consume more space as they get older.

**Important:** Snapshots aren't copies of your data. If you want to make copies of your data, consider using the NetApp Volumes backups or volume replication features. For more information, see [NetApp Volumes backups overview](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-volume-backups) and [NetApp Volumes volume replication overview](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-volume-replication).

## Considerations

Consider the following:

  * If you overwrite all of the data in a snapshot, then the snapshot consumes significant volume capacity, which factors into [provisioning volume capacity](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/overview#space_provisioning).

  * Volumes with a typical rate of change of 1-2% daily and typical [snapshot schedules](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/overview#snapshot_schedules) generally need an additional 20% of capacity for storing snapshots.




## Snapshot attributes

Snapshots have the following properties:

  * **Instant capture** : snapshots instantly capture data within a volume at an exact point in time.

  * **Space efficient** : snapshots consume a small amount of data by only overwriting modified or deleted data and maintain existing unchanged data.

  * **Readable as a file system** : all snapshots are accessible through standard file system interfaces as read-only files for each point in time.

  * **Quick clone creation** : you can clone a volume within seconds by creating a new volume from a snapshot.

For volumes with the Flex Unified service level, NetApp Volumes provides thin and thick clones. Thin clones are instantaneous, writable copies that initially share data blocks with the source volume and consume storage space only for new or modified data. While thick clones are independent copies of the volumes and don't have any shared data blocks with the source volume. For more information about cloning volumes, see [Volume clones](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-volume-clones).

For other service levels, it takes the same amount of time to create a new volume from a snapshot as it does to create a new empty volume independent of volume or snapshot size. The clone is a new volume and the storage pool needs sufficient free capacity to accommodate it.

  * **Fast restoration of snapshots** : within minutes, you can restore a volume to a snapshot version regardless of the volume size. Changes made to volumes after snapshot creation are undone, which includes newer snapshots.




## Types of snapshots

There are three types of snapshots:

  * **Manual snapshots** : snapshots you create and delete manually.

  * **Scheduled snapshots** : using scheduled snapshots, you can automatically create or delete snapshots. You can recognize scheduled snapshots by their name with the following format:

    * `<schedule>-<timestamp>`

      * `<schedule>`: hourly, weekly, or monthly

      * `<timestamp>`: appears in UTC (`YYYY-MM-DD at HH:MM:SS UTC`)

  * **Internal snapshots** : snapshots used by NetApp Volumes to support replication and backup operations. Internal snapshots aren't manually deletable. You can identify internal snapshots by their name. Depending on how you view snapshots, internal snapshots can have different names:

    * Internal snapshots used for volume replication, migration, and external replication use the `replication-<timestamp>` naming convention. If you access a snapshot by using NFS or SMB, internal snapshots use the `snapmirror.<uuid>.<timestamp>.` naming convention.

    * Internal snapshots used by scheduled backups use the `scheduled-backup-<randomchars>-<date>-<randomchars>` format.




## Snapshot capacity

Consider the following about snapshot capacity before you use snapshots:

  * For most datasets, an additional capacity of 20% is enough to keep snapshots for up to four weeks. As data gets older, its use for restorations becomes less likely.

  * Overwriting all of the data in a snapshot consumes significant volume capacity, which factors into provisioning volume capacity.




## Snapshot schedules

NetApp Volumes lets you configure snapshot schedules on a per-volume basis. You can choose to take hourly, daily, or weekly snapshots. You can also specify the number of snapshots to retain. Once the retention limit is reached, the snapshots are rotated and the oldest snapshots are automatically deleted to make space for the new snapshots.

**Warning:** Reducing the retention limit in a snapshot policy triggers the immediate and automated deletion of snapshots exceeding the new limit. This action is irreversible. Use the [backups](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-volume-backups) feature for independent recovery. 

To achieve common snapshot schedules, configure the following:

  * **Hourly snapshots taken in a 48-hour time period** : set up hourly snapshots and retain 48 snapshots.

  * **Daily snapshots taken during a 30-day time period** : set up daily snapshots and retain 30 snapshots.

  * **Weekly snapshots taken during a 56-day time period** : set up weekly snapshots and retain 8 snapshots.




## Use cases for snapshots

The following section describes scenarios where you can use snapshots to address data management challenges.

  * **Application cloning** : you can use the snapshot and application cloning feature to allow more test iterations at faster speeds independent of clone size and data structure.

  * **Volume recovery** : you can use snapshots with [NetApp Volumes backups](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-volume-backups) to recover individual files or directories if the data on the volume is corrupted or deleted. Since snapshots only exist within the volume, by themselves they don't offer complete protection from lost volumes.

  * **Data versioning** : snapshots help you keep multiple versions of the same dataset accessible.

  * **Application and data upgrades** : before upgrading applications, you can use NetApp Volumes to capture a snapshot of your data's current state. Then if the upgrade fails, you are able to revert to the previous state and recover your files.

  * **Ransomware protection:** NetApp Volumes helps defend against data loss from ransomware attacks. Because snapshots are read-only and not encryptable, they help defend against unwanted data encryption or deletion from a compromised VM which might have the volume mounted. In the event of a large data loss or compromise, you can use a snapshot to revert an entire volume back to a previous state in seconds.

You can also create a usable volume clone from an older snapshot in order to resume operations until your data is investigated for changes or corruptions following a ransomware attack. Both options make all your data usable within minutes.

  * **Application-consistent recovery points** : you can use NetApp Volumes to take application-consistent snapshots, which are snapshots taken after the operating system and application write the current state of the data to storage. Application-consistent snapshots provide a clear recovery point for the application and can be used to create a consistent clone of the application. Because snapshots are read-only accessible through the client, users can restore data immediately, which provides a substantial recovery time objective improvement.

  * **Crash-consistent snapshots** : you can also use crash-consistent snapshots to recover data, which works well for a majority of applications. However, some data in storage might not be current at the time of recovery because it's kept in operating system and application caches for some time before it's written to storage.

  * **Logical space use** : NetApp Volumes space usage reflects the data in the active file system and deleted blocks that snapshots retain. NetApp Volumes frees the retained snapshot blocks as soon as the latest snapshot that references the blocks is deleted. Your volume continues to consume provisioned space, which includes deleted data your snapshots retain.




## Snapshot space use example

The following example provides details on how to manage a snapshot space requirement:

  1. A user provisions a 5 TiB volume and writes 3 TiB of data into the volume.

Result: The client sees 2 TiB of free space.

  2. The client creates a snapshot and then deletes 1 TiB of data.

_5 TiB volume - 2 TiB user data - 1 TiB snapshot data_

Result: The client continues to see only 2 TiB of free space. This is because the system needs to retain 1 TiB of deleted data that is referenced by the snapshot. That capacity is counted against the allocated capacity.

  3. NetApp Volumes deletes the snapshot.

Result: 1 TiB of snapshot data is freed, and the client sees 3 TiB of free space.




## What's next

[Create a manual snapshot](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/create-manual-snapshots).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
