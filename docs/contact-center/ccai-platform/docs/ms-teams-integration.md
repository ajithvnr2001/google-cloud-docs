---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/ms-teams-integration/
title: Microsoft Teams \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:29.402769+00:00
---

# Microsoft Teams  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/ms-teams-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Microsoft Teams Stay organized with collections  Save and categorize content based on your preferences. 

You can set up Microsoft Teams users within the Contact Center AI Platform (CCAI Platform) to receive calls in the Microsoft Teams platform instead of CCAI Platform agent adapter. In addition it is possible to for calls to be routed the agent directly or through transfers. The Microsoft Teams integration is specifically designed for phone transfers; chat transfers are not supported.

To fully integrate Microsoft Teams with CCAI Platform you need to perform configuration changes to both Microsoft Teams and CCAI Platform.

## Prerequisites

In order to correctly link the CCAI Platform portal to Microsoft Teams, you must have an an account with **Global Administrative Permission**. The account cannot be a personal Microsoft account.

  * Microsoft Teams Essentials with AAD, E1/E3, A1/A3, F1/F3, or G1/G3 plan.

  * Microsoft Teams Phone standard licenses.

  * A Microsoft standalone calling plan or third-party PSTN carrier.




## SIP Trunking setup

The current iteration of MS Teams integration uses an SIP protocol to connect MS Teams agents to CCAI Platform. SIP ID/URIs are required for integration. You can use the SIP Trunking provider of your choice, but you must follow these basic steps before you can enable the connection to CCAI Platform:

  * Purchase a phone number from the SIP Trunking provider.

  * Add an SIP connection.

  * Assign the purchased phone number to the created SIP connection.

  * Set Outbound Voice Profile.

  * Create Inbound SIP Subdomain (`ujet.provider_domain`).




## User license setup (Microsoft 365)

Complete the following tasks to connect the SIP IDs to Microsoft:

  * Users in Microsoft must be set up with E5 licenses or equivalent.

  * Register the subdomain auto-generated from your SIP Trunking provider.

  * Activate the domain by creating a sub-account.




## Microsoft Teams license setup

The following table lists available MS Teams licenses and the add-ons required for integration. You can set up your license in the [Microsoft 365 Admin Portal](https://admin.microsoft.com/)

  1. In the Microsoft 365 Admin Portal, go to **User** > **Active User**.

  2. Select a user to assign a license to. Click the 3 vertical dots next to the user's email address, then click **Manage product licenses**.

  3. In the **User Detail** window, go to **Licenses** and assign the correct license.


Base plan | Add-on required for direct routing  
---|---  
Microsoft Business Basic/Standard/Premium | Microsoft 365 Business Voice without Calling Plan  
Microsoft Office 365 Enterprise E1/E3/F3/A1/A3 | Phone System  
Microsoft Office 365 Enterprise E5 | No add on required  
  
## Microsoft Teams direct routing setup

**Note:** This section assumes that you don't have an MS Teams Phone system already configured. If you do already have an MS Teams phone system set up, you can skip this section.

After SIP is set up and the domain is registered on Microsoft 365, you must now add the SIP Trunking SBC in Direct Routing. You can complete this setup in the Microsoft Teams [admin portal](https://admin.microsoft.com/), with the alternative option of using PowerShell. These instructions only cover setup using the Teams portal. For a comprehensive reference about configuring Direct Routing in Microsoft Teams, or if you prefer to perform these actions in PowerShell, see the [Microsoft Help Center documentation](https://learn.microsoft.com/en-us/microsoftteams/direct-routing-configure).

### Add Direct Routing

  1. Using the left-hand navigation menu, go to **Voice > Direct Routing > SBCs** and click **Add**.

  2. Enter a qualified domain name (FQDN) for the Session Border Controller (SBC) and configure appropriate settings for the SBC based on your needs.

  3. Click **Save**.




### Create voice routes and enroll SBC

  1. In the left-hand navigation menu, go to **Voice > Direct Routing > Voice routes**.

  2. Click **Add** , then enter a name and description for the voice route.

  3. Set the priority and specify the dialed number pattern.

  4. To enroll an SBC with the voice route, click **Add SBCs** under **SBCs enrolled (optional)**. Select the SBCs you want to enroll, then click **Apply**.

  5. (Optional). You can add PSTN (Public Switched Telephone Network) usage records at this point if you want, or you can wait until you have configured the voice routing policy in the following section. To add usage records click **Add PSTN usage** under **PSTN usage records (optional)** , select the PSTN records you want to add, then click **Apply**.

  6. Click **Save**.




### Configure voice routing policy and add PSTN Usage Records

  1. In the left-hand navigation menu, go to **Voice > Voice routing policies** and click **Add**.

  2. Enter a name and description for the policy.

  3. Go to **PSTN usage records > Add PSTN usage**, then select the records that you want to add. To create a new PSTN usage record, click **Add**.

  4. Arrange them in your preferred order, if multiple PSTN records are present.

  5. Click **Apply** , then **Save**.




### Assign dial plan and voice routing policy

Dial plans are assigned the same way as policies. Policies are assigned either directly to users (individually or at scale through a batch assignment), or to a group that the users are members of.

To create a new dial plan:

  1. In the left-hand navigation menu, go to **Voice > Dial plan > Add**.

  2. Enter a name and description for the dial plan.

  3. (Optional). Under **Dial plan details** , specify an external dialing prefix. This is only required if users need to dial one or more additional leading digits (for example, 9) to get an external line. To do this:

     1. In the **External dialing prefix** box, enter an external dialing prefix. The prefix can be up to four characters (#,*, and 0-9).

     2. Turn on **Optimized device dialing**. You must turn on this setting in order to make calls outside your organization if you specify an external dialing prefix.

  4. Configure and associate one or more normalization rules for the dial plan under **Normalization rules**. Each dial plan must have at least one normalization rule associated with it. To do this, do one or more of the following:

     1. To create a new normalization rule and associate it with the dial plan, click **Add** and then define the rule.

     2. To edit a normalization rule that's already associated with the dial plan, select the rule and then click **Edit**. Make the required changes, hen click **Save**.

     3. To remove a normalization rule from the dial plan, select the rule and click **Remove**.

  5. Arrange the normalization rules in your preferred order. Click **Move up** or **Move down** to change the position of rules in the list.




After setting up a dial plan, you should be able to see the SBCs. The screen might show error messages, but these errors are typically not blocking. If you would like to resolve the error messages, or troubleshoot any errors that might be blocking, reach out to Microsoft Support or your SIP Trunking provider for additional assistance.

## Set up SIP for a user

If you don't have a direct SIP URI for each MS Teams Phone System User, you can follow the steps in this section to create one. Be aware that these steps will change the login information for your users when they log into Microsoft 365 and their email.

After Direct Routing is set up, you can create or update a user using the Microsoft 365 portal. Microsoft Calling Plan and Operator Connect phone numbers can be managed only in the Microsoft 365 portal. Direct Routing phone numbers can be managed either in the on-premises Active Directory or in the Microsoft Teams portal. These instructions only demonstrate how to make these edits in the Microsoft 365 and Teams portals.

### Change subdomain of the user

  1. Navigate to **User > Active User**. Select the user, then select **Manage username and email**.

  2. Set up or change the domain to the domain created from your SIP Trunking provider.




### Add a number

  1. Navigate to the Microsoft Teams Admin Portal.

  2. Navigate to **Users > Manage Users**, then select the specific user.

  3. Under **General Information** , click **Edit**.

  4. To assign a phone number, set number type to **Direct Routing** and enter the phone number you set up with the SIP Trunking Provider.




### Set up SIP URI

To make a call to a MS Teams user, the SIP URI on CCAI Platform must be set up with the following configurations:

  1. If the subdomain is changed: `{username}@{sip_subdomain}`.

  2. If the MS Account is unchanged, and Direct Routing is set up through Teams: `{phone_number}@{subdomain}`.




## Microsoft Azure setup

Set up an **Application** in MS Azure. This application will allow CCAI Platform to use MS Graph in order to fetch important information such as user and presence information.

### Application registration

  1. Sign in to [MS Azure](https://portal.azure.com/#home) and search for **Azure Active Directory**.

  2. On the left-hand side, click **App registration**.

  3. Click **New registration**. Fill out the names and set the Supported account types (accounts in any organizational directory).

  4. Configure the **Redirect URI** in the following format: `{project_domain}/v1/ucaas/ms_teams/oauth_callback`.

  5. After the app has been registered, you will be able to see the Application (client) ID by clicking on the **Application** in **App registrations**. Make a note of this ID value.




### Client secret

  1. After you have registered an application, go to **Manage > Certificates > Secrets** in the left-hand navigation menu.

  2. Click **Client secrets** tab and click **New client secret**.

  3. Fill out the description and expiration date. The max expiration date for the client secret is 24 months. This value reflects when the client secret will expire from Azure. This value must be the same in CCAI Platform for the integration to function properly.

  4. After the secret has been generated, you will be ableo to see the value of the secret. Save this value in a secure location for later; it is only available temporarily, and if you lose the value you will need to generate another client secret.




## CCAI Platform setup

Configurations are done under the label of UCaaS rather than MS Teams specifically. UCaaS integration is similar to setting up a CRM. MS Teams does not support transfers for groups or teams, so you will need to configure each user individually.

**Reminder** :

In order to make a call to a Microsoft Teams user, the SIP URI on CCAI Platform must be set up with the following configurations:

  * If the subdomain is changed: `{username}@{sip_subdomain}`.

  * If the MS Account is unchanged, and Direct Routing is set up through Teams: `{phone_number}@{subdomain}`.




### Link Microsoft Teams to CCAI Platform

  1. In the CCAI Platform portal, go to **Developer Settings > UcaaS**.

  2. Use the drop-down menu to select your UcaaS platform (Microsoft Teams).

  3. Click **Save**. This will expose the other fields you need to fill out.

  4. Set **Connected App ID** and **Connected App Secret** to the App (client) ID value and client secret value you [created in Azure](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ms-teams-integration#microsoft_azure_setup).

  5. Click the **Link** button to connect the platforms. If you try to click **Save** before clicking the **Link** button, you will get an error message.

     1. If the link is successful, you will see a confirmation banner.

     2. If the link is unsuccessful, you will see a warning banner. The most likely reason for a failed link is incorrect credentials. Check for typos, or copy and paste if possible to ensure accuracy.

     3. Once the link is created, the button will change to an **Unlink** button. If you need to unlink the token, click the **Unlink** button.

  6. Set your multicast limit. The current limit is 100 external agents.

  7. Click **Save**.




### Configure Microsoft Teams users in CCAI Platform user settings

Microsoft Team users can be configured as an external UCaaS users in the **Add User** or Bulk User Management settings. You can add users individually by following these steps or you can import them in bulk.

When a user is added, they will need to activate their account using an email link to complete the process. For more detailed information on adding users, see the [Add and view users](https://docs.cloud.google.com/contact-center/ccai-platform/docs/add-edit-user) and [Bulk user management](https://docs.cloud.google.com/contact-center/ccai-platform/docs/bulk-user-management) documentation.

#### Add a user

  1. To add a user and enable them in UCaaS, go to **Settings > Users > Teams > +Add a User**.

  2. Enter the [required fields](https://docs.cloud.google.com/contact-center/ccai-platform/docs/add-edit-user).

  3. Check the **External UCaaS user** box, which will expose two required fields.

  4. Enter the **SIP URI/ID** and **UCaaS username** for the user.

  5. Click **Add**.




#### Edit a user

  1. To enable UCaaS for an existing user, click the pencil icon next to the user's name in **Settings > Users > Teams**.

  2. Check the **External UCaaS** user box, which will expose two required fields.

  3. Enter the **SIP URI/ID** and **UCaaS username** for the user.

  4. Click **Update**.




#### Bulk User Management

The template for configuring your spreadsheet for import to CCAI Platform as a CSV file can be found in the [bulk user management](https://docs.cloud.google.com/contact-center/ccai-platform/docs/bulk-user-management) documentation. Three fields (External User, External SIP URI, and UCaaS username) are available for UCaaS settings. There is also a field for restricting international calling. If you are updating an existing spreadsheet, be sure to account for these changes when you add new users.

#### Agent status inheritance

A change required to permit status changes in the Teams environment is found in the CCAI Platform portal under **Settings** > **Developer Settings** > **Agent Status Inheritance**. A UCaaS option is available to allow the relevant CCAI Platform agent statuses to be reflected correctly in the Teams environment, and allow you to configure your preferences regarding how the statuses are prioritized between the two platforms.

#### Status inheritance at login

It is typically expected that MS Teams agents won't be logged into both CCAI Platform and Microsoft Teams simultaneously, therefore it is expected that the agent will skip wrap-up altogether and go to the next status (Available). However, there are some instances where being logged into both platforms might be necessary. In those instances, the agent will go through wrap-up as they normally do. In the event the agent must be logged into CCAI Platform exclusively (such as during a Teams outage), their wrap-up and available statuses are handled as if they are a normal CCAI Platform agent.

Option | Expected Behavior  
---|---  
Do not inherit status at login | The CCAI Platform status is prioritized over the Teams agent status.  
Apply UCaaS agent status at login | When agents login to CCAI Platform, they will start off in the CCAI Platform status that their current UCaaS status is mapped to.  
UCaaS always overrides agent's next status | Even if the agent sets their next status in CCAI Platform, their UCaaS status will override the CCAI Platform next status.  
  
### Configure agent availability

Teams users can optionally be added to queues. CCAI Platform users will have the ability to transfer these calls to Teams users as an External transfer type. External agents don't have to be added to queues to be available for transfers. The transferred call receiver who is using MS Teams won't be linked with the CRM, so if they need to make additions to a case, they will need to take ownership of the case (if required by your process or CRM) and make notes within the case manually.

#### Add Teams users to queues

When you make changes to existing queues or creating new ones, you can identify your Teams users by the Teams icon next to their name. For detailed information about creating or editing existing queues see the [queue and menu setup](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Queue_and_Menu_Setup#ivr_add_and_edit_queue_menus) documentation.

## Test outputs

Agents should see the option to transfer to queues and individuals with Microsoft Teams profiles after you have made your configurations. If an external agent is assigned to a queue, then they will receive a call when it comes to that queue or when another agent transfers a call to that queue. There will be an indication in the transfer UI if the agent is external or if the queue contains external agents. External agents will be available for transfer regardless of whether they are assigned to a queue or not.

**Note:** Calls can be transferred to the Microsoft Teams platform, but cannot be transferred back.

When you monitor agents' statuses, it is expected behavior to see the Microsoft Teams users' statuses alongside the CCAI Platform users' statuses. There is no distinguishing indicator between which platform they are using, though you might be able to use the email field to make that distinction depending on the choices you make during configuration.

In Microsoft Teams, users will be able to receive transfers as long as they are configured to receive CCAI Platform transfers and are in an Available status. Incoming calls from CCAI Platform look like other incoming calls to Microsoft Teams and are handled normally. The only thing a user should keep in mind is that the call is no longer connected to the CRM once it's transferred to Microsoft Teams, so case handling within the CRM needs to be handled manually. Your company's case handling guidelines should determine whether a new case should be created or whether the user should manually take over the case to add notes, rather than the functionality of the tool.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
