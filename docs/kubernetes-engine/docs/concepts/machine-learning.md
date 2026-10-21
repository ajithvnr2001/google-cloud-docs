---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/
title: Introduction to AI/ML workloads on GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:41.296452+00:00
---

# Introduction to AI/ML workloads on GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Introduction to AI/ML workloads on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page provides a conceptual overview of Google Kubernetes Engine (GKE) for AI/ML workloads. GKE is a Google-managed implementation of the [Kubernetes](https://kubernetes.io) open source container orchestration platform.

[Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) provides a scalable, flexible, and cost-effective platform for running all your containerized workloads, including artificial intelligence and machine learning (AI/ML) applications. Whether you're training large foundation models, serving inference requests at scale, or building a comprehensive AI platform, GKE offers the control and performance you need.

This page is for Data and AI specialists, Cloud architects, Operators, and Developers who are looking for a scalable, automated, managed Kubernetes solution to run AI/ML workloads. To learn more about common roles, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Get started with AI/ML workloads on GKE

You can start exploring GKE in minutes by using GKE's [free tier](https://cloud.google.com/kubernetes-engine/pricing#cluster_management_fee_and_free_tier), which lets you get started with Kubernetes without incurring costs for cluster management.

  1. [Get started in Google Cloud console](https://console.cloud.google.com/kubernetes/aiml/overview)

  2. Try these quickstarts: 
     * [Inference on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-open-models-terraform): deploy an AI large language model (LLM) on GKE for inference using a pre-defined architecture.
     * [Training on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/train-model-gpus-standard): deploy an AI training model on GKE and store the predictions in Cloud Storage.
  3. Read [About accelerator consumption options for AI/ML workloads](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/consumption-option), which has guidance and resources for planning and obtaining accelerators (GPUs and TPUs) for your platform.
  4. Get AI-powered assistance to plan and design the infrastructure for your GKE clusters by prompting Gemini in the Google Cloud console. For more information, see [Design and optimize GKE clusters with Compute Advisor](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/design-with-gemini).



## Common use cases

GKE provides a unified platform that can support all of your AI workloads.

  * **Building an AI platform** : for enterprise platform teams, GKE provides the flexibility to build a standardized, multi-tenant platform that serves diverse needs.
  * **Low-latency online serving** : For developers building generative AI applications, GKE with the Inference Gateway provides the optimized routing and autoscaling needed to deliver a responsive user experience while controlling costs.



## Choose the right platform for your AI/ML workload

Google Cloud offers a spectrum of AI infrastructure products to support your ML journey, from fully managed to fully configurable. Choosing the right platform depends on your specific needs for control, flexibility, and level of management.

**Best practice** : 

Choose GKE when you need deep control, portability, and the ability to build a customized, high-performance AI platform.

  * **Infrastructure control and flexibility** : you require a high degree of control over your infrastructure, need to use custom pipelines, or require kernel-level customizations.
  * **Large-scale training and inference** : you want to train very large models or serve models with minimal latency, by using GKE's scaling and high performance.
  * **Cost efficiency at scale** : you want to prioritize cost optimization by using GKE's integration with Spot VMs and Flex-start VMs to effectively manage costs.
  * **Portability and open standards** : you want to avoid vendor lock-in and run your workloads anywhere with Kubernetes, and you already have existing Kubernetes expertise or a multi-cloud strategy.



You can also consider these alternatives:

Google Cloud service | Best for  
---|---  
Vertex AI | A fully managed, end-to-end platform to accelerate development and offload infrastructure management. Works well for teams focused on MLOps and rapid time-to-value. For more information, watch [Choosing between self-hosted GKE and managed Vertex AI host AI models](https://www.youtube.com/watch?v=539_P8SnW4M).  
Cloud Run | A serverless platform for containerized inference workloads that can scale to zero. Works well for event-driven applications and serving smaller models cost-effectively. For a comparative deep-dive, see [GKE and Cloud Run](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-and-cloud-run).  
  
## How GKE powers AI/ML workloads

GKE offers a suite of specialized components that simplify and accelerate each stage of the AI/ML lifecycle, from large-scale training to low-latency inference.

![In the following diagram, GKE is within Google Cloud
       and can use different cloud storage options \(such as Cloud Storage FUSE and Managed Lustre\) and different cloud infrastructure options
       \(such as Cloud TPU and Cloud GPUs\). GKE also works
       with open source software and frameworks for deep learning \(such as JAX or TensorFlow\), ML orchestration \(such as Jupyter or Ray\), and LLM inference
       \(such as vLLM or NVIDIA Dynamo.](https://docs.cloud.google.com/static/kubernetes-engine/images/gke-ai-platform.svg)**Figure 1** : GKE as a scalable managed platform for AI/ML workloads.

The following table summarizes the GKE features that support your AI/ML workloads or operational goals.

AI/ML workload or operation | How GKE supports you | Key features  
---|---|---  
**Inference and serving** | Optimized to serve AI models elastically, with low latency, high throughput, and cost efficiency. | 

  * [Accelerator flexibility](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/consumption-option): GKE supports both [GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus) and [TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus) for inference.
  * [GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway): a model-aware gateway that provides intelligent routing and load balancing specifically for AI inference workloads.
  * [GKE Inference Quickstart](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/inference-quickstart): a tool to simplify performance analysis and deployment by providing a set of benchmarked profiles for popular AI models.
  * [GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview): a GKE operational mode that automates cluster operations and capacity right-sizing, reducing overhead.

  
**Training and fine-tuning** | Provides the scale and orchestration capabilities necessary to efficiently train very large models while minimizing costs. | 

  * [Faster startup nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/fast-starting-nodes#autopilot-gpu-workloads): an optimization designed specifically for GPU workloads that reduces node startup times by up to 80%.
  * [flex-start provisioning mode powered by Dynamic Workload Scheduler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws): improves your ability to secure scarce GPU and TPU accelerators for short-duration training workloads.
  * [Kueue](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/kueue-intro): a Kubernetes-native job queueing system that manages resource allocation, scheduling, quota management, and prioritization for batch workloads.
  * [TPU multislice](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpu-multislice): a hardware and networking architecture that allows multiple TPU slices to communicate with each other over the Data Center Network (DCN) to achieve large scale training.

  
**Unified AI/ML development** | Managed support for Ray, an open-source framework for scaling distributed Python applications. | 

  * [Ray on GKE add-on](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview): abstracts Kubernetes infrastructure, letting you scale workloads like large-scale data preprocessing, distributed training, and online serving with minimal code changes.

  
  
## What's next

  * To explore our extensive collections of official guides, tutorials, and other resources for running AI/ML workloads on GKE, visit the [AI/ML orchestration on GKE portal](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra). 

  * [Learn about techniques to obtain computing accelerators, such as GPUs or TPUs, for your AI/ML workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/consumption-option).

  * [Learn about AI/ML model inference on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/inference). 

  * [Learn about Ray on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview). 

  * Explore experimental samples for leveraging GKE to accelerate your AI/ML initiatives in [GKE AI Labs](https://gke-ai-labs.dev/).

  * [View details for your AI/ML workloads in Google Cloud console](https://console.cloud.google.com/kubernetes/aiml), including resources such as JobSets, RayJobs, PyTorchJobs, and Deployments for inference serving.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
