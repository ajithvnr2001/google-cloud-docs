---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive/add-filters-to-gdrive-data-store/
title: Add filters to a Google Drive data store \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:33.710155+00:00
---

# Add filters to a Google Drive data store  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive/add-filters-to-gdrive-data-store/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Add filters to a Google Drive data store Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to add filters to your Google Drive data stores in Gemini Enterprise. Filters let you control which Google Drive content is available to the Assistant by restricting search to specific locations or explicitly excluding specific locations from search.

**Important:** Google Drive filters apply only to search results. For details, see Action behavior with filters.

## Filter types

The Google Drive data store supports the following filter types:

  * **Folder filter** : Limits search to a specific set of Google Drive folders. You configure this filter in one of two modes: 
    * **Include** : Search is scoped to only the folders that you list. Content in any other folder isn't included.
    * **Exclude** : The folders that you list are explicitly removed from search. Content in all other folders remains available.
  * **Shared drive filter** : Limits search to a specific set of shared drives. You configure this filter in one of two modes: 
    * **Include** : Search is scoped to only the shared drives that you list. Content in any other shared drive isn't included.
    * **Exclude** : The shared drives that you list are explicitly removed from search. Content in all other shared drives remains available.



For each filter type, you configure the **Include** mode or **Exclude** mode, not both at the same time.

Filters match nested content. Both keys match recursively: a file is in scope if the specified shared drive or folder appears in its ancestor chain.

To find a folder ID or shared drive ID, open the folder or shared drive in Google Drive and copy the ID from the URL. The URL follows this format: `https://drive.google.com/drive/folders/ID`. For example, `https://drive.google.com/drive/folders/123456789012345678901`.

**Note:** Data stores created before this feature was released keep working with their original folder and shared drive scoping. They aren't affected by these filters. You can't migrate an existing data store to the filter modes described on this page. To use these modes, create a Google Drive data store.

## Action behavior with filters

While a filter is active on the connection, the connector applies it to the **Search files** action only.

  * **Search files** returns only files that match the filter. The filter is combined with the user's search terms, so a user can't widen the scope through the query.
  * **All other Google Drive actions are unaffected by filters.** An enabled action other than **Search files** can still be applied to a file outside the filter if the user has permission to that file in Google Drive.

**Note:** Filters only take effect on a data store that has the **Search files** action enabled. You choose which actions to enable when you create the data store, or later on the **Actions** page. If you rely on filters to scope what the assistant can reach, enable only **Search files** and leave the other actions disabled. For more information, see [Manage actions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/manage-actions).

File access is always governed by the user's Google Drive permissions. Filters never grant additional access. However, filters only restrict **Search files** results. Users can still reach out-of-scope files through other enabled actions if they have permission to those files in Google Drive.

**Note:** Don't rely on Google Drive filters as a security or data-loss-prevention boundary. Use them to focus assistant search on the content that matters. To restrict which files users can reach at all, use Google Drive sharing permissions.

## Limitations

  * **Filters apply to search only.** See Action behavior with filters.
  * **Search indexing delay** : Recent changes to folders, such as moving files or creating new folders, can take a few moments to appear in search results. Until then, filters apply the file's previous folder location.
  * **Folder depth limit** : Searches might not find files nested deeper than 10 folder levels.



## Update filters in an existing data store

You can update filters in an existing data store using the Google Cloud console or API.

### Console

To add or update filter configurations: 

  1. In the Google Cloud console navigation menu, click **Data stores**.
  2. Select your Google Drive data store.
  3. Click **View/edit parameters**.
  4. In the **View/edit parameters** panel, add or update the folder filter and shared drive filter. For each filter, choose **Include** or **Exclude** mode and provide the folder IDs or shared drive IDs.
  5. Click **Save**.



### REST

To add or update filters in an existing Google Drive data store, call the [`updateDataConnector`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections/updateDataConnector) method.

Inclusion lists are set under `admin_filter` and exclusion lists are set under `admin_exclusion_filter`. For each filter type, populate the list under `admin_filter` or under `admin_exclusion_filter`, but not both.

In the request body, you must include all filter lists that you want to keep in the data store, including filter lists that you aren't updating.
    
    
        curl -X PATCH \
            -H "Authorization: Bearer $(gcloud auth print-access-token)" \
            -H "Content-Type: application/json" \
            -H "X-Goog-User-Project: PROJECT_ID" \
            "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/COLLECTION_ID/dataConnector?updateMask=params" \
            -d '{
              "params": {
                "admin_filter": {
                  "SharedDriveIds": INCLUDED_SHARED_DRIVE_IDS,
                  "FolderIds": INCLUDED_FOLDER_IDS
                },
                "admin_exclusion_filter": {
                  "SharedDriveIds": EXCLUDED_SHARED_DRIVE_IDS,
                  "FolderIds": EXCLUDED_FOLDER_IDS
                }
              }
            }'
        

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `ENDPOINT_LOCATION`: The region of your application. For example, `us` or `eu`.
  * `LOCATION`: The location of your data connector. It must be `global` or `us`.
  * `COLLECTION_ID`: The ID of the collection that contains your data connector. The collection ID is provided when you create a data store. The collection ID isn't the same as the data store ID.
  * `INCLUDED_SHARED_DRIVE_IDS`: A list of shared drive IDs to include in search, for example `["0ABCdEfGhIjKlMnOpQ"]`. Use an empty list `[]` if you aren't setting an inclusion list for shared drives.
  * `INCLUDED_FOLDER_IDS`: A list of folder IDs to include in search, for example `["1AbCdEfGhIjKlMnOpQrStUvWxYz"]`. Use an empty list `[]` if you aren't setting an inclusion list for folders.
  * `EXCLUDED_SHARED_DRIVE_IDS`: A list of shared drive IDs to exclude from search. Use an empty list `[]` if you aren't setting an exclusion list for shared drives.
  * `EXCLUDED_FOLDER_IDS`: A list of folder IDs to exclude from search. Use an empty list `[]` if you aren't setting an exclusion list for folders.



## Verify that the data store includes the filters

You can get the details of the data store to confirm that the filters you added or updated are correctly applied using the Google Cloud console or the API.

### Console

To view the existing filter configurations: 

  1. In the Google Cloud console navigation menu, click **Data stores**.
  2. Select your Google Drive data store.
  3. Click **View/edit parameters**.



In the **View/edit parameters** panel, the existing filters applied to the data store are displayed.

### REST

To verify data store settings, call the [`getDataConnector`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections/getDataConnector) method:
    
    
        curl -X GET \
            -H "Authorization: Bearer $(gcloud auth print-access-token)" \
            -H "X-Goog-User-Project: PROJECT_ID" \
            "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/COLLECTION_ID/dataConnector"
        

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `ENDPOINT_LOCATION`: The region of your application. For example, `us` or `eu`.
  * `LOCATION`: The location of your data connector. It must be `global` or `us`.
  * `COLLECTION_ID`: The ID of the collection that contains your data connector. The collection ID is provided when you create a data store. The collection ID isn't the same as the data store ID.



In the response, view the `admin_filter` or `admin_exclusion_filter` fields in `params` to verify the filters.

## Remove filters from a data store

When managing your data store configuration, you might need to clear specific filters or reset all filters. You can remove filters from an existing data store using the Google Cloud console or API.

### Console

To remove existing filter configurations: 

  1. In the Google Cloud console navigation menu, click **Data stores**.
  2. Select your Google Drive data store.
  3. Click **View/edit parameters**.
  4. In the **View/edit parameters** panel, delete the folder IDs or shared drive IDs from the filters that you want to remove.
  5. Click **Save**.



### REST

To remove filters from an existing Google Drive data store, call the [`updateDataConnector`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections/updateDataConnector) method.

#### Remove a specific filter

To remove a specific filter while keeping others, send an **update request**. Include the filter lists that you want to retain and set an empty list `[]` for the filter that you want to remove.

For example, to remove the folder inclusion list while retaining the shared drive inclusion list, use the following command:
    
    
        curl -X PATCH \
            -H "Authorization: Bearer $(gcloud auth print-access-token)" \
            -H "Content-Type: application/json" \
            -H "X-Goog-User-Project: PROJECT_ID" \
            "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/COLLECTION_ID/dataConnector?updateMask=params" \
            -d '{
              "params": {
                "admin_filter": {
                  "SharedDriveIds": INCLUDED_SHARED_DRIVE_IDS,
                  "FolderIds": []
                }
              }
            }'
        

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `ENDPOINT_LOCATION`: The region of your application. For example, `us` or `eu`.
  * `LOCATION`: The location of your data connector. It must be `global` or `us`.
  * `COLLECTION_ID`: The ID of the collection that contains your data connector. The collection ID is provided when you create a data store. The collection ID isn't the same as the data store ID.
  * `INCLUDED_SHARED_DRIVE_IDS`: A list of shared drive IDs to include in search, for example `["0ABCdEfGhIjKlMnOpQ"]`.

**Note:** Any filter list that you don't include in the request is overwritten and disabled.

#### Remove all filters

To remove all filters from the data store, send an update request with empty lists for every filter under both `admin_filter` and `admin_exclusion_filter`:
    
    
        curl -X PATCH \
            -H "Authorization: Bearer $(gcloud auth print-access-token)" \
            -H "Content-Type: application/json" \
            -H "X-Goog-User-Project: PROJECT_ID" \
            "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/COLLECTION_ID/dataConnector?updateMask=params" \
            -d '{
              "params": {
                "admin_filter": {
                  "SharedDriveIds": [],
                  "FolderIds": []
                },
                "admin_exclusion_filter": {
                  "SharedDriveIds": [],
                  "FolderIds": []
                }
              }
            }'
        

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `ENDPOINT_LOCATION`: The region of your application. For example, `us` or `eu`.
  * `LOCATION`: The location of your data connector. It must be `global` or `us`.
  * `COLLECTION_ID`: The ID of the collection that contains your data connector. The collection ID is provided when you create a data store. The collection ID isn't the same as the data store ID.



## What's next

  * To provide a user interface for querying your Google Drive data, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) and [connect it to the Google Drive data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store).
  * To preview how your search results appear after your app is set up, see [Get search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).
  * To enable alerts for the data store, see [Configure alerts for third-party data stores](https://docs.cloud.google.com/gemini/enterprise/docs/configure-periodic-data-alerts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
