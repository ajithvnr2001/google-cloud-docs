---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-media/
title: Create a media data store \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:14.038447+00:00
---

# Create a media data store  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-media/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Create a media data store Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to create a data store for media and import data into it.

## Before you begin

Make sure that you do the following:

  * Review the concepts related to media data and schema:

    * [About media documents and data stores](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-documents)

    * [Provide or auto-detect a schema](https://docs.cloud.google.com/generative-ai-app-builder/docs/provide-schema)

  * Decide whether you are using the [predefined Google schema for your media data or your own schema](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-documents#predefined-vs-custom).

  * If you're using your own schema, make sure your schema has fields that map well to the [media properties](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-documents#custom-schema) for the custom schema: `title`, `url`, `category`, and so on.

  * Put your media documents into the JSON schema and upload the data to BigQuery or Cloud Storage.

**Note:** It's also possible to create a data store and upload the data directly from a local file. If you want to take that approach, see Import documents using the API. The disadvantage of this approach is that you can't edit the schema until all the data is uploaded and if you then make changes to the schema you have to wait until it is reindexed before you can use the data store.
  * Review [About media user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-user-events) and prepare your user events for import. User events are required for all media apps.




## Choose the procedure according to your data source

To create a media data store and import documents, go to the section for the source that you plan to use:

  * BigQuery

  * Cloud Storage

  * Import documents using the API




## Import from BigQuery

### Console

To use the Google Cloud console to create a media data store and import documents and user events from BigQuery, follow these steps:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/)

  2. Go to the **Data Stores** page.

  3. Click **Create data store**.

  4. On the **Source** page, select **BigQuery**.

  5. Select **Media - BigQuery table with structured media data** as the kind of data that you are importing.

  6. In the **BigQuery path** field, click **Browse** , select the BigQuery data that you have prepared for ingesting, and then click **Select**. Alternatively, enter the location directly in the **BigQuery path** field.

  7. If your data is in the predefined Google schema, choose **Google predefined schema** , click **Continue** , and skip to step 11.

  8. If your data is in your own schema, choose **Custom schema** and click **Continue**.

  9. Review the detected schema and use the **Key properties** menu to assign properties to your schema fields.

**Note:** If fields are missing, click **Add new fields** and use those controls to add missing fields.
  10. Click **Continue**.

You can't continue until the required key properties are mapped, indicated by green checkmarks check_circle instead of orange warning marks warning.

  11. Enter a name for your data store and click **Create**.




## Import from Cloud Storage

### Console

To use the Google Cloud console to create a media data store and import documents from Cloud Storage, follow these steps:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/)

  2. Go to the **Data Stores** page.

  3. Click **Create data store**.

  4. On the **Source** page, select **Cloud Storage**.

  5. Select **Structured media data (JSONL containing media files)** as the kind of data that you are importing.

  6. In the **Select a folder or file you want to import** section, select **Folder** or **File**.

  7. Click **Browse** and choose the data that you have prepared for ingesting, and then click **Select**. Alternatively, enter the location directly in the **`gs://`** field.

  8. If your data is in the predefined Google schema, choose **Google predefined schema** , click **Continue** , and skip to step 11.

  9. If your data is in your own schema, choose **Custom schema** and click **Continue**.

  10. Review the detected schema and use the **Key properties** menu to assign properties to your schema fields.

**Note:** If fields are missing, click **Add new fields** and use those controls to add missing fields.
  11. Click **Continue**.

You can't continue until the required key properties are mapped, indicated by green checkmarks check_circle instead of orange warning marks warning.

  12. Enter a name for your data store and click **Create**.




## Import documents using the API

If you are using the Google predefined schema, you can import your documents by making a `POST` request to the [`Documents:import`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.dataStores.branches.documents/import) REST method, using the [`InlineSource`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.dataStores.branches.documents/import#InlineSource) object to specify your data.

For an example of the JSON document format, see JSON document format.

### Import requirements

Here are the requirements for importing media documents using the API:

  * Each document must be on its own line.

  * The maximum number of documents in a single import is 100.




### Procedure

To import media documents using the API, do the following:

  1. Create a data store.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores?dataStoreId=DATA_STORE_ID" \
         -d '{
           "displayName": "DATA_STORE_DISPLAY_NAME",
           "industryVertical": "MEDIA"
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `DATA_STORE_ID`: the ID of the Agent Search data store that you want to create. This ID can contain only lowercase letters, digits, underscores, and hyphens.
     * `DATA_STORE_DISPLAY_NAME`: the display name of the Agent Search data store that you want to create.
  2. Create the JSON file for your document and call it `./data.json`:
         
         {
         "inlineSource": {
         "documents": [
           { DOCUMENT_1 },
           { DOCUMENT_2 }
         ]
         }
         }
         

  3. Call the POST method:
         
         curl -X POST \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          -H "Content-Type: application/json; charset=utf-8" \
          --data @./data.json \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/dataStores/DATA_STORE_ID/branches/0/documents:import"

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `DATA_STORE_ID`: the ID of your data store.



### JSON document format

The following examples show `Document` entries in JSON format.

Provide an entire document on a single line. Each document should be on its own line.

Minimum required fields:
    
    
    {
       "id": "sample-01",
       "schemaId": "default_schema",
       "jsonData": "{\"title\":\"Test document title\",\"categories\":[\"sports > clip\",\"sports > highlight\"],\"uri\":\"http://www.example.com\",\"media_type\":\"sports-game\",\"available_time\":\"2022-08-26T23:00:17Z\"}"
    }

Complete object:
    
    
    {
       "id": "child-sample-0",
       "schemaId": "default_schema",
       "jsonData": "{\"title\":\"Test document title\",\"description\":\"Test document description\",\"language_code\":\"en-US\",\"categories\":[\"sports > clip\",\"sports > highlight\"],\"uri\":\"http://www.example.com\",\"images\":[{\"uri\":\"http://example.com/img1\",\"name\":\"image_1\"}],\"media_type\":\"sports-game\",\"in_languages\":[\"en-US\"],\"country_of_origin\":\"US\",\"content_index\":0,\"persons\":[{\"name\":\"sports person\",\"role\":\"player\",\"rank\":0,\"uri\":\"http://example.com/person\"},],\"organizations \":[{\"name\":\"sports team\",\"role\":\"team\",\"rank\":0,\"uri\":\"http://example.com/team\"},],\"hash_tags\":[\"tag1\"],\"filter_tags\":[\"filter_tag\"],\"production_year\":1900,\"duration\":\"100s\",\"content_rating\":[\"PG-13\"],\"aggregate_ratings\":[{\"rating_source\":\"imdb\",\"rating_score\":4.5,\"rating_count\":1250}],\"available_time\":\"2022-08-26T23:00:17Z\"}"
    }

## Monitor import and view data

  1. To check the status of your ingestion, go to the **Data Stores** page and click your data store name to see details about it on its **Data** page.

  2. Click the **Activity** tab.

When the status column on the **Activity** tab changes from **In progress** to **Import completed** , the ingestion is complete.

Depending on the size of your data, ingestion can take several minutes or several hours.

**Important:** Wait until your document import is complete before importing user events to avoid unjoined user events.
  3. Click **Documents** to view the data you imported.




## Import user events

To import user events to your media data store:

  * Follow the instructions in [Import historical user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/import-user-events).



## What's next

  * [Create a media recommendations app or a media search app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-app-media).

  * Keep your document data fresh.

Ideally, you should update your data store daily, by importing fresh data. Scheduling periodic imports prevents model quality from degrading over time. You can use [Google Cloud Scheduler](https://cloud.google.com/scheduler) to automate imports.

You can update only new or changed documents, or you can import the entire data store. If you import documents that are already in your data store, they are not added again. Any document that has changed is updated.

  * Keep your user-event data fresh.

It is particularly important that you keep your user events fresh. The recommendations app stops working if there aren't enough fresh user events to meet the data requirements.

For information about importing user event data in real time, see [Record real-time user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/record-user-events).

For information about monitoring user-event requirements, see [Check data quality for media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/check-media-data-quality).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
