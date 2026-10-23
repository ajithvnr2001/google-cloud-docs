---
url: https://docs.cloud.google.com/gemini/enterprise/docs/get-datastore-details/
title: Get data store and entity details \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:44.973218+00:00
---

# Get data store and entity details  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/get-datastore-details/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Developer guide ](https://docs.cloud.google.com/gemini/enterprise/docs/developer-guide)



Send feedback 

#  Get data store and entity details Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to retrieve resource details for Gemini Enterprise data stores and their underlying entities using either the Google Cloud console or the Discovery Engine REST API.

When you interact with data stores using APIs—such as configuring resource-level [IAM access controls](https://docs.cloud.google.com/gemini/enterprise/docs/iam-policy-for-apps-and-data-stores), querying search endpoints, or automating ingestion pipelines—you need the unique resource IDs of target data stores and their underlying entities.

**Key Term:** In Gemini Enterprise, the term _data store_ can be used interchangeably with the term _connector_ or _data connector_.

## Data store concepts

To understand how data store resources are structured in the Discovery Engine API, consider the following concepts:

Concept | Description  
---|---  
**Data store** |  A container for data ingested from Google or third-party data sources. Standalone data stores belong to the default collection (`default_collection`). For more information, see [Gemini Enterprise concepts](https://docs.cloud.google.com/gemini/enterprise/docs/concepts#ase-data-stores) and [About apps and data stores](https://docs.cloud.google.com/gemini/enterprise/docs/apps-data-stores).   
**Data collection** |  A logical grouping resource within a Google Cloud project and location (`projects/{project}/locations/{location}/collections/{collection}`). Multi-entity third-party data stores (such as Jira, Salesforce, or SharePoint Online) create a dedicated collection representing the data store instance.  
**Data store entity** |  When you connect a third-party data source that contains multiple entity types (such as Jira issues, Jira projects, or SharePoint files), Gemini Enterprise automatically creates a separate child data store for each entity type. These entity data stores reside as child resources under `collections/default_collection/dataStores/{DATA_STORE_ENTITY_ID}`.  For more information, see [Structured data for third-party data stores](https://docs.cloud.google.com/gemini/enterprise/docs/apps-data-stores#structured-third-party) and [Introduction to connectors and data stores](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/introduction-to-connectors-and-data-stores).  
  
## Retrieve data store and entity details

Select one of the following options:

### Console

To retrieve data store and entity details in the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the **Gemini Enterprise** > **Data Stores** page.

[Go to the Data Stores page](https://console.cloud.google.com/gemini-enterprise/data-stores)

  2. Click the name of your target data store.

  3. On the data store details page, view the **Data store ID** displayed in the header.

  4. If the data store contains entities, click the **Entities** tab to view the list of configured entities, display names, and their corresponding entity data store IDs (for example, `DataConnector3_entityA` and `DataConnector3_entityB`).




### REST

To retrieve data store and entity IDs using the REST API, complete the following steps:

  1. List data store collection IDs (for multi-entity data stores):

For third-party data stores with multiple entities (such as Jira or Salesforce), Gemini Enterprise creates a dedicated collection representing the connector instance. Call the `collections` list endpoint to retrieve collection IDs in your project:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections"
         

Replace the following:

     * `PROJECT_ID`: The ID of your Google Cloud project.
     * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
       * `us` for the US multi-region
       * `eu` for the EU multi-region
       * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
     * `LOCATION`: the multi-region of your data store: `global`, `us`, or `eu`.

The response contains the list of collections:
    
    {
      "collections": [
        {
          "name": "projects/123456789/locations/global/collections/DataConnector3",
          "displayName": "Jira Production Data Store"
        }
      ]
    }
    

In this example, the collection ID is `DataConnector3`. Use this ID when configuring collection-level access controls for the connector instance.

  2. List entity and standalone data store IDs under `default_collection`:

In Gemini Enterprise, all data store resources, including standalone data stores and child entities for multi-entity connectors, reside under `default_collection`. Even though a multi-entity data store has a dedicated collection ID (such as `DataConnector3`), its child entity data stores are registered under `default_collection` and prefixed with the connector ID.

Call the `dataStores` list endpoint on `default_collection` to locate your data store and entity IDs:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/dataStores"
         

Replace the following:

     * `PROJECT_ID`: The ID of your Google Cloud project.
     * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
       * `us` for the US multi-region
       * `eu` for the EU multi-region
       * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
     * `LOCATION`: the multi-region of your data store: `global`, `us`, or `eu`.

The response contains the list of data stores:
    
    {
      "dataStores": [
        {
          "name": "projects/123456789/locations/global/collections/default_collection/dataStores/DataConnector3_entityA",
          "displayName": "Jira Issues Entity"
        },
        {
          "name": "projects/123456789/locations/global/collections/default_collection/dataStores/DataConnector3_entityB",
          "displayName": "Jira Projects Entity"
        }
      ]
    }
    

In this example, the entity data store IDs are `DataConnector3_entityA` and `DataConnector3_entityB`. Use these IDs when configuring access controls for all underlying entity data stores of a multi-entity data store using the REST API.




## What's next

  * [Configure granular access controls for apps and data stores](https://docs.cloud.google.com/gemini/enterprise/docs/iam-policy-for-apps-and-data-stores#configure-data-store-permissions)
  * [Discovery Engine REST API reference](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
