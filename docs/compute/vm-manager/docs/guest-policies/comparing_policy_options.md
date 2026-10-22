---
url: https://docs.cloud.google.com/compute/vm-manager/docs/guest-policies/comparing_policy_options/
title: Compare OS policy versions \u00a0|\u00a0 VM Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:25.092659+00:00
---

# Compare OS policy versions  |  VM Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/guest-policies/comparing_policy_options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  Compare OS policy versions Stay organized with collections  Save and categorize content based on your preferences. 

This document compares the OS policy feature of VM Manager with the legacy guest policy feature.

## Comparison table

Both the OS policy and guest policy (legacy) features are part of the VM Manager suite, and can be enabled by setting up VM Manager. For more information, see [Set up VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs/setup).

However, there are a few differences between the two options. These differences are summarized in the following table.

| **Guest policy (legacy)** | **OS policy**  
---|---|---  
OS Config agent version | Any | Version dated `20210427` or later 1  
Resource type2 | Global | Zonal  
Policy enforcement and compliance supported | Enforcement only |   
Rollout supported 3 |  |   
Compliance reports available |  |   
Single policy can be defined for multiple operating systems |  |   
Exclusion filters available when selecting target VMs |  |   
Supported resources | 

  * Packages
  * Package repository
  * Software recipes4
    * File
    * Executable

| 

  * Packages
  * Package repository
  * Executable
  * File

  
  
1To view agent version, see [View OS Config agent version](https://docs.cloud.google.com/compute/vm-manager/docs/upgrade-vm-manager#view-version).

2For information about resource types, see [Global, regional, and zonal resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources). 

3For information about rollouts, see [Understanding rollouts](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/create-os-policy-assignment#rollouts).

4A software recipe only runs when a guest policy is first created. To rerun a software recipe, you would need to delete and recreate the guest policy. For this reason, OS policy uses an executable that can be continuously checked and enforced. 

## What's next?

  * Learn more about [OS policies](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
