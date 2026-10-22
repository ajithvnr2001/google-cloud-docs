---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/project-management/
title: Project overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:02:24.655413+00:00
---

# Project overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/project-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Project overview Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview for how projects work in Google Distributed Cloud (GDC) air-gapped. A _project_ is a collection of your resources. Projects help to segment resources within your organization and provide a boundary for managing resource lifecycles and enforcing policies. When a project is deleted, all resources within it are also deleted, and policies that apply to a project also apply to all the resources in the project. You can use projects to organize and manage your resources as a group. For more information, see [Resource hierarchy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/resource-hierarchy).

This document is for audiences such as IT administrators, security engineers, and network administrators within the platform administrator group who are responsible for managing resources within their organization. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Project identifiers

A project has two identifiers:

  * **Display name** : A human-readable name for your project. The display name isn't used by GDC APIs. You can edit the project name at any time during or after project creation. Display names don't need to be unique.

  * **Project name** : A globally unique identifier for your project. A project name is a unique string used to differentiate your project in GDC. The project name is generated from your initial display name when you create a project, and it cannot be modified after the project is available. The namespaces propagated by a project are the same as the project name.


**Important:** A project name must be unique within your organization and different from other project names, including of deleted projects.

Don't include sensitive information in your display name, project name, or other resource names. The project name is used in the name of many other GDC resources, and any reference to the project or related resources exposes the project name and resource name.

## Project namespace

The namespace for a project hosts several resources and configurations, such as:

  * Project-scoped service APIs or Kubernetes custom resource definitions.
  * Project-level policy configurations, such as roles and role bindings.



A project is considered a [Kubernetes namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) that can span multiple shared Kubernetes clusters in an organization. A _shared cluster_ is a Kubernetes cluster that can attach to multiple projects, whereas a _standard cluster_ is a Kubernetes cluster that operates within a single project namespace. For more information about Kubernetes clusters in GDC, see [Kubernetes cluster configurations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs).

Kubernetes treats each shared cluster as a separate entity, and each shared cluster has an independent project namespace. However, for all shared clusters in a GDC organization, GDC considers all namespaces with the same name to be the same namespace. This is referred to as _namespace sameness_. The single namespace has a consistent owner across the set of shared clusters. Service providers create project-scoped services by creating control plane and data plane components in the namespace.

![Namespace sameness illustrated across multiple shared Kubernetes clusters.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform/images/namespace-sameness.png)

This diagram illustrates namespace sameness across three shared clusters, each for container workloads corresponding to the development lifecycle of an organization. There are two project namespaces `backend` and `frontend` that provide namespaces that span across the clusters. Although a project namespace is replicated across multiple shared clusters, it's recognized as a single namespace with consistent permissions and characteristics.

## What's next

  * [Create a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-a-project)
  * [Design access boundaries between resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/access-boundaries)
  * [Design workload separation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/workload-separation)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
