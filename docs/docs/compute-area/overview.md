---
url: https://docs.cloud.google.com/docs/compute-area/overview/
title: Google compute overview \u00a0|\u00a0 Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:11:37.075901+00:00
---

# Google compute overview  |  Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/compute-area/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Guides ](https://docs.cloud.google.com/docs/compute-area/overview)



Send feedback 

#  Google compute overview Stay organized with collections  Save and categorize content based on your preferences. 

This document introduces the compute services that are available in Google Cloud. By understanding the spectrum of infrastructure control and management abstraction, you can gain the foundational knowledge needed to choose the right compute service for your workloads.

The term _compute_ in Google Cloud refers to the virtualized computing resources, such as processing power and memory, that are required to run your applications. These resources range from raw virtual machine (VM) instances to fully managed platforms. With VM instances, you can fully customize the operating system (OS), networking, and software stack. For managed platforms, Google handles most of the underlying infrastructure.

## High-level service areas

The compute category on Google Cloud encompasses the following key service areas:

  * **VM instances and bare metal instances** : Compute Engine provides configurable VM and bare metal instances where you can install and manage your own OS and applications. This configuration also includes adding graphics processing units (GPUs) or tensor processing units (TPUs) to a customized VM or bare metal instance.

  * **Containers** : services such as Google Kubernetes Engine (GKE) let you deploy and manage containerized applications.

  * **Batch processing** : services such as Batch help you run large-scale asynchronous jobs.

  * **AI infrastructure** : includes specialized services and tools like Cluster Director and Cluster Toolkit, purpose-built hardware (NVIDIA GPUs and Google TPUs), open software, and flexible consumption models. These services are designed to run complex, orchestrated training and inference workloads for artificial intelligence (AI) or machine learning (ML) at scale.

  * **HPC infrastructure** : includes specialized services and hardware to execute high performance computing (HPC) workloads, such as tightly coupled physics simulations, weather models, or molecular dynamics.




## Control versus abstraction in your infrastructure

Google Cloud offers compute services across a spectrum of control and abstraction. The two main categories are the following:

  * Infrastructure as a Service

  * Managed platforms and services




### Infrastructure as a Service

Infrastructure as a Service (IaaS) is the model that offers the most control. You manage the OS, middleware, and applications. Instead, Google manages the underlying virtualization, servers, storage, and networking. The IaaS solutions that are available in Google Cloud include the following:

  * **Compute Engine** : this service lets you create and run VM and bare metal instances on Google's infrastructure. Compute Engine offers flexibility to run a wide range of workloads by letting you choose from various machine series, storage services, accelerators, and guest OSs.

  * **Google Cloud VMware Engine** : a service that lets you migrate and run VMware workloads natively on Google Cloud. Google manages the underlying hardware and the VMware platform. You retain full control over your VMs, guest OSs, and applications. This approach helps you move to the cloud without re-architecting your existing VMware environments.




IaaS is often preferred by infrastructure architects, ML infrastructure engineers, and platform engineers who need to design and manage custom environments from scratch.

### Managed platforms and services

Managed platforms and services offer a balance of control and ease of use. Google manages the underlying infrastructure, OS, and runtime environments so that you can focus on running your workloads. The managed solutions that are available in Google Cloud include the following:

  * **Batch** : a managed service that lets you schedule, queue, and run batch computing jobs at scale. Batch provisions Compute Engine resources to run your jobs and manages their lifecycle, so you don't need to manage the underlying VM or bare metal instances directly.

  * **Cloud Run** : a fully managed platform that lets you develop and deploy highly scalable containerized applications on a serverless infrastructure. Cloud Run abstracts away all infrastructure management. This abstraction lets you run containers that respond to web requests or events without needing to manage servers or clusters.

  * **Cluster Director** : a managed service that automates the complex setup and configuration of AI, ML, or HPC clusters. Google manages the cluster infrastructure, letting you focus on running your workloads with minimal operational overhead.

  * **Cluster Toolkit** : an open source toolkit that helps you provision AI, ML, or HPC clusters on Google Cloud by using predefined blueprints. You manage the resulting cluster infrastructure, but the toolkit abstracts the deployment process and lets you customize your deployments and software stack.

  * **GKE** : a managed environment for running containerized applications on Kubernetes. Google manages the Kubernetes control plane, whereas you deploy and manage your container workloads. Depending on the deployment mode (_Autopilot_ or _Standard_), you can choose how much control you want over the underlying infrastructure.




Managed platforms and services are often preferred by data scientists, AI researchers, and ML engineers who want to quickly provision resources and deploy workloads without deep infrastructure management.

## What's next

  * [Choose compute options](https://docs.cloud.google.com/docs/compute-area/choose-compute-options)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
