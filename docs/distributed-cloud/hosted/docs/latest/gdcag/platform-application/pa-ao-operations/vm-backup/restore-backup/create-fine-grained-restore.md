---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/restore-backup/create-fine-grained-restore/
title: Create a fine-grained restore \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:54.239932+00:00
---

# Create a fine-grained restore  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/restore-backup/create-fine-grained-restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create a fine-grained restore Stay organized with collections  Save and categorize content based on your preferences. 

The document describes the process to create fine-grained restores that use filters to target specific resources in virtual machine (VM) and VM disk backups. You can create a restore for a backup created manually or automatically by a backup plan. The restored VMs and their associated disks have their name prefixed with the value of the `restoredResourceName` field.

VM restores support fine-grained resource selection using filters. Use a filter to restore a subset of resources from the previously created `VirtualMachineBackup` resource. This filter is an optional field. If the filter is not provided then the complete set of resources in the `VirtualMachineBackup` resource are restored.

This document is for developers in platform administrator or application operator groups that manage VM backup and restore operations. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To create a restore, ensure you have an existing backup available. You can [create backups on a schedule](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-plans/create-scheduled-backup-plan) using backup plans, or create backups manually.

### Request IAM roles

To create a fine-grained restore, ask your IAM Org Admin to grant you the **Organization Backup Admin** (`organization-backup-admin`) role. This role lets you create, get, list, watch, update, patch, and delete VM backup repositories, VM backup plan templates, VM backup requests, and VM restore requests.

## Create a fine-grained restore

To create a fine-grained restore for a previously created backup, follow these steps:

  1. Get a list of VMs and VM disks that were backed up in your target `VirtualMachineBackup` resource:

     1. Get the list of VMs:
            
            kubectl get virtualmachinebackups.virtualmachine.gdc.goog VM_BACKUP_NAME -n
            VM_BACKUP_NAMESPACE -o jsonpath=
            "{.status.backedUpVirtualMachines}{'\n'}"
            

Replace the following:

        * `VM_BACKUP_NAME`: the name of the backup containing the VM resources you want to restore.
        * `VM_BACKUP_NAMESPACE`: the namespace containing the backup.
     2. Get the list of VM disks:
    
    kubectl get virtualmachinebackups.virtualmachine.gdc.goog VM_BACKUP_NAME -n
    VM_BACKUP_NAMESPACE -o
    jsonpath="{.status.backedUpVirtualMachineDisks}{'\n'}"
    

  2. Use the values from this list to specify the target for your fine-grained restore. Create one of the following fine-grained restores:

     * Restore specific VMs
     * Restore specific VM disks
     * Restore specific VMs and VM disks
     * Restore all VM disks



### Restore specific VMs

  * Use the `targetedVirtualMachines` filter to target a list of VMs with this restore. This option restores the provided VMs and their associated disks. Create and apply a `VirtualMachineRestoreRequest` resource and supply your list of VMs to restore in the `targetedVirtualMachines` field:
        
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
        filter:
            targetedVirtualMachines:
            - resourceName: VM_NAME
        

Replace the following:

    * `VM_BACKUP_NAME`: the name of the `VirtualMachineBackup` resource to restore from.
    * `PROJECT_NAME`: the name of the GDC project.
    * `RESTORE_REQUEST_NAME`: the name to give the restore request that is being initiated.
    * `RESTORE_NAME`: the name to give the restore that is being initiated.
    * `RESTORE_PREFIX`: the prefix given to newly created VM resources. The restored VM and VM disk names are prefixed with `restoredResourceName` value in the restore request.
    * `RESTORED_RESOURCE_DESCRIPTION`: a description of the restore being performed.
    * `VM_NAME`: A list of VMs that is restored by this `VirtualMachineRestoreRequest` resource. If more than one VM is specified, the list must be in the following format:
          
          targetedVirtualMachines:
                - resourceName: "virtual-machine"
                - resourceName: "virtual-machine-2"
                ...
                - resourceName: "virtual-machine-n"
            ```
          




### Restore specific VM disks

  * Use the `targetedVirtualMachineDisks` filter to target a set of VM disks to restore. This option restores any disks that were backed up, and these disks don't have to be attached to the same VM. This option restores only the disks and not the VMs to which the disks were attached. Create and apply a `VirtualMachineRestoreRequest` resource and supply the list of VM disks to restore in the `targetedVirtualMachineDisks` field:
        
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
          filter:
            targetedVirtualMachineDisks:
            - VM_DISK_NAME
        

Replace `VM_DISK_NAME` with the list of VM disks that is restored by this `VirtualMachineRestoreRequest` resource. If more than one VM disk is specified, the list must be in the following format:
        
        targetedVirtualMachineDisks:
            - resourceName: "disk-1"
            - resourceName: "disk-2"
            ...
            - resourceName: "disk-n"
        




### Restore specific VMs and VM disks

  * To target combination of VMs and VM disks, use the `targetedVirtualMachines` and `targetedVirtualMachineDisks` filters together, this method restore the VMs specified in the `targetedVirtualMachines` filter along with their attached disks, and the VM disks mentioned in `targetedVirtualMachineDisks` filter. If the disk is already attached to the VM specified in the `targetedVirtualMachineDisks` list. In the `targetedVirtualMachineDisks` filter, specify only the disks that are not already included as part of the `targetedVirtualMachines`.
        
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
          filter:
            targetedVirtualMachines:
            - resourceName: VM_NAME
            targetedVirtualMachineDisks:
            - resourceName: VM_DISK_NAME
        

Replace the following:

    * `VM_NAME`:The list of VMs that is restored by this `VirtualMachineRestoreRequest` resource. If more than one VM is specified, the list must be in the following format:
          
          targetedVirtualMachines:
                    - resourceName: "virtual-machine"
                    - resourceName: "virtual-machine-2"
                    ...
                    - resourceName: "virtual-machine-n"
            ```
          

    * `VM_DISK_NAME`: the list of VM disks that is restored by this `VirtualMachineRestoreRequest` resource. If more than one VM disk is specified, the list must be in the following format:
          
          targetedVirtualMachineDisks:
              - resourceName: "disk-1"
              - resourceName: "disk-2"
              ...
              - resourceName: "disk-n"
          




### Restore all VM disks

  * Set the filter value `virtualMachineDiskOptions.allDisks` to true to restore all of the disks that were protected as part of `VirtualMachineBackup`. This action won't restore the VMs to which the disks were attached:
        
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
          filter:
            virtualMachineDiskOptions:
                allDisks: true
        




## What's next

  * [Clean up labels after restoring VM-attached disks](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/clean-up-labels-after-restore)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
