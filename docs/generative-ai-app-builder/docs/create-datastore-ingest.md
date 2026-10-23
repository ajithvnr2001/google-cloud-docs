---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest/
title: About apps and data stores \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:50.264650+00:00
---

# About apps and data stores  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  About apps and data stores Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Agent Search apps and data stores.

With Agent Search, you create a search or recommendations app and connect it to a data store. A Google Cloud project can contain multiple apps.

## Relationship between apps and data stores

The relationship between apps and data stores depends on the type of app:

  * Custom search apps have a many-to-many relationship with data stores. When multiple data stores are connected to a single custom search app, this is referred to as _blended search_. For information about limitations of connecting a search app to more than one data store, see About blended search.

  * A custom recommendations app has a one-to-one connection with its data store.

  * A media app has a many-to-one relationship with its data store. An app can only connect to one data store, whereas a given data store can be connected to several apps. For example, a media search app and a media recommendations app can share a data store.

  * A healthcare search app has a many-to-one relationship with its data store. An app can only connect to one data store, whereas a given data store can be connected to several apps. For example, a patient-facing app and a provider-facing app can connect to the same data store.

For a batch data import of healthcare data, data is imported into a data store that's within an app. For streaming data import (Preview) of healthcare data, data is imported into an _entity_ , which is a type of data store that's within a data connector. A data connector is also a type of data store that's within an app.

**Deprecated:** Agent Search for healthcare is deprecated and won't be available after May 15, 2027. 



After a data store is connected to an app, it can't be disconnected.

## Method of app creation and data ingestion

How you create an app and ingest data depends on the type of data you have:

  * For website data, you can use either the Google Cloud console or the API. To use a website data created with the API, you must attach it to an app with Enterprise features enabled in the Google Cloud console.

  * For structured or unstructured data, you can use either the Google Cloud console or the API.

  * For healthcare data, you can use either the Google Cloud console or the API.




## Documents

Each data store has one or more data records, called _documents_. What a document represents varies depending on the type of data in the data store:

  * **Website**. A document is a web page.

  * **Structured data**. A document is a row in a table or a JSON record that follows a particular schema. You can provide this schema yourself or you can let Agent Search derive the schema from the ingested data.

  * **Structured data for media**. A document is a row in a table or a JSON record that follows a schema that is specific to media. The documents are records pertaining to media content, such as videos, news articles, music files, and podcasts. A document contains information that describes the media item, at minimum: title, URI to the content location, categories, duration, and available date.

  * **Unstructured data**. A document is a file in any of the following formats: TXT, PDF, HTML, DOCX, PPTX, XLSX, and XLSM.

  * **Healthcare FHIR data**. A document is a supported [FHIR R4](https://docs.cloud.google.com/healthcare-api/docs/concepts/fhir) resource. For a list of FHIR R4 resources that Agent Search supports, see [Healthcare FHIR R4 data schema reference](https://docs.cloud.google.com/generative-ai-app-builder/docs/fhir-schema-reference).




## Data stores and apps

In Agent Search, there are various kinds of data stores. A data store can contain only one type of data.

  * Website data
  * Structured data
  * Structured content (media)
  * Unstructured data
  * Healthcare FHIR data



### Website data

A data store with website data uses data indexed from public websites. You can provide a set of URL patterns that you want to include in your data store. The web pages that fit the URL patterns are called _included_ web pages. You can then set up search over data crawled from the included web pages.

For example, you can provide URL patterns such as `example.com/faq/*` and `example.com/events/*` and enable search over the data crawled from these web pages that fit the pattern. This data includes text, images tagged with metadata, and other structured data such as `meta` tags, PageMap attributes, and schema.org data.

You can also provide URL patterns for portions of websites that you want excluded, for example, `example.com/events/members-only/*` or `example.com/events/past-*`. Excluded URLs take priority over included ones.

There are two types of website data stores:

  * **Basic website search** :

    * Provides search capabilities over the existing Google Search index for the included websites.
    * Doesn't require domain verification.
  * **Advanced website indexing** :

    * Provides advanced search capabilities over an index that's generated based on either of the following: 
      * The Agent Search app owners can control which web pages are indexed by submitting sitemaps and maintaining them. For more information, see [Index and refresh web pages using sitemaps](https://docs.cloud.google.com/generative-ai-app-builder/docs/index-refresh-sitemap). This process keeps the index fresh without manual intervention.
      * The Agent Search app owners can perform an initial indexing that mirrors the Google Search index and then expand the index's coverage by recrawling the websites whenever necessary, keeping it fresh. For more information, see [Refresh web pages](https://docs.cloud.google.com/generative-ai-app-builder/docs/recrawl-websites). The advanced capabilities of advanced website indexing are listed in [Advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#advanced-website-indexing).
    * Requires Agent Search data stores owners to verify the domains to which the included websites belong. For more information, see [Verify website domains](https://docs.cloud.google.com/generative-ai-app-builder/docs/domain-verification).
    * Provides the capability to add structured data to the data store schema. A website contains unstructured data, but you can add structured data in the form of `meta` tags, PageMap attributes, and schema.org data to your web pages. You can then use this structured data to edit the data store schema as explained in [Use structured data for advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-website-metadata).



#### What's next

For website search:

  * To understand the indexing prerequisites, see how to [prepare data for website search](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#website).
  * [Create a data store using website content](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#website).
  * [Create a search app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-engine-es).



### Structured data

A data store with structured data enables semantic search or recommendations over structured data. You can import data from BigQuery or Cloud Storage. You can also manually upload structured JSON data through the API.

For example, you can enable search or recommendations over a product catalog for your ecommerce experience or a directory of doctors for provider search or recommendations.

Agent Search auto-detects the schema from the data that you import. Optionally, you can provide a schema for your data. Providing a schema for your data typically improves the quality of results.

#### What's next

For custom search:

  * [Prepare structured data for ingestion](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#structured).
  * Create a search data store using one of these methods: 
    * [Import from BigQuery](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#bigquery).
    * [Import from Cloud Storage](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#cloud-storage).
    * [Upload structured JSON data with the API](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#api-json).
  * [Create a search app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-engine-es).



For custom recommendations:

  * [Create a custom recommendations data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-recommendations).
  * [Create a custom recommendations app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-generic-recommendations-app).



### Structured data for media

Media apps can only be connected to media data stores. Media data stores are structured data stores with a Google-defined schema or with your own custom schema that contains a specific set of five media-related fields. For more information about the schema, see [About media documents and data stores](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-documents).

For example, you can enable recommendations by creating a media recommendations app for a movie catalog or a news site so that your users will have suitable and personalized suggestion made for them.

In addition to media documents, media data stores also contain the user event information that allows Agent Search to customize recommendations and search for your users. User events are required for media apps. For information about user events, see [Record real-time user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/record-user-events).

#### What's next

  * [Create a media data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-media).
  * [Create media apps](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-app-media).



### Unstructured data

An unstructured data store enables semantic search over data such as documents and images.

Unstructured data stores support documents in TXT, PDF, HTML, DOCX, PPTX, XLSX, and XLSM formats.

Search provides results in the form of 10 URLs and summarized answers for natural language queries. Documents must be uploaded to a Cloud Storage bucket with appropriate access permissions. For example, a financial institution can enable search over their private corpus of financial research publications, or a biotech company can enable search or recommendations over their private repository of medical research.

#### What's next

For search:

  * [Prepare unstructured data for ingestion](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#unstructured).
  * Create a search data store using one of these methods: 
    * [Import from BigQuery](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#bigquery).
    * [Import from Cloud Storage](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#cloud-storage).
    * [Sync from Google Drive](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#google-drive).
  * [Create a search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es) for your unstructured data.
  * [Create a search app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-engine-es).



### Healthcare FHIR data

**Deprecated:** Agent Search for healthcare is deprecated and won't be available after May 15, 2027. 

A healthcare search app uses FHIR R4 data imported from a Cloud Healthcare API FHIR store. For a list of FHIR R4 resources that Agent Search supports, see [Healthcare FHIR R4 data schema reference](https://docs.cloud.google.com/generative-ai-app-builder/docs/fhir-schema-reference). A FHIR R4 data store must satisfy some requirements before it can be used as a data source for Agent Search data store. For more information, see how to [prepare healthcare FHIR data](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#hc-fhir-data) for ingestion.

#### What's next

  * [Prepare FHIR R4 data for ingestion](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#hc-fhir-data).
  * [Create a healthcare search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-hc).
  * [Create a healthcare search app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-app-hc).



## About blended search

You can create a blended search app, where multiple data stores can be connected to a single custom search app. This feature lets you use one app to search across multiple sources and types of data.

To make a blended search app, select multiple data stores when creating a new custom search app. If you don't select multiple data stores during creation, then you can't add additional data stores later.

When getting search results, you can either search across all data stores, or filter for results from a single data store.

The following limitations apply:

  * Adding and removing data stores: 
    * To turn on blended search for an app, you must connect at least two data stores to it during app creation.
    * You can add or remove data stores from a blended search app, but the app can't have fewer than two data stores connected to it at any time.
    * If you connect a single data store to a search app during app creation, then you can't add or remove that data store.
  * Website data stores need to have advanced website indexing turned on in order to be used for blended search. For more information, see [Advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#advanced-website-indexing).
  * Data stores that contain unstructured data imported using BigQuery are not supported.
  * Image search (using the [`params`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search#request-body) field with `searchType: 1`) isn't supported.
  * Blended search allows the following fields in [search requests](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search): 
    * `boostSpec`
    * `contentSearchSpec`
    * `dataStoreSpecs`
    * `facetSpecs`
    * `filter`
    * `languageCode`
    * `offset`
    * `oneBoxPageSize`
    * `orderBy`
    * `query`
    * `pageSize`
    * `pageToken`
    * `relevanceScoreSpec`
    * `relevanceThreshold`
    * `session`
    * `sessionSpec`
    * `spellCorrectionSpec`
    * `userInfo`
    * `userPseudoId`
  * Blended search allows the following fields in [`DataStoreSpec`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/DataStoreSpec): 
    * `dataStore`
    * `boostSpec`: If there are boost specs specified for both `SearchRequest` and `dataStoreSpecs`, both boost specs are applied to search results
    * `filter`: If there are filters specified for both `SearchRequest` and `dataStoreSpecs`, both filters are applied to search results
  * Create, Read, Update, and Delete (CRUD) operations on serving configs are supported for blended apps. Only the following fields can be added or updated in a serving config: 
    * `boostControlIds`
    * `displayName`
    * `filterControlIds`
    * `genericConfig`: 
      * `contentSearchSpec`
    * `name`
    * `solutionType`
    * `synonymsControlIds`
  * CRUD operations on the following controls are supported for blended search apps: 
    * `boostAction`
    * `synonymAction`
    * `filterAction`
  * There is a limit of 50 data stores per search app.
  * If one data store uses a CMEK configuration, all other data stores must also use the same CMEK configuration.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
