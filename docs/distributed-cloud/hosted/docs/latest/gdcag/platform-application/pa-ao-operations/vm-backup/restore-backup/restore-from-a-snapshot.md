---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/restore-backup/restore-from-a-snapshot/
title: Restore a VM from a snapshot \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:53.863329+00:00
---

# Restore a VM from a snapshot  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/restore-backup/restore-from-a-snapshot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Restore a VM from a snapshot Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to restore a virtual machine (VM) disk from an image disk snapshot that was created through Google Distributed Cloud (GDC) air-gapped backup and restore procedures.

This document is for developers in platform administrator or application operator groups that manage VM Backup and restore operations. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To restore a VM disk from a snapshot, you must have the following:

  * An existing [snapshot](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-plans/create-manual-backup#create-snapshot).



### Request IAM permissions

To manage VMs and VM disk restores, ask your IAM Project Admin to [grant you](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/role-bindings) the following roles:

  * Project VirtualMachine Admin (`project-vm-admin`): Manages VMs in the project namespace.
  * Backup Creator (`backup-creator`): Creates manual backups and restores.
  * Project Viewer (`project-viewer`): Has read-only access to all resources within project namespaces.



Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation#verify-user-access) your access.

## Restore a snapshot

Create a new VM from a disk snapshot by using the GDC console or the application programming interface (API).

### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Virtual Machines > Snapshots**.
  3. Select a project.
  4. In the list of snapshots, find the snapshot to restore and click **Restore**.
  5. In the **New disk name** field, enter the name of the disk to restore the backup in.
  6. Enter a **Restore name** for the restore.
  7. Click **Restore**.



### API

Create a `VirtualMachineRestoreRequest` custom resource to initiate the restore process.

The restoration of application capability is subject to the VM operating system or image. Create a `VirtualMachineRestoreRequest` custom resource to initiate the restore process:
    
    
    apiVersion: virtualmachine.gdc.goog/v1
    kind: VirtualMachineRestoreRequest
    metadata:
      name: RESTORE_REQUEST_NAME
      namespace: PROJECT_NAME
    spec:
      virtualMachineBackup: VM_BACKUP_NAME
      restoreName: RESTORE_NAME
      restoredResourceName: RESTORE_PREFIX
      restoredResourceDescription: RESTORED_RESOURCE_DESCRIPTION
    

Replace the following:

  * `VM_BACKUP_NAME`: the name of the `VirtualMachineBackup` resource to restore from.
  * `PROJECT_NAME`: the name of the GDC project.
  * `RESTORE_REQUEST_NAME`: the name of the restore request that is being initiated.
  * `RESTORE_NAME`: the name to give the restore that is being initiated.
  * `RESTORE_PREFIX`: a prefix that is appended to the start of the name for backups that this request restores.
  * `RESTORED_RESOURCE_DESCRIPTION`: description of why the restore is performed.



The result of the restore creates a new disk with the same configuration and disk state as the snapshot, completing the data backup and recovery process.

## View a restore

View a restore using the GDC console or `kubectl` command-line interface (CLI).

### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Virtual Machines > Snapshots**.
  3. Select a project.
  4. Click the **Restores** tab.
  5. In the list of restores, click the restore name to view its details.



### kubectl

View a restore by listing the restores and viewing their details:

  1. List the existing snapshots:
         
         kubectl get virtualmachinerestores.virtualmachine.gdc.goog -n PROJECT_NAME
         

Replace `PROJECT_NAME` with the name of the project.

  2. In the list, find the restore that you want to view.

  3. View the restore details:
         
         kubectl describe virtualmachinerestore.virtualmachine.gdc.goog RESTORE_NAME -n PROJECT_NAME
         

Replace the following:

     * `RESTORE_NAME`: the name of the restore.
     * `PROJECT_NAME`: the name of the project.



## Delete a restore

Delete a restore by using the `kubectl` command-line interface (CLI).

View a restore by listing the restores and viewing their details:

  1. List the existing restores:
         
         kubectl get virtualmachinerestores.virtualmachine.gdc.goog -n PROJECT_NAME
         

Replace `PROJECT_NAME` with the name of the project.

  2. In the list, find the restore that you want to delete.

  3. Delete the restore:
         
         kubectl delete virtualmachinerestores.virtualmachine.gdc.goog RESTORE_NAME -n PROJECT_NAME
         

Replace the following:

     * `RESTORE_NAME`: the name of the restore.
     * `PROJECT_NAME`: the name of the project.



## What's next

  * [Clean up labels after restoring VM-attached disks](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/clean-up-labels-after-restore)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
