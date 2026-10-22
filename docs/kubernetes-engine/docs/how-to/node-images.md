---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-images/
title: Specify a node image \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:44.667702+00:00
---

# Specify a node image  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Specify a node image Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to specify a node image for nodes in Google Kubernetes Engine (GKE) Standard mode clusters. To learn about how node images work, and the types of node images that are available, see [Node images](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images).

Nodes in GKE Autopilot clusters always use the [ Container-Optimized OS with containerd](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/using-containerd#about_containerd) (`cos_containerd`) node image. You can't specify a different node image in Autopilot mode.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Specifying a node image

You can select the node image you want to use when you create a new cluster, or you can change the node image for an existing cluster.

### Creating a new cluster

### gcloud

To create a new cluster with a specific node image, run the following command:
    
    
    gcloud container clusters create CLUSTER_NAME --image-type IMAGE_TYPE
    

Replace the following:

  * `CLUSTER_NAME`: the name you choose for the cluster.
  * `IMAGE_TYPE`: the name of your [node image type](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#available_node_images).



### Console

  1. In the Google Cloud console, go to the **Create a Kubernetes cluster** page. 

[Go to Create a Kubernetes cluster](https://console.cloud.google.com/kubernetes/add)

  2. Configure your cluster as desired.

  3. From the navigation pane, under **Node Pools** , click **Nodes**.

  4. In the **Image type** drop-down list, select the desired [node image](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images).

  5. Click **Create**.




###  Terraform 

To create a new cluster with a specific node image using Terraform, refer to the following example:
    
    
    resource "google_container_cluster" "default" {
      name               = "gke-standard-zonal-node-image"
      initial_node_count = 2
    
      node_config {
        image_type = "cos_containerd"
      }
    }

To learn more about using Terraform, see [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

### Upgrading an existing cluster

This change requires recreating the nodes, which can cause disruption to your running workloads. For details about this specific change, find the corresponding row in the [manual changes that recreate the nodes using a node upgrade strategy without respecting maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#manual-changes-strategy-but-no-respect-policies) table. To learn more about node updates, see [Planning for node update disruptions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#plan-node-disruption).

**Caution:** GKE immediately begins recreating the nodes for this change using the node upgrade strategy, regardless of active maintenance policies. GKE depends on [resource availability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota) for the change. Disabling node auto-upgrades [doesn't prevent this change](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable-only-versions). Ensure that your workloads running on the nodes are prepared for disruption before you initiate this change.

### gcloud

You can upgrade an existing cluster to use a specific node image by using the `gcloud container clusters upgrade` command. You can upgrade all node pools in the cluster, or you can specify specific a node pool using `--node-pool`.

To upgrade an existing cluster to use a specific node image, run the following command:
    
    
    gcloud container clusters upgrade CLUSTER_NAME --image-type IMAGE_TYPE \
        [--node-pool POOL_NAME]
    

Replace the following:

  * `CLUSTER_NAME`: the name of your existing cluster.
  * `POOL_NAME`: the name of the node pool you want to update.
  * `IMAGE_TYPE`: the name of your [node image type](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#available_node_images).



### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Click the **Nodes** tab.

  4. Under **Node Pools** , click the name of the node pool you want to upgrade.

  5. On the **Node pool details** page, click _edit_ **Edit**.

  6. Under **Node version** , click **Change**.

  7. Select the desired [node version](https://docs.cloud.google.com/kubernetes-engine/versioning#versioning) and click **Change** to start the upgrade.




## What's next

  * Learn more about [node images](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images).
  * Learn more about [containerd node images](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/using-containerd).
  * Learn more about [Arm workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke).
  * Learn more about [GKE node sizing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-node-sizes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
