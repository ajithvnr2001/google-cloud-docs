---
url: https://docs.cloud.google.com/iam/docs/pam-permissions-and-setup/
title: Privileged Access Manager permissions and setup \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:20.564755+00:00
---

# Privileged Access Manager permissions and setup  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/pam-permissions-and-setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Privileged Access Manager permissions and setup Stay organized with collections  Save and categorize content based on your preferences. 

Before you can start creating, modifying, or managing Privileged Access Manager entitlements and grants, your principals must have the appropriate permissions. The service must also be set up at the organization, folder, or project level.

Principals [requesting grants](https://docs.cloud.google.com/iam/docs/pam-request-temporary-elevated-access) and [approving or denying the grants](https://docs.cloud.google.com/iam/docs/pam-approve-deny-grants) don't require any Privileged Access Manager-specific permissions.

## Before you begin

Ensure that you have the required Identity and Access Management (IAM) permissions to set up and manage Privileged Access Manager permissions.

To get the permissions that you need to work with entitlements and grants, ask your administrator to grant you the following IAM roles on the organization, folder, or project: 

  * To create, update, and delete entitlements for an organization: [Privileged Access Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.admin) (`roles/privilegedaccessmanager.admin`) and [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`) 
  * To create, update, and delete entitlements for a folder: [](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.folderAdmin)[Privileged Access Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.admin) and [Folder IAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.folderAdmin) (`roles/resourcemanager.folderAdmin`) 
  * To create, update, and delete entitlements for a project: [](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin)[Privileged Access Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.admin) and [Project IAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) 
  * To view entitlements and grants: [](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.viewer)[Privileged Access Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.viewer) (`roles/privilegedaccessmanager.viewer`) 
  * To view audit logs: [Logs Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logs.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to work with entitlements and grants. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to work with entitlements and grants:

  * To enable Privileged Access Manager at an organization level: 
    * `privilegedaccessmanager.locations.checkOnboardingStatus`
    * `resourcemanager.organizations.get`
    * `resourcemanager.organizations.getIamPolicy`
    * `resourcemanager.organizations.setIamPolicy`
    * `serviceusage.services.enable`
  * To manage entitlements and grants for an organization: 
    * `resourcemanager.organizations.get`
    * `resourcemanager.organizations.setIamPolicy`
    * `privilegedaccessmanager.entitlements.create`
    * `privilegedaccessmanager.entitlements.delete`
    * `privilegedaccessmanager.entitlements.get`
    * `privilegedaccessmanager.entitlements.list`
    * `privilegedaccessmanager.entitlements.setIamPolicy`
    * `privilegedaccessmanager.grants.get`
    * `privilegedaccessmanager.grants.list`
    * `privilegedaccessmanager.grants.revoke`
    * `privilegedaccessmanager.operations.delete`
    * `privilegedaccessmanager.operations.get`
    * `privilegedaccessmanager.operations.list`
  * To view entitlements and grants for an organization: 
    * `resourcemanager.organizations.get`
    * `privilegedaccessmanager.entitlements.get`
    * `privilegedaccessmanager.entitlements.list`
    * `privilegedaccessmanager.grants.get`
    * `privilegedaccessmanager.grants.list`
    * `privilegedaccessmanager.operations.get`
    * `privilegedaccessmanager.operations.list`
  * To enable Privileged Access Manager at a folder level: 
    * `privilegedaccessmanager.locations.checkOnboardingStatus`
    * `resourcemanager.folders.get`
    * `resourcemanager.folders.getIamPolicy`
    * `resourcemanager.folders.setIamPolicy`
    * `serviceusage.services.enable`
  * To manage entitlements and grants for a folder: 
    * `resourcemanager.folders.get`
    * `resourcemanager.folders.setIamPolicy`
    * `privilegedaccessmanager.entitlements.create`
    * `privilegedaccessmanager.entitlements.delete`
    * `privilegedaccessmanager.entitlements.get`
    * `privilegedaccessmanager.entitlements.list`
    * `privilegedaccessmanager.entitlements.setIamPolicy`
    * `privilegedaccessmanager.grants.get`
    * `privilegedaccessmanager.grants.list`
    * `privilegedaccessmanager.grants.revoke`
    * `privilegedaccessmanager.operations.delete`
    * `privilegedaccessmanager.operations.get`
    * `privilegedaccessmanager.operations.list`
  * To view entitlements and grants for a folder: 
    * `resourcemanager.folders.get`
    * `privilegedaccessmanager.entitlements.get`
    * `privilegedaccessmanager.entitlements.list`
    * `privilegedaccessmanager.grants.get`
    * `privilegedaccessmanager.grants.list`
    * `privilegedaccessmanager.operations.get`
    * `privilegedaccessmanager.operations.list`
  * To enable Privileged Access Manager at a project level: 
    * `privilegedaccessmanager.locations.checkOnboardingStatus`
    * `resourcemanager.projects.get`
    * `resourcemanager.projects.getIamPolicy`
    * `resourcemanager.projects.setIamPolicy`
    * `serviceusage.services.enable`
  * To manage entitlements and grants for a project: 
    * `resourcemanager.projects.get`
    * `resourcemanager.projects.getIamPolicy`
    * `privilegedaccessmanager.entitlements.create`
    * `privilegedaccessmanager.entitlements.delete`
    * `privilegedaccessmanager.entitlements.get`
    * `privilegedaccessmanager.entitlements.list`
    * `privilegedaccessmanager.entitlements.setIamPolicy`
    * `privilegedaccessmanager.grants.get`
    * `privilegedaccessmanager.grants.list`
    * `privilegedaccessmanager.grants.revoke`
    * `privilegedaccessmanager.operations.delete`
    * `privilegedaccessmanager.operations.get`
    * `privilegedaccessmanager.operations.list`
  * To view entitlements and grants for a project: 
    * `resourcemanager.projects.get`
    * `privilegedaccessmanager.entitlements.get`
    * `privilegedaccessmanager.entitlements.list`
    * `privilegedaccessmanager.grants.get`
    * `privilegedaccessmanager.grants.list`
    * `privilegedaccessmanager.operations.get`
    * `privilegedaccessmanager.operations.list`
  * To view audit logs: `logging.logEntries.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Enable Privileged Access Manager

To enable Privileged Access Manager, you need to grant the [Privileged Access Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.serviceAgent) role to the Privileged Access Manager Service Agent for your organization, folder, or project.

To grant this role to the service agent, do the following:

  1. Go to the **Privileged Access Manager** page.

[Go to Privileged Access Manager](https://console.cloud.google.com/iam-admin/pam/entitlements/)

  2. Select the organization, folder, or project that you want to enable Privileged Access Manager for.

  3. Click **Set up PAM** to start the setup process.

  4. To grant access to the **Privileged Access Manager Service Agent** role to the [Privileged Access Manager service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) to manage privilege escalations, click **Grant role**.

**Important:** Privileged Access Manager uses only the organization-level service agent (`service-org-ORGANIZATION_NUMBER@gcp-sa-pam.iam.gserviceaccount.com`). Whether you set up Privileged Access Manager for an organization, folder, or project, you must grant the role to this organization-level service agent. Privileged Access Manager doesn't create or use folder-level or project-level service agents. If they don't appear in your resources, this is expected, and you don't need to create them.

When you grant the role to the organization-level service agent on an organization or folder, the role is inherited by all folders and projects within that resource in the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).

  5. Make sure the Privileged Access Manager service agent is added to the following security controls:

     * [Deny policies](https://docs.cloud.google.com/iam/docs/deny-overview): Add the Privileged Access Manager service agent to the [`exceptionPrincipals`](https://docs.cloud.google.com/iam/docs/deny-overview#deny-rules) field of your policies.

     * [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview): Add the Privileged Access Manager service agent to the appropriate [access levels](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level#members-example), or add an [ingress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) to the perimeter to allow the service agent.

  6. Click **Complete setup**.




### Allow the Privileged Access Manager email address

For email accounts and groups who receive Privileged Access Manager email notifications, add `pam-noreply@google.com` to your allow lists so the email isn't blocked.

## What's next

  * [Create entitlements](https://docs.cloud.google.com/iam/docs/pam-create-entitlements)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
