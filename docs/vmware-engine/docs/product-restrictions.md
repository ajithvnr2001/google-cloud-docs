---
url: https://docs.cloud.google.com/vmware-engine/docs/product-restrictions/
title: VMware Engine product restrictions \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:25.869588+00:00
---

# VMware Engine product restrictions  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/product-restrictions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Resources ](https://docs.cloud.google.com/vmware-engine/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# VMware Engine product restrictions

This document highlights product restrictions for Google Cloud VMware Engine. The following restrictions apply when you use VMware Engine:

  * **Aria Capabilities** : You may use Aria Suite Enterprise or Aria Operations for Networks ("Aria Capabilities") contained in VMware Cloud Foundation (VCF) only to manage VCF Cores.
  * **VMware Tools** : "VMware Tools" is a suite of utilities and drivers that can be installed in a Guest Operating System to enhance the performance and functionality of a Guest Operating System when running in a virtual machine in conjunction with a vSphere hypervisor. You may not use VMware Tools with any other (non-vSphere) hypervisor, and you may distribute the VMware Tools to third parties when they are installed in a Guest Operating System within a virtual machine.
  * **APIs and Third Party Applications (vDefend)** : The following restrictions apply when you use vDefend Firewall:

    * You may use the APIs included with vDefend (as defined at [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms)) only to integrate vDefend with your Google Cloud management, network management, and billing systems.
    * Any use of the APIs or other portions of vDefend for other services (including for protocols, traffic engineering, or L4-L7, or with any third-party applications written specifically for vDefend), must be approved in writing by CA Inc. and will be subject to your payment of additional fees.
  * **Microsoft products** : The following restrictions apply when you use Microsoft products:

    * Windows Server images provided by Google may only be used to run customer workload VMs on VMware Engine only. You can't migrate or export VMs that use Google-provided Windows Server images to on-premises or other environments outside of VMware Engine.
    * You can use a [combination of BYOL and on-demand Windows Server licenses](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/microsoft-licensing#combination-mode) from Google Cloud on a VMware Engine private cloud. Specifically, Google provides licenses only for vCPUs running Windows Server 2022 and newer versions, and you are responsible for licenses (BYOL) for all other versions of Windows Server running in that private cloud.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
