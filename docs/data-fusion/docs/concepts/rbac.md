---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/rbac/
title: Role-based access control (RBAC) overview \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:59.228023+00:00
---

# Role-based access control (RBAC) overview  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/concepts/rbac/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Role-based access control (RBAC) overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes fine-grained authorization with role-based access control (RBAC) in Cloud Data Fusion.

Enabling RBAC in your Cloud Data Fusion instances lets you control access within instances and namespaces, such as who can access Cloud Data Fusion resources and what they can do with them.

## Use cases for RBAC

RBAC provides namespace-level isolation within a single Cloud Data Fusion instance. It's recommended for the following use cases:

  * Helping minimize the number of instances used by your organization.
  * Having multiple developers, teams, or business units use a single Cloud Data Fusion instance.



With Cloud Data Fusion RBAC, organizations can:

  * Allow a user to only run a pipeline within a namespace, but not modify artifacts or runtime compute profiles.
  * Allow a user to only view the pipeline, but not modify or run a pipeline.
  * Allow a user to create, deploy, and run a pipeline.



**Recommended:** Even when you use RBAC, to maintain isolation, security, and performance stability, use separate projects and instances for development and production environments.

## Limitations

  * A user can be granted with one or multiple roles at either instance or namespace level.
  * RBAC is only available in the Cloud Data Fusion **Enterprise** edition.
  * Number of namespaces: No hard limit on the number of namespaces per instance.
  * For the maximum number of concurrent users in an RBAC-enabled instance, see [Pricing](https://cloud.google.com/data-fusion/pricing#compare_editions).
  * When using service account OAuth access tokens to access version 6.5 RBAC-enabled instances, the following scopes must be specified, especially the `userinfo.email` scope. Without them, you will encounter permission denied errors. 
    * `https://www.googleapis.com/auth/userinfo.email`
    * `https://www.googleapis.com/auth/cloud-platform` or `https://www.googleapis.com/auth/servicecontrol`



## Role assignments

**Key Point:** To control who has access to resources with RBAC, you assign [IAM roles](https://docs.cloud.google.com/iam/docs/overview#roles).

A role assignment consists of three elements: principal, role definition, and scope.

### Principal

You grant roles to [principals](https://docs.cloud.google.com/iam/docs/overview#how_cloud_iam_works) to change their access to Cloud Data Fusion resources.

### Role definition

A role contains a set of permissions that allows you to perform specific actions on Google Cloud resources. 

Cloud Data Fusion provides several [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions) that you can use.

**Examples:**

  * The Instance Admin role (`datafusion.admin`) lets principals create and delete namespaces, and grant permissions.
  * The Developer role (`datafusion.developer`) lets principals create and delete pipelines, deploy pipelines, and run previews.



### Scope

The scope is the set of resources that the access applies to. When you assign a role, you can further limit the actions allowed by defining a scope, such as an instance or a namespace. This is helpful if you want to assign somebody the Developer role, but only for one namespace.

## Security recommendations

Adopting a security model and catering it to your organization's needs and requirements can be challenging. The following recommendations are intended to help you simplify your journey to adopt Cloud Data Fusion's RBAC model:

  * **Instance Admin role** should be granted cautiously. This role enables full access to an instance and all its underlying Cloud Data Fusion resources. A principal with this role can grant permissions to others by using the REST API.
  * **Instance Admin role** shouldn't be granted when principals are required to have access to individual namespaces within a Cloud Data Fusion instance. Instead, grant the Instance Accessor role with one of the Viewer/Developer/Operator/Editor roles granted on a subset of the namespaces.
  * **Instance Accessor** role is safe to assign first, as it enables principals' access to instance, but won't grant access to any resources within the instance. This role is typically used along with one of Viewer/Developer/Operator/Editor to give access to one or a subset of the namespaces within an instance.
  * **Viewer role** is recommended to be assigned to users or Google groups who would like to self-serve for understanding the status of running jobs, or viewing pipelines or logs with Cloud Data Fusion instances. For example, consumers of daily reports who would like to know whether processing has been completed.
  * **Developer role** is recommended for ETL developers who are responsible for creating, testing, and managing pipelines.
  * **Operator role** for a namespace is recommended for users who are providing operations administrator or DevOps services. They are able to perform all actions that developers can perform (except for previewing pipelines) and also deploy artifacts and manage compute profiles.
  * **Editor role** for a namespace is a privileged role that gives the user or Google group full access to all resources in the namespace. Editor can be considered the union of the developer and operator roles.
  * **Operators** and **Admins** should be wary of installing untrusted plugins or artifacts as this can present a security risk.



## Troubleshooting

This page section shows you how to resolve issues related to RBAC in Cloud Data Fusion.

### A principal who has the Cloud Data Fusion Viewer role for a namespace in RBAC can edit pipelines

Access is based on a combination of IAM and RBAC roles. IAM roles have precedence over RBAC roles. Check if the principal has [Project Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) or [Cloud Data Fusion Admin](https://docs.cloud.google.com/data-fusion/docs/access-control#roles) IAM roles.

### A principal who has the Instance Admin role in RBAC can't view Cloud Data Fusion instances in the Google Cloud console

There is a known issue in Cloud Data Fusion where principals with the Instance Admin role cannot view instances in the Google Cloud console. To fix the issue, grant either the [Project Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) or one of the [Cloud Data Fusion IAM roles](https://docs.cloud.google.com/data-fusion/docs/access-control#roles) to the principal in addition to making them Admin to an instance. This grants Viewer access to the principal for all instances in the project.

### Prevent a principal from viewing namespaces where they have no role

To prevent a principal from viewing namespaces where they have no role, they must not have the [Project Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) or any of the [Cloud Data Fusion IAM roles](https://docs.cloud.google.com/data-fusion/docs/access-control#roles). Instead, only grant RBAC roles to the principal in the namespace where they need to operate.

The principal with this kind of access won't see the list of Cloud Data Fusion instances in the Google Cloud console. Instead, give them a direct link to the instance, similar to the following: `https://INSTANCE_NAME-PROJECT_ID.REGION_NAME.datafusion.googleusercontent.com/`

When the principal opens the instance, Cloud Data Fusion displays a list of namespaces where the principal is granted RBAC role. 

### Grant the Cloud Data Fusion Accessor role to a principal

The Accessor role is implicitly assigned to a principal when any other RBAC role is assigned to them for any Cloud Data Fusion instance. To verify if a principal has that role on a particular instance, see the [IAM Policy Analyzer](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies#policy-analyzer-what-access-console).

## What's next

  * Learn how to [use RBAC in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/how-to/create-role-based-access-control).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
