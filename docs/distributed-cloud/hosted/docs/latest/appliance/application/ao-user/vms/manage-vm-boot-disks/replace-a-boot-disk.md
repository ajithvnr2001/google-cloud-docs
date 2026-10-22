---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vm-boot-disks/replace-a-boot-disk/
title: Replace a boot disk \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:51.916530+00:00
---

# Replace a boot disk  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vm-boot-disks/replace-a-boot-disk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Replace a boot disk Stay organized with collections  Save and categorize content based on your preferences. 

This document contains instructions to replace a boot disk in Google Distributed Cloud (GDC) air-gapped appliance. If you need to create a boot disk before your replacement, see the [Create a boot disk](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vm-boot-disks/create-customized-boot-disk) page.

You can detach boot disks from your virtual machine (VM) instance and attach new boot disks to it. To repair boot disks, you mount them to another VM instance without deleting the original one. Also, instead of recreating an entire VM instance, you can replace its boot disks.

**Note:** If you try to start a VM instance without a boot disk, you get an error, but you can edit other instance properties.

## Before you begin

To use `gdcloud` command-line interface (CLI) commands, ensure that you have downloaded, installed, and configured the [`gdcloud` CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview). All commands for GDC air-gapped appliance use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.

### Get the kubeconfig file path

To run commands against the Management API server, ensure you have the following resources:

  1. Locate the Management API server name, or ask your Platform Administrator (PA) what the server name is.

  2. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#cli) the kubeconfig file for the Management API server if you don't have one.

  3. Use the path to replace `MANAGEMENT_API_SERVER{"</var>"}}` in these instructions.

  4. Obtain access to VM disks. Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/preparation#verify-user-access) that you have the required Project VM Admin role.




### Request permissions and access

To perform the tasks listed in this page, you must have the Project VirtualMachine Admin role. Follow the steps to either [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/preparation#verify-user-access) or have your Project IAM Admin [assign](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/preparation#grant-user-access-vm-resources) you the Project VirtualMachine Admin (`project-vm-admin`) role in the namespace of the project where the VM resides.

For VM operations using the GDC console or the gdcloud CLI, request your Project IAM Admin to assign you both the Project VirtualMachine Admin role and the Project Viewer (`project-viewer`) role.

## Restrictions

You have the following restrictions when replacing a boot disk:

  * Attach or detach a boot disk only from a [stopped VM instance](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#stop-a-vm).
  * Attach only one boot disk for each VM instance.
  * Attach only existing boot disks to a VM instance.
  * Replace the boot disk only with a new bootable disk.



## Replace a boot disk

Replace a boot disk by using the GDC console or the `kubectl` CLI.

###  Console 

  1. In the navigation menu, click **Virtual Machines > Instances**.

  2. In the list of VMs, click a VM name to view its details.

  3. Click **Replace boot disk**.

  4. In the confirmation dialog, click **Stop** to stop the VM.

  5. Wait a few minutes for the VM to stop.

  6. Click **Refresh**.

  7. When the VM is in a stopped state, click **Replace boot disk** again.

  8. In the Replace boot disk dialog, choose a new boot disk or an existing boot disk.

     * To provision a new boot disk, click the **New boot disk** tab.

       1. In the **Disk name** field, enter a new disk name that is unique to the project.
       2. In the **Size** field, enter a disk size between 12 and 65536 GiB.
       3. In the **Image name** list, select an image.
       4. In the Deletion rule section, click **Keep disk** or **Delete disk**.
       5. In the **Storage profile** section, choose a profile. The default profile is **Standard**.
     * To choose an existing boot disk, click the **Existing boot disk** tab.

       1. In the **Disk** list, select a disk.
       2. In the Deletion rule section, click **Keep disk** or **Delete disk**.
  9. Click **Save**.

  10. [Restart the VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#restart-a-vm).




###  kubectl 

  1. [Stop the VM instance](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#stop-a-vm).

**Note:** You don't need to unmount the disk.
  2. Open the current `spec.disks` value to change it for the new virtual machine disk:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER edit virtualmachines.virtualmachine.gdc.goog --namespace PROJECT VM_NAME
         

Replace the variables, using the following definitions.

Variable| Definition  
---|---  
`MANAGEMENT_API_SERVER` | The Management API server `kubeconfig` file.  
`PROJECT` | The GDC project where you want to replace the boot disk.  
`VM_NAME` | The VM name.  
  3. Modify the boot disk in the config file by replacing `VM_BOOT_DISK_NAME` with the new VM boot disk name:
         
         disks:
         - virtualMachineDiskRef:
             name: VM_BOOT_DISK_NAME
           boot: true
         

The result must look like the following example:
         
         disks:
         - virtualMachineDiskRef: 
             name: NEW_VM_BOOT_DISK_NAME
           boot: true
         

  4. [Restart the VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#restart-a-vm).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
