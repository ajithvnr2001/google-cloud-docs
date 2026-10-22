---
url: https://docs.cloud.google.com/support/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 Cloud Customer Care \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:31.172196+00:00
---

# Access control with IAM  |  Cloud Customer Care  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/support/docs/access-control/

When creating a case, **Live chat** is your quickest connection to a support representative. For more information, see [Create a support case](https://docs.cloud.google.com/support/docs/customer-care-procedures#create_a_support_case). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Customer Care ](https://docs.cloud.google.com/support/docs)
  * [ Guides ](https://docs.cloud.google.com/support/docs/overview)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

Identity and Access Management (IAM) roles let you control access to Cloud Customer Care support services. By granting these roles, you specify which team members can create, view, or manage technical support cases across your organization.

### Before you begin

  * You must have the [Standard Support](https://docs.cloud.google.com/support/docs/standard), [Enhanced Support](https://docs.cloud.google.com/support/docs/enhanced), or [Premium Support](https://docs.cloud.google.com/support/docs/premium) service.
  * You must have the Organization Administrator role (`roles/resourcemanager.organizationAdmin`) for your Google Cloud organization.



## What is Identity and Access Management (IAM)

Google Cloud offers [IAM](https://cloud.google.com/iam), which lets you give more granular access to specific Google Cloud resources and prevents unwanted access to other resources. IAM lets you adopt the [security principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege), so you grant only the necessary access to your resources.

IAM lets you control **who** (identity) has **what access** (roles) to **which resource** by setting IAM policies. IAM policies grant specific role(s) to a principal, giving the principal certain permissions. For example, for a given resource, such as a project, you can assign the Tech Support Viewer role (`roles/cloudsupport.techSupportViewer`) to a Google Account and that account can view support cases in the project, but cannot manage support cases.

## Access considerations

If you have transitioned from Silver, Gold, or Platinum Support, keep in mind that support cases are no longer accessible through the Google Cloud Support Center (GCSC). After you enable Standard, Enhanced, or Premium Support, you can manage access to transitioned cases by granting IAM roles to users, groups, or domains.

## Organization-level Cases

Customer Care cases can be created within either organizations or projects.

In order to manage organization-level cases, the user **must** have the `resourcemanager.organizations.get` permission at the organization level, or else they won't be able to select the organization in the Google Cloud console.

The simplest way to grant this permission is to grant the user the `roles/resourcemanager.organizationViewer` role on the organization. This role only grants the `resourcemanager.organizations.get` permission.

NOTE: Granting a user the `Organization Viewer` role is not the same as granting a user the `Viewer` role at the Organization level. This is a common point of confusion. The `Organization Viewer` role does not give the user access to view any resources within the organization, it only allows the user to see that the organization exists.

In addition, the user must have the relevant Technical Support IAM permissions, which are described in the following sections.

## Customer Care IAM roles

With IAM, every support user must have the appropriate permissions to view and manage cases and users. Users gain these permissions when you add them to an IAM role, a group that belongs to a role, or a domain assigned to a role.

**Note:** You can grant multiple roles to a principal on the same resource. For example, you can grant both the Support Admin role (`roles/cloudsupport.admin`) and the Support Viewer role (`roles/cloudsupport.viewer`) to your cloud support admin team's [Google group](https://docs.cloud.google.com/iam/docs/overview#google_group).

The following table lists the IAM roles available to Cloud Customer Care users, the associated permissions to which resources, and the lowest resource level that you can apply the permissions to.

Role | Permissions  
---|---  
  
#### Support Administrator 

(`roles/cloudsupport.admin`) Allows management of a support account and support cases. See the [Cloud Support documentation](https://docs.cloud.google.com/support/docs/access-control#support_account_admin) for more information.  Lowest-level resources where you can grant this role:

  * Organization 

|  `cloudsupport.*`

  * `cloudsupport.accounts.create`
  * `cloudsupport.accounts.delete`
  * `cloudsupport.accounts.get`
  * `cloudsupport.accounts.getIamPolicy`
  * `cloudsupport.accounts.getUserRoles`
  * `cloudsupport.accounts.list`
  * `cloudsupport.accounts.purchase`
  * `cloudsupport.accounts.setIamPolicy`
  * `cloudsupport.accounts.update`
  * `cloudsupport.accounts.updateUserRoles`
  * `cloudsupport.operations.get`
  * `cloudsupport.properties.get`
  * `cloudsupport.techCases.create`
  * `cloudsupport.techCases.escalate`
  * `cloudsupport.techCases.get`
  * `cloudsupport.techCases.list`
  * `cloudsupport.techCases.update`

`resourcemanager.organizations.get`  
  
#### Support Viewer 

(`roles/cloudsupport.viewer`) Read-only access to details of a support account. This does not allow viewing cases. See the [Cloud Support documentation](https://docs.cloud.google.com/support/docs/access-control#support_account_viewer) for more information.  Lowest-level resources where you can grant this role:

  * Organization 

|  `cloudsupport.accounts.get` `cloudsupport.accounts.getIamPolicy` `cloudsupport.accounts.getUserRoles` `cloudsupport.accounts.list` `cloudsupport.operations.get` `cloudsupport.properties.get` `cloudsupport.techCases.get` `cloudsupport.techCases.list`  
  
#### Advisory Support Editor 

(`roles/cloudsupport.advisorySupportEditor`) Full read-write access to advisory support cases applicable for Cloud Customer Care.  |  `cloudasset.assets.searchAllResources` `cloudsupport.properties.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Advisory Support Viewer 

(`roles/cloudsupport.advisorySupportViewer`) Read-only access to advisory support cases applicable for Cloud Customer Care.  |  `cloudsupport.properties.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Support Subscription Editor 

(`roles/cloudsupport.supportSubscriptionEditor`) Full read-write access to support event subscriptions.  |  `resourcemanager.organizations.get`  
  
#### Support Subscription Viewer 

(`roles/cloudsupport.supportSubscriptionViewer`) Read-only access to support event subscriptions.  |  `resourcemanager.organizations.get`  
  
#### Tech Support Editor 

(`roles/cloudsupport.techSupportEditor`) Full read-write access to technical support cases (applicable for Cloud Customer Care and Maps support). See the [Cloud Support documentation](https://docs.cloud.google.com/support/docs/access-control#tech_support_editor) for more information.  |  `billing.resourceAssociations.list` `cloudasset.assets.searchAllResources` `cloudsupport.properties.get` `cloudsupport.techCases.*`

  * `cloudsupport.techCases.create`
  * `cloudsupport.techCases.escalate`
  * `cloudsupport.techCases.get`
  * `cloudsupport.techCases.list`
  * `cloudsupport.techCases.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Tech Support Viewer 

(`roles/cloudsupport.techSupportViewer`) Read-only access to technical support cases (applicable for Cloud Customer Care and Maps support). See the [Cloud Support documentation](https://docs.cloud.google.com/support/docs/access-control#tech_support_viewer) for more information.  |  `cloudsupport.properties.get` `cloudsupport.techCases.get` `cloudsupport.techCases.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
To add a user, group, or domain to a role, see Granting IAM roles.

### Support Account Administrator

Users with the Support Account Administrator role (`roles/cloudsupport.admin`) can manage the purchased support service and how it is billed.

The Support Account Administrator is responsible for administering policies for the organization's support account, including:

  * Assigning new support users
  * Modifying roles for existing support users
  * Managing support billing



This role can only be granted at the organization level.

**Note:** The Support Account Administrator doesn't automatically have access to view or edit support cases. They must be assigned a Tech Support Viewer or Editor role to view or manage cases, which they can assign to themselves. To assign the role of Support Account Administrator, see the section on Granting IAM roles.

### Support Account Viewer

The Support Account Viewer role (`roles/cloudsupport.viewer`) can view account information for the service. They cannot view or edit support cases; to do so they must be assigned a Tech Support Viewer or Tech Support Editor role.

This role can only be granted at the organization level.

### Tech Support Editor

The Tech Support Editor role (`roles/cloudsupport.techSupportEditor`) can manage support cases, including viewing, creating, updating, escalating, and closing cases.

You can grant this role at the organization, folder, and project levels. For example, if you grant the Tech Support Editor role to a Google group on a specific project, all members of the group can manage support cases for that project.

You can also grant this role at multiple levels of the resource hierarchy to establish different permissions for nested resources. For example, if you have the Tech Support Viewer role for the organization and Tech Support Editor role on a project, you can view support cases across the organization, but only edit cases for the project.

### Tech Support Viewer

The Tech Support Viewer role (`roles/cloudsupport.techSupportViewer`) can view support cases and account information.

This role can be set at the organization, project, and folder levels. For example, you can grant the Tech Support Viewer role to a Google group on a specific folder within a project, which enables members of that group to view the support cases in the folder.

### Support Subscription Editor

The Support Subscription Editor role (`roles/cloudsupport.supportSubscriptionEditor`) can manage support event subscriptions, including creating, updating, deleting, and undeleting subscriptions.

This role can only be granted at the organization level.

### Support Subscription Viewer

The Support Subscription Viewer role (`roles/cloudsupport.supportSubscriptionViewer`) can view support event subscriptions.

This role can only be granted at the organization level.

## Granting IAM roles

Users, Google Groups, or domains must have the `resourcemanager.organizations.setIamPolicy` permission on the organization to add users to the Customer Care IAM roles. You can give a user or group that permission by granting them the Organization Administrator role (`roles/resourcemanager.organizationAdmin`).

For example, if your organization would like users granted the Support Account Administrators role to _also_ be able to add and remove users and groups from the other Customer Care IAM roles, then an Organization Administrator can do the following:

  * Create a Google Group for the users (MyCompanySupportAdmins).
  * Assign the Google Group (MyCompanySupportAdmins) the Organization Administrator role.
  * Assign the Google Group (MyCompanySupportAdmins) the Support Account Administrator role.



In the example, members of the Google Group (MyCompanySupportAdmins) can assign users and groups to IAM roles in the organization because the group has been granted the `setIamPolicy` permission when granted the Organization Administrator role. As new Support Account Administrators join the organization, add them to the Google Group (MyCompanySupportAdmins) to grant them the desired roles.

To grant an IAM role to a user, group, or domain:

  1. In the Google Cloud console, go to the **IAM** page.   
[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. From the top menu, click **Add**.

  3. Specify a user, Google Group, or domain.

  4. Select a **Support** role. For best security practices, we strongly recommend giving the principal the least amount of privilege needed.

  5. Click **Save**.




## What's next

Understand how to [manage support cases](https://docs.cloud.google.com/support/docs/manage-cases) in the Google Cloud console.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
