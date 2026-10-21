---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-backtest-results/
title: Create and manage backtest results \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:32:47.975936+00:00
---

# Create and manage backtest results  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-backtest-results/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Create and manage backtest results Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to create and manage AML AI backtest prediction results. Backtest prediction uses a trained model on existing historical data. For these months, the dataset must contain a party with suspicious activity or investigation start dates leading to an `AML_EXIT` event, for more information on how AML AI labels various parties, see [lifecycle of a risk case](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/lifecycle-risk-case).

The same dataset can be used for training and backtest as long as the training end date is before the backtest dates.

## Before you begin

  * To get the permissions that you need to create and manage backtest results, ask your administrator to grant you the Financial Services Admin (`financialservices.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  * [Create an instance](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-instances#create-instance)
  * [Create a model](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-models#create-model)
  * [Create a dataset](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-datasets#create-dataset)



## Create backtest results

Some API methods return a [long-running operation](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/manage-long-running-operations) (LRO). These methods are asynchronous and return an Operation object; for details, see [REST Reference](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest). The operation might not be completed when the method returns a response. For these methods, send the request and then check for the result. In general, all POST, PUT, UPDATE, and DELETE operations are long-running. 

### Send the request

To create backtest results, use the [`projects.locations.instances.backtestResults.create`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.backtestResults/create) method.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `financialservices.v1backtests.create`



Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
  * `LOCATION`: the location of the instance; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `INSTANCE_ID`: a user-defined identifier for the instance
  * `BACKTEST_RESULTS_ID`: a user-defined identifier for the backtest results
  * `MODEL_ID`: a user-defined identifier for the model
  * `BACKTEST_DATASET_ID`: the user-defined identifier for the [dataset](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-datasets) used for the backtest; tables should not have the training label columns
  * `BACKTEST_END_DATE`: The latest time from which data is used to generate features for backtests. This date should be the same or earlier than the end time of the datasets. Use RFC3339 UTC "Zulu" format (for example, `2014-10-02T15:01:23Z`).
  * `PARTY_INVESTIGATIONS_PER_PERIOD_HINT`: A hint on the number of parties from this data that will be investigated per period (monthly). This is used to ensure the model is evaluated at relevant investigation volumes. For example, when trying AML AI for the first time, we recommend setting this to the number of parties investigated in an average month, based on alerts from your existing automated alerting system. Either this field or `partyCountExceedingThresholdPerPeriodHint` should be provided. If both are omitted, or both are provided, it will throw an error.
  * `PARTY_COUNT_EXCEEDING_THRESHOLD_PER_PERIOD_HINT`: A hint on the number of parties from this data that should score above the threshold for alerting per period (monthly). This is used to ensure the model is evaluated at a relevant alerting volume and can be used for a quick comparison of backtesting for multiple candidate models. Either this field or `partyInvestigationsPerPeriodHint` should be provided. If both are omitted, or both are provided, it will throw an error.



Request JSON body: 
    
    
    {
        "model": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/models/MODEL_ID",
        "dataset": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets/BACKTEST_DATASET_ID",
        "endTime": "BACKTEST_END_DATE",
        "backtestPeriods": 5,
        "performanceTarget": {
          "partyInvestigationsPerPeriodHint": "PARTY_INVESTIGATIONS_PER_PERIOD_HINT"
        }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
        "model": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/models/MODEL_ID",
        "dataset": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets/BACKTEST_DATASET_ID",
        "endTime": "BACKTEST_END_DATE",
        "backtestPeriods": 5,
        "performanceTarget": {
          "partyInvestigationsPerPeriodHint": "PARTY_INVESTIGATIONS_PER_PERIOD_HINT"
        }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/backtestResults?backtest_result_id=BACKTEST_RESULTS_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
        "model": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/models/MODEL_ID",
        "dataset": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets/BACKTEST_DATASET_ID",
        "endTime": "BACKTEST_END_DATE",
        "backtestPeriods": 5,
        "performanceTarget": {
          "partyInvestigationsPerPeriodHint": "PARTY_INVESTIGATIONS_PER_PERIOD_HINT"
        }
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
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/backtestResults?backtest_result_id=BACKTEST_RESULTS_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/backtestResults/BACKTEST_RESULTS_ID",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

### Check for the result

To check if backtest results have been created, use the [`projects.locations.operations.get`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.operations/get) method. If the response contains `"done": false`, repeat the command until the response contains `"done": true`. These operations can take a few minutes to several hours to complete.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `financialservices.operations.get`



Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
  * `LOCATION`: the location of the instance; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `OPERATION_ID`: the identifier for the operation



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": "2023-03-14T15:52:55.358979323Z",
        "endTime": "2023-03-14T16:52:55.358979323Z",
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/backtestResults/BACKTEST_RESULTS_ID",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/dataresidency.monitoring.DataResidencyAugmentedView",
        "tpIds": [
          "i608e8cf4abb2a7d9-tp"
        ]
      }
    }
    

## Export metadata

To export metadata from backtest results, use the [`projects.locations.instances.backtestResults.exportMetadata`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.backtestResults/exportMetadata) method.

For more information, see [Exported metadata in the AML output data model](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-output-data-model#exported-metadata).

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `financialservices.v1backtests.exportMetadata`



Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
  * `LOCATION`: the location of the instance; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `INSTANCE_ID`: the user-defined identifier for the instance
  * `BACKTEST_RESULTS_ID`: a user-defined identifier for the backtest results
  * `BQ_OUTPUT_DATASET_NAME`: a BigQuery dataset in which to export a table that describes the structured metadata of the backtest results
  * `STRUCTURED_METADATA_TABLE`: the table to write the structured metadata to 
  * `WRITE_DISPOSITION`: the action that occurs if the destination table already exists; use one of the following values: 
    * `WRITE_EMPTY`: Only export data if the BigQuery table is empty. 
    * `WRITE_TRUNCATE`: Erase all existing data in the BigQuery table before writing to the table. 



Request JSON body: 
    
    
    {
      "structuredMetadataDestination": {
        "tableUri": "bq://PROJECT_ID.BQ_OUTPUT_DATASET_NAME.STRUCTURED_METADATA_TABLE",
        "writeDisposition": "WRITE_DISPOSITION"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "structuredMetadataDestination": {
        "tableUri": "bq://PROJECT_ID.BQ_OUTPUT_DATASET_NAME.STRUCTURED_METADATA_TABLE",
        "writeDisposition": "WRITE_DISPOSITION"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/backtestResults/BACKTEST_RESULTS_ID:exportMetadata"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "structuredMetadataDestination": {
        "tableUri": "bq://PROJECT_ID.BQ_OUTPUT_DATASET_NAME.STRUCTURED_METADATA_TABLE",
        "writeDisposition": "WRITE_DISPOSITION"
      }
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
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/backtestResults/BACKTEST_RESULTS_ID:exportMetadata" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/backtestResults/BACKTEST_RESULTS_ID",
        "verb": "exportMetadata",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

For more information on how to get the result of the long-running operation (LRO), see Check for the result. 

## Get backtest results

To get backtest results, use the [`projects.locations.instances.backtestResults.get`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.backtestResults/get) method.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `financialservices.v1backtests.get`



Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
  * `LOCATION`: the location of the instance; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `INSTANCE_ID`: the user-defined identifier for the instance
  * `BACKTEST_RESULTS_ID`: the user-defined identifier for the backtest results



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/backtestResults/BACKTEST_RESULTS_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/backtestResults/BACKTEST_RESULTS_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
        "name": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/backtestResults/BACKTEST_RESULTS_ID",
        "createTime": CREATE_TIME,
        "updateTime": UPDATE_TIME,
        "state": "ACTIVE",
        "dataset": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets/BACKTEST_DATASET_ID",
        "model": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/models/MODEL_ID",
        "endTime": "BACKTEST_END_DATE",
        "performanceTarget": {
          "partyInvestigationsPerPeriodHint": "PARTY_INVESTIGATIONS_PER_PERIOD_HINT"
        },
        "lineOfBusiness": "RETAIL"
    }
    

## Update backtest results

To update backtest results, use the [`projects.locations.instances.backtestResults.patch`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.backtestResults/patch) method.

Only the `labels` field in backtest results can be updated. The following example updates the key-value pair [user labels](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.backtestResults#BacktestResult.FIELDS.labels) associated with the backtest results.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `financialservices.v1backtests.update`



Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
  * `LOCATION`: the location of the instance; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `INSTANCE_ID`: the user-defined identifier for the instance
  * `BACKTEST_RESULTS_ID`: the user-defined identifier for the backtest results
  * `KEY`: The key in a key-value pair used to organize backtest results. See [`labels`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.backtestResults#BacktestResult.FIELDS.labels) for more information.
  * `VALUE`: The value in a key-value pair used to organize backtest results. See [`labels`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.backtestResults#BacktestResult.FIELDS.labels) for more information.



Request JSON body: 
    
    
    {
      "labels": {
        "KEY": "VALUE"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "labels": {
        "KEY": "VALUE"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/backtestResults/BACKTEST_RESULTS_ID?updateMask=labels"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "labels": {
        "KEY": "VALUE"
      }
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
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/backtestResults/BACKTEST_RESULTS_ID?updateMask=labels" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/backtestResults/BACKTEST_RESULTS_ID",
        "verb": "update",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

For more information on how to get the result of the long-running operation (LRO), see Check for the result. 

## List the backtest results

To list the backtest results for a given instance, use the [`projects.locations.instances.backtestResults.list`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.backtestResults/list) method.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `financialservices.v1backtests.list`



Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
  * `LOCATION`: the location of the instance; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `INSTANCE_ID`: the user-defined identifier for the instance



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/backtestResults"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/backtestResults" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "backtestResults": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/backtestResults/BACKTEST_RESULTS_ID",
          "createTime": CREATE_TIME,
          "updateTime": UPDATE_TIME,
          "state": "ACTIVE",
          "dataset": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets/BACKTEST_DATASET_ID",
          "model": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/models/MODEL_ID",
          "endTime": "BACKTEST_END_DATE",
          "performanceTarget": {
            "partyInvestigationsPerPeriodHint": "PARTY_INVESTIGATIONS_PER_PERIOD_HINT"
          },
          "lineOfBusiness": "RETAIL"
        }
      ]
    }
    

## Delete backtest results

To delete backtest results, use the [`projects.locations.instances.backtestResults.delete`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.backtestResults/delete) method.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `financialservices.v1backtests.delete`



Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
  * `LOCATION`: the location of the instance; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `INSTANCE_ID`: the user-defined identifier for the instance
  * `BACKTEST_RESULTS_ID`: the user-defined identifier for the backtest results



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/backtestResults/BACKTEST_RESULTS_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/backtestResults/BACKTEST_RESULTS_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/backtestResults/BACKTEST_RESULTS_ID",
        "verb": "delete",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

For more information on how to get the result of the long-running operation (LRO), see Check for the result. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
