---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multi-cluster-inference-gateway/
title: About multi-cluster GKE Inference Gateway \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:55.324859+00:00
---

# About multi-cluster GKE Inference Gateway  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multi-cluster-inference-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  About multi-cluster GKE Inference Gateway Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

The multi-cluster Google Kubernetes Engine (GKE) Inference Gateway load balances your AI/ML inference workloads across multiple GKE clusters. It integrates GKE multi-cluster gateways for cross-cluster traffic routing with Inference Gateway for AI/ML model serving. This integration improves the scalability and high availability of your deployments. This document explains the gateway's core concepts and benefits.

For more information about how to deploy multi-cluster GKE Inference Gateway, see [Set up the GKE multi-cluster Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multicluster-inference-gateway).

To understand this document, you must be familiar with the following:

  * [AI/ML orchestration on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra).
  * [Generative AI terminology](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/glossary-genai).
  * [GKE networking concepts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview) including [Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service), [GKE multi-cluster gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways), and the [Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api).
  * [Load balancing in Google Cloud](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview), especially how load balancers interact with GKE.



This document targets the following personas:

  * Machine learning (ML) engineers, Platform admins and operators, and Data and AI specialists interested in using Kubernetes container orchestration capabilities for serving AI/ML workloads.
  * Cloud architects or Networking specialists who interact with Kubernetes networking.



To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE Enterprise user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Benefits of the GKE multi-cluster Inference Gateway

The multi-cluster GKE Inference Gateway provides several benefits for managing your AI/ML inference workloads, including the following:

  * Enhances high availability and fault tolerance through intelligent load balancing across multiple GKE clusters, even across different geographical regions. Your inference workloads remain available, and the system automatically reroutes requests if a cluster or region experiences issues, thereby minimizing downtime.
  * Improves scalability and optimizes resource usage by pooling GPU and TPU resources from various clusters to handle increased demand. This pooling allows your workloads to burst beyond the capacity of a single cluster and efficiently use available resources across your fleet.
  * Maximizes performance with globally optimized routing. The gateway uses advanced metrics, such as Key-Value (KV) Cache usage from all clusters, to make efficient routing decisions. This approach helps to ensure that requests go to the cluster best equipped to handle them, thereby maximizing overall performance for your AI/ML inference fleet.



## Limitations

The multi-cluster GKE Inference Gateway has the following limitations:

  * **Model Armor integration** : the multi-cluster GKE Inference Gateway doesn't support [Model Armor](https://docs.cloud.google.com/model-armor/overview) integration.

  * **Network Endpoint Group (NEG) limits** : has a limit of 50 NEGs per Google Cloud Backend Service. When using a multi-port InferencePool, each port in each zone creates a dedicated NEG. For example, an InferencePool with eight ports in a typical regional cluster (three zones) generates 24 NEGs. Therefore, a multi-cluster gateway can only aggregate such an InferencePool from a maximum of two clusters (two clusters × 24 NEGs = 48 NEGs) before reaching the 50 NEG limit.

  * VPC networks: all target clusters and the config cluster must be in the same VPC network. Cross-VPC load balancing isn't supported.




## Key components

The multi-cluster GKE Inference Gateway uses several Kubernetes custom resources to manage inference workloads and traffic routing:

  * **InferencePool** : groups identical model server backends in your target cluster. This resource simplifies the management and scaling of your model serving instances. Multi-port InferencePool objects are supported in single and multi-cluster deployments.
  * **`InferenceObjective`** : defines routing priorities for specific models within an InferencePool. This routing helps to ensure that certain models receive traffic preference based on your requirements.
  * **`GCPInferencePoolImport`** : makes your model backends available for routing configuration by using `HTTPRoute` in the config cluster. This resource is automatically created in your config cluster when you export an InferencePool from a target cluster. The config cluster acts as the central point of control for your multi-cluster environment.
  * **`GCPBackendPolicy`** : customizes how traffic is load balanced to your backends. For example, you can enable load balancing based on custom metrics or set limits on in-flight requests per endpoint to protect your model servers.
  * **`AutoscalingMetric`** : defines custom metrics, such as `vllm:kv_cache_usage_perc`, to export from your model servers. You can then use these metrics within `GCPBackendPolicy` to make more intelligent load balancing decisions, and optimize performance and resource utilization.



## How the multi-cluster GKE Inference Gateway works

The multi-cluster GKE Inference Gateway manages and routes traffic to your AI/ML models deployed across multiple GKE clusters. It works as follows:

  * **Centralized traffic management:** a dedicated _config cluster_ defines your traffic routing rules. The config cluster acts as the central point of control for your multi-cluster environment. You designate a GKE cluster as the config cluster when you enable multi-cluster Ingress for your fleet. This centralized approach lets you manage how requests are directed to your models across your entire fleet of GKE clusters from a single place.
  * **Flexible model deployment:** your actual AI/ML models run in separate _target clusters_. This separation lets you deploy models where it makes the most sense (for example, closer to data or to clusters with specific hardware).
  * **Easy integration of models:** when you deploy a model in a target cluster, you group its serving instances using an InferencePool. Exporting this InferencePool automatically makes it available for routing in your config cluster.
  * **Intelligent load balancing:** the gateway doesn't only distribute traffic; it makes intelligent routing decisions. By configuring it to use various signals, including custom metrics from your model servers, the gateway helps to ensure that incoming requests are sent to the best-equipped cluster or model instance, which can maximize performance and resource utilization. For example, you can route requests to the cluster with the most available inference capacity based on metrics like Key-Value (KV) Cache usage.



## What's next

  * To deploy the gateway, see [Set up the multi-cluster GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multicluster-inference-gateway).
  * To learn how to use the `scopes` field in the `GCPBackendPolicy` resource, see [Customize backend configurations with `GCPBackendPolicy` scopes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-backend-multicluster-inference-gateway).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
