---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus/
title: About TPUs in GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:41.321429+00:00
---

# About TPUs in GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  About TPUs in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes how Cloud TPU works with Google Kubernetes Engine (GKE), including terminology, the benefits of Tensor Processing Units (TPUs), and workload scheduling considerations. TPUs are Google's custom-developed, application-specific integrated circuits (ASICs) for accelerating ML workloads that use frameworks such as [TensorFlow](https://www.tensorflow.org/), [PyTorch](https://pytorch.org/), and [JAX](https://github.com/google/jax).

This document is for Platform admins and operators and Data and AI specialists who run machine learning (ML) models that have characteristics such as being large-scale, long-running, or dominated by matrix computations. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/anthos/docs/concepts/roles-tasks).

Before reading this document, ensure that you're familiar with how ML accelerators work. For details, see [Introduction to Cloud TPU](https://docs.cloud.google.com/tpu/docs/intro-to-tpu).

## Benefits of using TPUs in GKE

GKE provides full support for TPU node and node pool lifecycle management, including creating, configuring, and deleting TPU VMs. GKE also supports [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms) and using reserved Cloud TPU. For more information, see [Cloud TPU consumption options](https://docs.cloud.google.com/tpu/docs/consumption-options).

Benefits of using TPUs in GKE include:

  * **Consistent operational environment:** You can use a single platform for all machine learning and other workloads.
  * **Automatic upgrades:** GKE automates version updates, which reduces operational overhead.
  * **Load balancing:** GKE distributes the load, thus reducing latency and improving reliability.
  * **Responsive scaling:** GKE automatically scales TPU resources to meet the needs of your workloads.
  * **Resource management:** With [Kueue](https://kueue.sigs.k8s.io/docs/overview/#why-use-kueue), a Kubernetes-native Job queuing system, you can manage resources across multiple tenants within your organization using queuing, preemption, prioritization, and fair sharing.
  * **Sandboxing options:** GKE Sandbox helps to protect your workloads with gVisor. For more information, see [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods).



### Get started with Ironwood (TPU7x)

Ironwood (TPU7x) is Google's seventh-generation TPU, designed for large-scale AI workloads. For more information about Ironwood (TPU7x) benefits, see [About Ironwood (TPU7x) in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpu-ironwood).

## Terminology related to TPUs in GKE

This document uses the following terminology related to TPUs:

  * **Cloud TPU ICI resiliency:** a feature that helps improve fault tolerance of the optical links and optical circuit switches (OCS) that connect TPUs between cubes. For more information, see [TPU architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm).
  * **TPU cube:** a `4x4x4` topology of interconnected TPU chips. This is only applicable to topologies in 3-tuples (`{A}x{B}x{C}`).
  * **TPU type:** the Cloud TPU type, like v5e.
  * **TPU slice:** a collection of chips all located inside the same TPU Pod connected by high-speed inter-chip interconnects (ICI). Slices are described in terms of chips or TensorCores, depending on the TPU version.
  * **TPU slice node:** a Kubernetes node represented by a single VM that has one or more interconnected TPU chips.
  * **TPU slice node pool:** a group of Kubernetes nodes within a cluster that all have the same TPU configuration.
  * **TPU topology:** the number and physical arrangement of the TPU chips in a TPU slice.
  * **Atomic:** GKE treats all the interconnected nodes as a single unit. During scaling operations, GKE scales the entire set of nodes to 0 and creates new nodes. If a machine in the group fails or terminates, GKE recreates the entire set of nodes as a new unit.
  * **Immutable:** you can't manually add new nodes to the set of interconnected nodes. However, you can create a new node pool that has the TPU topology that you want and schedule workloads on the new node pool.



## Types of TPU slice node pools

GKE supports two types of TPU node pools:

  * Multi-host TPU slice
  * Single-host TPU slice



The TPU type and topology determine whether your TPU slice node can be multi-host or single-host. We recommend:

  * For large-scale models, use multi-host TPU slice nodes.
  * For small-scale models, use single-host TPU slice nodes.
  * For large-scale training or inferencing, use _Pathways_. Pathways simplifies large-scale machine learning computations by enabling a single [JAX](https://github.com/jax-ml/jax?tab=readme-ov-file#what-is-jax) client to orchestrate workloads across multiple large TPU slices. For more information, see [Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-intro).



### Multi-host TPU slice node pools

A _multi-host TPU slice node pool_ is a node pool that contains two or more _interconnected_ TPU VMs. Each VM has a TPU device connected to it. The TPUs in a multi-host TPU slice are connected over a high speed interconnect (ICI). After a multi-host TPU slice node pool is created, you can't add nodes to it. For example, you can't create a [`v4-32`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus) node pool and then later add a Kubernetes node (TPU VM) to the node pool. To add a TPU slice to a GKE cluster, you must create a new node pool.

The VMs in a multi-host TPU slice node pool are treated as a single atomic unit. If GKE is unable to deploy one node in the slice, no nodes in the TPU slice node are deployed.

If a node within a multi-host TPU slice requires repairing, GKE shuts down all VMs in the TPU slice, forcing eviction of all the Kubernetes Pods in the workload. After all VMs in the TPU slice are up and running, the Kubernetes Pods can be scheduled on the VMs in the new TPU slice.

The following diagram shows a `v5litepod-16` (v5e) multi-host TPU slice. This TPU slice has four VMs. Each VM in the TPU slice has four TPU v5e chips connected with high-speed interconnects (ICI), and each TPU v5e chip has one TensorCore:

![Multi-host TPU slice diagram](https://docs.cloud.google.com/static/tpu/docs/images/kubernetes-diagram.png)

The following diagram shows a GKE cluster that contains one TPU `v5litepod-16` (v5e) TPU slice (topology: `4x4`) and one TPU `v5litepod-8` (v5e) slice (topology: `2x4`):

![TPU v5e Pod diagram](https://docs.cloud.google.com/static/tpu/docs/images/kubernetes-v5e.png)

### Single-host TPU slice node pools

A _single-host slice_ node pool is a node pool that contains one or more independent TPU VMs. Each VM has a TPU device connected to it. While the VMs within a single-host slice node pool can communicate over the Data Center Network (DCN), the TPUs attached to the VMs are not interconnected.

The following diagram shows an example of a single-host TPU slice that contains seven `v4-8` machines:

![Single-host slice node pool diagram](https://docs.cloud.google.com/static/tpu/docs/images/kubernetes-single-host.png)

## Characteristics of TPUs in GKE

TPUs have unique characteristics that require special planning and configuration.

### TPU consumption

To optimize resource utilization and cost while balancing workload performance, GKE supports the following TPU consumption options:

  * **Flex-start:** to provision Flex-start VMs for up to seven days, with GKE automatically allocating the hardware on a best-effort basis based on availability. For more information, see [About GPU, TPU, and H4D provisioning with flex-start provisioning mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws).
  * **Spot VMs:** to provision Spot VMs, you can get significant discounts, but Spot VMs can be preempted at any time, with a 30-second warning. For more information, see [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms).
  * **Future reservation for up to 90 days (in calendar mode):** to provision TPU resources for up to 90 days, for a specified time period. For more information, see [Request TPUs with future reservation in calendar mode](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpu-calendar-mode).
  * **TPU reservations:** to [request a future reservation for one year or longer](https://docs.cloud.google.com/tpu/docs/long-term-reservation).
  * **On-demand:** to consume TPUs without arranging capacity in advance. Before requesting resources, you must have enough [on-demand quota](https://docs.cloud.google.com/tpu/docs/quota#on-demand-quotas) for the specific type and quantity of TPU VMs. On-demand is the most flexible consumption option; however, there is no guarantee that enough on-demand resources will be available to satisfy your request.



On-demand is the default consumption model for TPUs in GKE if you don't specify another option. To choose the consumption option that meets your workload requirements, see [About accelerator consumption options for AI/ML workloads in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/consumption-option).

Before using TPUs in GKE, choose the consumption option that best fits your workload requirements.

### Topology

The topology defines the physical arrangement of TPUs within a TPU slice. GKE provisions a TPU slice in two- or three-dimensional topologies, depending on the TPU version. You specify a topology as the number of TPU chips in each dimension as follows:

For TPU v4, v5p, and Ironwood (TPU7x) scheduled in multi-host TPU slice node pools, you define the topology in 3-tuples (`{A}x{B}x{C}`), for example `4x4x4`. The product of `{A}x{B}x{C}` defines the number of TPU chips in the node pool. For example, you can define small topologies that have fewer than 64 TPU chips with topology forms such as `2x2x2`, `2x2x4`, or `2x4x4`. If you use larger topologies that have more than 64 TPU chips, the values you assign to {A}, {B}, and {C} must meet the following conditions:

  * {A}, {B}, and {C} must be multiples of four.
  * The largest topology supported for v4 is `12x16x16` and v5p is `16x16x24`.
  * The assigned values must keep the A ≤ B ≤ C pattern. For example, `4x4x8` or `8x8x8`.



### Machine type naming

Machine type naming for TPUs in GKE varies depending on the cluster mode and TPU version:

  * **GKE Standard:** you select a specific Compute Engine machine type, for example, `ct6e-standard-1t` for TPU Trillium (v6e).

  * **GKE Autopilot:** you don't select machine types directly. Instead, you request TPUs by using an accelerator type in your workload manifest. For example, use `tpu-v6e-slice` for TPU Trillium (v6e) or `tpu-v5-lite-podslice` for TPU v5e. GKE Autopilot then provisions the underlying nodes with the appropriate machine types to satisfy the request.




For the exact machine types available for each TPU version, refer to the tables in [Plan TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus).

### Privileged mode

If you use GKE versions earlier than 1.28, you must configure your containers with special capabilities to access TPUs. In Standard mode clusters, you can use privileged mode to grant this access. Privileged mode overrides many of the other security settings in the `securityContext`. For details, see [Run containers without privileged mode](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#privileged-mode).

Versions 1.28 and later don't require privileged mode or special capabilities.

## How TPUs in GKE work

Kubernetes resource management and prioritization treat VMs on TPUs the same as other VM types. To request TPU chips, use the resource name `google.com/tpu`:
    
    
    resources:
      requests:
        google.com/tpu: 4
      limits:
        google.com/tpu: 4
    

When using TPUs in GKE, consider the following TPU characteristics:

  * A VM can access up to 8 TPU chips.
  * A TPU slice contains a fixed number of TPU chips, with the number depending on the TPU machine type that you choose.
  * The number of requested `google.com/tpu` must be equal to the total number of available TPU chips on the TPU slice node. Any container in a GKE Pod that requests TPUs must consume _all_ the TPU chips in the node. Otherwise, your Deployment fails because GKE can't partially consume TPU resources. Consider the following scenarios: 
    * The machine type `ct5lp-hightpu-4t` with a `2x4` topology contains two TPU slice nodes with four TPU chips each, for a total of eight TPU chips. With this machine type, you:
    * Can't deploy a GKE Pod that requires eight TPU chips on the nodes in this node pool.
    * Can deploy two Pods that require four TPU chips each, each Pod on one of the two nodes in this node pool.
    * TPU v5e with topology 4x4 has 16 TPU chips in four nodes. The GKE Autopilot workload that selects this configuration must request four TPU chips in each replica, for one to four replicas.
  * In Standard clusters, multiple Kubernetes Pods can be scheduled on a VM, but only one container in each Pod can access the TPU chips.
  * To create kube-system Pods, such as kube-dns, each Standard cluster must have at least one non-TPU slice node pool.
  * By default, TPU slice nodes have the `google.com/tpu` [taint](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) which prevents non-TPU workloads from being scheduled on the TPU slice nodes. Workloads that don't use TPUs are run on non-TPU nodes, freeing up compute on TPU slice nodes for code that uses TPUs. Note that the taint does not guarantee that TPU resources are fully utilized.
  * GKE collects the logs emitted by containers running on TPU slice nodes. To learn more, see [Logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#logging).
  * TPU utilization metrics, such as runtime performance, are available in Cloud Monitoring. To learn more, see [Observability and metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#metrics).
  * You can sandbox your TPU workloads with GKE Sandbox. GKE Sandbox works with TPU models v4 and later. To learn more, see [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods).



### Node pool auto-creation with TPUs

Node pool auto-creation supports the following Cloud TPUs only in specific GKE versions:

  * **TPU v3** : 1.31.0 and later.
  * **TPU v5 and TPU v4** : 1.29.0 and later.
  * **TPU Trillium** : 1.32.0 and later.
  * **Ironwood (TPU7x)** : 1.34.1-gke.2541000 or later.



Other Cloud TPU types are supported in all GKE versions. To learn more about the available GKE versions for TPUs, see [Validate TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability).

#### Cloud TPU node pool autoscaling

GKE scales automatically created or manually created Cloud TPU node pools that use the cluster autoscaler in one of the following ways:

  * **Single-host TPU slice node pool** : GKE adds or removes TPU nodes in the existing node pool. The node pool might contain any number of TPU nodes between zero and the maximum size of the node pool as determined by the [`--max-nodes`](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--max-nodes) and the [`--total-max-nodes`](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--total-max-nodes) autoscaling flags. All of the TPU nodes in the node pool have the same machine type and topology. For more information about how to create a single-host TPU slice node pool, see [Create a single-host TPU slice node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#single-host).
  * **Multi-host TPU slice node pool** : GKE atomically scales up the node pool from zero to the number of nodes required to satisfy the TPU topology. For example, with a TPU node pool that has the `ct5lp-hightpu-4t` machine type and a topology of `16x16`, the node pool always has either 64 nodes or zero nodes. GKE scales the node pool down if there are no TPU workloads in the node pool. To scale the node pool down, GKE evicts all scheduled Pods and removes all of the nodes in the node pool. For more information about how to create a multi-host TPU slice node pool, see [Create a multi-host TPU slice node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#multi-host).



### Collection scheduling

Collection scheduling is only supported for TPU Trillium.

In TPU Trillium, you can use collection scheduling to group TPU slice nodes. Grouping these TPU slice nodes makes it easier to adjust the number of replicas to meet the workload demand. Google Cloud controls software updates to ensure that sufficient slices within the collection are always available to serve traffic.

TPU Trillium supports collection scheduling for single-host and multi-host node pools that run inference workloads. The following describes how collection scheduling behavior depends on the type of TPU slice that you use:

  * **Multi-host TPU slice:** GKE groups multi-host TPU slices to form a collection. Each GKE node pool is a replica within this collection. To define a collection, create a multi-host TPU slice and assign a unique name to the collection. To add more TPU slices to the collection, create another multi-host TPU slice node pool with the same collection name and workload type.
  * **Single-host TPU slice:** GKE considers the entire single-host TPU slice node pool as a collection. To add more TPU slices to the collection, you can resize the single-host TPU slice node pool.



Collection scheduling has the following limitations:

  * You can only schedule collections for TPU Trillium.
  * You can define collections only during node pool creation.
  * Spot VMs are not supported.
  * Collections that contain multi-host TPU slice node pools must use the same machine type, topology, and version for all node pools within the collection.



You can configure collection scheduling in the following scenarios:

  * [When creating a TPU slice node pool in GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus)
  * [When deploying workloads on GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus-autopilot#create-tpu-workload-collections)
  * [When creating a cluster that enables node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#tpu)



## What's next

To learn how to set up Cloud TPU in GKE, see the following pages:

  * [Plan TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus) to start your TPU setup
  * [Deploy TPU workloads in GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus-autopilot)
  * [Deploy TPU workloads in GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus)
  * Deploy [GKE Cloud TPU workloads in Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-overview)
  * Learn about [best practices](https://docs.cloud.google.com/tpu/docs/tpus) for using Cloud TPU for your ML tasks
  * [Video: Build large-scale machine learning on Cloud TPU with GKE](https://www.youtube.com/watch?v=wtKhG1aTgtY)
  * [Serve Large Language Models with KubeRay on TPUs](https://www.youtube.com/watch?v=RK_u6cfPnnw)
  * [Learn about Sandboxing GPU workloads with GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
