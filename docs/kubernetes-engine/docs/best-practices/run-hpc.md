---
url: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/run-hpc/
title: Best practices for running HPC workloads on GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:10.742615+00:00
---

# Best practices for running HPC workloads on GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/run-hpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Best practices for running HPC workloads on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Google Kubernetes Engine (GKE) provides a high-performance, scalable platform for high performance computing (HPC) workloads. To achieve high performance and operational efficiency, you can use workload-optimized infrastructure, such as HPC-specific VM families, that GKE provides. This document outlines best practices for managing your infrastructure and workloads to optimize running your HPC applications on GKE.

For a consolidated overview of all GKE best practices, see [Best practices for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices). 

## Infrastructure and node configuration

This section describes best practices for configuring your underlying infrastructure and GKE nodes for HPC workloads.

### Choose H4D VMs for compute-intensive workloads

Select the appropriate hardware for your application. H4D VMs are designed to maximize throughput for compute-intensive HPC applications. H4D VMs offer high performance, low cost, and scalability for multi-node workloads. H4D is part of the compute-optimized machine family, which offers compute-optimized instances ideal for compute-intensive and HPC.

For more information about the H4D machine series, see [Compute-optimized machine family: H4D machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_series).

For instructions on creating HPC-optimized GKE clusters, see [Run high performance computing workloads with H4D](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-hpc-workloads).

### Account for node allocatable resources

Understand the difference between a node's total resource capacity and the resources allocatable to your workloads. GKE nodes run system components, like the `kubelet` and container runtime, that require resources to function. GKE reserves a predefined quantity of resources for system functionality and node reliability. Understanding the amount of _actual_ resource allocation that you have for your workload (the VM size minus the capacity that GKE reserves) can help you properly size resource requests for your HPC workloads.

For more information, see the following resources:

  * GKE documentation about [planning node sizes: Check allocatable resources on a node](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-node-sizes#check_allocatable_resources_on_a_node).
  * Kubernetes documentation about [reserving Compute Resources for System Daemons](https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/).



### Reserve cores to mitigate preemptions

If a workload uses all physical cores available to it on a node, it can compete with latency-sensitive system daemons. This contention might cause frequent preemptions where the OS scheduler interrupts the HPC workload to perform system tasks, which can degrade performance.

To maintain performance, avoid allocating all available CPUs to your workload. Essential system processes require a small amount of CPU overhead to function properly. Allocating 100% of the compute capacity to your workload creates resource contention with these system components, which can degrade performance. For example, for H4D machine types, to maintain performance, configure your workload to use fewer than 192 CPUs.

## Cluster and workload configuration

This section describes best practices for configuring your GKE clusters and deploying your HPC workloads.

### Use Cluster Toolkit for cluster creation

Use the Cluster Toolkit to simplify the deployment and management of HPC workloads on GKE. The toolkit provides reference design blueprints that incorporate best practices for configuring compute, storage, and networking resources in a high-performance environment.

For instructions on using Cluster Toolkit to create an H4D cluster, see [Run high performance computing workloads with H4D](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-hpc-workloads).

### Use flex-start for capacity management

For bursty (dynamic) or time-insensitive HPC workloads, use flex-start to enhance capacity management when H4D on-demand or reserved capacity is unavailable. Flex-start manages the lifecycle of H4D nodes and helps address bursty or time-sensitive resource needs.

For more information, see [Create an H4D cluster with flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-hpc-workloads).

### Use a compact placement policy for tightly coupled workloads

Implement a compact placement policy for latency-sensitive, tightly coupled HPC workloads. This policy helps ensure that all Pods are provisioned close to each other on the host machines. This configuration minimizes network latency between nodes, which is crucial for applications that rely on inter-node communication.

If you create an H4D cluster using the gcloud CLI, as described in [Run high performance computing workloads with H4D](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-hpc-workloads), GKE automatically configures a compact placement policy. If you're using Cluster Toolkit, this policy is also automatically configured. If you want to manually configure compact placement for other node types, see [Define compact placement for GKE nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/compact-placement).

### Set appropriate resource requests

Inspect the actual allocatable CPU on your nodes before sizing your HPC jobs. Use the `kubectl get node` command to view allocatable resources. Ensure that your job's CPU requirements don't exceed what GKE has available after GKE system reservations.

GKE has several features to help analyze and automatically adjust your resource requests. For more information, start with [Identify underprovisioned and overprovisioned workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-workload-resource-utilization).

### Dedicate entire nodes to single workloads

Configure your MPI jobs to occupy an entire H4D node. H4D instances are provisioned as whole-host VMs. This strategy reserves the vast majority of the node's capacity, ensuring your workload is isolated. Use container resource requests or Pod anti-affinity to help ensure that replicas don't land on the same physical node.

### Enable Cloud RDMA for high-speed networking with H4D VMs

If you use H4D VMs, configure your deployment manifest to enable Cloud RDMA for your Pods. This configuration helps ensure that the high-speed RDMA network interfaces are correctly exposed to your containerized workload. For instructions, see [Configure manifests for RDMA](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-hpc-workloads#configure-manifests-for-rdma).

## Summary of best practices

The following table summarizes the best practices recommended in this document:

Topic | Task  
---|---  
Infrastructure and node configuration | Choose H4D VMs for compute-intensive workloads  
Infrastructure and node configuration | Account for node allocatable resources  
Infrastructure and node configuration | Reserve cores to mitigate preemptions  
Cluster and workload configuration | Use Cluster Toolkit for cluster creation  
Cluster and workload configuration | Use flex-start for capacity management  
Cluster and workload configuration | Use a compact placement policy for tightly coupled workloads  
Cluster and workload configuration | Set appropriate resource requests  
Cluster and workload configuration | Dedicate entire nodes to single workloads  
Cluster and workload configuration | Enable Cloud RDMA for high-speed networking with H4D VMs  
  
## What's next

  * [Run high performance computing (HPC) workloads with H4D](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-hpc-workloads).
  * [Learn how to plan for GKE node sizing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-node-sizes)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
