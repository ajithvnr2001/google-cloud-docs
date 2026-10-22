---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-completion/
title: Import autocomplete data for search \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:25.617188+00:00
---

# Import autocomplete data for search  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-completion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Import autocomplete data for search Stay organized with collections  Save and categorize content based on your preferences. 

Autocomplete is a feature for predicting the rest of a word a user is typing, which can improve the user search experience. It can provide typeahead suggestion based on your provided dataset or based on user events you provided.

Consider importing autocomplete data only if you want to have additional controls (Do Not Remove List, Deny List) or if you need to use your own autocomplete data. Turning on auto-learning is sufficient for most cases where autocomplete is needed. Auto-learning provides a machine learning-powered suggestion dataset based on user search events. See [Autocomplete](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/completion-overview) for how to turn on auto-learning. 

**Note:** From September 2022, you can use [Cloud console > **Controls**](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/site) > **Autocomplete Controls** UI to trigger data import.

These instructions are for uploading your own autocomplete data only. Keep it up to date if you plan to use your autocomplete dataset all the time. For getting autocomplete results at query time, refer to [CompletionService.CompleteQuery](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/completeQuery). Autocomplete data is used only for search. This data is not used by recommendations.

## Before you begin

Before you can import your autocomplete information, you must have completed the instructions in [Before you begin](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/setting-up), specifically [setting up your project](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/setting-up#project), [creating a service account](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/setting-up#service-account), and [adding the service account to your local environment](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/setting-up#local-environment).

You must have the **Retail Editor** IAM role to perform the import.

## Autocomplete import best practices

When you import autocomplete data, ensure that you implement the following best practices:

  * Read the BigQuery schema listed in the following [sections](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-completion#schema) and API documentation.

  * Do not use placeholder values.

  * Include as many fields as possible.

  * Keep your own autocomplete dataset up to date if you plan to use own uploaded dataset.

  * Importing data from another project is disallowed.




## Import autocomplete data

### Import autocomplete data from BigQuery

AI Commerce Search supports BigQuery data import for Deny List, Do Not Remove List, and Suggestion Terms List. See more details in [Autocomplete](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/completion-overview). 

To import autocomplete data in the correct format from BigQuery, use the [AI Commerce Search autocomplete schema](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-completion#schema) to [create a BigQuery table](https://docs.cloud.google.com/bigquery/docs/tables#creating_an_empty_table_with_a_schema_definition) with the correct format and [load the table](https://docs.cloud.google.com/bigquery/docs/loading-data) with your autocomplete data. Then, upload your data to AI Commerce Search.

For more help with BigQuery tables, see [Introduction to tables](https://docs.cloud.google.com/bigquery/docs/tables-intro). For help with BigQuery queries, see [Overview of querying BigQuery data](https://docs.cloud.google.com/bigquery/docs/query-overview).

#### BigQuery dataset location

When you first create your BigQuery dataset for your autocomplete BigQuery tables, make sure the dataset location is set to the multi-region location `"US"`. Not setting it correctly will cause your import request to fail later. To learn more about BigQuery dataset locations, see [Dataset locations](https://docs.cloud.google.com/bigquery/docs/locations) in the BigQuery documentation.

#### Populate data to BigQuery

Use the [AI Commerce Search autocomplete schema](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-completion#schema) to upload your autocomplete data to BigQuery.

BigQuery can use the schema to validate whether JSON-formatted data has correct field names and types (such as `STRING`, `INTEGER`, and `RECORD`), but cannot perform validations such as determining:

  * If a string field mapped into recognizable enum value.
  * If a string field is using the correct format.
  * If an integer or float field has value in a valid range.
  * If a missing field is a required field.



To ensure the quality of your data and the end user search experience, make sure you refer to the schema and reference documentation for details about values and format.

#### Set up access to your BigQuery dataset

To set up access, make sure that your BigQuery dataset is in the same project as your AI Commerce Search service and complete the following steps.

  1. Open the IAM page in the Google Cloud console.

[Open the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. Select your AI Commerce Search project.

  3. On the **IAM & Admin** page, click _person_add_ **Grant Access**.

  4. For **New principals** , enter `cloud-retail-customer-data-access@system.gserviceaccount.com` and select the **BigQuery > BigQuery Data Viewer** role.

If you do not want to provide the Data Viewer role to the entire project, you can add this role directly to the dataset. [Learn more](https://docs.cloud.google.com/bigquery/docs/dataset-access-controls).

  5. Click **Save**.




#### Trigger data import to AI Commerce Search

###  Console 

  1. [Go to the Controls page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/)

  2. Go to the **Autocomplete Controls** tab.

  3. In the **Term Lists** section, find the type of list you plan to import (**Deny list** , **Do Not Remove list** , or **Suggested terms list**) and click **Import** or **Replace**.

The **Import** pane opens.

  4. Enter the BigQuery path of your data location, or select **Browse** to select the location.

The BigQuery path must be in the same project and its schema should be correct. To check this, click **Browse** and click the table name to view its contents in theBigQuery console.

  5. In the **Import** pane, click **Import**.

The import begins. You can leave the page without disrupting the import.




###  cURL 

  1. Create a data file for the input parameters for the import. Your input parameter values depend on whether you are importing from Cloud Storage or BigQuery.

Use the [BigQuerySource](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/BigQuerySource) object to point to your BigQuery dataset.

     * dataset-id: The ID of the BigQuery dataset.
     * table-id: The ID of the BigQuery table holding your data.
     * data-schema: For the `dataSchema` property, use value `suggestions` (default), `allowlist`, `denylist`. Use the [AI Commerce Search autocomplete schema](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-completion#schema).
    
    {
      "inputConfig":{
        "bigQuerySource": {
          "datasetId":"dataset-id",
          "tableId":"table-id",
          "dataSchema":"data-schema"
        }
      }
    }

  2. Import your autocomplete information to AI Commerce Search by making a `POST` request to the [`CompletionData:import`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.completionData/import) REST method, providing the name of the data file (shown as `input.json` in the example below).
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" -d @./input.json
         "https://retail.googleapis.com/v2alpha/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/completionData:import"

You can check the status programmatically using the API. You should receive a response object that looks something like this:
         
         {
           "name": "projects/PROJECT_ID/locations/global/catalogs/default_catalog/operations/123456",
           "done": false
         }

The name field is the ID of the [operation object](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.operations). To request the status of this object, replace the name field with the value returned by the import method. When the import is complete, the `done` field returns as `true`:
         
         curl -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         "https://retail.googleapis.com/v2alpha/projects/PROJECT_ID/locations/global/catalogs/default_catalog/operations/123456"

When the operation completes, the returned object has a `done` value of `true`, and includes a Status object similar to the following example:
         
         {
           "name": "projects/PROJECT_ID/locations/global/catalogs/default_catalog/operations/123456",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.retail.v2alpha.ImportMetadata",
             "createTime": "2020-01-01T03:33:33.000001Z",
             "updateTime": "2020-01-01T03:34:33.000001Z",
             "successCount": "2",
             "failureCount": "1"
           },
           "done": true
           "response": {
             "@type": "type.googleapis.com/google.cloud.retail.v2alpha.ImportCompletionDataResponse",
           }
         }




### Autocomplete data format

Your JSON file should look like the following examples. The line breaks are for readability; you should provide an entire suggestion on a single line. Each suggestion should be on its own line.

Suggestion minimum required fields:
    
    
    {
      "suggestion": "ABC",
      "globalScore": "0.5"
    }
    

Or:
    
    
    {
      "suggestion": "ABC",
      "frequency": "100"
    }
    

### Autocomplete data import duration

It usually takes about a few minutes to one hour for one import from BigQuery to complete.

When the dataset import is finished, the `done` field in the [operation object](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.operations) is marked as true. After that, it might take additional 1~2 days for data to be indexed and be used in production serving.

## Keep your autocomplete dataset up to date

If you plan to use your own uploaded dataset, it's a best practice to keep the uploaded dataset up-to-date on a regular basis.

### Batch update

You can use the import method to batch update your autocomplete. You do this the same way you do the initial import; follow the steps in Importing autocomplete data. This will replace the whole imported dataset.

## Monitor import health

Keeping your own dataset up to date is important for getting high-quality suggestion results when you use it. You should monitor the import error rates and take action if needed.

## AI Commerce Search autocomplete schema

When importing autocomplete dataset from BigQuery, use the AI Commerce Search schema below to create BigQuery tables with the correct format and load them with your autocomplete data.

### Schema for suggestions

This dataset is used to provide your own autocomplete suggestion phrases with your own scores.

####  AI Commerce Search autocomplete suggestions schema JSON 

###  JSON 
    
    
    [
      {
        "description": "The suggestion text",
        "mode": "NULLABLE",
        "name": "suggestion",
        "type": "STRING"
      },
      {
        "description": "Global score of this suggestion. Control how this suggestion would be scored / ranked. Only one of this and frequency should be set.",
        "mode": "NULLABLE",
        "name": "globalScore",
        "type": "FLOAT"
      },
      {
        "description": "Frequency of this suggestion. Will be used to rank suggestions when score is not available.",
        "mode": "NULLABLE",
        "name": "frequency",
        "type": "INTEGER"
      },
      {
        "description": "BCP-47 language code of this suggestion.",
        "mode": "NULLABLE",
        "name": "languageCode",
        "type": "STRING"
      },
      {
        "description": "If two suggestions have the same groupID, they will not be returned together. Instead the one ranked higher will be returned. This can be used to deduplicate semantically identical suggestions.",
        "mode": "NULLABLE",
        "name": "groupID",
        "type": "STRING"
      },
      {
        "description": "The score of this suggestion within its group",
        "mode": "NULLABLE",
        "name": "groupScore",
        "type": "FLOAT"
      },
      {
        "description": "Device type for this suggestion.",
        "mode": "NULLABLE",
        "name": "deviceType",
        "type": "STRING"
      },
      {
        "description": "Alternative matching phrases for this suggestion.",
        "mode": "REPEATED",
        "name": "alternativePhrases",
        "type": "STRING"
      },
      {
        "fields": [
          {
            "description": "The name of the custom attribute.",
            "mode": "NULLABLE",
            "name": "key",
            "type": "STRING"
          },
          {
            "fields": [
              {
                "description": "The textual values of this custom attribute.",
                "mode": "REPEATED",
                "name": "text",
                "type": "STRING"
              },
              {
                "description": "The numerical values of this custom attribute.",
                "mode": "REPEATED",
                "name": "numbers",
                "type": "FLOAT"
              }
            ],
            "mode": "NULLABLE",
            "name": "value",
            "type": "RECORD"
          }
        ],
        "description": "A custom attribute that is not explicitly modeled, which can be retrieved together with the suggestion at serving time.",
        "mode": "REPEATED",
        "name": "customAttributes",
        "type": "RECORD"
      }
    ]

### Schema for denylist

This dataset is used as a denylist to block phrases from being suggested.

####  AI Commerce Search autocomplete denylist schema JSON 

###  JSON 
    
    
    [
      {
        "description": "The phrase to block from autocomplete suggestions.",
        "mode": "REQUIRED",
        "name": "phrase",
        "type": "STRING"
      },
      {
        "description": "The operator to apply for this phrase. Choose whether to block the exact phrase, or block any suggestions containing this phrase. Supported value \"EXACT_MATCH\", \"CONTAINS\"",
        "mode": "REQUIRED",
        "name": "operator",
        "type": "STRING"
      }
    ]

### Schema for allowlist

This dataset is used for skipping post processes (such as spell correction and zero-result filtering) for all the phrases in this allowlist.

####  AI Commerce Search autocomplete allowlist schema JSON 

###  JSON 
    
    
    [
      {
        "description": "The phrase to be exempted from autocomplete post processing, e.g. spell correction, filtering",
        "mode": "REQUIRED",
        "name": "phrase",
        "type": "STRING"
      },
      {
        "description": "The operator to apply for this phrase. Whether to match the exact phrase, or any suggestions contain this phrase. Supported values are \"EXACT_MATCH\", \"CONTAINS\".",
        "mode": "REQUIRED",
        "name": "operator",
        "type": "STRING"
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
