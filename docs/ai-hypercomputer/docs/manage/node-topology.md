---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/manage/node-topology/
title: View GKE node topology \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:28:40.136834+00:00
---

# View GKE node topology  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/manage/node-topology/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  View GKE node topology Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to view the physical topology of your Google Kubernetes Engine (GKE) nodes on A4X Max, A4X, A4, A3 Ultra, A3 Mega, and A3 High Compute Engine instances. Understanding the physical location of your nodes helps you optimize Pod placement for your AI workloads.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Connect to your cluster

  * Run the following command to connect to your cluster:
        
        gcloud container clusters get-credentials CLUSTER_NAME
        

Replace `CLUSTER_NAME` with the name of your cluster.




## Understand GKE node topology

You can understand the physical topology of GKE nodes on A4X Max, A4X, A4, and A3 Ultra Compute Engine instances by referring to the following node labels:

  * `cloud.google.com/gce-topology-block`: the organization-specific ID of the reserved block where the VM is located. A [block](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#block) is a collection of sub-blocks connected by a layer of distributed network fabric.
  * `cloud.google.com/gce-topology-subblock`: the organization-specific ID of the sub-block where the VM is located. A [sub-block](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#sub-block) is a group of hosts and associated connectivity hardware: 
    * For A4 and A3 Ultra VMs, the hosts connect through a large-scale distributed [Jupiter network fabric](https://cloud.google.com/blog/products/networking/speed-scale-reliability-25-years-of-data-center-networking).
    * A4X Max and A4X Compute Engine instances are organized into sub-blocks, each constituting an NVIDIA NVLink Domain (NVL72). Within each NVL72, GPUs are tightly interconnected through a dedicated high-bandwidth NVLink fabric. Across sub-blocks, GPUs can connect through RDMA NICs by using the RoCE fabric. Host communication across sub-blocks, as well as other network traffic such as storage, uses the Jupiter network fabric through high-speed frontend Ethernet NICs.
  * `cloud.google.com/gce-topology-host`: the organization-specific ID of the host where the VM is located. A [host or node](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#node) is a single physical server machine in the data center. Each GKE node is provisioned on a VM instance that is provisioned on top of a physical host.
  * `kubernetes.io/hostname`: the hostname of the Kubernetes node. This is typically also the GKE node name.

**Note:** For A4X Max, A4X, A4, and A3 Ultra nodes, GKE adds topology labels automatically because compact placement is enabled by default. For A3 Mega, A3 High, or other [supported machine types](https://docs.cloud.google.com/compute/docs/instances/view-instance-topology#limitations), when you provision the nodes as Spot VMs, you must define [compact placement](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/compact-placement) on the GKE nodes before you can view their physical topology for Topology Aware Scheduling (TAS). Otherwise, the topology labels don't appear on the nodes. For more information about provisioning A3 Mega and A3 High nodes with a placement policy, see [Create a GPU node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-bandwidth-gpudirect-tcpx#create-gpu-node-pool). 

## View the physical topology of your GKE cluster nodes

Run the following command to get the node labels for your GKE cluster nodes with a specific accelerator:
    
    
    kubectl get nodes -l cloud.google.com/gke-accelerator=ACCELERATOR \
        -ocustom-columns='0-NAME:.metadata.name,0-BLOCK:.metadata.labels.cloud\.google\.com/gce-topology-block,0-SUBBLOCK:.metadata.labels.cloud\.google\.com/gce-topology-subblock,0-HOST:.metadata.labels.cloud\.google\.com/gce-topology-host'| sort -k2,4

Replace `ACCELERATOR` with the name of the accelerator, such as `nvidia-h200-141gb`.

The output displays the block, sub-block, and host of each of the GKE nodes with the specified accelerator.

For more information, see [View the topology of a reservation](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity#view-capacity-topology).

## What's next

  * Learn how to [schedule GKE workloads with Topology Aware Scheduling](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/schedule-gke-workloads-tas).
  * Learn how to [manage host maintenance events, cluster upgrades, faulty host reporting for GKE clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/manage-gke-clusters)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
