---
url: https://docs.cloud.google.com/resource-manager/docs/access-control-folders/
title: Access control for folders with IAM \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:55:58.445820+00:00
---

# Access control for folders with IAM  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/access-control-folders/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Access control for folders with IAM Stay organized with collections  Save and categorize content based on your preferences. 

You can use folder-level [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) roles to manage access across groups of projects and resources. Folder-level roles help you to enforce the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege) across your resource hierarchy when you bind roles to principals in allow policies.

Use the Cloud Resource Manager API to create and manage allow policies, or apply [deny policies](https://docs.cloud.google.com/iam/docs/deny-overview) to explicitly block specific permissions. To set up a new environment and grant initial access, follow the [Google Cloud setup checklist](https://docs.cloud.google.com/docs/enterprise/setup-checklist). To manage ongoing access, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Overview of IAM roles for Folders

To help you configure your IAM roles, the following table lists:

  * The type of actions you want to enable.
  * The roles required to perform those actions.
  * The resource level on which you need to apply those roles.

**Note:** Allow policies are additive and inherited down the hierarchy. This means that moving a resource into a folder could grant a user additional roles on that resource. Conversely, moving a resource out of a folder might mean losing roles on that resource.Type of actions | Roles required | Resource level  
---|---|---  
Administer folders across the organization resource | Folder Admin | Organization resource  
Administer a folder and all projects and folders it contains | Folder Admin | Specific folder  
Access and administer a folder's allow policies | Folder IAM Admin | Specific folder  
Create new folders | Folder Creator | Parent resource for the location of the new folders  
Move folders and projects | Folder Mover | Parent resource for both the original folder location and the new folder location  
Move a project to a new folder | Project Editor **or** Project Owner | Parent resource for both the original project location and new project location  
Delete a folder | Folder Editor or Folder Admin | Specific folder  
  
## Best practices for using IAM roles and permissions with Folders

When assigning IAM roles and permissions for use with Folders, keep the following in mind:

  * Use groups whenever possible to manage principals.
  * Minimize usage of basic roles, such as owner, editor, and viewer. Instead, try to use the predefined roles for principle of least privilege.
  * For folder-wide management, assign permissions at folder level and have projects inherit them automatically. For example, you could assign a department administrator group the **Folder Admin** role on the folder. Network administrators that need to have department-wide permissions can have the **Network Admin** role for the folder.
  * Carefully consider what permissions might change before moving a resource out of a folder. Otherwise, you could risk breaking existing apps or workflows that require those permissions on that resource.
  * Plan and test your resource hierarchy carefully before moving production projects under folders. One way to do this is to create a test folder under your organization resource and creating a prototype of your intended hierarchy ahead of time.
  * Granting a role to a user at the folder level will grant the user that role for every resource underneath that folder as well. For example, if you grant a user the Compute Admin role (`roles/compute.admin`) on a folder, that user will have full control of all Compute Engine resources in every project in that folder.



## Understand folder roles and permissions

Folders act as administrative boundaries within your organization, letting you group projects and apply policies at scale. Access to these folders is managed through a combination of inherited permissions from the organization and roles granted directly at the folder level.

### Default roles

Creating a folder grants you the **Folder Admin** and **Folder Editor** roles, which provide full control. See the following table for the permissions these roles provide. You can change these default roles in an allow policy.

### Use predefined roles

Role | Permissions  
---|---  
  
#### Folder Admin 

(`roles/resourcemanager.folderAdmin`) Provides all available permissions for working with folders.  Lowest-level resources where you can grant this role:

  * Folder 

|  `essentialcontacts.*`

  * `essentialcontacts.contacts.create`
  * `essentialcontacts.contacts.delete`
  * `essentialcontacts.contacts.get`
  * `essentialcontacts.contacts.list`
  * `essentialcontacts.contacts.send`
  * `essentialcontacts.contacts.update`

`iam.policybindings.*`

  * `iam.policybindings.get`
  * `iam.policybindings.list`

`orgpolicy.constraints.list` `orgpolicy.policies.list` `orgpolicy.policy.get` `resourcemanager.capabilities.*`

  * `resourcemanager.capabilities.get`
  * `resourcemanager.capabilities.update`

`resourcemanager.folders.*`

  * `resourcemanager.folders.create`
  * `resourcemanager.folders.createPolicyBinding`
  * `resourcemanager.folders.delete`
  * `resourcemanager.folders.deletePolicyBinding`
  * `resourcemanager.folders.get`
  * `resourcemanager.folders.getIamPolicy`
  * `resourcemanager.folders.list`
  * `resourcemanager.folders.move`
  * `resourcemanager.folders.searchPolicyBindings`
  * `resourcemanager.folders.setIamPolicy`
  * `resourcemanager.folders.undelete`
  * `resourcemanager.folders.update`
  * `resourcemanager.folders.updatePolicyBinding`

`resourcemanager.hierarchyNodes.*`

  * `resourcemanager.hierarchyNodes.createTagBinding`
  * `resourcemanager.hierarchyNodes.deleteTagBinding`
  * `resourcemanager.hierarchyNodes.listEffectiveTags`
  * `resourcemanager.hierarchyNodes.listTagBindings`

`resourcemanager.projects.createPolicyBinding` `resourcemanager.projects.deletePolicyBinding` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.list` `resourcemanager.projects.move` `resourcemanager.projects.searchPolicyBindings` `resourcemanager.projects.setIamPolicy` `resourcemanager.projects.updatePolicyBinding`  
  
#### Folder IAM Admin 

(`roles/resourcemanager.folderIamAdmin`) Provides permissions to administer allow policies on folders.  Lowest-level resources where you can grant this role:

  * Folder 

|  `iam.policybindings.*`

  * `iam.policybindings.get`
  * `iam.policybindings.list`

`resourcemanager.folders.createPolicyBinding` `resourcemanager.folders.deletePolicyBinding` `resourcemanager.folders.get` `resourcemanager.folders.getIamPolicy` `resourcemanager.folders.searchPolicyBindings` `resourcemanager.folders.setIamPolicy` `resourcemanager.folders.updatePolicyBinding`  
  
#### Folder Creator 

(`roles/resourcemanager.folderCreator`) Provides permissions needed to browse the hierarchy and create folders.  Lowest-level resources where you can grant this role:

  * Folder 

|  `essentialcontacts.contacts.get` `essentialcontacts.contacts.list` `orgpolicy.constraints.list` `orgpolicy.policies.list` `orgpolicy.policy.get` `resourcemanager.capabilities.get` `resourcemanager.folders.create` `resourcemanager.folders.get` `resourcemanager.folders.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Folder Editor 

(`roles/resourcemanager.folderEditor`) Provides permission to modify folders as well as to view a folder's allow policy.  Lowest-level resources where you can grant this role:

  * Folder 

|  `essentialcontacts.contacts.get` `essentialcontacts.contacts.list` `orgpolicy.constraints.list` `orgpolicy.policies.list` `orgpolicy.policy.get` `resourcemanager.capabilities.*`

  * `resourcemanager.capabilities.get`
  * `resourcemanager.capabilities.update`

`resourcemanager.folders.delete` `resourcemanager.folders.get` `resourcemanager.folders.getIamPolicy` `resourcemanager.folders.list` `resourcemanager.folders.searchPolicyBindings` `resourcemanager.folders.undelete` `resourcemanager.folders.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Folder Mover 

(`roles/resourcemanager.folderMover`) Provides permission to move projects and folders into and out of a parent organization or folder.  Lowest-level resources where you can grant this role:

  * Folder 

|  `resourcemanager.folders.move` `resourcemanager.projects.move`  
  
#### Folder Viewer 

(`roles/resourcemanager.folderViewer`) Provides permission to get a folder and list the folders and projects below a resource.  Lowest-level resources where you can grant this role:

  * Folder 

|  `essentialcontacts.contacts.get` `essentialcontacts.contacts.list` `orgpolicy.constraints.list` `orgpolicy.policies.list` `orgpolicy.policy.get` `resourcemanager.capabilities.get` `resourcemanager.folders.get` `resourcemanager.folders.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Creating custom roles

In addition to the predefined roles described in this topic, you can also create [custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that are collections of permissions that you tailor to your needs. When creating a custom role for use with Resource Manager, be aware of the following points: 

  * List and get permissions, such as `resourcemanager.projects.get/list`, should always be granted as a pair.
  * When your custom role includes the `folders.list` and `folders.get` permissions, it should also include `projects.list` and `projects.get`. 
  * Be aware that the `setIamPolicy` permission for organization, folder, and project resources allows the user to grant all other permissions, and so should be assigned with care. 



## Grant roles to enable folder browsing

List permissions enable folder browsing. The two types of list permissions that typically need to be granted are `resourcemanager.folders.list`, which allows users to list folders under a resource, and `resourcemanager.projects.list`, which allows users to browse projects under an organization resource or folder. The Organization Administrator is initialized with both of these permissions. For users that have not been assigned the **Organization Administrator** role:

  * `resourcemanager.folders.list` can be granted using the **Folder Viewer** and **Folder Editor** roles.
  * `resourcemanager.projects.list` can be granted using the **Viewer** or **Browser** roles.



For organization resource principals to browse the entire organization resource hierarchy, list permissions should be granted at the organization resource level.

## Grant roles to enable folder creation

Users that need to create folders must be granted **Folder Creator** role on a resource in the hierarchy above the level at which the folder will be created. It can be helpful to grant browsing permissions along with folder creation permissions so users can effectively navigate to where in the hierarchy the folder will be created. See the section above for more information on browsing permissions.

**Folder Creator** does not grant a user permission to delete a folder. However, when a person creates a folder, that person is automatically granted the **Folder Editor** role. The **Folder Editor** role enables folder deletion.

## Grant roles to enable folder movement

To move a folder from one parent resource to another, users must have the **Folder Mover** role on both old and new parent resources, or on a common ancestor.

## Grant roles to enable project movement

To move a project into a folder, users must have the **Project Editor** or **Project Owner** roles on the project and the **Project Mover** on both the source and destination parent resources.

This is slightly different from the requirements for moving a non-org-owned project into the organization resource, where users must have the **Project Editor** or **Project Owner** role on the project and the **Project Creator** role on the organization resource.

## Grant folder-specific roles to enable project creation

To create projects, users must have the **Project Creator** role. However, rather than granting org-wide project creation permission, it can be useful to instead restrict users to viewing and creating projects only within a given folder.

To grant folder-specific permissions:

  1. Grant the user the **Organization Viewer** role at the organization resource level (for example, domain.com). In the Google Cloud console, select your organization resource from the project and organization picker at the top of the page, or click your domain in the **Inheritance** column on the **IAM** page.
  2. Create a new folder.
  3. Add the user to IAM at the folder level and grant them the **Folder Viewer** and **Project Creator** roles.



This lets the user create projects in their folder without granting them visibility to every project in the greater organization resource.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
