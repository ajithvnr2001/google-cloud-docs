---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-by-relevance/
title: Filter searches by document-level relevance \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:30.648933+00:00
---

# Filter searches by document-level relevance  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-by-relevance/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Filter searches by document-level relevance Stay organized with collections  Save and categorize content based on your preferences. 

When searching in your Agent Search app, you can specify document-level relevance filters so that only the documents that meet the filter threshold are returned as results. This page explains the types of threshold, the importance of optimizing the threshold, and how to specify relevance filters and their threshold.

## About filtering by document-level relevance

When a search query returns a result, it assigns a relevance level to each retrieved document. In your search request, you can set a threshold to return only those documents that meet the filter threshold. Setting a high threshold can reduce the number of documents that the query returns. Whereas setting a low threshold can dilute the results with documents that have little relevance to the user's query.

Therefore, if you find that the result contains too many documents of insufficient relevance to your users, set a high relevance threshold to narrow the results to only those few that are most relevant. If a high threshold is too restrictive, you can lower it to a more optimal value.

### Types of searches

You can apply relevance filters to the following types of searches:

  * **Keyword search** : retrieves documents based on keyword search.
  * **Semantic-similarity search** : retrieves documents based on embeddings.



In your relevance filter definition, you can specify the type of threshold for each of these searches. The search retrieves the documents for the given search and then applies the specified threshold.

### Types of threshold

You can specify one of the following types of threshold for keyword and semantic-similarity search when you send your search request.

  * **Relevance threshold** : When you set this threshold, the search uses a proprietary model to determine a document's relevance. In this case, the search might use any pertinent signal, such as keyword-similarity score, topicality score, and semantic-similarity score.

The relevance threshold is a coarse-grained setting that allows the following values: `HIGH`, `MEDIUM`, `LOW`, and `LOWEST`. A `HIGH` threshold might return fewer documents with high relevance score while the `LOWEST` threshold might return more documents that might not be relevant to the search query.

**Note:** This relevance filtering feature is different from and less precise than the [document-relevance score](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results#relevance-scores) that can be returned for search results.
  * **Semantic-relevance threshold** : When you set this threshold, the filter solely relies on the semantic-similarity score to determine a document's relevance.

The semantic-relevance threshold is a fine-grained setting and is a floating point value in the range [0,1]. Setting the threshold to zero returns all the documents while setting the threshold to one returns the documents that have the most relevance.




### Relevance filter definition and example

To define relevance filters in your search request, specify only one type of threshold (relevance threshold and semantic-relevance threshold) for each type of search (keyword search and semantic search). You can specify either one or both of the types of search inside the relevance filter specification. However, there must be only one type of threshold that's defined within each type of search. For example, consider the following:
    
    
    {
      "relevanceFilterSpec": {
        "keywordSearchThreshold":  {
          "relevanceThreshold": "LOW"
        },
        "semanticSearchThreshold":  {
          "semanticRelevanceThreshold": 0.871
        }
      }
    }
    

In this search request, the results are returned in two stages: retrieval and filtering.

  * The search retrieves the documents according to keyword matching and then filters the documents with a low relevance threshold. This returns a large number of retrieved documents.
  * Simultaneously, the search retrieves the documents according to semantic similarity and then filters the documents with a high semantic relevance threshold of `0.871`. This returns fewer retrieved documents.



The search emphasis is more on keyword matching than semantic similarity. The filters allow more documents that are retrieved due to keyword matching.

Similarly, you can define the relevance filter in the following manner to return fewer documents with matching keywords and more documents with semantic similarity.
    
    
    "relevanceFilterSpec": {
        "keywordSearchThreshold":  {
            "semanticRelevanceThreshold": 0.871
        },
        "semanticSearchThreshold":  {
            "relevanceThreshold": "LOW"
        }
    }
    

## Data types and apps supported for document-level relevance filter

The document-level relevance filter can be applied to data stores with following kinds of data:

  * Website data with advanced website indexing
  * Custom unstructured data
  * Custom structured data



The document-level relevance filter doesn't work for data stores with basic website indexing, media data, or healthcare data.

Furthermore, the document-level relevance filter can't be used with blended search apps. Blended search apps are apps that are connected to multiple data stores.

## Other kinds of filters

The document-level relevance filter is not the only way you can filter data returned by queries. You can also use filter expressions to filter results based on metadata (in advanced website indexing and unstructured data with metadata data stores) and field values (in structured data stores).

For information, see:

  * [Filter expressions with advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-website-search#filter-expressions-advanced-indexing)

  * [Filter custom search for structured or unstructured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata)




If you use both a filter expression and the document-level relevance filter, the filter expression is applied first to the results and then the document-level relevance filter is applied.

## Before you begin

Make sure you have created an app and data store and have ingested data into your data store. For more information, see [Create a search app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-engine-es). See also Data types and apps supported for document-level relevance filter.

## Search and filter results by document-level relevance

To filter by relevance, follow these steps: **Note:** You can search over an app using the [`engines.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method and you can search over a data store using the [`dataStores.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.servingConfigs/search) method. For the following procedure, Google recommends searching using the `engines.servingConfigs.search` method.

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page.

[Go to Apps](https://console.cloud.google.com/gen-app-builder/engines)

     2. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column.

  2. To filter search by document-level relevance, specify the `relevanceFilterSpec` field that defines only one type of threshold for each type of search using the [`engines.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method. That is, you can specify either `relevanceThreshold` or `semanticRelevanceThreshold` for a given type of search.

**Key Term:** In Agent Search, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs.
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search:search" \
         -d '{
          "servingConfig": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search",
         "query": "QUERY",
         "relevanceFilterSpec": {
           "keywordSearchThreshold":  {
               "relevanceThreshold": "RELEVANCE_THRESHOLD"
           },
           "semanticSearchThreshold":  {
               "semanticRelevanceThreshold": SEMANTIC_RELEVANCE_THRESHOLD
           }
         }
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `APP_ID`: the ID of the Agent Search app that you want to query.
     * `QUERY`: the query text to search.
     * `RELEVANCE_THRESHOLD`: one of the following: `HIGH`, `MEDIUM`, `LOW`, `LOWEST`.
     * `SEMANTIC_RELEVANCE_THRESHOLD`: a floating point value in the range [0,1].

#### Example command and result
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-search-app/servingConfigs/default_search:search" \
    -d '{
    "servingConfig": "projects/my-project-123/locations/global/collections/default_collection/engines/my-search-app/servingConfigs/default_search",
    "query": "What is the check grounding API",
    "relevanceFilterSpec": {
    "keywordSearchThreshold": {
     "relevanceThreshold": "HIGH"
    },
    "semanticSearchThreshold": {
     "semanticRelevanceThreshold": 0.45
    }
    }
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
          "link": "https://cloud.google.com/generative-ai-app-builder/docs/check-grounding",
          "htmlTitle": "Check grounding",
          "title": "Check grounding"
        }
      },
      "rankSignals": {
      ...
      },
      "retrievalSignals": {
        "retrievalSource": 1
      }
    }
    ],
    "totalSize": 1,
    "attributionToken": "f_B-CgwIidzwswYQyue15gESJDY2N2M1NmJkLTAwMDAtMjk3Ni1iMGI4LTg4M2QyNGZmNTZhOCIHR0VORVJJQypAjr6dFavEii3b7Ygt3o-aIoCymiLC8J4Vo4CXIra3jC3Usp0V24-aIt7tiC3n7YgtrsSKLeTtiC2DspoixsvzFw",
    "guidedSearchResult": {},
    "summary": {}
    }
    

Here, the relevance threshold is set to high, so only the most relevant results are returned. In this example, only one document was determined to be highly relevant. The retrieval source is indicated as 1, which maps to keyword similarity.

  3. Test multiple queries with different thresholds to determine the best threshold settings for your data and application.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
