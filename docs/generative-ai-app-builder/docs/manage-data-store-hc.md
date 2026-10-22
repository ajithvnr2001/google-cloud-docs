---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/manage-data-store-hc/
title: Manage a healthcare search data store \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:27.716248+00:00
---

# Manage a healthcare search data store  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/manage-data-store-hc/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Manage a healthcare search data store Stay organized with collections  Save and categorize content based on your preferences. 

**Deprecated:** Agent Search for healthcare is deprecated and won't be available after May 15, 2027. 

After you create healthcare data stores and import FHIR R4 data, you can perform the following operations to manage them:

  * Cancel batch import.
  * Pause or resume streaming.
  * Manual synchronization of streamed data: 
    * Synchronize all documents.
    * Synchronize selective documents.
    * Synchronize documents after a given timestamp.
  * Delete streaming.



## Cancel batch import

To cancel an ongoing batch import operation, do the following:

### REST

  1. Find the operation ID for the batch import operation. This operation ID is the same as the one returned when you [import the data](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-hc#create-data-store) into your data store. If you already have your operation ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page and in the navigation menu, click **Data Stores**.

[Go to the Data Stores page](https://console.cloud.google.com/gen-app-builder/data-stores)

     2. Click the data store whose import you want to cancel.

     3. On the data store details page, click **View details**. This is only available after the import operation is created and is in progress.

     4. In the **Activity log details** panel, get the operation ID.

  2. Cancel an ongoing batch import.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://us-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/us/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/operations/OPERATION_ID:cancel" \
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `DATA_STORE_ID`: the ID of the data store whose ongoing batch import you want to cancel.
     * `IMPORT_OPERATION_ID`: the ID of the ongoing batch import operation that you want to cancel. 

If the operation is cancelled successfully, you should receive an empty JSON object.




## Pause or resume streaming

To pause or resume a streaming operation, do the following:

### Console

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/)

  2. In the navigation menu, click **Data Stores**.

The **Data Stores** page displays a list of data stores in your Google Cloud project with their details.

  3. Click the data store for which you want to pause or resume the streaming.

  4. On the **Data** page of the data connector, click  pause  **Pause data streaming** to pause streaming or  play_arrow  **Resume data streaming** to resume data streaming.




### REST

  1. Find your collection ID. If you already have your collection ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page and in the navigation menu, click **Data Stores**.

[Go to the Data Stores page](https://console.cloud.google.com/gen-app-builder/data-stores)

     2. Click the name of your data connector whose streaming you want to pause or resume.

     3. On the **Data** page for your data connector, get the collection ID.

  2. Pause or resume streaming within a data connector.
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://us-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/us/collections/COLLECTION_ID/dataConnector?updateMask=auto_run_disabled" \
         -d ' {
           "name":"projects/PROJECT_ID/locations/us/collections/COLLECTION_ID/dataConnector",
           "autoRunDisabled": PAUSE_STREAM_TRUE|FALSE
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `COLLECTION_ID`: the ID of the data connector whose streaming you want to pause or resume.
     * `PAUSE_STREAM_TRUE|FALSE`: a boolean when set to `true` pauses the streaming and when set to `false` resumes a paused streaming. 

#### Response

You should receive a JSON response similar to the following. The field `autoRunDisabled` is only returned when you pause data streaming. 
    
    {
      "name": "projects/PROJECT_NUMBER/locations/us/collections/COLLECTION_ID/dataConnector",
      "state": "ACTIVE",
      "dataSource": "gcp_fhir",
      "params": {
        "instance_uri": "projects/PROJECT_ID/locations/us-central1/datasets/synthea-mock"
      },
      "refreshInterval": "0s",
      "entities": [
        {
          "entityName": "DATA_STORE_NAME",
          "dataStore": "projects/PROJECT_NUMBER/locations/us/collections/default_collection/dataStores/DATA_STORE_ID"
        }
      ],
      "createTime": "DATA_STORE_CREATE_TIMESTAMP",
      "syncMode": "STREAMING",
      "autoRunDisabled": true,
      "actionConfig": {},
      "latestPauseTime": "PAUSE_TIMESTAMP",
      "lastSyncTime": "LAST_SYNC_TIMESTAMP",
      "updateTime": "UPDATE_TIMESTAMP",
      "identityScheduleConfig": {}
    }
    




## Synchronize all documents in a streaming data store

You can manually trigger a backfill for all documents with the supported FHIR resource types. This lets you keep your Agent Search data store up-to-date with your Cloud Healthcare API FHIR store. Data synchronization is possible only in streaming data stores.

To synchronize all documents in a streaming data store, do the following:

### Console

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/)

  2. In the navigation menu, click **Data Stores**.

The **Data Stores** page displays a list of data stores in your Google Cloud project with their details.

  3. Select the data the data connector that you want to synchronize.

  4. On the data store details page, click  sync  **Re-import**.

  5. In the **Re-import data** pane, click  calendar_month , select a date after which you want to synchronize the data, and click **Close**.

  6. In the **Resources to re-import** section, select all the FHIR resource types. Doing so backfills all documents with the supported FHIR resource types.

  7. Click **Re-import**.




### REST

  1. Find your collection ID. If you already have your collection ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page and in the navigation menu, click **Data Stores**.

[Go to the Data Stores page](https://console.cloud.google.com/gen-app-builder/data-stores)

     2. Click the name of your data connector whose streaming you want to pause or resume.

     3. On the **Data** page for your data connector, get the collection ID.

  2. Trigger a synchronization or backfill of all documents with supported FHIR resource types.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://us-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/us/collections/COLLECTION_ID/dataConnector:startConnectorRun" \
         -d ' {
           "syncSinceTimestamp": {}
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `COLLECTION_ID`: the ID of the collection whose streaming you want to pause or resume.

#### Response

You should receive a JSON response similar to the following. The response contains a connector run ID. The `state` field shows one of the states of the synchronization run. For more information, see [ConnectorRun](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/ConnectorRun). 
    
    {
      "name": "projects/189082903055/locations/us/collections/contact/dataConnector/connectorRuns/CONNECTOR_RUN_ID",
      "state": "CONNECTOR_RUN_STATE"
    }
    

If you call the `startConnectorRun` method again while it's still running, you might get an error.




## Synchronize selective documents in a streaming data store

You can import selective documents with the supported FHIR resource types. This is useful when you want to update your Agent Search data store with documents of certain FHIR resources types. Data synchronization is possible only in streaming data stores.

To synchronize selective documents in a streaming data store, do the following:

### Console

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/)

  2. In the navigation menu, click **Data Stores**.

The **Data Stores** page displays a list of data stores in your Google Cloud project with their details.

  3. Select the data the data connector that you want to synchronize.

  4. On the data store details page, click  sync  **Re-import**.

  5. In the **Re-import data** pane, click  calendar_month , select a date after which you want to synchronize the data, and click **Close**.

  6. In the **Resources to re-import** section, select all the FHIR resource types that you want to import. Doing so imports all documents of the selected FHIR resource types.

  7. Click **Re-import**.




### REST

  1. Find your collection ID. If you already have your collection ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page and in the navigation menu, click **Data Stores**.

[Go to the Data Stores page](https://console.cloud.google.com/gen-app-builder/data-stores)

     2. Click the name of your data connector whose streaming you want to pause or resume.

     3. On the **Data** page for your data connector, get the collection ID.

  2. Trigger a synchronization or backfill of selective documents with supported FHIR resource types.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://us-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/us/collections/COLLECTION_ID/dataConnector:startConnectorRun" \
         -d ' {
           "syncSinceTimestamp": {},
           "healthcareFhirResourceTypes": "Patient",
           "healthcareFhirResourceTypes": "RESOURCE_TYPE"
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `COLLECTION_ID`: the ID of the collection whose streaming you want to pause or resume.
     * `RESOURCE_TYPE`: the resource type of the FHIR documents that you want to backfill.

#### Response

You should receive a JSON response similar to the following. The response contains a connector run ID. The `state` field shows one of the states of the synchronization run. For more information, see [ConnectorRun](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/ConnectorRun). 
    
    {
      "name": "projects/189082903055/locations/us/collections/contact/dataConnector/connectorRuns/CONNECTOR_RUN_ID",
      "state": "CONNECTOR_RUN_STATE"
    }
    

If you call the `startConnectorRun` method again while it's still running, you might get an error.




## Synchronize documents after a given timestamp in a streaming data store

You can import selective documents with the supported FHIR resource types after a given timestamp. Data synchronization is possible only in streaming data stores.

To synchronize documents after a given timestamp, do the following:

### Console

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/)

  2. In the navigation menu, click **Data Stores**.

The **Data Stores** page displays a list of data stores in your Google Cloud project with their details.

  3. Select the data the data connector that you want to synchronize.

  4. On the data store details page, click  sync  **Re-import**.

  5. In the **Re-import data** pane, click  calendar_month , select a date after which you want to synchronize the data, and click **Close**.

  6. In the **Resources to re-import** section, select all the FHIR resource types that you want to import. Doing so imports all documents of the selected FHIR resource types.

  7. Click **Re-import**.




### REST

  1. Find your collection ID. If you already have your collection ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page and in the navigation menu, click **Data Stores**.

[Go to the Data Stores page](https://console.cloud.google.com/gen-app-builder/data-stores)

     2. Click the name of your data connector whose streaming you want to pause or resume.

     3. On the **Data** page for your data connector, get the collection ID.

  2. Trigger a synchronization or backfill of all documents with supported FHIR resource types.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://us-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/us/collections/COLLECTION_ID/dataConnector:startConnectorRun" \
         -d ' {
           "syncSinceTimestamp": {
             "seconds": TIMESTAMP_SECONDS,
             "nanos": TIMESTAMP_NANOS
           }
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `COLLECTION_ID`: the ID of the collection whose streaming you want to pause or resume.
     * `TIMESTAMP_SECONDS`: the value of the timestamp in seconds since when you want to import the documents. It follows the [Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) format.
     * `TIMESTAMP_NANOS`: the value of the timestamp in seconds since when you want to import the documents. It follows the [Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) format.

#### Response

You should receive a JSON response similar to the following. The response contains a connector run ID. The `state` field shows one of the states of the synchronization run. For more information, see [ConnectorRun](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/ConnectorRun). 
    
    {
      "name": "projects/189082903055/locations/us/collections/contact/dataConnector/connectorRuns/CONNECTOR_RUN_ID",
      "state": "CONNECTOR_RUN_STATE"
    }
    

If you call the `startConnectorRun` method again while it's still running, you might get an error.




## Delete streaming

To delete a streaming operation, do the following:

### Console

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/)

  2. In the navigation menu, click **Data Stores**.

The **Data Stores** page displays a list of data stores in your Google Cloud project with their details.

  3. In the list of the data stores, click  more_vert **More options** for the data connector that you want to delete.

  4. Click  delete **Delete**.

  5. In the dialog that appears, type **yes** and click **Confirm** to confirm the deletion.




### REST

  1. Find your collection ID. If you already have your collection ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page and in the navigation menu, click **Data Stores**.

[Go to the Data Stores page](https://console.cloud.google.com/gen-app-builder/data-stores)

     2. Click the name of your data connector whose streaming you want to pause or resume.

     3. On the **Data** page for your data connector, get the collection ID.

  2. Trigger a synchronization or backfill of all documents with supported FHIR resource types.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://us-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/us/collections/COLLECTION_ID/dataConnector:startConnectorRun" \
         -d ' {
           "syncSinceTimestamp": {
             "seconds": TIMESTAMP_SECONDS,
             "nanos": TIMESTAMP_NANOS
           }
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `COLLECTION_ID`: the ID of the collection whose streaming you want to pause or resume.
     * `TIMESTAMP_SECONDS`: the value of the timestamp in seconds since when you want to import the documents. It follows the [Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) format.
     * `TIMESTAMP_NANOS`: the value of the timestamp in seconds since when you want to import the documents. It follows the [Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) format.

#### Response

You should receive a JSON response similar to the following. The response contains a connector run ID. The `state` field shows one of the states of the synchronization run. For more information, see [ConnectorRun](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/ConnectorRun). 
    
    {
      "name": "projects/189082903055/locations/us/collections/contact/dataConnector/connectorRuns/CONNECTOR_RUN_ID",
      "state": "CONNECTOR_RUN_STATE"
    }
    

If you call the `startConnectorRun` method again while it's still running, you might get an error.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
