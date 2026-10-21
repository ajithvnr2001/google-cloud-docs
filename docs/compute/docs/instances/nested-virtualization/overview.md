---
url: https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview/
title: About nested virtualization \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:11.752334+00:00
---

# About nested virtualization  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About nested virtualization Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

This document describes Compute Engine support for nested virtualization. Nested virtualization lets you run virtual machine (VM) instances inside of other VMs so you can create your own virtualization environments. To support nested virtualization, Compute Engine adds [Intel Virtualization Technology (VT-x)](https://en.wikipedia.org/wiki/X86_virtualization#Intel_virtualization_\(VT-x\)) or [AMD Virtualization (AMD-V)](https://en.wikipedia.org/wiki/X86_virtualization#AMD_virtualization_\(AMD-V\)) instructions to VMs, so when you create a VM, the hypervisor that is already on that VM can run additional VMs.

Compute Engine VMs run on a physical host that has [Google's security-hardened, KVM-based hypervisor](https://cloud.google.com/blog/products/gcp/7-ways-we-harden-our-kvm-hypervisor-at-google-cloud-security-in-plaintext). With nested virtualization, the physical host and its hypervisor are the level 0 (L0) environment. The L0 environment can host multiple level 1 (L1) VMs. On each L1 VM is another hypervisor, which is used to install the level 2 (L2) VMs. Figure 1 shows the relationship between the physical host, the L1 VMs, and the L2 VMs:

[ ![](https://docs.cloud.google.com/static/compute/images/nested-virtualization-diagram.svg)](https://docs.cloud.google.com/static/compute/images/nested-virtualization-diagram.svg) **Figure 1.** L0 physical host with L1 VMs and L2 VMs.

## Use cases

Scenarios where you might consider using nested virtualization include the following:

  * You have VMs that you can't run on Compute Engine: For example, you might have a disaster recovery solution for an on-premises workload that is running on VMs that fail over to Compute Engine VMs. Running nested virtualization might save you time that you would use to port your VMs to Compute Engine.

  * You have a software-validation framework that you use to test and validate new versions of a software package on numerous versions of different OSes: Using nested virtualization lets you avoid converting and managing a library of Compute Engine images.




## Performance considerations

Even with hardware-assisted nested virtualization, nested VMs might experience a 10% or greater decrease in performance for workloads that are CPU-bound and possibly greater than a 10% decrease for workloads that are input/output bound.

## Restrictions

L1 VMs have the following restrictions:

  * The only hypervisor supported in an L1 VM is Linux KVM; Microsoft Hyper-V isn't supported.

  * You can't use the following VMs:

    * E2 VMs

    * [Memory-optimized VMs](https://docs.cloud.google.com/compute/docs/machine-resource#memory-optimized_machine_family_guide)

    * VMs powered by [ARM processors](https://docs.cloud.google.com/compute/docs/cpu-platforms)

    * VMs powered by [AMD processors](https://docs.cloud.google.com/compute/docs/cpu-platforms) except **N4D** which does support nested virtualization

For information about the processors supported in each zone, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).




L2 VMs have the following restrictions:

  * For licensed operating systems, you must [bring your own licenses](https://docs.cloud.google.com/compute/docs/nodes/bringing-your-own-licenses).



## Using nested virtualization

To use nested virtualization, complete the following steps:

  1. [Check whether the nested virtualization constraint is disabled](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/managing-constraint)

  2. [Create an L1 VM that has nested virtualization enabled](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/enabling)

  3. [Create a nested L2 VM](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/creating-nested-vms)




If you run into any issues while creating a VM that has nested virtualization enabled or creating nested VMs, see [Troubleshoot nested virtualization](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-nested-vms).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
