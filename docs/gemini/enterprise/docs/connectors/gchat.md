---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gchat/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:41:51.021700+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gchat/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Public preview:** The federated search and actions features are in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

The Google Chat connector for Gemini Enterprise lets you search and perform actions on your Google Chat data using natural language commands.

**Note:** Gemini Enterprise has released new Google Workspace data connectors for Google Chat, Google Drive, Gmail, and Google Calendar. The new connectors use a Google-managed OAuth app, so you no longer create your own OAuth client or supply a client ID and client secret when you create the data store. For Google Chat setup instructions, see [Set up a Google Chat data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gchat/set-up-data-store).

## Supported actions

When the Google Chat data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions.

Action | Description  
---|---  
Send message | Sends a Google Chat message to a conversation.  
Send message (Markdown) | Sends a Google Chat message to a conversation with Markdown formatting.  
List messages | Retrieves messages from a specified Google Chat conversation (space, direct message, or group direct message).  
List messages (Markdown) | Retrieves messages from a specified Google Chat conversation in Markdown format.  
Search messages | Searches for Google Chat messages using keywords and filters. Works across all spaces the user has access to, or can be scoped to a specific conversation.  
Search conversations | Searches for Google Chat conversations by display name.  
Create conversation | Creates a Google Chat conversation (named space, direct message, or group direct message).  
Add reaction | Adds a reaction to a Google Chat message.  
Remove reaction | Removes a reaction from a Google Chat message.  
Add membership | Adds a member to a Google Chat conversation.  
Remove membership | Removes a user membership from a Google Chat conversation.  
Update membership | Updates a user membership in a Google Chat conversation.  
List memberships | Lists memberships in a Google Chat conversation.  
  
## Required permissions

The Google-managed OAuth app requests the following OAuth scopes. Users grant these scopes when they authorize the connector:

Scope | Purpose  
---|---  
`https://www.googleapis.com/auth/chat.spaces.readonly` | List and search Google Chat conversations.  
`https://www.googleapis.com/auth/chat.messages.readonly` | Read and search Google Chat messages.  
`https://www.googleapis.com/auth/chat.memberships.readonly` | List memberships in a Google Chat conversation.  
`https://www.googleapis.com/auth/chat.users.readstate.readonly` | Read the user's read state for Google Chat messages.  
`https://www.googleapis.com/auth/chat.messages.create` | Send Google Chat messages.  
`https://www.googleapis.com/auth/chat.spaces.create` | Create Google Chat conversations.  
`https://www.googleapis.com/auth/chat.memberships` | Add, remove, and update members in a Google Chat conversation.  
`https://www.googleapis.com/auth/chat.messages.reactions.create` | Add a reaction to a Google Chat message.  
`https://www.googleapis.com/auth/chat.messages.reactions` | Remove a reaction from a Google Chat message.  
  
## Limitations

  * The Google Chat data store is supported only in the `global`, `us`, and `eu` locations.



  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * If you use security controls, be aware of their limitations related to data in Google Chat, as discussed in the following table:

Security control | Note the following  
---|---  
[Data Residency (DRZ)](https://docs.cloud.google.com/gemini/enterprise/docs/locations) | Gemini Enterprise only guarantees data residency in Google Cloud. For information about data residency and Google Chat, see Google Workspace compliance guidance and documentation, including [Data regions for Google Workspace](https://support.google.com/a/answer/9223653). Also review examples like [Choose the region where data is stored](https://support.google.com/a/topic/7631290) and [ Digital sovereignty](https://workspace.google.com/intl/en_in/security/digital-sovereignty/).   
[Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/gemini/enterprise/docs/cmek) |  Your keys only encrypt data within Google Cloud. Cloud Key Management Service controls don't apply to data stored in Google Chat.   
[ Access Transparency](https://docs.cloud.google.com/gemini/enterprise/docs/access-transparency) |  Access Transparency logs actions taken by Google personnel on the Google Cloud project. You'll also need to review the Access Transparency logs created by Google Workspace. For more information, see [Access Transparency log events](https://support.google.com/a/answer/9230979) in the Google Workspace Admin Help documentation.   



## What's next

  * To create and configure a data store with Google Chat, see [Set up a Google Chat data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gchat/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
