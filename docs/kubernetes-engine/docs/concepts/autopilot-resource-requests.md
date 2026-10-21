---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests/
title: Resource requests in Autopilot \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:08.215672+00:00
---

# Resource requests in Autopilot  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Resource requests in Autopilot Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

To improve workload stability, Google Kubernetes Engine (GKE) Autopilot mode manages the values of Pod resource requests, such as CPU, memory, or ephemeral storage. This page includes the following information, which you can use to plan efficient, stable, and cost-effective workloads:

  * Default values that Autopilot applies to Pods that don't specify values.
  * Minimum and maximum values that Autopilot enforces for resource requests.
  * How the default, minimum, and maximum values vary based on the hardware that your Pods request.



This page is for Operators and Developers who provision and configure cloud resources, and deploy workloads. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

You should already be familiar with [Kubernetes resource management](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/).

## Overview of resource requests in Autopilot

Autopilot uses the resource requests that you specify in your workload configuration to configure the nodes that run your workloads. Autopilot enforces minimum and maximum resource requests based on the compute class or the hardware configuration that your workloads use. If you don't specify requests for some containers, Autopilot assigns default values to let those containers run correctly.

When you deploy a workload in an Autopilot cluster, GKE validates the workload configuration against the allowed minimum and maximum values for the selected [compute class](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-compute-classes) or hardware configuration (such as [GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus)). If your requests are less than the minimum, Autopilot automatically modifies your workload configuration to bring your requests within the allowed range. If your requests are greater than the maximum, Autopilot rejects your workload and displays an error message.

The following list summarizes the categories of resource requests:

  * Default resource requests: Autopilot adds these if you don't specify your own requests for workloads
  * Minimum and maximum resource requests: Autopilot validates your specified requests to ensure that they're within these limits. If your requests are outside the limits, Autopilot modifies your workload requests.
  * Workload separation and extended duration requests: Autopilot has different default values and different minimum values for workloads that you separate from each other, or for Pods that get extended protection from GKE-initiated eviction.
  * Resource requests for DaemonSets: Autopilot has different default, minimum, and maximum values for containers in DaemonSets.



### How to request resources

In Autopilot, you request resources in your Pod specification. The supported minimum and maximum resources that you can request change based on the hardware configuration of the node on which the Pods run. To learn how to request specific hardware configurations, refer to the following pages:

  * [Choose compute classes for Autopilot Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-compute-classes)
  * [Deploy GPU workloads in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus)



## Default resource requests

If you don't specify resource requests for some containers in a Pod, Autopilot applies default values. These defaults are suitable for many smaller workloads.

**Note:** We recommend that you explicitly set your resource requests for each container to meet your application requirements, as these default values might not be sufficient, or optimal.

Additionally, Autopilot applies the following default resource requests regardless of the selected compute class or hardware configuration:

  * Containers in DaemonSets

    * CPU: 50 mCPU
    * Memory: 100 MiB
    * Ephemeral storage: 100 MiB
  * All other containers

    * Ephemeral storage: 1 GiB



For more information about Autopilot cluster limits, see [Quotas and limits](https://docs.cloud.google.com/kubernetes-engine/quotas#limits_per_cluster).

### Default requests for compute classes

Autopilot applies the following default values to resources that are not defined in the Pod specification for Pods that run on [compute classes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-compute-classes). If you only set one of the requests and leave the other blank, GKE uses the CPU:memory ratio defined in the Minimum and maximum requests section to set the missing request to a value that complies with the ratio.

Autopilot doesn't enforce default requests for GPU Pods and Pods that use the `Performance` ComputeClass.

General-purposeBalancedScale-OutClear all

Compute class | Resource | Default request  
---|---|---  
General-purpose (the default `autopilot`, or `autopilot-arm`) | CPU | 0.5 vCPU  
Memory | 2 GiB  
Balanced | CPU | 0.5 vCPU  
Memory | 2 GiB  
Scale-Out | CPU | 0.5 vCPU  
Memory | 2 GiB  
  
## Minimum and maximum resource requests

The total resources requested by your deployment configuration should be within the supported minimum and maximum values that Autopilot allows. The following conditions apply:

  * **Per-node minimum request** : when you use the [Pod-based billing model](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters#pricing) to run workloads in Autopilot mode in Standard clusters, and the sum of resource requests of [billable Pods](https://docs.cloud.google.com/kubernetes-engine/pricing#general-purpose-autopilot-workloads) on a node is less than the minimum request that would apply to a single Pod, GKE adds a charge for that minimum request.

Because of how Autopilot modifies your Pod resource requests, the sum of the billable Pod requests on a node almost always meets or exceeds this per-node minimum request.

  * **Ephemeral storage requests** :

    * Ephemeral storage uses the VM boot disk unless your nodes have local SSDs attached.

Compute hardware that includes local SSDs like A100 (80GB) GPUs, H100 (80GB) GPUs, the Z3 machine series, or the Z4D machine series support a maximum request that's equal to the size of the local SSD minus any system overhead. For information about this system overhead, see [Ephemeral storage backed by local SSDs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-node-sizes#ephemeral_storage_backed_by_local_ssds).

    * In GKE version 1.29.3-gke.1038000 and later, Performance class Pods and hardware accelerator Pods support a maximum ephemeral storage request of 56 TiB unless the hardware includes local SSDs.

In all other Autopilot Pods regardless of the GKE version, the total ephemeral storage request across all of the containers in the Pod must be between 10 MiB and 10 GiB unless otherwise specified.

    * For larger volumes, use [generic ephemeral volumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/generic-ephemeral-volumes), which provide equivalent functionality and performance to ephemeral storage but with significantly more flexibility as they can be used with any GKE storage option. For example, the maximum size for a generic ephemeral volume using `pd-balanced` is 64 TiB.

  * For DaemonSet Pods, the minimum resource requests are as follows:

    * **Clusters that support bursting** : 1 mCPU per Pod, 2 MiB of memory per Pod, and 10 MiB of ephemeral storage per container in the Pod.
    * **Clusters that don't support bursting** : 10 mCPU per Pod, 10 MiB of memory per Pod, and 10 MiB of ephemeral storage per container in the Pod.

To check whether your cluster supports bursting, see [Bursting availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-bursting-gke#availability-in-gke).

  * If your cluster supports bursting, Autopilot doesn't enforce 0.25 vCPU increments for your Pod CPU requests. If your cluster doesn't support bursting, Autopilot rounds up your CPU requests to the nearest 0.25 vCPU. To check whether your cluster supports bursting, see [Bursting availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-bursting-gke#availability-in-gke).

  * The CPU:memory ratio must be within the allowed range for the selected compute class or hardware configuration. If your CPU:memory ratio is outside the allowed range, Autopilot automatically increases the smaller resource. For example, if you request 1 vCPU and 16 GiB of memory (1:16 ratio) for Pods running on the `Scale-Out` class, Autopilot increases the CPU request to 4 vCPUs, which changes the ratio to 1:4.




### Minimums and maximums for compute classes

The following table describes the minimum, maximum, and allowed CPU-to-memory ratio for each compute class that Autopilot supports:

General-purposeBalancedPerformanceScale-OutClear all

Compute class | CPU:memory ratio (vCPU:GiB) | Resource | Minimum | Maximum  
---|---|---|---|---  
General-purpose (the default `autopilot`, or `autopilot-arm`) | Between 1:1 and 1:6.5 | CPU | The value depends on whether your cluster supports bursting, as follows:

  * **Clusters that support bursting** : 50m CPU
  * **Clusters that don't support bursting** : 250m CPU

To check whether your cluster supports bursting, see [Bursting availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-bursting-gke#availability-in-gke). | 30 vCPU  
Memory | The value depends on whether your cluster supports bursting, as follows:

  * **Clusters that support bursting** : 52 MiB
  * **Clusters that don't support bursting** : 512 MiB

To check whether your cluster supports bursting, see [Bursting availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-bursting-gke#availability-in-gke). | 110 GiB  
Balanced | Between 1:1 and 1:8 | CPU | 0.25 vCPU | 222 vCPU If [minimum CPU platform](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/min-cpu-platform) selected:

  * Intel platforms: 126 vCPU
  * AMD platforms: 222 vCPU

  
Memory | 0.5 GiB | 851 GiB If [minimum CPU platform](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/min-cpu-platform) selected:

  * Intel platforms: 823 GiB
  * AMD platforms: 851 GiB

  
Performance | N/A | CPU | No minimum requests enforced | 

  * C2 machine series: 58 vCPU
  * C2D machine series: 110 vCPU
  * C3 machine series: 174 vCPU
  * C3 machine series with Local SSD: 174 vCPU
  * C3D machine series: 358 vCPU
  * C3D machine series with Local SSD: 358 vCPU
  * C4A machine series (see [requirements and limitations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke#arm-requirements-limitations)): 70 vCPU
  * C4D machine series (1.32.9-gke.1711000 or later): 382 vCPU
  * C4D machine series with Local SSD (1.32.9-gke.1711000 or later): 382 vCPU
  * C4N machine series (1.36.0-gke.3009002 or later): 192 vCPU
  * H3 machine series: 86 vCPU
  * H4D machine series (1.33.2-gke.4731000 or later): 192 vCPU
  * T2A machine series: 46 vCPU
  * T2D machine series: 58 vCPU
  * C4 machine series: 286 vCPU
  * M4 machine series (1.33.4-gke.1013000 or later): 224 vCPU
  * N4 machine series: 78 vCPU
  * N4A machine series (1.34.1-gke.3403001 or later): 64 vCPU
  * N4D machine series (1.33.13-gke.1079000 or later, or 1.34.1-gke.2037000 or later): 94 vCPU
  * Z3 machine series: 174 vCPU
  * Z4D machine series (1.36.3-gke.1244000 or later): 382 vCPU

  
Memory | No minimum requests enforced | 

  * C2 machine series: 218 GiB
  * C2D machine series: 835 GiB
  * C3 machine series: 1,345 GiB
  * C3 machine series with Local SSD: 670 GiB
  * C3D machine series: 2750 GiB
  * C3D machine series with Local SSD: 1,375 GiB
  * C4A machine series (see [requirements and limitations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke#arm-requirements-limitations)): 540 GiB
  * C4D machine series (1.32.9-gke.1711000 or later): 2905 GiB
  * C4D machine series with Local SSD (1.32.9-gke.1711000 or later): 2905 GiB
  * C4N machine series (1.36.0-gke.3009002 or later): 1,488 GiB
  * H3 machine series: 330 GiB
  * H4D machine series (1.33.2-gke.4731000 or later): 1400 GiB
  * T2A machine series: 172 GiB
  * T2D machine series: 218 GiB
  * C4 machine series: 2140 GiB
  * M4 machine series (1.33.4-gke.1013000 or later): 5952 GiB
  * N4 machine series: 600 GiB
  * N4A machine series (1.34.1-gke.3403001 or later): 512 GiB
  * N4D machine series (1.33.13-gke.1079000 or later, or 1.34.1-gke.2037000 or later): 768 GiB
  * Z3 machine series: 1406 GiB
  * Z4D machine series (1.36.3-gke.1244000 or later): 3024 GiB

  
Ephemeral storage | No minimum requests enforced | 

  * C2 machine series: 56 TiB
  * C2D machine series: 56 TiB
  * C3 machine series: 56 TiB
  * C3 machine series with Local SSD: 10,000 GiB
  * C3D machine series: 56 TiB
  * C3D machine series with Local SSD: 10,000 GiB
  * C4A machine series (see [requirements and limitations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke#arm-requirements-limitations)): 56 TiB
  * C4D machine series (1.32.9-gke.1711000 or later): 56 TiB
  * C4D machine series with Local SSD (1.32.9-gke.1711000 or later): 10,000 GiB
  * H3 machine series: 56 TiB
  * H4D machine series (1.33.2-gke.4731000 or later): 56 TiB
  * T2A machine series: 56 TiB
  * T2D machine series: 56 TiB
  * C4 machine series: 56 TiB
  * M4 machine series (1.33.4-gke.1013000 or later): 56 TiB
  * N4 machine series: 56 TiB
  * N4A machine series (1.34.1-gke.3403001 or later): 56 TiB
  * N4D machine series (1.33.13-gke.1079000 or later, or 1.34.1-gke.2037000 or later): 56 TiB
  * Z3 machine series: 34,000 GiB
  * Z4D machine series (1.36.3-gke.1244000 or later): 75,000 GiB

  
Scale-Out | Exactly 1:4 | CPU | 0.25 vCPU | 

  * `arm64`: 43 vCPU
  * `amd64`: 54 vCPU

  
Memory | 1 GiB | 

  * `arm64`: 172 GiB
  * `amd64`: 216 GiB

  
  
To learn how to request compute classes in your Autopilot Pods, refer to [Choose compute classes for Autopilot Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-compute-classes).

### Minimums and maximums for accelerators

GKE doesn't enforce minimum CPU, memory, or ephemeral storage requests for Pods that use accelerators. The following table describes the maximum requests for each of these resources based on the number and type of accelerator that you use.

Unless specified, the maximum ephemeral storage supported is 56 TiB.

NVIDIA A100 (40GB)NVIDIA A100 (80GB)NVIDIA H100 (80GB)NVIDIA H100 Mega (80GB)NVIDIA H200 (141GB)NVIDIA B200NVIDIA L4NVIDIA RTX PRO 6000NVIDIA Tesla T4TPU v6eTPU v5eTPU v5pTPU v4Ironwood (TPU7x)Clear all

Accelerator type | Resource | Maximum  
---|---|---  
NVIDIA B200  
`nvidia-B200` | CPU | 

  * 8 GPUs: 220 vCPU

  
Memory | 

  * 8 GPUs: 3800 GiB

  
Ephemeral storage | 

  * 8 GPUs: 10 TiB

  
NVIDIA H200 (141GB)  
`nvidia-h200-141gb` | CPU | 

  * 8 GPUs: 220 vCPU

  
Memory | 

  * 8 GPUs: 2810 GiB

  
Ephemeral storage | 

  * 8 GPUs: 10 TiB (1.32.2-gke.1182000 or later)
  * 8 GPUs: 2540 GiB (earlier than 1.32.2-gke.1182000)

  
NVIDIA H100 Mega (80GB)  
`nvidia-h100-mega-80gb` | CPU | 

  * 8 GPUs: 206 vCPU

  
Memory | 

  * 8 GPUs: 1795 GiB

  
Ephemeral storage | 

  * 8 GPUs: 5250 GiB

  
NVIDIA H100 (80GB)  
`nvidia-h100-80gb` | CPU | 

  * 8 GPUs: 206 vCPU

  
Memory | 

  * 8 GPUs: 1795 GiB

  
Ephemeral storage | 

  * 8 GPUs: 5250 GiB

  
NVIDIA A100 (40GB)  
`nvidia-tesla-a100` | CPU | 

  * 1 GPU: 11 vCPU
  * 2 GPUs: 22 vCPU
  * 4 GPUs: 46 vCPU
  * 8 GPUs: 94 vCPU
  * 16 GPUs: 94 vCPU

The sum of CPU requests of all DaemonSets that run on an A100 GPU node must not exceed 2 vCPU.  
Memory | 

  * 1 GPU: 74 GiB
  * 2 GPUs: 148 GiB
  * 4 GPUs: 310 GiB
  * 8 GPUs: 632 GiB
  * 16 GPUs: 1264 GiB

The sum of memory requests of all DaemonSets that run on an A100 GPU node must not exceed 14 GiB.  
NVIDIA A100 (80GB)  
`nvidia-a100-80gb` | CPU | 

  * 1 GPU: 11 vCPU
  * 2 GPUs: 22 vCPU
  * 4 GPUs: 46 vCPU
  * 8 GPUs: 94 vCPU

The sum of CPU requests of all DaemonSets that run on an A100 (80GB) GPU node must not exceed 2 vCPU.  
Memory | 

  * 1 GPU: 148 GiB
  * 2 GPUs: 310 GiB
  * 4 GPUs: 632 GiB
  * 8 GPUs: 1264 GiB

The sum of memory requests of all DaemonSets that run on an A100 (80GB) GPU node must not exceed 14 GiB.  
Ephemeral storage | 

  * 1 GPU: 280 GiB
  * 2 GPUs: 585 GiB
  * 4 GPUs: 1220 GiB
  * 8 GPUs: 2540 GiB

  
NVIDIA RTX PRO 6000  
`nvidia-rtx-pro-6000` **Important:** Starting on October 1, 2026, GKE bills for the Autopilot node management premium, in addition to existing applicable charges for the underlying hardware. These existing charges continue to apply both before and after this date. For more information about how billing works when requesting specific hardware with Autopilot workloads, see [Autopilot workloads that select specific hardware](https://docs.cloud.google.com/kubernetes-engine/pricing#autopilot-workloads-that-select-specific-hardware). | CPU | 

  * 1/8 GPU: 6 vCPU
  * 1/4 GPU: 12 vCPU
  * 1/2 GPU: 24 vCPU
  * 1 GPU: 47 vCPU
  * 2 GPUs: 94 vCPU
  * 4 GPUs: 190 vCPU
  * 8 GPUs: 380 vCPU

  
Memory | 

  * 1/8 GPU: 22 GiB
  * 1/4 GPU: 45 GiB
  * 1/2 GPU: 90 GiB
  * 1 GPU: 164 GiB
  * 2 GPUs: 330 GiB
  * 4 GPUs: 675 GiB
  * 8 GPUs: 1350 GiB

  
Ephemeral storage | 

  * 1/8 GPU: 0 GiB (doesn't support ephemeral storage)
  * 1/4 GPU: 375 GiB
  * 1/2 GPU: 750 GiB
  * 1 GPU: 1500 GiB
  * 2 GPUs: 3 TiB
  * 4 GPUs: 6 TiB
  * 8 GPUs: 12 TiB

  
NVIDIA L4  
`nvidia-l4` | CPU | 

  * 1 GPU: 31 vCPU
  * 2 GPUs: 23 vCPU
  * 4 GPUs: 47 vCPU
  * 8 GPUs: 95 vCPU

The sum of CPU requests of all DaemonSets that run on an L4 GPU node must not exceed 2 vCPU.  
Memory | 

  * 1 GPU: 115 GiB
  * 2 GPUs: 83 GiB
  * 4 GPUs: 177 GiB
  * 8 GPUs: 363 GiB

The sum of memory requests of all DaemonSets that run on an L4 GPU node must not exceed 14 GiB.  
NVIDIA Tesla T4  
`nvidia-tesla-t4` | CPU | 

  * 1 GPU: 46 vCPU
  * 2 GPUs: 46 vCPU
  * 4 GPUs: 94 vCPU

  
Memory | 

  * 1 GPU: 287.5 GiB
  * 2 GPUs: 287.5 GiB
  * 4 GPUs: 587.5 GiB

  
Ironwood (TPU7x)  
`tpu7x` | CPU | 

  * tpu7x-standard-4t: 224 vCPU

  
Memory | 

  * tpu7x-standard-4t: 992 GiB

  
Ephemeral storage | 56 TiB  
TPU v6e ([Preview](https://cloud.google.com/products#product-launch-stages))  
`tpu-v6e-slice` | CPU | 

  * ct6e-standard-1t: 44 vCPU
  * ct6e-standard-4t: 180 vCPU
  * ct6e-standard-8t: 180 vCPU

  
Memory | 

  * ct6e-standard-1t: 176 GiB
  * ct6e-standard-4t: 720 GiB
  * ct6e-standard-8t: 1440 GiB

  
Ephemeral storage | 56 TiB  
TPU v5e  
`tpu-v5-lite-podslice` | CPU | 

  * 1x1 topology: 24 vCPU
  * 2x2 topology: 112 vCPU
  * 2x4 topology (4-chip request): 112 vCPU
  * 2x4 topology (8-chip request): 224 vCPU
  * 4x4 topology: 112 vCPU
  * 4x8 topology: 112 vCPU
  * 8x8 topology: 112 vCPU
  * 8x16 topology: 112 vCPU
  * 16x16 topology: 112 vCPU

  
Memory | 

  * 1x1 topology: 48 GiB
  * 2x2 topology: 192 GiB
  * 2x4 topology (4-chip request): 192 GiB
  * 2x4 topology (8-chip request): 384 GiB
  * 4x4 topology: 192 GiB
  * 4x8 topology: 192 GiB
  * 8x8 topology: 192 GiB
  * 8x16 topology: 192 GiB
  * 16x16 topology: 192 GiB

  
Ephemeral storage | 56 TiB  
TPU v5p  
`tpu-v5p-slice` | CPU | 280 vCPU  
Memory | 448 GiB  
Ephemeral storage | 56 TiB  
TPU v4  
`tpu-v4-podslice` | CPU | 240 vCPU  
Memory | 407 GiB  
Ephemeral storage | 56 TiB  
  
**Note:** All A100 (80GB) GPU nodes use local SSDs for node boot disks at fixed sizes based on the number of GPUs. You're billed separately for the attached Local SSDs. For details, see [Autopilot pricing](https://cloud.google.com/kubernetes-engine/pricing#gpu-pods). A100 (40GB) GPUs don't use local SSDs for node boot disks.

To learn how to request GPUs in your Autopilot Pods, refer to [Deploy GPU workloads in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus).

### Resource requests for workload separation and extended duration

In the following scenarios, Autopilot enforces higher values for default and minimum resource requests:

  * You use a `podFamily` priority rule in any [custom Autopilot ComputeClass](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters#custom-ap-classes) that's not the [cluster-level default](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-pods-default-compute-classes).
  * You deploy workloads that meet both of the following criteria: 
    * Use one of the following compute configurations: 
      * The default container-optimized compute platform in Autopilot clusters.
      * Any built-in Autopilot ComputeClass.
      * `podFamily` priority rules in a custom Autopilot ComputeClass that's also the cluster-level default.
      * The `Balanced` or `Scale-Out` ComputeClasses in Autopilot clusters.
    * Manipulate Kubernetes scheduling and eviction behavior in any of the following ways: 
      * You use [workload separation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-separation) to ensure that certain Pods only get placed on specific nodes.
      * You use [Pod anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity) to prevent Pods from co-locating on the same node.
      * You use an annotation to [extend the run time of Autopilot Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/extended-duration-pods), preventing eviction because of node auto-upgrades and scale-down events for up to seven days.



By default, if your resource requests are lower than the allowed minimum value, Autopilot increases your resource requests to meet the minimum. The exception to this behavior is Pod anti-affinity, where Autopilot rejects the Pod with an error message.

The following table describes the default requests and the minimum resource requests that you can specify in these scenarios:

Configuration | Default | Minimum  
---|---|---  
Pods that modify scheduling or eviction behavior and use one of the following configurations:

  * Default Autopilot compute platform
  * Built-in Autopilot ComputeClasses
  * `podFamily` rules in cluster-level default ComputeClasses

| 

  * **CPU** : 0.5 vCPU
  * **Memory** : 2 GiB

| 

  * **CPU** : 0.5 vCPU
  * **Memory** : 0.5 GiB

  
Pods that use `podFamily` rules in non-default custom ComputeClasses | 

  * **CPU** : 0.5 vCPU
  * **Memory** : 2 GiB

| 

  * **CPU** : 0.5 vCPU
  * **Memory** : 0.5 GiB

  
Pods that modify scheduling or eviction behavior and use the `Balanced` ComputeClass in Autopilot clusters | 

  * **CPU** : 2 vCPU
  * **Memory** : 8 GiB

| 

  * **CPU** : 1 vCPU
  * **Memory** : 4 GiB

  
Pods that modify scheduling or eviction behavior and use the `Scale-Out` ComputeClass in Autopilot clusters | 

  * **CPU** : 0.5 vCPU
  * **Memory** : 2 GiB

| 

  * **CPU** : 0.5 vCPU
  * **Memory** : 2 GiB

  
  
### Init containers

[Init containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/#detailed-behavior) run sequentially, and all init containers must finish running before application containers can start. In Autopilot clusters, if you don't specify CPU or memory requests for init containers or explicitly set requests to `0`, Autopilot modifies your Pods during creation to add resource requests to each init container. The requests assigned to each init container are equal to the sum of requests for all application containers in the Pod. This is the default behavior.

This behavior differs from Standard clusters, where init containers use any [unallocated resources](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/#resource-sharing-within-containers) available on the _node_ on which the Pod is scheduled.

#### Automatic resource allocation for init containers

The automatic resource allocation for init containers occurs at Pod creation. We suggest that you don't manually specify resource requests for the init containers in Autopilot clusters, so that each container gets the full resources available to the Pod by default.

If you change the resource requests of non-init containers in the Pod after creation, Autopilot doesn't automatically adjust the resource requests of the init containers. As a result, you might notice charges that aren't consistent with the actual resource usage of the Pod. Your bill is based on the _effective resource request_ of the Pod, which is the larger of the following:

  * The largest resource request of any single init container in the Pod.
  * The sum of requests for all application containers in the Pod.



For more information, see Automatic resource management in Autopilot.

#### Manual resource allocation for init containers

If you need to change the existing resource requests for your application containers to manage costs and resources, we recommend that you do one of the following to adjust your init container requests:

  * [Manually update the resource requests](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#how-to-request) for the init container to match the new total requests on the Pod. Consider the following when manually specifying the resource requests: 
    * Requests lower than the Pod's total resources can constrain the init container.
    * Requests higher than the Pod's total resources can increase costs.
  * Remove the resource requests to let Autopilot re-compute them. Autopilot will default to re-allocating the resources to each init container based on the current total resources requested by all the application containers in the Pod.



## Setting resource limits in Autopilot

Kubernetes lets you set both `requests` and `limits` for resources in your Pod specification. The behavior of your Pods changes depending on whether your `limits` are different than your `requests`, as described in the following table:

Values set | Autopilot behavior  
---|---  
`requests` equal to `limits` | Pods use the `Guaranteed` QoS class. **Note:** Ephemeral storage limits must always be explicitly set equal to requests. GKE modifies your Pods to enforce this rule.  
`requests` set, `limits` not set | The behavior depends on whether your cluster supports bursting, as follows:

  * **Clusters that support bursting** : Pods can burst into available [burstable capacity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-bursting-gke#burstable-capacity).
  * **Clusters that don't support bursting** : GKE sets the `limits` equal to the `requests`

To check whether your cluster supports bursting, see [Bursting availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-bursting-gke#availability-in-gke).  
`requests` not set, `limits` set | Autopilot sets `requests` to the value of `limits`, which is the default Kubernetes behavior. Before:
    
    
    resources:
      limits:
        cpu: "400m"

After:
    
    
    resources:
      **requests:
        cpu: "400m"**
      limits:
        cpu: "400m"  
  
`requests` less than `limits` | The behavior depends on whether your cluster supports bursting, as follows:

  * **Clusters that support bursting** : Pods can burst up to the value specified in `limits`.
  * **Clusters that don't support bursting** : GKE sets the `limits` equal to the `requests`

To check whether your cluster supports bursting, see [Bursting availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-bursting-gke#availability-in-gke).  
`requests` greater than `limits` | Autopilot sets `requests` to the value of `limits`. Before:
    
    
    resources:
      requests:
        cpu: "450m"
      limits:
        cpu: "400m"

After:
    
    
    resources:
      requests:
        cpu: "400m"
      limits:
        cpu: "400m"  
  
`requests` not set, `limits` not set | Autopilot sets `requests` to the default values for the compute class or hardware configuration. The behavior for `limits` depends on whether your cluster supports bursting, as follows:

  * **Clusters that support bursting** : Autopilot doesn't set `limits`.
  * **Clusters that don't support bursting** : GKE sets the `limits` equal to the `requests`

To check whether your cluster supports bursting, see [Bursting availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-bursting-gke#availability-in-gke).  
  
In most situations, set adequate resource requests and equal limits for your workloads.

For workloads that temporarily need more resources than their steady-state, like during boot up or during higher traffic periods, set your limits higher than your requests to let the Pods burst. For details, see [Configure Pod bursting in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-bursting-gke).

## Automatic resource management in Autopilot

If your specified resource requests for your workloads are outside of the allowed ranges, or if you don't request resources for some containers, Autopilot modifies your workload configuration to comply with the allowed limits. Autopilot calculates resource ratios and the resource scale up requirements after applying default values to containers with no request specified.

  * **Missing requests:** If you don't request resources in some containers, Autopilot applies the default requests for the compute class or hardware configuration.
  * **CPU:memory ratio:** Autopilot scales up the smaller resource to bring the ratio within the allowed range.
  * **Ephemeral storage:** Autopilot modifies your ephemeral storage requests to meet the minimum amount required by each container. The cumulative value of storage requests across all containers cannot be more than the maximum allowed value. Prior to 1.28.6-gke.1317000, Autopilot scales down the requested ephemeral storage if the value exceeds the maximum. In version 1.28.6-gke.1317000 and later, Autopilot rejects your workload.
  * **Requests below minimums** : If you request fewer resources than the allowed minimum for the selected hardware configuration, Autopilot automatically modifies the Pod to request at least the minimum resource value.



By default, when Autopilot automatically scales a resource up to meet a minimum or default resource value, GKE allocates the extra capacity to the _first container_ in the Pod manifest. In GKE version 1.27.2-gke.2200 and later, you can tell GKE to allocate the extra resources to a specific container by adding the following to the `annotations` field in your Pod manifest:
    
    
    autopilot.gke.io/primary-container: "CONTAINER_NAME"
    

Replace `CONTAINER_NAME` with the name of the container.

### Resource modification examples

The following example scenario shows how Autopilot modifies your workload configuration to meet the requirements of your running Pods and containers.

#### Single container with < 0.05 vCPU

Container number | Original request | Modified request  
---|---|---  
1 |  CPU: 30 mCPU  
Memory: 0.5 GiB  
Ephemeral storage: 10 MiB  
|  **CPU: 50 mCPU**  
Memory: 0.5 GiB  
Ephemeral storage: 10 MiB  
  
  
#### Multiple containers with total CPU < 0.05 vCPU

Container number | Original requests | Modified requests   
---|---|---  
1 | CPU: 10 mCPU  
Memory: 0.5 GiB  
Ephemeral storage: 10 MiB | **CPU: 30 mCPU**  
Memory: 0.5 GiB  
Ephemeral storage: 10 MiB  
2 | CPU: 10 mCPU  
Memory: 0.5 GiB  
Ephemeral storage: 10 MiB | CPU: 10 mCPU  
Memory: 0.5 GiB  
Ephemeral storage: 10 MiB  
3 | CPU: 10 mvCPU  
Memory: 0.5 GiB  
Ephemeral storage: 10 MiB | CPU: 10 mCPU  
Memory: 0.5 GiB  
Ephemeral storage: 10 MiB  
Total Pod resources |  | **CPU: 50 mCPU**  
Memory: 1.5 GiB  
Ephemeral storage: 30 MiB  
  
#### Single container with memory too low for requested CPU

In this example, the memory is too low for the amount of CPU (1 vCPU:1 GiB minimum). The minimum allowed ratio for CPU to memory is 1:1. If the ratio is lower than that, the memory request is increased.

Container number | Original request | Modified request  
---|---|---  
1 | CPU: 4 vCPU  
Memory: 1 GiB  
Ephemeral storage: 10 MiB | CPU: 4 vCPU  
**Memory: 4 GiB**  
Ephemeral storage: 10 MiB  
Total Pod resources |  | CPU: 4 vCPU  
**Memory: 4 GiB**  
Ephemeral storage: 10 MiB  
  
## What's next

  * Learn how to [configure Pod bursting in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-bursting-gke).
  * Learn how to [choose compute classes for Autopilot Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-compute-classes).
  * Learn how to [accelerate application startup using CPU startup boost](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/boost-application-startup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
