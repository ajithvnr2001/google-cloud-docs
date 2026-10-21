---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a2/
title: Create an AI-optimized GKE cluster that uses A2 \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:34:54.754971+00:00
---

# Create an AI-optimized GKE cluster that uses A2  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Create an AI-optimized GKE cluster that uses A2 Stay organized with collections  Save and categorize content based on your preferences. 

[ General GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus)

This document describes how you can create custom Google Kubernetes Engine (GKE) clusters that use the A2 Standard (A100 40GB) or A2 Ultra (A100 80GB) accelerator-optimized machine types to support your artificial intelligence (AI) and machine learning (ML) workloads. A2 is a [General GPU machine series](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus), which provide independent compute resources designed for mainstream AI tasks such as training smaller models and single-host inference.

GKE provides a single platform surface to run a diverse set of workloads for your organization, reducing the operational burden of managing multiple platforms.

To create an AI-optimized GKE cluster that uses the A2 machine series, you'll do the following:

  1. Create the GKE environment
  2. Connect to your cluster
  3. Configure your Pod manifests



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Required roles

To get the permissions that you need to create and manage a GKE cluster, ask your administrator to grant you the following IAM roles on the project: 

  * [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`)
  * [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Choose a consumption option and obtain capacity

  1. **Choose a consumption option**. Make your choice based on how you want to get and use GPU resources. For more information, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).

For GKE, consider the following additional information when you choose a consumption option:

     * For more information about flex-start ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) and GKE, see [About GPU obtainability with flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws).
     * Flex-start uses best-effort compact placement. To examine your topology, see [View the physical topology of nodes in your GKE cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/schedule-gke-workloads-tas#view-physical-topology).
     * You can only get topology information when using Spot VMs if you configure [compact placement](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/compact-placement).
  2. **Obtain capacity**. Learn how to [obtain capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/obtain-capacity) for your consumption option.




### Requirements

For an AI-optimized GKE cluster that uses A2 machines, your GPU nodes must use NVIDIA driver version 450.80.02 or later.

### Limitations

The following limitations apply to A2 machines as a [General GPU](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus):

  * **Multi-instance GPU:** Although A2 (A100 GPUs) support hardware partitioning, multi-instance GPU (NVIDIA) is not supported when using GKE Autopilot. For workloads that require A100 GPU partitioning, you must use GKE Standard.



## Create the GKE environment

You can create a cluster in Autopilot or Standard mode.

###  Autopilot 

To create an Autopilot cluster, run the following command:
    
    
      gcloud container clusters create-auto CLUSTER_NAME \
          --region=REGION
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `REGION`: the region for your cluster.



###  Standard 

Create a Standard cluster and GPU node pool:

  1. To create a Standard cluster, run the following command:
         
         gcloud container clusters create CLUSTER_NAME \
             --region=REGION \
             --enable-ip-alias
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `REGION`: the region for your cluster.
  2. Create the node pool. After creating your cluster, you can add a node pool with A2 GPUs.

Note the following:

     * A2 Standard machine types (`a2-highgpu`) require you to manually attach Local SSD disks to your nodes to use them for scratch space or caching. Use the `--local-ssd-count` flag.
     * A2 Ultra machine types (`a2-ultragpu`) automatically include a fixed number of Local SSD disks by default.
     * For multi-node training workloads, we recommend using a [compact placement policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/compact-placement) to minimize networking latency between nodes.
     * For multi-node training workloads, we also recommend enabling [NCCL Fast Socket](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nccl-fast-socket) to improve network performance.

###  A2 Standard (A100 40GB) 
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --region=REGION \
        --node-locations=ZONE \
        --machine-type=MACHINE_TYPE \
        --accelerator=type=nvidia-tesla-a100,count=AMOUNT,gpu-driver-version=LATEST \
        --placement-type=COMPACT \
        --scopes="https://www.googleapis.com/auth/cloud-platform" \
        --local-ssd-count=LOCAL_SSD_COUNT
    

###  A2 Ultra (A100 80GB) 
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --region=REGION \
        --node-locations=ZONE \
        --machine-type=MACHINE_TYPE \
        --accelerator=type=nvidia-a100-80gb,count=AMOUNT,gpu-driver-version=LATEST \
        --placement-type=COMPACT \
        --scopes="https://www.googleapis.com/auth/cloud-platform"
    

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `REGION`: the region for your cluster.
     * `ZONE`: one or more zones within your region that has the requested GPUs available, for example, `us-central1-a`. This is required when using compact placement.
     * `NODE_POOL_NAME`: the name of your node pool.
     * `MACHINE_TYPE`: the machine type for your nodes, for example, `a2-highgpu-1g`.
     * `AMOUNT`: the number of GPUs to attach to each node.
     * `LOCAL_SSD_COUNT`: the number of Local SSD volumes to provision on each node.



## Connect to your cluster

Connect to your cluster so that you can run the `kubectl` commands in the next sections:
    
    
    gcloud container clusters get-credentials CLUSTER_NAME \
        --region=REGION
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `REGION`: the region for your cluster.



For more information, see [Install kubectl and configure cluster access](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl).

## Configure your Pod manifest (Autopilot only)

If you created an Autopilot cluster, you must select the appropriate GPUs in your Pod manifests so that GKE provisions the hardware.

  1. Specify the chosen GPU type and specific reservation by using node selectors:
         
         spec:
           nodeSelector:
             cloud.google.com/gke-accelerator: ACCELERATOR
             cloud.google.com/gke-gpu-driver-version: latest
             # Optional: Include if using reserved capacity
             cloud.google.com/reservation-name: RESERVATION_NAME
             cloud.google.com/reservation-affinity: "specific"
         

Replace the following:

     * `ACCELERATOR`: the accelerator that you reserved. You must use `nvidia-tesla-a100` (for A2 Standard) or `nvidia-a100-80gb` (for A2 Ultra).
     * `RESERVATION_NAME`: the name of the Compute Engine capacity reservation. To consume shared reservations, or specific blocks and sub-blocks of reservations, see the respective sections in [Consuming reserved zonal path resources](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations).
  2. Add the following resources to the container that requests GPUs:
         
         containers:
           - name: my-container
             resources:
               limits:
                 nvidia.com/gpu: AMOUNT
         

Replace `AMOUNT` with the number of GPUs to attach to each node.




## What's next

  * [Schedule GKE workloads](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/schedule-gke-workloads-tas)
  * [Enable node health prediction](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/enable-node-health-prediction)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
