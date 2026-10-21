---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/about-generic-search/
title: Introduction to custom search \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:27:58.429926+00:00
---

# Introduction to custom search  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/about-generic-search/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Introduction to custom search Stay organized with collections  Save and categorize content based on your preferences. 

This page introduces and lists the capabilities of Agent Search for custom apps. The page also provides links to the available features, tutorials, and checklists, to get you started with Agent Search for custom apps.

## What is Agent Search for custom apps?

Agent Search for custom apps is a powerful, Google-quality search and content discovery engine that you can integrate into your applications that contain website data and other structured or unstructured data. The search capability is beyond basic keyword matching and uses AI to deliver highly relevant results, provide personalized browse and search experiences, and generate AI answers grounded in your data.

You can use custom search app for vertical-agnostic data that's on public websites or is in structured or unstructured format. Additionally, Agent Search offers other vertical-specific search and recommendations apps.

  * For information about media data, see [Introduction to media search and recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-media).
  * For information about commerce and retail data, see [AI Commerce Search](https://docs.cloud.google.com/solutions/vertex-ai-search-commerce).
  * For information about healthcare data, see [Healthcare search checklist](https://docs.cloud.google.com/generative-ai-app-builder/docs/healthcare-search-checklist).



## Key capabilities

The key capabilities of Agent Search are as follows:

  * **High-quality search:** Leverages Google's search expertise to understand user intent, even with complex queries and natural language queries. It combines keyword and semantic search to serve the best results.
  * **Personalized browse:** Provides personalized results without a specific search query and personalized feed based on a user's context and navigation patterns. It is ideal for discovery experiences to view personalized category pages and home feeds.
  * **Data sources:** Works with the following variety of data sources: 
    * **Website:** Index your public websites and use advanced features, such as index enrichment with the structured data in your websites.
    * **Structured Data:** Search over data organized in a defined format, such as databases, JSON files in Cloud Storage, or BigQuery tables—for example, hotel catalogs, real estate listings, and restaurant directories.
    * **Unstructured Data:** Search over documents like PDFs, HTML files, and TXT files or image files like JPEG and PNG files that are stored in Cloud Storage or BigQuery.
    * **Blended Search:** Search over multiple data stores that _blend_ data from the data sources mentioned above. For example, you can create a search app and connect it to a website data store and a document data store. This lets your users search over all of your content at once.
  * **Grounded AI answer generation:** Generates AI answers grounded in your data, with citations to the source documents. You can also ask follow up questions and related queries.
  * **Personalization:** Improves results and ranking over time by learning from user interactions captured in user events, such as clicks and conversions.
  * **Customization:** Offers several ways to tune and configure the search and browse experience fit for your business needs.



## Overview

The following diagram shows the key components of custom search and how they work together:

![key components of generic custom search](https://docs.cloud.google.com/generative-ai-app-builder/images/generic-search-overview.svg)**Figure 1.** Different components of custom search 

The components of Agent Search for custom search can be explained as follows:

  * **Data store** : Your content from different data sources is stored in a Agent Search data store. The source data can be public website data or structured and unstructured data.
  * **Data processing and indexing** : Agent Search understands and indexes your data, creating a searchable and retrievable representation. This includes the following: 
    * **Keyword extraction:** Identifies and generates important terms necessary to retrieve the correct information.
    * **Semantic understanding using embeddings:** Creates vector embeddings to capture the meaning of the content.
    * **Metadata processing:** Processes your documents using the document's structured data or metadata. For example, location in a hotel catalog, modification or creation dates in a web page's metadata.
    * **Advanced document parsing:** Understands document structure and annotates advanced information, such as tables, images, and graphs, using OCR or layout parsing.
  * **Search app** : At the heart of the custom search is a search app, which connects to one or more data stores that bring data from different sources. For blended search, the data is ingested through _connectors_. You configure the search and browse behavior at the app level.
  * **User query** : The input from a user intended to retrieve information from your app, which can be of two types: 
    * Search query: The user enters a targeted search query using text or images. Textual search is powered by autocomplete.
    * Navigational query or browse: An exploratory search to deliver personalized relevant content with no specific query. It is powered by the user's past activity and other signals, such as current category page and location.
  * **Retrieval and ranking:** There are several sub-components to retrieval and ranking of results: 
    * **Query understanding for search:** Agent Search analyzes a search query using the following: 
      * **Natural language processing:** To understand the intent.
      * **Filters with natural language understanding:** Translates locations from natural language queries into geo-coordinates and the conditions in natural language queries into filters.
      * **Knowledge graph:** To disambiguate terms and expand the search.
      * **Optional features:** Includes spelling correction, synonyms, and query rephrasing.
    * **Retrieval:** Agent Search finds the most relevant documents or chunks based on the following methods: 
      * **Keyword matching for search:** Conventional search based on terms.
      * **Semantic search:** Using embeddings to find conceptually similar content.
      * **Filtering:** Applying any filters you've configured—for example, date, category, or relevance score.
    * **Ranking:** Agent Search ranks the results based on the following factors: 
      * **Relevance:** A combination of keyword and semantic matching during search.
      * **Web signals for website search:** Factors like page quality and popularity.
      * **Boosting and burying:** Your custom rules to promote or demote certain results.
      * **Personalization:** Learning from user interactions. This is optional but highly recommended.
      * **Ordering:** Applying ordering instructions, for example, by date.
  * **Results and answer generation:**
    * **Search results:** A ranked list of relevant documents or chunks is returned with optional features, such as snippets, extractive answers, and extractive segments. The results that are served can be configured with the help of serving controls. You can also tune the search results.
    * **Answer generation:** A concise, synthesized answer is generated based on the top and relevant results, with citations. This uses advanced LLM features.
    * **Personalized browse:** A personalized set of documents with the highest predicted likelihood of engagement or conversion is returned. This prediction uses an advanced model that learns from user interactions.
  * **User events:** A tracker for user interactions, such as clicks and views, that helps Agent Search learn and improve search and personalization. User events aid in optimizing your business KPIs including engagement, conversion, and revenue.



## Key features and configurations

The following features and configurations are available for your custom search apps. At each stage you can customize these settings to serve the best results to your users.

![key components of generic custom search](https://docs.cloud.google.com/generative-ai-app-builder/images/generic-search-features.svg)**Figure 2.** Key features and configurations in custom search 

To elaborate, here are the available configurations:

  * [**Data preparation**](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data): 
    * **Schema for structured data** : Define the structure of your data with field names and types. You can provide your own schema or let Agent Search auto-detect it. For more information, see [Provide or auto-detect a schema](https://docs.cloud.google.com/generative-ai-app-builder/docs/provide-schema).
    * **Metadata** : Add metadata to your structured or unstructured documents and web pages to improve search and enable filtering. For more information, see the following: 
      * [Use structured data for advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-website-metadata).
      * [Unstructured data with metadata](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#unstructured).
      * [Structured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#structured).
    * **Chunking** : Break documents into smaller pieces for better relevance and LLM processing. For more information, see [Parse and chunk documents](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents).
    * **Parsing** : Use one of the following options to extract text, images, and other annotations: 
      * [Digital parser](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents#digital-parsing) to extract machine readable text.
      * [OCR parser for PDFs](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents#parsing-pdfs) to extract text from scanned PDFs or images.
      * [Layout Parser](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents#layout-parsing) to detect document structure and annotate images and graphs for better chunking and document understanding, which is required for complex documents and RAG applications.
    * **Custom embeddings** : Upload your own prepared vector embeddings. For more information, see [Use custom embeddings](https://docs.cloud.google.com/generative-ai-app-builder/docs/bring-embeddings).
  * **Data ingestion** : Agent Search offers different types of ingestion for data from different sources, such as: 
    * [Crawling for website data](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#website)
    * Ingesting [structured](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#structured) and [unstructured](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#unstructured) data from Cloud Storage and BigQuery or [through the REST API](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.documents)
  * **Search and browse configuration** : 
    * **Field settings** : Control how fields are configured for search and answer generation, such as searchable, retrievable, or indexable. For more information, see [Configure field settings](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-field-settings).
    * **Autocomplete** : Provide query suggestions as users type. For more information, see [Configure autocomplete](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-autocomplete).
    * **Serving Controls** : Create rules to modify search behavior. For more information, see [Configure serving controls for search](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-serving-controls). 
      * **Boost/bury** : Promote or demote specific results based on filters.
      * **Filter** : Remove results based on filters.
      * **Synonyms** : Treat certain terms as equivalent.
      * **Redirect** : Send users to a specific URL for certain queries.
      * **Promote controls** : Promote results within and beyond your Agent Search data store.
    * **Search tuning (Preview)** : Further train the model based on query and text extract pairs. For more information, see [Improve search results with search tuning](https://docs.cloud.google.com/generative-ai-app-builder/docs/tune-search).
    * **Website specific configurations** : 
      * **Advanced indexing** : For more details, see [Turn on advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/turn-on-advanced-indexing).
      * **Refresh web pages** : You can refresh documents in your website regularly using [automatic or manual refresh](https://docs.cloud.google.com/generative-ai-app-builder/docs/recrawl-websites) or opt for [sitemap-based refresh](https://docs.cloud.google.com/generative-ai-app-builder/docs/index-refresh-sitemap).
  * **Retrieval** : Configure the following retrieval methods: 
    * [Filter with natural-language understanding](https://docs.cloud.google.com/generative-ai-app-builder/docs/natural-language-queries).
    * [Filter searches by document-level relevance](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-by-relevance).
    * [Filter using metadata](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata).
  * **Ranking** : [Boost or bury](https://docs.cloud.google.com/generative-ai-app-builder/docs/boost-search-results) the retrieved results, [order web search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/order-web-search-results), or [order results from structured data stores](https://docs.cloud.google.com/generative-ai-app-builder/docs/order-structured-results).
  * **Search results** : Use Agent Search to do the following: 
    * [Get answers and follow-ups](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer).
    * [Get search summaries](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-search-summaries).
    * [Get snippets and extractive content](https://docs.cloud.google.com/generative-ai-app-builder/docs/snippets).
    * Generate personalized browse experience that requires user events
  * **User events** : Record user interactions, such as clicks and views to improve search and personalization. For more information, see [About user events for custom apps](https://docs.cloud.google.com/generative-ai-app-builder/docs/user-events).



## What's next

  * [Get started with custom search](https://docs.cloud.google.com/generative-ai-app-builder/docs/try-enterprise-search).
  * Follow the [custom search checklist](https://docs.cloud.google.com/generative-ai-app-builder/docs/generic-search-checklist) and the [website search checklist](https://docs.cloud.google.com/generative-ai-app-builder/docs/website-search-checklist) to set up your own custom search app with all configurations.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
