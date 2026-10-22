---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi/
title: Running multi-instance GPUs \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:28.872068+00:00
---

# Running multi-instance GPUs  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Running multi-instance GPUs Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page provides instructions on how to increase utilization and reduce costs by running multi-instance GPUs. With this configuration, you partition an NVIDIA GB200, B200, H200, H100, A100, or RTX PRO 6000 graphics processing unit (GPU) to share a single GPU across multiple containers on Google Kubernetes Engine (GKE).

Before reading this page, ensure that you're familiar with Kubernetes concepts such as [Pods](https://kubernetes.io/docs/concepts/workloads/pods/), [nodes](https://kubernetes.io/docs/concepts/architecture/nodes/), [deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/), and [namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) and are familiar with GKE concepts such as [node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools), [autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler), and [auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning).

## Introduction

Kubernetes allocates one full GPU per container even if the container only needs a fraction of the GPU for its workload, which might lead to wasted resources and cost overrun, especially if you are using the latest generation of powerful GPUs. To improve GPU utilization, multi-instance GPUs allow you to partition a single supported GPU in up to seven slices. Each slice can be allocated to one container on the node independently, for a maximum of seven containers per GPU. Multi-instance GPUs provide hardware isolation between the workloads, and consistent and predictable QoS for all containers running on the GPU.

For [CUDA](https://developer.nvidia.com/cuda-zone)® applications, multi-instance GPUs are largely transparent. Each GPU partition appears as a regular GPU resource, and the programming model remains unchanged.

For more information on multi-instance GPUs, refer to the [NVIDIA multi-instance GPU user guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html).

### Supported GPUs

The following GPU types support multi-instance GPUs:

  * NVIDIA GB200 (1.33.0-gke.1636000 and later)
  * NVIDIA B200 (180 GB) (1.32.2-gke.1586000 and later)
  * NVIDIA H200 (141GB)
  * NVIDIA H100 (80GB)
  * NVIDIA A100 (80GB)
  * NVIDIA A100 (40GB)
  * NVIDIA RTX PRO 6000 
    * For partitions without suffixes: 1.34.0-gke.1662000 and later
    * For partitions with suffixes: 
      * **1.35 or later** : 1.35.3-gke.1389000 or later
      * **1.34** : 1.34.6-gke.1154000 or later

**Note:** If you split NVIDIA GB200, B200, H200, or H100 GPUs with multi-instance GPUs, you can't use GPUDirect technologies (including TCPX, TCPXO, and RDMA).

### Multi-instance GPU partitions

The GB200, B200, H200, H100, and A100 GPU each consist of seven compute units and eight memory units, which you can partition into GPU instances of varying sizes. To configure GPU partition sizes, use the following syntax: `[compute]g.[memory]gb`. For example, a GPU partition size of `1g.5gb` refers to a GPU instance with one compute unit (1/7th of streaming multiprocessors on the GPU), and one memory unit (5 GB). The partition size for the GPUs can be specified when you deploy an Autopilot workload or when you create a Standard cluster.

For the NVIDIA RTX PRO 6000, GKE supports MIG profiles which are specified in the table with the listed suffixes. For more information, see [RTX PRO 6000 Blackwell MIG Profiles](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/supported-mig-profiles.html#rtx-pro-6000-blackwell-mig-profiles).

The [partitioning table](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#partitioning) in the NVIDIA multi-instance GPU user guide lists all the different GPU partition sizes, along with the amount of compute and memory resources available on each GPU partition. The table also shows the number of GPU instances for each partition size that can be created on the GPU.

The following table lists the partition sizes that GKE supports:

Partition size | GPU instances  
---|---  
GPU: NVIDIA GB200 (`nvidia-gb200`)  
`1g.23gb` | 7  
`1g.47gb` | 4  
`2g.47gb` | 3  
`3g.93gb` | 2  
`4g.93gb` | 1  
`7g.186gb` | 1  
GPU: NVIDIA B200 (`nvidia-b200`)  
`1g.23gb` | 7  
`1g.45gb` | 4  
`2g.45gb` | 3  
`3g.90gb` | 2  
`4g.90gb` | 1  
`7g.180gb` | 1  
GPU: NVIDIA H200 (141GB) (`nvidia-h200-141gb`)  
`1g.18gb` | 7  
`1g.35gb` | 4  
`2g.35gb` | 3  
`3g.71gb` | 2  
`4g.71gb` | 1  
`7g.141gb` | 1  
GPU: NVIDIA H100 (80GB) (`nvidia-h100-80gb` and `nvidia-h100-mega-80gb`)  
`1g.10gb` | 7  
`1g.20gb` | 4  
`2g.20gb` | 3  
`3g.40gb` | 2  
`7g.80gb` | 1  
GPU: NVIDIA A100 (80GB) (`nvidia-a100-80gb`)  
`1g.10gb` | 7  
`2g.20gb` | 3  
`3g.40gb` | 2  
`7g.80gb` | 1  
GPU: NVIDIA A100 (40GB) (`nvidia-tesla-a100`)  
`1g.5gb` | 7  
`2g.10gb` | 3  
`3g.20gb` | 2  
`7g.40gb` | 1  
GPU: NVIDIA RTX PRO 6000 (`nvidia-rtx-pro-6000`)  
`1g.24gb` | 4  
`1g.24gb.me` | 1  
`1g.24gb.gfx` | 4  
`1g.24gb.me.all` | 1  
`1g.24gb-me` | 4  
`2g.48gb` | 2  
`2g.48gb.gfx` | 2  
`2g.48gb.me.all` | 1  
`2g.48gb-me` | 2  
`4g.96gb` | 1  
`4g.96gb.gfx` | 1  
  
Each GPU on each node within a node pool is partitioned the same way. For example, consider a node pool with two nodes, four GPUs on each node, and a partition size of `1g.5gb`. GKE creates seven partitions of size `1g.5gb` on each GPU. Since there are four GPUs on each node, there are 28 `1g.5gb` GPU partitions available on each node. Since there are two nodes in the node pool, a total of 56 `1g.5gb` GPU partitions are available in the entire node pool.

To create a GKE Standard cluster with more than one type of GPU partition, you must create multiple node pools. For example, if you want nodes with `1g.5gb` and `3g.20gb` GPU partitions in a cluster, you must create two node pools: one with the GPU partition size set to `1g.5gb`, and the other with `3g.20gb`.

A GKE Autopilot cluster automatically creates nodes with the correct partition configuration when you create workloads that require different partition sizes.

Each node is labeled with the size of GPU partitions that are available on the node. This labeling allows workloads to target nodes with the needed GPU partition size. For example, on a node with `1g.5gb` GPU instances, the node is labeled as:
    
    
    cloud.google.com/gke-gpu-partition-size=1g.5gb
    

### How it works

To use multi-instance GPUs, you perform the following tasks:

  1. Create a cluster with multi-instance GPUs enabled.
  2. Manually install drivers.
  3. Verify how many GPU resources are on the node.
  4. Deploy containers using multi-instance GPUs.



## Pricing

Multi-instance GPUs are exclusive to GB200, B200, H200, H100, A100, and RTX PRO 6000 GPUs, and are subject to the corresponding GPU pricing in addition to any other products used to run your workloads. You can only attach whole GPUs to nodes in your cluster for partitioning. For GPU pricing information, refer to the [GPUs pricing](https://cloud.google.com/compute/gpus-pricing) page.

## Limitations

  * Using multi-instance GPU partitions with GKE is not recommended for untrusted workloads.
  * Autoscaling and auto-provisioning GPU partitions are fully supported on GKE version 1.20.7-gke.400 or later. In earlier versions only node pools with at least one node can be auto-scaled based on demand for specific GPU partition sizes from workloads.
  * GPU utilization metrics (for example, `duty_cycle`) are not available for multi-instance GPUs.
  * Multi-instance splits a physical GPU into discrete instances, each of which is isolated from the others at the hardware level. A container that uses a multi-instance GPU instance can only access the CPU and memory resources available to that instance.
  * A pod can only consume up to one multi-instance GPU instance.
  * You can't run multi-instance GPUs with [G4 machine types](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) that have less than one GPU.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * You must have sufficient NVIDIA A100 GPU quota. See [Requesting an increase in quota](https://docs.cloud.google.com/compute/quotas#requesting_additional_quota).
  * If you want to use multi-instance GPUs with Autopilot, you can learn more about using GPUs with Autopilot at [Deploy GPU workloads in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus).



## Create a cluster with multi-instance GPUs enabled

If you use GKE Standard, you must enable multi-instance GPUs in the cluster. Autopilot clusters enable multi-instance GPUs by default. To use multi-instance GPUs in Autopilot, see the Deploy containers using multi-instance GPU section of this page.

When you create a Standard cluster with multi-instance GPUs, you must specify `gpuPartitionSize` along with `acceleratorType` and `acceleratorCount`. The `acceleratorType` must be one of the following:

  * `nvidia-gb200`
  * `nvidia-b200`
  * `nvidia-h200-141gb`
  * `nvidia-h100-80gb`
  * `nvidia-a100-80gb`
  * `nvidia-tesla-a100`
  * `nvidia-rtx-pro-6000`



The following example shows how to create a GKE cluster with one node, and seven GPU partitions of size `1g.5gb` on the node. The other steps in this page use a GPU partition size of `1g.5gb`, which creates seven partitions on each GPU. You can also use any of the supported GPU partition sizes mentioned earlier.

You can use the Google Cloud CLI or Terraform.

###  gcloud 

Create a cluster with multi-instance GPUs enabled:
    
    
    gcloud container clusters create CLUSTER_NAME  \
        --project=PROJECT_ID  \
        --location CONTROL_PLANE_LOCATION  \
        --cluster-version=CLUSTER_VERSION  \
        --accelerator type=nvidia-tesla-a100,count=1,gpu-partition-size=1g.5gb,gpu-driver-version=DRIVER_VERSION  \
        --machine-type=a2-highgpu-1g  \
        --num-nodes=1
    

Replace the following:

  * `CLUSTER_NAME`: the name of your new cluster.
  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * `CLUSTER_VERSION`: the version must be `1.19.7-gke.2503` or later.
  * `DRIVER_VERSION`: the NVIDIA driver version to install. Can be one of the following: 
    * `default`: Install the default driver version for your GKE version.
    * `latest`: Install the latest available driver version for your GKE version. Available only for nodes that use Container-Optimized OS.
    * `disabled`: Skip automatic driver installation. You **must** manually install a driver after you create the cluster. If you omit `gpu-driver-version`, this is the default option.



###  Terraform 

To create a cluster with multi-instance GPUs enabled using Terraform, refer to the following example:
    
    
    resource "google_container_cluster" "default" {
      name               = "gke-standard-zonal-gpu"
      location           = "us-central1-a"
      initial_node_count = 1
    
      node_config {
        guest_accelerator {
          type               = "nvidia-tesla-a100"
          count              = 1
          gpu_partition_size = "1g.5gb"
          gpu_driver_installation_config {
            gpu_driver_version = "LATEST"
          }
        }
        machine_type = "a2-highgpu-1g"
      }
    }

To learn more about using Terraform, see [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

## Connect to the cluster

Configure `kubectl` to connect to the newly created cluster:
    
    
    gcloud container clusters get-credentials CLUSTER_NAME
    

### Install drivers

If you chose to disable automatic driver installation when creating the cluster, or if you're running a GKE version earlier than 1.27.2-gke.1200, you must [manually install a compatible NVIDIA driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#installing_drivers) after creation completes. Multi-instance GPUs require an NVIDIA driver version 450.80.02 or later.

After the driver is installed, multi-instance GPU mode is enabled. If you automatically installed drivers, your nodes reboot when the GPU device plugin starts to create GPU partitions. If you manually installed drivers, your nodes reboot when driver installation completes. The reboot might take a few minutes to complete.

### Verify how many GPU resources are on the node

Run the following command to verify that the capacity and allocatable count of `nvidia.com/gpu` resources is 7:
    
    
    kubectl describe nodes
    

Here's the output from the command:
    
    
    ...
    Capacity:
      ...
      nvidia.com/gpu:             7
    Allocatable:
      ...
      nvidia.com/gpu:             7
    

## Deploy containers using multi-instance GPU

You can deploy up to one container per multi-instance GPU device on the node. In this example, with a partition size of `1g.5gb`, there are seven multi-instance GPU partitions available on the node. As a result, you can deploy up to seven containers that request GPUs on this node.

**Caution:** If your GKE nodes include both multi-instance GPU nodes and non-multi-instance GPU nodes, use [node anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity) on your Pods that don't need multi-instance GPUs. Node anti-affinity helps ensure that these Pods don't accidentally land on nodes that have multi-instance GPUs.

Here's an example that starts the `cuda:11.0.3-base-ubi7` container and runs `nvidia-smi` to print the UUID of the GPU within the container. In this example, there are seven containers, and each container receives one GPU partition. This example also sets the `cloud.google.com/gke-gpu-partition-size` node selector to target nodes with `1g.5gb` GPU partitions.

  1. Save the following sample manifest as `cuda-simple.yaml`:

### Autopilot
         
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
               

This manifest does the following: 

     * Requests the `nvidia-tesla-a100` GPU type by setting the `cloud.google.com/gke-accelerator` node selector.
     * Splits the GPU into the `1g.5gb` partition size.
     * Attaches a single GPU to the node by setting the `cloud.google.com/gke-accelerator-count` node selector.

### Standard
    
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
          

This manifest does the following:

     * Requests a single GPU with partition size `1g.5gb`.
  2. Apply the sample manifest to your cluster:
         
         kubectl apply -f cuda-simple.yaml
         

  3. Verify that all seven Pods are running:
         
         kubectl get pods
         

Here's the output from the command:
         
         NAME                           READY   STATUS    RESTARTS   AGE
         cuda-simple-849c47f6f6-4twr2   1/1     Running   0          7s
         cuda-simple-849c47f6f6-8cjrb   1/1     Running   0          7s
         cuda-simple-849c47f6f6-cfp2s   1/1     Running   0          7s
         cuda-simple-849c47f6f6-dts6g   1/1     Running   0          7s
         cuda-simple-849c47f6f6-fk2bs   1/1     Running   0          7s
         cuda-simple-849c47f6f6-kcv52   1/1     Running   0          7s
         cuda-simple-849c47f6f6-pjljc   1/1     Running   0          7s
         

  4. View the logs to see the GPU UUID, using the name of any Pod from the previous command:
         
         kubectl logs cuda-simple-849c47f6f6-4twr2
         

Here's the output from the command:
         
         GPU 0: A100-SXM4-40GB (UUID: GPU-45eafa61-be49-c331-f8a2-282736687ab1)
           MIG 1g.5gb Device 0: (UUID: MIG-GPU-45eafa61-be49-c331-f8a2-282736687ab1/11/0)
         




## What's next

  * Learn more about [GPUs](https://docs.cloud.google.com/compute/docs/gpus).
  * Learn how to [configure time-sharing on GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/timesharing-gpus).
  * Learn more about [cluster multi-tenancy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multitenancy-overview).
  * Learn more about [best practices for enterprise multi-tenancy](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/enterprise-multitenancy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
