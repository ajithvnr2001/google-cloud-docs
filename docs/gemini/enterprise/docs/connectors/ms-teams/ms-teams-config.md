---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams/ms-teams-config/
title: Microsoft Teams configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:32.276267+00:00
---

# Microsoft Teams configuration  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams/ms-teams-config/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Microsoft Teams configuration Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up authentication and permissions before creating the Microsoft Teams data store.

## Set up authentication and permissions

You must set up authentication and permissions in Microsoft 365, which is crucial to allow Gemini Enterprise to access Microsoft Teams data.

### Entra app registration for Microsoft Teams data store

You must set up a Microsoft Entra application registration to enable secure access to Microsoft Teams before you create the Gemini Enterprise data store.

To register Gemini Enterprise as an OAuth 2.0 application in Microsoft Entra, do the following:

  1. Navigate to [Microsoft Entra admin center](https://entra.microsoft.com).
  2. In the menu, expand the **Entra ID** section and select **App registrations**.
  3. On the **App registrations** page, select add **New registration**.
  4. On the **Register an application** page, create an app registration by doing the following: 
     1. In the **Name** section, enter a display name for the application. ![The Register an application page in Microsoft Entra admin center.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/entraid.png)Register an application page
     2. In the **Supported account types** section, select **Accounts in the organizational directory only**. This option restricts access to users within your organization's Microsoft Entra tenant, which is appropriate for an enterprise application.
     3. In the **Redirect URI** section, select **Web** and enter the following URL as web callback URL (or redirect URL): 
        * `https://vertexaisearch.cloud.google.com/oauth-redirect`
     4. Click **Register**. Microsoft Entra creates your app and displays it on the **All applications** page.



### Create an OAuth 2.0 configuration

To create a connection using the OAuth 2.0 authentication method, obtain a client ID, client secret, and tenant ID from your Microsoft Entra application registration page by following these steps.

#### Obtain client ID and client secret

To obtain the client ID and secret for the app, do the following:

  1. Navigate to [Microsoft Entra admin center](https://entra.microsoft.com).
  2. In the menu, expand the **Entra ID** section and select **App registrations**.
  3. On the **App registrations** page, select **All applications**.
  4. Open the application you created.
  5. On the app page, select **Certificates & secrets**.
  6. Click add **New client secret**.
  7. To obtain the client secret, do the following in the **Add a client secret** dialog: 
     1. Enter a description for the secret. ![The Add a client secret dialog in Microsoft Entra admin center.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/clientcred.png)Add a client secret dialog
     2. Select an expiry duration. It's recommended to select the default value.
     3. Click **Add**.
     4. Copy the client secret from the **Value** column.
  8. To obtain the client ID, do the following: 
     1. On the app page, select **Overview**.
     2. Copy the **Application (client) ID**.



#### Obtain tenant ID

Your tenant ID can be found in the **Tenant ID** box on the [overview page](https://entra.microsoft.com/#view/Microsoft_AAD_IAM/TenantOverview.ReactView) in the Microsoft Entra admin center.

![Screenshot of the Tenant ID on the overview page in Microsoft Entra admin center.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/tenant-id.png)Get the tenant ID

### Configure the Microsoft Graph permissions

To configure the required Microsoft Graph permissions for the app, do the following:

  1. Navigate to [Microsoft Entra admin center](https://entra.microsoft.com).
  2. In the navigation menu, expand the **Entra ID** section and select **App registrations**.
  3. On the **App registrations** page, select **All applications**.
  4. Open the application you created.
  5. On the app page, select **API permissions**.
  6. Click **Add a permission**.
  7. In the **Request API permissions** page, select **Microsoft Graph** , and select **Delegated permissions**.
  8. Search for and select the following permissions for your connection mode. Ensure that an administrator grants consent for all the delegated permissions listed in the following table. Once consent is granted, the **Status** column displays **Granted** with a green tick mark (✓).

Connection mode | Permission | Permission type | Purpose  
---|---|---|---  
Federated search | `Channel.ReadBasic.All` | Delegated | Allows the app to read the names and descriptions of channels.  
`ChannelMember.Read.All` | Delegated | Allows the app to read the members of channels.  
`ChannelMessage.Read.All` | Delegated | Allows the app to read user channel messages.  
`Chat.Read` | Delegated | Allows the app to read all chats.  
`Chat.ReadBasic` | Delegated | Allows the app to read basic properties of chats.  
`ChatMessage.Read` | Delegated | Allows the app to read all one-to-one and group chat messages.  
`Group.Read.All` | Delegated | Allows the app to read the Microsoft Purview sensitivity labels assigned to a team's parent Microsoft 365 group, which are used to apply Sensitive Data Protection (redaction) to Microsoft Teams content.  
`Schedule.Read.All` | Delegated | Allows the app to read schedules, schedule groups, and shifts for teams.  
`Team.ReadBasic.All` | Delegated | Allows the app to read the names and description of teams.  
`TeamMember.Read.All` | Delegated | Allows the app to read the members of teams.  
`User.Read.All` | Delegated | Allows the app to read all users' full profiles.  
Federated search and actions | `Channel.Create` | Delegated | Allows the app to create channels in Microsoft Teams. Required for the create channel action.  
`Channel.ReadBasic.All` | Delegated | Allows the app to read the names and descriptions of channels.  
`ChannelMember.Read.All` | Delegated | Allows the app to read the members of channels.  
`ChannelMember.ReadWrite.All` | Delegated | Allows the app to add and remove members from channels. Required for the add member to channel action.  
`ChannelMessage.Read.All` | Delegated | Allows the app to read user channel messages.  
`ChannelMessage.ReadWrite` | Delegated | Allows the app to update channel messages. Required for the update channel message action.  
`ChannelMessage.Send` | Delegated | Allows the app to send messages in any channel.  
`ChannelSettings.ReadWrite.All` | Delegated | Allows the app to read and update the settings of channels. Required for the update channel action.  
`Chat.Create` | Delegated | Allows the app to create new chats. Required for the create chat action.  
`Chat.Read` | Delegated | Allows the app to read all chats.  
`Chat.ReadBasic` | Delegated | Allows the app to read basic properties of chats.  
`Chat.ReadWrite` | Delegated | Allows the app to read and write one-to-one and group chat threads, including chat messages. Required for the update chat and update chat message actions.  
`ChatMessage.Read` | Delegated | Allows the app to read all one-to-one and group chat messages.  
`ChatMessage.Send` | Delegated | Allows the app to send chat messages.  
`Group.Read.All` | Delegated | Allows the app to read the Microsoft Purview sensitivity labels assigned to a team's parent Microsoft 365 group, which are used to apply Sensitive Data Protection (redaction) to Microsoft Teams content.  
`Schedule.Read.All` | Delegated | Allows the app to read schedules, schedule groups, and shifts for teams.  
`Schedule.ReadWrite.All` | Delegated | Allows the app to create and update schedules, shifts, and time-off entries for teams. Required for the create schedule, create time off entry, and update time off entry actions.  
`Team.ReadBasic.All` | Delegated | Allows the app to read the names and description of teams.  
`TeamMember.Read.All` | Delegated | Allows the app to read the members of teams.  
`User.Read.All` | Delegated | Allows the app to read all users' full profiles.  
**Note:** If you only intend to use the data store for search and not to perform any actions that modify content in Microsoft Teams, you can limit the scope to the `Read.All` permissions. Other permissions are required for [actions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams#supported-actions) that involve updating content in Microsoft Teams.
  9. Click **Add Permissions**.




### Grant administrator consent for permissions

To grant administrator consent for permissions, do the following:

  1. Sign in to [Microsoft Entra admin center](https://entra.microsoft.com) as a global or application administrator.
  2. In the navigation menu, expand the **Entra ID** section and select **App registrations**.
  3. On the **App registrations** page, select **All applications**.
  4. Open the application you created.
  5. On the app page, select **API permissions**.
  6. Click the **Grant admin consent for** button.

![The dialog to confirm granting admin consent.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/getconsent.png)Grant admin consent
  7. Select **Yes** in the dialog to confirm the consent action.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
