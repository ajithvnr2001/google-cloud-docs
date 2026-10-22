---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/update-node-pool/
title: Update a node pool \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:43.189350+00:00
---

# Update a node pool  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/update-node-pool/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Update a node pool

This topic explains how you can update your node pools. You can update your node pools for the following reasons:

  * To upgrade your node pool version
  * To change the number of nodes in your node pool
  * To change your node pool annotations (Only updatable through API) 



You can also change additional parameters on your node pools not listed above. For a complete list of parameters you can update, see the [`gcloud container azure node-pools update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/update) and the [`projects.locations.azureNodePools.patch`](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations.azureClusters.azureNodePools/patch) documentation.

## Update process

This section describes the processes GKE on Azure takes to update a node pool. The process is different depending on the extent of changes necessary to the node pool.

### Configuration-only update

If GKE on Azure can update a node pool without restarting or recreating any resources, it will make those changes. For example, updating your node pool's annotations will not restart any instances.

### Rolling update

When a change to a node pool requires restarting existing virtual machines— for example, when updating the Kubernetes version— GKE on Azure performs the following steps:

  1. Modify the node pool's virtual machine scale set with new configuration.
  2. Choose one node's underlying instance to update.
  3. GKE on Azure cordons and [drains](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/) the node. At this point, new Pods can not be scheduled on the target node. Existing Pod objects on the target node are rescheduled onto other nodes. Pods that can't be rescheduled onto any other existing node stay in the [**Pending** phase](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/pod#pod_lifecycle) until they can be scheduled.
  4. Update the instance to take the latest configuration from its virtual machine scale set.
  5. Reimage and reboot the instance.
  6. Wait until all the nodes in this node pool become healthy.
  7. If all nodes in this node pool are healthy, select another node until all nodes are updated. If any node is unhealthy, GKE on Azure places the node pool into a `DEGRADED` state. For more information, see Failed updates.



#### Protect workloads during a node pool rolling update

During node pool rolling update, GKE on Azure honors PodDisruptionBudget   
configuration for up to one hour after a node starts to drain. After one hour, GKE on Azure deletes any remaining Pods on the node.

During rolling update, GKE on Azure performs a graceful shutdown of any nodes to be restarted or removed with the best effort for up to two hours. After two hours, if there are any remaining Pod objects on the node, GKE on Azure deletes the node and reimages the underlying virtual machine instance. 

### Resizing node pools

GKE on Azure node pools have cluster autoscaler enabled by default. The cluster autoscaler automatically resizes the node pool based on the demands of your workloads. For more information on the cluster autoscaler, see [Cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/cluster-autoscaler).

When you change the maximum and minimum number of nodes in the node pool, GKE on Azure takes different actions depending on the new configuration and node pool's current number of nodes. These actions include the following:

  * If the node pool's current node count is already within the new range, GKE on Azure doesn't change the number of nodes in the pool.

  * If the new minimum number of nodes is higher than the node pool's current node count, GKE on Azure adds more nodes until the node pool reaches the new minimum size.



  * If the new maximum number of nodes is less than the node pool's current node count, GKE on Azure reduces the size of the node pool by performing the following actions:

    1. Update the autoscaling configuration onto the virtual machine scale set in the node pool
    2. Select a node to remove
    3. Cordon and drain the node
    4. Delete the underlying virtual machine instance
    5. Wait until the deleted virtual machine is fully gone
    6. Perform health check on the whole node pool
    7. Repeat until the number of nodes reaches the desired number



#### How GKE on Azure protects workloads during node pool resizing

During node pool resizing, GKE on Azure honors PodDisruptionBudget configuration for up to one hour after a node starts to drain. After one hour, GKE on Azure deletes any remaining Pod objects on the node.

During node pool resizing, GKE on Azure performs a graceful shutdown of any nodes to be restarted or removed and waits for up to two hours. After two hours, if there are any remaining Pod objects on the node, GKE on Azure deletes the underlying virtual machine instance.

### Check for a failed update status

If GKE on Azure performs a health check after an update and the health check fails, the node pool is marked as `DEGRADED`. You can find status information on your cluster with the following Google Cloud CLI command:
    
    
    gcloud container azure node-pools describe NODE_POOL_NAME \
        --cluster CLUSTER_NAME \
        --location GOOGLE_CLOUD_LOCATION
    

Replace the following:

  * `NODE_POOL_NAME`: the name of your node pool
  * `CLUSTER_NAME`: the name of your cluster
  * `GOOGLE_CLOUD_LOCATION`: the Google Cloud region that manages your cluster



The output includes information about the status and configuration of your node pool.

## Prerequisites

To update a node pool, you must have the `gkemulticloud.googleapis.com/azureNodePools.update` Identity and Access Management permission. 

## Update a node pool

You can update a node pool with the Google Cloud CLI. To update a node pool, run:
    
    
    gcloud container azure node-pools update NODE_POOL_NAME \
        --cluster CLUSTER_NAME \
        --location GOOGLE_CLOUD_LOCATION \
        --node-version NODE_POOL_VERSION \
        --min-nodes MIN_NODES \
        --max-nodes MAX_NODES     
    

Replace the following:

  * `NODE_POOL_NAME`: the name of the node pool to update
  * `CLUSTER_NAME`: the name of the cluster to attach the node pool to
  * `GOOGLE_CLOUD_LOCATION`: the [supported Google Cloud region](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-regions) that manages your cluster—for example, `us-west1`
  * `NODE_POOL_VERSION`: the new [supported node pool version](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-versions)
  * `MIN_NODES`: the new minimum number of nodes the node pool can contain. Must be `0` or greater.
  * `MAX_NODES`: the new maximum number of nodes the node pool can contain. Must at least `1` and the value of `MIN_NODES`.



## Cancelling an update operation

To cancel an ongoing node pool update operation, run the following command:
    
    
    gcloud container azure operations cancel OPERATION_NAME
    

Replace `OPERATION_NAME` with the name of the update operation.

Note that cancelling an update node pool operation which is in progress won't revert node updates that have already completed. This can result in a partially updated node pool.

## What's next

  * Read the [gcloud container azure node-pools create](https://docs.cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create) reference documentation.
  * [Delete a node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/delete-node-pool).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
