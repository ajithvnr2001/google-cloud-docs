---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/monday/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:40:46.264294+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/monday/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

The Monday connector for Gemini Enterprise lets you perform insert, delete, update, and read operations on Monday datasets.

## Supported actions

When the Monday connector is enabled, the end user can use natural language commands in Gemini Enterprise to perform the following actions.

Action | Description  
---|---  
Change item column values | Changes the column values of an item in Monday.  
Create board | Creates a new board in Monday.  
Create column | Creates a new column in Monday.  
Create dashboard | Creates a new dashboard in Monday.  
Create doc | Creates a new doc in Monday.  
Create form | Creates a new form in Monday.  
Create group | Creates a new group in Monday.  
Create item | Creates a new item in Monday.  
Create workspace | Creates a new workspace in Monday.  
**Note:** Additional read-only actions are also available.

## Required permissions

To enable Gemini Enterprise to perform federated search using the Monday data store, you need to enable following scopes:

Scope | Purpose  
---|---  
account:read | Allows the app to view account details and user information.  
assets:read | Allows the app to view and download files (assets) attached to items or updates.  
boards:read | Grants access to view board structures, column metadata, and all item data within boards.  
boards:write | Allows the app to create, modify, and delete boards, groups, columns, items, values, and widgets.  
docs:read | Allows the app to read the content and structure of Monday Workdocs.  
docs:write | Allows the app to create, edit, and delete Monday Workdocs.  
me:read | Allows the app to view information about the authenticated user.  
tags:read | Allows the app to view tags associated with items or boards.  
teams:read | Allows the app to view team information and structures.  
teams:write | Allows the app to create, update, and manage teams and team users.  
updates:read | Allows the app to read updates (posts), replies, and activity logs on items.  
updates:write | Allows the app to create and modify updates (posts) and comments on items.  
users:read | Allows the app to view user details and profiles within the account.  
users:write | Allows the app to update and modify user profiles and account details.  
webhooks:read | Allows the app to view the list of existing webhooks configured on a board.  
workspaces:read | Grants permission to view workspace names, IDs, and their internal structures.  
workspaces:write | Grants permission to create, update, and manage workspaces and folders.  
  
For information on how to configure these scopes, see [Set redirect URL and scopes](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/monday/monday-configuration#set-redirect-url-and-scopes).

## Limitations

This section outlines known issues and limitations that may affect your use of the Monday data store.

  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * Enforcing a VPC Service Controls perimeter on existing Monday data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).


  * The Monday data store is supported only in the `global`, `us`, and `eu` locations.



## What's next

  * To create and configure a connector with Monday, see [Set up a Monday data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/monday/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
