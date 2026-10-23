---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gcal/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:07.836534+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gcal/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

The Google Calendar connector for Gemini Enterprise lets you search and perform actions on your events and calendars.

**Note:** Gemini Enterprise has released new Google Workspace data connectors for Google Calendar, Google Drive, Gmail, and Google Chat. The new connectors use a Google-managed OAuth app, so you no longer create your own OAuth client or supply a client ID and client secret when you create the data store. For Google Calendar setup instructions, see [Set up a Google Calendar connector](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gcal/set-up-data-store).

## Supported Google Calendar versions

The Google Calendar data store supports Google Calendar version v3 and later.

## Supported actions

When the Google Calendar data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions.

Action | Description  
---|---  
Create event | Creates a new Google Calendar event.  
Update event | Updates an existing Google Calendar event.  
Delete event | Deletes an existing Google Calendar event.  
Get event | Fetches a Google Calendar event by ID.  
Respond to event | Responds to a Google Calendar event invitation.  
List events | Lists events from a Google Calendar.  
Search events | Searches for Google Calendar events matching a query.  
List calendars | Lists calendars in the user's Google Calendar account.  
Suggest time | Suggests a meeting time based on attendees' free/busy data.  
**Notes** : 

  * Google Calendar doesn't support file uploads and downloads.



### Required scopes

The Google-managed OAuth app requests the following OAuth scopes. Users grant these scopes when they authorize the connector:

Scope | Purpose  
---|---  
`https://www.googleapis.com/auth/calendar.calendarlist.readonly` | List calendars in the user's Google Calendar account.  
`https://www.googleapis.com/auth/calendar.events.readonly` | Read and search Google Calendar events.  
`https://www.googleapis.com/auth/calendar.readonly` | Read Google Calendar metadata and event attachments.  
`https://www.googleapis.com/auth/calendar.events` | Create, update, delete, and respond to Google Calendar events.  
`https://www.googleapis.com/auth/calendar.events.freebusy` | Query attendees' free/busy data to suggest meeting times.  
`https://www.googleapis.com/auth/calendar.freebusy` | Query free/busy information for a calendar.  
`https://www.googleapis.com/auth/calendar` | Perform write operations on Google Calendar data.  
  
## Limitations

  * The Google Calendar data store is supported only in the `global`, `us`, and `eu` locations.



  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * If you use security controls, be aware of their limitations related to data in Google Calendar, as discussed in the following table:

Security control | Note the following  
---|---  
[Data Residency (DRZ)](https://docs.cloud.google.com/gemini/enterprise/docs/locations) | Gemini Enterprise only guarantees data residency in Google Cloud. For information about data residency and Google Calendar, see Google Workspace compliance guidance and documentation, including [Data regions for Google Workspace](https://support.google.com/a/answer/9223653). Also review examples like [Choose the region where data is stored](https://support.google.com/a/topic/7631290) and [ Digital sovereignty](https://workspace.google.com/intl/en_in/security/digital-sovereignty/).   
[Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/gemini/enterprise/docs/cmek) |  Your keys only encrypt data within Google Cloud. Cloud Key Management Service controls don't apply to data stored in Google Calendar.   
[ Access Transparency](https://docs.cloud.google.com/gemini/enterprise/docs/access-transparency) |  Access Transparency logs actions taken by Google personnel on the Google Cloud project. You'll also need to review the Access Transparency logs created by Google Workspace. For more information, see [Access Transparency log events](https://support.google.com/a/answer/9230979) in the Google Workspace Admin Help documentation.   



## What's next

  * To create and configure a connector with Google Calendar, see [Set up a Google Calendar connector](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gcal/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
