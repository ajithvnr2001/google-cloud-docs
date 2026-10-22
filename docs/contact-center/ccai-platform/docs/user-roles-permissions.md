---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/user-roles-permissions/
title: User roles and permissions \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:27.961768+00:00
---

# User roles and permissions  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/user-roles-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  User roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

Users of Contact Center AI Platform (CCAI Platform) are allocated roles. The roles determine the permissions that a user has and what they can do in the CCAI Platform portal.

Roles in CCAI Platform are either default roles or custom roles.

## Default user roles and permissions

Within CCAI Platform there are 6 predefined roles that have assigned permission sets. These roles define the configuration, monitoring, and reporting available to the user. A user can be assigned one or a combination of multiple roles.

Beyond these 6 roles, any combination of permission sets can be configured for custom roles. For more information see Custom roles & permissions.

### Role details

**Agent** and **Admin** roles each have fixed permissions sets, whereas manager roles have fixed permission sets but the content varies based on who the user manages. Users with manager roles must be assigned as team managers in the CCAI Platform portal by going to **Settings** > **Users & Team** to be able to see configuration and monitoring data about agents.

#### Agent

The agent role is the only role that can access the CCAI Platform agent adapter.

##### CCAI Platform portal access

  * Agent adapter in the CCAI Platform portal and receives call and chat sessions based on queue assignment.

  * Agent adapter in your CRM.

  * Access to the Agent Desktop ([Preview](https://docs.cloud.google.com/products)).




##### No Access

  * Settings

  * Monitoring

  * External storage

  * Reports




##### Actions available

  * Taking inbound calls.

  * Placing outbound calls.

  * Listening to voicemails.

  * Answering escalation calls.




#### Manager

Manager roles are for users assigned as the team manager to one or more teams and access is partially based on the user's assigned teams. Refer to [Add and configure teams](https://docs.cloud.google.com/contact-center/ccai-platform/docs/add-configure-teams#configuration) for more information.

##### CCAI Platform portal access

  * Settings

    * Queue configuration

    * No access

    * Settings configuration

    * Settings - Call and chat, based on team and queue assignment.

  * Data

    * Monitoring

    * Call and chat dashboards: team-specific data only.

    * Agents: team-specific data only.

    * Calls and chats (connected, queued, completed): Team-specific data only.

    * Queue: team-specific data only.

    * External storage: access to call records, chat transcripts, or both, when they are stored in external storage.

    * Reporting

    * Report builder: team-specific data only




##### No Access

  * Agent adapter in the CCAI Platform portal or CRM

  * Settings - all besides call and chat




##### Actions available

  * Monitoring call and chat queues, only for queues in which their team members are assigned.

  * Downloading reports with data concerning agent performance, queue performance, call and chat volume - but only for their teams.

  * Creating and editing chat shortcuts.




#### Manager: Team

Manager roles are for users assigned as the team manager to one or more teams and access is partially based on the user's assigned teams. Refer to [Add and configure teams](https://docs.cloud.google.com/contact-center/ccai-platform/docs/add-configure-teams#configuration).

Users can now edit this role. Any user who is assigned that role will inherit the role permissions. Click the pencil icon to modify the roles.

##### CCAI Platform portal access

  * Settings

    * Queue configuration

      * Assign agents or teams to queues for assigned teams only.

      * Queue priority.

    * Settings configuration

      * No access.
  * Monitoring

  * Agents: team-specific data only.

  * Calls and chats (connected, queued, completed): team-specific data only.

  * External Storage: Access to call recordings and chat transcripts when they are stored in external storage.

  * Queue: team-specific data only.

  * Dashboard access (data for all teams)

    * Calls: team-specific data only.

    * Chats: team-specific data only.




##### No Access

  * Call or chat adapter in the CCAI Platform portal or CRM



##### Actions available

  * Monitoring call and chat queues, only for queues in which their team members are assigned

  * Downloading reports with data concerning agent performance, queue performance, call and chat volume - but only for their team's

  * Creating and editing chat shortcuts

  * **Shuffling team and agent assignments between queues based on volume**

  * **Assigning Agents and teams to queues**

  * **Configuring priority levels of existing queues (when Priority Routing is enabled)**

  * **Adding new users and assigning to teams or deactivating users**

  * **Assigning existing users to teams**




#### Manager: Data

Manager roles are for users assigned as the team manager to one or more teams and access is partially based on the user's assigned teams. Refer to [Add and configure teams](https://docs.cloud.google.com/contact-center/ccai-platform/docs/add-configure-teams#configuration).

Users can now edit this role. Any user who is assigned that role will inherit the role permissions. Simply click the pencil icon to modify the roles.

##### CCAI Platform portal access

  * Settings

    * Queue configuration

      * Assign agents or teams to queues - assigned teams only

      * Queue priorities

    * Settings Configuration

      * No access
  * Monitoring

    * Agents - team-specific data only.

    * Calls or Chats (connected, queued, completed): team-specific data only.

    * External Storage: Access to call recordings or chat transcripts when they are stored in external storage.

    * Queue: team-specific data only.

    * Dashboard access (data for all teams)

      * Calls - team-specific data only.

      * Chats - team-specific data only.

  * Reporting

    * Report Builder: Full access to all user data



##### No Access

  * Agent adapter in the CCAI Platform portal or CRM.



##### Actions available

  * Monitoring call and chat queues, only for queues in which their team members are assigned.

  * Downloading reports with data concerning agent performance, queue performance, call and chat volume - but only for their team's.

  * Shuffling team and agent assignments between queues based on volume.

  * Configuring queues, redirects, and per-queue routing options (doesn't include enabling the features at the environment level).

  * Assigning Agents and teams to queues.




#### Manager: Admin

Manager access is partially based on the user's assigned teams. Refer to [Add and configure teams](https://docs.cloud.google.com/contact-center/ccai-platform/docs/add-configure-teams#configuration).

Users can now edit this role. Any user who is assigned that role will inherit the role permissions. Click the pencil icon to modify the roles.

##### CCAI Platform portal access

  * Settings

    * Queue Configuration

      * Assign **any** agents or teams to queues

      * Queue priorities

    * Settings Configuration

      * Agent & team: Full access

      * Target Metrics (within **Settings > Operation Management**)

  * Data

    * Monitoring

      * Dashboard access (data for all teams)

        * Calls

        * Chats

      * Agents: Full access

      * Calls and chats (connected, queued, completed): Full access

      * External Storage: Access to call recordings or chat transcripts when they are stored in external storage.

      * Queue: Full access

  * Reporting

    * Report Builder: Full access to all user data



No access

  * Agent adapter in the CCAI Platform portal and CRM

  * Call and chat settings

  * Developer settings




##### Actions available

  * Monitoring all call and chat queues

  * Downloading reports with data concerning agent performance, queue performance, call and chat volume for all queues and Agents

  * Shuffling team and agent assignments between queues based on volume

  * Adding new users and assigning to teams and deactivating users

  * Assigning existing users to teams

  * **Creating or editing queue structures for any language or channel**




#### Admin

Full access to environment settings, queue configuration, monitoring, and reporting.

##### CCAI Platform portal access

  * Settings

    * Queue configuration

      * Add and edit queues with full access
    * Settings configuration

      * All settings access including Developer Settings

      * Agent & team: Full access

    * Agent Desktop ([Preview](https://docs.cloud.google.com/products))

      * Global, queue, and team settings
  * Data

    * Monitoring

      * Call and chat dashboard: Full access

      * Agents: Full access

      * Calls and chats (connected, queued, completed): Full access

      * External storage: access to call recordings, chat transcripts, or both, when they are stored in external storage.

      * Queue: Full access

    * Reporting

      * Report builder: Full access to all user data



##### No access

  * Agent adapter in the CCAI Platform portal and CRM



##### Actions available

  * Responsible for viewing or managing users on multiple teams, even when not assigned as the team manager

  * Are responsible for monitoring call and chat queues for all queues

  * Are responsible for downloading reports with data concerning agent performance, queue performance, call and chat volume for all users

  * Configuring queues, redirects, and per-queue routing options

  * Responsible for assigning agents to queues

  * Shuffling team and agent assignments between queues based on volume

  * Adding new users and assigning to teams or deactivating users

  * Assigning existing users to teams

  * Creating or editing queue structures for any language or channel

  * Modifying environment wide settings to disable or enable channels, update how Agents are notified of new sessions, hours of operation, messages played to consumers or routing features like enabling Auto Answer or Priority routing

  * Setting up technical integrations




Don't see a role you want? Create your on custom role: Custom roles & permissions.

## Custom roles and permissions

In addition to the 6 default user roles (Admin, Manager, Manager Data, Manager Teams, Manager Admin, Agent), with custom roles & permissions, you can create custom roles with unique sets of permissions assigned. This gives flexibility in deciding which users (or groups of users) have access to specific sections of the Contact Center AI Platform (CCAI Platform) portal, features, and the agent adapter.

You can grant users access to any page contained in the CCAI Platform portal, including the dashboards and settings pages. Permissions for users can be edit, view-only, or restricted to data relevant to the team that they are assigned to.

### Agents

An agent is a user that is assigned the agent role. Only an agent can answer a call or a chat. You can assign the agent role to a user when you [add a user](https://docs.cloud.google.com/contact-center/ccai-platform/docs/add-edit-user#add-users), or by [editing an existing user](https://docs.cloud.google.com/contact-center/ccai-platform/docs/add-edit-user#edit-user).

For an agent to be able to answer a call or a chat, you must either: (1) Assign the agent directly to a queue, or (2) Assign the agent to a team that is assigned to a queue. For more information, see [Add and configure teams](https://docs.cloud.google.com/contact-center/ccai-platform/docs/add-configure-teams#configuration) and [Queue and menu setup](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Queue_and_Menu_Setup).

### Feature specifics

The following sections provide overview of the specific features.

#### What are permissions?

The ability to perform actions within the CCAI Platform portal (including viewing content, editing content, and changing configuration) is governed by permissions. Each individual permission has a name (such as **Settings - Users & Teams - Edit User**) and covers one action or a small subset of actions. A user must be granted permission in order to do the corresponding action; permissions are defined by the pages and features that provide the actions.

#### What are roles?

Rather than assigning individual permissions directly to each user, permissions are grouped into roles. You can define one or more roles in your Contact Center AI Platform environment, and then grant permissions to each role.

Each user must be given a role upon creation, and may optionally be assigned up to 9 more additional roles. It is a good practice to create several roles in within your CCAI Platform environment.

#### General points about roles

  * There is a maximum of 100 custom roles per CCAI Platform instance.

  * There is a maximum of 10 roles per user.

  * When multiple roles are assigned to a user, the highest level of permissions will be granted.

  * When a user doesn't have view or edit access to a page, they won't see the associated section of the CCAI Platform portal.




#### Default roles

Default roles cannot be edited or renamed. If you want to adjust the permissions in a role, you can create a new role with the necessary permissions.

### Types of permissions

The following sections outline the types of permissions.

#### View versus edit permissions

For many permissions, you can specify view or edit access.

  * **View** : Allows the user to view the page.

  * **Edit** : Always grants view access and allows the user to make changes on the page.




#### Assigned team only

Some permissions have an assigned teams only option associated with it. When selected, users assigned this role will only be able to access information relevant to the teams they have been assigned to. Refer to [Add and configure teams](https://docs.cloud.google.com/contact-center/ccai-platform/docs/add-configure-teams#configuration) for more information.

This setting is specific to an individual permissions. A user may be given access to assigned teams only for one page permission, but be given access to all for another.

#### Assigned queues only

Dashboard permissions have an assigned queues only option associated. When selected, users assigned this role will only be able to access information relevant to the selected queues that their team has been assigned to.

This setting is specific to individual permissions. A user may be given access to assigned queues only for one page, but be given access to all data for another.

#### Assignable roles

Limit which roles a user can assign to other users using the **assignable roles** feature. An example use case would be to only allow a Supervisor to assign the agent role and ensure no new users are assigned the **Admin** role by the supervisor.

To assign the role:

  1. In the CCAI Platform portal, go to **Settings** > **Users & Teams** > **Edit User**.

  2. Click **Assignable roles**.

  3. Select the roles you want the current role to be able to assign to other users.




### License types

Within CCAI Platform there are various user license types for billing purposes which include agent, Screen Share agent, manager, and administrator. The following list provides the definitions for which user permissions constitute which type of license. Any custom role that is created will be assigned a license type.

The license type definitions will be the following:

  * **Admin** : A user with one or more administrator permissions.

  * **Manager** : A user with one or more manager permissions, but no 'Admin' permissions.

  * **Agent** : A user with only agent permissions.

  * **Screen Share agent** : A user with only agent permissions and Screen Share permissions.




If a user is assigned multiple different roles that fall into different license type categories, then the highest impact license type is assigned to the user. The impact order is: Admin > Manager > Screen Share agent > Agent.

In the following table is a breakdown of which permissions are associated with which license type.

![Permissions](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ca1fe05072.png)

![License types](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ca1fe22c78.png)

### CCAI Platform portal configuration

The following sections provide information on how to create, edit, and delete custom roles.

#### Create a new custom role

  1. In the CCAI Platform portal, go to **Settings** > **Users & teams**.

  2. Click **Roles & permissions**.

![Roles & permissions](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ca1fe44002.png)

  3. Click **Add roles**.

  4. Enter the role name as it will be viewed in this settings page and reports. The character limit is 20.

![Add roles display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ca1fe479c0.png)

  5. Enter the label name as it will show on the **Users & teams** settings page. The character limit is 16.

  6. Choose a label color. Labels show on the **Users & teams** page for quick views of role assignments.

  7. Click **X** to save your color setting.

![Color settings page](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ca1fe4b6fb.jpg)

Example view of labels and colors:

![Users and teams page](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ca1fe4eba1.png)

  8. Assign permissions to the role by checking the box next to the permission.

![Assign permission display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ca1fe5247c.png)

Refer to Assignable roles, View/Edit permissions, Assigned teams only, and Assigned queues only for permission type details.

  9. Click **Save**.




Your new role will show at the bottom of the **Roles & permissions** page, but can be dragged higher if preferred.

#### Edit a custom role

  1. From the CCAI Platform portal, go to **Settings** > **Users & Teams.**

  2. Click **Roles & permissions** at the top of the page.

  3. Click the pencil icon next to the role that you want to edit.

  4. After completing your edits, click **Save**.




Any users with the edited role assigned will need to refresh their web browser or sign out and back in to see the updates.

#### Delete a custom role

  1. From the CCAI Platform portal, go to **Settings** > **Users & Teams.**

  2. Click **Roles & permissions** at the top right of the page.

  3. Click the **X** icon next to your role.

  4. Confirm the deletion of the custom role.




#### Rearrange role order

The order of the list of roles on the Roles & Permissions settings page dictates the order of the roles in the Edit User drop-down.

Roles drop-down on the Add or Edit User UI:

![Add / Edit display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ca1fe6aa0f.png)

To change the order of the roles:

  1. In the CCAI Platform portal, go to **Settings** > **Users & teams**.

  2. Click **Roles & permissions**.

  3. Reorder the list by clicking and dragging it to the preferred location.

  4. The new order is saved automatically.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
