---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/order-web-search-results/
title: Order web search results \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:28:07.031826+00:00
---

# Order web search results  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/order-web-search-results/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Order web search results Stay organized with collections  Save and categorize content based on your preferences. 

Ordering is a type of ranking mechanism that dynamically changes the sequence in which results are returned after an initial ranking that's established during the retrieval process. During retrieval, Agent Search fetches the relevant documents from the data store in the order of thousands (subject to the size of the data store). After this the top results are served according to the condition specified for reordering. For more information, see [About retrieval and ranking](https://docs.cloud.google.com/generative-ai-app-builder/docs/ranking-overview).

This page explains how to order the results of a web search query by date.

  * For data stores that use basic website search, you can order by Google-inferred page dates.
  * For data stores that use advanced website indexing, you can order by custom data attributes or Google-inferred page dates that are added to the data store schema. For more information, see [Use structured data for advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-website-metadata).



## Before you begin

Make sure that you do the following:

  * Create a data store with website data. For more information, see [Website URLs](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#website).

  * Create a search app and connect it to the data store. For more information, see [Create a search app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-engine-es).




## Order search results for basic website search

To order the search results for a website data store with basic website search, follow these steps:

### REST

The following sample shows how to to order your web search results for an app with basic website search. This sample uses the [`engines.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method:

**Note:** You can search over an app using the [`engines.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method and you can search over a data store using the [`dataStores.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.servingConfigs/search) method. For the following procedure, Google recommends searching using the `engines.servingConfigs.search` method.

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page.

[Go to Apps](https://console.cloud.google.com/gen-app-builder/engines)

     2. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column.

  2. Make a search query and include the `orderBy` field.

**Key Term:** In Agent Search, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs.
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search:search" \
         -d '{
         "servingConfig": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search",
         "query": "QUERY",
         "orderBy": "ORDER_BY"
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `APP_ID`: the ID of the Agent Search app.
     * `QUERY`: the query text to search.
     * `ORDER_BY`: the order in which the results are arranged. For example, to order chronologically, specify `date` to return web pages sorted by Google-inferred page date. For more information on the Google-inferred page date, see the [Help Google Search know the best date for your web page](https://developers.google.com/search/blog/2019/03/help-google-search-know-best-date-for) blog post. The default sort order is descending, in which the pages with the most recent dates are returned first. To get ascending sort order, append `:a` to the `date` value—`date:a`. 



## Order search results for advanced website indexing

To order the search results for a website data store with advanced website indexing, follow these steps:

### REST

The following sample shows how to order your web search results for an app with advanced website indexing. This sample uses the [`engines.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method:

**Note:** You can search over an app using the [`engines.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method and you can search over a data store using the [`dataStores.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.servingConfigs/search) method. For the following procedure, Google recommends searching using the `engines.servingConfigs.search` method.

  1. Find your app ID. If you already have your app ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page.

[Go to Apps](https://console.cloud.google.com/gen-app-builder/engines)

     2. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column.

  2. Make a search query and include the `orderBy` field.

**Key Term:** In Agent Search, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs.
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search:search" \
         -d '{
         "servingConfig": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search",
         "query": "QUERY",
         "orderBy": "ORDER_BY"
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `APP_ID`: the ID of the Agent Search app.
     * `QUERY`: the query text to search.
     * `ORDER_BY`: the order in which the results are arranged. The field can have values that are of the following data types: datetime, integer, or number. To order chronologically, specify the custom date attribute specified in the schema or the Google-inferred page date to return web pages sorted by date. For example, to order by a `date_edited` PageMap attribute, you can specify the `orderBy` field as `"orderBy": "date_edited"`. The default sort order is ascending, in which older pages are returned first. To get the results in descending order, append `desc` to the custom attribute value—for example, `"orderBy":"date_edited desc"`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
