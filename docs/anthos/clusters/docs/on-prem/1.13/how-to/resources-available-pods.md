---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/resources-available-pods/
title: Resources available for your workloads \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:03:16.311582+00:00
---

# Resources available for your workloads  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/resources-available-pods/

**Version 1.13**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.13 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/overview)



Send feedback 

#  Resources available for your workloads Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.13 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/resources-available-pods)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/resources-available-pods)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This page shows how to determine how much CPU and memory is available on a node to run your workloads on Google Distributed Cloud.

## Reserved resources

On each cluster node, Google Distributed Cloud reserves the following resources for operating system components and core Kubernetes components:

  * 80 millicores + 1% of the CPU capacity
  * 330 MiB + 5% of the memory capacity



For example, suppose a node has the default capacity of 4 CPU cores and 8 GiB of memory. Then Google Distributed Cloud reserves:

  * 80 millicores + 1% of 4 cores = 120 millicores
  * 330 MiB + 5% of 8 GiB = 730 MiB



The operating system and core Kubernetes components do not run as Pods; they run as ordinary processes. The resources that remain, beyond these reserved resources, are available for Pods.

## Eviction threshold

To determine how much memory is available for Pods, you must also consider the [eviction threshold](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/). Google Distributed Cloud sets an eviction threshold of 100 MiB. This means that if available memory on a node falls below 100 MiB, the `kubelet` might evict one or more Pods.

## Allocatable resources

The resources on a node that are available for Pods are called the _allocatable resources_. Calculate the allocatable resources as follows:

  * `Allocatable CPU = CPU Capacity - Reserved CPU`
  * `Allocatable Memory = Memory Capacity - Reserved Memory - Eviction Threshold`



For example, suppose a node has 8 GiB of memory capacity, 680 MiB of reserved memory, and an eviction threshold of 100 MiB. Then the allocatable memory is:

`8 GiB - 680 MiB - 100 MiB = 7220 MiB`

## Resources available for your workloads

A node's allocatable resources are the resources available for Pods. This includes the Pods that run your workloads and the Pods that run Google Distributed Cloud add-ons. Add-ons include the ingress controller, the ingress service, the Connect agent, networking components, logging components, and more.

On a given node, to determine the resources available for your workloads, start with the allocatable resources and then subtract the resources used by add-ons.

The challenge is that add-ons are not distributed evenly among the nodes of a Google Distributed Cloud cluster. One node might have three add-ons, and another node might have ten add-ons. Also, the various add-ons require different amounts of CPU and memory.

As a general rule, you can figure that the add-ons running on a node require:

  * 200 millicores of CPU
  * 100 MiB of memory



Now you can calculate the resources available on a node for your workloads as follows:

  * `Allocatable CPU - 200 millicores`
  * `Allocatable memory - 100 MiB`



Certain nodes require more resources for add-ons than the preceding general rule indicates. For example, one node might run a Prometheus add-on that requires 2 GiB of memory. But if your cluster has more than a few nodes, it is reasonable to assume that the general rule applies to most nodes.

## What's next

To learn more about the concept of allocatable resources, see [Allocatable resources](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#node_allocatable) in the documentation for GKE on Google Cloud.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
