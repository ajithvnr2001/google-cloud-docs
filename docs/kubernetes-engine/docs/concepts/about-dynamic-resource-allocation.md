---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-dynamic-resource-allocation/
title: About dynamic resource allocation in GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:11.796583+00:00
---

# About dynamic resource allocation in GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-dynamic-resource-allocation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About dynamic resource allocation in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

You can use [_dynamic resource allocation (DRA)_](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/) to allocate GPUs to your Google Kubernetes Engine (GKE) workloads. This document explains the fundamentals of DRA, how to use DRA in GKE, and the benefits of using DRA.

This document is intended for the following roles:

  * [Platform administrators](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks#operators-platform-administrator) who want to reduce the complexity and overhead of setting up infrastructure with specialized hardware devices.
  * [App operators](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks#operators-app-sre) and [Data engineers](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks#data-ai-engineer) who run workloads like AI/ML or high performance computing (HPC).



You should already be familiar with the following:

  * [GPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus)
  * [Common Expression Language (CEL)](https://github.com/google/cel-spec)



## Introduction to DRA

DRA is a built-in Kubernetes feature that lets you flexibly request, allocate, and share hardware in your cluster among Pods and containers. DRA improves the experience of allocating attached hardware, such as accelerators, by letting device vendors and platform administrators declare _classes_ of devices that can be requested and allocated. App operators can ask for specific device configurations within those classes and then request those configurations in their workloads. Kubernetes and GKE manage Pod scheduling, node assignments, and device allocation based on workload requests.

For example, a platform administrator might define a device class that has only NVIDIA A100 GPUs. App operators can then filter the devices in that device class based on workload requirements, such as filtering for a minimum of 80 GB of GPU memory. When the app operator deploys a workload that requests the filtered configuration, GKE places the Pods on nodes that meet the selected criteria. In this example, GKE finds nodes that have available A100 (80 GB) GPUs. The app operator doesn't need to select specific nodes or device configurations in the workload manifest.

### Benefits of DRA

Without DRA, allocating hardware devices in Kubernetes relies on [_device plugins_](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/). To attach hardware resources to Pods by using device plugins, you use node labels to place Pods on specific nodes. Additionally, to dedicate an entire node's resources to a single Pod, you request the exact number of devices that's attached to the nodes.

With DRA, allocating devices to Pods is similar to allocating volumes for storage. You define classes of devices, request devices within those classes, and then assign those requested devices to workloads. DRA provides a significantly more extensible surface to filter for devices based on workload and business needs. The DRA approach of using expressions and templates to claim hardware and schedule Pods has the following benefits:

  * **Declarative device allocation** : platform administrators can define device configurations for specific types of workloads or teams.
  * **Reduced cross-team complexity** : when platform administrators provision nodes that have specialized hardware configurations, app operators don't need to know which nodes have specific configurations. Platform administrators don't need to label nodes or communicate information about specific nodes and devices to operators.
  * **Reduced developer complexity** : Kubernetes schedules Pods based on the referenced device configuration. App operators don't need to select specific nodes in their workloads and don't need to ensure that each Pod requests exactly the number of devices that are attached to those nodes.
  * **Centralized infrastructure management** : platform administrators can centrally define hardware configurations that meet specific business requirements. For example, a platform administrator could declare a high-performance configuration that has H100 GPUs alongside a small inference configuration that has Tesla T4 GPUs.
  * **Flexible hardware selection** : you can use CEL expressions to filter for devices that have specific attributes. Using expressions provides the flexibility to filter for devices that are optimal for specific workloads.



### When to use DRA

The primary reason to use DRA in GKE is the flexibility with which you can request devices for workloads. You can write a manifest once and deploy the workload to different clusters with different device types without needing to change the manifest. This flexibility is ideal for use cases like the following:

  * **Improve GPU flexibility, efficiency, and availability of compute capacity** : for workloads that need access to GPU hardware, you can use DRA to request _any_ available GPU in the cluster instead of needing to specify a GPU model. If those workloads have specific GPU memory (VRAM) requirements, you can request any GPU in the cluster that has a minimum amount of memory. This type of flexible request expands the set of GPU nodes that a workload can run on, which reduces the risk of the workload not being scheduled because of unavailable resources.
  * **Optimize node availability during scaling** : the quantity of devices that a workload requires might change depending on factors like the type of device and its capabilities. You can use GKE [_ComputeClasses_](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes) to place accelerated Pods on specific node pools based on device availability. You can then configure your Pods to claim the devices in any node that GKE places the Pods on.

Using DRA with ComputeClasses lets you minimize the risk of unscheduled workloads while also helping you to run workloads on optimized hardware.




### Terminology

Open source Kubernetes and managed Kubernetes providers like GKE use the following core DRA API kinds:

ResourceSlice
     A ResourceSlice lists one or more hardware devices in the cluster that nodes can access. For example, in a node that can access a single GPU, the ResourceSlice lists the GPU and the name of the node. The DRA device drivers on each node create ResourceSlices. The Kubernetes scheduler uses ResourceSlices to decide which devices to allocate to satisfy workload requests. 
DeviceClass
     A DeviceClass defines a category of devices, such as GPUs, that are available to request for workloads. Some device drivers provide built-in DeviceClasses, such as the `gpu.nvidia.com` DeviceClass for NVIDIA GPUs. Platform administrators can also create custom DeviceClasses that define specific device configurations. 
ResourceClaim
    

A ResourceClaim lets a Pod or a user request hardware resources by filtering for certain parameters within a DeviceClass. When a workload references a ResourceClaim, Kubernetes assigns devices that match the specified parameters to that ResourceClaim.

For example, consider a scenario in which you create a ResourceClaim for one A100 (40 GB) GPU and then deploy a workload that selects that ResourceClaim. Kubernetes assigns an available A100 (40 GB) GPU to the ResourceClaim and schedules your Pod on a node that can access that GPU.

ResourceClaimTemplate
    

A ResourceClaimTemplate defines a template that Pods can use to automatically create new per-Pod ResourceClaims. ResourceClaimTemplates are useful when you have multiple workloads that need access to similar device configurations, especially when using a workload controller like Deployments or StatefulSets.

App operators deploy ResourceClaimTemplates and then reference the templates in workloads. Kubernetes creates ResourceClaims for each Pod based on the specified template, allocates devices, and schedules the Pods. When the Pods terminate, Kubernetes cleans up the corresponding ResourceClaims.

For more information about DRA API kinds, see [DRA terminology](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#terminology).

## How DRA works

Using DRA in your clusters and workloads is a similar process to using StorageClasses, PersistentVolumeClaims, and PersistentVolumes to [dynamically provision volumes for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes).

The following diagram shows the steps that cluster administrators and app operators take to allocate devices by using DRA:

![](https://docs.cloud.google.com/static/kubernetes-engine/images/dra-user-flow.svg)

In this diagram, cluster administrators and app operators do the following:

  1. Cluster administrators install device drivers that support DRA in the nodes.
  2. Cluster administrators create DeviceClasses that filter for hardware that meets specific requirements, such as all GPUs with more than 40 GB of memory. Some devices might also include built-in DeviceClasses.
  3. Application operators create ResourceClaimTemplates or ResourceClaims that request device configurations. The primary use case for each type of claim is as follows: 
     * A ResourceClaim lets multiple Pods share access to the same device.
     * A ResourceClaimTemplate lets multiple Pods access separate, similar devices by automatically generating per-Pod ResourceClaims.
  4. Application operators add the ResourceClaimTemplates or ResourceClaims to their workload manifests.
  5. Application operators deploy the workload.



When you deploy a workload that references a ResourceClaimTemplate or a ResourceClaim, Kubernetes performs the following scheduling steps:

  1. If the workload references a ResourceClaimTemplate, Kubernetes creates a new `ResourceClaim` object for every instance of the workload (for example, every replica in a Deployment).
  2. The Kubernetes scheduler uses the ResourceSlices in the cluster to allocate available, eligible devices to each Pod's ResourceClaim.
  3. The scheduler places each Pod on a node that has access to the devices that were allocated to the Pod's ResourceClaim.
  4. The `kubelet` on the destination node calls the on-node DRA driver to attach the allocated hardware to the Pod to satisfy its resource request.



### When to use ResourceClaims and ResourceClaimTemplates

**Best practice:** if multiple Pods need independent access to similar device configurations, use a ResourceClaimTemplate. If multiple Pods need shared access to a device, use a ResourceClaim and reference it in each Pod specification. 

You can use ResourceClaims or ResourceClaimTemplates to indicate to Kubernetes that you want devices that meet specific requirements. When a ResourceClaim is referenced in a Pod, Kubernetes allocates devices to the corresponding `ResourceClaim` API resource in the Kubernetes API server. This allocation happens regardless of whether you created the ResourceClaim or Kubernetes created the ResourceClaim from a ResourceClaimTemplate.

If you create a ResourceClaim and then reference it in multiple Pods, all of those Pods can access the devices that Kubernetes allocates for that ResourceClaim. For example, this shared access might happen if you reference a specific ResourceClaim in a Deployment manifest that has multiple replicas. _However, if the allocated devices aren't configured to be shared by multiple processes, this shared device access across Pods might result in unintended behavior._

To allocate separate devices to Pods, you can use a ResourceClaimTemplate, which is a template that Kubernetes uses to automatically create individual ResourceClaims. For example, if you reference a ResourceClaimTemplate in a Deployment that has multiple replicas, Kubernetes creates a separate ResourceClaim for each replicated Pod. As a result, each Pod gets its own allocated device instead of sharing access to the device with other Pods. These auto-generated ResourceClaims are bound to the lifetime of the corresponding Pod, and are deleted when the Pod terminates. If you have independent Pods that need access to similar device configurations, use a ResourceClaimTemplate to allocate devices to each Pod separately.

The following table describes some differences between manually creating ResourceClaims and letting Kubernetes create ResourceClaims from a ResourceClaimTemplate:

**Table 1.** Comparison of ResourceClaims and ResourceClaimTemplates Manually-created ResourceClaims | Automatically-created ResourceClaims  
---|---  
Managed by you | Managed by Kubernetes  
Provides access to the same devices from multiple Pods | Provides access to devices from a single Pod  
Exists in the cluster independently of Pods | Bound to the lifecycle of the corresponding Pod  
Ideal for multiple workloads that need to share a specific device | Ideal for multiple workloads that need independent device access  
  
## Comparison of DRA with manual device allocation

DRA makes allocating attached devices a similar experience to dynamically provisioning PersistentVolumes. Kubernetes also supports allocating devices by using _device plugins_. This method involves the following steps:

  1. A cluster administrator creates nodes that have attached devices, like GPUs.
  2. The cluster administrator communicates information about specific nodes and their attached devices to workload operators.
  3. A workload operator requests devices in the workload manifest as follows: 
     * Select a node that has the required device configuration, like the GPU model, by using a `nodeSelector` field.
     * Specify the exact number of devices for the containers to consume by using the `resources` field in the Pod specification.



This manual allocation method requires the application operators and cluster administrators to communicate about which specific nodes or node pools have certain device configurations. They must coordinate workload requests to match the devices on the nodes, or the deployment fails. In comparison, DRA lets you use expressions to flexibly filter for devices based on attributes, and doesn't require workload operators to know the exact configuration of nodes in the cluster.

The following table compares DRA with device plugins:

**Table 2.** Comparison of DRA and manual device allocation DRA | Manual allocation  
---|---  
Flexible device selection using CEL expressions | Specific node selection using selectors and resource requests  
Scheduling decisions made by Kubernetes | Scheduling decisions made by the operator using node selectors  
Device filtering is separate from workload creation | Device filtering has to be done in the workload manifest  
Centralized device filtering and needs-based classes, managed by platform administrators | Isolated device filtering by application operators   
App operators don't need to know node capacity, node label information, or the attached device models for each node | App operators must know which nodes have specific models and quantities of certain devices attached.  
  
## DRA and infrastructure autoscaling

To automatically adjust the number of nodes within a Standard mode node pool, you use the [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler). You can enable the cluster autoscaler in any manually created node pools, including node pools that have DRA drivers.

For node pools that use DRA, device utilization affects how the cluster autoscaler adds and removes nodes in a node pool. To calculate device utilization in a node pool, the cluster autoscaler considers the following factors:

  * All of the devices in a [resource pool](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#resourceslice) must be local to a specific node. If a ResourceSlice has a pool of devices that are attached to multiple nodes, then the cluster autoscaler ignores those devices.
  * All devices in the node pool are equally important and are identical.
  * DRA devices are higher priority than CPU or memory. In DRA node pools, the cluster autoscaler ignores CPU and memory usage.



These factors might mean that you notice different scale-down behavior in DRA node pools than in other node pools.

## Supported GKE devices for DRA

The following table describes the devices that you can allocate to workloads with DRA in GKE:

**Table 3.** Supported devices for DRA in GKE Supported devices for DRA  
---  
GPUs | Any GPU type that's available in your location. For more information, see [GPU locations](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).  
Network interfaces | Multiple types of network interfaces, such as RDMA-capable interfaces, by installing the managed DRANET driver. For more information, see [Allocate network resources using GKE managed DRANET](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/allocate-network-resources-dra).  
  
## Limitations

The following limitations apply when you use DRA:

  * **Mode of operation** : DRA is available only in Standard mode clusters.

  * **Accelerator type** : DRA in GKE supports only GPUs.

  * **GPUs** :

    * You can't use time-sharing GPUs, multi-instance GPUs, or Multi-Process Service (MPS).
    * For nodes that use the DRA GPU drivers, you can't use the [managed NVIDIA Data Center GPU Manager (DCGM) metrics package](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dcgm-metrics) to send DCGM metrics to Cloud Monitoring.
    * The GPU driver for DRA is owned by NVIDIA, not by GKE. For more information, see [the NVIDIA documentation](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/dra-intro-install.html).
  * **Network interfaces** : see [Limitations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/allocate-network-resources-dra#limitations) in "Allocate network resources using GKE managed DRANET".

  * **Autoscaling** :

    * For third-party DRA drivers that you install, the cluster autoscaler requires your node pools to have at least one node. To prevent node pools that use third-party drivers from scaling to zero nodes, set the [minimum number of nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#autoscaling_limits) to at least `1`.
    * The cluster autoscaler might not work correctly with third-party DRA drivers. If you do use third-party drivers, verify that the drivers publish information only for devices that are local to specific nodes.
    * For DaemonSets in autoscaled node pools that use a static ResourceClaim to share device access amongst Pods, autoscaling supports up to 128 DaemonSet Pods. To avoid this limitation, do one of the following: 
      * Prevent the node pool from scaling to more than 128 nodes by setting the [maximum number of nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#autoscaling_limits).
      * Use the [`adminAccess` field (beta)](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#admin-access), in the ResourceClaim, which lets the DaemonSet access devices that are in use.
    * If your Pods reference ResourceClaims and have a PriorityClass that sets the preemption policy to `PreemptLowerPriority`, then the autoscaling latency might increase. `PreemptLowerPriority` is the default preemption policy for PriorityClass, so ensure that your PriorityClasses explicitly set the `preemptionPolicy` field to `Never`. For more information, see [Non-preempting PriorityClass](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#non-preempting-priority-class).



## Recommended skills for understanding and using DRA

This section provides recommendations for platform administrators or app operators who want to use DRA to allocate devices to workloads. DRA significantly changes the method by which you request attached devices, both in GKE and in Kubernetes. To benefit from more advanced use cases, such as cross-device fallback or fine-grained device filtering and selection, consider the following guidance:

  * **Learn CEL** : with DRA, you can use CEL expressions to perform fine-grained device filtering in your resource allocation requests and DeviceClasses. The following resources might help you to learn CEL:

    * [Read the CEL overview](https://cel.dev/overview/cel-overview)
    * [Do a CEL tutorial](https://cel.dev/tutorials/cel-get-started-tutorial)
    * [Refer to the CEL language definition](https://github.com/google/cel-spec/blob/master/doc/langdef.md)
  * **Learn about ComputeClasses in GKE** : you can use ComputeClasses with DRA to meet business needs like provisioning Spot VMs to run inference workloads that request cost-efficient GPUs. The following resources help you to learn about ComputeClasses:

    * [Read the ComputeClass overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-compute-classes)
    * [Configure a ComputeClass in a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-attributes-compute-classes)
    * [Refer to the ComputeClass CustomResourceDefinition](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass)



## What's next

  * [Prepare your GKE infrastructure for DRA workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/set-up-dra)
  * [Dynamically allocate devices to workloads with DRA](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-dra-workloads)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
