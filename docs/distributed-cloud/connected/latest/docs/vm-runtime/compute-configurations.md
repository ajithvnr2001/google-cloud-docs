---
url: https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/vm-runtime/compute-configurations/
title: Create a VM with specific CPU and memory resources \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:04:41.352826+00:00
---

# Create a VM with specific CPU and memory resources  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/vm-runtime/compute-configurations/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.13.0 (Latest) ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/overview)



Send feedback 

#  Create a VM with specific CPU and memory resources Stay organized with collections  Save and categorize content based on your preferences. 

When you create VMs that use VM Runtime on Google Distributed Cloud, you can configure compute resources in two ways:

  * Manually specify CPU and memory: Define compute resources directly in the `VirtualMachine` manifest. This approach is useful for one-time VMs or custom workloads that require unique resource allocations.
  * Create and use VM types: Define reusable `VirtualMachineType` custom resources that standardize CPU and memory allocations. This approach is useful for managing fleets of VMs, ensuring compute consistency across your cluster, and simplifying VM provisioning for developers.



## Before you begin

To manually specify CPU and memory resources and to create and use VM types, you need access to the following resources:

  * A Distributed Cloud connected cluster, version 1.9.0 or higher.
  * The Kubernetes command-line tool, `kubectl`, installed and configured to access your cluster. For more information, see [install `kubectl`](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin#install-kubectl).
  * Optional: The `virtctl` client tool installed as a plugin for `kubectl`. If needed, see [Install the `virtctl` management tool](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/virtual-machines#install-virtctl).



## Create a VM and specify the CPU and memory

When you create a VM, you can manually specify the CPU and memory requirements. Use this feature to create VMs that have the appropriate compute resources to match your application needs.

To create a VM and specify the CPU and memory, use a `VirtualMachine` manifest.

  1. In the editor of your choice, create a `VirtualMachine` manifest, such as `my-custom-vm.yaml`:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           name: VM_NAME
           namespace: NAMESPACE
         spec:
           compute:
             cpu:
               vcpus: VCPU_NUMBER
             memory:
               capacity: MEMORY_SIZE
           interfaces:
             - name: eth0
               networkName: L2_NETWORK_NAME
               default: true
           disks:
             - virtualMachineDiskName: VM_BOOT_NAME-boot-dv
               boot: true

In this YAML file, define the following settings:

     * `VM_NAME`: the name for your VM.
     * `NAMESPACE`: the target namespace for your VM.
     * `L2_NETWORK_NAME`: The name of the L2 network to connect the VM to.
     * `VCPU_NUMBER`: The number of vCPUs to assign to the VM. You can assign between 1 and 96 vCPUs to a VM.
     * `MEMORY_SIZE`: The amount of memory to assign to the VM. You can assign between 1 Mi and 1 Ti of memory to a VM. For more information, see [Memory resource units](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#meaning-of-memory) in the Kubernetes documentation.
     * `VM_BOOT_NAME`: the name of your VM boot disk. The boot disk must already exist. For more information, see [Create a virtual machine disk from a virtual machine image](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/virtual-machines#create_a_virtual_machine_disk_from_a_virtual_machine_image).

The VM connects the `eth0` interface to the specified L2 network.

  2. To create the VM, apply the manifest to your Distributed Cloud connected cluster using the [`kubectl apply`](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_apply/) command:
         
         kubectl apply -f my-custom-vm.yaml
         

  3. To verify that the VM is created, use the [`kubectl get`](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_get/) command:
         
         kubectl get vm VM_NAME -n NAMESPACE
         

The expected output shows the VM status. You can also use the [`kubectl describe`](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_describe/) command to view the detailed configuration, including the assigned CPU and memory.




## Create and use VM types

When you enable VM Runtime on GDC, the `VirtualMachineType` custom resource definition becomes available in your cluster. You can use this resource type to create reusable templates that define specific CPU and memory allocations. By creating custom VM types for your different workloads, you can provision multiple VMs with consistent compute resource configurations.

[If VM Runtime on GDC is enabled](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/vm-runtime/enable-disable) in Distributed Cloud connected, a predefined VM type might be available. You can't update this predefined VM type. The following definition shows the default `example-machinetype` VM type:
    
    
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
    

### Create a VM type

You can create your own VM types to fit the compute needs of your workloads.

  1. In the editor of your choice, create a `VirtualMachineType` manifest, such as `my-vm-type.yaml`:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachineType
         metadata:
           name: VM_TYPE_NAME
         spec:
           cpu:
             vcpus: VCPU_NUMBER
           memory:
             capacity: MEMORY_SIZE

In this VM type, define the following settings:

     * `VM_TYPE_NAME`: the name for your VM type.
     * `VCPU_NUMBER`: the number of vCPUs to assign to the VM. You can assign between 1 and 96 vCPUs to a VM.
     * `MEMORY_SIZE`: the amount of memory to assign to the VM. You can assign between 1 Mi and 1 Ti of memory to a VM. For more information, see [Memory resource units](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#meaning-of-memory) in the Kubernetes documentation.
  2. To create the VM type, apply the manifest to your Distributed Cloud connected cluster using the [`kubectl apply`](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_apply/) command:
         
         kubectl apply -f my-vm-type.yaml
         

  3. To verify that the VM type is created, run the [`kubectl get`](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_get/) command:
         
         kubectl get virtualmachinetype VM_TYPE_NAME
         




### Create a VM using a VM type

To apply the CPU and memory settings defined in a VM type to your VM, specify the name of the VM type in the `compute` section of the `VirtualMachine` manifest.

  1. In the editor of your choice, create a `VirtualMachine` manifest, such as `my-custom-vm.yaml`. In this YAML file, specify the name of the custom VM type that you created in the previous section, such as `my-vm-type`, as the value for the `virtualMachineTypeName`.
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           name: VM_NAME
           namespace: NAMESPACE
         spec:
           compute:
             virtualMachineTypeName: VM_TYPE_NAME
           interfaces:
             - name: eth0
               networkName: L2_NETWORK_NAME
               default: true
           disks:
             - virtualMachineDiskName: VM_BOOT_NAME-boot-dv
               boot: true

Define the following settings:

     * `VM_NAME`: the name for your VM.
     * `NAMESPACE`: the target namespace for your VM.
     * `L2_NETWORK_NAME`: The name of the L2 network to connect the VM to.
     * `VM_TYPE_NAME`: the name of the custom VM type that you created in the previous section, such as `my-vm-type`.
     * `VM_BOOT_NAME`: the name of your VM boot disk. The boot disk must already exist. For more information, see [Create a virtual machine disk from a virtual machine image](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/virtual-machines#create_a_virtual_machine_disk_from_a_virtual_machine_image).

The VM connects the `eth0` interface to the specified L2 network.

  2. To create the VM, apply the manifest to your Distributed Cloud connected cluster using the [`kubectl apply`](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_apply/) command:
         
         kubectl apply -f my-custom-vm.yaml
         

  3. To verify that the VM is using the VM type, run the [`kubectl get`](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_get/) command with the `-o jsonpath` option:
         
         kubectl get vm VM_NAME -n NAMESPACE -o jsonpath='{.spec.compute.virtualMachineTypeName}'
         

The expected output displays the name of your VM type.




## What's next

  * [Manage virtual machines](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/virtual-machines)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
