---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-gvnic/
title: Increase network traffic speed for GPU nodes \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:03.342104+00:00
---

# Increase network traffic speed for GPU nodes  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-gvnic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Increase network traffic speed for GPU nodes Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to increase network bandwidth for GPU nodes on Google Kubernetes Engine (GKE) clusters by using [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/networking/using-gvnic).

In Autopilot clusters, nodes that run GKE version 1.30.2-gke.1023000 and later have Google Virtual NIC (gVNIC) installed automatically. The instructions on this page only apply to Standard clusters.

To increase bandwidth on CPU nodes, consider enabling [Tier-1 bandwidth](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-tier-1#enable_tier_1_bandwidth).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Limitations

  * [Compute Engine](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#limitations) limitations apply.



### Requirements

  * GKE nodes must use a Container-Optimized OS [node image](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#cos).



## Enable gVNIC

You can create a cluster that has node pools that use gVNIC, create a node pool with gVNIC enabled, or update a node pool to use gVNIC.

### Create a cluster

Create a cluster with node pools that use gVNIC:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --accelerator type=GPU_TYPE,count=AMOUNT \
        --machine-type=MACHINE_TYPE \
        --enable-gvnic
    

Replace the following:

  * `CLUSTER_NAME`: the name of the new cluster.
  * `GPU_TYPE`: the type of [GPU accelerator](https://docs.cloud.google.com/compute/docs/gpus) that you use. For example, `nvidia-tesla-t4`.
  * `AMOUNT`: the number of GPUs to attach to nodes in the node pool.
  * `MACHINE_TYPE`: the type of machine you want to use. gVNIC is not supported on [memory-optimized machine types](https://docs.cloud.google.com/compute/docs/machine-types#memory-optimized_machine_type_family).



### Create a node pool

Create a node pool that uses gVNIC:
    
    
    gcloud container node-pools create NODEPOOL_NAME \
        --cluster=CLUSTER_NAME \
        --enable-gvnic
    

Replace the following:

  * `NODEPOOL_NAME`: the name of a new node pool.
  * `CLUSTER_NAME`: the name of the existing cluster.



### Update a node pool

Update a node pool to use gVNIC:
    
    
    gcloud container node-pools update NODEPOOL_NAME \
        --cluster=CLUSTER_NAME \
        --enable-gvnic
    

Replace the following:

  * `NODEPOOL_NAME`: the name of the node pool that you want to update.
  * `CLUSTER_NAME`: the name of the existing cluster.



This change requires recreating the nodes, which can cause disruption to your running workloads. For details about this specific change, find the corresponding row in the [manual changes that recreate the nodes using a node upgrade strategy without respecting maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#manual-changes-strategy-but-no-respect-policies) table. To learn more about node updates, see [Planning for node update disruptions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#plan-node-disruption).

**Caution:** GKE immediately begins recreating the nodes for this change using the node upgrade strategy, regardless of active maintenance policies. GKE depends on [resource availability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota) for the change. Disabling node auto-upgrades [doesn't prevent this change](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable-only-versions). Ensure that your workloads running on the nodes are prepared for disruption before you initiate this change.

## Disable gVNIC

Update the node pool using the `--no-enable-gvnic` flag:
    
    
    gcloud container node-pools update NODEPOOL_NAME \
        --cluster=CLUSTER_NAME \
        --no-enable-gvnic
    

This change requires recreating the nodes, which can cause disruption to your running workloads. For details about this specific change, find the corresponding row in the [manual changes that recreate the nodes using a node upgrade strategy without respecting maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#manual-changes-strategy-but-no-respect-policies) table. To learn more about node updates, see [Planning for node update disruptions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#plan-node-disruption).

**Caution:** GKE immediately begins recreating the nodes for this change using the node upgrade strategy, regardless of active maintenance policies. GKE depends on [resource availability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota) for the change. Disabling node auto-upgrades [doesn't prevent this change](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable-only-versions). Ensure that your workloads running on the nodes are prepared for disruption before you initiate this change.

## Troubleshooting

To troubleshoot gVNIC, see [Troubleshooting Google Virtual NIC](https://docs.cloud.google.com/compute/docs/troubleshooting/gvnic).

## What's next

  * Use [network policy logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging) to record when connections to Pods are allowed or denied by your cluster's [network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
