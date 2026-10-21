---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gchat/set-up-data-store/
title: Set up a Google Chat data store \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:21:15.187158+00:00
---

# Set up a Google Chat data store  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gchat/set-up-data-store/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Set up a Google Chat data store Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a data store and connect Google Chat to Gemini Enterprise.

## Before you begin

  * Sign in to the Google Cloud console using the same account associated with the Google Workspace instance you intend to connect. Gemini Enterprise uses your Google Workspace customer ID to connect to Google Chat. Personal Google Accounts (consumer accounts ending in `@gmail.com`) don't have a customer ID and aren't supported.

  * To enforce data source access control and secure data in Gemini Enterprise, ensure that you have [configured your identity provider](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider).

  * **Enable smart features** : In your Google Workspace account, turn on both **Smart features in Google Workspace** and **Smart features in other Google products**. For details, see [Turn Google Workspace smart features on or off](https://support.google.com/mail/answer/15604322).

  * **Allowlist the OAuth app (Administrators only)** : The Google Chat data store uses a Google-managed OAuth app to access your data. If your organization restricts OAuth app access, your Google Workspace administrator must add this app to your organization's allowlist. For details, see [Allowlist the Google-managed OAuth app](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gchat/config#allowlist-oauth-app).




## Create the Google Chat data store

To create the Google Chat data store, perform the following steps:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Select or [create](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project.

  3. In the navigation menu, click **Data stores**.

  4. Click + **Create data store**.

  5. In the **Source** , search for **Google Chat** , and click **Select**.

**Note:** Administrator filters (message recency and direct-message exclusion) are no longer supported for new Google Chat data stores. Data stores that were created before this change continue to work with their existing filters. To manage filters on those legacy data stores, see [Add filters to a Google Chat data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gchat/add-filters-to-gchat-data-store).
  6. In the **Actions** section, choose the actions from the list to enable them for the Google Chat connector.

**Note:** If you skip adding actions in this step, you can add them later. For more information, see [Add actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions#add-actions).

To manage the list of actions, see [Manage actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions).

  7. Click **Continue**.

  8. In the **Configuration** section: 

     1. From the **Multi-region** list, select the location for your data connector.
     2. In the **Data connector name** field, enter a name for your connector.
     3. If you selected `us` or `eu` as the location, configure the **Encryption settings** : 
        * Select **Google-managed encryption key** or **Cloud KMS key**.
        * If you selected **Cloud KMS key** : 
          * In the **Key management type** list, select the appropriate type.
          * In the **Cloud KMS key** list, select the key.
For more information, see [Customer-managed encryption keys](https://docs.cloud.google.com/gemini/enterprise/docs/cmek). 
  9. Optional: In the **Tag** field, enter a stable identifier for the data store. This identifier is used across different versions of the connector and becomes immutable after the data store is created, so choose a value that you don't need to change later.

  10. Optional: In the **Sensitive Data Protection policy** section, attach an existing [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview) policy to inspect and de-identify data that Gemini Enterprise retrieves through this data store. If your organization doesn't require a Sensitive Data Protection policy, you can skip this step.

  11. Click **Create**. Gemini Enterprise creates your data store and displays your data stores on the **Data Stores** page.




On the **Data Stores** page, click your data store name to see the status. When the data store state changes from **Creating** to **Active** , the Google Chat connector is ready to be used.

After creating the data store, connect the data store you just created to an existing app or [create a new app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) and [connect](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store) it to the new app, and [authorize](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store#user_authorization) Gemini Enterprise to access Google Chat before executing any queries.

## Query Execution

**Note:** For optimal response quality when querying Google Chat data, we recommend using Gemini 3.1 version.

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store.

After you authorize Google Chat and send a search query to Gemini Enterprise:

  * Gemini Enterprise sends your search query directly to the Google Chat API.
  * Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result.



## Error messages and troubleshooting

The following table describes common error messages that you might encounter when you work with the Google Chat connector, which includes possible HTTP error codes and suggested troubleshooting steps.

Error code | Error message | Description | Troubleshooting  
---|---|---|---  
403 (Permission Denied) | Search by using service account credentials isn't supported for Google Workspace data stores. | The engine being searched has Google Workspace data stores, and the credentials passed are of a service account. Search by using service account credentials on Google Workspace data stores isn't supported. | Call search using user credentials, or remove Google Workspace data stores from the engine.  
403 (Permission Denied) | Consumer accounts aren't supported for Google Workspace data stores. | Search is called using a consumer account (@gmail.com) credential, which isn't supported for Google Workspace data stores. | Remove Google Workspace data stores from the engine or use a managed Google Account.  
403 (Permission Denied) | Customer ID mismatch for data store | Search is only allowed for users who belong to the same organization as Google Workspace data stores. | Remove Google Workspace data stores from the engine or contact support if the user and Google Workspace data stores are meant to be in different organizations.  
403 (Permission Denied) | Workspace access for Agent Space disabled by organization administrator. | A Google Workspace administrator has disabled access to Google Workspace data for Gemini Enterprise. | Contact your Google Workspace administrator to [enable access](https://support.google.com/a/answer/16479199).  
  
## What's next

  * To provide a user interface for querying your Google Chat data, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) and [connect it to the Google Chat data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store).

  * To preview how your search results appear after your app is set up, see [Get search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
