---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/salesforce-integration-guide/
title: Salesforce integration guide \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:43:54.868742+00:00
---

# Salesforce integration guide  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/salesforce-integration-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Salesforce integration guide Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to integrate Salesforce with Contact Center AI Platform (CCAI Platform).

## Configure account lookup and field mapping

You can configure your Salesforce integration to provide flexible account lookup using primary and secondary lookup objects. You can map fields in these lookup objects to fields in the call adapter, which helps agents identify customers or leads. These account lookups are available for both Sales Cloud and Service Cloud.

You can configure the following:

  * **Lookup objects** : Define lookup objects to find customer records for incoming and outgoing calls. Lookup objects can be for contact, account, or lead object types. You can define primary and secondary lookup objects. If the primary lookup doesn't return a match, the system uses the secondary object. This is helpful when a customer record exists in one object type but not another.

  * **Lookup fields** : Select phone number lookup fields for each lookup object. When an incoming call arrives, the system attempts to find a match between the incoming phone number and the lookup field to identify the customer.

  * **Call adapter display fields** : Select the field types that appear in the call adapter when multiple accounts or records are matched. Agents can use these fields to identify which match represents the customer they want. You can configure a second display field (or a third, for record display fields) to help distinguish between matches.




### Before you begin

Before you begin, [install Salesforce](https://docs.cloud.google.com/contact-center/ccai-platform/docs/salesforce-installation-guide).

### Procedure

To configure account lookup and field mapping, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **CRM** pane, for **SFDC Cloud Selection** , select **Service Cloud** or **Sales Cloud** , depending on which one you're configuring.

  3. To configure the default user, do the following. The default user is the instance administrator, who you can assign to CRM interactions where a specific agent hasn't been identified or assigned. For more information, see [Default administrator](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-default-admin).

     1. Select the **Use the admin user for all record creations/updates that can't be attributed to a specific agent** checkbox to make the instance administrator the default author of new or updated tickets created in CCAI Platform when a specific agent hasn't been assigned.

     2. Select the **Always use the admin user for all record creations/updates** checkbox to make the instance administrator the default author of all new or updated tickets.

  4. To configure the primary lookup object, go to the **Primary Lookup Object** section, and then do the following:

     1. To define the primary lookup object, do the following:

        1. In the **Object Type** list, select the lookup object type.

        2. Optional: In the **Record Types** field, select a record type.

        3. In the **Phone number lookup fields** list, select one or more phone number lookup fields. Select phone number types that identify different records in the lookup object. CCAI Platform looks for a match between the phone number of an incoming call and the phone number in this field (except for SDK-based sessions where SDK custom field matching is turned on).

        4. In the **Phone number primary field** field, select a phone number primary field. When CCAI Platform creates a new CRM account, it uses this field to store the end-user's phone number.

        5. To encrypt the phone number in the lookup field, select the **Phone number lookup field is encrypted** checkbox.

     2. In the **Phone Number Format** list, select the phone number format.

     3. To configure a custom lookup field for sessions originating from the web SDK or the mobile SDKs, do the following:

        1. Select the **Mobile / Web SDKs: lookup users by custom field for SDK sessions** checkbox.

        2. In the **Custom lookup field in CRM** list, select the custom lookup field.

     4. To configure the CRM account display fields in the call adapter, do the following:

        1. In the **Matched account display field** list, select the field from the lookup object that appears when matched account record(s) are displayed in the call adapter field.

        2. Optional: To display a second field, do the following:

           1. Select the **Display a second field** checkbox.

           2. In the **Second Display Field** list, select a field.

           3. For **Second field display position** , configure whether the second field appears before or after the matched account display field.

  5. Optional: To configure a secondary lookup object, do the following:

     1. Select the **Secondary Lookup Object** checkbox.

     2. Configure the secondary lookup object the same way you configured the primary lookup object, except you don't need to select a primary phone number field.

  6. To configure the CRM record display fields in the call adapter, do the following:

     1. In the **Matched record display field** list, select the field (from the matched record) to display in the call adapter field.

     2. Optional: To display a second field, do the following:

        1. Select the **Display a second field** checkbox.

        2. In the **Second Display Field** list, select a field.

     3. Optional: To display a third field, do the following:

        1. Select the **Display a third field** checkbox.

        2. In the **Third Display Field** list, select a field.

  7. Click **Save**.




## Salesforce: Agent status inheritance

The CCAI Platform agent status inheritance feature gives admins an ability to map CRM agent statuses to CCAI Platform agent status to be updated in real-time. By inheriting the CRM's agent status, it allows admins to drive agent statuses from their CRM to CCAI Platform.

Custom mapping allows for flexibility to match each organization's distinct processes and status settings. One example would be for agents handling email in the CRM to be configured to define the agent's status as 'unavailable' in CCAI Platform.

This also allows an agent to determine their status from just one place. When they update the Salesforce Omni-Channel widget, their CCAI Platform status is updated in real-time, providing a single mechanism for manually updated and system updated statues to be set.

### Installation and configuration requirements

  * **Salesforce and CCAI Platform access required**

    * CCAI Platform: Ask your internal CCAI Platform contact or administrator for a CCAI Platform user account with both adminstrator and agent roles assigned

      * The Admin role gives you access to developer settings

      * The Agent role gives you access to the agent adapter to utilize and test the agent status capability.

    * Salesforce account with administrative access

      * Assigned Omni-channel access

      * Your profile will need to be assigned to the CCAI Platform Call Center that has been set up in order to see the CCAI Platform agent adapter in Salesforce

  * **Your organization's CCAI Platform environment URL** and tenant or environment name will be used throughout the process and can be found in your CCAI Platform administrator portal link. You will have access when your CCAI Platform account is set up. The URL is `https://[my-instance-name].ccaiplatform.com`.

**Note:** There is a limit of 20 characters for instance names.



### Feature details

  * 1 to 1 Salesforce agent account to CCAI Platform agent account mapping is required

  * This feature allows for 1-way sync from the CRM -> CCAI Platform

  * If the status is changed in CCAI Platform, the CRM status will not be changed




### Status change behavior

  * CCAI Platform statuses protected from real-time CRM changes

    * If an agent is In-call, In-chat, or Wrap-up, the status inherited from the CRM will be applied once the call, chat, or wrap-up has ended.
  * Once enabled and configured, there are 3 ways an agent status can be updated

    * Agent updates status in the Adapter: existing agent status behavior

    * Agent selects next status during a live session: existing agent feature, described in Allow agents to set their next status while on a call or chat.

    * CRM sends agent status update

      * When Agent is not Offline in CCAI Platform, CRM status changes will be made in CCAI Platform based on status mapping

      * When Agent is in Offline in CCAI Platform, CRM status changes will be ignored

  * When the CRM status changes while on an active session/call

    * CCAI Platform treats this status change the same as the agent Next Status feature and when the session is complete, after Wrap-up, the next status is governed by the new CRM status

      * If the agent has defined their Next Status and a CRM status change request is also received, the agent's next status will be set to the latest received status



### Salesforce Configuration

#### Configure omni-channel

_If your org has already configured Omni-Channel, skip this section._

This supplemental information should be used in conjunction with Salesforce documentation. We will guide you to configure the minimal Omni-Channel settings to be able to use the CCAI Platform Agent Status Inheritance App.

To enable omni-channel settings, follow these steps:

  1. Sign in to Salesforce as an Administrator.

  2. From **Setup** enter **omni** in the Quick Find box, then select **Omni-Channel Settings.**

  3. Select **Enable Omni-Channel**.

  4. Click **Save**.




#### Add presence statuses

The Presence statuses should match those used in the CCAI Platform Portal. If Statuses are already set up in the Admin Portal, make sure the statuses are all entered here as well.

  1. From **Setup** , enter **Presence Statuses** in the Quick Find box, then select **Presence Statuses** under **Omni-Channel**.

  2. Click **New.**

  3. In the next screen, you can add a status. For example type "Available For Generico" for **Status Name** and this will fill automatically "Available_For_Generico" for **Developer Name**.

  4. Repeat Step 3 according to your needs. For example you can create "Available For Email", "Busy", "Meal" etc for the Presence Statuses.




#### Add omni-channel

The steps required to implement omni-channel depend on the Salesforce version.

##### Salesforce Classic

_If you are using Lightning only, skip this step._

  1. From **Setup** , enter **App** in the Quick Find box, then select **Apps** under **Create.**

  2. Click the **Edit** button left of Sample Console (You may have a different name).

  3. In the Edit screen, find the **Choose Console Components** section.

  4. Select **Omni-Channel** in the **Available Items** dropdown.

  5. Click **Add** then **Omni-Channel** will appear in the **Selected Items** dropdown.

  6. Click **Save** at the bottom of the screen.




##### Salesforce Lightning

_If you are using Classic only, skip this step._

  1. If you are currently in Classic, click **Switch to Lightning Experience.**

  2. Click the gear icon, then click **Setup** in the upper right area of the Lightning screen.

  3. From **Setup** , enter **App** in the Quick Find box, then select **App Manager** under **Apps.**

  4. Click the downward arrow icon in the upper-right of Service Console (You may have a different name).

  5. Click **Edit**.

  6. Click **Utility Items** in the **Lightning App Builder** screen.

  7. Click **Add Utility Item** and select **Omni-Channel**.

  8. Click **Save**.

  9. Click **Back** in the upper right corner of the screen.




#### Grant users access to service presence statuses

In order for a Service Presence Status to be available to a User, access for each status needs to be granted to each applicable Profile/Permission Set. If a Profile/Permission set does not have access to a certain Service Presence Status, then that status will not be available/visible in the Omni-Channel widget for the assigned users.

Please reference [Give Users Access to Presence Statuses with Profiles](https://help.salesforce.com/articleView?id=service_presence_give_access_to_statuses_through_profiles.htm&type=5) and [Give Users Access to Presence Statuses with Permission Sets](https://help.salesforce.com/articleView?id=service_presence_give_access_to_statuses_through_permission_sets.htm&type=5) from Salesforce. The below steps are the simplified steps for giving access with Profiles.

  1. From **Setup** , enter **Users** in the Quick Find box, then select **Profiles** under **Manage Users**.

  2. Click a Profile name in the main section that you want grant access to Service Presence Status.

  3. Find **Enabled Service Presence Status Access** and click **Edit**.

  4. In the edit screen, select items in the **Available Service Presence Statuses** dropdown and click **Add**.

  5. Click **Save**.

  6. Repeat the steps 3 through 6 for each profile that you want to grant access to Service Presence Status.




#### Verify Omni-Channel

##### Salesforce Classic Console

_If you are using Lightning only, skip this step._

  1. If you are in **Setup** , click **Back to Sample Console**.

  2. Click **Omni-Channel**.

  3. Click the **Offline** link in the Omni-Channel widget.

  4. Select one of Service Presence Status and see if you can change the status.




##### Salesforce Lightning

_If you are using Classic only, skip this step._

  1. In the bottom-left area of the Console screen, click the **Omni-Channel** button.

  2. Click **Offline** link in the Omni-Channel widget.

  3. Select one of Service Presence Status and see if you can change the status.




Omni-Channel should now be enabled in your Salesforce org, allowing you to use Omni-Channel in your console.

#### Remote site settings

Configure the remote site settings for the CCAI Platform Agent Status Inheritance App to be able to send data from Salesforce to CCAI Platform.

  1. From **Setup** , enter **remote** in the Quick Find box, then select **Remote Site Settings** under **Security Controls**.

  2. Click **New Remote Site**.

  3. In the next screen input **Remote Site Name** and **Remote Site URL.** Ex. Use **CCAI Platform** for **Remote Site Name**. Input your CCAI Platform domain for **Remote Site URL.**




### CCAI Platform configuration

#### Establish admin tokens

Configure one or more Salesforce Admin Tokens in the CCAI Platform administrator portal so that the administrator portal can fetch your Salesforce Omni-Channel Service Presence Statuses. For more information, see [CRM default administrator](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-default-admin).

  1. In the CCAI Platform portal, go to **Settings** > **Developer Settings**

> **Salesforce Admin Token**.

  2. Click **Link New User**.

**Note:** If possible, it's best to use a Salesforce Admin account that is not tied to a specific user. Individual user accounts are prone to being disabled without understanding the underlying connections.
  3. In the oAuth popup, sign in as your Salesforce administrator and allow the oAuth request

  4. You will see your administrator user is linked in the **Connected Admin Users** section.




#### Enable Status Mapping

  1. From the Admin Portal, go to Settings > **Developer Settings** > **Salesforce Omnichannel Agent Status Inheritance**.

  2. Toggle the feature setting **On**.




#### Manage Status Mapping

Salesforce Statuses will be fetched from your Salesforce org automatically. If you don't see SFDC statuses please check the Establish Admin Token/s step and Configure Omni-Channel. Any Salesforce statuses that are not mapped will result in an error

  1. Sign in to the CCAI Platform portal, go to **Settings** > **Developer Settings**

> **Salesforce Omnichannel Agent Status Inheritance**.

  2. Click **Manage** in **Status Mapping.**

  3. In the popup, select a preferred CCAI Platform Status for each Salesforce Status.




#### Gather Company Key and Secret

  1. Sign in to the CCAI Platform portal, go to **Settings** > **Developer Settings**

> **Company Key & Secret Code.**

  2. Gather the **Company Key** and **Company Secret Code.**




#### Identify your connected app name

  1. From Salesforce, go to **Setup** , enter **app** in the Quick Find box, then select **Connected Apps** under **Manage Apps**.

  2. Identify your CCAI Platform Connected App name.




#### Install the CCAI Platform Agent Status Inheritance App

  1. Paste the installation link in the browser's url bar: https://login.salesforce.com/packaging/installPackage.apexp?p0=04t6g000003Rzxv

  2. Select **Install for all users**.

  3. After the installation is complete click **Done**.

For longer installations, you will get a notification email after the installation is complete.




#### Configure the app

  1. From **Setup** , enter **package** in the Quick Find box, then select **Installed Packages**.

  2. Click **Configure** left of the UJET_App_Status.

  3. In the new window, click **Add New Configuration**.

  4. In the configuration screen, select **Organization** as **Setup Owner**.

  5. Fill the values for **Company Key** , **Company Secret, Tenant name** and **Connected App name** you have copied in the previous steps.

  6. Check **Enable Agent Status Inheritance**.

  7. Fill the value in CCAI Platform URL you have copied in the **step 6 Copy settings value from CCAI Platform Admin Portal**.

  8. Click **Save CCAI Platform Configuration**.

  9. Close the window.




#### Verify the Agent Status Inheritance App is Working

  1. Change Omni-Channel status in your console.

  2. Confirm CCAI Platform status changes according to the mapping setting in the Admin Portal.




## Salesforce: CCAI Platform session object installation & configuration

The CCAI Platform session object provides a convenient, optimized, custom object, in which all session data will be stored. All session data, including associated files like voice recordings, chat transcripts, and media files uploaded by the end-user, are included within the related CCAI Platform Session object. This object is then related to the appropriate case or directly to a configured Account object.

Do the following actions and steps in order.

### Install the CCAI Platform Salesforce package

Install version 1.17 or later of the CCAI Platform Salesforce package.

For more information, see the [Salesforce installation guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/salesforce-installation-guide).

### Enable the CCAI Platform Session

To enable the CCAI Platform session, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **CRM Record Creation Details** pane.

  3. For **Session Data** , in the **Map data to** list, select **UJET session**.

  4. Click **Save General**.




For more information, see [Salesforce - CCAI Platform session mapping to case or account objects (person account, contact, lead)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/salesforce-integration-guide#salesforce-session-mapping-to-case-or-account-objects).

### Salesforce configuration

Steps to configure in Salesforce:

#### Step 1: Configure and enable Default Admin user

Define a CRM admin user to represent the default user for all CRM actions and events where a specific agent has not been identified or assigned. If this feature is not used, CCAI Platform will randomly assign the ticket or case to any users.

For more information, see [CRM default administrator](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-default-admin).

#### Step 2: Update Object Settings

  1. From Salesforce Setup, navigate to **Permission Sets.**

  2. Locate and select the **CCAI Platform Agent Clone** permission set (this may have a different name in your settings).

  3. Select **Object Settings.**

  4. Locate the following Permissions:

\- CCAI Platform Actions

\- CCAI Platform Sessions

\- CCAI Platform Transfers

  5. Click on the **CCAI Platform Actions** object.

If you are using the Default Admin token from Step 1 above, agents do not need create, edit, or view all permissions. If you are not using the Default Admin user, assign all permission for proper access and object creation.

If using the Default Admin user, click the **CCAI Platform Actions** object and enable **Read** permission.

If not using the Default Admin user, click the **CCAI Platform Actions** object and enable**Read** ,**Create** ,**Edit** , and**View All** access, then click**Save.**

  6. **Repeat this step for CCAI Platform Sessions and CCAI Platform Transfers.**




#### Step 3: Update Case or Account Object Page Layout

To see the CCAI Platform Session object, the Case or Account object Page Layout needs to be updated.

_Follow the same steps for the Account object you are using if not using Case._

  1. From Salesforce Setup, navigate to **Object Manager** > **Case** OR your configured **Account object**.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc0220b30.png)

  2. Click **Case** /Account object **Page Layouts** on the left.

  3. Select the Page layout used by CCAI Platform users.

  4. Locate CCAI Platform Sessions under **Related Lists** and drag the CCAI Platform Session object to where you want it to display in the Layout page.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc02260e2.png)

  5. Click **Save** at the top of the page.




#### Step 4: Optional additional step required for Lightning configuration

If using **Lightning** , follow these steps to create a new Lightning Record Page or update a current one.

  1. From Salesforce Setup, go to **Setup** > **Object Manager** > **Case** > **Lightning Record Page**.

  2. Click **New.**

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc022b879.png)

  3. Click **Record Page** , then **Next.**

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc02311d5.png)

  4. Create a **label** , and select **Case** as the object, then click **Next.**

  5. Choose a page template and click **Finish**.

  6. Include the component with the CCAI Platform Session object. In the following scenario, it was added to the "Related List" component.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc0251391.png)

  7. Click **Save**.

  8. Click **Activate**.

  9. Follow the Salesforce setup flow to assign the page to the application you are using in Lightning.




### CCAI Platform Portal configuration

  1. In the CCAI Platform Portal, go to **Settings** > **Operation Management**.

  2. Scroll to **Configure ticket creation details** and select the desired behaviors.

  3. If using Cases, go to **Ticket title** and configure the title of the Case as they are created.




## CCAI Platform custom session object for Salesforce configuration

The CCAI Platform Custom Session Object provides a convenient, optimized, custom CCAI Platform Session object, in which **all** session data will be stored in a **session object**. When enabled, instead of storing session data in the Activities object via multiple entries, all session data, including associated files, for example, voice recordings, chat transcripts, and media files uploaded by the end user are included within the CCAI Platform session object. This object is then attached to the appropriate case (or optionally directly to an Account object.

### Session object

The session object is an object for call or chat sessions and can be made available to Salesforce.

### Admin configuration

  1. In order for the CCAI Platform session object option to be available in the admin UI, CCAI Platform package 1.16 or higher, needs to be installed in Salesforce.

For more information, see [Salesforce installation guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/salesforce-installation-guide).

  2. Go to **Settings** > **Developer Settings** > **CRM** > **Salesforce** > **Session Data**.

  3. In the dropdown, set the option to **Map data** to **CCAI Platform Session**.




### Salesforce updates

Updates are needed periodically to the installation and configuration of Salesforce.

#### CCAI Platform Salesforce package upgrade

An upgrade to CCAI Platform's Salesforce package 1.16, or later is required.

  * V 1.16 - supporting sessions, transfers, actions, files

URL: [https://login.salesforce.com/packaging/installPackage.apexp?p0=04t4M000000syZQ&isdtp=p1](https://login.salesforce.com/packaging/installPackage.apexp?p0=04t4M000000syZQ&isdtp=p1)

  * V 1.17 - added Email field in Account object (UJET__Email__c)

URL: [https://login.salesforce.com/packaging/installPackage.apexp?p0=04t4M000000kkWd&isdtp=p1](https://login.salesforce.com/packaging/installPackage.apexp?p0=04t4M000000kkWd&isdtp=p1)




#### Salesforce configuration updates

The following configuration changes are required in Salesforce.

##### Step 1: Update object settings

  1. From Salesforce Setup, navigate to **Object Manager** > **Permission Sets**

> **Object Sessions**.

  2. Locate and select the **CCAI Platform Agent** permission set (this may have a different name in your settings).

  3. Select **Object Settings.**

![Salesforce object settings page](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc037c24a.png)

  4. Update the object settings to include for:

-CCAI Platform Actions

-CCAI Platform Sessions

-CCAI Platform Transfers (**Note** : Make sure to update all three objects.)

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc0381db2.png)

  5. Click on the Agent Actions object and enable **Read** , **Create** , **Edit** , and **View All** access, then click **Save.**

  6. Repeat this step for CCAI Platform Sessions and CCAI Platform Transfers.




##### Step 2: Update case page layout

  1. From Salesforce Setup, navigate to Case Page Layout section (this path varies for Classic and Lightning)

  2. Select the Case layouts used by CCAI Platform users.

  3. Locate CCAI Platform Sessions under Related Lists and drag the CCAI Platform Session object to where you want it to display in the Case Layout page.

  4. Click **Save** at the top of the page.




##### Step 3: Optional additional step required for Lightning configuration

If using **Lightning** , follow these steps to create a new Lightning Record Page or update a current one.

  1. From Salesforce Setup, go to Setup > Object Manager > Case > Lightning Record Page.

  2. Click **New.**

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc022b879.png)

  3. Click **Record Page** , then **Next**.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc02311d5.png)

  4. Create a **label** , and select **Case** as the object, then click **Next.**

  5. Choose a page template and click **Finish**.

  6. Include the component with the CCAI Platform session object. In the following scenario it was added to the **Related List** component.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc0251391.png)

  7. Click **Save**.

  8. Click **Activate**.

  9. Follow the Salesforce setup flow to assign the page to the application you are using in Lightning.




## Salesforce + CCAI Platform rules and behaviors

Salesforce is a powerful CRM platform with endless customizations possible. CCAI Platform has a specific set of interactions that are either performed by default or can be customized from various settings in the Admin Portal.

### Case creation

With standard configuration, using cases as the record type:

  * When a **Mobile or Web SDK call/chat** comes in, CCAI Platform:

    * Creates a case in Salesforce.

    * Assigns the case to the agent.

    * Includes any information available (i.e. Mobile user info + diagnostic data, Web user info, etc).

  * When an **IVR call** is answered by an agent, CCAI Platform:

    * Creates a case in Salesforce.

    * Assigns the case to the agent. In Salesforce, there is the concept of an object owner. By default, an object will assign to who creates a new object. For a case object, when an agent picks up a call, CCAI Platform will change the object owner to the agent who picked up the call.

    * Includes any information available (i.e. Name, menu selection, caller's phone number).

  * When an **outbound call** is placed using the agent adapter, CCAI Platform creates a new case in Salesforce.

  * When a user **calls** in but abandons the call, CCAI Platform creates a case in Salesforce.

  * When a caller calls and the call fails due to the agent canceling the call (ag_canceled), a case is created but not assigned to the agent who canceled the call.

  * When a caller leaves a **voicemail** , CCAI Platform creates a voicemail case in Salesforce even if there is an Open status case from the same customer.

    * The voicemail case can be reused by a new IVR call or outbound call.



### Case updates

All case updates will be viewable to the agent on the call/chat and if they were previously on the call and transferred the call/chat.

#### Appending calls or chats to cases

  * When there is an **inbound call/chat** from the same contact, same menu selection, and same channel as the most recent case for that contact is in New, Escalated or Working, CCAI Platform appends the call/chat to the open case as a new task on the case.

    * This can be disabled in [General Operation Management Settings](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-record-creation).
  * When an **outbound call** is placed using click-to-call from the details section of the case (not from the sidebar), if the most recent case with that user is in Open, Working, or Escalated status, CCAI Platform will append the outbound call to the existing case for follow-up cases.

  * When an agent uses the **Hang up and call back** option from the widget, CCAI Platform appends the call to the open case.

  * When a call is less than 10 seconds, and the agent uses the **Callback** button, CCAI Platform appends the call to the open case.




#### Case owner and assignment

  * After the [default administrator](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-default-admin) is enabled, the default administrator is used as the owner for the following:

    * **Ticket/case** and **contact** creation when a new chat is initiated before an agent is assigned to the chat

    * Voicemail tickets/cases before receiving a callback call

    * Call ticket/cases for abandoned calls (if enabled)

**Note:** If the default user is not configured, CCAI Platform uses a random Agent
  * When a **call/chat is transferred:**

    * CCAI Platform assigns the case to the agent who the call is transferred to.

    * A new task is added to the case about the transfer.




#### Attachments and actions logged

  * When an **inbound/outboundcall** ends, CCAI Platform updates the case with the call recording file when call recording is enabled.

  * When a **SmartAction** is completed, CCAI Platform updates the case with action results and attachments.

  * When a **SmartAction** fails due to an error on the user's side (i.e. fingerprint access not enabled), CCAI Platform updates the case with the error message.

  * When the company uses **custom field mapping** (set up from the Admin portal), the data coming in from Mobile/Web SDK will be placed in the designated field in the CRM.

  * When the end-user rates an **IVR** or **Mobile call/chat** , CCAI Platform adds a rating score to the case.

  * When an agent **reads/dismiss/calls back from voicemail** , CCAI Platform updates the case.




### Contact creation

  * When an **IVR call** comes in with a new phone number, CCAI Platform creates a contact in Salesforce.

  * When a new app user(new identifier) starts the **CCAI Platform Mobile SDK** , CCAI Platform creates a contact in Salesforce.

  * When IVR caller's number is blocked, CCAI Platform will create Unknown user contact in Salesforce.

  * When there are multiple contacts with the same phone number, CCAI Platform will display the contact selection screen in the Agent widget where the agent can choose which contact to use or choose to create a new contact.




### Contact update

  * If the contact was just created from the current call:

    * For **IVR** calls, the Contact Owner field is updated to the assigned agent.

    * For contacts created from Mobile, Callback, and Voicemail calls, the Default Admin token is used if the setup is complete, or if default admin token is not available CCAI Platform will use a random agent token. For more information about the default admin user, see [CRM default administrator](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-default-admin).




### Call and chat routing

  * **User segment DAP** : CCAI Platform will search for a contact using phone number (IVR) or email address (Mobile) or custom field (Mobile) from Salesforce to match settings in the queue and directly route call or chat to the queue.

  * **APEX REST DAP** : Admin can set up APEX REST endpoint as API Direct Access Point (DAP) endpoint. For more information, see API Direct Access Point - Salesforce REST API.




### Outbound click to call

When viewing a Contact in Salesforce you can click on the Contact's Phone Number to start an Outbound Call.

When clicked from within the case details, depending on settings, the call will append if the case is not closed.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc038742c.png)

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc03a5fde.png)

## Salesforce: CCAI Platform session mapping to case or account objects (person account, contact, lead)

When a call or chat takes place, the associated data needs to be made available in your CRM and CCAI Platform offers flexibility in how the call/chat session data to is attached to Salesforce data objects.

The following configuration options are available:

  * **Account Lookup:** ability to perform account lookup against any Salesforce end-user based account object

  * **Session Data Location** : map session data to an Account object (Contact, Person Account, Account, Lead, or Task rather than a Case.

  * **No Case:** ability to connect the CCAI Platform Custom Session object directly to any Salesforce account object, bypassing the need to create a case




This builds on two related features:

  * Option to look-up end users in Person Account object (instead of Contact (_default_))

  * Option to leverage our CCAI Platform Session Object which stores all assets and data related to a single session in optimized CCAI Platform Session object




### Configuration availability requirements

The configuration options for Account Lookup and Session Data are only available if the following conditions are met:

  * Account Lookup configuration

To configure custom account lookup settings, the following is required:

**Logged in Agent** \- at least one agent needs to be logged into a CCAI Platform adapter in Salesforce. This is required to ensure there is an active token enabling CCAI Platform to access Salesforce data during the admin session.

  * Session Data configuration

To configure session data mapping options like selecting the CCAI Platform Session object, the following is required:

    * **Logged in Agent** \- at least one agent needs to be logged into a CCAI Platform adapter in Salesforce. This is required to ensure there is an active token enabling CCAI Platform to access Salesforce data during the admin session.

    * CCAI Platform Salesforce package version 1.16 (or newer) is installed in your Salesforce instance. For Salesforce Lead object support, package version 1.18 is required, but version 1.20 or higher is recommended.




If the configuration access requirements for one or both of these settings are not met, the CCAI Platform Portal UI to configure **Account Lookup** and **Session Data** will be inactive as shown below:

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc03aae4f.png)

### CCAI Platform portal configuration

#### Account lookup and session data mapping

  1. In the CCAI Platform portal, go to **Settings** > **Developer Settings** and select **Salesforce**.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc03afc85.png)

  2. Select an **Object Type** :

Contact

Person Account

Account

Lead

  3. Select a **Record Type**. These options vary based on the selected **Object Type** above.

  4. Select the specific field CCAI Platform should match the end-user phone number against from the **Phone number lookup field** option. CCAI Platform will fetch all "phone type" fields from the selected account object above.

  5. Mark the SDK Custom Lookup field to activate the option to pass a custom user identifier (UID) to CCAI Platform for end user lookup. Available for mobile and web SDKs.

**Note:** this is an existing feature that has been relocated and relabeled from the previous setting labeled 'Custom Field Matching'.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc03b4aa4.png)

  6. Select a location for CCAI Platform to organize and attach core session data (call/chat ID, session duration, end-user file uploads, etc.) to Salesforce.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc03b97fb.png)

     1. **Activity Object** \- the session data is stored within the Salesforce Activity object. Records will be created with this option.

     2. **CCAI Platform Session** \- all session data is optimally organized and collected in CCAI Platform Session Object.

Offers an option to directly attach the CCAI Platform session object to a Salesforce Account, Contact, or Lead object based on your selection in step 2.

Based on your selection in step 2, if you select Contact or Lead, the CCAI Platform session object is directly attached to a Task object, then the Task is attached to the Contact or Lead object. If you select Person Accounts or Accounts, The CCAI Platform Session is attached to a Task Object, then the CCAI Platform Session is attached to the Account or Person Account.

     3. **Attach to Records** \- creates a CRM records and attaches to the session object.

**No Records** \- if the CCAI Platform Session object is directly attached to a Salesforce Account object or Task object, no records will be created. This option is only available when mapping to the CCAI Platform Session object.




### Required Salesforce permission sets configuration

Account object and field permission changes are required.

  1. As a Salesforce Admin, go to the **Setup** page.

  2. Using the search field, go to the **Permission Set** settings page.

  3. You will see something similar to UJET_Agent permission set.

![A list of permissions by role is shown.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc03bea9c.png)

  4. Select the UJET_Agent Permission set.

![Select the UJET_Agent Permissions listing.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc03e0974.png)

  5. Account permissions should be set to enable: Read, Create, Edit, View All. If they don't, add the Read, Create, Edit, and View All permissions to the Account object.

**Note:** this configuration should be the same as the permissions already set for the Case and Contacts objects.

![Accounts and their level of permissions or access is shown.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc03e6460.png)

  6. Scroll or use the drop-down sorting tools to view or change to the Field Permission section and enable Read and Edit access for **Type**.

![A scrollable list of Field Permissions and whether they have Read or Edit access is shown.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc03eb6b7.png)

  7. Click **Save** to complete the changes and update the Permission set.




## CCAI Platform custom session object for Salesforce

The CCAI Platform Custom Session Object provides a convenient, optimized, custom CCAI Platform Session object, in which **all** session data will be stored in a **session object**. When enabled, instead of storing session data in the Activities object using multiple entries, all session data, including associated files, for example voice recordings, chat transcripts, and media files uploaded by the end user, are included within the new CCAI Platform session object. This object is then attached to the appropriate case (or optionally directly to an Account object.

For Admin Config to map data to the session object see Salesforce: CCAI Platform Session Object Installation and Configuration.

### Session object details

When the session object is enabled for data mapping:

  * All CCAI Platform session data will be stored in the new CCAI Platform session object, instead of the default _Activity_ object.

  * The CCAI Platform session object will be attached directly to the case.

  * A case can have multiple CCAI Platform sessions attached to it, if the configuration and end user sessions logically align for that scenario to occur; for example the consumer calls back for the same issue while the underlying case is still open.




### Session object data hierarchy

The session object is organized as follows:

**Session(s) list** \- the list of session(s) attached to a case*.

  * ** **Session Detail** \- presents the core session object details**

    * **Core session fields** and lists any associated transfers and files.

    * **File list** \- any files that have been uploaded / created as part of the session

  * **Session detail** \- presents the core session object details; i.e.




**Sample UI of multiple CCAI Platform sessions attached to a case**

**Note:** it is possible to define how the sessions list is to be ordered (e.g. latest on top / bottom) using Salesforce configuration options for how to display the CCAI Platform session object.

#### Session overview

After opening a session, the following view will be provided, listing all associated CCAI Platform session actions, attached files, and transfers.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc03f07e7.png)

#### Session details

The available dataset for sessions includes the following fields:

  * Call/Chat ID: CCAI Platform call or chat ID

  * Created at: when the call, chat was created

  * Ended at: when the call, chat was ended

  * Channel: call or chat type (for example, Mobile, Web).

  * Session type: call or chat

  * Call duration: duration of session from start to end

  * Queued at: time session entered the queue

  * Assigned at: time session was assigned to agent

  * Wait: total wait duration in queue before being assigned to an agent for the session

  * Hold Duration: length of hold time does not include wait time (calls only)

  * Answer Type: indicates whether session was auto (0) or manually (1) answered

  * Fail reason: reason why a session "failed" and details.

  * Feedback: when enabled, shows customer feedback collected during session on record

  * Case: case the session object is attached to

  * Initial menu selected: initial queue menu selected

  * Materialized menu path: the selected path leading to connection with the agent

  * Language: the language used or selected for the session

  * Outbound phone number -- applicable outbound phone number

  * Status: status of the session

  * Total transfers: number of total transfers during the session




#### Files

All media files associated with the session object are attached as **files** to the session object. This includes:

  * Call recordings

  * Chat history

  * Mobile SDK based diagnostic package

  * Media files sent by end users




##### UI examples

**File List UI** \- sample for session file list for call recording

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc04228e2.png)

**File Detail UI** \- for example, image upload by the consumer.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc042762d.png)

#### Session actions

Reflects session activities:

  * **Started call**

  * Custom data from customer has arrived

  * Finished call

  * Customer rating feedback received




Example: Session action detail UI - end user feedback

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc042cc25.png)

#### Transfers

Any transfers associated with the session are listed in this section. If you are not already using API data, the Transfer details section introduces a new set of information about the call. Transfer details represent a complete account of each transfer and are defined using the fields:

  * Transfer name: the name of the transfer.

  * Transfer ID: the unique ID of the transfer.

  * Agent transferred from: agent initiating the session transfer

  * Agent transferred to: agent receiving the session transfer

  * Created at: time transfer was created

  * Fail reason: reason for failure of session transfer

  * Menu transferred from: the originating queue menu from which transfer was initiated

  * Menu transferred to: queue menu the session was transferred to

  * Session: CCAI Platform session ID

  * Status: status of transfer

  * Transfer from materialized path: the materialized path transfer was originated from

  * Transfer to materialized path: the materialized path the session was transferred to




## CCAI Platform agent experience in Salesforce Lightning

Provide expected CCAI Platform behaviour in Salesforce Lightning to Admins and Agents, specifically when connecting to the Activity object rather than the CCAI Platform Session object.

### Requirements

  * Salesforce Service Cloud licenses

  * Salesforce Service Console Lightning apps

  * Updated Salesforce instance

  * Salesforce Lightning enabled

  * CCAI Platform 1.15 or above




### The agent adapter

The agent adapter will show on the bottom left of the Service Console Lightning (or Sales Console Lightning) apps, in the utility bar. If you don't see the CCAI Platform phone adapter, contact your company's Salesforce or IT team.

When making or receiving calls or chats, the CCAI Platform integration will automatically pop the Salesforce case.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc0431f40.png)

#### Other notes

  * The widget can be minimized while in use.

  * The case will vary dependent on your Salesforce settings.

  * Case will auto-assign to the agent answering the ticket.

  * A corresponding Task is automatically created and related to the Case




### Standard data

Immediately upon case creation, CCAI Platform will provide standard data into the Description field of the Case. This includes the Call ID, Language, and Inbound Menu selection.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc0437636.png)

### Custom data

If using Custom Data from the CCAI Platform SDKs, the information will create a task related to the case Dependent upon your Salesforce settings, this will show in the publisher feed.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc043c76c.png)

## CCAI Platform agent experience in Salesforce Classic

The following sections outline expected behaviors between Salesforce Classic and CCAI Platform.

### Requirements

  * Salesforce Service Cloud licenses

  * Salesforce Service Console apps

  * Updated Salesforce instance

  * CCAI Platform 1.13 or later




### Agent adapter

The agent adapter will show on the bottom right of the Service Console (or Sales Console) apps.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc04424b3.png)

When making or receiving calls or chats, the CCAI Platform integration will automatically pop the Salesforce case.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc044889b.png)

#### Other notes

  * The adapter can be minimized while in use.

  * The case will vary dependent on your Salesforce settings.

  * Case will auto-assign to the agent answering the ticket.

  * A corresponding Task is automatically created and related to the Case




### Standard data

Immediately upon case creation, CCAI Platform will provide standard data into the Description field of the Case. This includes the Call ID, Language, and Inbound Menu selection.

#### Custom data

If using Custom Data from the CCAI Platform SDKs, the information will create a task related to the case Dependent upon your Salesforce settings, this will show in the publisher feed.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc044de1d.png)

## Salesforce: CCAI Platform session object technical details

The CCAI Platform Custom Session Object provides a convenient, optimized, custom CCAI Platform Session object, in which all call or chat session data will be stored. When enabled, instead of storing session data in the Activities object using multiple entries, all session data, including associated files like voice recordings, chat transcripts, and media files uploaded by the end user, are included within the CCAI Platform session object. This object is then related to the appropriate case or directly to a configured Account object.

For more information, see to [Salesforce: CCAI Platform session mapping to case or account objects (person account, contact, lead)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/salesforce-integration-guide#salesforce-session-mapping-to-case-or-account-objects).

### CCAI Platform session object

When the session object is enabled:

  * All CCAI Platform session data will be stored in the new CCAI Platform session object, instead of the current default 'Activity' object.

  * The CCAI Platform session object will be related directly to the Case or Account object as a single relationship for each session.

  * Settings for 'Abandoned call case creation' configured in **Settings** > **Operation Management** will be respected. A session object won't be created if the "create tickets for abandoned calls/chats" setting is disabled.

  * It is possible for a case or account object to have multiple CCAI Platform sessions related to it if the CCAI Platform configuration and end-user sessions logically align for that scenario to occur. Example: end-user calls back for the same issue while the underlying case is still open.




_Sample UI of multiple CCAI Platform sessions related to a case_

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc045353b.png)

#### CCAI Platform session object data hierarchy

The session object is organized as follows:

  * **Session(s) related list:** the list of session(s) related to a case or account object

    * **Session Detail** : presents the core session object details

    * **Core session fields:** lists any associated transfers and files

    * **File list:** any files that have been uploaded or created as part of the session

      * **File detail:** all details about a file, including access to file itself
    * **Actions:** a list of actions that occurred during the session

      * **Action detail:** additional info about a specific action
    * **Transfers:** complete list of transfers that occurred during the session

      * **Transfer detail:** displays all fields and data associated with a single transfer events



#### CCAI Platform session overview

After opening a session, the following view will be provided, listing all associated CCAI Platform session actions, attached files, and transfers.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc03f07e7.png)

#### CCAI Platform session data set fields

The available dataset for sessions includes the following fields. See Data Dictionary for more detailed definitions.

  * **Call/Chat ID** : The unique ID of the interaction.

  * **Created at** : When the call or chat was created.

  * **Ended at** : When the call, chat was ended.

  * **Channel** : The type of Channel (For example, Mobile, Web, IVR).

  * **Session type** : The type of session or interaction.

  * **Call duration** : Duration of session from start to end.

  * **Queued at** : Time session entered the queue.

  * **Assigned at** : Time session was assigned to agent.

  * **Wait** : Total wait duration in queue before being assigned to an agent for the session.

  * **Hold Duration** : Length of hold time- does not include wait time (calls only).

  * **Answer Type** : Indicates whether session was auto (0) or manually (1) answered.

  * **Fail reason** : Reason why a session failed.

  * **Feedback** : When enabled, shows customer feedback collected during session on record.

  * **Case** : Case the session object is attached to.

  * **Initial menu selected** : Initial queue menu selected.

  * **Materialized menu path** : The selected path leading to connection with the agent.

  * **Language** : The language used or selected for the session.

  * **Outbound phone number** : Applicable outbound phone number.

  * **Status** : Status of the session.

  * **Total transfers** : Number of total transfers during the session.




#### Files

All media files associated with the session object are attached as **files** to the session object. This includes:

  * Call recordings.

  * Chat history.

  * Mobile SDK based diagnostic package.

  * Media files sent by end users.




##### UI examples

**File list UI** : Example of session file list for call recording.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc047486a.png)

**File Detail UI** : Example of image upload by end user.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc049aaf4.png)

#### CCAI Platform Session actions

Reflects session activities:

  * Started call.

  * Custom data from the customer has arrived.

  * Finished call. .

  * Customer rating feedback received




Example session action detail UI: End-user feedback.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc042cc25.png)

#### Transfers

Any transfers associated with the session are listed in this section. It introduces a new set of information about the call that is not yet available in Admin Portal reports (this data has been available by API).

Transfer details represent a complete account of each transfer and are defined using the following fields:

  * **Transfer name** : CCAI Platform specific name of the transfer.

  * **Transfer ID** : ID of the transfer.

  * **Agent transferred from** : agent initiating the session transfer.

  * **Agent transferred to** : agent receiving the session transfer.

  * **Created at** : time transfer was created.

  * **Fail reason** : reason for failure of session transfer.

  * **Menu transferred from** : the originating queue menu from which transfer was initiated.

  * **Menu transferred to** : queue menu the session was transferred to.

  * **Session** : CCAI Platform session ID.

  * **Status** : status of transfer.

  * **Transfer from materialized path** : the materialized path transfer was originated from.

  * **Transfer to materialized path** : the materialized path the session was transferred to.




## Account lookup against multiple numbers

Admins can configure CCAI Platform portal to look up an account across multiple phone number fields in Salesforce. This makes it easier to connect different support sessions to a single account for consumers who have multiple phone numbers, such as mobile, home, or work numbers. This works for both inbound and outbound calls.

### Create a new phone number field in Salesforce

All existing phone number fields in Salesforce are available to use as a phone number lookup field. If there are still some phone number fields you want to add, you can create a new field. To add a new phone number field

  1. Go to **Object Manager**.

  2. Select the Account to edit.

  3. Click **Fields & Relationships**.

  4. Click **New** to add a new field.

  5. Enter the information for the new phone number field. For example, if you are adding a mobile number, you could enter Mobile as the `Field Label`, the mobile number as the `Field Name`, and Phone as the `Data Type`.

  6. After the new field is created, it will be displayed as a lookup field option in CCAI Platform portal. You can then add it as a lookup phone number for an account.




### Add phone numbers as lookup numbers in CCAI Platform portal

All phone number types across every CRM object (Contact, Account, Lead, and so on) are available selections in the CCAI Platform portal. You can update the following:

  * **Phone number lookup fields** : Previously-named phone number lookup fields. This option provides the ability to select multiple phone numbers, such as mobile, account phone, account fax. You can then associate these numbers with the same account.

  * **Phone number primary fields** :This field changes depending on what you select for phone number lookup fields. It provides the ability to select the phone number field to be used when you create a new CRM account.




To add multiple phone numbers as additional lookup numbers:

  1. Go to **Developer Settings > Account Lookup**.

  2. Select the **Object** and **Record Type** to apply the lookup fields to.

  3. In the **Phone number lookup fields** drop-down list, select the phone numbers to use as additional lookup numbers.

  4. Click **Save** in the drop-down box.

  5. Select the primary phone number to use when UJET creates a new CRM account. This drop-down list changes based on the phone numbers you selected for the previous field.

  6. Click **Save** in the Developer Settings section. The lookup numbers you selected will now connect to the same account.




## Salesforce flexible lookup permission changes

For Flexible Account lookup, the Agent permission set needs to be adjusted in order to open up flexibility regarding how CCAI Platform manages Salesforce data and process flow.

#### Example use cases

  * Disabling case creation and attaching the CCAI Platform Session object to an Account, Person Account or custom account object.

  * Disabling case creation and attaching the CCAI Platform Session object to Salescloud account objects like Leads and Opportunities.




### Additional setup steps

  1. Go to the Permission Sets settings page. You will see a cloned UJET_Agent permission set.

  2. Click **Object Settings.**

  3. You will see the Case and Contact object has Read, Create, Edit, and View All permissions, but Accounts does not. The next step is to add permissions for Account also.

  4. Add **Read** ; **Create, Edit** ; and **View All** access to the account object permissions and save it.

  5. Add **Tasks** type field permission.

  6. Check the boxes to allow **Read Access** and **Edit Access** for the Type field.




## Flexible outbound dialing

Flexible outbound call handling provides flexibility and granularity for managing outbound calls.

Requires CRM package v1.24, and for Sales Cloud requires v1.26.

Admins can configure if agents are able to create or not create a case, and whether or not agents can dial a number that won't be used for any account lookup or session association.

Many new updates to the Agent call adapter

  * Review and select from multiple matching account records

  * Select from open cases associated with the selected account

  * Create a new case

  * Configurable option to not create a ticket and/or create a new ticket

  * Handling multiple matching account records

  * Flexible ticket to session association




### Feature details

  * The object/term **Account** is referenced below as well as in the Agent Adapter UI, however, the object being referenced as "Account" may be different based on your configuration in **Developer Settings** .

  * Settings dependencies like settings for appending calls or chats to existing cases impact this feature.

  * Configuration saved in **Settings** > **Developer Settings** for Account Lookup can be overridden by agent selection in the agent adapter if an object other than the primary object is synced




### Account ID and case ID field details

#### Labels

The object/term **Account** is referenced in this article as well as in the Agent Adapter UI, however, the object being referenced as "Account" may be different based on your configuration in Developer Settings.

  * The Object Type, as set in the Admin portal > **Settings** > **Developer Settings** , under **Account Lookup** will populate the field called "Account ID."

  * The field called "Case ID" can be disabled.




_This UI will be updated to update the Agent Adapter fields dynamically based on settings in a future release._

#### Account and case behavior

##### Account ID

Account ID can be selected by:

  1. Clicking on the phone number from Account or Contact record

  2. Clicking the sync icon to sync when on the page of an Account or Contact record

  3. Entering an outbound phone number that is associated to an Account

  4. Clicking on a phone number in a Case that is associated with an Account ID and Case




##### Case ID

Case ID can be selected by:

  1. Once the Account ID is selected by one of the options above, CCAI Platform checks for one or more open cases for the selected Account ID and selects the most recent, or allows the agent to select based on your settings.

When the Account ID is selected and the **Prompt agents to select open case from list (when applicable)** option is enabled, select from the list of open cases.

When the Account ID is selected and the option **Allow agent to select "Create a new case" option for outbound calls** is enabled, a new case ID entered in the field and CCAI Platform pops a case and call attaches session data to the case using activity or CCAI Platform Session object.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc05d2899.png)




### Sync button behavior

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc05d778e.png)

Sync button works on the following types of Salesforce objects:

  * **Case** page

    * CCAI Platform finds the current lookup object - Contact, Account, Person Account, or Lead

    * The phone number field is populated based on the default phone setting

  * **Contact** or **Account** or **PersonAccount** or **Lead** page

    * If the current object is the same object type as lookup object, the object is populated and the object's phone number field.

    * If the current object is not the same object as a lookup object (set in Developer Settings), the default phone field's phone number is populated.

  * The page has a **CCAI Platform Session** or **Task** or **Activity**

    * CCAI Platform looks to see if object has the current lookup object association.

      * Ex. with the CCAI Platform Session object, this could be is UJET__Contact__c, UJET__Account__c, UJET__Lead__c.
    * If there is no lookup object association, information cannot be synced




### CCAI Platform configuration

#### Set lookup object

Based on your data model and process, you can choose what the primary lookup object should be when interacting with Salesforce.

#### Custom configuration: Enable or disable Cases

When using the CCAI Platform Session object to map session data to Salesforce, you have the option to disable cases. When this setting is disabled, the Case ID field in the Agent Adapter will no longer be available.

  1. In the CCAI Platform portal, go to **Settings** > **Operation Management**.

  2. In the Session Data section, when CCAI Platform Session is selected, enable or disable the option for **Attach CCAI Platform Sessions directly to the account lookup object.** No cases will be created.




#### Custom configuration: Operation management

  1. In the CCAI Platform portal, go to **Settings** > **Operation Management**.

  2. In the Multiple Account/Cases section enable or disable:

**Prompt agents to select open case from list (when applicable)** :

**Disabled:** most recent open case associated with the contact/account will be auto-selected.

**Enabled** : agent will be prompted to select from all open cases associated with the contact/account.

**Note:** In Ticket Creation Details, if "do not append call or chat" is enabled this option will not be editable.

When the above option is enabled, **Allow agent to select "Create a new case" option for outbound calls** can be enabled. When disabled the agent must use an existing open case.

**Allow agent to select "Do not create a case" option for outbound calls**

     1. When settings indicate that session data is mapped to the CCAI Platform Session object, call data including the call recording will be stored in the CCAI Platform Session and associated to the selected lookup object.

Agent adapter: The Case ID field will no longer appear in the UI.

     2. When settings indicate that session data is mapped to the Activity Object, no call data will be stored, including the call recording. _Do not enable this option if your compliance regulations/standards require all call recordings to be accessed_ because CCAI Platform will not be able to retrieve call recordings of calls where a case is not created.

**Allow "Use entered number to make call" option**

Enabled: Agents can select the Account ID, then enter a number not saved to the Account/Contact to place a call. The numbers will not be stored against the Account/Contact

Disabled: Outbound calls can only be placed to numbers that are stored on the Account/Contact object.




### Agent experience

#### Agent UI

Below is an example Call Adapter with all options enabled.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc05dcd92.png)

  1. Language and outbound number selection dictate which number will show when the caller answers the call. See [Multiple Outbound Numbers](https://docs.cloud.google.com/contact-center/ccai-platform/Call_Settings_and_Features/index.md#UUID-cb0a39b2-9150-011f-3ecb-44176d94c4a4) for details.

  2. Shows current selected, synced, or entered phone number to which the call will be placed.

  3. Dialpad icon opens the phone number input screen where you can enter or paste a phone number

  4. Check the checkbox to use a number that is not associated with the selected account/contact. See "Use entered number to make call" option. _May not be present based on settings._

  5. When the **sync** button is clicked, information from the currently open tab is used to populate the Account ID and/or Case ID fields.

  6. Account ID field displays the primary lookup, based on Admin settings in **Settings > DeveloperSettings > Account Lookup > Lookup object**. Further described above in Labels.

  7. Case ID field displays the selected record type, based on Admin settings in **Settings** > **DeveloperSettings** > **Account Lookup** | **Lookup object.** Further described above in Labels _May not be present based on settings._

  8. Once Account and Case ID are selected, **Call** places the outbound call.

  9. **Cancel** brings you back to the main Agent Adapter UI.




#### Agent UI variables

The Agent Adapter will display different options and different views based on your Developer Settings, and Operation Management settings.

##### Admin Portal settings that can impact the Agent experience

  * Do not append call or chat session to any existing open ticket

  * Prompt agents to select open case from list (when applicable)

  * Allow agent to select "Create a new case" option for outbound calls

  * Allow agent to select "Do not create a case" option for outbound calls

  * Allow "Use entered number to make call" option

  * Attach CCAI Platform Sessions directly to the account lookup object. No cases will be created




##### CRM data impacting the Agent experience

  * Number of contacts with the same phone number

    * No Contact with phone number

    * Only one Contact with phone number

    * Multiple Contacts with phone number

  * Number of open cases

    * No Case

    * Only one Case

    * Multiple Cases




### Placing an outbound call

#### Dialed outbound call

#### Placing a call by syncing with the current page in Salesforce

  1. From Salesforce, navigate to a Case, Contact, Account, or Lead.

  2. Click **Sync** in the Agent Adapter.

  3. If necessary, select the Account ID and Case ID objects from the dropdowns.

Be aware of the 3 things impact the adapter screen you will see after syncing

Your environment settings: select from open cases option enabled/disabled, create a new case option enabled/disabled, do not create a case option enabled/disabled

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc05e23c8.png)

Number of contacts with the same phone number

No Contact with phone number

Only one Contact with phone number

Multiple Contacts with phone number

Number of open cases

No Case

Only one Case

Multiple Cases

Click **Call**.




#### Use entered number to make call option

A specific account might have multiple locations or contacts, and not all phone numbers are saved to the account or contact. In this situation, your agents may need to dial out to numbers that aren't saved within the account/contact. This option lets an agent dial out to a number not saved to the contact while still associating the case with the contact. The number dialed will be saved in the comments of the CCAI Platform Session Object. To enable this capability, see Custom configuration: Operation management.

  1. From Salesforce, locate the account or contact and click the **sync** button in the Agent Adapter.

  2. Optional: Click the **Call a separate number** toggle to the on position to call a different number than the phone number you used to find the CRM account or record.

  3. Click the **dialpad** icon to edit the number.

  4. Paste or enter the phone number in the phone number field.

  5. Click **Call**.




## API Direct Access Point - Salesforce REST API

The API Direct Access Point(DAP) allows for routing logic to be implemented directly from an API source. Salesforce provides APEX REST class to fetch their data which CCAI Platform can use to direct callers using that API for Direct Access Points (DAP). Unlike other DAP options, AND logic can be used with multiple key/value pairs.

### Salesforce admin configuration

#### Prepare APEX REST class on Salesforce

  1. Quick search "apex".

  2. Select Custom Code > **Apex Classes** > **New**.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc05e7a28.png)




#### Create an APEX REST class

Although your code will be different, please see the below example:
    
    
    @RestResource(urlmapping = '/searchVIP')
    global class UjetVIPSearch {
        @httpPOST
        global static void searchVIP(){
            RestRequest req = RestContext.request;
            RestResponse res = RestContext.response;
            responsewrapper response= new responsewrapper();
            try{
                requestWrapper jsonBody;
                jsonBody  = (requestWrapper) JSON.deserialize(req.requestBody.toString(), requestWrapper.class);
    
                String aninumber = jsonBody.phone;
                // CCAI Platform will send phone parameter in format %222%333%4444
                if(string.isNotBlank(aninumber)){
                    integer cnt = [SELECT count() from Contact where Contact.Phone like :aninumber AND VIP__c = true];
                    response.is_vip = (cnt > 0);
                    res.responseBody = blob.valueof(JSON.serialize(response));
                }
                else{
                    res.statuscode = 404;
                    res.responseBody = blob.valueof('No Contact found');
                }
            }
            catch(exception e){
                res.statuscode = 500;
                res.responseBody = blob.valueof(e.getmessage());
            }
        }
        public class responsewrapper{
            public boolean is_vip;
        }
        public class requestWrapper{
            public string phone;
        }
    }
    

#### Modify security

Since the Apex REST class will be accessed by the agent's OAuth token, you will need to add all applicable agent profiles into the "Enabled Profiles" column.

  1. Once the APEX Rest class is created, click **Security** to edit.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc0613159.png)

  2. Select all agent profiles.

  3. Click the arrow to add to the Enabled Profiles column.

  4. Click the **Save** button.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc06189e0.png)




### Configuration

  * Choose from available routing logic options

  * Enable and configure in the CCAI Platform Portal

  * Create DAPs in the Queue Settings




### Test Routing

  1. Call the IVR using a phone number which should trigger the API DAP.

  2. Confirm the call is routed to the correct queue.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
