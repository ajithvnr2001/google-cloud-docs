---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview/
title: About Ray on GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:59.515644+00:00
---

# About Ray on GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  About Ray on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page provides an overview of the Ray Operator and relevant custom resources to deploy and manage Ray clusters and applications on Google Kubernetes Engine (GKE).

[Ray](https://www.ray.io/) is an open-source unified compute framework for scaling AI/ML and Python applications. Ray provides a set of libraries to distribute the compute runtime for AI/ML across multiple compute nodes.

To learn how to enable the Ray operator on GKE, see [Enable the Ray operator on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/enable-ray-on-gke).

## Why use the Ray Operator on GKE

The Ray Operator is the recommended way to deploy and manage Ray clusters on GKE. When you run the Ray Operator on GKE, you benefit from Ray's support for Python and GKE's enterprise-grade reliability, portability, and scalability.

The Ray Operator on GKE is based on [KubeRay](https://github.com/ray-project/kuberay), which provides declarative Kubernetes APIs specifically designed for managing Ray clusters. This means that you can provision, scale, and manage your Ray Deployments with other containerized workloads on GKE.

## How the Ray Operator on GKE works

When you enable the Ray Operator in your GKE clusters, GKE automatically installs and hosts the KubeRay operator.

KubeRay provides Kubernetes custom resources to manage Ray Deployments on Kubernetes, including:

  * RayCluster
  * RayJob
  * RayService



### RayCluster custom resource

The RayCluster custom resource lets you specify a Ray cluster that GKE deploys as Kubernetes Pods. A Ray cluster typically consists of a single head Pod and multiple worker Pods.

### RayJob custom resource

The RayJob custom resource lets you execute a single Ray job. KubeRay creates a RayCluster to provide compute resources for the job, then creates a Kubernetes Job that submits the Ray job to the head Pod of the RayCluster.

For efficient resource management, you can configure KubeRay to automatically clean up the RayCluster after your job is successfully completed.

### RayService custom resource

The RayService custom resource lets you configure [Ray Serve applications](https://docs.ray.io/en/latest/serve/index.html), such as applications for model serving and inference. KubeRay creates a RayCluster to provide the compute resources and then deploys the Ray Serve application as specified by the Ray Serve configuration.

## Ray on GKE shared responsibility

When you choose to run Ray workloads on GKE with the Ray operator, it's important to understand how responsibilities are divided between Google Cloud and you, the customer:

### Google's responsibilities

  * Maintaining the reliability and uptime of the KubeRay operator.
  * Managing version upgrades for the KubeRay operator.
  * Capabilities specific to KubeRay for managing the RayCluster, RayJob, and RayService custom resources.



### Customer's responsibilities

  * Maintaining container images used for the Ray head and Ray worker Pods.
  * Maintaining versioning and upgrades for the Ray head and Ray worker Pods.
  * Configuring resource requirements (CPU, GPU, TPU, memory, etc.) for your Ray clusters.
  * Following best practices for [securing Ray clusters](https://docs.ray.io/en/latest/ray-security/index.html).
  * Reliability and monitoring for your Ray applications.



See [GKE shared responsibility](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/shared-responsibility) to learn more.

## What's next

  * Learn how to [enable the Ray operator on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/enable-ray-on-gke).
  * Explore tutorials for using TPUs with Ray on GKE: 
    * [Configure KubeRay with TPU Trillium](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/kuberay-trillium)
    * [Train an LLM using JAX, Ray Train, and TPU Trillium on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/distributed-training-tpu)
    * [Multislice and elastic training on TPUs using Ray Train on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/multi-slice-training-ray)
    * [Optimize AI training on TPUs with DWS and Kueue](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/ray-kueue-dws)
    * [Serve Gemma open models using multi-host TPUs on GKE with Ray](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-multi-host-tpu-llm)
    * [Serve an LLM using TPUs on GKE with KubeRay](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-llm-tpu-ray)
    * [Deploy a Ray Serve application with a Stable Diffusion model on GKE with TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/tutorials/deploy-ray-serve-stable-diffusion-tpu)
    * [View TPU metrics on the Ray Dashboard](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/view-tpu-metrics)
  * Explore the [Ray on Kubernetes](https://docs.ray.io/en/latest/cluster/kubernetes/index.html) documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
