---
url: https://docs.cloud.google.com/gemini/enterprise/docs/apps-data-stores/
title: About apps and data stores \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:06.915797+00:00
---

# About apps and data stores  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/apps-data-stores/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  About apps and data stores Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Gemini Enterprise apps and data stores.

With Gemini Enterprise, you create an app and connect it to a data store. A given Google Cloud project can contain multiple apps.

Key terms:

  * **App** : A Gemini Enterprise app provides search results, actions, and agents to your end users. The term _app_ can be used interchangeably with the term _engine_ in the context of APIs.

  * **Data store** : A data store is an entity that contains the data ingested from a first-party data source such as Cloud Storage or third-party applications such as Jira or Salesforce. Data stores that contain data from third-party applications are also called _data connectors_.




## Relationship between apps and data stores

An app must be connected to a data store in order to use the data from it to serve search results, answers, or actions.

Apps have a many-to-many relationship with data stores. When multiple data stores are connected to a single app, this is referred to as _blended search_. For information about limitations of connecting a search app to more than one data store, see About blended search.

**Note:** You can't connect website data stores to your Gemini Enterprise search and assistant apps.

## Method of app creation and data ingestion

How you create an app and ingest data depends on the type of data you have:

  * For third-party data, you use the Google Cloud console, not the API, to create your app and ingest data.

  * For other data, you can use either the Google Cloud console or the API.




## Documents

Each data store has one or more data records, called _documents_. What a document represents varies depending on the type of data in the data store:

  * **Data for third-party data sources**. A document is an entity specific to the third-party data source, such as a Jira issue or Confluence space.

  * **Structured data**. A document is a row in a table or a JSON record that follows a particular schema. You can provide this schema yourself or you can let Gemini Enterprise derive the schema from the ingested data.

  * **Unstructured data**. A document is a file in HTML, PDF with embedded text, or TXT format. PPTX and DOCX formats are available in Preview.




## Data stores and apps

In Gemini Enterprise, there are various kinds of data stores. A data store can contain only one type of data.

  * Third-party data
  * Structured data
  * Unstructured data



### Structured data for third-party data stores

The following third-party data source connectors are available in Preview with allowlist:

  * Confluence
  * Jira
  * Salesforce
  * Sharepoint Online
  * Slack



Data from these third parties is considered structured data.

When you set up a new connector, you select a synchronization frequency. You also select which entities to sync. Entities vary depending on the source, such as issues for Jira and content and spaces for Confluence. A unique data store is created for each entity. Entity data stores are grouped by connector instance.

#### What's next

  * [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source).
  * [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).



### Structured data

A data store with structured data enables semantic search or recommendations over structured data. You can import data from BigQuery or Cloud Storage. You can also manually upload structured JSON data through the API.

For example, you can enable search or recommendations over a product catalog for your ecommerce experience or a directory of doctors for provider search or recommendations.

Gemini Enterprise auto-detects the schema from the data that you import. Optionally, you can provide a schema for your data. Providing a schema for your data typically improves the quality of results.

#### What's next

  * [Prepare structured data for ingestion](https://docs.cloud.google.com/gemini/enterprise/docs/prepare-data#structured).
  * Create a search data store using one of these methods: 
    * [Import from BigQuery](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-bigquery).
    * [Import from Cloud Storage](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-cloud-storage).
  * [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).



### Unstructured data

An unstructured data store enables semantic search or recommendations over data such as documents and images.

Unstructured data stores support documents in HTML, PDF with embedded text, and TXT format. PPTX and DOCX formats are available in Preview.

Search provides results in the form of 10 URLs and summarized answers for natural language queries. Documents must be uploaded to a Cloud Storage bucket with appropriate access permissions. For example, a financial institution can enable search or recommendations over their private corpus of financial research publications, or a biotech company can enable search or recommendations over their private repository of medical research.

#### What's next

  * [Prepare unstructured data for ingestion](https://docs.cloud.google.com/gemini/enterprise/docs/prepare-data#unstructured).
  * Create a search data store using one of these methods: 
    * [Import from BigQuery](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-bigquery).
    * [Import from Cloud Storage](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-cloud-storage).
    * [Sync from Google Drive](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive).
  * [Create a first-party datastore](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store) for your unstructured data.
  * [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).



## About blended search

With blended search, multiple data stores can be connected to a single app. This lets the app search across multiple sources and types of data.

**Note:** Blended search is rate-limited in the Gemini Enterprise Standard and Gemini Enterprise Frontline editions. Unlimited and enhanced blended search requires the Gemini Enterprise Plus edition.

To make a blended search app, you connect one or more data stores to an app after it has been created.

When getting search results, you can either search across all data stores, or filter for results from a single data store.

Blended search has the following limitations:

  * Data stores that contain unstructured data imported using BigQuery are not supported.
  * Blended search allows the following fields in [search requests](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search): 
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
  * Blended search allows the following fields in `dataStoreSpecs`: 
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
  * If one data store uses a CMEK configuration, all other data stores must also use the same CMEK configuration.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
