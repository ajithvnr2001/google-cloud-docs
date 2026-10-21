---
url: https://docs.cloud.google.com/kubernetes-engine/docs/get-started/deploy-workloads/
title: Deploying workloads \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:46.413754+00:00
---

# Deploying workloads  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/get-started/deploy-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Deploying workloads Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

As you read in our [Cluster lifecycle](https://docs.cloud.google.com/kubernetes-engine/docs/get-started/cluster-lifecycle) guide, as a GKE user you generally use Google Cloud tools for cluster management and Kubernetes tools like `kubectl` for cluster-internal tasks like deploying applications. This means that if you're already familiar with deploying workloads on another Kubernetes implementation, deploying workloads on GKE should involve many of the same workflows (if you're not already familiar with deploying workloads on Kubernetes, see [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) and the other resources in [Start learning about Kubernetes](https://docs.cloud.google.com/kubernetes-engine/docs/learn/get-started-with-kubernetes)).

However, GKE also provides additional features for deploying and managing your workloads, including observability tools, fully-managed database options for stateful applications, and specific hardware options for special workload types, including AI/ML workloads.

This page provides a quick overview for developers and administrators who want to deploy workloads on GKE clusters, with links to some more detailed documentation. You can find many more specific guides and tutorials in the **Deploy...** sections of the GKE core documentation.

Before you read this page, you should be familiar with the following:

  * [GKE overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)
  * [GKE modes of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)
  * [Cluster lifecycle](https://docs.cloud.google.com/kubernetes-engine/docs/get-started/cluster-lifecycle)



## Required roles

If you are not a project owner, you must have the following Identity and Access Management (IAM) role at minimum to deploy workloads:

  * Kubernetes Engine Cluster Viewer (`roles/container.clusterViewer`): This provides the `container.clusters.get` permission, which is required to authenticate to clusters in a Google Cloud project. This does not authorize you to perform any actions inside those clusters. Your cluster administrator can authorize you to perform other actions on the cluster by using either IAM or Kubernetes RBAC.

For details about all the permissions included in this role, or to grant a role with read/write permissions, see [Kubernetes Engine roles](https://docs.cloud.google.com/iam/docs/roles-permissions/container) in the IAM documentation.




You can learn more about how access control works in GKE in [Access control](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/access-control).

## Stateless applications

_Stateless applications_ are applications which don't store data or application state to the cluster or to persistent storage. Stateless applications can be deployed directly from the [**Workloads** menu in the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dashboards#workloads) as well as by using the Kubernetes API. You can learn how to deploy a stateless Linux application on GKE in [Deploying a stateless Linux application](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateless-apps). If you prefer, you can also learn how to deploy a stateless [Windows Server application](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-windows-app).

## Stateful applications and storage

Applications that need to save data that exists beyond the lifetime of their Pod are known as _stateful applications_. You or your administrator can use a Kubernetes _PersistentVolume_ object to provision this storage. In GKE, PersistentVolume storage is backed by Compute Engine disks. You can learn how to deploy a simple stateful application on GKE in [Deploying a stateful application](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-apps).

If you need your stateful application's data to persist in a database rather than storage that is tied to the lifetime of a cluster, GKE offers the following options:

  * **Fully-managed databases** : A managed database, such as [Cloud SQL](https://docs.cloud.google.com/sql) or [Spanner](https://docs.cloud.google.com/spanner), provides reduced operational overhead and is optimized for Google Cloud infrastructure. Managed databases require less effort to maintain and operate than a database that you deploy directly in Kubernetes.
  * **Kubernetes application** : You can deploy and run a database instance (such as [MySQL](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/stateful-workloads/mysql)) on a GKE cluster.



You can learn much more about data options in GKE in [Data on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/data) and [Plan your database deployments on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/database-options).

## AI/ML workloads

GKE has rich support for deploying [AI/ML workloads](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra). This includes support for training and serving models on specialist hardware, as well as flexible integration with distributed computing and data-processing frameworks. You can start learning more in the following guides:

  * [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus) introduces you to using Cloud TPU accelerators for AI/ML workloads in GKE. GKE provides full support for TPU node and node pool lifecycle management, including creating, configuring, and deleting TPU VMs. You can deploy TPU workloads on both Standard and Autopilot clusters.
  * [About GPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus) explains how to request and use GPU hardware with GKE workloads.



## Workloads with other special requirements

GKE provides features and guides to help you deploy workloads with other special requirements, including applications that require particular node architectures, or that need their Pods to run on the same or separate nodes. You can learn more about deploying some of these in the following guides:

  * [Compute classes in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-compute-classes) explains how you can pick specific compute architectures for scheduling your Pods when deploying applications on Autopilot clusters. For Standard clusters, you can directly specify the machine family you want to use for your nodes when creating a cluster.
  * [About custom compute classes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes) describes how to create custom compute classes for even greater flexibility when specifying hardware options for your applications on both Autopilot and Standard clusters.
  * [Configure workload separation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-separation) tells you how to ensure that your application's Pods run on the same or different underlying machines.
  * [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) explains how to protect your host kernel by using sandbox Pods when you deploy unknown or untrusted workloads.



## Observing your workloads

GKE provides a range of features for observing your workloads and their health, including at-a-glance overviews of workload state and metrics in the Google Cloud console, as well as more in-depth metrics, logs, and alerting.

  * Learn more about using the GKE pages in the Google Cloud console in [GKE in the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dashboards).
  * Learn more about using [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) to view your workloads and Services.
  * Learn more about GKE and Google Cloud observability in [Observability for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/observability).
  * [View details for your AI/ML workloads in Google Cloud console](https://console.cloud.google.com/kubernetes/aiml), including resources such as JobSets, RayJobs, PyTorchJobs, and Deployments for inference serving.



## Managing workload deployment

If you or your administrator want to set up a continuous integration and delivery (CI/CD) pipeline for deploying your workloads, you can find GKE-specific best practices and guidelines for CI/CD in [Best practices for continuous integration and delivery to GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/best-practices-continuous-integration-delivery-kubernetes), as well as tutorials for setting up CI/CD pipelines with specific tools and products.

## What's next

  * Learn more about tools for working with GKE:

    * [GKE in the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dashboards)
    * [Google Cloud CLI overview](https://docs.cloud.google.com/sdk/gcloud)
    * [Install `kubectl` and configure cluster access](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl)
    * [Provision GKE resources with Terraform](https://docs.cloud.google.com/kubernetes-engine/docs/terraform)
  * Learn how to simplify deployment from your IDE with Cloud Code in our [Deploy and update from an IDE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/developer-workflow) tutorial.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
