---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters/
title: About Autopilot mode workloads in GKE Standard \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:43.655632+00:00
---

# About Autopilot mode workloads in GKE Standard  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About Autopilot mode workloads in GKE Standard Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

You can use _ComputeClasses_ to run Google Kubernetes Engine (GKE) Autopilot workloads in your GKE Standard mode clusters. This document describes the methods that you can use to run your workloads in Autopilot mode and helps you to decide when to run a workload in a specific mode.

This information is intended for the following people:

  * Cloud architects who want to optimize operational costs in organizations.
  * Platform administrators who want to reduce the overhead of manual infrastructure management.
  * Site reliability engineers (SREs) who want to shift infrastructure maintenance, upgrades, and scaling to Google Cloud when possible.



You should already be familiar with the following concepts:

  * [Autopilot mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)
  * [ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes)



## About GKE Autopilot

Autopilot is a _mode of operation_ in GKE in which Google manages your node infrastructure, scaling, security, and pre-configured features. Autopilot mode is optimized for running most production workloads in an environment that applies recommended settings for security, reliability, performance, and scalability. To decide between Autopilot mode and Standard mode based on your requirements, see [About GKE modes of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).

You can use Autopilot mode in the following ways:

  * [**Create a cluster that uses Autopilot mode**](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster): Google manages the entire cluster and applies best practices for automation, reliability, security, and costs.
  * **Run workloads in Autopilot mode in Standard clusters** : you deploy Autopilot ComputeClasses and select them in workloads. Google manages the nodes that GKE creates for those specific workloads in an [Autopilot-managed node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools#autopilot-node-pools). You control the cluster and can run your own Standard node pools alongside the nodes that GKE manages.



## About Autopilot mode for ComputeClasses

A ComputeClass is a Kubernetes custom resource that defines a list of node configurations, like machine types or feature settings. You can select specific ComputeClasses in Kubernetes workload specifications. When a workload that selects a ComputeClass needs a new node, GKE attempts to provision the node with one of the configurations that the ComputeClass declares. GKE tries each configuration in the ComputeClass in order and falls back to the next configuration if node creation fails. For more information, see [About custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes).

To run Autopilot workloads in your GKE Standard clusters, you enable Autopilot mode in a ComputeClass and select that ComputeClass in specific workloads. Google manages any new nodes that GKE provisions for these workloads, similar to how Google manages the nodes in Autopilot clusters. Most of the benefits and security features of Autopilot mode apply to those workloads and the host nodes.

Autopilot mode ComputeClasses provide cluster administrators with additional flexibility to choose the level of control that you want over specific workloads and infrastructure in your cluster, such as in the following ways:

  * You can let GKE fully manage specific workloads by running them in Autopilot mode.
  * You retain full control over workloads and infrastructure that don't use Autopilot mode, such as manually created node pools.
  * You can set an Autopilot ComputeClass as the [default for your cluster or namespace](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-pods-default-compute-classes), so that workloads run in Autopilot mode unless they explicitly request a different option.



These options let cluster admins decide on the level and the scope with which they use Autopilot.

### Benefits of Autopilot ComputeClasses in Standard clusters

Running some of your workloads in Autopilot mode provides benefits like the following:

  * **Reduce infrastructure management costs** : Google upgrades, maintains, configures, and fine-tunes specific nodes for you.
  * **Use the Autopilot pricing model** : workloads that use an Autopilot ComputeClass are billing using the Autopilot pricing model. This pricing model includes per-Pod billing for workloads that don't request specific hardware. For more information, see the [Pricing section](https://cloud.google.com/kubernetes-engine/pricing#autopilot_mode).
  * **Improve scaling and security posture** : Autopilot workloads get benefits like access to the [container-optimized compute platform](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#autopilot-compute-platform), improved default security constraints, and node autoscaling based on resource requests. The nodes for those workloads use features like node auto-upgrades and automatic repairs.
  * **Improve reliability** : the GKE [service-level agreement (SLA)](https://cloud.google.com/kubernetes-engine/sla) includes a Pod uptime service-level objective (SLO) for Autopilot.



Many of these benefits are also provided by Autopilot clusters, which also provide a more managed experience than Standard clusters and include multiple security, networking, and resource management benefits. For more information, see [Autopilot overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#benefits).

## Hardware selection in Autopilot ComputeClasses

In Autopilot ComputeClasses, you can select specific hardware for your nodes (like GPUs or machine types), or you can let GKE place Pods on a general-purpose, container-optimized compute platform. The general-purpose option is recommended for most production workloads that don't require specific hardware to run well. It supports both x86 and Arm architectures.

The following table describes these configuration options, how to choose one in a ComputeClass, and how this choice affects your billing model:

**Table 1.** Hardware selection in Autopilot ComputeClasses Workload requirement | Recommended ComputeClass configuration | Billing model  
---|---|---  
General-purpose workloads | Use an Autopilot ComputeClass that has the `podFamily` priority rule to run workloads that don't require specific hardware on the Autopilot container-optimized compute platform. This platform works well for general-purpose workloads like the following:

  * Web servers
  * Event-driven jobs
  * Batch processing
  * CI/CD pipelines

The built-in Autopilot ComputeClasses use only `podFamily` priority rules. You can also add `podFamily` priority rules to custom Autopilot ComputeClasses. | [Pod-based billing model](https://cloud.google.com/kubernetes-engine/pricing#autopilot_pod)  
Workloads that need specific hardware | Use a ComputeClass that uses any available hardware configuration rule, such as the `machineFamily` rule or the `gpus` rule. | [Node-based billing model](https://cloud.google.com/kubernetes-engine/pricing#autopilot_node)  
  
## Configuration of Autopilot in ComputeClasses

You can use Autopilot mode in a Standard cluster by using a built-in Autopilot ComputeClass that GKE provides, or by enabling Autopilot in any custom ComputeClass that you create. The following sections describe each option.

### Built-in Autopilot ComputeClasses

GKE configures specific Autopilot ComputeClasses for you. You can [select these built-in Autopilot classes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-classes-standard-clusters#built-in-class) in any eligible cluster. The built-in Autopilot ComputeClasses in Standard clusters use the `podFamily` priority rule to run Pods on the container-optimized compute platform. For more information, see [About built-in ComputeClasses in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-built-in-compute-classes).

### Custom Autopilot ComputeClasses

You can enable Autopilot in any custom ComputeClass that you manage by using the `autopilot` field in the ComputeClass specification. Custom Autopilot ComputeClasses are useful in situations like the following:

  * Your workloads have specific hardware requirements, such as accelerators.
  * You want to modify certain node options, such as setting zones or applying taints, while still using the Autopilot container-optimized compute platform.



To enable Autopilot in an existing ComputeClass, you must delete it, update the configuration, and then recreate the ComputeClass in your cluster. Your changes apply to any new nodes that GKE creates for workloads that you deploy after you update the Autopilot ComputeClass.

For more information about enabling Autopilot in your custom ComputeClasses, see [Select specific hardware for your Autopilot Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-classes-standard-clusters#configure-custom-autopilot-class).

## Pricing

GKE Autopilot pricing applies to the nodes and workloads that GKE creates for an Autopilot ComputeClass. The Autopilot billing model that applies to a specific workload depends on the ComputeClass priority rule that GKE uses to create nodes for that workload.

The following table describes the billing model that applies to different Autopilot ComputeClass configurations in your Standard mode clusters:

**Table 2.** Pricing for Autopilot ComputeClasses Billing models for different ComputeClass configurations  
---  
[Pod-based billing model](https://cloud.google.com/kubernetes-engine/pricing#autopilot_pod) | The Pod-based billing model applies when GKE uses a `podFamily` priority rule to create nodes for a workload. The built-in Autopilot ComputeClasses, always use the Pod-based billing model.  
[Node-based billing model](https://cloud.google.com/kubernetes-engine/pricing#autopilot_node) | The node-based billing model applies when GKE uses a ComputeClass priority rule that explicitly request specific hardware, such as a certain machine family or GPUs.  
  
Autopilot pricing applies only to the workloads and nodes that use an _Autopilot_ ComputeClass. Your Standard mode cluster and any other node pools that you run continue to use [GKE Standard mode pricing](https://cloud.google.com/kubernetes-engine/pricing#standard_mode).

## Pre-configured settings for nodes managed by Autopilot

Before you enable Autopilot mode in your ComputeClasses, know what to expect from the nodes that GKE creates to run the Autopilot workloads. Google configures specific features and security constraints in Autopilot nodes. As a result, workloads that deploy and function correctly in your Standard mode nodes might be rejected by Autopilot mode if they don't meet the security requirements of Autopilot.

The following table describes the feature configurations that override the corresponding settings in your Standard cluster. If a configuration isn't in this table, the Autopilot nodes use the Standard cluster setting. For example, Workload Identity Federation for GKE isn't in this table, which means that the Workload Identity Federation for GKE setting of the Standard cluster applies to the Autopilot nodes that GKE creates.

**Table 3.** Pre-configured settings for Autopilot nodes Feature | Standard cluster-level setting | Autopilot-managed node setting  
---|---|---  
Node upgrades and maintenance |  Configurable:

  * [Node auto-repair](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair)
  * [Node auto-upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades-autopilot)
  * [Node upgrade strategy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pool-upgrade-strategies)

|  Pre-configured:

  * Node auto-repair: enabled
  * Node auto-upgrade: enabled
  * Node upgrade strategy: [surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades-autopilot#surge) with pre-configured parameters

  
Autoscaling | Configurable: [Autoscaling profile](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#autoscaling_profiles) | Pre-configured: [`optimize-utilization` autoscaling profile](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#autoscaling_profiles)  
Networking | [VPC-native or routes-based](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips) | Requires a VPC-native cluster  
Security |  Configurable:

  * Node IAM service account
  * Access scopes
  * [Secure boot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes#secure_boot)

|  Pre-configured:

  * Node IAM service account: uses the [service account for node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#identity).
  * Access scopes: uses the [access scopes for node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#identity).
  * Secure boot: enabled
  * Node security constraints: [built-in Autopilot security configurations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-security#built-in-security), enforced on a best-effort basis.

  
Node operating system |  Configurable:

  * [Node image](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-images)
  * [Node system configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config)
  * [Linux cgroup mode](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#cgroup-mode-options)

|  Pre-configured:

  * Node image: [Container-Optimized OS with containerd](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#cos)
  * Node system configuration: configurable only with the ComputeClass [`nodeSystemConfig` field](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#nodeSystemConfig).
  * cgroup mode: v2

  
Node boot disk |  Configurable:

  * [Boot disk type](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/custom-boot-disks)
  * [Boot disk size](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/custom-boot-disks)

|  Configurable:

  * Boot disk type: uses the value in the ComputeClass [`storage.bootDiskType`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#storage) field. If this field isn't set, GKE sets the boot disk type as follows: 
    * If the ComputeClass uses `podFamily` rules, GKE uses a `pd-balanced` disk.
    * If the ComputeClass doesn't use `podFamily` rules, GKE uses the default boot disk type for the cluster.
  * Boot disk size: GKE uses the value in the compute class [`storage.bootDiskSize`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#storage) field. If this field isn't set, GKE sets the boot disk size as follows: 
    * If you set a [default boot disk size for node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#custom_boot_disk), GKE uses that value.
    * If you don't set a default boot disk size for node auto-provisioning, GKE uses the cluster default size.

  
Node metadata | 

  * [Resource Manager Tags for firewall policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tags-firewall-policies#about-tags): updates to cluster-level tags don't affect existing nodes.

| 

  * [Resource Manager Tags for firewall policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tags-firewall-policies#about-tags): updates to cluster-level tags affect existing nodes.

  
  
## Resource requests for Autopilot workloads

For Autopilot workloads to run efficiently, GKE enforces certain minimum and maximum values for CPU, memory, and ephemeral storage requests in your Pods. GKE also applies default requests to Pods that don't explicitly request one of these resources. The specific values for the minimum, maximum, and default resource requirements in GKE Autopilot workloads vary based on the type of hardware that your Pods use.

For ephemeral storage, the default value if you don't request ephemeral storage is the same for all ComputeClasses and hardware selections. For more information, see [Default resource requests](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#defaults).

The following table provides links to the CPU and memory requirements for your Pod requests, depending on the type of hardware:

**Table 4.** Autopilot CPU and memory requirements Resource type | Minimum and maximum requests | Default requests  
---|---|---  
General-purpose Pods | 

  * For built-in Autopilot ComputeClasses, see the "General-purpose" row in the [Minimums and maximums for ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#compute-class-min-max) table.
  * For `podFamily` priority rules in custom Autopilot ComputeClasses, see [Resource requests for workload separation and extended duration](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#workload-separation).

| 

  * For built-in Autopilot ComputeClasses, see the "General-purpose" row in the [Default requests for ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#compute-class-defaults) table.
  * For `podFamily` priority rules in custom Autopilot ComputeClasses, see the [Resource requests for workload separation and extended duration](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#workload-separation).

  
GPUs and TPUs | Depends on the type and quantity of hardware accelerator. For more information, see [Minimums and maximums for accelerators](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#hardware-min-max). | No default requests.  
Specific Compute Engine machine types and machine families | 

  * **Minimum** : no minimum values for CPU or memory.
  * **Maximum** : the maximum value is the resource capacity of the Compute Engine instance.

| For any Compute Engine machine type or machine family, the default requests in the "General-purpose" row in the [Default requests for ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#compute-class-defaults) table.  
  
## What's next

  * [Learn about best practices for ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/computeclasses)
  * [Deploy workloads in Autopilot mode in Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-classes-standard-clusters)
  * [About custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
