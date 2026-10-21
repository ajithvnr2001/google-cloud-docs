---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/restore-backup/create-restore-scoped/
title: Create a restore \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:36:43.160685+00:00
---

# Create a restore  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/restore-backup/create-restore-scoped/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create a restore Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create a restore for virtual machine (VM) workloads in Google Distributed Cloud (GDC) air-gapped.

You can create a restore for a backup that was created manually or automatically by a backup plan. The restored VM and its associated disks contain different names based on the value you specify in the `restoredResourceName` field. All of the VM resources mentioned in the scope of `VirtualMachineBackupPlan` resource are restored. All the resources that are restored get their name prefixed with the value of the `restoredResourceName` field.

When a backup is restored, the entire VM is restored. After the resources are created, the restoration of application capability is subject to the VM operating system or image.

This document is for developers in platform administrator or application operator groups that manage VM Backup and restore operations. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

Ensure you have an existing backup available. You can [create backups on a schedule](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-plans/create-scheduled-backup-plan) using backup plans, or create backups manually.

### Request IAM roles

To create a restore, ask your Organization IAM Admin to grant you the **Organization Backup Admin** (`organization-backup-admin`) role. This role lets you create, get, list, watch, update, patch, and delete VM backup repositories, VM backup plan templates, VM backup requests, and VM restore requests.

## Create a manual VM backup

Create the `VirtualMachineRestoreRequest` resource using the API:
    
    
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
      targetNamespace: TARGET_NAMESPACE
    

Replace the following:

  * `VM_BACKUP_NAME`: the name of the `VirtualMachineBackup` resource to restore from.
  * `PROJECT_NAME`: the name of the GDC project.
  * `RESTORE_REQUEST_NAME`: the name to give the restore request that is being initiated.
  * `RESTORE_NAME`: the name to give the restore that is being initiated.
  * `RESTORE_PREFIX`: the prefix given to newly created VM resources. The restored VM and VM disk names are prefixed with `restoredResourceName` value in the restore request.
  * `RESTORED_RESOURCE_DESCRIPTION`: a description of the restore being performed.
  * `TARGET_NAMESPACE`: the namespace where the VM is restored. If not provided, the original namespace from the backup is used. Supported only for cluster node VM restorations.



## What's next

  * [Clean up labels after restoring VM-attached disks](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/clean-up-labels-after-restore)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
