---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform-first-party/
title: Map users with Cloud Identity \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:25:44.318895+00:00
---

# Map users with Cloud Identity  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform-first-party/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Map users with Cloud Identity

Supported in:

Google SecOps 

**Note:** "If you've already completed Stage 2 of SOAR migration to Google Cloud, you need to use IAM to manage feature access to Google SecOps including SOAR. The **Permission Group** column is still displayed post migration in the **Group Mapping** page for backward compatibility. Do not delete these assignments. The column will be removed by November 30, 2026 without any customer impact. For more information, see [Migrate to Google Cloud](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp).

This document explains how to authenticate and map users with secure identification to Google Security Operations. 

## Control user access

There are multiple ways to manage user access to different aspects of the platform: 

  * **Permissions groups** : Set user access levels by assigning them to specific permission groups. These groups determine which modules and submodules users can view or edit. For example, a user might have access to **Cases** and **Workdesk** pages, but be restricted from **Playbooks** and **Settings**. For more information, see [Work with permission groups](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-permission-groups). 
**Important:** Any permission group assigned to users must have at least one default landing module enabled in its **Permissions** settings. Examples include **Homepage** , **Dashboards** , or **Cases**. If you disable all default landing modules this will cause backend errors and result in an infinite login redirect loop.
  * **SOC roles** : Define the role of a group of users. You can assign users to SOC roles to streamline task management. Instead of assigning cases, actions, or playbooks to individuals, they can be assigned to a SOC role. Users can see cases assigned to them, their role, or additional roles. For more information, see [ Work with roles](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-roles). 
  * **Environments or environment groups** : Configure environments or environment groups to segment data across different networks or business units, commonly used by businesses and Managed Security Service Providers (MSSPs). Users can only access data within the environments or groups assigned to them. For more information, see [ Work with environments](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/environments/work-with-environments).



## Map email user groups

In this section, you can map user emails or Workforce Identity Federation subject attributes into groups to control user access within Google SecOps.

The combination of permission groups, SOC roles, and environments determines the Google SecOps user journey for each group in the platform.

There are various options for mapping. You can map users with either single or multiple permission groups, SOC roles, and environments. This process makes sure that different users mapped to different groups inherit all the necessary permission levels.

By default, Google SecOps includes a group of default administrators.

**Note:** IAM roles (predefined or custom) cannot be added as Group Names in Group Mapping.

To map email groups, follow these steps:

  1. Go to **Settings > SOAR Settings > Advanced > Group Mapping.**
  2. Make sure you have the following available: 
     * **Group Names** : The name you assign to an email group, such as `T1 analysts`.
     * **Group Members** : The collection of user emails or Workforce Identity Federation subject attributes that make up that group.
  3. Click  **Add** **Add** and map the emails or Workforce Identity Federation subject attributes for each group. Press **Add** after you add each item.
  4. Once you've finished, click **Add**. Each time a user signs in to the platform, they're automatically added to the **User Management** page, found under **Settings > Organization**.



When users attempt to sign in to the Google SecOps platform, but their email group hasn't been mapped, to prevent these users from being rejected, we recommend enabling the **Default Access Settings** and setting administrator permissions on this page. After the initial administrator setup is complete, we suggest you adjust the administrator permissions to a more minimal level of permissions. 

For information about multiple permission in group mapping, see [Map users with multiple control access parameters](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-with-multiple-control-access-parameters).

## Map groups to access control parameters

This section describes how to map different email groups to one or more access control parameters within the **Group Mapping** page. This approach is beneficial for customers who want to onboard and provision user groups based on specific customizations, rather than adhering to the standardization of the Google SecOps platform. While mapping groups to parameters may require you to create more groups initially, once the mapping is set, new users can join Google SecOps without the need to create additional groups.

### Delete a user

If you delete groups from here, make sure to delete the individual users from the **User Management** screen. For more information, see [Disable or delete a user account](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-soar-only/how-can-i-disabledelete-a-user-account-in-chronicle-soar). 

### Use case: Assign unique permission fields to each email group

The following use case illustrates how to use this feature to help onboard and provision users according to your company's needs.

Your company has three different personas: 

  * Security analysts (containing group members Sasha and Tal)
  * SOC engineers (containing group members Quinn and Noam)
  * NOC engineers (containing group members Kim and Kai)



Security analysts and SOC engineers have the same Google SecOps permission groups (analyst) and SOC roles (Tier 1). While the security analysts have permissions for the London environment, the SOC engineers have permissions for the Manchester environment. Meanwhile, NOC engineers have permissions for the **London** environment, but are assigned the **Basic** Permission Group and **Tier 2** SOC role.

This scenario is illustrated in the following table:

Group | Permission Group | SOC Role | Environment | Group Members  
---|---|---|---|---  
Security analysts | Analyst | Tier 1 | London | sasha@company.com, tal@company.com  
SOC engineers | Analyst | Tier 1 | Manchester | quinn@company.com, noam@company.com  
NOC engineers | Basic | Tier 2 | London | kim@company.com, kai@company.com  
  
### Set up email groups

To set up email groups in Google SecOps, do the following:

  1. Create the following email groups: 
     * Security analysts (containing Sasha and Tal)
     * SOC engineers (containing Quinn and Noam) 
     * NOC engineers (containing Kim and Kai)
  2. Go to **Settings > SOAR Settings > Advanced > Group Mapping**.
  3. Click **Add Group**.
  4. Enter the following details in the dialog:
     * Group: `Security analysts`
     * Permission Group: `Analyst`
     * SOC Role: `Tier 1`
     * Environment: _leave blank_
     * Group Members: `sasha@company.com, tal@company.com `
  5. Enter the following details in the next dialog:
     * Group: `SOC engineers`
     * Permission Group: `Analyst`
     * SOC Role: `Tier 1`
     * Environment: _leave blank_
     * Group Members: ` quinn@company.com, noam@company.com`
  6. Enter the following details in the next dialog:
     * Group: `NOC engineers`
     * Permission Group: `Basic`
     * SOC Role: `Tier 2`
     * Environment: _Leave blank_
     * Group Members: `kim@company.com`, `kai@company.com`
  7. Enter the following details in the next dialog:
     * Group: `London`
     * Permission Group: _leave blank_
     * SOC Role: _leave blank_
     * Group Members: _leave blank_
     * Environment: ` London `
  8. Enter the following details in the next dialog:
     * Group: `Manchester`
     * Permission Group: _leave blank_
     * SOC Role: _leave blank_
     * Group Members: _leave blank_
     * Environment: ` Manchester`



For customers who use the Case Federation feature, see [ Set up federated case access for Google SecOps](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/environments/case-federation-secops).

## Map service accounts for API access

To grant a _service account access_ or _workload identity federation access_ to Google SecOps, you must map the identity to the platform's access control parameters. This mapping is a mandatory step to provide the identity with the necessary access to **SOC Roles** , and **Environments** required to perform automated tasks or API operations.

  1. Go to **SOAR Settings > Advanced > Group Mapping**.
  2. Click add **Add**.
  3. Complete the fields in the **Add Mapping** dialog to map the identity to the platform's access control parameters.

     1. In the **IdP / User group** field, enter one of the following: 
        * The full email address of your service account, if identity was set up using Cloud Identity.
        * The Workload Identity principal string, if identity was set up using Workforce Identity Federation.
     2. Configure the following access control fields:

Field | Description  
---|---  
**Permission groups** | Select the permission groups to define which modules and submodules the identity can access.  
**SOC roles** | Select the SOC roles to define the identity's role (such as Tier 1).  
**Environments** | Select the environments or environment groups the identity can access (such as **All Environments**).  
**Group members** | Enter the required user emails if applicable. Press **Enter** after adding each email.  
**Restricted actions** | Select the restricted actions to limit specific operations within modules.  
  4. Click **Add**.




## Troubleshooting

**Infinite login redirect loop**

In Google SecOps, logging in can result in an infinite loading or redirect loop even when IdP group mappings, JWT assertions, and IAM permissions are correctly configured. 

If a user encounters an infinite loading loop, check if their assigned permission group has all its default landing modules disabled. Examples include **Homepage** , **Dashboards** , or **Cases**. Go to **SOAR Settings > Permissions** and enable at least one default landing module to restore access.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
