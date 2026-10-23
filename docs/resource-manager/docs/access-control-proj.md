---
url: https://docs.cloud.google.com/resource-manager/docs/access-control-proj/
title: Access control for projects with IAM \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:55:59.096147+00:00
---

# Access control for projects with IAM  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/access-control-proj/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Access control for projects with IAM Stay organized with collections  Save and categorize content based on your preferences. 

[Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) lets you grant granular access to specific Google Cloud resources and prevent unwanted access to others. This model helps you adopt the [principle of least privilege](https://wikipedia.org/wiki/Principle_of_least_privilege), which helps ensure that you grant only the necessary access to your resources.

By setting allow policies, you control _who (users)_ has _what access (roles)_ to _which resources_. To manage access to projects, you configure IAM roles and permissions, or use [deny policies](https://docs.cloud.google.com/iam/docs/deny-overview) to prevent principals from using specific permissions. For more information, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

If you're getting started with Google Cloud, you can establish your resource hierarchy and grant initial access as part of the [Google Cloud setup process](https://docs.cloud.google.com/docs/enterprise/setup-checklist).

## Permissions and roles

To control access to resources, Google Cloud requires that accounts making API requests have appropriate IAM roles. IAM roles include permissions that let users perform specific actions on Google Cloud resources. For example, the `resourcemanager.projects.delete` permission lets a user delete a project.

You don't directly give users permissions; instead, you grant them _roles_ , which have one or more permissions bundled within them. You grant these roles on a particular resource, but they also apply to all of that resource's descendants in the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).

### Permissions

To manage projects, the caller must have a role that includes the following permissions. The role is granted on the organization resource or folder that contains the projects:

Method | Required permission(s)  
---|---  
`[resourcemanager.projects.create](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/create)` | `resourcemanager.projects.create`  
`[resourcemanager.projects.delete](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/delete)` | `resourcemanager.projects.delete`  
`[resourcemanager.projects.get](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/get)` | `resourcemanager.projects.get`  
Granting this permission will also grant access to get the name of the billing account associated with the project through the Billing API method [`billing.projects.getBillingInfo`](https://docs.cloud.google.com/billing/docs/reference/rest/v1/projects/getBillingInfo) .  
`[resourcemanager.projects.getIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/getIamPolicy)` | `resourcemanager.projects.getIamPolicy`  
`[resourcemanager.projects.list](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/list)` | `resourcemanager.projects.list`  
`[resourcemanager.projects.search](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/search)` | `resourcemanager.projects.get`  
`[resourcemanager.projects.setIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/setIamPolicy)` | `resourcemanager.projects.setIamPolicy`  
`[resourcemanager.projects.testIamPermissions](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/testIamPermissions)` | Does not require any permission.  
`[resourcemanager.projects.undelete](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/undelete)` | `resourcemanager.projects.undelete`  
`[resourcemanager.projects.patch](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/patch)` | To update a project's metadata, requires `resourcemanager.projects.update` permission. To update a project's parent and move the project into an organization resource, requires `resourcemanager.projects.create` permission on the organization resource.  
`[projects.move](https://docs.cloud.google.com/sdk/gcloud/reference/beta/projects/move)` | `projects.move`  
  
### Using predefined roles

IAM predefined roles let you manage the permissions available to users. For a full list of the roles that can be granted at the project level, see [Understanding Roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

The following table lists the predefined roles you can use to grant access to a project. Each role includes a description of its purpose and the permissions it contains.

Role | Permissions  
---|---  
  
#### Project Creator 

(`roles/resourcemanager.projectCreator`) Provides access to create new projects. Once a user creates a project, they're automatically granted the owner role for that project.  Lowest-level resources where you can grant this role:

  * Folder 

|  `resourcemanager.organizations.get` `resourcemanager.projects.create`  
  
#### Project Deleter 

(`roles/resourcemanager.projectDeleter`) Provides access to delete Google Cloud projects.  Lowest-level resources where you can grant this role:

  * Project 

|  `resourcemanager.projects.delete`  
  
#### Project Mover 

(`roles/resourcemanager.projectMover`) Provides access to update and move projects.  Lowest-level resources where you can grant this role:

  * Project 

|  `resourcemanager.projects.get` `resourcemanager.projects.move` `resourcemanager.projects.update`  
  
#### Project IAM Admin 

(`roles/resourcemanager.projectIamAdmin`) Provides permissions to administer allow policies on projects.  Lowest-level resources where you can grant this role:

  * Project 

|  `iam.policybindings.*`

  * `iam.policybindings.get`
  * `iam.policybindings.list`

`resourcemanager.projects.createPolicyBinding` `resourcemanager.projects.deletePolicyBinding` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.searchPolicyBindings` `resourcemanager.projects.setIamPolicy` `resourcemanager.projects.updatePolicyBinding`  
  
#### Browser 

(`roles/browser`) Read access to browse the hierarchy for a project, including the folder, organization, and allow policy. This role doesn't include permission to view resources in the project.  Lowest-level resources where you can grant this role:

  * Project 

|  `resourcemanager.folders.get` `resourcemanager.folders.list` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.list`  
  
### Basic roles

Use basic roles only when necessary. These roles are highly privileged and grant extensive permissions across all Google Cloud services. For more information about when to use basic roles, see [Basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic).

Role | Description | Permissions  
---|---|---  
`roles/owner` | Full access to all resources. | All permissions for all resources.  
`roles/editor` | Edit access to most resources. | Create and update access for most resources.  
`roles/viewer` | Read access to most resources. | Get and list access for most resources.  
  
### Creating custom roles

In addition to the predefined roles described in this topic, you can also create [custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that are collections of permissions that you tailor to your needs. When creating a custom role for use with Resource Manager, be aware of the following points: 

  * List and get permissions, such as `resourcemanager.projects.get/list`, should always be granted as a pair.
  * When your custom role includes the `folders.list` and `folders.get` permissions, it should also include `projects.list` and `projects.get`. 
  * Be aware that the `setIamPolicy` permission for organization, folder, and project resources allows the user to grant all other permissions, and so should be assigned with care. 



## Access control at the project level

You can grant roles to users at the project level using the [Google Cloud console](https://console.cloud.google.com/), the Cloud Resource Manager API, and the Google Cloud CLI. For instructions, see [Granting, Changing, and Revoking Access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### Default roles

When you create a project, you receive the `roles/owner` role, which gives you full control over the project. You can change this default role in an allow policy.

## VPC Service Controls

**VPC Service Controls** can provide additional security when using the Cloud Resource Manager API. To learn more about VPC Service Controls, see the [VPC Service Controls overview](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

To learn about the current limitations in using Resource Manager with VPC Service Controls, see the [supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
