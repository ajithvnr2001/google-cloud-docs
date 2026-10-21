---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-datasets/
title: Create and manage AML AI datasets \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:32:46.432601+00:00
---

# Create and manage AML AI datasets  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-datasets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Create and manage AML AI datasets Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you the steps to create and manage AML AI datasets. A dataset is used as an input for the engine configuration, training, backtest, and prediction pipelines. An AML AI dataset contains references to BigQuery tables matching the [AML AI input data model](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model) in a Google Cloud project.

## Prerequisites

  * To get the permissions that you need to create and manage datasets, ask your administrator to grant you the Financial Services Admin (`financialservices.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  * [Create an instance](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-instances#create-instance)
  * Some API methods return a [long-running operation](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/manage-long-running-operations) (LRO). These methods are asynchronous and return an Operation object; for details, see [REST Reference](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest). The operation might not be completed when the method returns a response. For these methods, send the request and then check for the result. In general, all POST, PUT, UPDATE, and DELETE operations are long-running. 




## Create a dataset

To create a dataset, send the create request and then check for the result of the LRO.

### Send the request

To create a dataset, use the [`projects.locations.instances.datasets.create`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.datasets/create) method.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `financialservices.v1datasets.create`



Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
  * `LOCATION`: the location of the instance; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `INSTANCE_ID`: the user-defined identifier for the instance
  * `DATASET_ID`: a user-defined identifier for the AML AI dataset; use only lowercase letters, numbers, dashes, and underscores (for example, `train_jan2018_apr2020`) 
  * `BQ_INPUT_DATASET_NAME`: the BigQuery input dataset name
  * `PARTY_TABLE`: the [Party](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#party) table in the BigQuery input dataset
  * `ACCOUNT_PARTY_LINK_TABLE`: the [AccountPartyLink](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#accountpartylink) table in the BigQuery input dataset
  * `TRANSACTION_TABLE`: the [Transaction](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#transaction) table in the BigQuery input dataset
  * `RISK_CASE_EVENT_TABLE`: the [RiskCaseEvent](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#riskcaseevent) table in the BigQuery input dataset
  * `PARTY_SUPPLEMENTARY_DATA`: the [PartySupplementaryData](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#partysupplementarydata) table in the BigQuery input dataset; this table is optional and can be removed from the request JSON 
  * `DATA_START_DATE`: the start date and time of the data to use in the dataset; use RFC3339 UTC "Zulu" format (for example, `2014-10-02T15:01:23Z`)
  * `DATA_END_DATE`: the end date and time of the data to use in the dataset; use RFC3339 UTC "Zulu" format (for example, `2014-10-02T15:01:23Z`)



Request JSON body: 
    
    
    {
      "tableSpecs": {
        "party": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.PARTY_TABLE",
        "account_party_link": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.ACCOUNT_PARTY_LINK_TABLE",
        "transaction": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.TRANSACTION_TABLE",
        "risk_case_event": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.RISK_CASE_EVENT_TABLE",
        "party_supplementary_data": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.PARTY_SUPPLEMENTARY_DATA"
      },
      "dateRange": {
        "startTime": "DATA_START_DATE",
        "endTime": "DATA_END_DATE"
      },
      "timeZone": {
        "id": "UTC"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "tableSpecs": {
        "party": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.PARTY_TABLE",
        "account_party_link": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.ACCOUNT_PARTY_LINK_TABLE",
        "transaction": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.TRANSACTION_TABLE",
        "risk_case_event": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.RISK_CASE_EVENT_TABLE",
        "party_supplementary_data": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.PARTY_SUPPLEMENTARY_DATA"
      },
      "dateRange": {
        "startTime": "DATA_START_DATE",
        "endTime": "DATA_END_DATE"
      },
      "timeZone": {
        "id": "UTC"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets?dataset_id=DATASET_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "tableSpecs": {
        "party": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.PARTY_TABLE",
        "account_party_link": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.ACCOUNT_PARTY_LINK_TABLE",
        "transaction": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.TRANSACTION_TABLE",
        "risk_case_event": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.RISK_CASE_EVENT_TABLE",
        "party_supplementary_data": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.PARTY_SUPPLEMENTARY_DATA"
      },
      "dateRange": {
        "startTime": "DATA_START_DATE",
        "endTime": "DATA_END_DATE"
      },
      "timeZone": {
        "id": "UTC"
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
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets?dataset_id=DATASET_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets/DATASET_ID",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

Copy the returned `OPERATION_ID` to use in the next section.

### Check for the result

Use the [`projects.locations.operations.get`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.operations/get) method to check if the dataset has been created. If the response contains `"done": false`, repeat the command until the response contains `"done": true`. These operations can take a few minutes to several hours to complete.

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
        "target": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.Dataset",
        "name": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets/DATASET_ID",
        "createTime": CREATE_TIME,
        "updateTime": UPDATE_TIME,
        "tableSpecs": {
          "party": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.PARTY_TABLE",
          "account_party_link": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.ACCOUNT_PARTY_LINK_TABLE",
          "transaction": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.TRANSACTION_TABLE",
          "risk_case_event": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.RISK_CASE_EVENT_TABLE",
          "party_supplementary_data": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.PARTY_SUPPLEMENTARY_DATA"
        },
        "state": "ACTIVE",
        "dateRange": {
          "start_time": "DATA_START_DATE",
          "end_time": "DATA_END_DATE"
        },
        "timeZone": {
          "id": "UTC"
        }
      }
    }
    

## Get a dataset

To get a dataset, use the [`projects.locations.instances.datasets.get`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.datasets/get) method.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `financialservices.v1datasets.get`



Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
  * `LOCATION`: the location of the instance; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `INSTANCE_ID`: the user-defined identifier for the instance
  * `DATASET_ID`: the user-defined identifier for the dataset



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets/DATASET_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets/DATASET_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets/DATASET_ID",
      "createTime": CREATE_TIME,
      "updateTime": UPDATE_TIME,
      "tableSpecs": {
        "party": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.PARTY_TABLE",
        "account_party_link": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.ACCOUNT_PARTY_LINK_TABLE",
        "transaction": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.TRANSACTION_TABLE",
        "risk_case_event": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.RISK_CASE_EVENT_TABLE",
        "party_supplementary_data": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.PARTY_SUPPLEMENTARY_DATA"
      },
      "state": "ACTIVE",
      "dateRange": {
        "start_time": "DATA_START_DATE",
        "end_time": "DATA_END_DATE"
      },
      "timeZone": {
        "id": "UTC"
      }
    }
    

## Update a dataset

To update a dataset, use the [`projects.locations.instances.datasets.patch`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.datasets/patch) method.

The only fields which can be updated are label fields in AML AI. The following example updates the key-value pair [user labels](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.datasets#Dataset.FIELDS.labels) associated with the dataset.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `financialservices.v1datasets.update`



Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
  * `LOCATION`: the location of the instance; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `INSTANCE_ID`: a user-defined identifier for the instance
  * `DATASET_ID`: the user-defined identifier for the dataset
  * `KEY`: The key in a key-value pair used to organize datasets. See [`labels`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.datasets#Dataset.FIELDS.labels) for more information.
  * `VALUE`: The value in a key-value pair used to organize datasets. See [`labels`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.datasets#Dataset.FIELDS.labels) for more information.



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
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets/DATASET_ID?updateMask=labels"

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
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets/DATASET_ID?updateMask=labels" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets/DATASET_ID",
        "verb": "update",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

For more information on how to get the result of the long-running operation (LRO), see Check for the result. 

## List the datasets

To list the datasets for a given instance, use the [`projects.locations.instances.datasets.list`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.datasets/list) method.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `financialservices.v1datasets.list`



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
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "datasets": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets/DATASET_ID",
          "createTime": CREATE_TIME,
          "updateTime": UPDATE_TIME,
          "tableSpecs": {
            "party": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.PARTY_TABLE",
            "account_party_link": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.ACCOUNT_PARTY_LINK_TABLE",
            "transaction": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.TRANSACTION_TABLE",
            "risk_case_event": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.RISK_CASE_EVENT_TABLE",
            "party_supplementary_data": "bq://PROJECT_ID.BQ_INPUT_DATASET_NAME.PARTY_SUPPLEMENTARY_DATA"
          },
          "state": "ACTIVE",
          "dateRange": {
            "start_time": "DATA_START_DATE",
            "end_time": "DATA_END_DATE"
          },
          "timeZone": {
            "id": "UTC"
          }
        }
      ]
    }
    

## Delete a dataset

To delete a dataset, use the [`projects.locations.instances.datasets.delete`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.datasets/delete) method.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `financialservices.v1datasets.delete`



Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
  * `LOCATION`: the location of the instance; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `INSTANCE_ID`: the user-defined identifier for the instance
  * `DATASET_ID`: the user-defined identifier for the dataset



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets/DATASET_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets/DATASET_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets/DATASET_ID",
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
