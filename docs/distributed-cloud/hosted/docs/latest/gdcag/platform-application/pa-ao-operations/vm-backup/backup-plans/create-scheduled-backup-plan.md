---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-plans/create-scheduled-backup-plan/
title: Create a scheduled backup plan \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:17.130303+00:00
---

# Create a scheduled backup plan  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-plans/create-scheduled-backup-plan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create a scheduled backup plan Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create scheduled backup plans to back up virtual machine (VM) workloads on a defined schedule in Google Distributed Cloud (GDC) air-gapped.

Backup plans provide the configuration and location for backups. A backup plan contains a backup configuration including the source VM and the selection of which VM to back up. Backup plans define a regular schedule for which backups of VMs occur. Every VM-based backup plan references the target VM or VM disk resources to be backed up using a label selector defined in a `ProtectedApplication` resource.

This document is for developers in platform administrator or application operator groups that manage VM backup operations. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To create VM backup plans, you must have the following:

  * An [existing backup repository](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-repository/create-backup-repository).



### Request IAM roles

To manage the lifecycle of VM backup resources, including creating, viewing, and deleting backup and restore plans within user clusters, ask your Organization IAM Admin to [grant you](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/set-up-role-bindings) the **Organization Backup Admin** (`organization-backup-admin`) role. This role lets you configure and execute VM data protection strategies.

## Create a backup plan template for VMs

**Deprecated:** The `VirtualMachineBackupPlanTemplate` resource is deprecated in release 1.18. GDC supports existing template resources, but you can't create new backup plans with the `VirtualMachineBackupPlanTemplate` resource. Instead, use the direct `backupRepository` reference in `VirtualMachineBackupPlan` to create backup plans. 

To plan your backups, create a `VirtualMachineBackupPlanTemplate` custom resource. Here's an example of a `VirtualMachineBackupPlanTemplate`:
    
    
       apiVersion: virtualmachine.gdc.goog/v1
       kind: VirtualMachineBackupPlanTemplate
       metadata:
         name: BACKUP_TEMPLATE_NAME
         namespace: PROJECT_NAME
       spec:
         backupRepository: "BACKUP_REPOSITORY_NAME"
    

Replace the following:

  * `BACKUP_TEMPLATE_NAME`: the name of backup plan template.
  * `PROJECT_NAME`: the name of the project to create the template within.

  * `BACKUP_REPOSITORY_NAME`: the name of the repository created in the previous section.




## Create a defined backup plan for VMs

**Note:** This backup method is only supported through the API.

To create VM backups on a defined schedule that have a scope specified, you must create a `VirtualMachineBackupPlan` resource using the API. This resource specifies the scope of the VM backup and the cron schedule that defines the frequency of backup creation.

Set the scope of the VM backup plan in two ways:

  * Use a list: Specify the virtual machines or virtual machine disks to back up in the form of a list. These backup targets are listed in the fields `selectedVirtualMachines` and `selectedVirtualMachineDisks`.
  * Use a label: Provide a label that selects all virtual machines or virtual machine disks that contain that label value. Any matching VMs are backed up by this backup plan.



### Create a VM backup plan using a list

To create a VM backup plan using the list method, specify the backup targets in the `selectedVirtualMachines` and `selectedVirtualMachineDisks` fields:
    
    
    apiVersion: virtualmachine.gdc.goog/v1
    kind: VirtualMachineBackupPlan
    metadata:
        name: BACKUP_PLAN_NAME
        namespace: BACKUP_PLAN_NAMESPACE
    spec:
        virtualMachineBackupPlanTemplate: BACKUP_TEMPLATE_NAME
        backupConfig:
            backupScope:
                selectedVirtualMachines:
                    - resourceName: VM_NAME
                selectedVirtualMachineDisks:
                    - resourceName: VM_DISK_NAME
            volumeStrategy: VOLUME_STRATEGY
        backupSchedule:
            cronSchedule: CRON_SCHEDULE
            paused: false
            maxConcurrency: MAX_CONCURRENCY
    

Replace the following:

  * `BACKUP_PLAN_NAME`: the name of the backup plan.
  * `BACKUP_PLAN_NAMESPACE`: the namespace containing the backup plan.
  * `BACKUP_TEMPLATE_NAME`: the virtual machine backup plan template that points to the relevant backup repository created in Create a VM backup plan template.
  * `VM_NAME`: the VM names as a list in the `selectedVirtualMachines` field. This list of VMs is backed up by the virtual machine backup plan. If more than one VM is specified, you must list the VM names using the following format:
        
        selectedVirtualMachines:
            - resourceName: "virtualmachine"
            - resourceName: "virtualmachine-2"
            ...
            - resourceName: "virtualmachine-n"
        

  * `VM_DISK_NAME`: the VM disks to back up by the virtual machine backup plan. If you need to specify more than one VM disk, you must list the disks in the following format:
        
        selectedVirtualMachineDisks:
            - resourceName: "disk-1"
            - resourceName: "disk-2"
            ...
            - resourceName: "disk-n"
        

  * `VOLUME_STRATEGY`: the type of volume backup to perform. You must use one of the following values:

    * `ProvisionerSpecific`: leverages the backup and restore capabilities of the underlying storage provisioner. Use this option if `includeVolumeData` is `true`.
    * `LocalSnapshotOnly`: creates a point-in-time copy of the volume only on the local storage system itself.
  * `CRON_SCHEDULE`: the cron expression that defines the chosen backup schedule. For example, a cron value of `0 */12 * * *` creates a backup every 12 hours. The minimum interval between scheduled backups is 10 minutes.

  * `MAX_CONCURRENCY`: specifies the maximum number of active scheduled backups that can exist under a backup plan at the same time. If specified, no more than this number of scheduled backups from this backup plan can be in the active state at any given time. If not specified, it defaults to 2. The value must be between 1 and 7.




### Create a VM backup plan using a label

To create a VM backup plan using the label method, specify a label in `vmResourceLabelSelector` field that matches the target VMs you want to back up:

**Warning:** When referencing VM labels in the `vmResourceLabelSelector` field, you must prepend the prefix `user-label.gpc.gke.io/` to the label key. For example, if you assign the label `app: backend` to a VM, you must specify `user-label.gpc.gke.io/app: backend` in `vmResourceLabelSelector` to successfully match the VM. This prefix is specific to VMs and doesn't apply to any other workloads.
    
    
    apiVersion: virtualmachine.gdc.goog/v1
    kind: VirtualMachineBackupPlan
    metadata:
        name: BACKUP_PLAN_NAME
        namespace: BACKUP_PLAN_NAMESPACE
    spec:
        virtualMachineBackupPlanTemplate: BACKUP_TEMPLATE_NAME
        backupConfig:
            backupScope:
                vmResourceLabelSelector:
                    KEY: VALUE
            volumeStrategy: VOLUME_STRATEGY
        backupSchedule:
            cronSchedule: CRON_SCHEDULE
            paused: false
            maxConcurrency: MAX_CONCURRENCY
    

Replace the following:

  * `BACKUP_PLAN_NAME`: the name of the backup plan.
  * `BACKUP_PLAN_NAMESPACE`: the namespace containing the backup plan.
  * `BACKUP_TEMPLATE_NAME`: the virtual machine backup plan template that points to the relevant backup repository created in Create a VM backup plan template.
  * `KEY: VALUE`: the label selector that matches the given labels to any VMs that contain that label. Any matching VMs found in the same namespace are backed up by this backup plan. This object must be in the format `keys:string, values:string`.
  * `VOLUME_STRATEGY`: the type of volume backup to perform. You must use one of the following values: 
    * `ProvisionerSpecific`: leverages the backup and restore capabilities of the underlying storage provisioner. Use this option if `includeVolumeData` is `true`.
    * `LocalSnapshotOnly`: creates a point-in-time copy of the volume only on the local storage system itself.
  * `CRON_SCHEDULE`: the cron expression that defines the chosen backup schedule. For example, a cron value of `0 */12 * * *` creates a backup every 12 hours.
  * `MAX_CONCURRENCY`: specifies the maximum number of active scheduled backups that can exist under a backup plan at the same time. If specified, no more than this number of scheduled backups from this backup plan can be in the active state at any given time. If not specified, it defaults to 2. The value must be between 1 and 7.



## View a backup plan

View a backup plan using the GDC console or `kubectl`.

### Console

View a list of backup plans using the GDC console.

  1. Sign into the GDC console.
  2. In the navigation menu, click **Backup for Virtual Machines > Backup plans**.
  3. Select a project.
  4. Click a backup plan in the list to view its details.



### kubectl

View a backup plan by listing the backup plans and viewing their details using `kubectl`.

  1. List the existing backup plans:
         
         kubectl get backupplans.backup.gdc.goog -n PROJECT_NAME
         

  2. In the list, find the backup plan that you want to view.

  3. View the backup plan details:
         
         kubectl describe backupplans.backup.gdc.goog BACKUP_PLAN_NAME -n PROJECT_NAME
         

Replace the following:

     * `BACKUP_PLAN_NAME`: the name of the backup plan.
     * `PROJECT_NAME`: the name of the project.



## What's next

  * [Manage backups](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-plans/manage-backups)
  * [Create a restore](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/restore-backup/create-restore-scoped)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
