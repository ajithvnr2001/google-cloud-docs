---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/performance-pods/
title: Optimize Autopilot Pod performance by choosing a machine series \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T09:32:13.751851+00:00
---

# Optimize Autopilot Pod performance by choosing a machine series  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/performance-pods/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Optimize Autopilot Pod performance by choosing a machine series Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

This document shows you how to place workloads on a specific Compute Engine machine series for optimal workload performance in your Google Kubernetes Engine (GKE) Autopilot clusters.

Ensure that you're familiar with the following:

  * [Compute Engine machine series and use cases](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison)
  * Kernel-level requirements for your applications



## How machine series selection works

You can add a `cloud.google.com/machine-family` node selector to your Pod specification for Autopilot to allocate specific Compute Engine hardware for that Pod. For example, you can choose the C3 machine series for Pods that need more CPU power, or the N1 machine series for Pods that need more memory. To optimally run your workload, Autopilot provisions one of the predefined machine types from the machine series you selected.

In addition to optimal Pod performance, choosing a specific machine series offers the following benefits:

  * **Efficient node utilization** : By default, Autopilot optimizes node resource usage by scheduling onto each node as many Pods as possible that request the same machine series. This approach optimizes resource usage on the node, which improves the price-to-performance ratio. If your workload needs access to all of the resources on the node, you optionally can configure your workload to request one Pod for each node.

  * **Burstable workloads:** You can configure Pods to _burst_ into unused resource capacity on the node by setting your resource limits higher than your requests. For details, see [Configure Pod bursting in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-bursting-gke#burstable-capacity).




### Plan a dedicated node for each Pod

If you have CPU-intensive workloads that need reliable access to all of the node resources, you can optionally configure your Pod to get Autopilot to place a Pod that requests a machine series on its own node.

Dedicated nodes per Pod are recommended when you run large-scale, CPU-intensive workloads, like AI/ML training workloads or high performance computing (HPC) batch workloads.

### Choose between multiple-Pod and single-Pod scheduling

Use the following guidance to choose a Pod scheduling behavior based on your requirements:

  * If you have Pods that can share compute resources with other Pods or you want to optimize costs while running Pods on specialized hardware, use the default scheduling behavior of multiple Pods per node.
  * If you have Pods that need reliable access to full node resources or you want to minimize the chance of disruptions caused by sharing compute resources, Request a dedicated node for each Pod.



## Pricing

You're billed for the underlying VM and any attached hardware by Compute Engine, plus a premium for Autopilot node management and scalability. For details, see [GKE pricing](https://cloud.google.com/kubernetes-engine/pricing#autopilot_mode).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an existing Autopilot cluster running version 1.30.1-gke.1396000 or later. To create a cluster, see [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster#set-version).



## Select a machine series

This section shows you how to select a specific Compute Engine machine series in a Pod.

  1. Save the following manifest as `machine-series-pod.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: machine-series-pod
         spec:
           nodeSelector:
             **cloud.google.com/machine-family : MACHINE_SERIES**
           containers:
           - name: my-container
             image: "k8s.gcr.io/pause"
             resources:
               requests:
                 cpu: 5
                 memory: "25Gi"
               limits:
                 cpu: 20
                 memory: 100Gi
         

Replace `MACHINE_SERIES` with the Compute Engine machine series for your Pod, like `c3`. For supported values, see Supported machine series in this page.

  2. Deploy the Pod:
         
         kubectl apply -f machine-series-pod.yaml
         




This manifest lets Autopilot optimize node resource usage by efficiently scheduling other Pods that select the same machine series onto the same node if there's available capacity.

### Use Local SSDs

Pods that select a machine series can use Local SSDs for ephemeral storage if you specify a machine series that offers Local SSD. Autopilot considers ephemeral storage requests when choosing a Compute Engine machine type for the Pod.

To learn more, see [Use Local SSD-backed ephemeral storage with Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd#local-ssd-autopilot).

### Request a dedicated node for a Pod

If your Pod has specific performance requirements like needing reliable access to all of the resources of your node, you can request a dedicated node for each Pod by specifying the `cloud.google.com/compute-class: Performance` node selector along with your machine series node selector. This indicates to Autopilot to place your Pod on a new node that uses the specified machine series and is dedicated for that Pod. This node selector also prevents Autopilot from scheduling other Pods on that node.

  1. Save the following manifest as `dedicated-node-pod.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: dedicated-node-pod
         spec:
           nodeSelector:
             cloud.google.com/machine-family: MACHINE_SERIES
             **cloud.google.com/compute-class : Performance**
           containers:
           - name: my-container
             image: "k8s.gcr.io/pause"
             resources:
               requests:
                 cpu: 12
                 memory: "50Gi"
                 ephemeral: "200Gi"
         

Replace `MACHINE_SERIES` with a [supported machine series](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/performance-pods#supported-machine-series) that also supports one Pod per node scheduling. If the specified machine series doesn't support one Pod per node scheduling, the deployment fails with an error.

  2. Deploy the Pod:
         
         kubectl apply -f dedicated-node-pod.yaml
         




When you deploy this manifest, Autopilot does the following:

  * Ensures that the deployed Pod requests at least the [minimum resources for the performance-optimized node](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#compute-class-min-max).
  * Calculates the total resource requests of the deployed Pod and any DaemonSets in the cluster.
  * Provisions a node that's backed by the selected machine series.
  * Modifies the Pod manifest with a combination of node selectors and tolerations to ensure that the Pod runs on its own node.



## Supported machine series

The `machine-family` selector supports the following machine series:

Machine series | Node selector value | Supports multiple Pods per node | Supports single Pod per node  
---|---|---|---  
[C4N machine series](https://docs.cloud.google.com/compute/docs/network-optimized-machines#c4n_series) (see Version requirements) | `c4n` |  |   
[C4D machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4d_series) (see Version requirements) | `c4d` |  |   
[C4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series) (see [requirements and limitations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke#arm-requirements-limitations)) | `c4a` |  |   
[C4 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series)  
 _Default for the Performance class_ | `c4` |  |   
[C3 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_series) (see Limitations) | `c3` |  |   
[C3D machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3d_series) | `c3d` |  |   
[C2 machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#c2_series) | `c2` |  |   
[C2D machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#c2d_series) | `c2d` |  |   
[H4D machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_series) | `h4d` |  |   
[H3 machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h3_series) | `h3` |  |   
[T2D machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2d_machines) | `t2d` |  |   
[T2A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_machines) | `t2a` |  |   
[E2 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#e2_machine_types) | `e2` |  |   
[N4 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4_series) | `n4` |  |   
[N4D machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4d_series) (see Version requirements) | `n4d` |  |   
[N2 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_series) | `n2` |  |   
[N2D machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2d_machines) | `n2d` |  |   
[N1 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_machines) | `n1` |  |   
[Z3 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#z3_series) | `z3` |  |   
[Z4D machine series](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4d_series) (see Version requirements) | `z4d` |  |   
  
If you don't specify a machine series when you select the Performance class, GKE uses the C4 machine series if C4 machine types are [available in a region](https://docs.cloud.google.com/compute/docs/regions-zones#available).

To compare these machine series and their use cases, see [Machine series comparison](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison) in the Compute Engine documentation.

### Limitations

Bare metal machine types (such as `c3-standard-192-metal` and `c4a-standard-72-metal`) aren't supported when using the predefined Performance ComputeClass. To use bare metal machine shapes with Autopilot and node pool auto-creation, specify the exact machine type using a [custom ComputeClass](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#machinetype-rule).

### Version requirements

See the following version requirements for specific machine series:

  * **C4N** : GKE version 1.36.0-gke.3009002 and later
  * **C4D** : GKE version 1.32.9-gke.1711000 and later
  * **N4D** : 
    * GKE version 1.33.13-gke.1079000 and later
    * GKE version 1.34.1-gke.2037000 and later
  * **C3 and C4A bare metal types** : GKE version 1.35.3-gke.1389000 and later (using a [custom ComputeClass](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#machinetype-rule)).
  * **Z4D** : GKE version 1.36.3-gke.1244000 and later.



## Compatibility with other GKE features

Pods that select a machine series can use the GKE capabilities and features supported by that machine series, such as:

  * [Spot Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-spot-pods)
  * [Extended run time Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/extended-duration-pods) (only with dedicated nodes per Pod)
  * [Workload separation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-separation)
  * [Capacity reservations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations)
  * [Committed-use discounts](https://docs.cloud.google.com/kubernetes-engine/cud)



Spot Pods and extended run time Pods are mutually exclusive. GKE doesn't enforce higher minimum resource requests for dedicated Pods per node, even though they use workload separation.

## How GKE selects a machine type

To select a machine type in the specified machine series, GKE calculates the total CPU, total memory, and total ephemeral storage requests of the Pods and any DaemonSets that will run on the new node. GKE rounds these values up to the nearest available Compute Engine machine type that supports all of these totals.

  * Example 1: Consider a Deployment with four replicas that selects the C3D machine series. You don't request dedicated nodes per Pod. The resource requests of each replica are as follows:

    * 500m vCPU (0.5 vCPU)
    * 1 GiB of memory

Autopilot places all four Pods on a node that's backed by the `c3d-standard-4` machine type, which has 4 vCPUs and 16 GB of memory.

  * Example 2: Consider a Pod that selects the `C3D` machine series and Local SSDs for ephemeral storage. You request a dedicated node for the Pod. The total resource requests including DaemonSets are as follows:

    * 12 vCPU
    * 50 GiB of memory
    * 200 GiB of ephemeral storage

Autopilot places the Pod on a node that uses the `c3d-standard-16-lssd` machine type, which has 16 vCPUs, 64 GiB of memory, and 365 GiB of Local SSD capacity.




## What's next

  * For guidance about the compute options that Autopilot offers for various use cases, see [Compute classes in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-compute-classes).
  * [Deploy GPU-based workloads in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
