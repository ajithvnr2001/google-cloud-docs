---
url: https://docs.cloud.google.com/cluster-director/docs/overview/
title: Cluster Director overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:41:59.408878+00:00
---

# Cluster Director overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Cluster Director overview Stay organized with collections  Save and categorize content based on your preferences. 

Use Cluster Director to deploy, manage, and monitor clusters for running artificial intelligence (AI), machine learning (ML), or high performance computing (HPC) workloads. Cluster Director is a Google Cloud product that automates the complex setup and configuration of clusters, helping you configure compute, networking, and storage resources for your clusters to maximize performance and minimize downtimes.

Cluster Director is designed for IT administrators and AI researchers who want to avoid the overhead of managing a cluster, and instead focus on running their workloads.

## Cluster Director key features

Cluster Director integrates multiple Google Cloud services into a cohesive system that simplifies cluster management and provides the following features:

  * **Automated cluster lifecycle management** : the Cluster Director platform is built around a unified control plane with its own API and UI in the Google Cloud console. This feature is a central place to perform all cluster lifecycle operations, letting you programmatically deploy, manage, and scale clusters with all their necessary compute, networking, and storage resources.

  * **Managed cluster orchestration and scaling** : Cluster Director uses a managed Slurm environment for fault-tolerant and scalable job scheduling. This managed environment lets you dynamically scale your cluster by adding and editing machine configurations to an existing cluster to adjust resources based on your workload demands.

  * **Resilient, performance-optimized infrastructure** : clusters are built on a foundation of performance-optimized hardware, including compute-optimized and accelerator-optimized Compute Engine instances. The system uses topology-aware scheduling to colocate compute instances and minimize network latency. It also features built-in resiliency, with autohealing capabilities that automatically detect and replace failed compute instances to help minimize downtimes.

  * **Integrated observability** : Cluster Director provides built-in tools for monitoring the health, topology, and performance of your clusters through a dashboard in the Google Cloud console. These tools give you an at-a-glance view of your cluster's component health.




## Cluster Director use cases

Cluster Director is designed to meet the needs of the following use cases:

Use case | Example workloads  
---|---  
Large-scale AI workloads | 

  * Generative AI and large language model (LLM) training
  * Fraud detection
  * Recommendation models

  
HPC workloads | 

  * Complex simulations
  * Drug discovery, protein folding, and genomic analysis
  * Risk analysis and quantitative trading

  
  
## What's next

  * [Supported machine series in Cluster Director](https://docs.cloud.google.com/cluster-director/docs/compute)

  * [Try out Cluster Director](https://docs.cloud.google.com/cluster-director/docs/create/quickstart)

  * [Cluster creation process overview](https://docs.cloud.google.com/cluster-director/docs/create/process-overview)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
