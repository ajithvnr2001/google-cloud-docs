---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-admin-overview/
title: Cluster administration overview \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:44.728642+00:00
---

# Cluster administration overview  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-admin-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Cluster administration overview Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page provides a quick overview of managing GKE clusters for administrators.

If you are a developer running workloads on GKE, you might not need to carry out most of these tasks. For an introduction to deploying workloads on GKE, see [Deploying workloads](https://docs.cloud.google.com/kubernetes-engine/docs/get-started/deploy-workloads).

Before reading this page you should be familiar with the following, as well as [basic Kubernetes concepts](https://docs.cloud.google.com/kubernetes-engine/docs/learn/get-started-with-kubernetes):

  * [GKE overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)
  * [GKE modes of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)
  * [Cluster lifecycle](https://docs.cloud.google.com/kubernetes-engine/docs/get-started/cluster-lifecycle)



## What tools do I use?

As an administrator, you use a range of tools to work with GKE clusters.

  * To control a cluster's configuration and overall characteristics, you use **Google Cloud tools and APIs** , including the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) and the [Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dashboards). These tasks include creating, updating, viewing, and deleting clusters, and controlling who can access the cluster using Identity and Access Management (IAM). You might also use other Google Cloud tools and services, such as observability services for monitoring, logging, and alerting.

  * To control a cluster's _internal_ behavior, you use **the Kubernetes API and the`kubectl` command-line interface**. Tasks where you might need to use `kubectl` include deploying workloads, applying Kubernetes role-based access control (RBAC) policies, and specifying Kubernetes network policy rules. You can read more about configuring `kubectl` for use with GKE clusters in [Install `kubectl` and configure cluster access](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl).

  * To declaratively provision clusters and workloads, you might use **Terraform**. You can read more about using Terraform with GKE in [Provision GKE resources with Terraform](https://docs.cloud.google.com/kubernetes-engine/docs/terraform).




## Basic cluster administration

Basic cluster administration tasks include cluster configuration, cluster upgrades, and node configuration.

**Best practice** : 

Use Autopilot clusters because GKE handles most administration tasks for you, such as cluster upgrades and node configurations. In Standard, only upgrades are managed by GKE. For more information, see [GKE modes of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).

Basic cluster administration tasks are specific to GKE clusters on Google Cloud and typically don't involve the Kubernetes system itself; you perform these tasks entirely by using the Google Cloud console, the Google Cloud CLI, the GKE API, or Terraform's Google Cloud provider.

### Viewing clusters

You can see basic information about your clusters in the [Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dashboards) and by using the Google Cloud CLI or the GKE API. This includes whether a cluster is running and its current [configuration](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters), as well as listing all your clusters. For more details, see [Managing clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managing-clusters).

For more detailed information about cluster state and health, you can use observability tooling and features.

### Cluster and node upgrades

By default, clusters and nodes are upgraded automatically. You can learn more about configuring [how upgrades work](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades) on each cluster, including when they can and cannot occur.

### Cluster-level configuration

Cluster-level configuration tasks include [creating](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster) and [deleting](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deleting-a-container-cluster) GKE clusters and nodes. You can also update some cluster settings such as [when cluster maintenance tasks can occur](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions).

You can find out more about cluster configuration in the [Cluster configuration overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters).

### Node configuration

If you use Autopilot for your clusters, you don't need to worry about node configuration because GKE configures your nodes for you. Autopilot cluster nodes are all fully managed by GKE and all use the same [node operating system (OS), `cos_containerd`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images).

However, if you need to use Standard mode for any clusters, GKE offers a range of options for your cluster's nodes. For example, you can create one or more [node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools); node pools are groups of nodes within your cluster that share a common configuration. Your cluster must have at least one node pool, and a node pool called `default` is, by default, created when you create the cluster. You can read more about node pool management in GKE in [Add and manage node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools).

Other node configuration options for Standard clusters include choosing a non-default OS, using ephemeral [spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms), and choosing a [minimum CPU platform](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/min-cpu-platform) for new nodes ( Autopilot users can also specify a minimum CPU platform for compute-intensive workloads, but only on a workload-scoped basis).

Even with Standard clusters, you can't change `iptables` rules or other node-level settings that GKE manages. The node might become unreachable or unintentionally exposed when manual changes revert to the cluster's declarative configuration.

## Configuring cluster networking

An important aspect of cluster administration is enabling and controlling various networking features for your cluster, such as IP address options for Standard clusters, whether your cluster's nodes can be accessed from public networks (nodes that can't be accessed from public networks are known as _private nodes_), and network access policies.

Many networking features are set at cluster creation (and many of them cannot be changed without recreating the cluster): when you create a cluster using a Google Cloud interface, you must enable the networking features that you want to use. Because of this behavior, if you are not a Network administrators you might need to work closely with your Network administrators when setting up production-ready clusters.

Some networking features that can be enabled with Google Cloud tools, such as network policy enforcement, also require further configuration using Kubernetes APIs.

You can learn much more about GKE networking in [Network overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview).

## Cluster observability

Another important part of cluster administration is configuring and using _observability_ tooling to understand the health of your infrastructure and applications, and maintain application availability and reliability. By default, GKE clusters are configured to do the following:

  * Send [system logs, audit logs, and application logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs#what_logs) to Cloud Logging.
  * Send [system metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#system-metrics) to Cloud Monitoring.
  * Use [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) to collect configured third-party and user-defined metrics and then send them to Cloud Monitoring. Google Cloud Managed Service for Prometheus lets you monitor and alert on your workloads using Prometheus, without manually managing and operating Prometheus at scale.



GKE also provides observability features that help you use the data that you gather, including default and custom dashboards, alerting, service level objective (SLO) monitoring, and log analysis.

You can find out much more about setting up and using GKE observability in [Observability for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/observability).

## Configuring cluster security

GKE includes Google Cloud-specific and Kubernetes security features that you can use with your cluster. You can manage Google Cloud-level security, such as IAM, using the Google Cloud console. You manage intra-cluster security features such as Kubernetes role-based access control (RBAC) using Kubernetes APIs and other interfaces.

To learn about the security features and capabilities that are available in GKE, refer to the [Security overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview) and [Harden your cluster security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster). GKE Autopilot clusters implement many of these security features and hardening best practices automatically. For more information, refer to [Security capabilities in GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-security).

## Optimizing costs

GKE's tools let you view your cluster costs, and help you make sure that you are making the most efficient use of the Google Cloud resources that you're paying for. You can view utilization metrics for CPU, memory, and disk usage over different timescale, and use these metrics to help optimize resource usage: for example if you have potentially underutilized or overutilized clusters that you might want to resize. You can also use autoscaling to [reduce cluster size during off-peak hours](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/reducing-costs-by-scaling-down-gke-off-hours), and use [insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders) to identify idle clusters, along with other best practices.

You can also view metrics to optimize costs across your [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/enterprise-overview-dashboard#view_fleet_efficiency) and for individual [teams](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/enterprise-overview-dashboard#view_team_efficiency).

## Configuring for disaster recovery

To ensure that your production workloads remain available in the event of a service-interrupting event, you should prepare a disaster recovery (DR) plan. To learn more about DR planning, see the [Disaster recovery planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide).

Your Kubernetes configuration and any persistent volumes will not be backed up unless you take explicit action. To backup and restore your Kubernetes configuration and persistent volumes on GKE clusters, you can use [Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke).

## What's next

  * Learn more about [cluster configuration options](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters).
  * Learn more about cluster architecture and the GKE control plane in [GKE cluster architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture).
  * Learn more about tools for working with GKE:

    * [GKE in the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dashboards)
    * [Google Cloud CLI overview](https://docs.cloud.google.com/sdk/gcloud)
    * [Install `kubectl` and configure cluster access](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl)
    * [Provision GKE resources with Terraform](https://docs.cloud.google.com/kubernetes-engine/docs/terraform)
  * Learn how to set up a cluster and workload for staging with a simple example in our [Configure a cluster and workload for staging](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/admin-workflow) tutorial. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
