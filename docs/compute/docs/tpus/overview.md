---
url: https://docs.cloud.google.com/compute/docs/tpus/overview/
title: About TPUs on Google Cloud \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:17:39.753705+00:00
---

# About TPUs on Google Cloud  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/tpus/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About TPUs on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Tensor Processing Units (TPUs) are Google's custom-developed, application-specific integrated circuits (ASICs) designed to accelerate machine learning (ML) and artificial intelligence (AI) workloads. Whether you are training complex foundation models for weeks or running large-scale inference, TPUs offer scalable, specialized computing resources optimized for frameworks like JAX and PyTorch.

Cloud TPUs are engineered to tackle the most demanding AI workloads. The key benefits include:

  * **Optimized for matrix computations** : TPUs are specifically designed with Matrix Multiply Units (MXUs) to execute the massive matrix operations fundamental to ML algorithms with exceptional efficiency.

  * **High-bandwidth memory (HBM)** : On-chip high-bandwidth memory lets you train and serve larger models and effectively utilize larger batch sizes.

  * **Massive scalability with slices** : TPU chips can be connected in groups called slices. The slices let your workloads achieve scaling up to thousands of TPU chips for massive training jobs.




## When to use TPUs

TPUs are optimized for specific workloads, such as the following:

  * Models dominated by matrix computations
  * Models with no custom PyTorch/JAX operations inside the main training loop
  * Models that train for weeks or months
  * Large models with large effective batch sizes
  * Models with ultra-large embeddings common in advanced ranking and recommendation workloads



TPUs are _not_ suited to the following workloads:

  * Linear algebra programs that require frequent branching or contain many element-wise algebra operations
  * Workloads that require high-precision arithmetic
  * Neural network workloads that contain custom operations in the main training loop



## Provisioning options on Google Cloud

You can access and provision TPUs by using the following Google Cloud products depending on your operational needs.

### Compute Engine

Compute Engine lets you create and manage individual TPU VMs or slices, providing you with the capability for full lifecycle management of TPU VMs. Google recommends that you use Compute Engine over the legacy Cloud TPU API to provision your TPU resources.

To learn more, see [Cloud TPU resources in Compute Engine](https://docs.cloud.google.com/compute/docs/tpus/tpu-resources-in-compute-engine).

### Google Kubernetes Engine

Google Kubernetes Engine (GKE) provides a fully managed, multi-tenant Kubernetes environment for orchestrating large-scale AI workloads. GKE supports TPU node and node pool lifecycle management, including creating, configuring, and deleting TPU VMs.

To learn more, see [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).

### Cloud TPU

The [Cloud TPU API](https://docs.cloud.google.com/tpu/docs/intro-to-tpu#get-started-with-tpu), including the Google Cloud CLI and Cloud Client Libraries for Cloud TPU, is no longer under development. For provisioning and managing TPU resources, Google recommends that you use Compute Engine or GKE, based on your orchestration and workload needs.

For more information, see [Migrate from the Cloud TPU API](https://docs.cloud.google.com/compute/docs/tpus/tpu-resources-in-compute-engine#migrate).

## TPU versions supported in Compute Engine

Compute Engine supports the following TPU versions:

  * TPU7x (Ironwood)
  * TPU v6e (Trillium)
  * TPU v5p



For more information about each TPU version, see [TPU machines](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines).

## What's next

  * Learn about [Cloud TPU resources in Compute Engine](https://docs.cloud.google.com/compute/docs/tpus/tpu-resources-in-compute-engine)
  * Learn about [TPU hardware](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
