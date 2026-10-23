---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/ranking-overview/
title: About retrieval and ranking \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:42.831260+00:00
---

# About retrieval and ranking  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/ranking-overview/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  About retrieval and ranking Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how retrieval and ranking work together to deliver relevant search results in Agent Search apps.

## Overview

In short, retrieval is finding relevant documents, while ranking is ordering those retrieved documents. Ranking all the available documents can be computationally expensive. Therefore, retrieval and ranking work sequentially.

First, the search model understands the query and rewrites it. Then, depending on the data sources available and the number of indexed documents in your data store, the model retrieves documents in the order of thousands. A relevance score is assigned to the retrieved documents.

The ranking model then orders the retrieved documents and serves the top 400 ranked results. The following image shows how these two processes fit into the search workflow.

![retrieval and ranking in search](https://docs.cloud.google.com/generative-ai-app-builder/images/generic-search-overview.svg)**Figure 1.** Retrieval and ranking in search workflow 

## Retrieval methods

Retrieval is the process of selecting a subset of documents from your data store that are relevant to a user's query. Agent Search model manages retrieval for your search apps based on different signals, such as the following, and assigns relevance scores:

  * **Topicality** : Includes keyword matching, knowledge graphs, and web signals.

  * **Embeddings** : Includes embeddings to find conceptually similar content.

  * **Cross-attention** : Allows a model to consider the relationship between a query and a document to assign a relevance score to the document.

  * **Freshness** : Involves ascertaining the age of the documents in the data store.

  * **User events** : Includes conversion signals used for personalization.




Additionally, in a search request, you can supply [relevance filters](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-by-relevance) and metadata filters for [website data](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-website-search) and [structured or unstructured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata) to narrow down the list of relevant documents.

## Ranking methods

Ranking takes the documents that are selected during the retrieval phase, assigns them a new relevance score according to the following conditions, and reorders them:

  * **Boost** : Promotes and demotes certain results according to custom attributes or freshness. This impacts the first 1,000 retrieved documents and ranks the top 400. For more information, see [Boost search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/boost-search-results).
  * **Custom ranking** : Controls, tunes, and overrides the default ranking logic with a formula-based ranking algorithm to suit your specific requirements. The relevance score that custom ranking assigns takes a precedence when serving the results. For more information, see [Customize search results ranking](https://docs.cloud.google.com/generative-ai-app-builder/docs/custom-ranking).
  * **Ordering** : Applies ordering instructions, for example, by date.
  * **Search tuning** : Impacts how the model perceives the semantic relevance of your documents and changes the embedding relevance scores. For more information, see [Improve search results with search tuning](https://docs.cloud.google.com/generative-ai-app-builder/docs/tune-search).
  * **Event-based reranking** : Updates the results at the time of serving using user-events-based personalization model.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
