---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-plans/create-manual-backup/
title: Create a manual backup \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:11.911586+00:00
---

# Create a manual backup  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-plans/create-manual-backup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create a manual backup Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to manually create a backup for virtual machine (VM) workloads in Google Distributed Cloud (GDC) air-gapped.

By default, your backup plan automatically initiates scheduled backups. You can also manually create VM backups at any time, even if it is outside of the schedule you define. Manual VM backups offer the flexibility to capture a VM's state instantly, providing a recovery point independent of your scheduled backup plan.

This document is for developers in platform administrator or application operator groups that manage VM Backup operations. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To create manual VM backups, you must have a [single VM backup repository](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-repository/create-backup-repository) for backup data.

### Request IAM roles

Ask your IAM Org Admin to [grant you](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/set-up-role-bindings) the **Organization Backup Admin** (`organization-backup-admin`) role. This role lets you create, get, list, watch, update, patch, and delete VM backup repositories, VM backup plan templates, VM backup requests, and VM restore requests.

## Create a backup plan template for VMs

You must create a backup plan template before you can trigger a manual backup. Use the GDC console or the API to create a template. You only need to perform this step once for each backup repository. Don't create another template if you've already created one previously.

### Console

  1. Sign into the GDC console.
  2. In the navigation menu, click **Backup for Virtual Machines > Backup plans**.
  3. Click **Create a backup plan**.
  4. In the **Project** field, select a project for which this backup plan is available.
  5. Enter the backup plan name and description.
  6. In the **Backup repo** field, select a backup repository. Backup repositories are a set of object storage implementations.
  7. Click **Create**.



### API

To plan your backups, create a `VirtualMachineBackupPlanTemplate` custom resource. Here's an example of a `VirtualMachineBackupPlanTemplate`:
    
    
    apiVersion: virtualmachine.gdc.goog/v1
    kind: VirtualMachineBackupPlanTemplate
    metadata:
      name: BACKUP_TEMPLATE_NAME
      namespace: PROJECT_NAME
    spec:
      backupRepository: "BACKUP_REPOSITORY_NAME"
    

Replace the following:

  * `BACKUP_TEMPLATE_NAME`: the name of the backup plan template.
  * `PROJECT_NAME`: the name of the project to create the template within.

  * `BACKUP_REPOSITORY_NAME`: the name of the repository created in the previous section.




## Create manual backups

### Request IAM permissions for backup tasks

To back up VMs and create VM disk snapshots, ask your IAM Project Admin to [grant you](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/role-bindings) the following roles:

  * Project VirtualMachine Admin (`project-vm-admin`): Manages VMs in the project namespace.
  * Backup Creator (`backup-creator`): Creates manual backups and restores.
  * Project Viewer (`project-viewer`): Has read-only access to all resources within project namespaces.



Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation#verify-user-access) your access.

### Create a manual VM backup

When submitting a `VirtualMachineBackupRequest`, you must specify the target of the backup using one of two methods:

**Reference an existing backup plan** : Use the `namespace` field in the metadata to specify the project where the plan exists, and the `VirtualMachineBackupPlan` field to target the specific backup plan:
    
    
       apiVersion: virtualmachine.gdc.goog/v1
       kind: VirtualMachineBackupRequest
       metadata:
         name: BACKUP_REQUEST_NAME
         namespace: PROJECT # Use this field if the backup plan was created using the API.
       spec:
         virtualMachineBackupPlan: VM_BACKUP_PLAN
         virtualMachineBackupName: VM_BACKUP_NAME
         deleteLockDays: DELETE_LOCK_DAYS
         retainDays: RETAIN_DAYS
    

**Use a template and target a specific VM** : Use the `virtualMachineBackupPlanTemplate` and `virtualMachine` fields when defining a new, immediate backup based on a template. This method requires specifying the target Virtual Machine directly in the spec:
    
    
       apiVersion: virtualmachine.gdc.goog/v1
       kind: VirtualMachineBackupRequest
       metadata:
         name: BACKUP_REQUEST_NAME
       spec:
         virtualMachineBackupPlanTemplate: VM_BACKUP_PLAN_TEMPLATE
         virtualMachine: VM_NAME
         virtualMachineBackupName: VM_BACKUP_NAME
         deleteLockDays: DELETE_LOCK_DAYS
         retainDays: RETAIN_DAYS
    

Replace the following:

  * `BACKUP_REQUEST_NAME`: name to give the backup request that is being initiated.
  * `PROJECT`: the name of the project where the backup plan resides.
  * `VM_BACKUP_PLAN_TEMPLATE`: the name of the `VirtualMachineBackupPlanTemplate` resource to use for configuration of the backup.
  * `VM_NAME`: the name of the VM to back up.
  * `VM_BACKUP_NAME`: the name of the backup to create.
  * `DELETE_LOCK_DAYS` (optional): the number of days from the creation of this backup during which backup deletion is blocked. The value must not exceed 90 days and must be less than or equal to `RETAIN_DAYS`. If set to `0`, deletion is not blocked. If omitted, this value falls back to the associated backup plan's configuration.
  * `RETAIN_DAYS` (optional): the number of days to keep this backup for, after which it is automatically deleted. The value must not exceed 90 days. If set to `0`, the backup is not automatically deleted. If omitted, this value falls back to the associated backup plan's configuration.



### Create a snapshot

A snapshot captures a point-in-time image of a VM disk for quick restores, unlike a VM backup, which creates an independent copy of VM data in a backup repository.

Create a snapshot using either the GDC console or the API.

### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Virtual Machines > Snapshots**.
  3. Select a project.
  4. Click **Create snapshot**.
  5. In the **Source disk** field, select the disk that you want to create the snapshot from.
  6. Enter the **Snapshot name**.
  7. Click **Create**.



### API

Issue a `VirtualMachineBackupRequest` to initiate a snapshot:
    
    
    apiVersion: virtualmachine.gdc.goog/v1
    kind: VirtualMachineBackupRequest
    metadata:
      name: BACKUP_REQUEST_NAME
      namespace: PROJECT_NAME
    spec:
      virtualMachineBackupPlanTemplate: VM_BACKUP_PLAN
      virtualMachineDisk: VM_DISK
      virtualMachineBackupName: VM_BACKUP_NAME
      deleteLockDays: DELETE_LOCK_DAYS
      retainDays: RETAIN_DAYS
    

Replace the following:

  * `BACKUP_REQUEST_NAME`: the name to give the backup request that is being initiated.
  * `PROJECT_NAME`: the name of the GDC project.
  * `VM_BACKUP_PLAN`: the name of the `VirtualMachineBackupPlanTemplate` to use for configuration of the snapshot.
  * `VM_DISK`: the name of the disk to snapshot.
  * `VM_BACKUP_NAME`: the name of the snapshot to create.
  * `DELETE_LOCK_DAYS` (optional): the number of days from the creation of this snapshot during which backup deletion is blocked. The value must not exceed 90 days and must be less than or equal to `RETAIN_DAYS`. If set to `0`, deletion is not blocked. If omitted, this value falls back to the associated backup plan's configuration.
  * `RETAIN_DAYS` (optional): the number of days to keep this snapshot for, after which it is automatically deleted. The value must not exceed 90 days. If set to `0`, the backup is not automatically deleted. If omitted, this value falls back to the associated backup plan's configuration.



## What's next

  * [Manage backups](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-plans/manage-backups)
  * [Create a restore](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/restore-backup/create-restore-scoped)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
