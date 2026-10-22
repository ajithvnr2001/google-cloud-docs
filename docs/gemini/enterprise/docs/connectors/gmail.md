---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gmail/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:25.055488+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gmail/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

The Gmail connector for Gemini Enterprise lets you search and perform actions on your Gmail data using natural language commands.

**Note:** Gemini Enterprise has released new Google Workspace data connectors for Gmail, Google Drive, Google Chat, and Google Calendar. The new connectors use a Google-managed OAuth app, so you no longer create your own OAuth client or supply a client ID and client secret when you create the data store. For Gmail setup instructions, see [Set up a Gmail data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gmail/set-up-data-store).

## Supported actions

When the Gmail data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions.

Action | Description  
---|---  
Send message | Sends a new Gmail message.  
Reply | Replies to an existing Gmail message.  
Forward | Forwards an existing Gmail message.  
Create draft | Creates a new Gmail draft.  
Update draft | Updates an existing Gmail draft.  
List drafts | Lists Gmail drafts in the user's mailbox.  
List threads | Lists Gmail threads in the user's mailbox.  
Search threads | Searches for Gmail threads matching a query.  
Get thread | Fetches the full contents of a Gmail thread.  
Get message attachment | Fetches metadata for an attachment on a Gmail message.  
Create label | Creates a new label in Gmail.  
Update label | Updates an existing Gmail label.  
Delete label | Deletes an existing Gmail label.  
List labels | Lists labels defined in the user's Gmail mailbox.  
Label message | Adds one or more existing labels to a specific Gmail message.  
Unlabel message | Removes one or more existing labels from a specific Gmail message.  
Batch label messages | Adds one or more labels to multiple Gmail messages in a single request.  
Batch unlabel messages | Removes one or more labels from multiple Gmail messages in a single request.  
Label thread | Adds one or more existing labels to a specific Gmail thread.  
Unlabel thread | Removes one or more existing labels from a specific Gmail thread.  
Batch label threads | Adds one or more labels to multiple Gmail threads in a single request.  
Batch unlabel threads | Removes one or more labels from multiple Gmail threads in a single request.  
Create filter | Creates a new Gmail filter.  
List filters | Lists Gmail filters in the user's mailbox.  
Delete filter | Deletes an existing Gmail filter.  
**Notes** : 

  * The maximum file size for file uploads and downloads in Gemini Enterprise is 50 MB.



### Required scopes

The Google-managed OAuth app requests the following OAuth scopes. Users grant these scopes when they authorize the connector:

Scope | Purpose  
---|---  
`https://www.googleapis.com/auth/gmail.readonly` | Search and read Gmail messages, threads, drafts, labels, and attachments.  
`https://www.googleapis.com/auth/gmail.send` | Send and forward Gmail messages and replies.  
`https://www.googleapis.com/auth/gmail.compose` | Create and update Gmail drafts.  
`https://www.googleapis.com/auth/gmail.modify` | Add and remove labels on Gmail messages and threads.  
`https://www.googleapis.com/auth/gmail.labels` | Create, update, and delete Gmail labels.  
`https://www.googleapis.com/auth/gmail.settings.basic` | Create, list, and delete Gmail filters.  
`https://www.googleapis.com/auth/userinfo.email`, `https://www.googleapis.com/auth/userinfo.profile`, `openid` | Identify the authorizing user.  
  
## Limitations

  * The Gmail data store is supported only in the `global`, `us`, and `eu` locations.



  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * If you use security controls, be aware of their limitations related to data in Gmail, as discussed in the following table:

Security control | Note the following  
---|---  
[Data Residency (DRZ)](https://docs.cloud.google.com/gemini/enterprise/docs/locations) | Gemini Enterprise only guarantees data residency in Google Cloud. For information about data residency and Gmail, see Google Workspace compliance guidance and documentation, including [Data regions for Google Workspace](https://support.google.com/a/answer/9223653). Also review examples like [Choose the region where data is stored](https://support.google.com/a/topic/7631290) and [ Digital sovereignty](https://workspace.google.com/intl/en_in/security/digital-sovereignty/).   
[Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/gemini/enterprise/docs/cmek) |  Your keys only encrypt data within Google Cloud. Cloud Key Management Service controls don't apply to data stored in Gmail.   
[ Access Transparency](https://docs.cloud.google.com/gemini/enterprise/docs/access-transparency) |  Access Transparency logs actions taken by Google personnel on the Google Cloud project. You'll also need to review the Access Transparency logs created by Google Workspace. For more information, see [Access Transparency log events](https://support.google.com/a/answer/9230979) in the Google Workspace Admin Help documentation.   



## What's next

  * To create and configure a data store with Gmail, see [Set up a Gmail data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gmail/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
