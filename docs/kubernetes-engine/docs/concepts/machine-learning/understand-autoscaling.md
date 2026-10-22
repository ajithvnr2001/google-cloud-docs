---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/understand-autoscaling/
title: Simplified autoscaling concepts for AI/ML workloads in GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:36.871202+00:00
---

# Simplified autoscaling concepts for AI/ML workloads in GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/understand-autoscaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Simplified autoscaling concepts for AI/ML workloads in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document provides an overview of autoscaling concepts for AI/ML workloads in Google Kubernetes Engine (GKE).

This document is intended for Machine learning (ML) engineers who are new to GKE. We recommend that you read the following documents in the series to ease into using GKE for AI/ML workloads:

  1. [Why use GKE for AI/ML inference](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/why-use-gke-ai-ml-overview)
  2. [About AI/ML model inference on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/inference)
  3. Simplified autoscaling concepts for AI/ML workloads in GKE (this document)



## Before you begin

You should have basic familiarity with the following concepts:

  * **[Fundamental Kubernetes objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/)** : understand what containers, Pods, and nodes are, and how they relate to each other.
  * **[Basic GKE cluster architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture)** : understand how various GKE cluster components interact with each other.



## The challenge: meeting peak demand

Cymbal Shops, a fictional online retailer, is preparing for its annual sales event. The store's AI-powered recommendation engine must provide real-time, personalized suggestions to a massive influx of online shoppers.

If the recommendation engine slows down, user experience suffers, and sales are lost. However, provisioning excessive server capacity isn't cost-effective during periods of normal traffic. The goal is to have resources scale automatically in response to demand, which helps ensure a good user experience while keeping costs under control.

## The solution: on-demand autoscaling

GKE autoscaling functions like a store manager preparing for a sales rush. Instead of keeping a massive building fully staffed and powered up all the time, the manager dynamically adjusts the store's entire capacity--staff, floor space, and equipment--to match shopper needs at any given time.

GKE applies this same principle: it automatically scales the resources allocated to your application (both workload and infrastructure) based on real-time demand.

## Business benefits of GKE autoscaling

By combining horizontal and vertical scaling strategies, GKE offers a robust approach that provides three core benefits:

  * **Cost optimization** : you pay only for the compute resources you use, and avoid the expense of over-provisioning. GKE autoscaling prevents waste by automatically right-sizing your applications to their actual CPU and memory requirements. It can also provision expensive, specialized hardware (like GPUs) only for the moments they are required, and removes them when the job is done.
  * **Enhanced reliability and performance** : your application can automatically scale out (add more copies) to handle sudden traffic spikes, ensuring stability for your users. At the same time, GKE's autoscaling helps prevent common "Out of Memory" (OOM) errors that can crash applications. For the demanding AI/ML jobs, it helps ensure that the necessary high-performance hardware is available to run efficiently and complete the jobs on time.
  * **Reduced operational overhead** : GKE's multi-dimensional autoscaling strategy significantly simplifies resource management. GKE automates the complex tasks of tuning resource requests and managing specialized node pools for different hardware. This automation frees up your engineering teams to focus on application development rather than infrastructure tuning.



## Workload autoscaling

Workload autoscaling automatically adjusts your application's power to match demand. GKE employs a two-tiered autoscaling system to manage your application's resources efficiently.

### Horizontal Pod Autoscaler (HPA): adding more resources

The Horizontal Pod Autoscaler (HPA) monitors the resource utilization of your application's Pods. In our analogy, the Pods are the "sales associates," and the HPA is the "team manager" observing how busy the sales associates are.

When the demand on the Pods increases, the HPA automatically provisions more Pods to distribute the load. When demand decreases, the HPA terminates idle Pods to conserve resources.

For more information, see [Horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler).

### Vertical Pod Autoscaler (VPA): making resources more powerful

While horizontal scaling focuses on increasing the quantity of resources, vertical scaling is a complementary strategy that focuses on increasing the power of existing resources. In the context of our offline store analogy, this is not about hiring more staff, but about enhancing the capabilities of the current team to improve their individual efficiency.

This approach of Pod-level vertical scaling is managed by the Vertical Pod Autoscaler (VPA). The VPA analyzes the resource consumption of your application and adjusts the Pod's CPU and memory requests up or down to match its actual usage.

The VPA can adjust a Pod's resource requests and limits, for example, by re-provisioning the Pod to scale from 1 CPU and 16 GB to 4 CPUs and 64 GB. This process involves restarting the Pod with its new, more capable configuration to better handle its workload.

For more information, see the following resources:

  * [Vertical Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler)
  * [Scale container resource requests and limits](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling)
  * [Rightsize HPA workloads with VPA](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rightsize-hpa-workloads-with-vpa)



HPA and VPA are complementary. HPA adjusts the number of Pods in response to changes in traffic, and VPA helps ensure each of those Pods is correctly sized for its task. These scaling strategies prevent wasted resources, avoid unnecessary costs, and help ensure your app remains responsive and available during traffic fluctuations. Unless you use [HPA rightsizing with VPA](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rightsize-hpa-workloads-with-vpa) (Preview) on CPU, avoid using HPA and VPA on the same metrics (CPU and memory) because they can conflict. For more information, see [Horizontal Pod autoscaling limitations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler#limitations).

## Infrastructure autoscaling

Infrastructure autoscaling automatically adds or removes hardware to match the demands of your workloads.

### Cluster autoscaler: the building manager

The cluster autoscaler helps ensure that there is sufficient underlying infrastructure (VMs, or nodes in GKE's context) to accommodate the Pods. The nodes can be compared to the "floors" of a store, where the cluster autoscaler is the "building manager."

If the HPA needs to add more Pods but the existing nodes lack available capacity on the existing nodes, the cluster autoscaler provisions a new node. Conversely, if any node becomes underutilized, the cluster autoscaler moves that node's Pods onto other nodes, and terminates the now-empty node.

For more information, see [Cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).

### Node pool auto-creation: the automation specialist

While the cluster autoscaler adds nodes to existing node pools, the node pool auto-creation extends the Cluster autoscaler's capability by letting it automatically create new node pools that match the specific needs of your Pods.

Certain AI/ML workloads require specialized, high-performance hardware like GPUs or TPUs that aren't available in general-purpose node pools. Node pool auto-creation fully automates provisioning this specialized hardware when your workloads require it. This helps ensure that even the most computationally intensive tasks get the hardware they need, when they need it.

For more information, see [About node pool auto-creation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning).

For the available accelerators in GKE, see the following:

  * [About GPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus)
  * [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus)



### ComputeClasses: the trigger for node pool auto-creation

Although node pool auto-creation can be triggered by a Pod's request for a specific hardware type (like `nvidia-l4-vws`), using a ComputeClass is the more resilient and modern method. A ComputeClass is a GKE resource you define that acts on a set of rules to control and customize how your hardware autoscales. While it's not an autoscaler itself, it works with the Cluster autoscaler.

To extend the analogy, think of ComputeClasses as a "smart requisition form" for your store's equipment.

Instead of a sales associate (your Pod) demanding a specific, rigid piece of hardware (for example, "I need the Brand X Model 500 cash register"), they request a _capability_ using the requisition form (for example, "I need a high-speed checkout station"). The form—the ComputeClass—contains a set of rules for the purchasing team (GKE) on how to fulfill that order.

ComputeClasses separate your Pod's request for hardware from GKE's action of provisioning it. Instead of your Pod demanding a specific machine (like `a3-highgpu-8g`), it can request a ComputeClass. The ComputeClass itself defines the "smart" logic, a prioritized list of rules that tells GKE how to fulfill that request.

For more information, see [About GKE ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-compute-classes).

For a deep-dive in ComputeClasses with real-world examples and YAML configurations, see the technical guide: [Optimizing GKE workloads with custom ComputeClasses](https://github.com/GoogleCloudPlatform/accelerated-platforms/blob/main/docs/guides/optimizing-gke-workloads-with-custom-compute-classes/README.md).

**Note:** If your need for specialized hardware is static and predictable, such as for a long-running training job, you can still manually create or update a node pool to use a specific machine type. The automated approach is designed for on-demand, dynamic scaling.

## Key metrics and triggers for autoscaling

To make informed scaling decisions, the autoscaling components monitor different signals. The following table shows the comparison of metrics-based autoscaling triggers.

Component | Reacts to | Signal source | Thought process | GKE's action  
---|---|---|---|---  
HPA | Current load | Real-time consumption, for example, the CPU is at 90% right now. | "The current Pods are overwhelmed. We need to distribute this traffic immediately." | Scales out or in: changes the number of Pod replicas to meet demand.  
VPA | Sizing efficiency | Historical consumption, for example, average RAM usage over the last 24h. | "This Pod's resource needs have changed, or our initial estimates were incorrect. We need to adjust its resource allocation to match its actual usage" | Scales up or down: changes the size (CPU or RAM limits) of the Pod to right-size it.  
Node pool auto-creation | Hardware availability | Unfulfilled requests, for example, the Pod is in "Pending" status because no GPU nodes exist. | "This Pod can't start because the physical hardware it requested is missing." | Provisions infrastructure: creates new node pools with the specific hardware.  
  
### Horizontal Pod Autoscaler (HPA) triggers: reacting to load

The HPA scales your number of Pods (scales in or out) by watching real-time performance metrics. For example, **CPU and memory utilization** , the fundamental metrics that indicate the processing load on your Pods, are available out-of-the-box for HPA.

However, some metrics need explicit configurations, such as the following:

  * **Load balancer metrics (Requests-per-second (RPS))** : a direct measure of application traffic, enabling faster scaling responses. To use this metric, see [Enable utilization-based load balancing and Performance HPA profile](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-ubb#enable-ubb).
  * **Custom metrics** : configure autoscaling based on custom business metrics, such as "number of active users", to proactively manage resources based on anticipated demand. To use custom metrics, you need to set up a metrics pipeline to expose them to the HPA. For more information, see [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus).



### Vertical Pod Autoscaler (VPA) triggers: reacting to resource needs

The VPA scales your Pod's size (scales up or down) by watching its historical resource consumption:

  * **CPU and memory utilization** : the VPA analyzes a Pod's past usage to determine if its request for resources is correct. The VPA's primary goal is to prevent resource contention by increasing or decreasing a Pod's memory and CPU requests to match its real needs.



### Node pool auto-creation triggers: reacting to hardware requests

Node pool auto-creation provisions new node pools with specialized hardware. It's not triggered by performance metrics like CPU load. Instead, it's triggered by a Pod's resource request:

  * **Unschedulable resource request** : a key trigger. When a Pod is created, it requests specific hardware. If the cluster can't fulfill this request because no existing node has that hardware, node pool auto-creation takes action.
  * **ComputeClass request** : a Pod requests a ComputeClass, for example, `cloud.google.com/compute-class: premium-gpu`. If no node in the cluster can provide the "premium-gpu" capabilities, node pool auto-creation automatically creates a new node pool that can provide those capabilities.



To learn how to use custom, Prometheus, and external metrics to achieve autoscaling, see [About autoscaling workloads based on metrics](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/custom-and-external-metrics).

## Conclusion

By applying these autoscaling strategies, you can effectively manage fluctuating AI/ML workloads. Just like the Cymbal Shops store manager navigated their peak sales event by flexibly managing their resources, you can use GKE autoscaling to automatically expand and contract your infrastructure and workload resources. This helps ensure your models remain performant during traffic spikes and cost-efficient during quiet periods, keeping your environment right-sized.

## What's next

  * Get an overview of [AI/ML inference workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/inference).
  * Learn how to [serve open LLMs on GKE with a pre-configured architecture](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-open-models-terraform).
  * Learn how to [apply ComputeClasses to Pods by default](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-pods-default-compute-classes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
