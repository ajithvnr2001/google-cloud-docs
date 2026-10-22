---
url: https://docs.cloud.google.com/kubernetes-engine/networking/docs/gke-documentation/
title: Explore GKE documentation \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:40.492802+00:00
---

# Explore GKE documentation  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/networking/docs/gke-documentation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Explore GKE documentation Stay organized with collections  Save and categorize content based on your preferences. 

GKE has a rich ecosystem of features and products that help you deploy, run, and manage your containerized applications at scale. However, this also means there's a lot of documentation. Each documentation set in the GKE family contains guides, tutorials, reference material, release notes, examples, and more. This quick guide will help you find your way around.

If you're brand new to GKE, we recommend that you start your exploration with [Start learning about GKE](https://docs.cloud.google.com/kubernetes-engine/docs/learn).

## The big picture

The GKE documentation is organized into several documentation sets, reflecting the structure of the wider GKE ecosystem and families of features. Most users won't need to read beyond the core GKE documentation. Platform admins and operators might need to explore the documentation more broadly.

  * **Core GKE documentation** , which introduces GKE and covers core features that are available to all GKE users.
  * **GKE networking documentation** (this documentation set), for network administrators or anyone else who needs to dive deeper into GKE and Kubernetes networking.
  * **GKE security documentation** , for security practitioners who want to configure security features and maintain your platform security.
  * **AI/ML workloads on GKE documentation** , for data scientists, ML engineers, and application developers who want to train, serve, and manage AI/ML models.
  * **Fleet management documentation** , for when you want to manage groups of GKE clusters together as a _fleet_.
  * **Config Sync documentation** , for when you want to centralize your configuration files in a single source of truth, such as a Git repository.
  * **Policy Controller documentation** , for when you want to enable the application and enforcement of programmable policies for your Kubernetes clusters.
  * **Config Controller documentation** , for when you want to create and manage Google Cloud resources with a declarative, Kubernetes model.
  * **GKE outside Google Cloud documentation** sets, for users who want to use GKE on-premises or on other public clouds.



You can read more about these documentation sets in the following sections.

## Core GKE documentation

Start here. This documentation set covers core concepts and features that are available to all GKE users, with material for both IT administrators and Developers. It includes the following topics:

  * [Learn fundamentals](https://docs.cloud.google.com/kubernetes-engine/docs/learn): Kubernetes and GKE basics for new users. If you're new to Kubernetes, Google Cloud, or GKE, this section will help you learn the essentials.
  * [GKE best practices](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices): A consolidated list of best practices for designing, building, and operating applications on GKE.
  * [Get started](https://docs.cloud.google.com/kubernetes-engine/docs/get-started/cluster-lifecycle): Ready to create your first cluster? Here's what you need to know about.
  * Set up GKE clusters: Detailed instructions for creating and configuring [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster) and [Standard](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-zonal-cluster) clusters.
  * [Reduce and optimize costs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-optimization-metrics): Learn how and why to use cost optimization features in GKE.
  * [Provision storage](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/storage-overview): Learn about the supported storage options for GKE and how to use them.
  * [Configure cluster security](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview): GKE provides many ways to secure your workloads. This section introduces you to GKE security features and how to use them.
  * Deploy workloads: Learn how to deploy different types of workloads on GKE, from simple [stateless apps](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateless-apps) to [databases, caches, and data streaming workloads](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/database-options).
  * [Manage and optimize clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managing-clusters): Learn about administering clusters, including upgrades, notifications, and recommendations, plus node pool management for Standard clusters.
  * [Observability for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/observability): Use managed Prometheus, Cloud Monitoring, and Cloud Logging to observe your clusters and workloads.
  * [Troubleshoot](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/known-issues): Find troubleshooting guidance and known issues for all core features.



This documentation set also includes reference material for the [Kubernetes Engine (GKE) AP](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest).

## GKE networking

For network administrators (or anyone else who needs to dive deeper into GKE and Kubernetes networking), [GKE networking documentation](https://docs.cloud.google.com/kubernetes-engine/networking/docs) shows you how to configure and work with networking and traffic management features for your clusters. Topics range from planning your networking infrastructure on Google Cloud to setting up load balancers, exposing workloads as Services, and configuring cluster isolation. This documentation set includes the following GKE topics (and more), as well as links to useful sections in the Google Cloud Virtual Private Cloud and Compute Engine networking documentation.

  * [Networking overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview): Get a high level view of networking features, including how GKE manages networking both inside and outside your clusters.
  * [Best practices for GKE networking](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/networking): Follow best practices and opinionated guidance for planning and designing your network.
  * [Network isolation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation): Learn how to control network access to your clusters' control plane and nodes.
  * [Services in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service): Expose applications running on your clusters as Services, including setting up load balancers and using [multi-cluster Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-services).
  * [Enhance network security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy) with network policies.
  * [Observability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-dpv2-observability): Get metrics and insights about your network traffic.



## GKE security

The security documentation has information about the various security controls in GKE clusters and Kubernetes workloads. The security documentation shows you how to perform tasks like authenticating from workloads to Google Cloud APIs, controlling access to your clusters and Kubernetes resources, and monitoring your security posture over time.

To explore the GKE security documentation, see the [GKE security overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview). 

## AI/ML workloads on GKE

The AI/ML workloads documentation has information about training, serving, and managing AI/ML models on GKE. Topics include serving models for inference, training models at scale, deploying AI agents, using Ray for distributed AI/ML applications, managing AI infrastructure and accelerators like GPUs and TPUs, managing data and storage for AI/ML workloads, and monitoring your workloads.

To explore the AI/ML workloads on GKE documentation, see [Introduction to AI/ML workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning). 

## GKE fleet management

GKE uses the concept of a _fleet_ to simplify managing multiple clusters, regardless of which project they exist in and what workloads run on them. For example, fleets are used by a platform or cluster administrator who needs to work with multiple GKE clusters, possibly across multiple Google Cloud projects. The [fleet management documentation](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs) includes information about:

  * [Planning fleets](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts/plan-fleets): Learn how fleets work, with practical guidance for grouping your organization's clusters into fleets and enabling fleet features.
  * [Create your fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation): Add clusters to fleets.
  * [Work with fleet features](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts/fleet-features): Learn how to adopt, configure, and manage fleet-enabled features for your clusters and workloads.
  * [Fleet team management](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/team-management): Simplify provisioning and managing GKE resources for multiple teams across multiple clusters.
  * [Observe your fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/enterprise-overview-dashboard): Get an at-a-glance view of your entire fleet and view fleet-scoped logs and metrics.



This documentation set also includes reference material for the GKE Hub (Fleet) API.

## Config Sync

[Config Sync](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/overview) provides a consistent way to manage GKE cluster configuration, with configuration applied automatically from a single source of truth. This documentation set includes the following topics:

  * [Get started](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/tutorials/config-sync-multi-repo) with Config Sync.
  * Learn about [GitOps best practices](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/gitops-best-practices).
  * [Install Config Sync with default settings](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/install-default).
  * [Troubleshoot](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/troubleshooting-config-sync) common issues.



## Policy Controller

[Policy Controller](https://docs.cloud.google.com/kubernetes-engine/enterprise/policy-controller/docs/overview) lets you apply and enforce consistent policies on your GKE clusters. This documentation set includes the following topics:

  * [Install Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/installing-policy-controller).
  * [Apply best practices with policy bundles](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/concepts/policy-controller-bundles).
  * [Monitor compliance](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/policy-controller-status) with dashboards.



## Config Controller

[Config Controller](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-controller/docs/overview) creates and manages Google Cloud resources with a declarative, Kubernetes model. Config Controller is a hosted version of Config Connector that simplifies installation and maintenance. This documentation set includes the following topics:

  * [Set up Config Controller](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/setup).
  * [Manage resources with Config Controller](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-controller/docs/manage-resources).
  * [Troubleshoot](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/troubleshoot) common issues.



## GKE outside Google Cloud

Many organizations using Google Cloud also want or need to run workloads in their own data centers, factory floors, retail stores, and even in other public clouds – but they don't want to build new container platforms themselves in all these locations, or rethink how they configure, secure, monitor, and optimize container workloads depending on where they're running. GKE Multi-Cloud and Google Distributed Cloud both extend GKE for use outside Google Cloud, letting you create and manage hybrid or entirely on-premises deployments.

### GKE Multi-Cloud

  * [GKE on AWS](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws): Work with GKE clusters running on AWS infrastructure.
  * [GKE on Azure](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure): Work with GKE clusters running on Azure infrastructure.
  * [GKE attached clusters](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached): Add CNCF-conformant Kubernetes clusters to your fleet to view and manage along with your GKE clusters, with instructions for EKS, AKS, and other conformant cluster types.



### Google Distributed Cloud (on-premises)

  * [Google Distributed Cloud (software only) for VMware](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs): Run GKE clusters in a VMware VSphere environment.
  * [Google Distributed Cloud (software only) for bare metal](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs): Run GKE clusters directly on your own hardware.
  * [Google Distributed Cloud connected deployments](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/overview): Run GKE clusters on-premises on dedicated hardware provided and maintained by Google.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
