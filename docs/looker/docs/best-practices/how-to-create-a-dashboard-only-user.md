---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-create-a-dashboard-only-user/
title: Creating a dashboard-only user \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:59:22.484142+00:00
---

# Creating a dashboard-only user  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-create-a-dashboard-only-user/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Creating a dashboard-only user Stay organized with collections  Save and categorize content based on your preferences. 

In Looker, admins can limit a user's access to only the ability to view dashboards. Looker admins can do this by using a combination of [model sets](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#model_sets), [permission sets](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permission_sets), and [content access](https://docs.cloud.google.com/looker/docs/admin-panel-users-content-access) to create a role that you can apply to a user or a group of users. 

To create a dashboard-only user, follow these steps: 

  * Create a new [model set](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#model-sets) on the **Roles** page (under **Admin** > **Roles**). Select only the models that contain the LookML that is used in the tiles of the dashboard or dashboards that you want the dashboard-only user to access. 
  * Create a new [permission set](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permission-sets) with limited permissions. For example, if you want the user to see only LookML dashboards, select the `see_lookml_dashboards` permission: 

![LookML dashboard-only user permission set with only the access_data and see_lookml_dashboards permissions selected.](https://docs.cloud.google.com/static/looker/docs/images/creating-dashboard-only-user-1-2210.png)

If you want the user to also be able to see user-created dashboards in folders, select both the `see_lookml_dashboards` and the `see_user_dashboards` permissions: 

![Dashboard-only user permission set with the access_data, see_lookmL_dashboards, see_looks, and see_user_dashboards permissions selected.](https://docs.cloud.google.com/static/looker/docs/images/creating-dashboard-only-user-2-2210.png)
  * To allow users to view dashboards, you also need to give the user access to the folder or folders in which the dashboard or dashboards are saved. Under **Admin** > **Content Access** , highlight the folder or folders that you want users to access, and select **Manage Access**. Add the group or user being created and give them _View_ access. 
  * Finally, in **Admin** > **Roles** , select the **New Role** button to create a new role. Assign the model set and permission set you just created to the new role. Select the individual user(s), or a group of users, to be given the new role, which will limit their access to dashboards only. 



_Users and groups can have more than one role. Make sure the users or groups whose access you wish to limit are not assigned to other roles with greater access._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
