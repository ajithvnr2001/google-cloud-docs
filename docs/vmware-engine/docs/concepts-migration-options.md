---
url: https://docs.cloud.google.com/vmware-engine/docs/concepts-migration-options/
title: Workload VM migration \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:52.349142+00:00
---

# Workload VM migration  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/concepts-migration-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Workload VM migration

Using Google Cloud VMware Engine, you can migrate virtual machines (VMs) from an on-premises data center to your private cloud. Your private cloud provides native access to VMware vCenter, which supports a variety of tools for workload migration.

## Migration options

You can migrate workload VMs to your private cloud in multiple ways. Here are some of the more common options to consider:

  * **VMware HCX.** Create a hybrid infrastructure by abstracting and presenting vSphere-based on-premises and cloud resources to applications as one continuous resource
  * **Backup and disaster recovery tools.** Use your private cloud as a target to restore backups.
  * **VMware PowerCLI.** Migrate VMs from one vCenter to another using a command-line interface.
  * **ISO files and templates.** Create new VMs by uploading an ISO file to your private cloud and using a VM template from your published vSphere content library.
  * **NSX Layer 2 VPN.** Live migrate workload VMs by making an on-premises subnet available on your private cloud.



## Migration requirements

Migration of VMs and data from your on-premises environment requires network connectivity between it and your private cloud to establish a secure connection before you can migrate workloads.

The network path from your on-premises vCenter environment to your private cloud must support migration of VMs by using vMotion. The vMotion network on your on-premises vCenter must have routing abilities. Verify that your firewall allows all vMotion traffic between your on-premises vCenter and private cloud vCenter. On the private cloud, routing on the vMotion network is configured by default.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
