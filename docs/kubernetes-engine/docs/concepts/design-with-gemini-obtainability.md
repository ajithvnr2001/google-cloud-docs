---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/design-with-gemini-obtainability/
title: Design for capacity flexibility and efficiency on GKE with Gemini \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:50.338003+00:00
---

# Design for capacity flexibility and efficiency on GKE with Gemini  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/design-with-gemini-obtainability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Design for capacity flexibility and efficiency on GKE with Gemini Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document explains how to design resilient Google Kubernetes Engine (GKE) clusters and workload scheduling strategies that help you obtain resources, such as GPUs, TPUs, and high-performance CPUs. By leveraging Gemini in Google Cloud and [Compute Advisor](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/design-with-gemini) (Preview), you can prevent pending Pods and improve reliable scheduling for AI workloads.

This document is intended for Cloud architects and Platform admins and operators who manage GKE infrastructure and want to optimize capacity planning and scheduling.

## Overview of flexibility, efficiency, and availability of compute capacity on GKE

Kubernetes scheduling relies on declared resource requests. When scheduling large-scale accelerators, like GPUs or TPUs, strict resource requests can lead to clusters failing to scale up if specific hardware is unavailable. You can optimize capacity availability on GKE by using the following features:

  * **Node pool auto-creation:** dynamic, multi-family node pool creation.
  * **Workload-level fallbacks:** tolerations and node selectors configured to accept alternative hardware.
  * **Geographic and regional scheduling:** GKE multi-zonal and multi-regional capabilities.
  * **Reservation management:** consuming pre-purchased capacity before requesting on-demand resources.



## Best practices for flexibility, efficiency, and availability of compute capacity on GKE

This section provides recommendations to increase your capacity availability when scheduling workloads on GKE. These best practices cover strategies such as designing flexible hardware requirements, configuring node pool auto-creation, and leveraging geographic distribution to adapt to resource constraints. [Node pool auto-creation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning) automatically manages node pools based on Pod specifications. Rather than pre-defining node pools, specify resource requirements in your Pod manifests, and let GKE dynamically create nodes.

You can also discover and implement the following best practices by using Compute Advisor. For more information, see Use Compute Advisor.

### Options for increasing the availability of compute capacity

To optimize capacity availability, you can instruct GKE to avoid binding workloads to a single static machine family or accelerator type. The following are examples of how you can configure flexible node pools and Pod affinity rules for different workload classes. The specific alternatives you choose depend on your application's resource demands:

  * General-purpose CPU node pools:

    * **Primary example:** N2 (Intel-based general-purpose).
    * **Sample alternatives:** N2D (AMD EPYC), C2 or C2D (Compute-optimized), or E2 (Cost-optimized).
    * **Implementation pattern:** configure Pod specs with node affinity or tolerations that permit scheduling across multiple machine family labels, for example, `cloud.google.com/machine-family` in `["n2", "n2d", "c2d"]`. This configuration lets GKE provision whichever pool has available capacity.
  * GPU node pools:

    * **Primary example:** A2 Series (NVIDIA A100 GPUs).
    * **Sample alternatives:** L4 (Universal AI/ML) or T4 (Inference).
    * **Implementation pattern:** Configure separate node pools or ComputeClasses for different GPU tiers. For workloads that can run without A100-specific features, allow Pods to fall back to L4 or T4 pools if A2 provisioning is constrained.
  * TPU node pools:

    * **Primary example:** TPU Ironwood (TPU7x).
    * **Sample alternatives:** TPU v6 (Trillium) or TPU v5 (v5e or v5p).
    * **Implementation pattern:** TPU slice provisioning can be highly constrained. Design training workloads with framework-level flexibility (for example, JAX or PyTorch configurations supporting variable slice topologies) to deploy on v6 or v5 slices when TPU Ironwood (TPU7x) capacity is unavailable.



The following table summarizes the primary selections and hardware alternatives for different types of workloads:

Workload type | Primary selection example | Sample alternatives | Architectural considerations  
---|---|---|---  
**System or core workloads** | N2 | N2D, C2D, E2 | Spans Intel and AMD hardware pools for node pool auto-creation.  
**GPU inference and processing** | A2 (A100) | L4, T4 | Flexibly targets lower-cost or higher-availability GPU node pools.  
**TPU model training** | TPU Ironwood (TPU7x) | TPU v6, TPU v5 (v5e or v5p) | Utilizes flexible topologies for slice-based scheduling.  
  
### Implement node pool auto-creation and ComputeClasses

To optimize capacity availability, combine node pool auto-creation with [ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-compute-classes). The following list includes best practices:

  * **Define ComputeClasses:** create ComputeClass resources that specify a prioritized list of machine families, GPU types, or provisioning models. GKE attempts to provision nodes by using the highest-priority configuration available in the class. A prioritized fallback list significantly helps you obtain the resources that your workloads require. For example, to prevent GKE from falling back to general-purpose machines when a preferred specialized accelerator is unavailable, add the `whenUnsatisfiable: DoNotScaleUp` setting to your ComputeClass configuration. For more information, see [Control autoscaled node attributes with custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-attributes-compute-classes).

  * **Reference ComputeClasses in Pod specs:** in your workload Pod specifications, use the `cloud.google.com/compute-class` label to target your custom ComputeClass instead of a specific machine family or GPU type. For more information, see [Request a ComputeClass in a workload](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-attributes-compute-classes#request-compute-class-workload).

  * **Define multiple tolerations:** if you don't use ComputeClasses, use node affinity rules in your Pod specifications that permit a range of machine families (such as `cloud.google.com/machine-family` in `["n2", "n2d"]`). For more information, see [Configure node pool auto-creation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning).




### Geographic and multi-region flexibility on GKE

To increase capacity availability, deploy GKE clusters that span multiple zones, or run multi-cluster architectures:

  * **Multi-zonal clusters:** ensure node pools are configured to auto-scale across all available zones in a region.

  * **Multi-region cluster federation:** for large asynchronous jobs (such as offline batch inference or distributed training), deploy a multi-cluster orchestrator (like Kueue or Cluster Director) to queue workloads globally and dispatch them to a region with available capacity.

  * **Pods running on Spot VMs:** run interruptible workloads on Spot VMs by adding tolerations and instructing GKE to distribute excess capacity in different zones.




### Additional best practices for flexibility, efficiency, and availability of compute capacity in GKE

Beyond hardware diversification, incorporate these GKE best practices to optimize cluster scaling success:

  * **Implement Pod overprovisioning (capacity buffers):** deploy low-priority "pause" Pods that reserve node capacity in advance. When high-priority AI workloads are submitted and regional capacity is constrained, Kubernetes immediately preempts the pause Pods, allowing containers to start up without waiting for new node provisioning. For more information, see [About capacity buffers](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/capacity-buffer).
  * **Use Flex-start with queued provisioning:** for large batch and AI model training jobs, use Flex-start with queued provisioning, which integrates with Kueue and Dynamic Workload Scheduler. Flex-start with queued provisions all-or-nothing atomic node allocation, which prevents partial cluster scale-up failures. For more information, see [Run a large-scale workload with flex-start with queued provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/provisioningrequest).
  * **Enable image streaming and container image preloading:** for large AI container images (such as PyTorch or TensorFlow images exceeding 10 GB), enable GKE Image streaming or use secondary boot disks for image preloading. This configuration reduces node warm-up time, which lets newly provisioned nodes start running workloads in seconds. For more information, see [Use Image streaming to pull container images](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming) and [Use secondary boot disks to preload data or container images](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/data-container-image-preloading).
  * **Set cluster autoscaler location policy to`ANY`:** configure node pools (especially for Spot VMs or flex-start) with the `ANY` location policy. This setting instructs the cluster autoscaler to search for requested capacity across all specified zones. Cluster autoscaler finds capacity over balancing node counts. For more information, see [Cluster autoscaler overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).
  * **Optimize accelerator utilization with GPU sharing:** for workloads that don't require a dedicated GPU, use GPU time-sharing, multi-instance GPUs (MIG), or NVIDIA MPS to allow multiple containers to share a single accelerator. This approach optimizes effective capacity across node pools. For more information, see [About GPU sharing strategies in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/timesharing-gpus).



## Use Compute Advisor

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Compute Advisor is an AI-powered interface in the Google Cloud console, powered by Gemini, that helps you design resilient and cost-effective architectures for GKE.

Compute Advisor provides near-real-time availability guidance for Flex-start VMs and Spot VMs, while verifying your organization's policies and resource quotas before deployment. Compute Advisor doesn't provide availability guidance for workloads that require on-demand resources.

To access Gemini in the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **Overview** page.

[Go to Overview](https://console.cloud.google.com/kubernetes/overview)

  2. In the **Design your infrastructure with Compute Advisor** section, submit a prompt. Gemini starts to generate a response.

**Caution:** Generative AI can make mistakes. Validate all recommendations and configurations before you take any actions on a resource that Gemini recommends you to create, modify, or delete.
  3. To generate architectural recommendations, run one of the following example prompts in Compute Advisor. When you click the **Run prompt in Compute Advisor** buttons, the Google Cloud console might take longer than 15 seconds to load:



  * **General accelerator strategy** :

_Use case:_ use this prompt to analyze regional capacity signals and receive recommendations on machine types, zones, and fallback scheduling strategies when designing cluster configurations.
        
        Configure a GKE cluster to improve chances of obtaining scarce GPU or TPU capacity.
        

[Run prompt in Compute Advisor](https://console.cloud.google.com/compute/advisor/?advisor_ref=gke_obtainability_strategy)

  * **Geographic flexibility and fallbacks** :

_Use case:_ use this prompt when designing multi-cluster architectures or global job queuing systems (for example, with Kueue) to shift workload execution across regions depending on resource availability.
        
        Configure multi-region fallbacks and geographic scheduling on GKE to increase GPU availability.
        

[Run prompt in Compute Advisor](https://console.cloud.google.com/compute/advisor/?advisor_ref=gke_geographic_flexibility)

  * **Priority reservation consumption** :

_Use case:_ use this prompt to generate YAML configuration patterns for Pod affinity and autoscaling rules that prioritize reservation capacity.
        
        Configure GKE autoscaling rules and Pod specs to prioritize consuming active reservations before scaling into on-demand pools.
        

[Run prompt in Compute Advisor](https://console.cloud.google.com/compute/advisor/?advisor_ref=gke_reservation_consumption)

  * **ComputeClasses for fallback prioritization** :

_Use case:_ use this prompt to generate the YAML manifest for a ComputeClass CustomResourceDefinition that prioritizes high-performance GPUs but includes lower-tier fallbacks to ensure workload scheduling.
        
        Define a ComputeClass manifest for GKE to prioritize A2 GPU nodes with automatic fallbacks to L4 or T4 GPUs.
        

[Run prompt in Compute Advisor](https://console.cloud.google.com/compute/advisor/?advisor_ref=gke_compute_class_fallbacks)

  * **Node pool auto-creation for diversification** :

_Use case:_ Use this prompt to write the YAML manifest for GKE cluster autoscaler resource limits and Pod affinity rules that enable NAP to provision alternative GPU or CPU nodes automatically.
        
        Configure GKE node pool auto-creation to diversify machine families and prevent pending pods when regional accelerator capacity is constrained.
        

[Run prompt in Compute Advisor](https://console.cloud.google.com/compute/advisor/?advisor_ref=gke_nap_diversification)




## What's next

  * [Design and optimize GKE clusters with Compute Advisor](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/design-with-gemini)
  * [Configure node pool auto-creation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning)
  * [Troubleshoot horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/horizontal-pod-autoscaling)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
