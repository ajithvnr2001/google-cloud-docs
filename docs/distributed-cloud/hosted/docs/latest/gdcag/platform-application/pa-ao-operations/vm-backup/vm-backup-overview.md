---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/vm-backup-overview/
title: Overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:02:27.245248+00:00
---

# Overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/vm-backup-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of virtual machine (VM) backup and restore operations in Google Distributed Cloud (GDC) air-gapped environments. It outlines the different methodologies and the distinction between GDC console and API capabilities.

This document is for developers in platform administrator or application operator groups that manage VM backup operations. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

GDC supports the ability to back up and restore VM-based and container-based workloads. GDC VM backup supports the backup and restoration of multiple VM or VM disk snapshots. Backups are managed through backup plans, which let you schedule regular backups or create backups manually. You can restore entire VMs, creating a new instance with the same configuration and disk state as the backup, or restore disk snapshots.

GDC backup for VMs offer the following features:

  * Support for different VM instance configurations and sizes.
  * Customer data stored in primary storage in the form of Kubernetes persistent volumes and VM disk images.
  * Local snapshots for VM disks.



## Backup and restoration process

You can back up and restore your Distributed Cloud data in the GDC console or the API.

To back up and restore VM and container workloads, follow these general steps:

  1. [Create a backup repository](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-repository/create-backup-repository).
  2. Create a backup plan that references the backup repository: 
     * Either let the backup plan automatically [create scheduled backups](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-plans/create-scheduled-backup-plan) or [manually create a backup](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-plans/create-manual-backup).
  3. [Back up VMs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-plans/manage-backups) or [back up disks](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-plans/manage-backups) in the form of snapshots.
  4. [Restore VMs or snapshots](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/restore-backup/restore-from-a-snapshot) based on the backups.



## Backup repository overview

Before you create backups or snapshots, you must create a backup repository. A backup repository contains configuration information, for example, the bucket name, region, and storage endpoint. The backup repository name is provided as an input parameter when you create a VM backup plan.

For more information, see [Create a backup repository](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-repository/create-backup-repository).

## VM backup resources

The VM backup system in GDC consists of these key custom resources (CRs):

  * `BackupRepository`: The location where the backup data is stored. This resource is manageable through the API and the GDC console.
  * `VirtualMachineBackupPlanTemplate`: Defines the backup repository used. This resource is manageable through the API and the GDC console
  * `VirtualMachineBackupPlan`: Defines a scheduled, recurring backup strategy. This resource specifies the backup schedule, the scope of VMs to be backed up, and the retention policy for the backups. This resource is only manageable through the API.
  * `VirtualMachineBackupRequest`: Triggers an immediate backup. This resource can be used for both one-off manual backups and to manually initiate a backup defined in a `VirtualMachineBackupPlan`. This resource is manageable through the API and the GDC console, but you can only trigger a backup plan using the API.
  * `VirtualMachineRestoreRequest`: Restores a VM from a backup. This resource is manageable through the API and the GDC console.



## Plan backups

You can create a backup plan and perform backup and restore functions using either the API or the GDC console. All backup methods are supported through the API, while on-demand, manual backups are the only backup types the GDC console supports.

### Scheduled backups (API only)

This method involves the creation of a `VirtualMachineBackupPlan` resource, which references a `VirtualMachineBackupPlanTemplate`. You can define a recurring backup schedule, the scope of VMs to include, and a retention policy.

For more details, see [Create a scheduled backup plan to back up and restore VMs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-plans/create-scheduled-backup-plan).

### On-demand backups (GDC console and API)

This method uses a `VirtualMachineBackupRequest` resource that directly references a `VirtualMachineBackupPlanTemplate`. You can perform a one-time backup of a specific VM or VM disk. For more details, see [Create a manual backup](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-plans/create-manual-backup).

**Note:** On-demand backups are the only backup method supported through the GDC console.

### Manual trigger of a defined backup plan (GDC console and API)

This method uses a `VirtualMachineBackupRequest` resource that references an existing `VirtualMachineBackupPlan`. It immediately triggers a backup of all VMs defined in the scope of the referenced plan. This backup method is useful for taking an ad hoc backup of a group of VMs that are part of a scheduled plan.

For more information, see [Create a manual backup](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-plans/create-manual-backup).

## Restore backups

You can restore VM workloads or disk snapshots for backups you create manually or as part of the scheduled backup plans:

  * For scheduled backup plan restoration, see [Create a backup restore](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/restore-backup/create-restore-scoped) or [Create a fine-grained restore](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/restore-backup/create-fine-grained-restore)

  * For VM workloads, the restoration process creates a new VM with the same configuration and disk state as the backup. For more information, see [Create a VM from a backup](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/restore-backup/create-vm-from-backup).

  * For disk snapshots, the restore creates a new disk with the same configuration and disk state as the snapshot. For more information, see [Restore from a snapshot](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/restore-backup/restore-from-a-snapshot).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
