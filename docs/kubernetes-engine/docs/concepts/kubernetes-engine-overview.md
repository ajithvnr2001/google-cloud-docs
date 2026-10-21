---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview/
title: GKE overview \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:35:01.650285+00:00
---

# GKE overview  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  GKE overview Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page provides an overview of Google Kubernetes Engine (GKE). GKE is a managed implementation of the [Kubernetes](https://kubernetes.io) open source container orchestration platform. Kubernetes was developed by Google, drawing on years of experience operating production workloads at scale on [Borg](https://research.google/pubs/pub43438/), Google's in-house cluster management system. With GKE, you can deploy and operate your own containerized applications at scale using Google Cloud's infrastructure.

This page is for Operators and Developers who are looking for a scalable, automated, managed Kubernetes solution. To learn more about common roles, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks). 

## Get started with GKE

You can start exploring GKE in minutes. You can use GKE's [free tier](https://cloud.google.com/kubernetes-engine/pricing#cluster_management_fee_and_free_tier), which lets you get started with Kubernetes without incurring costs for cluster management.

  1. [Get started in Google Cloud console](https://console.cloud.google.com/kubernetes/overview/get-started)

  2. Try the [quickstart](https://docs.cloud.google.com/kubernetes-engine/docs/deploy-app-cluster) to deploy a containerized web application.
  3. Read the [Autopilot overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview), which has guidance and resources for planning and operating your platform.



## When to use GKE

GKE is ideal if you need a platform that lets you configure the infrastructure that runs your containerized apps, such as networking, scaling, hardware, and security. GKE provides the operational power of Kubernetes while managing many of the underlying components, such as the control plane and nodes, for you.

### Benefits of GKE

The following table describes some of the benefits of using GKE as your managed Kubernetes platform:

GKE benefits  
---  
Platform management | 

  * Fully-managed nodes in GKE [Autopilot mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) with built-in hardening and best practice configurations automatically applied.
  * Managed upgrade experience with [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) to improve security, reliability, and compliance.
  * Flexible [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions) that let you configure upgrade type and scope to meet business needs and architecture constraints.
  * In GKE Standard mode, flexible [node upgrade strategies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies) to optimize availability and manage disruptions.
  * Automatic scaling of nodes based on the number of Pods in the cluster with Autopilot mode or with node auto-provisioning in Standard mode.
  * [Node auto-repair](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-repair) to maintain node health and availability.
  * Fleet-based team management.
  * [Connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway).
  * Manage GKE cluster configuration with [Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview).
  * Built-in [logging and monitoring](https://docs.cloud.google.com/monitoring/kubernetes-engine).
  * Google Cloud integrated CI/CD options with [Cloud Build](https://docs.cloud.google.com/build) and [Cloud Deploy](https://docs.cloud.google.com/deploy).

  
Improved security posture | 

  * Hardened node operating system for apps: [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs/concepts/security).
  * [Built-in security measures](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-security).
  * [Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview).
  * [Automatic upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) to new GKE versions.
  * Integrated security posture monitoring tooling with the [security posture dashboard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard).
  * Google Cloud logging and monitoring integrations with [Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs/solutions/gke).

  
Cost optimization | 

  * In Autopilot mode, pay only for the compute resources your running Pods request. In GKE Standard mode, you pay for all resources on nodes, regardless of Pod requests.
  * Save costs by running fault-tolerant workloads, such as batch jobs, on [Spot Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-spot-pods).
  * Minimized operational overhead in Autopilot mode because Google Cloud manages both the nodes and the control plane.

  
Reliability and availability | 

  * >99% [monthly uptime SLO](https://cloud.google.com/kubernetes-engine/sla).
  * Pod-level SLA in Autopilot clusters because Google manages the nodes.
  * Highly-available control plane and worker nodes in [Autopilot mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) and in [regional Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters).
  * [Proactive monitoring and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations) to mitigate potential workload disruptions caused by upcoming deprecations.
  * Multi-cluster Service capabilities.

  
**Best practice** : 

Configure the application CI/CD pipeline to use Cloud Build, Cloud Deploy, and Artifact Registry. By using managed build and deployment services, you can optimize for security, scale, and simplicity.

### Use cases for GKE

GKE and Kubernetes are used in a variety of industries, including robotics, healthcare, retail, education, gaming, and financial services. Examples of workloads you can run include:

  * [AI and ML operations](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [Data processing at scale](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/data)
  * Scalable [online games platforms](https://agones.dev/site/docs/installation/creating-cluster/gke/)
  * Reliable applications under heavy load



For case studies by industry and application, refer to [Google Cloud customers](https://cloud.google.com/customers#more-customer-stories). 

## How GKE works

A GKE environment consists of _nodes_ , which are [Compute Engine virtual machines (VMs)](https://docs.cloud.google.com/compute), that are grouped together to form a _cluster_. You package your apps (also called _workloads_) into containers. You deploy sets of containers as _Pods_ to your nodes. You use the Kubernetes API to interact with your workloads, including administering, scaling, and monitoring.

Kubernetes clusters have a set of management nodes called the _control plane_ , which run system components such as the Kubernetes API server. In GKE, Google Cloud manages the control plane and system components for you. In Autopilot mode, which is the recommended way to run GKE, Google Cloud also manages your worker nodes. Google Cloud automatically upgrades component versions for improved stability and security, which helps ensure high availability and the integrity of data stored in the cluster's persistent storage.

For more information, refer to [GKE cluster architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture).

**Best practice** : 

If you run your workloads in VMs, consider using [Migrate for GKE](https://docs.cloud.google.com/migrate/containers/docs/getting-started) to containerize the workloads without having to rewrite apps or modify source code.

### Kubernetes versions and features

GKE automatically upgrades the control plane and worker nodes of clusters to new Kubernetes versions so that the clusters receives new features, bug fixes, and security patches. GKE provides various capabilities to manage these upgrades to minimize disruption to your workloads while keeping them performant, reliable, and secure.

For more information, see [About GKE cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades).

**Best practice** : 

To try less stable Kubernetes features in the _alpha_ and _beta_ stages or to test upcoming Kubernetes minor versions, use [alpha clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters). You can also selectively [use Kubernetes beta APIs with GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/use-beta-apis). Before you enable beta APIs in production clusters, review the [implications](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/use-beta-apis#considerations-for-beta-apis).

### Modes of operation

GKE has the Autopilot and Standard _modes of operation_ , which offer you different levels of flexibility, responsibility, and control. If you want more information before you choose a mode, refer to [Choose a GKE mode of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).

**Best practice** : 

Use the fully managed [Autopilot mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview), in which Google Cloud manages your nodes for you and provides a workload-focused, cost-optimized, production-ready experience. Only use Standard mode if you know you have a specific need to manually manage the node pools and clusters. 

## What's next

  * [Start learning about GKE](https://docs.cloud.google.com/kubernetes-engine/docs/learn).
  * [Learn how to deploy a containerized application in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/deploy-app-cluster).
  * [Learn more about types of clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters).
  * [Learn more about Kubernetes](https://docs.cloud.google.com/kubernetes-engine/docs/learn/get-started-with-kubernetes).
  * [Explore the GKE documentation](https://docs.cloud.google.com/kubernetes-engine/docs/about).
  * [Design and optimize GKE clusters with Compute Advisor](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/design-with-gemini).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
