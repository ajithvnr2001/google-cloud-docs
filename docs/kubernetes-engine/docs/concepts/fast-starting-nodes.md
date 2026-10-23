---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/fast-starting-nodes/
title: About quicker workload startup with fast-starting nodes \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:34.350718+00:00
---

# About quicker workload startup with fast-starting nodes  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/fast-starting-nodes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About quicker workload startup with fast-starting nodes Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

This page shows you how to deploy and scale workloads more quickly in Google Kubernetes Engine (GKE) clusters using fast-starting nodes. Fast-starting nodes are used in GKE with Autopilot mode on a best-effort basis when workloads use compatible configurations.

Fast-starting GKE nodes have significantly lower startup time for compatible machine families. The accelerated startup time provides you with the following benefits:

  * Faster cold start
  * Faster autoscaling
  * Improved Pod scheduling long-tail latency
  * Improved infrastructure cost efficiency



With fast-starting nodes, GKE pre-initializes hardware resources to accelerate startup time. The pre-initialized resources are available on a best-effort basis. Surge requests might only be partially served. Without fast-starting nodes, resources are initialized on-demand, and nodes are served at normal startup time.

## Requirements

Fast-starting nodes require no additional configuration. GKE automatically uses fast-starting nodes if your workloads use compatible configurations. You must meet all of the following requirements to use fast-starting nodes:

  * Use Autopilot clusters, or run [workloads in Autopilot mode in your Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters).
  * Don't use any features that are incompatible with fast-starting nodes. For more information, see Limitations.
  * Use one of the following compute resources which are described in the respective tables in the Configuration requirements for eligible compute resources section:

    * Autopilot container-optimized compute platform
    * G2 machine series
    * A2 machine series
    * A3 Mega machine type
    * G4 machine series



## Limitations

The following features aren't compatible with fast-starting GKE nodes. If you use any of these features, GKE provisions nodes with the typical startup time:

  * G2 with `DEFAULT` GPU driver version on GKE versions earlier than 1.33.0-gke.1304000. For 1.33.0-gke.1304000 or later, both `LATEST` and `DEFAULT` work with fast-starting nodes.
  * [Secondary boot disks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/data-container-image-preloading) on versions earlier than 1.33.2-gke.1015000.
  * [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms)
  * [Placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview)
  * [Multi-network support](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multinetwork-support-for-pods)



## Autopilot GPU workloads

Requesting compatible GPUs in Autopilot mode results in up to four times faster node startup time and up to two times faster Pod scheduling time than similar requests in GKE Standard mode, because the Autopilot GPU workloads can use fast-starting nodes.

The following are some example use cases. However, any Pods meeting the conditions from the Requirements section are compatible with fast-starting nodes.

### ComputeClass

Request a compatible accelerator type and count in a ComputeClass, like in the following example:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: ACCELERATOR_COMPUTE_CLASS_NAME
    spec:
      priorities:
      - gpu:
          type: ACCELERATOR_TYPE
          count: ACCELERATOR_COUNT
      nodePoolAutoCreation:
        enabled: true
    

When you select this ComputeClass in a Pod, like in the following example, GKE uses fast-starting nodes:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: POD_NAME
    spec:
      nodeSelector:
        # Select a ComputeClass that requests compatible GPUs
        cloud.google.com/compute-class: ACCELERATOR_COMPUTE_CLASS_NAME
      containers:
      - name: my-container
        image: registry.k8s.io/pause
        resources:
          limits:
            nvidia.com/gpu: ACCELERATOR_COUNT
    

Replace the following values:

  * `ACCELERATOR_COMPUTE_CLASS_NAME`: the name of the ComputeClass that requests the accelerators.
  * `ACCELERATOR_TYPE`: the type of accelerator.
  * `ACCELERATOR_COUNT`: the number of accelerators required by the Pod. This value must be less than or equal to the value in the `spec.priorities.gpu.count` field in the ComputeClass.
  * `POD_NAME`: the name of your Pod.



For more information about ComputeClass, see [About custom compute classes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes).

### Pod specification

Select a compatible accelerator type and count in your Pod specification, like in the following example:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: POD_NAME
    spec:
      nodeSelector:
        cloud.google.com/gke-accelerator: ACCELERATOR_NAME
      containers:
      - name: my-container
        image: registry.k8s.io/pause
        resources:
          limits:
            nvidia.com/gpu: ACCELERATOR_COUNT
    

Replace the following values:

  * `POD_NAME`: the name of your Pod.
  * `ACCELERATOR_NAME`: the name of the accelerator required by the Pod.
  * `ACCELERATOR_COUNT`: the number of accelerators required by the Pod.



## Configuration requirements for eligible compute resources

The tables in the following sections describe the specific requirements for GKE to provision the relevant compute resources as fast-starting nodes.

### Autopilot container-optimized compute platform

See the following requirements for GKE to provision fast-starting nodes with the Autopilot container-optimized compute platform.

Compute resource | Release channel and version support | Supported disks  
---|---|---  
[Autopilot container-optimized compute platform](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#autopilot-compute-platform) | 

  * Rapid channel
  * 1.33.0-gke.1696000 or later

| 

  * `pd-balanced` boot disks up to 100 GiB
  * No [Local SSDs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd).

  
  
### G2 machine series

See the following requirements for GKE to provision G2 machines as fast-starting nodes.

Compute resource | Release channel and version support | Supported disks  
---|---|---  
[G2 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-vms) | 

  * Rapid and Regular channels
  * 1.31 or later

| 

  * `pd-balanced` boot disks up to 500 GiB
  * No [Local SSDs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd).

  
  
### A2 machine series

See the following requirements for GKE to provision A2 machines as fast-starting nodes.

Compute resource | Release channel and version support | Supported disks  
---|---|---  
[A2 Standard machine types](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-standard-vms) | 

  * Rapid and Regular channels
  * 1.32.0-gke.1008000 or later

| 

  * `pd-balanced` or `pd-ssd` boot disks up to 1,000 GiB.
  * No [Local SSDs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd).

  
[A2 Ultra machine types](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-ultra-vms) | 

  * Rapid and Regular channels
  * 1.32.0-gke.1008000 or later

| 

  * `pd-balanced` or `pd-ssd` boot disks up to 1,000 GiB, with higher limits for `a2‑ultragpu‑4g` (1,500 GiB) and `a2‑ultragpu‑8g` (3,000 GiB).
  * With automatically attached [Local SSDs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd).

  
  
### A3 Mega machine type

See the following requirements for GKE to provision A3 Mega machines as fast-starting nodes.

Compute resource | Release channel and version support | Supported disks  
---|---|---  
[A3 Mega machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-mega-vms) | 

  * Rapid channel
  * 1.34.4-gke.1130000 or later

| 

  * `hyperdisk-balanced`, `pd-ssd`, or `pd-balanced` boot disks.
  * With automatically attached [Local SSDs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd).

  
  
### G4 machine series

See the following requirements for GKE to provision G4 machines as fast-starting nodes.

Compute resource | Release channel and version support | Supported disks  
---|---|---  
[G4 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series) | 

  * Rapid channel
  * 1.34.4-gke.1130000 or later

| 

  * `hyperdisk-balanced` boot disks
  * No [Local SSDs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd).

  
  
## Pricing

Fast-starting nodes are available in GKE Autopilot at no extra charge. For more information about GKE Autopilot pricing, see the Autopilot mode section in [Google Kubernetes Engine pricing](https://cloud.google.com//kubernetes-engine/pricing#autopilot_mode).

## What's next

  * [Strategies to reduce startup latency](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/startup-latency-reduction-strategies)
  * [About the Autopilot container-optimized compute platform](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#autopilot-compute-platform)
  * [About custom compute classes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes)
  * [Persistent Disk performance overview](https://docs.cloud.google.com/compute/docs/disks/performance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
