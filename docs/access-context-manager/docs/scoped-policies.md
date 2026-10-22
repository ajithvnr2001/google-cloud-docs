---
url: https://docs.cloud.google.com/access-context-manager/docs/scoped-policies/
title: Scoped policies \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:13.469508+00:00
---

# Scoped policies  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/scoped-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Scoped policies Stay organized with collections  Save and categorize content based on your preferences. 

Scoped policies are access policies that are scoped to specific folders or projects alongside an access policy that you can apply to the entire organization. You can use scoped policies to delegate administration of VPC Service Controls perimeters and access levels to folder-level and project-level administrators.

Organizations can only have one access policy at the organizational level, and you can apply the organizational-level access policy to any folder or project in your organization.

There might be instances when you want to delegate the management of a policy for a subset of an organization's resources, such as a folder, to a delegated administrator. You can create access policies that are scoped to specific folders or projects alongside an access policy that can apply to the entire organization. To delegate administration of VPC Service Controls perimeters and access levels to folder-level and project-level administrators, you can use scoped policies.

When you delegate administration of a scoped policy, the delegated administrators can modify or read that specific policy and not the organization's Access Context Manager policy. The scoped policies limit the resources that can be restricted in a VPC Service Controls perimeter, and the visibility of any access levels.

## Scoped policies management

As an organization-level Access Context Manager administrator, you can create, modify, and delete scoped policies. You can specify Identity and Access Management (IAM) bindings on Access Context Manager policy directly, and allow further delegation of Access Context Manager policy administration to other users in the organization. A scoped policy administrator can configure service perimeters and access levels in policies. However, a scoped policy administrator cannot create a new policy or change the scope of the policy to apply to another folder or project.

**Warning:** If an organization-level access policy doesn't exist for your organization, scoped policies that you create at the folder or project-level will not operate.

Here is a sequence of how administrators manage the scoped policies:

  1. The organization-level administrator creates a new access policy with a scope field referencing a specific folder or project.

  2. The organization-level administrator assigns IAM permissions to the delegated administrator directly on the access policy resource. The delegated administrator now has permissions on the scoped policy but does not have permissions on any other policy unless the organization-level administrator explicitly assigns them to the delegated administrator.

  3. The delegated administrator can now edit the policy to configure access levels and service perimeters. The delegated administrator can also grant IAM permissions on that policy to any other user.




When you delete a folder or a project, the policy that has the deleted folder or project as its scope is also deleted. Also, if you move a project to another node in the organization hierarchy, the policy scoped to the project is not automatically modified. You must delete the policy associated with the project, and then recreate the policy and specify the scope.

## Scoped policies hierarchy

The organization resource is the root node of the Google Cloud resource hierarchy and all resources that belong to an organization exist as children of the organization node. Folders are a grouping mechanism on top of projects. Folders and projects exist as child nodes of the organization resource.

The following diagram shows an example organization that contains folders for each department, and the folders contain dev, test, and production projects.

![Deployment architecture](https://docs.cloud.google.com/static/access-context-manager/images/scoped_policies.svg)

In the example organization, the following constraints apply to a service perimeter or an access level in a scoped policy:

  * Service perimeters in a scoped policy can only restrict resources that exist in the scope of that policy. For example, a service perimeter in a policy scoped to the engineering folder can secure the example-dev, example-prod, and example-test projects because the projects are in the engineering folder.

If the scoped policy applies to the sales folder, then service perimeters in that policy cannot secure any of example-dev, example-prod, and example-test projects. However, the service perimeter in the scoped policy can allow access to projects in other folders by using ingress and egress rules.

  * Access levels in a scoped policy are only visible within the scope of the policy. If you create an access level in the policy scoped to the engineering folder, then only service perimeters and access levels in the engineering folder can use it. Service perimeters and access levels in other folders cannot use the access level defined in the engineering folder.




A location, such as a folder, in the example.com organization resource hierarchy can have multiple policies that contain an access level or service perimeter. When multiple policies exist, a request for resources in the example.com organization is evaluated based on the following rules:

  * A policy can contain only one scope, such as a folder, but you can create a policy for each level of an organization. For example, if the scope of policy 1 is the engineering folder, you cannot set the engineering folder as the scope of any other policy. You can set another policy with the scope set to the child of the engineering folder, such as example-prod.

  * If the scope of a policy applies to a project or a parent of the project, you can add the project to the policy. However, a project can be a member of only one service perimeter across all policies. For example, A policy with scope set to the organization example.com can define a service perimeter with example-dev. A policy with scope set to the engineering folder or scope set to the example-dev project can also add the example-dev project to a perimeter defined within either of them. However, only one of those three policies can contain this project.




## What's next

  * [Create an access policy](https://docs.cloud.google.com/access-context-manager/docs/create-access-policy)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
