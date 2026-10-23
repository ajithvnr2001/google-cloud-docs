---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-bigtable/
title: Import from Bigtable \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:09.679916+00:00
---

# Import from Bigtable  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-bigtable/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Import from Bigtable Stay organized with collections  Save and categorize content based on your preferences. 

To ingest data from Bigtable, use the following steps to create a data store and ingest data using the API.

## Set up Bigtable access

To give Gemini Enterprise access to Bigtable data that's in a different project, follow these steps:

  1. Replace the following `PROJECT_NUMBER` variable with your Gemini Enterprise project number, then copy the contents of this code block. This is your Gemini Enterprise service account identifier:
         
         service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com`
         

  2. Go to the **IAM & Admin** page.

[IAM & Admin](https://console.cloud.google.com/iam-admin/iam)

  3. Switch to your Bigtable project on the **IAM & Admin** page and click **Grant Access**.

  4. For **New principals** , enter the instance's service account identifier and select the **Bigtable > Bigtable Reader** role.

  5. Click **Save**.

  6. Switch back to your Gemini Enterprise project.




Next, go to Import data from Bigtable.

## Import data from Bigtable

### REST

To use the command line to create a data store and ingest data from Bigtable, follow these steps:

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
  2. Import data from Bigtable.
         
         curl -X POST \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents:import" \
           -d '{
             "bigtableSource ": {
               "projectId": "BIGTABLE_PROJECT_ID",
               "instanceId": "INSTANCE_ID",
               "tableId": "TABLE_ID",
               "bigtableOptions": {
                 "keyFieldName": "KEY_FIELD_NAME",
                 "families": {
                   "key": "KEY",
                   "value": {
                     "fieldName": "FIELD_NAME",
                     "encoding": "ENCODING",
                     "type": "TYPE",
                     "columns": [
                       {
                         "qualifier": "QUALIFIER",
                         "fieldName": "FIELD_NAME",
                         "encoding": "COLUMN_ENCODING",
                         "type": "COLUMN_VALUES_TYPE"
                       }
                     ]
                   }
                  }
                  ...
               }
             },
             "reconciliationMode": "RECONCILIATION_MODE",
             "autoGenerateIds": "AUTO_GENERATE_IDS",
             "idField": "ID_FIELD",
           }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Gemini Enterprise project.
     * `DATA_STORE_ID`: the ID of the data store. The ID can contain only lowercase letters, digits, underscores, and hyphens.
     * `BIGTABLE_PROJECT_ID`: the ID of your Bigtable project.
     * `INSTANCE_ID`: the ID of your Bigtable instance.
     * `TABLE_ID`: the ID of your Bigtable table.
     * `KEY_FIELD_NAME`: optional but recommended. The field name to use for the row key value after ingesting to Gemini Enterprise.
     * `KEY`: required. A string value for the column family key.
     * `ENCODING`: optional. The encoding mode of the values when the type is not STRING.This can be overridden for a specific column by listing that column in `columns` and specifying an encoding for it.
     * `COLUMN_TYPE`: optional. The type of values in this column family.
     * `QUALIFIER`: required. Qualifier of the column.
     * `FIELD_NAME`: optional but recommended. The field name to use for this column after ingesting to Gemini Enterprise.
     * `COLUMN_ENCODING`: optional. The encoding mode of the values for a specific column when the type is not STRING.
     * `RECONCILIATION_MODE`: optional. Values are `FULL` and `INCREMENTAL`. Default is `INCREMENTAL`. Specifying `INCREMENTAL` causes an incremental refresh of data from Bigtable to your data store. This does an upsert operation, which adds new documents and replaces existing documents with updated documents with the same ID. Specifying `FULL` causes a full rebase of the documents in your data store. In other words, new and updated documents are added to your data store, and documents that are not in Bigtable are removed from your data store. The `FULL` mode is helpful if you want to automatically delete documents that you no longer need.
     * `AUTO_GENERATE_IDS`: optional. Specifies whether to automatically generate document IDs. If set to `true`, document IDs are generated based on a hash of the payload. Note that generated document IDs might not remain consistent over multiple imports. If you auto-generate IDs over multiple imports, Google highly recommends setting `reconciliationMode` to `FULL` to maintain consistent document IDs.

Specify `autoGenerateIds` only when `bigquerySource.dataSchema` is set to `custom`. Otherwise an `INVALID_ARGUMENT` error is returned. If you don't specify `autoGenerateIds` or set it to `false`, you must specify `idField`. Otherwise the documents fail to import.

     * `ID_FIELD`: optional. Specifies which fields are the document IDs. 




## Next steps

  * To attach your data store to an app, create an app and select your data store following the steps in [Create a search app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).

  * To preview how your search results appear after your app and data store are set up, see [Preview search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
