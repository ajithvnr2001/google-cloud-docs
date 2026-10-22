---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/tutorial-create-vm/
title: Tutorial: Create and manage a Linux VM in VM Runtime on GDC \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:11.293795+00:00
---

# Tutorial: Create and manage a Linux VM in VM Runtime on GDC  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/tutorial-create-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Tutorial: Create and manage a Linux VM in VM Runtime on GDC Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to create and manage a Linux virtual machine (VM) on a new installation of VM Runtime on GDC. You learn the process to create and define the basic dependencies such as a `StorageClass` and virtual network, then create a VM that uses these resources. You then learn how to edit the VM, such as to add a new disk.

## Objectives

  * Configure basic dependencies 
    * Create a `StorageClass` for VM Runtime on GDC
    * Create a virtual network for your VMs to use
  * Create a virtual machine boot disk
  * Create a VM
  * Edit a VM to add a new virtual disk



## Before you begin

To complete this tutorial, you need access to the following resources and tools:

  * Access to Google Distributed Cloud version 1.12.0 (`anthosBareMetalVersion: 1.12.0`) or higher cluster. You can use any cluster type capable of running workloads. If needed, [try Google Distributed Cloud on Compute Engine](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/try/gce-vms) or see the [cluster creation overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-clusters-overview).
  * The `virtctl` client tool installed as a plugin for `kubectl`. If needed, [install the virtctl client tool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/quickstart#install_the_virtctl_client_tool).



## Create a `StorageClass`

You use a `StorageClass` to define the type of storage you make available to VMs. Different storage classes might map to a different type of storage hardware, file system, or performance.

It's beyond the scope of this tutorial to provide specific instructions for each `StorageClass` and storage partner.

[Google Distributed Cloud Ready storage partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage) provide qualified [Container Storage Interface (CSI)](https://github.com/container-storage-interface/spec) drivers that install and configure the required custom resources for your storage. To install the CSI driver in your cluster, review the list of supported storage partners and follow their instructions.

After you install the CSI driver for your storage platform, one or more storage classes are available in your cluster. You use one of these storage classes to create a virtual hard disk in this tutorial.

The following basic example [NFS `StorageClass`](https://kubernetes.io/docs/concepts/storage/storage-classes/#nfs) uses the [NFS CSI Driver](https://github.com/kubernetes-csi/csi-driver-nfs). You define the NFS server address and path to use in the `StorageClass`. All the nodes in your cluster can then connect to and use this NFS storage:
    
    
      apiVersion: storage.k8s.io/v1
      kind: StorageClass
      metadata:
        name: example-nfs
      provisioner: nfs.csi.k8s.io
      parameters:
        server: nfs-server.example.com
        path: /vm-share
      reclaimPolicy: Delete
      volumeBindingMode: Immediate
      mountOptions:
        - nconnect=8
        - nfsvers=4.1
    

In this tutorial, use the name of a `StorageClass` in your own cluster.

VM Runtime on GDC automatically generates one storage profile for each `StorageClass` in a cluster. The storage profile is the same name as the associated `StorageClass`. Storage profiles provide extra configuration options associated with each `StorageClass`. For more information about storage profiles, including configuration instructions, see [Configure storage profiles](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/storage-classes#configure_storage_profiles).

## Create a virtual network

VMs connect to a virtual network using a virtual network interface. The virtual network lets them communicate with other VMs in the cluster, or to resources outside of the cluster.

In this tutorial, you create a basic Layer 2 (`L2`) virtual network that can use an external DHCP server. When you enable the use of an external DHCP server, you can skip configuration of DNS and gateway settings if they're provided by DHCP.

To create a network that uses an external DHCP server, complete the following steps:

  1. Create a `Network` manifest, such as `dhcp-network.yaml`, in the editor of your choice:
         
         nano dhcp-network.yaml
         

  2. Copy and paste the following YAML manifest:
         
         apiVersion: networking.gke.io/v1
         kind: Network
         metadata:
           name: NETWORK_NAME
         spec:
           type: L2
           nodeInterfaceMatcher:
             interfaceName: INTERFACE_NAME
           externalDHCP4: true
         

Replace the following values:

     * `NETWORK_NAME`: the name for your network.
     * `INTERFACE_NAME`: the interface name on your Google Distributed Cloud node to attach the network to. All nodes should have the same interface name.

In this `Network` manifest, the following values are set:

     * Workloads can have only an `L2` attachment to this network. This is the only network `type` that you can create in VM Runtime on GDC.
     * The network has external DHCP enabled. The external DHCP server is responsible for IPv4 address allocation, routes, gateway, and DNS configuration for workloads connected to this network.
  3. Save and close the `Network` manifest in your editor.

  4. Create the network using `kubectl`:
         
         kubectl apply -f use-dhcp-network.yaml
         




## Create a VM boot disk

A VM can use a precreated disk image, or boot from an ISO image to manually install the OS. These disk images can be stored and accessed using HTTP, or in Cloud Storage and accessed using a `Secret`.

In this tutorial, you create a boot disk from the public Ubuntu Server 20.04 cloud image using HTTP.

To create a disk from an image, complete the following steps.

  1. Create a `VirtualMachineDisk` manifest, such as `my-disk.yaml`, in the editor of your choice:
         
         nano my-disk.yaml
         

  2. Copy and paste the following YAML definition:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachineDisk
         metadata:
           name: DISK_NAME
         spec:
           size: 20Gi
           storageClassName: STORAGE_CLASS_NAME
           source:
             http:
               url: https://cloud-images.ubuntu.com/releases/focal/release/ubuntu-20.04-server-cloudimg-amd64.img
         

Replace the following values:

     * `DISK_NAME`: the name that you want for your disk. This example creates a `20Gi` (20 gibibyte) disk named `DISK_NAME` using a public Ubuntu Server 20.04 image.
     * `STORAGE_CLASS_NAME`: the `StorageClass` that you want to use for your `VirtualMachineDisk`. 
       * Use `kubectl get storageclass` to list what's available in your cluster.
**Note:** It can take 15–20 minutes to download this public image, create the `VirtualMachineDisk`, and apply the OS image to the new disk. The process to create the `VirtualMachineDisk` is much faster when you use a locally stored image. For most production scenarios, use a local HTTP image repository rather than pull from an external public source each time.
  3. Save and close the `VirtualMachineDisk` manifest in your editor.

  4. Create the disk using `kubectl`:
         
         kubectl apply -f my-disk.yaml
         




## Create a VM

With a virtual network and boot disk created in the previous sections, now create a VM. The VM connects to the virtual network, and boots from the virtual disk. The following instructions create a VM by directly applying a `VirtualMachine` YAML manifest file with the `kubectl` CLI.

**Note:** When you create a VM from a YAML manifest, you can configure it to have a custom initialization whenever it starts. For prerequisites and instructions for configuring a new VM with startup routines, see [Configure VM startup routines](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/vm-startup-config).

  1. Create a manifest that defines a `VirtualMachine`, such as `my-vm.yaml`, in the editor of your choice:
         
         nano my-vm.yaml
         

  2. Copy and paste the following YAML definition:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           name: VM_NAME
         spec:
           osType: linux
           compute:
             cpu:
               vcpus: VCPU_NUMBER
             memory:
               capacity: MEMORY_SIZE
           interfaces:
             - name: eth0
               networkName: NETWORK_NAME
               default: true
           disks:
             - boot: true
               virtualMachineDiskName: DISK_NAME
         

Replace the following values:

     * `VM_NAME`: the name for your VM.
     * `VCPU_NUMBER`: The optional number of vCPUs to assign to the VM. Without this setting, the default of 2 vCPUs is assigned. 
       * You can assign between 1 and 96 vCPUs to a VM.
     * `MEMORY_SIZE`: The optional amount of memory to assign to the VM. Without this setting, the default of 4 GiB of memory is assigned. 
       * You can assign between 1M and 1T of memory to a VM. For more information, see [Memory resource units](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#meaning-of-memory).
     * `NETWORK_NAME`: the name of your network created in a previous section.
     * `DISK_NAME`: the name of your boot disk created in the previous section. This disk is set to `boot: true`.
  3. Save and close the manifest in your editor.

  4. Create the VM and disk using `kubectl`:
         
         kubectl apply -f my-vm.yaml
         

  5. It can take a few minutes to create the VM. Check the status of the VM with the kubectl command:
         
         kubectl get gvm VM_NAME
         

The following example output shows the VM in a `Running` state:
         
         NAME    STATUS    AGE   IP
         MY_VM   Running   64s   192.168.2.124
         




## Connect to the VM

When your VM is running, connect to the console of the VM. This console connection lets you perform basic tasks such as to further configure the VM or install an application.

  1. To access a VM from the console, use `kubectl`:
         
         kubectl virt console VM_NAME
         

  2. When prompted, enter the user credentials that you specified to create the VM.

  3. After you successfully connect to the console of the VM, exit the VM session and console:
         
         Ctrl + ]
         




## Edit the VM

During the lifecycle of your VM, you might want to edit your VM. For example, you might want to add storage to install an application on a dedicated disk, or use additional storage for your application.

In this tutorial, create a blank disk and attach it to the VM. This scenario lets you create a data disk to store application data.

  1. Create a `VirtualMachineDisk` manifest, such as `my-data-disk.yaml`, in the editor of your choice:
         
         nano my-data-disk.yaml
         

  2. Copy and paste the following YAML definition:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachineDisk
         metadata:
           name: DATA_DISK_NAME
         spec:
           size: 10Gi
           storageClassName: STORAGE_CLASS_NAME
         

Replace the following values:

     * `DATA_DISK_NAME`: the name that you want for your data disk. This example creates a `10Gi` (10 gibibyte) disk.
     * `STORAGE_CLASS_NAME`: the `StorageClass` that you want to use for your `VirtualMachineDisk`. 
       * Use `kubectl get storageclass` to list what's available in your cluster.
  3. Save and close the disk manifest in your editor.

  4. Create the disk using `kubectl`:
         
         kubectl apply -f my-data-disk.yaml
         

  5. Use `kubectl` to stop your VM before you attach the new virtual disk:
         
         kubectl virt stop VM_NAME
         

  6. Edit your VM resource:
         
         kubectl edit gvm VM_NAME
         

Update the `VirtualMachine` YAML manifest to attach the disk at the end of the VM's `spec.disks` section:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           name: VM_NAME
         spec:
           ...
           disks:
             - boot: true
               virtualMachineDiskName: DISK_NAME
             - virtualMachineDiskName: DATA_DISK_NAME
         

Replace `DATA_DISK_NAME` with the name of your disk created in the previous step.

  7. Save and close the updated VM manifest in your editor.

  8. Use `kubectl` to start the VM:
         
         kubectl virt start VM_NAME
         




## Clean up

To delete the resources created in this tutorial, complete the following steps:

  1. Delete your VM:
         
         kubectl delete -f my-vm.yaml
         

  2. Delete your `VirtualMachineDisk` resources:
         
         kubectl delete -f my-data-disk.yaml
         kubectl delete -f my-disk.yaml
         




If you don't want to keep the basic dependencies in your cluster, complete the following steps:

  1. Delete your virtual network:
         
         kubectl delete -f use-dhcp-network.yaml
         

  2. To remove the CSI driver from your cluster, follow the instructions from your storage partner.




## What's next

  * [Create and use storage classes in Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/storage-classes)
  * [Create and use virtual networks in Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/create-networks)
  * [Create and manage virtual disks in Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/create-manage-disks)
  * [Edit VMs in Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/edit-vm)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
