---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/create-data-store/
title: Connect a Google data source \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:40:45.128992+00:00
---

# Connect a Google data source  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/create-data-store/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Connect a Google data source Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a data store for Google data sources, such as Cloud Storage or Google Drive.

**Note:** Google Workspace data sources, such as Google Drive, Gmail, Google Calendar, and Google Chat, require a Google Workspace organization account and a Customer ID. Personal Google Accounts (consumer accounts ending in `@gmail.com`) don't have a customer ID and aren't supported for data connectors.

To import data from a third-party data source, see [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source).

### Generally Available

  * [Connect to BigQuery](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-bigquery) (ingestion mode)
  * [Import from Cloud Storage](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-cloud-storage)
  * [Sync from Google Drive](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive)
  * [Sync from Gmail](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gmail)
  * [Sync from Google Calendar](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gcal)
  * [Connect to Google Sites](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-sites)
  * [Sync people data](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-people)
  * [Connect to Cloud SQL](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-cloud-sql) (ingestion mode)
  * [Connect to Spanner](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-spanner) (ingestion mode)
  * [Import from Firestore](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-firestore)
  * [Import from Bigtable](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-bigtable)
  * [Connect toAlloyDB for PostgreSQL](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-alloydb) (ingestion mode)
  * [Create a data store using Terraform](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-terraform)



### Public Preview

  * [Sync from Google Chat](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gchat) (Preview)
  * [Import from Compute Engine](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/google-compute-engine) (Preview)
  * [Connect Google Stitch with data federation](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/googlestitch) (Preview)
  * [Sync from Google Groups](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-groups) (Preview)
  * [Import people data from a custom source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-people-custom) (Preview)
  * [Enable Gemini Notebook Enterprise as a search source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-notebooklm) (Preview)
  * [Connect to data from AlloyDB for PostgreSQL](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-alloydb-data) (Preview)
  * [Connect to data from BigQuery using federated query](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-bigquery) (Preview)
  * [Connect to data from Spanner using federated query](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-spanner) (Preview)
  * [Connect to data from Cloud SQL using federated query](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-cloud-sql) (Preview)
  * [Connect to data from AlloyDB for PostgreSQL using federated query](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-alloydb) (Preview)
  * [Use Knowledge Catalog with federated query connectors](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-knowledge-catalog) (Preview)



## Supported actions

Expand the data store name in the following list to reveal the available actions for each.

**Note:** Not all Google data stores support actions (for example, Google Sites is ingestion-only and doesn't support actions).

Google CalendarLaunch date | Action | Description  
---|---|---  
9/1/26 | Create event | Creates a new Google Calendar event.  
Delete event | Deletes an existing Google Calendar event.  
Get event | Fetches a Google Calendar event by ID.  
List calendars | Lists calendars in the user's Google Calendar account.  
List events | Lists events from a Google Calendar.  
Respond to event | Responds to a Google Calendar event invitation.  
Search events | Searches for Google Calendar events matching a query.  
Suggest time | Suggests a meeting time based on attendees' free/busy data.  
Update event | Updates an existing Google Calendar event.  
Google ChatLaunch date | Action | Description  
---|---|---  
9/1/26 | Add membership | Adds a member to a Google Chat conversation.  
Add reaction | Adds a reaction to a Google Chat message.  
Create conversation | Creates a Google Chat conversation (named space, direct message, or group direct message).  
List memberships | Lists memberships in a Google Chat conversation.  
List messages | Retrieves messages from a specified Google Chat conversation (space, direct message, or group direct message).  
List messages (Markdown) |  Retrieves messages from a specified Google Chat conversation in Markdown format.   
Remove membership | Removes a user membership from a Google Chat conversation.  
Remove reaction | Removes a reaction from a Google Chat message.  
Search conversations | Searches for Google Chat conversations by display name.  
Search messages | Searches for Google Chat messages using keywords and filters. Works across all spaces the user has access to, or can be scoped to a specific conversation.  
Send message | Sends a Google Chat message to a conversation.  
Send message (Markdown) |  Sends a Google Chat message to a conversation with Markdown formatting.   
Update membership | Updates a user membership in a Google Chat conversation.  
GmailLaunch date | Action | Description  
---|---|---  
9/1/26 | Batch label messages | Adds one or more labels to multiple Gmail messages in a single request.  
Batch label threads | Adds one or more labels to multiple Gmail threads in a single request.  
Batch unlabel messages | Removes one or more labels from multiple Gmail messages in a single request.  
Batch unlabel threads | Removes one or more labels from multiple Gmail threads in a single request.  
Create draft | Creates a new Gmail draft.  
Create filter | Creates a new Gmail filter.  
Create label | Creates a new label in Gmail.  
Delete filter | Deletes an existing Gmail filter.  
Delete label | Deletes an existing Gmail label.  
Forward | Forwards an existing Gmail message.  
Get message attachment | Fetches metadata for an attachment on a Gmail message.  
Get thread | Fetches the full contents of a Gmail thread.  
Label message | Adds one or more existing labels to a specific Gmail message.  
Label thread | Adds one or more existing labels to a specific Gmail thread.  
List drafts | Lists Gmail drafts in the user's mailbox.  
List filters | Lists Gmail filters in the user's mailbox.  
List labels | Lists labels defined in the user's Gmail mailbox.  
List threads | Lists Gmail threads in the user's mailbox.  
Reply | Replies to an existing Gmail message.  
Search threads | Searches for Gmail threads matching a query.  
Send message | Sends a new Gmail message.  
Unlabel message | Removes one or more existing labels from a specific Gmail message.  
Unlabel thread | Removes one or more existing labels from a specific Gmail thread.  
Update draft | Updates an existing Gmail draft.  
Update label | Updates an existing Gmail label.  
Google DriveLaunch date | Action | Description  
---|---|---  
9/1/26 | Copy file | Copies a file in Google Drive.  
Create file | Creates a new file in Google Drive.  
Download file content | Downloads the content of a Google Drive file.  
Get file metadata | Fetches metadata for a Google Drive file.  
Get file permissions | Lists the permissions on a Google Drive file.  
List recent files | Lists recent files in Google Drive.  
List shared drives | Lists shared drives in Google Drive.  
Read file content | Reads the contents of a Google Drive file.  
Search files | Searches for Google Drive files matching a query.  
Share file | Shares a Google Drive file with one or more users.  
Trash file | Moves a Google Drive file to the trash.  
Update file | Updates an existing Google Drive file.  
10/12/26 | Get cell values | Reads cell values from a Google Sheets spreadsheet.  
Get spreadsheet | Reads the contents and metadata of a Google Sheets spreadsheet.  
Insert dimension | Inserts rows or columns into a Google Sheets spreadsheet.  
Read document | Reads the contents of a Google Docs document.  
Read presentation | Reads the contents of a Google Slides presentation.  
Update cell values | Writes cell values to a Google Sheets spreadsheet.  
Update formulas | Writes formulas to a Google Sheets spreadsheet.  
Google StitchLaunch date | Action | Description  
---|---|---  
6/5/26 | Create project | Creates a new Stitch project.  
Update design system | Updates a design system.  
6/23/26 | Apply design system | Applies a design system to a project.  
Create design system | Creates a new design system.  
7/29/26 | Edit screens | Edits screens.  
  
## Troubleshoot data ingestion

If you're using [customer-managed encryption keys](https://docs.cloud.google.com/gemini/enterprise/docs/cmek) and data import fails (with error message `The caller does not have permission`), then make sure that the CryptoKey Encrypter/Decrypter IAM role (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) on the key has been granted to the Cloud Storage service agent. For more information, see [Before you begin](https://docs.cloud.google.com/gemini/enterprise/docs/cmek#before-you-begin) in "Customer-managed encryption keys".

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
