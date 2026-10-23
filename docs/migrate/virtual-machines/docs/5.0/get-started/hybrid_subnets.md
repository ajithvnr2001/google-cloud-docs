---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/hybrid_subnets/
title: Set up Hybrid Subnets for your migration \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:18.962604+00:00
---

# Set up Hybrid Subnets for your migration  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/hybrid_subnets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Set up Hybrid Subnets for your migration Stay organized with collections  Save and categorize content based on your preferences. 

If you need to retain connectivity within a subnet while migrating virtual machine (VM) instances from an on-premises VMware source, consider using [hybrid subnets](https://docs.cloud.google.com/vpc/docs/hybrid-subnets). For example, you can use hybrid subnets during a multi-stage migration in which some VMs or IP addresses from an on-premises subnet need to be reachable to VM instances that are already migrated to Compute Engine.

A hybrid subnet combines an on-premises subnet and a Virtual Private Cloud (VPC) subnet into a single logical subnet. You can migrate individual workloads and instances from the on-premises subnet to the VPC subnet over time, without needing to change IP addresses. After all the workloads and VMs have been migrated, you can decommission the on-premises subnet.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
