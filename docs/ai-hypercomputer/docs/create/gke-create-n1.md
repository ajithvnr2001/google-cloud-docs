---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-n1/
title: Create an AI-optimized GKE cluster that uses N1 \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:43.279124+00:00
---

# Create an AI-optimized GKE cluster that uses N1  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-n1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Create an AI-optimized GKE cluster that uses N1 Stay organized with collections  Save and categorize content based on your preferences. 

[ General GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus)

This document describes how you can create custom Google Kubernetes Engine (GKE) clusters that use the N1 general-purpose machine series with attached NVIDIA T4 or V100 GPUs to support your artificial intelligence (AI) and machine learning (ML) workloads. N1 machines with attached GPUs are considered [General GPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus), which provide independent compute resources designed for mainstream AI tasks such as small-to-medium inference and graphics-intensive applications.

GKE provides a single platform surface to run a diverse set of workloads for your organization, reducing the operational burden of managing multiple platforms.

To create an AI-optimized GKE cluster that uses the N1 machine series, you'll do the following:

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

  2. **Obtain capacity**. Learn how to [obtain capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/obtain-capacity) for your consumption option.




### Requirements

For an AI-optimized GKE cluster that uses N1, your nodes must use NVIDIA driver version 535 or later.

### Limitations

The following limitations apply to N1 as a [General GPU](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus) machine series:

  * **Multi-instance GPU (NVIDIA):** N1 machine series doesn't support multi-instance GPUs (NVIDIA).
  * **NCCL Fast Socket:** you cannot use [NCCL Fast Socket](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nccl-fast-socket) with N1 machines on GKE. While N1 machines support multi-node communication, they use standard VPC networking. For large-scale distributed training that requires maximum network throughput, we recommend using a [Clustered GPU](https://docs.cloud.google.com/ai-hypercomputer/docs/cluster-capabilities) machine series, such as [A3 High or A3 Mega](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-standard-a3-high-mega) (which use GPUDirect TCPX) or [A3 Ultra and A4](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4-a3-ultra) (which use GPUDirect RDMA).



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
  2. Create the node pool. After creating your cluster, you can add a node pool with N1 machines with attached T4 or V100 GPUs.

To create a node pool, use the following command:

**Tip:** If you plan on running graphics-intensive workloads on this VM, then we recommend that you use the `nvidia-tesla-t4-vws` or `nvidia-tesla-p4-vws` accelerator type because it supports [NVIDIA RTX Virtual Workstation (vWS)](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations). When you create an instance that uses NVIDIA RTX Virtual Workstation, Compute Engine automatically adds a vWS license. For information about pricing for virtual workstations, see the [GPU pricing page](https://cloud.google.com/compute/gpus-pricing).

###  N1 with attached T4 GPUs 
         
         gcloud container node-pools create NODE_POOL_NAME \
             --cluster=CLUSTER_NAME \
             --region=REGION \
             --node-locations=ZONE \
             --machine-type=MACHINE_TYPE \
             --accelerator=type=nvidia-tesla-t4,count=AMOUNT,gpu-driver-version=LATEST \
             --scopes="https://www.googleapis.com/auth/cloud-platform" \
             --local-ssd-count=LOCAL_SSD_COUNT
         

###  N1 with attached V100 GPUs 
         
         gcloud container node-pools create NODE_POOL_NAME \
             --cluster=CLUSTER_NAME \
             --region=REGION \
             --node-locations=ZONE \
             --machine-type=MACHINE_TYPE \
             --accelerator=type=nvidia-tesla-v100,count=AMOUNT,gpu-driver-version=LATEST \
             --scopes="https://www.googleapis.com/auth/cloud-platform" \
             --local-ssd-count=LOCAL_SSD_COUNT
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `REGION`: the region for your cluster.
     * `ZONE`: one or more zones within your region that has the requested GPUs available, for example, `us-central1-a`. This is required when using compact placement.
     * `NODE_POOL_NAME`: the name of your node pool.
     * `MACHINE_TYPE`: the N1 machine type for your nodes, for example, `n1-standard-4`.
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

     * `ACCELERATOR`: the accelerator that you want to use. Use `nvidia-tesla-t4` for T4 GPUs, or `nvidia-tesla-v100` for V100 GPUs.
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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
