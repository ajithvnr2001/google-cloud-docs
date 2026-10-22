---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gsites/add-filters-to-gsites-data-store/
title: Add filters to a Google Sites data store \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:17.956446+00:00
---

# Add filters to a Google Sites data store  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gsites/add-filters-to-gsites-data-store/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Add filters to a Google Sites data store Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to add filters to your Google Sites data stores in Gemini Enterprise. Use filters to narrow search results by including or excluding specific Site URLs or URL prefixes.

## Filter types

The Google Sites data store supports the following filter:

  * **Site Path Prefix** : A list of exact Site URLs or URL prefixes. You can apply this filter in one of two modes for each data store:

    * **Include in search** : Only sites whose URLs start with one of the listed prefixes are retrieved. This mode maps to the `admin_filter.SitePathPrefix` parameter in the API.
    * **Exclude from search** : Sites whose URLs start with one of the listed prefixes are removed from search results. This mode maps to the `admin_exclusion_filter.SitePathPrefix` parameter in the API.

**Note:** The **Site Path Prefix** filter for each data store can be configured to either include or exclude specified URL prefixes. You cannot apply both inclusion and exclusion filters simultaneously for the same data store. Set `admin_filter.SitePathPrefix` to only include matching prefixes, or set `admin_exclusion_filter.SitePathPrefix` to exclude matching prefixes.

## Add filters to a new data store

You can add a filter when you create a Google Sites data store using either the Google Cloud console or the API.

### Console

To add a filter when you create a Google Sites data store:

  1. In the Google Cloud console, go to the Gemini Enterprise page. 

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. In the navigation menu, click **Data stores**.
  3. Click **\+ Create data store**.
  4. On the **Select a data source** page, select **Google Sites**.
  5. On the **Specify the Google Sites source for your data store** step, under **Filters** , configure the **Site Path Prefix** filter: 
     1. Select **Include in search** to retrieve only the listed sites, or **Exclude from search** to remove the listed sites from search results.
     2. In the **Site Path Prefix** field, enter one or more exact Site URLs or URL prefixes. For example, `https://sites.google.com/a/example.com/site-name`.
  6. Click **Continue**.
  7. Complete the remaining configuration steps and click **Create**.



If you select **Include in search** , the filter is saved as `admin_filter.SitePathPrefix` in the data connector parameters. If you select **Exclude from search** , it is saved as `admin_exclusion_filter.SitePathPrefix`.

### REST

To add a filter when you create a Google Sites data store, call the [`setUpDataConnector`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations/setUpDataConnector) method.

Set either `admin_filter.SitePathPrefix` (to include sites) or `admin_exclusion_filter.SitePathPrefix` (to exclude sites) in the `params` field. Don't set both in the same request.

#### Include in search
    
    
        curl -X POST \
            -H "Authorization: Bearer $(gcloud auth print-access-token)" \
            -H "Content-Type: application/json" \
            -H "X-Goog-User-Project: PROJECT_ID" \
            "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION:setUpDataConnector" \
            -d '{
              "collectionId": "COLLECTION_ID",
              "collectionDisplayName": "COLLECTION_DISPLAY_NAME",
              "dataConnector": {
                "dataSource": "google_sites",
                "params": {
                  "admin_filter": {
                    "SitePathPrefix": [
                      "SITE_URL_PREFIX_1",
                      "SITE_URL_PREFIX_2"
                    ]
                  }
                },
                "entities": [ { "entityName": "google_sites" } ]
              }
            }'
        

#### Exclude from search
    
    
        curl -X POST \
            -H "Authorization: Bearer $(gcloud auth print-access-token)" \
            -H "Content-Type: application/json" \
            -H "X-Goog-User-Project: PROJECT_ID" \
            "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION:setUpDataConnector" \
            -d '{
              "collectionId": "COLLECTION_ID",
              "collectionDisplayName": "COLLECTION_DISPLAY_NAME",
              "dataConnector": {
                "dataSource": "google_sites",
                "params": {
                  "admin_exclusion_filter": {
                    "SitePathPrefix": [
                      "SITE_URL_PREFIX_1",
                      "SITE_URL_PREFIX_2"
                    ]
                  }
                },
                "entities": [ { "entityName": "google_sites" } ]
              }
            }'
        

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `ENDPOINT_LOCATION`: The region of your application. For example, `us` or `eu`.
  * `LOCATION`: The location of your data connector. It must be either `global` or `us`.
  * `COLLECTION_ID`: The unique ID of the data store.
  * `COLLECTION_DISPLAY_NAME`: The display name of the data store.
  * `SITE_URL_PREFIX_1`, `SITE_URL_PREFIX_2`: Exact Site URLs or URL prefixes. For example, `https://sites.google.com/a/example.com/site-name`.



## Update filters in an existing data store

You can update the **Site Path Prefix** filter in an existing data store using either the Google Cloud console or the API.

### Console

To modify the existing filter configuration:

  1. In the Google Cloud console navigation menu, click **Data stores**.
  2. Select your Google Sites data store.
  3. Click **View/edit parameters**.
  4. In the **View/edit parameters** panel, under **Filters** : 
     1. Switch the radio selection between **Include in search** and **Exclude from search** , or keep the current selection.
     2. Add, edit, or remove **Site Path Prefix** entries.
  5. Click **Save**.



### REST

To update the filter in an existing Google Sites data store, call the [`updateDataConnector`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections/updateDataConnector) method with `updateMask=params`.

The request body replaces the `SitePathPrefix` list with the one that you provide. Include the complete list of Site URL prefixes that you want active.
    
    
        curl -X PATCH \
            -H "Authorization: Bearer $(gcloud auth print-access-token)" \
            -H "Content-Type: application/json" \
            -H "X-Goog-User-Project: PROJECT_ID" \
            "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/COLLECTION_ID/dataConnector?updateMask=params" \
            -d '{
              "params": {
                "admin_filter": {
                  "SitePathPrefix": [
                    "SITE_URL_PREFIX_1",
                    "SITE_URL_PREFIX_2"
                  ]
                }
              }
            }'
        

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `ENDPOINT_LOCATION`: The region of your application. For example, `us` or `eu`.
  * `LOCATION`: The location of your data connector. It must be either `global` or `us`.
  * `COLLECTION_ID`: The ID of the collection that contains your data connector.
  * `SITE_URL_PREFIX_1`, `SITE_URL_PREFIX_2`: Exact Site URLs or URL prefixes.

**Note:** To switch from inclusion to exclusion (or the reverse), send only the target key in the request body. For example, to switch from inclusion to exclusion, include only `admin_exclusion_filter.SitePathPrefix`. The previously set `admin_filter` is overwritten and disabled.

## Remove filters from a data store

You can remove the **Site Path Prefix** filter from an existing data store using either the Google Cloud console or the API.

### Console

To remove the existing filter configuration:

  1. In the Google Cloud console navigation menu, click **Data stores**.
  2. Select your Google Sites data store.
  3. Click **View/edit parameters**.
  4. In the **View/edit parameters** panel, under **Filters** , clear all entries in the **Site Path Prefix** field.
  5. Click **Save**.



### REST

#### Remove a specific Site URL prefix

To modify the list of Site URL prefixes, send an update request. The `SitePathPrefix` field in your request must contain the complete list of all prefixes you want to retain. Any existing prefixes not included in this new list will be removed, as the provided list completely replaces the current one.
    
    
        {
          "params": {
            "admin_filter": {
              "SitePathPrefix": [
                "SITE_URL_PREFIX_TO_KEEP"
              ]
            }
          }
        }
        

#### Remove the filter entirely

To remove the filter from the data store, use the `remove_param_keys` attribute in an update request. This deletes the `admin_filter` or `admin_exclusion_filter` key.
    
    
        {
          "remove_param_keys": ["admin_filter", "admin_exclusion_filter"]
        }
        

Including both keys in `remove_param_keys` is safe even when only one is set on the data store.

## Parameter reference

The following table describes the API parameters that the **Site Path Prefix** filter maps to.

Parameter | Type | Description  
---|---|---  
`params.admin_filter.SitePathPrefix` | Repeated string | Site URLs or URL prefixes to include in retrieval. Set when the Console filter mode is **Include in search**. Mutually exclusive with `admin_exclusion_filter`.  
`params.admin_exclusion_filter.SitePathPrefix` | Repeated string | Site URLs or URL prefixes to exclude from retrieval. Set when the Console filter mode is **Exclude from search**. Mutually exclusive with `admin_filter`.  
  
## What's next

  * To provide a user interface for querying your Google Sites data, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) and [connect it to the Google Sites data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store).
  * To preview how your search results appear after your app is set up, see [Get search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).
  * To enable alerts for the data store, see [Configure alerts for third-party data stores](https://docs.cloud.google.com/gemini/enterprise/docs/configure-periodic-data-alerts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
