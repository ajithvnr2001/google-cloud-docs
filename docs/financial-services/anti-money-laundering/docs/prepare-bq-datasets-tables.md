---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/prepare-bq-datasets-tables/
title: Prepare BigQuery datasets and tables \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:14.465206+00:00
---

# Prepare BigQuery datasets and tables  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/prepare-bq-datasets-tables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Prepare BigQuery datasets and tables Stay organized with collections  Save and categorize content based on your preferences. 

To create AML AI datasets in an instance, you need to stage data in BigQuery within that Google Cloud project. The following sections show one way of preparing these datasets and tables.

## Create a BigQuery output dataset

Run the following command to [create a dataset](https://docs.cloud.google.com/bigquery/docs/datasets) to be used to send the pipeline outputs to BigQuery. In the following command, select a name for BQ_OUTPUT_DATASET_NAME that contains only letters (uppercase or lowercase), numbers, and underscores. _You cannot use hyphens_.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * ``bigquery.datasets.create``



### bash
    
    
    bq mk \
      --location=LOCATION \
      --project_id=PROJECT_ID \
      BQ_OUTPUT_DATASET_NAME
    

### powershell
    
    
    bq mk `
      --location=LOCATION `
      --project_id=PROJECT_ID `
      BQ_OUTPUT_DATASET_NAME
    

To see the AML AI outputs, see [AML output data model](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-output-data-model).

## Create the BigQuery input dataset

Create a BigQuery input dataset. Later, you will input your financial institution's transaction data into this dataset.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * ``bigquery.datasets.create``



### gcloud
    
    
    bq mk \
      --location=LOCATION \
      --project_id=PROJECT_ID \
      BQ_INPUT_DATASET_NAME
    

### Powershell
    
    
    bq mk `
      --location=LOCATION `
      --project_id=PROJECT_ID `
      BQ_INPUT_DATASET_NAME
    

## Create the BigQuery input dataset tables and upload the transaction data

We provide the [AML input data model](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model) schema in the following formats:

  * A single CSV file [`aml-input-data-model.csv`](https://docs.cloud.google.com/static/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model.csv) with all tables included
  * A single JSON file [`aml-input-data-model.json`](https://docs.cloud.google.com/static/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model.json) with all tables included
  * Individual JSON files for each table: 
    * [`party.json`](https://docs.cloud.google.com/static/financial-services/anti-money-laundering/docs/reference/schemas/party.json)
    * [`account_party_link.json`](https://docs.cloud.google.com/static/financial-services/anti-money-laundering/docs/reference/schemas/account_party_link.json)
    * [`transaction.json`](https://docs.cloud.google.com/static/financial-services/anti-money-laundering/docs/reference/schemas/transaction.json)
    * [`risk_case_event.json`](https://docs.cloud.google.com/static/financial-services/anti-money-laundering/docs/reference/schemas/risk_case_event.json)
    * [`party_supplementary_data.json`](https://docs.cloud.google.com/static/financial-services/anti-money-laundering/docs/reference/schemas/party_supplementary_data.json)



We provide the [party registration table](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/register-parties#prepare-party-registration-tables) in JSON format. You use this table later when you register parties in order to create prediction results.

  * [`party_registration.json`](https://docs.cloud.google.com/static/financial-services/anti-money-laundering/docs/reference/schemas/party_registration.json)



To download the JSON file for each table and use it to create the associated BigQuery table by applying the schema, run the following command.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * ``bigquery.datasets.create``


    
    
    for table in party_registration party account_party_link transaction risk_case_event party_supplementary_data interaction_event
    do
      curl -O "https://cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/${table}.json"
      bq mk --table --project_id PROJECT_ID BQ_INPUT_DATASET_NAME.$table $table.json
    done
    

Upload your financial institution's transaction data into the dataset tables. For more information, see any of the [BigQuery quickstarts](https://docs.cloud.google.com/bigquery/docs/quickstarts).

## Grant access to the BigQuery datasets

The API automatically creates a service account in your project. The service account needs access to the BigQuery input and output datasets.

For PROJECT_NUMBER, use the project number associated with PROJECT_ID. You can find the project number on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `bigquery.datasets.setIamPolicy`
  * `bigquery.datasets.update`



  1. Install [`jq`](https://jqlang.github.io/jq/download/) on your development machine. If you cannot install `jq` on your development machine, you can use Cloud Shell or one of the other methods for [granting access to a resource](https://docs.cloud.google.com/bigquery/docs/control-access-to-resources-iam#grant_access_to_a_resource) found in the BigQuery documentation.
  2. Run the following commands to grant read access to the input dataset and its tables.
         
         # The BigQuery input dataset name. You created this dataset and
         # uploaded the financial data into it in a previous step. This dataset should be
         # stored in the Google Cloud project.
         
         export BQ_INPUT_DATASET_NAME="BQ_INPUT_DATASET_NAME"
         
         # The BigQuery tables in the input dataset. These tables should
         # be part of the same project as the intended instance.
         # Make sure to replace each table variable with the appropriate table name.
         export PARTY_TABLE="PARTY_TABLE"
         export ACCOUNT_PARTY_LINK_TABLE="ACCOUNT_PARTY_LINK_TABLE"
         export TRANSACTION_TABLE="TRANSACTION_TABLE"
         export RISK_CASE_EVENT_TABLE="RISK_CASE_EVENT_TABLE"
         # Optional table
         export PARTY_SUPPLEMENTARY_DATA_TABLE="PARTY_SUPPLEMENTARY_DATA_TABLE"
         # Registered parties table
         export PARTY_REGISTRATION_TABLE="PARTY_REGISTRATION_TABLE"
         
         # Grant the API read access to the BigQuery dataset.
         # Update the current access permissions on the BigQuery dataset and store in a temp file.
         # Note: This step requires jq as a dependency.
         # If jq is not available, the file /tmp/mydataset.json may be created manually.
         bq show --format=prettyjson "PROJECT_ID:BQ_INPUT_DATASET_NAME" | jq '.access+=[{"role":"READER","userByEmail":"service-PROJECT_NUMBER@gcp-sa-financialservices.iam.gserviceaccount.com" }]'> /tmp/mydataset.json
         # Update the BigQuery dataset access permissions using the temp file.
         bq update --source /tmp/mydataset.json "PROJECT_ID:BQ_INPUT_DATASET_NAME"
         
         # Grant the API read access to the BigQuery table if the table is provided.
         for TABLE in $PARTY_TABLE $TRANSACTION_TABLE $ACCOUNT_PARTY_LINK_TABLE $RISK_CASE_EVENT_TABLE $PARTY_SUPPLEMENTARY_DATA_TABLE $PARTY_REGISTRATION_TABLE; do
           [ -n TABLE ] && bq add-iam-policy-binding \
             --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-financialservices.iam.gserviceaccount.com" --role="roles/bigquery.dataViewer" \
           PROJECT_ID:BQ_INPUT_DATASET_NAME.${TABLE}
         done
         

  3. Run the following commands to grant write access to the output dataset.
         
         # Note: This step requires jq as a dependency.
         # If jq isn't available, the file /tmp/mydataset.json may be created manually.
         bq show --format=prettyjson PROJECT_ID:BQ_OUTPUT_DATASET_NAME | jq '.access+=[{"role":"roles/bigquery.dataEditor","userByEmail":"service-PROJECT_NUMBER@gcp-sa-financialservices.iam.gserviceaccount.com" }]'> /tmp/perms.json
         
         bq update --source /tmp/perms.json PROJECT_ID:BQ_OUTPUT_DATASET_NAME
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
