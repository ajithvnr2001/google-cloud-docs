---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/manage-actions/
title: Manage actions \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:43:22.388541+00:00
---

# Manage actions  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/manage-actions/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Manage actions Stay organized with collections  Save and categorize content based on your preferences. 

You can add actions either during data store creation or later. This page provides steps to add new actions after data store creation, and manage the list of actions.

**Note:** Users with data store configuration permissions can view its associated actions, provided that the data source includes default search or read-only actions, or that Gemini Enterprise has prebuilt actions for it. 

For more information, see the following:

  * Prebuilt actions supported for Google data stores: [Google data store actions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/create-data-store#supported_actions)
  * Prebuilt actions supported for third-party data stores: [Third-party data store actions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source#supported_actions)



## Add actions

### Console

To add new actions to the data store, follow these steps:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. In the navigation menu, click **Data Stores**.

  3. Select a data store of your choice.

  4. From the navigation menu, select **Actions**.

  5. On the **Actions** page:

     1. If actions were not added during data store creation, click **Enable actions**. Then, on the **Enable actions** page, to add new actions, do the following: 
        * For a federated data store: 
          1. Select the actions from the list.
          2. Click **Enable actions**.
        * For an ingestion data store: 
          1. Expand the **Authentication settings** section and provide the authentication details. 
             1. Click **Login** and sign in to the data store to verify your account.
             2. Click **Continue**.
          2. Optional: Expand the **Advanced settings** and provide the necessary details.
          3. Select the actions to enable.
          4. Click **Enable actions**.
     2. To add additional actions to the existing list, do the following: 
        1. Select the actions from the list.
        2. Click **Enable actions**.
  6. To reauthenticate using different credentials than those used for creating the data store, do the following:

     1. Click **Re-authenticate** on the **Actions** page.
     2. Provide the authentication details.
     3. Click **Login** to authorize Gemini Enterprise to access the data store.
     4. Click **Update** to update the new authentication details.
  7. To view or edit the data store parameters for actions, do the following:

     1. Click **View/Edit parameters** to edit connector-specific details. For example, for Microsoft Outlook, SharePoint, OneDrive, provide the Tenant ID.
     2. Click **Save** to update the parameter details.



## View actions

### Console

To view the list of actions for a data store, do the following:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. In the navigation menu, click **Data Stores**.

  3. Select the data store of your choice.

  4. From the navigation menu, select **Actions**. The actions you enabled during data store creation appear as a table on the **Actions** page.




## Disable actions

### Console

To disable actions, do the following: 

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. In the navigation menu, click **Data Stores**.

  3. Select the data store of your choice.

  4. Select **Actions** from the navigation menu.

  5. Select the actions to disable from the table.

  6. Click **Disable actions**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
