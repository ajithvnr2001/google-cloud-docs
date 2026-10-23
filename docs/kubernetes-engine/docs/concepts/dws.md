---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws/
title: About GPU, TPU, and H4D consumption with flex-start provisioning mode \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:58.458637+00:00
---

# About GPU, TPU, and H4D consumption with flex-start provisioning mode  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  About GPU, TPU, and H4D consumption with flex-start provisioning mode Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes flex-start in Google Kubernetes Engine (GKE). Flex-start, powered by [Dynamic Workload Scheduler](https://cloud.google.com/products/dws/pricing), provides a flexible and cost-effective technique to consume specialized compute resources, like GPUs or TPUs, when you need to run AI/ML workloads.

Flex-start lets you dynamically provision Flex-start VMs for GPUs, TPUs, and H4D machine series as needed, for up to seven days, not bounded to a specific start time, and without the management of long-term reservations. Therefore, flex-start works well for smaller to medium-sized workloads with fluctuating demand requirements or short durations. For example, small model pre-training, model fine-tuning, or scalable serving models.

The information on this page can help you to do the following:

  * Understand how flex-start in GKE works.
  * Decide whether flex-start is right for your workload.
  * Decide which flex-start configuration is right for your workload.
  * Manage disruptions when using Flex-start VMs.
  * Understand the limitations of Flex-start VMs in GKE.



This page is intended for [Platform admins and operators](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks#operators-platform-admin) and [Machine learning (ML) engineers](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks#data-ai-ml-engineer) who want to optimize accelerator infrastructure for their workloads.

## When to use flex-start

We recommend that you use flex-start if your workloads meet all of the following conditions:

  * Your workloads require GPU resources.
  * Your workloads require TPU resources that run in [single-host TPU slice node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#single-host).
  * Your workloads require other specialized hardware, such as the HPC-optimized H4D machine series.
  * You have limited or no [reserved](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations) GPU or TPU capacity and you need more reliable access to these accelerators.
  * Your workload is time-flexible and your use case can afford to wait to get all the requested capacity, for example, when GKE allocates the GPU resources outside of the busiest hours.



## Flex-start pricing

Flex-start is recommended if your workload requires dynamically provisioned resources as needed, for up to seven days with short-term reservations, no complex quota management, and cost-effective access. Flex-start is powered by Dynamic Workload Scheduler and is billed using [Dynamic Workload Scheduler pricing](https://cloud.google.com/products/dws/pricing):

  * Can receive a discount (up to 53%) for vCPUs, GPUs, TPUs, and any attached Local SSD disks.
  * You pay as you go (PAYG).



## Requirements

To use flex-start in GKE, your cluster must meet the following requirements:

  * To run GPUs, use GKE version 1.32.2-gke.1652000 or later.
  * To run TPUs, see the GKE version requirements in [Plan TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus). Flex-start supports the following version and zones:

    * Ironwood (TPU7x) in `us-central1-c`.
    * TPU Trillium (v6e) in `asia-northeast1-b`, `us-east5-a`, and `us-east5-b`.
    * TPU v5e in `us-west4-a`.
    * TPU v5p in `us-east5-a`.

TPU v3 and v4 are not supported.




## How flex-start provisioning mode works

With flex-start, you specify the required compute capacity (such as GPUs or TPUs) in your workloads. Additionally, with Standard clusters, you configure flex-start on specific node pools. GKE automatically provisions Flex-start VMs by completing the following process when capacity becomes available:

  1. The workload requests capacity that is not immediately available. This request can be made directly by the workload specification or through orchestration tools such as [custom compute classes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes) or [Kueue](https://kueue.sigs.k8s.io/).
  2. GKE identifies that your node has flex-start enabled. If the `--request-valid-for-duration` flag is not specified, GPU workloads can wait up to 14 days for resources. In contrast, TPU workloads can wait for an indeterminate amount of time.
  3. The cluster autoscaler accepts your request and calculates the number of necessary nodes, treating them as a single unit.
  4. The cluster autoscaler provisions the necessary nodes when they are available. These nodes run for a maximum of seven days, or for a shorter duration if you specify a value in the `maxRunDurationSeconds` parameter. If you don't specify a value for the `maxRunDurationSeconds` parameter, the default is seven days.
  5. After the running time you defined in the `maxRunDurationSeconds` parameter ends, the nodes and the Pods are [preempted](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/).
  6. If the Pods finish sooner and the nodes are no longer utilized, the cluster autoscaler removes them according to the [autoscaling profile](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#autoscaling_profiles).



GKE counts the duration for each flex-start request on a node level. The time available for running Pods might be slightly smaller due to delays during startup. Pod retries share this duration, which means that less time is available for Pods after retry. GKE counts the duration for each flex-start request separately.

## Flex-start configurations

GKE supports the following flex-start configurations:

  * **Flex-start** , where GKE allocates resources node by node. This configuration only requires you to set the `--flex-start` flag during node creation.
  * **Flex-start with queued provisioning** , where GKE allocates all requested resources at the same time. To use this configuration, you have to add the `--flex-start` and `enable-queued-provisioning` flags when you create the node pool. GKE follows the process in How flex-start provisioning mode works in this document, but also applies the following conditions:

    * The scheduler waits until all the requested resources are available in a single zone.
    * All Pods of the workload can run together on newly provisioned nodes.
    * The provisioned nodes aren't reused between workload executions.
**Note:** Clusters running GKE version 1.29.1-gke.1708000 and later optimize zone selection for lower wait times. Earlier versions might experience longer queueing.



The following table compares the flex-start configurations:

| Flex-start | Flex-start with queued provisioning  
---|---|---  
Availability | [Preview](https://cloud.google.com/products#product-launch-stages) | Generally Available (GA) Note: Flex-start supports the `flex-start` and `enable-queued-provisioning` flags in Preview.   
Supported accelerators | 

  * GPU
  * TPU in [single-host TPU slice node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#single-host) and [multi-host TPU slice node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#multi-host)

| 

  * GPU
  * TPU in [multi-host TPU slice node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#multi-host)

  
Recommended workload size | Small to medium, which means that the workload can run on a single node. For example, this configuration works well if you are running small training jobs, offline inference, or batch jobs. | Medium to large, which means that the workload can run on multiple nodes. Your workload requires multiple resources and can't start running until all nodes are provisioned and ready at the same time. For example, this configuration works well if you are running distributed machine learning training workloads.  
Provisioning type | GKE provisions one node at a time when resources are available. For TPUs, GKE creates one node at a time in single-host TPU slice node pools, and the complete slice at a time in multi-host TPU slice node pools. | GKE allocates all requested resources simultaneously.  
Setup complexity | Less complex. This configuration is similar to on-demand and Spot VMs. | More complex. We strongly recommend that you use a quota management tool, such as [Kueue](https://kueue.sigs.k8s.io/docs/overview/).  
[Custom compute classes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#reservations) support | Yes | No  
Node recycling | Yes | No  
Price | Flex Start SKU | Flex Start SKU  
Quota | 

  * GPU [preemptible](https://docs.cloud.google.com/compute/resource-usage#preemptible-quotas) quota
  * TPU [preemptible](https://docs.cloud.google.com/tpu/docs/quota#preemptible-quotas) quota

| 

  * GPU [preemptible](https://docs.cloud.google.com/compute/resource-usage#preemptible-quotas) quota
  * TPU [preemptible](https://docs.cloud.google.com/tpu/docs/quota#preemptible-quotas) quota

  
Node upgrade strategy | [Short-lived upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#short-lived-upgrades-flex-start) | [Short-lived upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#short-lived-upgrades-flex-start)  
[`gcloud container node pool create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create) flag | `--flex-start` | 

  * `--flex-start`
  * `--enable-queued-provisioning`

  
Get started |  GPUs: 

  * [Serve LLMs on GKE with a cost-optimized and high-availability GPU provisioning strategy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dws-flex-start-inference)
  * [Run a small batch workload with GPUs and flex-start provisioning mode](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dws-flex-start-training)

TPUs: 
  * [Run a small batch workload with TPUs and flex-start provisioning mode](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dws-flex-start-training-tpu)

|  [Run a large-scale workload with flex-start with queued provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/provisioningrequest)  
  
### Optimize flex-start configuration

To create robust and cost-optimized AI/ML infrastructure, you can combine flex-start configurations with available GKE features. We recommend that you use [Compute Classes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes) to define a prioritized list of node configurations based on your workload requirements. GKE will select the most suitable configuration based on availability and your defined priority.

## Manage disruptions in workloads that use Dynamic Workload Scheduler

Workloads that require the availability of all nodes, or most nodes, in a node pool are sensitive to evictions. In addition, nodes that are provisioned by using Dynamic Workload Scheduler requests don't support automatic repair. Automatic repair removes all workloads from a node, and thus prevents them from running.

All nodes using Flex-start VMs, queued provisioning, or both, use [short-lived upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#short-lived-upgrades-flex-start) when the cluster control plane runs the minimum version for flex-start, 1.32.2-gke.1652000 or later.

Short-lived upgrades update a Standard node pool or group of nodes in an Autopilot cluster without disrupting running nodes. New nodes are created with the new configuration, gradually replacing existing nodes with the old configuration over time. Earlier versions of GKE, which don't support flex-start or short-lived upgrades, require different best practices.

### Best practices to minimize workload disruptions for nodes using short-lived upgrades

Nodes that use Flex-start VMs and nodes which use queued provisioning are automatically configured to use short-lived upgrades when the cluster runs version 1.32.2-gke.1652000 or later.

To minimize disruptions to workloads running on nodes that use short-lived upgrades, perform the following tasks:

  * Configure [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions) to set when GKE should and shouldn't perform update operations, such as node upgrades, while ensuring that GKE still has the time to do automatic maintenance.
  * [Disable node auto-repair](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair#disable).



For nodes on clusters running versions earlier than 1.32.2-gke.1652000, and thus not using short-lived upgrades, refer to the specific guidance for those nodes.

### Best practices to minimize workload disruption for queued provisioning nodes without short-lived upgrades

Nodes using queued provisioning on a cluster running a GKE version earlier than 1.32.2-gke.1652000 don't use short-lived upgrades. Clusters upgraded to 1.32.2-gke.1652000 or later with existing queued provisioning nodes are automatically updated to use short-lived upgrades.

For nodes running these earlier versions, refer to the following guidance:

  * Depending on your cluster's [release channel enrollment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/release-channels#finding_your_clusters_channel), use the following best practices to prevent node auto-upgrades from disrupting your workloads: 
    * If your cluster is enrolled in a release channel, use [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions) to prevent GKE from automatically upgrading your nodes while your workload is running.
    * If your cluster isn't enrolled in a release channel, [disable node auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable). However, we recommend using release channels, where you can use maintenance exclusions with more granular scopes.
  * [Disable node auto-repair](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair#disable).
  * Use [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions) to minimize disruption to running workloads, while ensuring that GKE still has the time to do automatic maintenance. Be sure to schedule that time for when no workloads are running.
  * To ensure that your node pool remains up to date, [manually upgrade your node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_nodes) when no Dynamic Workload Scheduler requests are active and the node pool is empty.



### Considerations for when your cluster migrates to short-lived upgrades

GKE updates existing nodes using queued provisioning to use short-lived upgrades when the cluster is upgraded to version 1.32.2-gke.1652000 or later. GKE doesn't update other settings, such as enabling node auto-upgrades if you disabled them for a specific node pool.

We recommend that you consider implementing the following best practices now that your node pools use short-lived upgrades:

  * If you disabled node auto-upgrades by using the `--no-enable-autoupgrade` flag, this migration doesn't re-enable node auto-upgrades for the node pool. We recommend that you [enable node auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#enable), because short-lived upgrades are not disruptive to existing nodes and the workloads that run on them. For more information, see [Short-lived upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#short-lived-upgrades-flex-start).
  * We also recommend that, if your cluster wasn't already enrolled in a release channel, you [enroll your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/release-channels#existing-cluster), so that you can use more granular maintenance exclusion scopes.



## Node recycling in flex-start

To help ensure a smooth transition of nodes and prevent downtime for your running jobs, flex-start supports _node recycling_. When a node reaches the end of its duration, GKE automatically replaces the node with a new one to preserve your running workloads.

To use _node recycling_ , you must create a [custom compute class profile](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes) and include the `nodeRecycling` field in the `flexStart` specification with the `leadTimeSeconds` parameter.

The `leadTimeSeconds` parameter lets you balance resource availability and cost efficiency. This parameter specifies how early (in seconds) before a node reaches the end of its seven-day duration for a new node provisioning process should start to substitute it. A longer lead time increases the probability that the new node is ready before the old one is removed, but might incur additional costs.

The node recycling process consists of the following steps:

  1. **Recycling phase:** GKE validates that a flex-start-provisioned node has the `nodeRecycling` field with the `leadTimeSeconds` parameter set. If so, GKE starts the node recycling phase when the current date is greater than or equal to the difference between the values from the following fields:

     * `creationTimestamp` plus `maxRunDurationSeconds`
     * `leadTimeSeconds`

The `creationTimeStamp` flag includes the time when the node was created. The `maxRunDurationSeconds` field can be specified in the [custom compute class](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes), and defaults to seven days.

  2. **Node creation:** the creation process for the new node begins, proceeding through queueing and provisioning phases. The duration of the queueing phase can vary dynamically depending on the zone and specific accelerator capacity.

  3. **Cordon the node that's reaching the end of its seven-day duration:** after the new node is running, the old node is cordoned. This action prevents any new Pods from being scheduled on it. Existing Pods in that node continue to run.

  4. **Node deprovisioning:** the node that's reaching the end of its seven-day duration is eventually deprovisioned after a suitable period, which helps ensure that running workloads have migrated to the new node.




The following example of a compute class configuration includes `leadTimeSeconds` and `maxRunDuration` fields:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: dws-model-inference-class
    spec:
      priorities:
        - machineType: g2-standard-24
          spot: true
        - machineType: g2-standard-24
          maxRunDurationSeconds: 72000
          flexStart:
            enabled: true
            nodeRecycling:
              leadTimeSeconds: 3600
      nodePoolAutoCreation:
        enabled: true
    

For more information about how to use node recycling, try the [Serve LLMs on GKE with a cost-optimized and high-availability GPU provisioning strategy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dws-flex-start-inference) tutorial.

## Limitations

  * [Inter-pod anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity) is not supported. Cluster autoscaler doesn't consider inter-pod anti-affinity rules during node provisioning, which might lead to unschedulable workloads. This situation might happen when nodes for two or more Dynamic Workload Scheduler objects were provisioned in the same node pool.
  * Reservations aren't supported with Dynamic Workload Scheduler. Dynamic Workload Scheduler requires and supports only the `ANY` [location policy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#location_policy) for cluster autoscaling.
  * A single Dynamic Workload Scheduler request can create up to 1,000 virtual machines (VMs), which is the maximum number of nodes per zone for a single node pool.
  * GKE uses the Compute Engine `ACTIVE_RESIZE_REQUESTS` quota to control the number of Dynamic Workload Scheduler requests that are pending in a queue. By default, this quota has a limit of 100 requests per Google Cloud project. If you attempt to create a Dynamic Workload Scheduler request that's greater than this quota, the new request fails.
  * Node pools that use Dynamic Workload Scheduler are sensitive to disruption because the nodes are provisioned together. To learn more, see Manage disruption in workloads that use Dynamic Workload Scheduler.
  * You might see additional short-lived VMs listed in the Google Cloud console. This behavior is intended because Compute Engine might create and then promptly remove VMs until the capacity to provision all of the required machines is available.
  * [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms) aren't supported.
  * Dynamic Workload Scheduler doesn't support [ephemeral volumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/generic-ephemeral-volumes#request-ephemeral-storage). You must use persistent volumes for storage. To select the best storage type that uses persistent volumes, see [Storage for GKE clusters overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/storage-overview).
  * If the workload uses node recycling and it's deployed by a Job, configure the Job with [completion mode](https://kubernetes.io/docs/concepts/workloads/controllers/job/#completion-mode) set to `Indexed`.
  * A single `ProvisioningRequest` object supports only one entry in the `podSets` list. Requests with multiple `podSet` entries fail.



## What's next

  * [Select a GPU type](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus#gpu-selection-gke)
  * [Deploy GPUs with Dynamic Workload Scheduler](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/provisioningrequest).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
