---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/concepts/overview/
title: About Slurm on GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:41:43.759139+00:00
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

This document helps you understand the benefits, the shared responsibility model, and workload mixing options for deploying and managing Slurm clusters on Google Kubernetes Engine (GKE).

[Slurm](https://slurm.schedmd.com/) is a highly scalable, open-source workload manager and job scheduler for artificial intelligence (AI), machine learning (ML), and high performance computing (HPC) workloads. Running Slurm on GKE integrates the Slurm interface for batch jobs with GKE's scalability and dynamic resource management.

This document is for Platform engineers who want to deploy and configure Slurm clusters with the Slurm Operator add-on for GKE and share compute resources across Slurm and Kubernetes workloads.

## Why use Slurm on GKE

Running Slurm on GKE lets you set up environments where Slurm training jobs can run in parallel with other Kubernetes workloads, such as inference or serving, on the same shared node pool.

The **Slurm Operator add-on for GKE** offers a managed installation of the open-source [Slinky Slurm Operator](https://github.com/SlinkyProject/slurm-operator) that follows Google best practices. The Slurm Operator add-on for GKE helps you build custom platforms that run artificial intelligence (AI), machine learning (ML), and HPC workloads on accelerator- and compute-optimized machines, with full control over Slurm configurations and custom containers.

The Slurm Operator add-on for GKE has the following benefits:

  * **Unified infrastructure:** you can manage a single GKE cluster for both HPC batch jobs and microservices. This reduces operational silos.
  * **Efficient scaling:** the Slurm Operator add-on for GKE uses GKE's rapid node provisioning and efficient bin-packing to optimize resource usage.
  * **High-performance hardware:** you can access Google Cloud's latest accelerators, such as [TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus) and [GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus), by using Slurm commands.



## Understand the infrastructure layer

Typically, Slurm is deployed directly on bare-metal servers or VMs. In these setups, Slurm assumes a relatively static set of nodes that it manages for the duration of its lifecycle.

GKE, on the other hand, is a managed service that abstracts away the underlying VMs by presenting them as nodes in a dynamic pool. GKE handles the scheduling and scaling of these nodes automatically.

With the Slurm Operator add-on for GKE, Slurm runs as a workload on top of GKE. In this model, GKE and Slurm provide the following capabilities:

  * **GKE as the infrastructure manager:** GKE provides and manages the underlying nodes, networking, and security.
  * **Slurm as the workload manager:** Slurm provides the interface for users to submit and manage batch jobs.



This convergence creates a heterogeneous stack where Slurm jobs can share the same underlying hardware (like GPUs and TPUs) with Kubernetes applications, such as inference or serving.

## How the Slurm Operator add-on works

When you enable the Slurm Operator add-on for GKE in your GKE clusters, GKE performs the following steps:

  1. GKE installs and hosts the [Slurm Operator](https://slinky.schedmd.com/projects/slurm-operator/en/release-1.0/#kubernetes-operator-for-slurm-clusters). This operator runs in the GKE control plane and manages the lifecycle of Slurm components deployed in your cluster. This operator automatically handles prerequisites like certificate generation and custom resource management.
  2. After the operator is running, you define your Slurm cluster topology by using Kubernetes custom resources.
  3. The operator deploys the necessary Pods (such as controller, login, and workers) to match the specifications of your workload.



### Custom resources

The Slurm Operator add-on for GKE utilizes the following custom resources to manage the Slurm cluster:

  * **NodeSet:** defines a set of homogeneous worker nodes. You can map Slurm workers to specific GKE node pools or hardware types. For example, you can create a NodeSet for H100 GPUs and another for TPUs.
  * **Controller:** deploys and manages the Slurm controller (`slurmctld`) component, which orchestrates cluster state, partitions, and job scheduling.
  * **LoginSet:** defines the login nodes where users sign in to submit jobs.
  * **Restapi:** deploys the `slurmrestd` component, which provides a REST API interface to the Slurm cluster.
  * **Accounting:** when configured, deploys the `slurmdbd` component to handle job accounting and usage tracking, typically connected to a Cloud SQL database.



### The shared responsibilities of the Slurm Operator add-on

When you choose to run Slurm on GKE with the Slurm Operator add-on for GKE, Google Cloud and you share responsibilities. This integration gives you the flexibility to customize the environment while Google manages the orchestration layer.

#### Google's responsibilities

  * **Operator lifecycle:** install and manage the Slurm Operator and its webhook in the GKE control plane.
  * **GKE control plane:** manage the reliability and uptime of the GKE control plane.
  * **Kubernetes CustomResourceDefinition:** install and manage the CustomResourceDefinitions required for Slurm.
  * **Base images:** provide optimized, Google-owned container images for Slurm components. The use of these images is optional; when you configure your Slurm cluster, you can use these Google-provided images or use your own images.



#### Customer's responsibilities

  * **Slurm configuration:** define the Slurm cluster topology, partitions, limits, and plugins by using Helm values and YAML files.
  * **Job submission:** manage user access and job submission workflows.
  * **Custom images:** maintain custom container images used for login or worker nodes if the default Google images don't meet specific requirements.
  * **External dependencies:** manage external resources such as Cloud SQL for accounting or Filestore for shared storage.



For more information, see [GKE shared responsibility](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/shared-responsibility).

## Workload mixing on GKE

Workload mixing lets you dynamically share GKE compute resources, such as GPUs, TPUs, and CPUs, between Slurm batch jobs and non-Slurm Kubernetes workloads (such as inference or serving) on the same cluster. Instead of maintaining separate, statically partitioned node pools for Slurm and Kubernetes, you can optimize accelerator and compute utilization by dynamically reassigning cluster capacity based on workload demand and priority.

Depending on your scheduling model and platform requirements, you can implement workload mixing on GKE by using either _Slurm Bridge_ or _K8s Bridge_.

### Slurm Bridge

[Slurm Bridge](https://github.com/SlinkyProject/slurm-bridge) is an open-source scheduler plugin from the Slinky project that uses _Slurm as the primary scheduler_ for shared resources. When you submit Kubernetes workloads to a configured namespace, Slurm Bridge intercepts the Pods, registers them as external jobs in Slurm, and binds the Pods to GKE nodes after Slurm allocates the required capacity.

Use Slurm Bridge if your use case meets the following conditions:

  * You operate a Slurm-first environment with dedicated or static node pools.
  * You want a single Slurm scheduler to manage all workloads.
  * You rely on Slurm scheduling capabilities, such as Multi-Factor Priority, fair-share scheduling, backfill scheduling, and job suspension.



For more information, see the [Slurm Bridge documentation](https://github.com/SlinkyProject/slurm-bridge/tree/main/docs).

### K8s Bridge

[K8s Bridge](https://github.com/GoogleCloudPlatform/k8s-bridge) is an open-source Kubernetes controller developed by Google that uses _[Kueue](https://kueue.sigs.k8s.io/) as the central admission controller_ across Slurm and Kubernetes workloads. With K8s Bridge, you can submit batch and interactive jobs by using standard Slurm commands (such as `sbatch`, `salloc`, and `srun`) without needing to learn deep Kubernetes concepts. When a job is submitted to a configured Slurm partition, K8s Bridge translates it into a Kueue-managed Kubernetes workload, provisions dedicated worker Pods on the shared node pool after Kueue admits the job, and releases the resources when the job completes.

Because K8s Bridge is configured per Slurm partition, you can also combine dedicated Slurm-only partitions and shared partitions within the same cluster.

In addition to dynamic workload mixing, K8s Bridge extends the Slurm Operator add-on with the following GKE benefits:

  * **Unified quotas, priorities, and bidirectional preemption:** centrally manage multi-tenant quotas, fair sharing, and priorities in Kueue. High-priority Kubernetes workloads (such as scaling inference services) can preempt lower-priority Slurm jobs with automatic requeuing. Conversely, high-priority Slurm jobs can also preempt lower-priority Kubernetes workloads.
  * **Queue-based and all-or-nothing autoscaling:** enable queue-based, topology- and workload-aware autoscaling with the GKE Cluster Autoscaler, including support for [flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws) all-or-nothing provisioning. You can automatically provision nodes when jobs are queued and scale down to zero when idle.
  * **Resource fungibility and availability:** improve the flexibility, efficiency, and availability of compute capacity across machine types and consumption options (reservations, Spot VMs, and flex-start) by using [ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes) and Kueue `ResourceFlavor` objects, as well as multi-region and multi-cluster availability with [MultiKueue](https://kueue.sigs.k8s.io/docs/concepts/multikueue/).
  * **Per-job Pod and sidecar customization:** customize worker Pod templates per Slurm partition to configure container images, shared memory, storage mounts (such as Filestore, Managed Lustre, or Cloud Storage FUSE), and isolated per-job sidecar containers.
  * **Unified GKE observability:** centralize visibility into both Slurm and Kubernetes workloads and cluster resources in the Google Cloud console, Cloud Logging, and Cloud Monitoring, while keeping Slurm jobs visible in Slurm.



## What's next

To get started with the Slurm Operator add-on for GKE, do the following:

  * Learn how to [deploy a Slurm cluster on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/quickstarts/deploy-slurm-on-gke).
  * Learn how to [enable the Slurm Operator add-on](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/how-to/enable-slurm-operator-addon).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
