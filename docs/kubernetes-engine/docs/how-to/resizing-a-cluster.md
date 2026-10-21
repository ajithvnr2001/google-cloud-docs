---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/resizing-a-cluster/
title: Resize a Standard cluster by adding or removing nodes \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:56:10.653504+00:00
---

# Resize a Standard cluster by adding or removing nodes  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/resizing-a-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Resize a Standard cluster by adding or removing nodes Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to manually resize Google Kubernetes Engine (GKE) Standard clusters. You can resize a cluster to increase or decrease the number of nodes in that cluster. Alternatively, you can autoscale your cluster, where GKE automatically resizes your node pools in response to changing conditions, such as changes in your workloads and resource usage.

These instructions don't apply to GKE [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) clusters, which automatically resize based on the number of Pods in the cluster.

When you add or remove nodes in your cluster, GKE adds or removes the associated virtual machine (VM) instances from the underlying Compute Engine [Managed Instance Groups (MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) provisioned for your node pools. For removing nodes, do not use `kubectl delete node` as this does not delete the Compute Engine VM instance in the node pool's underlying MIG. Use cluster autoscaler or manually decrease the size of your cluster.

**Note:** When you increase or decrease the size of a node pool that spans multiple zones, the new size represents the number of nodes in the node pool per zone. For example, if you have a node pool size of two that spans two zones, the total node count is four. If you resize the node pool to a size of four nodes, the total node count becomes eight.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Increase the size of your cluster

When you increase the size of a cluster, the following changes occur:

  * New node instances are created using the same configuration as the existing instances.
  * New Pods may be scheduled on the new instances.
  * Existing Pods are **not** moved to the new instances.




### gcloud

To increase the size of a cluster's node pools, run the [`gcloud container clusters resize`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/resize) command:
    
    
    gcloud container clusters resize CLUSTER_NAME --node-pool POOL_NAME \
        --num-nodes NUM_NODES

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster to resize.
  * `POOL_NAME`: the name of the node pool to resize.
  * `NUM_NODES`: the number of nodes in the pool in a zonal cluster. If you use multi-zonal or regional clusters, `NUM_NODES` is the number of nodes for each zone the node pools is in.



Repeat this command for each node pool. If your cluster has only one node pool, omit the `--node-pool` flag.

### Console

To increase the size of a cluster's node pools, perform the following steps:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Beside the cluster you want to edit, click _more_vert_ **Actions** , then click **Edit**.

  3. Click the **Nodes** tab next to the **Details** tab.

  4. In the **Node Pools** section, click the name of the node pool that you want to increase in size.

  5. Click _edit_ **Resize**.

  6. In the **Number of nodes** field, enter how many nodes that you want in the node pool, and then click **Resize**.

  7. Repeat for each node pool as needed.




## Decrease the size of your cluster

**Warning:** Do not use both cluster autoscaler and manual resize commands simultaneously on a node pool, as this can cause interactions that result in unstable or incorrect node pool size.

When you decrease the size of a cluster, the following changes occur:

  * GKE gracefully terminates nodes that are being deleted, using the [drain](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/) process to remove the Pods from the instance. [`PodDisruptionBudget`](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) and [`terminationGracePeriodSeconds`](https://kubernetes.io/docs/concepts/workloads/pods/pod/#termination-of-pods) are both respected for up to one hour.
  * Pods managed by a replication controller are rescheduled by the controller to run on the remaining instances.
  * Pods not managed by a replication controller are not restarted.



The MIG does not differentiate between instances running Pods and instances without Pods. Resizing down removes instances at random.

**Note:** Although the selection of nodes for removal during a resize operation isn't guaranteed, the MIG prioritizes the removal of nodes that have been cordoned and drained. If you need to selectively remove a node, you can first drain the node, and then resize the node pool.

To learn how to add node pools and to manage existing ones, refer to [Adding and managing node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools).

### gcloud

To decrease the size of a cluster's node pools, run the [`gcloud container clusters resize`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/resize) command:
    
    
    gcloud container clusters resize CLUSTER_NAME --node-pool POOL_NAME \
        --num-nodes NUM_NODES

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster to resize.
  * `POOL_NAME`: the name of the node pool to resize.
  * `NUM_NODES`: the number of nodes in the pool in a zonal cluster. If you use multi-zonal or regional clusters, `NUM_NODES` is the number of nodes for each zone the node pools is in.



Repeat this command for each node pool. If your cluster has only one node pool, omit the `--node-pool` flag.

### Console

To decrease the size of a cluster's node pools, perform the following steps:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Beside the cluster you want to edit, click _more_vert_ **Actions** , then click **Edit**.

  3. Click the **Nodes** tab next to the **Details** tab.

  4. In the **Node Pools** section, click the name of the node pool that you want to decrease in size.

  5. Click _edit_ **Resize**.

  6. In the **Number of nodes** field, enter how many nodes that you want in the node pool, and then click **Resize**.

  7. Repeat for each node pool as needed.




## Autoscaling a cluster

GKE's [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) feature automatically resizes your node pools in response to changing conditions, such as changes in your workloads and resource usage.

To learn more about how autoscaling works, refer to the [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) documentation. To set up autoscaling for your cluster, see [Autoscaling a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler).

## What's next

  * [Learn more about clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
