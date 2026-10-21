---
url: https://docs.cloud.google.com/looker/docs/overview-of-permissions-for-looker-reports/
title: Overview of permissions for Looker reports \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:04:53.458107+00:00
---

# Overview of permissions for Looker reports  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/overview-of-permissions-for-looker-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Overview of permissions for Looker reports Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Important:**

As of December 4, 2025, new instances or instances that have not already enabled Looker reports won't be able to enable Looker reports.

As of June 15, 2026, the Looker reports preview is no longer supported. If you have enabled the preview for Looker reports, be aware of the following:

  * You will no longer have the option to create new reports.
  * You will lose the ability to view or edit reports that were created during the preview period.



Access to the rest of your Looker content in your instance will remain unaffected and you will continue to have access to Looker as a data source from Data Studio and Data Studio Pro.

You can create ad hoc Explores using Looker's [self-service Explores](https://docs.cloud.google.com/looker/docs/exploring-self-service) feature, which lets you upload CSV, XLS, and XLSX files to Looker and then query and visualize the data in a Looker Explore without needing to configure a LookML model or set up Git version control.

In addition to the [requirements that a Looker instance must fulfill](https://docs.cloud.google.com/looker/docs/enabling-looker-reports#requirements_and_limitations) to enable the Looker reports feature, certain tasks that are related to the setup and use of Looker reports require specific Looker permissions. Additional permissions are required to view and use data from [Looker data sources](https://docs.cloud.google.com/looker/docs/studio/connect-to-looker). Permissions are granted in the Looker instance by a Looker admin.

Read the following sections on this page to learn about Looker permissions for reports:

  * Things to know about permissions for Looker reports
  * Permissions for Looker reports



## Things to know about permissions for Looker reports

There are several things to know about how Looker permissions are applied to Looker report users:

  * Users _must_ have access to underlying [LookML models](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#model_sets) to view or use data from Looker data sources in Looker reports.

  * User access to folders is controlled by [access levels](https://docs.cloud.google.com/looker/docs/organizing-spaces#folder_access_levels) and user permissions. To change the access level settings for a folder, see [Viewing and managing folder access levels](https://docs.cloud.google.com/looker/docs/organizing-spaces#viewing_and_managing_folder_access_levels).

  * See [Controlling user content access](https://docs.cloud.google.com/looker/docs/access-control-and-permission-management#controlling_user_content_access) and [How content access and permissions interact](https://docs.cloud.google.com/looker/docs/access-control-and-permission-management#how_content_access_and_permissions_interact) to understand the additive nature of permissions and content access.




## Permissions for Looker reports

Looker admins can assign roles, permissions, and model sets to users and groups on the [**Roles** page in the **Admin** panel](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles).

In addition to [default permission sets in Looker](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_permission_sets), you can create [permission sets for Looker reports](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permission_sets) and [model sets](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#model_sets) to assign to Looker reports users and groups.

See the following table for an overview of Looker permissions that control how users can interact with Looker report features.

**Caution:** Assigning these permissions also impacts how users can interact with other Looker features and content. Click the permission name link for each entry in the **Looker permission** column to learn more about that permission in Looker.Looker permission | Depends on | Type | Looker report task  
---|---|---|---  
[`explore`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore) | `access_data`, `see_looks` | Model specific for Looker data sources | Users can view Looker Explore data, and [create reports from an Explore](https://docs.cloud.google.com/looker/docs/create-view-edit-reports#from_an_explore_page).  
[`see_user_dashboards`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_user_dashboards) | `access_data`, `see_looks` | Model specific for Looker data sources | Users can view reports in folders.  
[`save_dashboards`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#save_dashboards) | `access_data`, `see_looks`, `save_content` | Instance wide | Users can save and edit reports.  
[`download_with_limit`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#download_with_limit) | `access_data`, `see_looks` | Model specific for Looker data sources | Users can download reports, but _must_ specify a limit of 5,000 rows or fewer.  
[`download_without_limit`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#download_without_limit) | `access_data`, `see_looks` | Model specific for Looker data sources | Users can download reports without specifying a limit, up to a maximum of 5,000 rows.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
