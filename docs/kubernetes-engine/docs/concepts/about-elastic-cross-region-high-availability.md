---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-elastic-cross-region-high-availability/
title: About elastic cross-region high availability \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:12.211544+00:00
---

# About elastic cross-region high availability  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-elastic-cross-region-high-availability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  About elastic cross-region high availability Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

You can achieve elastic cross-region high availability for demanding AI inference workloads on Google Kubernetes Engine (GKE) to efficiently and reliably access accelerator capacity across different Google Cloud regions. This solution uses the GKE Multi-Cluster Inference Gateway and GKE autoscaling features, enabling your workloads to access and scale with accelerator capacity across various regions. This approach enhances resource availability, scalability, and resilience for your AI applications. This document describes the benefits, key components, and overall mechanics of how elastic cross-region high availability works.

Before you read this document, you should be familiar with the following:

  * [GKE Multi-Cluster Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multi-cluster-inference-gateway)
    * [Utilization-based balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-ubb)
  * [Preferred backends](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services#preferred_location_policy) for advanced load balancing options
  * [GKE cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler)
  * [Configuring horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling)



This document is for the following personas:

  * Machine learning (ML) engineers, platform administrators and operators, and data and AI specialists interested in using Kubernetes for serving AI/ML workloads
  * Cloud architects or networking specialists who interact with Kubernetes networking



To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE Enterprise user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Benefits of elastic cross-region high availability

Elastic cross-region high availability provides several key benefits for managing your AI/ML inference workloads, including the following:

  * **Greater capacity and scalability:** overcome single-region accelerator shortages by pooling GPU or TPU resources from multiple clusters across different regions. You can also use different accelerator types to further expand the capacity pool. This approach lets your AI inference workloads burst beyond the capacity of any single region or accelerator type, automatically tapping into available resources in your fleet, regardless of region.
  * **Automated spillover and enhanced reliability and availability:** the Gateway intelligently routes traffic, prioritizing preferred regions or clusters. When capacity limits are reached in one location, traffic automatically spills over to other locations that have available resources. This approach, combined with multi-region deployments, enhances high availability and fault tolerance because the system can bypass clusters or regions that are experiencing issues.
  * **AI-optimized traffic distribution:** use Utilization-Based Load Balancing with custom AI-specific metrics, such as key-value cache usage. This setup ensures globally optimized routing decisions. AI-optimized traffic distribution sends requests to the backends that are equipped to handle them, which enhances maximizing performance and helps to prevent overload across your Multi-Cluster Inference fleet.



## How elastic cross-region high availability works

Elastic cross-region high availability on GKE enables your AI inference workloads to automatically use accelerator capacity (such as GPUs or TPUs) across multiple Google Cloud regions. When your primary region experiences capacity constraints for required resources, this solution intelligently routes traffic and scales workloads to other regions with available capacity, while respecting your defined preferences.

The following explains key components of elastic cross-region high availability and how they work together:

  * **Multi-Cluster Inference Gateway** : your inference application is deployed across multiple GKE clusters in different regions. These clusters are managed as part of a GKE fleet. A GKE Multi-Cluster Inference Gateway (MCG) is configured with an Internal Load Balancer, which provides a single, private endpoint for your inference requests. This gateway is aware of your service deployments across all clusters in the fleet.
  * **Utilization-based balancing** : instead of using basic request rates, the load balancer distributes traffic based on real-time custom utilization metrics reported from your model servers. For AI inference, this is often a metric such as KV cache utilization, which reflects the actual load on the server.
  * **Location and resource preferences** : you can configure which regions or zones are permitted to run your AI inference workloads during cluster creation, and you can specify a preference order using the following: 
    * **`GCPBackendPolicy`** : this policy is attached to the gateway and lets you define preferred backends. You can specify which regions (that is, clusters) the load balancer should prioritize sending traffic to. This policy is typically aligned with where you have reserved capacity or where you have lower latency requirements.
    * **Custom Compute Class (optional, if you use node pool auto-creation)** : within each individual GKE cluster, you can use custom ComputeClass objects to define preferred node types, including machine types (for example, `a3-highgpu-8g`), capacity types (such as reserved, on-demand, and spot), and even preferred zones within that region.
  * **Dynamic scaling and traffic routing** : traffic is scaled and routed according to the following process: 
    * Incoming requests reach the Multi-Cluster Ingress Gateway's Internal Load Balancer.
    * The load balancer, guided by the `GCPBackendPolicy`, sends traffic to backends in your preferred regions first.
    * Traffic is distributed within a region and across backends based on the custom utilization metrics.
    * The Horizontal-Pod-Autoscaler (HPA) in each cluster scales the number of model server Pods up or down based on the same utilization metrics
    * GKE Cluster Autoscaler and node auto-provisioning, guided by the custom ComputeClass, add or remove nodes of the preferred types and zones to meet the scaling demands of the Pod.
  * **Elastic cross-region high availability in action** : if the model servers in the preferred regions become fully utilized (that is, with no additional capacity available), the load balancer automatically spills over traffic to clusters in other configured regions that have available capacity. The HPA and Cluster Autoscaler then scale up resources in those fallback regions as needed.



## What's next

  * Learn how to deploy an elastic cross-region high availability solution in [Configure elastic cross-region high availability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-elastic-cross-region-high-availability).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
