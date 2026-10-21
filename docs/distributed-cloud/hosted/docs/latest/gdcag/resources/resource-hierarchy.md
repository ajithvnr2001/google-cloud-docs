---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/resource-hierarchy/
title: Resource hierarchy \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:34.468329+00:00
---

# Resource hierarchy  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/resource-hierarchy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Resource hierarchy Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the Google Distributed Cloud (GDC) air-gapped resource hierarchy and how resources are managed in an air-gapped instance. For concepts on managing resources across multiple zones, see the [Multi-zone overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/mz-overview).

The purpose of the GDC resource hierarchy is twofold:

  * Provide a hierarchy of ownership, which binds the lifecycle of a resource to its immediate parent in the hierarchy.
  * Provide attach points and inheritance for access control and organization policies.



The GDC resource hierarchy resembles the file system found in operating systems as a way of organizing and managing entities hierarchically. Generally, each resource has exactly one parent. This hierarchical organization of resources lets you set access control policies, such as Identity and Access Management (IAM), which are inherited by child resources.

For more information about best practices for organizing your access boundaries, see [Design access boundaries between resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/access-boundaries).

## Resource structure in detail

The following entities are resource types recognized in the GDC resource hierarchy:

  * Organization
  * Project
  * Shared Kubernetes cluster
  * Service resource



GDC resources are organized hierarchically. Most resources in the resource hierarchy have exactly one parent. The exception only applies to the highest resource. At the lowest level, service resources are the fundamental components that make up all GDC services.

An organization is the top of the GDC resource hierarchy, and all resources that belong to an organization are grouped under the organization resource. This provides central visibility and control over every resource that belongs to an organization.

Both projects and shared Kubernetes clusters are organization-scoped. They can be attached to one another to organize service resources. However, projects and shared clusters function independently from one another. This flexibility provides many different options for how to organize services and workloads. For example, you can have a shared cluster dedicated to a single project. Likewise, a shared cluster can span across multiple projects.

Service resources are entities that must belong to a project, and cannot be shared across projects. Examples of service resources include virtual machines (VMs), standard Kubernetes clusters, databases, storage buckets, and backups. Most of these lower-level resources have project resources as their parents.

The following diagram represents an example GDC resource hierarchy:

![Resource hierarchy for organizations, projects, and resources](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/images/gdch-resource-hierarchy.png)

For more information about best practices for organizing your resource hierarchy for optimal workload management, see [Design user workload separation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/workload-separation).

## Organization

The organization resource represents an administrative unit or a business function, such as a company, and is the top-level resource in the GDC resource hierarchy. An organization defines a security boundary that encloses infrastructure resources to be administered together so that users can deploy application workloads. Organizations are global and span all zones in a universe. Within an organization, service resources such as VMs and storage volumes are logically grouped by projects.

All projects, clusters, and service resources belong to your organization instead of their creators. This means that any resource type for an organization is not deleted if the user who created it leaves the organization. Instead, all resource types follow the organization's lifecycle in GDC.

The IAM access control policies applied to the organization resource apply throughout the hierarchy on all resources in the organization. For more information about granting organization-wide policies and permissions, see the [Organization policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/org-policy) and [IAM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/set-up-role-bindings) sections.

## Project

A project is a tenancy unit that every service must integrate. Projects provide logical grouping of service resources. Projects are global and span all zones in a universe.

Projects enable segmentation of service resources within an organization and provide a lifecycle and policy boundary for managing resources. Service resources inside a project can never outlive the project itself or move between projects, ensuring that control is available for the life of a resource. Therefore, you must deploy resources of any type within a project namespace.

A project is considered a proper Kubernetes namespace that spans across multiple shared clusters in an organization. _Namespace sameness_ considers all namespaces of a given name the same namespace for all shared clusters within the same organization. The single namespace has a consistent owner across the set of shared clusters. Service providers create project-scoped services by creating control plane and data plane components in the namespace.

The namespace for a project hosts the following:

  * Project-scoped service APIs.
  * Project-level policy configurations, such as roles and role bindings.



You can attach a project to only a subset of shared clusters in an organization. You can deploy containerized workloads on these shared clusters within a project namespace. The namespace sameness concept applies to the project namespace on these shared clusters. Namespace-scoped policies, such as role-based access (RBAC) policies, apply to all those namespaces.

For more information about projects, see the [Projects overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/project-management).

## Shared Kubernetes cluster

A Kubernetes cluster is a set of nodes that run containerized workloads as part of GKE on GDC. You can provision Kubernetes clusters to support the compute requirements of your applications.

A _shared cluster_ is a cluster configuration that is organization-scoped, and must be attached to one or more projects. The _standard cluster_ is another cluster configuration that operates within a single project only, but is considered a service resource in the resource hierarchy. These Kubernetes cluster configurations are designed to build a Kubernetes architecture that offers container management options across software development environments, such as for testing, development, and production. For more information on container workload separation best practices, see [Design workload separation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/workload-separation).

For more information about the different cluster types in GDC, see [Kubernetes cluster configurations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs).

![Resource hierarchy with cluster spanning two projects](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/images/gdch-resource-hierarchy-clusters.png)

Shared clusters subdivide infrastructure resources into isolated pools to be consumed by projects within an organization. Clusters are also logically separated from each other to provide different failure domains and isolation guarantees. The enforcement of policies per organization ensures shared clusters can be shared across teams and users while also maintaining performance and resource guarantees. Additionally, organization policies enable VM workloads to run alongside container workloads without introducing operational complexity.

Clusters are beneficial for instances where you must deploy containerized workloads. However, with the option to deploy VM-based workloads, the existence of a Kubernetes cluster is not required in GDC.

Clusters are a zonal resource only and cannot span multiple zones. To operate clusters in a multi-zone deployment, you must manually deploy clusters in each zone.

For more information about Kubernetes clusters, see [Kubernetes cluster overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/clusters).

## Service resource

Service resources include many entities, such as:

  * VMs
  * Standard Kubernetes clusters
  * Databases
  * Storage buckets
  * Containerized workloads
  * Backups



Service resources must belong to a project, and they cannot be shared across projects. This project-specific lifecycle means that service resources inside a project can never outlive the project itself, ensuring that control is available for the life of the resource.

Service resources can be deployed globally or zonally depending on the type. Reference the specific service's documentation for information on multi-zone deployment options. Service resources are enabled by default and can be disabled using an [organization policy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/org-policy).

## What's next

  * [Design access boundaries](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/access-boundaries)
  * [Zones in GDC air-gapped](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/mz-overview)
  * [High availability for your apps](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
