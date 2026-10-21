---
url: https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine/
title: TPU resources in Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:20.460687+00:00
---

# TPU resources in Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# TPU resources in Compute Engine

You can create and manage TPUs by using Compute Engine resources. This page provides a conceptual overview of using TPUs with Compute Engine. It maps TPU concepts to Compute Engine resources and outlines the process to migrate to Compute Engine.

## TPU and Compute Engine concepts

To manage TPU resources within Compute Engine, it's helpful to understand these primary TPU and Compute Engine concepts:

  * **TPU VM** : A virtual machine that connects directly to the TPU hardware. A single TPU VM is the same as a single-host slice.
  * **TPU slice** : A logical group of interconnected TPU chips, accessed through one or more TPU VMs. Slices have one of the following scopes: 
    * **Single-host slice** : A slice consisting of one host machine. _Single-host slice_ is another way of referring to a single TPU VM.
    * **Multi-host slice** : A slice that consists of multiple TPU VMs interconnected using a high-speed inter-chip interconnect (ICI).



To create and manage TPU resources in Compute Engine, you use the following Compute Engine resources:

  * **VM instance** : A Compute Engine virtual machine. A single-host TPU slice is created as an individual VM instance. In the legacy Cloud TPU API, a single TPU slice is represented by a [`Node`](https://docs.cloud.google.com/tpu/docs/reference/rest/v2/projects.locations.nodes#Node) REST object.
  * **Managed instance group (MIG)** : A collection of VM instances managed as a single unit. Multi-host TPU slices are created as a MIG with an accelerator topology specified in a workload policy. In the legacy Cloud TPU API, one or more slices are represented using [`QueuedResource`](https://docs.cloud.google.com/tpu/docs/reference/rest/v2/projects.locations.queuedResources#resource:-queuedresource) or [`Node`](https://docs.cloud.google.com/tpu/docs/reference/rest/v2/projects.locations.nodes#Node) REST objects.



## TPU and Compute Engine concept map

The following table describes how TPU concepts map to Compute Engine resources:

TPU concept | Compute Engine resource | Resource details | Use case  
---|---|---|---  
TPU VM | VM instance | A Compute Engine VM that provides direct access to TPU hardware. | Individual VM tasks, SSH command execution, or debugging  
TPU single-host or sub-host slice | VM instance or MIG with a single VM | A configuration consisting of one physical host machine. | Inference with autoscaling  
TPU multi-host slice | MIG with accelerator topology specified in workload policy | A group of TPU VMs interconnected using ICI, managed as a single logical unit. | Large-scale, distributed training requiring atomic provisioning  
  
## Migrate from the Cloud TPU API

The Cloud TPU API is no longer under active development. This includes the Google Cloud CLI for the Cloud TPU API and the Cloud Client Libraries for the Cloud TPU API. The Cloud TPU API will receive bug fixes and security updates only. New hardware generations, starting with TPU7x (Ironwood), are supported only through Compute Engine or Google Kubernetes Engine (GKE). For the latest features and support for the latest TPU versions, migrate by replacing your legacy Cloud TPU API calls with their equivalents in Compute Engine or GKE.

Depending on your orchestration and workload requirements, choose one of the following paths:

  * **Compute Engine** : Recommended for users who require direct VM-level control or custom OS images. To get started with provisioning TPUs in Compute Engine, see [Quickstart: Create a TPU VM](https://docs.cloud.google.com/tpu/docs/quickstart-create-tpu-instance).
  * **GKE** : Recommended for containerized workloads, automated scaling, and large-scale orchestration. For more information about using TPUs with GKE, see [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).



### Existing TPU resources

TPU resources created using the Cloud TPU API (`Node` or `QueuedResource` REST objects) are incompatible with Compute Engine and GKE. To start using Compute Engine or GKE:

  * Rewrite any scripts that use the Cloud TPU API to use the Compute Engine or GKE APIs.
  * Delete resources using the Cloud TPU API and recreate them using Compute Engine or GKE APIs.



## Limitations

TPUs in Compute Engine have the following limitations:

  * **TPU versions** : Compute Engine supports v5p, v6e, and TPU7x.
  * **Multislice** : Creating groups of interconnected multi-host TPU slices isn't available with Compute Engine. To use Multislice, you must use Google Kubernetes Engine (GKE). For more information, see [Deploy TPU Multislices in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpu-multislice).
  * **Collections** : Collection scheduling isn't available with Compute Engine. To use collection scheduling, you must use GKE. For more information, see [Collection scheduling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#collection-scheduling) in the GKE documentation.



## What's next

  * [Quickstart: Create a TPU instance](https://docs.cloud.google.com/tpu/docs/quickstart-create-tpu-instance)
  * [Create a TPU VM instance using Compute Engine](https://docs.cloud.google.com/tpu/docs/create-instance-compute)
  * [Create TPU VMs with MIGs](https://docs.cloud.google.com/tpu/docs/tpus-and-migs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
