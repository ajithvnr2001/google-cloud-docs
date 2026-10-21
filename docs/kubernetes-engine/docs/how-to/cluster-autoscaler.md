---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler/
title: Autoscaling a cluster \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:58.105806+00:00
---

# Autoscaling a cluster  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Autoscaling a cluster Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to autoscale your Standard Google Kubernetes Engine (GKE) clusters. To learn about how the cluster autoscaler works, refer to [Cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).

With Autopilot clusters, you don't need to worry about provisioning nodes or managing node pools because node pools are _automatically_ provisioned through [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning), and are [automatically scaled](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) to meet the requirements of your workloads.

## Using the cluster autoscaler

**Note:** Enabling or disabling cluster autoscaling might cause the control plane to restart, which takes several minutes to complete. Once autoscaling is enabled for at least one node pool, further changes to the cluster autoscaler configuration does not cause the control plane to restart until autoscaling is disabled for the last node pool. However, autoscaling might still take up to one minute for changes to propagate after the operation completes.

The following sections explain how to use cluster autoscaler.

### Creating a cluster with autoscaling

You can create a cluster with autoscaling enabled using the Google Cloud CLI or the Google Cloud console.

### gcloud

To create a cluster with autoscaling enabled, use the `--enable-autoscaling` flag and specify `--min-nodes` and `--max-nodes`:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --enable-autoscaling \
        --num-nodes NUM_NODES \
        --min-nodes MIN_NODES \
        --max-nodes MAX_NODES \
        --location=CONTROL_PLANE_LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster to create.
  * `NUM_NODES`: the number of nodes to create in each location.
  * `MIN_NODES`: the minimum number of nodes to automatically scale for the specified node pool per zone. To specify the minimum number of nodes for the entire node pool in GKE versions 1.24 and later, use `--total-min-nodes`. The flags `--total-min-nodes` and `--total-max-nodes` are mutually exclusive with the flags `--min-nodes` and `--max-nodes`.
  * `MAX_NODES`: the maximum number of nodes to automatically scale for the specified node pool per zone. To specify the maximum number of nodes for the entire node pool in GKE versions 1.24 and later, use `--total-max-nodes`. The flags `--total-min-nodes` and `--total-max-nodes` are mutually exclusive with the flags `--min-nodes` and `--max-nodes`.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.



**Example: Creating a cluster with node autoscaling enabled and min and max nodes**

The following command creates a cluster with 90 nodes, or 30 nodes in each of the 3 zones present in the region. Node autoscaling is enabled and resizes the number of nodes based on [cluster load](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#operating_criteria). The cluster autoscaler can reduce the size of the default node pool to 15 nodes or increase the node pool to a maximum of 50 nodes per zone.
    
    
    gcloud container clusters create my-cluster --enable-autoscaling \
        --num-nodes=30 \
        --min-nodes=15 --max-nodes=50 \
        --location=us-central1
    

**Example: Creating a cluster with node autoscaling enabled and total nodes**

The following command creates a cluster with 30 nodes, or 10 nodes in each of the 3 zones present in the region. Node autoscaling is enabled and resizes the number of nodes based on [cluster load](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#operating_criteria). In this example, the total size of the cluster can be between 10 and 60 nodes, regardless of spreading between zones.
    
    
    gcloud container clusters create my-cluster --enable-autoscaling \
        --num-nodes 10 \
        --location us-central1 \
        --total-min-nodes 10  --total-max-nodes 60
    

### Console

To create a new cluster in which the default node pool has autoscaling enabled:

  1. In the Google Cloud console, go to the **Create a Kubernetes cluster** page. 

[Go to Create a Kubernetes cluster](https://console.cloud.google.com/kubernetes/add)

  2. Configure your cluster as desired.

  3. From the navigation pane, under **Node Pools** , click **default-pool**.

  4. Select the **Enable autoscaling** checkbox.

  5. Change the values of the **Minimum number of nodes** and **Maximum number of nodes** fields as desired.

  6. Click **Create**.




### Adding a node pool with autoscaling

You can create a node pool with autoscaling enabled using the gcloud CLI or the Google Cloud console.

### gcloud

To add a node pool with autoscaling to an existing cluster, use the following command:
    
    
    gcloud container node-pools create POOL_NAME \
        --cluster=CLUSTER_NAME \
        --enable-autoscaling \
        --min-nodes=MIN_NODES \
        --max-nodes=MAX_NODES \
        --location=CONTROL_PLANE_LOCATION
    

Replace the following:

  * `POOL_NAME`: the name of the desired node pool.
  * `CLUSTER_NAME`: the name of the cluster in which the node pool is created.
  * `MIN_NODES`: the minimum number of nodes to automatically scale for the specified node pool per zone. To specify the minimum number of nodes for the entire node pool in GKE versions 1.24 and later, use `--total-min-nodes`. The flags `--total-min-nodes` and `--total-max-nodes` are mutually exclusive with the flags `--min-nodes` and `--max-nodes`.
  * `MAX_NODES`: the maximum number of nodes to automatically scale for the specified node pool per zone. To specify the maximum number of nodes for the entire node pool in GKE versions 1.24 and later, use `--total-max-nodes`. The flags `--total-min-nodes` and `--total-max-nodes` are mutually exclusive with the flags `--min-nodes` and `--max-nodes`.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.



**Example: Adding a node pool with node autoscaling enabled**

The following command creates a node pool with node autoscaling that scales the node pool to a maximum of 5 nodes and a minimum of 1 node:
    
    
    gcloud container node-pools create my-node-pool \
        --cluster my-cluster \
        --enable-autoscaling \
        --min-nodes 1 --max-nodes 5 \
        --location us-central1-c
    

### Console

To add a node pool with autoscaling to an existing cluster:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Click the **Nodes** tab.

  4. Click _add_box_ **Create user-managed node pool**.

  5. Configure the node pool as desired.

  6. Under **Size** , select the **Enable autoscaling** checkbox.

  7. Change the values of the **Minimum number of nodes** and **Maximum number of nodes** fields as desired.

  8. Click **Create**.




### Enabling autoscaling for an existing node pool

You can enable autoscaling for an existing node pool using the gcloud CLI or the Google Cloud console.

### gcloud

To enable autoscaling for an existing node pool, use the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --enable-autoscaling \
        --node-pool=POOL_NAME \
        --min-nodes=MIN_NODES \
        --max-nodes=MAX_NODES \
        --location=CONTROL_PLANE_LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster to update.
  * `POOL_NAME`: the name of the desired node pool. If you have only one node pool, supply `default-pool` as the value.
  * `MIN_NODES`: the minimum number of nodes to automatically scale for the specified node pool per zone. To specify the minimum number of nodes for the entire node pool in GKE versions 1.24 and later, use `--total-min-nodes`. The flags `--total-min-nodes` and `--total-max-nodes` are mutually exclusive with the flags `--min-nodes` and `--max-nodes`.
  * `MAX_NODES`: the maximum number of nodes to automatically scale for the specified node pool per zone. To specify the maximum number of nodes for the entire node pool in GKE versions 1.24 and later, use `--total-max-nodes`. The flags `--total-min-nodes` and `--total-max-nodes` are mutually exclusive with the flags `--min-nodes` and `--max-nodes`.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.



### Console

To enable autoscaling for an existing node pool:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Click the **Nodes** tab.

  4. Under **Node Pools** , click the name of the node pool you want to modify, then click _edit_ **Edit**.

  5. Under **Size** , select the **Enable autoscaling** checkbox.

  6. Change the values of the **Minimum number of nodes** and **Maximum number of nodes** fields as desired.

  7. Click **Save**.




#### Verifying that autoscaling for the existing node pool is enabled

You verify that your cluster is using autoscaling with the Google Cloud CLI or the Google Cloud console.

### gcloud

Describe the node pools in the cluster:
    
    
    gcloud container node-pools describe NODE_POOL_NAME --cluster=CLUSTER_NAME |grep autoscaling -A 1
    

Replace the following:

  * `NODE_POOL_NAME`: the name of the new node pool that you choose.
  * `CLUSTER_NAME`: the name of the cluster.



If autoscaling is enabled, the output is similar to the following:
    
    
    autoscaling:
      enabled: true
    

### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to verify.

  3. Click the **Nodes** tab.

  4. Under **Node Pools** , verify that node pool `Autoscalling` state.




### Creating a node pool that prioritizes optimization of unused reservations

**Note:** Starting in GKE version 1.27, cluster autoscaler always considers [reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview) when making the scale-up decisions, regardless of the used location policy.

You can use the `--location-policy=ANY` flag when you create a node pool to instruct the cluster autoscaler to [prioritize utilization of unused reservations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#balancing_across_zones):
    
    
    gcloud container node-pools create POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location-policy=ANY
    

Replace the following:

  * `POOL_NAME`: the name of the new node pool that you choose.
  * `CLUSTER_NAME`: the name of the cluster.



### Disabling autoscaling for an existing node pool

You can disable autoscaling for an existing node pool using the gcloud CLI or the Google Cloud console.

### gcloud

To disable autoscaling for a specific node pool, use the `--no-enable-autoscaling` flag:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --no-enable-autoscaling \
        --node-pool=POOL_NAME \
        --location=CONTROL_PLANE_LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster to update.
  * `POOL_NAME`: the name of the desired node pool.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.



The cluster size is fixed at the cluster's current default node pool size, which can be [manually updated](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/update).

### Console

To disable autoscaling for a specific node pool:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Click the **Nodes** tab.

  4. Under **Node Pools** , click the name of the node pool you want to modify, then click _edit_ **Edit**.

  5. Under **Size** , clear the **Enable autoscaling** checkbox.

  6. Click **Save**.




### Resizing a node pool

For clusters with autoscaling enabled, the cluster autoscaler automatically resizes node pools within the boundaries specified by either the minimum size (`--min-nodes`) and maximum size (`--max-nodes`) values or the minimum total size (`--total-min-nodes`) and maximum total size (`--total-max-nodes`). These flags are mutually exclusive. You can't manually resize a node pool by changing these values.

If you want to manually resize a node pool in your cluster that has autoscaling enabled, perform the following:

  1. Disable autoscaling on the node pool.
  2. [Manually resize the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/resizing-a-cluster).
  3. Re-enable autoscaling and specify the minimum and maximum node pool size.



### Preventing Pods scheduling on selected nodes

You can use `startup` or `status` taints to prevent Pods scheduling on selected nodes, depending on the use case.

This feature is available in GKE in version 1.28 and later.

#### Startup taints

Use `startup` taints when there is an operation that has to complete before any Pods can run on the node. For example, Pods shouldn't run until the drivers installation on node finishes.

Cluster autoscaler treats nodes tainted with `startup` taints as unready, but taken into account during scale up logic, assuming they will become ready shortly.  We recommend that you don't apply the `startup` taints to the nodes for an extended period of time. The cluster autoscaler _might stop working_ if a substantial number of nodes are tainted with startup taints, which means that they are unready. In this case, GKE doesn't scale up the cluster because even new nodes don't become ready. Therefore, GKE treats this cluster as broken. 

Startup taints are defined as all taints with the prefix `startup-taint.cluster-autoscaler.kubernetes.io/`

#### Status taints

Use `status` taints when GKE shouldn't use a given node to run Pods.

Cluster autoscaler treats nodes tainted with `status` taints as ready, but ignores them during scale up logic. Even though the tainted node is ready, no Pods should run. If more resources are needed by the Pods, GKE scales up the cluster and ignores the tainted nodes.

Status taints are defined as all taints with the prefix `status-taint.cluster-autoscaler.kubernetes.io/`

#### Ignore taints

**Deprecated:** Ignore taints are now deprecated and treated as startup taints. 

Ignore taints are defined as all taints with the prefix `ignore-taint.cluster-autoscaler.kubernetes.io/`

## Troubleshooting

For troubleshooting advice, see the following pages:

  * [Troubleshoot cluster autoscaler not scaling down](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cluster-autoscaler-scale-down).
  * [Troubleshoot cluster autoscaler not scaling up](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cluster-autoscaler-scale-up).



## What's next

  * Learn more about the [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).
  * Read an overview of [node pool auto-creation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning).
  * Learn how to [configure node pool auto-creation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning).
  * Learn about [cluster autoscaler visibility](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler-visibility).
  * Learn how to [resize a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/resizing-a-cluster).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
