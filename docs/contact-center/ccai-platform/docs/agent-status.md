---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-status/
title: Agent statuses \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:59.997937+00:00
---

# Agent statuses  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Agent statuses Stay organized with collections  Save and categorize content based on your preferences. 

Agent statuses, also referred to as Aux codes, are used to track time spent on different tasks and to make agents available for calls or chats. CCAI Platform has default statuses and the ability to create custom statuses to fit a variety of processes and needs.

  * All statuses are available for all agents in your environment with the exception of Special Task, which is only available to Managers.

  * With the exception of Available and In-chat, all default and custom statuses will be considered. "unavailable" states so calls and chats won't be routed to agents while in that status.

  * The **Agent Monitoring** page shows agent statuses.

  * Default status and changing statuses.

    * The system maintains your last status: when putting the computer to sleep or logging out, in most cases the status you're in will be saved when you come back to your computer or sign in.

    * Admins can set the default status on login in **Settings** > **Operation Management**.

See [Auto Answer - Calls](https://docs.cloud.google.com/contact-center/ccai-platform/docs/auto_answer) for default status setting specifics.

    * Agents can change their status while not on a call or chat, OR

    * When enabled, Agents can have the ability to choose which status to go into after their current call or chat to go on break.

    * Managers and Admins can update Agent's statuses. See [Admin or Manager - Updating an Agent's Status](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-status-update) for details.




With the exception of Available and In-chat, all default and custom statuses are considered "unavailable" states and calls or chats aren't routed to agents in an "unavailable" status. An exception is when agent status breakthough is enabled. If an agent is in In-Chat status and has not reached the max chat threshold, they will be routed new chats until the threshold is met. See [Chat Settings](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-settings-web-and-mobile#UUID-edf6dbbd-4caa-3edc-9070-2dfecf1af729) for further information regarding maximum chats.

Status name | Color | Set by | Meaning | Notes  
---|---|---|---|---  
Available | Green | System/Agent | Calls and chats will be routed to agents |   
Unavailable | Red | System/Agent | Calls and chats won't be routed to agents |   
Break | Yellow | System/Agent | Calls and chats won't be routed to agents |   
Special Task | Pink | Manager Only | Calls and chats won't be routed to agents | Agents cannot put themselves in this status, it must be assigned by a manager from the **Agents** page.  
Meal | Brown | Agent | Calls and chats won't be routed to agents |   
Missed Call | Purple | System | If using Deltacast, this status will show after an agent misses a set amount of calls. | When a call gets put into Missed Call status, the agent then has to put themselves back into _Available_ status. See [Call Multicast and deltacast](https://docs.cloud.google.com/contact-center/ccai-platform/docs/routing#multicast_and_deltacast) for more details.  
Missed Chat | Grey | System | If using Deltacast, this status will show after an agent misses a set amount of chats. | See [Call Multicast and deltacast](https://docs.cloud.google.com/contact-center/ccai-platform/docs/routing#multicast_and_deltacast) for more details.  
Unresponsive | Lime | System | A system status an agent is put into if our system registers more than x (a configurable number) consecutive `skipped` calls. | This status is indicative of an agent unable to receive calls, due to the hardware, software, networks, or combination of these factors.  
Wrap-up | Purple | System/Agent | Calls and chats won't be routed to agents. This status is either system-set based on automatic wrap-up settings, or can be selected manually by the agent. | Wrap-up status set manually shows the same in reports as when agents are placed in Wrap-up automatically. To differentiate, we suggest creating a custom status for Wrap up called "Manual Wrap-up" or "Excess Wrap-up" and train agents to use this instead when using the status manually.  
Wrap-up Exceeded | Light Grey | System | Calls and chats won't be routed to agents. | This status is system-set and cannot be selected by a manager or agent. Once it is on, the transition from _wrap-up_ status to _wrap-up exceeded_ is automatic.  
In-call | Light Blue | System | Agents are automatically placed in this status when on a call | Agents cannot log out during this status  
In-chat | Indigo | System | Agents are automatically placed in this status when in a chat | Agents cannot log out during this status  
Offline | Grey | System/Agent | When an agent logs out or the Timeout limit is met, an agent will be considered offline |   
  
## Agent status configuration

This section shows you how to configure and manage agents statuses.

### Create a custom agent status

You can create a custom agent status if the default and system statuses don't meet your needs. Custom agent statuses are designated `Unavailable`. That is, agents that are in one of your custom statuses won't receive calls or chats.

To create a custom agent status, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.
  2. Go to the **Agent Status** pane, and then click **View agent status list**. The **Agent Status** list appears.
  3. Click **Add Status**. The **Add Agent Status** dialog appears.
  4. In the **Status name** field, enter a name for your custom agent status. This name appears in the **Agent Status** list.
  5. Click the **Status color** field. A list of colors appears.
  6. Click a color. The color appears next to your status name in the **Agent Status** list.
  7. To prevent users from selecting this agent status, do the following: 
     1. Under **Status access** , click **Restrict agent status**.
     2. Do one of the following: 
        * To prevent all users (regardless of their roles) from selecting this agent status, click **To all roles**. 
        * To prevent users with specific roles from selecting this agent status, do the following: 
          1. Click **To specific roles**.
          2. Click the **List of restricted roles is required** field. A list of available roles appears.
          3. Click a role that you want to prevent from selecting this agent status. The role appears in the field. 
          4. To add additional roles, repeat these steps.
  8. If you want calls to break through to an agent in this status, click **Allow calls to breakthrough this agent status**. For more information, see [Agent status breakthrough](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-status#agent-status-breakthrough).
  9. To add translations, follow these steps: 
     1. Click **Add Translation**. The **Add a translation** dialog appears. 

**Note:** If you have already added translations for all available languages, the **Add Translation** button doesn't appear. 

     2. Click the **Language** field. A list of languages appears. Languages for which you already have a translation are not in this list.
     3. Click a language for which you want to add a translation.
     4. In the **Translation** field, enter your translation, and then click **Add**. Your new translation appears in the table under **Translations**.
     5. To add another translation, click **Add Translation** and repeat these steps.
  10. Click **Add**.



### Edit a custom agent status

To edit a custom agent status, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Agent Status** pane, and then click **View agent status list**. The **Agent Status** list appears.

  3. For the agent status that you want edit, click more_horiz **More** , and then click **Edit agent status**.

  4. Make your edits, and then click **Save**.




### Agent status on login

  1. Go to **Settings** > **Operation Management**.

  2. Navigate to the **Agent Status** section.

  3. Select one option:

**Same status before logout** : assigns the last status of that specific agent before the last logout.

**Specific status** : select from the list of available statuses to always assign the same status at login.

  4. Click **Set Agent Status**.




### Allow agents to set their next status while on a call or chat

By default, the status selector is only available to agents when not in In-call or In-chat status. When the **Set agent status** option is enabled, the agent is presented with a menu to change their "next status" so that once they are off their current call/chats, they won't be placed into Available.

  1. Go to **Settings** > **Operation Management**.

  2. Navigate to the Agent Status section.

  3. Mark the checkbox to enable.

  4. Click **Set Agent Status**.




### Availability preferences

Sometimes agents who are skilled for voice and chat need the flexibility to take only chats or only voice calls. You can use availability preferences to receive only certain types of contacts to meet the needs of the customer, prioritizing what is most needed at the time.

This feature is enabled at the global level by administrators, and can be enabled for agents so they can change their own availability preferences without the need for a manager or administrator to be available to do it for them. This page discusses the steps required to enable this feature, and links to other articles which explain how the feature will be used by agents.

#### Let agents change their own availability preferences

To let agents change their own availability preferences, follow these steps:

  1. Go to **Settings > Operation Management > Agent Status**.

  2. Check the box next to **Allow agents to change Availability preferences** to allow agents to change their own availability preferences. If you only want for administrators or managers to be able to do this, leave this checkbox unchecked.

  3. Check the box next to **Allow agents to select to receive calls on their mobile phone** to allow Either to the phone number specified in their user profile, or the Agent App if given the correct permission.

  4. Select **Save Agent Status**.




#### Create an availability preferences filter

You can create multiple preset filters to apply to agents as needed. Follow these steps to create a filter:

  1. Go to **Settings > Users & Teams > Availability Preferences**.

  2. Click **\+ Add Preferences**.

  3. A new window appears, make your selections:

     1. Name the filter.

     2. Add a description (optional).

     3. Check the boxes next to the filters you would like to apply. You can create multiple filters.

  4. Once you have selected all the filters you want to allow for this configuration, click **Save**.

![The availability preferences filters choices are shown, arranged by section.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/availability-preferences-filters.png)




You will then see the new filter in the list on the availability preferences page.

If you need to edit or delete a preset filter, you can go back to the availability preferences page where the Actions column can be found on the right side of the screen on the row containing the filter you want to change.

Once you have created a set of filters, you can update existing users or teams to include these availability preferences.

#### Add availability preferences to a user

Availability preferences can be added to an agent's profile in the Users & Teams settings menu. For information about how to add, view, and edit users, see [Add, view and edit users.](https://docs.cloud.google.com/contact-center/ccai-platform/docs/add-edit-user)

  1. Go to **Settings > Users & Teams > Manage Users & Teams.**

  2. Select **Add a User** to add a new user, or select the **Edit button** (pencil icon) next to an existing user to open the **Add User / Edit User** menu.

     1. If you need to create a new user, fill in all the other required fields.
  3. At the bottom of the menu there is an **Availability Preferences** drop-down list, select the preferred filter from the options in the list.

  4. Select **Save**.




#### Add availability preferences to a team

Availability preferences can be added to a team's profile in the Users & Teams settings menu. For information about how to add and edit teams, see [Add, view, and edit teams](https://docs.cloud.google.com/contact-center/ccai-platform/docs/add-configure-teams).

  1. Go to **Settings > Users & Teams > Manage Users & Teams**.

  2. Select **Add a Team** to add a new team, or click the **Edit button** (pencil icon) next to an existing team to open the **Add Team / Edit Team** menu.

     1. If you need to create a new team, fill in all the other required fields.
  3. At the bottom of the menu, there will be an Availability Preferences field with a search bar. Start typing the preferred filter keyword and choose from the options presented in the list.

  4. Select **Save**.




### Enable transfers to all logged in agents

When this setting is enabled, agents can transfer a call or chat to another agent, regardless of their current status. This is useful for escalations and allowing consumers to work with the same agent without having to call back when they are busy.

  1. Go to **Settings** > **Operation Management**.

  2. Navigate to the Agent Status section.

  3. Mark the checkbox to enable call or chat transfers to all logged in agents.

  4. Click **Set Agent Status**.




## Agent experience

![The agent experience for status at login](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632c99ccbc873.png)

## Agent status lists

You can use agent status lists to set custom agent statuses for queues and teams. This grants customers the flexibility to choose which statuses the members of specific queues and teams can have access to by assigning a list of custom statuses to them. The agents of these queues and teams will not be able to see any other statuses (except the default statuses and system list) in the status selectors of their call and chat adapters.

**Note:** Only custom statuses and optional default statuses can be added to an agent status list. The System List is available by default to all agents. See [Default Statuses](https://support.ujet.co/hc/en-us/articles/115006056888-Agent-Statuses#UUID-a2e1f3f5-588e-6e7c-b23f-be7b751ed630_section-idm234692142583864).

### Creating, editing and deleting an agent status list

#### Create

To create an agent status list, follow these steps:

  1. Go to **Settings > Operation Management > Agent Status > Manage Agent Statuses.**

  2. Select **Agent Status Lists**.

  3. Select **Create agent status list**.

  4. Enter a name for your list in the **Agent status list name** text field.

  5. Select **Create**. You will be returned to the Agent Status Lists page where you will see your newly created list.

  6. Custom statuses or optional default statuses must be added to the list. Select the new list to open it.

  7. From here you can:

     1. **Import agent status** (See Bulk Status Management)

     2. **Add agent status**

     3. **Create agent status** (See Create a custom agent status for this process.)

  8. Select **Add agent status**.

  9. A drop-down menu appears from which you can multi-select all statuses you wish to assign to this list.

  10. When all statuses are chosen, select **Add**.

  11. Statuses will be added to the Agent Status List.




#### Edit

To edit a agent status list, follow these steps:

  1. Go to **Settings > Operation Management > Agent Status > Manage Agent Statuses**.

  2. Select **Agent Status Lists**.

  3. Select the list to edit.

  4. Select the **Options Button** (ellipsis) and choose **Edit agent status list.**

  5. Make all changes in the Edit Agent Status List page.

  6. Select **Save** to implement changes, or **Cancel** to discard changes made.


**Note:** The system list cannot be edited.

#### Delete

To delete an agent status list, follow these steps:

  1. Go to **Settings > Operation Management > Agent Status > Manage Agent Statuses.**

  2. Select **Agent Status Lists**.

  3. Select the list to delete it.

  4. Select the **Options Button** (ellipsis) and choose **Delete** **agent status list.**

  5. A pop up window appears asking you to confirm your decision. Select **Delete** to remove the status, or **Cancel**.




### Assign an agent status list to a queue

When an agent status list is assigned to a queue, all agents operating within that queue will see only the statuses of that list available to them, as well as the statuses in the System List (see Default Statuses). All other custom statuses that are not part of the assigned list will be hidden.

One agent can be a member of multiple queues, which may have different agent status lists assigned to them. In this case the agent will see a union set of all of their queues' available custom statuses.

  1. Go to **Settings > Queue > IVR/Mobile/Web**.

  2. Select the queue to add an Agent Status List to.

  3. Scroll to **Agent Status List**.




![The headings for the agent status list is shown.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/assign-agent-status-list.png)

  1. Select **Configure.**

  2. Select an agent status list from the drop-down menu. The System List and Global Agent Status list won't be shown as they are always available to all agents, as well as the status list assigned to the queue.

  3. Select **Save**.




### Assign an agent status list to a team

When an agent status list is assigned to a team, all agents operating within that team, regardless of the queue they are assigned to, will see only the statuses of that list available to them, as well as the System List and Global Agent Status List, and the status list assigned to the queue. All other custom statuses that are not part of the assigned lists will be hidden.

One agent can be a member of multiple teams, which may have different agent status lists assigned to them. In this case the agent will see a union set of all of their teams' available custom statuses.

  1. Go to **Settings > Users & Teams.**

  2. Choose the team to assign an agent status list to.

  3. Select the **Edit button** (pencil icon) next to the team name in the menu bar. Agent status lists can also be assigned to teams when they are created.

  4. Go to the **Agent status list** section.

![The agent status list options are shown, with allow transfers into this team selected.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/assign-agent-status-list.png)

  5. Select the agent status list to assign the status to the team from the drop-down menu.

  6. Select **Save**.




### Bulk status management

Bulk status management lets you use the contents of a .CSV file to create or modify large numbers of statuses simultaneously.

  1. Go to **Settings > Operation management > Agent status > Manage agent statuses**.

  2. Go to **Bulk Status Management**.

  3. If there has been a previous import, the page will show the latest status of the latest import. If there has been a previous import, select **Upload statuses**.

  4. On the **Import statuses** page, use the buttons in the **Step 1: Download template** section to download a file to use for adding or modifying statuses. Only custom statuses will be created and edited. If the uploaded file includes default or system statuses, it will generate an error.

![The options for importing statuses are shown.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/import-bulk-status-management.png)

  5. To add new statuses, click the **Template** button to download a sample CSV file that you can populate with the information for the statuses being added.

  6. To modify existing statuses, click the **Complete list of statuses** to download the information for all current statuses as a CSV file. You can then make any necessary changes to modify existing statuses in this file.

  7. Once the CSV file has been updated, proceed to the **Step 3: Upload CSV** section and either drag-and-drop the updated CSV file into the space provided or click the **Browse your files** button to manually select the file to upload.

  8. Click **Process**. The **Import Statuses** pane indicates when the import is complete. In addition, Contact Center AI Platform sends a confirmation email indicating that the import is complete.




#### Import agent statuses

When creating a new Agent Status List, the option is presented to **Import Agent Statuses**. This option will trigger the same bulk status import flow. However, since it is occurring within the list creation page, all imported statuses will automatically be assigned to the list being created. If there are new statuses being imported that have not been previously created they will be automatically added to the Agent Statuses list.

## Agent status in reporting

For a summary of time spent in each status, pull the Agent Activity Summary Report (**Reports** > **Agent & Team** > **Agent Activity - Summary Report**).

For a detailed timeline view of when and for how long an agent was in each status, as well as other detailed actions, pull the Agent Activity Timeline Report (**Reports** > **Agent & Team** > **Agent Activity -Timeline Report**).

Agent status names appear in English (US) in reports.

## Agent status translation

CCAI Platform translates default and system agent statuses into a specific set of languages. The agent adapter displays these agent statuses according to the location that is assigned to the agent. If an agent isn't assigned a location, agent statuses appears in English (US).

### Custom agent status translation

When you create custom agent statuses, you can provide your own translations for them in any of the languages that CCAI Platform supports. You can provide translations for only the languages that you need. If there isn't an agent status translation available for the location assigned to an agent, the status appears in English (US) in the agent adapter.

You can only add translations for custom agent statuses. Default and system statuses are translated by default and these translations are not editable.

### View translations for default and system agent statuses

You can view the translations that are available for default and system agent statuses. These translations are not editable.

To view translations for default and system agent statuses, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Agent Status** pane, and then click **View agent status list**. The **Agent Status** list appears.

  3. For any default or system agent status, click more_horiz **More** , and then **Edit agent status**. Under **Translations** , a table appears that shows the agent status translations for each available language.




### Create a custom agent status with translations

To create a custom agent status with translations, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.
  2. Go to the **Agent Status** pane, and then click **View agent status list**. The **Agent Status** list appears.
  3. Click **Add Status**. The **Add Agent Status** dialog appears.
  4. In the **Status name** field, enter a name for your custom agent status. This name appears in the **Agent Status** list.
  5. Click the **Status color** field. A list of colors appears.
  6. Click a color. The color appears next to your status name in the **Agent Status** list.
  7. To prevent users from selecting this agent status, do the following: 
     1. Under **Status access** , click **Restrict agent status**.
     2. Do one of the following: 
        * To prevent all users (regardless of their roles) from selecting this agent status, click **To all roles**. 
        * To prevent users with specific roles from selecting this agent status, do the following: 
          1. Click **To specific roles**.
          2. Click the **List of restricted roles is required** field. A list of available roles appears.
          3. Click a role that you want to prevent from selecting this agent status. The role appears in the field. 
          4. To add additional roles, repeat these steps.
  8. If you want calls to break through to an agent in this status, click **Allow calls to breakthrough this agent status**. For more information, see [Agent status breakthrough](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-status#agent-status-breakthrough).
  9. To add translations, follow these steps: 
     1. Click **Add Translation**. The **Add a translation** dialog appears. 

**Note:** If you have already added translations for all available languages, the **Add Translation** button doesn't appear. 

     2. Click the **Language** field. A list of languages appears. Languages for which you already have a translation are not in this list.
     3. Click a language for which you want to add a translation.
     4. In the **Translation** field, enter your translation, and then click **Add**. Your new translation appears in the table under **Translations**.
     5. To add another translation, click **Add Translation** and repeat these steps.
  10. Click **Add**.



### Add translations to an existing custom agent status

To add translations to an existing custom agent status, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Agent Status** pane, and then click **View agent status list**. The **Agent Status** list appears.

  3. For the custom agent status that you want to edit, click more_horiz **More** , and then click **Edit agent status**.

  4. To add translations, follow these steps: 
     1. Click **Add Translation**. The **Add a translation** dialog appears. 

**Note:** If you have already added translations for all available languages, the **Add Translation** button doesn't appear. 

     2. Click the **Language** field. A list of languages appears. Languages for which you already have a translation are not in this list.
     3. Click a language for which you want to add a translation.
     4. In the **Translation** field, enter your translation, and then click **Add**. Your new translation appears in the table under **Translations**.
     5. To add another translation, click **Add Translation** and repeat these steps.
  5. Click **Save**.




## Agent status breakthrough

Agent status breakthrough allows incoming calls to be routed to agents even when they are in a specific status, such as `Unavailable`. This feature provides greater flexibility in managing call routing and agent availability.

### Statuses that you can break through

**Default statuses:**

  * Unavailable
  * Break
  * Special task
  * Meal
  * Wrap-up



**System:**

  * Missed Call
  * Missed Chat
  * In-chat
  * Wrap-up Exceeded (if enabled)



**Custom:**

  * Any custom status



### Turn on agent status breakthrough globally

To turn on agent status breakthrough globally, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Agent Status** pane.

  3. For **Agent Status Breakthrough** , select the **Allow incoming calls to be routed to agents while on breakthrough statuses** checkbox.

  4. Click **Save Agent Status**.




### Turn on agent status breakthrough at the queue level

To turn on agent status breakthrough at the queue level, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **IVR (Interactive Voice Response)** pane, click **Edit / View**.

  3. Click the queue that you want to edit.

  4. In the **Settings** pane, go to the **Agent Status Breakthrough** section, and then click **Configure**.

  5. Click the **Agent Status Breakthrough** toggle to the on position.

  6. Optional: To configure breakthrough for a DAP, do the following:

     1. Select the **Allow calls to breakthrough agent status only when received through certain DAPs** checkbox.

     2. Select a DAP from the list that appears.

  7. Click **Save**.




### Allow breakthrough for an agent status

To allow breakthrough for an agent status, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Agent Status** pane, and then click **Manage Agent Statuses**.

  3. For the status that you want to edit, click more_horiz, and then click **Edit agent status**.

  4. For **Form Group Headline** , select the **Allow calls to breakthrough this agent status** checkbox.

  5. Click **Save**.




## Breakthrough for wrap-up

The breakthrough for wrap-up capability lets agents receive calls while they're in `Wrap-up` and `Wrap-up Exceeded` status. This lets agents answer high-priority calls immediately, even if they haven't completed wrap-up for a previous call. It also prevents agents from being unavailable for extended wrap-up periods.

When an agent accepts a breakthrough call while in `Wrap-up` and `Wrap-up Exceeded` status, they can switch between the call and the wrap-up screen. The caller is placed on hold when the agent switches to the wrap-up screen. Timers for the call and the wrap-up screen continue counting even when they're in the background. For more information, see Agent experience.

Breakthrough for wrap-up works regardless of whether disposition codes are configured as `Off`, `Optional`, or `Mandatory`. If your contact center allows multiple concurrent calls, a wrap-up session counts as one call against the limit.

To configure breakthrough for `Wrap-up` and `Wrap-up Exceeded` statuses, turn on agent status breakthrough and then allow breakthrough for the `Wrap-up` and `Wrap-up Exceeded` agent statuses. For more information, see Agent status breakthrough.

### Reporting

The following metrics are available in standard reporting:

  * **Call received in Wrap-up**. A call was offered to an agent in `Wrap-up` status.

  * **Call received in Wrap-up Exceeded**. A call was offered to an agent in `Wrap-up Exceeded` status.

  * **Call answered in Wrap-up**. An agent answered a call while in `Wrap-up` status.

  * **Call answered in Wrap-up Exceeded**. An agent answered a call while in `Wrap-up Exceeded` status.

  * **Call missed in Wrap-up**. An agent in `Wrap-up` status didn't answer a call.

  * **Call missed in Wrap-up Exceeded**. An agent in `Wrap-up Exceeded` status didn't answer a call.

  * **Call declined in Wrap-up**. An agent in `Wrap-up` declined a call.

  * **Call declined in Wrap-up exceeded**. An agent in `Wrap-up Exceeded` declined a call.




### Agent experience

If your administrator has configured breakthrough for `Wrap-up` and `Wrap-up Exceeded` statuses, you should expect to receive breakthrough calls when you're in these statuses. This section explains how breakthrough for wrap-up works.

#### Handle a call

Here's the workflow for handling a breakthrough call while you're in `Wrap-up` or `Wrap-up Exceeded` status:

  1. In the call adapter, a banner appears with an **Answer** button.

  2. Click **Answer**. The call connects, and the call screen appears. Your wrap-up notes and disposition codes are preserved.

**Note:** If auto answer is turned on, the call connects without the **Answer** button appearing.
  3. To switch back to the wrap-up screen, click ![Switch between call and wrap-up](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-switch.png)**Switch**. The call is put on hold, and the wrap-up screen appears.

  4. To switch back to the call, click ![Switch between call and wrap-up](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-switch.png)**Switch** again. You can switch between the call and the wrap-up screen until the call ends or you finish wrap-up.




You can follow a similar workflow using the agent desktop.

#### Decline a call

Here's the workflow for declining a breakthrough call while you're in `Wrap-up` or `Wrap-up Exceeded` status:

  1. In the call adapter, a banner appears with **Answer** and **Decline** buttons. (The **Decline** button appears only for direct calls.)

  2. Click **Decline**. The call doesn't connect and you can continue wrap-up.




If you don't click a button and let the call finish ringing, your contact center treats it as a missed call.

You can follow a similar workflow using the agent desktop.

#### Tips for agents

  * **Complete unfinished wrap-ups**. If you answer a call before you complete a wrap-up, you must return to the wrap-up later and complete any required fields.

  * **Use switching judiciously**. If you switch back to wrap-up while still on a call, be brief and return to the caller promptly.

  * **Watch for call banners in wrap-up**. If you see a call banner during wrap-up, you're expected to answer the call.




## Wrap-up exceeded status

Wrap-up Exceeded is a system-set status that lets you transition agents into a _Wrap-up Exceeded_ Status once they have gone beyond a wrap-up threshold time and have cleared all ongoing sessions. When an agents transitions to _Wrap-up Exceeded_ status, an agent-level notification appears.

For more information, see [Agent Statuses](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-status).

**Note:** This status is only available when disposition codes/ notes are enabled.

### Enable Wrap-up Exceeded

  1. In the CCAI Platform portal, go to **Settings Operation Management** > **Wrap-up**.

  2. Turn on the _Wrap-up Exceeded_ status.




### Agent Status Transition Examples

The following are common scenarios from the agent's perspective demonstrating how the _Wrap-up Exceeded_ status transitions based on the adapter activity.

The _Wrap-up Exceeded_ status is impacted by the following configuration considerations:

  * The _Wrap-up Exceeded_ status functions as a single configuration for calls and chats. Once enabled, agents can transition to _Wrap-up Exceeded_ after a call or chat session.

  * Once the agent exceeds wrap-up time on a communication, and have cleared all ongoing sessions, they transition into _Wrap-up Exceeded_ status. While in this status, or when _Wrap-up Exceeded_ is their next status, the agent cannot receive new communication and won't be able to manually change their next status. However, the agent is not taken away from the wrap-up screen and still can enter disposition codes/ notes. See **Scenarios 2** and **3** for examples.

  * Once the agent is in _Wrap-up Exceeded_ status and is not handling any calls or chats, they can switch to their next status and still can enter disposition codes/notes, depending on configuration.




**Scenario 1: Call Adapter is Active / Chat Adapter is off**

  1. An active call ends and goes to the wrap-up screen.

  2. The agent status moves from _In-call_ to _Wrap-up_.

  3. The agent exceeds the wrap-up time.

  4. The agent is moved to _Wrap-up Exceeded_ status, where the agent can still work on the wrap-up screen.

  5. The agent completes the wrap-up work in the notes and disposition screen, then clicks **Save**.

  6. The agent stays in the _Wrap-up Exceeded_ status and the wrap-up screen closes.

  7. The agent selects a new status.

  8. The agent successfully moves to the newly selected status.




**Scenario 2: Call Adapter is off / Chat Adapter is active**

  1. There are two active chats: one chat ends and goes to the wrap-up screen (Chat A), and the second chat (Chat B) is still ongoing.

  2. The agent status stays in _In-chat_ status (Chat A wrap-up is in progress, Chat B is in progress).

  3. The agent exceeds wrap-up time on Chat A.

  4. A Wrap-up Exceeded banner displays on the call and agent adapter since Chat A Wrap-up exceeded and Chat B is in progress. This alerts the agent that the next status is _Wrap-up Exceeded_.

  5. The agent stays in _In-chat_ status (the agent is still working on Chat B). The agent still can work on the wrap-up screen of Chat A.

  6. The agent finishes Chat B and goes to wrap-up for Chat B.

  7. The agent stays in the _In-chat_ status.

  8. The agent exceeds the wrap-up time on Chat B.

  9. The agent is moved to the _Wrap-up Exceeded_ status, where the agent can still work on the wrap-up for both chats (A and B). The agent still can't move into a new status while they are working on the wrap-up.

  10. The agent completes the wrap-up work and clicks **Save & Close** on both chats.

  11. The agent stays in _Wrap-up Exceeded_ status (no communications are active or in wrap-up state).

  12. The agent chooses a new status.

  13. The agent successfully moves to the newly selected status.




**Scenario 3: Call Adapter is active / Chat Adapter is active**

  1. There is an active call and an active chat. The agent finishes the call, and the chat is still in progress (active).

  2. The agent status changes from _In-call_ to _Wrap-up_ status.

  3. The agent exceeds call wrap-up time.

  4. The agent stays in _Wrap-up_ status because there is still an active chat in progress.

A Wrap-up Exceeded banner displays on the call and agent adapter, which alerts the agent that the next status is _Wrap-up Exceeded_.

  5. The agent finishes call wrap-up and clicks **Save** on the wrap-up screen.

  6. The agent moves from _Wrap-up_ status to _In-chat_ status, because there is still an active chat in progress.

  7. The agent finishes the chat wrap-up in the chat allotted wrap-up time.

  8. The agent moves from _In-chat_ status to _Wrap-up Exceeded_ status since the prior call wrap-up time was exceeded.

  9. The agent chooses a new status.

  10. The agent successfully moves to the newly selected status.




### Reporting

Wrap-up Exceeded can be found in the following standard reports:

**Agents & Teams**

  * Interactions Summary by Agent Report

    * Wrap-up Exceeded: (Count) The total number of times the agent goes into _Wrap-up Exceeded_ status.
  * Agent Activity Summary Report

    * Total Exceeded Wrap-up (Calls/Chats) - The total time the agent(s) was in _Wrap-up Exceeded_ status. This is calculated as the time from when the wrap-up timer elapses to when the agent submits the wrap-up.
  * Individual Call or Chat History Report

    * Wrap-up Exceeded: Indicates whether a wrap-up exceeded status occurred. This formats as a True or False.
  * Activity Timeline Report

    * _Wrap-up Exceeded_ appears as a status under **Activity log**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
