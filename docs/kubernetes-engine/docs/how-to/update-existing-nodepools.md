---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/update-existing-nodepools/
title: Update Kubernetes node labels and taints for node pools \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:46.045289+00:00
---

# Update Kubernetes node labels and taints for node pools  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/update-existing-nodepools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Update Kubernetes node labels and taints for node pools Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document provides instructions on how to update the Kubernetes node labels and node taints of an existing node pool in a Google Kubernetes Engine (GKE) Standard cluster by using the GKE API. Kubernetes node labels are distinct from [GKE cluster and node labels](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-managing-labels).

Node [taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) and [labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) are in the object metadata of Kubernetes nodes. Kubernetes labels are used to schedule Pods on particular nodes. In contrast, taints can be used to steer Pods away from particular nodes. For more information, see [Configure workload separation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-taints).

Using the GKE API, you can apply updates to the Kubernetes node labels and node taints of an existing GKE node pool without re-creating the node pool and disrupting running workloads. The updated node pool configuration is preserved in GKE, so that future node pool upgrades and new nodes provisioned in the node pool will use the new configuration.

For more information about how changes affect the operation of a GKE cluster, see [Manage cluster lifecycle changes to minimize disruption](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters). For details about specific changes, see the **Types of changes to a GKE cluster** section.

## Label syntax

Kubernetes labels must meet all of the following requirements:

  * Label keys and values must meet the requirements for [syntax and character set](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set).
  * The length of the value that you specify in the `--node-labels` gcloud CLI flag must be less than or equal to 1,024 characters.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * [Connect to an existing GKE Standard cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl).



## Updating node labels

To update node labels for a node pool, use the following command:
    
    
    gcloud container node-pools update NODEPOOL_NAME \
        --node-labels=[NODE_LABEL,...] \
        --cluster=CLUSTER_NAME
        --location=CONTROL_PLANE_LOCATION
        [GCLOUD_WIDE_FLAG …]
    

**Warning:** This update overwrites any previous user-specified values.

Replace the following:

  * `NODEPOOL_NAME`: the name of the node pool to update.
  * `[NODE_LABEL,...]`: the new node labels (for example, `label1=value1,label2=value2`).
  * `CLUSTER_NAME`: the name of the cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.



## Updating node taints

To update node taints for a node pool, use the following command:
    
    
    gcloud container node-pools update NODEPOOL_NAME \
        --node-taints=[NODE_TAINT,...] \
        --cluster=CLUSTER_NAME
        --location=CONTROL_PLANE_LOCATION
        [GCLOUD_WIDE_FLAG …]
    

**Warning:** This update overwrites any previous user-specified values.

Replace the following:

  * `NODEPOOL_NAME`: the name of the node pool to update.
  * `[NODE_TAINT,...]`: the new node taints (for example, `key1=val1:NoSchedule,key2=val2:PreferNoSchedule`).
  * `CLUSTER_NAME`: the name of the cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.



### Updating architecture taints

Similarly to other GKE-managed system taints, architecture taints like `kubernetes.io/arch=arm64:NoSchedule` on Arm nodes are managed differently than custom node taints and can't be removed using the previously described instructions. However, you can modify the architecture taints. For more information, see [Configure the default Arm architecture taint](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-arm-workloads-for-deployment#configure-default-taint).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
