---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/manage-users/
title: Manage users in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:36:11.116550+00:00
---

# Manage users in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/manage-users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)



Send feedback 

#  Manage users in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Appliance management console user rights and roles will be deprecated in the near future and will be replaced with Google Cloud [Identity and Access Management (IAM)](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-control) roles for Backup and DR.

To access the Backup and DR, each user needs a Google Account added to a Google Cloud project, folder, or organization as a principal with an IAM role that allows access to the appliance management console. The first time a Google Account user (with the relevant IAM role) logs into the management console they are automatically added as a appliance management console user. The appliance management console has its own roles which determines what actions that user can take. Your IAM role will map to a appliance management console role. See the [Appliance management console roles](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/manage-roles) page for more details.

The following table describes the roles that grant access to the management console.

IAM Role | Appliance management console role  
---|---  
Owner 1 | Administrator  
Editor 1 | Administrator  
Backup and DR Admin 1 | Administrator  
Backup and DR User 2 | Basic  
Backup and DR Viewer 3 | Can access the appliance management console  
  
1 After the user first logs in to the appliance management console, it is recommended to manually add the administrator role to their user. Without it they won't be an administrator in **Report Manager**. It also makes it clear that they have the administrator role. See the [Edit a user](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/manage-users#edit-user) section to perform this task. Note that if a user with this IAM role sets their appliance management console role to a less powerful one, they will still hold the appliance management console administrator role because of their IAM role.

2 A Google Account with this IAM role only has the **Basic** role on the appliance management console. They need a user with **System Manage** rights (such as any user who has the administrator role) to manually set their appliance management console role.

3 A Google Account who only has the Backup and DR Viewer IAM role can view the appliance management console with read-only access to limited menus.

The administrator role effectively has the rights of every role, meaning they not only have all possible rights, they can also operate on every resource. Any appliance management console user who has the **Owner** , **Editor** , or **Backup and DR Admin** role is automatically placed into the administrator role, even if that role is not selected in the role assignment panel. The only way to change this is to change their IAM role.

To assign IAM roles to a user:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Click a **Select a project** drop-down menu at the top of the page.

  3. Select the project for which you want to view users.

  4. Find the principal's email address, domain, or other identifier in **Principals** and select **Edit principal**.

  5. The **Select a role** drop-down menu displays all the roles (including any custom roles) that you can grant to the principal on this resource. Search for Backup and DR and assign Backup and DR Admin or Backup and DR User roles.




The appliance management console lets you add, delete, and manage multiple users. The appliance management console roles are assigned to each user such that the user receives the proper authorization to execute certain functions within the appliance management console for managed appliances. The **Users** page under the **Manage** tab lists all of the users that have logged in or been manually added in the appliance management console.

You can create a appliance management console role and assign rights to the role. Based on the rights assigned to a user's role, a user can also be constrained from using or viewing the various components of the appliance management console. From the **Users** page, you can see information such as username, timezone, ID, and creation date. You can modify the display of fields that appear in the **Users** list, and you can also use the filter feature to locate specific users.

## View users in the appliance management console

Use these instructions to view users in the appliance management console:

  1. Click the **Manage** tab and select **Users** from the drop-down menu. The **Users** page opens listing all appliances managed by the management console.
  2. To modify the display of the user properties, you can do the following:

     * **Adjust Fields** : To modify the fields that appear in the table, right-click within the table header row and click the checkboxes for the fields you want displayed (or those fields you don't want to view).
     * **Sort Content** : To sort the content listed in a table column by alphanumeric order, select a column header and then click the up or down arrow to change the order.
     * **Adjust Column Width** : To adjust the width of a table column to show more content in the table, drag the column divider in a column header to the left or right to resize the column width. Column dividers are marked by a pair of thin gray lines.
     * **Filter By** : To filter the list, enter one or more filter criteria as appropriate. (If you don't see the **Filter By** area, click **show filter**). To clear a filter, click the **x** to the right of the applied filter.

**Note:** Filters that are of type text, list, and date, persist across different appliance management console sessions for the same user.
  3. To export the user list click the **Export** icon. You can export in PDF format.




## Create a user

**Note:** The **Create User** option cannot create a Google Account, it can only pre-add it to the appliance management console. Doing so lets you predefine their appliance management console role. Google Account users are created outside of Backup and DR.

Use these instructions to create a new user:

  1. Click the **Manage** tab and select **Users** from the drop-down menu. The **Users** page opens listing all users managed by the appliance management console.
  2. Click **Create User** to open the **Create User** page.
  3. Enter the name of the new user in the **Username** field. The **Username** field is case sensitive.
  4. Select the user's time zone from the **Timezone** drop-down list.
  5. From the **Roles** area in the **Create User** window, check the checkboxes for the roles that you would like to assign to this user. The **Basic** option is selected by default.

  6. Click **Save User**.




## Edit a user

Use these instructions to edit information about an existing user:

  1. Click the **Manage** tab and select **Users** from the drop-down menu.

The **Users** page opens.

  2. Select the user from the list that you want to modify and then select **Edit** (bottom right-hand corner of the page).

The **Edit User** page opens. You can also right-click on the user in the list and select **Edit** from the menu.

  3. Make modifications to the user as described in **Creating a New User**.

  4. Click **Save User** to accept the changes.




## Delete a user

You need **System Manage** rights to delete a user.

**Note:** The **Delete User** option does not delete the Google Account, it will only remove the user from the appliance management console. If the user has a relevant IAM role they are able to sign in again and they are automatically added to the appliance management console, although a user with the Backup and DR User IAM role loses any appliance management console roles that they previously had.

Use these instructions to delete a user:

  1. Click the **Manage** tab and select **Users** from the drop-down menu.

The **Users** page opens listing all appliances managed by the management console.

  2. Select the user from the list and then select **Delete** (bottom right-hand corner of the page). You can also right-click on the user in the list and select **Delete** from the menu.

  3. Click **Confirm** in the confirmation dialog.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
