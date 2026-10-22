---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/choose-lb-strategy/
title: Choose a load balancing strategy for AI/ML model inference on GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:24.111988+00:00
---

# Choose a load balancing strategy for AI/ML model inference on GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/choose-lb-strategy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Choose a load balancing strategy for AI/ML model inference on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page helps you choose the appropriate load balancing strategy for AI/ML model inference workloads on Google Kubernetes Engine (GKE).

This page is intended for the following personas:

  * Machine learning (ML) engineers, Platform admins and operators, and Data and AI specialists who are interested in using Kubernetes container orchestration capabilities for serving AI/ML workloads.
  * Cloud architects and Networking specialists who interact with Kubernetes networking.



To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/anthos/docs/concepts/roles-tasks).

Before you read this page, ensure that you're familiar with the following:

  * [GKE networking concepts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview)
  * [GKE Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api)
  * [Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



When you deploy AI/ML model inference workloads on GKE, choose the right load balancing strategy to optimize performance, scalability, and cost-effectiveness:

  * Choose [GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway) for optimized routing and load balancing for serving AI/ML workloads.
  * Choose GKE Gateway with custom metrics, which uses [ Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/applb-custom-metrics). This option provides general-purpose control and lets you configure traffic distribution based on metrics specific to your application or infrastructure requirements.



## GKE Inference Gateway overview

GKE Inference Gateway optimizes and manages demanding Generative AI (GenAI) and complex Large Language Model (LLM) inference workloads. It extends the GKE Gateway API, offering several key advantages:

  * **Intelligent, AI-aware routing:** GKE Inference Gateway monitors critical AI-specific metrics, including:

    * Model server KV cache utilization
    * Pending request queue length
    * Overall GPU/TPU utilization
    * LoRA adapter availability
    * The computational cost of individual requests Based on these metrics, the gateway intelligently distributes traffic to the most suitable and least loaded model server replica.
  * **Request prioritization:** The gateway provides mechanisms to prioritize requests.

  * **Optimized autoscaling:** The gateway offers optimized autoscaling mechanisms for model servers.




## GKE Gateway with Custom Metrics overview

Google Cloud offers Application Load Balancer resources that support scopes like global external and regional external. These general-purpose load balancers distribute traffic based on custom metrics reported by your backend services. This approach provides fine-grained control over load distribution, enabling you to base it on application-specific performance indicators.

## Compare GKE Inference Gateway and GKE Gateway with Custom Metrics

Use the following table to compare the features of GKE Inference Gateway and GKE Gateway with Custom Metrics and choose the right load balancing solution for your AI/ML inference workloads on GKE.

Feature | GKE Inference Gateway | GKE Gateway with Custom Metrics (via Application Load Balancers)  
---|---|---  
Primary use case | Optimizes Generative AI and machine learning inference workloads on Kubernetes, including serving Large Language Models (LLMs). It helps ensure fair access to model resources and optimizes latency-sensitive, GPU or TPU-based LLM workloads. | Provides general-purpose HTTP(S) load balancing, distributing traffic based on custom, application-reported metrics. Such load balancing is ideal for latency-sensitive services, such as real-time gaming servers or high-frequency trading platforms, that report custom utilization data.  
Base routing | Supports standard HTTP(S) routing based on host and path, extending the GKE Gateway API. | Supports standard HTTP(S) routing based on host and path. You configure this using the GKE Gateway API's standard resources.  
Advanced routing logic | Provides advanced capabilities such as model-aware routing, traffic splitting, mirroring, and the application of priority and criticality levels to requests. | Balances traffic based on custom metrics reported by the application through the Open Request Cost Aggregation (ORCA) standard. This enables policies like `WEIGHTED_ROUND_ROBIN` for endpoint weighting within a locality.  
Supported metrics | Utilizes a suite of native, AI-specific metrics, such as GPU or TPU utilization, KV cache hits, and request queue length. It can also be configured to use application-reported metrics using a standardized HTTP header mechanism. | Relies on application-reported metrics using a standardized HTTP header mechanism, specifically [Open Request Cost Aggregation (ORCA)](https://github.com/cncf/xds/blob/main/source/common/orca.proto) load reporting. This mechanism supports standard metrics like CPU and memory, as well as custom-named metrics for application-specific constrained resources.  
Request handling | Designed to handle workloads with non-uniform request costs, which are common in LLMs due to varying prompt complexities. It supports request [criticality levels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway#traffic-distribution), allowing for prioritization of different types of inference requests. | Best suited for workloads where individual requests have relatively uniform processing costs. This solution doesn't include native request prioritization capabilities.  
LoRa adapter support | Offers native, affinity-based routing to backends equipped with specific LoRa adapters, which helps ensure that requests are directed to the appropriate resources. | Does not provide native support for LoRa adapters or affinity-based routing based on LoRa configurations.  
Autoscaling integration | Optimizes autoscaling for model servers by leveraging AI-specific metrics, such as KV cache utilization, to make more informed scaling decisions. | Integrates with the Horizontal Pod Autoscaler (HPA) using [custom and external metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autoscale-using-metrics). These metrics are reported to the Application Load Balancer and are used in a generic manner for scaling, based on the reported load signals.  
Setup and configuration | Configure it with the GKE Gateway API. Extends the standard API with specialized `[InferencePool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway#understand_key_concepts)` and `[InferenceModel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway#understand_key_concepts)` Custom Resource Definitions (CRDs) to enable its AI-aware features. | You configure this solution using the standard resources of the GKE Gateway API. The application must implement an HTTP header-based mechanism, such as Open Request Cost Aggregation (ORCA), to report custom metrics for load balancing.  
Security | This solution includes AI-content filtering using [Model Armor](https://docs.cloud.google.com/security-command-center/docs/model-armor-overview) at the gateway level. It also leverages foundational GKE security features, such as TLS, Identity and Access Management (IAM), role-based access control (RBAC), and namespaces. | This solution uses the standard Application Load Balancer security stack, which includes [Google Cloud Armor](https://cloud.google.com/security/products/armor), TLS termination, and IAM. To enable AI-content filtering, you can integrate Google Cloud Armor as a Service Extension.  
Observability | Offers built-in observability into AI-specific metrics, including GPU or TPU utilization, KV cache hits, request queue length, and model latency. | Observability relies on any custom metrics the application is configured to report. You can view these in [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs). These can include standard or custom-named metrics.  
Extensibility | Built on an extensible, open-source foundation, allowing for a user-managed Endpoint Picker algorithm. It extends the GKE Gateway API with specialized [Custom Resource Definitions (CRDs)](/kubernetes-engine/docs/how-to/deploy-gke-inference-gateway), such as `InferencePool` and `InferenceModel`, to simplify common AI use cases. | Designed for flexibility, allowing you to extend load balancing using any [custom metric (load signal)](/load-balancing/docs/https/applb-custom-metrics) that the application reports using the ORCA standard.  
Launch stage | [GA](https://cloud.google.com/products#product-launch-stages) | [GA](https://cloud.google.com/products#product-launch-stages)  
  
## When to use GKE Inference Gateway

Choose GKE Inference Gateway to optimize sophisticated AI and machine learning inference workloads on GKE, especially for Large Language Models (LLMs). We recommend this solution in the following situations:

  * **Serving LLMs:** you need routing decisions based on LLM-specific states, such as KV cache utilization or request queue length, when using model servers like vLLM.
  * **Deploying models with LoRa adapters:** you require intelligent, affinity-based routing to backends equipped with the correct and available LoRa adapters.
  * **Handling inference requests with highly variable processing costs:** for example, dynamic prompt sizes or complexity necessitate a cost-aware load balancer.
  * **Implementing request prioritization:** you need to prioritize different classes of inference traffic, such as critical, standard, or sheddable requests.
  * **Optimizing autoscaling:** you want an autoscaling mechanism tightly coupled with specific performance metrics of Generative AI (GenAI) model servers, such as KV cache utilization, for more informed scaling decisions.
  * **Utilizing Model Armor integration:** you need to use Model Armor for AI safety checks at the gateway level.
  * **Gaining out-of-the-box observability:** you require built-in observability for critical AI-specific metrics, including GPU or TPU utilization, KV cache hits, and request queue length.
  * **Simplifying GenAI deployments:** you prefer a purpose-built solution that simplifies common GenAI deployment patterns on GKE, while retaining options for future customization through its extensible GKE Gateway API foundation.



## When to use GKE Gateway with Custom Metrics

To achieve flexible, general-purpose load balancing based on your application's unique performance indicators, use GKE Gateway with Custom Metrics. This approach enables load distribution based on unique, application-defined performance indicators, including specific inference scenarios. We recommend this in the following scenarios:

  * Your workload has a high volume of traffic with relatively uniform processing costs per request.
  * Load distribution can be effectively managed by one or two specific custom metrics reported by the application, typically through HTTP response headers using the Open Request Cost Aggregation (ORCA) load reporting standard.
  * Your load balancing requirements don't depend on GenAI or LLM-specific features.
  * Your operational model doesn't require the specialized AI-specific intelligence provided by GKE Inference Gateway, avoiding unnecessary architectural complexity.
  * Maintaining consistency with existing Application Load Balancer deployments is a priority, and these deployments meet the inference service's load balancing requirements.



## What's next

  * Learn about [GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway).
  * Learn about [Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/applb-custom-metrics).
  * Explore experimental samples for leveraging GKE to accelerate your AI/ML initiatives in [GKE AI Labs](https://gke-ai-labs.dev/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
