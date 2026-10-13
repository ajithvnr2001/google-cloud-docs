---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-manage-users-with-groups/
title: Best practice: Manage users with groups \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:55:01.186859+00:00
---

# Best practice: Manage users with groups  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-manage-users-with-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Best practice: Manage users with groups Stay organized with collections  Save and categorize content based on your preferences. 

> _These best practices reflect recommendations shared by a cross-functional team of seasoned Lookers. These insights come from years of experience working with Looker customers from implementation to long-term success. The practices are written to work for most users and situations, but you should use your best judgment when implementing._

Managing users properly is crucial to ensuring that only the appropriate people have access to particular data, features, and content within Looker. Unless you have a completely [open system](https://docs.cloud.google.com/looker/docs/access-levels#configuring_a_completely_open_system), it will be important to implement a strategy for managing users that ensures that all data and content is secured. Using groups will help with this and can prevent the need to add, manage, and update user access at the individual user level. 

##  Map out permissions 

Begin by making a high-level plan and mapping out the permissions and access that will be required across your user base. 

    * Identify the different datasets available within Looker and the combinations of these that should be available to different user groups. If your organization has only one model, this is easy. If your organization has several models, there may be a few different combinations of models ([model sets](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#model_sets)) that need to be created. 
    * Identify the different user types that you have. Common users include people who can view dashboards but not explore data, people who can explore data but not write LookML, people who can write LookML, and administrators. The features that each of these user types will be able to use should be set up using [permission sets](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permission_sets). 
    * Think about how the data access (model sets) and feature access (permission sets) intersect. For example, there may be a large number of users whose data access is restricted to a single model and whose feature access is restricted to dashboards. This data and feature access would be combined to create a role. 



##  Map out groups 

Next, think about the functional groups within your user base, such as Sales, Finance, etc. These functional groups should be reflected in the [groups](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups) you can assign users to within Looker. Groups can be used to secure content (dashboards and Looks). 

    * For example, you might have a Sales department in your organization, and inside of that department there may be several account executives alongside a small Sales Operations team. You could create a Sales group in Looker, and then inside of the Sales group create one subgroup for Account Executives and another subgroup for Sales Ops. The Account Executives group might map to a role with viewer permissions, and the Sales Ops group might map to a role with explorer permissions. 
    * Access to folders — and therefore to content — can be [managed using these groups](https://docs.cloud.google.com/looker/docs/organizing-spaces#viewing_and_managing_folder_access_levels). For example, within the **Shared** folder you could create a **Sales** folder that only the Sales department can see. Members of the Account Executives group could be given View access to that folder, while the Sales Ops team might have the ability to manage access to that folder and edit content within it. 
    * Changes to access or permissions for the entire Sales department can be managed using the Sales group. 
    * Changes to access or permissions for either the Account Executives or the Sales Ops team can be managed at the subgroup level. 
    * New users can be added to the appropriate group and will automatically inherit the appropriate permissions. 



##  Apply controls at the group level 

As you begin to apply controls at the group level, keep the following tips in mind: 

  * When setting up users, do not give any roles directly to the user. Simply assign each user to a group. Users given individual roles and roles based on group membership will _inherit all roles from both the individual and group assignments_. 
  * Take care when placing users in multiple groups. Users in multiple groups get the sum of _all_ privileges of all the groups they're in, so ensure that users in multiple groups are still limited to the appropriate level of access. 
  * When possible, assign user attribute values at the group level. 



To see these practices applied, refer to the Best Practices page on setting up secure content access — [Best practice: Secure your spaces! A content access walk-through](https://docs.cloud.google.com/looker/docs/best-practices/how-to-secure-your-folders). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
