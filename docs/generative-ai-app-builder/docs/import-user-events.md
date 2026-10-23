---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/import-user-events/
title: Import historical user events \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:11.432470+00:00
---

# Import historical user events  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/import-user-events/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Import historical user events Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to import user event data from past events in bulk. User events are required for media apps. If you don't use media apps, importing user events isn't required. However, recording user events is recommended for custom search and recommendations apps.

For the user event types that you can import, see the `eventType` field of the [`userEvents`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents) object. By importing user events, you can improve the quality of your results. For example, user events affect the ranking of search results. Results with higher click-through rates are boosted, while results with lower click-through rates are buried. Only import user events for documents that you are already imported into your data store.

If an event has documents listed in `userEvents.Documents`, then Agent Search automatically joins the events with that document. Joining allows Agent Search to attribute events such as clicks and views to the correct document in a search result or recommendation. For custom search and recommendations apps, joining occurs _asynchronously_ , that is, user events are joined to documents after the batch import is complete (generally happening within minutes). For media apps, joining occurs _synchronously_ , Agent Search starts joining user events to documents while the batch import is still in progress. For how to view unjoined event metrics in the console, see [View aggregated user event information](https://docs.cloud.google.com/generative-ai-app-builder/docs/manage-user-events#view-events).

If you are using a search app with multiple data stores attached, import user events at the location level instead of the data-store level. This allows a given user event to be sent to the data store that it's associated with. When importing user events at a location level, include the `engine` field in the user event to associate the event with the correct app. For examples of user events that include the `engine` field, see the following:

  * [Custom apps user event type examples and schemas ](https://docs.cloud.google.com/generative-ai-app-builder/docs/user-events#formats)
  * [Media apps user event type examples and schemas ](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-user-events)



For more information on the import method, see [`userEvents.import`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.userEvents/import).

To import user events in real-time, see [Record real-time user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/record-user-events).

You can import historical events in the following ways:

  * From Cloud Storage
  * From BigQuery
  * As local JSON data



For the JSON representation for user events, see [`userEvents`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents) in the API reference.

## Before you begin

Before you import user events:

  * Create a data store and an app.
  * Review [About media user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-user-events) or [About user events for custom apps](https://docs.cloud.google.com/generative-ai-app-builder/docs/user-events) for user event requirements.



## Import historical user events from Cloud Storage

If you have a media app, you can import user events using the Google Cloud console or the API. For other app types, you can only import using the API. 

###  Console 

To import user events for media apps using the console, follow these steps:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/engines)

  2. On the **Apps** page, click your media app.

  3. Go to the **Data** page.

For media recommendations apps, the **Requirements** tab displays the media documents and user events that you need to import.

  4. Click the **Events** tab. If you have already imported any events, information about them is displayed on this tab.

  5. Click **Import events**.

  6. Select **Cloud Storage** as your data source.

  7. Enter or select the Cloud Storage location of your user events.

  8. Click **Import**.

  9. The **Activity** tab displays the status of your import.

  10. If import errors occur, in the **Activity** tab:

     1. Expand the error in the **Details** column and click **View details** to see more information in the **Activity log details** pane.

     2. In the **Activity log details** pane, click **View full error logs** to see the error in Logs Explorer.




###  REST 

To import historical user events in bulk from Cloud Storage, follow these steps:

  1. Create one or more data files for the input parameters for the import. Use the [`gcsSource`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/GcsSource) object to point to your Cloud Storage bucket.
         
         {
         "gcsSource": {
           "inputUris": ["INPUT_FILE_1", "INPUT_FILE_2"],
           "dataSchema": "user_event"
           },
           "errorConfig":{
               "gcsPrefix":"ERROR_DIRECTORY"
           }
         }
         

Replace the following:

     * `INPUT_FILE`: a file in Cloud Storage containing your user event data. Make sure each user event is on its own single line, with no line breaks. For the JSON representation for user events, see [`userEvents`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents) in the API reference. The input file fields must be in this format: `gs://<bucket>/<path-to-file>/`.
     * `ERROR_DIRECTORY`: optional. A Cloud Storage directory for error information about the import—for example, `gs://<your-gcs-bucket>/directory/import_errors`. Google recommends leaving this field empty to let Agent Search automatically create a temporary directory.
  2. Import your events by making a POST request to the [`userEvents.import`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.userEvents/import) method, providing the name of the data file.
         
         curl -X POST \
             -v \
             -H "Content-Type: application/json; charset=utf-8" \
             -H "Authorization: Bearer "$(gcloud auth print-access-token)"" \
             --data @DATA_FILE.json \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_NUMBER/locations/global/userEvents:import"
         




## Import historical user events from BigQuery

When creating tables for user events in BigQuery, use the schemas documented in [About media user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-user-events#bigquery) and [About user events for custom apps](https://docs.cloud.google.com/generative-ai-app-builder/docs/user-events#bigquery). Each `search` user event must include an `engine` field to associate the event with an app. For more information, see [`engine`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#UserEvent.FIELDS.engine).

### Set up BigQuery access

If your BigQuery dataset is in a different project than your data store, follow these steps to set up access to BigQuery.

  1. Open the [IAM & Admin](https://console.cloud.google.com/iam-admin/iam) page in the Google Cloud console.
  2. Select the project that contains the data store that you want to import user events into.
  3. Select the **Include Google-provided role grants** checkbox.
  4. Find the service account with the name **Discovery Engine Service Account**.
  5. If you have not previously initiated an import operation with Discovery Engine, this service account might not be listed. If you don't see this service account, return to the import task and initiate the import. When it fails due to permission errors, return here and complete this task. The Discovery Engine service account will be listed.
  6. Copy the identifier for the service account, which looks like an email address—for example, `service-525@gcp-sa-discoveryengine.iam.gserviceaccount.com`.
  7. Switch to your BigQuery project (on the same **IAM & Admin** page) and click **Grant Access**.
  8. For **New principals** , enter the identifier for the service account and select the **BigQuery > BigQuery Data Viewer** role.
  9. Click **Save**.



For more information about BigQuery access, see [Controlling access to datasets](https://docs.cloud.google.com/bigquery/docs/dataset-access-controls) in the BigQuery documentation.

### Import events from BigQuery

If you have a media app, you can import user events using the Google Cloud console or the API. For other app types, you can only import using the API. 

###  Console 

To import user events for media apps using the console, follow these steps:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/engines)

  2. On the **Apps** page, click your media app.

  3. Go to the **Data** page.

For media recommendations apps, the **Requirements** tab displays the media documents and user events that you need to import.

  4. Click the **Events** tab. If you have already imported any events, information about them is displayed on this tab.

  5. Click **Import events**.

  6. Select **BigQuery** as your data source.

  7. Enter or select the BigQuery path for your user events.

  8. Click **Import**.

  9. The **Activity** tab displays the status of your import.

  10. If import errors occur, in the **Activity** tab:

     1. Expand the error in the **Details** column and click **View details** to see more information in the **Activity log details** pane.

     2. In the **Activity log details** pane, click **View full error logs** to see the error in Logs Explorer.




###  REST 

To import historical user events in bulk from BigQuery, follow these steps:

  1. Import your user events by making a POST request to the [`userEvents.import`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.userEvents/import) method, providing the name of the BigQuery project, dataset ID, and table ID.

When importing your events, use the value `user_event` for `dataSchema`.
         
         curl \
           -v \
           -X POST \
           -H "Content-Type: application/json; charset=utf-8" \
           -H "Authorization: Bearer "$(gcloud auth print-access-token)"" \
           "https://discoveryengine.googleapis.com/v1/projects/[PROJECT_NUMBER]/locations/global/userEvents:import" \
           --data '{
               "bigquerySource": {
                   "projectId":"PROJECT_ID",
                   "datasetId": "DATASET_ID",
                   "tableId": "TABLE_ID",
                   "dataSchema": "user_event"
               }
             }'
         




## Import historical user events as local JSON data

You can import user events by including local JSON data for the events in your call to the [`userEvents.import`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.userEvents/import) method.

To put user event data into a JSON file and specify the file in an API request, follow these instructions:

  1. Create a JSON file containing your user event data. For the JSON representation for user events, see [`userEvents`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents) in the API reference documentation.
         
         {
           "inlineSource": {
             "userEvents": [
               {
                 USER_EVENT_1
               },
               {
                 USER_EVENT_2
               }
             ]
           }
         }
         

  2. Import your events by making a POST request to the [`userEvents.import`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.userEvents/import) method, providing the name of the data file.
         
         curl -X POST \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/json; charset=utf-8" \
             --data @[JSON_FILE] \
           "https://discoveryengine.googleapis.com/v1/projects/PROJECT_NUMBER/locations/global/userEvents:import"
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
