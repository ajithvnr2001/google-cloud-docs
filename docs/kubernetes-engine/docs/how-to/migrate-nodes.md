---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-nodes/
title: Migrate nodes to a different machine type \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:40:44.442971+00:00
---

# Migrate nodes to a different machine type  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-nodes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Migrate nodes to a different machine type Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to move workloads between machine types in Google Kubernetes Engine (GKE) clusters.

GKE clusters run workloads on [worker nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes) which are Compute Engine virtual machines (VMs). You can choose which machine types to run your workloads on depending on your cluster mode:

  * **Autopilot** : Use compute classes to choose a specific compute configuration based on your workload requirements. You can choose a specific [machine series](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology). To learn more, see [Compute classes in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-compute-classes#when-to-use).
  * **Standard** : Specify a machine type when you [add a node pool to a Standard cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#add).



Over time, you might want to change the machines that run your workloads to optimize for evolving workload requirements or to benefit from newly released machine series. Newer generation machine series can have advantages such as improved price-to-performance and improved performance consistency. For more details about machine series and choosing between different options, see the [Machine families resource and comparison guide](https://docs.cloud.google.com/compute/docs/machine-resource).

Before you decide to migrate to a new machine type, ensure that the machine type supports your specific requirements, including regional availability.

To move workloads between machine types, take the following steps:

  * **Autopilot** : Update your workload configuration.
  * **Standard** : Choose one of the following options: 
    * [Change the node machine attributes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#change-machine-attributes) of your existing node pool. GKE uses the node pool's configured node upgrade strategy to migrate your workloads from the previous machine type to the new machine type.
    * Create a new node pool and then [migrate workloads between node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#migrate). You must use this approach for migrating from an x86-based machine type (for example, C4) to an Arm-based machine type (for example, C4A). For more information about this specific type of migration, see [Migrate x86 application on GKE to multi-arch with Arm](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/migrate-x86-to-multi-arch-arm).



After you've migrated between machine types, ensure that your workloads perform as expected on the newer machine type. You can perform the same steps if you need to move back to the original configuration.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
