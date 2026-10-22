---
url: https://docs.cloud.google.com/iam/docs/overview/
title: IAM overview \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:14.079513+00:00
---

# IAM overview  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  IAM overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how Google Cloud's Identity and Access Management (IAM) system works and how you can use it to manage access in Google Cloud.

IAM is a tool to manage fine-grained authorization for Google Cloud. In other words, it lets you control _who_ can do _what_ on _which resources_.

## Access in Google Cloud

Every action in Google Cloud requires certain permissions. When someone tries to perform an action in Google Cloud—for example, create a VM instance or view a dataset—IAM first checks if they have the required permissions. If they don't, then IAM prevents them from performing the action.

Giving someone permissions in IAM involves the following three components:

  * **Principal** : The identity of the person or system that you want to give permissions to.
  * **Role** : The collection of permissions that you want to give the principal.
  * **Resource** : The Google Cloud resource that you want to let the principal access.



To give the principal permission to access the resource, you grant them a role on the resource. You grant these roles using an _allow policy_.

Allow policies are directly attached to some Google Cloud resources, which are organized hierarchically—for example, projects contain service-specific resources. This means that you can grant access to a single resource or a container of resources.

The following sections describe these concepts in more detail.

### Principals

In Google Cloud you control access for _principals_. Principals represent one or more identities that have authenticated to Google Cloud.

In the past, principals were referred to as _members_. Some APIs still use that term.

There are various types of principals in IAM, but they can be divided into two broad categories:

  * **Human users** : Some IAM principal types represent human users. You use these principal types for managing your employees' access to Google Cloud resources.

Principal types that represent human users include Google Accounts, Google groups, and federated identities in workforce identity pools. 

  * **Workloads** : Some IAM principal types represent workloads. You use these principal types when managing your workloads' access to Google Cloud resources.

Principal types that represent workloads include service accounts and federated identities in a workload identity pool.




For more information about principals, see [IAM principals](https://docs.cloud.google.com/iam/docs/principals-overview).

### Permissions and roles

Permissions determine what operations are allowed on a resource. In IAM, permissions are typically represented in the form `service.resource.verb`. Often, permissions correspond one-to-one with REST API methods—for example, the `resourcemanager.projects.list` permission lets you list Resource Manager projects.

_You can't directly grant permissions to a principal_. Instead, you give principals permissions by granting them _roles_.

Roles are collections of permissions. When you grant a role to a principal, you give that principal all of the permissions in that role.

There are three types of roles:

  * **Predefined roles** : Roles that are managed by Google Cloud services. These roles contain the permissions needed to perform common tasks for each given service. For example, the Pub/Sub Publisher role (`roles/pubsub.publisher`) provides access to publish messages to a Pub/Sub topic.

  * **Custom roles** : Roles that you create that contain only the permissions that you specify. You have complete control over the permissions in these roles. However, they have a higher maintenance burden than predefined roles and there's a limit to the number of custom roles that you can have in your project and in your organization.

  * **Basic roles** : Highly permissive roles that provide broad access to Google Cloud services. These roles can be useful for testing purposes, but shouldn't be used in production environments.




For more information about roles and permissions, see [Roles and permissions](https://docs.cloud.google.com/iam/docs/roles-overview).

### Resources

Most Google Cloud services have their own resources. For example, Compute Engine has resources like instances, disks, and subnetworks.

In IAM, you grant roles on a resource. Granting a principal a role on a resource means that the principal can use the permissions in that role to access the resource.

You can grant roles on a subset of Google Cloud resources. For a full list of resources that you can grant roles on, see [Resource types that accept allow policies](https://docs.cloud.google.com/iam/docs/resource-types-with-policies).

Google Cloud also has container resources, including projects, folders, and organizations. These container resources are organized hierarchically, which lets child resources inherit the policies of their parent resources. This means that granting a principal a role on a container resource gives the principal access to both the container resource _and_ the resources in that container. This feature lets you use a single role grant to manage access to multiple resources, including resources that you can't grant roles on directly. For more information, see Policy inheritance on this page.

### Allow policies

You grant roles to principals using _allow policies_. In the past, these policies were referred to as _IAM policies_.

An allow policy is a YAML or JSON object that's attached to a Google Cloud resource.

The following diagram shows how an allow policy is structured:

![An allow policy with two role bindings. The role bindings
  associate specific principals with specific roles.](https://docs.cloud.google.com/static/iam/img/iam-overview-basics.svg)

![](https://docs.cloud.google.com/static/iam/img/iam-overview-basics.svg)

Each allow policy contains a list of _role bindings_ that associate IAM roles with the principals who are granted those roles.

When an authenticated principal attempts to access a resource, IAM checks the resource's allow policy to determine whether the principal has the required permissions. If the principal is in a role binding that includes a role with the required permissions, then they're allowed to access the resource.

To see examples of allow policies and learn about their structure, see [Understanding allow policies](https://docs.cloud.google.com/iam/docs/allow-policies).

## Policy inheritance

Google Cloud has container resources—such as projects, folders, and organizations—that let you organize your resources in a parent-child hierarchy. This hierarchy is called the _resource hierarchy_.

The Google Cloud resource hierarchy has the following structure:

  * The _organization_ is the root node in the hierarchy.
  * _Folders_ are children of the organization, or of another folder.
  * _Projects_ are children of the organization, or of a folder.
  * _Resources_ for each service are descendants of projects.



The following diagram is an example of a Google Cloud resource hierarchy:

![Hierarchy for IAM resources.](https://docs.cloud.google.com/static/iam/img/policy-inheritance.svg)

![](https://docs.cloud.google.com/static/iam/img/policy-inheritance.svg)

If you set an allow policy on a container resource, then the allow policy also applies to all resources in that container. This concept is called _policy inheritance_ , because descendant resources effectively inherit their ancestor resources' allow policies.

Policy inheritance has the following implications:

  * **You can use a single role binding to grant access to multiple resources.** If you want to give a principal access to all resources in a container, then grant them a role on the container instead of on the resources in the container.

For example, if you want to let your security administrator manage allow policies for all resources in your organization, then you could grant them the Security Admin role (`roles/iam.securityAdmin`) on the organization.

  * **You can grant access to resources that don't have their own allow policies.** Not all resources accept allow policies, but all resources inherit allow policies from their ancestors. To give a principal access to a resource that can't have its own allow policy, grant them a role on one of the resource's ancestors.

For example, imagine you want to give someone permission to write logs to a log bucket. Log buckets don't have their own allow policies, so to give someone this permission, you can instead grant them the Logs Bucket Writer role (`roles/logging.bucketWriter`) on the project that contains the log bucket.

  * **To understand who can access a resource, you need to also view _all_ of the allow policies that affect the resource**. To get a complete list of the principals that have access to the resource, you need to view the resource's allow policy _and_ the resource's ancestors' allow policies. The union of all of these policies is called the _effective allow policy_.




For more information about policy inheritance for allow policies, see [Using resource hierarchy for access control](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control).

## Advanced access control

In addition to allow policies, IAM provides the following access control mechanisms to help you refine who has access to what resources:

  * **Additional policy types** : IAM offers the following policy types in addition to allow policies:

    * **Deny policies** : Deny policies prevent principals from using certain permissions, even if they're granted a role with the permission.

    * **Principal Access Boundary (PAB) policies** : Principal Access Boundary policies define and enforce the resources a principal is eligible to access. Principals can't access resources that they're not eligible to access, even if they've been granted a role on the resource.

To learn more about these policies, see [Policy types](https://docs.cloud.google.com/iam/docs/policy-types).



  * **IAM Conditions** : IAM Conditions lets you define and enforce conditional, attribute-based access control. You can use conditions in various policy types. For example, you can add a condition to a role binding in an allow policy to ensure that the role is only granted if the condition is met.

You can write conditions based on attributes like the resource in the request and the time of the request.

To learn more about IAM Conditions, see [Overview of IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview).



  * **Privileged Access Manager (PAM)** : With Privileged Access Manager, you can let principals request and be given temporary, auditable access to resources. For example, you could require that principals request access each time they want to view a sensitive resource instead of permanently granting them a IAM role.

You can also configure whether principals are required to provide justifications or get approvals when they request access.

To learn more about Privileged Access Manager, see [Privileged Access Manager overview](https://docs.cloud.google.com/iam/docs/pam-overview).




## Consistency model for the IAM API

The [IAM API](https://docs.cloud.google.com/iam/docs/reference/rest) is [eventually consistent](https://wikipedia.org/wiki/Eventual_consistency). In other words, if you write data with the IAM API, then immediately read that data, the read operation might return an older version of the data. The changes that you make might also take time to affect access checks.

This consistency model affects how the IAM API works. For example, if you create a service account, then immediately refer to that service account in another request, the IAM API might say that the service account couldn't be found. This behavior occurs because operations are eventually consistent; it can take time for the new service account to become visible to read requests.

## What's next

  * To learn how to configure identities for Google Cloud, see [Identity management for Google Cloud](https://docs.cloud.google.com/iam/docs/google-identities).
  * To learn how to grant, change, and revoke IAM roles to principals, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).
  * To see available IAM roles, see [Predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions).
  * To get help with choosing the most appropriate predefined roles, read [Find the right predefined roles](https://docs.cloud.google.com/iam/docs/choose-predefined-roles).
  * To see the policy types available in IAM, see [Policy types](https://docs.cloud.google.com/iam/docs/policy-types).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Get started for free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
