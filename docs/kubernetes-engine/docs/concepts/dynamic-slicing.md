---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dynamic-slicing/
title: About GKE dynamic slicing \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:12.272180+00:00
---

# About GKE dynamic slicing  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dynamic-slicing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  About GKE dynamic slicing Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes _dynamic slicing_ in Google Kubernetes Engine (GKE) for Cloud TPU. Dynamic slicing enhances TPU efficiency and flexibility by decoupling TPU provisioning from workload TPU slice needs. Dynamic slicing helps improve TPU resource utilization by reducing workload startup time by up to five times, and recovery time by up to 4.5 times.

Dynamic slicing is intended for Machine learning (ML) engineers and Platform engineers who want to optimize TPU utilization, reduce provisioning time, and improve fault tolerance for large-scale training and inference workloads.

Before reading this document, you should be familiar with the following:

  * [TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).
  * [TPU All Capacity mode overview](https://docs.cloud.google.com/tpu/docs/all-capacity-overview). Dynamic slicing features are available exclusively on TPUs that use All Capacity mode.



## What is dynamic slicing?

Dynamic slicing is a GKE TPU optimization feature that decouples physical and static TPU hardware provisioning from TPU slice allocation at runtime when workloads are scheduled.

When you use static TPU topologies, GKE node pools are bound to the specific topology you configured during creation. Because of this limitation, if any node in a static pool fails, the entire node pool is impacted. Your workload topology must also exactly match the node pool TPU topology to get scheduled, which can require frequent re-provisioning of TPU infrastructure for different workloads.

Dynamic slicing enables GKE to configure TPU slices at runtime when workloads are scheduled. Instead of manually creating node pools with the exact TPU topology required for every new workload, you pre-provision your entire TPU capacity into granular, fixed-size node pools. For Ironwood (TPU7x), each node pool consists of a `4x4x4` topology, also known as a [_sub-block_](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpu-all-capacity-mode). A sub-block represents a 16-node group of TPU VMs without an active Inter-Chip Interconnect (ICI) topology mesh. At runtime, when workloads are scheduled, GKE dynamic slicing reconfigures the TPU network interconnect to either stitch multiple node pools into the required large TPU slice or subdivide node pools to form smaller TPU slices. This reconfiguration creates the precise multi-dimensional topology requested by a workload in seconds.

## Benefits of dynamic slicing

Implementing a dynamic TPU architecture in GKE provides the following advantages:

  * **Faster workload recovery** : if a physical hardware failure occurs, GKE isolates the issue to a single partition. The GKE slice controller automatically reshapes the active slice and reconfigures the network to replace the faulty partition with a healthy spare. This process improves resiliency or mean time to recovery (MTTR) by up to 4.5 times compared to re-creating an entire node pool.
  * **Accelerated Job startup** : workload slices can be formed dynamically, which offers up to a five times improvement in Job startup latency compared to creating static node pools.
  * **Failure isolation** : hardware failures are isolated to the specific partition where the fault occurs. This isolation helps to protect other concurrent jobs in the cluster from cascading failures.
  * **Optimized resource utilization** : dynamic slicing helps eliminate stranded or underutilized capacity. Because slices are configured to match workload demands, dynamic slicing helps to maximize fleet utilization and minimize idle hardware.
  * **Declarative orchestration** : dynamic slicing uses Kubernetes-native custom resources and annotations, such as `JobSet` and Kueue. This approach automatically manages low-level networking and hardware orchestration.



## Dynamic slicing configurations

Dynamic slicing offers the following configurations:

  * **Dynamic super-slicing** : _combines_ multiple physically separate, pre-provisioned TPU node pools to form a single virtual slice at workload scheduling time. For example, you can combine two `4x4x4` node pools to form a `4x4x8` topology. This capability lets you create slices that are equal to or greater than a `4x4x4` topology. This configuration requires version 1.35.2-gke.1842000 or later. You can use dynamic super-slicing to train large foundation models that exceed the capacity of a single physical hardware block.

The slice controller orchestrates physical reconfigurations within the Optical Circuit Switch (OCS) network fabric. By dynamically reconfiguring the OCS, GKE extends the Inter-Chip Interconnect (ICI) network across independent hardware racks. From the perspective of the workloads, the combined sub-blocks operate as a single toroidal mesh. In a toroidal mesh, the connections wrap around. The chips on the right edge connect directly back to the chips on the left edge, and the top connects to the bottom. If you visualized this arrangement, it would form the shape of a torus (a ring shape).

  * **Dynamic sub-slicing** : _partitions_ a single, pre-provisioned TPU node pool into multiple smaller, independent units at the workload level. Dynamic sub-slicing lets you create smaller topologies within a single sub-block, specifically `2x2x1`, `2x2x2`, `2x2x4`, and `2x4x4`. For example, you can partition a `4x4x4` sub-block into one `2x2x4` sub-slice and two `2x2x2` sub-slices. This configuration requires version 1.36.0-gke.3712000 or later in the Rapid channel.

With dynamic sub-slicing, you run multiple workloads on a single physical node pool. For example, you can run concurrent fine-tuning, experimentation, and online inference. Sub-slicing provides electrical and network isolation between these sub-slices, which helps isolate failures or performance impacts between workloads.




### Key characteristics of dynamic slicing configurations

Dynamic slicing configurations have the following characteristics:

  * **Incremental provisioning of node pools** : dynamic slicing uses _incremental provisioning_ , which is a fault-tolerant provisioning model of node pools. This model converts all your TPU capacity into node pools comprising 16-node groups of Ironwood (TPU7x) VMs, which lets you continue provisioning and utilizing even partially unhealthy cubes.
  * **Slice controller** : a Kubernetes Custom Resource controller running within the GKE control plane that manages dynamic slicing. The slice controller manages the lifecycle of a [_Slice custom resource_](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/slice), which represents a dynamic slice (handling creation, continuous monitoring, and deletion). It also propagates infrastructure health data (host, ICI, OCS) to node labels to help identify healthy candidate nodes.
  * **Slice custom resource** : represents the logical slice and initiates the dynamic configuration of inter-node links (ICI and OCS) to form the requested TPU topology. This process either stitches multiple sub-blocks together (super-slicing) or isolates a smaller topology within a single sub-block (sub-slicing). You can inspect the progress or health of dynamic slice formation by inspecting the Slice custom resource's status fields.



## Requirements

To use dynamic slicing in GKE, you must meet the following requirements:

  * Use a Standard cluster in the Rapid channel in one of the following versions: 
    * For dynamic super-slicing configuration (topologies equal to or larger than `4x4x4`), use version 1.35.2-gke.1842000 or later.
    * For dynamic sub-slicing configuration (topologies smaller than `4x4x4`), use version 1.36.0-gke.3712000 or later.
  * Use Ironwood (TPU7x) version.
  * Use the Container-Optimized OS image for your nodes.
  * To use incremental provisioning, use [All Capacity mode](https://docs.cloud.google.com/tpu/docs/all-capacity-overview#all_capacity_mode) reservations. All Capacity mode is a feature enabled by TPU Cluster Director.
  * For dynamic sub-slicing, ensure that your nodes have a pending maintenance events. [Monitor your instances for pending maintenance events](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu#monitor-notification). If any of your nodes have a pending maintenance event with an end time between September 18, 2026 and September 30, 2026, you must manually [trigger the host maintenance event](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) on those nodes before you can use sub-slicing.



## Use schedulers for dynamic slicing

To use dynamic slicing, you can use any of the following options:

  * Use your own scheduler to manage Slice custom resources. This option is useful if you have complex scheduling requirements or if you want to integrate dynamic slicing with your existing scheduling infrastructure. To get started, see [Use dynamic slicing with a custom scheduler](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/create-dynamic-slices).
  * Use a scheduler to automatically create a Slice custom resource. You can configure [Kueue](https://kueue.sigs.k8s.io/docs/overview/) and [Topology Aware Scheduling (TAS)](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/schedule-gke-workloads-tas#what-is-tas) to automatically create a Slice custom resource. To get started, see [Schedule dynamic slices with Kueue and TAS](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/use-gke-dynamic-slicing).



## What's next

  * [Request TPU capacity in All Capacity mode](https://docs.cloud.google.com/tpu/docs/request-all-capacity-mode-reservation).
  * [Schedule dynamic slices with Kueue and TAS](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/use-gke-dynamic-slicing).
  * [Use dynamic slicing with a custom scheduler](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/create-dynamic-slices).
  * [Deploy Cloud TPU workloads with dynamic slicing in Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/deploy-tpu-dynamic-slicing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
