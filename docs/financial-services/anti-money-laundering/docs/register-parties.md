---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/register-parties/
title: Register your parties \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:44:47.047154+00:00
---

# Register your parties  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/register-parties/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Register your parties Stay organized with collections  Save and categorize content based on your preferences. 

This page leads you through the following steps to register and deregister parties in order to create prediction results:

  1. Ensure you're ready to register parties
  2. Prepare the party registration tables
  3. Use the [`projects.locations.instances.importRegisteredParties`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances/importRegisteredParties) method to register or deregister parties
  4. Validate the method response
  5. (Optional) Export a table of registered parties



## Before you begin

Before you begin, you need an [AML AI instance](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/set-up-instance).

To enable a model to create risk score predictions, you must first register parties. We recommend that you register parties when you already have the following:

  * One or more [datasets](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/prepare-bq-datasets-tables)
  * A [tuned, trained, and backtested model](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/overview-model-preparation)



## When to register parties

Before you can create predictions for a [party](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/glossary#party) in one of your [datasets](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/understand-data-model-requirements), you need to register the party. Registration is not required for training, tuning, or backtesting.

Prediction results are used in investigating customers for money laundering in either a production or testing (parallel) phase. You may also want to build your own governance and model analysis processes around the results you obtain from predictions.

Registering parties incurs additional monthly costs per registered party (see the [Pricing page](https://cloud.google.com/financial-services/anti-money-laundering/pricing) for more information).

**Note:** Before registering parties for an instance, consider whether there is another instance which uses the same parties. If so, see [Party registration sharing for multiple instances](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/registration-sharing).

## How to prepare party registration tables

Read the [Pricing page](https://cloud.google.com/financial-services/anti-money-laundering/pricing) for information on registering parties.

Prepare a table for the [line of business](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/glossary#lob) you want to register parties for. If you have some parties registered already, this party registration table could contain a subset of the parties from the [Party](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#party) table that you want to use for prediction results.

### Retail parties schema

Column| Type| Description  
---|---|---  
`party_id`| [`STRING`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#string_type)| Unique identifier of the party in the instance's datasets  
`party_size`| [`STRING`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#string_type)| NULL; content is ignored for retail party registrations  
  
### Commercial parties schema

Column| Type| Description  
---|---|---  
`party_id`| [`STRING`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#string_type)| Unique identifier of the party in the instance's datasets  
`party_size`| [`STRING`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#string_type) | Requested party size. The tier is based on the average number of monthly transactions for the party over the preceding 365 days: 

  * `SMALL` for small commercial parties with less than 500 average monthly transactions
  * `LARGE` for large commercial parties with greater than or equal to 500 average monthly transactions

All values are case sensitive.   
  
## How to register parties

Parties are registered separately for each AML AI instance. Note the following:

  * Retail and commercial parties must be registered separately. Use separate API calls and separate party registration tables. If a party is in both lists, they are considered separate registrations.
  * Predictions require all parties to be registered with the [line of business](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/glossary#lob) associated with the engine version used. **You can't create prediction results if a dataset is used that contains any party not registered with the same line of business.**
  * The provided party registration table is used to either append to the existing list of registered parties in the instance or replace all registered parties for the provided line of business in the instance.
  * Once registered, a party can't be deregistered for some time (see the [Pricing page](https://cloud.google.com/financial-services/anti-money-laundering/pricing)). For this reason, you can set the `validateOnly` field to `TRUE`. This field allows you to see the net effect and response of the method without changing the registered parties. Once validated, you can rerun the operation and set the `validateOnly` parameter to `FALSE`.
  * Always check the response of a registration request to ensure all parties were registered successfully, even if a previous `validateOnly` request succeeded.
  * For commercial party registrations, a value other than `SMALL` or `LARGE` in the `party_size` field in the party registration table triggers an error (`Invalid party_size present in table`). Registered parties are not updated.
  * For retail party registrations, the `party_size` field is ignored and all parties in the provided party registration table are registered.



To import registered parties, use the [`projects.locations.instances.importRegisteredParties`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances/importRegisteredParties) method.

(The following information is also available in [Create and manage instances](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-instances).)

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `financialservices.v1instances.importRegisteredParties`



Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
  * `LOCATION`: the location of the instance; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `INSTANCE_ID`: the user-defined identifier for the instance
  * `BQ_INPUT_REGISTERED_PARTIES_DATASET_NAME`: a BigQuery dataset that contains a table that describes the registered parties
  * `PARTY_REGISTRATION_TABLE`: the table that lists the registered parties **Note** : You can provide multiple tables that list the registered parties. Use the format `"bq://{project}.{bqDatasetID}.{bqTableID}"` for each table in the `partyTables` array.
  * `UPDATE_MODE`: use `REPLACE` to replace parties that are removable in the registered parties table with new parties, or use `APPEND` to add new parties to the registered parties table
  * `LINE_OF_BUSINESS`: this field must match the `lineOfBusiness` value in the [engine version](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/manage-engine-versions) used by the [engine config](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-engine-configs); use `COMMERCIAL` for commercial banking customers (legal and natural entities), or use `RETAIL` for retail banking customers



Request JSON body: 
    
    
    {
      "partyTables": [
         "bq://PROJECT_ID.BQ_INPUT_REGISTERED_PARTIES_DATASET_NAME.PARTY_REGISTRATION_TABLE"
      ],
      "mode": "UPDATE_MODE",
      "lineOfBusiness": "LINE_OF_BUSINESS"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "partyTables": [
         "bq://PROJECT_ID.BQ_INPUT_REGISTERED_PARTIES_DATASET_NAME.PARTY_REGISTRATION_TABLE"
      ],
      "mode": "UPDATE_MODE",
      "lineOfBusiness": "LINE_OF_BUSINESS"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID:importRegisteredParties"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "partyTables": [
         "bq://PROJECT_ID.BQ_INPUT_REGISTERED_PARTIES_DATASET_NAME.PARTY_REGISTRATION_TABLE"
      ],
      "mode": "UPDATE_MODE",
      "lineOfBusiness": "LINE_OF_BUSINESS"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID:importRegisteredParties" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": "2023-03-14T15:52:55.358979323Z",
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID",
        "verb": "importRegisteredParties",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

For information on how to get the result of the long-running operation (LRO), see [Manage long-running operations](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/manage-long-running-operations). 

### Registration response

When the LRO completes, the response indicates the number of parties that were added, removed, or updated by the operation.

Response field| Type| Description  
---|---|---  
`partiesAdded`| `integer` | Number of parties added by this operation   
`partiesRemoved`| `integer` | Number of parties removed by this operation   
`partiesTotal`| `integer` | Total number of parties that are registered in this instance, after the update operation was completed   
`partiesUptiered`| `integer` | Total number of commercial parties that are uptiered from small to large   
`partiesDowntiered`| `integer` | Total number of commercial parties that are downtiered from large to small   
`partiesFailedToDowntier`| `integer` | Total number of commercial parties that failed to downtier from large to small   
`partiesFailedToRemove`| `integer` | Number of parties that failed to be removed by this operation   
  
## How to deregister parties

Parties are deregistered per AML AI instance using the same [`projects.locations.instances.importRegisteredParties`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances/importRegisteredParties) method and replacing the existing list of parties. Set the `mode` field to `REPLACE`. This setting deregisters any registered parties (for the provided line of business) that are not part of the provided party registration table.

**Note:** A minimum number of days before a party can be deregistered might apply; see the [Pricing page](https://cloud.google.com/financial-services/anti-money-laundering/pricing). The API response indicates which parties were successfully deregistered.

### Deregistration responses

After the operation completes, check the API response to check if the operation led to the intended result in terms of numbers of parties added or removed, and the total number of registered parties.

The API response also returns the number of parties which couldn't be removed due to constraints; for example, a customer can't be deregistered until a minimum number of days has passed.

## Export registered parties

To export registered parties, use the [`projects.locations.instances.exportRegisteredParties`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances/exportRegisteredParties) method.

(The following information is also available in [Create and manage instances](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-instances).)

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `financialservices.v1instances.exportRegisteredParties`



Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
  * `LOCATION`: the location of the instance; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `INSTANCE_ID`: the user-defined identifier for the instance
  * `BQ_OUTPUT_DATASET_NAME`: a BigQuery dataset in which to export a table that describes the registered parties
  * `PARTY_REGISTRATION_TABLE`: the table to write the registered parties to 
  * `WRITE_DISPOSITION`: the action that occurs if the destination table already exists; use one of the following values: 
    * `WRITE_EMPTY`: Only export data if the BigQuery table is empty. 
    * `WRITE_TRUNCATE`: Erase all existing data in the BigQuery table before writing to the table. 
  * `LINE_OF_BUSINESS`: use `COMMERCIAL` for commercial banking customers (legal and natural entities), or use `RETAIL` for retail banking customers



Request JSON body: 
    
    
    {
      "dataset": {
        "tableUri": "bq://PROJECT_ID.BQ_OUTPUT_DATASET_NAME.PARTY_REGISTRATION_TABLE",
        "writeDisposition": "WRITE_DISPOSITION"
      },
      "lineOfBusiness": "LINE_OF_BUSINESS"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "dataset": {
        "tableUri": "bq://PROJECT_ID.BQ_OUTPUT_DATASET_NAME.PARTY_REGISTRATION_TABLE",
        "writeDisposition": "WRITE_DISPOSITION"
      },
      "lineOfBusiness": "LINE_OF_BUSINESS"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID:exportRegisteredParties"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "dataset": {
        "tableUri": "bq://PROJECT_ID.BQ_OUTPUT_DATASET_NAME.PARTY_REGISTRATION_TABLE",
        "writeDisposition": "WRITE_DISPOSITION"
      },
      "lineOfBusiness": "LINE_OF_BUSINESS"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID:exportRegisteredParties" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": "2023-03-14T15:52:55.358979323Z",
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID",
        "verb": "exportRegisteredParties",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

For information on how to get the result of the long-running operation (LRO), see [Manage long-running operations](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/manage-long-running-operations). 

This method outputs a BigQuery table with the following schema:

Column| Type| Description  
---|---|---  
`party_id`| [`STRING`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#string_type)| Unique identifier of the party in the instance's datasets  
`party_size`| [`STRING`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#string_type) | Specifies the tier for commercial customers (large versus small). This field does not apply to retail customers. 

  * `NULL` for all retail customers
  * `SMALL` for small commercial parties with less than 500 average monthly transactions
  * `LARGE` for large commercial parties with greater than or equal to 500 average monthly transactions

All values are case sensitive.   
`earliest_remove_time`| [`STRING`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#string_type)| The earliest time at which the party can be removed  
`party_with_prediction_intent`| [`STRING`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#string_type)| The indicator that suggests if a party has been predicted on since the registration  
`registration_or_uptier_time`| [`STRING`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#string_type)| The time at which the party was registered or uptiered  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
