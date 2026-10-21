---
url: https://docs.cloud.google.com/docs/get-started/organize-resources/
title: Organize resources \u00a0|\u00a0 Get started \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:22.048755+00:00
---

# Organize resources  |  Get started  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/get-started/organize-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Get started ](https://docs.cloud.google.com/docs/get-started)
  * [ Guides ](https://docs.cloud.google.com/docs/overview)



Send feedback 

#  Organize resources Stay organized with collections  Save and categorize content based on your preferences. 

As you develop your applications and workloads on Google Cloud, you create the following resource types:

  * _Container resources_ help you organize and control access. These resources include organizations, folders, and projects.
  * _Service resources_ are fundamental components that make up Google Cloud products and services. These resources include Compute Engine virtual machines (VMs), Google Kubernetes Engine clusters, and Pub/Sub topics.



This document provides provides an overview of organizing your service resources using container resources and App Hub applications. For additional guidance, see the following documentation:

  * [Decide a resource hierarchy for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy)
  * [Application-centric Google Cloud](https://docs.cloud.google.com/app-hub/docs/application-centric-google-cloud)



## Organize and manage hierarchically

To isolate resources from each other and limit access to users, you can group and manage resources as a single unit. You do this using the following structure, known as the resource hierarchy:

  * _Organization_ : Represents your company, and serves as the root of your resource hierarchy.
  * _Folders_ : An optional grouping mechanism you can use to isolate groups of projects. For example, you might create folders for legal entities, departments, or teams.
  * _Projects_ : The base-level organizing entity that contains your service resources.



For a detailed overview of the resource hierarchy, see [Resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).

To learn how to use the resource hierarchy to manage access, see [Using resource hierarchy for access control](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control).

### Organization: Create the root of your hierarchy

An organization is the root node of the hierarchy, under which you create all other resources. The access policies you apply to your organization are applied to all other resources. This means that you can apply an access control at the organization level instead of duplicating and managing the same control across all projects.

When you create an organization resource, underlying projects belong to the organization, instead of the users who create projects. This means that projects and their underlying resources can continue to exist, even if a user is removed.

### Folders: Isolate groups of projects

You can use folders to create isolation boundaries between projects. For example, you might have distinct project collections for departments or teams. Folders can contain projects and subfolders. You can apply access controls to ensure that users in one team cannot access resources in folders assigned to another team.

### Projects: Isolate resources

Google Cloud resources must belong to a project, which is an organizing entity that helps you isolate and control access to resources. For example, you might create distinct projects for development and production environments.

A project contains settings, permissions, and other metadata that describe your applications. Resources within a single project can work together by communicating through an internal network, subject to regions-and-zones rules. A project can't access another project's resources unless you use [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) or [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering).

#### Name and reference your projects

You use identifiers to reference your projects in commands and API calls. Each Google Cloud project has the following identifiers:

  * **Project name** : A name that you provide.
  * **Project ID** : An identifier that you can provide or Google Cloud can provide for you. Each project ID is unique across Google Cloud. After you delete a project, its ID can never be used again.
  * **Project number** : Provided by Google Cloud.



For more information, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

## Manage related resources as applications

The resource hierarchy is useful for organizing your resources to support internal requirements such as team ownership, geography, or compliance with policies. However, cloud applications often combine resources in ways that don't match the resource hierarchy. For example, an online shop might have user interface components in one project and a database in another project.

Google Cloud helps you to group your resources together as [App Hub applications](https://docs.cloud.google.com/app-hub/docs/key-concepts#application) without changing the structure of the resource hierarchy. By grouping related resources together, you can better understand resource dependencies and simplify deployment, monitoring, updates, troubleshooting, and other tasks. In addition, you can use Gemini Cloud Assist to help you with tasks such as designing applications, troubleshooting, and managing application costs.

To learn more, see [Application-centric Google Cloud](https://docs.cloud.google.com/app-hub/docs/application-centric-google-cloud).

[ Previous arrow_back  Consider geographic distribution  ](https://docs.cloud.google.com/docs/get-started/consider-geographic-distribution)

[ Next Consider maintenance  arrow_forward  ](https://docs.cloud.google.com/docs/get-started/consider-resource-maintenance)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
