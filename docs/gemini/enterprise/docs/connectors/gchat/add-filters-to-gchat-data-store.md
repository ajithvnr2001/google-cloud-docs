---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gchat/add-filters-to-gchat-data-store/
title: Add filters to a Google Chat data store \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:21:15.389166+00:00
---

# Add filters to a Google Chat data store  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gchat/add-filters-to-gchat-data-store/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Add filters to a Google Chat data store Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to add filters to your Google Chat data stores in Gemini Enterprise. Filters determine which information is retrieved or excluded from the Google Chat data store when users chat with the Assistant using the Gemini Enterprise app.

## Filter types

The Google Chat data store supports the following filter types:

  * **Message Recency** : This filter limits search results to a specific timeframe to ensure data relevance and reduce noise. For example, setting the value to 90 days will include only messages from the last 90 days in the index, automatically excluding older data.
  * **Exclude Direct Messages** : This filter excludes all private 1:1 direct messages from the search results. When enabled, the Google Chat data store only indexes content from multi-user spaces and group chats.



## Update filters in an existing data store

You can update filters in an existing data store using either the Google Cloud console or the API. 

### Console

To modify existing filter configurations: 

  1. In the Google Cloud console navigation menu, click **Data stores**.
  2. Select your Google Chat data store.
  3. Click **View/edit parameters**.
  4. In the **View/edit parameters** panel, add or update the filter types.
  5. Click **Save**.



### REST

To add or update filters in an existing Google Chat data store, call the [`updateDataConnector`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections/updateDataConnector) method.

In the request body, you must include all filters that you want in the data store, including filters that you are not updating.
    
    
        curl -X PATCH   
    
            -H "Authorization: Bearer $(gcloud auth print-access-token)"   
    
            -H "Content-Type: application/json"   
    
            -H "X-Goog-User-Project: PROJECT_ID"   
    
            "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/COLLECTION_ID/dataConnector?updateMask=params"   
    
            -d '{
              "params": {
                "admin_filter": {
                  "ExcludeDirectMessages": EXCLUDE_DMS,
                  "MessageRecency": RECENCY_DAYS
                }
              }
            }'
        

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `ENDPOINT_LOCATION`: The region of your application. For example, `us` or `eu`.
  * `LOCATION`: The location of your data connector. It must be either `global` or `us`.
  * `COLLECTION_ID`: The ID of the collection that contains your data connector. The collection ID is provided when you create a data store. The collection ID is not the same as the data store ID.
  * `EXCLUDE_DMS`: A boolean value (true or false).
  * `RECENCY_DAYS`: An integer representing the age limit in days. For example, 90.



## Remove filters from a data store

When managing your data store configuration, you may need to clear specific filters or reset filters entirely. You can remove filters from an existing data store using either the Google Cloud console or the API.

### Console

To remove existing filter configurations: 

  1. In the Google Cloud console navigation menu, click **Data stores**.
  2. Select your Google Chat data store.
  3. Click **View/edit parameters**.
  4. In the **View/edit parameters** panel, delete the filter types.
  5. Click **Save**.



### REST

####  Remove a specific filter

To remove a specific filter while keeping others, send an **update request**. Within the `admin_filter` object in the `params` attribute, include only the filters you want to retain. Any filter that is not listed will be removed. 

For example, to remove `MessageRecency` but retain `ExcludeDirectMessages`, use the following command:
    
    
        {
          "params": {
            "admin_filter": {
              "ExcludeDirectMessages": EXCLUDE_DMS
            }
          }
        }
        

Replace the following:

  * `EXCLUDE_DMS`: A boolean value (true or false).

**Note:** If you don't include a filter you previously had enabled, it will be overwritten and disabled.

####  Remove all filters

To remove all filters from the data store, use the `remove_param_keys` attribute in an update request. This deletes the entire `admin_filter` key and its associated logic.
    
    
        {
          "remove_param_keys": "admin_filter"
        }
        

## What's next

  * To provide a user interface for querying your Google Chat data, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) and [connect it to the Google Chat data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store).
  * To manage the list of actions, see [Manage actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions).
  * To preview how your search results appear after your app is set up, see [Get search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).
  * To enable alerts for the data store, see [Configure alerts for third-party data stores](https://docs.cloud.google.com/gemini/enterprise/docs/configure-periodic-data-alerts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
