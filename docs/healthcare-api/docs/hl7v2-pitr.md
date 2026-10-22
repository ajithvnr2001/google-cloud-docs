---
url: https://docs.cloud.google.com/healthcare-api/docs/hl7v2-pitr/
title: Recover HL7v2 messages with point-in-time recovery (PITR) \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:41.245901+00:00
---

# Recover HL7v2 messages with point-in-time recovery (PITR)  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/hl7v2-pitr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Recover HL7v2 messages with point-in-time recovery (PITR) Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use point-in-time recovery (PITR) to recover HL7v2 messages in an HL7v2 store to a state within the last 21 days. You can use PITR to recover from unwanted changes, such as accidentally deleting HL7v2 messages.

## Before you begin

PITR requests are categorized as advanced operation requests and are billed accordingly. Before using PITR, review the pricing for [advanced-operation requests](https://cloud.google.com/healthcare-api/pricing#advanced-ops).

## Recovery workflow

To ensure a production recovery runs as expected, first do a dry run. The dry run outputs one or more files containing the IDs of the HL7v2 messages to recover. Verify the correctness of the output files before running the recovery again in production.

To recover specific HL7v2 messages, or recover HL7v2 messages according to a filtering criteria, specify a filter.

## Do a dry run

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) roles:

**Permissions**

  * `healthcare.hl7V2Stores.rollback`



**Roles**

  * Healthcare HL7v2 Store Administrator (`roles/healthcare.hl7V2StoreAdmin`) 



You can ask your administrator to grant you these Identity and Access Management roles. For instructions on granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) or [Control access to Cloud Healthcare API resources](https://docs.cloud.google.com/healthcare-api/docs/controlling-access#using_cloud_iam_with_datasets). You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

**Note** : If you created a Google Cloud project for this guide, then, as the project creator, you're automatically granted the Owner (`roles/owner`) IAM role, which has the permissions. You don't need to be granted any additional IAM roles. 

Before recovering HL7v2 messages in production, do a dry run.

The following samples show how to do a dry run using the [`hl7V2Stores.rollback`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/rollback) method.

### REST

  1. Recover the HL7v2 messages.

To do a dry run, ensure the [`force`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/rollback#body.request_body.FIELDS.force) field is `false`.

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: the ID of your Google Cloud project
     * `LOCATION`: the dataset location
     * `DATASET_ID`: the HL7v2 store's parent dataset
     * `HL7V2_STORE_ID`: the HL7v2 store ID
     * `RECOVERY_TIMESTAMP`: a recovery point within the last 21 days. Use the [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339) format. Specify the time to the second and include a time zone, for example `2015-02-07T13:28:17.239+02:00` or `2017-01-01T00:00:00Z`.
     * `CLOUD_STORAGE_BUCKET`: the fully qualified URI to a Cloud Storage folder or bucket where output files are written

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    cat > request.json << 'EOF'
    {
      "rollbackTime": "RECOVERY_TIMESTAMP",
      "resultGcsBucket": "gs://CLOUD_STORAGE_BUCKET",
      "force": "false"
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID:rollback"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "rollbackTime": "RECOVERY_TIMESTAMP",
      "resultGcsBucket": "gs://CLOUD_STORAGE_BUCKET",
      "force": "false"
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
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID:rollback" | Select-Object -Expand Content

#### APIs Explorer

Copy the request body and open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/rollback). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

The output is the following. The response contains an identifier for a [long-running operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations) (LRO). Long-running operations are returned when method calls might take additional time to complete. Note the value of `OPERATION_ID`. You need this value in the next step. 

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

  2. Use the [`projects.locations.datasets.operations.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) method to get the status of the long-running operation.

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: the ID of your Google Cloud project
     * `DATASET_ID`: the dataset ID
     * `LOCATION`: the dataset location
     * `OPERATION_ID`: the ID returned from the long-running operation

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

The output is the following. When the response contains `"done": true`, the long-running operation has finished. 

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.hl7v2.Hl7V2Service.RollbackHl7V2Messages",
        "createTime": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "endTime": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "logsUrl": "https://console.cloud.google.com/CLOUD_LOGGING_URL",
        "counter": {
          "success": "SUCCESS_COUNT",
          "failure": "FAILURE_COUNT"
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.hl7v2.RollbackHl7V2MessagesResponse",
        "hl7V2Store": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID"
      }
    }
    




### View dry run output files

Each dry run outputs one or more files containing the IDs and types of the HL7v2 messages to recover. The files are created in a subfolder in the `rollback_messages` folder in the destination Cloud Storage bucket. The subfolder name is the LRO ID returned in the `hl7V2Stores.rollback` response. To view the files and ensure the recovery works as expected, see [View object metadata](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata#view).

The number of files is proportional to the number of recovered HL7v2 messages.

File names use the format `trial-NUMBER-of-TOTAL_NUMBER.txt`, where `NUMBER` is the file number and `TOTAL_NUMBER` is the total number of files.

### Dry run output file schema

The output files from a dry run recovery use the schema shown in the following table:

`MESSAGE_ID` | `TIMESTAMP`  
---|---  
The HL7v2 message ID. | The time when the HL7v2 message was created or updated in the HL7v2 store.  
  
## Recover in production

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) roles:

**Permissions**

  * `healthcare.hl7V2Stores.rollback`



**Roles**

  * Healthcare HL7v2 Store Administrator (`roles/healthcare.hl7V2StoreAdmin`) 



To write the production output files to Cloud Storage, you must grant permissions to the **Cloud Healthcare Service Agent** service account. For instructions, see [Write output files to Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/permissions-healthcare-api-gcp-products#write-hl7v2-gcs).

You can ask your administrator to grant you these Identity and Access Management roles. For instructions on granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) or [Control access to Cloud Healthcare API resources](https://docs.cloud.google.com/healthcare-api/docs/controlling-access#using_cloud_iam_with_datasets). You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

**Note** : If you created a Google Cloud project for this guide, then, as the project creator, you're automatically granted the Owner (`roles/owner`) IAM role, which has the permissions. You don't need to be granted any additional IAM roles. 

Before recovering in production, do a dry run and inspect the dry run output files to ensure the production recovery runs as expected.

The following samples show how to restore HL7v2 messages in production using the [`hl7V2Stores.rollback`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/rollback) method.

### REST

  1. Recover the HL7v2 messages.

Ensure the [`force`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/rollback#body.request_body.FIELDS.force) field is `true`.

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: the ID of your Google Cloud project
     * `LOCATION`: the dataset location
     * `DATASET_ID`: the HL7v2 store's parent dataset
     * `HL7V2_STORE_ID`: the HL7v2 store ID
     * `RECOVERY_TIMESTAMP`: a recovery point within the last 21 days. Use the [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339) format. Specify the time to the second and include a time zone, for example `2015-02-07T13:28:17.239+02:00` or `2017-01-01T00:00:00Z`.
     * `CLOUD_STORAGE_BUCKET`: the fully qualified URI to a Cloud Storage folder or bucket where output files are written

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    cat > request.json << 'EOF'
    {
      "rollbackTime": "RECOVERY_TIMESTAMP",
      "resultGcsBucket": "gs://CLOUD_STORAGE_BUCKET",
      "force": "true"
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID:rollback"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "rollbackTime": "RECOVERY_TIMESTAMP",
      "resultGcsBucket": "gs://CLOUD_STORAGE_BUCKET",
      "force": "true"
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
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID:rollback" | Select-Object -Expand Content

#### APIs Explorer

Copy the request body and open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/rollback). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

The output is the following. The response contains an identifier for a [long-running operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations) (LRO). Long-running operations are returned when method calls might take additional time to complete. Note the value of `OPERATION_ID`. You need this value in the next step. 

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

  2. Use the [`projects.locations.datasets.operations.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) method to get the status of the long-running operation.

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: the ID of your Google Cloud project
     * `DATASET_ID`: the dataset ID
     * `LOCATION`: the dataset location
     * `OPERATION_ID`: the ID returned from the long-running operation

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

The output is the following. When the response contains `"done": true`, the long-running operation has finished. 

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.hl7v2.Hl7V2Service.RollbackHl7V2Messages",
        "createTime": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "endTime": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "logsUrl": "https://console.cloud.google.com/CLOUD_LOGGING_URL",
        "counter": {
          "success": "SUCCESS_COUNT",
          "failure": "FAILURE_COUNT"
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.hl7v2.RollbackHl7V2MessagesResponse",
        "hl7V2Store": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID"
      }
    }
    




### View production recovery output files

A production recovery outputs the following files. The files are created in a subfolder in the `rollback_messages` folder in the destination Cloud Storage bucket. The subfolder name is the LRO ID returned in the `hl7V2Stores.rollback` response. To view the files, see [View object metadata](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata#view).

  * `success-NUMBER-of-TOTAL_NUMBER.txt`: Contains successfully recovered HL7v2 messages.
  * `fail-NUMBER-of-TOTAL_NUMBER.txt`: Contains HL7v2 messages that failed to be recovered. An empty file is generated even if there are no failures.



In the file names, `NUMBER` is the file number, and `TOTAL_NUMBER` is the total number of files.

### Production output file schema

The success and failure files from a production recovery use the following schema. Error files contain an additional `ERROR_MESSAGE` column.

`MESSAGE_ID` | `ERROR_MESSAGE` (Error files only)  
---|---  
The HL7v2 message ID. | Error files only. Describes why the HL7v2 message failed to be recovered.  
  
## Use filters to restore an HL7v2 store to a previous state

If an HL7v2 store was modified by one or more [long-running operations (LROs)](https://docs.cloud.google.com/healthcare-api/docs/how-tos/long-running-operations), you can specify the LRO IDs in a filter to restore the HL7v2 store to its previous state. For example, you can restore an HL7v2 store to its previous state before an import operation imported HL7v2 messages.

You specify the LRO IDs in the [`RollbackHL7MessagesFilteringFields`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/rollback#RollbackHL7MessagesFilteringFields) object when sending an `hl7V2Stores.rollback` request.

See [Listing LROs](https://docs.cloud.google.com/healthcare-api/docs/how-tos/long-running-operations#listing_lros) for information on listing and viewing LRO IDs in a Cloud Healthcare API dataset.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
