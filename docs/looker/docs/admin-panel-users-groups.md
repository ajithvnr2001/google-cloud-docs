---
url: https://docs.cloud.google.com/looker/docs/admin-panel-users-groups/
title: Admin settings - Groups \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:26.600112+00:00
---

# Admin settings - Groups  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/admin-panel-users-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings - Groups Stay organized with collections  Save and categorize content based on your preferences. 

The **Groups** page in the **Users** section of the **Admin** menu lists all the user groups on your Looker instance. Placing users into groups is helpful for managing [folder access](https://docs.cloud.google.com/looker/docs/organizing-spaces) and [other permissions](https://docs.cloud.google.com/looker/docs/access-control-and-permission-management).

Consider creating groups that are related to the type of content that they handle. Users can [filter the **Top Content by group**](https://docs.cloud.google.com/looker/docs/finding-content#viewing_top_content), so thoughtful group design can help them find the content they need.

**Note:** If you have a permission that provides access to only select pages in the Admin panel, such as [`manage_schedules`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_schedules), [`manage_themes`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_themes), or [`see_admin`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_admin), but you don't have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles), the page or pages that are described here may not be visible to you in the Admin panel.

## Default groups

The following groups are created by default in the Looker instance:

  * All Users
  * Looker CI Users
  * Gemini Default Users



### All Users

The **All Users** group contains all users in the Looker instance. You can't delete the group, remove users from it, or assign roles to it within the Looker user interface.

You can, however, use this group to manage content access. Looker's default configuration allows completely open access to all folders. The **All Users** group is assigned to **Manage Access, Edit** on the Shared folder, and all subfolders within the Shared folder inherit that access from it. You can manage this setting from the **Content Access** section of the **Admin** panel.

### Looker CI Users

This user group is created automatically for Looker instances that have been [enabled for Continuous Integration](https://docs.cloud.google.com/looker/docs/admin-panel-platform-ci#enable_continuous_integration). The **Looker CI Users** group contains the Looker CI service accounts. You can view these accounts in the **Service Accounts** tab of the [**Users**](https://docs.cloud.google.com/looker/docs/admin-panel-users-users) Admin page. Looker uses these CI service accounts to perform [CI runs](https://docs.cloud.google.com/looker/docs/ci-run-suite) on the instance.

### Gemini Default Users

This user group has been created automatically for all Looker (original) instances that use an [open system configuration](https://docs.cloud.google.com/looker/docs/access-levels#open_and_closed_systems_of_access_to_folders). Users in this group are assigned the [**Gemini** role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#gemini), which grants them the ability to use [Gemini in Looker](https://docs.cloud.google.com/looker/docs/gemini-overview-looker) features.

You can edit the **Gemini Default Users** group to add or remove users, or to delete the group entirely. You can also add additional roles to the group. You cannot rename the **Gemini Default Users** group.

The status of the **Automated Gemini in Looker enablement and user management** setting affects the group as follows:

  * If you enable the setting: 
    * New users who are added to the instance are added to the group automatically.
  * If you disable the setting: 
    * New users who are added to the instance must be added to the group manually.
    * Existing users were already added to the group automatically. You must remove them manually.



The status of the setting as of June 9, 2025, has the following effects:

  * If the setting was enabled before June 9, 2025, all existing users have been added to the group and all new users will be added to the group.
  * If the setting was disabled as of June 9, 2025, all users must be added to the group manually.



The **Automated Gemini in Looker enablement and user management** setting is managed on the **Settings** page in the **Admin** panel.

## Viewing and searching groups

The **Groups** page shows the following information:

![](https://docs.cloud.google.com/static/looker/docs/images/admin-groups-2308.png)

  1. You can use the **Filter List** field to limit which groups are displayed. When you click the **Filter List** field, you are given the choice to filter on ID or group name. When you filter on ID, entering a group ID will display that group. In the case of group name, when you enter any string, the list of groups displayed will show all the groups whose name contains the string you entered in the filter field.
  2. You can sort the table by group name in either ascending or descending order by clicking the **Group** column heading.
  3. Each row lists the assigned group name and group ID. Click the row to edit the group to add or remove users. Groups that cannot be edited, either because they are system-created groups (such as **All Users**), or because they are externally managed by [LDAP](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-ldap#groups_and_roles), [SAML](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-saml#groups_and_roles), or [OpenID Connect](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-openid-connect#groups_and_roles) protocols, are indicated by a lock on the group icon.
  4. The **Role** column lists any roles assigned to the group.
  5. The **Users** column shows how many members, either users or other groups, belong to the group.
  6. Click **Add Group** to add a new group. Looker will display a dialog where you can type the name of the new group. After you click the **Create** button, Looker adds the group to the **Groups** page. You can then edit the group to add or remove users.
  7. Hold your cursor over a group to display the three-dot menu at the right. You can use the three-dot menu to delete the group. If you choose to delete a group, Looker will ask you to confirm.

**Warning:** Deleting a group is irreversible. Deleting a group while it is still in use can impact a wide variety of user permissions, which can prevent users from accessing the folders or features they are used to.



## Editing groups

To edit a group, click the row the group is in. There you can view and adjust several settings:

![](https://docs.cloud.google.com/static/looker/docs/images/admin-edit-group-2116.png)

  1. You can use the **Filter List** field to limit which groups members are displayed. When you click the **Filter List** field, you are given the choice to filter on member ID or member name. When you filter on member ID, entering a member ID will display that group member. In the case of member name, when you enter any string, the list of group members displayed will show all the group members whose name contains the string you entered in the filter field.
  2. Each row shows a member of the group with an icon indicating whether the member is an individual user or another group. The row lists the user or group ID and, in the case of a user, the user's primary login credential.
  3. If the group member is a user, the **Active Credential** column shows the type of credentials that the user can use to log in to Looker. If the group member is another group, the **Active Credential** column shows how many users are in the member group.
  4. Hold your cursor over a row to display the three-dot menu for that group member at the right. Use the three-dot menu to remove that member from the group. If you choose to remove the member, Looker will ask you to confirm.
  5. You can click **Add Members** to add a user or another group as a member of the group. Looker will display a dialog where you can search for a username or group name and add the user or group as a member.
  6. You can click the group's three-dot menu to rename the group or delete the group. If you choose to delete the group, Looker will ask you to confirm.

**Warning:** Deleting a group is irreversible. Deleting a group while it is still in use can impact a wide variety of user permissions, which can prevent users from accessing the folders or features they are used to.



## Adding roles to groups

To assign a role to a group, use the **Roles** page in the **Users** section of the **Admin** menu. From there, you can edit the role and assign a group or groups to that role. For more information, see the [Roles](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#assigning_roles) documentation page.

## Deleting groups

To delete a group, click the **Delete** button on the right side of its row. Looker displays a confirmation dialog before you delete the group.

**Warning:** Deleting a group is irreversible. Deleting a group while it is still in use can impact a wide variety of user permissions, which can prevent users from accessing the folders or features they are used to.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
