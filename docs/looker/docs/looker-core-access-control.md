---
url: https://docs.cloud.google.com/looker/docs/looker-core-access-control/
title: Looker (Google Cloud core) access control with IAM \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:18:58.433222+00:00
---

# Looker (Google Cloud core) access control with IAM  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Looker (Google Cloud core) access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

Looker (Google Cloud core) uses Identity and Access Management (IAM) to provision user and admin access through a set of IAM roles. For a detailed description of Google Cloud IAM, see the [IAM documentation](https://docs.cloud.google.com/iam/docs).

## What is Identity and Access Management (IAM)

IAM lets you control who has access to the resources in your Google Cloud project. IAM lets you adopt the [security principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege), so you grant only the necessary access to your resources.

Principals are the "who" of IAM. Principals can be individual users, groups, or Workspace domains. Principals are granted roles that give them the ability to perform actions with Looker (Google Cloud core) as well as Google Cloud more generally. Each role is a collection of one or more permissions. Permissions are the basic units of IAM: each permission allows a principal to perform a certain action.

For example, the `looker.instances.login` permission lets a principal log in to Looker (Google Cloud core) instances. This permission is included in several [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#role-types), including the Looker Admin role (`roles/looker.admin`) and the Looker Instance User role (`roles/looker.instanceUser`).

## Required role

To get the permissions that you need to assign Looker (Google Cloud core) IAM roles, ask your administrator to grant you the [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) IAM role on the project in which the instance was created. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** [IAM basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) might also contain permissions to assign Looker (Google Cloud core) IAM roles. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 

## IAM roles versus Looker roles

Two different kinds of roles grant permissions for Looker (Google Cloud core): IAM roles and Looker roles.

  * **Looker IAM roles:** These kinds of roles govern the following abilities:

    * Users' capabilities within the Google Cloud console with regard to Looker (Google Cloud core)

When used together with [Workforce Identity Federation](https://docs.cloud.google.com/looker/docs/looker-core-workforce-identity) or [OAuth](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication), they also govern the following abilities:

    * Users' abilities to sign in to a Looker (Google Cloud core) instance
    * Whether or not users are automatically assigned the **Admin via IAM** Looker role once they sign in to a Looker (Google Cloud core) instance. For more information, see the [Authentication and authorization with OAuth and IAM](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication#auth) documentation.

See the [IAM documentation](https://docs.cloud.google.com/iam/docs/manage-access-other-resources#grant-single-role) for information on how to grant IAM roles.

  * **Looker roles:** These kinds of roles govern what users can do once they sign in to a Looker (Google Cloud core) instance. See the [Roles](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles) and [Groups](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups) documentation pages for information on how to grant Looker roles.




Looker roles are assigned or revoked within a Looker (Google Cloud core) instance, with the exception of the **Admin via IAM** Looker role, which can be assigned or revoked only through IAM. IAM roles can be assigned or revoked only in the Google Cloud console.

## Looker (Google Cloud core) IAM roles

**Note:** To learn more about roles, see the [Basic and predefined roles reference](https://docs.cloud.google.com/iam/docs/roles-permissions/looker).

Three predefined roles for Looker (Google Cloud core) users are available. These roles are granted at the Google Cloud project level and will control access uniformly for all Looker (Google Cloud core) instances within a Google Cloud project. If a user is authenticating with [Workforce Identity Federation](https://docs.cloud.google.com/looker/docs/looker-core-workforce-identity) or [OAuth](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication), the IAM role assigned to each principal also affects which [Looker roles are assigned](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication#auth) at sign into the instance.

You can grant these roles to Google Accounts, Google Groups, or [workforce identity pool principals and groups](https://docs.cloud.google.com/looker/docs/looker-core-workforce-identity#grant-permissions).

Role Name | Permissions  
---|---  
**Looker Viewer**`(roles/looker.viewer)` Read-only access to all Looker (Google Cloud core) resources in the Google Cloud console. |  looker.backups.get looker.backups.list looker.instances.get looker.instances.list looker.instances.login looker.locations.get looker.locations.list looker.operations.get looker.operations.list resourcemanager.projects.get resourcemanager.projects.list  
**Looker Instance User**`roles/looker.instanceUser` Access to sign in to a Looker (Google Cloud core) instance. |  looker.instances.get looker.instances.login resourcemanager.projects.get resourcemanager.projects.list  
**Looker Schema Viewer**`roles/looker.schemaViewer` Access to Looker (Google Cloud core) schema data in Knowledge Catalog. |  looker.schemas.view  
**Looker Admin**`roles/looker.admin` Full access to all Looker (Google Cloud core) resources. |  looker.backups.create looker.backups.delete looker.backups.get looker.backups.list looker.instances.create looker.instances.delete looker.instances.export looker.instances.get looker.instances.import looker.instances.list looker.instances.login looker.instances.update looker.locations.get looker.locations.list looker.operations.cancel looker.operations.delete looker.operations.get looker.operations.list looker.schemas.view resourcemanager.projects.get resourcemanager.projects.list  
  
At least one principal must have the Looker Admin (`roles/looker.admin`) IAM role.

If the predefined roles don't provide the set of permissions that you want, you can also create your own [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

**Warning:** The Looker Service Agent IAM role is intended only for the Looker [service account](https://docs.cloud.google.com/iam/docs/service-agents#looker-service-account) and is automatically assigned to the service account when the [Looker API is enabled](https://docs.cloud.google.com/looker/docs/looker-core-instance-create#before_you_begin). Don't grant [service agent](https://docs.cloud.google.com/iam/docs/service-agents) roles to any principals except service agents. Instead, choose a different [predefined role](https://docs.cloud.google.com/iam/docs/roles-permissions), or create a [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) with the permissions that you need.

## What's next

  * [Use Google OAuth for Looker (Google Cloud core) user authentication](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication)
  * [Manage users within Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-user-management)
  * [Configure a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-instance-setup)
  * [Looker (Google Cloud core) admin settings](https://docs.cloud.google.com/looker/docs/looker-core-admin-looker)
  * [Administer a Looker (Google Cloud core) instance from the Google Cloud console](https://docs.cloud.google.com/looker/docs/looker-core-admin-console)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
