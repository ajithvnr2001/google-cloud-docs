---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/add-edit-user/
title: Add, view, and edit users \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:14.239725+00:00
---

# Add, view, and edit users  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/add-edit-user/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Add, view, and edit users Stay organized with collections  Save and categorize content based on your preferences. 

Users can be added individually by following these steps or can be imported in bulk. When a user is added, they will need to activate their account. The account activation is done by clicking on the link in the email to complete the process.

For details about each default user role and how to create custom roles, see [Default user roles and permissions: Agent, Managers, Admin](https://docs.cloud.google.com/contact-center/ccai-platform/docs/user-roles-permissions#default-roles) and [Custom roles & permissions](https://docs.cloud.google.com/contact-center/ccai-platform/docs/user-roles-permissions#custom_roles_permissions).

See [Bulk user management](https://docs.cloud.google.com/contact-center/ccai-platform/docs/bulk-user-management) for details on adding more than one user at a time.

## Add a user

To add a user, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Users & Teams**. If you don't see the **Settings** menu, click menu **Menu**. The **Users & Teams Settings** page appears.

  2. Click **Add Users**. The **Add User** pane appears.

  3. To add user information, open the **User Information** section, and then do the following:

     1. In the **Work Email Address** field, enter the email address that the agent uses to sign in.

     2. In the **First Name** field, enter the agent's first name.

     3. In the **Last Name** field, enter the agent's last name.

     4. Optional: In the **Aliases** field, enter the agent's alias. For more information, see [Agent aliases](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-alias).

     5. In the **Agent ID** field, enter the agent ID.

     6. In the **Location** list, select the location of the user. This controls the default language of the agent adapter.

  4. To assign roles to the user, open the **Role** section, and then do the following:

     1. Click **Assign role**. The **Assign role** dialog appears.

     2. In the **Select role** list, select a role, and then click **Assign**.

     3. To assign additional roles, repeat the previous step.

**Note:** If you're creating a user for an administrator or manager and you want that user to have access to the agent adapter, assign the agent role in addition to any other roles.

For more information about roles, see [Custom roles and permissions](https://docs.cloud.google.com/contact-center/ccai-platform/docs/user-roles-permissions#custom_roles_permissions).

  5. To configure preferences for the user, open the **Preferences** section, and then do the following:

     1. Optional: Configure the user's call concurrency or chat concurrency settings. Enter the maximum number of calls or chats that the user can handle at one time. This setting overrides the general call and chat concurrency settings.

     2. Optional: To enable your global phone management settings' international calling configuration, click the **International calling** toggle to the on position. For more information, see [Phone number management](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#phone-number-management).

     3. Optional: In the **Availability Preference** list, select the availability preference for the user.

  6. Click **Add**.




### Invitation email

After you click the **Add** button in the create user flow, an email will be sent to the email address specified with an invite link to activate their account.

  * **Email subject:** Invitation to <Your Company Name> Support. The company name used here is set in **Settings > Support center details**.

  * **Email body:** You have been invited to join YOUR COMPANY NAME on the CCAI Platform.

  * **Invite Link:** Takes the user to the CCAI Platform portal sign in page set up their password or sign in using SSO if enabled. The link doesn't have a defined expiration duration, however, it will be invalidated once it is accepted or a new invitation link has been sent.




## View existing users and teams

The user list for any selected team will only display the list of users that are directly assigned to that team or sub-team. To avoid confusion and not show an agent or user assigned to a sub-team multiple times in any higher-level teams, users only show in the team they are directly assigned to.

Example:

  * Parent team A (450 users) - all 450 agents are assigned to sub-teams, none are directly assigned to team A - user list will show: **0 users**

    * Team A-1 (200 users) - user list will show: **200 users**

    * Team A-2 (150 users) - user list will show: **150 users**

    * Team A-3 (100 users) - user list will show: **0 users**

    * Team A-3.1 (90 users) - user list will show: **90 users**

    * Team A-3.2 (10 users) - user list will show: **10 users**




The **filter** drop-down can be used to restrict the users that are displayed. Filter options include:

  * Unactivated users.

  * Unassigned agents.




## Edit a user

Edit a user only when that user isn't signed in. Otherwise, your edits might not be saved.

To edit a user, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Users & Teams**. If you don't see the **Settings** menu, click menu **Menu**. The **Users & Teams Settings** page appears.

  2. For the user that you want to edit, click more_horiz, and then click edit **Edit user**. The **Edit User** pane appears.

  3. Edit the user's information, and then click **Update**.




## Remove a user from teams

To remove a user from one or more teams, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Users & Teams**. If you don't see the **Settings** menu, click menu **Menu**. The **Users & Teams Settings** page appears.

  2. For the user that you want to edit, click more_horiz, and then click edit **Edit user**. The **Edit User** pane appears.

  3. Open the **Teams** section.

  4. Do one of the following:

     1. To remove a user from specific teams, clear the checkbox next to the teams to remove the user from.

     2. To remove a user from all teams, click **Remove from all teams**.

  5. Click **Update**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
