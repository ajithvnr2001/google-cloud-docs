---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:42:06.792910+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

The Jira Data Center data store for Gemini Enterprise lets you search and perform actions on your projects, issues, and users.

The Jira Data Center connector supports the following connection modes, which have different launch stages:

  * **Federated search and actions** : Generally available (GA).
  * **Data ingestion** : In Private Preview. You need to be on the allowlist to use the data ingestion data store. To be added to the allowlist, contact your [account team](https://cloud.google.com/tam) or the [sales team](https://cloud.google.com/contact).



## Supported Jira Data Center versions

The Jira Data Center connector supports Jira Data Center version `9.4.8` and later.

## Supported actions

When the Jira Data Center connector is enabled, the end user can use natural language commands in Gemini Enterprise to perform the following actions.

Action | Description  
---|---  
Create issue | Create a new issue or ticket.  
Update issue | Change the details of a ticket, like updating its summary, description, priority, or assignee.  
Change Issue Status | Change the status of an issue.  
Create comment | Add a comment on an issue.  
Update comment | Modify an existing comment on an issue.  
Download attachment | Download an attachment from an issue.  
Upload attachment | Add an attachment to an issue.  
**Notes** : 

  * Additional read-only actions are also available.
  * The maximum file size for file uploads and downloads in Gemini Enterprise is 200 MB.



## Required scopes

To enable Gemini Enterprise to perform necessary search, actions, and data ingestion, the following scopes are required:

Connection mode | Scopes | Purpose  
---|---|---  
Data ingestion | `READ` | Required to ingest Jira Data Center projects, comments, issues, attachments, and worklogs.  
Federated search and actions | `WRITE` | Required to perform search and actions like creating issues, updating issues, updating comments, and uploading attachments.  
  
For information about how to configure these scopes, see [Set up OAuth 2.0 authentication and OAuth scopes](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc/jira-dc-configuration#create-oauth-app-link).

## Limitations

  * Enforcing a VPC Service Controls perimeter on existing Jira Data Center data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).

  * When adding a data store to a new or existing application, it is recommended to add a data store with actions belonging to a single connector type. For example, don't associate two Jira Data Center data stores with actions enabled to the same application.

  * The Jira Data Center data store is supported only in Global, US, and EU locations.




## What's next

  * To create and configure a data store with Jira Data Center, see [Set up a Jira Data Center data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
