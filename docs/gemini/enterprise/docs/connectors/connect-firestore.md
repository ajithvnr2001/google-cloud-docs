---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-firestore/
title: Import from Firestore \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:42:43.923075+00:00
---

# Import from Firestore  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-firestore/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Import from Firestore Stay organized with collections  Save and categorize content based on your preferences. 

To ingest data from Firestore, use the following steps to create a data store and ingest data using either the Google Cloud console or the API.

If your Firestore data is in the same project as Gemini Enterprise, go to Import data from Firestore.

If your Firestore data is in a different project than your Gemini Enterprise project, go to Set up Firestore access.

## Set up Firestore access from a different project

To give Gemini Enterprise access to Firestore data that's in a different project, follow these steps:

  1. Replace the following `PROJECT_NUMBER` variable with your Gemini Enterprise project number, and then copy the contents of this code block. This is your Gemini Enterprise service account identifier:
         
         service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com
         

  2. Go to the **IAM & Admin** page.

[IAM & Admin](https://console.cloud.google.com/iam-admin/iam)

  3. Switch to your Firestore project on the **IAM & Admin** page and click **Grant Access**.

  4. For **New principals** , enter the instance's service account identifier and select the **Datastore > Cloud Datastore Import Export Admin** role.

  5. Click **Save**.

  6. Switch back to your Gemini Enterprise project.




Next, go to Import data from Firestore.

## Import data from Firestore

### Console

To use the console to ingest data from Firestore, follow these steps:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Go to the **Data Stores** page.

  3. Click **Create Data Store**.

  4. On the **Select a data source** page, select **Firestore**.

  5. Specify the project ID, database ID, and collection ID of the data that you plan to import.

  6. Click **Continue**.

  7. Choose a region for your data store.

  8. Enter a name for your data store.

  9. Click **Create**.

  10. To check the status of your ingestion, go to the **Data Stores** page and click your data store name to see details about it on its **Data** page. When the status column on the **Activity** tab changes from **In progress** to **Import completed** , the ingestion is complete.

Depending on the size of your data, ingestion can take several minutes or several hours.




### REST

To use the command line to create a data store and ingest data from Firestore, follow these steps:

  1. Create a data store.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores?dataStoreId=DATA_STORE_ID" \
         -d '{
           "displayName": "DISPLAY_NAME",
           "industryVertical": "GENERIC",
           "solutionTypes": ["SOLUTION_TYPE_SEARCH"],
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `DATA_STORE_ID`: the ID of the data store. The ID can contain only lowercase letters, digits, underscores, and hyphens.
     * `DISPLAY_NAME`: the display name of the data store. This might be displayed in the Google Cloud console.
  2. Import data from Firestore.
         
         curl -X POST \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents:import" \
           -d '{
             "firestoreSource": {
               "projectId": "FIRESTORE_PROJECT_ID",
               "databaseId": "DATABASE_ID",
               "collectionId": "COLLECTION_ID",
             },
             "reconciliationMode": "RECONCILIATION_MODE",
             "autoGenerateIds": "AUTO_GENERATE_IDS",
             "idField": "ID_FIELD",
           }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Gemini Enterprise project.
     * `DATA_STORE_ID`: the ID of the data store. The ID can contain only lowercase letters, digits, underscores, and hyphens.
     * `FIRESTORE_PROJECT_ID`: the ID of your Firestore project.
     * `DATABASE_ID`: the ID of your Firestore database.
     * `COLLECTION_ID`: the ID of your Firestore collection.
     * `RECONCILIATION_MODE`: optional. Values are `FULL` and `INCREMENTAL`. Default is `INCREMENTAL`. Specifying `INCREMENTAL` causes an incremental refresh of data from Firestore to your data store. This does an upsert operation, which adds new documents and replaces existing documents with updated documents with the same ID. Specifying `FULL` causes a full rebase of the documents in your data store. In other words, new and updated documents are added to your data store, and documents that are not in Firestore are removed from your data store. The `FULL` mode is helpful if you want to automatically delete documents that you no longer need.
     * `AUTO_GENERATE_IDS`: optional. Specifies whether to automatically generate document IDs. If set to `true`, document IDs are generated based on a hash of the payload. Note that generated document IDs might not remain consistent over multiple imports. If you auto-generate IDs over multiple imports, Google highly recommends setting `reconciliationMode` to `FULL` to maintain consistent document IDs.
     * `ID_FIELD`: optional. Specifies which fields are the document IDs. 



## Next steps

  * To attach your data store to an app, create an app and select your data store following the steps in [Create a search app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).

  * To preview how your search results appear after your app and data store are set up, see [Preview search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
