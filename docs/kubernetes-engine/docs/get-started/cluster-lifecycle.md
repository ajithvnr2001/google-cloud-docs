---
url: https://docs.cloud.google.com/kubernetes-engine/docs/get-started/cluster-lifecycle/
title: Cluster lifecycle \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:44.534482+00:00
---

# Cluster lifecycle  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/get-started/cluster-lifecycle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Cluster lifecycle Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page provides an overview of the lifecycle of a Google Kubernetes Engine (GKE) cluster, including which tasks you can perform yourself and which are managed by Google Cloud, with links to more detailed guides to get you started.

Before you read this page, you should be familiar with the following, as well as [basic Kubernetes concepts](https://docs.cloud.google.com/kubernetes-engine/docs/learn/get-started-with-kubernetes):

  * [GKE overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)
  * [GKE modes of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)



## Creating clusters

As you saw if you completed one of our [quickstarts](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/create-cluster), creating a Kubernetes cluster with GKE can be very simple, particularly if you choose to use the Google Cloud console and use all the provided default options. In real life, cluster creation can be a little more complex, particularly when it comes to choosing cluster options to suit your organizational and technical needs. You might need to make decisions in consultation with networking, security, or other colleagues before you create your cluster, as some cluster options can't be changed after they're configured without recreating the cluster.

You can create clusters using the Google Cloud console, gcloud CLI, or the Terraform provider for GKE.

  * For more details about cluster configuration options (including options that you can't change after cluster creation), see the [Cluster configuration overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters).
  * To learn how to create an Autopilot cluster (recommended), see [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).
  * To learn how to create a Standard cluster, see [Create a Standard cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster).
  * For some thoughts about whether you need to create multiple clusters, see [Multi-cluster use cases](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/multi-cluster-use-cases).



## Working with clusters

If you are a cluster administrator, much of your work will involve working with running clusters. Tasks might include monitoring and troubleshooting cluster state, or for larger organizations (particularly those using GKE's [enterprise tier](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-editions)), managing multiple clusters together as part of a [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs). If you are Security specialists or Networking specialists, you might have more specialized tasks such as applying security policies or configuring networking infrastructure. If you are a developer using GKE, you might not need to create or manage clusters, but you might need to deploy workloads to clusters, or troubleshoot issues with your workloads.

Tools that you might use include the following:

  * Google Cloud tools for creating, managing, and viewing clusters and their state, including the Google Cloud console and gcloud CLI.
  * The Kubernetes command-line tool `kubectl` for _cluster-internal_ tasks such as deploying workloads or applying Kubernetes role-based access control (RBAC) policies.
  * [Terraform](https://docs.cloud.google.com/kubernetes-engine/docs/terraform) to declaratively provision clusters and workloads.



Because GKE is a managed service, you don't need to worry about the underlying infrastructure, such as the virtual machines that run your cluster nodes, or the state of Kubernetes control plane components: GKE manages this for you.

You can read more about working with clusters and the tools and workflows that you use for this in our [Cluster administration overview](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-admin-overview). To learn more about cluster architecture and the GKE control plane, see [ GKE cluster architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture).

## Upgrading clusters

A cluster _upgrade_ updates the version of the GKE system software running on the cluster's control plane and nodes. By default, GKE automatically upgrades your clusters to ensure that they receive security updates, fixes to known issues, and new features, and that they run a supported version of Kubernetes.

For greater control over the upgrade process, GKE provides [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). Release channels let you pick versions for your clusters with your chosen balance between feature availability and stability. [Maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions) let you choose when you'd like upgrades and other cluster maintenance to occur.

All clusters are enrolled in the Regular release channel by default. You can find out much more about getting the most from release channels with minimal disruption to your workloads in [Best practices for upgrading clusters](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/upgrading-clusters).

You can also initiate cluster upgrades yourself. To learn more, see [Manually upgrading a cluster or node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster).

## Updating clusters

As mentioned in the previous section on creating clusters, there are a number of changes that you can make to a cluster's configuration after it's been created. Updates that you _can_ make to a cluster include:

  * Resize a Standard cluster (Autopilot clusters are resized automatically based on your workload's needs).
  * Add a cluster to a [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs).
  * Change the cluster's [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels).
  * Update zones for Standard clusters.
  * Update the cluster's [maintenance policy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions).
  * Update a subset of networking options.
  * Enable and disable cluster features, including backups, logging, monitoring, and more.



For more details about what you can and can't change after cluster creation, see [Cluster configuration overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters).

## Resizing clusters

Autopilot clusters are sized automatically based on your Pod specifications, so resizing your cluster isn't something you need to worry about. For example, if you change the number of replicas of your Pod, or the resources it requests, the cluster will be sized up or down appropriately.

If you use Standard mode, you can manually resize your cluster to increase or decrease the number of nodes it has. For example, if you want to stop your cluster from consuming resources without deleting it, you can scale the nodes down to zero. To learn more about resizing, see [Resizing a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/resizing-a-cluster). You can also choose to use [cluster autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler), letting GKE automatically resize your cluster's node pools based on the demands of your workloads, and [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning), where GKE automatically creates and deletes node pools for you.

If you would like a more efficient way to optimize your clusters, you can also use [Vertical Pod Autoscaling (VPA)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler). The autoscaler can recommend values for CPU and memory requests and limits, or it can automatically update the values.

## Deleting clusters

When needed, you can delete a cluster. To learn more, see [Deleting a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deleting-a-cluster).

## Adding clusters to a fleet

If your organization uses multiple clusters, you can simplify multi-cluster management by adding the clusters to a _fleet_ : a logical grouping of Kubernetes clusters. Creating a fleet helps your organization uplevel management from individual clusters to entire groups of clusters, and lets you use fleet-enabled features such as [Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress), [ Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/config-sync-overview), and [ Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller).

You can add GKE clusters to a fleet by using the Google Cloud console, gcloud CLI, or declaratively using Terraform or Config Connector.

You can learn more about how fleets work in [Fleet management](https://docs.cloud.google.com/kubernetes-engine/docs/fleets-overview), and about creating fleets in [Create fleets to simplify multi-cluster management](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-fleets).

## What's next

  * Learn more about managing clusters in our [Cluster administration overview](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-admin-overview).
  * Learn more about [cluster configuration options](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters).
  * Learn about [Deploying workloads](https://docs.cloud.google.com/kubernetes-engine/docs/get-started/deploy-workloads).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
