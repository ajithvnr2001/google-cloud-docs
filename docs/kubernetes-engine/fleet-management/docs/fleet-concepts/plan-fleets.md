---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts/plan-fleets/
title: Plan fleet resources \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:37:11.864495+00:00
---

# Plan fleet resources  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts/plan-fleets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Plan fleet resources Stay organized with collections  Save and categorize content based on your preferences. 

As you learned in the [Fleet management overview](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs), fleets are a grouping mechanism to manage, configure and secure Kubernetes clusters at scale. Fleets are a powerful tool that remove the need to perform repeated operations in a multi-cluster environment and provide consistency and comprehensive observability over large groups of clusters. A number of [GKE features](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/deployment-options) are available only through a fleet.

The grouping strategy you use to create fleets can vary depending on your organization's technical and business needs. For example, one organization might group clusters based on the type of applications running in them, while another might group them by region, environment, or other relevant factors. All else being equal, it is convenient to have as few fleets as necessary within your organization.

This guide is for Cloud architects who want to get started with fleets in their organizations. It provides some practical guidance on organizing your clusters into fleets, including:

  * When you want to create completely new clusters.
  * When you want to create fleets with existing clusters.



The patterns described here work for many organizations, but they are not the only way of planning fleets. Fleets are flexible and you might decide to use a different grouping pattern for your clusters.

Before reading this page, ensure that you're familiar with the following concepts:

  * The concepts covered in our [Fleet management overview](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs).
  * Basic Kubernetes concepts and the Google Cloud [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).



## Fleet and resource limitations

The following general limitations apply when creating fleets:

  * A given Google Cloud project can have only a single fleet (or no fleets) associated with it, although that fleet can include clusters from multiple projects. The project associated with a fleet is known as the fleet's [fleet host project](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts#fleet-host-project).
  * Clusters can only be members of a single fleet at any given time.
  * All clusters in a given project must be in the same fleet, or not in a fleet. If a project already contains fleet members, you can't register a cluster from that project to a different fleet.
  * The default limit for the number of clusters in a fleet is 250, though you can [request a higher limit](https://docs.cloud.google.com/docs/quotas/view-manage) if required.



It can be convenient for many reasons to place multiple clusters in the same project. However, consider the following limits when planning what clusters to put together in a project:

  * A [Virtual Private Cloud (VPC)](https://docs.cloud.google.com/vpc/docs/overview) network can't have more than 75 private clusters.
  * If you plan to use Multi Cluster Ingress or multi-cluster Gateway, consider the [limits for `MultiClusterIngress` and `MultiClusterService` resources in a project](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress#default_quotas).
  * Review the [Compute Engine quotas and limits](https://docs.cloud.google.com/compute/quotas-limits). For example, Compute Engine enforces [allocation quotas](https://docs.cloud.google.com/compute/resource-usage) on compute resources that are used by a cluster.



## General principles

The following are general questions that you should ask when deciding whether to group clusters together in a fleet. We'll look at how these apply in more detail in the following sections.

  * Are the resources related to one another? 
    * Resources that have large amounts of cross-service communication benefit the most from being managed together in a fleet.
    * Resources in the same deployment environment (for example, your production environment) should be managed together in a fleet.
  * Who administers the resources? 
    * Having unified (or at least mutually trusted) control over the resources is crucial to ensuring the integrity of the fleet.



## Plan fleets for new clusters

This section describes how to plan fleets when you have a known set of applications, but are flexible about where those applications are deployed. This might be because you have not yet developed those applications, or are migrating them from a different container platform. Alternatively you might already have applications running in existing clusters, but are open to moving applications to new clusters to achieve a preferred architecture.

After fleets have been identified, you can create a new project per fleet, create a fleet in each project, and create and register clusters to the intended fleet.

### Audit your workloads

Start with a list of all the Kubernetes workloads (for example Deployments) that you want to deploy. This need not be a literal list; it can just be an idea of what workloads you will need. Then, follow the steps in the rest of this section to progressively divide that set of applications into subsets until you have the minimal set of groupings needed. This will define what fleets and clusters you need.

### Consider business units

Your organization might have a federated IT structure, where there is one central IT team for the organization, as well as separate IT teams for each business unit. In this case, each federated IT team may want to manage its own fleets. Use separate fleets if two business units' workloads (for example, auditing and trading in a bank) can't communicate with each other at all for regulatory reasons.

### Separate workloads by environment

A common pattern that works for many organizations is to group clusters by environment. A typical configuration is to have three primary environments: development, non-production (or staging), and production. Application changes are typically deployed progressively (or promoted) to each environment in the list. Because of this, you have separate deployments in each environment for the same underlying application, such as the same base container image name. See the [Enterprise foundations blueprint](https://docs.cloud.google.com/architecture/security-foundations) for an example of how to create environments in your organization.

A fleet should only contain clusters from one environment. Three environments, with one fleet in each environment, might be sufficient for many organizations. See the [Enterprise application blueprint](https://docs.cloud.google.com/architecture/enterprise-application-blueprint) for an example where each environment has one fleet and how applications can be deployed progressively.

### Combine redundant workload instances

When an application needs high availability, one pattern is to run it in two or more regions. This involves two or more clusters running very similarly-configured deployments that are managed as a unit. Often they will have a load balancer spanning application instances in all clusters, or use DNS load balancing.

In these scenarios, place all of those clusters into the same fleet. Clusters in different regions generally don't need to be in separate fleets, unless required for regulatory or other reasons.

## Plan fleets with existing clusters

This section describes how to plan fleets when you have workloads running on existing clusters, and you don't plan to relocate them. Those clusters might be on or outside Google Cloud. In this scenario, the goal is to create a set of fleets within your organization and assign existing clusters to them.

After fleets have been identified, you can create a new project per fleet, create a fleet in each project, and register clusters to the intended fleet.

### Audit your clusters

Start with a list of all the Kubernetes clusters in your organization. [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/overview) is one way to search your organization for Kubernetes cluster resources.

You can then follow the steps in the rest of this section to progressively divide that set of applications into subsets until you have the minimal set of groupings needed. This will define what fleets you need.

### Consider business units

Your organization might have a federated IT structure, where there is one central IT team for the organization, as well as separate IT teams for each business unit. These per-business-unit IT teams might have created your existing clusters. Typically in this case you partition the set of clusters by business unit. An example is where certain business units' workloads (for example, auditing and trading in a bank) can't communicate with each other at all for regulatory reasons.

If business units exist purely for cost accounting purposes, but use a common IT team, then consider combining their clusters in a single fleet, especially if there is significant inter-service dependencies across business units.

### Group clusters by environment

Identify what environments are used in your organization. Typical environment names are dev, non-production (or staging), and prod.

If each cluster is clearly in only one of your environments, then separate your list of clusters by environment. However, if some clusters contain workloads that logically belong to different environments, then we recommend that you redeploy the applications into clusters that only contain applications belonging to a single logical environment.

### Minimize the number of cluster owners

When combining existing projects into a fleet there might be different sets of users authorized to act as administrators on those clusters, considering both the the IAM policies (`container.admin`) and RBAC (admin ClusterRoleBinding). If you plan to use features that require sameness, the goal should be to get all clusters having the same set of admins, and for there to be a small set of admins for the fleet. If clusters must have different admins, and the goal is to use those features that require sameness, then they probably don't belong in the same fleet.

For example, if clusters C1 and C2 have different admins who are not mutually trusting, and not willing to share admin permissions to a central platform team that manages fleets, then they shouldn't be grouped together in a fleet.

You can learn more about sameness and which features require it in [How fleets work](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts#sameness).

## Consider fleet features

Regardless of whether you are working with new or existing clusters, the fleet features you choose can also affect your optimal fleet organization. For example, if you choose to use fleet-wide Workload Identity Federation you might want to organize your fleets in a way that minimizes risk when setting up fleet-wide workload authentication, or if you want to use Cloud Service Mesh you might need certain clusters to be in the same fleet. If you use Virtual Private Cloud (VPC), some features require the use of a single VPC per fleet.

You can find out more about adopting fleet features and their requirements and limitations in the next guide in this series, [Plan fleet features](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts/fleet-features).

## Consider VPC perimeters

Another issue to consider for both new and existing clusters is if you have chosen to or want to create your own private networks on Google Cloud with [Virtual Private Cloud (VPC)](https://docs.cloud.google.com/vpc/docs/overview). Clusters within a VPC perimeter (for example on a Shared VPC that has VPC Service Controls), can be in a fleet together. If you have both restricted and non-restricted Shared VPCs, a good practice is to put those into separate fleets.

If you are planning to use VPC Service Controls perimeters, then typically some workloads are in the perimeter and some are outside it. You should plan to have VPC Service Controls and non-VPC Service Controls versions of each fleet in each environment (or at least prod and the environment immediately before prod).

Be aware when planning fleets with VPCs that some fleet features have [specific VPC requirements](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts/fleet-features#vpc-requirements), such as requiring all the clusters that use them to be within the same VPC network.

## What's next

  * Get best practices for adding features to your fleet in [Plan fleet features](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts/fleet-features).
  * Dive deeper into how fleets work in [How fleets work](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts).
  * Get started creating your fleet following the [Fleet creation overview](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
