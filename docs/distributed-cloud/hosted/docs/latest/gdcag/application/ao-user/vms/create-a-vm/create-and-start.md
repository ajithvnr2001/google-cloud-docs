---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/create-and-start/
title: Create and start a VM instance \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:38.413031+00:00
---

# Create and start a VM instance  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/create-and-start/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create and start a VM instance Stay organized with collections  Save and categorize content based on your preferences. 

Create a virtual machine (VM) instance using a boot disk image or a boot disk snapshot. You can create a VM with one or more disks, or [add disks](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-storage/add-a-vm-disk) later. Google Distributed Cloud (GDC) air-gapped automatically starts the VM instance when you create it.

You can also add [startup scripts](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-the-os/startup-script-vm-instance) to a VM instance, either before or after you create the instance.

This document is for developers in platform administrator or application operator groups that create and manage VMs in a GDC environment. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

**Note:** Image imports, image listing, and VM instance creation using the gdcloud CLI or the kubectl CLI are zonal operations. When you import or list images, or when you create VMs, you must target the specific zone and zonal management API server where you intend to run the VM.

To use `gdcloud` command-line interface (CLI) commands, ensure that you have downloaded, installed, and configured the [`gdcloud` CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview). All commands for Distributed Cloud use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.

### Get the kubeconfig file path

To run commands against the Management API server, ensure you have the following resources:

  1. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#cli) the kubeconfig file for the Management API server if you don't have one.

  2. Use the path to the kubeconfig file of the Management API server to replace `MANAGEMENT_API_SERVER` in these instructions.




### VM naming guidelines

Refer to the following naming guidelines when creating VM instances:

  * VM names must only contain alphanumeric characters and dashes.
  * Using symbols other than alphanumeric characters and dashes, such as a period, results in connection failures to the VM.
  * The VM name must not be longer than 53 characters.



### Request IAM roles

To get the permissions that you need to create and start a VM instance, ask your Project IAM Admin to grant you the following roles on your project:

  * **Virtual Machine Project Admin** (`project-vm-admin`): create, modify, list, and delete VMs in the project namespace.

  * **Project Viewer** (`project-viewer`): view all resources within project namespaces.

  * **Virtual Machine Image Project Admin** (`project-vm-image-admin`): create, list, and delete GDC-provided and custom VM images in the project namespace.




All VM roles must bind to the namespace of the project where the VM resides. Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation#verify-user-access) your access.

## Create a VM instance from an image

This section describes how to create a VM from either a GDC-provided OS image or from a custom OS image.

### View a list of available GDC-provided images

Before you create a VM using a GDC-provided image, review the list of available images. See [supported VM images](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/supported-vm-images) for more information about GDC-provided images.

###  gdcloud 

  * List all available images and their minimum disk size:
        
        gdcloud compute images list
        

This command includes both GDC-provided and custom images. Choose either image in the `vm-system` namespace.




###  API 

  1. List all available GDC-provided images:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n vm-system \
           get virtualmachineimage.virtualmachine.gdc.goog
         

  2. Get the `minimumDiskSize` for a particular GDC-provided image:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n vm-system \
           get virtualmachineimage.virtualmachine.gdc.goog BOOT_DISK_IMAGE_NAME \
           -ojsonpath='{.spec.minimumDiskSize}{"\n"}'
         

Replace the following:

     * `MANAGEMENT_API_SERVER`: the kubeconfig file for the management API server.
     * `BOOT_DISK_IMAGE_NAME`: the name of the image.



### Create a VM instance from a GDC-provided image

By default, all GDC projects can create VMs from GDC-provided OS images.

###  Console 

  1. In the navigation menu, select **Virtual Machines > Instances**.
  2. Click **Create Instance**.
  3. In the **Name** field, specify a name for the VM.
  4. Select the zone in which to create the VM.
  5. Optional: Click **Add Labels** to assign any labels to the VM. This helps organize your VM instances.
  6. Select the machine configuration to use for the VM: 
     1. **General-purpose** : make sure the machine type aligns with your workload requirements.
     2. **Custom** : set the number of cores and memory requirements for your machine.
  7. Click **Next**.
  8. If you want to enable external access, select **Allow external access**.
  9. Click **Next**.
  10. In the **Boot disk** section, GDC automatically adds a boot disk with default configurations. You can keep this configuration as is, or click **Change** to modify the default configurations: 
     1. In the **Disk details** section, modify the **Disk name**.
     2. In the **Disk settings** section, modify the **Size** value.
     3. In the **Source image** section, click the **Image name** menu and select one of the images.
     4. Select or deselect **Turn on Secure Boot**. If using a Windows image, you must have Secure Boot enabled.
     5. Select either **Keep disk** or **Delete disk** to configure your disk deletion rule.
     6. Click **Save**.
  11. Click **Create** to create the VM instance.



###  gdcloud 

**Note:** Creating a VM from an image using the gdcloud CLI is a zonal operation. Ensure that your gdcloud CLI target matches the specific zone where you imported or listed your image.

  1. Select a GDC-provided image to create the VM instance in your target zone:
         
         gdcloud compute instances create VM_NAME \
           --machine-type=MACHINE_TYPE \
           --image=BOOT_DISK_IMAGE_NAME \
           --image-project=vm-system \
           --boot-disk-size=BOOT_DISK_SIZE \
           --no-boot-disk-auto-delete=NO_BOOT_DISK_AUTO_DELETE
         

Replace the following:

Variable| Definition | `VM_NAME` | The name of the new VM. The name can contain up to 53 alphanumeric characters and dashes.  
---|---  
`MACHINE_TYPE` | The predefined machine type for the new VM. To select an available machine type, run the following:  
` gdcloud compute machine-types list `  
`BOOT_DISK_IMAGE_NAME` | The name of the image to use for the new VM boot disk.  
`BOOT_DISK_SIZE` | The size of the boot disk, such as `20GB`.  
This value must always be greater than or equal to the `minimumDiskSize` of the boot disk image.  
`NO_BOOT_DISK_AUTO_DELETE` | Specify `true` to keep the boot disk when you delete the VM instance, or `false` to delete the boot disk automatically.  



###  API 

**Note:** Creating a VM using the API is a zonal operation. Ensure that `MANAGEMENT_API_SERVER` points to the kubeconfig file of the zonal management API server for the zone where you want to create the VM.

  1. Select a GDC-provided image to create the VM instance in your target zone:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT \
           apply -f - <<EOF
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

Variable| Definition | `MANAGEMENT_API_SERVER` | The management API server kubeconfig file.  
---|---  
`PROJECT` | The GDC project to create the VM.  
`VM_BOOT_DISK_NAME` | The name of the new VM boot disk.  
`BOOT_DISK_IMAGE_NAME` | The name of the image to use for the new VM boot disk.  
`BOOT_DISK_SIZE` | The size of the boot disk, such as `20Gi`.  
This value must always be greater than or equal to the `minimumDiskSize` of the boot disk image.  
`VM_NAME` | The name of the new VM. The name can contain up to 53 alphanumeric characters and dashes.  
`MACHINE_TYPE` | The predefined machine type for the new VM. To select an available machine type, run the following:  
` kubectl --kubeconfig MANAGEMENT_API_SERVER get virtualmachinetype.virtualmachine.gdc.goog --namespace vm-system `  
`BOOT_DISK_AUTO_DELETE` | Specify `true` to automatically delete the boot disk when you delete the VM instance, or `false` to keep it.  
  2. Verify successful VM creation and wait for the VM to show the `Running` state. The `Running` state does not indicate that the OS is fully ready and accessible.
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT \
           get virtualmachine.virtualmachine.gdc.goog VM_NAME
         

Replace `VM_NAME` and `PROJECT` with the name and project of the VM.

To add a startup script to your VM instance creation, follow the steps provided on the [Use a startup script with a VM instance](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-the-os/startup-script-vm-instance) page. Ensure you shut down the VM before you add the script.




### Create a VM instance from a custom image

A custom image belongs exclusively to your project. To create a VM with a custom image, you must first [create a custom image](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-custom-images/create-custom-images) in the same project.

###  Console 

  1. In the navigation menu, select **Virtual Machines > Instances**.
  2. Click **Create Instance**.
  3. In the **Name** field, specify a name for the VM.
  4. Select the zone in which to create the VM.
  5. Optional: Click **Add Labels** to assign any labels to the VM. This helps organize your VM instances.
  6. Select the machine configuration to use for the VM: 
     1. **General-purpose** : make sure the machine type aligns with your workload requirements.
     2. **Custom** : set the number of cores and memory requirements for your machine.
  7. Click **Next**.
  8. Select the **Allow external access** checkbox to enable external access for your VM instance.
  9. Click **Next**.
  10. In the **Boot disk** section, GDC automatically adds a boot disk with default configurations. You can keep this configuration as is, or click **Change** to modify the default configurations:

     1. In the **Disk details** section, modify the **Disk name**.
     2. In the **Disk settings** section, modify the **Size** value.
     3. In the **Source image** section, click the **Image name** menu and select one of the images with the **Created by customer** subtext.
     4. Select or deselect **Turn on Secure Boot**. If using a Windows image, you must have Secure Boot enabled.

**Important:** To avoid boot errors in Unified Extensible Firmware Interface (UEFI) mode, verify that your custom image is UEFI-compatible before you turn on Secure Boot. A UEFI-compatible image requires a GUID Partition Table (GPT) and a FAT32-formatted EFI System Partition (ESP) with a properly structured boot loader.
     5. Select either **Keep disk** or **Delete disk** to configure your disk deletion rule.

     6. Click **Save**.

  11. Click **Create** to create the VM instance.




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

Variable| Definition | `VM_NAME` | The name of the new VM. The name can contain up to 53 alphanumeric characters and dashes.  
---|---  
`MACHINE_TYPE` | The predefined machine type for the new VM. To select an available machine type, run the following:  
` gdcloud compute machine-types list `  
`BOOT_DISK_IMAGE_NAME` | The name of the image to use for the new VM boot disk.  
`BOOT_DISK_SIZE` | The size of the boot disk, such as `20GB`.  
This value must always be greater than or equal to the `minimumDiskSize` of the boot disk image.  
`NO_BOOT_DISK_AUTO_DELETE` | Specify `true` to keep the boot disk when you delete the VM instance, or `false` to delete the boot disk automatically.  



###  API 

  1. List all custom images:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT \
           get virtualmachineimage.virtualmachine.gdc.goog
         

Get the `minimumDiskSize` of a particular image to create a VM instance:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT \
           get virtualmachineimage.virtualmachine.gdc.goog BOOT_DISK_IMAGE_NAME \
           -ojsonpath='{.spec.minimumDiskSize}{"\n"}'
         

Replace the following:

Variable| Definition | `MANAGEMENT_API_SERVER` | The management API server kubeconfig file.  
---|---  
`PROJECT` | The project of the image.  
`BOOT_DISK_IMAGE_NAME` | The name of the custom image.  
  2. Create the VM instance:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT \
           apply -f - <<EOF
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
         

Replace the following:

Variable| Definition | `MANAGEMENT_API_SERVER` | The management API server kubeconfig file.  
---|---  
`PROJECT` | The GDC project to create the VM.  
`VM_BOOT_DISK_NAME` | The name of the new VM boot disk.  
`BOOT_DISK_IMAGE_NAME` | The name of the image to use for the new VM boot disk.  
`BOOT_DISK_SIZE` | The size of the boot disk, such as `20Gi`.  
This value must always be greater than or equal to the `minimumDiskSize` of the boot disk image.  
`VM_NAME` | The name of the new VM. The name can contain up to 53 alphanumeric characters and dashes.  
`MACHINE_TYPE` | The predefined machine type for the new VM. To select an available machine type, run the following:  
` kubectl --kubeconfig MANAGEMENT_API_SERVER get virtualmachinetype.virtualmachine.gdc.goog --namespace vm-system `  
`BOOT_DISK_AUTO_DELETE` | Specify `true` to automatically delete the boot disk when you delete the VM instance, or `false` to keep it.  
  3. Verify successful VM creation and wait for the VM to show that it's in the `Running` state. Being in the `Running` state doesn't mean that the OS is fully ready and accessible.
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT \
           get virtualmachine.virtualmachine.gdc.goog VM_NAME
         

Replace `VM_NAME` and `PROJECT` with the name and project of the VM.




### Create a VM instance with additional non-boot disks

You can create non-boot disks when you create a VM. Each additional disk can either specify an image source or not. The latter case is for creating a blank disk.

###  Console 

  1. In the navigation menu, select **Virtual Machines > Instances**.
  2. Click **Create Instance**.
  3. In the **Name** field, specify a name for the VM.
  4. Select the zone in which to create the VM.
  5. Optional: Click **Add Labels** to assign any labels to the VM. This helps organize your VM instances.
  6. Select the machine configuration to use for the VM: 
     1. **General-purpose** : make sure the machine type aligns with your workload requirements.
     2. **Custom** : set the number of cores and memory requirements for your machine.
  7. Click **Next**.
  8. Select the **Allow external access** checkbox to enable external access for your VM instance.
  9. Click **Next**.
  10. In the **Boot disk** section, GDC automatically adds a boot disk with default configurations. You can keep this configuration as is, or click **Change** to modify the default configurations: 
     1. In the **Disk details** section, modify the **Disk name**.
     2. In the **Disk settings** section, modify the **Size** value.
     3. In the **Source image** section, click the **Image name** menu and select one of the images.
     4. Select or deselect **Turn on Secure Boot**. If using a Windows image, you must have Secure Boot enabled.
     5. Select either **Keep disk** or **Delete disk** to configure your disk deletion rule.
     6. Click **Save**.
  11. To add more disks to your VM instance, select **Add New Disk** : 
     1. Assign your VM disk a name.
     2. Configure your disk size and attachment settings.
     3. Click **Save**.
  12. Click **Create** to create the VM instance.



###  gdcloud 

  1. Create a boot disk from an image:
         
         gdcloud compute disks create VM_BOOT_DISK_NAME \
           --size=BOOT_DISK_SIZE \
           --image=BOOT_DISK_IMAGE_NAME \
           --image-project=BOOT_DISK_IMAGE_NAMESPACE
         

  2. Create an additional non-boot disk from an image:
         
         gdcloud compute disks create NON_BOOT_DISK_FROM_IMAGE \
           --size=NON_BOOT_DISK_SIZE \
           --image=NON_BOOT_DISK_IMAGE_NAME \
           --image-project=NON_BOOT_DISK_IMAGE_NAMESPACE
         

  3. Create the blank non-boot disk:
         
         gdcloud compute disks create NON_BOOT_BLANK_DISK \
           --size=NON_BOOT_BLANK_DISK_SIZE
         

  4. Create an instance with the disks from the previous steps:
         
         gdcloud compute instances create VM_NAME \
           --machine-type=MACHINE_TYPE \
           --disk=name=VM_BOOT_DISK_NAME,boot=true \
           --no-boot-disk-auto-delete=NO_BOOT_DISK_AUTO_DELETE \
           --disk=name=NON_BOOT_DISK_FROM_IMAGE \
           --disk=name=NON_BOOT_BLANK_DISK
         

Replace the following:

Variable| Definition  
---|---  
`VM_BOOT_DISK_NAME` | The name of the new VM boot disk.  
`BOOT_DISK_SIZE` | The size of the boot disk, such as `20GB`.  
This value must always be greater than or equal to the `minimumDiskSize` of the boot disk image.  
`BOOT_DISK_IMAGE_NAME` | The name of the image to use for the new VM boot disk.  
`BOOT_DISK_IMAGE_NAMESPACE` | The namespace of the image to use for the new VM boot disk. Use `vm-system` for a GDC-provided image, or leave the field blank for a custom image.  
`NON_BOOT_DISK_FROM_IMAGE` | The name of the additional non-boot disk you create from an image.  
`NON_BOOT_DISK_SIZE` | The size of the additional non-boot disk, for example, `20GB`.  
`NON_BOOT_DISK_IMAGE_NAME` | The name of the image to use for the non-boot disk.  
`NON_BOOT_DISK_IMAGE_NAMESPACE` | The namespace of the image to use for the non-boot disk. Use `vm-system` for a GDC-provided image, or leave the field blank for a custom image.  
`NON_BOOT_BLANK_DISK` | The name of the additional blank non-boot disk.  
`NON_BOOT_BLANK_DISK_SIZE` | The size of the additional blank non-boot disk, for example, `20GB`.  
`VM_NAME` | The name of the new VM. The name can contain up to 53 alphanumeric characters and dashes.  
`MACHINE_TYPE` | The predefined machine type for the new VM. To select an available machine type, run the following:  
` gdcloud compute machine-types list `  
`NO_BOOT_DISK_AUTO_DELETE` | Specify `true` to keep the boot disk when you delete the VM instance, or `false` to delete the boot disk automatically.  



###  API 

  1. Create a VM with a non-boot disk:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT \
           apply -f - <<EOF
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

Variable| Definition | `MANAGEMENT_API_SERVER` | The management API server kubeconfig file.  
---|---  
`PROJECT` | The GDC project to create in the VM.  
`NON_BOOT_DISK_FROM_IMAGE` | The name of the additional non-boot disk you create from an image.  
`NON_BOOT_DISK_IMAGE_NAME` | The name of the image to use for the non-boot disk.  
`NON_BOOT_DISK_IMAGE_NAMESPACE` | The namespace of the image to use for the non-boot disk. Use `vm-system` for a GDC-provided image, or blank for a custom image.  
`NON_BOOT_DISK_SIZE` | The size of the additional non-boot disk you create from an image, for example, `20Gi`.  
`NON_BOOT_BLANK_DISK` | The name of the additional blank non-boot disk.  
`NON_BOOT_BLANK_DISK_SIZE` | The size of the additional blank non-boot disk, for example, `20Gi`.  
`VM_BOOT_DISK_NAME` | The name of the new VM boot disk.  
`BOOT_DISK_IMAGE_NAME` | The name of the image to use for the new VM boot disk.  
`BOOT_DISK_IMAGE_NAMESPACE` | The namespace of the image to use for the new VM boot disk. Use the namespace `vm-system` for a GDC-provided image, or blank for a custom image.  
`BOOT_DISK_SIZE` | The size of the boot disk, such as `20Gi`.  
This value must always be greater than or equal to the `minimumDiskSize` of the boot disk image.  
`VM_NAME` | The name of the new VM. The name can contain up to 53 alphanumeric characters and dashes.  
`MACHINE_TYPE` | The predefined machine type for the new VM. To select an available machine type, run the following:  
` kubectl --kubeconfig MANAGEMENT_API_SERVER get virtualmachinetype.virtualmachine.gdc.goog --namespace vm-system `  
`BOOT_DISK_AUTO_DELETE` | Specify `true` to automatically delete the boot disk when you delete the VM instance, or `false` to keep it.  
  
[Format and mount](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-storage/add-a-vm-disk#format-mount-nonboot-disk) the disks before using them.




## Create a VM from a snapshot or backup

You can create a new VM from a snapshot in the following ways:

  * **Restore a VM boot disk** : If you backed up a boot disk of a VM with a snapshot, use that snapshot to create a new VM. For more information, see [Restore a snapshot](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/restore-backup/restore-from-a-snapshot#restore-from-a-snapshot). 
    * **Restore a non-boot disk:** If you backed up a non-boot disk with a snapshot, you can also restore the snapshot to a new non-boot disk when you create a VM, using the same instructions.



To create more than one VM with the same boot disk, do the following:

  1. [Create a custom image](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-custom-images/create-custom-images).
  2. [Create VMs from that image](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-custom-images/create-custom-images#create-vm-from-custom-image) without using a snapshot.



## Create a VM instance with a specified IP address and subnet

By default, you can create a GDC VM without the network specification. This type of VM attaches to the Default VPC and dynamically assigns an IP address from the default subnet. To create a VM with the default configurations, see Create a VM with a GDC-provided image.

If you don't want to use the default IP address configuration for your GDC VM, you can create a VM with a dynamic or static IP address:

  * Dynamic IP address from a custom subnet: you create a subnet with a specific `CIDR`, and create a VM with an IP address dynamically assigned from that `CIDR`.

  * Static IP address from a custom subnet: you create a subnet with a specific `CIDR`, and create a VM with a static IP address from that `CIDR`.




For more information about subnet creation, see [Subnet and IP addresses in GDC](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/subnets-overview#static-dynamic-cidr).

This section shows you how to create a VM with either a dynamically assigned IP address or with a static IP address.

### Create a VM with a dynamically-assigned IP address from a custom subnet

Create a VM with a dynamically-assigned IP address from a specific `CIDR`:
    
    
       kubectl --kubeconfig MANAGEMENT_API_SERVER \
         -n PROJECT \
         apply -f - <<EOF
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
         network:
           interfaces:
           - network: NETWORK_NAME
             subnet: SUBNET_NAME
       EOF
    

Replace the following variables:

Variable| Definition | `MANAGEMENT_API_SERVER` | The management API server kubeconfig file.  
---|---  
`PROJECT` | The GDC project to create the VM.  
`VM_BOOT_DISK_NAME` | The name of the new VM boot disk.  
`BOOT_DISK_IMAGE_NAME` | The name of the image to use for the new VM boot disk.  
`BOOT_DISK_SIZE` | The size of the boot disk, such as `20Gi`.  
This value must always be greater than or equal to the `minimumDiskSize` of the boot disk image.  
`VM_NAME` | The name of the new VM. The name can contain up to 53 alphanumeric characters and dashes.  
`MACHINE_TYPE` | The predefined machine type for the new VM. Select an available machine type:  
` kubectl --kubeconfig MANAGEMENT_API_SERVER get virtualmachinetype.virtualmachine.gdc.goog --namespace vm-system `  
`BOOT_DISK_AUTO_DELETE` | Specify `true` to automatically delete the boot disk when you delete the VM instance, or `false` to keep it.  
`NETWORK_NAME` | The name of the VPC network, such as `default`.  
`SUBNET_NAME` | The name of the custom subnet.  
  
### Create a VM with a static IP address from a subnet

Create a VM with a static IP address from a custom subnet:
    
    
       kubectl --kubeconfig MANAGEMENT_API_SERVER \
         -n PROJECT \
         apply  -f - <<EOF
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
         network:
           interfaces:
           - network: NETWORK_NAME
             subnet: SUBNET_NAME
             ipAddresses:
             - address: IP_ADDRESS
       EOF
    

Replace the following variables:

Variable| Definition | `MANAGEMENT_API_SERVER` | The management API server kubeconfig file.  
---|---  
`PROJECT` | The GDC project to create the VM.  
`VM_BOOT_DISK_NAME` | The name of the new VM boot disk.  
`BOOT_DISK_IMAGE_NAME` | The name of the image to use for the new VM boot disk.  
`BOOT_DISK_SIZE` | The size of the boot disk, such as `20Gi`.  
This value must always be greater than or equal to the `minimumDiskSize` of the boot disk image.  
`VM_NAME` | The name of the new VM. The name can contain up to 53 alphanumeric characters and dashes.  
`MACHINE_TYPE` | The predefined machine type for the new VM. To select an available machine type, run the following:  
` kubectl --kubeconfig MANAGEMENT_API_SERVER get virtualmachinetype.virtualmachine.gdc.goog --namespace vm-system `  
`BOOT_DISK_AUTO_DELETE` | Specify `true` to automatically delete the boot disk when you delete the VM instance, or `false` to keep it.  
`NETWORK_NAME` | The name of the VPC network, such as `default`.  
`SUBNET_NAME` | The name of the custom subnet.  
`IP_ADDRESS` | The IP address. This must be within the chosen subnet range. You can only specify one IP address in the `ipAddresses` field.  
  
## What's next

  * [Supported VM images](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/supported-vm-images)
  * [Create custom images](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-custom-images/create-custom-images)
  * [Import virtual disks](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-custom-images/import-virtual-disk)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
