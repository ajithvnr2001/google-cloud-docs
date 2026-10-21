---
url: https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy/
title: Decide a resource hierarchy for your Google Cloud landing zone \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:28.334386+00:00
---

# Decide a resource hierarchy for your Google Cloud landing zone  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Decide a resource hierarchy for your Google Cloud landing zone Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-01-02 UTC

A resource hierarchy helps to organize your resources in Google Cloud. This document describes how to choose your resource hierarchy as part of your [landing zone](https://docs.cloud.google.com/architecture/landing-zones) design. It's intended for cloud system administrators, architects, and technical practitioners who are involved in designing the resource hierarchy. This document is part of a series on landing zones. It includes sample hierarchies that demonstrate common ways that businesses can structure resources in Google Cloud.

## Design factors for resource hierarchy

When you define your [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) in Google Cloud, you must consider how your organization works today and the ideal end state of your cloud transformation. The best way to manage resources is based on your organization's intended way of working in the cloud. As every organization is different, there is no single, best approach for resource hierarchy.

However, we recommend that you avoid mapping your corporate organization structure to the resource hierarchy. Instead, focus on your business needs and operations in Google Cloud.

### Google Cloud resource hierarchy

The [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) in Google Cloud starts at the root node, which is called the _organization_. We recommend that businesses have only one root node, except for in specific situations. You define lower levels of the hierarchy using [_folders_](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#folders) and [_projects_](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects), and you create folders within folders to build your hierarchy. You can create the projects that host your workloads at any level of the hierarchy.

The following diagram shows a root node called _Organization_ , and folders at levels one, two, and three. Projects and subfolders are created under the folders in level two.

![Example hierarchy with root node, folders, and projects.](https://docs.cloud.google.com/static/architecture/landing-zones/images/decide-resource-hierarchy-example.svg)

### Resource hierarchy factors

When you decide your resource hierarchy, consider the following factors:

  * Who is responsible for cloud resources? Is it your departments, subsidiaries, technical teams, or legal entities?
  * What are your compliance needs?
  * Do you have upcoming business events, such as mergers, acquisitions, and spin-offs?



### Understand resource interactions throughout the hierarchy

[Organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) are inherited by descendants in the resource hierarchy, but can be superseded by policies defined at a lower level. For more information, see [understanding hierarchy evaluation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy). You use organization policy constraints to set guidelines around the whole organization or significant parts of it and still allow for exceptions.

[Allow policies](https://docs.cloud.google.com/iam/docs/overview) are inherited by descendants, and allow policies at lower levels are additive. However, allow policies can be superseded by [deny policies](https://docs.cloud.google.com/iam/docs/deny-overview), which let you restrict permissions at the project, folder, and organization level. Deny policies are applied before allow policies.

You also need to consider the following:

  * [Cloud Logging](https://docs.cloud.google.com/logging/docs) includes [aggregated sinks](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks) that you can use to aggregate logs at the folder or organization level. For more information, see [decide the security for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-security#aggregate-logs).
  * Billing is not directly linked to the resource hierarchy, but assigned at the project level. However, to get aggregated information at the folder level, you can [analyze your costs by project hierarchy](https://docs.cloud.google.com/billing/docs/how-to/reports-project-hierarchy) using billing reports.
  * [Hierarchical firewall policies](https://docs.cloud.google.com/vpc/docs/firewall-policies) let you implement consistent firewall policies throughout the organization or in specific folders. Inheritance is implicit, which means that you can allow or deny traffic at any level or you can delegate the decision to a lower level.



## Decision points for resource hierarchy design

The following flowchart shows the things that you must consider to choose the best resource hierarchy for your organization.

![Decisions for resource hierarchies.](https://docs.cloud.google.com/static/architecture/landing-zones/images/decide-resource-hierarchy-flow.svg)

The preceding diagram outlines the following decision points:

  1. Do different subsidiaries, regional groups, or business units have very different policy requirements? 
     1. If yes, follow the design based on region or subsidiaries.
     2. If no, go to the next decision point.
  2. Do your workload or product teams require strong autonomy over their policies? For example, you don't have a central security team that determines policies for all workload or product teams.

     1. If yes, see the design based on accountability framework.

     2. If no, see the design based on application environment.




Your specific use case might lead you to another resource hierarchy design than what the decision chart suggests. Most organizations choose a hybrid approach and select different designs at different levels of the resource hierarchy, starting with the design that most affects policies and access.

## Option 1: Hierarchy based on application environments

In many organizations, you define different policies and access controls for different application environments, such as development, production, and testing. Having separate policies that are standardized across each environment eases management and configuration. For example, you might have security policies that are more stringent in production environments than in testing environments.

Use a hierarchy based on application environments if the following is true:

  * You have separate application environments that have different policy and administration requirements.
  * You have centralized security or audit requirements that a central security team must be able to enforce consistently on all production workloads and data.
  * You require different Identity and Access Management (IAM) roles to access your Google Cloud resources in different environments.



Avoid this hierarchy if the following is true:

  * You don't run multiple application environments.
  * You don't have varying application dependencies and business processes across environments.
  * You have strong policy differences for different regions, teams, or applications.



The following diagram shows a hierarchy for example.com, which is a fictitious financial technology company.

![Option 1 diagram.](https://docs.cloud.google.com/static/architecture/landing-zones/images/decide-resource-hierarchy-option1.svg)

As shown in the preceding diagram, example.com has three application environments that have different policies, access controls, regulatory requirements, and processes. The environments are as follows:

  * **Development and QA environment:** This environment is managed by developers who are both internal employees and consultants. They continuously push code and are responsible for quality assurance. This environment is never available to your business' consumers. The environment has less strict integration and authentication requirements than the production environment, and developers are assigned approved roles with suitable permissions. The Development and QA environment is designed only for standard application offerings from example.com.

  * **Testing environment:** This environment is used for regression and application testing, and supports the business-to-business (B2B) offerings of example.com clients who use example.com APIs. For this purpose, example.com creates two project types:

    * Internal testing projects to complete internal regression, performance, and configuration for B2B offerings.
    * Client UAT projects with multi-tenant support so that B2B clients can validate their configurations and align with example.com requirements for user experience, branding, workflows, reports, and so on.
  * **Production environment:** This environment hosts all product offerings that are validated, accepted, and launched. This environment is subject to Payment Card Industry Data Security Standard (PCI DSS) regulations, uses hardware security modules (HSMs), and integrates with third-party processors for items such as authentication and payment settlements. The audit and compliance teams are critical stakeholders of this environment. Access to this environment is tightly controlled and limited mostly to automated deployment processes.




For more information about designing a hierarchy that is based on application environments, see [Organization structure](https://docs.cloud.google.com/architecture/security-foundations/organization-structure) in the enterprise foundations blueprint.

## Option 2: Hierarchy based on regions or subsidiaries

Some organizations operate across many regions and have subsidiaries doing business in different geographies or have been a result of mergers and acquisitions. These organizations require a resource hierarchy that uses the scalability and management options in Google Cloud, and maintains the independence for different processes and policies that exist between the regions or subsidiaries. This hierarchy uses subsidiaries or regions as the highest folder level in the resource hierarchy. Deployment procedures are typically focused around the regions.

Use this hierarchy if the following is true:

  * Different regions or subsidiaries operate independently.
  * Regions or subsidiaries have different operational backbones, digital platform offerings, and processes.
  * Your business has different regulatory and compliance standards for regions or subsidiaries.



The following diagram shows an example hierarchy of a global organization with two subsidiaries and a holding group with a regionalized structure.

![Option 2 diagram.](https://docs.cloud.google.com/static/architecture/landing-zones/images/decide-resource-hierarchy-option2.svg)

The preceding diagram has the following hierarchy structure:

  * The following folders are on the first level: 
    * The `Subsidiary 1` and `Subsidiary 2` folders represent the two subsidiaries of the company that have different access permissions and policies from the rest of the organization. Each subsidiary uses [IAM](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control) to restrict access to their projects and Google Cloud resources.
    * The `Holding group` folder represents the groups that have high-level common policies across regions.
    * The `Bootstrap` folder represents the common resources that are required to deploy your Google Cloud infrastructure, as described in the [enterprise foundations blueprint](https://docs.cloud.google.com/architecture/security-foundations/organization-structure#folders).
  * On the second level, within the _Group Holding_ folder, there are the following folders: 
    * The `APAC`, `EMEA`, and `Americas` folders represent the various regions within the group that have different governance, access permissions, and policies.
    * The `Shared infrastructure` folder represents resources that are used globally across all regions.
  * Within each folder are various projects that contain the resources that these subsidiaries or regions are responsible for.



You can add more folders to separate different legal entities, departments, and teams within your company.

## Option 3: Hierarchy based on an accountability framework

A hierarchy based on an accountability framework works best when your products are run independently or organizational units have clearly defined teams who own the lifecycle of the products. In these organizations, the product owners are responsible for the entire product lifecycle, including its processes, support, policies, security, and access rights. Your products are independent from each other, and organization-wide guidelines and controls are uncommon.

Use this hierarchy when the following is true:

  * You run an organization that has clear ownership and accountability for each product.
  * Your workloads are independent and don't share many common policies.
  * Your processes and external developer platforms are offered as service or product offerings.



The following diagram shows an example hierarchy for an ecommerce platform provider.

![Option 3 diagram.](https://docs.cloud.google.com/static/architecture/landing-zones/images/decide-resource-hierarchy-option3.svg)

The preceding diagram has the following hierarchy structure:

  * The following folders are on the first level: 
    * The folders that are named `Ecommerce Modules` and `Logistics and Warehousing Modules` represent the modules within the platform offering that require the same access permissions and policies during the product lifecycle.
    * The `Reconciliation and Billing` folder represents the product teams who are responsible for the end-to-end modules for specific business components within the platform offering.
    * The `Bootstrap` folder represents the common resources that are required to deploy your Google Cloud infrastructure, as described in the [enterprise foundations blueprint](https://docs.cloud.google.com/architecture/security-foundations/organization-structure#folders).
  * Within each folder are various projects that contain the independent modules that different product teams are responsible for.



## Best practices for resource hierarchy

The following sections describe the best practices for designing resource hierarchy that we recommend, regardless of the resource hierarchy that you choose.

For more best practices on how to configure your Cloud Identity and Google Workspace accounts and organizations, see [Best practices for planning accounts and organizations](https://docs.cloud.google.com/architecture/identity/best-practices-for-planning).

### Use a single organization node

To avoid management overhead, use a single organization node whenever possible. However, consider using multiple organization nodes to address the following use cases:

  * You want to test major changes to your IAM levels or resource hierarchy.
  * You want to experiment in a sandbox environment that doesn't have the same organization policies.
  * Your organization includes sub-companies that are likely to be sold off or run as completely separate entities in the future.



### Use standardized naming conventions

Use a standardized naming convention throughout your organization. The enterprise foundations blueprint has a [sample naming convention](https://docs.cloud.google.com/architecture/security-foundations/summary#naming-conventions) that you can adapt to your requirements.

### Keep bootstrapping resources and common services separate

Keep separate folders for bootstrapping the Google Cloud environment using infrastructure-as-code (IaC) and for common services that are shared between environments or applications. Place the bootstrap folder right below the organization node in the resource hierarchy.

Place the folders for common services at different levels of the hierarchy, depending on the structure that you choose.

Place the folder for common services right below the organization node when the following is true:

  * Your hierarchy uses application environments at the highest level and teams or applications at the second layer.
  * You have shared services such as monitoring that are common between environments.



Place the folder for common services at a lower level, below the application folders, when the following is true:

  * You have services that are shared between applications and you deploy a separate instance for each deployment environment.

  * Applications share microservices that require development and testing for each deployment environment.




The following diagram shows an example hierarchy where there is a shared infrastructure folder that is used by all environments and shared services folders for each application environment at a lower level in the hierarchy:

![Example hierarchy with shared infrastructure folder.](https://docs.cloud.google.com/static/architecture/landing-zones/images/decide-resource-hiearchy-shared-infra-example.svg)

The preceding diagram has the following hierarchy structure:

  * The folders on the first level are as follows: 
    * The `Development environment` and `Production environment` folders contain the application environments.
    * The `Shared infrastructure` folder contains common resources that are shared across environments, such as monitoring.
    * The `Bootstrap` folder contains the common resources required to deploy your Google Cloud infrastructure, as described in the [enterprise foundations blueprint](https://docs.cloud.google.com/architecture/security-foundations/organization-structure#folders).
  * On the second level, there are the following folders: 
    * A folder in each environment for each application (`App 1` and `App 2`) which contains the resources for these applications.
    * A `Shared` folder for both application environments that contains services that are shared between the applications but are independent for each environment. For example, you might have a [folder-level secrets project](https://docs.cloud.google.com/architecture/security-foundations/organization-structure#projects) so that you can apply different allow policies to your production secrets and non-production secrets.
  * Within each application folder are various projects that contain the independent modules that are part of each application.



## What's next

  * [Design the network for your landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-network-design) (the next document in this series).
  * Review the [enterprise foundations blueprint](https://docs.cloud.google.com/architecture/security-foundations).
  * Read the blueprints and whitepapers that are available in the [Google Cloud security best practices center](https://cloud.google.com/security/best-practices).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-02 UTC."],[],[]] 
