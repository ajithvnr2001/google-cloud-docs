---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-tier-1/
title: Increase network bandwidth for clusters and nodes \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:41.021410+00:00
---

# Increase network bandwidth for clusters and nodes  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-tier-1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Increase network bandwidth for clusters and nodes Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to increase network bandwidth limit for Google Kubernetes Engine (GKE) clusters and cluster nodes by using [Tier 1 bandwidth](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#bandwidth-tiers).

## Pricing

[Higher bandwidth pricing](https://cloud.google.com/products/compute/pricing/general-purpose#tier-1-higher-bandwidth-network-pricing) applies when you enable Tier 1 bandwidth.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Limitations

  * [Compute Engine VM Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#limitations) limitations apply.
  * When you enable Tier 1 bandwidth, GKE enables [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/networking/using-gvnic), and GKE manages gVNIC as long as the node pool has Tier 1 bandwidth enabled.



### Requirements

  * GKE nodes must use a Container-Optimized OS [node image](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#cos).



## Enable Tier 1 bandwidth on a cluster

You can create a cluster that has Tier 1 bandwidth enabled, or you can update a cluster to use Tier 1 bandwidth.

A Tier 1 bandwidth enabled cluster has node pool Tier 1 bandwidth enabled by default. If you set the node pool bandwidth to `TIER_UNSPECIFIED`, the node pool settings override the cluster bandwidth settings.

### Create a cluster with Tier 1 bandwidth enabled

Create a cluster that uses Tier 1 bandwidth:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --network-performance-configs=total-egress-bandwidth-tier=TIER_1
    

Replace the `CLUSTER_NAME` with the name of the cluster.

### Update a cluster to enable Tier 1 bandwidth

Update a cluster to use Tier 1 bandwidth:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --network-performance-configs=total-egress-bandwidth-tier=TIER_1
    

Replace the `CLUSTER_NAME` with the name of the existing cluster.

**Note:** When you update a cluster to use Tier 1 bandwidth, only the default value of the new node pool changes. The default value of existing node pools remains unchanged.

## Enable Tier 1 bandwidth on a node pool

You can create a node pool that has Tier 1 bandwidth enabled, or you can update a node pool to use Tier 1 bandwidth.

A Tier 1 bandwidth enabled cluster has node pool Tier 1 bandwidth enabled by default. However, the node pool API overrides your cluster-level configuration for Tier 1.

### Create a node pool with Tier 1 bandwidth enabled

Create a node pool that uses Tier 1 bandwidth:
    
    
    gcloud container node-pools create NODEPOOL_NAME \
        --cluster=CLUSTER_NAME \
        --network-performance-configs=total-egress-bandwidth-tier=TIER_1
    

Replace the following:

  * `NODEPOOL_NAME`: the name of the new node pool.
  * `CLUSTER_NAME`: the name of the existing cluster.



### Update a node pool to enable Tier 1 bandwidth

Update a node pool to use Tier 1 bandwidth:
    
    
    gcloud container node-pools update NODEPOOL_NAME \
        --cluster=CLUSTER_NAME \
        --network-performance-configs=total-egress-bandwidth-tier=TIER_1
    

Replace the following:

  * `NODEPOOL_NAME`: the name of the node pool that you want to update.
  * `CLUSTER_NAME`: the name of the existing cluster.



## Disable Tier 1 bandwidth on a cluster or a node pool

You can disable Tier 1 bandwidth at the cluster level or node pool level. When you disable Tier 1 bandwidth at the cluster level, node pool Tier 1 bandwidth is set to `TIER_UNSPECIFIED`. Disabling Tier 1 bandwidth at cluster level does not disable existing node pool configuration.

Update the cluster to use default bandwidth:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --cluster=CLUSTER_NAME \
        --network-performance-configs=total-egress-bandwidth-tier=TIER_UNSPECIFIED
    

Update the node pool to use default bandwidth:
    
    
    gcloud container node-pools update NODEPOOL_NAME \
        --cluster=CLUSTER_NAME \
        --network-performance-configs=total-egress-bandwidth-tier=TIER_UNSPECIFIED
    

## What's next

  * Use [network policy logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging) to record when connections to Pods are allowed or denied by your cluster's [network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/).
  * Learn how to [set the network tier](https://docs.cloud.google.com/network-tiers/docs/set-network-tier).
  * Know more about the highest [maximum transmission unit (MTU)](https://docs.cloud.google.com/compute/docs/networking/benchmarking-higher-bandwidth-vms#setup-benchmark-vms) setting.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
