---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/contact-list/
title: Contact lists \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:11.974985+00:00
---

# Contact lists  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/contact-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Contact lists Stay organized with collections  Save and categorize content based on your preferences. 

A contact list is a collection of contact points that agents can use to start calls to end-users.

Here are the three types of contact lists:

  * **Global contact list** : the default contact list for your contact center. Every contact center has one global contact list and it can't be renamed or deleted. As a Contact Center AI Platform (CCAI Platform) administrator, you can create, edit, and remove contacts from the global contact list. You can make the global contact list available to any queue. You can also make the global contact list available to all agents, regardless of which queue they are assigned to. For more information, see Give agents access to the global contact list.

  * **Custom contact list** : a contact list that you can create, edit, and delete. You can assign a custom contact list to a queue or a team. This gives the agents that are assigned to the queue or team quick access to the contacts in the list. You can create as many custom contact lists as you need. For more information, see Manage contact lists.

  * **Personal contact list** : a contact list that an agent creates and which is available only to that agent. Agents can create personal contact lists only if you enable the capability. For more information, see [Create a personal contact list](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-agent-guide#create-personal-contact-list).




## Configure contact lists

This section explains how to configure contact list appearance and behavior.

### Configure contact list appearance in the agent adapter

To configure how contact lists appear in the agent adapter, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Call**. If you don't see the **Settings** menu, click menu **Menu** , and then click **Settings > Call**.

  2. Go to the **Contact Lists** pane.

  3. To display the global contact list to all agents in the agent adapter, select the **Access to the global contact list** checkbox. You can override this setting at the queue or team level.

  4. To display full SIP URI addresses in the agent adapter, select the **Display SIP URI address in Agent Adapter** checkbox.

  5. Click **Save Contact List**.




### Let agents create a personal contact list

To let agents create a personal contact list, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Call**. If you don't see the **Settings** menu, click menu **Menu** , and then click **Settings > Call**.

  2. Go to the **Contact Lists** pane, and then click the **Personal Contact List** toggle to the on position.

  3. Click **Save Contact List**.




### Create a custom role with contact list permissions

CCAI Platform roles have certain permissions by default. The following roles contact list permissions by default:

  * **Admin** : has permissions to create and edit custom contact lists and edit global contact lists.

  * **Agent** : has permissions to view the global contact list in the agent adapter (if the administrator gives access to the global contact list). For more information, see Give agents access to the global contact list.




You can create a custom role with contact list permissions. To do so, create a custom role as described in [CCAI Platform portal configuration](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent_team_configuration#configuration) while meeting these requirements:

  * On the **Add Role** page, select the **View** and **Edit** checkboxes for the **Settings | Call** permission. This grants the ability to create and edit custom contact lists and edit global contact lists.

  * On the **Add Role** page, select the **Edit** checkbox for the **Function | Agent** permission. This grants the ability to view the global contact list in the agent adapter (if the administrator has given access to the global contact list). For more information, see Give agents access to the global contact list.




## Manage contact lists

This section explains how to manage contact lists.

### Create a custom contact list

To create a custom contact list, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Call**. If you don't see the **Settings** menu, click menu **Menu** , and then click **Settings > Call**.

  2. Go to the **Contact Lists** pane, and then click **Contact list management**.

  3. Click **Create contact list**.

  4. In the **Contact list name** field, enter a name, and then click **Create**. Your new custom contact list appears in the **Contact list name** column.




After you a custom contact list, you can assign it to a queue or team. For more information, see Assign contact lists to queues and teams.

### Add a destination to a contact list

Destinations are the contact points used for making calls to end-users. Here are the two types of destination points:

  * **SIP URI address** : an address used in VoIP (Voice over Internet Protocol) communications. When you use a SIP URI address as a destination, you can configure data parameters to be passed when an agent makes an outbound call or transfers a call using the contact list. For information about configuring data parameters, see [Add a SIP URI address destination to a contact list](https://docs.cloud.google.com/contact-center/ccai-platform/docs/contact-list#add-sip-uri-address-destination).

  * **Phone number** : a phone number on the public switched telephone network (PSTN).




#### Add a SIP URI address destination to a contact list

To add a SIP URI address destination to the global contact list or a custom contact list, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Call**. If you don't see the **Settings** menu, click menu **Menu** , and then click **Settings > Call**.

  2. Go to the **Contact Lists** pane, and then click **Contact list management**.

  3. In the **Contact list name** column, click the contact list that you want to edit. This can be the global contact list or any custom contact list that you have created. For more information, see Create a custom contact list.

  4. Click **Add Destination**. The **Add Destination** dialog appears.

  5. In the **Destination Name** field, enter a name. Destination names must be unique within your CCAI Platform instance and are case sensitive.

  6. Select **SIP URI Address**.

  7. In the **SIP Destination URI** field, enter a SIP URI address. This typically follows one of these formats: `sip:username@domain.com` or `sip:username@ip_address`.

  8. Optional: Select the **Use SIP REFER when available** checkbox.

**Note:** SIP REFER is only available when using [Bring-Your-Own-Carrier (BYOC)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/byoc).
  9. Optional: To add data parameters to pass, click the **Pass Data Parameter** toggle to the on position.

  10. To automatically pass all inbound SIP headers to the outbound SIP destination, select the **Automatically Include and Pass all Inbound SIP Headers** checkbox. A row is added to the **Data parameters** table that represents this inbound SIP header pass-through. All inbound SIP headers are forwarded to the outbound SIP URI without requiring manual mapping.

  11. Click **Add Parameter**. The **Add Parameter** dialog appears.

  12. Do one of the following:

     * To create a fixed parameter, do the following:

       1. In the **Type** field, click **Fixed**.

       2. In the **Destination Field** field, enter the name of the data parameter to be passed to the target SIP address.

       3. In the **Destination Value** field, enter the value to be passed to the target SIP address. A preview of your data parameter appears in the **Preview** field.

       4. Click **Add Parameter**.

     * To create a dynamic parameter, do the following:

       1. In the **Type** field, click **Dynamic**.

       2. In the **Source** field, select the source type for your data parameter: either **SIP Header** or **Session Metadata**.

       3. In the **Incoming Field** field, do one of the following:

          * If you selected **SIP Header** in the previous step, enter the field name for the incoming SIP header.

          * If you selected **Session Metadata** in the previous step, select the type of session metadata that you want.

       4. In the **Destination Field** field, enter the name of the data parameter to be passed to the target SIP address. A preview of your data parameter appears in the **Preview** field.

       5. Click **Add Parameter**.

  13. For **Data Records** , select one or both checkboxes, depending on how you want the data parameter information to be recorded.

  14. Optional: Under **CRM record** , select the **Create CRM records for outbound calls to this contact** checkbox.

  15. Click **Add Destination**. Your destination appears in the **Destination** list.

  16. Click **Save Changes**.




#### Add a phone number destination to a contact list

To add a phone number destination to the global contact list or a custom contact list, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Call**. If you don't see the **Settings** menu, click menu **Menu** , and then click **Settings > Call**.

  2. Go to the **Contact Lists** pane, and then click **Contact list management**.

  3. Under **Contact list name** , click the contact list that you want to edit. This can be the global contact list or any custom contact list that you have created. For more information, see Create a custom contact list.

  4. Click **Add Destination**. The **Add Destination** dialog appears.

  5. In the **Destination Name** field, enter a name. Destination names must be unique within your CCAI Platform instance and are case sensitive.

  6. Click **Phone number** , and then enter a phone number in the **Destination Phone Number** field.

  7. Optional: Under **CRM record** , select the **Create CRM records for outbound calls to this contact** checkbox.

  8. Click **Add Destination**. Your destination appears in the **Destination** list.

  9. Click **Save Changes**.




### Edit or delete a destination in a contact list

To edit or delete a destination in the global contact list or a custom contact list, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Call**. If you don't see the **Settings** menu, click menu **Menu** , and then click **Settings > Call**.

  2. Go to the **Contact Lists** pane, and then click **Contact list management**.

  3. Under **Contact list name** , click the contact list that you want edit. This can be the global contact list or any custom contact list that you have created. For more information, see Create a custom contact list.

  4. Do one of the following:

     * To edit a destination, do the following:

       1. Next to the destination that you want to edit, click more_horiz **More** , and then click **Edit destination**.

       2. Under **Edit Destination** , make the edits that you want, and then click **Save**. A confirmation dialog appears.

       3. To continue, click **Save**.

     * To delete a destination, do the following:

       1. Next to the destination that you want to delete, click more_horiz **More** , and then click **Delete destination**. A confirmation dialog appears.

       2. To continue, click **Delete**.


**Note:** Editing or deleting a destination affects any queue or team that the destination is assigned to.

### Bulk import destinations to a contact list

  1. In the CCAI Platform portal, click **Settings > Call**. If you don't see the **Settings** menu, click menu **Menu** , and then click **Settings > Call**.

  2. Go to the **Contact Lists** pane, and then click **Contact list management**.

  3. Under **Contact list name** , click the contact list that you want edit. This can be the global contact list or any custom contact list that you have created. For more information, see Create a custom contact list.

  4. Click **Import Destinations**. The **Import Destination** page appears.

  5. Follow the instructions on the page, and then click **Process**.


**Note:** You can run only one bulk import operation at a time.

## Assign contact lists to queues and teams

You can assign custom contact lists to specific queues and teams. You can also give specific queues and teams access to the global contact list. These actions let you provide the right set of contacts to each of your queues and teams.

### Assign contact lists to a queue

To assign contact lists to a queue, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu** , and then click **Settings > Queue**.

  2. In the **IVR (Interactive Voice Response)** pane, click **Edit / View**.

  3. Click the queue that you want to edit.

  4. In the **Settings for My queue** pane, next to **Contact List** , click **Configure**.

  5. Under **Contact List** , select the custom contact list that you want to assign to your queue. For more information, see Create a custom contact list.

  6. To make the global contact list available to your queue, click the **Access to the global contact list** toggle to the on position.

  7. Click **Save**.


**Note:** Child queues inherit contact list settings from parent queues. You can edit the inherited settings in a child queue.

### Assign a custom contact list to a team

To assign contact lists to a team, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Users and Teams**. If you don't see the **Settings** menu, click menu **Menu** , and then click **Settings > Users and Teams**.

  2. Under **Teams** , next to the team that you want to edit, click edit **Edit**. The **Edit Team** dialog appears. For more information, see [Create users and teams](https://docs.cloud.google.com/contact-center/ccai-platform/docs/create-contact-center#users-and-teams).

  3. Under **Contact List** , select the custom contact list that you want to assign to your team. For more information, see Create a custom contact list.

  4. Click **Save**




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
