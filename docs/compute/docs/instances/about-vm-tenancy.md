---
url: https://docs.cloud.google.com/compute/docs/instances/about-vm-tenancy/
title: About VM tenancy \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:17:42.987117+00:00
---

# About VM tenancy  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/about-vm-tenancy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About VM tenancy Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

The _tenancy_ of a virtual machine (VM) instance indicates whether the VM shares its Compute Engine server with VMs from other Google Cloud projects. If a VM shares its Compute Engine server with VMs from other Google Cloud projects, it is a _multi-tenant_ VM. If a VM doesn't share its Compute Engine server with VMs from other projects, it is a _sole-tenant_ VM.

VMs are multi-tenant by default. After you create a VM, Compute Engine places it on a multi-tenant server. Compute Engine allows users in other [Google Cloud projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) to create VMs on that server.

[Sole-tenancy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes) is suited for workloads that require exclusive access to a Compute Engine server. Sole-tenancy lets you have exclusive access to a _sole-tenant node_ , which is a Compute Engine server that is dedicated to hosting VMs from only your Google Cloud projects.

## Pricing considerations

For multi-tenant VMs, you pay for the type of machine that you create the VM on, so [pricing for multi-tenant VMs](https://cloud.google.com/compute/vm-instance-pricing) is based on that VM's [machine family](https://docs.cloud.google.com/compute/docs/machine-resource).

For sole-tenant VMs, you pay for all of the hardware resources on the server because you are reserving an entire physical server. [Pricing for a sole-tenant node](https://cloud.google.com/compute/sole-tenant-pricing) is based on the price of the [sole-tenant node type](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_types) that you specify when you create a [sole-tenant node template](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_templates). This price includes a premium because you are reserving the entire physical server.

## Workload considerations

For typical workloads, [create multi-tenant VMs](https://docs.cloud.google.com/compute/docs/instances/create-start-instance). However, if you have workloads with any of the following characteristics, consider [using sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms):

  * Gaming workloads with specific computing performance requirements.
  * Finance or healthcare workloads with security and compliance requirements.
  * Windows workloads with licensing requirements.
  * Machine learning, data processing, or image rendering workloads. For these workloads, consider [reserving GPUs](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms).
  * Workloads requiring increased input/output operations per second (IOPS) and decreased latency, or workloads that use temporary storage in the form of caches, processing space, or low-value data. For these workloads, consider [reserving Local SSDs](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms).



For more information about workloads that might benefit from using sole-tenancy, see [Workload considerations for sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#workload_considerations).

## Maintenance event considerations

For maintenance events on multi-tenant servers, Compute Engine [live migrates](https://docs.cloud.google.com/compute/docs/instances/live-migration-process) VMs to another server in the same zone.

For maintenance events on sole-tenant nodes, Compute Engine migrates VMs according to how you configure the [maintenance policy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#maintenance_policies) on the [sole-tenant node group](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_groups_and_vm_provisioning).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
