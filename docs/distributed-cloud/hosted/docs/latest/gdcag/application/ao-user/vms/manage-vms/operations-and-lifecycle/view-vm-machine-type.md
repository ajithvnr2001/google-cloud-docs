---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/view-vm-machine-type/
title: View machine type \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:33:02.356344+00:00
---

# View machine type  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/view-vm-machine-type/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  View machine type Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the predefined machine types available to configure your virtual machine (VM) instance in Google Distributed Cloud (GDC) air-gapped environments.

When you create a VM workload in (GDC), you can select the `VirtualMachineType` template, which determines the resources allocated to that VM. GDC has some predefined `VirtualMachineType` templates to choose from during your VM workload creation. Use either the GDC console or command-line interface (CLI) to view all available `VirtualMachineType` templates.

This document is for developers in platform administrator or application operator groups that create and configure VM instances. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

Before continuing, ensure that you have the following:

  * The [gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview) downloaded, installed, and configured. All CLI commands for GDC use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.


  * Use the path to the kubeconfig file of the Management API server to replace `MANAGEMENT_API_SERVER` in these instructions.



## About `VirtualMachineType`

GDC defines a `VirtualMachineType` resource with some parameters for a VM, which include CPU, memory, and GPU. GDC has various `VirtualMachineType` templates for different purposes. You can also use predefined `VirtualMachineType` templates that are differentiated by memory configurations, such as `standard`, `highmem`, and `highcpu`.

### N machine series

You can use N-series machines for general-purpose VM workloads, for example, [high performance computing (HPC)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/vm-high-mem) and CPU-bound tasks.

The following is a list of all Distributed Cloud predefined n-series `VirtualMachineType` machines:

Name | vCPUs | Memory | GPU  
---|---|---|---  
n2-standard-2-gdc | 2 | 8G | N/A  
n2-standard-4-gdc | 4 | 16G | N/A  
n2-standard-8-gdc | 8 | 32G | N/A  
n2-standard-16-gdc | 16 | 64G | N/A  
n2-standard-32-gdc | 32 | 128G | N/A  
n2-highcpu-8-gdc | 8 | 8G | N/A  
n2-highmem-2-gdc | 2 | 16G | N/A  
n2-highmem-4-gdc | 4 | 32G | N/A  
n2-highmem-8-gdc | 8 | 64G | N/A  
n2-highmem-16-gdc | 16 | 128G | N/A  
n2-highmem-32-gdc | 32 | 256G | N/A  
n3-standard-2-gdc | 2 | 8G | N/A  
n3-standard-4-gdc | 4 | 16G | N/A  
n3-standard-8-gdc | 8 | 32G | N/A  
n3-standard-16-gdc | 16 | 64G | N/A  
n3-standard-32-gdc | 32 | 128G | N/A  
n3-standard-64-gdc | 64 | 256G | N/A  
n3-standard-80-gdc | 80 | 320G | N/A  
n4-highmem-4-gdc | 4 | 32G | N/A  
n4-highmem-8-gdc | 8 | 64G | N/A  
n4-highmem-16-gdc | 16 | 128G | N/A  
n4-highmem-32-gdc | 32 | 256G | N/A  
n4-highmem-48-gdc | 48 | 384G | N/A  
n4-highmem-64-gdc | 64 | 512G | N/A  
n4-highmem-80-gdc | 80 | 640G | N/A  
  
### A machine series

A-series machines are "accelerator-optimized" machines that use NVIDIA GPUs. You can use these machine types to run GPU-accelerated workloads, for example, artificial intelligence (AI) and machine learning (ML).

The following is a list of all Distributed Cloud predefined A-series `VirtualMachineType` machines:

Name | vCPUs | Memory | GPU  
---|---|---|---  
a2-highgpu-1g-gdc | 12 | 85G | 1x A100 40GB  
a2-ultragpu-1g-gdc | 12 | 170G | 1x A100 80GB  
a2-ultragpu-2g-gdc | 24 | 340G | 2x A100 80GB  
a3-highgpu-1g-gdc  | 28 | 240G | 1x H100 94GB  
a3-highgpu-2g-gdc  | 56 | 480G | 2x H100 94GB  
a3-highgpu-4g-gdc | 112 | 960G | 4x H100 94GB  
a3-ultragpu-8g-gdc | 224 | 1792G | 8x H200 141GB  
a4-ultragpu-8g-gdc | 224 | 3584G | 8x B300  
**Preview:** The following machine types are in Preview: 

  * a3-highgpu-1g-gdc
  * a3-highgpu-2g-gdc

For more information on Preview features, see [Feature stages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/feature-stages#preview). 

To use an A-series machine type for your VM instance, see [Create and start a VM instance with NVIDIA GPUs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/create-vm-gpu).

## List all predefined `VirtualMachineType` machines

To view all available `VirtualMachineType` templates in your environment, you can either check the **Machine type** list within the GDC console, or use either one of the following `kubectl` or gdcloud CLI commands:

###  Console 

  1. [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#console) to the GDC console.
  2. In the navigation menu, click **Virtual Machines** > **Instances** > **Create Instance**.
  3. On the **Basics** page, go to the **Machine type** section. Make sure that the **General-purpose** toggle button is selected.
  4. Review the list of available predefined machine types.



###  gdcloud 
    
    
    gdcloud compute machine-types list
    

###  kubectl 
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER \
      -n vm-system \
      get virtualmachinetypes.virtualmachine.gdc.goog
    

  * Replace `MANAGEMENT_API_SERVER` with the kubeconfig file for the Management API server.



## View a single `VirtualMachineType`

To view a specific `VirtualMachineType`, you can use the `kubectl` CLI:

###  kubectl 
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER \
      -n vm-system \
      get virtualmachinetypes.virtualmachine.gdc.goog VMType_NAME \
      -o yaml
    

Replace the following:

  * `MANAGEMENT_API_SERVER` with the kubeconfig file for the Management API server.
  * `VMType_NAME` with the name of the `VirtualMachineType` you want to query.



## What's next

  * [Securely boot a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/secure-vms/secure-boot)
  * [Add a disk to a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-storage/add-a-vm-disk)
  * [Delete a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/delete-vms)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
