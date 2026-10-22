---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive/set-up-data-store/
title: Set up a Google Drive data store \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:36.449741+00:00
---

# Set up a Google Drive data store  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive/set-up-data-store/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Set up a Google Drive data store Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a data store and connect Google Drive to Gemini Enterprise. This connection allows Gemini Enterprise to directly retrieve information from Google Drive. Because data is not copied into the Gemini Enterprise index, you don't need to manage data storage.

## Before you begin

  * You must be signed into the Google Cloud console with the same account that you use for the Google Drive instance that you plan to connect. Gemini Enterprise uses your Google Workspace customer ID to connect to Google Drive. Personal Google Accounts (consumer accounts ending in `@gmail.com`) don't have a customer ID and aren't supported.

  * To enforce data source access control and secure data in Gemini Enterprise, ensure that you have [configured your identity provider](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider).

  * Verify that all the documents are accessible, either by placing them in a shared drive that is owned by the domain or by assigning the ownership to a user in the domain.

  * **Enable smart features** : In your Google Workspace account, turn on both **Smart features in Google Workspace** and **Smart features in other Google products**. For details, see [Turn Google Workspace smart features on or off](https://support.google.com/mail/answer/15604322).

  * **Allowlist the OAuth app (Administrators only)** : The Google Drive data store uses a Google-managed OAuth app to access your data. If your organization restricts OAuth app access, your Google Workspace administrator must add this app to your organization's allowlist. For details, see [Allowlist the Google-managed OAuth app](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive/config#allowlist-oauth-app).




### Create the Google Drive data store

To create the Google Drive data store, perform the following steps:

**Note:** When using data federation, the Google Drive connector only searches documents that are owned by the domain of the user who performs the search. Before setting up this connector, verify that all documents are accessible, either by placing them in a shared drive that is owned this domain or by setting ownership to a user in this domain.

  1. In the Google Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Select or [create](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project.

  3. In the navigation menu, click **Data stores**.

  4. Click add **Create data store**.

  5. In the **Source** section, search for **Google Drive** , and click **Select**.

  6. Optional: In the **Data** section, configure filters that scope which Google Drive content the data store searches. To configure filters using the Google Cloud console or REST API, select one of the following options:

### Console

     1. In the **Shared Drive IDs** field, the **Folder IDs** field, or both, enter the IDs that you want to filter on.
     2. For each field, choose **Include** to search only the specified IDs, or **Exclude** to omit them from search. Configure either **Include** mode or **Exclude** mode for each field, but not both.
     3. To locate a folder ID or shared drive ID, open the folder or shared drive in Google Drive and copy the ID from the URL. The URL follows this format: `https://drive.google.com/drive/folders/ID`. For example, `https://drive.google.com/drive/folders/123456789012345678901`.

### REST API

To create a data store with filters, call the [`setUpDataConnector`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations/setUpDataConnector) method.

Inclusion lists are set under `admin_filter` and exclusion lists are set under `admin_exclusion_filter`. For each filter type, populate the list under `admin_filter` or under `admin_exclusion_filter`, but not both.
    
    curl -X POST \
       -H "Authorization: Bearer $(gcloud auth print-access-token)" \
       -H "Content-Type: application/json" \
       -H "X-Goog-User-Project: PROJECT_ID" \
       "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION:setUpDataConnector" \
       -d '{
           "collectionId": "COLLECTION_ID",
           "collectionDisplayName": "COLLECTION_DISPLAY_NAME",
           "dataConnector": {
             "dataSource": "google_drive",
             "params": {
               "FILTER_TYPE": {
                 "FILTER_KEY": [
                   "FILTER_VALUE_1",
                   "FILTER_VALUE_2"
                 ]
               }
             },
             "entities": [
               {
                 "entityName": "google_drive"
               }
             ],
             "connectorModes": [
               "FEDERATED"
             ]
           }
       }'
       

Replace the following:

     * `PROJECT_ID`: the ID of your project. 
     * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
       * `us` for the US multi-region
       * `eu` for the EU multi-region
       * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
     * `LOCATION`: the multi-region of your data store: `global` or `us`. 
     * `COLLECTION_ID`: the unique ID of the data store. 
     * `COLLECTION_DISPLAY_NAME`: the display name of the data store. 
     * `FILTER_TYPE`: the type of filter, either `admin_filter` for inclusion or `admin_exclusion_filter` for exclusion. Populate the list under `admin_filter` or under `admin_exclusion_filter`, but not both. 
     * `FILTER_KEY`: the Drive entity to filter on, either `SharedDriveIds` or `FolderIds`. 
     * `FILTER_VALUE_1`, `FILTER_VALUE_2`: the shared drive IDs or folder IDs to filter on. 

**Note:** Filters scope search results only. Data stores created with the previous scoping options continue to work with their existing configuration. For more details on filter types, and to add or change filters after the data store is created, see [Add filters to a Google Drive data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive/add-filters-to-gdrive-data-store).
  7. In the **Actions** section, choose the actions from the list to enable them for the Google Drive connector.

**Note:** If you skip adding actions in this step, you can add them later. For more information, see [Add actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions#add-actions).

To manage the list of actions, see [Manage actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions).

  8. Click **Continue**.

  9. In the **Configuration** section: 

     1. From the **Multi-region** list, select the location for your data connector.
     2. In the **Data connector name** field, enter a name for your connector.
     3. If you selected `us` or `eu` as the location, configure the **Encryption settings** : 
        * Select **Google-managed encryption key** or **Cloud KMS key**.
        * If you selected **Cloud KMS key** : 
          * In the **Key management type** list, select the appropriate type.
          * In the **Cloud KMS key** list, select the key.
For more information, see [Customer-managed encryption keys](https://docs.cloud.google.com/gemini/enterprise/docs/cmek). 
  10. Optional: In the **Tag** field, enter a stable identifier for the data store. This identifier is used across different versions of the connector and becomes immutable after the data store is created, so choose a value that you don't need to change later.

  11. Optional: In the **Sensitive Data Protection policy** section, attach an existing [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview) policy to inspect and de-identify data that Gemini Enterprise retrieves through this data store. If your organization doesn't require a Sensitive Data Protection policy, you can skip this step.

  12. Click **Create**. Gemini Enterprise creates your data store and displays your data stores on the **Data Stores** page.




To verify the state of the data store, do the following:

  1. Navigate to the connector in the data store list and monitor its state until it changes to **Active**.
  2. When the data store state changes from **Creating** to **Active** , the Google Drive connector is ready to be used.



After creating the data store, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) and [connect it to the Google Drive data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store) before executing the query.

## Query execution

After you authorize Google Drive, when you enter a search query:

  1. Gemini Enterprise sends your search query to the Google Drive API.

  2. Gemini Enterprise blends the results with those from other sources and displays them.




## Error messages and troubleshooting

The following table describes error messages, including HTTP error codes and suggested troubleshooting steps, that you might encounter when working with this Google data source.

Error code | Error message | Description | Troubleshooting  
---|---|---|---  
403 Permission Denied | Searching using service account credentials isn't supported for Google Workspace data stores. | The engine being searched has Google Workspace data stores, and the credentials passed are of a service account. Searching using service account credentials on Google Workspace data stores isn't supported. | Call search using user credentials, or remove Google Workspace data stores from the engine.  
403 Permission Denied | Consumer accounts aren't supported for Google Workspace data stores. | Search is called using a consumer account (@gmail.com) credential, which isn't supported for Google Workspace data stores. | Remove Google Workspace data stores from the engine or use a managed Google Account.  
403 Permission Denied | Customer id mismatch for data store | Search is only allowed for users who belong to same organization as Google Workspace data stores. | Remove Google Workspace data stores from the engine or contact support if the user and Google Workspace data stores are meant to be in different organizations.  
403 Permission Denied | Workspace access for Agentspace disabled by organization administrator. | A Google Workspace administrator has disabled access to Google Workspace data for Gemini Enterprise. | Contact your Google Workspace administrator to [enable access](https://support.google.com/a/answer/16479199).  
400 Invalid Argument | Request contains an invalid argument. | This error occurs if the data connector name in the request doesn't meet the naming requirements. Verify the data connector name, ensuring it is 1 to 63 characters long, starts with a lowercase letter, ends with a lowercase letter or digit, and contains only lowercase letters, digits, hyphens, or underscores. For example, use a name like `cymbal-collection-123456789` instead of `123456789-cymbal-collection`.  
  
For common search issues that you encounter when querying your Google Drive data, see [Common search issues](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive#common-search-issues).

## What's next

  * To provide a user interface for querying your data, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) and [connect it to the Google Drive data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store).
  * To add or update folder and shared drive filters on your data store, see [Add filters to a Google Drive data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive/add-filters-to-gdrive-data-store).
  * To preview how your search results appear after your app is set up, see [Get search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).
  * To enable alerts for the data store, see [Configure alerts for third-party data stores](https://docs.cloud.google.com/gemini/enterprise/docs/configure-periodic-data-alerts).
  * If your app wasn't initially configured to include cross-domain documents, enable the **Include cross-domain documents** feature in the **Manage web app features** settings. For more information, see [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
