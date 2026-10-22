---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-cloud-storage/
title: Import from Cloud Storage \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:10.613849+00:00
---

# Import from Cloud Storage  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-cloud-storage/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Import from Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

You can create data stores from Cloud Storage tables in two ways:

  * **One-time ingestion** : You import data from a Cloud Storage folder or file into a data store. The data in the data store doesn't change unless you manually [refresh the data](https://docs.cloud.google.com/gemini/enterprise/docs/refresh-data).

  * **Periodic ingestion** : You import data from a Cloud Storage folder or file, and you set a sync frequency that determines how often the data store is updated with the most recent data from that Cloud Storage location.




The following table compares the two ways that you can import Cloud Storage data into Gemini Enterprise data stores.

One-time ingestion | Periodic ingestion  
---|---  
Generally available (GA). | Public preview.  
Data must be refreshed manually. | Data updates automatically every one, three, or five days. Data cannot be manually refreshed.  
Gemini Enterprise creates a single data store from one folder or file in Cloud Storage.  | Gemini Enterprise creates a _data connector_ , and associates a data store (called an _entity_ data store) with it for the file or folder that is specified. Each Cloud Storage data connector can have a single entity data store.  
Data from multiple files, folders, and buckets can be combined in one data store by first ingesting data from one Cloud Storage location and then more data from another location.  | Because manual data import is not supported, the data in an entity data store can only be sourced from one Cloud Storage file or folder.  
Data source access control is supported. For more information, see [Data source access control](https://docs.cloud.google.com/gemini/enterprise/docs/identity). | Data source access control is not supported. The imported data can contain access controls but these controls won't be respected.  
You can create a data store using either the Google Cloud console or the API. | You must use the console to create data connectors and their entity data stores.   
CMEK-compliant. | CMEK-compliant.  
  
## Before you begin

To import data from a source Google Cloud project that's different from the Google Cloud project with the Gemini Enterprise data store, grant the following Identity and Access Management (IAM) roles to the `service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com` service account in the project that contains the Gemini Enterprise data store:

  * [Storage Object Admin (`roles/storage.objectAdmin`)](https://docs.cloud.google.com/storage/docs/access-control/iam-roles)
  * [Storage Object Viewer (`roles/storage.objectViewer`)](https://docs.cloud.google.com/storage/docs/access-control/iam-roles)

**Caution:** When you import data from Cloud Storage into a Gemini Enterprise data store, Cloud Storage permissions aren't imported with the data. After import, any user with [sufficient Gemini Enterprise permissions](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#roles) can view the data, even if they don't have permission to view the data in Cloud Storage.

## Import once from Cloud Storage

To ingest data from Cloud Storage, use the following steps to create a data store and ingest data using either the Google Cloud console or the API.

Before importing your data, review [Prepare data for ingesting](https://docs.cloud.google.com/gemini/enterprise/docs/prepare-data#unstructured).

**Note:** Data import is recursive. That is, if there are folders within the bucket or folder that you specify, files within those folders are imported.

### Console

To use the console to ingest data from a Cloud Storage bucket, follow these steps:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Go to the **Data Stores** page.

  3. Click **Create Data Store**.

  4. On the **Select a data source** page, select **Cloud Storage**.

  5. In the **Select a folder or file you want to import** section, select **Folder** or **File**.

  6. Click **Browse** and choose the data you have [prepared for ingesting](https://docs.cloud.google.com/gemini/enterprise/docs/prepare-data), and then click **Select**. Alternatively, enter the location directly in the **`gs://`** field.

  7. Select what kind of data you are importing.

  8. Click **Continue**.

  9. If you are doing one-time import of structured data:

     1. Map fields to key properties.

     2. If there are important fields missing from the schema, use **Add new field** to add them.

For more information, see [About auto-detect and edit](https://docs.cloud.google.com/gemini/enterprise/docs/provide-schema#about-auto-and-edit).

     3. Click **Continue**.

  10. Choose a region for your data store.

  11. Enter a name for your data store.

  12. Optional: If you selected unstructured documents, you can select parsing and chunking options for your documents. To compare parsers, see [Parse documents](https://docs.cloud.google.com/gemini/enterprise/docs/parse-chunk-documents#parsing). For information about chunking see [Chunk documents for RAG](https://docs.cloud.google.com/gemini/enterprise/docs/parse-chunk-documents#parse-chunk-rag).

The [OCR parser](https://docs.cloud.google.com/gemini/enterprise/docs/parse-chunk-documents#parsing-pdfs) and [layout parser](https://docs.cloud.google.com/gemini/enterprise/docs/parse-chunk-documents#layout-parsing) can incur additional costs. See [Document AI feature pricing](https://docs.cloud.google.com/generative-ai-app-builder/pricing#document_ai_feature_pricing).

To select a parser, expand **Document processing options** and specify the parser options that you want to use.

  13. Click **Create**.

  14. To check the status of your ingestion, go to the **Data Stores** page and click your data store name to see details about it on its **Data** page. When the status column on the **Activity** tab changes from **In progress** to **Import completed** , the ingestion is complete.

Depending on the size of your data, ingestion can take several minutes or several hours.




### REST

To use the command line to create a data store and ingest data from Cloud Storage, follow these steps.

**Note:** If you are importing structured data and want to specify a schema instead of letting Vertex AI auto-detect the schema for you, do the steps in [Provide your own schema as a JSON object](https://docs.cloud.google.com/gemini/enterprise/docs/provide-schema#provide-your-own) and then begin the following procedure at step 2.

  1. Create a data store.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores?dataStoreId=DATA_STORE_ID" \
         -d '{
           "displayName": "DATA_STORE_DISPLAY_NAME",
           "industryVertical": "GENERIC",
           "solutionTypes": ["SOLUTION_TYPE_SEARCH"],
           "contentConfig": "CONTENT_REQUIRED",
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `DATA_STORE_ID`: the ID of the data store that you want to create. This ID can contain only lowercase letters, digits, underscores, and hyphens.
     * `DATA_STORE_DISPLAY_NAME`: the display name of the data store that you want to create.

Optional: To configure document parsing or to turn on document chunking for RAG, specify the [`documentProcessingConfig`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores#documentprocessingconfig) object and include it in your data store creation request. Configuring an OCR parser for PDFs is recommended if you're ingesting scanned PDFs. For how to configure parsing or chunking options, see [Parse and chunk documents](https://docs.cloud.google.com/gemini/enterprise/docs/parse-chunk-documents).

  2. Import data from Cloud Storage.
         
         curl -X POST \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents:import" \
           -d '{
             "gcsSource": {
               "inputUris": ["INPUT_FILE_PATTERN_1", "INPUT_FILE_PATTERN_2"],
               "dataSchema": "DATA_SCHEMA",
             },
             "reconciliationMode": "RECONCILIATION_MODE",
             "autoGenerateIds": "AUTO_GENERATE_IDS",
             "idField": "ID_FIELD",
             "errorConfig": {
               "gcsPrefix": "ERROR_DIRECTORY"
             }
           }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `DATA_STORE_ID`: the ID of the data store.
     * `INPUT_FILE_PATTERN`: a file pattern in Cloud Storage containing your documents.

For structured data or for unstructured data with metadata, an example of the input file pattern is `gs://<your-gcs-bucket>/directory/object.json`and an example of pattern matching one or more files is `gs://<your-gcs-bucket>/directory/*.json`.

For unstructured documents, an example is `gs://<your-gcs-bucket>/directory/*.pdf`. Each file that is matched by the pattern becomes a document.

If `<your-gcs-bucket>` is not under `PROJECT_ID`, you need to give the service account `service-<project number>@gcp-sa-discoveryengine.iam.gserviceaccount.com` "Storage Object Viewer" permissions for the Cloud Storage bucket. For example, if you are importing a Cloud Storage bucket from source project "123" to destination project "456", give `service-456@gcp-sa-discoveryengine.iam.gserviceaccount.com` permissions on the Cloud Storage bucket under project "123".

     * `DATA_SCHEMA`: optional. Values are `document`, `custom`, `csv`, and `content`. The default is `document`.

       * `document`: Upload unstructured data with metadata for unstructured documents. Each line of the file has to follow one of the following formats. You can define the ID of each document:

         * `{ "id": "<your-id>", "jsonData": "<JSON string>", "content": { "mimeType": "<application/pdf or text/html>", "uri": "gs://<your-gcs-bucket>/directory/filename.pdf" } }`
         * `{ "id": "<your-id>", "structData": <JSON object>, "content": { "mimeType": "<application/pdf or text/html>", "uri": "gs://<your-gcs-bucket>/directory/filename.pdf" } }`
       * `custom`: Upload JSON for structured documents. The data is organized according to a schema. You can specify the schema; otherwise it is auto-detected. You can put the JSON string of the document in a consistent format directly in each line, and Gemini Enterprise automatically generates the IDs for each document imported.

       * `content`: Upload unstructured documents (PDF, HTML, DOC, TXT, PPTX). The ID of each document is automatically generated as the first 128 bits of SHA256(GCS_URI) encoded as a hex string. You can specify multiple input file patterns as long as the matched files don't exceed the 100K files limit.

       * `csv`: Include a header row in your CSV file, with each header mapped to a document field. Specify the path to the CSV file using the `inputUris` field.

     * `ERROR_DIRECTORY`: optional. A Cloud Storage directory for error information about the import—for example, `gs://<your-gcs-bucket>/directory/import_errors`. Google recommends leaving this field empty to let Gemini Enterprise automatically create a temporary directory.

     * `RECONCILIATION_MODE`: optional. Values are `FULL` and `INCREMENTAL`. Default is `INCREMENTAL`. Specifying `INCREMENTAL` causes an incremental refresh of data from Cloud Storage to your data store. This does an upsert operation, which adds new documents and replaces existing documents with updated documents with the same ID. Specifying `FULL` causes a full rebase of the documents in your data store. In other words, new and updated documents are added to your data store, and documents that are not in Cloud Storage are removed from your data store. The `FULL` mode is helpful if you want to automatically delete documents that you no longer need.

     * `AUTO_GENERATE_IDS`: optional. Specifies whether to automatically generate document IDs. If set to `true`, document IDs are generated based on a hash of the payload. Note that generated document IDs might not remain consistent over multiple imports. If you auto-generate IDs over multiple imports, Google highly recommends setting `reconciliationMode` to `FULL` to maintain consistent document IDs.

Specify `autoGenerateIds` only when `gcsSource.dataSchema` is set to `custom` or `csv`. Otherwise an `INVALID_ARGUMENT` error is returned. If you don't specify `autoGenerateIds` or set it to `false`, you must specify `idField`. Otherwise the documents fail to import.

     * `ID_FIELD`: optional. Specifies which fields are the document IDs. For Cloud Storage source documents, `idField` specifies the name in the JSON fields that are document IDs. For example, if `{"my_id":"some_uuid"}` is the document ID field in one of your documents, specify `"idField":"my_id"`. This identifies all JSON fields with the name `"my_id"` as document IDs.

Specify this field only when: (1) `gcsSource.dataSchema` is set to `custom` or `csv`, and (2) `auto_generate_ids` is set to `false` or is unspecified. Otherwise an `INVALID_ARGUMENT` error is returned.

Note that the JSON field name specified by `id_field` must be of string type, must be between 1 and 63 characters, and must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034). Otherwise, the documents fail to import.




## Connect to Cloud Storage with periodic syncing

Before importing your data, review [Prepare data for ingesting](https://docs.cloud.google.com/gemini/enterprise/docs/prepare-data).

The following procedure describes how to create a data connector that associates a Cloud Storage location with a Gemini Enterprise data connector and how to specify a folder or file in that location for the data store that you want to create. Data stores that are children of data connectors are called _entity_ data stores.

Data is synced periodically to the entity data store. You can specify synchronization daily, every three days, or every five days.

### Console

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Go to the **Data Stores** page.

  3. Click **Create Data Store**.

  4. On the **Source** page, select **Cloud Storage**.

  5. Select what kind of data you are importing.

  6. Click **Periodic**.

  7. Select the **Synchronization frequency** , how often you want the Gemini Enterprise connector to sync with the Cloud Storage location. You can change the frequency later.

  8. In the **Select a folder or file you want to import** section, select **Folder** or **File**.

  9. Click **Browse** and choose the data you have [prepared for ingesting](https://docs.cloud.google.com/gemini/enterprise/docs/prepare-data), and then click **Select**. Alternatively, enter the location directly in the **`gs://`** field.

  10. Click **Continue**.

  11. Choose a region for your data connector.

  12. Enter a name for your data connector.

  13. Optional: If you selected unstructured documents, you can select parsing and chunking options for your documents. To compare parsers, see [Parse documents](https://docs.cloud.google.com/gemini/enterprise/docs/parse-chunk-documents#parsing). For information about chunking see [Chunk documents for RAG](https://docs.cloud.google.com/gemini/enterprise/docs/parse-chunk-documents#parse-chunk-rag).

The OCR parser and layout parser can incur additional costs.

To select a parser, expand **Document processing options** and specify the parser options that you want to use.

  14. Click **Create**.

You have now created a data connector, which will periodically sync data with the Cloud Storage location. You have also created an entity data store, which is named `gcs_store`.

  15. To check the status of your ingestion, go to the **Data Stores** page and click your data connector name to see details about it on its **Data** page

> **Data ingestion activity** tab. When the status column on the **Data ingestion activity** tab changes from **In progress** to **succeeded** , the first ingestion is complete.

Depending on the size of your data, ingestion can take several minutes to several hours.




After you set up your data source and import data the first time, data is synced from that source at a frequency that you select during setup. About an hour after the data connector is created, the first sync occurs. The next sync then occurs around 24 hours, 72 hours, or 120 hours later.

## Next steps

  * To attach your data store to an app, create an app and select your data store following the steps in [Create a search app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).

  * To preview how your search results appear after your app and data store are set up, see [Preview search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
