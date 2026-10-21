---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/minimize-vm-start/
title: Minimize the VM start time \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:06:51.747956+00:00
---

# Minimize the VM start time  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/minimize-vm-start/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Minimize the VM start time Stay organized with collections  Save and categorize content based on your preferences. 

**Preview:** Minimize the VM start time is a Preview feature that is available as-is and is not recommended for production environments. Google provides no Service-Level agreements (SLA) or technical support commitments for Preview features. For more information, see Google Distributed Cloud (GDC) air-gapped [feature stages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/feature-stages).

If you require your VMs to boot as quickly as possible, minimize your virtual machine (VM) start time with the instructions on this page. Minimizing the start time comes at the cost of resource efficiency—your project consumes additional resources, and has an increased security surface.

This document is for developers in platform administrator or application operator groups that configure VM instance start time in a Distributed Cloud environment. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To use `gdcloud` command-line interface (CLI) commands, ensure that you have downloaded, installed, and configured the [`gdcloud` CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview). All commands for Distributed Cloud use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.

### Get the kubeconfig file path

To run commands against the Management API server, ensure you have the following resources:

  1. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#cli) the kubeconfig file for the Management API server if you don't have one.

  2. Use the path to the kubeconfig file of the Management API server to replace `MANAGEMENT_API_SERVER` in these instructions.




### Request IAM roles

To minimize the start time of your VM, contact your Project IAM Admin to request the **Virtual Machine Project Admin** (`project-vm-admin`) role.

All VM roles must bind to the namespace of the project where the VM resides. Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation#verify-user-access) your access.

## Keep disk connections alive

When a VM starts, initiating a connection from the VM's node to the VM's disk takes a few seconds. To make the VM start up faster, the disk connection must be kept alive when the VM is shut down so that the disk connection doesn't reinitiate on subsequent VM starts. To achieve this, when you run the command to enable disk connection keep-alive the system automatically creates a dummy pod that mounts all the VM's disks.

### Enable disk connection keep-alive

To keep disk connections alive for a VM called `VM_NAME` in the project `PROJECT`, run the following command. When you do, the system automatically creates the dummy pod:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER \
      -n PROJECT \
      patch virtualmachines.virtualmachine.gdc.goog VM_NAME \
      --type merge --patch $'
    metadata:
      annotations:
        disk.virtualmachine.gdc.goog/enable-connection-keep-alive: "true"
    '
    

Replace the variables throughout these instructions, using the following definitions.

Variable| Definition | `MANAGEMENT_API_SERVER` | The Management API server kubeconfig file.  
---|---  
`VM_NAME` | The name of the VM.  
`PROJECT` | The GDC project in which the VM resides.  
  
When the disk connection keep-alive is enabled, a pod named `disk-connection-keep-alive-VM_NAME` is created in the same project as the VM. The next VM restart is faster, as are subsequent start times, because the VM's disk connections are kept alive by the pod.

### Set up disk connection keep-alive affinity

The Kubernetes scheduler might select a different node for the VM when it restarts. To reduce the chances of that happening, configure an inter-VM affinity rule between the VM and the keep-alive pod. Configure this to happen automatically:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER \
      -n PROJECT \
      patch virtualmachines.virtualmachine.gdc.goog VM_NAME \
      --type merge --patch $'
    metadata:
      annotations:
        disk.virtualmachine.gdc.goog/add-connection-keep-alive-affinity: "true"
    '
    

This adds a preferred-affinity setting on the VM to the keep-alive pod.

### Caveats

There are two caveats to keeping disk connections alive:

  * The keep-alive pod incurs additional resource usage: 
    * It counts towards the limit of the number of pods per node.
    * It uses an additional IP address that is assigned by Kubernetes.
    * It uses a negligible additional amount of CPU and memory.
  * The security surface increases, because the node where the keep-alive pod is present always has the VM's disks attached, even when the VM is shut down.



## Use BIOS firmware

In GDC, starting a VM with Unified Extensible Firmware Interface (UEFI) firmware is slower than starting a VM with BIOS firmware.

  1. To ensure that the start time is minimal, set the VM's firmware type to BIOS:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT \
           patch virtualmachines.virtualmachine.gdc.goog VM_NAME \
           -type merge --patch $'
         spec:
           firmware:
             type: bios
             enableSecureBoot:
         '
         

  2. If the VM is running, restart it using the instructions to [restart the VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#restart-a-vm).




### Caveats

The caveat to using BIOS firmware is that it doesn't support [secure boot](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/secure-vms/secure-boot).

## Use a large boot disk

To minimize the VM start time, attach a boot disk with a size of 500 GB or greater to the VM.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
