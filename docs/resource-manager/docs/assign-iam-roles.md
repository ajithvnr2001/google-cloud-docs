---
url: https://docs.cloud.google.com/resource-manager/docs/assign-iam-roles/
title: Assign Identity and Access Management roles and permissions \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:44:01.539858+00:00
---

# Assign Identity and Access Management roles and permissions  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/assign-iam-roles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)



Send feedback 

#  Assign Identity and Access Management roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** When assigning permissions related to a cross-organization-resource migration, you must designate the roles on the same principal email address in both the source and the destination organization resources.

You need the following permissions to migrate a project between organization resources.

To gain these permissions, ask your administrator to grant the suggested role at the appropriate level of the [resource hierarchy](https://docs.cloud.google.com/iam/docs/tags-access-control#resource-hierarchy).

### Project migration permissions

To migrate a project between organization resources, you need the following roles on the project, its parent resource, and the destination resource:

  * Project IAM Admin (`roles/resourcemanager.projectIamAdmin`) on the project that you want to migrate between organization resources.
  * Project Mover (`roles/resourcemanager.projectMover`) on the project's parent resource (folder or organization resource).
  * **If the destination resource is a folder:** Project Mover (`roles/resourcemanager.projectMover`) on the destination resource.
  * **If the destination resource is an organization resource:** Project Creator (`roles/resourcemanager.projectCreator`) on the destination resource.



These roles give you the following required permissions:

#### Required permissions

  * `resourcemanager.projects.getIamPolicy` on the project you want to migrate between organization resources 
  * `resourcemanager.projects.update` on the project you want to migrate between organization resources 
  * `resourcemanager.projects.move` on the project's parent resource (folder or organization resource) 
  * **If the destination resource is a folder:** `resourcemanager.projects.move` on the destination resource 
  * **If the destination resource is an organization resource:** `resourcemanager.projects.create` on the destination resource 
  * **If you want to migrate a project that is not associated with an organization:** `resourcemanager.projects.setIamPolicy` on the project you want to migrate 



You can also gain these permissions with a [custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles), or other predefined roles.

### Organization policy permissions

On the source and destination organization resources, the user setting the organization policies must have the `roles/orgpolicy.policyAdmin` role, which grants permission to create and manage organization policies.

### Billing account permissions

Cloud Billing accounts can be used across organization resources. Moving a project from one organization resource to another won't impact billing, and charges will continue against the old billing account. However, migration of projects between organization resources often also include a requirement to migrate to a new billing account.

To get the permissions that you need to change the project's billing account, ask your administrator to grant you the following IAM roles: 

  * [Billing Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.user) (`roles/billing.user`) on the destination billing account
  * [Project billing manager ](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.projectManager) (`roles/billing.projectManager`) on the project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to change the project's billing account. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to change the project's billing account:

  * `billing.resourceAssociations.create` on the destination billing account
  * `resourcemanager.projects.createBillingAssignment` on the project
  * `resourcemanager.projects.deleteBillingAssignment` on the project



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## What's next

To learn about how to configure organization policies, see [Configure organization policies](https://docs.cloud.google.com/resource-manager/docs/configure-org-policy).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
