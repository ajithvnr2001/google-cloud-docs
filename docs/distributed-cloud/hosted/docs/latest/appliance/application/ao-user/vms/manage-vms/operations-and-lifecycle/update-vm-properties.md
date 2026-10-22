---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/update-vm-properties/
title: Update VM properties \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:26.537025+00:00
---

# Update VM properties  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/update-vm-properties/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Update VM properties Stay organized with collections  Save and categorize content based on your preferences. 

This page describes which virtual machine (VM) properties you can update for an existing VM and how to perform such an update.

## Before you begin

To use `gdcloud` command-line interface (CLI) commands, ensure that you have downloaded, installed, and configured the [`gdcloud` CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview). All commands for GDC air-gapped appliance use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.

### Get the kubeconfig file path

To run commands against the Management API server, ensure you have the following resources:

  1. Locate the Management API server name, or ask your Platform Administrator (PA) what the server name is.

  2. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#cli) the kubeconfig file for the Management API server if you don't have one.

  3. Use the path to replace `MANAGEMENT_API_SERVER{"</var>"}}` in these instructions.




### Request permissions and access

To perform the tasks listed in this page, you must have the Project VirtualMachine Admin role. Follow the steps to either [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/preparation#verify-user-access) or have your Project IAM Admin [assign](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/preparation#grant-user-access-vm-resources) you the Project VirtualMachine Admin (`project-vm-admin`) role in the namespace of the project where the VM resides.

For VM operations using the GDC console or the gdcloud CLI, request your Project IAM Admin to assign you both the Project VirtualMachine Admin role and the Project Viewer (`project-viewer`) role.

## Updatable properties

You can only change the properties that are in the `spec` of the VM.

### View updatable properties

Find properties you want to change by using the GDC console or `kubectl`.

###  Console 

  1. In the navigation menu, click **Virtual Machines > Instances**.

  2. In the list of VMs, click a VM name to view its properties.

  3. Editable properties have an _edit_ **Edit** icon.




###  kubectl 

  1. View the list of properties for the VM `spec` and the valid values corresponding to each property:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER explain virtualmachines.virtualmachine.gdc.goog.spec
         

The output is similar to the following:
         
         KIND:     VirtualMachine
         VERSION:  virtualmachine.gdc.goog/v1
         
         RESOURCE: spec <Object>
         
         DESCRIPTION:
              Defines the specification of the Virtual Machine.
         
         FIELDS:
            compute      <Object>
              Specifies the CPU and Memory of the VM. CPU and Memory can be defined
              directly or through the VirtualMachineType. Changes to Compute require a
              reboot to take effect. Compute is immutable when the VM is in `Unknown`
              state.
         
            disks        <[]Object> -required-
              Specifies the list of disks attached to this vm. There must be exactly one
              boot disk. Changes to disk attachments require a reboot to take effect.
         
            ...
         

  2. Recursively view the sub-properties for each property. These examples show the return for the `compute` and the `vcpus` sub-properties:

     * This example command returns the fields for the `compute` sub-property:
           
           kubectl --kubeconfig MANAGEMENT_API_SERVER explain virtualmachines.virtualmachine.gdc.goog.spec.compute
           

The output is similar to the following:
           
           KIND:     VirtualMachine
           VERSION:  virtualmachine.gdc.goog/v1
           
           RESOURCE: compute <Object>
           
           DESCRIPTION:
                Specifies the CPU and Memory of the VM. CPU and Memory can be defined
                directly or through the VirtualMachineType. Changes to Compute require a
                reboot to take effect. Compute is immutable when the VM is in `Unknown`
                state.
           
           FIELDS:
              memory       <>
                Specifies the amount of physical memory available to the instance. memory
                must have a minimum value of `1G`, and can be up to (including) `400G`.
           
              vcpus        <integer>
                Specifies the number of VCPUs that are available to the instance. Specify
                `vcpus` as an integer. This value must be a multiple of 2, with 2 as the
                minimum and 128 as the maximum allowed.
           
              ...
           

     * This example command returns the fields for the `vcpus` sub-property:
           
           kubectl --kubeconfig MANAGEMENT_API_SERVER explain virtualmachines.virtualmachine.gdc.goog.spec.compute.vcpus
           

The output is similar to the following:
           
           KIND:     VirtualMachine
           VERSION:  virtualmachine.gdc.goog/v1
           
           FIELD:    vcpus <integer>
           
           DESCRIPTION:
                Specifies the number of VCPUs that are available to the instance. Specify
                `vcpus` as an integer. This value must be a multiple of 2, with 2 as the
                minimum and 128 as the maximum allowed.
           




All of the properties can be updated on a running VM, but often require the VM to be restarted to take effect.

These property updates require that the VM be restarted for the changes to take effect:

  * compute
  * disks
  * firmware
  * [startupScripts](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-the-os/startup-script-vm-instance)



These property updates take effect immediately:

  * guestEnvironment
  * runningState



## Update VM properties

Update VM properties by using the GDC console or `kubectl`.

###  Console 

  1. In the navigation menu, click **Virtual Machines > Instances**.

  2. In the list of VMs, click a VM name to view its properties.

  3. Click _edit_ **Edit** next to the property that you want to edit and make your changes.

  4. If you want to replace the boot disk or add a new disk, see [Replace a boot disk](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vm-boot-disks/replace-a-boot-disk) or [Add a disk to a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-storage/add-a-vm-disk).

  5. Click **Save**.




###  kubectl 

  1. Run the following command:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
            edit virtualmachines.virtualmachine.gdc.goog VM_NAME \
            -n PROJECT
         

Replace the variables as defined in the following table.

Variable| Definition  
---|---  
`MANAGEMENT_API_SERVER`| The `kubeconfig` file.  
`VM_NAME`| The VM's name.  
`PROJECT`| The project name.  
  2. Edit the `spec` to update the required fields and values for the updatable properties.

  3. Save the file.

  4. If the property update requires the VM to be restarted, use the [Restart a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#restart-a-vm) instructions to restart the VM.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
