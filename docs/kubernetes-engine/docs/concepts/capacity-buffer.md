---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/capacity-buffer/
title: About capacity buffers \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:55.228081+00:00
---

# About capacity buffers  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/capacity-buffer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About capacity buffers Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode) [ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Capacity buffers help you reduce Pod startup latency for your Google Kubernetes Engine (GKE) workloads by letting you proactively declare tiers of active or standby capacity buffers in your cluster. By declaring spare capacity ahead of time, you can achieve faster workload startups in a cost-efficient manner.

This document explains how capacity buffers work. To learn how to enable and use capacity buffers, see [Configure capacity buffers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-capacity-buffer).

## When to use capacity buffers

Use capacity buffers for applications that are sensitive to startup latency and need to scale rapidly. When you experience sudden increases in traffic, an active buffer provides pre-provisioned capacity that's designed for low-latency scaling. When you experience a sustained increase in traffic, a standby buffer provides Pod scheduling at a more affordable cost than pre-provisioning.

Capacity buffers provide the following benefits:

  * **Minimize scaling latency** : active buffers provide running nodes, which help minimize latency. Standby buffers resume quickly, providing faster capacity availability than fresh nodes at a lower cost compared to active buffers.
  * **Cost-efficient over-provisioning** : capacity buffers help you maintain a safety net. For large-scale workloads, this approach is often more cost-efficient than other over-provisioning methods, such as lowering horizontal Pod autoscaler (HPA) utilization targets, which can increase idle capacity linearly as your cluster grows.
  * **Meet workload requirements:** you have full control over your capacity buffer configuration. Your options include incorporating custom daemonsets to preload images, tuning startup time, and controlling buffer sizes to fit your needs.



We recommend capacity buffers for latency-sensitive workloads that require rapid scale-up, such as AI agents, AI inference, retail applications during sales events, or game servers during peak player activity.

## How capacity buffers work

Implement a capacity buffer by using a Kubernetes CapacityBuffer custom resource to define a buffer of spare capacity. The GKE cluster autoscaler monitors CapacityBuffer resources and treats them as pending demand to help ensure that spare capacity is available. If your cluster doesn't have enough capacity to satisfy the resource requests defined in the buffer, the cluster autoscaler provisions additional nodes.

When a high-priority workload scales up, GKE schedules the workload on the available capacity in the buffer immediately. This immediate scheduling applies to the number of replicas or the resource amount that's reserved in the buffer, avoiding the typical delay associated with node provisioning. When a workload uses a buffer unit, the cluster autoscaler provisions a new node to refill the buffer.

## Capacity buffer strategies

You can configure capacity buffers by using different provisioning strategies based on your requirements for latency and cost.

### Active buffer

An _active buffer_ provides running nodes for low-latency scaling of workloads that fit within the reserved capacity. Because the nodes are already running, they provide minimal latency for claiming Pods during a scale-up event.

### Standby buffer

A _standby buffer_ provides suspended nodes. The standby strategy is more cost-effective than the active strategy, but introduces a short delay to resume the node before it accepts workloads.

## Cost and pricing

Capacity buffers are provided at no extra charge in addition to your standard node-based compute costs, which apply to [Standard node pools](https://cloud.google.com/kubernetes-engine/pricing#compute) and [Autopilot workloads that select specific hardware](https://cloud.google.com/kubernetes-engine/pricing#autopilot-workloads-that-select-specific-hardware). Capacity buffers don't support the [Pod-based billing model](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters#pricing).

Billing for the underlying nodes differs depending on the buffer type:

  * **Active buffers** : you are charged standard node-based compute rates for the running VMs that GKE maintains to serve as active buffer capacity.
  * **Standby buffers** : while VM instances are suspended, you don't pay compute costs (CPU or memory). You incur minor storage charges (for example, VM boot disks and stored memory state) and costs for associated resources such as static external IP addresses. When GKE resumes the standby VMs to host workloads, standard node-based compute rates apply. For more information, see [Suspended instance pricing](https://docs.cloud.google.com/compute/docs/instances/suspend-stop-reset-instances-overview#pricing).



## CapacityBuffer CRD

To configure a capacity buffer, you create a CapacityBuffer CustomResourceDefinition (CRD). You can configure the capacity buffer to meet different criteria:

  * **Fixed replicas** : specify a fixed number of buffer Pods to create based on the resource requests of a referenced Pod template. This configuration is the simplest way to create a buffer of a known size.
  * **Resource limits** : specify the total amount of CPU and memory that the buffer should reserve. The controller calculates how many buffer Pods to create based on the resource requests of a referenced Pod template.
  * **Percentage-based** : define the buffer size as a percentage of an existing scalable object that defines a scale subresource (such as a Deployment, StatefulSet, ReplicaSet, or Job). The buffer size adjusts dynamically as the reference workload scales. Percentage-based capacity buffers are only supported for objects that implement the Kubernetes [scale subresource](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#scale-subresource).



For more information, see the [CapacityBuffer CRD reference documentation](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/capacitybuffer).

## Best practices

To optimize for cost-efficiency and responsiveness when configuring capacity buffers, use the following recommendations:

  * **Use a cost-optimal, standby-first strategy** : prioritize standby buffers if your workloads can tolerate a brief scale-up delay of approximately 30 seconds. This strategy avoids cold node boots of fresh VMs without having to incur the full cost of active VMs.
  * **Use active buffers for latency-sensitive workloads** : use active buffers for workloads that can't tolerate node resume times when Pod scheduling time must be as low as possible.
  * **Use a hybrid strategy to balance performance and cost** : Combine a small active buffer with a larger standby buffer for a cost-effective setup. GKE prioritizes refilling the active buffer by resuming nodes from the standby buffer (taking about 30 seconds), while new nodes are provisioned in the background to backfill the standby buffer. This setup absorbs initial spikes with active capacity, and accommodates sustained growth using the lower cost standby capacity.
  * **Size active buffers for initial bursts** : define the size of your active buffer to cover the initial sudden replica spikes you expect to encounter, before standby buffer nodes can resume.
  * **Size standby buffers for sustained load** : define standby buffers that are sufficient to cover the extended load you expect to encounter, so that buffers can refill in the background from a cold start. A sufficiently-sized standby buffer can drop your maximum Pod scheduling latency to the time it takes to resume a node, which is approximately 30 seconds. When the capacity buffer starts to be used and gets refilled, new buffer nodes transition to an active state prior to suspending. This strategy helps to boost active capacity during a prolonged load.
  * **Use the buffer simulator** : experiment with different active and standby buffer sizes to get the best result for your specific workload. Run simulations of workload scaling behavior by using the open-source GKE buffers simulator at <https://github.com/gke-labs/buffers-simulator> to fine-tune your buffer sizing rules and achieve your performance targets.
  * **Reduce cold-start latency when scaling workloads from zero** : pair workloads that [scale to and from zero using HPA](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/scale-to-from-zero-hpa) (`minReplicas: 0`) with capacity buffers. When demand increases and the workload scales up from zero, GKE immediately schedules Pods on pre-warmed buffer nodes instead of waiting for new compute nodes to provision.



## Requirements and limitations

Capacity buffers have the following requirements and limitations:

  * Capacity buffers are available for GKE clusters running version 1.35.2-gke.1842000 or later for active buffers, and version 1.36.0-gke.2253000 for standby buffers.
  * Capacity buffers support only workloads that use a [node-based billing model](https://cloud.google.com/kubernetes-engine/pricing#compute) for Standard node pools and [Autopilot node pools that select specific hardware](https://cloud.google.com/kubernetes-engine/pricing#autopilot-workloads-that-select-specific-hardware). Capacity buffers don't support workloads that use the [Pod-based billing model](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters#pricing).
  * On Standard clusters, we recommend that you enable [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning). Node auto-provisioning allows the cluster autoscaler to create new node pools based on the resource requests in your CapacityBuffer. If you don't enable node auto-provisioning, the cluster autoscaler only scales up existing node pools.
  * Both active and standby capacity buffers count against [Compute Engine quotas](https://docs.cloud.google.com/compute/quotas-limits).
  * If your CapacityBuffer configuration dependency (for example, a PodTemplate) selects a custom ComputeClass, the dependency must define any tolerations, node selectors, or runtime classes required to schedule on the provisioned nodes (for example, requirements for GKE Sandbox). For instructions, see [custom ComputeClass documentation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes).



Standby buffers have the following additional limitations:

  * They are supported on Standard clusters with node auto-provisioning enabled.
  * They are supported on Autopilot clusters running version 1.36.0-gke.2853000 or later.
  * Nodes with attached GPUs or TPUs are not supported.
  * Local SSDs are not supported.
  * Although standby buffers support customer-managed encryption keys ([CMEK](https://docs.cloud.google.com/kms/docs/cmek)) for the node's storage, the node's memory is encrypted using Google-owned and Google-managed encryption keys during suspension.
  * [Confidential Google Kubernetes Engine Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes) are not supported.
  * Standby buffers support only GKE [Container-Optimized OS and Ubuntu node images](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images). Windows Server nodes aren't supported. If you use a custom node operating system, you must ensure that the OS supports [Compute Engine suspend and resume operations](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance#limitations).
  * You should be familiar with limitations related to [Compute Engine suspend and resume operations](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance#limitations). Some key limitations include the following: 
    * Nodes with customer-supplied encryption keys (CSEK)-protected disks are not supported.
    * Nodes with more than 208 GB of memory are not supported.
    * Bare metal instances are not supported.
    * The node OS must support ACPI S3 sleep signals.
    * The suspension process length is proportional to the memory size.
    * The resumption depends on the availability of the underlying resources required to resume.



## What's next

  * To learn how to implement a capacity buffer, see [Configure capacity buffers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-capacity-buffer).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
