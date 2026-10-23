---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-support/
title: About machine support with GKE clusters \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:51:08.131660+00:00
---

# About machine support with GKE clusters  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About machine support with GKE clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes the machines that Google Kubernetes Engine (GKE) supports. In a GKE cluster, nodes are the worker machines that run your workloads. The individual machines are [ Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances) that GKE creates. For more information, see [About the nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes) in the "GKE cluster architecture" document.

To support different kinds of workloads, Compute Engine has multiple machine families—for example, [general-purpose](https://docs.cloud.google.com/compute/docs/general-purpose-machines), [storage-optimized](https://docs.cloud.google.com/compute/docs/storage-optimized-machines), and [compute-optimized](https://docs.cloud.google.com/compute/docs/compute-optimized-machines). Each machine family offers multiple machine series, which each offer a series of machine types. GKE supports most of the available Compute Engine machine types, with some exceptions that are listed in this document. To get started with learning about the various machines that Compute Engine offers, see [Machine families resource and comparison guide](https://docs.cloud.google.com/compute/docs/machine-resource).

GKE offers [two modes of operation](https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-standard-feature-comparison), Standard and Autopilot. In Standard mode, you choose a Compute Engine machine type when creating a Standard node pool. In Autopilot, you request [ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-compute-classes) which can declare the machines that GKE uses. One GKE cluster can use multiple machine types at the same time.

The following sections explain how to find machine support for specific GKE features, and how to find what machines GKE does and doesn't support from Compute Engine.

## Get information about machine requirements and limitations

GKE might have specific requirements for successfully using the machine series. For example, see the following:

  * **Specific GKE version requirement for using a machine series** : you must use a specific GKE version or later to use a specific machine series. For example, you must use GKE version 1.35.0-gke.2398002 or later to use a specific machine series.
  * **Specific version requirement for using a machine series with a specific feature** : you must use a specific version to use a specific machine series with a specific feature. For example, to create a cluster that uses Autopilot mode and N4A nodes, use GKE version 1.34.1-gke.3403001 or later.
  * **Certain features require specific machine series** : you can use a specific feature only with specific machine series. For example, an accelerator-focused feature might support only accelerator-optimized machines. [Multi-instance GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi#supported_gpus) are only supported with specific machine series (or, in this case, their associated GPUs).



For information about requirements and limitations for machine series when using the machines with GKE clusters, see the following:

  * Search the [GKE release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes) for any notes about the respective machine series. For example, the [February 24, 2026](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#February_24_2026) and [December 13, 2024](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#December_13_2024) release notes have information about the C4A machine series.
  * Search the respective feature documents in the GKE documentation. For example, for Local SSD in Autopilot, see the section [Machine series that support Local SSD in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd#supported-machine-series).
  * Search the Compute Engine documentation for underlying technical details about specific machine series. For example, for more information about H4D, see the [H4D machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_series) section in the "Compute-optimized machine family for Compute Engine" document.



## Machine support with GKE

GKE supports all [machines from Compute Engine](https://docs.cloud.google.com/compute/docs/machine-resource), with the following exceptions:

Machine series | Unsupported machine types from the machine series  
---|---  
[C4N](https://docs.cloud.google.com/compute/docs/network-optimized-machines#c4n_series) |  GKE doesn't support the `-lssd` machine types ([Preview](https://cloud.google.com/products#product-launch-stages)), including the following:

  * `c4n-standard-4-lssd`
  * `c4n-standard-8-lssd`
  * `c4n-standard-16-lssd`
  * `c4n-standard-24-lssd`
  * `c4n-standard-48-lssd`
  * `c4n-standard-96-lssd`
  * `c4n-standard-192-lssd`
  * `c4n-highmem-4-lssd`
  * `c4n-highmem-8-lssd`
  * `c4n-highmem-16-lssd`
  * `c4n-highmem-24-lssd`
  * `c4n-highmem-48-lssd`
  * `c4n-highmem-96-lssd`
  * `c4n-highmem-192-lssd`

  
[M4](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m4_series) |  GKE doesn't support any `m4-hypermem-` machine types, including the following:

  * `m4-hypermem-8`
  * `m4-hypermem-16`
  * `m4-hypermem-32`
  * `m4-hypermem-64`

  
[C4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series) |  GKE doesn't support the `-metal` machine types, including the following:

  * `c4-standard-288-metal`
  * `c4-standard-288-lssd-metal`
  * `c4-highmem-288-metal`
  * `c4-highmem-288-lssd-metal`

  
[X4](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x4_series) | GKE doesn't support any machine types of the X4 machine series.  
[Z3](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_series) | GKE doesn't support the `z3-highmem-192-highlssd-metal` machine type.  
[Z4D](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4d_series) | GKE doesn't support the `-metal` machine types.  
[Z4M](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4m_series) |  GKE doesn't support the `-metal` machine types.   
  
## What's next

  * For more information about node pools and how to manage them, see [About node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) and [Add and manage node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools).
  * To migrate nodes between machine types, see [Migrate nodes to a different machine type](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-nodes).
  * To plan and design the infrastructure for your GKE cluster by using Gemini assistance, see [Design and optimize GKE clusters with Compute Advisor](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/design-with-gemini).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
