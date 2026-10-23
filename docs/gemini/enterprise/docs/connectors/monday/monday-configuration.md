---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/monday/monday-configuration/
title: Monday configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:38.837538+00:00
---

# Monday configuration  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/monday/monday-configuration/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Monday configuration Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up and configure a third-party application before creating the Monday data store.

## Create OAuth app

  1. Sign in to your Monday.com account.

  2. Click the profile icon and select **Developers**.

  3. In the **My apps** page, click **Create app**.

  4. In the **Create new app** dialog, enter an **App name** and **App slug** and click **Submit**.

  5. Click the app that you created.

  6. In the application page, copy the **Client ID** and **Client secret** , and store them securely for later use.




## Set redirect URL and scopes

After creating the OAuth app, configure its redirect URL and scopes:

  1. In the **My apps** page, click the app that you created in previous section.

  2. Open the OAuth application page.

  3. In the navigation menu, go to **Build** > **OAuth & permissions**.

  4. In the **OAuth & permissions** page, do the following:

a. Select the **Redirect URL** tab.

b. In the **Redirect URL** field, enter `https://vertexaisearch.cloud.google.com/oauth-redirect`.

c. Select the **Scopes** tab.

d. Select the following scopes:

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
  
e. Click **Save scopes**.




## Activate and install the app

To ensure the app is accessible to your organization, you must promote the version to "Live" and complete the installation.

  1. In the navigation menu, go to **Build** > **App versions**.

  2. Locate the current version of your app and click **Promote to live**.

  3. In the navigation menu, go to **Publish** > **Install**.

  4. Click **Install App**. This authorizes the application for use within your Monday.com organization.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
