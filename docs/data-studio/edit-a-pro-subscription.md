---
url: https://docs.cloud.google.com/data-studio/edit-a-pro-subscription/
title: Edit a Data Studio Pro subscription \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:15.653157+00:00
---

# Edit a Data Studio Pro subscription  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/edit-a-pro-subscription/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Edit a Data Studio Pro subscription Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to edit an existing Data Studio Pro subscription.

Don't have a subscription yet? [Subscribe to Data Studio Pro](https://docs.cloud.google.com/data-studio/pro-subscription-overview).

## Before you begin

  * To perform the steps on this page, you must have either the [Owner role](https://docs.cloud.google.com/iam/docs/understanding-roles#owner) on the Google Cloud project that's associated with your Data Studio Pro subscription or the [Workspace Services Admin role](https://support.google.com/a/answer/2405986#services_admin).
  * If the original project owner has left the organization, assign another user the Owner or Looker Studio Pro Manager role on the project to manage or cancel the subscription. Contact an administrator who has the Organization Administrator role (`roles/resourcemanager.organizationAdmin`) to update IAM permissions if needed. Without one of these roles, the option to cancel the subscription isn't visible.



For complete details about required administrative permissions, including configuring [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) for day-to-day user management, see [Data Studio Pro roles and permissions](https://docs.cloud.google.com/data-studio/about-pro-roles-and-permissions).

## Ways to edit a Pro subscription

You can edit a Data Studio Pro subscription by using either the Data Studio Pro interface or the Google Cloud console.

Editing your Pro subscription lets you do the following:

  * Add new users and groups to the subscription
  * Remove users and groups from the subscription
  * Adjust the number of licenses in the subscription



To prevent update conflicts or errors, such as `Couldn't update users/licenses for subscription`, wait at least five minutes between making user membership edits and adjusting license counts. For example, if you want to add or remove users and adjust the number of licenses, first change the users and then wait at least five minutes before adjusting your licenses. Waiting between update requests ensures that your changes are properly recorded.

* * *

## Add users to the subscription

Before your users can access Data Studio Pro features, you need to add the users to the subscription.

### User account prerequisites

  * You can assign licenses only to managed Google Accounts that belong to the same organization as the Google Cloud project that is used for Data Studio Pro. Users from outside your organization can't be included in the subscription. Any external users in a Google Group are excluded from the subscription.
  * If you have enabled [Trusted Organizations](https://docs.cloud.google.com/data-studio/step-2-add-people-to-the-subscription#add-users-from-other-organizations), you can add and manage individual user accounts from those trusted external organizations inside your subscription. However, you can't use Google Groups from an external organization to manage subscription access. External Google Groups aren't supported for cross-organizational subscription membership, and members must be added individually.



Users who only need to view reports that are created within a Data Studio Pro environment don't require a Pro license. They only need the appropriate sharing permissions for the specific reports or data sources. However, these viewers don't have access to Pro-specific features like team workspaces or enhanced content management.

### License count and billing rules

If a user is in multiple Google Groups in a subscription, you are charged for a license only once for that user. However, if an individual user belongs to multiple subscriptions, you are charged for a license for each subscription that the user is in.

  * The number of Data Studio Pro users can't exceed the number of Data Studio Pro licenses that are associated with the subscription. If you plan to add new users to the subscription and don't have enough Pro licenses, you must purchase additional licenses before or during the user assignment process.



### Use the Data Studio interface

To add users or groups to your Data Studio Pro subscription from inside Data Studio, follow these steps:

  1. [Sign in to Data Studio](https://datastudio.google.com).
  2. In the left navigation, click **Pro subscription**.
  3. Locate the Google Cloud project that is associated with your Data Studio Pro subscription, and click **Manage subscription** ![Manage subscription icon](https://docs.cloud.google.com/static/data-studio/images/gmpersonaddgrey60048dp-2020-03-12.png).
  4. To add a user or team to the subscription, enter the user's email address or the Google Group alias in the **Add people and groups** field.
  5. Click **Next**. Because every Data Studio Pro user must have a Pro license, you might need to buy additional licenses for the added users. To learn more, see Add or remove Pro licenses.



### Use the Google Cloud console

To add users or groups to your Data Studio Pro subscription by using the Google Cloud console, follow these steps:

  1. In the Google Cloud project that is associated with your Data Studio Pro subscription, navigate to the Data Studio product homepage: <https://console.cloud.google.com/looker-studio/home>.
  2. Click **Manage access**.
  3. To add a user or team to the subscription, enter the user's email address or the Google Group alias in the **Assign new users / groups** field. If you need more licenses, click **Buy now** to purchase additional licenses, and then return to this screen to assign the users.
  4. Click **Assign**.



* * *

## Remove users or groups from the subscription

### Use the Data Studio interface

To remove users or groups from your Data Studio Pro subscription within Data Studio, follow these steps:

  1. [Sign in to Data Studio](https://datastudio.google.com).
  2. In the left navigation, click **Pro subscription**.
  3. Locate the Google Cloud project that is associated with your Data Studio Pro subscription, and click **Manage subscription** ![Manage subscription icon](https://docs.cloud.google.com/static/data-studio/images/gmpersonaddgrey60048dp-2020-03-12.png).
  4. To remove a user or group, click ![Remove user icon](https://docs.cloud.google.com/static/data-studio/images/donotdisturbonbaselinep900fill0wght400grad0opsz24-2023-09-22.png)**Remove user** for that user or group.
  5. Click **Next** to adjust the number of licenses that are required to support the number of Pro subscribers.



### Use the Google Cloud console

To remove users or groups from your Data Studio Pro subscription from the Google Cloud console, follow these steps:

  1. In the Google Cloud project that is associated with your Data Studio Pro subscription, navigate to the Data Studio product homepage: <https://console.cloud.google.com/looker-studio/home>.
  2. Click **Manage access**.
  3. To remove a user or group, select the user or group under **Manage assigned users/groups** , and click **Delete**.
  4. To confirm that you want to remove this user or group, click **Delete**.



You can adjust the number of licenses that are required to support your Pro subscribers as needed.

### What happens when users are removed from a Pro subscription?

When a user is removed from a Data Studio Pro subscription, the following effects occur immediately:

  * **Feature access:** The removed user no longer has access to Pro features, though they might still use the no-cost version of Data Studio if permitted by your organization.
  * **Content location and ownership:**
    * **Owned by me content:** If the user has content in an **Owned by me** location in Data Studio Pro, that content moves to the user's **Owned by me** location in the no-cost version of Data Studio.
    * **Sandbox content:**
      * If the Pro administrator has [disabled **Owned by me**](https://docs.cloud.google.com/data-studio/set-a-default-google-cloud-project-for-pro) and the user has a **Sandbox** location, the **Sandbox** content remains within the subscription.
      * The removed user's **Sandbox** content won't be visible in the Data Studio report and data source lists; however, the content appears in search results.
    * **Team workspaces:** Content that is created in a team workspace folder remains in that folder and doesn't move.
  * **Alerts and scheduled reports:**
    * **Alerts:** Any alerts that are created by the user stop working.
    * **Schedules:** Scheduled reports that are created by the user continue to work.
  * **License deactivation timeline:** When removing a user from a subscribed Google Group, it can take up to 72 hours for that user's license to be removed from the subscription.

**Important note on suspended users:** Data Studio Pro licenses are provisioned automatically based on Google Group membership. If you suspend a user's Google Workspace account (for example, when an employee leaves the company), you must also remove that user from the Google Group associated with your Data Studio Pro subscription. If a suspended user remains in the Google Group, Data Studio Pro will continue to assign a license to them, and you will continue to be billed for that seat. Removing the user from the group will automatically revoke the license and update your billing count. 

* * *

## Add or remove Pro licenses

Every user of Data Studio Pro, including those within a group, must have a Pro license. You'll be billed for the number of Pro licenses in the subscription, even if the license isn't currently in use.

### Use the Data Studio interface

To add or remove Pro licenses from your Data Studio Pro subscription inside Data Studio, follow these steps:

  1. [Sign in to Data Studio](https://datastudio.google.com).
  2. In the left navigation, click **Pro subscription**.
  3. Locate the Google Cloud project that is associated with your Data Studio Pro subscription, and click **Manage subscription** ![Manage subscription icon](https://docs.cloud.google.com/static/data-studio/images/gmpersonaddgrey60048dp-2020-03-12.png).
  4. To adjust the number of licenses without adding or removing users, or to continue with the number of licenses for users that you just added, click **Next**. To learn more about changing user access, see Add users to the subscription.
  5. Data Studio indicates how many total Data Studio Pro licenses are required to support your subscription. The value of the **Number of licenses to buy** field must be equal to or greater than the number of licenses required to support your subscription. If you choose to buy additional licenses beyond what is required, you can manually update the value in the **Number of licenses to buy** field. If you have removed users from your subscription, you can reduce the number of licenses. The **Number of licenses changed** shows how many users you added in the previous step and the net change in licenses from any manual adjustments.
  6. Review and confirm the adjustment in the number of Pro licenses, and click **Save**.



#### Automatically assign licenses to new users in Pro groups

When you select the **Auto assign available licenses to subscribed groups** option, Data Studio Pro automatically assigns available licenses to new users who join or are added to Google Groups that are part of the subscription. Data Studio assigns available licenses in the order that users open or use the application, until all licenses are assigned.

### Use the Google Cloud console

To use the Google Cloud console to add or remove Pro licenses from your Data Studio Pro subscription, follow these steps:

  1. In the Google Cloud project that is associated with your Data Studio Pro subscription, navigate to the Data Studio product homepage: <https://console.cloud.google.com/looker-studio/home>.
  2. The console indicates the number of licenses that are associated with this subscription under **Purchased licenses**. To adjust this number, click **Add / Remove licenses**.
  3. The value of the **Total licenses** field must be equal to or greater than the number of licenses required to support your subscription. If you choose to buy additional licenses beyond what is required, you can manually update the value in the **Total licenses** field. If you have removed users from your subscription, you can reduce the number of licenses. The **Number of licenses increased** reflects the net increase in licenses that are associated with this Pro subscription.
  4. If you have more Pro licenses than are required across your Data Studio Pro subscription, you can assign available licenses automatically to any new users who are added to an existing group. To assign licenses to these users, select **Auto-assign licenses to new users added to a group**. Data Studio assigns available licenses in the order that users open or use the application, until all licenses are assigned.
  5. Review and confirm the adjustment in the number of Pro licenses, and then click **Confirm**.



* * *

## Troubleshoot "Enter a valid email address" error

When you assign licenses in the Google Cloud console, you might see an `Enter a valid email address` error even when you provide a valid email address for a user in your organization. This situation typically occurs if you lack sufficient `Group View Permission` in the Google Admin console.

To resolve this issue, use one of the following options:

  * **Assign licenses in Data Studio** : Assign users directly through the Data Studio interface at [datastudio.google.com](https://datastudio.google.com). In the navigation panel, select **Pro subscription** to manage license assignments.
  * **Update permissions in the Google Admin console** : Ask your Workspace administrator to grant you organization-wide permissions to view all members.
  * **Use a Google Group** : Create a Google Group for the users to whom you want to assign licenses. Ensure that you have **Viewer** permissions for that group and then assign the license to the group in the Google Cloud console.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
