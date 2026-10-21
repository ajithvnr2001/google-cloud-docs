---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-g2-g4/
title: Create an AI-optimized GKE cluster that uses G2 or G4 \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:34:54.570416+00:00
---

# Create an AI-optimized GKE cluster that uses G2 or G4  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-g2-g4/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Create an AI-optimized GKE cluster that uses G2 or G4 Stay organized with collections  Save and categorize content based on your preferences. 

[ General GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus)

This document describes how you can create AI-optimized Google Kubernetes Engine (GKE) clusters that use the G2 (NVIDIA L4) or G4 (NVIDIA RTX PRO 6000) accelerator-optimized machine series to support your artificial intelligence (AI) and machine learning (ML) workloads. G2 and G4 are [General GPU](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus) machine series, which provide independent compute resources designed for mainstream AI tasks such as small-to-medium inference and graphics-intensive applications. In addition to single-GPU and multi-GPU machine types, the G4 machine series supports virtual GPUs (vGPUs) on machine types that have less than one GPU:

  * `g4-standard-6` (one-eighth of a GPU)
  * `g4-standard-12` (one-quarter of a GPU)
  * `g4-standard-24` (one-half of a GPU)



GKE provides a single platform surface to run a diverse set of workloads for your organization, reducing the operational burden of managing multiple platforms.

To create an AI-optimized GKE cluster with G2 or G4, complete the following steps:

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

To create an AI-optimized GKE cluster that uses G2 or G4, ensure that you meet the following requirements:

  * **GKE version:** G4 (NVIDIA RTX PRO 6000) machines require the following minimum GKE versions: 
    * **Standard mode:**
      * Machine types that have one or more GPUs: `1.34.0-gke.1662000` or later
      * Machine types that have less than one GPU (`g4-standard-6`, `g4-standard-12`, and `g4-standard-24`): 
        * **1.35:** `1.35.8-gke.1518000` or later
        * **1.36 or later:** `1.36.4-gke.1082000` or later
    * **Autopilot mode:**
      * Machine types that have one or more GPUs: `1.34.1-gke.1829001` or later
      * Machine types that have less than one GPU (`g4-standard-6`, `g4-standard-12`, and `g4-standard-24`): 
        * **1.35:** `1.35.8-gke.1518000` or later
        * **1.36 or later:** `1.36.4-gke.1082000` or later
  * **GPU drivers:**
    * G2 (NVIDIA L4) nodes must use NVIDIA driver version `535` or later.
    * G4 (NVIDIA RTX PRO 6000) nodes must use NVIDIA driver version `580` or later.



### Limitations

The following limitations apply to G2 and G4 as [General GPU](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus) machine series:

  * **Local SSDs:** G2 and G4 machine types don't include Local SSD disks by default. You must manually attach them if required. The `g4-standard-6` (one-eighth of a GPU) machine type doesn't support Local SSDs.
  * **NCCL Fast Socket:** you can't use [NCCL Fast Socket](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nccl-fast-socket) with G2 or G4 machines on GKE. While G2 and G4 machines support multi-node communication, they use standard VPC networking. For large-scale distributed training that requires maximum network throughput, we recommend using the [Clustered GPU machine series](https://docs.cloud.google.com/ai-hypercomputer/docs/cluster-capabilities), such as [A3 High or A3 Mega](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-standard-a3-high-mega) (which use GPUDirect TCPX) or [A3 Ultra and A4](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4-a3-ultra) (which use GPUDirect RDMA).
  * **G4 machine types that have less than one GPU:** for `g4-standard-6`, `g4-standard-12`, and `g4-standard-24`: 
    * You can't use [Ubuntu node images](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#ubuntu).
    * You can't use [multi-instance GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi), [NVIDIA MPS](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nvidia-mps-gpus), or [GPU time-sharing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/timesharing-gpus).



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
  2. Create the node pool. After creating your cluster, you can add a node pool with G2 or G4. For multi-node workloads using G2 (L4) or G4 (RTX PRO 6000), we recommend using a [compact placement policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/compact-placement) to minimize networking latency between nodes.

To create a node pool, use the following command:

**Tip:** To run graphics-intensive workloads on this VM, you must use either the `nvidia-l4-vws` (for G2) or `nvidia-rtx-pro-6000-vws` (for G4 machine types that have one or more GPUs) accelerator type because they support [NVIDIA RTX Virtual Workstation (vWS)](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations). When you create an instance that uses NVIDIA RTX Virtual Workstation, Compute Engine automatically adds a vWS license. For information about pricing for virtual workstations, see the [GPU pricing page](https://cloud.google.com/compute/gpus-pricing).

###  G2 (NVIDIA L4) 
         
         gcloud container node-pools create NODE_POOL_NAME \
             --cluster=CLUSTER_NAME \
             --region=REGION \
             --node-locations=ZONE \
             --machine-type=MACHINE_TYPE \
             --accelerator=type=nvidia-l4,count=AMOUNT,gpu-driver-version=LATEST \
             --placement-type=COMPACT \
             --scopes="https://www.googleapis.com/auth/cloud-platform" \
             --local-ssd-count=LOCAL_SSD_COUNT
         

###  G4 (NVIDIA RTX PRO 6000) 
         
         gcloud container node-pools create NODE_POOL_NAME \
             --cluster=CLUSTER_NAME \
             --region=REGION \
             --node-locations=ZONE \
             --machine-type=MACHINE_TYPE \
             --accelerator=type=nvidia-rtx-pro-6000,count=AMOUNT,gpu-driver-version=LATEST \
             --disk-type=hyperdisk-balanced \
             --placement-type=COMPACT \
             --scopes="https://www.googleapis.com/auth/cloud-platform" \
             --local-ssd-count=LOCAL_SSD_COUNT
         

###  G4 Virtual Workstation (vWS) 
         
         gcloud container node-pools create NODE_POOL_NAME \
             --cluster=CLUSTER_NAME \
             --region=REGION \
             --node-locations=ZONE \
             --machine-type=MACHINE_TYPE \
             --accelerator=type=nvidia-rtx-pro-6000-vws,count=AMOUNT,gpu-driver-version=LATEST \
             --disk-type=hyperdisk-balanced \
             --placement-type=COMPACT \
             --scopes="https://www.googleapis.com/auth/cloud-platform" \
             --local-ssd-count=LOCAL_SSD_COUNT
         

Replace the following:

     * `NODE_POOL_NAME`: the name of your node pool.
     * `CLUSTER_NAME`: the name of your cluster.
     * `REGION`: the region for your cluster.
     * `ZONE`: one or more zones within your region that has the requested GPUs available, for example, `us-central1-a`. This is required when using compact placement.
     * `MACHINE_TYPE`: the machine type for your nodes, for example, `g2-standard-4` for G2 machines, `g4-standard-48` for a single-GPU G4 machine, or `g4-standard-6`, `g4-standard-12`, or `g4-standard-24` for G4 machine types that have less than one GPU (with the `nvidia-rtx-pro-6000` accelerator type).
     * `AMOUNT`: the number of GPUs to attach to each node. If you use a G4 machine type that has less than one GPU (`g4-standard-6`, `g4-standard-12`, or `g4-standard-24`), or `g4-standard-48` (one GPU), you must set `AMOUNT` to `1`.
     * `LOCAL_SSD_COUNT`: the number of Local SSD volumes to provision on each node. Omit the `--local-ssd-count` flag if you use the `g4-standard-6` machine type, because `g4-standard-6` doesn't support Local SSDs.



## Connect to your cluster

Connect to your cluster so that you can run the `kubectl` commands in the next sections:
    
    
    gcloud container clusters get-credentials CLUSTER_NAME \
        --region=REGION
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `REGION`: the region for your cluster.



For more information, see [Install kubectl and configure cluster access](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl).

## Configure your Pod manifests (Autopilot only)

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

     * `ACCELERATOR`: the accelerator that you reserved. You must use `nvidia-l4` (for G2), `nvidia-rtx-pro-6000` (for G4), or `nvidia-rtx-pro-6000-vws` (for G4 with Virtual Workstation).
     * `RESERVATION_NAME`: the name of the Compute Engine capacity reservation. To consume shared reservations, or specific blocks and sub-blocks of reservations, see the respective sections in [Consuming reserved zonal path resources](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations).
  2. Add the following resources to the container that requests GPUs:
         
         containers:
           - name: my-container
             resources:
               limits:
                 nvidia.com/gpu: AMOUNT
         

Replace `AMOUNT` with the number of GPUs for the container to consume. To request a G4 machine type that has less than one GPU (`g4-standard-6`, `g4-standard-12`, or `g4-standard-24`) in an Autopilot cluster, you must use a custom `ComputeClass` that specifies the machine type and you must set `nvidia.com/gpu` to `1`. For instructions, see [Request G4 machine types that have less than one GPU](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus#request-g4-less-than-one).




## What's next

  * [Schedule GKE workloads](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/schedule-gke-workloads-tas)
  * [Enable node health prediction](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/enable-node-health-prediction)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
