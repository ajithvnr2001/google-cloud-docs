---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-a-vm/create-and-start/
title: Create and start a VM instance \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:52.984606+00:00
---

# Create and start a VM instance  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-a-vm/create-and-start/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Create and start a VM instance Stay organized with collections  Save and categorize content based on your preferences. 

This page gives instructions for creating a virtual machine (VM) instance using a boot disk image or a boot disk snapshot.

You can create a VM with one or more disks. You can also [add disks](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-storage/add-a-vm-disk) to your VM after creation. Google Distributed Cloud (GDC) air-gapped appliance automatically starts the VM instance after creation.

You can add startup scripts to a VM, either before or after creation. To read more about startup scripts, see the [Use a startup script with a VM instance](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-the-os/startup-script-vm-instance) page.

## Before you begin

To use `gdcloud` command-line interface (CLI) commands, ensure that you have downloaded, installed, and configured the [`gdcloud` CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview). All commands for GDC air-gapped appliance use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.

### Get the kubeconfig file path

To run commands against the Management API server, ensure you have the following resources:

  1. Locate the Management API server name, or ask your Platform Administrator (PA) what the server name is.

  2. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#cli) the kubeconfig file for the Management API server if you don't have one.

  3. Use the path to replace `MANAGEMENT_API_SERVER{"</var>"}}` in these instructions.


**Important:** VM names must only contain alphanumeric characters and dashes. Using symbols other than alphanumeric characters and dashes, such as a period, results in connection failures to the VM. The VM name must be no longer than 53 characters.

### Request permissions and access

To perform the tasks listed in this page, you must have the Project VirtualMachine Admin role. Follow the steps to either [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/preparation#verify-user-access) or have your Project IAM Admin [assign](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/preparation#grant-user-access-vm-resources) you the Project VirtualMachine Admin (`project-vm-admin`) role in the namespace of the project where the VM resides.

For VM operations using the GDC console or the gdcloud CLI, request your Project IAM Admin to assign you both the Project VirtualMachine Admin role and the Project Viewer (`project-viewer`) role.

## Create a VM instance from an image

This section shows how to create a VM from either a GDC-provided OS image or from a custom OS image.

### View a list of available GDC-provided images

Before you create a VM using a GDC-provided image, review the list of available images.

###  gdcloud 

List all available images and their minimum disk size:
    
    
    gdcloud compute images list
    

This command includes both GDC-provided and custom images. Choose either image in the `vm-system` namespace.

###  API 

  1. List all available GDC-provided images:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
             get virtualmachineimage.virtualmachine.gdc.goog --namespace vm-system
         

  2. Get the `minimumDiskSize` for a particular GDC-provided image:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
             get virtualmachineimage.virtualmachine.gdc.goog --namespace vm-system \
             BOOT_DISK_IMAGE_NAME -ojsonpath='{.spec.minimumDiskSize}{"\n"}'
         

Replace the following:

     * `MANAGEMENT_API_SERVER` with the `kubeconfig` for the Management API server.
     * `BOOT_DISK_IMAGE_NAME` with the name of the image.



### Create a VM instance from a GDC-provided image

By default, all GDC projects can create VMs from GDC-provided OS images.

###  gdcloud 

Select a GDC-provided image to create the VM instance:
    
    
    gdcloud compute instances create VM_NAME \
        --machine-type=MACHINE_TYPE \
        --image=BOOT_DISK_IMAGE_NAME --image-project=vm-system \
        --boot-disk-size=BOOT_DISK_SIZE \
        --no-boot-disk-auto-delete=NO_BOOT_DISK_AUTO_DELETE
    

Replace the following:

Variable| Definition | `VM_NAME` | The name of the new VM. The name must only contain alphanumeric characters and dashes, and be no longer than 53 characters.  
---|---  
`BOOT_DISK_IMAGE_NAME` | The name of the image to use for the new VM boot disk.  
`BOOT_DISK_SIZE` | The size of the boot disk, such as `20G`.  
This value must always be greater than or equal to the `minimumDiskSize` of the boot disk image.  
`NO_BOOT_DISK_AUTO_DELETE` | Either `true` or `false`, indicating the inverse of whether the boot disk is automatically deleted when the VM instance gets deleted.  
`MACHINE_TYPE` | The predefined machine type for the new VM. To select an available machine type, run this command:  
` gdcloud compute machine-types list `  
  
###  API 

  1. Select a GDC air-gapped appliance-provided image to create the VM instance:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
             apply -n PROJECT -f - <<EOF
         apiVersion: virtualmachine.gdc.goog/v1
         kind: VirtualMachineDisk
         metadata:
           name: VM_BOOT_DISK_NAME
         spec:
           source:
             image:
               name: BOOT_DISK_IMAGE_NAME
               namespace: vm-system
           size: BOOT_DISK_SIZE
         ---
         apiVersion: virtualmachine.gdc.goog/v1
         kind: VirtualMachine
         metadata:
           name: VM_NAME
         spec:
           compute:
             virtualMachineType: MACHINE_TYPE
           disks:
             - virtualMachineDiskRef:
                 name: VM_BOOT_DISK_NAME
               boot: true
               autoDelete: BOOT_DISK_AUTO_DELETE
         EOF
         

Replace the following:

Variable| Definition | `MANAGEMENT_API_SERVER` | The Management API server `kubeconfig` path.  
---|---  
`PROJECT` | The GDC air-gapped appliance project to create the VM.  
`VM_NAME` | The name of the new VM. The name must only contain alphanumeric characters and dashes, and be no longer than 53 characters.  
`VM_BOOT_DISK_NAME` | The name of the new VM boot disk.  
`BOOT_DISK_IMAGE_NAME` | The name of the image to use for the new VM boot disk.  
`BOOT_DISK_SIZE` | The size of the boot disk, such as `20G`.  
This value must always be greater than or equal to the `minimumDiskSize` of the boot disk image.  
`BOOT_DISK_AUTO_DELETE` | Either `true` or `false`, indicating whether the boot disk is automatically deleted when the VM instance gets deleted.  
`MACHINE_TYPE` | The predefined machine type for the new VM. To select an available machine type, run this command:  
` gdcloud compute machine-types list `  
  2. Verify that the VM is created and wait for the VM to show that it's in the `Running` state. The `Running` state does not indicate that the OS is fully ready and accessible..
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
             get virtualmachine.virtualmachine.gdc.goog VM_NAME -n PROJECT
         

Replace `VM_NAME` and `PROJECT` with the name and project of the VM. `VM_NAME` must only contain alphanumeric characters and dashes.

To add a startup script to your VM instance creation, follow the steps provided on the [Use a startup script with a VM instance](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-the-os/startup-script-vm-instance) page. Ensure you shut down the VM before you add the script.




### Create a VM instance from a custom image

A custom image belongs exclusively to your project. To create a VM with a custom image, you must first [create a custom image](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-custom-images/create-custom-images) in the same project if you don't already have one.

###  gdcloud 

  1. List all custom images:
         
         gdcloud compute images list --no-standard-images=true
         

  2. Create the VM instance:
         
         gdcloud compute instances create VM_NAME \
             --machine-type=MACHINE_TYPE \
             --image=BOOT_DISK_IMAGE_NAME \
             --boot-disk-size=BOOT_DISK_SIZE \
             --no-boot-disk-auto-delete=NO_BOOT_DISK_AUTO_DELETE
         

Replace the following:

Variable| Definition | `VM_NAME` | The name of the new VM. The name must only contain alphanumeric characters and dashes, and be no longer than 53 characters.  
---|---  
`BOOT_DISK_IMAGE_NAME` | The name of the image to use for the new VM boot disk.  
`BOOT_DISK_SIZE` | The size of the boot disk, such as `20G`.  
This value must always be greater than or equal to the `minimumDiskSize` of the boot disk image.  
`NO_BOOT_DISK_AUTO_DELETE` | Either `true` or `false`, indicating the inverse of whether the boot disk is automatically deleted when the VM instance gets deleted.  
`MACHINE_TYPE` | The predefined machine type for the new VM. To select an available machine type, run this command:  
` gdcloud compute machine-types list `  



###  API 

  1. List all custom images:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
             get virtualmachineimage.virtualmachine.gdc.goog --namespace PROJECT
         

Get the `minimumDiskSize` of a particular image to create a VM instance:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
             get virtualmachineimage.virtualmachine.gdc.goog --namespace PROJECT \
             BOOT_DISK_IMAGE_NAME -ojsonpath='{.spec.minimumDiskSize}{"\n"}'
         

Replace the following:

Variable| Definition | `MANAGEMENT_API_SERVER` | The Management API server `kubeconfig` path.  
---|---  
`BOOT_DISK_IMAGE_NAME` | The name of the image chosen from the command to list all custom images.  
`PROJECT` | The project of the image.  
  2. Create the VM instance:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
             apply -n PROJECT -f - <<EOF
         apiVersion: virtualmachine.gdc.goog/v1
         kind: VirtualMachineDisk
         metadata:
           name: VM_BOOT_DISK_NAME
         spec:
           source:
             image:
               name: BOOT_DISK_IMAGE_NAME
           size: BOOT_DISK_SIZE
         ---
         apiVersion: virtualmachine.gdc.goog/v1
         kind: VirtualMachine
         metadata:
           name: VM_NAME
         spec:
           compute:
             virtualMachineType: MACHINE_TYPE
           disks:
             - virtualMachineDiskRef:
                 name: VM_BOOT_DISK_NAME
               boot: true
               autoDelete: BOOT_DISK_AUTO_DELETE
         EOF
         

Replace the variables using the following definitions:

Variable| Definition | `MANAGEMENT_API_SERVER` | The Management API server `kubeconfig` file.  
---|---  
`PROJECT` | The GDC air-gapped appliance project to create the VM.  
`VM_NAME` | The name of the new VM. The name must only contain alphanumeric characters and dashes, and be no longer than 53 characters.  
`VM_BOOT_DISK_NAME` | The name of the new VM boot disk.  
`BOOT_DISK_IMAGE_NAME` | The name of the image to use for the new VM boot disk.  
`BOOT_DISK_SIZE` | The size of the boot disk, such as `20G`.  
This value must always be greater than or equal to the `minimumDiskSize` of the boot disk image.  
`BOOT_DISK_AUTO_DELETE` | Either `true` or `false`, indicating whether the boot disk is automatically deleted when the VM instance gets deleted.  
`MACHINE_TYPE` | The predefined machine type for the new VM. To select an available machine type, run this command:  
` kubectl --kubeconfig MANAGEMENT_API_SERVER get virtualmachinetype.virtualmachine.gdc.goog --namespace vm-system `  
  3. Verify that the VM is created and wait for the VM to show that it's in the `Running` state. The `Running` state does not indicate that the OS is fully ready and accessible.
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
             get virtualmachine.virtualmachine.gdc.goog VM_NAME -n PROJECT
         

Replace `VM_NAME` and `PROJECT` with the name and project of the VM. `VM_NAME` must only contain alphanumeric characters and dashes.




### Create a VM instance with additional non-boot disks

You can create non-boot disks when you create a VM. Each additional disk can either specify an image source or not. The latter case is for creating a blank disk.

###  gdcloud 

  1. Create a disk from an image:
         
         gdcloud compute disks create NON_BOOT_DISK_FROM_IMAGE \
             --size=NON_BOOT_DISK_SIZE \
             --image=NON_BOOT_DISK_IMAGE_NAME \
             --image-project=NON_BOOT_DISK_IMAGE_NAMESPACE
         

  2. Create a disk from a blank image:
         
         gdcloud compute disks create NON_BOOT_BLANK_DISK \
             --size=NON_BOOT_BLANK_DISK_SIZE \
         

  3. Create an instance with the disks from the previous step:
         
         gdcloud compute instances create VM_NAME \
             --machine-type=MACHINE_TYPE \
             --image=BOOT_DISK_IMAGE_NAME --image-project=vm-system \
             --boot-disk-size=BOOT_DISK_SIZE \
             --no-boot-disk-auto-delete=NO_BOOT_DISK_AUTO_DELETE \
             --disk=name=NON_BOOT_DISK_FROM_IMAGE \
             --disk=name=NON_BOOT_BLANK_DISK
         

Replace the following:

Variable| Definition | `VM_NAME` | The name of the new VM. The name must only contain alphanumeric characters and dashes, and be no longer than 53 characters.  
---|---  
`BOOT_DISK_IMAGE_NAME` | The name of the image to use for the new VM boot disk.  
`BOOT_DISK_IMAGE_NAMESPACE` | The namespace of the image to use for the new VM boot disk. Use `vm-system` for a GDC-provided image, or leave the field blank for a custom image.  
`BOOT_DISK_SIZE` | The size of the boot disk, such as `20G`.  
This value must always be greater than or equal to the `minimumDiskSize` of the boot disk image.  
`NO_BOOT_DISK_AUTO_DELETE` | Either `true` or `false`, indicating the inverse of whether the boot disk is automatically deleted when the VM instance gets deleted.  
`MACHINE_TYPE` | The predefined machine type for the new VM. To select an available machine type, run this command:  
` gdcloud compute machine-types list `  
  
For additional disks, replace the following: 

     * `NON_BOOT_DISK_FROM_IMAGE`, `NON_BOOT_BLANK_DISK`: the name of the additional disk.
     * `NON_BOOT_DISK_SIZE`, `NON_BOOT_BLANK_DISK_SIZE`: the size of the additional disks, for example, `20G`.
     * `NON_BOOT_DISK_IMAGE_NAME`: the name of the image to use as a non-boot disk.
     * `NON_BOOT_DISK_IMAGE_NAMESPACE`: the namespace of the image to use as a non-boot disk. Use `vm-system` for a GDC-provided image, or leave the field blank for a custom image.




###  API 

  1. Create a VM with a non-boot disk:


    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER \
        apply -n PROJECT -f - <<EOF
    apiVersion: virtualmachine.gdc.goog/v1
    kind: VirtualMachineDisk
    metadata:
      name: NON_BOOT_DISK_FROM_IMAGE
    spec:
      source:
        image:
          name: NON_BOOT_DISK_IMAGE_NAME
          namespace: NON_BOOT_DISK_IMAGE_NAMESPACE
      size: NON_BOOT_DISK_SIZE
    ---
    apiVersion: virtualmachine.gdc.goog/v1
    kind: VirtualMachineDisk
    metadata:
      name: NON_BOOT_BLANK_DISK
    spec:
      size: NON_BOOT_BLANK_DISK_SIZE
    ---
    apiVersion: virtualmachine.gdc.goog/v1
    kind: VirtualMachineDisk
    metadata:
      name: VM_BOOT_DISK_NAME
    spec:
      source:
        image:
          name: BOOT_DISK_IMAGE_NAME
          namespace: BOOT_DISK_IMAGE_NAMESPACE
      size: BOOT_DISK_SIZE
    ---
    apiVersion: virtualmachine.gdc.goog/v1
    kind: VirtualMachine
    metadata:
      name: VM_NAME
    spec:
      compute:
        virtualMachineType: MACHINE_TYPE
      disks:
        - virtualMachineDiskRef:
            name: VM_BOOT_DISK_NAME
          boot: true
          autoDelete: BOOT_DISK_AUTO_DELETE
        - virtualMachineDiskRef:
            name: NON_BOOT_DISK_FROM_IMAGE
        - virtualMachineDiskRef:
            name: NON_BOOT_BLANK_DISK
    EOF
    

Replace the following:

Variable| Definition | `MANAGEMENT_API_SERVER` | The Management API server `kubeconfig` path.  
---|---  
`PROJECT` | The GDC project in which you want to create the VM.  
`VM_NAME` | The name of the new VM. The name must only contain alphanumeric characters and dashes, and be no longer than 53 characters.  
`VM_BOOT_DISK_NAME` | The name of the new VM boot disk.  
`BOOT_DISK_IMAGE_NAME` | The name of the image to use for the new VM boot disk.  
`BOOT_DISK_IMAGE_NAMESPACE` | The namespace of the image to use for the new VM boot disk. Use the namespace `vm-system` for a GDC-provided image, or blank for a custom image.  
`BOOT_DISK_SIZE` | The size of the boot disk, such as `20G`.  
This value must always be greater than or equal to the `minimumDiskSize` of the boot disk image. | `BOOT_DISK_AUTO_DELETE` | Either `true` or `false`, indicating whether the boot disk is automatically deleted when the VM instance gets deleted.  
`MACHINE_TYPE` | The predefined machine type for the new VM. To select an available machine type, run this command:  
` kubectl --kubeconfig MANAGEMENT_API_SERVER get virtualmachinetype.virtualmachine.gdc.goog --namespace vm-system `  
  
For additional disks, replace the following: 

  * `NON_BOOT_DISK_FROM_IMAGE`, `NON_BOOT_BLANK_DISK`: the name of the additional disk.
  * `NON_BOOT_DISK_SIZE`, `NON_BOOT_BLANK_DISK_SIZE`: the size of the additional disks, for example, `20G`.
  * `NON_BOOT_DISK_IMAGE_NAME`: the name of the image that you want to use as a non-boot disk.
  * `NON_BOOT_DISK_IMAGE_NAMESPACE`: the namespace of the image that you want to use as a non-boot disk. Use the namespace `vm-system` for a GDC-provided image, or blank for a custom image.



[Format and mount](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-storage/add-a-vm-disk#format-mount-nonboot-disk) the disks before using them.

## Create a VM from a snapshot or backup

You can create a new VM from a snapshot in the following ways:

  * **Restore a VM boot disk** : If you backed up a boot disk of a VM with a snapshot, use that snapshot to create a new VM. See [Restore a snapshot](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/backup-and-restore/restore-from-backup/restore-from-a-snapshot#restore-from-a-snapshot).
  * **Restore a non-boot disk:** If you backed up a non-boot disk with a snapshot, you can also restore the snapshot to a new non-boot disk when you create a VM, using the same instructions.



To create more than one VM with the same boot disk, do the following:

  1. [Create a custom image](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-custom-images/create-custom-images).
  2. [Create VMs from that image](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-custom-images/create-custom-images#create-vm-from-custom-image) without using a snapshot.



## Create a VM without using machine type

GDC air-gapped appliance offers [predefined machine types](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/view-vm-machine-type) that you can use when you create a VM instance. A predefined machine type has a preset number of vCPUs and amount of memory.

If predefined VMs don't meet your needs, create a VM instance with custom virtualized hardware settings.

Custom VMs are ideal in the following scenarios:

  * Workloads that aren't applicable for the predefined VM types.
  * Workloads that require more processing power or more memory but don't need all the upgrades that the next-level machine type provides.




###  gdcloud 

  1. Create a VM with a machine type that you define:
         
         gdcloud compute instances create VM_NAME \
             --custom-cpu=NUM_VCPU \
             --custom-memory=MEMORY
             --image=BOOT_DISK_IMAGE_NAME --image-project=vm-system \
             --boot-disk-size=BOOT_DISK_SIZE \
             --no-boot-disk-auto-delete=NO_BOOT_DISK_AUTO_DELETE
         

Replace the following:

Variable| Definition | `VM_NAME` | The name of the new VM. The name must only contain alphanumeric characters and dashes, and be no longer than 53 characters.  
---|---  
`BOOT_DISK_IMAGE_NAME` | The name of the image to use for the new VM boot disk.  
`BOOT_DISK_SIZE` | The size of the boot disk, such as `20G`.  
This value must always be greater than or equal to the `minimumDiskSize` of the boot disk image.  
`NO_BOOT_DISK_AUTO_DELETE` | Either `true` or `false`, indicating the inverse of whether the boot disk is automatically deleted when the VM instance gets deleted.  
`NUM_VCPU` | The number of vCPUs. The maximum number of vCPUs supported is 192.  
`MEMORY` | The size of memory, such as `8G`. The maximum memory size is one terabyte (TB).  



###  API 

  1. Create a VM with a machine type that you define:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
             apply -n PROJECT -f - <<EOF
         apiVersion: virtualmachine.gdc.goog/v1
         kind: VirtualMachineDisk
         metadata:
           name: VM_BOOT_DISK_NAME
         spec:
           source:
             image:
               name: BOOT_DISK_IMAGE_NAME
               namespace: vm-system
           size: BOOT_DISK_SIZE
         ---
         apiVersion: virtualmachine.gdc.goog/v1
         kind: VirtualMachine
         metadata:
           name: VM_NAME
         spec:
           compute:
             vcpus: NUM_VCPU
             memory: MEMORY
           disks:
             - virtualMachineDiskRef:
                 name: VM_BOOT_DISK_NAME
               boot: true
               autoDelete: BOOT_DISK_AUTO_DELETE
         EOF
         

Replace the following:

Variable| Definition | `MANAGEMENT_API_SERVER` | The Management API server `kubeconfig` path.  
---|---  
`PROJECT` | The GDC air-gapped appliance project to create the VM.  
`VM_NAME` | The name of the new VM. The name must only contain alphanumeric characters and dashes, and be no longer than 53 characters.  
`VM_BOOT_DISK_NAME` | The name of the new VM boot disk.  
`BOOT_DISK_IMAGE_NAME` | The name of the image to use for the new VM boot disk.  
`BOOT_DISK_SIZE` | The size of the boot disk, such as `20G`.  
This value must always be greater than or equal to the `minimumDiskSize` of the boot disk image.  
`BOOT_DISK_AUTO_DELETE` | Either `true` or `false`, indicating whether the boot disk is automatically deleted when the VM instance gets deleted.  
`NUM_VCPU` | The number of vCPUs. The maximum number of vCPUs supported is 192.  
`MEMORY` | The size of memory, such as `8G`. The maximum memory size is one TB.  



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
