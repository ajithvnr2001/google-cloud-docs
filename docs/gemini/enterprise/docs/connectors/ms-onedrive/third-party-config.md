---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive/third-party-config/
title: Microsoft OneDrive configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:42:07.428186+00:00
---

# Microsoft OneDrive configuration  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive/third-party-config/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Microsoft OneDrive configuration Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up and configure a third-party configuration before creating the OneDrive data store.

## Set up authentication and permissions

You must set up authentication and permissions in Microsoft 365. This is crucial for allowing the connector to access and synchronize data. The OneDrive connector supports various authentication methods, such as OAuth client credentials or API tokens.

### Register Microsoft Entra app for Microsoft OneDrive connector

You must set up an Entra application registration to enable secure access to Microsoft OneDrive before you can create the connector in Gemini Enterprise.

To register Gemini Enterprise as an OAuth 2.0 application in Entra, do the following:

  1. Navigate to [Microsoft Entra admin center](https://entra.microsoft.com).
  2. In the navigation menu, expand the **Entra ID** and select **App registrations**.
  3. On the **App registrations** page, click add**New registration**.
  4. On the **Register an application** page, do the following:

     1. In the **Name** field, enter a name for your app.
     2. In the **Supported account types** section, select **Accounts in this organizational directory only**.
     3. In the **Redirect URI** section, do the following: 
        1. In the platform list, select `Web`.
        2. In the redirect URI field, enter `https://vertexaisearch.cloud.google.com/console/oauth/default_oauth.html`.
     4. Click **Register**. Microsoft Entra creates your app and displays the overview page of your app.
  5. In the app navigation menu, click **Authentication**.

  6. Click add**Add redirect URI**.

  7. In the platform selection pane, do the following:

     1. Select **Web**.
     2. In the **Redirect URI** field, enter `https://vertexaisearch.cloud.google.com/oauth-redirect`.
     3. Click **Configure**.



#### Add federated credential for data ingestion

If you are using **Data ingestion** as the connection mode and **Federated credentials** as authentication method, then do the following:

  1. In the app navigation menu, click **Certificates & secrets**.
  2. Select the **Federated credentials** tab.
  3. Click add**Add credential**.
  4. Select **Other issuer** from the **Federated credential scenario** list.
  5. In the **Issuer** field, enter `https://accounts.google.com`.
  6. In the **Subject identifier** field, enter the value that you get from the Google Cloud console. This value is generated during the [Microsoft OneDrive data store creation](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive/set-up-data-store#create-data-store) in the data section.
  7. In the **Name** field, enter a unique label for the federated credential.
  8. Click **Add** to grant access.



### Create an OAuth 2.0 configuration

To create a connection using the OAuth 2.0 authentication method, you need to obtain a client ID, client secret, and your Tenant ID from your Microsoft Entra application registration page.

#### Obtain client ID and client secret

  1. To obtain the client ID, do the following:

     1. In the app navigation menu, select **Overview**.
     2. Copy the **Application (client) ID**.
  2. To obtain the client secret for the app, do the following:

     1. In the app navigation menu, select **Certificates & secrets**.
     2. Click add**New client secret**.
     3. In the client secret pane, do the following: 
        1. In the **Description** field, enter a description for the secret.
        2. In the **Expires** list, select an expiry duration.
        3. Click **Add**.
     4. Copy the client secret from the **Value** column.



#### Obtain Tenant ID

Your tenant ID can be found in the **Tenant ID** box on the [overview page](https://entra.microsoft.com/#view/Microsoft_AAD_IAM/TenantOverview.ReactView) in the Microsoft Entra admin center.

### Configure Microsoft API permissions

To configure the required API permissions for the app, do the following:

  1. Navigate to the app page.
  2. In the app navigation menu, select **API permissions**.

  3. Click add**Add permissions**.

  4. In the **Request API permissions** pane, select **Microsoft Graph**.

  5. Search for and select the following permissions based on your connection mode:


**Connection mode** | **Type** | **Scope** | **Purpose**  
---|---|---|---  
**Federated search** | Delegated | `Files.Read.All` | Allows the data store to read all files that the user can access.  
Delegated | `Sites.Read.All` | Allows the data store to read documents and list items in all site collections that the user can access.  
Delegated | `User.Read.All` | Allows the data store to resolve user drive locations for content discovery.  
**Data ingestion** | Application | `Files.Read.All` | Allows the data store to read and synchronize files across the organization without a signed-in user.  
Application | `Group.Read.All` | Allows the data store to read properties and memberships of all groups.  
Application | `GroupMember.Read.All` | Allows the data store to read memberships for all groups to manage access control (ACL) syncing.  
Delegated | `User.Read` | Allows the data store to read the profile and basic company information of signed-in users.  
Application | `Sites.FullControl.All` | Allows full control of all site collections.  
Application | `Sites.Selected` | Allows access to a specific subset of site collections.  
Federated credentials only | `User.Read.All` | Allows the data store to read user profiles.  
Delegated | `User.ReadBasic.All` | Allows reading a basic set of profile properties for users in the organization.  
**Actions** | Delegated | `Files.ReadWrite.AppFolder` | Allows the data store to read, create, update and delete files in the Microsoft OneDrive folder.  
Delegated | `Files.ReadWrite` | Allows the data store to read, download, create, upload, update, and delete the files that the user can access.  
Delegated | `Files.ReadWrite.All` | Allows the data store to read and update files across all drives the user has access to. Required for the file and folder mutation actions (copy, move, rename, share, update properties) that operate on files stored in drives beyond the user's own Microsoft OneDrive.  
  
  6. Click **Add Permissions**.
  7. Grant administrator consent. For information about how to grant consent, see [Grant tenant-wide administrator consent to an application](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal) in the Microsoft Entra documentation.



## Troubleshooting

This section describes how to resolve common issues with the Microsoft OneDrive connector.

### Users see "Need admin approval" when they connect

When users connect to Microsoft OneDrive from the Gemini Enterprise web app for the first time, Microsoft might show a **Need admin approval** screen. This happens if Gemini Enterprise requests administrator-level permissions, or if your Microsoft Entra tenant prohibits users from authorizing third-party apps without prior tenant-wide administrator consent.

To resolve this issue, an administrator must complete the first authorization. After that, other users in your tenant can connect without the approval screen.

  1. Ask a Microsoft Entra ID administrator who can grant tenant-wide consent to sign in to the Gemini Enterprise web app and connect to Microsoft OneDrive.

  2. On the permissions screen, have the administrator select **Consent on behalf of your organization** , and then click **Accept**.

  3. Ask users to connect again.




For more information, see [Grant tenant-wide admin consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal) in the Microsoft Entra documentation.

**Note:** Deleting and re-creating the data store doesn't resolve this issue, because consent is granted in your Microsoft Entra tenant, not to the data store.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
