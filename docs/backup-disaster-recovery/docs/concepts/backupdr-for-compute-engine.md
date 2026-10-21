---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-compute-engine/
title: Backup and DR for Compute Engine on a backup/recovery appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:50.688740+00:00
---

# Backup and DR for Compute Engine on a backup/recovery appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-compute-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Backup and DR for Compute Engine on a backup/recovery appliance Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

A Compute Engine instance is a virtual machine (VM) hosted on Google Cloud. Each instance stores data on Persistent Disk that are attached to the instance.

Backup and DR uses snapshots to incrementally back up data from your Persistent Disks at the instance level. After Backup and DR creates a snapshot to back up the current state of some or all Persistent Disks attached to an instance, you can use the backup to either:

  * [Mount the backup to create a new instance](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-snapshot-images-of-cloud-instances).

  * [Mount the backup to a new disk attached to the source instance or a different instance](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-snapshot-images-of-cloud-instances).

  * [Restore the backup to the source instance](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-instance).




Compute Engine stores multiple copies of each snapshot across multiple locations with automatic checksums to ensure the integrity of your data. To learn more, see [Snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots).

Note that snapshots are different from [custom images](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images) and [machine images](https://docs.cloud.google.com/compute/docs/machine-images), which are useful for creating instance boot disks. To learn more, see the [table comparing the use of images, snapshots, and instance templates](https://docs.cloud.google.com/compute/docs/machine-images#when-to-use).

## How it works: Backup and DR Persistent Disk snapshots

Data backup with Persistent Disk snapshots follows these steps:

  1. The first successful snapshot of an instance creates a snapshot of each Persistent Disk. For each disk this is a full snapshot that contains all the data on the Persistent Disk. Metadata relating to the instance is also backed up to a OnVault pool that is automatically created.

**Note:** Protection of Compute Engine instances using Backup and DR does not consume any space in the backup/recovery appliance Snapshot pool.
  2. The second snapshot only contains any new data or modified data since the first snapshot. Data that hasn't changed since snapshot 1 isn't included. Instead, snapshot 2 contains references to snapshot 1 for any unchanged data.

  3. The third snapshot contains any new or changed data since snapshot 2 but won't contain any unchanged data from snapshot 1 or 2. Instead, snapshot 3 contains references to blocks in snapshot 1 and snapshot 2 for any unchanged data.




This repeats for all subsequent snapshots of each protected instances Persistent Disk. Snapshots are always created based on the last successful snapshot taken. If an additional disk is added to the instance, this disk is automatically included in the next snapshot of the instance. You can also use include and exclude rules to control which persistent disks are included in each backup.

Data restore with Persistent Disk snapshots follows these steps:

  1. Select the instance and point in time that they want to work with. You should take note also of the storage type and regional location.

  2. Select if you want to mount to an existing instance, create a new instance or restore the disks of the source instance.

  3. If creating a new instance, select the location variables such as in which project or zone the instance is created.

  4. Backup and DR requests Compute Engine to create new disks from the snapshots When these disks are created they are attached to the new or existing instance.


**Note:** If you create application consistent snapshots of Windows Compute Engine instances then on mount to existing VM or mount as new VM, you need to [mark your disk as available for read and write](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot#read-only) to make them usable.

## Snapshot storage location

When you create a backup plan for a Compute Engine instance, you can specify where the backup is stored. The location of a snapshot affects its [availability](https://cloud.google.com/storage/sla) and can incur [networking costs](https://cloud.google.com/storage/pricing#network-pricing) when creating the snapshot or restoring it to a new disk.

Snapshots can be stored in either one [Cloud Storage multi-regional location](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr), such as asia, or one [Cloud Storage regional location](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r), such as asia-south1.

A multi-regional storage location provides the highest availability and resilience. A regional storage location gives you more control over the physical location of your data because you specify a single region.

A snapshot can be used to create a new instance or disk in any region and zone, regardless of the storage location of the snapshot.

If you have an [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) that includes the resource locations [constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints), any snapshot storage location that you specify must be in the set of locations defined by the constraint. See [Compute Engine resource locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services#compute-engine) for more information.

If you don't specify a storage location for a snapshot, Backup and DR uses the [default location](https://docs.cloud.google.com/compute/docs/disks/snapshots#default_location), which stores your snapshot in a Cloud Storage multi-regional location closest to the region of the source disk.

## The Backup and DR Compute Engine guide

  * [Check for the cloud credentials](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/create-cloud-credentials)

  * [Discover and protect Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-ce-inst)

  * [Mount backups of Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-snapshot-images-of-cloud-instances)

  * [Restore a Compute Engine instance](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-instance)

  * [Import Persistent Disk snapshot images](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/import-pdsnapshot-images)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
