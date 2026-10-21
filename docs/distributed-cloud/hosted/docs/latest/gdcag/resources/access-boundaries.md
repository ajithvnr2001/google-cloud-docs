---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/access-boundaries/
title: Design access boundaries between resources \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:34.276350+00:00
---

# Design access boundaries between resources  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/access-boundaries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Design access boundaries between resources Stay organized with collections  Save and categorize content based on your preferences. 

This document introduces best practices for designing the hierarchy and separation for workloads in Google Distributed Cloud (GDC) air-gapped using organizations, projects, and Kubernetes clusters. This guidance balances efficient resource usage, isolation of workloads, and ease of operations.

## Design organizations for physical and logical isolation between customers

The `Organization` resource is the root for all the resources owned by a single customer. Granular access control between workloads within an organization can be defined through role bindings and network policies. See [Identity and access management](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in) for more information.

Each organization within a GDC zone provides physical isolation for compute infrastructure, and logical isolation for networking, storage, and other services. Users in one organization have no access to resources in another organization unless explicitly granted access. Network connectivity from one organization to another is not allowed by default, unless explicitly configured to allow data transfer out from one organization and data transfer in to another.

## Define the scope of workloads that can share an organization

The scope of an organization in your company context might vary based on how your company defines trust boundaries. Some companies might prefer to create multiple organization resources for different entities in the company. For example, each company department might be an independent customer of GDC with an independent organization if the departments require complete physical and administrative separation of their workloads.

In general, we recommend that you group multiple workloads into a single organization based on the following signals:

  * Workloads can share dependencies. For example, this might be a shared data source, connectivity between workloads, or a shared monitoring tool.
  * Workloads can share an administrative root of trust. The same administrator can be trusted with privileged access over all workloads in the organization.
  * Workloads are allowed to share underlying physical infrastructure with other workloads in the same organization, as long as sufficient logical separation is in place.
  * The same budget holder has accountability for workload budgets in aggregate. For details on viewing aggregate costs for the organization or granular analysis per workload, see the [Billing](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/manage-billing-accounts) page.
  * Workload availability requirements must follow your high availability requirements for multi-zone distance. 



## Design projects for logical isolation between workloads

Within an organization, we recommend provisioning multiple projects to create a logical separation between resources. Projects in the same organization might share the underlying physical infrastructure, but projects are used to separate workloads with a logical boundary based on Identity and Access Management (IAM) policies and network policies.

When designing project boundaries, think of the largest set of functionality that can be shared by resources, such as [role bindings](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/set-up-role-bindings), [network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview#security-and-connectivity), or [observability](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/monitoring-overview) requirements. Group the resources that can share this functionality into a project, and move resources that cannot share this functionality to another project.

In Kubernetes terms, a project is a Kubernetes _namespace_ that is reserved across all clusters in an organization. Though a namespace is reserved across multiple clusters, that does not mean a pod is automatically scheduled across all clusters. A pod scheduled to a particular cluster remains scheduled to that particular cluster.

The following diagram shows how a role binding is applied to a project that spans multiple clusters.

![GDC RBAC policy](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform-application/images/04-rbac-multi-cluster.png)

Role bindings are set at the project level to define who can do what to which resource type. Workloads like VMs or pods are deployed to a project, and access to these workloads is governed by the role binding. The role binding applies consistently to VM-based workloads and container-based workloads, regardless of which cluster they are deployed to.

The following diagram shows how network policies manage access between projects. Inter-project communication between the `Backend Project`, `Frontend Project`, and `Database Project` is disabled. However, resources within each project can communicate with each other.

![](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform-application/images/05-default-network-policy.png)

[Network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview#security-and-connectivity) are set at the project level to selectively allow network access between resources. By default, all resources within a single project are allowed to communicate with each other on the internal network, and a resource in one project cannot communicate with a resource in another project. This behavior for network policies applies whether resources are deployed to the same cluster or not.

You can also define a `ProjectNetworkPolicy` custom resource to enable inter-project communication. This policy is defined for each project to allow ingress traffic from other projects. The following diagram illustrates a `ProjectNetworkPolicy` custom resource defined for the `Backend Project` to enable data transfer in from the `Frontend Project` and `Database Project`.

![GDC project level policy](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform-application/images/06-custom-network-policy.png)

Additionally, the [monitoring](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/monitoring-overview) stack collects metrics across the organization, but you can filter and query at various levels of the resource hierarchy. You can query metrics with entities such as a cluster or namespace.

## Create projects per software development environment

For each workload, we recommend creating separate projects for each software development environment. A _software development environment_ is an area within your GDC universe intended for all operations that correspond to a designated lifecycle phase. For example, you could have software development environments for testing, development, and production. Separating your software development environments lets you define role bindings and network policies granularly, so that changes made in a project used for a non-production environment don't impact the production environment.

## Grant resource-level role bindings within projects

Depending on your team structure and requirements, you might allow developers to modify any resource within the project they manage, or you might require more granular access control. Within a project, you grant granular role bindings to let individual developers access to some but not all resources in the project. For example, a team might have a database administrator who must manage the database but not modify other resources, while the software developers on the team must not have permission to modify the database.

## Design clusters for logical isolation of Kubernetes operations

A Kubernetes cluster is not a hard tenant boundary because [role bindings](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/set-up-role-bindings) and [network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview#security-and-connectivity) apply to projects, not Kubernetes clusters. Kubernetes clusters and projects have a many-to-many relationship. You might have multiple Kubernetes clusters in a single project, or a single Kubernetes cluster that spans multiple projects.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
