---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/timesharing-gpus/
title: Share GPUs across workloads with GPU time-sharing \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:10.811650+00:00
---

# Share GPUs across workloads with GPU time-sharing  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/timesharing-gpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Share GPUs across workloads with GPU time-sharing Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to let multiple workloads get _GPU time-sharing_ access to a single NVIDIA® GPU hardware accelerator in your Google Kubernetes Engine (GKE) nodes. By using GPU time-sharing in GKE, you can more efficiently use your attached GPUs and save running costs.

This page is for Developers who design and deploy workloads on GKE clusters and for Admins and architects who create and manage a GKE cluster, plan infrastructure and resourcing requirements, and monitor the cluster's performance. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this page, ensure that you're familiar with [how time-sharing works in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/timesharing-gpus), including limitations and situations when you should use GPU time-sharing.

## Requirements

  * **GKE version** : You can enable GPU time-sharing on GKE Standard clusters running GKE version 1.23.7-gke.1400 and later. You can use time-sharing GPUs on GKE Autopilot clusters running GKE version 1.29.3-gke.1093000 and later.
  * **GPU type** : You can enable GPU time-sharing on all [NVIDIA GPU models](https://docs.cloud.google.com/compute/docs/gpus). However, you can't enable time-sharing for [G4 machine types](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) that have less than one GPU.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have sufficient [NVIDIA GPU models](https://docs.cloud.google.com/compute/docs/gpus#nvidia_t4_gpus) quota. If you need more quota, refer to [Requesting an increase in quota](https://docs.cloud.google.com/compute/quotas#requesting_additional_quota).
  * Plan your GPU capacity based on the resource needs of the workloads and the capacity of the underlying GPU.
  * Review the limitations of GPU time-sharing.



## Enable GPU time-sharing on GKE clusters and node pools

As a platform administrator, you must enable GPU time-sharing on a GKE Standard cluster before developers can deploy workloads to use the GPUs. To enable GPU time-sharing, you must do the following:

  1. Enable GPU time-sharing on a GKE cluster.
  2. Install NVIDIA GPU device drivers (if required).
  3. Verify the GPU resources available on your nodes.



Autopilot clusters that run version 1.29.3-gke.1093000 and later enable time-sharing GPUs by default. Time-sharing on Autopilot clusters is configured in the workload specification. To learn more, see the Deploy workloads that use time-shared GPUs section.

### Enable GPU time-sharing on a GKE Standard cluster

You can enable GPU time-sharing when you create GKE Standard clusters. The default node pool in the cluster has the feature enabled. You still need to enable GPU time-sharing when you manually create new node pools in that cluster.
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --cluster-version=CLUSTER_VERSION \
        --machine-type=MACHINE_TYPE \
        --accelerator=type=GPU_TYPE,count=GPU_QUANTITY,gpu-sharing-strategy=time-sharing,max-shared-clients-per-gpu=CLIENTS_PER_GPU,gpu-driver-version=DRIVER_VERSION
    

Replace the following:

  * `CLUSTER_NAME`: the name of your new cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * `CLUSTER_VERSION`: the GKE version for the cluster control plane and nodes. Use GKE version 1.23.7-gke.1400 or later. Alternatively, specify a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#current_versions) with that GKE version by using the `--release-channel=RELEASE_CHANNEL` flag.
  * `MACHINE_TYPE`: the Compute Engine machine type for your nodes. We recommend that you select an [Accelerator-optimized machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines).
  * `GPU_TYPE`: the GPU type, which must be an [NVIDIA GPU platform](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads) such as `nvidia-tesla-v100`.
  * `GPU_QUANTITY`: the number of physical GPUs to attach to each node in the default node pool.
  * `CLIENTS_PER_GPU`: the maximum number of containers that can share each physical GPU.
  * `DRIVER_VERSION`: the NVIDIA driver version to install. Can be one of the following: 
    * `default`: Install the default driver version for your GKE version.
    * `latest`: Install the latest available driver version for your GKE version. Available only for nodes that use Container-Optimized OS.
    * `disabled`: Skip automatic driver installation. You **must** manually install a driver after you create the node pool. If you omit `gpu-driver-version`, this is the default option.



### Enable GPU time-sharing on a GKE node pool

You can enable GPU time-sharing when you manually create new node pools in a GKE cluster.
    
    
    gcloud container node-pools create NODEPOOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --machine-type=MACHINE_TYPE \
        --accelerator=type=GPU_TYPE,count=GPU_QUANTITY,gpu-sharing-strategy=time-sharing,max-shared-clients-per-gpu=CLIENTS_PER_GPU,gpu-driver-version=DRIVER_VERSION
    

Replace the following:

  * `NODEPOOL_NAME`: the name of your new node pool.
  * `CLUSTER_NAME`: the name of your cluster, which must run GKE version 1.23.7-gke.1400 or later.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * `MACHINE_TYPE`: the Compute Engine machine type for your nodes. We recommend that you select an [Accelerator-optimized machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines).
  * `GPU_TYPE`: the GPU type, which must be an [NVIDIA GPU platform](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads) such as `nvidia-tesla-v100`.
  * `GPU_QUANTITY`: the number of physical GPUs to attach to each node in the node pool.
  * `CLIENTS_PER_GPU`: the maximum number of containers that can share each physical GPU.
  * `DRIVER_VERSION`: the NVIDIA driver version to install. Can be one of the following:

    * `default`: Install the default driver version for your GKE version.
    * `latest`: Install the latest available driver version for your GKE version. Available only for nodes that use Container-Optimized OS.
    * `disabled`: Skip automatic driver installation. You **must** manually install a driver after you create the node pool. If you omit `gpu-driver-version`, this is the default option.
**Note:** The `gpu-driver-version` option is only available for GKE version 1.27.2-gke.1200 and later. In earlier versions, omit this flag and manually install a driver after you create the node pool.



### Install NVIDIA GPU device drivers

Before you proceed, connect to your cluster by running the following command:
    
    
    gcloud container clusters get-credentials CLUSTER_NAME
    

If you chose to disable automatic driver installation when creating the cluster, or if you use a GKE version earlier than 1.27.2-gke.1200, you must manually install a compatible NVIDIA driver to manage the GPU time-sharing division of the physical GPUs. To install the drivers, you deploy a GKE installation DaemonSet that sets the drivers up.

For instructions, refer to [Installing NVIDIA GPU device drivers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#installing_drivers).

If you plan to use node auto-provisioning in your cluster, you must also configure node auto-provisioning with the scopes that allow GKE to install the GPU device drivers for you. For instructions, refer to [Using node auto-provisioning with GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#using_node_auto-provisioning_with_gpus).

### Verify the GPU resources available on your nodes

To verify that the number of GPUs visible in your nodes matches the number you specified when you enabled GPU time-sharing, describe your nodes:
    
    
    kubectl describe nodes NODE_NAME
    

The output is similar to the following:
    
    
    ...
    Capacity:
      ...
      nvidia.com/gpu:             3
    Allocatable:
      ...
      nvidia.com/gpu:             3
    

In this example output, the number of GPU resources on the node is `3` because the value that was specified for `max-shared-clients-per-gpu` was `3` and the `count` of physical GPUs to attach to the node was `1`. As another example, if the `count` of physical GPUs was `2`, the output would show `6` allocatable GPU resources, three on each physical GPU.

## Deploy workloads that use GPU time-sharing

As an application operator who is deploying GPU workloads, you can select GPU time-sharing enabled by specifying the appropriate node labels in a `nodeSelector` in your manifests. When planning your requests, review the [request limits](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/timesharing-gpus#request-limits) to ensure that GKE doesn't reject your deployments.

To deploy a workload to consume GPU time-sharing, complete the following steps:

  1. Add a `nodeSelector` to your workload manifest for the following labels:

     * `cloud.google.com/gke-gpu-sharing-strategy: time-sharing`: selects nodes that use GPU time-sharing.
     * `cloud.google.com/gke-max-shared-clients-per-gpu: "CLIENTS_PER_GPU"`: selects nodes that allow a specific number of containers to share the underlying GPU.
  2. Add the `nvidia.com/gpu=1` GPU resource request to your container specification, in `spec.containers.resources.limits`.




For example, the following steps show you how to deploy three Pods to a GPU time-sharing node pool. GKE allocates each container to the same physical GPU. The containers print the UUID of the GPU that's attached to that container.

  1. Save the following manifest as `gpu-timeshare.yaml`:



### Autopilot
    
    
            apiVersion: apps/v1
            kind: Deployment
            metadata:
              name: cuda-simple
            spec:
              replicas: 3
              selector:
                matchLabels:
                  app: cuda-simple
              template:
                metadata:
                  labels:
                    app: cuda-simple
                spec:
                  nodeSelector:
                    cloud.google.com/gke-accelerator: "GPU_TYPE"
                    cloud.google.com/gke-gpu-sharing-strategy: "time-sharing"
                    cloud.google.com/gke-max-shared-clients-per-gpu: "CLIENTS_PER_GPU"
                    cloud.google.com/gke-accelerator-count: "GPU_COUNT"
                  containers:
                  - name: cuda-simple
                    image: nvidia/cuda:11.0.3-base-ubi7
                    command:
                    - bash
                    - -c
                    - |
                      /usr/local/nvidia/bin/nvidia-smi -L; sleep 300
                    resources:
                      limits:
                        nvidia.com/gpu: 1
          

Replace the following:

  * `GPU_TYPE`: the GPU type.
  * `CLIENTS_PER_GPU`: the number of workloads that'll use this GPU. For this example, use `3`.
  * `GPU_COUNT`: the number of physical GPUs to attach to the node. For this example, use `1`.



### Standard
    
    
            apiVersion: apps/v1
            kind: Deployment
            metadata:
              name: cuda-simple
            spec:
              replicas: 3
              selector:
                matchLabels:
                  app: cuda-simple
              template:
                metadata:
                  labels:
                    app: cuda-simple
                spec:
                  nodeSelector:
                    cloud.google.com/gke-gpu-sharing-strategy: "SHARING_STRATEGY"
                    cloud.google.com/gke-max-shared-clients-per-gpu: "CLIENTS_PER_GPU"
                  containers:
                  - name: cuda-simple
                    image: nvidia/cuda:11.0.3-base-ubi7
                    command:
                    - bash
                    - -c
                    - |
                      /usr/local/nvidia/bin/nvidia-smi -L; sleep 300
                    resources:
                      limits:
                        nvidia.com/gpu: 1
          

Replace the following:

  * `SHARING_STRATEGY` with "time-sharing" to request time-sharing for your GPU.
  * `CLIENTS_PER_GPU`: the number of workloads that will use this GPU. For this example, use `3`.



  1. Apply the manifest:
         
         kubectl apply -f gpu-timeshare.yaml
         

  2. Check that all Pods are running:
         
         kubectl get pods -l=app=cuda-simple
         

  3. Check the logs for any Pod to view the UUID of the GPU:
         
         kubectl logs POD_NAME
         

The output is similar to the following:
         
         GPU 0: Tesla V100-SXM2-16GB (UUID: GPU-0771302b-eb3a-6756-7a23-0adcae8efd47)
         

  4. If your nodes have one physical GPU attached, check the logs for any other Pod on the same node to verify that the GPU UUID is the same:
         
         kubectl logs POD2_NAME
         

The output is similar to the following:
         
         GPU 0: Tesla V100-SXM2-16GB (UUID: GPU-0771302b-eb3a-6756-7a23-0adcae8efd47)
         




## Use GPU time-sharing with multi-instance GPUs

As a platform administrator, you might want to combine multiple GKE GPU features. GPU time-sharing works with [multi-instance GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi), which partition a single physical GPU into up to seven slices. These partitions are isolated from each other. You can configure GPU time-sharing for each multi-instance GPU partition.

For example, if you set the `gpu-partition-size` to `1g.5gb`, the underlying GPU would be split into seven partitions. If you also set `max-shared-clients-per-gpu` to `3`, each partition would support up to three containers, for a total of up to 21 GPU time-sharing devices available to allocate in that physical GPU. To learn about how the `gpu-partition-size` converts to actual partitions, refer to [Multi-instance GPU partitions](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi#multi-instance_gpu_partitions).

To create a multi-instance GPU cluster with GPU time-sharing enabled, run the following command:

###  Autopilot 

With Autopilot, GPU time-sharing and multi-instance GPUs can be used together by using both sets of node selectors.
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: cuda-simple
    spec:
      replicas: 7
      selector:
        matchLabels:
          app: cuda-simple
      template:
        metadata:
          labels:
            app: cuda-simple
        spec:
          nodeSelector:
            cloud.google.com/gke-gpu-partition-size: 1g.5gb
            cloud.google.com/gke-gpu-sharing-strategy: time-sharing
            cloud.google.com/gke-max-shared-clients-per-gpu: "3"
            cloud.google.com/gke-accelerator: nvidia-tesla-a100
            cloud.google.com/gke-accelerator-count: "1"
          containers:
          - name: cuda-simple
            image: nvidia/cuda:11.0.3-base-ubi7
            command:
            - bash
            - -c
            - |
              /usr/local/nvidia/bin/nvidia-smi -L; sleep 300
            resources:
              limits:
                nvidia.com/gpu: 1
    

###  Standard 

With Standard, you need to create GPU time-shared, multi-instance cluster by running the following command:
    
    
    gcloud container node-pools create NODEPOOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --machine-type=MACHINE_TYPE \
        --accelerator=type=nvidia-tesla-a100,count=GPU_QUANTITY,gpu-partition-size=PARTITION_SIZE,gpu-sharing-strategy=time-sharing,max-shared-clients-per-gpu=CLIENTS_PER_GPU,gpu-driver-version=DRIVER_VERSION
    

Replace `PARTITION_SIZE` with the [multi-instance GPU partition size](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi#multi-instance_gpu_partitions) that you want, such as `1g.5gb`.

## Limitations

  * With GPU time-sharing, GKE enforces address space isolation, performance isolation, and error isolation between containers that share a physical GPU. However, memory limits aren't enforced on GPUs. To avoid running into out-of-memory (OOM) issues, set GPU memory limits in your workloads. To avoid security issues, only deploy workloads that are in the same trust boundary to GPU time-sharing.
  * To prevent unexpected behavior during capacity allocation, GKE might reject certain GPU time-sharing requests. For details, see [GPU requests for GPU time-sharing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/timesharing-gpus#request-limits).
  * The maximum number of containers that can use time-sharing in a single physical GPU is **48**. When planning your GPU time-sharing configuration, consider the resource needs of your workloads and the capacity of the underlying physical GPUs to optimize your performance and responsiveness.
  * You can't enable time-sharing for [G4 machine types](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) that have less than one GPU.



## What's next

  * Learn more about [GPU sharing strategies available in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/timesharing-gpus).
  * Learn more about [GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus).
  * Learn more about [Running multi-instance GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi).
  * For more information about compute preemption for the NVIDIA GPU, refer to the [NVIDIA Pascal Tuning Guide](https://docs.nvidia.com/cuda/pascal-tuning-guide/index.html#preemption).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
