---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus/
title: About GPUs in Google Kubernetes Engine (GKE) \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:26:19.012600+00:00
---

# About GPUs in Google Kubernetes Engine (GKE)  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  About GPUs in Google Kubernetes Engine (GKE) Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes GPUs in Google Kubernetes Engine (GKE) to help you to select the optimal GPU configuration for your workloads. If you want to deploy GPU workloads that use Slurm, see instead [Create an AI-optimized Slurm cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-fully-managed-slurm-cluster).

You can use GPUs to accelerate resource intensive tasks, such as machine learning and data processing. The information on this page can help you to do the following:

  * Ensure GPU availability when needed.
  * Decide whether to use GPUs in GKE Autopilot mode or GKE Standard mode clusters.
  * Choose GPU-related features to efficiently use your GPU capacity.
  * Monitor GPU node metrics.
  * Improve GPU workload reliability by handling disruptions more effectively.



This page is intended for [Platform admins and operators](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks#operators-platform-admin) and [Machine learning (ML) engineers](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks#data-ai-ml-engineer) who want to ensure that accelerator infrastructure is optimized for your workloads.

Before reading this page, ensure that you're familiar with the following:

  * [Autopilot mode and Standard mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)
  * [Quotas in Google Cloud](https://docs.cloud.google.com/docs/quotas/overview)



## GPU selection in GKE

In GKE, the way you request GPU hardware depends on whether you are using Autopilot or Standard mode. In Autopilot, you request GPU hardware by specifying GPU resources in your workloads. In GKE Standard mode, you can attach GPU hardware to nodes in your clusters, and then allocate GPU resources to containerized workloads running on those nodes. For detailed instructions on how to attach and use GPUs in your workloads, refer to [Deploy GPU workloads on Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus) or [Run GPUs on Standard node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus).

GKE offers some GPU-specific features to improve efficient GPU resource utilization of workloads running on your nodes, including time-sharing, multi-instance GPUs, and multi-instance GPUs with NVIDIA MPS.

This page helps you to consider choices for requesting GPUs in GKE, including the following:

  * Choosing your GPU quota, the maximum number of GPUs that can run in your project
  * Deciding between Autopilot and Standard modes
  * Manage the GPU stack through GKE or NVIDIA GPU Operator on GKE
  * Choosing features to reduce the amount of underutilized GPU resources
  * Accessing NVIDIA CUDA-X libraries for CUDA applications
  * Monitoring GPU node metrics
  * Handling disruption due to node maintenance
  * [Use GKE Sandbox to secure GPU workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods)



## Available GPU models

The GPU hardware that's available for use in GKE is a subset of the [GPU models available on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus#gpu-models). The specific hardware that's available depends on the Compute Engine region or zone of your cluster. For more information about specific availability, see [GPU regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).

Google Cloud's most performant machine types—such as A4X Max, A4X, A4, and A3 Ultra—require specific configuration to maximize the performance of the underlying hardware. Details about how to configure GKE clusters to use these GPU machine types reside in the AI Hypercomputer documentation, which illustrates the capabilities of Google Cloud's integrated supercomputing system.

For information about how to create AI-optimized GKE clusters with these machine types, see the following:

  * To quickly deploy production-ready GKE clusters, [create an AI-optimized GKE cluster with Cluster Toolkit](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute)
  * For precise customization or expansion of existing production GKE environments, use the Google Cloud CLI to create a GKE cluster. Choose one of the following instructions based on which machine type and GPU you want to use: 
    * **GB300** : [Create an AI-optimized GKE cluster that uses A4X Max](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4x-max)
    * **GB200** : [Create an AI-optimized GKE cluster that uses A4X](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4x)
    * **B200 or H200** : [Create an AI-optimized GKE cluster that uses A4 or A3 Ultra](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4-a3-ultra)



For information about GPU pricing, see the [Google Cloud SKUs](https://cloud.google.com/skus) and the [GPU pricing page](https://cloud.google.com/compute/gpus-pricing).

## Plan GPU quota

Your GPU quota is the maximum number of GPUs that can run in your Google Cloud project. To use GPUs in your GKE clusters, your project must have enough GPU quota. Check the [**Quotas** page](https://console.cloud.google.com/iam-admin/quotas) to ensure that you have enough GPUs available in your project.

Your GPU quota should be at least equal to the total number of GPUs you intend to run in your cluster. If you enable [cluster autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler), you should request GPU quota at least equivalent to your cluster's maximum number of nodes multiplied by the number of GPUs per node.

For example, if you expect to utilize three nodes with two GPUs each, then six is the GPU quota required for your project.

To request additional GPU quota, follow the instructions to [request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase), using `gpus` as the metric.

## Choose GPU support using Autopilot or Standard

GPUs are available in Autopilot and Standard clusters.

**Best practice** : 

Use Autopilot clusters for a fully managed Kubernetes experience. In Autopilot, GKE manages driver installation, node scaling, Pod isolation, and node provisioning.

The following table provides an overview of the differences between Autopilot and Standard GPU support:

Description | Autopilot | Standard  
---|---|---  
Requesting GPU hardware | Specify GPU resources in your workloads.  | Attach GPU hardware to nodes in your clusters, and then allocate GPU resources to containerized workloads running on those nodes.   
GPU hardware availability | 

  * NVIDIA GB300
  * NVIDIA GB200
  * NVIDIA B200
  * NVIDIA H200 141GB
  * NVIDIA H100 80GB
  * NVIDIA A100 80GB
  * NVIDIA A100 40GB
  * NVIDIA RTX PRO 6000
  * NVIDIA L4
  * NVIDIA T4

| All GPU types that are supported by Compute Engine  
Selecting a GPU | You request a GPU quantity and type in your workload specification. By default, Autopilot installs the default driver for that GKE version and manages your nodes. To select a specific driver version in Autopilot, see [ NVIDIA drivers selection for Autopilot GPU Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus#drivers-selection). |  You perform the steps described on [Run GPUs on Standard node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus): 

  1. Create a node pool with the specific GPU type and corresponding Compute Engine machine type and choose a driver to install.
  2. Manually install GPU drivers on the nodes if you didn't use automatic installation.
  3. Request GPU quantities in Pod specification.

  
Improve GPU utilization | 

  * [Multi-instance GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi)
  * [Time-sharing GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/timesharing-gpus)

| 

  * [Multi-instance GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi)
  * [Time-sharing GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/timesharing-gpus)
  * [NVIDIA MPS](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nvidia-mps-gpus)

  
Security | 

  * [GPUs with GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#gpus)
  * [GPUs with Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-confidential-nodes)

| 

  * [GPUs with GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#gpus)
  * [GPUs with Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-confidential-nodes)

  
Pricing | [Autopilot GPU Pod pricing](https://docs.cloud.google.com/kubernetes-engine/pricing#autopilot_mode) | [Compute Engine GPU pricing](https://cloud.google.com/compute/gpus-pricing)  
  
To choose the GKE mode of operation that's the best fit for your workloads, see [Choose a GKE mode of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).

## Consume GPUs

GKE offers GPU consumption options that vary based on your workload requirements. Use the [About accelerator consumption options for AI/ML workloads in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/consumption-option) page to choose the best option for your use case.

## Manage the GPU stack through GKE or the NVIDIA GPU Operator on GKE

By default, GKE manages the entire lifecycle of the GPU nodes, including automatic GPU driver installation, monitoring GPU workloads on GKE with [NVIDIA Data Center GPU Manager (DCGM)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dcgm-metrics), and GPU sharing strategies.

**Best practice** : 

Use GKE to manage your GPU nodes, since GKE fully manages the GPU node lifecycle.

Get started with GKE for GPU node management by choosing one of the following:

  * [Deploy GPU workloads in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus)
  * [Run GPUs in Standard node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus)
  * [Deploy clusters with NVIDIA B200 or NVIDIA H200 141GB GPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute)



The [NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/overview.html) may be used as an alternative to fully managed GPU support on GKE on both Container-Optimized OS (COS) and Ubuntu node images. Select this option if you are looking for a consistent experience across multiple cloud service providers, you are already using the NVIDIA GPU Operator, or if you are using software that depends on the NVIDIA GPU operator. To learn more, see [Manage the GPU stack with the NVIDIA GPU Operator](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-operator).

To select the best option for your use case, refer to the following table comparing the two methods of managing GPU nodes on GKE.

**Description** | **Use GKE to manage GPU nodes** | **Use NVIDIA GPU Operator on GKE**  
---|---|---  
Management of GPU node lifecycle (installation, upgrade) | Fully managed by GKE. | Managed by the user.  
Driver installation | [Automatic and manual installation of GPU drivers.](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#create-gpu-pool-auto-drivers) | Manual installation of GPU drivers.  
Node selectors | `cloud.google.com/gke-gpu=true` | `nvidia.com/gpu=true`  
GPU sharing strategies | 

  * Multi-instance GPUs: [ Configure using the GKE API.](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi)


  * Time sharing: [ Configure using the GKE API.](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/timesharing-gpus)


  * Multi-Process Service: [ Configure using the GKE API.](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nvidia-mps-gpus)

| 

  * Multi-instance GPUs: [Configure using node label and ConfigMap](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-operator-mig.html). Supports in-place re-configuration.


  * Time sharing: [Configure using node label and ConfigMap.](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-sharing.html)


  * Multi-process Service: Not supported.

  
Health checking of GPU nodes | 

  * Monitor XID 48 error codes; you can also [ opt-in to monitor other error codes.](https://github.com/richardsliu/container-engine-accelerators/blob/nvidia/nvidia-driver-installer/patch/README.md)


  * Trigger [ node repair](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair#repair_criteria) in 15 min if GPU allocatable count is not equal to capacity and auto-repair is enabled.

| 

  * Monitor all error codes by default.


  * Trigger [ node repair](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair#repair_criteria) in 15 mins if GPU allocatable count is not equal to capacity and auto-repair is enabled.

  
Metrics and observability  | 

  * [ GKE Managed DCGM available](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dcgm-metrics)


  * With [ system metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#system-metrics) enabled, the following GPU metrics are available in Cloud Monitoring: duty cycle, memory usage, and memory capacity.

| 

  * Self-managed DCGM provided by GPU operator.


  * Even when [GKE GPU system metrics](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus#monitoring) are enabled, GPU-related system metrics are not collected, including duty cycle, memory usage, and memory capacity.

  
  
## Optimize resource usage using GPU features in GKE

By default, Kubernetes only supports assigning GPUs as whole units to containers but GKE provides additional features that you can use to optimize the resource usage of your GPU workloads.

The following features are available in GKE to reduce the amount of underutilized GPU resources:

GPU features  
---  
[Multi-instance GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi) |  **Available on:** Autopilot and Standard Split a single GPU into up to seven hardware-separated instances that can be assigned as individual GPUs to containers on a node. Each assigned container gets the resources available to that instance.  
[Time-sharing GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/timesharing-gpus) |  **Available on:** Autopilot and Standard Present a single GPU as multiple units to multiple containers on a node. The GPU driver context-switches and allocates the full GPU resources to each assigned container as needed over time.  
[NVIDIA MPS](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nvidia-mps-gpus) |  **Available on:** Standard Share a single physical NVIDIA GPU across multiple containers. NVIDIA MPS is an alternative, binary-compatible implementation of the CUDA API designed to transparently enable co-operative multi-process CUDA applications to run concurrently on a single GPU device.  
  
## Access the NVIDIA CUDA-X libraries for CUDA applications

[CUDA](https://developer.nvidia.com/cuda-zone) is NVIDIA's parallel computing platform and programming model for GPUs. To use CUDA applications, the image that you use must have the libraries. To add the NVIDIA CUDA-X libraries, you can build and use your own image by including the following values in the `LD_LIBRARY_PATH` environment variable in your container specification: 

  * `/usr/local/nvidia/lib64`: the location of the NVIDIA device drivers.
  * `/usr/local/cuda-CUDA_VERSION/lib64`: the location of the NVIDIA CUDA-X libraries on the node. 

Replace `CUDA_VERSION` with the CUDA-X image version that you used. Some versions also contain debug utilities in `/usr/local/nvidia/bin`. For details, see [the NVIDIA CUDA image on DockerHub](https://hub.docker.com/r/nvidia/cuda).

To check the minimum GPU driver version required for your version of CUDA, see [CUDA Toolkit and Compatible Driver Versions](https://docs.nvidia.com/deploy/cuda-compatibility/index.html#binary-compatibility__table-toolkit-driver).


Ensure that the GKE patch version running on your nodes includes a GPU driver version that's compatible with your chosen CUDA version. For more information about mapping the GPU driver version to GKE version, see [Map the GKE version and Container-Optimized OS node image version to the GPU driver version](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#map-gke-cos-gpu). 

In Autopilot clusters, GKE manages the driver version selection and installation.

## Monitor your GPU node workload performance

If your GKE cluster has [system metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/managing-metrics#system-metrics) enabled, then the following metrics are available in [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) to monitor your GPU workload performance: 

  * **Duty Cycle (`container/accelerator/duty_cycle`): ** Percentage of time over the past sample period (10 seconds) during which the accelerator was actively processing. Between 1 and 100. 
  * **Memory Usage (`container/accelerator/memory_used`): ** Amount of accelerator memory allocated in bytes. 
  * **Memory Capacity (`container/accelerator/memory_total`): ** Total accelerator memory in bytes. 



These metrics apply at the container level (`container/accelerator`) and are not collected for containers scheduled on a GPU that uses GPU time-sharing or NVIDIA MPS. 

You can use predefined dashboards to monitor your clusters with GPU nodes. For more information, see [ View observability metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics). For general information about monitoring your clusters and their resources, refer to [Observability for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/observability). 

### View usage metrics for workloads

You view your workload GPU usage metrics from the **Workloads** dashboard in the Google Cloud console. 

To view your workload GPU usage, perform the following steps:

  1. Go to the **Workloads** page in the Google Cloud console.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload/overview)
  2. Select a workload.



The Workloads dashboard displays charts for GPU memory usage and capacity, and GPU duty cycle. 

### View NVIDIA Data Center GPU Manager (DCGM) metrics

You can collect and visualize NVIDIA DCGM metrics by using [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus). For Autopilot clusters, GKE installs the drivers. For Standard clusters, you must install the NVIDIA drivers. 

For instructions on how to deploy the GKE-managed DCGM package, see [Collect and view NVIDIA Data Center GPU Manager (DCGM) metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dcgm-metrics). 

### JobSet and node health metrics for GPU workloads

In addition to DCGM metrics, you can use the following metrics to monitor the health and performance of your GPU workloads, especially when running them as JobSets. 

#### JobSet metrics

The following metrics apply to both GPU and TPU JobSets that have a single replicated Job: 

  * `kubernetes.io/jobset/times_between_interruptions`
  * `kubernetes.io/jobset/times_to_recover`
  * `kubernetes.io/jobset/uptime`



For more information about these system metrics, see [Kubernetes metrics](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes). 

You can also use the **JobSet dashboard** in the Google Cloud console to visualize and monitor your GPU workloads:

[Go to Deployments](https://console.cloud.google.com//kubernetes/aiml/deployments/jobs)

#### Node health metrics

The following node-level metrics apply to all nodes, including those with GPUs:

  * `kubernetes.io/node/status_condition`: This metric requires GKE version 1.32.1-gke.1357001 or later. 



Node interruption and node pool interruption metrics also apply to non-TPU nodes.

#### Kube-state-metrics for JobSets

The kube-state-metrics for JobSets can be used with GPUs. Collection of these metrics requires GKE version 1.32.1-gke.1357001 or later. For more information, see the [JobSet metrics documentation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/kube-state-metrics#ksm-jobset-metrics). 

## Handle disruption due to node maintenance

The GKE nodes that host the GPUs are subject to maintenance events or other disruptions that might cause node shutdown. In GKE clusters with the control plane running version 1.29.1-gke.1425000 and later, you can reduce disruption to workloads by configuring GKE to terminate your workloads gracefully.

To understand, configure, and monitor disruption events that might occur on GKE nodes running AI/ML workloads, see [Manage GKE node disruption for GPUs and TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu#gcloud).

## What's next

  * Learn how to [run GPUs in Standard node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus).
  * Learn how to [train a model with GPUs in Standard](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/train-model-gpus-standard).
  * Learn how to [deploy GPU workloads in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus).
  * Learn how to use [Multi-instance GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi).
  * Learn more about [Time-sharing GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/timesharing-gpus).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
