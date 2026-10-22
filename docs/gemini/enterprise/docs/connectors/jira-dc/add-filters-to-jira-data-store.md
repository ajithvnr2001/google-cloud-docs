---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc/add-filters-to-jira-data-store/
title: Add filters to a Jira Data Center data store \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:43:02.997540+00:00
---

# Add filters to a Jira Data Center data store  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc/add-filters-to-jira-data-store/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)



Send feedback 

#  Add filters to a Jira Data Center data store Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to add filters to your Jira Data Center data stores in Gemini Enterprise. Filters determine which information is retrieved or excluded from the Jira Data Center data store when users chat with the Assistant using the Gemini Enterprise app or run actions against your Jira instance.

## Filter types

You can configure the following filters within the `params` object of your data connector:

  * **Inclusion filter (`admin_filter`)**: Retrieves only specific information from the Jira Data Center data store and restricts actions to allowed projects.
  * **Exclusion filter (`admin_exclusion_filter`)**: Excludes specific information from the Jira Data Center data store and prevents actions on out-of-scope projects.



## Filter keys

The filter parameters accept an object containing key-value pairs. The keys represent the Jira Data Center fields you want to filter on, and the values are arrays of strings containing the criteria to match. When updating filters using the API, the following keys are supported:

Filter name | `FILTER_KEY` | Description | Value examples  
---|---|---|---  
Project | `Project` | Filters search results and restricts actions to specific Jira project keys. Mutations and retrievals on out-of-scope projects fail or return no results. | • `ENG`   
• `HR`   
• `SUPPORT`  
  
## Update filters in an existing data store

You can update filters in an existing data store using either the Google Cloud console or the API.

### Console

To modify existing filter configurations: 

  1. In the Google Cloud console navigation menu, click **Data stores**.
  2. Select your Jira Data Center data store.
  3. Click **View/edit parameters**.
  4. In the **View/edit parameters** panel, add or update the project keys and filter types.
  5. Click **Save**.



### REST

To add or to update filters in an existing Jira Data Center data store, call the [`updateDataConnector`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections/updateDataConnector) method with any one of these fields:

  * The `admin_filter` field for inclusion filter.
  * The `admin_exclusion_filter` field for exclusion filter.



In the request body, the field must contain all the filters you want to have in the data store, including the filters that are not updated.

To add or update filters in an existing Jira Data Center data store, run the following command:
    
    
            curl -X PATCH   
            -H "Authorization: Bearer $(gcloud auth print-access-token)"   
            -H "Content-Type: application/json"   
            -H "X-Goog-User-Project: PROJECT_ID"   
            "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/COLLECTION_ID/dataConnector?updateMask=params"   
            -d '{
                "params": {
                  "FILTER_TYPE": {
                    "FILTER_KEY": [
                      "UPDATED_FILTER_VALUE1",
                      "UPDATED_FILTER_VALUE2"
                    ]
                  }
                }
            }'
            

Replace the following:

  * `PROJECT_ID`: the ID of your project. 
  * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * `LOCATION`: the multi-region of your data store: `global`, `us`, or `eu`
  * `COLLECTION_ID`: The ID of the collection containing the data store. 
  * `FILTER_TYPE`: the type of filter added to your Jira Data Center data stores. For more information, see [Filter types](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc/add-filters-to-jira-data-store#filter-types). 
  * `FILTER_KEY`: the key for the filter, corresponding to a field in your data. For more information, see [Filter keys](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc/add-filters-to-jira-data-store#filter-keys). 
  * `UPDATED_FILTER_VALUES`: the value or values to filter on for the specified `FILTER_KEY` (for example, project keys such as `ENG`). 



#### Important Considerations

  * If you switch from an inclusion filter to an exclusion filter, or from an exclusion filter to an inclusion filter, you must explicitly remove the filter that is no longer required by setting it to empty in the request body. For example, if you have an `admin_filter` and want to switch to `admin_exclusion_filter`, include `"admin_filter": {}` in addition to `admin_exclusion_filter` in your API request `params` object. The following example shows `params` object when switching from `admin_filter` to `admin_exclusion_filter`:
        
        "params": {
                  "admin_filter": {},
                  "admin_exclusion_filter": {
                    "Project": ["ENG"]
                  }
                }
                

  * When updating filters, you must include the previously added filters as well.




## Verify that the data store includes the filters

You can get the details of the data store to confirm that the filters you added or updated are correctly applied using the Google Cloud console or the API:

### Console

To view the existing filter configurations: 

  1. In the Google Cloud console navigation menu, click **Data stores**.
  2. Select your Jira Data Center data store.
  3. Click **View/edit parameters**.



In the **View/edit parameters** panel, the existing filters applied to the data store are displayed.

### REST

To verify data store settings, call the [`getDataConnector`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections/getDataConnector) method:
    
    
            curl -X GET \
            -H "Authorization: Bearer $(gcloud auth print-access-token)" \
            -H "X-Goog-User-Project: PROJECT_ID" \
            "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/COLLECTION_ID/dataConnector"
            

Replace the following:

  * `PROJECT_ID`: the ID of your project. 
  * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * `LOCATION`: the multi-region of your data store: `global`, `us`, or `eu`
  * `COLLECTION_ID`: the ID of the collection containing the data store. 



In the response, view the `admin_filter` or `admin_exclusion_filter` fields in `params` to verify the filters.

## What's next

  * To provide a user interface for querying your Jira Data Center data, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) and [connect it to the Jira Data Center data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store).
  * To manage the list of actions, see [Manage actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions).
  * To preview how your search results appear after your app is set up, see [Get search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).
  * To enable alerts for the data store, see [Configure alerts for third-party data stores](https://docs.cloud.google.com/gemini/enterprise/docs/configure-periodic-data-alerts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
