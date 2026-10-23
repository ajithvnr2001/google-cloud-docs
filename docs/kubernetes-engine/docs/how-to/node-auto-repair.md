---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair/
title: Auto-repair nodes \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:28.233043+00:00
---

# Auto-repair nodes  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Auto-repair nodes Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how node auto-repair works and how to use the feature for Standard Google Kubernetes Engine (GKE) clusters.

_Node auto-repair_ helps keep the nodes in your GKE cluster in a healthy, running state. When enabled, GKE makes periodic checks on the health state of each node in your cluster. If a node fails consecutive health checks over an extended time period, GKE initiates a repair process for that node.

## Settings for Autopilot and Standard

Autopilot clusters always automatically repair nodes. You can't disable this setting.

In Standard clusters, node auto-repair is enabled by default for new node pools. Although you can disable auto repair for an existing node pool, we recommend keeping the default configuration. Disabling auto-repair can have unintended consequences. For example, if you use `kubectl` to delete an unhealthy node when auto-repair is disabled, the underlying VM instance might become orphaned from the cluster, and you would continue to be billed for it. If you need to remove nodes, you can instead [resize the node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#scale-node-pool).

## Repair criteria

GKE uses the node's health status to determine if a node needs to be repaired. A node reporting a `Ready` status is considered healthy. GKE triggers a repair action if a node reports consecutive unhealthy status reports for a given time threshold. An unhealthy status can mean:

  * A node reports a `NotReady` status on consecutive checks over the given time threshold (approximately 10 minutes).
  * A node does not report any status at all over the given time threshold (approximately 10 minutes).
  * A node's boot disk is out of disk space for an extended time period (approximately 30 minutes).
  * A node in an Autopilot cluster is cordoned for longer than the given time threshold (approximately 10 minutes).



You can manually check your node's health signals at any time by using the `kubectl get nodes` command.

## Node repair process

If GKE detects that a node requires repair, the node is drained and re-created. This process preserves the original name of the node. GKE waits one hour for the drain to complete. If the drain doesn't complete, the node is shut down and a new node is created.

If multiple nodes require repair, GKE might repair nodes in parallel. GKE balances the number of repairs depending on the size of the cluster and the number of broken nodes. GKE will repair more nodes in parallel on a larger cluster, but fewer nodes as the number of unhealthy nodes grows.

If you disable node auto-repair at any time during the repair process, in- progress repairs are _not_ canceled and continue for any node under repair.

**Note:** Modifications on the boot disk of a node VM don't persist across node re-creations. To preserve modifications across node re-creation, use a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/).**Note:** Node auto-repair uses a set of signals, including signals from the [Node Problem Detector](https://github.com/kubernetes/node-problem-detector). The Node Problem Detector is enabled by default on nodes that use [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs/how-to/monitoring) and Ubuntu images.

### Node auto repair in TPU slice nodes

If a TPU slice node in a [multi-host TPU slice node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#node_pool) is unhealthy and requires auto repair, the _entire_ node pool is recreated. To learn more about the TPU slice node conditions, see [TPU slice node auto repair](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#node-auto-repair).

## Enable auto-repair for an existing Standard node pool

You enable node auto-repair on a _per-node pool_ basis.

If auto-repair is disabled on an existing node pool in a Standard cluster, use the following instructions to enable it:

### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Click the **Nodes** tab.

  4. Under **Node Pools** , click the name of the node pool you want to modify.

  5. On the **Node pool details** page, click _edit_ **Edit**.

  6. Under **Management** , select the **Enable auto-repair** checkbox.

  7. Click **Save**.




### gcloud
    
    
    gcloud container node-pools update POOL_NAME \
        --cluster CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --enable-autorepair
    

Replace the following:

  * `POOL_NAME`: the name of your node pool.
  * `CLUSTER_NAME`: the name of your Standard cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.



## Verify node auto-repair is enabled for a Standard node pool

Node auto-repair is enabled on a _per-node pool_ basis. You can verify that a node pool in your cluster has node auto-repair enabled with the Google Cloud CLI or the Google Cloud console.

### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. On the **Google Kubernetes Engine** page, click the name of the cluster of the node pool you want to inspect.

  3. Click the **Nodes** tab.

  4. Under **Node Pools** , click the name of the node pool you want to inspect.

  5. Under **Management** , in the **Auto-repair** field, verify that auto-repair is enabled.




### gcloud

Describe the node pool:
    
    
    gcloud container node-pools describe NODE_POOL_NAME \
    --cluster=CLUSTER_NAME
    

If node auto-repair is enabled, the output of the command includes these lines:
    
    
    management:
      ...
      autoRepair: true
    

## Disable node auto-repair

You can disable node auto-repair for an existing node pool in a Standard cluster by using the gcloud CLI or the Google Cloud console.

### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Click the **Nodes** tab.

  4. Under **Node Pools** , click the name of the node pool you want to modify.

  5. On the **Node pool details** page, click _edit_ **Edit**.

  6. Under **Management** , clear the **Enable auto-repair** checkbox.

  7. Click **Save**.




### gcloud
    
    
    gcloud container node-pools update POOL_NAME \
        --cluster CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --no-enable-autorepair
    

Replace the following:

  * `POOL_NAME`: the name of your node pool.
  * `CLUSTER_NAME`: the name of your Standard cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.



## Get information about recent automated repair events

GKE generates a log entry for automated repair events. You can check the logs by running the following commands:

  1. List the operations:
         
         gcloud container operations list --location=CONTROL_PLANE_LOCATION
         

Replace `CONTROL_PLANE_LOCATION` with the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.

  2. Find the reason why the node auto-repair operation was triggered by running the following command:
         
         gcloud container operations describe OPERATION_NAME --location=CONTROL_PLANE_LOCATION
         

Replace `OPERATION_NAME` with the name of an operation listed in the output from the previous command.




In the output from the command, check the `operationReason` for the reason why the repair operation was triggered. For example, `AUTO_REPAIR_LONG_UNHEALTHY` means that the node auto-repair was triggered because the node was unhealthy for 10 minutes.

## What's next

  * [Learn more about node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
