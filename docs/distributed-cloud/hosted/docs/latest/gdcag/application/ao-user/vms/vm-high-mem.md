---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/vm-high-mem/
title: Create a high-performance VM \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:14.264721+00:00
---

# Create a high-performance VM  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/vm-high-mem/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create a high-performance VM Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create high-performance virtual machines (VMs) in Google Distributed Cloud (GDC) air-gapped for memory-intensive workloads.

This type of VM uses an N4 machine shape and is ideal for applications that require consistent throughput and low-latency, such as large scale databases and real-time data analytics. For more information on how shapes optimize compute and virtualization, see [Virtual Machine Types](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/view-vm-machine-type).

This document is for platform administrators within platform administrator groups responsible for creating virtual machines. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

Open a ticket to request that the Infrastructure Operator provisions the necessary `o3-highmem1-192-gdc-metal` servers and enables HPC optimizations. When the ticket is resolved, you can create a high performance VM.

### Request IAM roles

Contact your IAM Project Admin to request the following roles on your project:

  * **Virtual Machine Project Admin** (`project-vm-admin`): create, modify, list, and delete standard and high-performance VMs in the project namespace.



All VM roles must bind to the namespace of the project where the VM resides. Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation#verify-user-access) your access.

## Create a high performance VM

To enable high performance computing (HPC) on a VM, you add the `virtualmachine.gdc.goog/enable-high-perf: "true"` label to the `VirtualMachine` manifest. When this label is applied, taints and labels are automatically added to the VM to ensure it runs on dedicated, optimized nodes.

  1. To create a disk for your VM, save the following `VirtualMachineDisk` manifest as `DISK_NAME.yaml`:
         
         apiVersion: virtualmachine.gdc.goog/v1
         kind: VirtualMachineDisk
         metadata:
           name: DISK_NAME
         spec:
           source:
             image:
               name: VM_IMAGE
               namespace: vm-system
           size: 20Gi
         

  2. Create the disk:
         
         kubectl apply -f DISK_NAME.yaml
         

  3. To create the high-performance VM, save the following `VirtualMachine` manifest as `VM_NAME.yaml`. Note the inclusion of the `virtualmachine.gdc.goog/enable-high-perf: "true"` label.
         
         apiVersion: virtualmachine.gdc.goog/v1
         kind: VirtualMachine
         metadata:
           name: VM_NAME
           labels:
             virtualmachine.gdc.goog/enable-high-perf: "true"
         spec:
           compute:
             virtualMachineType: VM_TYPE
           disks:
           - virtualMachineDiskRef:
               name: DISK_NAME
             boot: true
             autoDelete: true
           shieldConfig:
             bootType: uefi
             enableSecureBoot: true
             enableVtpm: false
         

  4. Create the VM:
         
         kubectl apply -f VM_NAME.yaml
         




## What's next

  * Review [GDC-supported images](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/supported-vm-images)
  * [Create and start a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/create-and-start) instance that uses your image.
  * [Create a boot disk](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vm-boot-disks/create-customized-boot-disk) for your VM.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
