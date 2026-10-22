---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-ai-conformance/
title: About GKE AI conformance \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:47.725798+00:00
---

# About GKE AI conformance  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-ai-conformance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  About GKE AI conformance Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document explains what the Kubernetes AI conformance program is, why it's important for your AI/ML workloads on Google Kubernetes Engine (GKE), and how you can set up conformant GKE clusters. 

## Why AI conformance matters for your GKE clusters

The [Kubernetes AI conformance program](https://github.com/cncf/ai-conformance) defines a standard for Kubernetes clusters to ensure they can reliably and efficiently run AI and ML workloads. Setting up a Kubernetes cluster for AI/ML can be complex. It often involves navigating a landscape of specific driver installations, API versions, and potential workarounds for unexpected bugs.

A conformant platform like GKE is designed to handle these underlying complexities for you, providing a path from setup to deployment. By building on a conformant GKE version, you can be confident that your environment is optimized for criteria like the following:

  * **Scalability** : efficiently scale your AI/ML workloads up and down based on demand.
  * **Performance** : get the most out of your hardware, including GPUs and TPUs.
  * **Portability** : run your AI/ML applications on any conformant Kubernetes cluster with minimal changes.
  * **Interoperability** : integrate with other tools and frameworks in the AI/ML ecosystem.



## How to create an AI-conformant GKE cluster

To create an AI-conformant GKE cluster, you need to do the following:

  1. Check the [`ai-conformance` GitHub repository](https://github.com/cncf/ai-conformance) to view the list of conformant versions.
  2. Create a GKE cluster in [Standard mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode) running on a conformant version, such as 1.34.0-gke.1662000 or later.
  3. [Enable Gateway API on your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#enable-gateway).



Your cluster now meets the mandatory requirements for Kubernetes AI conformance.

## What makes GKE a Kubernetes AI conformant platform

GKE manages the underlying requirements for AI conformance so you don't have to. The following table highlights some of these key features for AI/ML workloads. Some of these features are enabled by default, but others, like [Kueue](https://kueue.sigs.k8s.io/) for gang scheduling, are optional additions that you can install to enhance your AI/ML workloads.

The Kubernetes AI conformance program is designed to evolve with the AI/ML ecosystem. The requirements are updated with each Kubernetes minor version release based on the state of the ecosystem. For the full set of requirements for a specific minor version, in the [`ai-conformance` GitHub repository](https://github.com/cncf/ai-conformance), see the `docs/AIConformance-MINOR_VERSION.yaml` file, where `MINOR_VERSION` is your specific version, such as `v1.34`.

Requirement  
---  
Dynamic resource allocation (DRA) | Enables more flexible and fine-grained resource requests beyond counts. For more information, see [About dynamic resource allocation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-dynamic-resource-allocation).  
Kubernetes Gateway API | Provides advanced traffic management for inference services, which enables capabilities like weighted traffic splitting and header-based routing. For more information, see [About GKE Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api).  
Gang scheduling | Ensures all-or-nothing scheduling for distributed AI workloads. GKE allows for the installation and successful operation of at least one gang scheduling solution. For an example, see [Deploy a batch system using Kueue](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/kueue-intro).  
Cluster autoscaler for accelerators | Scales node groups that contain specific accelerator types up and down, based on pending Pods requesting those accelerators. For more information, see: 

  * [About GKE cluster autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler). 
  * [About custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes). 

  
Horizontal Pod Autoscaler (HPA) for accelerators |  Functions correctly for Pods utilizing accelerators, including the ability to scale these Pods based on custom metrics relevant to AI/ML workloads. For more information, see: 

  * [Configure autoscaling for LLM workloads on GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/autoscaling).
  * [Configure autoscaling for LLM workloads on TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/autoscaling-tpu).

  
Accelerator performance metrics |  Exposes fine-grained performance metrics by using a standardized, machine-readable format metrics endpoint. For more information, see: 

  * [Monitor your GPU node workload performance](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus#monitoring).
  * [Observability and metrics for TPU workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#metrics).

  
Standardized monitoring | Provides a monitoring system capable of discovering and collecting metrics from workloads that expose them in a standard format (for example, Prometheus exposition format). For more information, see [Observability for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/observability).  
AI operator support | Must prove that at least one complex AI operator with a custom resource definition (CRD) can be installed on the platform and that it functions reliably. For more information, see [Building a Machine Learning Platform with Kubeflow and Ray on Google Kubernetes Engine](https://cloud.google.com/blog/products/ai-machine-learning/build-a-ml-platform-with-kubeflow-and-ray-on-gke).  
  
## What's next

  * Explore the [Kubernetes AI conformance repository](https://github.com/cncf/ai-conformance) for more details on the program.
  * Read the [Introduction to AI/ML workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning).
  * Learn more about [AI model inference on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/inference#examples) and [try inference examples](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/inference#examples).
  * [Try an example of training a model on GPUs with GKE Standard mode](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/train-model-gpus-standard). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
