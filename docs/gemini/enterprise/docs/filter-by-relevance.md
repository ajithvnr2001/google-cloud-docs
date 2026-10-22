---
url: https://docs.cloud.google.com/gemini/enterprise/docs/filter-by-relevance/
title: Filter searches by document-level relevance (Legacy) \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:16.708403+00:00
---

# Filter searches by document-level relevance (Legacy)  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/filter-by-relevance/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Developer guide ](https://docs.cloud.google.com/gemini/enterprise/docs/developer-guide)



Send feedback 

#  Filter searches by document-level relevance (Legacy) Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** Gemini Enterprise retrieves search results from the assistant using StreamAssist. We recommend using the StreamAssist instead of the Search and Answer. For more information, see [Get search results using StreamAssist](https://docs.cloud.google.com/gemini/enterprise/docs/get-answers-from-streamassist). 

**Note:** This feature is a Preview offering, subject to the "Pre-GA Offerings Terms" of the [GCP Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA products and features may have limited support, and changes to pre-GA products and features may not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). Further, by using this feature, you agree to the [Generative AI Preview terms and conditions](https://cloud.google.com/trustedtester/aitos) ("Preview Terms"). For this feature, you can process personal data as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to applicable restrictions and obligations in the Agreement (as defined in the Preview Terms). 

When searching in your Gemini Enterprise app, you can apply a relevance threshold so that only the documents that meet this threshold are returned as results. This page explains how to specify a relevance threshold in order to reduce the number of documents returned in queries.

## About filtering by document-level relevance

Each document returned by a search query is given a relevance level, which indicates the relevance of the returned document to the query. When you make a query through an API call, you can set a relevance threshold. Setting a high relevance threshold can reduce the number of documents returned by a query.

For example, if you find that search is returning too many documents of insufficient relevance to your users, set the relevance threshold to high to narrow the results to only those few that are most relevant. If the high setting is too restrictive, try the medium setting.

**Note:** This document-level relevance filtering feature is different from and less precise than the [document-relevance score](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results#relevance-scores) that can be returned for search results.

## Data types and apps supported for document-level relevance filter

The document-level relevance filter can be applied to data stores with following kinds of data:

  * Website data with advanced website indexing
  * Custom unstructured data
  * Custom structured data



The document-level relevance filter doesn't work for data stores with basic website indexing, media data, or healthcare data.

Furthermore, the document-level relevance filter can't be used with blended search apps. Blended search apps are apps that are connected to multiple data stores.

## Other kinds of filters

The document-level relevance filter is not the only way you can filter data returned by queries. You can also use filter expressions to filter results based on metadata (in unstructured data with metadata data stores) and field values (in structured data stores).

For information, see [Filter search with metadata](https://docs.cloud.google.com/gemini/enterprise/docs/filter-search-metadata).

If you use both a filter expression and the document-level relevance filter, the filter expression is applied first to the results and then the document-level relevance filter is applied.

## Before you begin

Make sure you have created an app and data store and have ingested data into your data store. For more information, see [Create a first-party app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app). See also Data types and apps supported for document-level relevance filter.

## Search and filter results by document-level relevance

To filter by relevance, follow these steps: **Note:** You can search over an app using the [`engines.servingConfigs.search`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method and you can search over a data store using the [`dataStores.servingConfigs.search`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.servingConfigs/search) method. For the following procedure, Google recommends searching using the `engines.servingConfigs.search` method.

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Go to Apps](https://console.cloud.google.com/gemini-enterprise/apps)

     2. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column.

  2. To filter search by document-level relevance, use the `relevanceThreshold` field with the [`engines.servingConfigs.search`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.servingConfigs/search) method.

**Key Term:** In Gemini Enterprise, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs. A Gemini Enterprise engine is a generic search engine where the `app_type` field is set to `APP_TYPE_INTRANET`.
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search:search" \
         -d '{
          "servingConfig": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search",
         "query": "QUERY",
         "relevanceThreshold": "RELEVANCE_THRESHOLD"
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `APP_ID`: the ID of the app that you want to query.
     * `QUERY`: the query text to search.
     * `RELEVANCE_THRESHOLD`: one of the following: `HIGH`, `MEDIUM`, `LOW`, `LOWEST`.

#### Example command and result
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)"
    -H "Content-Type: application/json" \
    "https://discoveryengine.googleapis.com/v1alpha/projects/my-project-123/locations/global/collections/default_collection/engines/my-search-app/servingConfigs/default_search:search" \
    -d '{
    "servingConfig": "projects/my-project-123/locations/global/collections/default_collection/engines/my-search-app/servingConfigs/default_search",
    "query": "What is the check grounding API",
    "relevanceThreshold": "HIGH"
    }'
    
    
    * * *
    
    
    {
    "results": [
    {
      "id": "a082e70352c073a4443502477255bd2a",
      "document": {
        "name": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/a082e70352c073a4443502477255bd2a",
        "id": "a082e70352c073a4443502477255bd2a",
        "derivedStructData": {
          "displayLink": "cloud.google.com",
          "link": "https://cloud.google.com/example/docs/check-grounding",
          "htmlTitle": "Check grounding | Example | Google Cloud",
          "title": "Check grounding | Example | Google Cloud"
        }
      }
    }
    ],
    "totalSize": 1,
    "attributionToken": "f_B-CgwIidzwswYQyue15gESJDY2N2M1NmJkLTAwMDAtMjk3Ni1iMGI4LTg4M2QyNGZmNTZhOCIHR0VORVJJQypAjr6dFavEii3b7Ygt3o-aIoCymiLC8J4Vo4CXIra3jC3Usp0V24-aIt7tiC3n7YgtrsSKLeTtiC2DspoixsvzFw",
    "guidedSearchResult": {},
    "summary": {}
    }
    

Here, the relevance threshold is set to high, so only the most relevant results are returned. In this example, only one document was determined to be highly relevant.

  3. Test multiple queries with different thresholds to determine the best threshold settings for your data and application.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
