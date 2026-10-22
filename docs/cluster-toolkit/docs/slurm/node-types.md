---
url: https://docs.cloud.google.com/cluster-toolkit/docs/slurm/node-types/
title: About node types \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:07.629045+00:00
---

# About node types  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/slurm/node-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  About node types Stay organized with collections  Save and categorize content based on your preferences. 

This document helps you choose the compute node types for your Slurm cluster that best fit your workload needs.

Understanding autoscaling and static nodes helps you optimize for cost, performance, and resource availability for your high performance computing (HPC) workloads.

## Overview

In a cluster running Slurm, the following compute node types are available:

  * _Autoscaling compute nodes_ : these use ephemeral Compute Engine instances that are created and deleted by the Slurm controller based on demand. To select autoscaling compute nodes, you would use the [node_count_dynamic_max](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/community/modules/compute/schedmd-slurm-gcp-v6-nodeset/README.md#input_node_count_dynamic_max) setting.
  * _Static compute nodes_ : these use a fixed set of nodes that are created at the time of cluster creation and are generally in an active state while the cluster is running. Static compute nodes more closely resemble an on-premise setup where resources are fixed. To select static compute nodes, you would use the [node_count_static](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/community/modules/compute/schedmd-slurm-gcp-v6-nodeset/README.md#input_node_count_static) setting.



In practice a cluster can have both static and autoscaling compute nodes.

For most use cases, autoscaling compute nodes are a good default selection. Using autoscaling is ideal for running HPC workloads in the cloud, where you only need to pay for the resources while they are in use, as your workloads might grow and shrink over time.

However, in some scenarios the use of static compute nodes might prove more beneficial. For example, when building a GPU cluster, static compute nodes are often a preferred choice to avoid the impacts of limited resource availability and longer startup time.

## When to use static compute nodes

While autoscaling compute nodes is a good default selection for most use cases, if you are concerned about any of the following factors then it is recommended that you use static compute nodes.

### Limited resource availability

When on-demand resources are scarce, [reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type) can be used to ensure that the compute instances are always available. After a reservation has been obtained, the reservation owner is billed for the compute resources as if the instances were in use, whether or not the instances have actually been created using the reservation. When using a reservation, the resources are already paid for, so there is no longer a cost benefit to autoscaling and using static compute nodes is a good choice.

### Startup time

Startup time is the time from when a compute instance creation request is sent to Google Cloud and when the instance is available to do useful work. Some of this time is spent waiting for Google Cloud to provision an instance but it also includes the time required to boot the operating system, run startup scripts, install required software, and configure the system.

In normal operation static compute nodes are always up. This means that startup time occurs up front. In most cases when using autoscaling nodes, the startup time occurs just before a job that is run.

### Data staging

For workloads where significant staging to Local SSDs is needed, you can benefit from using static compute nodes to amortize the transfer cost over more than one job.

## Considerations when using static compute nodes

It is often the combination of reserved resources and longer startup time that makes the use of static compute nodes an attractive choice. This can be the case for GPU clusters where both resource scarcity and longer startup time is observed. However when using static compute nodes, keep the following in mind:

  * Because static compute nodes are always backed by compute instances, you pay for the resources even when they are idle.
  * Static compute nodes are not created on a per-job basis, so their topology doesn't change to meet the needs of individual jobs.
  * Static compute nodes don't provide the same level of isolation between jobs as autoscaling nodes because they are not created on a per-job basis. This means that node-local issues from a previous job can potentially impact future jobs running on the same node.
  * When using static compute nodes there are additional maintenance considerations such as updating VM images for the compute nodes and handling host maintenance events. For more information about managing static compute nodes, see [Manage static compute node](https://docs.cloud.google.com/cluster-toolkit/docs/slurm/manage-static-nodes).



## What's next

  * Review [Best practices for static compute nodes](https://docs.cloud.google.com/cluster-toolkit/docs/slurm/static-nodes-best-practices)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
