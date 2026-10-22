---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-plans/manage-backups/
title: Manage virtual machine backups \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:54.556942+00:00
---

# Manage virtual machine backups  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-plans/manage-backups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Manage virtual machine backups Stay organized with collections  Save and categorize content based on your preferences. 

This document guides you through managing Virtual Machine (VM) backups and VM disk snapshots in Google Distributed Cloud (GDC) air-gapped, and details how to view and delete them.

This document helps developers in platform administrator or application operator groups who optimize storage usage while complying with data retention policies. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

### Request IAM roles

To manage VMs and VM disk backups, ask your IAM Project Admin to grant you the following roles:

  * **Project VirtualMachine Admin** (`project-vm-admin`): creates, gets, lists, watches, updates, patches, and deletes virtual machines and VM disks in project namespaces.

  * **Backup Creator** (`backup-creator`): creates, gets, lists, watches, updates, patches, and deletes manual backup requests and manual restore requests.

  * **Project Viewer** (`project-viewer`): gets, lists, and watches all resources within project namespaces.




Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation#verify-user-access) your access.

## Manage VM backups

The following section describes the technical steps to list and delete your VM backups.

### List VM backups

View a list of VM backups using the GDC console or `kubectl`.

### Console

  1. Sign into the GDC console.
  2. In the navigation menu, click **Backup for Virtual Machines**.
  3. Select a project.
  4. Click the **Backups** tab.
  5. Click a backup in the list to view its details.



### kubectl

View a VM backup by listing the backups and viewing their details.

  1. List the existing backups:
         
         kubectl get virtualmachinebackups.virtualmachine.gdc.goog -n PROJECT_NAME
         

Replace `PROJECT_NAME` with the name of the project.

  2. In the list, find the backup that you want to view.

  3. View the backup details:
         
         kubectl describe virtualmachinebackup.virtualmachine.gdc.goog VM_BACKUP_NAME -n PROJECT_NAME
         

Replace the following:

     * `VM_BACKUP_NAME`: the name of the backup.
     * `PROJECT_NAME`: the name of the project.



### Delete a VM backup

Delete VM backups by using the GDC console or `kubectl`.

### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Backup for Virtual Machines**.
  3. Select a project.
  4. Click the **Backups** tab.
  5. In the list of backups, find the backup to delete and click **Delete Backup**.
  6. In the **Backup name** field, enter the name of the backup to delete.
  7. Click **Delete Backup**.



### kubectl

Delete a VM backup using `kubectl`.

  1. List the existing VM backups:
         
         kubectl get virtualmachinebackups.virtualmachine.gdc.goog -n PROJECT_NAME
         

Replace `PROJECT_NAME` with the name of the project.

  2. In the list, find the backup that you want to delete.

  3. Issue a `VirtualMachineDeleteBackupRequest` to delete the backup:
         
         apiVersion: virtualmachine.gdc.goog/v1
         kind: VirtualMachineDeleteBackupRequest
         metadata:
           name: DELETE_BACKUP_REQUEST_NAME
           namespace: PROJECT_NAME
         spec:
           virtualMachineBackupRef:
             name: VM_BACKUP_NAME
         

Replace the following:

     * `DELETE_BACKUP_REQUEST_NAME`: the name to give the `VirtualMachineDeleteBackupRequest` that is being initiated.
     * `VM_BACKUP_NAME`: the name of the backup to delete.
     * `PROJECT_NAME`: the name of the project.



## Manage VM disk backups

The following section describes the technical steps to list and delete your VM disk backups.

### View snapshots

View snapshots and their details using the Google Cloud console or `kubectl`.

### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Virtual Machines > Snapshots**.
  3. Select a project.
  4. In the list of snapshots, click the snapshot name to view its details.



### kubectl

View a snapshot by listing the snapshots and viewing their details.

  1. List the existing snapshots:
         
         kubectl get virtualmachinebackups.virtualmachine.gdc.goog -n PROJECT_NAME
         

Replace `PROJECT_NAME` with the name of the project.

  2. In the list, find the snapshot that you want to view.

  3. View the snapshot details:
         
         kubectl describe virtualmachinebackup.virtualmachine.gdc.goog VM_BACKUP_NAME -n PROJECT_NAME
         

Replace the following:

     * `VM_BACKUP_NAME`: the name of the snapshot.
     * `PROJECT_NAME`: the name of the project.



### Delete a snapshot

Delete snapshots using the Google Cloud console or `kubectl`. Disks created from snapshots are not affected when you delete the underlying snapshot.

### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Virtual Machines > Snapshots**.
  3. Select a project.
  4. In the list of snapshots, find the snapshot to delete and click **Delete**.
  5. Click **Confirm**.



### kubectl

Run `kubectl` from a `gdcloud`-configured machine to delete a snapshot. Don't perform this task from the cluster's bootstrapper node.

  1. List the existing snapshots:
         
         kubectl get virtualmachinebackups.virtualmachine.gdc.goog -n PROJECT_NAME
         

Replace `PROJECT_NAME` with the name of the project.

  2. In the list, find the snapshot that you want to delete.

  3. Issue a `VirtualMachineDeleteBackupRequest` to delete the snapshot:
         
         apiVersion: virtualmachine.gdc.goog/v1
         kind: VirtualMachineDeleteBackupRequest
         metadata:
           name: DELETE_BACKUP_REQUEST_NAME
           namespace: PROJECT_NAME
         spec:
           virtualMachineBackupRef:
             name: VM_BACKUP_NAME
         

Replace the following:

     * `DELETE_BACKUP_REQUEST_NAME`: the name to give the delete backup request that is being initiated.
     * `VM_BACKUP_NAME`: the name of the snapshot to delete.
     * `PROJECT_NAME`: the name of the project.



## What's next

  * [Create a restore](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/restore-backup/create-restore-scoped)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
