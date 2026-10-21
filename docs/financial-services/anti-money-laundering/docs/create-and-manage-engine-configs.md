---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-engine-configs/
title: Create and manage engine configs \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:07.138773+00:00
---

# Create and manage engine configs  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-engine-configs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Create and manage engine configs Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to create and manage AML AI engine configs, which are configurations for training models. An engine config might include information that is tuned for specific datasets.

For more information on what an engine config is, see [Configure an engine](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/configure-engine).

**Note:** If you're using this as a set up guide, you only need to create the engine config and export the associated metadata at this point. The other engine config methods are provided for completeness.

## Before you begin

  * To get the permissions that you need to create and manage engine configs, ask your administrator to grant you the Financial Services Admin (`financialservices.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  * [Create an instance](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-instances#create-instance)
  * [Get an engine version](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/manage-engine-versions#list-engine-versions)
  * [Create a dataset](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-datasets#create-dataset)



## Create an engine config that includes automatic tuning

Some API methods return a [long-running operation](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/manage-long-running-operations) (LRO). These methods are asynchronous and return an Operation object; for details, see [REST Reference](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest). The operation might not be completed when the method returns a response. For these methods, send the request and then check for the result. In general, all POST, PUT, UPDATE, and DELETE operations are long-running. 

### Send the request

To create an engine config, use the [`projects.locations.instances.engineConfigs.create`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs/create) method.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `financialservices.v1engineconfigs.create`



Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
  * `LOCATION`: the location of the instance; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `INSTANCE_ID`: the user-defined identifier for the instance
  * `ENGINE_CONFIG_ID`: a user-defined identifier for the engine config
  * `ENGINE_VERSION_ID`: the [engine version](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/manage-engine-versions), which is used for the initial settings of the engine config
  * `DATASET_ID`: the user-defined identifier for the primary dataset used for tuning a model
  * `TUNING_END_DATE`: The latest time from which data is used to generate features for training. This date should be the same or earlier than the end time of the datasets. Use RFC3339 UTC "Zulu" format (for example, `2014-10-02T15:01:23Z`).
  * `PARTY_INVESTIGATIONS_PER_PERIOD_HINT`: A number that gives the tuner a hint on the number of parties from this data that will be investigated per period (monthly). This is used to control how the model is evaluated. For example, when trying AML AI for the first time, we recommend setting this to the number of parties investigated in an average month, based on alerts from your existing automated alerting system.



Request JSON body: 
    
    
    {
      "engineVersion": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineVersions/ENGINE_VERSION_ID",
      "tuning": {
        "primaryDataset": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets/DATASET_ID",
        "endTime": "TUNING_END_DATE"
      },
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
      "engineVersion": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineVersions/ENGINE_VERSION_ID",
      "tuning": {
        "primaryDataset": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets/DATASET_ID",
        "endTime": "TUNING_END_DATE"
      },
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
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs?engine_config_id=ENGINE_CONFIG_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "engineVersion": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineVersions/ENGINE_VERSION_ID",
      "tuning": {
        "primaryDataset": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets/DATASET_ID",
        "endTime": "TUNING_END_DATE"
      },
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
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs?engine_config_id=ENGINE_CONFIG_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs/ENGINE_CONFIG_ID",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

### Check for the result

Use the [`projects.locations.operations.get`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.operations/get) method to check if the engine config has been created. If the response contains `"done": false`, repeat the command until the response contains `"done": true`. These operations can take a few minutes to several hours to complete.

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
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs/ENGINE_CONFIG_ID",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.EngineConfig",
        "name": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs/ENGINE_CONFIG_ID",
        "createTime": CREATE_TIME,
        "updateTime": UPDATE_TIME,
        "state": "ACTIVE",
        "engineVersion": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineVersions/ENGINE_VERSION_ID",
        "tuning": {
          "primaryDataset": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets/DATASET_ID",
          "endTime": "TUNING_END_DATE",
        },
        "performanceTarget": {
          "partyInvestigationsPerPeriodHint": "PARTY_INVESTIGATIONS_PER_PERIOD_HINT"
        },
        "lineOfBusiness": "RETAIL",
        "billingUuid": "BILLING_UUID"
      }
    }
    

## Export metadata

To export metadata from an engine config, use the [`projects.locations.instances.engineConfigs.exportMetadata`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs/exportMetadata) method.

For more information, see [Exported metadata in the AML output data model](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-output-data-model#exported-metadata).

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `financialservices.v1engineconfigs.exportMetadata`



Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
  * `LOCATION`: the location of the instance; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `INSTANCE_ID`: the user-defined identifier for the instance
  * `ENGINE_CONFIG_ID`: the user-defined identifier for the engine config
  * `BQ_OUTPUT_DATASET_NAME`: a BigQuery dataset in which to export a table that describes the structured metadata of the engine config
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
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs/ENGINE_CONFIG_ID:exportMetadata"

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
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs/ENGINE_CONFIG_ID:exportMetadata" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs/ENGINE_CONFIG_ID",
        "verb": "exportMetadata",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

For more information on how to get the result of the long-running operation (LRO), see Check for the result. 

## Create an engine config that inherits hyperparameters

To avoid re-tuning each time you adopt a new model engine version, you can choose to inherit hyperparameters from an existing engine config. For more information, see [Configure an engine](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/configure-engine).

**Note:** This feature is only available with an engine version from tuning version v004 and minor versions aml-retail.default.v004.000.202312-001, aml-commercial.default.v004.000.202312-001, aml-retail.default.v003.000.202312-000, aml-commercial.default.v003.000.202312-000 and later, also with any major engine versions higher than v004.000. Any engine config, including those with a lower version than previously noted, can be used as a source.

To create an engine config, use the [`projects.locations.instances.engineConfigs.create`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs/create) method.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `financialservices.v1engineconfigs.create`



Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
  * `LOCATION`: the location of the instance; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `INSTANCE_ID`: the user-defined identifier for the instance
  * `ENGINE_CONFIG_ID`: a user-defined identifier for the engine config
  * `ENGINE_VERSION_ID`: the [engine version](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/manage-engine-versions), which is used for the initial settings of the engine config; the line of business for the engine version must match the line of business in the source engine config you are inheriting from
  * `SOURCE_ENGINE_CONFIG_ID`: the user-defined identifier for the source engine config; the outputs and hyperparameters are inherited from this source engine config



Request JSON body: 
    
    
    {
      "engineVersion": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineVersions/ENGINE_VERSION_ID",
      "hyperparameterSourceType": "INHERITED",
      "hyperparameterSource": {
        "sourceEngineConfig": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs/SOURCE_ENGINE_CONFIG_ID"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "engineVersion": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineVersions/ENGINE_VERSION_ID",
      "hyperparameterSourceType": "INHERITED",
      "hyperparameterSource": {
        "sourceEngineConfig": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs/SOURCE_ENGINE_CONFIG_ID"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs?engine_config_id=ENGINE_CONFIG_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "engineVersion": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineVersions/ENGINE_VERSION_ID",
      "hyperparameterSourceType": "INHERITED",
      "hyperparameterSource": {
        "sourceEngineConfig": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs/SOURCE_ENGINE_CONFIG_ID"
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
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs?engine_config_id=ENGINE_CONFIG_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs/ENGINE_CONFIG_ID",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

For more information on how to get the result of the long-running operation (LRO), see Check for the result. 

## Get an engine config

To get an engine config, use the [`projects.locations.instances.engineConfigs.get`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs/get) method.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `financialservices.v1engineconfigs.get`



Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
  * `LOCATION`: the location of the instance; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `INSTANCE_ID`: the user-defined identifier for the instance
  * `ENGINE_CONFIG_ID`: the user-defined identifier for the engine config



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs/ENGINE_CONFIG_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs/ENGINE_CONFIG_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs/ENGINE_CONFIG_ID",
      "createTime": CREATE_TIME,
      "updateTime": UPDATE_TIME,
      "state": "ACTIVE",
      "engineVersion": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineVersions/ENGINE_VERSION_ID",
      "tuning": {
        "primaryDataset": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets/DATASET_ID",
        "endTime": "TUNING_END_DATE",
      },
      "performanceTarget": {
        "partyInvestigationsPerPeriodHint": "PARTY_INVESTIGATIONS_PER_PERIOD_HINT"
      },
      "lineOfBusiness": "RETAIL"
    }
    

## Update an engine config

To update an engine config, use the [`projects.locations.instances.engineConfigs.patch`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs/patch) method.

Only the label field in an engine config can be updated. The following example updates these key-value pair [user labels](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs#EngineConfig.FIELDS.labels) associated with the engine config.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `financialservices.v1engineconfigs.update`



Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
  * `LOCATION`: the location of the instance; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `INSTANCE_ID`: the user-defined identifier for the instance
  * `ENGINE_CONFIG_ID`: the user-defined identifier for the engine config
  * `KEY`: The key in a key-value pair used to organize engine configs. See [`labels`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs#EngineConfig.FIELDS.labels) for more information.
  * `VALUE`: The value in a key-value pair used to organize engine configs. See [`labels`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs#EngineConfig.FIELDS.labels) for more information.



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
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs/ENGINE_CONFIG_ID?updateMask=labels"

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
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs/ENGINE_CONFIG_ID?updateMask=labels" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs/ENGINE_CONFIG_ID",
        "verb": "update",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

For more information on how to get the result of the long-running operation (LRO), see Check for the result. 

## List the engine configs

To list the engine configs for a given location, use the [`projects.locations.instances.engineConfigs.list`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs/list) method.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `financialservices.v1engineconfigs.list`



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
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "engineConfigs": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs/ENGINE_CONFIG_ID",
          "createTime": CREATE_TIME,
          "updateTime": UPDATE_TIME,
          "state": "ACTIVE",
          "engineVersion": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineVersions/ENGINE_VERSION_ID",
          "tuning": {
            "primaryDataset": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets/DATASET_ID",
            "endTime": "TUNING_END_DATE",
          },
          "performanceTarget": {
            "partyInvestigationsPerPeriodHint": "PARTY_INVESTIGATIONS_PER_PERIOD_HINT"
          },
          "lineOfBusiness": "RETAIL"
        },
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs/my-other-engine-config",
          "createTime": CREATE_TIME,
          "updateTime": UPDATE_TIME,
          "state": "ACTIVE",
          "engineVersion": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineVersions/ENGINE_VERSION_ID",
          "tuning": {
            "primaryDataset": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/datasets/DATASET_ID",
            "endTime": "TUNING_END_DATE",
          },
          "performanceTarget": {
            "partyInvestigationsPerPeriodHint": "PARTY_INVESTIGATIONS_PER_PERIOD_HINT"
          },
          "lineOfBusiness": "RETAIL"
        }
      ]
    }
    

## Delete an engine config

To delete an engine config, use the [`projects.locations.instances.engineConfigs.delete`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs/delete) method.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `financialservices.v1engineconfigs.delete`



Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
  * `LOCATION`: the location of the instance; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `INSTANCE_ID`: the user-defined identifier for the instance
  * `ENGINE_CONFIG_ID`: the user-defined identifier for the engine config



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs/ENGINE_CONFIG_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs/ENGINE_CONFIG_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs/ENGINE_CONFIG_ID",
        "verb": "delete",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

For more information on how to get the result of the long-running operation (LRO), see Check for the result. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
