---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/refresh-data/
title: Refresh structured and unstructured data \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:24.521536+00:00
---

# Refresh structured and unstructured data  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/refresh-data/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Refresh structured and unstructured data Stay organized with collections  Save and categorize content based on your preferences. 

This page describes refreshing structured and unstructured data.

To refresh your website apps, see [Refresh your web page](https://docs.cloud.google.com/generative-ai-app-builder/docs/recrawl-websites).

## Refresh structured data

You can refresh the data in a structured data store as long as you use a schema that is the same or backward compatible with the schema in the data store. For example, adding only new fields to an existing schema is backward compatible.

You can refresh structured data in the Google Cloud console or using the API.

### Console

To use the Google Cloud console to refresh structured data from a branch of a data store, follow these steps:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/engines)

  2. In the navigation menu, click **Data Stores**.

  3. In the **Name** column, click the data store that you want to edit.

  4. On the **Documents** tab, click add**Import data**.

  5. To refresh from Cloud Storage:

     1. In the **Select a data source** pane, select **Cloud Storage**.
     2. In the **Import data from Cloud Storage** pane, click **Browse** , select the bucket that contains your refreshed data, and then click **Select**. Alternatively, enter the bucket location directly in the **gs://** field.
     3. Under **Data Import Options** , select an import option.
     4. Click **Import**.
  6. To refresh from BigQuery:

     1. In the **Select a data source** pane, select **BigQuery**.
     2. In the **Import data from BigQuery** pane, click **Browse** , select a table that contains your refreshed data, and then click **Select**. Alternatively, enter the table location directly in the **BigQuery path** field.
     3. Under **Data Import Options** , select an import option.
     4. Click **Import**.



### REST

Use the [`documents.import`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.documents/import) method to refresh your data, specifying the appropriate `reconciliationMode` value.

To refresh structured data from BigQuery or Cloud Storage using the command line, follow these steps:

  1. Find your data store ID. If you already have your data store ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page and in the navigation menu, click **Data Stores**.

[Go to the Data Stores page](https://console.cloud.google.com/gen-app-builder/data-stores)

     2. Click the name of your data store.

     3. On the **Data** page for your data store, get the data store ID.

  2. To import your structured data from BigQuery call the following method. You can import either from BigQuery or Cloud Storage. To import from Cloud Storage, skip to the next step.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents:import" \
         -d '{
           "bigquerySource": {
             "projectId": "PROJECT_ID",
             "datasetId":"DATASET_ID",
             "tableId": "TABLE_ID",
             "dataSchema": "DATA_SCHEMA_BQ",
           },
           "reconciliationMode": "RECONCILIATION_MODE",
           "autoGenerateIds": AUTO_GENERATE_IDS,
           "idField": "ID_FIELD",
           "errorConfig": {
             "gcsPrefix": "ERROR_DIRECTORY"
           }
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `DATA_STORE_ID`: the ID of the Agent Search data store.
     * `DATASET_ID`: the name of your BigQuery dataset.
     * `TABLE_ID`: the name of your BigQuery table.
     * `DATA_SCHEMA_BQ`: an optional field to specify the schema to use when parsing data from the BigQuery source. Can have the following values: 
       * `document`: the default value. The BigQuery table that you use must conform to the following default BigQuery schema. You can define the ID of each document yourself, while wrapping the entire data in the `json_data` string.
       * `custom`: any BigQuery table schema is accepted, and Agent Search automatically generates the IDs for each document that is imported.
     * `ERROR_DIRECTORY`: an optional field to specify a Cloud Storage directory for error information about the import—for example, `gs://<your-gcs-bucket>/directory/import_errors`. Google recommends leaving this field empty to let Agent Search automatically create a temporary directory.
     * `RECONCILIATION_MODE`: an optional field to specify how the imported documents are reconciled with the existing documents in the destination data store. Can have the following values: 
       * `INCREMENTAL`: the default value. Causes an incremental refresh of data from BigQuery to your data store. This does an upsert operation, which adds new documents and replaces existing documents with updated documents with the same ID.
       * `FULL`: causes a full rebase of the documents in your data store. Therefore, new and updated documents are added to your data store, and documents that are not in BigQuery are removed from your data store. The `FULL` mode is helpful if you want to automatically delete documents that you no longer need.
     * `AUTO_GENERATE_IDS`: an optional field to specify whether to automatically generate document IDs. If set to `true`, document IDs are generated based on a hash of the payload. Note that generated document IDs might not remain consistent over multiple imports. If you auto-generate IDs over multiple imports, Google highly recommends setting `reconciliationMode` to `FULL` to maintain consistent document IDs.

Specify `autoGenerateIds` only when `bigquerySource.dataSchema` is set to `custom`. Otherwise, an `INVALID_ARGUMENT` error is returned. If you don't specify `autoGenerateIds` or set it to `false`, you must specify `idField`. Otherwise, the documents fail to import.

     * `ID_FIELD`: an optional field to specify which fields are the document IDs. For BigQuery source files, `idField` indicates the name of the column in the BigQuery table that contains the document IDs.

Specify `idField` only when both these conditions are satisfied, otherwise, an `INVALID_ARGUMENT` error is returned:

       * `bigquerySource.dataSchema` is set to `custom`
       * `auto_generate_ids` is set to `false` or is unspecified.

Additionally, the value of the BigQuery column name must be of string type, must be between 1 and 63 characters, and must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034). Otherwise, the documents fail to import.

Here is the default BigQuery schema. Your BigQuery table must conform to this schema when you set `dataSchema` to `document`.
    
    [
     {
       "name": "id",
       "mode": "REQUIRED",
       "type": "STRING",
       "fields": []
     },
     {
       "name": "jsonData",
       "mode": "NULLABLE",
       "type": "STRING",
       "fields": []
     }
    ]
    

  3. To import your structured data from Cloud Storage call the following method. You can either import from BigQuery or Cloud Storage. To import from BigQuery, go to the previous step.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents:import" \
         -d '{
           "gcsSource": {
             "inputUris": ["GCS_PATHS"],
             "dataSchema": "DATA_SCHEMA_GCS",
           },
           "reconciliationMode": "RECONCILIATION_MODE",
           "idField": "ID_FIELD",
           "errorConfig": {
             "gcsPrefix": "ERROR_DIRECTORY"
           }
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `DATA_STORE_ID`: the ID of the Agent Search data store.
     * `GCS_PATHS`: a list of comma-separated URIs to Cloud Storage locations from where you want to import. Each URI can be 2,000 characters long. URIs can match the full path for a storage object or can match the pattern for one or more objects. For example, `gs://bucket/directory/*.json` is a valid path.
     * `DATA_SCHEMA_GCS`: an optional field to specify the schema to use when parsing data from the BigQuery source. Can have the following values: 
       * `document`: the default value. The BigQuery table that you use must conform to the following default BigQuery schema. You can define the ID of each document yourself, while wrapping the entire data in the `json_data` string.
       * `custom`: any BigQuery table schema is accepted, and Agent Search automatically generates the IDs for each document that is imported.
     * `ERROR_DIRECTORY`: an optional field to specify a Cloud Storage directory for error information about the import—for example, `gs://<your-gcs-bucket>/directory/import_errors`. Google recommends leaving this field empty to let Agent Search automatically create a temporary directory.
     * `RECONCILIATION_MODE`: an optional field to specify how the imported documents are reconciled with the existing documents in the destination data store. Can have the following values: 
       * `INCREMENTAL`: the default value. Causes an incremental refresh of data from BigQuery to your data store. This does an upsert operation, which adds new documents and replaces existing documents with updated documents with the same ID.
       * `FULL`: causes a full rebase of the documents in your data store. Therefore, new and updated documents are added to your data store, and documents that are not in BigQuery are removed from your data store. The `FULL` mode is helpful if you want to automatically delete documents that you no longer need. 



### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import discoveryengine
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = "YOUR_PROJECT_ID"
    # location = "YOUR_LOCATION" # Values: "global"
    # data_store_id = "YOUR_DATA_STORE_ID"
    # bigquery_dataset = "YOUR_BIGQUERY_DATASET"
    # bigquery_table = "YOUR_BIGQUERY_TABLE"
    
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )
    
    # Create a client
    client = discoveryengine.[DocumentServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.DocumentServiceClient.html)(client_options=client_options)
    
    # The full resource name of the search engine branch.
    # e.g. projects/{project}/locations/{location}/dataStores/{data_store_id}/branches/{branch}
    parent = client.[branch_path](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.DocumentServiceClient.html#google_cloud_discoveryengine_v1_services_document_service_DocumentServiceClient_branch_path)(
        project=project_id,
        location=location,
        data_store=data_store_id,
        branch="default_branch",
    )
    
    request = discoveryengine.[ImportDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsRequest.html)(
        parent=parent,
        bigquery_source=discoveryengine.[BigQuerySource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BigQuerySource.html)(
            project_id=project_id,
            dataset_id=bigquery_dataset,
            table_id=bigquery_table,
            data_schema="custom",
        ),
        # Options: `FULL`, `INCREMENTAL`
        reconciliation_mode=discoveryengine.[ImportDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsRequest.html).[ReconciliationMode](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsRequest.ReconciliationMode.html).INCREMENTAL,
    )
    
    # Make the request
    operation = client.[import_documents](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.DocumentServiceClient.html#google_cloud_discoveryengine_v1_services_document_service_DocumentServiceClient_import_documents)(request=request)
    
    print(f"Waiting for operation to complete: {operation.operation.name}")
    response = operation.result()
    
    # After the operation is complete,
    # get information from operation metadata
    metadata = discoveryengine.[ImportDocumentsMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsMetadata.html)(operation.metadata)
    
    # Handle the response
    print(response)
    print(metadata)

## Refresh unstructured data

You can refresh unstructured data in the Google Cloud console or using the API.

### Console

To use the Google Cloud console to refresh unstructured data from a branch of a data store, follow these steps:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/engines)

  2. In the navigation menu, click **Data Stores**.

  3. In the **Name** column, click the data store that you want to edit.

  4. On the **Documents** tab, click add**Import data**.

  5. To ingest from a Cloud Storage bucket (with or without metadata):

     1. In the **Select a data source** pane, select **Cloud Storage**.
     2. In the **Import data from Cloud Storage** pane, click **Browse** , select the bucket that contains your refreshed data, and then click **Select**. Alternatively, enter the bucket location directly in the **`gs://`** field.
     3. Under **Data Import Options** , select an import option.
     4. Click **Import**.
  6. To ingest from BigQuery:

     1. In the **Select a data source** pane, select **BigQuery**.
     2. In the **Import data from BigQuery** pane, click **Browse** , select a table that contains your refreshed data, and then click **Select**. Alternatively, enter the table location directly in the **BigQuery path** field.
     3. Under **Data Import Options** , select an import option.
     4. Click **Import**.



### REST

To refresh unstructured data using the API, re-import it using the [`documents.import`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.documents/import) method, specifying the appropriate `reconciliationMode` value. For more information about importing unstructured data, see [Unstructured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-engine-es#unstructured-data).

### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import discoveryengine
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = "YOUR_PROJECT_ID"
    # location = "YOUR_LOCATION" # Values: "global"
    # data_store_id = "YOUR_DATA_STORE_ID"
    
    # Examples:
    # - Unstructured documents
    #   - `gs://bucket/directory/file.pdf`
    #   - `gs://bucket/directory/*.pdf`
    # - Unstructured documents with JSONL Metadata
    #   - `gs://bucket/directory/file.json`
    # - Unstructured documents with CSV Metadata
    #   - `gs://bucket/directory/file.csv`
    # gcs_uri = "YOUR_GCS_PATH"
    
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )
    
    # Create a client
    client = discoveryengine.[DocumentServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.DocumentServiceClient.html)(client_options=client_options)
    
    # The full resource name of the search engine branch.
    # e.g. projects/{project}/locations/{location}/dataStores/{data_store_id}/branches/{branch}
    parent = client.[branch_path](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.DocumentServiceClient.html#google_cloud_discoveryengine_v1_services_document_service_DocumentServiceClient_branch_path)(
        project=project_id,
        location=location,
        data_store=data_store_id,
        branch="default_branch",
    )
    
    request = discoveryengine.[ImportDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsRequest.html)(
        parent=parent,
        gcs_source=discoveryengine.[GcsSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GcsSource.html)(
            # Multiple URIs are supported
            input_uris=[gcs_uri],
            # Options:
            # - `content` - Unstructured documents (PDF, HTML, DOC, TXT, PPTX)
            # - `custom` - Unstructured documents with custom JSONL metadata
            # - `document` - Structured documents in the discoveryengine.Document format.
            # - `csv` - Unstructured documents with CSV metadata
            data_schema="content",
        ),
        # Options: `FULL`, `INCREMENTAL`
        reconciliation_mode=discoveryengine.[ImportDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsRequest.html).[ReconciliationMode](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsRequest.ReconciliationMode.html).INCREMENTAL,
    )
    
    # Make the request
    operation = client.[import_documents](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.DocumentServiceClient.html#google_cloud_discoveryengine_v1_services_document_service_DocumentServiceClient_import_documents)(request=request)
    
    print(f"Waiting for operation to complete: {operation.operation.name}")
    response = operation.result()
    
    # After the operation is complete,
    # get information from operation metadata
    metadata = discoveryengine.[ImportDocumentsMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsMetadata.html)(operation.metadata)
    
    # Handle the response
    print(response)
    print(metadata)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
