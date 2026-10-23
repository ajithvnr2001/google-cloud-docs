---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pool-upgrade-strategies/
title: Configure node upgrade strategies \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:17.015141+00:00
---

# Configure node upgrade strategies  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pool-upgrade-strategies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Configure node upgrade strategies Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

As a platform administrator, you can configure a node upgrade strategy to tune how Google Kubernetes Engine (GKE) upgrades the nodes in your GKE clusters. For more information about node upgrade strategies, see [Node upgrade strategies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Requirements

  * To use autoscaled blue-green upgrades, a cluster's control plane must be running version 1.34.0-gke.2201000 or later, and have cluster autoscaler enabled.



## Configure a node upgrade strategy

When configuring your cluster's Standard node pools, you can select and configure one of the following supported node upgrade strategies:

  * [Surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#surge)
  * [Blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#blue-green-upgrade-strategy)
  * [Autoscaled blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#autoscaled-blue-green-upgrade-strategy)



Using these upgrade strategies lets you optimize the node pool upgrade process based on your cluster environment's needs. [Autopilot-managed node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools#autopilot-node-pools) in Standard clusters use surge upgrades, and you can't select a different strategy or change the configuration.

**Important:** Because Compute Engine instances with accelerators (GPUs or TPUs) don't support live migration, Compute Engine must shut down and re-create the nodes during host maintenance. This process can disrupt workloads such as AI/ML training or inference jobs. To minimize disruption, perform both Compute Engine host maintenance and GKE node upgrades at the same time. For more information, see [Perform host maintenance for nodes running training and inference workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/perform-host-maintenance-accelerators).

## Configure surge upgrades

[Surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#surge) allow you to change the number of nodes GKE upgrades at one time and the amount of disruption an upgrade makes on your workloads. 

The `max-surge-upgrade` and `max-unavailable-upgrade` flags are defined for each node pool. For more information on choosing the right parameters, go to [Optimize your surge upgrade configuration](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#optimizing-surge). 

**Note:** All new node pools are automatically configured to use surge upgrades `maxSurge=1 maxUnavailable=0`. To tune your configuration, see [Optimize your surge upgrade configuration](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#optimizing-surge). **Warning:** For [nodes that use Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/spot-vms), surge upgrade values are ignored because there is no availability guarantee. During an upgrade, old nodes are drained directly without waiting for surge nodes that use Spot VMs to be ready. 

You can change these settings when creating or updating a cluster or node pool.

The following variables are used in the commands mentioned below:

  * `CLUSTER_NAME`: the name of the cluster for the node pool.
  * `COMPUTE_ZONE`: the zone for the cluster.
  * `NODE_POOL_NAME`: the name of the node pool.
  * `NUMBER_NODES`: the number of nodes in the node pool in each of the cluster's zones.
  * `SURGE_NODES`: the number of extra (surge) nodes to be created on each upgrade of the node pool.
  * `UNAVAILABLE_NODES`: the number of nodes that can be unavailable at the same time on each upgrade of the node pool.



####  Creating a cluster with specific surge parameters 

To create a cluster with specific settings for surge upgrades, use the `max-surge-upgrade` and `max-unavailable-upgrade` flags.
    
    
    gcloud container clusters create CLUSTER_NAME \
        --max-surge-upgrade=SURGE_NODES --max-unavailable-upgrade=UNAVAILABLE_NODES

####  Creating a cluster which uses fixed capacity to upgrade 

To create a cluster, which uses fixed capacity to upgrade, set the value for the `max-surge-upgrade` flag to `0`, and the `max-unavailable-upgrade` flag to a value greater than `0`.
    
    
    gcloud container clusters create CLUSTER_NAME \
        --max-surge-upgrade=0 --max-unavailable-upgrade=1

####  Creating a node pool with specific surge parameters 

To create a node pool in an existing cluster with specific settings for surge upgrades, use the `max-surge-upgrade` and `max-unavailable-upgrade` flags.
    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --num-nodes=NUMBER_NODES --cluster=CLUSTER_NAME \
        --max-surge-upgrade=SURGE_NODES --max-unavailable-upgrade=UNAVAILABLE_NODES

####  Change surge upgrade settings for an existing node pool 

To update the upgrade settings of an existing node pool, use the `max-surge-upgrade` and `max-unavailable-upgrade` flags. If you set `max-surge-upgrade` to greater than `0`, GKE creates surge nodes. If you set `max-surge-upgrade` to `0`, GKE doesn't create surge nodes. 
    
    
    gcloud container node-pools update NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --max-surge-upgrade=SURGE_NODES --max-unavailable-upgrade=UNAVAILABLE_NODES

####  Checking if surge upgrades are enabled on a node pool 

To see if surge upgrades are enabled on a node pool, use `gcloud` to describe the cluster's parameters:
    
    
    gcloud container node-pools describe NODE_POOL_NAME \
        --cluster=CLUSTER_NAME

If surge upgrades are enabled on the node pool, the strategy listed is `SURGE`.

**Note:** While recreating nodes does not require additional Compute Engine resources, surge upgrading nodes does. Resource allocation is subjected to [Compute Engine quota](https://docs.cloud.google.com/compute/quotas). Depending on your configuration, this quota can limit the number of parallel upgrades or even cause the upgrade to fail. If you don't have any additional quota or reservation for the nodes in your node pool, then use a fixed capacity by setting the `max-unavailable-upgrade` flag to a value greater than `0`. For more information about quota, go to [Ensure resources for node upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota).

## Configure blue-green upgrades

With [blue-green node pool upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#blue-green-upgrade-strategy), you can control:

  * `BATCH_NODE_COUNT` or `BATCH_PERCENT`: the size of batches of nodes that GKE drains at a time, meaning that the Pods are removed from the nodes. Default is `BATCH_NODE_COUNT=1`. If either of these settings are set to 0, GKE skips this phase and proceeds to the [Soak node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#bg-phase-soak-node-pool) phase.
  * `BATCH_SOAK_DURATION`: the time between each batch of nodes being drained.
  * `NODE_POOL_SOAK_DURATION`: the amount of soak time for you to validate your workload on the new node configuration.



For more information about how the phases of blue-green upgrades work, see [Phases of blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#phases-of-blue-green-upgrades).

The following variables are used in the commands listed in the next sections:

  * `CLUSTER_NAME`: the name of the cluster for the node pool.
  * `NODE_POOL_NAME`: the name of the node pool.
  * `NUMBER_NODES`: the number of nodes in the node pool in each of the cluster's zones.
  * `BATCH_NODE_COUNT`: the number of blue nodes to drain in a batch during the blue pool drain phase. Default is 1. If it is set to 0, the blue pool drain phase will be skipped.
  * `BATCH_PERCENT`: the percentage of blue nodes to drain in a batch during the blue pool drain phase, expressed as a decimal between 0 and 1, inclusive. GKE rounds down to the nearest node, to a minimum value of 1 node, if the percentage isn't a whole number of nodes. If it is set to 0 the blue pool drain phase will be skipped.
  * `BATCH_SOAK_DURATION`: the duration in seconds to wait after each batch drain. Default is 0.
  * `NODE_POOL_SOAK_DURATION`: the duration in seconds to wait after completing drain of all batches. Default is 3600 seconds.



### Creating a node pool that uses the blue-green upgrade strategy

#### Create a node pool that uses blue-green upgrade default parameters

To create a node pool in an existing cluster that uses the blue-green upgrade strategy with the default parameters, use the following command:
    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --enable-blue-green-upgrade
    

#### Create a node pool that uses blue-green upgrades with absolute node count batch sizes

To create a node pool that uses custom blue-green upgrade settings, use the parameter flags with the node pool creation command.

This command creates a node pool with the following customized blue-green configuration, using an absolute node count for the batch drains:

  * `BATCH_NODE_COUNT` = 2
  * `BATCH_SOAK_DURATION` = 10s
  * `NODE_POOL_SOAK_DURATION` = 600s


    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --enable-blue-green-upgrade \
        --standard-rollout-policy=batch-node-count=2,batch-soak-duration=10s \
        --node-pool-soak-duration=600s
    

#### Create a node pool that uses blue-green upgrade with percentage-based batch sizes

This command creates a node pool with the following customized blue-green configuration, using a percentage for the batch drains:

  * `BATCH_PERCENTAGE` = 25% (of the node pool size)
  * `BATCH_SOAK_DURATION` = 10s
  * `NODE_POOL_SOAK_DURATION` = 1800s


    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --enable-blue-green-upgrade \
        --standard-rollout-policy=batch-percent=0.25,batch-soak-duration=10s \
        --node-pool-soak-duration=1800s
    

### Updating an existing node pool to use the blue-green upgrade strategy

#### Update a node pool to use blue-green upgrades with the default parameters

To update an existing node pool to the blue-green upgrade strategy, use the following command:
    
    
    gcloud container node-pools update NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --enable-blue-green-upgrade
    

#### Update a node pool to use blue-green upgrades with absolute node count batch sizes

To update an existing node pool to the blue-green upgrade strategy with custom settings, use the parameter flags with the node pool creation command.

This command updates a node pool to use the following customized blue-green configuration, using an absolute node count for the batch drains:

  * `BATCH_NODE_COUNT` = 2
  * `BATCH_SOAK_DURATION` = 10s
  * `NODE_POOL_SOAK_DURATION` = 600s


    
    
    gcloud container node-pools update NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --enable-blue-green-upgrade \
        --standard-rollout-policy=batch-node-count=2,batch-soak-duration=10s \
        --node-pool-soak-duration=600s
    

#### Update a node pool to use blue-green upgrades with percentage-based batch sizes

This command creates a node pool with the following customized blue-green configuration, using a percentage for the batch drains:

  * `BATCH_PERCENTAGE` = 25% (of the node pool size)
  * `BATCH_SOAK_DURATION` = 10s
  * `NODE_POOL_SOAK_DURATION` = 1800s


    
    
    gcloud container node-pools update NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --enable-blue-green-upgrade \
        --standard-rollout-policy=batch-percent=0.25,batch-soak-duration=10s \
        --node-pool-soak-duration=1800s
    

### Switching back to surge upgrades

You can change the behavior of [blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#phases-of-blue-green-upgrades) with settings, and [control the upgrade process with commands](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#control-in-progress-blue-green-upgrade).

However, if you want to use [surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#surge) instead, run the following command to switch back to surge upgrades:
    
    
    gcloud container node-pools update NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --enable-surge-upgrade
    

## Configure autoscaled blue-green upgrades

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To use autoscaled blue-green upgrades for a node pool, you don't need to configure any of the additional parameters for batch size or soaking. You can, however, configure the length of time between cordoning and draining the nodes. Before you enable this upgrade strategy, review the [best practices](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#best-practices-autoscaled-bg) and [limitations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#autoscaled-bg-limitations).

### Create a node pool that uses autoscaled blue-green upgrades

Create a node pool with autoscaled blue-green upgrades enabled:
    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster CLUSTER_NAME \
        --enable-autoscaling \
        --max-nodes=MAX_NODES \
        --enable-blue-green-upgrade \
        --autoscaled-rollout-policy=[wait-for-drain-duration=WAIT_FOR_DRAIN_DURATIONs]
    

To set the `MIN_NODE` and `MAX_NODE` parameters, see the recommendations for [how to configure your cluster and node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#autoscaled-bg-best-practices-cluster--node-pool-config).

Replace the optional `WAIT_FOR_DRAIN_DURATION` parameter with the time, in seconds, to wait after cordoning the blue pool and before draining the nodes. You can configure this time between zero and seven days, with the default being three days (`259200` seconds).

### Update a node pool to use autoscaled blue-green upgrades

Update an existing node pool to use autoscaled blue-green upgrades:
    
    
    gcloud container node-pools update NODE_POOL_NAME \
        --cluster CLUSTER_NAME \
        --enable-blue-green-upgrade \
        --autoscaled-rollout-policy=[wait-for-drain-duration=WAIT_FOR_DRAIN_DURATIONs]
    

Replace the optional `WAIT_FOR_DRAIN_DURATION` parameter with the time, in seconds, to wait after cordoning the blue pool and before draining the nodes. You can configure this time between zero and seven days, with the default being three days (`259200` seconds).

## Inspect the upgrade settings of a node pool

To inspect the current upgrade settings of a node pool, you can use the following command to describe the node pool:
    
    
    gcloud container node-pools describe NODE_POOL_NAME \
        --cluster=CLUSTER_NAME
    

The following snippet is an example output of the command. The `strategy` field indicates the upgrade strategy in use:

  * **SURGE** indicates that the surge upgrade strategy is enabled.
  * **BLUE_GREEN** indicates that the blue-green upgrade strategy is enabled:

    * Standard blue-green upgrades are enabled if the output includes values for `standardRolloutPolicy` under `blueGreenSettings`.
    * Autoscaled blue-green upgrades are enabled if `autoscaledRolloutPolicy` is mentioned.


    
    
    upgradeSettings:
      blueGreenSettings:
        nodePoolSoakDuration: 1800s
        standardRolloutPolicy:
          batchNodeCount: 1
          batchSoakDuration: 10s
      strategy: BLUE_GREEN
    

This command also shows you the current phase of an in-progress blue-green upgrade. Learn more about [checking the upgrade settings of a node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#check-settings).

## What's next

  * Learn more about [node upgrade strategies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies).
  * Learn how to [manually upgrade a cluster or node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster).
  * Learn more about [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions).
  * Learn more about [Standard cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades).
  * Learn how to [configure node auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
