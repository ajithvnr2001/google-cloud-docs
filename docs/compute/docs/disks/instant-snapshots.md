---
url: https://docs.cloud.google.com/compute/docs/disks/instant-snapshots/
title: About instant snapshots \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:21.279159+00:00
---

# About instant snapshots  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/instant-snapshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About instant snapshots Stay organized with collections  Save and categorize content based on your preferences. 

An instant snapshot is an in-place backup of a disk that can be used to rapidly create a new disk in minutes.

Instant snapshots capture data at a specific point in time. They are optimized for rapidly restoring captured data to a new disk. Use instant snapshots to quickly recover data in cases where the zone and disk are still intact but the data on the disk has been lost or corrupted, such as the following:

  * User error
  * Failed software upgrades
  * Application-level failures



Creating an instant snapshot of a disk before one of these events occurs lets you quickly restore the data from the instant snapshot to a new disk. Reducing the time to restore a disk helps avoid downtime and long maintenance windows.

Instant snapshots are incremental and can be more cost effective than using multiple disk clones.

**Warning:** Instant snapshots of a disk are deleted when the disk is deleted and don't protect against zonal or regional failures. To protect your data from zonal or regional failures, create a backup in another region using [standard snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots) or another [data backup option](https://docs.cloud.google.com/compute/docs/disks/data-protection).

## Snapshot types

You can back up a disk with snapshots. The three types of snapshots—standard, instant, and archive—all capture the contents of a disk at a specific point in time.

The following are the key differences between the snapshot types:

  * Retention after source disk deletion
  * [Data recovery time (RTO)](https://wikipedia.org/wiki/Recovery_point_objective)
  * Storage location



### Retention after source disk deletion

An instant snapshot of a disk **only exists until the source disk is deleted**. Standard and archive snapshots aren't deleted with the source disk. Therefore, if you want to retain a backup of a disk after you delete the disk itself, use archive or standard snapshots.

### Data recovery time

The data recovery time is the length of time needed to create a new disk from a snapshot and varies by snapshot type.

  * Instant snapshots offer the lowest and best recovery times.
  * Standard snapshots have faster data recovery times than archive snapshots.
  * Archive snapshots have the longest data recovery times, but offer the most cost efficient storage.



### Storage location by snapshot type

The storage location is the zone or region where Compute Engine stores the snapshot.

  * Instant snapshots are local disk backups that are stored in the same zone or region as the source disk.
  * Archive and standard snapshots are remote backups of disk data stored separately from the source disk.



Compute Engine stores archive and standard snapshots in the same manner. Copies of archive and standard snapshots are stored across multiple locations with automatic checksums to ensure the integrity of your data.

Unless otherwise specified, references to standard snapshots include archive snapshots.

### Snapshot type comparison

The following table compares the differences between the types of snapshots:

Snapshot type | Best for | Storage redundancy | Support for Hyperdisk | Can be created with snapshot schedules | Deleted on source disk deletion  
---|---|---|---|---|---  
Standard snapshots | Geo-redundant data backup to safeguard against local, zonal, and regional outages. | Redundant. Stored in one or more regions. Not restricted to the same zone or region as the source disk. | Yes | Yes | No  
Archive snapshots | Same as standard snapshots, but for data that is rarely accessed and must be retained for several months or years. Lower cost geo-redundant storage that is better suited for data related to compliance, audits, and cold-storage. | Redundant. Stored in one or more regions. Not restricted to the same zone or region as the source disk. | Yes | No | No  
Instant snapshots | In-place data backup to enable quick restore to a new disk in case of user error or application corruption. | **Not redundant. Stored in the same zone or region as source disk only.** | Yes, for certain  
Hyperdisk types* | No | **Yes**  
  
*You can't create instant snapshots of Hyperdisk ML or Hyperdisk Throughput volumes.  


In addition to snapshots, Compute Engine offers other data backup options. Review the chart describing [data backup options](https://docs.cloud.google.com/compute/docs/disks/data-protection).

The information in this document applies to instant snapshots. Learn more [about standard snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots).

## Supported disk types

Instant snapshots support the following disk types:

  * Hyperdisk Balanced
  * Hyperdisk Balanced High Availability
  * Hyperdisk Extreme
  * Persistent Disk, including Extreme Persistent Disk



You can back up both boot and non-boot disks with instant snapshots.

Instant snapshots can be used with zonal and regional disks. You can't use instant snapshots to back up Hyperdisk Throughput or Hyperdisk ML volumes.

An instant snapshot of a disk is always stored in the same zone or region as the disk. For example, instant snapshots of a disk in the `us-east1-d` zone are stored in the `us-east1-d` zone. Likewise, instant snapshots of a regional Persistent Disk volume in the `us-east1` region are stored in the `us-east1` region.

## Access the data on a snapshot

The data in snapshots is read-only. To access or modify the data on a snapshot, create a disk from the snapshot.

Create a [disk clone](https://docs.cloud.google.com/compute/docs/disks/create-disk-from-source#clone) if you want a writeable, immediately accessible copy of a disk for debugging or experimentation.

## Back up data across a group of disks

For workloads that use multiple disks, you can capture the data on all the disks at the same point in time by creating a consistency group of instant snapshots. For example, before you make a major change to your workload, you can back up all impacted disks at once. If you need to, you can later restore all the disks in the workload to the same point in time.

To create a consistency group of instant snapshots, you first [create a consistency group of the disks](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-consistency-groups#create_a_consistency_group) that you want to back up, then [create consistency groups of instant snapshots from the group of disks](https://docs.cloud.google.com/compute/docs/disks/create-instant-snapshots#create-instant-snapshots-group). Consistency groups of instant snapshots offer the same functionality as individual instant snapshots, but on a larger scale.

## Work with instant snapshots

  * [Create instant snapshots of individual disks](https://docs.cloud.google.com/compute/docs/disks/create-instant-snapshots#create-instant-snapshots) or [groups of disks](https://docs.cloud.google.com/compute/docs/disks/create-instant-snapshots#create-instant-snapshots-group).

  * To verify, view, or modify the data on a snapshot, [create a disk from the snapshot](https://docs.cloud.google.com/compute/docs/disks/restore-instant-snapshot). After you create the disk, you can attach it to a VM or create a new VM from the disk, if it is a boot disk.

  * If you no longer need an instant snapshot, [delete the snapshot](https://docs.cloud.google.com/compute/docs/disks/create-instant-snapshots#delete_an_instant_snapshot) to reduce your storage costs.

  * You can [list all the instant snapshots in a project](https://docs.cloud.google.com/compute/docs/disks/create-instant-snapshots#list-instant-snapshots), or only [list the instant snapshots of a disk](https://docs.cloud.google.com/compute/docs/disks/create-instant-snapshots#list-instant-snapshots_disk).

  * For a given disk, there are [limitations](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots#limitations) regarding the maximum number of instant snapshots and maximum time between snapshots.




## Store an instant snapshot in a different location

You can't directly move an instant snapshot to a different location, but you can [create a standard snapshot from an instant snapshot](https://docs.cloud.google.com/compute/docs/disks/convert-instant-snapshot) and store the standard snapshot in the location that you want.

## Limitations

  * You can't create instant snapshots of Hyperdisk Throughput or Hyperdisk ML volumes.
  * You can't select the storage location of an instant snapshot. It's always stored in the same region or zone as the source disk.

  * When you delete a disk, all instant snapshots of the disk are deleted, including instant snapshots that are part of a consistency group. This means that when you delete an instance, instant snapshots of the instance's boot disk are deleted. Instant snapshots of non-boot disks attached to the instance are also deleted if you've [enabled auto-delete for the disk](https://docs.cloud.google.com/compute/docs/disks/modify-persistent-disk#updateautodelete). To retain the data on an instant snapshot before it is deleted, [create a standard snapshot from the instant snapshot](https://docs.cloud.google.com/compute/docs/disks/convert-instant-snapshot).

  * An instant snapshot is accessible only within the zone or region where it's stored. To move an instant snapshot to another region, you must create a standard snapshot from the instant snapshot.

  * When you create a disk from a CMEK-encrypted instant snapshot, you must provide the instant snapshot's encryption key.

  * You can create a standard snapshot of an individual disk at most 6 times every 60 minutes. This limit also applies to creating a standard snapshot from an instant snapshot of a disk.

  * You can't create a VM from an instant snapshot of a boot disk. Create a disk from the instant snapshot first, and choose the disk as the source for the VM.

  * You can create an instant snapshot of a given disk at most once every 30 seconds.

  * You can't have more than 32 instant snapshots of the same disk.

  * You can't create instant snapshots with snapshot schedules.

  * You can't create instant snapshots on secondary asynchronously replicated Persistent Disk volumes.

  * Instant snapshots are [crash consistent](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices#prepare_for_consistency) and not application consistent. This means that any in-memory data that hasn't yet been written to the disk isn't captured in the instant snapshot. If you require application consistency, create an [application consistent standard snapshot](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices#creating_application_consistent_snapshots).

  * You can't move a disk until you delete all the instant snapshots of the disk. For more information, see [Moving a disk that has instant snapshots](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-vm-creation#move-disk).

  * You can't edit the data stored in an instant snapshot.

  * You can't recover deleted instant snapshots.

  * You can't add new instant snapshots to an existing consistency group of instant snapshots. You must add the disk to the consistency group of disks, then create a new consistency group of instant snapshots using the updated consistency group.




## How instant snapshot sizes work

An instant snapshot's size indicates how much data changed on the source disk from the moment you created the instant snapshot until you created a newer instant snapshot. However, after data on a disk changes, Compute Engine might not immediately update the size of the most recent instant snapshot.

Therefore, an instant snapshot's size might be zero for one of the following reasons:

  * No data has changed on the disk since you created the instant snapshot.
  * Data has changed on the disk, but Compute Engine temporarily hasn't updated the instant snapshot's size to reflect the changes on the disk.



If an instant snapshot's size is zero, this doesn't mean that the disk is empty or that a problem occurred backing up the disk.

## Billing for instant snapshots

Instant snapshots are billed based on the amount of data changed on the disk since the instant snapshot was taken.

### How storage costs are calculated

The following costs apply to instant snapshots:

  * **Operation costs** : Applicable at creation time for each snapshot.
  * **Storage costs** : Charges apply based on how much data changes on the disk from the instant snapshot's creation until another instant snapshot is taken, or until the instant snapshot is deleted. The storage is billed at the [same rate as the source disk](https://docs.cloud.google.com/compute/disks-image-pricing#disk).



There are no additional costs to use consistency groups of instant snapshots.

The following is a summary of how costs are calculated:

  * After taking an instant snapshot, there is no additional storage cost until the data on the source disk changes.

  * For a given instant snapshot, storage costs increase as you write to the disk until you create another instant snapshot. Subsequent changes to the disk are billed to the newer snapshot.

  * Instant snapshots are stored as incremental resources. Whenever a block on the disk is changed, charges accrue to the most recent instant snapshot of that disk. If other instant snapshots had tracked changes to the same blocks, charges for those blocks only apply to the newest instant snapshot.




#### Example

Suppose you create an instant snapshot, `IS-1`, of a disk at 9:00. At that time, the size of `IS-1` is 0 bytes. For the next 90 minutes, you write data to the disk and create additional instant snapshots, `IS-2` and `IS-3`, at 9:30 and 10:15, respectively.

The total costs at 10:30 are as follows:

  * **Operation costs** :

    * At 9:00 for `IS-1`.
    * At 9:30 for `IS-2`.
    * At 10:15 for `IS-3`.
  * **Storage costs** :

    * Charges apply to `IS-1` for the bytes changed on the disk from 9:00 to 9:30.
    * Charges apply to `IS-2` for the bytes changed on the disk from 9:30 to 10:15.
    * Charges apply to `IS-3` for the bytes changed on the disk from 10:15 to 10:30.



If you delete `IS-3`, then the storage size of `IS-2` increases to contain the bytes changed on the disk from 9:30 to 10:30. Then, if you delete `IS-2`, `IS-1` increases to contain the bytes changed on the disk from 9:00 to 10:30.

Alternatively, if you delete only `IS-1`, the storage sizes of `IS-2` and `IS-3` remain the same and the bytes changed on the disk from 9:00 to 9:30 aren't transferred to a newer snapshot.

## Instant snapshot encryption

An instant snapshot uses the same encryption as its source disk. You can't encrypt an instant snapshot with a key that is different from the key used by the source disk.

Suppose you have a disk, `D-1`, that's encrypted with a customer-supplied encryption key (CSEK)([Deprecated](https://docs.cloud.google.com/compute/docs/deprecations)) or a customer-managed encryption key (CMEK).

If you create an instant snapshot, `IS-1` from `D-1`, then `IS-1` uses the same encryption keys as `D-1`. In addition, if you create a disk, `D-2`, from `IS-1`, then `D-2` also uses the same encryption keys as `IS-1` and `D-1`.

When you create a disk from a CSEK- or CMEK-encrypted instant snapshot, you must provide the encryption keys for the source disk.

## What's next

  * [Create an instant snapshot](https://docs.cloud.google.com/compute/docs/disks/create-instant-snapshots) of a disk.
  * Back up a disk for disaster recovery with [standard snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots).
  * Learn how to [copy an instant snapshot to a standard snapshot](https://docs.cloud.google.com/compute/docs/disks/convert-instant-snapshot).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
