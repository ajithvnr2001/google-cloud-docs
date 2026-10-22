---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/
title: Fleet management overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:44.107576+00:00
---

# Fleet management overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Fleet management overview Stay organized with collections  Save and categorize content based on your preferences. 

GKE offers a set of capabilities that helps you and your organization (from infrastructure operators and workload developers to security and network engineers) manage clusters, infrastructure, and workloads, on Google Cloud and across public cloud and on-premises environments. These capabilities are all built around the idea of the _fleet_ : a logical grouping of Kubernetes clusters and other resources that can be managed together. Fleets are managed by the Fleet service, also known as the Hub service.

This page describes our expanding portfolio of multi-cluster management capabilities and provides resources to get started managing your fleet.

## Introducing fleets

Typically, as organizations embrace cloud-native technologies like containers, container orchestration, and service meshes, they reach a point where running a single cluster is no longer sufficient. There are a variety of reasons why organizations choose to deploy multiple clusters to achieve their technical and business objectives; for example, separating production from non-production environments, or separating services across tiers, locales, or teams. You can read more about the benefits and tradeoffs involved in multi-cluster approaches in [multi-cluster use cases](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/multi-cluster-use-cases).

Google Cloud uses the concept of a _fleet_ to simplify managing multiple clusters, regardless of which project they exist in and what workloads run on them. For example, suppose your organization has ten Google Cloud projects with two GKE clusters in each project, using them to run multiple different production applications. Without fleets, if you want to make a production-wide change to clusters, you need to make the change on the individual clusters, in multiple projects. Even observing multiple clusters can require switching context between projects. With fleets, you can logically group and normalize clusters, helping you uplevel management and observability from individual clusters to entire groups of clusters, with a single "fleet host project" to view and manage your fleet.

However, fleets can be more than just simple groups of clusters. You can build on fleets by enabling fleet-based features that let you abstract away cluster boundaries - for example, by defining and managing resources that belong to specific teams across multiple clusters, or by automating applying the same configuration across your fleet.

A fleet can be entirely made up of [Google Kubernetes Engine clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters) on Google Cloud, or include clusters outside Google Cloud.

  * To learn more about how fleets work, and to find a complete list of fleet-enabled features, see [How fleets work](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts). 
  * To learn about current limitations and requirements for using fleets in multi-cluster deployments, as well as recommendations for implementing fleets in your organization, see [Fleet requirements and best practices](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts/best-practices).

  * To help you implement fleets in your own systems, read about hypothetical scenarios that use fleets in [Fleet examples](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts/examples).




## Creating a fleet

Creating a fleet involves registering the clusters you want to manage together to a fleet in your chosen fleet host project. Some cluster types are automatically registered at cluster creation time, while other cluster types must be manually registered. You can read more about how this works in the [Fleet creation overview](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation), and follow the linked instructions to start adding clusters to your fleet.

When you add a cluster outside Google Cloud to your fleet, a [Connect Agent](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent) is installed on the cluster to establish control plane connectivity between the cluster and Google Cloud. The agent can traverse NATs, egress proxies, VPNs, and other interconnects that you have between your environments and Google. Your Kubernetes clusters and their API servers do not need public or externally exposed IP addresses. To learn more about the Connect Agent, see the [Connect Agent overview](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent).

## Authenticating to clusters

Connecting and authenticating users and service accounts to clusters across multiple environments can be challenging. With fleets, you can choose from two options for consistent, secure authentication to clusters for all your organization's developers and admins.

  * **Google Cloud identity** : If you want to use Google Cloud as your identity provider, the Connect gateway builds on fleets to provide a consistent way to connect to and run commands against your registered clusters from the command line, and makes it simpler to automate DevOps tasks across multiple clusters, including clusters outside Google Cloud. Users don't need direct IP connectivity to a cluster to connect to it using this option. Find out more in the [Connect gateway guide](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway).

  * **Third-party identity** : Fleets also support using your existing third-party identity provider, such as Microsoft ADFS, letting you configure your fleet clusters so that users can log in with their existing third-party ID and password. OIDC and LDAP providers are supported. Find out more in [Set up the connect gateway with third party identities](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup-third-party) and [Introducing GKE Identity Service](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity).




With either approach, users can log in to clusters from the command line or from the Google Cloud console.

## Google Cloud console

The Google Cloud console provides a central user interface for managing all of your fleet clusters no matter where they are running. After you have registered your clusters to your fleet, you can log in to view, monitor, debug, and manage your workloads.

To learn more and to get started, see [Work with clusters from the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console).

## Who can use fleet management features?

GKE includes fleet management features. Features such as [Multi Cluster Ingress](https://cloud.google.com/kubernetes-engine/pricing#multi-cluster-gateway-and-multi-cluster-ingress) and [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview) are available at additional cost.

For details of which features are included in each deployment environment, see the GKE [deployment options](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/deployment-options) page.

## Use cases

While managing more than one cluster has its challenges, there are many reasons to deploy multiple clusters to achieve technical and business objectives. Find out more in our [Multi-cluster use cases](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/multi-cluster-use-cases) guide.

## What's next?

  * Learn more about fleets in [How fleets work](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts)
  * Start planning how to organize your clusters into fleets with [Plan fleet resources](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts/plan-fleets)
  * Get best practices for adding features to your fleet in [Plan fleet features](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts/fleet-features)
  * Get started creating your fleet following the [Fleet creation overview](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
