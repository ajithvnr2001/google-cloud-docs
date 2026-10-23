---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nccl-fast-socket/
title: Improve workload efficiency using NCCL Fast Socket \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:50.382365+00:00
---

# Improve workload efficiency using NCCL Fast Socket  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nccl-fast-socket/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Improve workload efficiency using NCCL Fast Socket Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to use the [NVIDIA Collective Communication Library (NCCL) Fast Socket plugin](https://github.com/google/nccl-fastsocket) to run more efficient workloads on your Google Kubernetes Engine (GKE) clusters.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Limitations

  * [Compute Engine limitations](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#limitations) apply.
  * [gVNIC limitations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-gvnic#limitations) apply.
  * NCCL Fast Socket is only supported on node pools that have [hardware accelerators](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus) enabled.



### Requirements

GKE Autopilot:

  * GKE Autopilot clusters must be running 1.30.2-gke.1023000 or later.



For details, see [Creating an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster#set-version).

GKE Standard:

  * Your node pools must have gVNIC enabled to use NCCL Fast Socket.
  * GKE nodes must use a Container-Optimized OS [node image](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#cos).
  * Your clusters must be running GKE version 1.25.2-gke.1700 or later.



For details, see [Creating a regional cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster).

## Enable NCCL Fast Socket in Standard clusters

**Note:** If you use machine types from [later generation A series](https://docs.cloud.google.com/compute/docs/gpus#gpu-models) newer than the [A2 machine series](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus), we strongly recommend using the following optimized networking instead of NCCL Fast Socket: 

  * **A3 Ultra (`nvidia-h200-141gb`), A4 (`nvidia-b200`, `nvidia-gb200`), and newer:** use [GPUDirect RDMA](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4-a3-ultra) (for A4X specifically, see [Create an AI-optimized GKE cluster that uses A4X](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4x)). 
  * **A3 High (`nvidia-h100-80gb`) and A3 Mega (`nvidia-h100-mega-80gb`):** use [GPUDirect TCPX](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-bandwidth-gpudirect-tcpx). 



This section shows you how to enable the NCCL Fast Socket plugin in GKE Standard node pools. If you use GKE Autopilot clusters, GKE automatically enables the plugin when you request NCCL Fast Socket in your workloads. For instructions, see the NCCL Fast Socket in Autopilot section.

For Standard clusters, create a node pool that uses the NCCL Fast Socket plugin. You can also update an existing node pool using [`gcloud container node-pools update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/update).
    
    
    gcloud container node-pools create NODEPOOL_NAME \
        --accelerator type=ACCELERATOR_TYPE,count=ACCELERATOR_COUNT \
        --machine-type=MACHINE_TYPE \
        --cluster=CLUSTER_NAME \
        --enable-fast-socket \
        --enable-gvnic
    

Replace the following:

  * `NODEPOOL_NAME`: the name of the new node pool.
  * `CLUSTER_NAME`: the name of the cluster.
  * `ACCELERATOR_TYPE`: the type of [GPU accelerator](https://docs.cloud.google.com/compute/docs/gpus) that you use. For example, `nvidia-tesla-t4`.
  * `ACCELERATOR_COUNT`: the number of GPUs per node.
  * `MACHINE_TYPE`: the type of machine you want to use. NCCL Fast Socket is not supported on [memory-optimized machine types](https://docs.cloud.google.com/compute/docs/machine-types#memory-optimized_machine_type_family).



## Install NVIDIA GPU device drivers

In Autopilot, GPU device drivers are automatically installed.

For Standard clusters, follow the instructions in [Installing NVIDIA GPU device drivers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#installing_drivers) to install the required NVIDIA device drivers on your nodes.

## NCCL Fast Socket in Autopilot

**Note:** If you use machine types from [later generation A series](https://docs.cloud.google.com/compute/docs/gpus#gpu-models) newer than the [A2 machine series](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus), we strongly recommend using the following optimized networking instead of NCCL Fast Socket: 

  * **A3 Ultra (`nvidia-h200-141gb`), A4 (`nvidia-b200`, `nvidia-gb200`), and newer:** Use [GPUDirect RDMA](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4-a3-ultra) (for A4X, see [Create an AI-optimized GKE cluster that uses A4X](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4x)). 
  * **A3 High (`nvidia-h100-80gb`) and A3 Mega (`nvidia-h100-mega-80gb`):** Use [GPUDirect TCPX](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-bandwidth-gpudirect-tcpx-autopilot). 



In Autopilot clusters, you request NCCL Fast Socket in your workloads by using the `cloud.google.com/gke-nccl-fastsocket` node selector. When you request NCCL Fast Socket in a workload, GKE enables gVNIC and NCCL Fast Socket on nodes that GKE provisions for the workload. You can use NCCL Fast Socket with any GPU type that Autopilot supports.

The following pod requests NCCL Fast Socket:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: my-gpu-pod
    spec:
      nodeSelector:
        cloud.google.com/gke-accelerator: GPU_TYPE
        **cloud.google.com/gke-nccl-fastsocket : "true"**
      containers:
      - name: my-gpu-container
        image: nvidia/cuda:11.0.3-runtime-ubuntu20.04
        command: ["/bin/bash", "-c", "--"]
        args: ["while true; do sleep 600; done;"]
        resources:
          limits:
            nvidia.com/gpu: GPU_QUANTITY
    

Replace the following:

  * `GPU_TYPE`: the type of GPU hardware. Allowed values are the following: 
    * `nvidia-gb200`: NVIDIA GB200 (Preview)
    * `nvidia-b200`: NVIDIA B200 (180GB)
    * `nvidia-h200-141gb`: NVIDIA H200 (141GB)
    * `nvidia-h100-mega-80gb`: NVIDIA H100 Mega (80GB)
    * `nvidia-h100-80gb`: NVIDIA H100 (80GB)
    * `nvidia-a100-80gb`: NVIDIA A100 (80GB)
    * `nvidia-tesla-a100`: NVIDIA A100 (40GB)
    * `nvidia-rtx-pro-6000`: NVIDIA RTX PRO 6000
    * `nvidia-l4`: NVIDIA L4
    * `nvidia-tesla-t4`: NVIDIA T4
  * `GPU_QUANTITY`: the number of GPUs to allocate to the container.



## Verify that NCCL Fast Socket is enabled

To verify that NCCL Fast Socket is enabled, view the kube-system pods:
    
    
    kubectl get pods -n kube-system
    

The output is similar to the following:
    
    
    NAME                             READY   STATUS    RESTARTS   AGE
    nccl-fastsocket-installer-qvfdw  2/2     Running   0          10m
    nccl-fastsocket-installer-rtjs4  2/2     Running   0          10m
    nccl-fastsocket-installer-tm294  2/2     Running   0          10m
    

In this output, the number of Pods should be equal to the number of nodes in the node pool.

## Disable NCCL Fast Socket

In GKE Autopilot clusters, the NCCL Fast Socket plugin is disabled by default. To disable the plugin on an existing workload, redeploy the workload without the NCCL Fast Socket node selector.

To disable NCCL Fast Socket for a node pool in Standard clusters, run the following command:
    
    
    gcloud container node-pools update NODEPOOL_NAME \
        --cluster=CLUSTER_NAME \
        --no-enable-fast-socket
    

This command re-creates the nodes in the node pool without the NCCL Fast Socket plugin. This process might disrupt running workloads.

## Troubleshooting

To troubleshoot gVNIC, see [Troubleshooting Google Virtual NIC](https://docs.cloud.google.com/compute/docs/troubleshooting/gvnic).

## What's next

  * Use [network policy logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging) to record when connections to Pods are allowed or denied by your cluster's [network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
