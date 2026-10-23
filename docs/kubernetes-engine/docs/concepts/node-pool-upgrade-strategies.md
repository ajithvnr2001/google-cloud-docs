---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies/
title: Node upgrade strategies \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:31.210494+00:00
---

# Node upgrade strategies  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Node upgrade strategies Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document discusses the node upgrade strategies you can use with your Google Kubernetes Engine (GKE) clusters.

In GKE Standard clusters, you can configure one of the following node upgrade strategies for each Standard node pool:

  * **Surge upgrades** : Nodes are upgraded in a rolling window. You can control how many nodes can be upgraded at once and how disruptive upgrades are to the workloads. You can also upgrade using fixed capacity for resource-constrained environments.
  * **Blue-green upgrades** : Existing nodes are kept available for rolling back while the workloads are validated on the new node configuration.
  * **Autoscaled blue-green upgrades** ([Preview](https://cloud.google.com/products#product-launch-stages)): Workloads can run for longer, while you minimize cost from idle or underutilized nodes.



GKE chooses the following strategies for these specific scenarios:

  * In Autopilot clusters, GKE uses surge upgrades. For more information, see the Autopilot cluster upgrades document's [Surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades-autopilot#surge) section.
  * For [Autopilot-managed node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools#autopilot-node-pools) in Standard clusters, GKE uses surge upgrades. You can't select a different strategy or change the configuration.
  * For nodes that use Flex-start VMs, GKE uses short-lived upgrades. Flex-start with queued provisioning supports new flags that are part of the flex-start preview launch. Flex-start is powered by Dynamic Workload Scheduler.



By choosing an upgrade strategy for your Standard node pool, you can pick the process with the right balance of speed, workload disruption, risk mitigation, and cost optimization. For more information about which node upgrade strategy is right for your environment, see the following:

  * When to choose surge upgrades
  * When to choose blue-green upgrades
  * When to choose autoscaled blue-green upgrades



With each of these strategies, you can configure upgrade settings to optimize the process based on your environment's needs. For more information, see [Configure your chosen upgrade strategy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pool-upgrade-strategies). Ensure that for the strategy that you pick, you have enough quota, resource availability, or reservation capacity to upgrade your nodes using that strategy. For more information about resource considerations, see [Ensure resources for node upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota). When upgrading in a resource-constrained environment, see [Upgrade in a resource-constrained environment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota#upgrade-resource-constrained).

**Note:** Node upgrade strategies are used for any type of node configuration change that requires the nodes to be recreated. For more information, see When GKE uses surge upgrades, When GKE uses blue-green upgrades, and When GKE uses autoscaled blue-green upgrades.

### Disruptive upgrades for node pools that use accelerators and run AI/ML workloads

Because Compute Engine instances with accelerators (GPUs or TPUs) don't support live migration, Compute Engine must shut down and re-create the nodes during host maintenance. This process can disrupt workloads such as AI/ML training or inference jobs. To minimize disruption, perform both Compute Engine host maintenance and GKE node upgrades at the same time. For more information, see [Perform host maintenance for nodes running training and inference workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/perform-host-maintenance-accelerators).

## Surge upgrades

Surge upgrades are the default upgrade strategy, and best for applications that can handle incremental changes. Surge upgrades use a rolling method to upgrade nodes, in an undefined order. Find the optimal balance of speed and disruption for your environment by choosing how many new, surge nodes can be created, with `maxSurge`, and how many existing nodes can be disrupted at once, with `maxUnavailable`.

Surge upgrades also work with the cluster autoscaler to prevent changes to nodes that are being upgraded.

### When to choose surge upgrades for your environment

If cost optimization is important for you and your workload can tolerate being shut down in less than 60 minutes, we recommend choosing surge upgrades for your node pools.

Surge upgrades are optimal for the following scenarios:

  * If you want to optimize for the speed of upgrades.
  * If workloads are more tolerant of disruptions, where graceful termination up to 60 minutes is acceptable.
  * If you want to control costs by minimizing the creation of new nodes.
  * If you are performing upgrades in a resource-constrained environment.



### When GKE uses surge upgrades

If enabled, GKE uses surge upgrades when the following types of changes occur:

  * [Version changes (upgrades)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades#node_pool_upgrades)
  * [Vertically scaling the nodes by changing the node machine attributes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#change-machine-attributes), including machine type, disk type, and disk size
  * [Image type changes](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade#--image-type)
  * [IP rotation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-rotation)
  * [Credential rotation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation)
  * [Network policy creation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy)
  * [Enabling image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming)
  * [Network performance configuration updates](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--network-performance-configs)
  * [Enabling gVNIC](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--enable-gvnic)
  * [Node system configuration changes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config)
  * [Confidential nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes#on_an_existing_node_pool)



Other changes, including [applying updates to node labels and taints of existing node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/update-existing-nodepools), don't use surge upgrades as they don't require recreating the nodes.

### Understand surge upgrade settings

Use surge upgrade settings to select the appropriate balance between speed and disruption for your node pool during cluster maintenance using the surge settings. You can change how many nodes GKE attempts to upgrade at once by [changing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pool-upgrade-strategies#surge) the surge upgrade parameters on a Standard node pool.

Surge upgrade behavior is determined by the `maxSurge` and `maxUnavailable` settings, which determine how many nodes are upgraded at the same time in a rolling window with the described steps. The following options are available:

  * To upgrade with _surge nodes_ , use the `maxSurge` field and set it to a value greater than zero. Upgrading by using surge nodes is helpful when you want to minimize disruption to workloads. For more information, see the `maxSurge`: GKE creates a new surge node before removing an existing one section.
  * To upgrade with _fixed capacity_ use the `maxUnavailable` field and set it to a value greater than zero. A fixed capacity upgrade is helpful when working in resource-constrained environments. For more information, see the `maxUnavailable`: GKE makes an existing node unavailable to recreate it section.
  * You can also use a combination of surge nodes and fixed capacity to upgrade your nodes. For more information, see the Example use of `maxSurge` and `maxUnavailable` settings section.



#### `maxSurge`: GKE creates a new surge node before removing an existing one

Set `maxSurge` to choose the maximum number of additional, surge nodes that can be added to the node pool during an upgrade, per zone. By using surge nodes increases the likelihood that workloads running on the existing node can migrate to a new node immediately. The default for the `maxSurge` field is one. To upgrade one node, GKE performs the following steps:

  1. Provision a new node.
  2. Wait for the new node to be ready.
  3. [Cordon](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#cordon) the existing node.
  4. [Drain](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#drain) the existing node, respecting [PodDisruptionBudget](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) and [GracefulTerminationPeriod](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination) settings for up to one hour. After one hour, any remaining Pods are forcefully evicted so that the upgrade can proceed.
  5. Delete the existing node.



For GKE to create surge nodes, your project must have the resources to temporarily create additional nodes. If you don't have additional capacity and the `maxUnavailable` field is set to zero, then GKE won't start upgrading a node until the resources are available. For more information, see [Resources for surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota#quota-surge-upgrades).

#### `maxUnavailable`: GKE makes an existing node unavailable to recreate it

Set `maxUnavailable` to a value greater than zero to upgrade using fixed capacity. The `maxUnavailable` field specifies the maximum number of nodes that can be simultaneously unavailable during an upgrade, per zone. The default is zero.

To upgrade one node, GKE performs the following steps:

  1. [Cordon](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#cordon) the existing node.
  2. [Drain](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#drain) the existing node, with the following considerations: 
     * The [PodDisruptionBudget](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) and [GracefulTerminationPeriod](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination) settings are respected for up to one hour. After one hour, any remaining Pods are forcefully evicted so that the upgrade can proceed.
     * If no other nodes have capacity, then workloads running on the existing node might need to wait for the existing node to upgrade. When these workloads wait, the Pods are in a pending state.
  3. Recreate the existing node with the new configuration.
  4. Wait for the existing node to be ready.
  5. Uncordon the existing, upgraded node.



To help preserve existing capacity when performing version upgrades in a resource-constrained environment, set the `maxUnavailable` field to a value greater than zero. For example, you could set `maxSurge=0` and `maxUnavailable=1`. For GPUs and TPUs, see additional guidance in [Upgrade in a resource-constrained environment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota#upgrade-resource-constrained).

When performing a version upgrade on CPU node pools, if the `maxUnavailable` field is set to a value greater than zero, then GKE reuses the same Compute Engine instance, which retains the existing capacity of the node.

For all other node pool updates and upgrades, when GKE re-creates the existing node using `maxUnavailable`, GKE temporarily releases the capacity of the node if the capacity isn't from a reservation. This means that if there is limited capacity, you risk losing the existing capacity.

For example, GKE doesn't reuse the existing Compute Engine instance and instead deletes and re-creates the instance in the following scenarios:

  * Node pool updates other than version upgrades (such as machine type, disk type, or disk size changes).
  * Version upgrades of node pools that contain GPUs or TPUs.
  * Version upgrades of node pools that use Spot VMs or preemptible VMs.
  * Rolling back an incomplete surge upgrade.
  * Node auto-repairs.



#### Example use of `maxSurge` and `maxUnavailable` settings

For example, a GKE cluster has a single-zone node pool with 30 nodes and the following surge upgrade configuration: `maxSurge=2;maxUnavailable=1`.

During a surge upgrade with this node pool, in a rolling window, GKE creates two new surge nodes (`maxSurge=2`) and immediately takes down one existing node (`maxUnavailable=1`). Once the two surge nodes are ready, GKE takes down two more existing nodes, disrupting up to three existing nodes at a time while keeping the node pool between 29 and 32 nodes.

For upgrades which support reusing the existing capacity of the node, the node upgraded using the `maxUnavailable=1` budget is upgraded in-place by reusing the existing instance, and if additional capacity is unavailable to create the two surge nodes, GKE still progresses the upgrade by upgrading one existing node at a time.

#### Considerations for surge upgrade settings

Consider the following information before configuring surge upgrade settings:

  * Nodes created by surge upgrade are subject to your Google Cloud [resource quotas](https://docs.cloud.google.com/compute/quotas), [resource availability](https://docs.cloud.google.com/compute/resource-usage#quotas_and_resource_availability), and [reservation capacity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations), for node pools with [specific reservation affinity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations#specific). If your environment is resource-constrained, see [Upgrade in a resource-constrained environment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota#upgrade-resource-constrained).
  * The number of nodes that GKE upgrades simultaneously is the sum of `maxSurge` and `maxUnavailable`. The maximum number of nodes upgraded simultaneously is limited to 20 for Autopilot mode and 100 for Standard mode. Surge upgrades also work with the [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) to prevent changes to nodes that are being upgraded.
  * GKE upgrades [multi-zone node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools#multiple-zones) one zone at a time. Surge upgrade parameters are applicable only up to the number of nodes in the zone. The maximum number of nodes that can be upgraded in parallel will be no higher than the sum of `maxSurge` plus `maxUnavailable`, and no higher than the number of nodes in the zone.
  * If your node pool uses Spot VMs, GKE creates surge nodes with Spot VMs, but doesn't wait for Spot VMs to be ready before cordoning and draining existing nodes. For more information, see [Upgrade Standard node pools using Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms#upgrade).



### Tune surge upgrade settings to balance speed and disruption

The following table describes four different upgrade profiles as examples to help you understand different configurations:

Description | Configuration | Typical use case  
---|---|---  
Balanced (Default), slower but least disruptive | `maxSurge=1 maxUnavailable=0` | Most workloads  
Balanced, resource constrained environments, no surge resources | `maxSurge=0 maxUnavailable=1` | Resource-constrained node pool  
Fast, no surge resources, most disruptive | `maxSurge=0 maxUnavailable=100` | Large node pools after jobs have to run to completion  
Fast, most surge resources and less disruptive | `maxSurge=100 maxUnavailable=0` | Large node pools  
  
#### Balanced (Default)

The simplest way to take advantage of surge upgrades is to use the default configuration, `maxSurge=1;maxUnavailable=0.` With this configuration, upgrades progress slowly, with only one surge node added at a time, meaning only one node is upgraded at a time. Pods can restart immediately on the new, surge node. This configuration only requires the resources to temporarily create one new node.

#### Fast and no surge resources

If you have a large node pool and your workload isn't sensitive to disruption (for example, a batch job that has run to completion), use the following configuration to maximize speed without using any additional resources: `maxSurge=0;maxUnavailable=100`. This configuration does not bring up additional surge nodes and allows 100 nodes to be upgraded at the same time.

#### Fast and less disruptive

If your workload is sensitive to disruption and you have already set up [PodDisruptionBudgets](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) (PDB) and you are not using `externalTrafficPolicy: Local`, which does not work with parallel node drains, you can increase the speed of the upgrade by using `maxSurge=100;maxUnavailable=0`. This configuration upgrades 100 nodes in parallel while the PDB limits the number of Pods that can be drained at a given time. Although the configurations of PDBs may vary, if you create a PDB with `maxUnavailable=1` for one or more workloads running on the node pool, then only one Pod of those workloads can be evicted at a time, limiting the parallelism of the entire upgrade. This configuration requires the resources to temporarily create 100 new nodes.

#### Balanced, resource constrained environments

If you can't use any additional resources, you can use `maxSurge=0;maxUnavailable=1` to recreate one node at a time.

### Control an in-progress surge upgrade

With surge upgrades, while an upgrade is in progress you can use commands to exercise some control over it. For more control over the upgrade process, we recommend using blue-green upgrades.

#### Cancel (pause) a surge upgrade

You can cancel an in-progress surge upgrade at any time during the upgrade process. Cancelling pauses the upgrade, stopping GKE from upgrading new nodes, but doesn't automatically roll back the upgrade of the already-upgraded nodes. After you cancel an upgrade, you can either resume or roll back.

When you cancel an upgrade, GKE does the following with each of the nodes:

  * Nodes that have started the upgrade complete it.
  * Nodes that have not started the upgrade don't upgrade.
  * Nodes that have already successfully completed the upgrade are unaffected and are not rolled back.



This means that the node pool might end up in a state where nodes are running two different versions. If [automatic upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades) are enabled for the node pool, the node pool can be scheduled for auto-upgrade again, which would upgrade the remaining nodes in the node pool running the older version.

Learn how to [cancel a node pool upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#cancel).

#### Resume a surge upgrade

If a node pool upgrade was canceled and left partially upgraded, you can resume the upgrade to complete the upgrade process for the node pool. This will upgrade any remaining nodes that had not been upgraded in the original operation. Learn how to [resume a node pool upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#resume).

#### Roll back a surge upgrade

If a node pool is left partially upgraded, you can roll back the node pool to revert it to its previous state. You can't roll back node pools after they have been successfully upgraded. Nodes that have not started an upgrade are unaffected. Learn how to [roll back a node pool upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#rollback).

If you want to downgrade a node pool back to its previous version after the upgrade is already complete, see [Downgrading node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#downgrading_nodes).

## Blue-green upgrades

Blue-green upgrades are an alternative upgrade strategy to the default surge upgrade strategy. With blue-green upgrades, GKE first creates a new set of node resources ("green" nodes) with the new node configuration before evicting any workloads on the original resources ("blue" nodes). GKE keeps the "blue" resources, if needed, for rolling back workloads until their soaking time has been met. You can adjust the pace of upgrades and soaking time based on your environment's needs.

With this strategy, you have more control over the upgrade process. You can roll back an in-progress upgrade, if necessary, as the original environment is maintained during the upgrade. This upgrade strategy, however, is also more resource intensive. As the original environment is replicated, the node pool uses double the number of resources during the upgrade.

### When to choose blue-green upgrades for your environment

If you have highly-available production workloads that you need to be able to roll back quickly in case the workload does not tolerate the upgrade, and a temporary cost increase is acceptable, we recommend choosing blue-green upgrades for your node pools.

Blue-green upgrades are optimal for the following scenarios:

  * if you want a gradual rollout where risk mitigation is most important, where graceful termination greater than 60 minutes is needed.
  * if your workloads are less tolerant of disruptions.
  * if a temporary cost increase due to higher resource usage is acceptable.



Blue-green upgrades continue until completion if they exceed a [maintenance window](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#maintenance_windows). For more information, see [How node upgrade strategies work with maintenance windows](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/upgrades#node-upgrade-strategies-maintenance-windows).

### When GKE uses blue-green upgrades

For GKE nodes, there are different types of configuration changes that require the nodes to be recreated. If enabled, GKE uses blue-green upgrades when the following types of changes occur:

  * [Version changes (upgrades)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades#node_pool_upgrades)
  * [Vertically scaling the nodes by changing the node machine attributes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#change-machine-attributes), including machine type, disk type, and disk size
  * [Image type changes](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade#--image-type)
  * [Add or replace storage pools in a node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/hyperdisk-storage-pools#when-updating-node-pool)



Surge upgrades are used for any other updates requiring the nodes to be recreated. For more information, see When surge upgrades are used.

### Phases of blue-green upgrades

With blue-green upgrades, you can customize and control the process by:

  * using the upgrade configuration parameters.
  * using commands to cancel (pause), resume, roll back, or complete the steps.



This section explains the phases of the upgrade process. You can use upgrade settings to tune how the phases work, and commands to control the upgrade process.

#### Phase 1: Create green pool

In this phase, a new set of managed instance groups (MIGs)—known as the "green" pool—are created for each zone under the target pool with the new node configuration (new version or image type).

[Quota](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota) will be checked before starting provisioning new green resources.

In this phase, the original MIGs—known as the blue pool—cluster autoscaler will stop scaling up or down. The green pool can only scale up in this phase.

In this phase, you can cancel the upgrade if necessary. When you cancel a blue-green upgrade, the upgrade is paused in its current phase. After you've canceled it, you can either resume it or roll back. At this phase, rolling back will delete the green pool.

#### Phase 2: Cordon blue pool

In this phase, all the original nodes in the blue pool (existing MIGs) will be cordoned (marked as unschedulable). Existing workloads will keep running, but new workloads won't be scheduled on the existing nodes.

In this phase, you can cancel the upgrade if necessary. When you cancel a blue-green upgrade, the upgrade is paused in its current phase. After you've canceled it, you can either resume it or roll back. At this phase, rolling back will un-cordon the blue pool and delete the green pool.

#### Phase 3: Drain blue pool

In this phase, the original nodes in the blue pool (existing MIGs) will be drained in batches. When Kubernetes drains a nodes, eviction requests are sent to all the Pods running on the node. The Pods will be rescheduled. For Pods that have [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#how-disruption-budgets-work) violations or long [terminationGracePeriodSeconds](https://v1-30.docs.kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#podtemplatespec-v1-core) during the draining, they will be deleted in the Delete blue pool phase when the node is deleted. You can use `BATCH_SOAK_DURATION` and `NODE_POOL_SOAK_DURATION`, which are described here and in the next section, to extend the period before Pods are deleted.

**Note:** To ensure that Pods evicted from nodes in the blue pool only get rescheduled to nodes in the green pool, add a nodeSelector for the label `cloud.google.com/gke-nodepool: ${MY_NODE_POOL}` to your workload. If you omit this label and have other node pools in your cluster, your evicted Pods might be scheduled to those nodes.

You can control the size of the batches with either of the following settings:

  * `BATCH_NODE_COUNT`: the absolute number of nodes to drain in a batch.
  * `BATCH_PERCENT`: the percentage of nodes to drain in a batch, expressed as a decimal between 0 and 1, inclusive. GKE rounds down to the nearest percentage of nodes, to a minimum value of 1 node, if the percentage isn't a whole number of nodes.



If either of these settings are set to zero GKE skips this phase and proceeds to the Soak node pool phase.

Additionally, you can control how long each batch drain soaks with `BATCH_SOAK_DURATION`. This duration is defined in seconds, with the default being zero seconds. 

In this phase, you can still cancel the upgrade if necessary. When you cancel a blue-green upgrade, the upgrade is paused in its current phase. After you've canceled it, you can either resume it or roll back. If the previous batch is already drained and you resume the upgrade, the next batch of nodes might be immediately processed without honoring the `BATCH_SOAK_DURATION` for that batch. Rolling back at this phase stops the draining of the blue pool and uncordons it. Workloads can then be rescheduled on the blue pool (not guaranteed), and the green pool is drained and deleted.

#### Phase 4: Soak node pool

This phase is used for you to verify the workload's health after the blue pool nodes have been drained.

The soak time is set with `NODE_POOL_SOAK_DURATION`, in seconds. By default, it is set to one hour (3600 seconds). If the total soak duration reaches 7 days (604,800 seconds), the Delete blue pool phase begins immediately.

The total soak duration is the sum of `NODE_POOL_SOAK_DURATION`, plus `BATCH_SOAK_DURATION` multiplied by the number of batches, which is determined by either `BATCH_NODE_COUNT` or `BATCH_PERCENT`.

In this phase, you can finish the upgrade and skip any remaining soak time by completing the upgrade. This will immediately begin the process of removing the blue pool nodes.

You can still cancel the upgrade if necessary. When you cancel a blue-green upgrade, the upgrade is paused in its current phase. After you've canceled it, you can either resume it or roll back.

In this phase, cluster autoscaler can now scale up or down the green pool as normal.

#### Phase 5: Delete blue pool

After the expiration of the soaking time, the blue pool nodes will be removed from the target pool. This phase can't be paused. Also, this phase does not use eviction and instead attempts to delete the Pods. Unlike eviction, deletion doesn't respect PDBs and forcibly deletes the Pods. The deletion caps a Pod's `terminationGracePeriodSeconds` to no more than 60 minutes. After this final attempt is made to delete the remaining Pods, the blue pool nodes are deleted from the node pool.

At the completion of this phase, your node pool will have only new nodes with the updated configuration (version or image type).

### How cluster autoscaler works with blue-green upgrades

During the phases of a blue-green upgrade, the original "blue" pool does not scale up or down. When the new "green" pool is created, it can only be scaled up until the Soak node pool phase, where it can scale up or down. If an upgrade is rolled back, the original "blue" pool might scale up during this process if additional capacity is needed.

### Control an in-progress blue-green upgrade

With blue-green upgrades, while an upgrade is in progress you can use commands to exercise control over it. This gives you a high level of control over the process in case you determine, for instance, that your workloads need to be rolled back to the old node configuration.

#### Cancel (pause) a blue-green upgrade

When you cancel a blue-green upgrade, you pause the upgrade in its current phase. This command can be used at all phases except the Delete blue pool phase. When cancelled, the node pool will be paused at an intermediate status based on the phase where the request was issued.

Learn how to [cancel a node pool upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#cancel).

After an upgrade is canceled, you can choose one of two paths forward: resume or roll back.

#### Resume a blue-green upgrade

If you have determined the upgrade is okay to move forward, you can resume it.

If you resume, the upgrade process will continue at the intermediate phase it was paused. To learn how to resume a node pool upgrade, see [Resume a node pool upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#resume).

#### Roll back a blue-green upgrade

If you have determined that the upgrade shouldn't move forward and you want to bring the node pool back to its original state, you can roll back. To learn how to roll back a node pool upgrade, see [roll back a node pool upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#rollback).

With the roll back workflow, the process reverses itself to bring the node pool back to its original state. The blue pool will be un-cordoned so that workloads may be rescheduled on it. During this process, cluster autoscaler may scale up the blue pool as needed. The green pool will be drained and deleted.

If you want to downgrade a node pool back to its previous version after the upgrade is already complete, see [Downgrading node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#downgrading_nodes).

#### Complete a blue-green upgrade

During the Soak phase, you can complete an upgrade if you have determined that the workload does not need further validation on the new node configuration and the old nodes can be removed. Completing an upgrade skips the rest of the Soak phase and proceeds to the Delete blue pool phase.

For more information about how to use the `complete` command, see [Complete a blue-green node pool upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#complete).

## Autoscaled blue-green upgrades

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** Autoscaled blue-green upgrades require the cluster's control plane to run version 1.34.0-gke.2201000 or later, and require cluster autoscaling to be enabled.

Autoscaled blue-green upgrades are a different type of upgrade strategy that maximizes the amount of time before disruption-intolerant workloads are evicted, while minimizing cost. This strategy is derived from the standard blue-green upgrades. However, with autoscaled blue-green upgrades, GKE doesn't drain nodes with workloads that are marked as not safe to evict for up to seven days after the nodes are cordoned.

The following section explains when you should choose this strategy, how this strategy's implementation of blue-green upgrades is different from the standard blue-green upgrades, and what best practices you should follow when using this strategy.

To use autoscaled blue-green upgrades, see [Configure autoscaled blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pool-upgrade-strategies#configure-autoscaled-blue-green).

### When to choose autoscaled blue-green upgrades for your environment

If you have workloads that need the maximum amount of time before eviction, but don't need to be rescheduled as quickly as possible, we recommend choosing autoscaled blue-green upgrades for your node pools.

Autoscaled blue-green upgrades works well if these scenarios apply to you:

  * You have batch workloads that must run to completion.
  * You want to minimize cost compared to standard blue-green upgrades by minimizing the amount of idle or underutilized nodes.
  * You don't need Pods to be guaranteed immediate rescheduling, or immediate rollback to the previous node configuration.



Choose standard blue-green upgrades if you need to minimize the time to reschedule workloads to new nodes, and the ability to roll back to the previous node configuration.

Autoscaled blue-green upgrades, like standard blue-green upgrades, continue until completion if they exceed a [maintenance window](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#maintenance_windows). For more information, see [How node upgrade strategies work with maintenance windows](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/upgrades#node-upgrade-strategies-maintenance-windows).

### Phases of autoscaled blue-green upgrades

When GKE upgrades node pools with autoscaled blue-green upgrades, the phases differ from standard blue-green upgrades. For the standard upgrade strategy's phases, see the phases of blue-green upgrades.

When the autoscaled blue-green upgrades policy is enabled, GKE performs these steps during an operation:

  1. GKE creates the green pool. However, the green pool starts with zero nodes. When GKE evicts Pods from the blue pool in a later phase, cluster autoscaler scales up the green pool to run those Pods.
  2. GKE cordons the blue pool.
  3. GKE waits for a period of time, which you can configure from zero to seven days (with a default of three days). During this time, GKE does the following:

     * Cluster autoscaler scales down underutilized blue pool nodes, unless those nodes have Pods that are running the `"cluster-autoscaler.kubernetes.io/safe-to-evict": "false"` annotation. This annotation ensures that workloads needing the most time to spin down can continue to run. If cluster autoscaler isn't actively scaling down underutilized nodes, see [Troubleshoot cluster autoscaler not scaling down](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cluster-autoscaler-scale-down) and [Consider Pod scheduling and disruption](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#scheduling-and-disruption).
     * GKE ignores the [autoscaling limits](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#autoscaling_limits) of the `--min-nodes` and `--total-min-nodes` parameters when scaling down the blue pool. If all blue pool nodes are scaled down before this period of time is complete, GKE immediately proceeds to the phase to delete the blue pool.
  4. GKE drains the blue pool, draining the remaining blue pool nodes up to 20 at a time in parallel. GKE respects `PodDisruptionBudget` settings for up to 1 hour, and `terminationGracePeriodSeconds` settings for up to 24 hours.

  5. GKE skips the soak node pool phase.

  6. GKE deletes the blue pool.




### Best practices for autoscaled blue-green upgrades

The following sections provide best practices—for your cluster, node pool, and Pods—to minimize workload disruption during autoscaled blue-green upgrades.

#### Cluster and node pool configuration

  * GKE respects the [autoscaling limits](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#autoscaling_limits) when scaling up the green pool. Set the `--max-nodes` or `--total-max-nodes` parameters high enough so that cluster autoscaler can scale up the green pool when GKE reschedules workloads from the blue pool to the green pool. GKE doesn't respect the `--min-nodes` or `--total-min-nodes` parameters when scaling down the blue pool.
  * Configure the `optimize-utilization` autoscaling profile if you want GKE to scale down underutilized nodes in the blue pool more aggressively. For more information, see [Autoscaling profiles](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#autoscaling_profiles).
  * Don't update node pools created with [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning) to use autoscaled blue-green upgrades. Also, don't configure your cluster to use autoscaled blue-green upgrades [for new auto-provisioned node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#bg-nap-settings).



#### Pod configuration

  * To ensure that Pods are not evicted during the pause before draining the blue pool, add the `"cluster-autoscaler.kubernetes.io/safe-to-evict": "false"` annotation to those Pods. This annotation prevents cluster autoscaler from evicting the Pod if the Pod's node is underutilized.
  * Like with standard blue-green upgrades, to help ensure that Pods evicted from nodes in the blue pool only get rescheduled to nodes in the green pool, add a nodeSelector for the `cloud.google.com/gke-nodepool:NODE_POOL_NAME` label to your workload. If you omit this label and have other node pools in your cluster, your evicted Pods might be scheduled to nodes in those other node pools.



### Limitations of autoscaled blue-green upgrades

  * You can cancel and resume autoscaled blue-green upgrades; however, you can't roll back the canceled upgrade.
  * When the blue pool is cordoned and drained, Pods can become temporarily unschedulable if cluster autoscaler can't scale up the green pool due to [quotas and limits](https://docs.cloud.google.com/kubernetes-engine/quotas) or [resource availability](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshoot-node-pools#insufficient-resources), because the green pool is created with zero nodes.
  * You can only upgrade node pools with autoscaled blue-green upgrades if the cluster's control plane is running version 1.34.0-gke.2201000 or later, and cluster autoscaler is enabled.



### When GKE uses autoscaled blue-green upgrades

GKE uses autoscaled blue-green upgrades for the same types of changes as standard blue-green upgrades. For more information about the types of changes GKE uses the standard blue-green upgrade strategy for, see When GKE uses blue-green upgrades.

### How cluster autoscaler works with autoscaled blue-green upgrades

To configure autoscaled blue-green upgrades, you must also configure cluster autoscaler.

If you use autoscaled blue-green upgrades, cluster autoscaler does the following:

  * During the phase where GKE waits to drain the blue pool, the blue pool doesn't scale up and is only scaled down by cluster autoscaler when the nodes become underutilized. Cluster autoscaler can scale down the blue pool to zero, without respecting the `--min-nodes` or `--total-min-nodes` parameters. In all of the other phases, cluster autoscaler doesn't scale up or down the blue pool.
  * Cluster autoscaler scales up the green pool from zero nodes, or down to the `--min-nodes` setting, as required in all of the phases of the upgrade strategy.



## Short-lived upgrades (flex-start and queued provisioning only)

Short-lived upgrades are a node upgrade strategy exclusively for use with nodes that use Flex-start VMs and nodes that use queued provisioning (with 1.32.2-gke.1652000 or later), both of which are powered by Dynamic Workload Scheduler. For more information about the nodes that use short-lived upgrades, see [About GPU, TPU, and H4D consumption with flex-start provisioning mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws).

GKE uses the short-lived upgrades strategy for Standard node pools and groups of nodes in Autopilot clusters.

With this strategy, GKE upgrades these limited runtime nodes without disrupting existing workloads. The strategy works in the following way:

  1. Existing nodes run until they're preempted.
  2. New nodes use the new node configuration.
  3. Over a maximum of seven days, the nodes transition from running the existing configuration to running the new configuration.



GKE automatically configures this strategy for nodes that use Flex-start VMs. This strategy has no configuration settings.

### When GKE uses short-lived upgrades

GKE automatically sets nodes that use Flex-start VMs to apply short-lived upgrades. Nodes which only use queued provisioning, but run on clusters on GKE version 1.32.2-gke.1652000 or later, also use short-lived upgrades.

For Standard node pools and groups of nodes in Autopilot clusters that use short-lived upgrades, GKE uses this strategy in situations where surge upgrades would otherwise be used. In addition to node upgrades (version changes), GKE uses short-lived upgrades for other types of node updates, similar to how surge upgrades are used. For more information, see When surge upgrades are used.

## What's next

  * Learn how to [manually upgrade a cluster or node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster).
  * Learn how to [configure node pool upgrade strategies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pool-upgrade-strategies).
  * Learn how to [configure node auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades).
  * Learn more about [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions).
  * Learn more about [best practices for upgrading clusters](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/upgrading-clusters).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
