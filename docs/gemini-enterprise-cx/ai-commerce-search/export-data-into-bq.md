---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/export-data-into-bq/
title: Export your data into BigQuery \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:19.646953+00:00
---

# Export your data into BigQuery  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/export-data-into-bq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Export your data into BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to upload retail product and user event data into BigQuery. After your data is in BigQuery, you'll be able to use it to perform sales forecasting with Vertex AI and to view the data in prebuilt Looker dashboards.

If your commerce data is already in product and user event tables in BigQuery, in AI Commerce Search format, you can skip this page and go directly to [Get dashboards that show key performance indicators](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/get-dashboards-that-show-kpis) and [Generate sales forecasts from retail data](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/generate-sales-forecasts). For more information about the format, see [Product schema](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/catalog#schema) and [About user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events).

**Note:** Only `bigqueryDestination` is supported for exporting user events. Moreover, the BigQuery dataset provided in `bigqueryDestination` must reside in the US multi-region.

## Before you begin

Before you can export your commerce data into BigQuery, you must have completed the procedures in [Initial setup](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/setting-up).

This includes:

  * [Importing catalog information](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/upload-catalog).
  * [Recording real-time user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/record-events).
  * [Importing historical user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-user-events).



## Create a dataset in BigQuery

You need to create one or two datasets in BigQuery to hold your product and user event data.

You can use one dataset to hold both types of data or you can create two datasets, one for each type of data.

You must create the datasets in the same project where you implemented AI Commerce Search.

  1. If you haven't used BigQuery in your project before, enable the BigQuery API and make sure that you have the IAM role that lets you create datasets and tables.

See [Before you begin](https://docs.cloud.google.com/bigquery/docs/quickstarts/query-public-dataset-console#before-you-begin) and [Access control with IAM](https://docs.cloud.google.com/bigquery/docs/access-control) in the BigQuery documentation.

  2. Create a dataset in BigQuery in the **US multi-region**. For example, name it `retail_data`.

**Note:** AI Commerce Search user event data cannot be exported to non-US regions. Keep in mind that AI Commerce Search does not use PII. If you choose an EU-based region for the dataset location, your Core BigQuery Customer Data resides in the EU. Core BigQuery Customer Data is defined in the BigQuery [Service Specific Terms](https://cloud.google.com/terms/service-terms#13-google-bigquery-service).
  3. Optional: To place your user event data in a separate dataset from your product data, create a second dataset. For example, name it `retail_user_event_data`.




For more information about creating BigQuery datasets see the [BigQuery documentation](https://docs.cloud.google.com/bigquery/docs/datasets).

This dataset will be used to hold the data tables that you export. The following procedures describe how to export.

## Export your AI Commerce Search catalog to a BigQuery table

Use the [`export`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/export) method to export your retail catalog into a BigQuery table.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: The ID of the AI Commerce Search API project where you created the BigQuery dataset. 
  * BRANCH_ID: The ID of the catalog branch. Use `default_branch` to get data from the default branch. For more information, see [Catalog branches](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/catalog#branch). 
  * DATASET_ID: The name of the dataset that you created in [ Create a dataset in BigQuery](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/export-data-into-bq#create-dataset). For example, use `retail_data` or `retail_product_data`. The dataset must be in the same project. Do not add the project ID to the `datasetId` field here. 
  * TABLE_ID_PREFIX: A prefix for the table ID. This prefix can't be an empty string. A suffix of `_retail_products_BRANCH_ID` is added to complete the table name. For example, if the prefix is `test`, the table is named `_test_retail_products_BRANCH_ID`. 



Request JSON body: 
    
    
    {
      "outputConfig":
      {
        "bigqueryDestination":
        {
          "datasetId": "DATASET_ID",
            "tableIdPrefix": "TABLE_ID_PREFIX",
            "tableType": "view"
        }
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "outputConfig":
      {
        "bigqueryDestination":
        {
          "datasetId": "DATASET_ID",
            "tableIdPrefix": "TABLE_ID_PREFIX",
            "tableType": "view"
        }
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://retail.googleapis.com/v2alpha/projects/PROJECT_ID/locations/global/catalogs/default_catalog/branches/BRANCH_ID/products:export"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "outputConfig":
      {
        "bigqueryDestination":
        {
          "datasetId": "DATASET_ID",
            "tableIdPrefix": "TABLE_ID_PREFIX",
            "tableType": "view"
        }
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://retail.googleapis.com/v2alpha/projects/PROJECT_ID/locations/global/catalogs/default_catalog/branches/BRANCH_ID/products:export" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/branches/BRANCH_ID/operations/17986570020347019923",
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.retail.v2alpha.ExportProductsResponse",
        "outputResult": {
          "bigqueryResult": [
            {
              "datasetId": "DATASET_ID",
              "tableId": "TABLE_ID_PREFIX_retail_products_BRANCH_ID"
            }
          ]
        }
      }
    }
    

## Export your user events to a BigQuery table

Use the `userEvents.export` method to export your retail user events into a BigQuery table:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: The ID of the AI Commerce Search API project where you created the BigQuery dataset. 
  * DATASET_ID: The name of the dataset that you created in [Create a dataset in BigQuery](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/export-data-into-bq#create-dataset). For example, use `retail_data` or `retail_product_data`. 
  * TABLE_ID_PREFIX: A prefix for the table ID. This prefix can't be an empty string. A suffix of `retail_products` is added to complete the table name. For example, if the prefix is `test`, the table is named`test_retail_products`. 



Request JSON body: 
    
    
    {
      "outputConfig":
      {
        "bigqueryDestination":
        {
          "datasetId": "DATASET_ID",
            "tableIdPrefix": "TABLE_ID_PREFIX",
            "tableType": "view"
        }
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "outputConfig":
      {
        "bigqueryDestination":
        {
          "datasetId": "DATASET_ID",
            "tableIdPrefix": "TABLE_ID_PREFIX",
            "tableType": "view"
        }
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://retail.googleapis.com/v2alpha/projects/PROJECT_ID/locations/global/catalogs/default_catalog/userEvents:export"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "outputConfig":
      {
        "bigqueryDestination":
        {
          "datasetId": "DATASET_ID",
            "tableIdPrefix": "TABLE_ID_PREFIX",
            "tableType": "view"
        }
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://retail.googleapis.com/v2alpha/projects/PROJECT_ID/locations/global/catalogs/default_catalog/userEvents:export" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/operations/17203443067109586170",
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.retail.v2alpha.ExportUserEventsResponse",
        "outputResult": {
          "bigqueryResult": [
            {
              "datasetId": "DATASET_ID",
              "tableId": "TABLE_ID_PREFIX_retail_user_events"
            }
          ]
        }
      }
    }
    

## About the exported data

Here are things to know about the commerce data that you export to BigQuery tables:

  * The data that is exported to BigQuery tables in your project are [authorized views](https://docs.cloud.google.com/bigquery/docs/authorized-views), not [materialized views](https://docs.cloud.google.com/bigquery/docs/materialized-views-intro).

  * You cannot change or update the data in these tables.

  * Products are refreshed hourly.

  * User events are refreshed near-real time.




## About the exported user event data

Here are things to know about the product information that is included with the exported user event data.

### Product price information

The way product price information is returned by the `userEvents.export` method depends on the following:

  * **You included price information in your user event data at the time of ingestion.** When you call the `userEvents.export` method, the price returned with a user event is the price of the product at the time of the event.

  * **You did not include price information with your user event data, but you included price information in your product data at the time of ingestion.** When you call the `userEvents.export` method, the price returned with a user event is not necessarily the price of the product at the time of the event. It is the price found in your product data at the time of ingestion.

  * **You did not include price information with your user event data and there is no price information available in your product data.** When you call the `userEvents.export` method, no price is returned with user events.




### Other product information

All product information (except price) is joined to user event information at the time you call the `userEvents.export` method. Product values can change from the time of the user event to the time you call `userEvents.export`. For this reason, the non-price product values returned in the user event table could be different from the product values at the time of the user event.

## Optional: Confirm that the new tables are in BigQuery

After you have exported your product data and user-event data to BigQuery, make sure that new tables are present.

  1. In BigQuery, navigate to the dataset or datasets that you created in Create dataset in BigQuery.

  2. Open the dataset(s) and make sure you see the two tables that you exported. For example, look for tables with names ending in `_retail_products_BRANCH_ID` and `retail_user_events`.




For more information about working with BigQuery tables, see [Query and view data](https://docs.cloud.google.com/bigquery/docs/query-overview).

Review the [Data governance](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/data-governance-retail) page for more information about how AI Commerce Search handles customer data.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
