---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/schedule-vms/
title: Schedule VMs that use VM Runtime on GDC \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:47:17.573201+00:00
---

# Schedule VMs that use VM Runtime on GDC  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/schedule-vms/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Schedule VMs that use VM Runtime on GDC Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/vm-runtime/schedule-vms)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/schedule-vms)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



This document is intended for application owners and platform administrators that run Google Distributed Cloud. This document shows you how to use schedule configurations such as affinity and anti-affinity for VMs that use VM Runtime on GDC.

## Before you begin

To complete this document, you need access to the following resources:

  * Access to Google Distributed Cloud version 1.12.0 (`anthosBareMetalVersion: 1.12.0`) or higher cluster. You can use any cluster type capable of running workloads. If needed, [try Distributed Cloud on Compute Engine](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/try/gce-vms) or see the [cluster creation overview](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/create-clusters-overview).
  * The `virtctl` client tool installed as a plugin for `kubectl`. If needed, [install the virtctl client tool](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/quickstart#install_the_virtctl_client_tool).

**Note:** The `VirtualMachine` manifests in this document use the default networking configuration. For more information about VM networking, see [Create and use virtual networks for VM Runtime on GDC](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/create-networks).

## Schedule configurations overview

Schedule configurations are optional values in VM Runtime on GDC. If no scheduling configuration is specified, the VM defaults to Kubernetes default scheduling behavior.

With the default scheduling behavior, VMs are spread across your cluster. The scheduler looks at the current node resource availability, such as CPU and memory, and schedules VMs on nodes to distribute the compute demands. If you have no specific requirements, you don't need to define any schedule configurations.

The following three fields are available to schedule VMs:

  * `nodeSelector`: specifies node labels that the host node of a VM must have. VM Runtime on GDC schedules the VM only on those nodes that have a specified label.
  * Affinity: specifies the affinity rules of the VM. It includes node affinity and inter-VM affinity or anti-affinity. You define a soft or hard requirement for the scheduler: 
    * `preferredDuringSchedulingIgnoredDuringExecution`: is a soft requirement. The scheduler tries to honor your request. If the scheduler can't honor the request, the VM may be scheduled on an unpreferred node.
    * `requiredDuringSchedulingIgnoredDuringExecution`: is a hard requirement. The scheduler tries to honor your request. If no nodes are available that match your requirement, the VM is not scheduled.
  * `Tolerations`: allows the VM to be scheduled onto nodes with matching taints.



You can define any of these scheduling configurations to support your compute workloads and scheduling needs. In addition to scheduling configurations, VM scheduling is contingent upon available resources.

**Note:** To update scheduling configurations on existing VMs, the VM must first be in a `Stopped` state. After you make changes, start the VM. The scheduler uses the new configuration to run the VM on an appropriate nodes. For more information, see [manage the powers state of a VM](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/manage-power-state).

VM Runtime on GDC uses the same VM scheduling logic and manifest structure as Kubernetes to [assign Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/). For more information on these scheduling configurations, see the following links:

  * [nodeSelector](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector)
  * [Affinity and anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity)
  * [Taints and tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)



## Put VMs on a specific node

If you have nodes with specific hardware configurations, you can schedule VMs to only run on these nodes. For example, your VM might want a particular CPU chipset, or need GPU support. You can use a basic `nodeSelector`, or more flexible affinity rules, to schedule VMs to run on these nodes.

###  nodeSelector 

The following `VirtualMachine` manifest uses a `nodeSelector` for a hard scheduling requirement. If no node is available that meets the scheduling configuration, the VM can't be scheduled.

  1. Create a `VirtualMachine` manifest, such as _my-scheduled-vm.yaml,_ in the editor of your choice:
         
         nano my-scheduled-vm.yaml
         

  2. Copy and paste the following YAML manifest:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           name: VM_NAME
         spec:
           interfaces:
             - name: eth0
               networkName: pod-network
               default: true
           disks:
             - virtualMachineDiskName: VM_NAME-boot-dv
               boot: true
           scheduling:
             nodeSelector:
               kubernetes.io/hostname: NODE_NAME
         

Replace the following values:

     * `VM_NAME`: the name of your VM.
     * `NODE_NAME`: the node(s) that you want to schedule your VM on.

The boot disk named `VM_NAME-boot-dv` must already exist. For more information, see [Create a VM boot disk](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/create-manage-disks#create-a-vm-with-an-attached-disk).

  3. Save and close the VM manifest in your editor.

  4. Create the VM and schedule configuration using `kubectl`:
         
         kubectl apply -f my-scheduled-vm.yaml
         




###  Affinity 

The following `VirtualMachine` manifest uses affinity for a soft scheduling requirement. The scheduler tries to honor your request. If the scheduler can't honor the request, the VM is scheduled on an unpreferred node.

  1. Create a `VirtualMachine` manifest, such as _my-scheduled-vm.yaml,_ in the editor of your choice:
         
         nano my-scheduled-vm.yaml
         

  2. Copy and paste the following YAML manifest:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           name: VM_NAME
         spec:
           interfaces:
             - name: eth0
               networkName: pod-network
               default: true
           disks:
             - virtualMachineDiskName: VM_NAME-boot-dv
               boot: true
           scheduling:
               affinity:
                 nodeAffinity:
                   preferredDuringSchedulingIgnoredDuringExecution:
                   - weight: 100
                     preference:
                       matchExpressions:
                       - key: kubernetes.io/hostname
                         operator: In
                         values:
                         - NODE_NAME
         

Replace the following values:

     * `VM_NAME`: the name of your VM.
     * `NODE_NAME`: the node(s) that you want to schedule your VM on.

The boot disk named `VM_NAME-boot-dv` must already exist. For more information, see [Create a VM boot disk](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/create-manage-disks#create-a-vm-with-an-attached-disk).

**Note:** For a hard scheduling requirement, set `requiredDuringSchedulingIgnoredDuringExecution` rather than `preferredDuringSchedulingIgnoredDuringExecution`.
  3. Save and close the VM manifest in your editor.

  4. Create the VM and schedule configuration using `kubectl`:
         
         kubectl apply -f my-scheduled-vm.yaml
         




## Don't put VMs on a specific node

Certain VMs might have workloads that don't run on a particular node. You can use anti-affinity rules to avoid scheduling VMs on these nodes.

The following `VirtualMachine` manifest uses affinity for a soft scheduling requirement. The scheduler tries to honor your request. If the scheduler can't honor the request, the VM may be scheduled on an inappropriate node.

  1. Create a `VirtualMachine` manifest, such as _my-scheduled-vm.yaml,_ in the editor of your choice:
         
         nano my-scheduled-vm.yaml
         

  2. Copy and paste the following YAML manifest:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           name: VVM_NAME
         spec:
           interfaces:
             - name: eth0
               networkName: pod-network
               default: true
           disks:
             - virtualMachineDiskName: VM_NAME-boot-dv
               boot: true
           scheduling:
             affinity:
               nodeAffinity:
                 preferredDuringSchedulingIgnoredDuringExecution:
                 - weight: 100
                   preference:
                     matchExpressions:
                     - key: kubernetes.io/hostname
                       operator: NotIn
                       values:
                       - NODE_NAME
         

Replace the following values:

     * `VM_NAME`: the name of your VM.
     * `NODE_NAME`: the node that you want to schedule your VM on.

The boot disk named `VM_NAME-boot-dv` must already exist. For more information, see [Create a VM boot disk](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/create-manage-disks#create-a-vm-with-an-attached-disk).

**Note:** For a hard scheduling requirement, set `requiredDuringSchedulingIgnoredDuringExecution` rather than `preferredDuringSchedulingIgnoredDuringExecution`.
  3. Save and close the VM manifest in your editor.

  4. Create the VM and schedule configuration using `kubectl`:
         
         kubectl apply -f my-scheduled-vm.yaml
         




## Keep VMs apart

Your compute workloads might have VMs that should be spread across nodes for high availability, such as a pool of frontend VMs. You can use inter-VM anti-affinity rules to avoid scheduling VMs together on nodes.

The following `VirtualMachine` manifest uses affinity for a soft scheduling requirement. The scheduler tries to honor your request. If the scheduler can't honor the request, the VM may be scheduled on an inappropriate node.

  1. Create a `VirtualMachine` manifest, such as _my-scheduled-vm.yaml,_ in the editor of your choice:
         
         nano my-scheduled-vm.yaml
         

  2. Copy and paste the following YAML manifest:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           name: VM_NAME
           labels:
             KEY:VALUE
         spec:
           interfaces:
             - name: eth0
               networkName: pod-network
               default: true
           disks:
             - virtualMachineDiskName: VM_NAME-boot-dv
               boot: true
           scheduling:
             affinity:
               podAntiAffinity:
                 preferredDuringSchedulingIgnoredDuringExecution:
                 - weight: 100
                   podAffinityTerm:
                     topologyKey: kubernetes.io/hostname
                     labelSelector:
                       matchLabels:
                         KEY:VALUE
         

Replace the following values:

     * `VM_NAME`: the name of your VM.
     * `KEY:VALUE`: the `key:value` label to apply to your VMs that you want to schedule across different nodes. For more information, see [Labels and selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).

The boot disk named `VM_NAME-boot-dv` must already exist. For more information, see [Create a VM boot disk](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/create-manage-disks#create-a-vm-with-an-attached-disk).

**Note:** For a hard scheduling requirement, set `requiredDuringSchedulingIgnoredDuringExecution` rather than `preferredDuringSchedulingIgnoredDuringExecution`.
  3. Save and close the VM manifest in your editor.

  4. Create the VM and schedule configuration using `kubectl`:
         
         kubectl apply -f my-scheduled-vm.yaml
         




## Keep VMs together

Your compute workloads might have VMs that should be kept together on nodes to reduce latency, such as a middleware and database tier. You can use inter-VM affinity rules to schedule VMs together on nodes.

The following `VirtualMachine` manifest uses affinity for a soft scheduling requirement. The scheduler tries to honor your request. If the scheduler can't honor the request, the VM may be scheduled on an inappropriate node.

  1. Create a `VirtualMachine` manifest, such as _my-scheduled-vm.yaml,_ in the editor of your choice:
         
         nano my-scheduled-vm.yaml
         

  2. Copy and paste the following YAML manifest:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           name: VM_NAME
           labels:
             KEY:VALUE
         spec:
           interfaces:
             - name: eth0
               networkName: pod-network
               default: true
           disks:
             - virtualMachineDiskName: VM_NAME-boot-dv
               boot: true
           scheduling:
             affinity:
               podAffinity:
                 preferredDuringSchedulingIgnoredDuringExecution
                 - podAffinityTerm:
                     topologyKey: kubernetes.io/hostname
                     labelSelector:
                       matchLabels:
                         KEY:VALUE
                   weight: 100
         

Replace the following values:

     * `VM_NAME`: the name of your VM.
     * `KEY:VALUE`: the `key:value` label pair to apply to your VMs that you want to schedule across different nodes. For more information, see [Labels and selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).

The boot disk named `VM_NAME-boot-dv` must already exist. For more information, see [Create a VM boot disk](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/create-manage-disks#create-a-vm-with-an-attached-disk).

**Note:** For a hard scheduling requirement, set `requiredDuringSchedulingIgnoredDuringExecution` rather than `preferredDuringSchedulingIgnoredDuringExecution`.
  3. Save and close the VM manifest in your editor.

  4. Create the VM and schedule configuration using `kubectl`:
         
         kubectl apply -f my-scheduled-vm.yaml
         




## Schedule VMs on nodes with taints

Taints are a scheduling property that lets nodes only allow VMs with specified tolerations to be scheduled to run on them. You can apply a taint to a node, then in the `VirtualMachine` manifest define a toleration to let the VM run on the node. For more information, see [Taints and tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).

  1. Create a `VirtualMachine` manifest, such as _my-scheduled-vm.yaml,_ in the editor of your choice:
         
         nano my-scheduled-vm.yaml
         

  2. Copy and paste the following YAML manifest:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           name: VM_NAME
         spec:
           interfaces:
             - name: eth0
               networkName: pod-network
               default: true
           disks:
             - virtualMachineDiskName: VM_NAME-boot-dv
               boot: true
           scheduling:
             tolerations:
             - key: KEY_NAME
               operator: "Equal"
               value: KEY_VALUE
               effect: "NoSchedule"
         

Replace the following values:

     * `VM_NAME`: the name of your VM.
     * `KEY_NAME`: the key name of your toleration that matches the taint on the node.
     * `KEY_VALUE`: the value of the key for your toleration that matches the taint on the node.

The boot disk named `VM_NAME-boot-dv` must already exist. For more information, see [Create a VM boot disk](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/create-manage-disks#create-a-vm-with-an-attached-disk).

  3. Save and close the VM manifest in your editor.

  4. Create the VM and schedule configuration using `kubectl`:
         
         kubectl apply -f my-scheduled-vm.yaml
         




## What's next

  * [Edit a VM in Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/edit-vm).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
