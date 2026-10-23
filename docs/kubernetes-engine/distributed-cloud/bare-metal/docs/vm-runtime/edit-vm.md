---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/edit-vm/
title: Edit VM configuration in VM Runtime on GDC \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:06.908636+00:00
---

# Edit VM configuration in VM Runtime on GDC  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/edit-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Edit VM configuration in VM Runtime on GDC Stay organized with collections  Save and categorize content based on your preferences. 

This document is intended for application owners that use VM Runtime on GDC to run virtual machines (VMs) in clusters created with Distributed Cloud software only for bare metal. This document shows you how to edit VMs running in bare metal clusters. For example, you can edit resource allocation, such as CPU and memory, or change the network a VM connects to.

You can modify any field in the `spec` section of a `VirtualMachine` resource. You can also edit the labels for a VM. Other fields, such as the VM name (`metadata.name`), can't be edited. By default, your VM must be in a `Stopped` state before you edit the resource. However, starting with Google Distributed Cloud version 1.13.0, you can configure your `VirtualMachine` resource to restart automatically whenever you change the configuration.

If your edits to the `VirtualMachine` resource contain errors when you save them, the changes are rejected and you see a notification. Correct the errors and try to save the `VirtualMachine` resource again. If your VM doesn't start after you make changes, use the `kubectl describe gvm VM_NAME` command to view troubleshooting information and correct the errors.

## Before you begin

To complete this document, you need access to the following resources:

  * A VM that runs in one of your clusters. If needed, [create a VM in a bare metal cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/quickstart).
  * The `virtctl` client tool installed as a plugin for `kubectl`. If needed, [install the virtctl client tool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/quickstart#install_the_virtctl_client_tool).



## Edit compute resources

If your compute workload demands change, you can update the number of virtual CPUs and amount of virtual memory you assign to your VMs. To edit your compute workloads, complete the following steps:

  1. Stop the VM that you want to edit:
         
         kubectl virt stop VM_NAME
         

Replace `VM_NAME` with the name of the VM that you want to stop.

  2. Use `kubectl` to edit the VM:
         
         kubectl edit gvm VM_NAME
         

Replace `VM_NAME` with the name of the VM that you want to edit.

  3. In your editor, update the compute resource values that you want to change.

For example, the following sample `VirtualMachine` manifest shows that the VM resource has `2` vCPUs assigned:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           name: vm1
         spec:
           ...
           compute:
             cpu:
               vcpus: 2
         ...
         

If you want to update the number of assigned vCPUs, change the value in your editor, as shown in the following example:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           name: vm1
         spec:
           ...
           compute:
             cpu:
               vcpus: 4
         ...
         

  4. Save and close the VM manifest.

  5. Start the VM that you edited:
         
         kubectl virt start VM_NAME
         

Replace `VM_NAME` with the name of the VM that you edited.

  6. Check the `STATUS` of your VM:
         
         kubectl get gvm VM_NAME
         

Make sure that your VM is in a `Running` state. If your VM requests more compute resources than the host can provide, your VM can't start. If the VM isn't in a `Running` state, check your `VirtualMachine` resource manifest and the compute resource availability on the host.

The following example output shows the VM in a `Running` state:
         
         NAME   STATUS    AGE   IP
         vm1    Running   1m    192.168.2.72
         

  7. View detailed information about a VM using `kubectl describe gvm`:
         
         kubectl describe gvm VM_NAME
         

Replace `VM_NAME` with the name of the VM that you edited.

The following example output shows the condensed information for a VM, with a change to the number of vCPUs successfully applied:
         
         Name:         vm1
         Namespace:    default
         Labels:       <none>
         Annotations:  <none>
         API Version:  vm.cluster.gke.io/v1
         Kind:         VirtualMachine
         ...
         Spec:
           Compute:
             Cpu:
               Vcpus:  4
         ...
         




For more information, see how to [create VMs with specific vCPU and memory compute configurations](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/compute-configurations).

## Edit disk resources

If your storage requirements change, you can add or remove virtual disks to a VM. To edit the disks attached to your VM, complete the following steps:

  1. Stop the VM that you want to edit:
         
         kubectl virt stop VM_NAME
         

Replace `VM_NAME` with the name of the VM that you want to stop.

  2. Use `kubectl` to edit the VM:
         
         kubectl edit gvm VM_NAME
         

Replace `VM_NAME` with the name of the VM that you want to edit.

  3. In your editor, update the `spec.disks` section to attach or detach disks.

For example, the following sample `VirtualMachine` manifest shows that only a boot disk is attached to the VM:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           name: vm1
         spec:
           ...
           disks:
             - boot: true
               virtualMachineDiskName: vm1-boot-dv
           ...
         

If you want to add an existing empty disk, update the disk configuration in your editor, as shown in the following example:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           name: vm1
         spec:
           ...
           disks:
             - boot: true
               virtualMachineDiskName: vm1-boot-dv
             - virtualMachineDiskName: DISK_NAME
           ...
         

Replace `DISK_NAME` with the name of the disk to attach.

  4. Save and close the VM manifest.

  5. Start the VM that you edited:
         
         kubectl virt start VM_NAME
         

Replace `VM_NAME` with the name of the VM that you edited.

  6. Check the `STATUS` of your VM:
         
         kubectl get gvm VM_NAME
         

Make sure that your VM is in a `Running` state. If your VM requests a `StorageClass` or disk assignment that the host can't provide, your VM can't start. If the VM isn't in a `Running` state, check your `VirtualMachine` and `VirtualMachineDisk` resource manifests and the host storage support.

  7. View detailed information about a VM using `kubectl describe gvm`:
         
         kubectl describe gvm VM_NAME
         

Replace `VM_NAME` with the name of the VM that you edited.

The following example output shows the condensed information for a VM, with a change to the attached disks successfully applied:
         
         Name:         vm1
         Namespace:    default
         Labels:       <none>
         Annotations:  <none>
         API Version:  vm.cluster.gke.io/v1
         Kind:         VirtualMachine
         ...
         Spec:
           Disks:
             Name:  vm1-boot-dv
             Name:  data-disk-01
         ...
         




For more information, see how to [create and manage disks](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/create-manage-disks).

## Edit network resources

As your infrastructure changes, you might want to change the network configuration for a VM. For example, you might want to connect the VM to a different virtual network or manually assign an IP address. To edit the network configuration for a VM, complete the following steps:

  1. Stop the VM that you want to edit:
         
         kubectl virt stop VM_NAME
         

Replace `VM_NAME` with the name of the VM that you want to stop.

  2. Use `kubectl` to edit the VM:
         
         kubectl edit gvm VM_NAME
         

Replace `VM_NAME` with the name of the VM that you want to edit.

  3. In your editor, update the network configuration settings that you want to change.

For example, the following sample `VirtualMachine` manifest shows that the VM connects to a network named `backend-vlan100` and uses DHCP since no IP address is defined:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           name: vm1
         spec:
           ...
           interfaces:
             - name: eth0
               networkName: backend-vlan100
               default: true
         ...
         

If you want to change the network that the VM connects to or assign a manual IP address, update the network configuration in your editor, as shown in the following example:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           name: vm1
         spec:
           ...
           interfaces:
             - name: eth0
               networkName: NETWORK_NAME
                 ipAddresses:
                   - IP_ADDRESS
               default: true
         ...
         

Replace `NETWORK_NAME` with the name of the network to connect to, or add the `ipAddresses` section and specify the `IP_ADDRESS` for your VM to use.

  4. Save and close the VM manifest.

  5. Start the VM that you edited:
         
         kubectl virt start VM_NAME
         

Replace `VM_NAME` with the name of the VM that you edited.

  6. Check the `STATUS` of your VM:
         
         kubectl get gvm VM_NAME
         

Make sure that your VM is in a `Running` state. If your VM requests a network connection that the host can't provide, your VM can't start. If the VM isn't in a `Running` state, check your `VirtualMachine` resource manifest and the host network support.

  7. View detailed information about a VM using `kubectl describe gvm`:
         
         kubectl describe gvm VM_NAME
         

Replace `VM_NAME` with the name of the VM that you edited.

The following example output shows the condensed information for a VM, with a change to the network and IP address configuration successfully applied:
         
         Name:         vm1
         Namespace:    default
         Labels:       <none>
         Annotations:  <none>
         API Version:  vm.cluster.gke.io/v1
         Kind:         VirtualMachine
         ...
         Spec:
           Compute:
           Interfaces:
             Name:          eth0
             Network Name:  backend-vlan200
         ...
         Status:
           ...
           Interfaces:
             Dns Config:
               Nameservers:
                 8.8.8.8
             gateway4:  10.200.0.9
             Ip Addresses:
               10.200.0.22/24
             Mac Address:    22:b4:e3:d2:ef:fb
             Name:           eth0
             Resource Name:  vm1-eth0-f2468
         ...
         




For more information, see how to [create and manage virtual networks](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/create-networks).

## Configure your VM for automatic restarts

Many VM configuration changes, such as changes to the `compute` settings, require the VM to be stopped and restarted for the changes to get synchronized with the corresponding VM instance (`VirtualMachineInstance`). VMs running in version 1.13.0 clusters or higher can be configured to restart automatically whenever you make changes to their configuration. When you configure a VM to use this feature, you don't need to stop and restart a VM when you edit its custom resource. VM Runtime on GDC monitors the VM and, if it detects a configuration change, it restarts the VM automatically to sync the changes.

If you are using Config Sync to manage your YAML configuration files, this feature is especially useful. Without this feature, you must stop the VM manually before you make any changes to the `VirtualMachine` custom resource and start the VM manually after you've completed your changes.

To enable automatic restarts:

**Note:** You don't need to stop and restart the VM to enable automatic restarts. The `autoRestartOnConfigurationChange` field, like the `autoDelete` field for disks, isn't synchronized with the VM instance.

  1. Use `kubectl` to edit the VM:
         
         kubectl edit gvm VM_NAME
         

  2. In your editor, add the `autoRestartOnConfigurationChange` field and set it to `true`.

You can make additional changes to your VM, such as update the `vcpus` value. If you edit `compute` settings, VM Runtime on GDC restarts your VM automatically when you save your changes.
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           ...
           name: vm-sample-01
           namespace: default
           resourceVersion: "16711824"
           uid: ed623879-0cfa-52de-ad2c-b63308e6116c
         spec:**  autoRestartOnConfigurationChange: true**
           compute:
             cpu:
               vcpus: 2
               ...
         

  3. Save and close the VM manifest.

If you have made any other changes to the VM that need to be synchronized with the corresponding VM instance, VM Runtime on GDC restarts the VM. If you've only made the change to enable automatic restarts, no VM restart is needed.

  4. Check the `status` of your VM:
         
         kubectl get gvm VM_NAME
         

Depending upon how quickly you get the VM, you may see `state: Starting` as the VM restarts. When the VM has successfully restarted, you see `state: Running`. Subsequent configuration changes to the `VirtualMachine` custom resource don't require you to stop and start the VM manually. Subsequent changes to the custom resource are reflected in the VM instance consistently.




Note the following situational feature behavior:

  * If you stop a VM manually before you edit the `VirtualMachine` custom resource, the configuration change doesn't trigger a restart. The stopped state of the VM before the configuration change is persisted.

  * If you have made label or scheduling changes for the VM prior to enabling the automatic restart feature, adding `autoRestartOnConfigurationChange` now without any other change doesn't trigger a restart. Ideally, this feature keeps the VM instance consistent with the VM configuration. However, VM Runtime on GDC can't detect prior inconsistencies.




## What's next

  * [Create VMs with specific vCPU and memory compute configurations](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/compute-configurations).
  * [Create and manage disks](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/create-manage-disks).
  * [Create and manage virtual networks](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/create-networks).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
