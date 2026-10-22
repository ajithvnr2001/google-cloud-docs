---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nvidia-mps-gpus/
title: Share GPUs with multiple workloads using NVIDIA MPS \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:31.565172+00:00
---

# Share GPUs with multiple workloads using NVIDIA MPS  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nvidia-mps-gpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Share GPUs with multiple workloads using NVIDIA MPS Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to use CUDA [Multi-Process Service (MPS)](https://docs.nvidia.com/deploy/mps/index.html) to let multiple workloads share a single NVIDIA GPU hardware accelerator in your Google Kubernetes Engine (GKE) nodes.

## Overview

NVIDIA MPS is a GPU sharing solution that allows multiple containers to share a single physical NVIDIA GPU hardware attached to a node.

NVIDIA MPS relies on NVIDIA's Multi-Process Service on CUDA. NVIDIA MPS is an alternative, binary-compatible implementation of the CUDA API designed to transparently enable co-operative multi-process CUDA applications to run concurrently on a single GPU device.

With NVIDIA MPS, you can specify the maximum shared containers of a physical GPU. This value determines how much of the physical GPU power each container gets, in terms of the following characteristics:

  * [Pinned device memory limit](https://docs.nvidia.com/deploy/mps/index.html#topic_5_2_7).
  * [Active thread percentage](https://docs.nvidia.com/deploy/mps/index.html#topic_5_2_5).



To learn more about how GPUs are scheduled with NVIDIA MPS, and when you should use CUDA MPS, see [About GPU sharing solutions in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/timesharing-gpus).

## Who should use this guide

The instructions in this section apply to you if you are one of the following:

  * **Platform administrator** : Creates and manages a GKE cluster, plans infrastructure and resourcing requirements, and monitors the cluster's performance.
  * **Application developer** : Designs and deploys workloads on GKE clusters. If you want instructions for requesting NVIDIA MPS with GPUs, refer to Deploy workloads that use NVIDIA MPS with GPUs.



## Requirements

  * **GKE version** : You can enable GPU sharing with NVIDIA MPS on GKE Standard clusters running GKE version 1.27.7-gke.1088000 and later.
  * **GPU type** : You can enable NVIDIA MPS for all NVIDIA GPU types. However, you can't enable NVIDIA MPS for [G4 machine types](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) that have less than one GPU.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have sufficient [NVIDIA GPU](https://docs.cloud.google.com/compute/docs/gpus#nvidia_t4_gpus) quota. If you need more quota, refer to [Requesting an increase in quota](https://docs.cloud.google.com/compute/quotas#requesting_additional_quota).
  * Plan your GPU capacity based on the resource needs of the workloads and the capacity of the underlying GPU.
  * Review the limitations for the NVIDIA MPS with GPUs.



## Enable NVIDIA MPS with GPUs on GKE clusters

As a platform administrator, you must enable NVIDIA MPS with GPUs on a GKE Standard cluster. Then, application developers can deploy workloads to use the NVIDIA MPS with GPUs. To enable NVIDIA MPS with GPUs on GKE, do the following:

  1. Enable NVIDIA MPS with GPUs on a new GKE cluster.
  2. Install NVIDIA GPU device drivers (if required).
  3. Verify the GPU resources available on your nodes.



### Enable NVIDIA MPS with GPUs on a GKE cluster

You can enable NVIDIA MPS with GPUs when you create GKE Standard clusters. The default node pool in the cluster has the feature enabled. You still need to enable NVIDIA MPS with GPUs when you manually create new node pools in that cluster.

Create a cluster with NVIDIA MPS enabled using the Google Cloud CLI:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --cluster-version=CLUSTER_VERSION \
        --machine-type=MACHINE_TYPE \
        --accelerator=type=GPU_TYPE,count=GPU_QUANTITY,gpu-sharing-strategy=mps,max-shared-clients-per-gpu=CLIENTS_PER_GPU,gpu-driver-version=DRIVER_VERSION
    

Replace the following:

  * `CLUSTER_NAME`: the name of your new cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters. The GPU type that you use must be [available](https://docs.cloud.google.com/compute/docs/regions-zones#available) in the selected region.
  * `CLUSTER_VERSION`: the GKE version for the cluster control plane and nodes. Use GKE version 1.27.7-gke.1088000 or later. Alternatively, specify a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#current_versions) with that GKE version by using the `--release-channel=RELEASE_CHANNEL` flag.
  * `MACHINE_TYPE`: the Compute Engine machine type for your nodes. The compatible machine series varies by GPU type. For example, for A100 GPUs, use an [A2 machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-vms). To find more compatible machine series by GPU, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus).
  * `GPU_TYPE`: the GPU type, which must be an [NVIDIA GPU platform](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads) such as `nvidia-tesla-v100`.
  * `GPU_QUANTITY`: the number of physical GPUs to attach to each node in the default node pool.
  * `CLIENTS_PER_GPU`: the maximum number of containers that can share each physical GPU.
  * `DRIVER_VERSION`: the NVIDIA driver version to install. Can be one of the following: 
    * `default`: Install the default driver version for your GKE version.
    * `latest`: Install the latest available driver version for your GKE version. Available only for nodes that use Container-Optimized OS.
    * `disabled`: Skip automatic driver installation. You **must** manually install a driver after you create the node pool. If you omit `gpu-driver-version`, this is the default option.



### Enable NVIDIA MPS with GPUs on a new node pool

You can enable NVIDIA MPS with GPUs when you manually create new node pools in a GKE cluster. Create a node pool with NVIDIA MPS enabled using the Google Cloud CLI:
    
    
    gcloud container node-pools create NODEPOOL_NAME \
        --cluster=CLUSTER_NAME \
        --machine-type=MACHINE_TYPE \
        --location=CONTROL_PLANE_LOCATION \
        --accelerator=type=GPU_TYPE,count=GPU_QUANTITY,gpu-sharing-strategy=mps,max-shared-clients-per-gpu=CONTAINER_PER_GPU,gpu-driver-version=DRIVER_VERSION
    

Replace the following:

  * `NODEPOOL_NAME`: the name of your new node pool.
  * `CLUSTER_NAME`: the name of your cluster, which must run GKE version 1.27.7-gke.1088000 or later.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * `MACHINE_TYPE`: the Compute Engine machine type for your nodes. The compatible machine series varies by GPU type. For example, for A100 GPUs, use an [A2 machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-vms).For L4 GPUs, use a [G2 machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-vms). To find more compatible machine series by GPU, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus).
  * `GPU_TYPE`: the GPU type, which must be an [NVIDIA GPU platform](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads) such as `nvidia-tesla-v100`.
  * `GPU_QUANTITY`: the number of physical GPUs to attach to each node in the node pool.
  * `CONTAINER_PER_GPU`: the maximum number of containers that can share each physical GPU.
  * `DRIVER_VERSION`: the NVIDIA driver version to install. Can be one of the following:

    * `default`: Install the default driver version for your GKE version.
    * `latest`: Install the latest available driver version for your GKE version. Available only for nodes that use Container-Optimized OS.
    * `disabled`: Skip automatic driver installation. You **must** manually install a driver after you create the node pool. If you omit `gpu-driver-version`, this is the default option.
**Note:** The `gpu-driver-version` option is only available for GKE version 1.27.2-gke.1200 and later. In earlier versions, omit this flag and manually install a driver after you create the node pool.



### Install NVIDIA GPU device drivers

If you chose to disable automatic driver installation when creating the cluster, or if you use a GKE version earlier than 1.27.2-gke.1200, you must manually install a compatible NVIDIA driver to manage the NVIDIA MPS division of the physical GPUs. To install the drivers, you deploy a GKE installation DaemonSet that sets the drivers up.

For instructions, refer to [Installing NVIDIA GPU device drivers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#installing_drivers).

## Verify the GPU resources available

You can verify that the number of GPUs in your nodes matches the number you specified when you enabled NVIDIA MPS. You can also verify that the NVIDIA MPS control daemon is running.

### Verify the GPU resources available on your nodes

To verify the GPU resources available on your nodes, run the following command:
    
    
    kubectl describe nodes NODE_NAME
    

Replace NODE_NAME with the name of your node.

The output is similar to the following:
    
    
    ...
    Capacity:
      ...
      nvidia.com/gpu:             3
    Allocatable:
      ...
      nvidia.com/gpu:             3
    

In this output, the number of GPU resources on the node is `3` because of the following values:

  * The value in `max-shared-clients-per-gpu` is `3`.
  * The `count` of physical GPUs to attach to the node is `1`. If the `count` of physical GPUs was `2`, the output would show `6` allocatable GPU resources, three on each physical GPU.



### Verify that the MPS control daemon is running

The GPU device plugin performs a health check on the MPS control daemon. When the MPS control daemon is healthy, you can deploy a container.

To verify the NVIDIA MPS status, run the following command:
    
    
    kubectl logs -l k8s-app=nvidia-gpu-device-plugin -n kube-system \
          -c nvidia-gpu-device-plugin --tail=100 | grep MPS
    

The output is similar to the following:
    
    
    I1118 08:08:41.732875       1 nvidia_gpu.go:75] device-plugin started
    ...
    I1110 18:57:54.224832       1 manager.go:285] MPS is healthy, active thread percentage = 100.0
    ...
    

In the output, you might see that the following events happened:

  * The `failed to start GPU device manager` error is preceding the `MPS is healthy` error. This error is transient. If you see the `MPS is healthy` message, then the control daemon is running.
  * The `active thread percentage = 100.0` message means that the whole physical GPU resource has a completely active thread.



## Deploy workloads that use MPS

As an application operator who is deploying GPU workloads, you can tell GKE to share MPS sharing units in the same physical GPU. In the following manifest, you request one physical GPU and set `max-shared-clients-per-gpu=3`. The physical GPU gets three MPS sharing units, and starts a `nvidia/samples:nbody` Job with three Pods (containers) running parallel.

  1. Save the manifest as `gpu-mps.yaml`:
         
         apiVersion: batch/v1
           kind: Job
           metadata:
             name: nbody-sample
           spec:
             # Specifies the desired number of successfully finished Pods.
             completions: 3
             # Specifies the maximum desired number of Pods that should run at any given time.
             parallelism: 3
             template:
               spec:
                 # Allows the Pod to share the host's IPC namespace.
                 # The following field is required for containers to communicate with the MPS control daemon.
                 hostIPC: true
                 # Selects a node with the 'mps' GPU sharing strategy.
                 nodeSelector:
                   cloud.google.com/gke-gpu-sharing-strategy: mps
                 containers:
                   - name: nbody-sample
                     # A sample CUDA application from NVIDIA.
                     image: nvidia/samples:nbody
                     # The command to run in the container.
                     command: ["/tmp/nbody"]
                     # Arguments for the command. Runs the nbody simulation in benchmark mode.
                     args: ["-benchmark", "-i=5000"]
                     resources:
                       limits:
                         # Requests one MPS sharing unit from a physical GPU.
                         nvidia.com/gpu: 1
                 restartPolicy: "Never"
             backoffLimit: 1
         

In this manifest:

     * `hostIPC: true` enables Pods to talk to the MPS control daemon. It is required. However, consider that the `hostIPC: true` configuration allows container to access the host resource which introduce security risks.
     * 5,000 iterations run in benchmark mode.
  2. Apply the manifest:
         
         kubectl apply -f gpu-mps.yaml
         

  3. Verify that all Pods are running:
         
         kubectl get pods
         

The output is similar to the following:
         
         NAME                           READY   STATUS    RESTARTS   AGE
         nbody-sample-6948ff4484-54p6q   1/1     Running   0          2m6s
         nbody-sample-6948ff4484-5qs6n   1/1     Running   0          2m6s
         nbody-sample-6948ff4484-5zpdc   1/1     Running   0          2m5s
         

  4. Check the logs from Pods to verify the Job completed:
         
         kubectl logs -l job-name=nbody-sample -f
         

The output is similar to the following:
         
         ...
         > Compute 8.9 CUDA device: [NVIDIA L4]
         18432 bodies, total time for 5000 iterations: 9907.976 ms
         = 171.447 billion interactions per second
         = 3428.941 single-precision GFLOP/s at 20 flops per interaction
         ...
         

Because GKE runs 5,000 iterations, the log might take several minutes.




## Clean up

Delete the Jobs and all of its Pods by running the following command:
    
    
    kubectl delete job --all
    

## Limit pinned device memory and active thread with NVIDIA MPS

By default, when using GPU with NVIDIA MPS on GKE, the following CUDA environment variables are injected into the GPU workload:

  * `CUDA_MPS_ACTIVE_THREAD_PERCENTAGE`: This variable indicates the percentage of available threads that each MPS sharing unit can use. By default, each MPS sharing unit of the GPU is set to `100 / MaxSharedClientsPerGPU` to get an equal slice of the GPU compute in terms of stream multiprocessor.
  * `CUDA_MPS_PINNED_DEVICE_MEM_LIMIT`: This variable limits the amount of GPU memory that can be allocated by a MPS sharing unit of GPU. By default, each MPS sharing unit of the GPU is set to `total mem / MaxSharedClientsPerGPU` to get an equal slice of the GPU memory.

**Note:** `CUDA_MPS_PINNED_DEVICE_MEM_LIMIT` is only valid starting in version [CUDA 11.5](https://developer.nvidia.com/blog/revealing-new-features-in-the-cuda-11-5-toolkit/). Images built with earlier CUDA versions don't support the `CUDA_MPS_PINNED_DEVICE_MEM_LIMIT` variable.



To set resource limit for your GPU workloads, configure these NVIDIA MPS environment variables:

  1. Review and build the image of the [`cuda-mps` example in GitHub](https://github.com/GoogleCloudPlatform/container-engine-accelerators/tree/master/example/cuda-mps).

  2. Save the following manifest as `cuda-mem-and-sm-count.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: cuda-mem-and-sm-count
         spec:
           # Allows the Pod to share the host's IPC namespace.
           # The following field is required for containers to communicate with the MPS control daemon.
           hostIPC: true
           # Selects a node with the 'mps' GPU sharing strategy.
           nodeSelector:
             cloud.google.com/gke-gpu-sharing-strategy: mps
           containers:
             - name: cuda-mem-and-sm-count
               # The custom image built from the cuda-mps example.
               image: CUDA_MPS_IMAGE
               # Grants the container extended privileges on the host machine.
               securityContext:
                 privileged: true
               resources:
                 limits:
                   # Requests one MPS sharing unit from a physical GPU.
                   nvidia.com/gpu: 1
         

Replace the `CUDA_MPS_IMAGE` with the name of the image that you built for the `cuda-mps` example.

NVIDIA MPS requires that you set `hostIPC:true` on Pods. The `hostIPC:true` configuration allows container to access the host resource which introduces security risks.

  3. Apply the manifest:
         
         kubectl apply -f cuda-mem-and-sm-count.yaml
         

  4. Check the logs for this Pod:
         
         kubectl logs cuda-mem-and-sm-count
         

In an example which uses NVIDIA Tesla [L4](https://www.nvidia.com/en-us/data-center/l4/) with `gpu-sharing-strategy=mps` and `max-shared-clients-per-gpu=3`, the output is similar as the following:
         
         For device 0:  Free memory: 7607 M, Total memory: 22491 M
         For device 0:  multiProcessorCount: 18
         

In this example, the NVIDIA Tesla [L4](https://www.nvidia.com/en-us/data-center/l4/) GPU has 60 SM count and 24 GB memory. Each MPS sharing unit roughly gets 33% active thread and 8 GB memory.

**Note:** the number of multi processors count may not match exactly the `CUDA_MPS_ACTIVE_THREAD_PERCENTAGE` as the driver needs to round down the number of [streaming multiprocessor](https://docs.nvidia.com/cuda/ampere-tuning-guide/index.html#streaming-multiprocessor). CUDA fractionalizes compute on a GPC (Graphics Processing Cluster) boundary, not streaming multiprocessor boundary.
  5. Update the manifest to request 2 `nvidia.com/gpu`:
         
         resources:
                 limits:
                   nvidia.com/gpu: 2
         

The output is similar to the following:
         
         For device 0:  Free memory: 15230 M, Total memory: 22491 M
         For device 0:  multiProcessorCount: 38
         

  6. Update the manifest to override the `CUDA_MPS_ACTIVE_THREAD_PERCENTAGE` and `CUDA_MPS_PINNED_DEVICE_MEM_LIMIT` variables:
         
         env:
             - name: CUDA_MPS_ACTIVE_THREAD_PERCENTAGE
               value: "20"
             - name: CUDA_MPS_PINNED_DEVICE_MEM_LIMIT
               value: "0=8000M"
         

The output is similar to the following:
         
         For device 0:  Free memory: 7952 M, Total memory: 22491 M
         For device 0:  multiProcessorCount: 10
         




## Limitations

  * MPS on pre-Volta GPUs like the NVIDIA P100 (approaching [end of support](https://docs.cloud.google.com/compute/docs/eol/p100-eos)) has [limited capabilities](https://docs.nvidia.com/deploy/mps/#topic_2_1_2) compared with GPU types in and after [Volta](https://www.nvidia.com/en-us/data-center/volta-gpu-architecture/).
  * With NVIDIA MPS, GKE helps ensure that each container gets limited pinned device memory and active thread. However, other resources like memory bandwidth, encoders or decoders are not captured as part of these resource limits. As a result, containers might negatively affect the performance of other containers if they are all requesting the same unlimited resource.
  * NVIDIA MPS has memory protection and error containment [limitations](https://docs.nvidia.com/deploy/mps/#topic_3_3_3). We recommend that you evaluate this limitations to ensure compatibility with your workloads.
  * NVIDIA MPS requires that you set `hostIPC:true` on Pods. The `hostIPC:true` configuration allows container to access the host resource which introduces security risks.
  * GKE might reject certain GPU requests when using NVIDIA MPS, to prevent unexpected behavior during capacity allocation.
  * The maximum number of containers that can share a single physical GPU with NVIDIA MPS is **48** (pre-Volta GPU only supports **16**). When planning your NVIDIA MPS configuration, consider the resource needs of your workloads and the capacity of the underlying physical GPUs to optimize performance and responsiveness.
  * You can't enable NVIDIA MPS for [G4 machine types](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) that have less than one GPU.



## What's next

  * For more information about the GPU sharing strategies available in GKE, see [About GPU sharing strategies in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/timesharing-gpus)
  * For more information about Multi-Process Service (MPS), refer to the [NVIDIA documentation](https://docs.nvidia.com/deploy/mps/index.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
