---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota/
title: Ensure resources for node upgrades \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:17.208142+00:00
---

# Ensure resources for node upgrades  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Ensure resources for node upgrades Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to ensure that you can use [node upgrade strategies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies) to make changes to your cluster's nodes. We recommend verifying whether your project has enough resources to update your Google Kubernetes Engine (GKE) Standard node pools depending on the strategy that you choose.

## Required resources for node upgrades

Node upgrades might require GKE to temporarily create additional nodes, depending on which node strategy and configuration that you chose. Because of this, GKE might require additional resources for a node pool upgrade.

All nodes that GKE creates, including nodes used for upgrades, are subject to the [resource quota](https://docs.cloud.google.com/compute/quotas) of your project, [resource availability](https://docs.cloud.google.com/compute/resource-usage#quotas_and_resource_availability), and [reservation capacity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations), for node pools with [specific reservation affinity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations#specific).

We strongly recommend verifying you have adequate resources if you have special machine type requirements and capacity constraints. You might need to configure a strategy that requires less resources to ensure that you can upgrade your nodes, or take other action such as creating a reservation. To learn more, see Upgrade in a resource-constrained environment.

## Resources needed for different upgrade strategies

The following sections describe the additional resources are required to use the available upgrade strategies. If you're experiencing upgrade issues, check upgrade operations and follow the instructions to resolve upgrade errors.

### Resources for surge upgrades

Surge upgrades are the default node upgrade strategy. As [surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#surge) create extra VMs—if `maxSurge` is set to more than zero—before draining and deleting old nodes, upgrades can fail if your project does not have enough resources.

If the available resources are less than the number of nodes specified in `maxSurge`, then the number of parallel upgrades is less than `maxSurge` plus `maxUnavailable`. If you have no additional capacity, see how to upgrade in a resource-constrained environment.

The following table describes examples to demonstrate different upgrade behaviors:

Upgrade Settings | Number of additional nodes allowed by available resources | Result  
---|---|---  
maxSurge: 5 maxUnavailable: 0  | 5 | Upgrades 5 nodes in parallel.  
maxSurge: 5 maxUnavailable: 0  | 2 | Upgrades only 2 nodes in parallel.  
maxSurge: 5 maxUnavailable: 0  | 0 |  **Upgrade fails** , since it's not possible to bring up additional nodes and restarting existing ones is prohibited by the upgrade settings. GKE continues to try automatically upgrading until the operation succeeds.   
maxSurge: 5 maxUnavailable: 1  | 5 | Upgrades 6 nodes in parallel, while ensuring the node pool temporarily loses only one node due to upgrade.  
maxSurge: 5 maxUnavailable: 1  | 2 | Upgrades only 3 nodes in parallel, while ensuring the node pool is no more than one node short due to upgrade.  
maxSurge: 5 maxUnavailable: 1  | 0 | Upgrades only 1 node at a time by recreating each node with a rolling upgrade method.  
  
## Resources for blue-green upgrades

[Blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#blue-green) temporarily double the number of nodes in a node pool, which means that your node pool temporarily needs twice as many resources. If you don't have enough resources available and you configured your node pool to use this strategy, [configure surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pool-upgrade-strategies#surge) instead if you need to unblock upgrades. When configuring this strategy, ensure that you configure surge upgrade parameters that'll work with the available resources for the node pool's nodes. To learn more, see the previous section, Resources for surge upgrades.

## Check upgrade operations for resource-related failures

You can find more information about your upgrade operations as well as information about if and why any upgrades failed by checking your upgrade operation objects. To list the upgrade operation objects, run the following command:
    
    
    gcloud container operations list \
        --filter="STATUS=DONE AND TYPE=UPGRADE_NODES AND targetLink:https://container.googleapis.com/v1/projects/PROJECT_ID/zones/COMPUTE_ZONE/clusters/CLUSTER_NAME"
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `COMPUTE_ZONE`: the Compute Engine [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) for your cluster.
  * `CLUSTER_NAME`: the name of your cluster.



If your most recent upgrade failed due to insufficient resource quota, the output is similar to the following:
    
    
    gcloud container operations describe operation-1234567891234-1abc2d3e
    detail: "**Insufficient quota to satisfy the request** : waiting on IG: instance https://www.googleapis.com/compute/v1/projects/my-project-123/zones/us-central1-a/instances/gke-my-cluster-default-pool-123ab45c-de67\
      \ is still CREATING. Last attempt errors: **[QUOTA_EXCEEDED]** Instance 'gke-my-cluster-default-pool-123ab45c-de67'\
      \ creation failed: **Quota 'IN_USE_ADDRESSES' exceeded.  Limit: 50.0 in region us-central1**.\
    ...
    

If the reason was due to insufficient reservation, the output is similar to the following:
    
    
    gcloud container operations describe operation-1234567891234-1abc2d3e
    detail: "**Reservation does not have enough resources for the request** : waiting on IG:\
      \ instance https://www.googleapis.com/compute/v1/projects/my-project-123/zones/us-central1-a/instances/gke-my-cluster-default-pool-123ab45c-de67\
      \ is still CREATING. Last attempt error: **[CONDITION_NOT_MET]** Instance 'gke-my-cluster-default-pool-123ab45c-de67'\
      \ creation failed: **Specified reservation 'foo' does not have available resources\
      \ for the request.** "
    

If the reason was due to insufficient capacity, you'll see [resource availability error messages](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-vm-creation#resource_availability).

## Resolving upgrade errors

If your upgrade failed due to insufficient resources, try these steps:

  1. Consider a less resource-intensive upgrade strategy. If you're using blue-green upgrades, consider surge upgrades.
  2. Check if there are any Compute Engine resources in your project that are consuming resources and are no longer needed. If you find any, remove them and retry the upgrade.
  3. If the first two steps can't unblock your upgrade, [request a quota increase](https://docs.cloud.google.com/compute/quotas#requesting_additional_quota) or [increase the size of the specific reservation](https://docs.cloud.google.com/compute/docs/instances/reserving-zonal-resources#resizing_a_reservation).
  4. If you're operating in a resource-constrained environment with, for example, special machine type requirements and capacity constraints, see the next section for steps to unblock upgrades.

**Note:** Your configuration determines resource requirements. For example, the [machine type](https://docs.cloud.google.com/compute/docs/machine-types) for your node pool implies resources requirements of a single node. If you create a private cluster, you won't need external IPs for your nodes.

## Upgrade in a resource-constrained environment

If Google Cloud has limited capacity for a specific resource that your node pool is using, then for GPUs and TPUs we recommend that you [use a reservation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations). For node pools that only contain CPUs, we recommend that you upgrade CPUs using fixed capacity.

These two strategies can help ensure that you have adequate resources to perform a version upgrade. If you don't have adequate resources, you might not be able to upgrade your nodes until you can access more capacity.

If you don't have additional capacity, then you can't use blue-green upgrades.

When you use surge upgrades in a resource-constrained environment, note the following:

  * When you use surge nodes for an upgrade requires additional nodes, which might be difficult to achieve in a resource-constrained environment. For more information about this setting, see [`maxSurge`: GKE creates a new surge node before removing an existing one](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#max-surge).
  * When you set the `maxUnavailable` field to a value greater than zero and the capacity isn't from a reservation, then in some scenarios GKE temporarily releases the capacity of the node when upgrading it. This means that if there is limited capacity, you risk losing the capacity. For more information, see [`maxUnavailable`: GKE makes an existing node unavailable to recreate it](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#max-unavailable).



Use the following guidance, depending on whether you have a reservation for your node pool that needs to be upgraded.

### Upgrade with fixed capacity

For CPUs, to upgrade in a resource-constrained environment, use fixed capacity. To do so, use surge upgrades and set the `maxUnavailable` setting to a value greater than zero. For details, see [`maxUnavailable`: GKE makes an existing node unavailable to recreate it](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#max-unavailable).

Upgrading using a fixed capacity lets you perform upgrades when you can't get any additional capacity, and helps prevent you from losing existing capacity during the upgrade.

### Upgrade with limited capacity with a reservation

For GPUs and TPUs, to upgrade in a capacity-constrained environment, [use a reservation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations) and [tune surge upgrade settings for speed and reliability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#optimizing-surge).

If you have additional capacity in the reservation, you can use `maxSurge` to create surge nodes. Set `maxSurge` depending on how many nodes you want to disrupt at one time, and how much additional capacity you have. For example, set `maxSurge=1;maxUnavailable=0` if you only want to disrupt one node at a time, or if you only have capacity to create one additional node.

If you don't have any additional capacity, you can use `maxUnavailable` with a configuration such as `maxSurge=0;maxUnavailable=1`, as the capacity is reserved. This configuration disrupts one node a time, recreating the node to update it. We recommend this approach for [performing host maintenance for nodes running training and inference workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/perform-host-maintenance-accelerators#use_surge_upgrades).

## What's next

  * Learn about [Node upgrade strategies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies)
  * Learn about [resource quota](https://docs.cloud.google.com/compute/quotas)
  * Learn about [consuming reservations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
