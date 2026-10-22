---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/why-use-gke-ai-ml-overview/
title: Why use GKE for AI/ML inference \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:25.677474+00:00
---

# Why use GKE for AI/ML inference  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/why-use-gke-ai-ml-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Why use GKE for AI/ML inference Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document is the first part of a series that's intended for Machine learning (ML) engineers who are new to using Google Kubernetes Engine (GKE), and want to start running inference workloads on GKE as quickly as possible.

In this series, we won't attempt to teach you about all of the available GKE options. Instead, we provide you with the basic information that you need to know to get your workloads on GKE. This series includes the following documents:

  * Why use GKE for AI/ML inference (this document)
  * [About AI/ML model inference on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/inference)
  * [Simplified autoscaling concepts for AI/ML workloads in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/understand-autoscaling)



As an AI/ML platform engineer, you can use GKE to help you manage your model deployments. GKE is a service that lets you automate the deployment, scaling, and monitoring of your [Kubernetes-based](https://kubernetes.io/docs/home/) inference workloads and the computing infrastructure that your workloads run on. This document covers some of the key benefits of using GKE for model inference, including the following:

  * Consistent application performance
  * Streamlined access to specialized inference hardware
  * Automatic scaling of your inference workloads
  * Automated monitoring and logging of workload performance and health
  * Portability and flexibility of using open standards and open-source technologies



## Before you begin

Before you read this document, you should be familiar with the following:

  * [Fundamental Kubernetes concepts](https://docs.cloud.google.com/kubernetes-engine/docs/learn/get-started-with-kubernetes): learn about containers, Pods, nodes, and clusters; and how they relate to each other.
  * [GKE modes of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode): learn about Autopilot and Standard GKE clusters, their uses, and their differences.



## Package your models for consistent performance

Consistent and reliable model inference is crucial for your AI application, and GKE can reduce the operational complexity of managing inference at scale. By packaging your trained model, inference server, and all dependencies into a [container](https://cloud.google.com/learn/what-are-containers), you create a standardized, portable artifact that runs on GKE. Containerization helps reduce errors that are caused by mismatched dependencies or inconsistent environments. GKE automatically deploys and manages these containers. It handles tasks like restarting crashing workloads or reprovisioning resources to help stabilize the performance of your AI/ML workloads.

## Use GPUs and TPUs to reduce serving latency

Latency is an issue for inference workloads, and some complex models rely on hardware accelerators like [GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus) and [TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus) to accelerate inference serving. GKE streamlines the process of using GPUs or TPUs for your latency-sensitive inference workloads by simplifying hardware provisioning and management. You choose the specific hardware configurations that best fit your requirements for performance and cost, and GKE [automatically provisions nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning) with your selected hardware to run your workloads. GKE also automates setup steps that typically require manual configuration in Kubernetes, such as installing NVIDIA drivers. For more fine-grained control over node configuration, you can use [custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes) to create specific, reusable hardware profiles that GKE uses when it provisions nodes.

GKE also offers resource management capabilities so that you can more efficiently use TPU and GPU resources for inference serving. For example, you can improve GPU utilization by hosting multiple models on a single GPU server by using [GPU sharing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/timesharing-gpus), or reduce costs for fault-tolerant inference jobs by running them on [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot) with accelerators. For small to medium-sized workloads with fluctuating demand requirements or short durations, you can use [Flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws), which provides a flexible and cost-effective technique to consume specialized compute resources, like GPUs or TPUs. These capabilities help you maximize your use of accelerator resources while optimizing for both serving latency and cost.

## Handle fluctuating traffic patterns automatically

Traffic and load on real-time inference workloads can be unpredictable and dynamic. A spike in demand might lead to increased latency and reduced performance. GKE offers a multi-layered approach to autoscaling so that you can automatically add or remove resources to meet variable inference demand. For example, you can use the [Horizontal Pod Autoscaler (HPA)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler) to automatically adjust the number of Pods in a Deployment, or [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) to automatically adjust the number of nodes in an existing node pool. By using GKE autoscaling capabilities, you can efficiently match the amount resources that your inference workload needs to the amount of application demand.

## Monitor the health and performance of your inference workload

GKE is integrated with the Google Cloud observability suite ([Cloud Logging](https://docs.cloud.google.com/logging/docs) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs)), and you can use [built-in observability features](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/observability) to monitor the health and performance of your inference workloads. These observability features give you insight and visibility into how your workload is performing after you deploy it. For example, you might wonder whether your model is working as expected, or whether your workload meets your requirements for latency and accuracy.

GKE automatically reports infrastructure metrics like CPU, memory, and accelerator utilization. To answer questions about model-specific performance, you can use [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) or send [custom metrics](https://docs.cloud.google.com/monitoring/custom-metrics) from your inference application to Cloud Monitoring. For example, you can [configure automatic application monitoring](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-automatic-application-monitoring) and monitor key inference metrics, such as requests per second (RPS); monitor concept drift by analyzing model-specific metrics, such as input data distribution; and debug issues by conducting historical log analysis.

## Use GKE for portability and flexibility

By using open standards like containers and open-source technologies like Kubernetes, GKE gives you the freedom to move your inference serving workloads to different locations–and use different resources and tools–as your requirements change. For example, you can develop and test your inference application on GKE, and then deploy that same containerized application to your on-premises environment for production.

In conclusion, you can use GKE to streamline how you move your AI/ML models from development to production. GKE handles many complexities that are involved with infrastructure management, which means that you can focus on running your inference workloads on a performant, scalable, and observable environment. As you go through this series, you will learn how you can use GKE to transform your AI/ML models into powerful, production-ready applications.

## What's next

  * [About AI/ML model inference on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/inference) (the next document in this series)
  * [Learn best practices for running inference workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference)
  * [Learn how to serve a model with a single GPU in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/online-ml-inference)
  * [Learn how to serve open LLMs on GKE with a pre-configured architecture](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-open-models-terraform)
  * [Learn how to serve open LLMs on GKE using TPUs with a pre-configured architecture](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-open-models-tpu-terraform)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
