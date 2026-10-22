---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-bigquery-streaming/
title: Stream DICOM metadata to BigQuery \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:14.943615+00:00
---

# Stream DICOM metadata to BigQuery  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-bigquery-streaming/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Stream DICOM metadata to BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure a DICOM store to export DICOM instance metadata to a BigQuery table whenever one of the following occurs:

  * You store a DICOM instance using the [Store transaction](https://docs.cloud.google.com/healthcare-api/docs/dicom#store_transaction) or by [importing DICOM objects from a Cloud Storage bucket](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-import-export#importing_dicom_objects).
  * You delete a DICOM instance using a [Deletion](https://docs.cloud.google.com/healthcare-api/docs/dicom#deletion) request.
  * You [change the storage class](https://docs.cloud.google.com/healthcare-api/docs/dicom-storage-class) of a DICOM instance.



Streaming DICOM metadata to a BigQuery table synchronizes the table with your DICOM data so you can run complex queries on the latest version of your DICOM store.

## Before you begin

Before you configure your DICOM store, complete the following 

### Set BigQuery permissions

Before streaming DICOM metadata to BigQuery, you must grant the required permissions to the **Cloud Healthcare Service Agent** [service account](https://docs.cloud.google.com/iam/docs/service-accounts). For more information, see [DICOM store BigQuery permissions](https://docs.cloud.google.com/healthcare-api/docs/how-tos/permissions-healthcare-api-gcp-products#dicom_store_bigquery_permissions).

### Learn to export DICOM metadata to BigQuery

Before configuring streaming, understand how to [export DICOM metadata to BigQuery](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-export-bigquery).

## Configure the DICOM store

To enable streaming to BigQuery, configure the [`StreamConfig`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores#streamconfig) object in your DICOM store. In the `StreamConfig` object, set the [`BigQueryDestination`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores#BigQueryDestination) object to a fully qualified BigQuery table URI as a DICOM instance metadata destination.

You can specify up to five BigQuery destinations as comma-separated JSON objects.

Deleting DICOM instances in a DICOM store doesn't delete the BigQuery rows containing the metadata for those instances.

### Console

To update a DICOM store to enable BigQuery streaming, complete the following steps: 

  1. In the Google Cloud console, go to the **Datasets** page.  
[Go to Datasets](https://console.cloud.google.com/healthcare/browser)
  2. Select the dataset containing the DICOM store you want to edit.
  3. Select the DICOM store for which you are adding a streaming configuration.
  4. In the **Overview** tab of the **Data store details** page, click **Add new streaming configuration**.
  5. In the **New streaming configuration** field, click **Browse**. 
     1. In the **Select table** pane, select a BigQuery table.
     2. Click **Select**.
  6. Click **Done**.



### REST

The following samples show how to update a DICOM store to enable BigQuery streaming. In these samples, the DICOM store and the BigQuery table are in the same project. To export DICOM metadata to another project, see [Exporting DICOM metadata to a different project](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-export-bigquery#exporting_dicom_metadata_to_a_different_project).

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the DICOM store's parent dataset
  * DICOM_STORE_ID: the DICOM store ID
  * BIGQUERY_DATASET_ID: the name of an existing BigQuery dataset
  * BIGQUERY_TABLE_ID: a unique name for a table in the BigQuery dataset. See [Table naming](https://docs.cloud.google.com/bigquery/docs/tables#table_naming) for naming requirements. The BigQuery dataset must exist, but the Cloud Healthcare API can update an existing table or create a new one.



Request JSON body: 
    
    
    {
      'streamConfigs': [{
         'bigqueryDestination': {
          'tableUri': 'bq://PROJECT_ID.BIGQUERY_DATASET_ID.BIGQUERY_TABLE_ID'
         }
      }]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      'streamConfigs': [{
         'bigqueryDestination': {
          'tableUri': 'bq://PROJECT_ID.BIGQUERY_DATASET_ID.BIGQUERY_TABLE_ID'
         }
      }]
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID?updateMask=streamConfigs"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      'streamConfigs': [{
         'bigqueryDestination': {
          'tableUri': 'bq://PROJECT_ID.BIGQUERY_DATASET_ID.BIGQUERY_TABLE_ID'
         }
      }]
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID?updateMask=streamConfigs" | Select-Object -Expand Content

#### APIs Explorer

Copy the request body and open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/patch). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID",
      "streamConfigs": [
        {
          "bigqueryDestination": {
            "tableUri": "bq://PROJECT_ID.BIGQUERY_DATASET_ID.BIGQUERY_TABLE_ID"
          }
        }
      ]
    }
    

## Deletion metadata

In previous Cloud Healthcare API versions, DICOM instance metadata was only exported to BigQuery when a DICOM instance was inserted into a DICOM store. When writing metadata for deletions was added, two new columns, named `Type` and `LastUpdated`, were added to the generated table containing the DICOM metadata.

Any metadata in the table that existed before the introduction of deletion metadata has a `NULL` value for these columns. A `NULL` is the lowest value and appears last when sorting by descending order.

## Generated BigQuery view

When you insert or delete a DICOM instance in a DICOM store, the configured BigQuery table is updated.

If a [view](https://docs.cloud.google.com/bigquery/docs/views-intro) of the table doesn't exist, the view is created. Otherwise, the view is updated.

## Limitations and additional behavior

Some DICOM tags might be missing from the exported metadata. If so, the missing tags are added to a separate column named `DroppedTags.TagName` in the destination BigQuery table.

Tags will be missing for one of the following reasons:

  * The DICOM tag is an unsupported VR listed in [Excluded VRs](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-bigquery-schema#excluded_vrs).
  * The DICOM tag approximately exceeds 1 MB.
  * The number of columns in the destination BigQuery table exceeds the [maximum number of columns](https://docs.cloud.google.com/bigquery/quotas#standard_tables). When exporting DICOM metadata to a BigQuery table exceeds the column limit, DICOM tags that don't match an existing column are added to the `DroppedTags.Name` column. If the `DroppedTags` column can't be added, the DICOM tags are dropped without a notification and a warning log is generated. For more information, see Troubleshooting DICOM streaming requests for viewing logs.



### Incorporate deletion metadata into an existing table

The generated view's behaviour depends on whether its base table contains metadata added before the deletion metadata feature was introduced.

Suppose a BigQuery table contains DICOM metadata from before deletion metadata was supported, and then the following occurs:

  1. You insert a DICOM instance into a DICOM store.
  2. You delete the DICOM instance from the DICOM store.
  3. You edit the tags of the original DICOM instance, and insert the modified DICOM instance into the DICOM store.



Because the BigQuery table contained the original metadata before deletion metadata was supported, the original DICOM instance and its edited version have the same studies, series, and instance unique identifiers (UID). The generated view might contain either the original DICOM instance or the most recent DICOM instance. Without the `LastUpdated` column, the view can't identify which DICOM instance is newer.

To ensure you're querying the most recent DICOM instance metadata, do one of the following:

  * Query the base table instead of the view. Ensure the query searches for the updated tags in the edited DICOM instance.
  * Delete the existing table containing DICOM metadata, and then recreate it by [exporting the DICOM metadata to BigQuery manually](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-export-bigquery). The recreated table contains the `LastUpdated` column.

This option removes historical streaming metadata, but ensures that the table contains the `LastUpdated` column with valid values.




## Troubleshoot DICOM streaming requests

If errors occur during a DICOM export metadata to BigQuery request, the errors are logged to [Cloud Logging](https://docs.cloud.google.com/logging/docs). For more information, see [Viewing error logs in Cloud Logging](https://docs.cloud.google.com/healthcare-api/docs/how-tos/logging).

To filter streaming DICOM metadata error logs in the Google Cloud console, complete the following steps:

  1. Go to the **Logs explorer** page.

[Go to Logs explorer](https://console.cloud.google.com/logs/)

  2. In the **Query** field, enter the following query:
         
         logName="healthcare.googleapis.com%2Fdicom_stream"
         

  3. Click **Run query**.

Any error logs are displayed in the **Query results** section.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
