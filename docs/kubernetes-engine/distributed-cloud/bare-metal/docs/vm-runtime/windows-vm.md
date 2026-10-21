---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/windows-vm/
title: Create a Windows VM from ISO image in Google Distributed Cloud \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:12:09.669888+00:00
---

# Create a Windows VM from ISO image in Google Distributed Cloud  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/windows-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Create a Windows VM from ISO image in Google Distributed Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to create a Windows virtual machine (VM) that boots from an ISO using VM Runtime on GDC. When the VM boots, you manually complete the Windows setup routine.

You can also create a Windows VM from a prepared disk image [using an HTTP source](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/create-manage-disks#from_image) or [from Cloud Storage](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/create-storage-credentials#use_a_secret_to_import_an_image).

## Before you begin

To complete this document, you need access to the following resources:

  * Access to Google Distributed Cloud version 1.12.0 (`anthosBareMetalVersion: 1.12.0`) or higher cluster. You can use any cluster type capable of running workloads. If needed, [try Google Distributed Cloud on Compute Engine](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/try/gce-vms) or see the [cluster creation overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-clusters-overview).
  * The `virtctl` client tool installed as a plugin for `kubectl`. If needed, [install the virtctl client tool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/quickstart#install_the_virtctl_client_tool).



## Create a virtual disk for the ISO image

To successfully create a Windows VM, follow the steps and sections in this document in order.

To boot from a Windows ISO image, first create a `VirtualMachineDisk` with `diskType` of `cdrom`. Use your Windows ISO as the source for this disk.

  1. Create a `VirtualMachineDisk` manifest, such as `windows-iso.yaml`, in the editor of your choice:
         
         nano windows-iso.yaml
         

  2. Copy and paste the following YAML manifest:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachineDisk
         metadata:
           name: windows-iso
         spec:
           source:
             http:
               url: IMG_URL
           size: 10Gi
           diskType: cdrom
         

Replace `IMG_URL` with the HTTP path to your Windows ISO. You can also [create and use credentials to import an ISO from Cloud Storage](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/create-storage-credentials).

  3. Save and close the manifest in your editor.

  4. Create the `VirtualMachineDisk` using `kubectl`:
         
         kubectl apply -f windows-iso.yaml
         




## Create a VM drivers disk

To successfully boot from a Windows ISO and complete the install process, the VM needs access to the [`virtio` drivers](https://wiki.libvirt.org/page/Virtio). To provide the `virtio` drivers to the VM, complete the following steps:

  1. Create a `VirtualMachineDisk` manifest, such as `virtio-driver.yaml`, in the editor of your choice:
         
         nano virtio-driver.yaml
         

  2. Copy and paste the following YAML manifest:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachineDisk
         metadata:
           name: virtio-driver
         spec:
           size: 1Gi
           source:
             registry:
               url: docker://quay.io/kubevirt/virtio-container-disk:latest
           diskType: cdrom
         

This manifest pulls the latest `virtio` drivers from a public Docker repo and sets the `diskType` as `cdrom`. Your VM uses this disk during the install process.

  3. Save and close the manifest in your editor.

  4. Create the `VirtualMachineDisk` using `kubectl`:
         
         kubectl apply -f virtio-driver.yaml
         




## Create a Windows VM

Create a VM that boots from the Windows ISO `VirtualMachineDisk`, and attaches the `virtio` drivers disk:

  1. Create a manifest that defines a `VirtualMachineDisk` for the boot volume and a `VirtualMachine`, such as `windows-vm.yaml`, in the editor of your choice:
         
         nano windows-vm.yaml
         

  2. Copy and paste the following YAML manifest:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachineDisk
         metadata:
           name: VM_NAME-boot-dv
         spec:
           size: 100Gi
         ---
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           name: VM_NAME
         spec:
           osType: Windows
           disks:
             - virtualMachineDiskName: VM_NAME-boot-dv
               boot: true
             - virtualMachineDiskName: windows-iso
             - virtualMachineDiskName: virtio-driver
           compute:
             cpu:
               vcpus: 2
             memory:
               capacity: 4Gi
           interfaces:
             - name: eth0
               networkName: pod-network
         

Replace `VM_NAME` with the name that you want for your VM.

This manifest creates a _100 Gibibyte (GiB)_ boot volume. As this boot volume is empty when the VM first starts, the VM boots from ISO as a CD-ROM device to start the setup routine. The `virtio` drivers are also attached to complete the install process.

  3. Save and close the manifest in your editor.

  4. Create the `VirtualMachineDisk` and `VirtualMachine` using `kubectl`:
         
         kubectl apply -f windows-vm.yaml
         




## Connect to Windows VM and complete OS install

The VM starts and boots from the Windows ISO in the previous section. Connect to your VM and complete the Windows install process and configure your VM:

  1. Connect to your Windows VM:
         
         kubectl virt vnc VM_NAME
         

Replace `VM_NAME` with the name of your Windows VM.

When prompted, enter your [Windows guest OS user credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/connect-vms#create_initial_user_credentials) for your VM.

For more information about using `kubectl virt vnc` to connect to your VM, see [Connect directly using VNC](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/connect-vms#connect_directly_using_vnc).

  2. In the Windows setup, choose to perform a **Custom install**.

  3. Select **Load driver** , browse to the **viostor** directory on the `virtio` disk, then select the directory that matches the version of Windows you want to install.

For more information, see [KubeVirt Windows `virtio` drivers](https://kubevirt.io/user-guide/virtual_machines/windows_virtio_drivers/).

  4. With the storage and network drivers from `virtio` now available, complete the rest of the Windows install process.

We recommend that you enable Remote Desktop Protocol so you can connect directly to the VM after install.




## Detach the ISO image and drivers disk

After the Windows install is complete, remove the `virtio` drivers disk and Windows ISO image from the VM:

  1. Stop your Windows VM:
         
         kubectl virt stop VM_NAME
         

Replace `VM_NAME` with the name of your Windows VM.

  2. Use `kubectl` to edit the VM:
         
         kubectl edit gvm VM_NAME
         

Replace `VM_NAME` with the name of your Windows VM.

  3. In your editor, update the `spec.disks` section to remove the Windows ISO and `virtio` disks, as shown in the following example. The only disk left attached to the VM should be the `VM_NAME-boot-dv`:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           name: windows-vm
         spec:
           osType: Windows
           disks:
             - virtualMachineDiskName: windows-vm-boot-dv
               boot: true
           interfaces:
         ...
         

  4. Save and close the VM manifest.

  5. Start your Windows VM:
         
         kubectl virt start VM_NAME
         

Replace `VM_NAME` with the name of your Windows VM.

  6. Check the `STATUS` of your VM:
         
         kubectl get gvm VM_NAME
         

Replace `VM_NAME` with the name of your Windows VM.

Make sure that your VM is in a `Running` state. If the VM isn't in a `Running` state, check your `VirtualMachine` resource manifest to make sure you only removed the Windows ISO and `virtio` disk. Check that the host has enough compute resources to start your VM.




## What's next

  * [Connect to VMs](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/connect-vms)
  * [Manage the power state of a VM](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/manage-power-state)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
