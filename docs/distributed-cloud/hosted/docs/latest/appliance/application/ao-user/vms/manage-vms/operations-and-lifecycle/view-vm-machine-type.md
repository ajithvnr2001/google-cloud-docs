---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/view-vm-machine-type/
title: View machine type \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:26.294155+00:00
---

# View machine type  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/view-vm-machine-type/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  View machine type Stay organized with collections  Save and categorize content based on your preferences. 

When you create a virtual machine (VM) workload in Google Distributed Cloud air-gapped appliance (GDC), you can select the `VirtualMachineType` template which determines the resources allocated to that VM. These templates are called `VirtualMachineType`. GDC has some predefined `VirtualMachineType` templates to choose from during your VM workload creation. Use either the Console (UI) or command-line interface (CLI) to view all available `VirtualMachineType` templates.

## VirtualMachineType

GDC defines a `VirtualMachineType` with some parameters for a VM, which include CPU, memory, and GPU. GDC has various `VirtualMachineType` templates for different purposes. For example, it uses `n2-standard-2-gdc` for general purpose VM workloads. You can also find `VirtualMachineType`s for memory- optimized purposes, such as `n2-highcpu-8-gdc`.

The following is a list of all GDC predefined `VirtualMachineType`s:

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
a2-highgpu-1g-gdc | 12 | 85G | 1x A100 40GB  
a2-ultragpu-1g-gdc | 12 | 170G | 1x A100 80GB  
a2-ultragpu-2g-gdc | 24 | 340G | 2x A100 80GB  
a3-highgpu-1g-gdc  | 28 | 240G | 1x H100 94GB  
a3-highgpu-2g-gdc  | 56 | 480G | 2x H100 94GB  
a3-highgpu-4g-gdc | 112 | 960G | 4x H100 94GB  
**Preview:** The following machine types are in Preview: 

  * a3-highgpu-1g-gdc
  * a3-highgpu-2g-gdc

For more information on Preview features, see [Feature stages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/feature-stages#preview). 

## List all predefined VirtualMachineTypes

To view all available `VirtualMachineType` templates in your environment, you can directly check the `VirtualMachineType` drop-down list on the UI. Run either of the following `kubectl` CLI or gdcloud CLI command:

###  gdcloud 
    
    
    gdcloud compute machine-types list
    

###  kubectl 
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER get virtualmachinetypes.virtualmachine.gdc.goog -n vm-system
    

  * Replace `MANAGEMENT_API_SERVER` with the kubeconfig file for the Management API server.



## View a single VirtualMachineType

To view a specific `VirtualMachineType`, directly check it from UI on the VM workload creation page, or run the following `kubectl` CLI:

###  kubectl 
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER get virtualmachinetypes.virtualmachine.gdc.goog VMType_NAME -n vm-system
    -o yaml
    

Replace the following:

  * `MANAGEMENT_API_SERVER` with the kubeconfig file for the Management API server.
  * `VMType_NAME` with the name of the `VirtualMachineType` you want to query.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
