---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:43.589951+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

The Microsoft Outlook data store for Gemini Enterprise lets you search and perform actions on your emails, calendars, contacts, and Microsoft 365 files (Excel workbooks, Word documents, and PowerPoint presentations) stored in OneDrive and SharePoint.

**Note:** When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service.

## Supported Microsoft Outlook versions

The Microsoft Outlook data store supports Microsoft Graph API v1.0 with IDP integration.

## Supported actions

When the Microsoft Outlook data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions.

Action | Description  
---|---  
Create contact | Creates a new contact in Microsoft Outlook.  
Create event | Creates a new event.  
Download attachments | Downloads an attachment from a Microsoft Outlook email message.  
Send mail | Sends an email message. This includes sending email with attachments.  
Add attachments | Adds one or more attachments to an existing draft email message.  
Create message | Creates a new draft email message in the signed-in user's mailbox.  
Forward mail | Forwards an existing email message to one or more recipients.  
Move mail | Moves an email message to a different mail folder in the signed-in user's mailbox.  
Reply to message | Sends a reply to an existing email message in the signed-in user's mailbox.  
Update message | Updates an existing draft email message in the signed-in user's mailbox.  
Update contact | Updates an existing contact in Microsoft Outlook.  
Update event | Updates an existing event.  
Read Excel data | Lists workbooks, reads worksheets, tables, and rows from Excel (.xlsx) files stored in OneDrive or SharePoint.  
Edit Excel data | Adds and updates rows, creates worksheets and tables, and adds key columns in Excel (.xlsx) files stored in OneDrive or SharePoint.  
Create Word document | Creates a new Word (.docx) document in the user's OneDrive.  
Convert Word document to PDF | Converts a Word (.docx) document stored in OneDrive or SharePoint to PDF.  
Create PowerPoint presentation | Creates a new PowerPoint (.pptx) presentation in the user's OneDrive.  
Convert PowerPoint to PDF | Converts a PowerPoint (.pptx) presentation stored in OneDrive or SharePoint to PDF.  
Create calendar | Creates a new calendar for the signed-in user.  
Update calendar | Updates an existing calendar for the signed-in user.  
RSVP to event | Responds (accept, decline, or tentatively accept) to a calendar event invitation.  
**Notes** : 

  * Additional read-only actions are also available.
  * The maximum file size for file uploads and downloads in Gemini Enterprise is 25 MB.
  * Excel, Word, and PowerPoint actions require additional Microsoft Graph API permissions on the OneDrive or SharePoint files that the user is working with. For details, see [Required permissions](#required-permissions).



### Required permissions

The following table outlines the permissions required for Microsoft Outlook search and actions.

**Connection mode** | **Permission** | **Purpose**  
---|---|---  
**Federated search** | `Mail.Read`  
`Mail.Read.Shared`  
`Calendars.Read`  
`Contacts.Read` | (Delegated) Allows the data store to read the signed-in user's mailbox, email from shared mailboxes, calendar events, and contacts.  
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
`Mail.ReadWrite` | (Delegated) Allows the data store to create, read, update, move, and delete messages, and add attachments to messages. Required for the **Add attachments**, **Create message**, **Update message**, and **Move mail** actions.  
`Calendars.ReadWrite` | (Delegated) Allows the data store to create, read, update, and delete events in user calendars.  
`Contacts.ReadWrite` | (Delegated) Allows the data store to create, read, update, and delete user contacts.  
`User.Read` | (Delegated) Allows the data store to read the profile of signed-in users.  
**File productivity (Excel, Word, PowerPoint)** | `Files.Read.All` | (Delegated) Sufficient **only** for tools that read file metadata or download file content: listing Excel workbooks, reading Excel workbook metadata, and converting Word (.docx) or PowerPoint (.pptx) documents to PDF. Reads all files the user can access, including files stored in SharePoint sites the user has access to. **Not sufficient for Excel workbook content operations** (see next row).  
`Files.ReadWrite.All` | (Delegated) Required for **all** Excel workbook content operations (read **and** write), including get worksheets, get tables, get rows, get row, create worksheets and tables, add and update rows, and add key columns. Per the Microsoft Graph API reference for these endpoints (for example, [worksheet-list](https://learn.microsoft.com/graph/api/worksheet-list), [table-list](https://learn.microsoft.com/graph/api/table-list), [tablerow-list](https://learn.microsoft.com/graph/api/tablerow-list)), the accepted delegated permission is `Files.ReadWrite`. `Files.ReadWrite.All` grants the same capability across all drives the user can access (personal OneDrive and any SharePoint document library the user has access to). Also required for creating Word and PowerPoint documents in the user's OneDrive.  
`User.Read` | (Delegated) Required to resolve the signed-in user's OneDrive location for file operations.  
**Tasks (Outlook to-do lists and tasks)** | `Tasks.Read` | (Delegated) Required for read operations on the signed-in user's Outlook task lists and tasks (list task lists, list tasks, get task).  
`Tasks.ReadWrite` | (Delegated) Required for write operations: creating, updating, and deleting tasks in the signed-in user's Outlook task lists.  
**Users and directory (delegated enumeration)** | `User.ReadBasic.All` | (Delegated) Required for tools that enumerate or look up profiles of other users in the organization (Get User, List Users, and tools that operate on other users' mailboxes or calendars).  
**Note:** The file-productivity actions above require the user's tenant admin to grant the corresponding Microsoft Graph API permissions on the OAuth app registration. If these permissions are not granted, requests to Excel, Word, and PowerPoint tools fail with an HTTP 403 `accessDenied` error. **Recommended:** grant `Files.ReadWrite.All`, which covers every file-productivity tool. If you only need Word or PowerPoint PDF conversion and Excel workbook listing/metadata (no worksheet, table, or row access), `Files.Read.All` alone is sufficient. For the driveItem-based operations (Word/PowerPoint PDF conversion, listing Excel workbooks, reading Excel workbook metadata), Microsoft Graph also documents `Sites.Read.All` or `Sites.ReadWrite.All` as accepted alternatives (see [driveItem-get](https://learn.microsoft.com/graph/api/driveitem-get) and [driveItem-get-content-format](https://learn.microsoft.com/graph/api/driveitem-get-content-format)). See [Configure Microsoft Outlook and set the necessary permissions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook/third-party-config#configure-api-permissions) for the setup steps. **Note:** Missing `Tasks.Read` or `Tasks.ReadWrite` causes Outlook task tools to fail with HTTP 403 `notAllowed`. Missing `User.ReadBasic.All` (delegated) causes user-lookup tools to fail with HTTP 403 `Authorization_RequestDenied`. Tenants that need higher-privileged user access can substitute `User.Read.All` or `Directory.Read.All` for `User.ReadBasic.All`. 

For information on how to add the permissions for Microsoft Outlook, see [Configure Microsoft Outlook and set the necessary permissions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook/third-party-config#configure-api-permissions).

## Rate limits for data ingestion

The request volume limit is 10,000 API requests per 10-minute period. These rate limits apply exclusively to the Microsoft Outlook data store when you choose to use ingestion as the connection mode.

## Limitations

This section outlines known issues and limitations that may affect your use of the Microsoft Outlook data store.

  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * Enforcing a VPC Service Controls perimeter on existing Microsoft Outlook data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).


  * The Microsoft Outlook data store is supported only in the `global`, `us`, and `eu` locations.


  * The Microsoft Outlook data store can process one transaction per second, per node, and throttles any transactions beyond this limit.

  * The Microsoft Outlook data store's ability to retry on rate-limit exceeded errors depends on receiving a _retry-after_ value from the Microsoft Graph API, which is only provided for the Outlook data store. The default number of retry attempts is three.

  * The Microsoft Outlook data store's throughput is limited by API call restrictions imposed by Microsoft Graph. Limits apply to each app ID and mailbox combination—that is, a specific app accessing a specific user or group mailbox. Exceeding the limit for one mailbox doesn't affect the ability of the application to access another mailbox.

  * The Microsoft Outlook data store maps one-to-one with a single Azure Tenant ID. It can't span multiple, isolated Microsoft 365 tenants within a Multi-Tenant Organization (MTO). You must create a dedicated data store for each distinct tenant.

  * Mailboxes must be fully migrated to Exchange Online. Mailboxes hosted on-premise in a Hybrid Exchange environment aren't accessible through the Microsoft Graph API. Attempts to query these or cross-tenant mailboxes can result in a `MailboxNotEnabledForRESTAPI` error.

  * The Microsoft Outlook data store can process one transaction per second per node and throttles any transactions beyond this limit.




## What's next

  * To create and configure a data store with Microsoft Outlook, see [Set up a Microsoft Outlook data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
