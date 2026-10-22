---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/control-access-to-platform/
title: SOAR access overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:56.870291+00:00
---

# SOAR access overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/control-access-to-platform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SOAR access overview

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains how these mechanisms—SOC roles, environments, and either permission groups or IAM roles—work together to control user access to different parts of the platform. It also describes how these mechanisms determine who can view cases. 

## Assign SOC roles

You can assign different access rights to SOC roles to control the scope of responsibility for each user group in Google Security Operations. Google SecOps includes predefined SOC roles, but you can also add custom roles.

The predefined SOC roles are defined as follows:

  * **Tier 1** : Perform basic triage on the alerts.
  * **Tier 2** : Review high-priority security threats.
  * **Tier 3** : Handle major incidents.
  * **SOC Manager** : Manage the SOC team.
  * **CISO** : Serve as the top-level manager within your organization.
  * **Administrator** : Access the entire Google SecOps platform.



You can set one of these SOC roles as the default, and the system automatically assigns it to incoming cases. Each SOC role can also have additional SOC roles attached to it, letting users monitor all cases assigned to those roles. For example, a Tier 1 analyst can see cases assigned to their Tier 1 role and any additional roles.

After a case is created, you can reassign it from the default SOC role to a specific SOC role or an individual user—manually or with a playbook automated action. Assigning a case to a SOC role makes sure that a group of people is aware of it. When an analyst self-assigns the case, they indicate that they're handling it.

For more information about SOC roles, see [Manage SOC roles](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-roles). 

## Environments and environment groups

You can define different environments and environment groups to create logical data segregation. This separation applies to most platform modules, such as cases, playbooks, ingestion, and dashboards. This process is useful for businesses and Managed Security Service Providers (MSSPs) who need to segment their operations and networks. Each environment or group can have its own unique automation processes and settings. For MSSPs with many different customers, each environment or group can represent a separate customer.

You can configure platform settings so that only analysts associated with a specific environment or group can see its cases. For example, you can configure the playbooks module for multiple environments. The system uses the default environment as the platform baseline when you've not defined or selected other environments. Platform administrators have access to all current and future environments and environment groups.

For more information about environment groups, see [Work with environments.](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/environments/work-with-environments) **Note:** Installed integrations share code across all platform environments. Granting access to the integrated development environment (IDE) module lets you create and execute custom code across all platform environments, regardless of your specific environment access. 

##  Permission groups or IAM roles 

Google SecOps lets you create groups of users and assign different permission levels to various modules. Prior to [migrating SOAR to Google Cloud](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp), these are controlled by permission groups in the SOAR Settings. After you complete the SOAR migration to Google Cloud, these are controlled by IAM roles.

  


### Permission groups (pre-migration)

The Google SecOps platform includes predefined permission groups, and you can add permission groups, as needed. The predefined groups are as follows:

  * Admin
  * Basic
  * Readers
  * View Only
  * Collaborators
  * Managed
  * Managed-Plus



Permission groups control the level of access each group has to different modules and settings in the platform. You can set permissions at a granular level.

For example: 

  * **Top level** : Enable access to the Reports module for a specific permission group.
  * **Mid level** : Enable access only to view advanced reports.
  * **Granular level** : Let users edit advanced reports.

For more information about permission groups, see [Manage permission groups](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-permission-groups)

### Identity and Access Management roles (post-migration)

After you complete SOAR migration to Google Cloud, the permission groups are migrated into IAM roles. For more information on migrating permission groups to IAM roles, see [Migrate SOAR permissions to Google Cloud IAM.](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-soar-permissions-iam) The Google SecOps platform supports predefined IAM roles as well as custom roles, which you can add as needed. The predefined IAM SOAR roles are as follows: Predefined role in IAM | Title | Description  
---|---|---  
`roles/chronicle.admin` | Chronicle API Admin | Full access to Google SecOps application and API services, including global settings.  
`roles/chronicle.editor` | Chronicle API Editor | Modify access to Google SecOps application and API resources.  
`roles/chronicle.viewer` | Chronicle API Viewer | Read-only access to Google SecOps application and API resources.  
`roles/chronicle.limitedViewer` | Chronicle API Limited Viewer | Grants read-only access to Google SecOps application and API resources, excluding detection engine rules and retrohunts.  
`roles/chronicle.soarAdmin` | Chronicle SOAR Admin | Full administrative access to SOAR settings and management.  
  
##  Restrict actions 

**Note:** This section only applies to customers who haven't migrated to Google Cloud. After completing Stage 1 of the migration, the Restrict Actions option appears in the **Group Mapping** page.

Each permission group includes a section where the administrator can select actions that are restricted for that specific permission group. For a restricted action to apply, it must be selected in all permission groups assigned to the user group. That is, if a user group is mapped to multiple permission groups, but the restricted action is only assigned in one of those groups, the restriction isn't enforced.

## Map users

There are different ways to map users depending on whether or not you have migrated to Google Cloud: 

  * Before SOAR migration - SOC roles, permission groups and environments map to different IdP groups, or user email groups, depending on how you have authenticated to the product. You can also specify Workforce Identity Federation subject attributes in place of user emails.

  * After SOAR migration - SOC roles and environments map to different IAM roles.




For more information about how to map users in the platform, see the document that applies to you:

  * If you have set up authentication using Workforce Identity Federation, and are before migration, map IdP Groups to Permission Groups, SOC Roles and Environments. See [Map users in the Google SecOps platform](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform).

  * If you have set up authentication using Cloud Identity, and are before migration, map user email groups to Permission Groups, SOC Roles and Environments. See [ Map users in the platform using Cloud Identity](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform-first-party).

  * If you have set up authentication using Cloud Identity, and are after migration, map IAM roles to SOC Roles and Environments. See [ Map users in the platform using Cloud Identity](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform-first-party).

  * Google SecOps SOAR standalone customers, see [Manage users](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-soar-only/how-do-i-add-a-new-user-to-the-platform).




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
