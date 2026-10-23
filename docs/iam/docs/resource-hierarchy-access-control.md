---
url: https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control/
title: Using resource hierarchy for access control \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:48.778343+00:00
---

# Using resource hierarchy for access control  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Using resource hierarchy for access control Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** You can now use [deny policies](https://docs.cloud.google.com/iam/docs/deny-overview) to prevent principals from using some permissions. Using deny policies might cause the features described on this page to work differently. 

Google Cloud resources are organized hierarchically, where the organization node is the root node in the hierarchy, the projects are the children of the organization, and the other resources are descendants of projects. You can set allow policies at different levels of the resource hierarchy. Resources inherit the allow policies of the parent resource. The effective allow policy for a resource is the union of the allow policy set at that resource and the allow policy inherited from its parent.

This page describes some examples of how allow policy inheritance works and explains the best practices that you must take into consideration when you create resources during Identity and Access Management (IAM) deployment.

## Prerequisites

  * Understand the [basic concepts](https://docs.cloud.google.com/iam/docs/overview) of IAM, in particular the [Google Cloud resource hierarchy](https://docs.cloud.google.com/iam/docs/overview#resource-hierarchy).



## Background

The following diagram shows an example of a Google Cloud resource hierarchy.

![From top to bottom, the hierarchy includes organizations, folders, projects, and service-specific resources.](https://docs.cloud.google.com/static/iam/img/policy-inheritance.svg)

![](https://docs.cloud.google.com/static/iam/img/policy-inheritance.svg)

IAM lets you set allow policies at the following levels of the resource hierarchy:

  * **Organization level**. The organization resource represents your company. IAM roles granted at this level are inherited by all resources under the organization. For more information, see [Access control for organizations using IAM](https://docs.cloud.google.com/resource-manager/docs/access-control-org).

  * **Folder level**. Folders can contain projects, other folders, or a combination of both. Roles granted at the highest folder level will be inherited by projects or other folders that are contained in that parent folder. For more information, see [Access control for folders using IAM](https://docs.cloud.google.com/resource-manager/docs/access-control-folders).

  * **Project level**. Projects represent a trust boundary within your company. Services within the same project have a default level of trust. IAM roles granted at the project level are inherited by resources within that project. For more information, see [Access control for projects using IAM](https://docs.cloud.google.com/resource-manager/docs/access-control-proj).

  * **Resource level**. In addition to the existing Cloud Storage and BigQuery ACL systems, additional resources such as Pub/Sub topics and Compute Engine instances support lower-level roles so that you can grant certain users permission to a single resource within a project.




Allow policies are hierarchical and propagate down the structure. The effective allow policy for a resource is the union of the allow policy set at that resource and the allow policy inherited from its parent.

The following examples explain how allow policy inheritance works in practice.

### Example: Pub/Sub

In Pub/Sub, topics and subscriptions are resources that live under a project. Assume that `project_1` has a topic `topic_a` under it. If you set an allow policy on `project_1` that grants the Editor role to Kalani, and set an allow policy on `topic_a` that grants the Publisher role to Nur, you effectively grant the Editor role to Kalani and the Publisher role to Nur for `topic_a`.

The following diagram illustrates the preceding example.

![Pub/Sub example.](https://docs.cloud.google.com/static/iam/img/resource-hierarchy-pubsub-1.svg)

![](https://docs.cloud.google.com/static/iam/img/resource-hierarchy-pubsub-1.svg)

If an inherited role already gives a principal all of the permissions that they need, then you don't need to grant them additional roles on the resource itself. Granting another role that contains the same or fewer permissions is redundant, and doesn't have any effect.

For example, consider the basic roles Owner, Editor, and Viewer. These roles are concentric; that is, the Owner role includes the permissions in the Editor role, and the Editor role includes the permissions of the Viewer role. As a result, if you grant Kalani the Editor role at the project level, then granting them the Viewer role on `topic_a` is redundant. This is because Kalani already has all of the permissions in the Viewer role through the Editor role, which is inherited from the project's allow policy.

The following diagram illustrates the preceding example.

![Pub/Sub example.](https://docs.cloud.google.com/static/iam/img/resource-hierarchy-pubsub-2.svg)

![](https://docs.cloud.google.com/static/iam/img/resource-hierarchy-pubsub-2.svg)

### Example: Cloud Storage

In Cloud Storage, buckets and objects are resources, and objects are located in buckets. An example of using IAM with Cloud Storage is to allow read access to files that are uploaded.

Consider a scenario where many users upload files to a bucket, but they shouldn't be able to read or delete any of the files uploaded by other users. Your data processing expert should be able to read and delete uploaded files, but they shouldn't be able to delete buckets because others are using the bucket location to upload their files. In this scenario, you would set allow policies on the project as follows:

  * Grant the [Storage Object Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`) to your data processing expert, Nur. This role lets Nur read, add, and delete any object in any bucket in the project.
  * Grant the [Storage Object Creator role](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectCreator) (`roles/storage.objectCreator`) to the `data-uploaders` group. This role lets group members upload files to the bucket, but doesn't let them read or delete any files that other users upload.



The following diagram illustrates the preceding example.

![Cloud Storage example.](https://docs.cloud.google.com/static/iam/img/resource-hierarchy-storage.svg)

![](https://docs.cloud.google.com/static/iam/img/resource-hierarchy-storage.svg)

### Example: Compute Engine

In larger companies, the management of network and security resources such as firewalls are typically managed by a dedicated team, which is different from the development team. The development teams might want the flexibility to launch instances and carry out other actions related to instances in their projects.

In a situation like this, you could configure your allow policies as follows:

  * Grant the [Compute Network Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) to your network and security administrator, Kalani, at the organization level. This role lets Kalani make changes to the network resources in the organization and in any projects under that organization.
  * Grant the [Compute Instance Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`) to a development team lead, Nur, on their project `project_2`. This role lets Nur carry out any actions on their instances while preventing them from making any changes to the network resources associated with their project. However, it doesn't let them make changes to network resources in other projects.



![Compute Engine example.](https://docs.cloud.google.com/static/iam/img/resource-hierarchy-compute.svg)

![](https://docs.cloud.google.com/static/iam/img/resource-hierarchy-compute.svg)

## Permissions for viewing inherited policies

To view IAM policies that are inherited from a parent resource, you need permission to view the parent resource's IAM policy. For example, to view all inherited IAM policies for a project, you need permission to view the IAM policy of the project's parent organization and to view the IAM policies of any parent folders.

To get the permissions that you need to view IAM policies that are inherited from parent resources, ask your administrator to grant you the following IAM roles: 

  * View an IAM policy that is inherited from an organization: [Organization Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationAdmin) (`roles/resourcemanager.organizationAdmin`) on the organization 
  * View an IAM policy that is inherited from a folder: [Folder Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.folderAdmin) (`roles/resourcemanager.folderAdmin`) on the folder 
  * View an IAM policy that is inherited from a project: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) on the project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to view IAM policies that are inherited from parent resources. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view IAM policies that are inherited from parent resources:

  * View an IAM policy that is inherited from an organization: `resourcemanager.organizations.getIamPolicy` on the organization 
  * View an IAM policy that is inherited from a folder: `resourcemanager.folders.getIamPolicy` on the folder 
  * View an IAM policy that is inherited from a project: `resourcemanager.projects.getIamPolicy` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** In the Google Cloud console, a resource's IAM page only shows inherited roles if the roles are [grantable on the resource](https://docs.cloud.google.com/iam/docs/viewing-grantable-roles).

## Best practices

  * Mirror your Google Cloud resource hierarchy structure to your organization structure. The Google Cloud resource hierarchy should reflect how your company is organized, whether it's a startup, a SME, or a large corporation. A startup may start out with a flat resource hierarchy with no organization resource. When more people start collaborating on projects and the number of projects increase, getting an organization resource might make sense. An organization resource is recommended for larger companies with multiple departments and teams where each team is responsible for their own set of applications and services.

  * Use projects to group resources that share the same trust boundary. For example, resources for the same product or microservice can belong to the same project.

  * Grant roles to a group instead of to individual users when possible. It is easier to manage members in a group than to update an allow policy. Make sure to control the ownership of the group used in allow policies.

For more information about how to manage Google groups, see [Google Groups help](https://support.google.com/groups/).

  * Use the security principle of [least privilege](https://wikipedia.org/wiki/Principle_of_least_privilege) to grant IAM roles; that is, only give the least amount of access necessary to your resources.

To find the appropriate predefined role, see the [predefined roles reference](https://docs.cloud.google.com/iam/docs/roles-permissions). If there are no appropriate predefined roles, you can also create your own [custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles).

  * Grant roles at the smallest scope needed. For example, if a user only needs access to publish messages to a Pub/Sub topic, grant the [Publisher](https://docs.cloud.google.com/pubsub/access_control#tbl_roles) role to the user for that topic.

  * Remember that the allow policies for child resources inherit from the allow policies for their parent resources. For example, if the allow policy for a project grants a user the ability to administer Compute Engine virtual machine (VM) instances, then the user can administer any Compute Engine VM in that project, regardless of the allow policy you set on each VM.

  * On every project, ensure that at least two principals have the Owner role (`roles/owner`). Alternatively, grant the Owner role to a group that contains at least two principals.

This practice helps ensure that if one of the principals leaves your company, you still have a way to manage your project.

  * If you need to grant a role to a user or group that spans across multiple projects, set that role at the folder level instead of setting it at the project level.

  * Use labels to annotate, group, and filter resources.

  * Audit your allow policies to ensure compliance. [Audit logs](https://docs.cloud.google.com/logging/docs/audit) contain all `setIamPolicy()` calls, so you can trace when an allow policy has been created or modified.

  * Audit the ownership and the membership of the groups used in allow policies.

  * If you want to limit project creation in your organization, change the [organization access policy](https://docs.cloud.google.com/resource-manager/docs/access-control-org) to grant the [Project Creator role](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager) to a group that you manage.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
