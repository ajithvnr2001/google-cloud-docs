---
url: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/
title: Best practices for GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:49.305290+00:00
---

# Best practices for GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Best practices for GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document provides a consolidated overview of best practices for designing, building, and operating applications on Google Kubernetes Engine (GKE). Following these recommendations helps you optimize for cost, performance, security, and reliability. Each entry links to more detailed documentation for specific topics.

Select a category of best practices: AI and ML workloadsCost optimizationDatabasesNetworkingOperationsReliability and scalabilitySecurity

Category | Best practices | Summary  
---|---|---  
AI and ML workloads | [Optimize AI/ML workload efficiency](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/optimize-ai-utilization) | Maximize resource efficiency for AI/ML tasks on GKE.  
AI and ML workloads | [Inference workloads](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference) | Run machine learning inference workloads on GKE.  
AI and ML workloads Reliability and scalability | [Autoscale LLM inference with GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling) | Automatically scale large language model (LLM) inference using GPUs on GKE.  
AI and ML workloads Reliability and scalability | [Autoscale LLM inference with TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling-tpu) | Automatically scale large language model (LLM) inference using TPUs on GKE.  
AI and ML workloads | [Optimize LLM inference with GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/llm-optimization) | Optimize LLM inference with GPUs on GKE.  
AI and ML workloads | [Batch processing platform](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/batch-platform-on-gke) | Build and operate a batch processing platform on GKE.  
Cost optimization | [Design and configure clusters for cost optimization](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/cost-optimization) | Implement high-value configurations and strategies to operate resource-efficient clusters.  
Databases | [Database options](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/database-options) | Choose and manage database solutions for GKE applications.  
Networking | [Networking](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/networking) | Configure and manage network connectivity for GKE.  
Networking | [Network observability](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/network-observability) | Implement network observability, alerting, and cost optimization for GKE.  
Operations | [Upgrading clusters](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/upgrading-clusters) | Learn how to perform smooth and reliable GKE cluster upgrades.  
Operations | [CI/CD for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/best-practices-continuous-integration-delivery-kubernetes) | Implement continuous integration and delivery pipelines for GKE applications.  
Reliability and scalability | [Scalability](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/scalability) | Learn principles and techniques for scaling applications on GKE.  
Reliability and scalability | [Plan for scalability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-scalability) | Learn strategies for designing scalable GKE environments.  
Reliability and scalability | [Plan large GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-clusters) | Learn how to architect and manage large-scale GKE clusters.   
Reliability and scalability | [Best practices for ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/computeclasses) | Best practices to improve reliability, scalability, security, and performance for ComputeClasses.  
Reliability and scalability | [Best practices for running HPC workloads](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/run-hpc) | Best practices to optimize running high performance computing (HPC) workloads on GKE.  
Reliability and scalability | [Plan large workloads](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-workloads) | Deploy and manage resource-intensive applications.  
Security | [Harden your GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster) | Enhance the GKE security posture of your GKE clusters.  
Security | [Plan RBAC policies](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/rbac) | Define role-based access control to manage permissions.  
Security | [Enterprise multi-tenancy](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/enterprise-multitenancy) | Run multiple tenants securely on a single GKE cluster.  
Security | [Best practices for AI workload security on GKE](https://docs.cloud.google.com/kubernetes-engine/security/ai-security-best-practices) | Improve the security of infrastructure, models, and Kubernetes applications that form your AI deployments.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
