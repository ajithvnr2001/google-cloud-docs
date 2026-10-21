---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-vmware-vms/
title: Backup and DR for VMware Engine on a backup/recovery appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:50.748782+00:00
---

# Backup and DR for VMware Engine on a backup/recovery appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-vmware-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Backup and DR for VMware Engine on a backup/recovery appliance Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Backup and DR uses VMware vSphere Storage APIs - Data Protection to create backups of VMware VMs, placing these backups either in the snapshot pool of the backup/recovery appliance or in OnVault pools, or in both.

**Note:** Only backing up old Windows server OS versions inside the Google Cloud VMware Engine VM is supported. Installing a Backup and DR agent won't let you back up support team cannot assist with OS boot-up issues or other OS-related problems. In such cases, you must contact the OS vendor for support.

Backup and DR uses snapshots to incrementally backup data from your VMDKs at the VM level. After Backup and DR creates a backup of the current state of all VMDKs attached to a VM, you can use it to either:

  * Mount that data to create a new VMware VM. See [Mount a VMware backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-vmware-image).

  * Mount that data as a new disk(s) attached to a selected VM (either the source VM or a different physical host or VM). See [Mount a VMware backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-vmware-image).

**Note:** OnVault pools pointing to backup vaults don't support mount operations.
  * Restore that data to either all or selected disks attached to the source VMware VM. See [Restore a VMware VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-vm).

  * Clone that data to either all or selected disks attached to a new target VMware VM. See [Restore a VMware VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/clone-image-of-a-vm).




Backup and DR can be configured to store multiple copies of each snapshot across multiple locations using OnVault that writes backups to Cloud Storage, or StreamSnap that copies snapshots to a second backup/recovery appliance. Backup and DR uses automatic checksums to ensure the integrity of your data after each successful backup job.

## How it works: Backup and DR VMware VM snapshots

Data backup with VMware VMs follows these steps:

  1. The first successful snapshot of a VMware VM creates a snapshot of each virtual disk (VMDK). For each disk this is a full snapshot that contains all of the data on the virtual disk.

  2. The second snapshot only contains any new data or modified data since the first snapshot. Data that hasn't changed since snapshot 1 isn't included. Instead, snapshot 2 contains references to snapshot 1 for any unchanged data.

  3. Snapshot 3 contains any new or changed data since snapshot 2 but won't contain any unchanged data from snapshot 1 or 2. Instead, snapshot 3 contains references to blocks in snapshot 1 and snapshot 2 for any unchanged data.




This repeats for all subsequent snapshots of the VMware VM. Snapshots are always created based on the last successful snapshot taken by Backup and DR. If an additional virtual disk is added to the VMware VM, this disk is automatically included in the next snapshot of the VM. You can also use include or exclude rules to control which virtual disks are included in each backup. By default, all virtual disks are included in the Volume Inclusion Rule.

Data mount with VMware VM backups follows these steps:

  1. Select the VMware VM and point in time that they want to work with.

  2. Select if you want to mount to an existing host or VM, create a new VMware VM or restore the disks of the source VMware VM.

  3. If creating a new VMware VM, select the location variables such as which vCenter, ESX host and datastore to be used.

  4. Backup and DR uses snapshot technology to create new virtual disks from the backups. When these disks are created they are attached to the host or to the new or existing VMware VM. These virtual disks are writable, and can be migrated to physical disks using a VMware Storage VMotion task.




## Backup storage location

When you create a backup plan and apply it to a VMware VM, the policies and profile specify where the backup is stored.

VMware VM-based backup data can be stored directly into Google Cloud Storage, using a Direct to OnVault template in the backup plan. This works for Google Cloud VMware Engine, though it is recommended to ensure sufficient bandwidth exists if you are using this feature. If bandwidth is limited, then a local snapshot policy is recommended, which retains a copy of the backup data for a user defined period of time, and in addition to the snapshot policy, additional OnVault policies can be enabled to store data for longer periods of time in Google Cloud Storage bucket(s).

OnVault backups can be stored in a [Cloud Storage multi-regional location](https://docs.cloud.google.com/storage/docs/locations#location-mr), a [Cloud Storage dual-region location](https://docs.cloud.google.com/storage/docs/locations#location-dr), or a [Cloud Storage regional location](https://docs.cloud.google.com/storage/docs/locations#location-r).

Each VM can have up to four OnVault policies, each specifying different Google Cloud Storage buckets, which could be different storage classes and different location types.

A multi-regional storage location provides the highest availability and resilience. A regional storage location gives you more control over the physical location of your data because you specify a single region.

## The VMware administrator's guide

  * [Backup and DR for VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/vmware-intro)

  * [Configure Google Cloud VMware Engine for Backup and DR protection](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-vmware)

  * [Add vCenter and ESX server hosts to the appliance management console](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-vcenter-host)

  * [Discover and protect VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-vms)

  * [Apply a backup template to protect a VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-template-to-manage-a-VM)

  * [Configure application settings for VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/configure-application-settings-for-vmware-vm)

  * [Restore a VMware VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-vm)

  * [Mount a VMware backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-vmware-image)

  * [Clone a backup of a VMware VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/clone-image-of-a-vm)

  * [Create LiveClone workflows](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/create-liveclone-workflows)

  * [Move VM management between two backup/recovery appliances](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/supported-vmware)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
