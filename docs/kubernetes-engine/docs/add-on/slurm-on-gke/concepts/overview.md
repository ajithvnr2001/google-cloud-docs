---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/concepts/overview/
title: About Slurm on GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:26:18.786523+00:00
---

# About Slurm on GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/concepts/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  About Slurm on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview — Slurm Operator add-on for GKE**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document helps you understand the benefits and the shared responsibility model for deploying and managing Slurm clusters on Google Kubernetes Engine (GKE). [Slurm](https://slurm.schedmd.com/) is a highly scalable, open-source workload manager and job scheduler focused on high performance computing (HPC) workloads.

This document focuses on the [Slurm Operator add-on for GKE](https://github.com/SlinkyProject), which integrates the Slurm interface for batch jobs with GKE's scalability and efficient resource management.

This document is for Data administrators, Operators, and Developers who want to enable and configure Slurm with the Slurm Operator add-on for GKE.

## Why use Slurm on GKE

Running Slurm on GKE lets you set up environments where Slurm training jobs can run in parallel with other Kubernetes workloads, such as Ray jobs or serving inference, on the same shared compute pool.

Google Cloud offers the following ways to run Slurm on GKE:

  * **Cluster Director:** a managed solution that provides an opinionated, pre-configured experience. We recommend that you use Cluster Director if you want a managed experience with minimal configuration, where Google manages the Slurm control plane, software versions, and configurations. For more information, see [Cluster Director](https://docs.cloud.google.com/cluster-director/docs/overview).

  * **Slurm Operator add-on for GKE:** an open-source technology developed as part of the open-source Slinky project, offers a managed installation of the Slurm Operator. This managed installation follows Google best practices. The Slurm Operator add-on for GKE helps platform engineers who want to build custom platforms that run artificial intelligence (AI), machine learning (ML), and HPC workloads on accelerator-optimized machines. We recommend that you use the Slurm Operator add-on for GKE if you need full control over your Slurm configurations, want to integrate custom containers, or need to run Slurm with other workloads, like Ray or inference, on the same cluster. The Slurm Operator add-on for GKE has the following benefits:

    * **Unified infrastructure:** you can manage a single GKE cluster for both HPC batch jobs and microservices. This reduces operational silos.
    * **Efficient scaling:** the Slurm Operator add-on for GKE uses GKE's rapid node provisioning and efficient bin-packing to optimize resource usage.
    * **High-performance hardware:** you can access Google Cloud's latest accelerators, such as [TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus) and [GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus), by using Slurm commands.



The following sections of this document focus on the Slurm Operator add-on.

## Understand the infrastructure layer

Typically, Slurm is deployed directly on bare-metal servers or VMs. In these setups, Slurm assumes a relatively static set of nodes that it manages for the duration of its lifecycle.

GKE, on the other hand, is a managed service that abstracts away the underlying VMs by presenting them as nodes in a dynamic pool. GKE handles the scheduling and scaling of these nodes automatically.

With the Slurm Operator add-on for GKE, Slurm runs as a workload on top of GKE. In this model, GKE and Slurm provide the following capabilities:

  * **GKE as the infrastructure manager:** GKE provides and manages the underlying nodes, networking, and security.
  * **Slurm as the workload manager:** Slurm provides the interface for users to submit and manage batch jobs.



This convergence creates a heterogeneous stack where Slurm jobs can share the same underlying hardware (like GPUs and TPUs) with Kubernetes applications, such as Ray or inference serving.

## How the Slurm Operator add-on works

When you enable the Slurm Operator add-on for GKE in your GKE clusters, GKE performs the following steps:

  1. GKE installs and hosts the [Slurm Operator](https://slinky.schedmd.com/projects/slurm-operator/en/release-1.0/#kubernetes-operator-for-slurm-clusters). This operator runs in the GKE control plane and manages the lifecycle of Slurm components deployed in your cluster. This operator automatically handles prerequisites like certificate generation and custom resource management.
  2. After the operator is running, you define your Slurm cluster topology by using Kubernetes custom resources.
  3. The operator deploys the necessary Pods—such as controller, login, and workers—to match the specifications of your workload.



### Custom resources

The Slurm Operator add-on for GKE utilizes the following custom resources to manage the Slurm cluster:

  * **NodeSet:** defines a set of homogeneous worker nodes. You can map Slurm workers to specific GKE node pools or hardware types. For example, you can create a NodeSet for H100 GPUs and another for TPUs.
  * **Controller:** defines a core component of the Slurm Cluster, which is a Controller. This resource creates a `slurmctld` component in a Pod and all other components, such as a NodeSet or LoginSet.
  * **LoginSet:** defines the login nodes where users sign in to submit jobs.
  * **Restapi:** defines a REST API component of the Slurm Cluster.
  * **Accounting:** when configured, deploys the `slurmdbd` component to handle job accounting and usage tracking, typically connected to a Cloud SQL database.



### The shared responsibilities of the Slurm Operator add-on

When you choose to run Slurm on GKE with the Slurm Operator add-on for GKE, Google Cloud and you share responsibilities. This integration gives you the flexibility to customize the environment while Google manages the orchestration layer.

#### Google's responsibilities

  * **Operator lifecycle:** install the Slurm Operator.
  * **GKE control plane:** manage the reliability and uptime of the GKE control plane.
  * **Kubernetes CustomResourceDefinition:** manage the custom resources required for Slurm.
  * **Base images:** provide optimized, Google-owned container images for Slurm components. The use of these images is optional; when you configure your Slurm cluster, you can use these Google-provided images or use your own images.



#### Customer's responsibilities

  * **Slurm configuration:** define the Slurm cluster topology, partitions, limits, and plugins by using YAML files.
  * **Job submission:** manage user access and job submission workflows.
  * **Custom images:** maintain custom container images used for login or worker nodes if the default Google images don't meet specific requirements.
  * **External dependencies:** manage external resources such as Cloud SQL for accounting or Filestore for shared storage.



For more information, see [GKE shared responsibility](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/shared-responsibility).

## What's next

To get started with the Slurm Operator add-on for GKE, do the following:

  * Learn how to [deploy a Slurm cluster on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/quickstarts/deploy-slurm-on-gke).
  * Learn how to [enable the Slurm Operator add-on](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/how-to/enable-slurm-operator-addon).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
