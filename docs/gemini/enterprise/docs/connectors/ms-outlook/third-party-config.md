---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook/third-party-config/
title: Microsoft Outlook configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:56.146349+00:00
---

# Microsoft Outlook configuration  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook/third-party-config/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Microsoft Outlook configuration Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up and configure a third-party configuration before creating the Outlook data store.

## Set up authentication and permissions

You need to set up authentication and permissions in Microsoft Entra admin center. This is crucial for allowing the connector to access and synchronize data.

### Register Entra app for Microsoft Outlook connector

Before creating the Microsoft Outlook connector in Gemini Enterprise, register a Microsoft Entra application to enable secure access.

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
           1. Click **Register**. Microsoft Entra creates your app and displays the overview page of your app.
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
  6. In the **Subject identifier** field, enter the value that you get from the Google Cloud console. This value is generated during the [Microsoft Outlook data store creation](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook/set-up-data-store#create-data-store) in the data section.
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

  1. On the app page, select **API permissions**.

  2. Click **Add permissions**.

  3. In the **Request API permissions** page, select **Microsoft Graph**.

  4. Search for and select the following permissions based on your connection mode:

**Connection mode** | **Permission** | **Purpose**  
---|---|---  
**Federated search** | `Mail.Read`  
`Mail.Read.Shared`  
`Calendars.Read`  
`Contacts.Read` | (Delegated) Allows the data store to read the signed-in user's mailbox, mail from shared mailboxes, calendar events, and contacts.  
**Data ingestion** | `Calendars.Read` | (Application) Allows the data store to read events of all calendars.  
`Calendars.ReadBasic.All` | (Application) Allows the data store to read events of all calendars, except for properties such as body, attachments, and extensions.  
`Contacts.Read` | (Application) Allows the data store to read all contacts in all mailboxes.  
`Mail.Read` | (Application) Allows the data store to read mail in all mailboxes.  
`Mail.ReadBasic` | (Application) Allows the data store to read basic mail properties in all mailboxes. Includes all properties except body, previewBody, attachments and any extended properties.  
`Mail.ReadBasic.All` | (Application) Allows the data store to read basic mail properties in all mailboxes. Includes all properties except body, previewBody, attachments and any extended properties.  
`User.Read` | (Delegated) Allows the data store to read the profile of signed-in users.  
`User.Read.All` | (Application) Allows the data store to read the full set of profile properties, reports, and managers of other users in your organization.  
`User.ReadBasic.All` | (Application) Allows the data store to read a basic set of profile properties of other users in your organization.  
**Actions** | `Mail.Send` | (Delegated) Allows the data store to send mail as users in the organization.  
`Mail.ReadWrite` | (Delegated) Required for the **Add attachments**, **Create message**, **Update message**, and **Move mail** actions.  
`Calendars.ReadWrite` | (Delegated) Allows the data store to create, read, update, and delete events in user calendars.  
`Contacts.ReadWrite` | (Delegated) Allows the data store to create, read, update, and delete user contacts.  
`User.Read` | (Delegated) Allows the data store to read the profile of signed-in users.  
**File productivity (Excel, Word, PowerPoint)** | `Files.Read.All` | (Delegated) Sufficient **only** for tools that read file metadata or download file content: listing Excel workbooks, reading Excel workbook metadata, and converting Word (.docx) or PowerPoint (.pptx) documents to PDF. **Not sufficient for Excel workbook content operations** (see next row).  
`Files.ReadWrite.All` | (Delegated) Required for **all** Excel workbook content operations (read **and** write), including get worksheets, get tables, get rows, get row, create worksheets and tables, add and update rows, and add key columns. Per the Microsoft Graph API reference for these endpoints (for example, [worksheet-list](https://learn.microsoft.com/graph/api/worksheet-list), [table-list](https://learn.microsoft.com/graph/api/table-list), [tablerow-list](https://learn.microsoft.com/graph/api/tablerow-list)), the accepted delegated permission is `Files.ReadWrite`. `Files.ReadWrite.All` grants the same capability across all drives the user can access. Also required for creating Word and PowerPoint documents in the user's OneDrive.  
`User.Read` | (Delegated) Required to resolve the signed-in user's OneDrive location for file operations.  
**Tasks (Outlook to-do lists and tasks)** | `Tasks.Read` | (Delegated) Required for read operations on the signed-in user's Outlook task lists and tasks (list task lists, list tasks, get task).  
`Tasks.ReadWrite` | (Delegated) Required for write operations: creating, updating, and deleting tasks in the signed-in user's Outlook task lists.  
**Users and directory (delegated enumeration)** | `User.ReadBasic.All` | (Delegated) Required for tools that enumerate or look up profiles of other users in the organization (Get User, List Users, and tools that operate on other users' mailboxes or calendars).  
  5. Click **Add Permissions**.


**Note:** If you only intend to use the data store for search and not perform any actions, you can limit the scopes to just `Mail.Read`, `Calendars.Read`, and `Contacts.Read`. The other scopes are required to perform the actions mentioned in [Supported actions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook#supported-actions).**Note:** For the file-productivity actions on Excel, Word, and PowerPoint, **grant`Files.ReadWrite.All` if you plan to use any Excel workbook content operations** (worksheets, tables, rows) — per the [worksheet-list](https://learn.microsoft.com/graph/api/worksheet-list), [table-list](https://learn.microsoft.com/graph/api/table-list), and [tablerow-list](https://learn.microsoft.com/graph/api/tablerow-list) Microsoft Graph API references, the accepted delegated permission for those endpoints is `Files.ReadWrite`, so `Files.Read.All` alone is not sufficient. `Files.Read.All` is sufficient only for listing Excel workbooks, reading Excel workbook metadata, and Word or PowerPoint PDF conversion. Tenants that skip the required scope will see HTTP 403 `accessDenied` errors. For the driveItem-based operations (Word/PowerPoint PDF conversion, listing Excel workbooks, reading Excel workbook metadata), Microsoft Graph also documents `Sites.Read.All` or `Sites.ReadWrite.All` as accepted alternatives (see [driveItem-get](https://learn.microsoft.com/graph/api/driveitem-get) and [driveItem-get-content-format](https://learn.microsoft.com/graph/api/driveitem-get-content-format)).**Note:** The Outlook task tools require `Tasks.Read` (read task lists and tasks) or `Tasks.ReadWrite` (create, update, delete tasks). The user-lookup tools (Get User, List Users, and tools that operate on other users' mailboxes or calendars) require `User.ReadBasic.All` at minimum. Tenants that skip these scopes will see HTTP 403 `notAllowed` on task tools and HTTP 403 `Authorization_RequestDenied` on user-lookup tools. Tenants that need higher-privileged user access can substitute `User.Read.All` or `Directory.Read.All`.**Note:** After adding application permissions, you need to grant admin consent for your tenant. For more information, see [Grant tenant-wide admin consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal#grant-tenant-wide-admin-consent-in-enterprise-apps-pane).

## Troubleshooting

This section describes how to resolve common issues with the Microsoft Outlook connector.

### Troubleshoot REST API and message search issues

If the Gemini Enterprise assistant reports that message search isn't working, or that the REST API isn't enabled for a user's mailbox (corresponding to a `MailboxNotEnabledForRESTAPI` error from Microsoft Graph), you can troubleshoot the issue in your Microsoft environment.

This error occurs for the following reasons:

  * The mailbox is hosted on-premises (in a hybrid Exchange deployment) and hasn't been enabled for REST API access.

  * The mailbox is inactive or soft-deleted.

  * There is a tenant or directory mismatch.




To resolve this issue, ensure that the mailbox is hosted in Exchange Online or configure REST API access for hybrid mailboxes. For more information, see [How to fix MailboxNotEnabledForRESTAPI](https://learn.microsoft.com/en-us/answers/questions/1657546/how-to-fix-mailboxnotenabledforrestapi) in the Microsoft documentation.

### Users see "Need admin approval" when they connect

When users connect to Microsoft Outlook from the Gemini Enterprise web app for the first time, Microsoft might show a **Need admin approval** screen. This happens if Gemini Enterprise requests administrator-level permissions, or if your Microsoft Entra tenant prohibits users from authorizing third-party apps without prior tenant-wide administrator consent.

To resolve this issue, an administrator must complete the first authorization. After that, other users in your tenant can connect without the approval screen.

  1. Ask a Microsoft Entra ID administrator who can grant tenant-wide consent to sign in to the Gemini Enterprise web app and connect to Microsoft Outlook.

  2. On the permissions screen, have the administrator select **Consent on behalf of your organization** , and then click **Accept**.

  3. Ask users to connect again.




For more information, see [Grant tenant-wide admin consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal) in the Microsoft Entra documentation.

**Note:** Deleting and re-creating the data store doesn't resolve this issue, because consent is granted in your Microsoft Entra tenant, not to the data store.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
