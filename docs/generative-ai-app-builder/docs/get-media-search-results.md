---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/get-media-search-results/
title: Get search results for media apps \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:35.362796+00:00
---

# Get search results for media apps  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/get-media-search-results/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Get search results for media apps Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to preview search results for media apps using the Google Cloud console and how to get search results using the API.

To implement the search app, you can create a [search widget](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-widget) to add to your web page or you can make API calls and integrate those calls into your webpage or application.

## About search modes

There are several modes of search query for media apps:

  * **Full queries** : When end users intend for their whole search term or phrase to be searched for. For example, in a music streaming app, users type the whole title of the song and search for it in one go. This is a preferred way of searching when using an input interface that lets users search in one go, such as audio input or keyboard input.

In full queries, if the entry includes a spelling mistake, users expect that mistake to be corrected.

This is the same behavior as search for non-media (custom) apps. See [Get search results for an app with structured or unstructured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results#structured-unstructured).

  * **Partial (or search-as-you-type) queries** : When end users dynamically receive a new set of search results as they type each letter. For example, in a music streaming app, users start entering the name of the song they're searching for and with each letter they type, the search results dynamically update and narrow down.

  * **Auto mode** : Auto mode is a mix of full and partial modes. With auto mode, you let media search decide whether to return query results as partial or full.

To determine the end users' probable intent, media search analyzes and weights various signals, such as the number of letters entered, the speed of entry, and whether the entry is a recognized entity—for example, the name of an actor or movie.




## Which mode to use

The default mode for media search queries is the auto mode. However, there are scenarios where you might choose to override the default mode and specify the full or partial query mode. Here are some use-case examples:

Scenario | Mode  
---|---  
You are very confident that your end users' queries are full queries. For example, you have a search box that includes an Enter function to mark the query complete and the user presses Enter. | Full queries  
You are very confident that your end users' queries are intended as partial queries—that is, they are expecting the results list to update after each letter entered. | Partial queries  
Neither of the above scenarios apply. Let media search decide whether to return query results as partial or full. | Auto  
  
## Get search results for a media app

**Note:** Depending on the amount of data, it can take hours after data ingestion to generate a preview.

You can preview search results from the Google Cloud console or get search results using the API. To get search results for a media app:

### Console

To use the Google Cloud console to preview media search and to configure a widget:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/start)

  2. Click the name of the media search app.

  3. Click **Configurations**.

  4. Click the **UI** tab.

  5. On the **UI** tab, set the **General configurations** and **Data display** options.

  6. In the **Preview** pane, start typing a query.

  7. To save the configurations and to make them available in the **Integration** tab, click **Save and publish**.




### REST

Use the [`engines.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method to get search results for a media app:

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page.

[Go to Apps](https://console.cloud.google.com/gen-app-builder/engines)

     2. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column.

  2. Run the following curl command to get search-as-you-type results.

All the fields except for `contentSearchSpec` can be used in conjunction with the `searchAsYouTypeSpec` field. For clarity, the optional fields have been omitted from the curl command. For the optional fields, see [Get search results for an app with structured or unstructured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results#structured-unstructured).
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search:search" \
         -d '{
         "query": "QUERY",
         "searchAsYouTypeSpec": {"condition": "SPEC_CONDITION"}
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `APP_ID`: the ID of the Agent Search app that you want to query.
     * `QUERY`: the query text to search.
     * `SPEC_CONDITION`: the search as you type spec can have one of the following values:

       * `ENABLED`: for partial queries
       * `DISABLED`: for full queries
       * `AUTO`: for partial or full as deemed appropriate. If you leave the `SPEC_CONDITION` field empty or don't specify it, the default search mode is `AUTO`.

#### Example command and partial result
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:search" \
    -d '{
    "query": "Mission Impossible",
    "searchAsYouTypeSpec": {"condition": "DISABLED"}
    }'
    
    
    * * *
    
    {
      "results": [
        {
          "id": "189333",
          "document": {
          "name": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/189333",
            "id": "189333",
            "structData": {
              "uri": "http://mytestdomain.movie/content/189333",
              "title": "Mission: Impossible - Fallout (2018)",
              "categories": [
                "Action",
                "Adventure",
                "Thriller"
              ],
              "available_time": "2023-01-01T00:00:00Z",
              "media_type": "movie",
              "expire_time": "2033-01-01T00:00:00Z"
            }
          }
        },
        {
          "id": "111781",
          "document": {
          "name": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/111781",
            "id": "111781",
            "structData": {
              "media_type": "movie",
              "available_time": "2023-01-01T00:00:00Z",
              "uri": "http://mytestdomain.movie/content/111781",
              "title": "Mission: Impossible - Rogue Nation (2015)",
              "categories": [
                "Action",
                "Adventure",
                "Thriller"
              ],
              "expire_time": "2033-01-01T00:00:00Z"
            }
          }
        },
        ...
        {
          "id": "116507",
          "document": {
          "name": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/116507",
            "id": "116507",
            "structData": {
              "uri": "http://mytestdomain.movie/content/116507",
              "categories": [
                "Comedy"
              ],
              "media_type": "movie",
              "available_time": "2023-01-01T00:00:00Z",
              "title": "Mission London (2010)",
              "expire_time": "2033-01-01T00:00:00Z"
            }
          }
        }
      ],
      "totalSize": 5628,
      "attributionToken": "vgL0PQEKDAiZxMbCBhD2koiqAxIkNjg1MWM3OTUtMDAwMC0yOWVmLThhNzUtZDQzYTJjYzdiYmNmIgVNRURJQSpUtreMLa_WoTGs1qExwvCeFaOAlyKrtZwxxcvzF-7r6TGotZwxkPeyMI6RyTDPv-Iw1L_iMJvWty2Ovp0V1LKdFfHr6THs4K8tkvGsMJXxrDCY1rctMAFKEjB4OTYzYjdjNGE0ZGYwN2FhZlKUAXByb2plY3RzLzc1NjIwNjYwODQ3OS9sb2NhdGlvbnMvZ2xvYmFsL2NvbGxlY3Rpb25zL2RlZmF1bHRfY29sbGVjdGlvbi9lbmdpbmVzL3F1aWNrc3RhcnQtbWVkaWEtcmVjb21tZW5kXzE3NDUwMjUyMjYwNDMvc2VydmluZ0NvbmZpZ3MvZGVmYXVsdF9zZWFyY2g",
      "nextPageToken": "Y2YiJ2NjNmMhNDNk1SN3EGOtYWZ5ITLwADMw0CN5czYxUDO2QiGDI9kgzIEGIs1tmJCMIBM1IgC",
      "summary": {},
      "queryExpansionInfo": {}
    }




## Next steps

  * [Add the search widget to a web page](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-widget)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
