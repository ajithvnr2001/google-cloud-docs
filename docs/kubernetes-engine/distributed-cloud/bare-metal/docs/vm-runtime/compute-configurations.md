---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/compute-configurations/
title: Create a VM with specific CPU and memory resources using VM Runtime on GDC \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:00.433226+00:00
---

# Create a VM with specific CPU and memory resources using VM Runtime on GDC  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/compute-configurations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Create a VM with specific CPU and memory resources using VM Runtime on GDC Stay organized with collections  Save and categorize content based on your preferences. 

This document is intended for application owners and platform administrators that run Google Distributed Cloud. This document shows you how to create and use VM types or manually specify CPU and memory resources when you create VMs that use VM Runtime on GDC.

## Before you begin

To complete this document, you need access to the following resources:

  * Access to Google Distributed Cloud version 1.12.0 (`anthosBareMetalVersion: 1.12.0`) or higher cluster. You can use any cluster type capable of running workloads. If needed, [try Google Distributed Cloud on Compute Engine](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/try/gce-vms) or see the [cluster creation overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-clusters-overview).
  * The `virtctl` client tool installed as a plugin for `kubectl`. If needed, [install the virtctl client tool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/quickstart#install_the_virtctl_client_tool).



## Create a VM

When you create a VM, you can manually specify the CPU and memory requirements. This ability lets you create VMs with the appropriate compute resources to match your application needs.

To create a VM and manually specify the CPU and memory requirements, use the following steps.

###  CLI 

  * Use `kubectl` to create a VM:
        
        kubectl virt create vm VM_NAME \
          --image ubuntu20.04 \
          --cpu CPU_NUMBER \
          --memory MEMORY_SIZE
        

Replace the following values:

    * `VM_NAME`: the name for your VM. For more information on name constraints, see [Object names and IDs](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/).
    * `CPU_NUMBER`: The number of virtual CPUs (vCPUs)to assign to the VM. 
      * You can assign between 1 and 96 vCPUs to a VM.
    * `MEMORY_SIZE`: The amount of memory to assign to the VM. 
      * You can assign between 1M and 1T of memory to a VM. For more information, see [Memory resource units](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#meaning-of-memory).
**Note:** In the `~/google-virtctl` directory, a `VM_NAME.yaml` file is created. You can view the content of this file to see the definition of the Kubernetes resources that were created by the VM Runtime on GDC.



###  Manifest 

  1. Create a `VirtualMachine` manifest, such as _my-custom-vm.yaml_ , in the editor of your choice:
         
         nano my-custom-vm.yaml
         

  2. Copy and paste the following YAML manifest:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           name: VM_NAME
         spec:
           compute:
             cpu:
               vcpus: VCPU_NUMBER
             memory:
               capacity: MEMORY_SIZE
           interfaces:
             - name: eth0
               networkName: pod-network
               default: true
           disks:
             - virtualMachineDiskName: VM_NAME-boot-dv
               boot: true
         

In this YAML file, define the following settings:

     * `VM_NAME`: the name for your VM. For more information on name constraints, see [Object names and IDs](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/).
     * `VCPU_NUMBER`: The number of vCPUs to assign to the VM. 
       * You can assign between 1 and 96 vCPUs to a VM.
     * `MEMORY_SIZE`: The amount of memory to assign to the VM. 
       * You can assign between 1M and 1T of memory to a VM. For more information, see [Memory resource units](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#meaning-of-memory).

The VM connects `eth0` to the default `pod-network` network.

The boot disk named `VM_NAME-boot-dv` must already exist. For more information, see [Create and manage virtual disks](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/create-manage-disks).

  3. Save and close the VM manifest in your editor.

  4. Create the VM using `kubectl`:
         
         kubectl apply -f my-custom-vm.yaml
         




## Create and use VM types

When you enable VM Runtime on GDC, a new _VirtualMachineType_ custom resource definition is available. This definition is used to specify CPU and memory resources of a VM. You can create VM types for the different workloads you need, and apply a consistent set of compute resources to VMs based on these types.

If VM Runtime on GDC is enabled in Google Distributed Cloud, the `vm-controller-manager` installs a predefined VM type. The following definition shows the default `example-machinetype` VM type:
    
    
      apiVersion: vm.cluster.gke.io/v1
      kind: VirtualMachineType
      metadata:
        name: "example-machinetype"
        labels:
          vm.cluster.gke.io/predefined-machinetype: "true"
      spec:
        cpu:
          vcpus: 2
        memory:
          capacity: 4G
    

You can't update this predefined VM type. This predefined VM type is re-installed if it doesn't exist in the cluster every time the `vm-controller-manager` is started or restarted, such as if you deleted the VM type.

### Create a VM type

You can create your own VM types to fit the compute needs of your workloads.

  1. Create a `VirtualMachineType` manifest such as _my-vm-type.yaml_ , in the editor of your choice:
         
         nano my-vm-type.yaml
         

  2. Copy and paste the following YAML manifest:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachineType
         metadata:
           name: my-vm-type
         spec:
           cpu:
             vcpus: VCPU_NUMBER
           memory:
             capacity: MEMORY_SIZE
         

In this VM type, you define the following settings:

     * `VM_NAME`: the name for your VM. For more information on name constraints, see [Object names and IDs](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/).
     * `VCPU_NUMBER`: The number of vCPUs to assign to the VM. 
       * You can assign between 1 and 96 vCPUs to a VM.
     * `MEMORY_SIZE`: The amount of memory to assign to the VM. 
       * You can assign between 1M and 1T of memory to a VM. For more information, see [Memory resource units](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#meaning-of-memory).
  3. Save and close the VM type manifest in your editor.

  4. Create the VM type using `kubectl`:
         
         kubectl apply -f my-vm-type.yaml
         




### Create a VM using a VM type

Specify a VM type in your `VirtualMachine` manifest to apply predefined `compute` settings to your VM.

  1. Create a `VirtualMachine` manifest, such as _my-custom-vm.yaml_ , in the editor of your choice.
         
         nano my-custom-vm.yaml
         

  2. Copy and paste the following YAML manifest:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           name: VM_NAME
         spec:
           compute:
             virtualMachineTypeName: my-vm-type
           interfaces:
             - name: eth0
               networkName: pod-network
               default: true
           disks:
             - virtualMachineDiskName: VM_NAME-boot-dv
               boot: true
         

In this YAML file, specify the name of your custom VM type that you created in the previous section, such as `my-vm-type`, as the value for the `virtualMachineTypeName`.

The VM connects `eth0` to the default `pod-network` network.

The boot disk named `VM_NAME-boot-dv` must already exist. For more information, see [Create and manage virtual disks](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/create-manage-disks).

  3. Save and close the VM manifest in your editor.

  4. Create the VM using `kubectl`:
         
         kubectl apply -f my-custom-vm.yaml
         




## What's next

  * [Edit a VM in Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/edit-vm).
  * When you no longer need VMs, [Delete a VM in Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/delete).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
